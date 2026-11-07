# ARCHITECTURAL_BRIEF: linux-1.0
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/kalamangga-net/linux-1.0.git` |
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
- **Scope:** 477 analyzed artifact(s), 102941 LOC.
- **Load-bearing artifact:** `include/linux/sched.h` -- 176 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `net/inet/sock.c` -- pulls in 29 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `net/inet/tcp.c` at magnitude 3593.62 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 477 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 85 |
| Total LOC | 102941 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 84.9% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4052 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1158 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 21.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5758 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 30 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 418 | 98057 | 87.6% |
| MAKEFILE | 26 | 850 | 5.5% |
| ASSEMBLY | 19 | 3581 | 4.0% |
| MARKDOWN | 6 | 0 | 1.3% |
| PLAINTEXT | 4 | 0 | 0.8% |
| SHELL | 3 | 132 | 0.6% |
| BMS | 1 | 321 | 0.2% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 476 |
| cp1252 | cp1252-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 34%, Large Core Modules (3) 22%, Many-Argument Workhorses Files 13%, Compute Cores Files 8%, Data / Markup / Trivial 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 467 | 97.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 2.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 85*

**Composition by Extension & Reason:**
- `.c`: 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 400 LOC)
- `.h`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.plip`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sbpcd`: 1x Excluded (Unsupported Extension: '.sbpcd')
- `.src`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dlink`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pro`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.linux`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.in`: 1x Zero-Density Threshold (LOC: 122, Signals: 0)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.7 | 33.3 | 6.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.5 | 39.6 | 52.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 23.6 | 10.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 32.9 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 19.1 | 4.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 28.2 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 48.8 | 21.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 0.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 61.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 789 | 136 | 5 | `zBoot/inflate.c` |
| cleanup | 54 | 23 | 0 | `Makefile` |
| guards | 3071 | 249 | 20 | `drivers/block/sbpcd.c` |
| danger | 1123 | 173 | 7 | `Configure` |
| concurrency | 38 | 14 | 0 | `net/inet/tcp.c` |
| connectivity | 3141 | 387 | 16 | `include/linux/sys.h` |
| io | 239 | 57 | 1 | `Configure` |
| crypto | 0 | 0 | 0 | - |
| ipc | 289 | 46 | 0 | `net/unix/sock.c` |
| time | 30 | 10 | 0 | `drivers/char/tpqic02.c` |
| serialization | 4 | 2 | 0 | `net/inet/Makefile` |
| regex | 3 | 1 | 0 | `kernel/ksyms.sh` |
| events | 126 | 28 | 0 | `boot/setup.S` |
| tests | 4 | 3 | 0 | `drivers/scsi/aha152x.c` |
| docs | 61 | 13 | 0 | `drivers/char/tpqic02.c` |
| debt | 340 | 106 | 1 | `Configure` |
| mutation | 29324 | 286 | 188 | `drivers/block/sbpcd.c` |
| dead_code | 1016 | 237 | 6 | `kernel/sys.c` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 394 | 41 | 0 | `drivers/FPU-emu/fpu_trig.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.3077**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Configure` (Hits: 51)
- `boot/setup.S` (Hits: 36)
- `Makefile` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **sched.h** (`include/linux/sched.h`) — 176 inbound connections
2. **errno.h** (`include/linux/errno.h`) — 149 inbound connections
3. **segment.h** (`include/asm/segment.h`) — 139 inbound connections
4. **printk.c** (`kernel/printk.c`) — 139 inbound connections
5. **kernel.h** (`include/linux/kernel.h`) — 121 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **sock.c** (`net/inet/sock.c`) — 29 outbound dependencies
2. **fs.h** (`include/linux/fs.h`) — 26 outbound dependencies
3. **dev.c** (`net/inet/dev.c`) — 26 outbound dependencies
4. **arp.c** (`net/inet/arp.c`) — 24 outbound dependencies
5. **loopback.c** (`net/inet/loopback.c`) — 23 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `internal_command` **(Many-Argument Workhorses)** (@ `drivers/scsi/seagate.c`) -> Impact: **379.1** | LOC: 967
- `vt_ioctl` **(Many-Argument Workhorses)** (@ `drivers/char/vt.c`) -> Impact: **301.1** | LOC: 476
  * *Intent:* /* * We handle the console-specific ioctl's here. We allow the * capability to modify any console, not just the fg_console. */
- `tty_ioctl` **(Many-Argument Workhorses)** (@ `drivers/char/tty_ioctl.c`) -> Impact: **294.1** | LOC: 336
- `tcp_rcv` **(Many-Argument Workhorses)** (@ `net/inet/tcp.c`) -> Impact: **246.7** | LOC: 433
- `aha152x_intr` **(Many-Argument Workhorses)** (@ `drivers/scsi/aha152x.c`) -> Impact: **231.6** | LOC: 983
  * *Intent:* /* * Interrupts handler (main routine of the driver) */
- `tcp_ack` **(Many-Argument Workhorses)** (@ `net/inet/tcp.c`) -> Impact: **230.8** | LOC: 368
  * *Intent:* /* This routine deals with incoming acks, but not outgoing ones. */
- `con_write` **(Compute Cores)** (@ `drivers/char/console.c`) -> Impact: **209.9** | LOC: 323
- `sys_semctl` **(Many-Argument Workhorses)** (@ `ipc/sem.c`) -> Impact: **204.0** | LOC: 190
- `parse_options` **(Many-Argument Workhorses)** (@ `fs/msdos/inode.c`) -> Impact: **187.0** | LOC: 71
- `sys_ptrace` **(Many-Argument Workhorses)** (@ `kernel/ptrace.c`) -> Impact: **176.7** | LOC: 225

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `drivers/scsi` | 43 | 13876.24 | 37.92% | 20.11% |
| `net/inet` | 33 | 11591.38 | 36.11% | 28.98% |
| `drivers/char` | 20 | 10773.52 | 53.81% | 20.31% |
| `fs` | 21 | 8077.66 | 66.98% | 48.67% |
| `drivers/block` | 11 | 7869.46 | 69.28% | 34.22% |
| `kernel` | 23 | 5546.62 | 55.27% | 50.21% |
| `drivers/FPU-emu` | 42 | 5463.98 | 22.95% | 35.43% |
| `fs/ext2` | 16 | 5363.38 | 57.29% | 23.94% |
| `fs/sysv` | 11 | 4004.7 | 59.62% | 26.54% |
| `include/linux` | 126 | 3347.14 | 0.66% | 1.99% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `drivers/FPU-emu/fpu_arith.c` -> **100.0%** Exposure
- `drivers/FPU-emu/Makefile` -> **99.999%** Exposure
- `ibcs/Makefile` -> **99.999%** Exposure
- `ipc/Makefile` -> **99.9925%** Exposure
- `kernel/Makefile` -> **99.9925%** Exposure
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
- **Unknown Dependencies:** `2228` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `net/inet/tcp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.64)
- **Top Global Matches:** file_cluster_6: 7.64, file_cluster_8: 9.175, file_cluster_4: 15.84
- **Magnitude:** 3593.62 | **LOC:** 3752 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **22**; blast radius 1.156; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tcp_rcv` **(Many-Argument Workhorses)** (Impact: 246.7)
  * `tcp_ack` **(Many-Argument Workhorses)** (Impact: 230.8)
    * *Intent:* /* This routine deals with incoming acks, but not outgoing ones. */
  * `tcp_write` **(Many-Argument Workhorses)** (Impact: 153.2)
    * *Intent:* /* * This routine copies from a user buffer into a socket, * and starts the transmit system. */
  * `tcp_data` **(Many-Argument Workhorses)** (Impact: 142.2)
    * *Intent:* /* * This routine handles the data. If there is room in the buffer, * it will be have already been m...
  * `tcp_read` **(Many-Argument Workhorses)** (Impact: 90.4)
    * *Intent:* /* This routine copies from a sock struct into the user buffer. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 564 instances
* *State Mutation (weighted view):* 1866
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 629`, `structural_boundaries: 465`, `args: 65`, `func_start: 48`, `class_start: 68`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 738`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 27`, `unreferenced_by_name: 3`
* *Architecture:* `api: 12`, `import: 23`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.156
  * `Choke Point (Betweenness):` 0.000245 | `Ripple Effect (Closeness):` 0.010321
  * `Imports (Out-Degree: 32):` arp.h, segment.h, system.h, dev.h, icmp.h, inet.h, ip.h, errno.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `drivers/block/sbpcd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.815)
- **Top Global Matches:** file_cluster_6: 5.815, file_cluster_4: 8.68, file_cluster_16: 16.234
- **Magnitude:** 2716.8 | **LOC:** 2995 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 1.268; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sbpcd_ioctl` **(Many-Argument Workhorses)** (Impact: 165.4)
    * *Intent:* /*==========================================================================*/ /*===================...
  * `sbpcd_init` **(Many-Argument Workhorses)** (Impact: 50.8)
    * *Intent:* /*==========================================================================*/ /* * Test for presenc...
  * `xx_SetVolume` **(I/O & Config Routines)** (Impact: 49.4)
    * *Intent:* /*==========================================================================*/
  * `sbp_data` **(I/O & Config Routines)** (Impact: 44.0)
    * *Intent:* /*==========================================================================*/ /* * Check the comple...
  * `prepare` **(Many-Argument Workhorses)** (Impact: 40.2)
    * *Intent:* /*==========================================================================*/ /* * called always if...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 569 instances
* *State Mutation (weighted view):* 1778
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 502`, `structural_boundaries: 325`, `args: 130`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 640`, `fragile_debt: 17`, `unreferenced_by_name: 4`
* *Architecture:* `api: 8`, `import: 17`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.268
  * `Choke Point (Betweenness):` 0.002239 | `Ripple Effect (Closeness):` 0.128438
  * `Imports (Out-Degree: 25):` io.h, segment.h, system.h, blk.h, cdrom.h, config.h, ddi.h, errno.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `drivers/char/console.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.262)
- **Top Global Matches:** file_cluster_4: 5.262, file_cluster_16: 10.264, file_cluster_6: 10.981
- **Magnitude:** 1928.04 | **LOC:** 1968 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **14**; blast radius 1.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `con_write` **(Compute Cores)** (Impact: 209.9)
  * `set_selection` **(Compute Cores)** (Impact: 68.9)
    * *Intent:* /* set the current selection. Invoked by ioctl(). */
  * `set_mode` **(Compute Cores)** (Impact: 40.7)
  * `csi_m` **(Compute Cores)** (Impact: 33.8)
  * `scrup` **(Many-Argument Workhorses)** (Impact: 26.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 340 instances
* *State Mutation (weighted view):* 1104
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 396`, `structural_boundaries: 230`, `args: 77`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 424`, `fragile_debt: 1`, `unreferenced_by_name: 10`
* *Architecture:* `api: 24`, `import: 14`
* *Defense:* `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.257
  * `Choke Point (Betweenness):` 0.001174 | `Ripple Effect (Closeness):` 0.115721
  * `Imports (Out-Degree: 21):` io.h, segment.h, system.h, kbd_kern.h, config.h, ctype.h, errno.h, kd.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `drivers/char/tty_io.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.099)
