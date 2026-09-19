# ARCHITECTURAL_BRIEF: darwin-xnu
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/apple/darwin-xnu.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 4054 analyzed artifact(s), 1209690 LOC.
- **Load-bearing artifact:** `bsd/sys/param.h` -- 403 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `iokit/Tests/Tests.cpp` -- pulls in 144 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `osfmk/vm/vm_map.c` at magnitude 17876.02 (structural weight, not risk).
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
| Total Artifacts | 4535 |
| Analyzed Artifacts (Scanned) | 4054 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 481 |
| Total LOC | 1209690 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 89.4% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5256 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1227 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.4463 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 188 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 2780 | 999054 | 68.6% |
| CPP | 310 | 103580 | 7.6% |
| PLAINTEXT | 260 | 0 | 6.4% |
| HTML | 254 | 19230 | 6.3% |
| MAKEFILE | 153 | 6981 | 3.8% |
| ASSEMBLY | 101 | 16325 | 2.5% |
| PYTHON | 65 | 24262 | 1.6% |
| XML | 46 | 0 | 1.1% |
| OBJECTIVE-C | 34 | 34286 | 0.8% |
| SHELL | 21 | 2637 | 0.5% |
| MARKDOWN | 15 | 0 | 0.4% |
| LUA | 7 | 950 | 0.2% |
| PERL | 3 | 559 | 0.1% |
| YACC | 2 | 340 | 0.0% |
| SWIFT | 1 | 1092 | 0.0% |
| BMS | 1 | 16 | 0.0% |
| REXX | 1 | 378 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `5.634`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +5.63; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 36%, Data / Markup / Trivial 21%, Large Core Modules (3) 16%, Many-Argument Workhorses Files 6%, Encapsulated Accessors Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3779 | 93.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 275 | 6.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 481*

