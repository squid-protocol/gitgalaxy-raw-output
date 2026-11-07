# ARCHITECTURAL_BRIEF: raspberrypi
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dwelch67/raspberrypi.git` |
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
- **Scope:** 557 analyzed artifact(s), 36012 LOC.
- **Load-bearing artifact:** `twain/zutil.h` -- 7 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `jtagproxy/ft232rl/parport.c` -- pulls in 12 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tas/tas.c` at magnitude 4047.12 (structural weight, not risk).
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
| Total Artifacts | 930 |
| Analyzed Artifacts (Scanned) | 557 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 373 |
| Total LOC | 36012 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 59.9% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7747 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.073 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3713 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 19 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 217 | 27542 | 39.0% |
| MARKDOWN | 118 | 0 | 21.2% |
| ASSEMBLY | 116 | 5044 | 20.8% |
| MAKEFILE | 99 | 3426 | 17.8% |
| PLAINTEXT | 7 | 0 | 1.3% |

## 4.1 SOURCE ENCODINGS
All 557 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 31%, Data / Markup / Trivial 26%, Parameter Forwarders Files 21%, Interface Declarations Files 8%, Large Core Modules (3) 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 432 | 77.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 125 | 22.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 373*

**Composition by Extension & Reason:**
- `no_extension`: 107x Unsupported Format (.undeterminable), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.o`: 58x Excluded (Explicitly Denied Extension: '.o')
- `.h`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Embedded Hex Payload: 4352 hex tokens in 2822 LOC), 2x Excluded (Embedded Hex Payload: 4402 hex tokens in 2906 LOC)
- `.elf`: 28x Excluded (Unsupported Extension: '.elf')
- `.list`: 28x Excluded (Unsupported Extension: '.list')
- `.hex`: 26x Excluded (Unsupported Extension: '.hex')
- `.c`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 20x Excluded (Unsupported Extension: '.cfg')
- `.img`: 15x Excluded (Unsupported Extension: '.img')
- `.bin`: 14x Excluded (Unsupported Extension: '.bin')
- `.s`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Statistical Anomaly (Z-Score: -5.26 < -4.55), 1x Excluded (Monolithic Amalgamation: 1048579 LOC exceeds the 150000 LOC backstop)
- `.ps`: 6x Excluded (Unsupported Extension: '.ps')
- `.bc`: 2x Excluded (Unsupported Extension: '.bc')
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.a`: 1x Excluded (Explicitly Denied Extension: '.a')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.1 | 21.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.3 | 28.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 45.5 | 37.8 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 8.7 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 77.8 | 10.8 | 8.2 | 8.2 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 39.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.9 | 6.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 91.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 44 | 12 | 0 | `twain/deflate.c` |
| cleanup | 745 | 107 | 8 | `spi01/Makefile` |
| guards | 329 | 36 | 0 | `twain/zlib.h` |
| danger | 61 | 15 | 0 | `twain/deflate.c` |
| concurrency | 60 | 10 | 0 | `boards/pi2/SVC/blinker01/vectors.s` |
| connectivity | 3044 | 416 | 15 | `twain/zlib.h` |
| io | 192 | 109 | 2 | `tas/tas.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 51 | 12 | 0 | `boards/piaplus/mmu/novectors.s` |
| tests | 0 | 0 | 0 | - |
| docs | 37 | 12 | 0 | `twain/inflate.c` |
| debt | 287 | 14 | 0 | `tas/tas.c` |
| mutation | 8433 | 280 | 26 | `tas/tas.c` |
| dead_code | 1735 | 322 | 8 | `tas/tas.c` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 538 | 86 | 1 | `twain/Makefile` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tas/tas.c` (Hits: 7)
- `spi01/blinker02.s` (Hits: 6)
- `bootloader07/Makefile` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **zutil.h** (`twain/zutil.h`) — 7 inbound connections
2. **zlib.h** (`twain/zlib.h`) — 5 inbound connections
3. **inftrees.h** (`twain/inftrees.h`) — 3 inbound connections
4. **BCM2835.h** (`bootloader07/BCM2835.h`) — 2 inbound connections
5. **BCM2836.h** (`bootloader07/BCM2836.h`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **parport.c** (`jtagproxy/ft232rl/parport.c`) — 12 outbound dependencies
2. **parport_fast.c** (`jtagproxy/ft232rl/parport_fast.c`) — 12 outbound dependencies
3. **parport.c** (`jtagproxy/msplaunchpad/parport.c`) — 11 outbound dependencies
4. **syscalls.c** (`newlib0/syscalls.c`) — 10 outbound dependencies
5. **ser.c** (`bootloader01/ser.c`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `assemble` **(Many-Argument Workhorses)** (@ `tas/tas.c`) -> Impact: **762.1** | LOC: 1722
  * *Intent:* //-------------------------------------------------------------------
- `inflate` **(Many-Argument Workhorses)** (@ `twain/inflate.c`) -> Impact: **390.9** | LOC: 648
  * *Intent:* */
- `dissassemble` **(Many-Argument Workhorses)** (@ `tas/tas.c`) -> Impact: **295.9** | LOC: 597
  * *Intent:* //-------------------------------------------------------------------
- `deflate` **(Many-Argument Workhorses)** (@ `twain/deflate.c`) -> Impact: **206.1** | LOC: 312
  * *Intent:* /* ========================================================================= */
- `inflate_table` **(Many-Argument Workhorses)** (@ `twain/inftrees.c`) -> Impact: **140.7** | LOC: 275
  * *Intent:* */
- `_tr_flush_block` **(Many-Argument Workhorses)** (@ `twain/trees.c`) -> Impact: **125.5** | LOC: 318
  * *Intent:* /* =========================================================================== * Determine the best encoding for the current block: dynamic trees, sta...
- `inflate_fast` **(Many-Argument Workhorses)** (@ `twain/inffast.c`) -> Impact: **120.2** | LOC: 257
  * *Intent:* */
- `main` **(Many-Argument Workhorses)** (@ `tas/tas.c`) -> Impact: **95.3** | LOC: 278
  * *Intent:* //-------------------------------------------------------------------
- `deflateInit2_` **(Many-Argument Workhorses)** (@ `twain/deflate.c`) -> Impact: **86.4** | LOC: 108
  * *Intent:* /* ========================================================================= */
- `longest_match` **(Many-Argument Workhorses)** (@ `twain/deflate.c`) -> Impact: **66.0** | LOC: 142
  * *Intent:* #ifndef FASTEST /* =========================================================================== * Set match_start to the longest match starting at the ...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `twain` | 27 | 7126.64 | 32.56% | 22.59% |
| `tas` | 7 | 4102.2 | 20.95% | 29.02% |
| `bootloader01` | 9 | 822.8 | 27.4% | 40.01% |
| `boards/pizero/float02` | 7 | 775.52 | 26.49% | 30.78% |
| `float02` | 7 | 775.16 | 26.47% | 30.85% |
| `boards/piaplus/float02` | 7 | 771.42 | 26.47% | 30.11% |
| `bootloader07` | 11 | 692.58 | 28.77% | 36.17% |
| `spi01` | 8 | 547.38 | 18.46% | 29.95% |
| `boards/pizero/asmdelay` | 5 | 518.06 | 25.3% | 42.05% |
| `boards/pi2/bootloader07` | 5 | 405.84 | 24.85% | 42.11% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `atags/vectors.s` -> **100.0%** Exposure
- `boards/pi1/bootloader07/vectors.s` -> **100.0%** Exposure
- `boards/pi2/bootloader07/vectors.s` -> **100.0%** Exposure
- `boards/pi3/aarch32/bootloader07/vectors.s` -> **100.0%** Exposure
- `boards/pi3/imgtest/bs32.s` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `armjtag/armjtag.c` -> **100.0%** Exposure
- `armjtag/rpi2/armjtag.c` -> **100.0%** Exposure
- `bench02/uart.c` -> **100.0%** Exposure
- `blinker07/blinker07.c` -> **100.0%** Exposure
- `blinker08/blinker08.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `boards/pizero/asmdelay/start.s` -> **16** Orphaned Functions | **0** Duplicates
- `bench02/novectors.s` -> **15** Orphaned Functions | **0** Duplicates
- `boards/pi2/SVC_BOOT/uart01/vectors.s` -> **14** Orphaned Functions | **0** Duplicates
- `boards/pi2/SVC_BOOT/uart02/vectors.s` -> **14** Orphaned Functions | **0** Duplicates
- `boards/pi2/bootloader07/vectors.s` -> **11** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `86` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `133` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tas/tas.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.682)
- **Top Global Matches:** file_cluster_8: 5.682, file_cluster_6: 14.974, file_cluster_3: 22.111
- **Magnitude:** 4047.12 | **LOC:** 2936 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.635; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.1%), Guard Balance (formerly Safety Score) (89.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assemble` **(Many-Argument Workhorses)** (Impact: 762.1)
    * *Intent:* //-------------------------------------------------------------------
  * `dissassemble` **(Many-Argument Workhorses)** (Impact: 295.9)
    * *Intent:* //-------------------------------------------------------------------
  * `main` **(Many-Argument Workhorses)** (Impact: 95.3)
    * *Intent:* //-------------------------------------------------------------------
  * `parse_immed` **(Compute Cores)** (Impact: 32.4)
    * *Intent:* //-------------------------------------------------------------------
  * `parse_low_reg` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* //-------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 885 instances
* *State Mutation (weighted view):* 2700
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 727`, `structural_boundaries: 495`, `args: 14`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 930`, `dead_code: 95`, `unreferenced_by_name: 2`
* *Architecture:* `io: 7`, `api: 13`, `import: 3`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `twain/deflate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.438)
- **Top Global Matches:** file_cluster_8: 6.438, file_cluster_6: 17.21, file_cluster_3: 19.763
- **Magnitude:** 1971.24 | **LOC:** 1966 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 2.535; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deflate` **(Many-Argument Workhorses)** (Impact: 206.1)
    * *Intent:* /* ========================================================================= */
  * `deflateInit2_` **(Many-Argument Workhorses)** (Impact: 86.4)
    * *Intent:* /* ========================================================================= */
  * `longest_match` **(Many-Argument Workhorses)** (Impact: 66.0)
    * *Intent:* #ifndef FASTEST /* =========================================================================== * Set...
  * `deflate_slow` **(Many-Argument Workhorses)** (Impact: 56.4)
    * *Intent:* #ifndef FASTEST /* =========================================================================== * Sam...
  * `deflate_rle` **(Compute Cores)** (Impact: 50.2)
    * *Intent:* #endif /* FASTEST */ /* =========================================================================== ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 329 instances
* *State Mutation (weighted view):* 1047
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 400`, `structural_boundaries: 107`, `args: 5`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 389`, `dead_code: 3`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 43`, `import: 1`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.535
  * `Choke Point (Betweenness):` 0.000112 | `Ripple Effect (Closeness):` 0.002982
  * `Imports (Out-Degree: 5):` deflate.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `twain/inflate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.708)
- **Top Global Matches:** file_cluster_4: 6.708, file_cluster_9: 8.726, file_cluster_15: 10.236
- **Magnitude:** 1656.8 | **LOC:** 1497 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 2.535; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.8%), Guard Balance (formerly Safety Score) (85.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inflate` **(Many-Argument Workhorses)** (Impact: 390.9)
    * *Intent:* */
  * `inflateCopy` **(Compute Cores)** (Impact: 23.1)
  * `inflateInit2_` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `updatewindow` **(Many-Argument Workhorses)** (Impact: 21.5)
    * *Intent:* */
  * `inflateReset2` **(Compute Cores)** (Impact: 20.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 315 instances
* *State Mutation (weighted view):* 1001
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 305`, `structural_boundaries: 142`, `args: 5`, `func_start: 19`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 371`, `dead_code: 11`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `doc: 12`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.535
  * `Choke Point (Betweenness):` 0.000154 | `Ripple Effect (Closeness):` 0.002982
  * `Imports (Out-Degree: 10):` inffast.h, inffixed.h, inflate.h, inftrees.h, zutil.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `twain/trees.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.319)