- **Top Global Matches:** file_cluster_6: 5.099, file_cluster_4: 10.866, file_cluster_8: 13.816
- **Magnitude:** 1773.24 | **LOC:** 1846 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **18**; blast radius 1.74; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.3%)
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
* *Structure:* `branch: 423`, `structural_boundaries: 280`, `args: 79`, `func_start: 45`, `class_start: 26`
* *Risk/State:* `state_mutation: 290`, `dead_code: 2`, `fragile_debt: 3`, `unreferenced_by_name: 12`
* *Architecture:* `io: 3`, `api: 23`, `import: 18`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.74
  * `Choke Point (Betweenness):` 0.022558 | `Ripple Effect (Closeness):` 0.150058
  * `Imports (Out-Degree: 31):` bitops.h, segment.h, system.h, kbd_kern.h, ctype.h, errno.h, fcntl.h, kd.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `net/inet/sock.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.485)
- **Top Global Matches:** file_cluster_6: 5.485, file_cluster_4: 10.319, file_cluster_8: 14.972
- **Magnitude:** 1772.04 | **LOC:** 1901 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **29**; blast radius 1.277; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.4%), Complexity Load (formerly Cognitive Load) (72.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sock_setsockopt` **(Many-Argument Workhorses)** (Impact: 98.0)
    * *Intent:* /* * This is meant for all protocols to use and covers goings on * at the socket level. Everything h...
  * `inet_ioctl` **(Many-Argument Workhorses)** (Impact: 89.9)
  * `sock_getsockopt` **(Many-Argument Workhorses)** (Impact: 58.3)
  * `inet_connect` **(Many-Argument Workhorses)** (Impact: 50.8)
  * `inet_create` **(Many-Argument Workhorses)** (Impact: 44.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 263 instances
* *State Mutation (weighted view):* 883
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 358`, `args: 64`, `func_start: 42`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 357`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 3`, `unreferenced_by_name: 10`
* *Architecture:* `io: 4`, `api: 18`, `import: 29`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.277
  * `Choke Point (Betweenness):` 0.001111 | `Ripple Effect (Closeness):` 0.012197
  * `Imports (Out-Degree: 46):` arp.h, segment.h, system.h, dev.h, icmp.h, inet.h, ip.h, config.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `drivers/char/serial.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.403)
- **Top Global Matches:** file_cluster_6: 6.403, file_cluster_4: 8.42, file_cluster_16: 15.658
- **Magnitude:** 1733.16 | **LOC:** 2076 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 1.108; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.7%), Complexity Load (formerly Cognitive Load) (73.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_serial_info` **(Many-Argument Workhorses)** (Impact: 69.1)
  * `rs_ioctl` **(Many-Argument Workhorses)** (Impact: 66.4)
  * `block_til_ready` **(Many-Argument Workhorses)** (Impact: 59.9)
    * *Intent:* /* * ------------------------------------------------------------ * rs_open() and friends * --------...
  * `startup` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `change_speed` **(Compute Cores)** (Impact: 36.1)
    * *Intent:* /* * This routine is called to set the UART divisor registers to match * the specified baud rate for...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 312 instances
* *State Mutation (weighted view):* 965
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 354`, `structural_boundaries: 243`, `args: 77`, `func_start: 43`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 341`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 16`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.108
  * `Choke Point (Betweenness):` 0.000994 | `Ripple Effect (Closeness):` 0.113843
  * `Imports (Out-Degree: 24):` bitops.h, io.h, segment.h, system.h, config.h, errno.h, fcntl.h, interrupt.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `drivers/char/tpqic02.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.118)
- **Top Global Matches:** file_cluster_8: 8.118, file_cluster_6: 8.615, file_cluster_4: 17.025
- **Magnitude:** 1667.14 | **LOC:** 2623 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 1.1; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.6%), Complexity Load (formerly Cognitive Load) (59.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_ioctl_cmd` **(Compute Cores)** (Impact: 93.5)
    * *Intent:* } /* do_qic_cmd */ /* Not all ioctls are supported for all drives. Some rely on * optional QIC-02 co...
  * `tape_qic02_ioctl` **(Many-Argument Workhorses)** (Impact: 81.1)
    * *Intent:* } /* tape_qic02_release */ /* ioctl allows user programs to rewind the tape and stuff like that */
  * `tape_qic02_read` **(Many-Argument Workhorses)** (Impact: 71.8)
    * *Intent:* * like 4k or so). * * Scott S. Bertilson suggested to continue filling the user buffer, rather * tha...
  * `tape_qic02_open` **(Many-Argument Workhorses)** (Impact: 71.8)
    * *Intent:* /* tape_qic02_open() * We allow the device to be opened, even if it is marked 'dead' because * we wa...
  * `tape_qic02_write` **(Many-Argument Workhorses)** (Impact: 62.6)
    * *Intent:* * If there is insufficient room, write as much as will fit and * return the amount written. If the r...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 275 instances
* *State Mutation (weighted view):* 843
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 374`, `structural_boundaries: 216`, `args: 160`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 293`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 7`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 1`, `import: 15`
* *Defense:* `doc: 29`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.1
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.002795
  * `Imports (Out-Degree: 22):` dma.h, io.h, segment.h, system.h, config.h, delay.h, errno.h, fcntl.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `drivers/scsi/st.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.368)
- **Top Global Matches:** file_cluster_3: 11.368, file_cluster_8: 14.014, file_cluster_6: 26.503
- **Magnitude:** 1515.58 | **LOC:** 1476 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `st_int_ioctl` **(Many-Argument Workhorses)** (Impact: 149.5)
    * *Intent:* count = total; /* Read only one variable length block */ } /* for (total = 0; total < count; ) */ SC...
  * `st_write` **(Many-Argument Workhorses)** (Impact: 122.4)
  * `st_read` **(Many-Argument Workhorses)** (Impact: 119.2)
  * `st_ioctl` **(Many-Argument Workhorses)** (Impact: 66.2)
  * `scsi_tape_open` **(Many-Argument Workhorses)** (Impact: 56.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 267 instances
* *State Mutation (weighted view):* 845
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 272`, `structural_boundaries: 139`, `args: 52`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 311`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` blk.h, segment.h, system.h, constants.h, errno.h, fcntl.h, fs.h, ioctl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/scsi/scsi.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.693)
- **Top Global Matches:** file_cluster_8: 7.693, file_cluster_3: 18.282, file_cluster_6: 18.925
- **Magnitude:** 1443.44 | **LOC:** 1721 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **8**; blast radius 1.59; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scsi_done` **(Compute Cores)** (Impact: 113.9)
    * *Intent:* * (2) Call internal_cmnd to requeue the command. This will result in * scsi_done being called again ...
  * `scan_scsis` **(I/O & Config Routines)** (Impact: 74.5)
    * *Intent:* /* * Detecting SCSI devices : * We scan all present host adapter's busses, from ID 0 to ID 6. * We u...
  * `allocate_device` **(Many-Argument Workhorses)** (Impact: 62.6)
    * *Intent:* of the packets for each device */
  * `request_queueable` **(Compute Cores)** (Impact: 41.3)
    * *Intent:* of the calling code to ensure that this is the case. */
  * `scsi_dev_init` **(Many-Argument Workhorses)** (Impact: 40.1)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 262 instances
* *State Mutation (weighted view):* 864
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 142`, `args: 69`, `func_start: 20`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 2`, `state_mutation: 340`, `fragile_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.59
  * `Choke Point (Betweenness):` 0.01177 | `Ripple Effect (Closeness):` 0.116879
  * `Imports (Out-Degree: 12):` blk.h, system.h, constants.h, hosts.h, sched.h, string.h, timer.h, scsi.h
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `mm/memory.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.835)
- **Top Global Matches:** file_cluster_6: 6.835, file_cluster_4: 8.243, file_cluster_9: 14.646
- **Magnitude:** 1442.14 | **LOC:** 1226 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **11**; blast radius 3.869; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.8%)
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
* *Amplified Cascading Flux:* 278 instances
* *State Mutation (weighted view):* 851
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 149`, `args: 54`, `func_start: 30`, `class_start: 11`
* *Risk/State:* `state_mutation: 295`, `planned_debt: 1`
* *Architecture:* `api: 32`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.869
  * `Choke Point (Betweenness):` 0.008023 | `Ripple Effect (Closeness):` 0.181051
  * `Imports (Out-Degree: 19):` system.h, config.h, errno.h, head.h, kernel.h, mman.h, ptrace.h, sched.h...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `net/inet/ip.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.077)
