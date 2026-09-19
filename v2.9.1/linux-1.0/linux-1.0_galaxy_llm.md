# ARCHITECTURAL_BRIEF: linux-1.0
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/kalamangga-net/linux-1.0.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 549 analyzed artifact(s), 123132 LOC.
- **Load-bearing artifact:** `include/linux/sched.h` -- 198 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `net/inet/sock.c` -- pulls in 29 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `net/inet/tcp.c` at magnitude 3631.52 (structural weight, not risk).
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
| Total Artifacts | 562 |
| Analyzed Artifacts (Scanned) | 549 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 13 |
| Total LOC | 123132 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 97.7% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3777 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0738 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5122 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 41 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 485 | 118078 | 88.3% |
| MAKEFILE | 28 | 1020 | 5.1% |
| ASSEMBLY | 19 | 3581 | 3.5% |
| MARKDOWN | 7 | 0 | 1.3% |
| PLAINTEXT | 6 | 0 | 1.1% |
| SHELL | 3 | 132 | 0.5% |
| BMS | 1 | 321 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `2.336`
> **Composition Archetype:** `Hub-Coupled App` (z +2.34; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 32%, Large Core Modules (3) 22%, Many-Argument Workhorses Files 13%, Compute Cores Files 8%, Data / Markup / Trivial 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 536 | 97.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 2.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 13*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (Machine-Generated Source Code Signature: 60 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.plip`: 2x Excluded (Unsupported Extension: '.PLIP')
- `.sbpcd`: 1x Excluded (Unsupported Extension: '.sbpcd')
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 400 LOC)
- `.src`: 1x Excluded (Unsupported Extension: '.SRC')
- `.dlink`: 1x Excluded (Unsupported Extension: '.DLINK')
- `.pro`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.linux`: 1x Excluded (Unsupported Extension: '.linux')
- `.in`: 1x Zero-Density Threshold (LOC: 122, Signals: 0)
- `.h`: 1x Zero-Density Threshold (LOC: 68, Signals: 0)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.4 | 37.2 | 26.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 52.8 | 72.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 26.1 | 11.8 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 34.7 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 17.9 | 3.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 28.2 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 52.1 | 90.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 91.7 | 1.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 62.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 32970 | 364 | 182 | `net/inet/tcp.c` |
| cleanup | 70 | 30 | 0 | `Makefile` |
| guards | 3937 | 295 | 22 | `drivers/sound/gus_wave.c` |
| danger | 1074 | 187 | 6 | `Configure` |
| concurrency | 38 | 14 | 0 | `net/inet/tcp.c` |
| connectivity | 3646 | 448 | 16 | `include/linux/sys.h` |
| io | 261 | 63 | 1 | `Configure` |
| crypto | 0 | 0 | 0 | - |
| ipc | 291 | 48 | 0 | `net/unix/sock.c` |
| time | 27 | 9 | 0 | `drivers/char/tpqic02.c` |
| serialization | 5 | 3 | 0 | `net/inet/Makefile` |
| regex | 3 | 1 | 0 | `kernel/ksyms.sh` |
| events | 133 | 34 | 0 | `boot/setup.S` |
| tests | 4 | 3 | 0 | `drivers/scsi/aha152x.c` |
| docs | 79 | 21 | 0 | `drivers/char/tpqic02.c` |
| debt | 463 | 125 | 1 | `drivers/sound/configure.c` |
| mutation | 34828 | 341 | 188 | `drivers/block/sbpcd.c` |
| dead_code | 1184 | 294 | 7 | `kernel/sys.c` |
| credential | 0 | 0 | 0 | - |
| threat | 1472 | 203 | 8 | `include/linux/tty.h` |
| ml_ai | 407 | 48 | 0 | `drivers/FPU-emu/fpu_trig.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Configure` (Hits: 51)
- `boot/setup.S` (Hits: 36)
- `Makefile` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **sched.h** (`include/linux/sched.h`) — 198 inbound connections
2. **errno.h** (`include/linux/errno.h`) — 169 inbound connections
3. **segment.h** (`include/asm/segment.h`) — 143 inbound connections
4. **kernel.h** (`include/linux/kernel.h`) — 140 inbound connections
5. **system.h** (`include/asm/system.h`) — 116 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **sock.c** (`net/inet/sock.c`) — 29 outbound dependencies
2. **slip.c** (`drivers/net/slip.c`) — 28 outbound dependencies
3. **dev.c** (`net/inet/dev.c`) — 26 outbound dependencies
4. **fs.h** (`include/linux/fs.h`) — 26 outbound dependencies
5. **8390.c** (`drivers/net/8390.c`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `aha152x_intr` **(Compute Cores)** (@ `drivers/scsi/aha152x.c`) -> Impact: **384.3** | LOC: 983
  * *Intent:* /* * Interrupts handler (main routine of the driver) */
- `internal_command` **(Many-Argument Workhorses)** (@ `drivers/scsi/seagate.c`) -> Impact: **309.3** | LOC: 472
- `vt_ioctl` **(Many-Argument Workhorses)** (@ `drivers/char/vt.c`) -> Impact: **301.1** | LOC: 476
  * *Intent:* /* * We handle the console-specific ioctl's here. We allow the * capability to modify any console, not just the fg_console. */
- `tty_ioctl` **(Many-Argument Workhorses)** (@ `drivers/char/tty_ioctl.c`) -> Impact: **294.1** | LOC: 336
- `tcp_rcv` **(Many-Argument Workhorses)** (@ `net/inet/tcp.c`) -> Impact: **267.6** | LOC: 433
- `tcp_ack` **(Many-Argument Workhorses)** (@ `net/inet/tcp.c`) -> Impact: **233.1** | LOC: 368
  * *Intent:* /* This routine deals with incoming acks, but not outgoing ones. */
- `main` **(Many-Argument Workhorses)** (@ `drivers/sound/configure.c`) -> Impact: **213.5** | LOC: 320
- `con_write` **(Compute Cores)** (@ `drivers/char/console.c`) -> Impact: **211.3** | LOC: 323
- `sys_semctl` **(Many-Argument Workhorses)** (@ `ipc/sem.c`) -> Impact: **204.0** | LOC: 190
- `fdomain_16x0_intr` **(Compute Cores)** (@ `drivers/scsi/fdomain.c`) -> Impact: **193.7** | LOC: 424

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `drivers/scsi` | 43 | 14645.94 | 41.3% | 22.6% |
| `net/inet` | 33 | 11746.98 | 37.24% | 31.07% |
| `drivers/char` | 20 | 10931.72 | 55.05% | 23.84% |
| `drivers/net` | 30 | 10150.22 | 50.91% | 14.73% |
| `drivers/sound` | 42 | 9380.18 | 44.05% | 28.14% |
| `drivers/block` | 11 | 8268.46 | 70.29% | 37.2% |
| `fs` | 21 | 8085.86 | 67.1% | 52.79% |
| `drivers/FPU-emu` | 42 | 5488.98 | 26.13% | 44.02% |
| `kernel` | 23 | 5450.62 | 55.54% | 57.16% |
| `fs/ext2` | 16 | 5338.88 | 57.58% | 27.78% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `drivers/FPU-emu/fpu_arith.c` -> **100.0%** Exposure
- `drivers/sound/midibuf.c` -> **100.0%** Exposure
- `drivers/FPU-emu/Makefile` -> **99.9998%** Exposure
- `ibcs/Makefile` -> **99.9998%** Exposure
- `ipc/Makefile` -> **99.9983%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `drivers/FPU-emu/get_address.c` -> **100.0%** Exposure
- `drivers/FPU-emu/poly_l2.c` -> **100.0%** Exposure
- `drivers/FPU-emu/reg_ld_str.c` -> **100.0%** Exposure
- `drivers/block/cdu31a.c` -> **100.0%** Exposure
- `drivers/block/floppy.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `kernel/sys.c` -> **40** Orphaned Functions | **0** Duplicates
- `drivers/FPU-emu/fpu_arith.c` -> **18** Orphaned Functions | **0** Duplicates
- `fs/open.c` -> **17** Orphaned Functions | **0** Duplicates
- `drivers/FPU-emu/errors.c` -> **15** Orphaned Functions | **0** Duplicates
- `drivers/FPU-emu/reg_ld_str.c` -> **15** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2650` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `net/inet/tcp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3631.52 | **LOC:** 3752 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tcp_rcv` **(Many-Argument Workhorses)** (Impact: 267.6)
  * `tcp_ack` **(Many-Argument Workhorses)** (Impact: 233.1)
    * *Intent:* /* This routine deals with incoming acks, but not outgoing ones. */
  * `tcp_write` **(Many-Argument Workhorses)** (Impact: 153.2)
    * *Intent:* /* * This routine copies from a user buffer into a socket, * and starts the transmit system. */
  * `tcp_data` **(Many-Argument Workhorses)** (Impact: 146.7)
    * *Intent:* /* * This routine handles the data. If there is room in the buffer, * it will be have already been m...
  * `tcp_read` **(Many-Argument Workhorses)** (Impact: 90.4)
    * *Intent:* /* This routine copies from a sock struct into the user buffer. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 569 instances
* *State Mutation (weighted view):* 1876
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 645`, `structural_boundaries: 483`, `args: 94`, `func_start: 48`, `class_start: 68`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 738`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 27`, `unreferenced_by_name: 3`
* *Architecture:* `api: 12`, `import: 23`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` arp.h, segment.h, system.h, dev.h, icmp.h, inet.h, ip.h, errno.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/block/sbpcd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3050.7 | **LOC:** 2995 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sbpcd_ioctl` **(Many-Argument Workhorses)** (Impact: 176.6)
    * *Intent:* /*==========================================================================*/ /*===================...
  * `sbpcd_init` **(Many-Argument Workhorses)** (Impact: 59.4)
    * *Intent:* /*==========================================================================*/ /* * Test for presenc...
  * `prepare` **(Many-Argument Workhorses)** (Impact: 50.6)
    * *Intent:* /*==========================================================================*/ /* * called always if...
  * `sbp_data` **(I/O & Config Routines)** (Impact: 50.0)
    * *Intent:* /*==========================================================================*/ /* * Check the comple...
  * `xx_SetVolume` **(I/O & Config Routines)** (Impact: 49.4)
    * *Intent:* /*==========================================================================*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 623 instances
* *State Mutation (weighted view):* 1938
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 630`, `structural_boundaries: 373`, `args: 133`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 692`, `dead_code: 3`, `fragile_debt: 17`, `unreferenced_by_name: 7`
* *Architecture:* `api: 8`, `import: 17`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` io.h, segment.h, system.h, blk.h, cdrom.h, config.h, ddi.h, errno.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/sound/gus_wave.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2238.46 | **LOC:** 3421 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `guswave_load_patch` **(Many-Argument Workhorses)** (Impact: 109.3)
  * `guswave_start_note2` **(Many-Argument Workhorses)** (Impact: 82.2)
  * `gus_mixer_ioctl` **(Many-Argument Workhorses)** (Impact: 74.2)
  * `guswave_patchmgr` **(Many-Argument Workhorses)** (Impact: 74.1)
    * *Intent:* #endif
  * `guswave_hw_control` **(Many-Argument Workhorses)** (Impact: 56.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 372 instances
* *State Mutation (weighted view):* 1176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 398`, `structural_boundaries: 288`, `args: 130`, `func_start: 73`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 432`, `fragile_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 17`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` gus_hw.h, ultrasound.h, sound_config.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/char/console.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1934.04 | **LOC:** 1968 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.3%), Complexity Load (formerly Cognitive Load) (92.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `con_write` **(Compute Cores)** (Impact: 211.3)
  * `set_selection` **(Compute Cores)** (Impact: 68.9)
    * *Intent:* /* set the current selection. Invoked by ioctl(). */
  * `set_mode` **(Compute Cores)** (Impact: 40.7)
  * `csi_m` **(Compute Cores)** (Impact: 33.8)
  * `con_init` **(I/O & Config Routines)** (Impact: 24.8)
    * *Intent:* /* * long con_init(long); * * This routine initalizes console interrupts, and does nothing * else. I...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 342 instances
* *State Mutation (weighted view):* 1108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 408`, `structural_boundaries: 237`, `args: 98`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 424`, `fragile_debt: 1`, `unreferenced_by_name: 10`
* *Architecture:* `api: 24`, `import: 14`
* *Defense:* `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` io.h, segment.h, system.h, kbd_kern.h, config.h, ctype.h, errno.h, kd.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `net/inet/sock.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1795.44 | **LOC:** 1901 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sock_setsockopt` **(Many-Argument Workhorses)** (Impact: 98.0)
    * *Intent:* /* * This is meant for all protocols to use and covers goings on * at the socket level. Everything h...
  * `inet_ioctl` **(Many-Argument Workhorses)** (Impact: 91.9)
  * `sock_getsockopt` **(Many-Argument Workhorses)** (Impact: 58.3)
  * `inet_connect` **(Many-Argument Workhorses)** (Impact: 50.8)
  * `inet_create` **(Many-Argument Workhorses)** (Impact: 45.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 271 instances
* *State Mutation (weighted view):* 899
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 337`, `structural_boundaries: 358`, `args: 64`, `func_start: 42`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 357`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`, `unreferenced_by_name: 10`
* *Architecture:* `io: 4`, `api: 18`, `import: 29`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` arp.h, segment.h, system.h, dev.h, icmp.h, inet.h, ip.h, config.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/char/tty_io.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1788.54 | **LOC:** 1846 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.1%), Complexity Load (formerly Cognitive Load) (80.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copy_to_cooked` **(Compute Cores)** (Impact: 140.1)
  * `read_chan` **(Many-Argument Workhorses)** (Impact: 101.4)
  * `eraser` **(Many-Argument Workhorses)** (Impact: 72.4)
  * `init_dev` **(Compute Cores)** (Impact: 58.1)
    * *Intent:* /* * This is so ripe with races that you should *really* not touch this * unless you know exactly wh...
  * `release_dev` **(Many-Argument Workhorses)** (Impact: 48.2)
    * *Intent:* /* * Even releasing the tty structures is a tricky business.. We have * to be very careful that the ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 278 instances
* *State Mutation (weighted view):* 846
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 432`, `structural_boundaries: 280`, `args: 79`, `func_start: 45`, `class_start: 26`
* *Risk/State:* `state_mutation: 290`, `fragile_debt: 3`, `unreferenced_by_name: 12`
* *Architecture:* `io: 3`, `api: 23`, `import: 18`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` bitops.h, segment.h, system.h, kbd_kern.h, ctype.h, errno.h, fcntl.h, kd.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/char/serial.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1749.26 | **LOC:** 2076 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_serial_info` **(Many-Argument Workhorses)** (Impact: 69.1)
  * `rs_ioctl` **(Many-Argument Workhorses)** (Impact: 66.4)
  * `block_til_ready` **(Many-Argument Workhorses)** (Impact: 63.9)
    * *Intent:* /* * ------------------------------------------------------------ * rs_open() and friends * --------...
  * `startup` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `change_speed` **(Compute Cores)** (Impact: 36.1)
    * *Intent:* /* * This routine is called to set the UART divisor registers to match * the specified baud rate for...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 312 instances
* *State Mutation (weighted view):* 965
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 369`, `structural_boundaries: 243`, `args: 77`, `func_start: 43`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 341`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 16`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` bitops.h, io.h, segment.h, system.h, config.h, errno.h, fcntl.h, interrupt.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/char/tpqic02.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1738.74 | **LOC:** 2623 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_ioctl_cmd` **(Compute Cores)** (Impact: 106.2)
    * *Intent:* } /* do_qic_cmd */ /* Not all ioctls are supported for all drives. Some rely on * optional QIC-02 co...
  * `tape_qic02_ioctl` **(Many-Argument Workhorses)** (Impact: 83.4)
    * *Intent:* } /* tape_qic02_release */ /* ioctl allows user programs to rewind the tape and stuff like that */
  * `tape_qic02_read` **(Many-Argument Workhorses)** (Impact: 78.5)
    * *Intent:* * like 4k or so). * * Scott S. Bertilson suggested to continue filling the user buffer, rather * tha...
  * `tape_qic02_open` **(Many-Argument Workhorses)** (Impact: 73.6)
    * *Intent:* /* tape_qic02_open() * We allow the device to be opened, even if it is marked 'dead' because * we wa...
  * `tape_qic02_write` **(Many-Argument Workhorses)** (Impact: 64.8)
    * *Intent:* * If there is insufficient room, write as much as will fit and * return the amount written. If the r...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 280 instances
* *State Mutation (weighted view):* 854
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 216`, `args: 160`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 294`, `dead_code: 13`, `planned_debt: 2`, `fragile_debt: 7`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 1`, `import: 15`
* *Defense:* `doc: 29`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` dma.h, io.h, segment.h, system.h, config.h, delay.h, errno.h, fcntl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/scsi/st.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 1538.88 | **LOC:** 1476 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `st_int_ioctl` **(Many-Argument Workhorses)** (Impact: 149.5)
    * *Intent:* count = total; /* Read only one variable length block */ } /* for (total = 0; total < count; ) */ SC...
  * `st_write` **(Many-Argument Workhorses)** (Impact: 133.6)
  * `st_read` **(Many-Argument Workhorses)** (Impact: 121.4)
  * `st_ioctl` **(Many-Argument Workhorses)** (Impact: 66.2)
  * `scsi_tape_open` **(Many-Argument Workhorses)** (Impact: 57.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 268 instances
* *State Mutation (weighted view):* 847
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 139`, `args: 52`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 311`, `dead_code: 3`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` blk.h, segment.h, system.h, constants.h, errno.h, fcntl.h, fs.h, ioctl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/scsi/NCR5380.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1471.74 | **LOC:** 2448 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 1.249; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NCR5380_information_transfer` **(Many-Argument Workhorses)** (Impact: 186.9)
    * *Intent:* * Purpose : run through the various SCSI phases and do as the target * directs us to. Operates on th...
  * `NCR5380_transfer_dma` **(Many-Argument Workhorses)** (Impact: 151.9)
    * *Intent:* * * Inputs : instance - instance of driver, *phase - pointer to * what phase is expected, *count - p...
  * `NCR5380_transfer_pio` **(Many-Argument Workhorses)** (Impact: 67.9)
    * *Intent:* * maximum number of bytes, 0 if all bytes or transfered or exit * is in same phase. * * Also, *phase...
  * `NCR5380_intr` **(Compute Cores)** (Impact: 38.2)
    * *Intent:* /* * Function : void NCR5380_intr (int irq) * * Purpose : handle interrupts, restablishing I_T_L or ...
  * `NCR5380_abort` **(Many-Argument Workhorses)** (Impact: 34.5)
    * *Intent:* * * Inputs : cmd - the Scsi_Cmnd to abort, code - code to set the * host byte of the result field to...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 245 instances
* *State Mutation (weighted view):* 753
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 119`, `args: 158`, `func_start: 23`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 263`, `dead_code: 7`, `planned_debt: 3`, `fragile_debt: 16`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.249
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.005455
  * `Imports (Out-Degree: 1):` delay.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `drivers/scsi/scsi.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1464.64 | **LOC:** 1721 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scsi_done` **(Compute Cores)** (Impact: 116.8)
    * *Intent:* * (2) Call internal_cmnd to requeue the command. This will result in * scsi_done being called again ...
  * `scan_scsis` **(I/O & Config Routines)** (Impact: 82.5)
    * *Intent:* /* * Detecting SCSI devices : * We scan all present host adapter's busses, from ID 0 to ID 6. * We u...
  * `allocate_device` **(Many-Argument Workhorses)** (Impact: 62.6)
    * *Intent:* of the packets for each device */
  * `request_queueable` **(Compute Cores)** (Impact: 41.3)
    * *Intent:* of the calling code to ensure that this is the case. */
  * `scsi_dev_init` **(Many-Argument Workhorses)** (Impact: 40.1)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 265 instances
* *State Mutation (weighted view):* 870
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 142`, `args: 69`, `func_start: 20`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 2`, `state_mutation: 340`, `dead_code: 3`, `fragile_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` blk.h, system.h, constants.h, hosts.h, sched.h, string.h, timer.h, scsi.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `net/inet/ip.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1432.96 | **LOC:** 1610 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.0%)
- **Documentation Coverage:** 97.619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_options` **(Many-Argument Workhorses)** (Impact: 71.4)
  * `ip_rcv` **(Many-Argument Workhorses)** (Impact: 53.6)
    * *Intent:* #endif /* This function receives all incoming IP datagrams. */
  * `ip_defrag` **(Many-Argument Workhorses)** (Impact: 53.3)
    * *Intent:* /* Process an incoming IP datagram fragment. */
  * `ip_forward` **(Many-Argument Workhorses)** (Impact: 44.2)
    * *Intent:* #ifdef CONFIG_IP_FORWARD /* Forward an IP datagram to its next destination. */
  * `ip_build_header` **(Many-Argument Workhorses)** (Impact: 38.6)
    * *Intent:* /* * This routine builds the appropriate hardware/IP headers for * the routine. It assumes that if *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 275 instances
* *State Mutation (weighted view):* 878
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 236`, `args: 60`, `func_start: 29`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 328`, `fragile_debt: 3`, `unreferenced_by_name: 8`
* *Architecture:* `api: 14`, `import: 21`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` arp.h, segment.h, system.h, dev.h, eth.h, icmp.h, inet.h, ip.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/scsi/aha152x.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1418.56 | **LOC:** 2369 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.9%), Guard Balance (formerly Safety Score) (91.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `aha152x_intr` **(Compute Cores)** (Impact: 384.3)
    * *Intent:* /* * Interrupts handler (main routine of the driver) */
  * `disp_ports` **(I/O & Config Routines)** (Impact: 83.8)
    * *Intent:* /* * Display registers of AIC-6260 */
  * `aha152x_detect` **(Compute Cores)** (Impact: 70.4)
  * `aha152x_abort` **(Many-Argument Workhorses)** (Impact: 37.2)
    * *Intent:* /* * Abort a queued command * (commands that are on the bus can't be aborted easily) */
  * `show_command` **(Compute Cores)** (Impact: 26.6)
    * *Intent:* #endif /* * Show the command data of a command */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 197 instances
* *State Mutation (weighted view):* 604
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 478`, `structural_boundaries: 123`, `args: 414`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 210`, `dead_code: 4`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 13`, `import: 12`
* *Defense:* `test: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` blk.h, aha152x.h, io.h, system.h, constants.h, hosts.h, errno.h, ioport.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mm/memory.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1413.54 | **LOC:** 1226 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `remap_page_range` **(Many-Argument Workhorses)** (Impact: 59.7)
    * *Intent:* /* * maps a range of physical memory into the requested pages. the old * mappings are removed. any r...
  * `share_page` **(Many-Argument Workhorses)** (Impact: 46.7)
    * *Intent:* /* * share_page() tries to find a process that could share a page with * the current one. Address is...
  * `do_no_page` **(Many-Argument Workhorses)** (Impact: 40.9)
  * `zeromap_page_range` **(Many-Argument Workhorses)** (Impact: 38.9)
  * `__do_wp_page` **(Many-Argument Workhorses)** (Impact: 29.8)
    * *Intent:* /* * This routine handles present pages, when users try to write * to a shared page. It is done by c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 277 instances
* *State Mutation (weighted view):* 849
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 153`, `args: 66`, `func_start: 30`, `class_start: 11`
* *Risk/State:* `state_mutation: 295`, `planned_debt: 1`
* *Architecture:* `api: 32`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` system.h, config.h, errno.h, head.h, kernel.h, mman.h, ptrace.h, sched.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/nfs/proc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1292.3 | **LOC:** 874 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nfs_proc_readdir` **(Many-Argument Workhorses)** (Impact: 59.0)
  * `nfs_proc_read` **(Many-Argument Workhorses)** (Impact: 36.5)
  * `nfs_proc_lookup` **(Many-Argument Workhorses)** (Impact: 28.9)
  * `nfs_proc_write` **(Many-Argument Workhorses)** (Impact: 28.3)
  * `nfs_proc_create` **(Many-Argument Workhorses)** (Impact: 28.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 235 instances
* *State Mutation (weighted view):* 773
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 131`, `args: 41`, `func_start: 30`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 303`, `unreferenced_by_name: 15`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` config.h, errno.h, in.h, mm.h, nfs_fs.h, param.h, sched.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/ext2/namei.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1267.8 | **LOC:** 1121 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Complexity Load (formerly Cognitive Load) (84.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_ext2_rename` **(Many-Argument Workhorses)** (Impact: 129.4)
    * *Intent:* /* * rename uses retrying to avoid race-conditions: at least they should be * minimal. * it tries to...
  * `ext2_find_entry` **(Many-Argument Workhorses)** (Impact: 60.6)
    * *Intent:* /* * ext2_find_entry() * * finds an entry in the specified directory with the wanted name. It * retu...
  * `ext2_add_entry` **(Many-Argument Workhorses)** (Impact: 59.8)
    * *Intent:* /* * ext2_add_entry() * * adds a file entry to the specified directory, using the same * semantics a...
  * `ext2_mknod` **(Many-Argument Workhorses)** (Impact: 55.1)
  * `ext2_rmdir` **(Many-Argument Workhorses)** (Impact: 42.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 220 instances
* *State Mutation (weighted view):* 693
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 159`, `args: 30`, `func_start: 16`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 253`, `fragile_debt: 5`, `unreferenced_by_name: 6`
* *Architecture:* `api: 9`, `import: 9`
* *Defense:* `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` segment.h, errno.h, ext2_fs.h, fcntl.h, fs.h, locks.h, sched.h, stat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/block/cdu31a.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1152.46 | **LOC:** 1853 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.4%), Complexity Load (formerly Cognitive Load) (90.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scd_ioctl` **(Many-Argument Workhorses)** (Impact: 131.8)
    * *Intent:* /* * The big ugly ioctl handler. */
  * `get_data` **(Many-Argument Workhorses)** (Impact: 71.7)
    * *Intent:* /* * This routine issues a read data command and gets the data. I don't * really like the way this i...
  * `get_result` **(Many-Argument Workhorses)** (Impact: 42.0)
    * *Intent:* /* * The following reads data from the command result register. It is a * fairly complex routine, al...
  * `do_sony_cd_cmd` **(Many-Argument Workhorses)** (Impact: 38.5)
    * *Intent:* /* * Do a command that does not involve data transfer. This routine must * be re-entrant from the sa...
  * `do_cdu31a_request` **(I/O & Config Routines)** (Impact: 27.9)
    * *Intent:* /* * The OS calls this to perform a read or write operation to the drive. * Write obviously fail. Re...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 183 instances
* *State Mutation (weighted view):* 618
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 166`, `args: 92`, `func_start: 41`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 252`, `fragile_debt: 5`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` io.h, segment.h, system.h, blk.h, cdrom.h, cdu31a.h, errno.h, fs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/hpfs/hpfs_fs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1146.94 | **LOC:** 1725 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_opts` **(Many-Argument Workhorses)** (Impact: 93.1)
    * *Intent:* /* * A tiny parser for option strings, stolen from dosfs.
  * `hpfs_read_super` **(Many-Argument Workhorses)** (Impact: 43.5)
    * *Intent:* /* super block ops */ /* * mount. This gets one thing, the root directory inode. It does a * bunch o...
  * `hpfs_lookup` **(Many-Argument Workhorses)** (Impact: 42.8)
    * *Intent:* /* directory ops */ /* * lookup. Search the specified directory for the specified name, set * *resul...
  * `map_dirent` **(Many-Argument Workhorses)** (Impact: 30.7)
    * *Intent:* /*
  * `hpfs_readdir` **(C Struct Operations)** (Impact: 29.2)
    * *Intent:* * dewey-decimal record of subtree locations. Like so: * * (1 (1.1 1.2 1.3) 2 3 (3.1 (3.1.1 3.1.2) 3....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *State Mutation (weighted view):* 569
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 249`, `args: 67`, `func_start: 37`, `class_start: 60`
* *Risk/State:* `state_mutation: 211`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 11`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` bitops.h, segment.h, hpfs.h, errno.h, fs.h, hpfs_fs.h, locks.h, malloc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/exec.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1143.3 | **LOC:** 911 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (85.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_execve` **(Many-Argument Workhorses)** (Impact: 129.1)
    * *Intent:* /* * sys_execve() executes a new program. */
  * `copy_strings` **(Many-Argument Workhorses)** (Impact: 44.1)
    * *Intent:* * to be put directly into the top of new user memory. * * Modified by TYT, 11/24/91 to add the from_...
  * `load_aout_binary` **(Many-Argument Workhorses)** (Impact: 41.1)
    * *Intent:* /* * These are the functions used to load a.out style executables and shared * libraries. There is n...
  * `core_dump` **(Many-Argument Workhorses)** (Impact: 35.0)
    * *Intent:* /* * Routine writes a core dump image in the current directory. * Currently only a stub-function. * ...
  * `flush_old_exec` **(Compute Cores)** (Impact: 34.7)
    * *Intent:* /* * This function flushes out all traces of the currently running executable so * that a new one ca...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 231 instances
* *State Mutation (weighted view):* 705
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 80`, `args: 39`, `func_start: 13`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 243`, `dead_code: 2`, `unreferenced_by_name: 3`
* *Architecture:* `io: 6`, `api: 22`, `import: 19`
* *Defense:* `safety: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` segment.h, system.h, a.out.h, binfmts.h, errno.h, fcntl.h, fs.h, kernel.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/buffer.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1134.68 | **LOC:** 1026 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getblk` **(Many-Argument Workhorses)** (Impact: 49.6)
    * *Intent:* /* * Ok, this is getblk, and it isn't very clear, again to hinder * race-conditions. Most of the cod...
  * `sync_buffers` **(Compute Cores)** (Impact: 39.2)
    * *Intent:* before the writes have finished; fsync() may not. */
  * `check_disk_change` **(Compute Cores)** (Impact: 32.6)
    * *Intent:* /* * This routine checks whether a floppy has been changed, and * invalidates all buffer-cache-entri...
  * `set_blocksize` **(Compute Cores)** (Impact: 29.7)
  * `try_to_load_aligned` **(Many-Argument Workhorses)** (Impact: 25.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 212 instances
* *State Mutation (weighted view):* 650
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 160`, `args: 65`, `func_start: 36`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 226`, `fragile_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 24`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` io.h, system.h, config.h, errno.h, kernel.h, locks.h, major.h, sched.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/ext/namei.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1110.04 | **LOC:** 901 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Complexity Load (formerly Cognitive Load) (84.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_ext_rename` **(Many-Argument Workhorses)** (Impact: 90.3)
    * *Intent:* /* * rename uses retrying to avoid race-conditions: at least they should be minimal. * it tries to a...
  * `ext_add_entry` **(Many-Argument Workhorses)** (Impact: 66.1)
    * *Intent:* /* * ext_add_entry() * * adds a file entry to the specified directory, using the same * semantics as...
  * `ext_find_entry` **(Many-Argument Workhorses)** (Impact: 61.7)
    * *Intent:* /* * ext_find_entry() * * finds an entry in the specified directory with the wanted name. It * retur...
  * `ext_mknod` **(Many-Argument Workhorses)** (Impact: 51.9)
  * `ext_rmdir` **(Many-Argument Workhorses)** (Impact: 26.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 199 instances
* *State Mutation (weighted view):* 626
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 150`, `args: 20`, `func_start: 16`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 228`, `unreferenced_by_name: 8`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` segment.h, errno.h, ext_fs.h, fcntl.h, kernel.h, sched.h, stat.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/net/depca.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1091.58 | **LOC:** 1363 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `depca_probe1` **(Many-Argument Workhorses)** (Impact: 61.7)
  * `depca_start_xmit` **(Many-Argument Workhorses)** (Impact: 45.8)
    * *Intent:* /*
  * `depca_probe` **(Compute Cores)** (Impact: 32.1)
  * `depca_tx` **(Compute Cores)** (Impact: 23.5)
    * *Intent:* /*
  * `DevicePresent` **(Stateful Encapsulated Methods)** (Impact: 22.4)
    * *Intent:* /* ** Look for a special sequence in the Ethernet station address PROM that ** is common across all ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 244 instances
* *State Mutation (weighted view):* 756
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 121`, `args: 81`, `func_start: 17`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 268`, `dead_code: 5`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 6`, `import: 19`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` arp.h, bitops.h, dma.h, io.h, depca.h, dev.h, eth.h, iow.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/FPU-emu/reg_ld_str.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1091.5 | **LOC:** 1464 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reg_store_single` **(I/O & Config Routines)** (Impact: 55.3)
    * *Intent:* /* Put a float into user memory */
  * `reg_store_double` **(I/O & Config Routines)** (Impact: 53.6)
    * *Intent:* /* Put a double into user memory */
  * `fldenv` **(Compute Cores)** (Impact: 31.5)
    * *Intent:* /*===========================================================================*/
  * `round_to_int` **(Compute Cores)** (Impact: 29.7)
    * *Intent:* the largest possible value */
  * `write_to_extended` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 218 instances
* *State Mutation (weighted view):* 676
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 108`, `args: 76`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 240`, `unreferenced_by_name: 15`
* *Architecture:* `api: 20`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` segment.h, control_w.h, exception.h, fpu_emu.h, fpu_system.h, reg_constant.h, status_w.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/xiafs/namei.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1080.24 | **LOC:** 848 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Complexity Load (formerly Cognitive Load) (84.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_xiafs_rename` **(Many-Argument Workhorses)** (Impact: 92.9)
    * *Intent:* /* * rename uses retry to avoid race-conditions: at least they should be minimal. * it tries to allo...
  * `xiafs_add_entry` **(Many-Argument Workhorses)** (Impact: 73.1)
    * *Intent:* /* * xiafs_add_entry() * * adds a file entry to the specified directory, using the same * semantics ...
  * `xiafs_find_entry` **(Many-Argument Workhorses)** (Impact: 54.3)
    * *Intent:* /* * xiafs_find_entry() * * finds an entry in the specified directory with the wanted name. It * ret...
  * `xiafs_mknod` **(Many-Argument Workhorses)** (Impact: 49.3)
  * `empty_dir` **(Compute Cores)** (Impact: 29.8)
    * *Intent:* /* * routine to check that the specified directory is empty (for rmdir) */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 186 instances
* *State Mutation (weighted view):* 586
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 147`, `args: 16`, `func_start: 16`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 214`, `fragile_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 9`, `import: 9`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` segment.h, errno.h, fcntl.h, kernel.h, sched.h, stat.h, string.h, xia_fs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/sysv/namei.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1080.14 | **LOC:** 837 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Complexity Load (formerly Cognitive Load) (87.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_sysv_rename` **(Many-Argument Workhorses)** (Impact: 112.4)
    * *Intent:* /* * rename uses retrying to avoid race-conditions: at least they should be minimal. * it tries to a...
  * `sysv_mknod` **(Many-Argument Workhorses)** (Impact: 54.4)
  * `sysv_add_entry` **(Many-Argument Workhorses)** (Impact: 42.3)
    * *Intent:* /* * sysv_add_entry() * * adds a file entry to the specified directory, returning a possible * error...
  * `sysv_rmdir` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `sysv_unlink` **(Many-Argument Workhorses)** (Impact: 24.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 203 instances
* *State Mutation (weighted view):* 628
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 134`, `args: 19`, `func_start: 16`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 222`, `dead_code: 2`, `unreferenced_by_name: 8`
* *Architecture:* `api: 9`, `import: 7`
* *Defense:* `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` errno.h, fs.h, kernel.h, sched.h, stat.h, string.h, sysv_fs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `include/linux/sched.h` -> **Severity: 2.504** (Bridge: 0.0255 * Flux: 98.1204%)
- `drivers/sound/os.h` -> **Severity: 0.499** (Bridge: 0.005 * Flux: 99.9987%)
- `drivers/block/blk.h` -> **Severity: 0.07** (Bridge: 0.0007 * Flux: 99.9985%)
- `drivers/FPU-emu/fpu_system.h` -> **Severity: 0.031** (Bridge: 0.0018 * Flux: 16.7982%)
- `include/linux/mm.h` -> **Severity: 0.015** (Bridge: 0.0016 * Flux: 9.4233%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `include/linux/sched.h` -> **Severity: 25.34** (Embedded: 0.3462 * Error Risk: 73.1935%)
- `include/asm/segment.h` -> **Severity: 19.061** (Embedded: 0.236 * Error Risk: 80.7547%)
- `include/linux/kernel.h` -> **Severity: 14.497** (Embedded: 0.2305 * Error Risk: 62.9017%)
- `include/linux/mm.h` -> **Severity: 11.206** (Embedded: 0.2126 * Error Risk: 52.7082%)
- `include/linux/page.h` -> **Severity: 10.462** (Embedded: 0.149 * Error Risk: 70.2063%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `include/linux/sched.h` -> **Severity: 2370.3** (Blast Radius: 23.703 * Doc Risk: 100.0%)
- `include/asm/segment.h` -> **Severity: 1480.8** (Blast Radius: 14.808 * Doc Risk: 100.0%)
- `include/linux/string.h` -> **Severity: 1398.9** (Blast Radius: 13.989 * Doc Risk: 100.0%)
- `include/asm/system.h` -> **Severity: 1256.7** (Blast Radius: 12.567 * Doc Risk: 100.0%)
- `include/linux/mm.h` -> **Severity: 636.3** (Blast Radius: 6.363 * Doc Risk: 100.0%)

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
