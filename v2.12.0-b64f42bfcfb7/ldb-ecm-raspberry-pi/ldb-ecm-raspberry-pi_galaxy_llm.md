# ARCHITECTURAL_BRIEF: ldb-ecm-raspberry-pi
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/LdB-ECM/Raspberry-Pi.git` |
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
- **Scope:** 215 analyzed artifact(s), 69607 LOC.
- **Load-bearing artifact:** `FreeRTOSv10.1.1/FreeRTOS/Source/include/task.h` -- 15 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `FreeRTOSv10.1.1/FreeRTOS/Source/include/deprecated_definitions.h` -- pulls in 44 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Arm32_64_USB/rpi-usb.c` at magnitude 2247.72 (structural weight, not risk).
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
| Total Artifacts | 377 |
| Analyzed Artifacts (Scanned) | 215 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 162 |
| Total LOC | 69607 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 57.0% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8343 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.3047 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7749 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 28 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 138 | 55015 | 64.2% |
| ASSEMBLY | 27 | 12688 | 12.6% |
| BATCH | 16 | 384 | 7.4% |
| MARKDOWN | 15 | 0 | 7.0% |
| MAKEFILE | 10 | 663 | 4.7% |
| PLAINTEXT | 6 | 0 | 2.8% |
| CPP | 3 | 857 | 1.4% |

## 4.1 SOURCE ENCODINGS
> 5 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 198 |
| utf-8 | bom | 12 |
| cp1252 | cp1252-fallback | 5 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 40%, Large Core Modules (3) 22%, Parameter Forwarders Files 15%, Data / Markup / Trivial 10%, State Mutators Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 194 | 90.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 21 | 9.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 162*