**Composition by Extension & Reason:**
- `.defs`: 84x Excluded (Unsupported Extension: '.defs')
- `.2`: 73x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Lexical Monotony: High structural repetition detected in 2261 LOC), 1x Excluded (Machine-Generated Source Code Signature: 254 LOC)
- `no_extension`: 35x Excluded (Binary Format Detected), 13x Excluded (Unsupported Extension: '.entitlements'), 9x Unsupported Format (.undeterminable)
- `.exports`: 41x Excluded (Unsupported Extension: '.exports')
- `.gz`: 34x Excluded (Explicitly Denied Extension: '.gz')
- `.h`: 7x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 58 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1240 LOC)
- `.d`: 18x Unsupported Format (.d)
- `.arm64`: 17x Excluded (Unsupported Extension: '.arm64')
- `.x86_64`: 17x Excluded (Unsupported Extension: '.x86_64')
- `.iig`: 14x Excluded (Unsupported Extension: '.iig')
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.c`: 4x Excluded (Saturation: Line 40 exceeds 500 chars), 1x Excluded (Embedded Array/Matrix Payload: 3779 commas in 1022 LOC), 1x Excluded (Machine-Generated Source Code Signature: 10831 LOC)
- `.template`: 9x Excluded (Unsupported Extension: '.template')
- `.pbxproj`: 5x Excluded (Unsupported Extension: '.pbxproj'), 2x Unsupported Format (.pbxproj)
- `.sub`: 7x Excluded (Unsupported Extension: '.sub')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.6 | 21.6 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 39.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 18.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 19.1 | 4.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 29.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 42.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 331343 | 2419 | 163 | `EXTERNAL_HEADERS/AvailabilityInternal.h` |
| cleanup | 1156 | 310 | 0 | `libkern/c++/OSKext.cpp` |
| guards | 45607 | 1973 | 31 | `osfmk/arm/pmap.c` |
| danger | 11444 | 1041 | 6 | `tests/kqueue_file_tests.c` |
| concurrency | 2284 | 290 | 0 | `osfmk/tests/kernel_tests.c` |
| connectivity | 43470 | 2507 | 28 | `bsd/nfs/nfs.h` |
| io | 4140 | 467 | 1 | `osfmk/man/index.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2815 | 358 | 0 | `tests/vsock.c` |
| time | 221 | 67 | 0 | `bsd/nfs/nfs.h` |
| serialization | 5 | 3 | 0 | `libkdd/tests/Tests.swift` |
| regex | 242 | 58 | 0 | `libsyscall/xcodescripts/create-syscalls.pl` |
| events | 1766 | 299 | 0 | `bsd/vfs/vfs_cluster.c` |
| tests | 920 | 91 | 0 | `libkdd/tests/Tests.swift` |
| docs | 7545 | 400 | 0 | `bsd/net/kpi_interface.h` |
| debt | 7492 | 946 | 3 | `bsd/net/net_stubs.c` |
| mutation | 303013 | 2339 | 172 | `EXTERNAL_HEADERS/AvailabilityInternal.h` |
| dead_code | 14136 | 1439 | 9 | `bsd/net/if.c` |
| credential | 2 | 2 | 0 | `tests/poll_select_kevent_paired_fds.c` |
| threat | 17886 | 1284 | 10 | `bsd/vfs/vfs_syscalls.c` |
| ml_ai | 1635 | 253 | 0 | `bsd/kern/kern_sysctl.c` |
| ui | 4795 | 254 | 0 | `osfmk/man/mach_msg_header.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `osfmk/man/index.html` (Hits: 424)
- `bsd/kern/makesyscalls.sh` (Hits: 331)
- `config/generate_symbolset_plist.sh` (Hits: 79)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **param.h** (`bsd/sys/param.h`) — 403 inbound connections
2. **cdefs.h** (`bsd/sys/cdefs.h`) — 356 inbound connections
3. **systm.h** (`bsd/sys/systm.h`) — 322 inbound connections
4. **mach_types.h** (`osfmk/mach/mach_types.h`) — 291 inbound connections
5. **sysctl.h** (`bsd/sys/sysctl.h`) — 284 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Tests.cpp** (`iokit/Tests/Tests.cpp`) — 144 outbound dependencies
2. **bsd_init.c** (`bsd/kern/bsd_init.c`) — 91 outbound dependencies
3. **kern_exec.c** (`bsd/kern/kern_exec.c`) — 89 outbound dependencies
4. **dlil.c** (`bsd/net/dlil.c`) — 83 outbound dependencies
5. **startup.c** (`osfmk/kern/startup.c`) — 70 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `pf_test_rule` **(Many-Argument Workhorses)** (@ `bsd/net/pf.c`) -> Impact: **1414.0** | LOC: 1191
- `m_clalloc` **(Many-Argument Workhorses)** (@ `bsd/kern/uipc_mbuf.c`) -> Impact: **1254.7** | LOC: 2853
  * *Intent:* /* * Allocate some number of mbuf clusters and place on cluster freelist. */
- `dtrace_disx86` **(Many-Argument Workhorses)** (@ `bsd/dev/i386/dis_tables.c`) -> Impact: **1214.1** | LOC: 2458
  * *Intent:* /* * Dissassemble a single x86 or amd64 instruction. * * Mode determines the default operating mode (SIZE16, SIZE32 or SIZE64) * for interpreting inst...
- `vm_fault_internal` **(Many-Argument Workhorses)** (@ `osfmk/vm/vm_fault.c`) -> Impact: **1187.5** | LOC: 2121
- `vm_map_enter` **(Many-Argument Workhorses)** (@ `osfmk/vm/vm_map.c`) -> Impact: **1129.0** | LOC: 1178
- `ip_output_list` **(Many-Argument Workhorses)** (@ `bsd/netinet/ip_output.c`) -> Impact: **1055.0** | LOC: 1528
  * *Intent:* /* * IP output. The packet in mbuf chain m contains a skeletal IP * header (with len, off, ttl, proto, tos, src, dst). * The mbuf chain containing the...
- `tcp_input` **(Many-Argument Workhorses)** (@ `bsd/netinet/tcp_input.c`) -> Impact: **1038.5** | LOC: 2548
- `sys_fcntl_nocancel` **(Many-Argument Workhorses)** (@ `bsd/kern/kern_descrip.c`) -> Impact: **1024.9** | LOC: 2218
  * *Intent:* * VNOP_ALLOCATE:??? * [F_SETSIZE,F_RDADVISE] * EBADF * EINVAL * copyin:EFAULT * vnode_getwithref:??? * [F_RDAHEAD,F_NOCACHE] * EBADF * vnode_getwithre...
- `dtrace_dif_subr` **(Many-Argument Workhorses)** (@ `bsd/dev/dtrace/dtrace.c`) -> Impact: **1022.3** | LOC: 1553
  * *Intent:* /* * Emulate the execution of DTrace ID subroutines invoked by the call opcode. * Notice that we don't bother validating the proper number of argument...
- `ip6_output_list` **(Many-Argument Workhorses)** (@ `bsd/netinet6/ip6_output.c`) -> Impact: **985.8** | LOC: 1415
  * *Intent:* * IP6 output. Each packet in mbuf chain m contains a skeletal IP6 * header (with pri, len, nxt, hlim, src, dst). * This function may modify ver and hl...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `bsd/kern` | 113 | 126791.46 | 65.37% | 40.25% |
| `bsd/net` | 152 | 99369.68 | 30.83% | 19.81% |
| `osfmk/kern` | 203 | 72878.91 | 30.52% | 29.0% |
| `osfmk/vm` | 59 | 69145.36 | 36.52% | 18.95% |
| `bsd/netinet` | 96 | 65478.76 | 37.61% | 18.05% |
| `iokit/Kernel` | 73 | 64004.5 | 56.0% | 69.42% |
| `bsd/nfs` | 31 | 56455.5 | 47.86% | 11.69% |
| `bsd/vfs` | 26 | 55717.52 | 63.42% | 37.52% |
| `bsd/netinet6` | 66 | 47741.88 | 43.79% | 32.95% |
| `tests` | 267 | 28232.6 | 16.24% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `bsd/kern/subr_xxx.c` -> **100.0%** Exposure
- `bsd/net/net_stubs.c` -> **100.0%** Exposure
- `bsd/net/skywalk_stubs.c` -> **100.0%** Exposure
- `libkern/os/object.c` -> **100.0%** Exposure
- `bsd/sys/vm.h` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `EXTERNAL_HEADERS/AvailabilityInternal.h` -> **100.0%** Exposure
- `libkdd/kcdata_core.m` -> **100.0%** Exposure
- `SETUP/config/main.c` -> **100.0%** Exposure
- `SETUP/config/mkheaders.c` -> **100.0%** Exposure
- `SETUP/config/mkioconf.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `bsd/vfs/kpi_vfs.c` -> **195** Orphaned Functions | **0** Duplicates
- `iokit/Kernel/IOPMrootDomain.cpp` -> **185** Orphaned Functions | **2** Duplicates
- `iokit/Kernel/IOServicePM.cpp` -> **184** Orphaned Functions | **0** Duplicates
- `iokit/Kernel/IOService.cpp` -> **166** Orphaned Functions | **2** Duplicates
- `iokit/Kernel/IOUserClient.cpp` -> **151** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `25700` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `osfmk/vm/vm_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 17876.02 | **LOC:** 21972 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.7%), Complexity Load (formerly Cognitive Load) (92.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vm_map_enter` **(Many-Argument Workhorses)** (Impact: 1129.0)
  * `vm_map_lookup_locked` **(Many-Argument Workhorses)** (Impact: 571.4)
    * *Intent:* * If contended != NULL, *contended will be set to * true iff the thread had to spin or block to acqu...
  * `vm_map_enter_mem_object_helper` **(Many-Argument Workhorses)** (Impact: 570.6)
  * `vm_map_remap_extract` **(Many-Argument Workhorses)** (Impact: 437.6)
    * *Intent:* /* * Routine: vm_map_remap_extract * * Description: This routine returns a vm_entry list from a map....
  * `vm_map_enter_fourk` **(Many-Argument Workhorses)** (Impact: 435.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2363 instances
* *State Mutation (weighted view):* 7661
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3039`, `structural_boundaries: 828`, `args: 455`, `func_start: 196`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 2935`, `dead_code: 18`, `planned_debt: 7`, `fragile_debt: 31`, `unreferenced_by_name: 78`
* *Architecture:* `api: 183`, `import: 44`
* *Defense:* `safety: 368`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 39):` ipc_port.h, assert.h, backtrace.h, counter.h, exc_guard.h, kalloc.h, misc_protos.h, sched_prim.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/dev/dtrace/dtrace.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 16452.2 | **LOC:** 19416 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Complexity Load (formerly Cognitive Load) (93.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.4962% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dtrace_dif_subr` **(Many-Argument Workhorses)** (Impact: 1022.3)
    * *Intent:* /* * Emulate the execution of DTrace ID subroutines invoked by the call opcode. * Notice that we don...
  * `dtrace_difo_validate` **(Many-Argument Workhorses)** (Impact: 527.9)
    * *Intent:* /* * Validate a DTrace DIF object by checking the IR instructions. The following * rules are current...
  * `dtrace_ioctl` **(Many-Argument Workhorses)** (Impact: 491.8)
    * *Intent:* /*ARGSUSED*/
  * `dtrace_dif_emulate` **(Many-Argument Workhorses)** (Impact: 418.7)
    * *Intent:* /* * Emulate the execution of DTrace IR instructions specified by the given * DIF object. This funct...
  * `dtrace_probe` **(Many-Argument Workhorses)** (Impact: 414.8)
    * *Intent:* /* * If you're looking for the epicenter of DTrace, you just found it. This * is the function called...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2627 instances
* *State Mutation (weighted view):* 8223
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3166`, `structural_boundaries: 1661`, `args: 521`, `func_start: 264`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 104`, `state_mutation: 2969`, `planned_debt: 5`, `fragile_debt: 14`, `unreferenced_by_name: 8`
* *Architecture:* `api: 54`, `import: 34`
* *Defense:* `safety: 143`, `doc: 6`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` IOPlatformExpert.h, dtrace_xoroshiro128_plus.h, ast.h, cpu_data.h, monotonic.h, sched_prim.h, task.h, zalloc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `EXTERNAL_HEADERS/AvailabilityInternal.h` (OBJECTIVE-C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 14635.52 | **LOC:** 23427 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 6.221; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Complexity Load (formerly Cognitive Load) (48.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4663 instances
* *State Mutation (weighted view):* 14155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1546`
* *Risk/State:* `state_mutation: 4829`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.221
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.136233
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bsd/net/pf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 12928.44 | **LOC:** 10804 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **49**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.8%), Complexity Load (formerly Cognitive Load) (94.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pf_test_rule` **(Many-Argument Workhorses)** (Impact: 1414.0)
  * `pf_test_state_icmp` **(Many-Argument Workhorses)** (Impact: 496.9)
  * `pf_test_state_tcp` **(Many-Argument Workhorses)** (Impact: 486.2)
  * `pf_test6` **(Many-Argument Workhorses)** (Impact: 454.4)
  * `pf_test` **(Many-Argument Workhorses)** (Impact: 407.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1680 instances
* *State Mutation (weighted view):* 5219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2576`, `structural_boundaries: 1644`, `args: 256`, `func_start: 120`, `class_start: 380`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1859`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 11`, `unreferenced_by_name: 17`
* *Architecture:* `api: 88`, `import: 49`
* *Defense:* `safety: 6`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` randomdev.h, md5.h, libkern.h, thread_act.h, endian.h, bpf.h, dlil.h, ethernet.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/vfs/vfs_syscalls.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10925.7 | **LOC:** 13443 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **57**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.1%), Guard Balance (formerly Safety Score) (96.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mount_common` **(Many-Argument Workhorses)** (Impact: 660.3)
    * *Intent:* /* * common mount implementation (final stage of mounting) * * Arguments: * fstypename file system t...
  * `renameat_internal` **(Many-Argument Workhorses)** (Impact: 453.0)
    * *Intent:* /* * Rename files. Source and destination must either both be directories, * or both not be director...
  * `fsctl_internal` **(Many-Argument Workhorses)** (Impact: 234.1)
    * *Intent:* /* * Make a filesystem-specific control call: */ /* ARGSUSED */
  * `unlinkat_internal` **(Many-Argument Workhorses)** (Impact: 182.4)
    * *Intent:* /* * Delete a name from the filesystem. */ /* ARGSUSED */
  * `open1` **(Many-Argument Workhorses)** (Impact: 155.1)
    * *Intent:* * * Returns: 0 Success * EINVAL * EINTR * falloc:ENFILE * falloc:EMFILE * falloc:ENOMEM * vn_open_au...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1542 instances