- **Top Global Matches:** file_cluster_6: 7.319, file_cluster_4: 7.508, file_cluster_12: 14.758
- **Magnitude:** 1203.2 | **LOC:** 1225 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 2.066; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_tr_flush_block` **(Many-Argument Workhorses)** (Impact: 125.5)
    * *Intent:* /* =========================================================================== * Determine the best ...
  * `send_tree` **(Many-Argument Workhorses)** (Impact: 42.3)
    * *Intent:* /* =========================================================================== * Send a literal or d...
  * `scan_tree` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* /* =========================================================================== * Scan a literal or d...
  * `gen_bitlen` **(Many-Argument Workhorses)** (Impact: 29.9)
    * *Intent:* /* =========================================================================== * Compute the optimal...
  * `build_tree` **(Many-Argument Workhorses)** (Impact: 24.9)
    * *Intent:* /* =========================================================================== * Construct one Huffm...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 227 instances
* *State Mutation (weighted view):* 710
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 55`, `args: 4`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 256`, `dead_code: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 43`, `import: 3`
* *Defense:* `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.066
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.003067
  * `Imports (Out-Degree: 2):` deflate.h, stdio.h, trees.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `boards/piaplus/float02/slowfloat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.891)
- **Top Global Matches:** file_cluster_6: 6.891, file_cluster_4: 8.704, file_cluster_16: 15.475
- **Magnitude:** 526.92 | **LOC:** 665 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 2.329; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.6%), Guard Balance (formerly Safety Score) (76.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `floatXAdd` **(Compute Cores)** (Impact: 52.0)
  * `floatXToFloat32` **(Compute Cores)** (Impact: 45.0)
  * `roundFloatXTo24` **(Stateful Encapsulated Methods)** (Impact: 25.9)
    * *Intent:* //static flag le64( bits64X a, bits64X b ) //{ //return ( a.a0 < b.a0 ) || ( ( a.a0 == b.a0 ) && ( a...
  * `roundFloatXTo53` **(Stateful Encapsulated Methods)** (Impact: 25.9)
  * `floatXToInt32` **(Stateful Encapsulated Methods)** (Impact: 21.6)
    * *Intent:* //ax.isZero = TRUE; //return ax; //} //ax.isZero = FALSE; //ax.sig = shortShift64Left( ax.sig, 23 );...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 287
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 64`, `args: 15`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `state_mutation: 107`, `dead_code: 16`
* *Architecture:* `api: 22`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001789
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `boards/pizero/float02/slowfloat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.891)
- **Top Global Matches:** file_cluster_6: 6.891, file_cluster_4: 8.704, file_cluster_16: 15.475
- **Magnitude:** 526.92 | **LOC:** 665 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 2.329; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.6%), Guard Balance (formerly Safety Score) (76.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `floatXAdd` **(Compute Cores)** (Impact: 52.0)
  * `floatXToFloat32` **(Compute Cores)** (Impact: 45.0)
  * `roundFloatXTo24` **(Stateful Encapsulated Methods)** (Impact: 25.9)
    * *Intent:* //static flag le64( bits64X a, bits64X b ) //{ //return ( a.a0 < b.a0 ) || ( ( a.a0 == b.a0 ) && ( a...
  * `roundFloatXTo53` **(Stateful Encapsulated Methods)** (Impact: 25.9)
  * `floatXToInt32` **(Stateful Encapsulated Methods)** (Impact: 21.6)
    * *Intent:* //ax.isZero = TRUE; //return ax; //} //ax.isZero = FALSE; //ax.sig = shortShift64Left( ax.sig, 23 );...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 287
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 64`, `args: 15`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `state_mutation: 107`, `dead_code: 16`
* *Architecture:* `api: 22`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001789
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `float02/slowfloat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.891)
- **Top Global Matches:** file_cluster_6: 6.891, file_cluster_4: 8.704, file_cluster_16: 15.475
- **Magnitude:** 526.92 | **LOC:** 665 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 2.329; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.6%), Guard Balance (formerly Safety Score) (76.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `floatXAdd` **(Compute Cores)** (Impact: 52.0)
  * `floatXToFloat32` **(Compute Cores)** (Impact: 45.0)
  * `roundFloatXTo24` **(Stateful Encapsulated Methods)** (Impact: 25.9)
    * *Intent:* //static flag le64( bits64X a, bits64X b ) //{ //return ( a.a0 < b.a0 ) || ( ( a.a0 == b.a0 ) && ( a...
  * `roundFloatXTo53` **(Stateful Encapsulated Methods)** (Impact: 25.9)
  * `floatXToInt32` **(Stateful Encapsulated Methods)** (Impact: 21.6)
    * *Intent:* //ax.isZero = TRUE; //return ax; //} //ax.isZero = FALSE; //ax.sig = shortShift64Left( ax.sig, 23 );...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 287
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 64`, `args: 15`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `state_mutation: 107`, `dead_code: 16`
* *Architecture:* `api: 22`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.329
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001789
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `twain/inftrees.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 4.812)
- **Top Global Matches:** file_cluster_1: 4.812, file_cluster_3: 48.134, file_cluster_8: 69.991
- **Magnitude:** 388.22 | **LOC:** 307 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.85; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inflate_table` **(Many-Argument Workhorses)** (Impact: 140.7)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 12`, `func_start: 1`
* *Risk/State:* `state_mutation: 85`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.85
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003067
  * `Imports (Out-Degree: 2):` inftrees.h, zutil.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `twain/crc32.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.219)