**Composition by Extension & Reason:**
- `.img`: 53x Excluded (Unsupported Extension: '.img')
- `.ld`: 28x Excluded (Unsupported Extension: '.ld')
- `.elf`: 18x Excluded (Unsupported Extension: '.elf')
- `.bin`: 14x Excluded (Unsupported Extension: '.bin')
- `.dat`: 14x Excluded (Unsupported Extension: '.dat')
- `.md`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 6x Excluded (Explicitly Denied Extension: '.JPG'), 1x Excluded (Explicitly Denied Extension: '.jpg')
- `no_extension`: 3x Unsupported Format (.undeterminable), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mtl`: 4x Excluded (Unsupported Extension: '.mtl')
- `.map`: 1x Excluded (Embedded Hex Payload: 660 hex tokens in 589 LOC), 1x Excluded (Embedded Hex Payload: 1442 hex tokens in 1069 LOC), 1x Excluded (Embedded Hex Payload: 665 hex tokens in 572 LOC)
- `.o`: 4x Excluded (Explicitly Denied Extension: '.o')
- `.obj`: 2x Excluded (Explicitly Denied Extension: '.obj')
- `.readme`: 1x Excluded (Unsupported Extension: '.readme')
- `.url`: 1x Excluded (Unsupported Extension: '.url')
- `.bmp`: 1x Excluded (Explicitly Denied Extension: '.bmp')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.0 | 21.5 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.5 | 34.8 | 49.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 29.9 | 19.9 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 32.0 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 25.2 | 8.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 33.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 93.4 | 3.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 45.0 | 50.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 286 | 45 | 4 | `FreeRTOSv10.1.1/FreeRTOS/Source/tasks.c` |
| cleanup | 14 | 12 | 0 | `arduino/wstring.cpp` |
| guards | 3241 | 152 | 60 | `FreeRTOSv10.1.1/FreeRTOS/Source/stream_buffer.c` |
| danger | 195 | 59 | 2 | `FreeRTOSv10.1.1/FreeRTOS/Source/portable/GCC/RaspberryPi/portmacro.h` |
| concurrency | 94 | 23 | 1 | `10_virtualmemory/SmartStart64.S` |
| connectivity | 3802 | 172 | 57 | `FreeRTOSv10.1.1/FreeRTOS/Source/include/mpu_prototypes.h` |
| io | 53 | 21 | 0 | `GLES2_Model/rpi-GLES.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 55 | 2 | 0 | `Arm32_64_USB/rpi-usb.c` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 27 | 10 | 0 | `FreeRTOSv10.1.1/Makefile` |
| events | 41 | 18 | 0 | `10_virtualmemory/emb-stdio.c` |
| tests | 2 | 2 | 0 | `PlayGround/emb-stdio.c` |
| docs | 506 | 71 | 6 | `FreeRTOSv10.1.1/FreeRTOS/Source/include/task.h` |
| debt | 412 | 128 | 5 | `GLES2_Model/rpi-GLES.c` |
| mutation | 17145 | 127 | 277 | `Arm32_64_USB/rpi-usb.c` |
| dead_code | 1191 | 99 | 22 | `FreeRTOSv10.1.1/FreeRTOS/Source/tasks.c` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 15 | 6 | 0 | `PlayGround/main.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `GLES2_Model/rpi-GLES.c` (Hits: 10)
- `PlayGround/Makefile` (Hits: 6)
- `SimpleSched/Makefile` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **task.h** (`FreeRTOSv10.1.1/FreeRTOS/Source/include/task.h`) — 15 inbound connections
2. **FreeRTOS.h** (`FreeRTOSv10.1.1/FreeRTOS/Source/include/FreeRTOS.h`) — 14 inbound connections
3. **tasks.c** (`FreeRTOSv10.1.1/FreeRTOS/Source/tasks.c`) — 12 inbound connections
4. **rpi-smartstart.h** (`GLES2_Model/rpi-smartstart.h`) — 6 inbound connections
5. **list.c** (`FreeRTOSv10.1.1/FreeRTOS/Source/list.c`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **deprecated_definitions.h** (`FreeRTOSv10.1.1/FreeRTOS/Source/include/deprecated_definitions.h`) — 44 outbound dependencies
2. **emb-stdio.c** (`PlayGround/emb-stdio.c`) — 12 outbound dependencies
3. **emb-stdio.c** (`SimpleSched/emb-stdio.c`) — 12 outbound dependencies
4. **rpi-SmartStart.c** (`GLES2_Model/rpi-SmartStart.c`) — 11 outbound dependencies
5. **rpi-SmartStart.c** (`GLES2_Rotate/rpi-SmartStart.c`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `vsscanf` **(Many-Argument Workhorses)** (@ `PlayGround/emb-stdio.c`) -> Impact: **397.9** | LOC: 518
  * *Intent:* {--------------------------------------------------------------------------*/
- `vsscanf` **(Many-Argument Workhorses)** (@ `SimpleSched/emb-stdio.c`) -> Impact: **397.9** | LOC: 518
  * *Intent:* {--------------------------------------------------------------------------*/
- `vsscanf` **(Many-Argument Workhorses)** (@ `GLES2_Model/emb-stdio.c`) -> Impact: **397.6** | LOC: 512
  * *Intent:* {--------------------------------------------------------------------------*/
- `vsscanf` **(Many-Argument Workhorses)** (@ `Multicore/emb-stdio.c`) -> Impact: **397.6** | LOC: 512
  * *Intent:* {--------------------------------------------------------------------------*/
- `Process_Out` **(Many-Argument Workhorses)** (@ `PlayGround/emb-stdio.c`) -> Impact: **257.0** | LOC: 354
  * *Intent:* .--------------------------------------------------------------------------*/
- `Process_Out` **(Many-Argument Workhorses)** (@ `SimpleSched/emb-stdio.c`) -> Impact: **257.0** | LOC: 354
  * *Intent:* .--------------------------------------------------------------------------*/
- `ParseWaveFrontMesh` **(Many-Argument Workhorses)** (@ `GLES2_Model/rpi-GLES.c`) -> Impact: **216.3** | LOC: 345
  * *Intent:* #include <float.h>
- `_doprnt` **(Many-Argument Workhorses)** (@ `10_virtualmemory/emb-stdio.c`) -> Impact: **199.2** | LOC: 452
  * *Intent:* * @param fmt * Format string. * @param ap * Variable-length list of values that will be formatted. * @param putc_func * Character output function. It ...
- `_doprnt` **(Many-Argument Workhorses)** (@ `FreeRTOSv10.1.1/Demo/emb-stdio.c`) -> Impact: **199.2** | LOC: 452
  * *Intent:* * @param fmt * Format string. * @param ap * Variable-length list of values that will be formatted. * @param putc_func * Character output function. It ...
- `_doprnt` **(Many-Argument Workhorses)** (@ `Arm32_64_USB/emb-stdio.c`) -> Impact: **187.4** | LOC: 439
  * *Intent:* * @param fmt * Format string. * @param ap * Variable-length list of values that will be formatted. * @param putc_func * Character output function. It ...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `GLES2_Model` | 15 | 6370.94 | 24.55% | 26.77% |
| `Arm32_64_USB` | 12 | 5050.3 | 21.18% | 28.16% |
| `FreeRTOSv10.1.1/FreeRTOS/Source` | 8 | 4710.38 | 47.28% | 47.23% |
| `SD_FAT32` | 16 | 4567.06 | 16.53% | 21.81% |
| `PlayGround` | 10 | 4319.82 | 26.56% | 33.26% |
| `SimpleSched` | 11 | 3985.1 | 22.23% | 37.49% |
| `Multicore` | 14 | 3411.36 | 18.47% | 22.46% |
| `GL_GUI_STEP1` | 12 | 3214.26 | 18.31% | 30.04% |
| `10_virtualmemory` | 14 | 3174.76 | 20.13% | 25.9% |
| `GLES2` | 12 | 3012.14 | 15.65% | 32.48% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `SimpleSched/Makefile` -> **99.9447%** Exposure
- `myBlinker/SmartStart32.S` -> **99.3307%** Exposure
- `SimpleSched/SmartStart32.S` -> **99.0814%** Exposure
- `Arm32_64_USB/SmartStart32.S` -> **99.0264%** Exposure
- `Core3Interrupt/SmartStart32.S` -> **99.0264%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `10_virtualmemory/emb-stdio.c` -> **100.0%** Exposure
- `10_virtualmemory/mmu.c` -> **100.0%** Exposure
- `10_virtualmemory/windows.c` -> **100.0%** Exposure
- `Arm32_64_USB/emb-stdio.c` -> **100.0%** Exposure
- `Arm32_64_USB/rpi-SmartStart.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `FreeRTOSv10.1.1/FreeRTOS/Source/tasks.c` -> **58** Orphaned Functions | **0** Duplicates
- `FreeRTOSv10.1.1/FreeRTOS/Source/queue.c` -> **33** Orphaned Functions | **0** Duplicates
- `PlayGround/rpi-SmartStart.c` -> **33** Orphaned Functions | **0** Duplicates
- `SimpleSched/rpi-SmartStart.c` -> **32** Orphaned Functions | **0** Duplicates
- `Arm32_64_USB/rpi-SmartStart.c` -> **31** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `19` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `575` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Arm32_64_USB/rpi-usb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.148)
- **Top Global Matches:** file_cluster_6: 5.148, file_cluster_4: 10.856, file_cluster_8: 13.854
- **Magnitude:** 2247.72 | **LOC:** 3393 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 3.814; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.3%), Complexity Load (formerly Cognitive Load) (63.8%)
- **Documentation Coverage:** 86.0658% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HcdProcessRootHubMessage` **(Many-Argument Workhorses)** (Impact: 164.7)
    * *Intent:* {==========================================================================*/
  * `EnumerateDevice` **(Many-Argument Workhorses)** (Impact: 85.3)
    * *Intent:* --------------------------------------------------------------------------*/
  * `UsbGetDescription` **(Compute Cores)** (Impact: 85.2)
    * *Intent:* --------------------------------------------------------------------------*/
  * `HCDChannelTransfer` **(Many-Argument Workhorses)** (Impact: 66.7)
    * *Intent:* --------------------------------------------------------------------------*/
  * `HCDReadStringDescriptor` **(Many-Argument Workhorses)** (Impact: 48.9)
    * *Intent:* --------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 326 instances
* *State Mutation (weighted view):* 1077
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 465`, `structural_boundaries: 810`, `args: 64`, `func_start: 51`, `class_start: 133`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 425`, `dead_code: 10`, `fragile_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 82`, `import: 8`
* *Defense:* `safety: 20`, `doc: 14`, `immutability_locks: 74`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.814
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004673
  * `Imports (Out-Degree: 2):` assert.h, rpi-smartstart.h, rpi-usb.h, stdbool.h, stdint.h, stdlib.h, string.h, wchar.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `FreeRTOSv10.1.1/FreeRTOS/Source/tasks.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.224)
