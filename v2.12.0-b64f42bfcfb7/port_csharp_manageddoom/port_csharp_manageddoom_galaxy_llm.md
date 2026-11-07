# ARCHITECTURAL_BRIEF: port_csharp_manageddoom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/sinshu/managed-doom.git` |
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
- **Scope:** 245 analyzed artifact(s), 41620 LOC.
- **Load-bearing artifact:** `ManagedDoom/src/Doom/Math/Fixed.cs` -- 26 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `README.md` -- pulls in 16 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `ManagedDoom/src/Video/ThreeDRenderer.cs` at magnitude 2147.54 (structural weight, not risk).
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
| Total Artifacts | 350 |
| Analyzed Artifacts (Scanned) | 245 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 105 |
| Total LOC | 41620 |
| Volatility Index | 0.016 |
| % Scanned of codebase = | 70.0% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5891 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1179 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2977 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 25 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 243 | 41614 | 99.2% |
| MARKDOWN | 1 | 0 | 0.4% |
| BATCH | 1 | 6 | 0.4% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | bom | 243 |
| utf-8 | utf-8 | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 38%, Large Core Modules (3) 22%, State Mutators Files 21%, Many-Argument Workhorses Files 7%, Compute Cores Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 244 | 99.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 105*

**Composition by Extension & Reason:**
- `.lmp`: 48x Excluded (Unsupported Extension: '.lmp')
- `.wad`: 35x Excluded (Unsupported Extension: '.wad')
- `.txt`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.csproj`: 2x Excluded (Unsupported Extension: '.csproj')
- `.cs`: 1x Excluded (Embedded Array/Matrix Payload: 8705 commas in 999 LOC), 1x Excluded (Embedded Array/Matrix Payload: 16385 commas in 2086 LOC)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.slnx`: 1x Excluded (Unsupported Extension: '.slnx')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 95.9 | 23.2 | 14.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 79.8 | 40.6 | 53.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 28.0 | 16.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 17.6 | 5.5 | 5.4 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.2 | 0.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 58.0 | 90.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 8.1 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.5 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 67.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 602 | 50 | 6 | `ManagedDoom/src/Doom/Game/SaveAndLoad.cs` |
| cleanup | 43 | 17 | 0 | `ManagedDoom/src/Silk/SilkDoom.cs` |
| guards | 2394 | 165 | 23 | `ManagedDoom/src/Doom/Info/DoomInfo.Strings.cs` |
| danger | 53 | 33 | 1 | `ManagedDoom/src/Doom/Wad/Wad.cs` |
| concurrency | 35 | 4 | 0 | `ManagedDoom/src/Silk/SilkMusic.cs` |
| connectivity | 2305 | 243 | 21 | `ManagedDoom/src/Doom/Info/DoomInfo.Strings.cs` |
| io | 26 | 11 | 0 | `ManagedDoom/src/ConfigUtilities.cs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 6 | 4 | 0 | `ManagedDoom/src/Silk/SilkDoom.Run.cs` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 521 | 37 | 4 | `ManagedDoom/src/Video/ThreeDRenderer.cs` |
| tests | 996 | 28 | 10 | `ManagedDoomTest/src/UnitTests/NodeTest.cs` |
| docs | 457 | 19 | 0 | `ManagedDoom/src/Doom/World/ThingMovement.cs` |
| debt | 71 | 25 | 1 | `ManagedDoom/src/Doom/DeHackEd.cs` |
| mutation | 12208 | 195 | 140 | `ManagedDoom/src/Video/ThreeDRenderer.cs` |
| dead_code | 637 | 147 | 6 | `ManagedDoom/src/Doom/Info/DoomInfo.MobjActions.cs` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 434 | 43 | 2 | `ManagedDoomTest/src/UnitTests/GeometryTest.cs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.8333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ManagedDoom/src/ConfigUtilities.cs` (Hits: 8)
- `ManagedDoom/src/Doom/Wad/Wad.cs` (Hits: 4)
- `ManagedDoom/src/Doom/DeHackEd.cs` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Fixed.cs** (`ManagedDoom/src/Doom/Math/Fixed.cs`) — 26 inbound connections
2. **World.cs** (`ManagedDoom/src/Doom/World/World.cs`) — 18 inbound connections
3. **GameContent.cs** (`ManagedDoom/src/Doom/Game/GameContent.cs`) — 14 inbound connections
4. **Mobj.cs** (`ManagedDoom/src/Doom/World/Mobj.cs`) — 14 inbound connections
5. **Geometry.cs** (`ManagedDoom/src/Doom/Math/Geometry.cs`) — 13 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`README.md`) — 16 outbound dependencies
2. **SilkDoom.cs** (`ManagedDoom/src/Silk/SilkDoom.cs`) — 9 outbound dependencies
3. **SilkVideo.cs** (`ManagedDoom/src/Silk/SilkVideo.cs`) — 8 outbound dependencies
4. **DeHackEd.cs** (`ManagedDoom/src/Doom/DeHackEd.cs`) — 6 outbound dependencies
5. **SilkMusic.cs** (`ManagedDoom/src/Silk/SilkMusic.cs`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `UseSpecialLine` **(Many-Argument Workhorses)** (@ `ManagedDoom/src/Doom/World/MapInteraction.cs`) -> Impact: **370.9** | LOC: 458
  * *Intent:* /// <summary> /// Called when a thing uses a special line. /// Only the front sides of lines are usable. /// </summary>
- `CrossSpecialLine` **(Many-Argument Workhorses)** (@ `ManagedDoom/src/Doom/World/MapInteraction.cs`) -> Impact: **358.6** | LOC: 452
  * *Intent:* //////////////////////////////////////////////////////////// // Line crossing //////////////////////////////////////////////////////////// /// <summar...
- `TouchSpecialThing` **(Many-Argument Workhorses)** (@ `ManagedDoom/src/Doom/World/ItemPickup.cs`) -> Impact: **246.2** | LOC: 421
  * *Intent:* /// <summary> /// Check for item pickup. /// </summary>
- `DrawPassWallRange` **(Many-Argument Workhorses)** (@ `ManagedDoom/src/Video/ThreeDRenderer.cs`) -> Impact: **220.5** | LOC: 491
- `ToString` **(Compute Cores)** (@ `ManagedDoom/src/UserInput/DoomKeyEx.cs`) -> Impact: **157.6** | LOC: 210
- `Parse` **(Compute Cores)** (@ `ManagedDoom/src/UserInput/DoomKeyEx.cs`) -> Impact: **157.6** | LOC: 210
- `SilkToDoom` **(Compute Cores)** (@ `ManagedDoom/src/Silk/SilkUserInput.cs`) -> Impact: **150.6** | LOC: 128
- `DoomToSilk` **(Compute Cores)** (@ `ManagedDoom/src/Silk/SilkUserInput.cs`) -> Impact: **145.4** | LOC: 108
- `GetChar` **(Compute Cores)** (@ `ManagedDoom/src/UserInput/DoomKeyEx.cs`) -> Impact: **97.0** | LOC: 130
- `DoLocalDoor` **(Many-Argument Workhorses)** (@ `ManagedDoom/src/Doom/World/SectorAction.cs`) -> Impact: **96.3** | LOC: 160
  * *Intent:* /// <summary> /// Open a door manually, no tag value. /// </summary>

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `ManagedDoom/src/Doom/World` | 60 | 9629.66 | 22.5% | 19.55% |
| `ManagedDoom/src/Video` | 12 | 3969.9 | 40.74% | 33.87% |
| `ManagedDoom/src/Doom/Game` | 16 | 1848.18 | 20.56% | 14.71% |
| `ManagedDoom/src/Silk` | 8 | 1800.72 | 61.59% | 24.88% |
| `ManagedDoomTest/src/CompatibilityTests` | 11 | 1559.68 | 50.27% | 59.42% |
| `ManagedDoom/src/Doom/Intermission` | 9 | 1353.4 | 24.43% | 13.45% |
| `ManagedDoom/src/Doom/Info` | 16 | 854.36 | 0.0% | 12.5% |
| `ManagedDoom/src/Doom` | 3 | 846.56 | 41.18% | 10.69% |
| `ManagedDoom/src/Doom/Map` | 16 | 832.78 | 17.88% | 26.89% |
| `ManagedDoom/src/Doom/Graphics` | 20 | 807.48 | 19.74% | 16.9% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ManagedDoom/src/Doom/Info/DoomInfo.MobjActions.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Info/DoomInfo.PlayerActions.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Math/Angle.cs` -> **99.9994%** Exposure
- `ManagedDoom/src/Doom/Math/Fixed.cs` -> **99.9988%** Exposure
- `ManagedDoom/src/Audio/ISound.cs` -> **99.9925%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ManagedDoom/src/Doom/Common/DoomDebug.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Common/DoomInterop.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Common/DoomString.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Doom.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Game/Demo.cs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ManagedDoom/src/Doom/Info/DoomInfo.MobjActions.cs` -> **52** Orphaned Functions | **0** Duplicates
- `ManagedDoom/src/Doom/World/MonsterBehavior.cs` -> **41** Orphaned Functions | **0** Duplicates
- `ManagedDoom/src/Doom/Math/Fixed.cs` -> **30** Orphaned Functions | **0** Duplicates
- `ManagedDoomTest/src/UnitTests/GeometryTest.cs` -> **23** Orphaned Functions | **0** Duplicates
- `ManagedDoom/src/Doom/Info/DoomInfo.PlayerActions.cs` -> **22** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `512` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ManagedDoom/src/Video/ThreeDRenderer.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.235)
- **Top Global Matches:** file_cluster_4: 6.235, file_cluster_6: 8.514, file_cluster_16: 12.606
- **Magnitude:** 2147.54 | **LOC:** 3058 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 2.616; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.1%), Guard Balance (formerly Safety Score) (74.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DrawPassWallRange` **(Many-Argument Workhorses)** (Impact: 220.5)
  * `DrawSprite` **(Compute Cores)** (Impact: 70.2)
  * `DrawSolidWallRange` **(Many-Argument Workhorses)** (Impact: 56.0)
  * `DrawPlayerSprite` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `ProjectSprite` **(Many-Argument Workhorses)** (Impact: 35.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 349 instances
* *State Mutation (weighted view):* 1224
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 444`, `args: 54`, `func_start: 54`, `class_start: 6`
* *Risk/State:* `state_mutation: 526`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 38`, `import: 2`
* *Defense:* `doc: 24`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.000767 | `Ripple Effect (Closeness):` 0.004098
  * `Imports (Out-Degree: 7):` System, System.Collections.Generic
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/World/SectorAction.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.352)
- **Top Global Matches:** file_cluster_8: 7.352, file_cluster_6: 8.937, file_cluster_4: 17.418
- **Magnitude:** 1645.6 | **LOC:** 1774 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **1**; blast radius 6.675; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.6%), Complexity Load (formerly Cognitive Load) (62.0%)
- **Documentation Coverage:** 77.0492% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DoLocalDoor` **(Many-Argument Workhorses)** (Impact: 96.3)
    * *Intent:* /// <summary> /// Open a door manually, no tag value. /// </summary>
  * `MovePlane` **(Many-Argument Workhorses)** (Impact: 94.6)
    * *Intent:* /// <summary> /// Move a plane (floor or ceiling) and check for crushing. /// </summary>
  * `DoFloor` **(Many-Argument Workhorses)** (Impact: 88.4)
  * `DoPlatform` **(Many-Argument Workhorses)** (Impact: 53.4)
  * `DoCeiling` **(Compute Cores)** (Impact: 43.8)
    * *Intent:* //////////////////////////////////////////////////////////// // Ceiling ////////////////////////////...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 270 instances
* *State Mutation (weighted view):* 856
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 197`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `state_mutation: 316`, `unreferenced_by_name: 19`
* *Architecture:* `api: 28`, `import: 1`
* *Defense:* `safety: 1`, `doc: 20`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.675
  * `Choke Point (Betweenness):` 0.003134 | `Ripple Effect (Closeness):` 0.039344
  * `Imports (Out-Degree: 15):` System
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/World/MonsterBehavior.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.335)
- **Top Global Matches:** file_cluster_4: 5.335, file_cluster_15: 10.076, file_cluster_16: 10.297
- **Magnitude:** 1024.06 | **LOC:** 2015 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 3.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.5%), Complexity Load (formerly Cognitive Load) (62.3%)
- **Documentation Coverage:** 90.2655% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BossDeath` **(Compute Cores)** (Impact: 80.8)
  * `NewChaseDir` **(Compute Cores)** (Impact: 54.0)
  * `SpawnFly` **(Compute Cores)** (Impact: 38.2)
  * `Chase` **(Compute Cores)** (Impact: 37.3)
  * `Look` **(Compute Cores)** (Impact: 30.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 110 instances
* *State Mutation (weighted view):* 386
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 224`, `args: 62`, `func_start: 62`, `class_start: 1`
* *Risk/State:* `state_mutation: 166`, `unreferenced_by_name: 41`
* *Architecture:* `api: 52`, `import: 1`
* *Defense:* `safety: 4`, `doc: 20`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.015
  * `Choke Point (Betweenness):` 0.000391 | `Ripple Effect (Closeness):` 0.043716
  * `Imports (Out-Degree: 12):` System
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/World/MapInteraction.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.314)
- **Top Global Matches:** file_cluster_8: 6.314, file_cluster_6: 12.77, file_cluster_4: 21.328
- **Magnitude:** 916.1 | **LOC:** 1081 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **1**; blast radius 4.658; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.3%), Complexity Load (formerly Cognitive Load) (43.0%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UseSpecialLine` **(Many-Argument Workhorses)** (Impact: 370.9)
    * *Intent:* /// <summary> /// Called when a thing uses a special line. /// Only the front sides of lines are usa...
  * `CrossSpecialLine` **(Many-Argument Workhorses)** (Impact: 358.6)
    * *Intent:* //////////////////////////////////////////////////////////// // Line crossing //////////////////////...
  * `ShootSpecialLine` **(Compute Cores)** (Impact: 24.8)
    * *Intent:* //////////////////////////////////////////////////////////// // Line shoot /////////////////////////...
  * `UseTraverse` **(Stateful Encapsulated Methods)** (Impact: 7.2)
  * `UseLines` **(Parameter Forwarders)** (Impact: 2.2)
    * *Intent:* /// <summary> /// Looks for special lines in front of the player to activate. /// </summary>
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 355`, `structural_boundaries: 27`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 45`, `unreferenced_by_name: 3`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `doc: 20`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.658
  * `Choke Point (Betweenness):` 0.001319 | `Ripple Effect (Closeness):` 0.048177
  * `Imports (Out-Degree: 7):` System
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/Game/SaveAndLoad.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.99)
- **Top Global Matches:** file_cluster_4: 5.99, file_cluster_6: 9.931, file_cluster_16: 11.28
- **Magnitude:** 776.66 | **LOC:** 1013 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 2.88; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.0%), Guard Balance (formerly Safety Score) (74.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ArchiveSpecials` **(Many-Argument Workhorses)** (Impact: 40.9)
  * `ArchivePlayer` **(Many-Argument Workhorses)** (Impact: 35.4)
  * `UnArchiveSpecials` **(Compute Cores)** (Impact: 33.9)
  * `UnArchivePlayer` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `UnArchiveThinkers` **(Compute Cores)** (Impact: 18.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 111 instances
* *State Mutation (weighted view):* 486
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 101`, `args: 31`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `state_mutation: 264`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 8`, `import: 2`
* *Defense:* `safety: 10`, `doc: 7`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.88
  * `Choke Point (Betweenness):` 9.3e-05 | `Ripple Effect (Closeness):` 0.004098
  * `Imports (Out-Degree: 5):` System, System.IO
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/World/ThingMovement.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.558)
- **Top Global Matches:** file_cluster_4: 6.558, file_cluster_6: 8.154, file_cluster_9: 12.936
- **Magnitude:** 627.96 | **LOC:** 1179 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **1**; blast radius 6.83; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.2%), Complexity Load (formerly Cognitive Load) (33.0%)
- **Documentation Coverage:** 53.8462% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `XYMovement` **(Compute Cores)** (Impact: 46.7)
  * `ZMovement` **(Compute Cores)** (Impact: 35.6)
  * `TryMove` **(Many-Argument Workhorses)** (Impact: 25.8)
    * *Intent:* /// <summary> /// Attempt to move to a new position, crossing special lines unless /// MobjFlags.Tel...
  * `CheckThing` **(Compute Cores)** (Impact: 24.8)
  * `SlideMove` **(Compute Cores)** (Impact: 22.5)
    * *Intent:* /// <summary> /// The MomX / MomY move is bad, so try to slide along a wall. /// Find the first line...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 93 instances