- **Top Global Matches:** file_cluster_15: 7.219, file_cluster_9: 7.647, file_cluster_16: 8.48
- **Magnitude:** 387.3 | **LOC:** 426 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 2.281; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `crc32` **(Many-Argument Workhorses)** (Impact: 21.6)
    * *Intent:* /* ========================================================================= */ #define DO1 crc = cr...
  * `crc32_combine_` **(Many-Argument Workhorses)** (Impact: 18.7)
    * *Intent:* /* ========================================================================= */
  * `crc32_big` **(Many-Argument Workhorses)** (Impact: 17.7)
    * *Intent:* #define DOBIG32 DOBIG4; DOBIG4; DOBIG4; DOBIG4; DOBIG4; DOBIG4; DOBIG4; DOBIG4 /* ==================...
  * `crc32_little` **(Many-Argument Workhorses)** (Impact: 17.6)
    * *Intent:* #define DOLIT32 DOLIT4; DOLIT4; DOLIT4; DOLIT4; DOLIT4; DOLIT4; DOLIT4; DOLIT4 /* ==================...
  * `make_crc_table` **(I/O & Config Routines)** (Impact: 15.8)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 249
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 24`, `args: 2`, `func_start: 11`
* *Risk/State:* `state_mutation: 83`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 15`, `import: 3`
* *Defense:* `immutability_locks: 19`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.281
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.004954
  * `Imports (Out-Degree: 2):` crc32.h, stdio.h, zutil.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `twain/inffast.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 4.43)
- **Top Global Matches:** file_cluster_1: 4.43, file_cluster_3: 48.109, file_cluster_8: 69.98
- **Magnitude:** 380.32 | **LOC:** 340 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 1.85; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inflate_fast` **(Many-Argument Workhorses)** (Impact: 120.2)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 11`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 98`, `dead_code: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.85
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003067
  * `Imports (Out-Degree: 4):` inffast.h, inflate.h, inftrees.h, zutil.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bootloader01/prograspi.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.142)
- **Top Global Matches:** file_cluster_8: 9.142, file_cluster_6: 11.526, file_cluster_4: 19.503
- **Magnitude:** 376.96 | **LOC:** 331 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.635; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.1%), Test Surface (formerly Verification) (80.0%), Dead Code Surface (formerly Dead Code) (79.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readhex` **(Compute Cores)** (Impact: 36.5)
    * *Intent:* //-----------------------------------------------------------------------------
  * `main` **(Many-Argument Workhorses)** (Impact: 15.5)
    * *Intent:* //-----------------------------------------------------------------------------
  * `raspload` **(Many-Argument Workhorses)** (Impact: 13.4)
    * *Intent:* //-----------------------------------------------------------------------------
  * `check_packet` **(Compute Cores)** (Impact: 8.9)
    * *Intent:* //-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 294
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 29`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 110`, `dead_code: 16`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 4`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ser.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gps_clock/notmain.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.021)
- **Top Global Matches:** file_cluster_4: 7.021, file_cluster_15: 10.402, file_cluster_11: 11.382
- **Magnitude:** 353.88 | **LOC:** 494 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.635; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Dead Code Surface (formerly Dead Code) (98.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_nmea` **(I/O & Config Routines)** (Impact: 42.4)
    * *Intent:* //------------------------------------------------------------------------
  * `show_time` **(I/O & Config Routines)** (Impact: 12.9)
    * *Intent:* //rc=0; //for(ra=0;ra<11;ra++) //{ //if(s[ra]==0) break; //for(rb=0;rb<8;rb++) //{ //rd=s[ra]; //spi...
  * `hexstrings` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* //------------------------------------------------------------------------
  * `spi_one_byte` **(Compute Cores)** (Impact: 7.7)
    * *Intent:* //------------------------------------------------------------------------
  * `notmain` **(I/O & Config Routines)** (Impact: 6.9)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 70 instances
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 34`, `args: 54`, `func_start: 12`
* *Risk/State:* `state_mutation: 94`, `dead_code: 39`, `unreferenced_by_name: 1`
* *Architecture:* `api: 15`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fontdata.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spi03/spi03.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.029)
- **Top Global Matches:** file_cluster_4: 7.029, file_cluster_6: 10.439, file_cluster_15: 11.445
- **Magnitude:** 352.12 | **LOC:** 394 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.635; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.1%), Guard Balance (formerly Safety Score) (82.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `notmain` **(I/O & Config Routines)** (Impact: 46.0)
    * *Intent:* //------------------------------------------------------------------------
  * `show_string` **(Compute Cores)** (Impact: 9.8)
    * *Intent:* //------------------------------------------------------------------------
  * `hexstrings` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* //------------------------------------------------------------------------
  * `spi_one_byte` **(Compute Cores)** (Impact: 7.7)
    * *Intent:* //------------------------------------------------------------------------
  * `uart_putc` **(Compute Cores)** (Impact: 4.6)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 245
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 21`, `args: 50`, `func_start: 10`
* *Risk/State:* `state_mutation: 93`, `dead_code: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 13`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fontdata.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pizero/asmdelay/asmdelay.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.759)
- **Top Global Matches:** file_cluster_3: 6.759, file_cluster_8: 20.531, file_cluster_6: 33.372
- **Magnitude:** 344.74 | **LOC:** 290 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_it` **(Compute Cores)** (Impact: 51.7)
  * `notmain` **(I/O & Config Routines)** (Impact: 8.3)
    * *Intent:* //-------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 21`, `args: 47`, `func_start: 2`