- **Top Global Matches:** file_cluster_4: 6.224, file_cluster_15: 8.956, file_cluster_16: 9.089
- **Magnitude:** 1968.66 | **LOC:** 5111 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **9**; blast radius 11.489; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.0%), Debt Markers (formerly Tech Debt) (59.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xTaskGenericNotifyFromISR` **(Many-Argument Workhorses)** (Impact: 47.8)
    * *Intent:* #endif /* configUSE_TASK_NOTIFICATIONS */ /*--------------------------------------------------------...
  * `vTaskPrioritySet` **(Many-Argument Workhorses)** (Impact: 46.0)
    * *Intent:* #endif /* INCLUDE_uxTaskPriorityGet */ /*-----------------------------------------------------------...
  * `prvInitialiseNewTask` **(Many-Argument Workhorses)** (Impact: 43.2)
    * *Intent:* #endif /* configSUPPORT_DYNAMIC_ALLOCATION */ /*----------------------------------------------------...
  * `xTaskGenericNotify` **(Many-Argument Workhorses)** (Impact: 38.9)
    * *Intent:* #endif /* configUSE_TASK_NOTIFICATIONS */ /*--------------------------------------------------------...
  * `xTaskIncrementTick` **(I/O & Config Routines)** (Impact: 33.2)
    * *Intent:* #endif /* INCLUDE_xTaskAbortDelay */ /*----------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 271 instances
* *State Mutation (weighted view):* 893
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 412`, `structural_boundaries: 192`, `args: 100`, `func_start: 81`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 351`, `fragile_debt: 1`, `unreferenced_by_name: 58`
* *Architecture:* `api: 26`, `import: 9`
* *Defense:* `safety: 4`, `doc: 3`, `immutability_locks: 88`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.489
  * `Choke Point (Betweenness):` 0.001942 | `Ripple Effect (Closeness):` 0.056075
  * `Imports (Out-Degree: 7):` FreeRTOS.h, freertos_tasks_c_additions.h, stack_macros.h, stdio.h, stdlib.h, string.h, task.h, tasks_test_access_functions.h...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `GLES2_Model/SDCard.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.353)
- **Top Global Matches:** file_cluster_6: 7.353, file_cluster_8: 9.761, file_cluster_4: 15.346
- **Magnitude:** 1811.9 | **LOC:** 2497 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.7%), Complexity Load (formerly Cognitive Load) (67.9%)
- **Documentation Coverage:** 77.3583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LocateFATEntry` **(Many-Argument Workhorses)** (Impact: 98.2)
    * *Intent:* .--------------------------------------------------------------------------*/ #define FILE_EMPTY 0x0...
  * `sdTransferBlocks` **(Many-Argument Workhorses)** (Impact: 81.2)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `sdInitCard` **(Many-Argument Workhorses)** (Impact: 52.9)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `sdReadFile` **(Many-Argument Workhorses)** (Impact: 47.0)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `sdCreateFile` **(Many-Argument Workhorses)** (Impact: 46.1)
    * *Intent:* .--------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 299 instances
* *State Mutation (weighted view):* 951
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 364`, `structural_boundaries: 354`, `args: 66`, `func_start: 36`, `class_start: 79`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 353`, `dead_code: 11`, `planned_debt: 4`, `unreferenced_by_name: 11`
* *Architecture:* `api: 39`, `import: 9`
* *Defense:* `safety: 15`, `doc: 5`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` SDCard.h, assert.h, ctype.h, emb-stdio.h, rpi-smartstart.h, stdbool.h, stdint.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `SD_FAT32/SDCard.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.353)
- **Top Global Matches:** file_cluster_6: 7.353, file_cluster_8: 9.761, file_cluster_4: 15.346
- **Magnitude:** 1811.9 | **LOC:** 2497 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.7%), Complexity Load (formerly Cognitive Load) (67.9%)
- **Documentation Coverage:** 65.3131% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LocateFATEntry` **(Many-Argument Workhorses)** (Impact: 98.2)
    * *Intent:* .--------------------------------------------------------------------------*/ #define FILE_EMPTY 0x0...
  * `sdTransferBlocks` **(Many-Argument Workhorses)** (Impact: 81.2)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `sdInitCard` **(Many-Argument Workhorses)** (Impact: 52.9)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `sdReadFile` **(Many-Argument Workhorses)** (Impact: 47.0)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `sdCreateFile` **(Many-Argument Workhorses)** (Impact: 46.1)
    * *Intent:* .--------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 299 instances