* *State Mutation (weighted view):* 4856
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2042`, `structural_boundaries: 1181`, `args: 406`, `func_start: 217`, `class_start: 255`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 1772`, `dead_code: 11`, `planned_debt: 4`, `fragile_debt: 47`, `unreferenced_by_name: 92`
* *Architecture:* `io: 3`, `api: 163`, `concurrency: 1`, `import: 59`
* *Defense:* `safety: 47`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 53):` IOBSD.h, audit_kevents.h, host.h, ipc_misc.h, kalloc.h, kern_types.h, task.h, OSAtomic.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libkern/c++/OSKext.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10784.46 | **LOC:** 15434 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **44**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.5%)
- **Documentation Coverage:** 30.1158% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OSKext::load` **(Many-Argument Workhorses)** (Impact: 796.9)
    * *Intent:* /********************************************************************* *****************************...
  * `OSKext::jettisonLinkeditSegment` **(I/O & Config Routines)** (Impact: 468.4)
    * *Intent:* #endif /* VM_MAPPED_KEXTS */ /********************************************************************* ...
  * `OSKext::handleRequest` **(Many-Argument Workhorses)** (Impact: 411.4)
    * *Intent:* /********************************************************************* * XXX - this function is a bi...
  * `OSKext::copyInfo` **(Compute Cores)** (Impact: 291.6)
    * *Intent:* /********************************************************************* * Any info that needs to do a...
  * `OSKext::mapKCFileSet` **(Many-Argument Workhorses)** (Impact: 180.0)
    * *Intent:* #if defined(__x86_64__) || defined(__i386__) /******************************************************...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1414 instances
* *State Mutation (weighted view):* 4444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2397`, `structural_boundaries: 1191`, `args: 752`, `func_start: 255`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 127`, `state_mutation: 1616`, `dead_code: 8`, `planned_debt: 4`, `fragile_debt: 46`, `unreferenced_by_name: 131`
* *Architecture:* `io: 1`, `import: 44`
* *Defense:* `safety: 45`, `doc: 215`, `immutability_locks: 157`, `cleanup: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 38):` IOBSD.h, IOCatalogue.h, IOLib.h, IOPlatformExpert.h, IORegistryEntry.h, IOService.h, IOStatisticsPrivate.h, IOUserServer.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `osfmk/arm/pmap.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 10445.2 | **LOC:** 15781 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **53**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.1%), Complexity Load (formerly Cognitive Load) (91.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.454% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pmap_enter_options_internal` **(Many-Argument Workhorses)** (Impact: 392.5)
  * `pmap_page_protect_options_with_flush_range` **(Many-Argument Workhorses)** (Impact: 272.0)
    * *Intent:* /* * Routine: pmap_page_protect_options * * Function: * Lower the permission for all mappings to a g...
  * `pmap_protect_options_internal` **(Many-Argument Workhorses)** (Impact: 197.4)
  * `pmap_nest_internal` **(Many-Argument Workhorses)** (Impact: 162.2)
    * *Intent:* #endif /* HAS_APPLE_PAC */ /* * kern_return_t pmap_nest(grand, subord, vstart, size) * * grand = the...
  * `arm_force_fast_fault_with_flush_range` **(Many-Argument Workhorses)** (Impact: 145.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1412 instances
* *State Mutation (weighted view):* 4449
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2285`, `structural_boundaries: 1337`, `args: 775`, `func_start: 408`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 211`, `state_mutation: 1625`, `dead_code: 6`, `planned_debt: 7`, `fragile_debt: 6`, `unreferenced_by_name: 80`
* *Architecture:* `api: 326`, `import: 53`
* *Defense:* `safety: 165`, `doc: 23`, `test: 14`, `immutability_locks: 287`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 49):` IOHibernatePrivate.h, caches_internal.h, cpu_capabilities.h, cpu_data.h, cpu_data_internal.h, cpu_number.h, machine_cpu.h, misc_protos.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/nfs/nfs4_vnops.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 9366.58 | **LOC:** 9101 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nfs4_named_attr_get` **(Many-Argument Workhorses)** (Impact: 581.8)
    * *Intent:* * * Also, in an attempt to reduce the number of copies/variations of this code, * parts of the RPC b...
  * `nfs_advlock_setlock` **(Many-Argument Workhorses)** (Impact: 469.2)
    * *Intent:* /* * Acquire a file lock for the given range. * * Add the lock (request) to the lock queue. * Scan t...
  * `nfs4_open_rpc_internal` **(Many-Argument Workhorses)** (Impact: 362.0)
    * *Intent:* /* * common OPEN RPC code * * If create is set, ctx must be passed in. * Returns a node on success i...
  * `nfs_advlock_unlock` **(Many-Argument Workhorses)** (Impact: 211.1)
    * *Intent:* /* * Release all (same style) locks within the given range. */
  * `nfs4_claim_delegated_open_rpc` **(Many-Argument Workhorses)** (Impact: 175.0)
    * *Intent:* /* * Send an OPEN RPC to claim a delegated open for a file */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1331 instances