- **Top Global Matches:** file_cluster_6: 6.077, file_cluster_4: 7.567, file_cluster_16: 15.048
- **Magnitude:** 1417.86 | **LOC:** 1610 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **21**; blast radius 1.194; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.2%)
- **Documentation Coverage:** 97.619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_options` **(Many-Argument Workhorses)** (Impact: 71.4)
  * `ip_defrag` **(Many-Argument Workhorses)** (Impact: 53.3)
    * *Intent:* /* Process an incoming IP datagram fragment. */
  * `ip_rcv` **(Many-Argument Workhorses)** (Impact: 49.6)
    * *Intent:* #endif /* This function receives all incoming IP datagrams. */
  * `ip_forward` **(Many-Argument Workhorses)** (Impact: 42.2)
    * *Intent:* #ifdef CONFIG_IP_FORWARD /* Forward an IP datagram to its next destination. */
  * `ip_build_header` **(Many-Argument Workhorses)** (Impact: 38.6)
    * *Intent:* /* * This routine builds the appropriate hardware/IP headers for * the routine. It assumes that if *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 270 instances
* *State Mutation (weighted view):* 868
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 221`, `args: 37`, `func_start: 29`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 328`, `dead_code: 12`, `fragile_debt: 3`, `unreferenced_by_name: 8`
* *Architecture:* `api: 14`, `import: 21`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.194
  * `Choke Point (Betweenness):` 0.000213 | `Ripple Effect (Closeness):` 0.011181
  * `Imports (Out-Degree: 32):` arp.h, segment.h, system.h, dev.h, eth.h, icmp.h, inet.h, ip.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `drivers/scsi/NCR5380.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.179)