* *State Mutation (weighted view):* 951
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 364`, `structural_boundaries: 354`, `args: 66`, `func_start: 36`, `class_start: 79`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 353`, `dead_code: 11`, `planned_debt: 4`, `unreferenced_by_name: 11`
* *Architecture:* `api: 39`, `import: 9`
* *Defense:* `safety: 15`, `doc: 5`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` SDCard.h, assert.h, ctype.h, emb-stdio.h, rpi-smartstart.h, stdbool.h, stdint.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `PlayGround/emb-stdio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.317)
- **Top Global Matches:** file_cluster_6: 6.317, file_cluster_8: 10.885, file_cluster_4: 13.798
- **Magnitude:** 1784.3 | **LOC:** 1579 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.3%)
- **Documentation Coverage:** 88.78% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vsscanf` **(Many-Argument Workhorses)** (Impact: 397.9)
    * *Intent:* {--------------------------------------------------------------------------*/
  * `Process_Out` **(Many-Argument Workhorses)** (Impact: 257.0)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `cvt_int` **(Many-Argument Workhorses)** (Impact: 67.3)
    * *Intent:* /* we are called with base 2, 8, 10 or 16 */ static const char digits[16] = "0123456789ABCDEF"; /* "...
  * `number` **(Many-Argument Workhorses)** (Impact: 65.7)
  * `cvt` **(Many-Argument Workhorses)** (Impact: 34.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 280 instances
* *State Mutation (weighted view):* 851
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 173`, `args: 27`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 291`, `dead_code: 1`, `unreferenced_by_name: 7`
* *Architecture:* `io: 1`, `api: 12`, `import: 12`
* *Defense:* `safety: 32`, `doc: 2`, `test: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ctype.h, emb-stdio.h, float.h, math.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stddef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `SimpleSched/emb-stdio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.317)
- **Top Global Matches:** file_cluster_6: 6.317, file_cluster_8: 10.885, file_cluster_4: 13.798
- **Magnitude:** 1784.3 | **LOC:** 1579 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.3%)
- **Documentation Coverage:** 78.019% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vsscanf` **(Many-Argument Workhorses)** (Impact: 397.9)
    * *Intent:* {--------------------------------------------------------------------------*/
  * `Process_Out` **(Many-Argument Workhorses)** (Impact: 257.0)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `cvt_int` **(Many-Argument Workhorses)** (Impact: 67.3)
    * *Intent:* /* we are called with base 2, 8, 10 or 16 */ static const char digits[16] = "0123456789ABCDEF"; /* "...
  * `number` **(Many-Argument Workhorses)** (Impact: 65.7)
  * `cvt` **(Many-Argument Workhorses)** (Impact: 34.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 280 instances
* *State Mutation (weighted view):* 851
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 173`, `args: 27`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 291`, `dead_code: 1`, `unreferenced_by_name: 7`
* *Architecture:* `io: 1`, `api: 12`, `import: 12`
* *Defense:* `safety: 32`, `doc: 2`, `test: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ctype.h, emb-stdio.h, float.h, math.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stddef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `FreeRTOSv10.1.1/loader/RaspberryPi/rpi-SmartStart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.205)
- **Top Global Matches:** file_cluster_4: 6.205, file_cluster_15: 7.606, file_cluster_16: 8.087
- **Magnitude:** 1747.26 | **LOC:** 2510 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.9%), Complexity Load (formerly Cognitive Load) (62.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SelectObject` **(Many-Argument Workhorses)** (Impact: 44.7)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `PiConsole_Init` **(Many-Argument Workhorses)** (Impact: 39.5)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `Rectangle` **(Many-Argument Workhorses)** (Impact: 34.1)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `console_uart_init` **(Compute Cores)** (Impact: 25.0)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `set_Activity_LED` **(Compute Cores)** (Impact: 24.6)
    * *Intent:* .--------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 295 instances
* *State Mutation (weighted view):* 948
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 252`, `structural_boundaries: 334`, `args: 79`, `func_start: 91`, `class_start: 72`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 358`, `planned_debt: 2`, `unreferenced_by_name: 30`
* *Architecture:* `api: 92`, `import: 8`
* *Defense:* `safety: 11`, `doc: 6`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Font8x16.h, assert.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stdint.h, string.h, types.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `PlayGround/rpi-SmartStart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.813)
- **Top Global Matches:** file_cluster_4: 5.813, file_cluster_16: 7.54, file_cluster_15: 7.735
- **Magnitude:** 1688.82 | **LOC:** 1953 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 4.037; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.6%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (76.7%)
- **Documentation Coverage:** 88.78% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CvtBmpLine` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `PiConsole_Init` **(Many-Argument Workhorses)** (Impact: 39.4)
  * `set_Activity_LED` **(Compute Cores)** (Impact: 24.5)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `LineTo` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `gpio_edgeDetect` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* .-------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 327 instances
* *State Mutation (weighted view):* 1038
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 272`, `args: 76`, `func_start: 67`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 384`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 33`
* *Architecture:* `api: 69`, `import: 9`
* *Defense:* `safety: 10`, `doc: 5`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.037
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.004673
  * `Imports (Out-Degree: 2):` Font8x16.h, assert.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stdint.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `SimpleSched/rpi-SmartStart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.753)
- **Top Global Matches:** file_cluster_4: 6.753, file_cluster_15: 6.947, file_cluster_16: 7.299
- **Magnitude:** 1618.18 | **LOC:** 1878 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.4%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (77.3%)
- **Documentation Coverage:** 78.019% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CvtBmpLine` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `PiConsole_Init` **(Many-Argument Workhorses)** (Impact: 39.3)
  * `LineTo` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `gpio_edgeDetect` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* .-------------------------------------------------------------------------*/
  * `set_Activity_LED` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* .--------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 317 instances
* *State Mutation (weighted view):* 996
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 261`, `args: 71`, `func_start: 62`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 362`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 32`
* *Architecture:* `api: 67`, `import: 9`
* *Defense:* `safety: 10`, `doc: 5`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Font8x16.h, assert.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stdint.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Arm32_64_USB/rpi-SmartStart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.37)
- **Top Global Matches:** file_cluster_4: 5.37, file_cluster_15: 8.152, file_cluster_16: 8.267
- **Magnitude:** 1590.66 | **LOC:** 1603 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (85.5%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 86.944% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CvtBmpLine` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `PiConsole_Init` **(Many-Argument Workhorses)** (Impact: 39.3)
  * `set_Activity_LED` **(Compute Cores)** (Impact: 24.5)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `LineTo` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `gpio_edgeDetect` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* .-------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 316 instances
* *State Mutation (weighted view):* 990
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 218`, `args: 65`, `func_start: 58`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 358`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 31`
* *Architecture:* `api: 51`, `import: 9`
* *Defense:* `safety: 9`, `doc: 5`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Font8x16.h, assert.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stdint.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Core3Interrupt/rpi-SmartStart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.366)
- **Top Global Matches:** file_cluster_4: 5.366, file_cluster_15: 8.146, file_cluster_16: 8.263
- **Magnitude:** 1590.66 | **LOC:** 1603 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (85.5%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 77.356% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CvtBmpLine` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `PiConsole_Init` **(Many-Argument Workhorses)** (Impact: 39.3)
  * `set_Activity_LED` **(Compute Cores)** (Impact: 24.5)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `LineTo` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `gpio_edgeDetect` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* .-------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 316 instances
* *State Mutation (weighted view):* 990
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 218`, `args: 65`, `func_start: 58`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 358`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 31`
* *Architecture:* `api: 51`, `import: 9`
* *Defense:* `safety: 9`, `doc: 5`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Font8x16.h, assert.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stdint.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `GLES2/rpi-SmartStart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.37)
- **Top Global Matches:** file_cluster_4: 5.37, file_cluster_15: 8.152, file_cluster_16: 8.267
- **Magnitude:** 1590.66 | **LOC:** 1603 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (85.5%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 79.192% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CvtBmpLine` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `PiConsole_Init` **(Many-Argument Workhorses)** (Impact: 39.3)
  * `set_Activity_LED` **(Compute Cores)** (Impact: 24.5)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `LineTo` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `gpio_edgeDetect` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* .-------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 316 instances
* *State Mutation (weighted view):* 990
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 218`, `args: 65`, `func_start: 58`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 358`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 31`
* *Architecture:* `api: 51`, `import: 9`
* *Defense:* `safety: 9`, `doc: 5`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Font8x16.h, assert.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stdint.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `GL_GUI_STEP1/rpi-SmartStart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.37)
- **Top Global Matches:** file_cluster_4: 5.37, file_cluster_15: 8.152, file_cluster_16: 8.267
- **Magnitude:** 1590.66 | **LOC:** 1603 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (85.5%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 91.483% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CvtBmpLine` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `PiConsole_Init` **(Many-Argument Workhorses)** (Impact: 39.3)
  * `set_Activity_LED` **(Compute Cores)** (Impact: 24.5)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `LineTo` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `gpio_edgeDetect` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* .-------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 316 instances
* *State Mutation (weighted view):* 990
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 218`, `args: 65`, `func_start: 58`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 358`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 31`
* *Architecture:* `api: 51`, `import: 9`
* *Defense:* `safety: 9`, `doc: 5`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Font8x16.h, assert.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stdint.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `myBlinker/rpi-SmartStart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.368)
- **Top Global Matches:** file_cluster_4: 5.368, file_cluster_15: 8.148, file_cluster_16: 8.262
- **Magnitude:** 1590.32 | **LOC:** 1605 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.0%), Debt Markers (formerly Tech Debt) (83.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 86.077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CvtBmpLine` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `PiConsole_Init` **(Many-Argument Workhorses)** (Impact: 39.3)
  * `set_Activity_LED` **(Compute Cores)** (Impact: 24.5)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `LineTo` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `gpio_edgeDetect` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* .-------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 316 instances
* *State Mutation (weighted view):* 990
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 218`, `args: 65`, `func_start: 58`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 358`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 30`
* *Architecture:* `api: 52`, `import: 9`
* *Defense:* `safety: 9`, `doc: 5`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Font8x16.h, assert.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stdint.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `GLES2_Model/rpi-SmartStart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.337)
- **Top Global Matches:** file_cluster_4: 6.337, file_cluster_15: 7.218, file_cluster_16: 7.444
- **Magnitude:** 1546.18 | **LOC:** 1603 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.5%), Debt Markers (formerly Tech Debt) (83.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 78.937% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CvtBmpLine` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `PiConsole_Init` **(Many-Argument Workhorses)** (Impact: 39.0)
  * `LineTo` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `gpio_edgeDetect` **(Compute Cores)** (Impact: 16.6)
    * *Intent:* .-------------------------------------------------------------------------*/
  * `set_Activity_LED` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* .--------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 309 instances
* *State Mutation (weighted view):* 961
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 222`, `args: 71`, `func_start: 55`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 343`, `dead_code: 1`, `planned_debt: 5`, `unreferenced_by_name: 28`
* *Architecture:* `api: 58`, `import: 11`
* *Defense:* `safety: 9`, `doc: 4`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Font8x16.h, assert.h, errno.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stdint.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Multicore/rpi-SmartStart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.461)
- **Top Global Matches:** file_cluster_4: 6.461, file_cluster_15: 7.259, file_cluster_16: 7.45
- **Magnitude:** 1545.36 | **LOC:** 1558 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.0%), Debt Markers (formerly Tech Debt) (83.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 73.735% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CvtBmpLine` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `PiConsole_Init` **(Many-Argument Workhorses)** (Impact: 39.0)
  * `LineTo` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `gpio_edgeDetect` **(Compute Cores)** (Impact: 16.6)
    * *Intent:* .-------------------------------------------------------------------------*/
  * `set_Activity_LED` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* .--------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 308 instances
* *State Mutation (weighted view):* 959
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 214`, `args: 64`, `func_start: 57`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 343`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 29`
* *Architecture:* `api: 50`, `import: 9`
* *Defense:* `safety: 9`, `doc: 5`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Font8x16.h, assert.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stdint.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `SD_FAT32/rpi-SmartStart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.181)
- **Top Global Matches:** file_cluster_4: 6.181, file_cluster_15: 7.555, file_cluster_16: 7.722
- **Magnitude:** 1410.82 | **LOC:** 1478 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (84.4%), Guard Balance (formerly Safety Score) (84.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 66.646% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CvtBmpLine` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `PiConsole_Init` **(Many-Argument Workhorses)** (Impact: 38.9)
  * `LineTo` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `gpio_edgeDetect` **(Compute Cores)** (Impact: 16.6)
    * *Intent:* .-------------------------------------------------------------------------*/
  * `set_Activity_LED` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* .--------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 283 instances
* *State Mutation (weighted view):* 868
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 213`, `args: 65`, `func_start: 50`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 302`, `dead_code: 1`, `planned_debt: 5`, `unreferenced_by_name: 26`
* *Architecture:* `api: 56`, `import: 10`
* *Defense:* `safety: 9`, `doc: 4`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Font8x16.h, assert.h, errno.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stdint.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `FreeRTOSv10.1.1/FreeRTOS/Source/queue.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.424)
- **Top Global Matches:** file_cluster_6: 6.424, file_cluster_4: 7.826, file_cluster_15: 15.446
- **Magnitude:** 1256.72 | **LOC:** 2942 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 4.045; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.9%), Debt Markers (formerly Tech Debt) (54.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xQueueGenericSend` **(Many-Argument Workhorses)** (Impact: 90.9)
    * *Intent:* #endif /* ( ( configUSE_COUNTING_SEMAPHORES == 1 ) && ( configSUPPORT_DYNAMIC_ALLOCATION == 1 ) ) */...
  * `xQueueGenericSendFromISR` **(Many-Argument Workhorses)** (Impact: 65.6)
    * *Intent:* /*-----------------------------------------------------------*/
  * `xQueueSemaphoreTake` **(Many-Argument Workhorses)** (Impact: 55.8)
    * *Intent:* /*-----------------------------------------------------------*/
  * `xQueuePeek` **(Many-Argument Workhorses)** (Impact: 51.4)
    * *Intent:* /*-----------------------------------------------------------*/
  * `xQueueReceive` **(Many-Argument Workhorses)** (Impact: 51.0)
    * *Intent:* /*-----------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 129 instances
* *State Mutation (weighted view):* 402
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 130`, `args: 59`, `func_start: 50`, `class_start: 6`
* *Risk/State:* `state_mutation: 144`, `planned_debt: 2`, `unreferenced_by_name: 33`
* *Architecture:* `api: 19`, `import: 6`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 105`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.045
  * `Choke Point (Betweenness):` 0.000527 | `Ripple Effect (Closeness):` 0.02243
  * `Imports (Out-Degree: 8):` FreeRTOS.h, croutine.h, queue.h, stdlib.h, string.h, task.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `GLES2_Rotate/rpi-SmartStart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.705)
- **Top Global Matches:** file_cluster_15: 6.705, file_cluster_16: 6.936, file_cluster_12: 7.384
- **Magnitude:** 1183.0 | **LOC:** 1363 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (88.2%), Guard Balance (formerly Safety Score) (81.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 88.27% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PiConsole_Init` **(Many-Argument Workhorses)** (Impact: 38.8)
  * `LineTo` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `gpio_edgeDetect` **(Compute Cores)** (Impact: 16.6)
    * *Intent:* .-------------------------------------------------------------------------*/
  * `set_Activity_LED` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `DiagLine16` **(Stateful Encapsulated Methods)** (Impact: 13.5)
    * *Intent:* .--------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 227 instances
* *State Mutation (weighted view):* 699
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 207`, `args: 64`, `func_start: 49`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 245`, `planned_debt: 5`, `unreferenced_by_name: 25`
* *Architecture:* `api: 55`, `import: 10`
* *Defense:* `safety: 9`, `doc: 4`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Font8x16.h, assert.h, errno.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stdint.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Multicore/emb-stdio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.958)
- **Top Global Matches:** file_cluster_8: 8.958, file_cluster_3: 16.104, file_cluster_6: 20.905
- **Magnitude:** 1171.3 | **LOC:** 872 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%)
- **Documentation Coverage:** 73.735% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vsscanf` **(Many-Argument Workhorses)** (Impact: 397.6)
    * *Intent:* {--------------------------------------------------------------------------*/
  * `emb_vsprintf` **(Many-Argument Workhorses)** (Impact: 114.5)
  * `number` **(Many-Argument Workhorses)** (Impact: 85.7)
  * `sscanf` **(Parameter Forwarders)** (Impact: 4.5)
    * *Intent:* {--------------------------------------------------------------------------*/
  * `checkdigit` **(Encapsulated Accessors)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 177 instances
* *State Mutation (weighted view):* 534
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 103`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 180`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 6`, `import: 10`
* *Defense:* `safety: 10`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ctype.h, emb-stdio.h, rpi-SmartStart.h, stdarg.h, stdbool.h, stddef.h, stdint.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `GLES2_Model/emb-stdio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.954)
- **Top Global Matches:** file_cluster_8: 8.954, file_cluster_3: 16.101, file_cluster_6: 20.903
- **Magnitude:** 1171.28 | **LOC:** 871 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.8%)
- **Documentation Coverage:** 78.937% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vsscanf` **(Many-Argument Workhorses)** (Impact: 397.6)
    * *Intent:* {--------------------------------------------------------------------------*/
  * `emb_vsprintf` **(Many-Argument Workhorses)** (Impact: 114.5)
  * `number` **(Many-Argument Workhorses)** (Impact: 85.7)
  * `sscanf` **(Parameter Forwarders)** (Impact: 4.5)
    * *Intent:* {--------------------------------------------------------------------------*/
  * `checkdigit` **(Encapsulated Accessors)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 177 instances
* *State Mutation (weighted view):* 534
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 103`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 180`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 6`, `import: 9`
* *Defense:* `safety: 10`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ctype.h, emb-stdio.h, rpi-smartstart.h, stdarg.h, stdbool.h, stdint.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `10_virtualmemory/windows.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.485)
- **Top Global Matches:** file_cluster_4: 6.485, file_cluster_12: 8.07, file_cluster_16: 8.637
- **Magnitude:** 1137.56 | **LOC:** 1056 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SelectObject` **(Many-Argument Workhorses)** (Impact: 44.7)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `PiConsole_Init` **(Many-Argument Workhorses)** (Impact: 39.6)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `Rectangle` **(Many-Argument Workhorses)** (Impact: 34.1)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `LineTo` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `TextOut` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* .--------------------------------------------------------------------------*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 213 instances
* *State Mutation (weighted view):* 674
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 96`, `args: 42`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 248`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Font8x16.h, rpi-smartstart.h, stdbool.h, stdint.h, windows.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `GLES2_Model/rpi-GLES.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.065)
- **Top Global Matches:** file_cluster_15: 7.065, file_cluster_4: 7.379, file_cluster_16: 7.722
- **Magnitude:** 939.86 | **LOC:** 1339 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 3.68; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.0%)
- **Documentation Coverage:** 78.937% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ParseWaveFrontMesh` **(Many-Argument Workhorses)** (Impact: 216.3)
    * *Intent:* #include <float.h>
  * `SetupRenderer` **(Many-Argument Workhorses)** (Impact: 22.8)
  * `CreateVertexData` **(Many-Argument Workhorses)** (Impact: 21.5)
  * `TransformPoint3D` **(Many-Argument Workhorses)** (Impact: 18.1)
    * *Intent:* {--------------------------------------------------------------------------*/
  * `DoRotate` **(Many-Argument Workhorses)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 149 instances
* *State Mutation (weighted view):* 508
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 142`, `args: 31`, `func_start: 30`, `class_start: 26`
* *Risk/State:* `state_mutation: 210`, `dead_code: 12`, `planned_debt: 1`, `unreferenced_by_name: 17`
* *Architecture:* `io: 10`, `api: 38`, `import: 9`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.68
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004673
  * `Imports (Out-Degree: 4):` SDCard.h, emb-stdio.h, float.h, math.h, rpi-GLES.h, rpi-smartstart.h, stdbool.h, stdint.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `arduino/wstring.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.031)
- **Top Global Matches:** file_cluster_15: 6.031, file_cluster_11: 8.182, file_cluster_16: 8.337
- **Magnitude:** 689.1 | **LOC:** 824 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 8.092; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.7%), Connectivity (formerly Api Exposure) (61.7%)
- **Documentation Coverage:** 77.1439% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `String::replace` **(Compute Cores)** (Impact: 28.1)
  * `ltoa` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* */ #include <stdint.h> #include <math.h> #include <stdio.h> #include "WString.h"
  * `String::lastIndexOf` **(Compute Cores)** (Impact: 16.2)
  * `ultoa` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `String::getBytes` **(Type Conversions)** (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 131`, `args: 93`, `func_start: 87`