* *State Mutation (weighted view):* 321
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 122`, `args: 22`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 135`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `doc: 55`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.83
  * `Choke Point (Betweenness):` 0.001764 | `Ripple Effect (Closeness):` 0.052459
  * `Imports (Out-Degree: 13):` System
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/Intermission/Intermission.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.124)
- **Top Global Matches:** file_cluster_6: 9.124, file_cluster_8: 9.785, file_cluster_4: 16.718
- **Magnitude:** 599.38 | **LOC:** 859 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.39; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.6%), Complexity Load (formerly Cognitive Load) (62.7%)
- **Documentation Coverage:** 73.6842% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UpdateNetGameStats` **(I/O & Config Routines)** (Impact: 59.6)
  * `UpdateSinglePlayerStats` **(I/O & Config Routines)** (Impact: 32.9)
  * `UpdateDeathmatchStats` **(I/O & Config Routines)** (Impact: 32.9)
  * `Update` **(I/O & Config Routines)** (Impact: 22.1)
    * *Intent:* //////////////////////////////////////////////////////////// // Update /////////////////////////////...
  * `Intermission` **(Compute Cores)** (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 109 instances
* *State Mutation (weighted view):* 357
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 49`, `args: 32`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 139`
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `doc: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System, System.Collections.Generic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/ItemPickup.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.99)
- **Top Global Matches:** file_cluster_8: 7.99, file_cluster_6: 9.869, file_cluster_4: 18.127
- **Magnitude:** 579.28 | **LOC:** 762 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 3.461; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.1%), Complexity Load (formerly Cognitive Load) (45.7%)
- **Documentation Coverage:** 16.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TouchSpecialThing` **(Many-Argument Workhorses)** (Impact: 246.2)
    * *Intent:* /// <summary> /// Check for item pickup. /// </summary>
  * `GiveAmmo` **(Many-Argument Workhorses)** (Impact: 63.1)
    * *Intent:* /// <summary> /// Give the player the ammo. /// </summary> /// <param name="amount"> /// The number ...
  * `GiveWeapon` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* /// <summary> /// Give the weapon to the player. /// </summary> /// <param name="dropped"> /// True ...
  * `GivePower` **(Stateful Encapsulated Methods)** (Impact: 14.3)
    * *Intent:* /// <summary> /// Give the power up to the player. /// </summary> /// <returns> /// False if the pow...
  * `GiveHealth` **(Stateful Encapsulated Methods)** (Impact: 6.0)
    * *Intent:* /// <summary> /// Give the health point to the player. /// </summary> /// <returns> /// False if the...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 196
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 64`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 68`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `doc: 39`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.461
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.045397
  * `Imports (Out-Degree: 3):` System
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Silk/SilkUserInput.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.153)
- **Top Global Matches:** file_cluster_8: 6.153, file_cluster_6: 14.138, file_cluster_4: 22.781
- **Magnitude:** 567.52 | **LOC:** 581 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 3.708; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SilkToDoom` **(Compute Cores)** (Impact: 150.6)
  * `DoomToSilk` **(Compute Cores)** (Impact: 145.4)
  * `BuildTicCmd` **(Compute Cores)** (Impact: 49.8)
  * `IsPressed` **(Stateful Encapsulated Methods)** (Impact: 11.5)
  * `SilkUserInput` **(Many-Argument Workhorses)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 236`, `args: 12`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 71`, `unreferenced_by_name: 5`