* *Risk/State:* `state_mutation: 90`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spi01/spi01.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.859)
- **Top Global Matches:** file_cluster_15: 5.859, file_cluster_16: 7.704, file_cluster_2: 7.811
- **Magnitude:** 310.54 | **LOC:** 338 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.635; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pdi_command` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* //------------------------------------------------------------------------
  * `prog_avr` **(I/O & Config Routines)** (Impact: 17.8)
    * *Intent:* //------------------------------------------------------------------------
  * `hexstrings` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* //------------------------------------------------------------------------
  * `uart_putc` **(Compute Cores)** (Impact: 4.6)
    * *Intent:* //------------------------------------------------------------------------
  * `uart_init` **(I/O & Config Routines)** (Impact: 4.5)
    * *Intent:* #define AUX_SPI0_CLK 0x20204008 #define AUX_SPI0_DLEN 0x2020400C #define AUX_SPI0_LTOH 0x20204010 #d...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 232
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 26`, `args: 56`, `func_start: 8`
* *Risk/State:* `state_mutation: 90`, `dead_code: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 11`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` blinker.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/piaplus/swd/swd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.843)
- **Top Global Matches:** file_cluster_4: 5.843, file_cluster_16: 9.711, file_cluster_6: 10.832
- **Magnitude:** 277.44 | **LOC:** 396 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `swd_write` **(Many-Argument Workhorses)** (Impact: 25.9)
    * *Intent:* //-------------------------------------------------------------------
  * `notmain` **(Compute Cores)** (Impact: 25.9)
    * *Intent:* #define DPW_CTRL 0x8D //1 00 10 1 01 #define DPW_SELECT 0x95 #define DP_SELECT_IDR 0xFC0000F0 #defin...
  * `swd_read` **(Many-Argument Workhorses)** (Impact: 24.2)
    * *Intent:* //-------------------------------------------------------------------
  * `swd_delay` **(Encapsulated Accessors)** (Impact: 3.5)
    * *Intent:* #define GPFSEL0 0x20200000 #define GPSET0 0x2020001C #define GPCLR0 0x20200028 #define GPLEV0 0x2020...
  * `sda_read` **(Encapsulated Accessors)** (Impact: 1.4)
    * *Intent:* //-------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 63`, `args: 63`, `func_start: 12`