- **Top Global Matches:** file_cluster_8: 7.179, file_cluster_6: 14.862, file_cluster_3: 23.183
- **Magnitude:** 1330.94 | **LOC:** 2448 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 1.249; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.6%), Complexity Load (formerly Cognitive Load) (68.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NCR5380_information_transfer` **(Many-Argument Workhorses)** (Impact: 153.0)
    * *Intent:* * Purpose : run through the various SCSI phases and do as the target * directs us to. Operates on th...
  * `NCR5380_transfer_dma` **(Many-Argument Workhorses)** (Impact: 96.0)
    * *Intent:* * * Inputs : instance - instance of driver, *phase - pointer to * what phase is expected, *count - p...
  * `NCR5380_transfer_pio` **(Many-Argument Workhorses)** (Impact: 52.2)
    * *Intent:* * maximum number of bytes, 0 if all bytes or transfered or exit * is in same phase. * * Also, *phase...
  * `NCR5380_select` **(Many-Argument Workhorses)** (Impact: 47.0)
    * *Intent:* * Side effects : * If bus busy, arbitration failed, etc, NCR5380_select() will exit * with registers...
  * `NCR5380_reselect` **(Compute Cores)** (Impact: 29.0)
    * *Intent:* /* * Function : void NCR5380_reselect (struct Scsi_Host *instance) * * Purpose : does reselection, i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 227 instances
* *State Mutation (weighted view):* 717
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 118`, `args: 158`, `func_start: 23`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 263`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 16`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.249
  * `Choke Point (Betweenness):` 0.000103 | `Ripple Effect (Closeness):` 0.006289
  * `Imports (Out-Degree: 5):` delay.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `fs/nfs/proc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.005)
- **Top Global Matches:** file_cluster_4: 8.005, file_cluster_16: 8.204, file_cluster_9: 8.269
- **Magnitude:** 1292.3 | **LOC:** 874 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **9**; blast radius 1.386; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.1%)
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
* *Structure:* `branch: 173`, `structural_boundaries: 131`, `args: 41`, `func_start: 30`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 303`, `unreferenced_by_name: 15`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.386
  * `Choke Point (Betweenness):` 0.000961 | `Ripple Effect (Closeness):` 0.010482
  * `Imports (Out-Degree: 12):` config.h, errno.h, in.h, mm.h, nfs_fs.h, param.h, sched.h, string.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `fs/ext2/namei.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.967)
- **Top Global Matches:** file_cluster_8: 6.967, file_cluster_6: 15.856, file_cluster_3: 22.017
- **Magnitude:** 1252.2 | **LOC:** 1121 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.9%), Guard Balance (formerly Safety Score) (81.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_ext2_rename` **(Many-Argument Workhorses)** (Impact: 129.4)
    * *Intent:* /* * rename uses retrying to avoid race-conditions: at least they should be * minimal. * it tries to...
  * `ext2_find_entry` **(Many-Argument Workhorses)** (Impact: 58.4)
    * *Intent:* /* * ext2_find_entry() * * finds an entry in the specified directory with the wanted name. It * retu...
  * `ext2_add_entry` **(Many-Argument Workhorses)** (Impact: 54.9)
    * *Intent:* /* * ext2_add_entry() * * adds a file entry to the specified directory, using the same * semantics a...
  * `ext2_mknod` **(Many-Argument Workhorses)** (Impact: 52.6)
  * `ext2_rmdir` **(Many-Argument Workhorses)** (Impact: 42.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 218 instances
* *State Mutation (weighted view):* 689
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 159`, `args: 27`, `func_start: 16`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 253`, `fragile_debt: 5`, `unreferenced_by_name: 8`
* *Architecture:* `api: 9`, `import: 9`
* *Defense:* `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` segment.h, errno.h, ext2_fs.h, fcntl.h, fs.h, locks.h, sched.h, stat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/scsi/aha152x.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.859)
- **Top Global Matches:** file_cluster_6: 5.859, file_cluster_8: 11.988, file_cluster_4: 12.928
- **Magnitude:** 1178.16 | **LOC:** 2369 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `aha152x_intr` **(Many-Argument Workhorses)** (Impact: 231.6)
    * *Intent:* /* * Interrupts handler (main routine of the driver) */
  * `disp_ports` **(I/O & Config Routines)** (Impact: 80.8)
    * *Intent:* /* * Display registers of AIC-6260 */
  * `aha152x_detect` **(Compute Cores)** (Impact: 53.4)
  * `aha152x_abort` **(Many-Argument Workhorses)** (Impact: 35.4)
    * *Intent:* /* * Abort a queued command * (commands that are on the bus can't be aborted easily) */
  * `show_command` **(Compute Cores)** (Impact: 26.6)
    * *Intent:* #endif /* * Show the command data of a command */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 177 instances
* *State Mutation (weighted view):* 564
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 123`, `args: 414`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 210`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 13`, `import: 12`
* *Defense:* `test: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` blk.h, aha152x.h, io.h, system.h, constants.h, hosts.h, errno.h, ioport.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/exec.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.698)
- **Top Global Matches:** file_cluster_8: 9.698, file_cluster_3: 14.717, file_cluster_6: 22.062
- **Magnitude:** 1152.2 | **LOC:** 911 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **18**; blast radius 1.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.0%), Complexity Load (formerly Cognitive Load) (85.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_execve` **(Many-Argument Workhorses)** (Impact: 129.1)
    * *Intent:* /* * sys_execve() executes a new program. */
  * `copy_strings` **(Many-Argument Workhorses)** (Impact: 44.1)
    * *Intent:* * to be put directly into the top of new user memory. * * Modified by TYT, 11/24/91 to add the from_...
  * `core_dump` **(Many-Argument Workhorses)** (Impact: 43.9)
    * *Intent:* /* * Routine writes a core dump image in the current directory. * Currently only a stub-function. * ...
  * `load_aout_binary` **(Many-Argument Workhorses)** (Impact: 41.1)
    * *Intent:* /* * These are the functions used to load a.out style executables and shared * libraries. There is n...
  * `flush_old_exec` **(Compute Cores)** (Impact: 34.7)
    * *Intent:* /* * This function flushes out all traces of the currently running executable so * that a new one ca...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 231 instances
* *State Mutation (weighted view):* 705
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 80`, `args: 39`, `func_start: 13`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 243`, `unreferenced_by_name: 3`
* *Architecture:* `io: 6`, `api: 22`, `import: 19`
* *Defense:* `safety: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.00029 | `Ripple Effect (Closeness):` 0.006289
  * `Imports (Out-Degree: 30):` segment.h, system.h, a.out.h, binfmts.h, errno.h, fcntl.h, fs.h, kernel.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `drivers/block/cdu31a.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.347)
- **Top Global Matches:** file_cluster_4: 5.347, file_cluster_6: 9.245, file_cluster_16: 11.053
- **Magnitude:** 1146.76 | **LOC:** 1853 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **15**; blast radius 1.686; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%)
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
* *Amplified Cascading Flux:* 181 instances
* *State Mutation (weighted view):* 614
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 166`, `args: 92`, `func_start: 41`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 252`, `fragile_debt: 5`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.686
  * `Choke Point (Betweenness):` 0.003467 | `Ripple Effect (Closeness):` 0.147948
  * `Imports (Out-Degree: 22):` io.h, segment.h, system.h, blk.h, cdrom.h, cdu31a.h, errno.h, fs.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `fs/hpfs/hpfs_fs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.894)
- **Top Global Matches:** file_cluster_4: 5.894, file_cluster_16: 9.618, file_cluster_6: 10.943
- **Magnitude:** 1144.24 | **LOC:** 1725 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.8%), Complexity Load (formerly Cognitive Load) (74.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_opts` **(Many-Argument Workhorses)** (Impact: 90.4)
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
* *Structure:* `branch: 197`, `structural_boundaries: 249`, `args: 67`, `func_start: 37`, `class_start: 60`
* *Risk/State:* `state_mutation: 211`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 11`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` bitops.h, segment.h, hpfs.h, errno.h, fs.h, hpfs_fs.h, locks.h, malloc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/buffer.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.011)
- **Top Global Matches:** file_cluster_4: 5.011, file_cluster_6: 10.238, file_cluster_16: 10.49
- **Magnitude:** 1122.38 | **LOC:** 1026 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **76** in-repo importer(s); it depends on **10**; blast radius 10.825; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.5%), Complexity Load (formerly Cognitive Load) (80.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getblk` **(Many-Argument Workhorses)** (Impact: 47.6)
    * *Intent:* /* * Ok, this is getblk, and it isn't very clear, again to hinder * race-conditions. Most of the cod...
  * `sync_buffers` **(Compute Cores)** (Impact: 39.2)
    * *Intent:* before the writes have finished; fsync() may not. */
  * `set_blocksize` **(Compute Cores)** (Impact: 29.7)
  * `try_to_load_aligned` **(Many-Argument Workhorses)** (Impact: 25.0)
  * `check_aligned` **(Many-Argument Workhorses)** (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 212 instances
* *State Mutation (weighted view):* 650
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 160`, `args: 62`, `func_start: 36`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 226`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 25`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.825
  * `Choke Point (Betweenness):` 0.048707 | `Ripple Effect (Closeness):` 0.213369
  * `Imports (Out-Degree: 22):` io.h, system.h, config.h, errno.h, kernel.h, locks.h, major.h, sched.h...
  * `Imported By (In-Degree: 76):` (Excluded from Brief to save tokens)

### `fs/ext/namei.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.973)
- **Top Global Matches:** file_cluster_8: 8.973, file_cluster_6: 10.711, file_cluster_4: 18.812
- **Magnitude:** 1088.24 | **LOC:** 901 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.8%), Complexity Load (formerly Cognitive Load) (83.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_ext_rename` **(Many-Argument Workhorses)** (Impact: 90.3)
    * *Intent:* /* * rename uses retrying to avoid race-conditions: at least they should be minimal. * it tries to a...
  * `ext_add_entry` **(Many-Argument Workhorses)** (Impact: 59.4)
    * *Intent:* /* * ext_add_entry() * * adds a file entry to the specified directory, using the same * semantics as...
  * `ext_find_entry` **(Many-Argument Workhorses)** (Impact: 59.0)
    * *Intent:* /* * ext_find_entry() * * finds an entry in the specified directory with the wanted name. It * retur...
  * `ext_mknod` **(Many-Argument Workhorses)** (Impact: 49.4)
  * `ext_rmdir` **(Many-Argument Workhorses)** (Impact: 26.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 195 instances
* *State Mutation (weighted view):* 618
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 150`, `args: 16`, `func_start: 16`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 228`, `unreferenced_by_name: 8`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` segment.h, errno.h, ext_fs.h, fcntl.h, kernel.h, sched.h, stat.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/FPU-emu/reg_ld_str.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.122)
- **Top Global Matches:** file_cluster_6: 7.122, file_cluster_8: 13.107, file_cluster_4: 13.432
- **Magnitude:** 1083.2 | **LOC:** 1464 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 1.286; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.0%), Complexity Load (formerly Cognitive Load) (73.9%)
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
* *Amplified Cascading Flux:* 216 instances
* *State Mutation (weighted view):* 672
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 108`, `args: 76`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 240`, `unreferenced_by_name: 15`
* *Architecture:* `api: 20`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.286
  * `Choke Point (Betweenness):` 0.000364 | `Ripple Effect (Closeness):` 0.012481
  * `Imports (Out-Degree: 11):` segment.h, control_w.h, exception.h, fpu_emu.h, fpu_system.h, reg_constant.h, status_w.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `fs/sysv/namei.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.763)
- **Top Global Matches:** file_cluster_6: 6.763, file_cluster_4: 13.025, file_cluster_8: 13.143
- **Magnitude:** 1080.54 | **LOC:** 837 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.4%), Guard Balance (formerly Safety Score) (84.2%), Test Surface (formerly Verification) (80.0%)
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
* *Structure:* `branch: 157`, `structural_boundaries: 134`, `args: 16`, `func_start: 16`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 222`, `dead_code: 2`, `unreferenced_by_name: 8`
* *Architecture:* `api: 9`, `import: 7`
* *Defense:* `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` errno.h, fs.h, kernel.h, sched.h, stat.h, string.h, sysv_fs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/xiafs/namei.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.674)
- **Top Global Matches:** file_cluster_8: 5.674, file_cluster_6: 15.207, file_cluster_3: 21.767
- **Magnitude:** 1080.24 | **LOC:** 848 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.9%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` segment.h, errno.h, fcntl.h, kernel.h, sched.h, stat.h, string.h, xia_fs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs/minix/namei.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.896)
- **Top Global Matches:** file_cluster_6: 7.896, file_cluster_4: 8.415, file_cluster_9: 14.215
- **Magnitude:** 1055.06 | **LOC:** 829 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.3%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_minix_rename` **(Many-Argument Workhorses)** (Impact: 112.4)
    * *Intent:* /* * rename uses retrying to avoid race-conditions: at least they should be minimal. * it tries to a...
  * `minix_mknod` **(Many-Argument Workhorses)** (Impact: 49.3)
  * `minix_add_entry` **(Many-Argument Workhorses)** (Impact: 39.9)
    * *Intent:* /* * minix_add_entry() * * adds a file entry to the specified directory, returning a possible * erro...
  * `minix_rmdir` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `minix_unlink` **(Many-Argument Workhorses)** (Impact: 24.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 197 instances
* *State Mutation (weighted view):* 611
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 137`, `args: 16`, `func_start: 16`, `class_start: 44`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 217`, `unreferenced_by_name: 8`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` segment.h, errno.h, fcntl.h, kernel.h, minix_fs.h, sched.h, stat.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/scsi/seagate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.093)
- **Top Global Matches:** file_cluster_4: 6.093, file_cluster_16: 11.104, file_cluster_6: 11.14
- **Magnitude:** 1041.74 | **LOC:** 1712 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `internal_command` **(Many-Argument Workhorses)** (Impact: 379.1)
  * `seagate_st0x_biosparam` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* #ifdef CONFIG_BLK_DEV_SD #include <asm/segment.h> #include "sd.h" #include "scsi_ioctl.h"
  * `seagate_st0x_detect` **(Compute Cores)** (Impact: 24.6)
    * *Intent:* #endif /* def SLOW_HANDSHAKE */
  * `seagate_st0x_queue_command` **(Many-Argument Workhorses)** (Impact: 20.3)
  * `seagate_reconnect_intr` **(Stateful Encapsulated Methods)** (Impact: 12.0)
    * *Intent:* /* * The seagate_reconnect_intr routine is called when a target reselects the * host adapter. This o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 163 instances
* *State Mutation (weighted view):* 518
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 88`, `args: 36`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 192`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 10`, `import: 14`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` blk.h, io.h, segment.h, system.h, constants.h, hosts.h, config.h, sched.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `include/asm/segment.h` (C) | Magnitude: 95.3 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 118, structural_boundaries: 41, branch: 22, explicit_casts: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `kernel/mktime.c` (C) | Magnitude: 30.78 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 24, state_mutation: 8, pointers: 7, macros: 4
- `include/linux/sysv_fs.h` (C) | Magnitude: 98.4 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 134, structural_boundaries: 89, api: 55, args: 44
- `net/ddi.c` (C) | Magnitude: 32.32 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 16, pointers: 12, structural_boundaries: 10, import: 10
- `kernel/ldt.c` (C) | Magnitude: 93.88 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 59, branch: 19, structural_boundaries: 19, state_mutation: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `include/linux/tcp.h` (C) | Magnitude: 16.74 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 18, indent_tabs: 8, macros: 5, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `kernel/Makefile` (MAKEFILE) | Magnitude: 18.62 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: func_start: 14, indent_tabs: 12, unreferenced_by_name: 6, io: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `mm/swap.c` (C) | Magnitude: 856.58 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 549, state_mutation: 197, pointers: 171, branch: 158

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `drivers/FPU-emu/fpu_system.h` (C) | Magnitude: 16.68 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: macros: 29, args: 17, pointers: 9, reflection_metaprogramming: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `drivers/char/mouse.c` (C) | Magnitude: 47.86 | Delta: **0.136** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 14, pointers: 12, macros: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `fs/buffer.c` -> **Severity: 4.871** (Bridge: 0.0487 * Flux: 100.0%)
- `kernel/sched.c` -> **Severity: 3.473** (Bridge: 0.0347 * Flux: 100.0%)
- `include/linux/sched.h` -> **Severity: 3.061** (Bridge: 0.0318 * Flux: 96.1115%)
- `kernel/exit.c` -> **Severity: 2.583** (Bridge: 0.0258 * Flux: 100.0%)
- `drivers/char/tty_io.c` -> **Severity: 2.256** (Bridge: 0.0226 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `kernel/printk.c` -> **Severity: 28.281** (Embedded: 0.3329 * Error Risk: 84.9584%)
- `include/linux/sched.h` -> **Severity: 21.209** (Embedded: 0.3743 * Error Risk: 56.6567%)
- `kernel/sched.c` -> **Severity: 20.59** (Embedded: 0.2663 * Error Risk: 77.3186%)
- `include/asm/segment.h` -> **Severity: 19.614** (Embedded: 0.3226 * Error Risk: 60.8027%)
- `kernel/vsprintf.c` -> **Severity: 18.859** (Embedded: 0.2089 * Error Risk: 90.2704%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `include/linux/sched.h` -> **Severity: 2285.7** (Blast Radius: 22.857 * Doc Risk: 100.0%)
- `kernel/printk.c` -> **Severity: 1819.5** (Blast Radius: 18.195 * Doc Risk: 100.0%)
- `include/linux/string.h` -> **Severity: 1493.8** (Blast Radius: 14.938 * Doc Risk: 100.0%)
- `kernel/sched.c` -> **Severity: 1430.9** (Blast Radius: 14.309 * Doc Risk: 100.0%)
- `include/asm/segment.h` -> **Severity: 1403.8** (Blast Radius: 14.038 * Doc Risk: 100.0%)

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 99 literal sites + 38 sites through wrappers = 137
- **`panics_and_aborts`:** 147 literal sites + 38 sites through wrappers = 185

- `die` (function, debug_prints, primitive): 33 call sites in 1 files -- `tools/build.c`
- `die` (function, panics_and_aborts, primitive): 33 call sites in 1 files -- `tools/build.c`
- `die` (function, debug_prints, primitive): 5 call sites in 1 files -- `zBoot/xtract.c`
- `die` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `zBoot/xtract.c`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 12704 call pairs -- scoped 29.8%, unique 26.8%, ambiguous 0.3%, external 43.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 12593 | 29.8% | 27.0% | 0.3% | 42.9% |
| assembly | 97 | 35.1% | 2.1% | 0.0% | 62.9% |
| shell | 14 | 28.6% | 0.0% | 0.0% | 71.4% |

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