* *Risk/State:* `state_mutation: 99`, `fragile_debt: 1`
* *Architecture:* `api: 37`, `import: 4`
* *Defense:* `doc: 20`, `immutability_locks: 75`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.092
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006231
  * `Imports (Out-Degree: 0):` WString.h, math.h, stdint.h, stdio.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `10_virtualmemory/emb-stdio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 4.758)
- **Top Global Matches:** file_cluster_4: 4.758, file_cluster_6: 9.703, file_cluster_15: 10.933
- **Magnitude:** 683.86 | **LOC:** 888 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 3.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.7%)
- **Documentation Coverage:** 32.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_doprnt` **(Many-Argument Workhorses)** (Impact: 199.2)
    * *Intent:* * @param fmt * Format string. * @param ap * Variable-length list of values that will be formatted. *...
  * `ulong_to_string` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* /*#define ALWAYS_USE_DIVISION*/ /** * Convert an unsigned long integer to a string. * * @param num *...
  * `printf` **(Compute Cores)** (Impact: 6.1)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `vprintf` **(Compute Cores)** (Impact: 5.9)
    * *Intent:* .--------------------------------------------------------------------------*/
  * `blockprn_to_buf` **(Stateful Encapsulated Methods)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 131 instances
* *State Mutation (weighted view):* 400
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 53`, `args: 12`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 138`, `unreferenced_by_name: 7`
* *Architecture:* `api: 9`, `import: 7`
* *Defense:* `safety: 4`, `doc: 9`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` emb-stdio.h, limits.h, stdarg.h, stdbool.h, stddef.h, stdint.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `10_virtualmemory/mmu.c` (C) | Magnitude: 89.38 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 96, state_mutation: 30, macros: 18, pointers: 14
- `GLES2/Makefile` (MAKEFILE) | Magnitude: 37.8 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 34, design_upper_case: 34, func_start: 26, indent_tabs: 17
- `GLES2_Model/Makefile` (MAKEFILE) | Magnitude: 37.8 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 34, design_upper_case: 34, func_start: 26, indent_tabs: 17
- `GL_GUI_STEP1/Makefile` (MAKEFILE) | Magnitude: 37.8 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 34, design_upper_case: 34, func_start: 26, indent_tabs: 17
- `myBlinker/Makefile` (MAKEFILE) | Magnitude: 37.8 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 34, design_upper_case: 34, func_start: 26, indent_tabs: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `PlayGround/Makefile` (MAKEFILE) | Magnitude: 24.6 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 27, design_upper_case: 26, structural_boundaries: 20, func_start: 17
- `SimpleSched/Makefile` (MAKEFILE) | Magnitude: 26.1 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: func_start: 18, core_var_decl: 18, design_upper_case: 17, structural_boundaries: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `Arm32_64_USB/main.c` (C) | Magnitude: 28.72 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 41, branch: 9, structural_boundaries: 9, debug_prints: 9

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `FreeRTOSv10.1.1/FreeRTOS/Source/tasks.c` -> **Severity: 0.194** (Bridge: 0.0019 * Flux: 99.9809%)
- `FreeRTOSv10.1.1/FreeRTOS/Source/timers.c` -> **Severity: 0.083** (Bridge: 0.0008 * Flux: 99.0713%)
- `FreeRTOSv10.1.1/FreeRTOS/Source/queue.c` -> **Severity: 0.052** (Bridge: 0.0005 * Flux: 99.2722%)
- `FreeRTOSv10.1.1/FreeRTOS/Source/portable/GCC/RaspberryPi/port.c` -> **Severity: 0.051** (Bridge: 0.0005 * Flux: 100.0%)
- `RayCast/rpi-BasicHardware.c` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `FreeRTOSv10.1.1/FreeRTOS/Source/tasks.c` -> **Severity: 3.591** (Embedded: 0.0561 * Error Risk: 64.0356%)
- `FreeRTOSv10.1.1/FreeRTOS/Source/portable/GCC/RaspberryPi/port.c` -> **Severity: 2.675** (Embedded: 0.0354 * Error Risk: 75.5424%)
- `FreeRTOSv10.1.1/FreeRTOS/Source/list.c` -> **Severity: 2.643** (Embedded: 0.0376 * Error Risk: 70.2706%)
- `FreeRTOSv10.1.1/FreeRTOS/Source/timers.c` -> **Severity: 1.836** (Embedded: 0.0306 * Error Risk: 60.0132%)
- `FreeRTOSv10.1.1/FreeRTOS/Source/include/stack_macros.h` -> **Severity: 1.599** (Embedded: 0.0316 * Error Risk: 50.6097%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `FreeRTOSv10.1.1/FreeRTOS/Source/tasks.c` -> **Severity: 1148.9** (Blast Radius: 11.489 * Doc Risk: 100.0%)
- `RayCast/rpi-BasicHardware.c` -> **Severity: 882.4** (Blast Radius: 8.824 * Doc Risk: 100.0%)
- `FreeRTOSv10.1.1/FreeRTOS/Source/list.c` -> **Severity: 643.1** (Blast Radius: 6.431 * Doc Risk: 100.0%)
- `FreeRTOSv10.1.1/FreeRTOS/Source/portable/GCC/RaspberryPi/port.c` -> **Severity: 635.8** (Blast Radius: 6.358 * Doc Risk: 100.0%)
- `arduino/wstring.cpp` -> **Severity: 624.248** (Blast Radius: 8.092 * Doc Risk: 77.1439%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3424 call pairs -- scoped 24.7%, unique 9.2%, ambiguous 18.2%, external 47.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 3215 | 23.9% | 9.8% | 17.9% | 48.5% |
| cpp | 203 | 38.9% | 0.5% | 23.2% | 37.4% |
| makefile | 6 | 0.0% | 0.0% | 0.0% | 100.0% |

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