* *Risk/State:* `state_mutation: 60`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 22`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bootloader01/bootloader01.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.97)
- **Top Global Matches:** file_cluster_15: 5.97, file_cluster_11: 7.171, file_cluster_16: 7.911
- **Magnitude:** 270.82 | **LOC:** 271 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.5%), Complexity Load (formerly Cognitive Load) (63.6%), Debt Markers (formerly Tech Debt) (11.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `notmain` **(I/O & Config Routines)** (Impact: 17.0)
    * *Intent:* //------------------------------------------------------------------------
  * `recv_packet` **(I/O & Config Routines)** (Impact: 9.8)
    * *Intent:* //------------------------------------------------------------------------
  * `hexstrings` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* //------------------------------------------------------------------------
  * `send_result` **(Compute Cores)** (Impact: 5.4)
    * *Intent:* //------------------------------------------------------------------------
  * `uart_send` **(Compute Cores)** (Impact: 4.6)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 60 instances
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 27`, `args: 30`, `func_start: 7`
* *Risk/State:* `state_mutation: 85`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pi2/bootloader07/bootloader07.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.998)
- **Top Global Matches:** file_cluster_1: 5.998, file_cluster_3: 48.28, file_cluster_8: 70.091
- **Magnitude:** 261.8 | **LOC:** 245 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `notmain` **(I/O & Config Routines)** (Impact: 53.6)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 44`, `args: 26`, `func_start: 1`
* *Risk/State:* `state_mutation: 63`, `unreferenced_by_name: 1`
* *Architecture:* `api: 23`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pi3/aarch32/bootloader07/bootloader07.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.998)
- **Top Global Matches:** file_cluster_1: 5.998, file_cluster_3: 48.28, file_cluster_8: 70.091
- **Magnitude:** 261.8 | **LOC:** 245 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `notmain` **(I/O & Config Routines)** (Impact: 53.6)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 44`, `args: 26`, `func_start: 1`
* *Risk/State:* `state_mutation: 63`, `unreferenced_by_name: 1`
* *Architecture:* `api: 23`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spi02/spi02.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.33)
- **Top Global Matches:** file_cluster_15: 5.33, file_cluster_11: 6.9, file_cluster_17: 7.57
- **Magnitude:** 243.06 | **LOC:** 356 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.635; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%), Complexity Load (formerly Cognitive Load) (60.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `notmain` **(I/O & Config Routines)** (Impact: 9.9)
    * *Intent:* //------------------------------------------------------------------------
  * `show_text_hex` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* //------------------------------------------------------------------------
  * `hexstrings` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* //------------------------------------------------------------------------
  * `spi_one_byte` **(Compute Cores)** (Impact: 7.7)
    * *Intent:* //------------------------------------------------------------------------
  * `show_text` **(Compute Cores)** (Impact: 5.8)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 25`, `args: 70`, `func_start: 15`
* *Risk/State:* `state_mutation: 64`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 18`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fontdata.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/piaplus/bootloader07/bootloader07.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.973)
- **Top Global Matches:** file_cluster_1: 5.973, file_cluster_3: 48.277, file_cluster_8: 70.089
- **Magnitude:** 238.08 | **LOC:** 233 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `notmain` **(I/O & Config Routines)** (Impact: 52.1)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 42`, `args: 22`, `func_start: 1`
* *Risk/State:* `state_mutation: 55`, `unreferenced_by_name: 1`
* *Architecture:* `api: 21`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pizero/bootloader07/bootloader07.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.973)
- **Top Global Matches:** file_cluster_1: 5.973, file_cluster_3: 48.277, file_cluster_8: 70.089
- **Magnitude:** 238.08 | **LOC:** 233 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `notmain` **(I/O & Config Routines)** (Impact: 52.1)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 42`, `args: 22`, `func_start: 1`
* *Risk/State:* `state_mutation: 55`, `unreferenced_by_name: 1`
* *Architecture:* `api: 21`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pi1/bootloader07/bootloader07.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.963)
- **Top Global Matches:** file_cluster_1: 5.963, file_cluster_3: 48.276, file_cluster_8: 70.089
- **Magnitude:** 236.94 | **LOC:** 230 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `notmain` **(I/O & Config Routines)** (Impact: 52.0)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 40`, `args: 21`, `func_start: 1`
* *Risk/State:* `state_mutation: 55`, `unreferenced_by_name: 1`
* *Architecture:* `api: 20`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bootloader07/bootloader07.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.963)
- **Top Global Matches:** file_cluster_1: 5.963, file_cluster_3: 48.276, file_cluster_8: 70.089
- **Magnitude:** 236.94 | **LOC:** 230 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `notmain` **(I/O & Config Routines)** (Impact: 52.0)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 40`, `args: 21`, `func_start: 1`
* *Risk/State:* `state_mutation: 55`, `unreferenced_by_name: 1`
* *Architecture:* `api: 20`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pi3/aarch64/bootloader07/bootloader07.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.945)
- **Top Global Matches:** file_cluster_1: 5.945, file_cluster_3: 48.274, file_cluster_8: 70.088
- **Magnitude:** 234.9 | **LOC:** 227 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `notmain` **(I/O & Config Routines)** (Impact: 52.0)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 38`, `args: 19`, `func_start: 1`
* *Risk/State:* `state_mutation: 55`, `unreferenced_by_name: 1`
* *Architecture:* `api: 18`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `boards/pi3/aarch64/uart02/uart02.c` (C) | Magnitude: 89.94 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 65, args: 33, structural_boundaries: 21, macros: 17
- `boards/pi3/imgtest/bs32.s` (ASSEMBLY) | Magnitude: 25.44 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: args: 18, structural_boundaries: 15, indent_spaces: 15, func_start: 9
- `atags/vectors.s` (ASSEMBLY) | Magnitude: 25.32 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: args: 18, structural_boundaries: 15, indent_spaces: 14, func_start: 9
- `bootloader04/vectors.s` (ASSEMBLY) | Magnitude: 25.32 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: args: 18, structural_boundaries: 15, indent_spaces: 14, func_start: 9
- `boards/pi2/SVC/blinker05/vectors.s` (ASSEMBLY) | Magnitude: 34.04 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: args: 96, indent_spaces: 64, structural_boundaries: 31, func_start: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `boards/pi3/aarch64/uart04/vectors.s` (ASSEMBLY) | Magnitude: 44.98 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 47, args: 41, structural_boundaries: 37, func_start: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `boards/piaplus/mmu/novectors.s` (ASSEMBLY) | Magnitude: 47.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: args: 107, indent_spaces: 83, structural_boundaries: 60, func_start: 18
- `boards/pizero/mmu/novectors.s` (ASSEMBLY) | Magnitude: 47.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: args: 107, indent_spaces: 83, structural_boundaries: 60, func_start: 18
- `mmu/novectors.s` (ASSEMBLY) | Magnitude: 47.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: args: 107, indent_spaces: 83, structural_boundaries: 60, func_start: 18
- `boards/pi3/aarch32/SVC/uart05/start.s` (ASSEMBLY) | Magnitude: 41.04 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: args: 73, indent_spaces: 57, structural_boundaries: 28, func_start: 13
- `blinker08/vectors.s` (ASSEMBLY) | Magnitude: 37.86 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: args: 84, indent_spaces: 44, structural_boundaries: 34, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `boards/pizero/blinker01/blinker01.c` (C) | Magnitude: 30.76 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, args: 8, state_mutation: 7, dead_code: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `bootloader01/ser.h` (C) | Magnitude: 22.16 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 8, args: 8, api: 8, pointers: 2
- `blinker01/blinker01.c` (C) | Magnitude: 30.34 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 13, args: 8, state_mutation: 7, bitwise_ops: 6
- `boards/pi1/blinker01/blinker01.c` (C) | Magnitude: 30.34 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 13, args: 8, state_mutation: 7, bitwise_ops: 6
- `boards/pi2/HYP/blinker01/blinker01.c` (C) | Magnitude: 37.88 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 19, args: 12, bitwise_ops: 12, state_mutation: 10
- `boards/piaplus/blinker01/blinker01.c` (C) | Magnitude: 37.88 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 19, args: 12, bitwise_ops: 12, state_mutation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `twain/adler32.c` (C) | Magnitude: 164.24 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 105, state_mutation: 47, bitwise_ops: 23, branch: 18

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `twain/twain.c` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 100.0%)
- `twain/inflate.c` -> **Severity: 0.015** (Bridge: 0.0002 * Flux: 100.0%)
- `twain/zutil.c` -> **Severity: 0.014** (Bridge: 0.0001 * Flux: 99.9991%)
- `twain/deflate.c` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 100.0%)
- `twain/uncompr.c` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `twain/zlib.h` -> **Severity: 0.716** (Embedded: 0.014 * Error Risk: 51.0451%)
- `twain/crc32.c` -> **Severity: 0.414** (Embedded: 0.005 * Error Risk: 83.6551%)
- `twain/adler32.c` -> **Severity: 0.394** (Embedded: 0.005 * Error Risk: 79.6256%)
- `twain/zutil.c` -> **Severity: 0.337** (Embedded: 0.005 * Error Risk: 67.8736%)
- `twain/twain.c` -> **Severity: 0.291** (Embedded: 0.0041 * Error Risk: 71.5669%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `bench02/novectors.s` -> **Severity: 302.4** (Blast Radius: 3.024 * Doc Risk: 100.0%)
- `boards/cpuid/vectors.s` -> **Severity: 302.4** (Blast Radius: 3.024 * Doc Risk: 100.0%)
- `boards/pi3/aarch32/SVC/uart05/start.s` -> **Severity: 302.4** (Blast Radius: 3.024 * Doc Risk: 100.0%)
- `boards/pizero/asmdelay/start.s` -> **Severity: 302.4** (Blast Radius: 3.024 * Doc Risk: 100.0%)
- `bssdata/start.s` -> **Severity: 302.4** (Blast Radius: 3.024 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 280 literal sites + 1740 sites through wrappers = 2020
- **`panics_and_aborts`:** 13 literal sites + 1 sites through wrappers = 14

- `PUT32` (function, debug_prints, primitive): 1739 call sites in 138 files -- `bootloader07/ihex.c`
- `z_error` (function, debug_prints, primitive): 1 call sites in 1 files -- `twain/zutil.c`
- `z_error` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `twain/zutil.c`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2031 call pairs -- scoped 29.5%, unique 3.9%, ambiguous 53.0%, external 13.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 2030 | 29.6% | 3.9% | 53.1% | 13.5% |
| assembly | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