* *State Mutation (weighted view):* 4211
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1939`, `structural_boundaries: 718`, `args: 173`, `func_start: 97`, `class_start: 294`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1549`, `dead_code: 22`, `fragile_debt: 22`, `unreferenced_by_name: 40`
* *Architecture:* `io: 18`, `api: 97`, `import: 43`
* *Defense:* `safety: 15`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 43):` clock.h, sched_prim.h, task.h, OSAtomic.h, fifo.h, specdev.h, if.h, in.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `osfmk/vm/vm_pageout.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9030.04 | **LOC:** 10937 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.6%), Complexity Load (formerly Cognitive Load) (94.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vm_object_iopl_request` **(Many-Argument Workhorses)** (Impact: 557.7)
  * `upl_commit_range` **(Many-Argument Workhorses)** (Impact: 550.7)
  * `vm_object_upl_request` **(Many-Argument Workhorses)** (Impact: 539.2)
    * *Intent:* * the original object. If a page list structure * is not specified, this call is a no-op. * * Note: ...
  * `vm_map_create_upl` **(Many-Argument Workhorses)** (Impact: 268.9)
  * `upl_abort_range` **(Many-Argument Workhorses)** (Impact: 234.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1376 instances
* *State Mutation (weighted view):* 4408
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1732`, `structural_boundaries: 450`, `args: 229`, `func_start: 123`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 1656`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 4`, `unreferenced_by_name: 57`
* *Architecture:* `api: 147`, `import: 43`
* *Defense:* `safety: 190`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 36):` debug.h, counter.h, host_statistics.h, kalloc.h, kern_types.h, machine.h, misc_protos.h, policy_internal.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `iokit/Kernel/IOPMrootDomain.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 8934.42 | **LOC:** 12586 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **47**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.6%), Complexity Load (formerly Cognitive Load) (90.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.153% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IOPMrootDomain::evaluatePolicy` **(Many-Argument Workhorses)** (Impact: 215.4)
    * *Intent:* //****************************************************************************** // evaluatePolicy /...
  * `IOPMrootDomain::evaluateSystemSleepPolicy` **(Many-Argument Workhorses)** (Impact: 177.8)
  * `IOPMrootDomain::powerChangeDone` **(Many-Argument Workhorses)** (Impact: 168.5)
    * *Intent:* //****************************************************************************** // powerChangeDone ...
  * `IOPMrootDomain::handleOurPowerChangeStart` **(Many-Argument Workhorses)** (Impact: 150.7)
  * `IOPMrootDomain::setProperties` **(Compute Cores)** (Impact: 144.9)
    * *Intent:* //****************************************************************************** // setProperties //...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1199 instances
* *State Mutation (weighted view):* 3844
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2337`, `structural_boundaries: 799`, `args: 527`, `func_start: 275`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 124`, `state_mutation: 1446`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 185`
* *Architecture:* `api: 4`, `import: 47`
* *Defense:* `safety: 19`, `doc: 30`, `test: 26`, `sync_locks: 15`, `immutability_locks: 222`, `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 46):` AssertMacros.h, IOCPU.h, IOCatalogue.h, IOCommandGate.h, IODeviceTreeSupport.h, IOHibernatePrivate.h, IOKitDebug.h, IOKitKeys.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/vfs/vfs_subr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 8821.94 | **LOC:** 11424 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **53**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.9%), Guard Balance (formerly Safety Score) (94.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vnode_authattr` **(Many-Argument Workhorses)** (Impact: 311.0)
    * *Intent:* /* * Check that the attribute information in vap can be legally written by the * context. * * Call t...
  * `vn_authorize_renamex_with_paths` **(Many-Argument Workhorses)** (Impact: 229.7)
  * `vnode_authorize_callback_int` **(Many-Argument Workhorses)** (Impact: 180.9)
  * `vnode_create_internal` **(Many-Argument Workhorses)** (Impact: 167.6)
  * `vnode_authattr_new_internal` **(Many-Argument Workhorses)** (Impact: 148.9)
    * *Intent:* /* * Check that the attribute information in vattr can be legally applied to * a new file by the con...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1169 instances
* *State Mutation (weighted view):* 3659
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1936`, `structural_boundaries: 923`, `args: 328`, `func_start: 229`, `class_start: 131`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1321`, `dead_code: 15`, `planned_debt: 1`, `fragile_debt: 43`, `unreferenced_by_name: 88`
* *Architecture:* `api: 183`, `import: 56`
* *Defense:* `safety: 27`, `doc: 6`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 51):` video_console.h, panic_hooks.h, assert.h, clock.h, kalloc.h, sched_prim.h, thread.h, OSAtomic.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/kern/uipc_mbuf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 8432.96 | **LOC:** 8920 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.8%), Complexity Load (formerly Cognitive Load) (94.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `m_clalloc` **(Many-Argument Workhorses)** (Impact: 1254.7)
    * *Intent:* /* * Allocate some number of mbuf clusters and place on cluster freelist. */
  * `m_allocpacket_internal` **(Many-Argument Workhorses)** (Impact: 248.8)
    * *Intent:* /* * Return list of mbuf linked by m_nextpkt. Try for numlist, and if * wantall is not set, return w...
  * `slab_free` **(Many-Argument Workhorses)** (Impact: 130.8)
    * *Intent:* /* * Place a slab of object(s) back into a class's slab list. */
  * `m_copyback0` **(Many-Argument Workhorses)** (Impact: 129.4)
  * `m_copym_with_hdrs` **(Many-Argument Workhorses)** (Impact: 100.0)
    * *Intent:* /* * Equivalent to m_copym except that all necessary mbuf hdrs are allocated * within this routine a...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1248 instances
* *State Mutation (weighted view):* 3894
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1405`, `structural_boundaries: 820`, `args: 725`, `func_start: 153`, `class_start: 141`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 1398`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 44`
* *Architecture:* `api: 101`, `import: 32`
* *Defense:* `safety: 25`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` IOMapper.h, randomdev.h, backtrace.h, kern_types.h, percpu.h, queue.h, sched_prim.h, simple_lock.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/netkey/key.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 8097.72 | **LOC:** 10513 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `key_spdadd` **(Many-Argument Workhorses)** (Impact: 226.2)
    * *Intent:* * add a entry to SP database, when received * <base, address(SD), (lifetime(H),) policy> * from the ...
  * `key_setsaval` **(Many-Argument Workhorses)** (Impact: 132.6)
    * *Intent:* /* * copy SA values from PF_KEY message except *SPI, SEQ, PID, STATE and TYPE*. * You must update th...
  * `key_cmpspidx_withmask` **(Many-Argument Workhorses)** (Impact: 131.5)
    * *Intent:* /* * compare two secindex structure with mask. * IN: * spidx0: source, it is often in SPD. * spidx1:...
  * `key_parse` **(Many-Argument Workhorses)** (Impact: 125.8)
    * *Intent:* /* * parse sadb_msg buffer to process PFKEYv2, * and create a data to response if needed. * I think ...
  * `key_timehandler` **(I/O & Config Routines)** (Impact: 125.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1239 instances
* *State Mutation (weighted view):* 3891
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1836`, `structural_boundaries: 1932`, `args: 280`, `func_start: 128`, `class_start: 401`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 1413`, `dead_code: 10`, `planned_debt: 1`, `fragile_debt: 71`, `unreferenced_by_name: 19`
* *Architecture:* `api: 44`, `import: 44`
* *Defense:* `safety: 15`, `immutability_locks: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` locks.h, rand.h, endian.h, if.h, net_osdep.h, pfkeyv2.h, raw_cb.h, route.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/nfs/nfs_vnops.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 7775.96 | **LOC:** 8840 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nfs_vnop_write` **(Many-Argument Workhorses)** (Impact: 220.6)
    * *Intent:* /* * NFS write call */
  * `nfs_close` **(Many-Argument Workhorses)** (Impact: 189.0)
    * *Intent:* /* * nfs_close(): common function that does all the heavy lifting of file closure * * Takes an open ...
  * `nfs_vnop_setattr` **(Compute Cores)** (Impact: 159.4)
    * *Intent:* /* * NFS setattr call. */
  * `nfs_vnop_pageout` **(Many-Argument Workhorses)** (Impact: 158.0)
    * *Intent:* /* * vnode OP for pageout using UPL * * No buffer I/O, just RPCs straight from the mapped pages. * F...
  * `nfs_dir_buf_cache_lookup` **(Many-Argument Workhorses)** (Impact: 148.3)
    * *Intent:* /* * Look up a name in a directory's buffers. * Note: should only be called with RDIRPLUS directory ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1267 instances
* *State Mutation (weighted view):* 3936
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1764`, `structural_boundaries: 657`, `args: 148`, `func_start: 76`, `class_start: 243`
* *Risk/State:* `safety_bypasses: 250`, `state_mutation: 1402`, `dead_code: 27`, `fragile_debt: 24`, `unreferenced_by_name: 14`
* *Architecture:* `api: 107`, `import: 43`
* *Defense:* `safety: 25`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 43):` clock.h, sched_prim.h, task.h, OSAtomic.h, fifo.h, specdev.h, if.h, in.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `osfmk/vm/vm_resident.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 7511.6 | **LOC:** 9854 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **42**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vm_page_find_contiguous` **(Many-Argument Workhorses)** (Impact: 342.4)
    * *Intent:* #endif
  * `hibernate_page_list_setall` **(Many-Argument Workhorses)** (Impact: 258.8)
    * *Intent:* /* * Bits zero in the bitmaps => page needs to be saved. All pages default to be saved, * pages know...
  * `vm_page_insert_internal` **(Many-Argument Workhorses)** (Impact: 208.5)
  * `vm_page_free_list` **(Many-Argument Workhorses)** (Impact: 131.9)
    * *Intent:* /* * Free a list of pages. The list can be up to several hundred pages, * as blocked up by vm_pageou...
  * `vm_page_do_delayed_work` **(Many-Argument Workhorses)** (Impact: 101.6)
    * *Intent:* * collections of pages that don't require any work brokered by the * vm_page_queue_lock... to mitiga...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1212 instances
* *State Mutation (weighted view):* 3839
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1560`, `structural_boundaries: 421`, `args: 295`, `func_start: 139`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 1415`, `dead_code: 6`, `planned_debt: 4`, `fragile_debt: 7`, `unreferenced_by_name: 53`
* *Architecture:* `api: 133`, `import: 42`
* *Defense:* `safety: 292`, `test: 8`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` IOHibernatePrivate.h, cpu_internal.h, debug.h, misc_protos.h, counter.h, host_statistics.h, kalloc.h, ledger.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/nfs/nfs_socket.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 7292.16 | **LOC:** 7122 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nfs_connect` **(Many-Argument Workhorses)** (Impact: 479.3)
    * *Intent:* * * Search for a location to connect a socket to and initialize the connection. * * An NFS mount may...
  * `nfs_request_finish` **(Many-Argument Workhorses)** (Impact: 232.4)
    * *Intent:* /* * Finish up an NFS request by dequeueing it and * doing the initial NFS request reply processing....
  * `nfs_aux_request` **(Many-Argument Workhorses)** (Impact: 189.0)
  * `nfs_send` **(Many-Argument Workhorses)** (Impact: 179.8)
    * *Intent:* * - send the request * * If sent successfully, R_MUSTRESEND and R_RESENDERR are cleared. * rexmit co...
  * `nfs4_cb_handler` **(Many-Argument Workhorses)** (Impact: 167.3)
    * *Intent:* /* * Handle an NFS callback channel request. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1111 instances
* *State Mutation (weighted view):* 3393
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1603`, `structural_boundaries: 726`, `args: 157`, `func_start: 83`, `class_start: 154`
* *Risk/State:* `state_mutation: 1171`, `dead_code: 11`, `fragile_debt: 13`, `unreferenced_by_name: 10`
* *Architecture:* `api: 112`, `import: 37`
* *Defense:* `safety: 15`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` clock.h, task.h, thread.h, thread_call.h, OSAtomic.h, in.h, tcp.h, krpc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/net/dlil.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 7275.18 | **LOC:** 10702 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **83**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.3%)
- **Documentation Coverage:** 97.3214% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dlil_output` **(Many-Argument Workhorses)** (Impact: 316.0)
    * *Intent:* * Caller should have a lock on the protocol domain if the protocol * doesn't support finer grained l...
  * `dlil_input_packet_list_common` **(Many-Argument Workhorses)** (Impact: 181.2)
  * `ifnet_attach` **(Many-Argument Workhorses)** (Impact: 131.6)
  * `ifnet_enqueue_ifclassq` **(Many-Argument Workhorses)** (Impact: 108.4)
  * `dlil_rxpoll_input_thread_cont` **(Many-Argument Workhorses)** (Impact: 102.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1020 instances
* *State Mutation (weighted view):* 3266
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1494`, `structural_boundaries: 1431`, `args: 486`, `func_start: 232`, `class_start: 240`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1226`, `dead_code: 9`, `fragile_debt: 4`, `unreferenced_by_name: 82`
* *Architecture:* `api: 155`, `import: 83`
* *Defense:* `safety: 26`, `doc: 7`, `immutability_locks: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 81):` randomdev.h, assert.h, locks.h, sched_prim.h, task.h, thread.h, zalloc.h, OSAtomic.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/kern/uipc_socket.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6994.44 | **LOC:** 8016 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **57**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.3%), Guard Balance (formerly Safety Score) (96.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `soreceive` **(Many-Argument Workhorses)** (Impact: 540.4)
    * *Intent:* * sbwait:EBADF * sbwait:EINTR * sodelayed_copy:EFAULT * <pru_rcvoob>:EINVAL[TCP] * <pru_rcvoob>:EWOU...
  * `sosetoptlock` **(Many-Argument Workhorses)** (Impact: 474.6)
    * *Intent:* * sooptcopyin:EINVAL * sooptcopyin:EFAULT * sooptcopyin_timeval:EINVAL * sooptcopyin_timeval:EFAULT ...
  * `sosend` **(Many-Argument Workhorses)** (Impact: 305.3)
    * *Intent:* * <pru_send>:ENOBUFS[TCP] * <pru_send>:???[TCP] [ignorable: mostly IPSEC/firewall/DLIL] * <pru_send>...
  * `sogetoptlock` **(Many-Argument Workhorses)** (Impact: 250.8)
    * *Intent:* /* * Return: 0 Success * ENOPROTOOPT * <pr_ctloutput>:EOPNOTSUPP[AF_UNIX] * <pr_ctloutput>:??? * <sf...
  * `soreceive_list` **(Many-Argument Workhorses)** (Impact: 224.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 967 instances
* *State Mutation (weighted view):* 2989
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1496`, `structural_boundaries: 753`, `args: 214`, `func_start: 112`, `class_start: 133`
* *Risk/State:* `state_mutation: 1055`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 37`
* *Architecture:* `api: 87`, `import: 58`
* *Defense:* `safety: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 56):` assert.h, locks.h, policy_internal.h, task.h, zalloc.h, OSAtomic.h, section_keywords.h, limits.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/vfs/vfs_cluster.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 6880.9 | **LOC:** 7508 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cluster_io` **(Many-Argument Workhorses)** (Impact: 531.9)
  * `cluster_read_copy` **(Many-Argument Workhorses)** (Impact: 363.5)
  * `cluster_read_direct` **(Many-Argument Workhorses)** (Impact: 295.9)
  * `cluster_write_copy` **(Many-Argument Workhorses)** (Impact: 290.0)
  * `cluster_write_direct` **(Many-Argument Workhorses)** (Impact: 209.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1056 instances
* *State Mutation (weighted view):* 3256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1084`, `structural_boundaries: 455`, `args: 237`, `func_start: 70`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1144`, `dead_code: 2`, `fragile_debt: 5`, `unreferenced_by_name: 9`
* *Architecture:* `api: 35`, `import: 31`
* *Defense:* `safety: 19`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` kalloc.h, policy_internal.h, task.h, OSAtomic.h, libkern.h, mach_types.h, memory_object_types.h, upl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/kern/kern_memorystatus.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6843.36 | **LOC:** 8574 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **42**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `memorystatus_cmd_get_jetsam_snapshot` **(Many-Argument Workhorses)** (Impact: 751.4)
  * `memorystatus_update` **(Many-Argument Workhorses)** (Impact: 192.1)
    * *Intent:* * memlimit_active_is_fatal When a process is active and exceeds its memory footprint, * this describ...
  * `memorystatus_update_priority_locked` **(Many-Argument Workhorses)** (Impact: 168.2)
    * *Intent:* * - if the 'jetsam aging policy' is NOT 'legacy': * When this flag is TRUE, it means we are going * ...
  * `memorystatus_dirty_set` **(Many-Argument Workhorses)** (Impact: 136.8)
  * `memorystatus_control` **(Many-Argument Workhorses)** (Impact: 130.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 897 instances
* *State Mutation (weighted view):* 2826
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1425`, `structural_boundaries: 497`, `args: 276`, `func_start: 136`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1032`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 33`
* *Architecture:* `api: 85`, `concurrency: 1`, `import: 42`
* *Defense:* `safety: 113`, `sync_locks: 2`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` IOBSD.h, task_corpse.h, assert.h, debug.h, host.h, kalloc.h, locks.h, policy_internal.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/nfs/nfs_vfsops.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 6776.86 | **LOC:** 6775 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **40**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mountnfs` **(Many-Argument Workhorses)** (Impact: 572.8)
    * *Intent:* #define NFS_MAX_SUPPORTED_VERSION ((long)(sizeof (maxminorverstab) / sizeof (uint32_t) - 1)) #define...
  * `nfs_convert_old_nfs_args` **(Many-Argument Workhorses)** (Impact: 378.4)
    * *Intent:* #endif /* NO_MOUNT_PRIVATE */ #endif /* * Convert old style NFS mount args to XDR. */
  * `nfs_vfs_sysctl` **(Many-Argument Workhorses)** (Impact: 373.5)
    * *Intent:* /* * Do that sysctl thang... */
  * `nfs_mirror_mount_domount` **(Many-Argument Workhorses)** (Impact: 256.1)
    * *Intent:* #if CONFIG_TRIGGERS /* * We've detected a file system boundary on the server and * need to mount a n...
  * `nfs4_mount` **(Many-Argument Workhorses)** (Impact: 222.2)
    * *Intent:* /* Set up an NFSv4 mount */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 974 instances
* *State Mutation (weighted view):* 3071
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1431`, `structural_boundaries: 468`, `args: 136`, `func_start: 49`, `class_start: 107`
* *Risk/State:* `state_mutation: 1123`, `dead_code: 10`, `fragile_debt: 8`, `unreferenced_by_name: 6`
* *Architecture:* `api: 70`, `import: 40`
* *Defense:* `safety: 26`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 40):` OSAtomic.h, if.h, route.h, in.h, krpc.h, nfs.h, nfs_conf.h, nfs_gss.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `iokit/Kernel/IOService.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 6144.82 | **LOC:** 8388 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **38**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.7%), Complexity Load (formerly Cognitive Load) (91.1%), Debt Markers (formerly Tech Debt) (81.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IOService::matchInternal` **(Many-Argument Workhorses)** (Impact: 181.4)
  * `IOService::probeCandidates` **(Many-Argument Workhorses)** (Impact: 178.3)
    * *Intent:* /* * Alloc and probe matching classes, * called on the provider instance */
  * `IOService::updateConsoleUsers` **(Many-Argument Workhorses)** (Impact: 103.3)
  * `IOService::copyExistingServices` **(Many-Argument Workhorses)** (Impact: 99.0)
    * *Intent:* // internal - call with gNotificationLock
  * `IOService::matchPassive` **(Many-Argument Workhorses)** (Impact: 80.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 916 instances
* *State Mutation (weighted view):* 2885
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1409`, `structural_boundaries: 576`, `args: 415`, `func_start: 251`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 123`, `high_risk_execution: 2`, `state_mutation: 1053`, `dead_code: 6`, `planned_debt: 7`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 166`
* *Architecture:* `import: 39`
* *Defense:* `safety: 36`, `doc: 2`, `sync_locks: 13`, `immutability_locks: 192`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 36):` AppleKeyStoreInterface.h, IOBSD.h, IOCPU.h, IOCatalogue.h, IOCommand.h, IODeviceMemory.h, IODeviceTreeSupport.h, IOHibernatePrivate.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `osfmk/vm/vm_fault.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 6074.94 | **LOC:** 8030 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **41**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.2%), Guard Balance (formerly Safety Score) (89.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.1039% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vm_fault_internal` **(Many-Argument Workhorses)** (Impact: 1187.5)
  * `vm_fault_page` **(Many-Argument Workhorses)** (Impact: 831.4)
  * `vm_fault_cs_handle_violation` **(Many-Argument Workhorses)** (Impact: 214.8)
    * *Intent:* /* * Handles a code signing violation by either rejecting the page or forcing a disconnect. * @param...
  * `vm_fault_copy` **(Many-Argument Workhorses)** (Impact: 175.5)
    * *Intent:* * destination map. * * Results: * Returns KERN_SUCCESS if no errors were encountered in * reading or...
  * `vm_fault_enqueue_page` **(Many-Argument Workhorses)** (Impact: 123.0)
    * *Intent:* /* * Enqueue the page on the appropriate paging queue. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 649 instances
* *State Mutation (weighted view):* 2044
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1161`, `structural_boundaries: 328`, `args: 157`, `func_start: 58`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 746`, `dead_code: 9`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 43`, `import: 41`
* *Defense:* `safety: 136`, `doc: 7`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 39):` backtrace.h, counter.h, host.h, host_statistics.h, kern_types.h, mach_param.h, macro_help.h, misc_protos.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `iokit/Kernel/IOMemoryDescriptor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5684.94 | **LOC:** 5964 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.6%), Complexity Load (formerly Cognitive Load) (93.2%), Debt Markers (formerly Tech Debt) (67.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IOGeneralMemoryDescriptor::initWithOptions` **(Many-Argument Workhorses)** (Impact: 320.2)
    * *Intent:* /* * initWithOptions: * * IOMemoryDescriptor. The buffer is made up of several virtual address range...
  * `IOGeneralMemoryDescriptor::dmaCommandOperation` **(Many-Argument Workhorses)** (Impact: 229.1)
  * `IOGeneralMemoryDescriptor::memoryReferenceMapNew` **(Many-Argument Workhorses)** (Impact: 174.9)
    * *Intent:* #define LOGUNALIGN 0
  * `IOGeneralMemoryDescriptor::memoryReferenceMap` **(Many-Argument Workhorses)** (Impact: 171.5)
  * `IOGeneralMemoryDescriptor::wireVirtual` **(Many-Argument Workhorses)** (Impact: 143.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 896 instances
* *State Mutation (weighted view):* 2727
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1202`, `structural_boundaries: 332`, `args: 235`, `func_start: 132`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 935`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 99`
* *Architecture:* `import: 33`
* *Defense:* `safety: 52`, `doc: 1`, `sync_locks: 22`, `immutability_locks: 25`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` IODMACommand.h, IOKitDebug.h, IOKitKeysPrivate.h, IOLib.h, IOMapper.h, IOMemoryDescriptor.h, IOMultiMemoryDescriptor.h, IOSubMemoryDescriptor.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/kern/kern_event.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5661.36 | **LOC:** 9153 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **59**; blast radius 0.102; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.5%)
- **Documentation Coverage:** 91.1051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filt_wlupdate` **(Many-Argument Workhorses)** (Impact: 157.8)
    * *Intent:* #define EVFILT_WORKLOOP_EFAULT_RETRY_COUNT 100 #define FILT_WLATTACH 0 #define FILT_WLTOUCH 1 #defin...
  * `kevent_internal` **(Many-Argument Workhorses)** (Impact: 134.4)
    * *Intent:* * @brief * Common kevent code. * * @discussion * Needs to be inlined to specialize for legacy or mod...
  * `kevent_register` **(Many-Argument Workhorses)** (Impact: 130.4)
    * *Intent:* /* * kevent_register - add a new event to a kqueue * * Creates a mapping between the event source an...
  * `kqworkloop_update_threads_qos` **(Many-Argument Workhorses)** (Impact: 112.4)
  * `kqueue_process` **(Many-Argument Workhorses)** (Impact: 79.2)
    * *Intent:* * * caller holds a reference on the kqueue. * kqueue locked on entry and exit - but may be dropped *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 773 instances
* *State Mutation (weighted view):* 2422
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1143`, `structural_boundaries: 1256`, `args: 352`, `func_start: 232`, `class_start: 215`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 876`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 31`
* *Architecture:* `api: 106`, `import: 63`
* *Defense:* `safety: 128`, `doc: 48`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 53):` assert.h, ast.h, clock.h, cpu_data.h, kalloc.h, kcdata.h, locks.h, policy_internal.h...
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

- `osfmk/i386/cpu_data.h` -> **Severity: 0.186** (Bridge: 0.0019 * Flux: 99.8948%)
- `osfmk/kern/thread.h` -> **Severity: 0.087** (Bridge: 0.0101 * Flux: 8.6515%)
- `EXTERNAL_HEADERS/corecrypto/cc.h` -> **Severity: 0.069** (Bridge: 0.0007 * Flux: 99.9998%)
- `osfmk/arm64/monotonic.h` -> **Severity: 0.063** (Bridge: 0.0007 * Flux: 94.0548%)
- `bsd/sys/event.h` -> **Severity: 0.053** (Bridge: 0.0012 * Flux: 44.9622%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `bsd/sys/cdefs.h` -> **Severity: 15.359** (Embedded: 0.2839 * Error Risk: 54.1064%)
- `EXTERNAL_HEADERS/AvailabilityInternal.h` -> **Severity: 13.277** (Embedded: 0.1362 * Error Risk: 97.4586%)
- `EXTERNAL_HEADERS/Availability.h` -> **Severity: 10.716** (Embedded: 0.1832 * Error Risk: 58.5068%)
- `osfmk/kern/queue.h` -> **Severity: 10.26** (Embedded: 0.1093 * Error Risk: 93.841%)
- `libkern/os/overflow.h` -> **Severity: 9.388** (Embedded: 0.1254 * Error Risk: 74.8553%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `bsd/sys/types.h` -> **Severity: 963.1** (Blast Radius: 9.631 * Doc Risk: 100.0%)
- `libkern/libkern/c++/intrusive_shared_ptr.h` -> **Severity: 415.7** (Blast Radius: 4.157 * Doc Risk: 100.0%)
- `osfmk/mach/port.h` -> **Severity: 402.4** (Blast Radius: 4.024 * Doc Risk: 100.0%)
- `osfmk/mach/message.h` -> **Severity: 354.7** (Blast Radius: 3.547 * Doc Risk: 100.0%)
- `libkern/libkern/c++/bounded_ptr.h` -> **Severity: 334.8** (Blast Radius: 3.348 * Doc Risk: 100.0%)

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