* *Architecture:* `api: 11`, `import: 6`
* *Defense:* `safety: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006148
  * `Imports (Out-Degree: 1):` ManagedDoom.UserInput, Silk.NET.Input, Silk.NET.Windowing, System, System.Numerics, System.Runtime.ExceptionServices
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/Intermission/Finale.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.84)
- **Top Global Matches:** file_cluster_8: 8.84, file_cluster_6: 10.343, file_cluster_4: 18.248
- **Magnitude:** 524.38 | **LOC:** 567 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.39; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.8%), Complexity Load (formerly Cognitive Load) (75.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UpdateCast` **(I/O & Config Routines)** (Impact: 71.8)
  * `Finale` **(Compute Cores)** (Impact: 67.1)
  * `Update` **(I/O & Config Routines)** (Impact: 16.1)
  * `BunnyScroll` **(I/O & Config Routines)** (Impact: 8.8)
  * `DoEvent` **(Type Conversions)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 27`, `args: 18`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 115`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Silk/SilkMusic.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.439)
- **Top Global Matches:** file_cluster_4: 6.439, file_cluster_6: 8.648, file_cluster_16: 12.733
- **Magnitude:** 483.8 | **LOC:** 646 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 3.966; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.2%), Complexity Load (formerly Cognitive Load) (86.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SendEvents` **(Compute Cores)** (Impact: 56.1)
  * `ReadSingleEvent` **(I/O & Config Routines)** (Impact: 27.4)
  * `OnGetData` **(Stateful Encapsulated Methods)** (Impact: 14.7)
  * `ReadData` **(Stateful Encapsulated Methods)** (Impact: 13.7)
  * `ReadSingleEventGroup` **(Stateful Encapsulated Methods)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 67 instances
* *Concurrency (weighted view):* 45
* *State Mutation (weighted view):* 231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 65`, `args: 19`, `func_start: 19`, `class_start: 7`
* *Risk/State:* `state_mutation: 97`, `unreferenced_by_name: 1`
* *Architecture:* `api: 21`, `concurrency: 20`, `import: 6`
* *Defense:* `safety: 2`, `immutability_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.966
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.007881
  * `Imports (Out-Degree: 1):` DrippyAL, ManagedDoom.Audio, MeltySynth, System, System.IO, System.Runtime.ExceptionServices
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Video/DrawScreen.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.356)
- **Top Global Matches:** file_cluster_4: 6.356, file_cluster_9: 9.889, file_cluster_16: 10.643
- **Magnitude:** 481.24 | **LOC:** 535 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 7.804; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%), Complexity Load (formerly Cognitive Load) (69.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DrawLine` **(Many-Argument Workhorses)** (Impact: 50.0)
  * `Bresenham` **(Many-Argument Workhorses)** (Impact: 34.8)
  * `DrawText` **(Many-Argument Workhorses)** (Impact: 21.8)
  * `DrawText` **(Many-Argument Workhorses)** (Impact: 21.8)
  * `MeasureText` **(Compute Cores)** (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 102`, `args: 17`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `state_mutation: 72`, `unreferenced_by_name: 5`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.804
  * `Choke Point (Betweenness):` 6.7e-05 | `Ripple Effect (Closeness):` 0.016393
  * `Imports (Out-Degree: 1):` System, System.Collections.Generic
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Silk/SilkSound.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.366)
- **Top Global Matches:** file_cluster_16: 7.366, file_cluster_15: 7.781, file_cluster_9: 8.214
- **Magnitude:** 445.88 | **LOC:** 586 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 3.708; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.4%), Complexity Load (formerly Cognitive Load) (64.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `StartSound` **(Many-Argument Workhorses)** (Impact: 28.0)
  * `SilkSound` **(Many-Argument Workhorses)** (Impact: 17.1)
  * `Update` **(I/O & Config Routines)** (Impact: 16.4)
  * `SetParam` **(Stateful Encapsulated Methods)** (Impact: 14.1)
  * `GetPitch` **(Stateful Encapsulated Methods)** (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 74`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `state_mutation: 104`, `unreferenced_by_name: 6`
* *Architecture:* `api: 23`, `import: 5`
* *Defense:* `safety: 2`, `immutability_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.708
  * `Choke Point (Betweenness):` 0.00027 | `Ripple Effect (Closeness):` 0.008197
  * `Imports (Out-Degree: 2):` DrippyAL, ManagedDoom.Audio, System, System.Numerics, System.Runtime.ExceptionServices
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/World/ThingAllocation.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.683)
- **Top Global Matches:** file_cluster_6: 6.683, file_cluster_4: 7.497, file_cluster_16: 14.735
- **Magnitude:** 444.24 | **LOC:** 727 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **2**; blast radius 9.106; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.9%), Debt Markers (formerly Tech Debt) (37.3%)
- **Documentation Coverage:** 16.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CheckSpot` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* /// <summary> /// Returns false if the player cannot be respawned at the given /// mapthing spot bec...
  * `SpawnMapThing` **(Compute Cores)** (Impact: 42.1)
    * *Intent:* /// <summary> /// Spawn a mobj at the mapthing. /// </summary>
  * `SpawnMobj` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* //////////////////////////////////////////////////////////// // Thing spawn functions for the middle...
  * `SpawnPlayer` **(Compute Cores)** (Impact: 13.0)
    * *Intent:* /// <summary> /// Called when a player is spawned on the level. /// Most of the player structure sta...
  * `GetMissileSpeed` **(Stateful Encapsulated Methods)** (Impact: 12.3)
    * *Intent:* /// <summary> /// Get the speed of the given missile type. /// Some missiles have different speeds a...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 239
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 73`, `args: 17`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 109`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `safety: 1`, `doc: 47`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.106
  * `Choke Point (Betweenness):` 0.00145 | `Ripple Effect (Closeness):` 0.06053
  * `Imports (Out-Degree: 12):` System, System.Collections.Generic
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/Game/DoomGame.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.173)
- **Top Global Matches:** file_cluster_4: 7.173, file_cluster_6: 7.753, file_cluster_16: 13.706
- **Magnitude:** 442.08 | **LOC:** 621 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 2.88; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.4%), Complexity Load (formerly Cognitive Load) (46.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Update` **(Compute Cores)** (Impact: 85.9)
    * *Intent:* /// <summary> /// Advance the game one frame. /// </summary>
  * `DoCompleted` **(I/O & Config Routines)** (Impact: 50.0)
  * `InitNew` **(Many-Argument Workhorses)** (Impact: 17.8)
    * *Intent:* //////////////////////////////////////////////////////////// // Miscellaneous things ///////////////...
  * `DoReborn` **(Stateful Encapsulated Methods)** (Impact: 12.4)
  * `DoEvent` **(Compute Cores)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 224
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 44`, `args: 23`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `state_mutation: 96`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 16`, `import: 2`
* *Defense:* `safety: 1`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.88
  * `Choke Point (Betweenness):` 8.6e-05 | `Ripple Effect (Closeness):` 0.004098
  * `Imports (Out-Degree: 5):` System, System.IO
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/UserInput/DoomKeyEx.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.883)
- **Top Global Matches:** file_cluster_1: 5.883, file_cluster_3: 48.232, file_cluster_8: 70.061
- **Magnitude:** 427.34 | **LOC:** 578 | **CtrlFlow:** 48.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.39; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (25.6%), Debt Markers (formerly Tech Debt) (12.3%), Connectivity (formerly Api Exposure) (5.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ToString` **(Compute Cores)** (Impact: 157.6)
  * `Parse` **(Compute Cores)** (Impact: 157.6)
  * `GetChar` **(Compute Cores)** (Impact: 97.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 269`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/DeHackEd.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.176)
- **Top Global Matches:** file_cluster_4: 6.176, file_cluster_16: 7.635, file_cluster_15: 9.309
- **Magnitude:** 425.6 | **LOC:** 788 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 8.76; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.5%), Complexity Load (formerly Cognitive Load) (33.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ProcessBlock` **(Many-Argument Workhorses)** (Impact: 54.5)
  * `GetBlockType` **(Compute Cores)** (Impact: 38.1)
  * `ProcessBexStringsBlock` **(Stateful Encapsulated Methods)** (Impact: 14.8)
  * `ProcessBexParsBlock` **(Stateful Encapsulated Methods)** (Impact: 14.6)
  * `ProcessLines` **(Stateful Encapsulated Methods)** (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 135`, `args: 35`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `state_mutation: 82`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 2`, `import: 6`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.76
  * `Choke Point (Betweenness):` 0.000253 | `Ripple Effect (Closeness):` 0.031798
  * `Imports (Out-Degree: 1):` System, System.Collections.Generic, System.IO, System.Linq, System.Runtime.ExceptionServices, System.Text
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/World/PlayerBehavior.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.275)
- **Top Global Matches:** file_cluster_6: 6.275, file_cluster_4: 9.461, file_cluster_8: 16.272
- **Magnitude:** 423.08 | **LOC:** 660 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 4.747; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.7%), Complexity Load (formerly Cognitive Load) (35.1%)
- **Documentation Coverage:** 8.6957% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PlayerThink` **(Many-Argument Workhorses)** (Impact: 57.1)
    * *Intent:* //////////////////////////////////////////////////////////// // Player movement ////////////////////...
  * `PlayerInSpecialSector` **(Compute Cores)** (Impact: 36.2)
    * *Intent:* /// <summary> /// Called every tic frame that the player origin is in a special sector. /// </summar...
  * `SetPlayerSprite` **(Many-Argument Workhorses)** (Impact: 20.0)
    * *Intent:* /// <summary> /// Change the player's weapon sprite. /// </summary>
  * `DeathThink` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* /// <summary> /// Fall on your face when dying. /// Decrease POV height to floor height. /// </summa...
  * `CalcHeight` **(Compute Cores)** (Impact: 19.0)
    * *Intent:* /// <summary> /// Calculate the walking / running height adjustment. /// </summary>
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 22`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 77`, `unreferenced_by_name: 4`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `doc: 43`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.747
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.04918
  * `Imports (Out-Degree: 7):` System
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/Doom.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.533)
- **Top Global Matches:** file_cluster_4: 7.533, file_cluster_6: 7.82, file_cluster_16: 14.401
- **Magnitude:** 404.74 | **LOC:** 557 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 4.592; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CheckFunctionKey` **(Compute Cores)** (Impact: 51.3)
  * `Update` **(I/O & Config Routines)** (Impact: 28.5)
  * `Doom` **(Many-Argument Workhorses)** (Impact: 19.5)
  * `DoEvents` **(I/O & Config Routines)** (Impact: 17.1)
  * `CheckGameArgs` **(I/O & Config Routines)** (Impact: 16.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 60 instances
* *State Mutation (weighted view):* 208
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 40`, `args: 25`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 88`, `unreferenced_by_name: 6`
* *Architecture:* `api: 21`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.592
  * `Choke Point (Betweenness):` 0.000135 | `Ripple Effect (Closeness):` 0.013805
  * `Imports (Out-Degree: 1):` ManagedDoom.Audio, ManagedDoom.UserInput, ManagedDoom.Video, System, System.Collections.Generic
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/Math/Geometry.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.539)
- **Top Global Matches:** file_cluster_8: 5.539, file_cluster_6: 16.994, file_cluster_3: 19.439
- **Magnitude:** 381.38 | **LOC:** 626 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **1**; blast radius 13.262; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.2%), Guard Balance (formerly Safety Score) (55.7%), Debt Markers (formerly Tech Debt) (28.4%), Complexity Load (formerly Cognitive Load) (16.3%)
- **Documentation Coverage:** 4.3478% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PointToAngle` **(Many-Argument Workhorses)** (Impact: 39.8)
    * *Intent:* /// <summary> /// Calculate the angle of the line passing through the two points. /// </summary>
  * `BoxOnLineSide` **(Compute Cores)** (Impact: 35.4)
    * *Intent:* /// <summary> /// Calculate on which side of the line the box is. /// </summary> /// <returns> /// 0...
  * `PointOnSegSide` **(Many-Argument Workhorses)** (Impact: 35.1)
    * *Intent:* /// <summary> /// Calculate on which side of the line the point is. /// </summary> /// <returns> ///...
  * `PointOnDivLineSide` **(Many-Argument Workhorses)** (Impact: 34.9)
    * *Intent:* /// <summary> /// Calculate on which side of the line the point is. /// </summary> /// <returns> ///...
  * `PointOnSide` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* /// <summary> /// Calculate on which side of the node the point is. /// </summary> /// <returns> ///...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 108`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `unreferenced_by_name: 7`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `doc: 54`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.262
  * `Choke Point (Betweenness):` 0.000528 | `Ripple Effect (Closeness):` 0.071136
  * `Imports (Out-Degree: 4):` System
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/World/WeaponBehavior.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.686)
- **Top Global Matches:** file_cluster_16: 7.686, file_cluster_15: 7.959, file_cluster_4: 8.206
- **Magnitude:** 369.98 | **LOC:** 698 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 5.046; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (85.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CheckAmmo` **(Type Conversions)** (Impact: 38.4)
  * `RecursiveSound` **(Many-Argument Workhorses)** (Impact: 29.5)
  * `WeaponReady` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `Saw` **(Compute Cores)** (Impact: 14.1)
  * `BFGSpray` **(Compute Cores)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 53`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 60`, `unreferenced_by_name: 21`
* *Architecture:* `api: 29`, `import: 1`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.046
  * `Choke Point (Betweenness):` 0.000766 | `Ripple Effect (Closeness):` 0.045397
  * `Imports (Out-Degree: 10):` System
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ManagedDoomTest/src/CompatibilityTests/Monsters.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.781)
- **Top Global Matches:** file_cluster_13: 5.781, file_cluster_10: 6.611, file_cluster_2: 7.586
- **Magnitude:** 339.28 | **LOC:** 645 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.39; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (80.2%), Guard Balance (formerly Safety Score) (61.2%), Complexity Load (formerly Cognitive Load) (57.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NightmareTest` **(Annotated & Test Methods)** (Impact: 5.5)
  * `BarrelTest` **(Annotated & Test Methods)** (Impact: 5.5)
  * `ZombiemanTest` **(Annotated & Test Methods)** (Impact: 5.5)
  * `ZombiemanTest2` **(Annotated & Test Methods)** (Impact: 5.5)
  * `ShotgunguyTest` **(Annotated & Test Methods)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 175`, `args: 42`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`, `unreferenced_by_name: 21`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `test: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ManagedDoom, Microsoft.VisualStudio.TestTools.UnitTesting, System, System.Collections.Generic, System.Linq
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Video/IntermissionRenderer.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.769)
- **Top Global Matches:** file_cluster_16: 5.769, file_cluster_15: 8.011, file_cluster_9: 8.621
- **Magnitude:** 328.36 | **LOC:** 720 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 2.616; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (39.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DrawNumber` **(Many-Argument Workhorses)** (Impact: 22.7)
  * `Render` **(Compute Cores)** (Impact: 18.4)
  * `DrawDeathmatchStats` **(Compute Cores)** (Impact: 17.5)
  * `DrawTime` **(Stateful Encapsulated Methods)** (Impact: 15.7)
  * `DrawSuitablePatch` **(Stateful Encapsulated Methods)** (Impact: 15.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 57`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 54`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004098
  * `Imports (Out-Degree: 1):` System, System.Collections.Generic
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Video/StatusBarRenderer.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.893)
- **Top Global Matches:** file_cluster_6: 6.893, file_cluster_4: 11.108, file_cluster_8: 15.426
- **Magnitude:** 315.2 | **LOC:** 480 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 2.616; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.8%), Complexity Load (formerly Cognitive Load) (57.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Render` **(Many-Argument Workhorses)** (Impact: 31.8)
  * `DrawNumber` **(Many-Argument Workhorses)** (Impact: 18.9)
  * `Patches` **(Compute Cores)** (Impact: 12.5)
  * `StatusBarRenderer` **(Many-Argument Workhorses)** (Impact: 6.0)
  * `DrawPercent` **(Stateful Encapsulated Methods)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 28`, `args: 6`, `func_start: 6`, `class_start: 5`
* *Risk/State:* `state_mutation: 130`, `unreferenced_by_name: 1`
* *Architecture:* `api: 24`, `import: 1`
* *Defense:* `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004098
  * `Imports (Out-Degree: 1):` System
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ManagedDoom/src/Doom/World/Cheat.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.818)
- **Top Global Matches:** file_cluster_16: 5.818, file_cluster_15: 7.857, file_cluster_10: 8.259
- **Magnitude:** 299.7 | **LOC:** 429 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 3.015; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.2%), Complexity Load (formerly Cognitive Load) (65.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DoPowerUp` **(Stateful Encapsulated Methods)** (Impact: 21.0)
  * `CheckBuffer` **(I/O & Config Routines)** (Impact: 12.2)
  * `ChangeMusic` **(Stateful Encapsulated Methods)** (Impact: 10.0)
  * `ChangeLevel` **(Stateful Encapsulated Methods)** (Impact: 9.9)
  * `GiveWeapons` **(Type Conversions)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 57`, `args: 37`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `state_mutation: 67`, `unreferenced_by_name: 1`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `safety: 3`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.044541
  * `Imports (Out-Degree: 3):` System, System.Linq
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `ManagedDoom/src/Doom/World/MobjStateDef.cs` (CSHARP) | Magnitude: 25.84 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 21, args: 19, closures: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `ManagedDoom/src/Silk/SilkVideo.cs` (CSHARP) | Magnitude: 78.9 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 119, core_var_decl: 32, structural_boundaries: 27, design_snake_case: 21
- `ManagedDoom/src/Doom/Map/MapThing.cs` (CSHARP) | Magnitude: 34.24 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 22, core_var_decl: 19, design_snake_case: 13
- `ManagedDoom/src/Doom/Intermission/WorldMap.cs` (CSHARP) | Magnitude: 11.18 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 7, api: 6, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ManagedDoom/src/Doom/Map/ThingFlags.cs` (CSHARP) | Magnitude: 17.24 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 8, core_var_decl: 4, design_pascal_case: 4, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `ManagedDoom/src/Doom/Info/DoomInfo.Strings.cs` (CSHARP) | Magnitude: 286.0 | Delta: **0.145** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 496, api: 258, globals: 256, immutability_locks: 256

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `ManagedDoom/src/Audio/ISound.cs` (CSHARP) | Magnitude: 25.56 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, api: 12, args: 9, func_start: 9
- `ManagedDoom/src/Doom/Info/DoomInfo.ParTimes.cs` (CSHARP) | Magnitude: 19.5 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 5, api: 4, class_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `ManagedDoom/src/Video/Renderer.cs` (CSHARP) | Magnitude: 204.58 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 304, core_var_decl: 55, branch: 43, structural_boundaries: 39
- `ManagedDoom/src/Doom/World/GlowingLight.cs` (CSHARP) | Magnitude: 37.98 | Delta: **0.145** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 11, core_var_decl: 11, args: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `ManagedDoom/src/Doom/Math/Angle.cs` -> Churn: **85.53%** | Cog Load: 6.0595% | Debt: 99.9994%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `ManagedDoom/src/Video/Renderer.cs` -> **Nobuaki Tanaka** (100.0% isolated ownership) | Magnitude: 204.58
- `ManagedDoom/src/Doom/Math/Angle.cs` -> **Nobuaki Tanaka** (100.0% isolated ownership) | Magnitude: 67.24

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `ManagedDoom/src/Doom/World/World.cs` -> **Severity: 0.943** (Bridge: 0.0094 * Flux: 99.9993%)
- `ManagedDoom/src/Doom/World/SectorAction.cs` -> **Severity: 0.313** (Bridge: 0.0031 * Flux: 100.0%)
- `ManagedDoom/src/Doom/World/ThingMovement.cs` -> **Severity: 0.176** (Bridge: 0.0018 * Flux: 99.9999%)
- `ManagedDoom/src/Doom/World/LightingChange.cs` -> **Severity: 0.17** (Bridge: 0.0017 * Flux: 100.0%)
- `ManagedDoom/src/Doom/Menu/DoomMenu.cs` -> **Severity: 0.157** (Bridge: 0.0018 * Flux: 89.3082%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `ManagedDoom/src/Doom/Math/Fixed.cs` -> **Severity: 7.23** (Embedded: 0.144 * Error Risk: 50.211%)
- `ManagedDoom/src/Doom/World/World.cs` -> **Severity: 5.021** (Embedded: 0.0761 * Error Risk: 65.9301%)
- `ManagedDoom/src/Doom/Math/Angle.cs` -> **Severity: 4.307** (Embedded: 0.0851 * Error Risk: 50.6369%)
- `ManagedDoom/src/Doom/World/ThingAllocation.cs` -> **Severity: 4.29** (Embedded: 0.0605 * Error Risk: 70.8697%)
- `ManagedDoom/src/Doom/World/ThingInteraction.cs` -> **Severity: 4.129** (Embedded: 0.0562 * Error Risk: 73.4618%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ManagedDoom/src/Doom/Math/Fixed.cs` -> **Severity: 5488.9** (Blast Radius: 54.889 * Doc Risk: 100.0%)
- `ManagedDoom/src/Doom/Menu/DoomMenu.cs` -> **Severity: 2110.8** (Blast Radius: 21.108 * Doc Risk: 100.0%)
- `ManagedDoom/src/Doom/Math/Angle.cs` -> **Severity: 2099.6** (Blast Radius: 20.996 * Doc Risk: 100.0%)
- `ManagedDoom/src/Doom/Map/Vertex.cs` -> **Severity: 2028.7** (Blast Radius: 20.287 * Doc Risk: 100.0%)
- `ManagedDoom/src/Doom/Graphics/Column.cs` -> **Severity: 1822.4** (Blast Radius: 18.224 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 4049 call pairs -- scoped 43.6%, unique 2.3%, ambiguous 29.3%, external 24.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| csharp | 4049 | 43.6% | 2.3% | 29.3% | 24.7% |

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
