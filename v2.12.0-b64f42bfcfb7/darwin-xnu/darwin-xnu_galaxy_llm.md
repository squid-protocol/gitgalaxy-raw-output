# ARCHITECTURAL_BRIEF: darwin-xnu
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/apple/darwin-xnu.git` |
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
- **Scope:** 4058 analyzed artifact(s), 1221653 LOC.
- **Load-bearing artifact:** `libsyscall/wrappers/_libc_funcptr.c` -- 546 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `iokit/Tests/Tests.cpp` -- pulls in 144 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `osfmk/vm/vm_map.c` at magnitude 17414.62 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 4058 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 477 |
| Total LOC | 1221653 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 89.5% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4874 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1127 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 31.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.4392 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 145 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 2768 | 1011950 | 68.2% |
| CPP | 335 | 106684 | 8.3% |
| PLAINTEXT | 262 | 0 | 6.5% |
| HTML | 254 | 19230 | 6.3% |
| MAKEFILE | 153 | 6981 | 3.8% |
| ASSEMBLY | 101 | 16325 | 2.5% |
| PYTHON | 65 | 24262 | 1.6% |
| XML | 45 | 0 | 1.1% |
| OBJECTIVE-C | 25 | 30249 | 0.6% |
| SHELL | 21 | 2637 | 0.5% |
| MARKDOWN | 14 | 0 | 0.3% |
| LUA | 7 | 950 | 0.2% |
| PERL | 3 | 559 | 0.1% |
| YACC | 2 | 340 | 0.0% |
| SWIFT | 1 | 1092 | 0.0% |
| BMS | 1 | 16 | 0.0% |
| REXX | 1 | 378 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 4057 |
| cp1252 | cp1252-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 36%, Data / Markup / Trivial 21%, Large Core Modules (3) 15%, Many-Argument Workhorses Files 7%, Encapsulated Accessors Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3782 | 93.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 276 | 6.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 477*

**Composition by Extension & Reason:**
- `.defs`: 84x Excluded (Unsupported Extension: '.defs')
- `.2`: 73x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 254 LOC)
- `no_extension`: 35x Excluded (Binary Format Detected), 13x Excluded (Unsupported Extension: '.entitlements'), 9x Unsupported Format (.undeterminable)
- `.exports`: 41x Excluded (Unsupported Extension: '.exports')
- `.gz`: 34x Excluded (Explicitly Denied Extension: '.gz')
- `.h`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 58 LOC)
- `.d`: 18x Unsupported Format (.d)
- `.arm64`: 17x Excluded (Unsupported Extension: '.arm64')
- `.x86_64`: 17x Excluded (Unsupported Extension: '.x86_64')
- `.iig`: 14x Excluded (Unsupported Extension: '.iig')
- `.c`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 547 LOC)
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.template`: 9x Excluded (Unsupported Extension: '.template')
- `.pbxproj`: 5x Excluded (Unsupported Extension: '.pbxproj'), 2x Unsupported Format (.pbxproj)
- `.sub`: 7x Excluded (Unsupported Extension: '.sub')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.6 | 18.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.1 | 30.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 19.8 | 5.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 28.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 42.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 20494 | 1101 | 5 | `EXTERNAL_HEADERS/AvailabilityInternal.h` |
| cleanup | 1159 | 312 | 0 | `libkern/c++/OSKext.cpp` |
| guards | 46273 | 1984 | 31 | `osfmk/arm/pmap.c` |
| danger | 12225 | 1084 | 7 | `tests/kqueue_file_tests.c` |
| concurrency | 2259 | 276 | 0 | `osfmk/tests/kernel_tests.c` |
| connectivity | 44254 | 2607 | 28 | `bsd/nfs/nfs.h` |
| io | 4133 | 462 | 1 | `osfmk/man/index.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2850 | 363 | 0 | `tests/vsock.c` |
| time | 219 | 67 | 0 | `bsd/nfs/nfs.h` |
| serialization | 5 | 3 | 0 | `libkdd/tests/Tests.swift` |
| regex | 242 | 58 | 0 | `libsyscall/xcodescripts/create-syscalls.pl` |
| events | 1766 | 299 | 0 | `bsd/vfs/vfs_cluster.c` |
| tests | 920 | 91 | 0 | `libkdd/tests/Tests.swift` |
| docs | 8246 | 402 | 0 | `bsd/net/kpi_interface.h` |
| debt | 7453 | 948 | 3 | `bsd/net/net_stubs.c` |
| mutation | 303865 | 2343 | 169 | `EXTERNAL_HEADERS/AvailabilityInternal.h` |
| dead_code | 12787 | 1335 | 8 | `bsd/vfs/kpi_vfs.c` |
| credential | 2 | 2 | 0 | `tests/poll_select_kevent_paired_fds.c` |
| threat | 22 | 4 | 0 | `EXTERNAL_HEADERS/corecrypto/ccdigest.h` |
| ml_ai | 1666 | 253 | 0 | `bsd/kern/kern_sysctl.c` |
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

1. **_libc_funcptr.c** (`libsyscall/wrappers/_libc_funcptr.c`) — 546 inbound connections
2. **param.h** (`bsd/sys/param.h`) — 404 inbound connections
3. **cdefs.h** (`bsd/sys/cdefs.h`) — 360 inbound connections
4. **printf.c** (`osfmk/kern/printf.c`) — 352 inbound connections
5. **systm.h** (`bsd/sys/systm.h`) — 323 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Tests.cpp** (`iokit/Tests/Tests.cpp`) — 144 outbound dependencies
2. **bsd_init.c** (`bsd/kern/bsd_init.c`) — 91 outbound dependencies
3. **kern_exec.c** (`bsd/kern/kern_exec.c`) — 89 outbound dependencies
4. **dlil.c** (`bsd/net/dlil.c`) — 83 outbound dependencies
5. **startup.c** (`osfmk/kern/startup.c`) — 70 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `tcp_input` **(Many-Argument Workhorses)** (@ `bsd/netinet/tcp_input.c`) -> Impact: **1442.2** | LOC: 3591
- `pf_test_rule` **(Many-Argument Workhorses)** (@ `bsd/net/pf.c`) -> Impact: **1382.8** | LOC: 1191
- `m_clalloc` **(Many-Argument Workhorses)** (@ `bsd/kern/uipc_mbuf.c`) -> Impact: **1248.7** | LOC: 2853
  * *Intent:* /* * Allocate some number of mbuf clusters and place on cluster freelist. */
- `dtrace_disx86` **(Many-Argument Workhorses)** (@ `bsd/dev/i386/dis_tables.c`) -> Impact: **1202.0** | LOC: 2458
  * *Intent:* /* * Dissassemble a single x86 or amd64 instruction. * * Mode determines the default operating mode (SIZE16, SIZE32 or SIZE64) * for interpreting inst...
- `vm_fault_internal` **(Many-Argument Workhorses)** (@ `osfmk/vm/vm_fault.c`) -> Impact: **1171.7** | LOC: 2121
- `vm_map_enter` **(Many-Argument Workhorses)** (@ `osfmk/vm/vm_map.c`) -> Impact: **1084.1** | LOC: 1178
- `necp_application_find_policy_match_internal` **(Many-Argument Workhorses)** (@ `bsd/net/necp.c`) -> Impact: **1013.9** | LOC: 837
- `sys_fcntl_nocancel` **(Many-Argument Workhorses)** (@ `bsd/kern/kern_descrip.c`) -> Impact: **988.9** | LOC: 2218
  * *Intent:* * VNOP_ALLOCATE:??? * [F_SETSIZE,F_RDADVISE] * EBADF * EINVAL * copyin:EFAULT * vnode_getwithref:??? * [F_RDAHEAD,F_NOCACHE] * EBADF * vnode_getwithre...
- `dtrace_dif_subr` **(Many-Argument Workhorses)** (@ `bsd/dev/dtrace/dtrace.c`) -> Impact: **948.8** | LOC: 1553
  * *Intent:* /* * Emulate the execution of DTrace ID subroutines invoked by the call opcode. * Notice that we don't bother validating the proper number of argument...
- `ip_output_list` **(Many-Argument Workhorses)** (@ `bsd/netinet/ip_output.c`) -> Impact: **930.6** | LOC: 1528
  * *Intent:* /* * IP output. The packet in mbuf chain m contains a skeletal IP * header (with len, off, ttl, proto, tos, src, dst). * The mbuf chain containing the...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `bsd/kern` | 113 | 123651.96 | 63.85% | 38.35% |
| `bsd/net` | 153 | 109385.32 | 27.9% | 17.91% |
| `osfmk/kern` | 203 | 69060.36 | 26.22% | 27.44% |
| `osfmk/vm` | 59 | 66399.82 | 32.54% | 18.04% |
| `bsd/netinet` | 96 | 64656.92 | 33.76% | 16.77% |
| `iokit/Kernel` | 73 | 62581.6 | 53.92% | 67.76% |
| `bsd/nfs` | 31 | 55594.1 | 42.64% | 11.1% |
| `bsd/vfs` | 28 | 54625.44 | 57.88% | 37.22% |
| `bsd/netinet6` | 66 | 46617.18 | 42.3% | 30.91% |
| `tests` | 268 | 27834.22 | 14.92% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `bsd/kern/subr_xxx.c` -> **100.0%** Exposure
- `bsd/net/net_stubs.c` -> **100.0%** Exposure
- `bsd/net/skywalk_stubs.c` -> **100.0%** Exposure
- `bsd/vfs/vfs_support.c` -> **100.0%** Exposure
- `libkern/os/object.c` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `libkdd/kcdata_core.m` -> **100.0%** Exposure
- `SETUP/config/main.c` -> **100.0%** Exposure
- `SETUP/config/mkheaders.c` -> **100.0%** Exposure
- `SETUP/config/mkioconf.c` -> **100.0%** Exposure
- `SETUP/config/mkmakefile.c` -> **100.0%** Exposure
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
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `25787` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `osfmk/vm/vm_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.944)
- **Top Global Matches:** file_cluster_6: 7.944, file_cluster_8: 9.623, file_cluster_4: 15.745
- **Magnitude:** 17414.62 | **LOC:** 21972 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **72** in-repo importer(s); it depends on **43**; blast radius 0.456; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vm_map_enter` **(Many-Argument Workhorses)** (Impact: 1084.1)
  * `vm_map_lookup_locked` **(Many-Argument Workhorses)** (Impact: 553.4)
    * *Intent:* * If contended != NULL, *contended will be set to * true iff the thread had to spin or block to acqu...
  * `vm_map_enter_mem_object_helper` **(Many-Argument Workhorses)** (Impact: 542.6)
  * `vm_map_remap_extract` **(Many-Argument Workhorses)** (Impact: 428.1)
    * *Intent:* /* * Routine: vm_map_remap_extract * * Description: This routine returns a vm_entry list from a map....
  * `vm_map_enter_fourk` **(Many-Argument Workhorses)** (Impact: 413.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2317 instances
* *State Mutation (weighted view):* 7569
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2861`, `structural_boundaries: 827`, `args: 455`, `func_start: 196`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 2935`, `dead_code: 26`, `planned_debt: 7`, `fragile_debt: 31`, `unreferenced_by_name: 78`
* *Architecture:* `api: 183`, `import: 44`
* *Defense:* `safety: 368`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.13598
  * `Imports (Out-Degree: 85):` ipc_port.h, assert.h, backtrace.h, counter.h, exc_guard.h, kalloc.h, misc_protos.h, sched_prim.h...
  * `Imported By (In-Degree: 72):` (Excluded from Brief to save tokens)

### `bsd/dev/dtrace/dtrace.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.24)
- **Top Global Matches:** file_cluster_6: 6.24, file_cluster_4: 9.454, file_cluster_8: 16.355
- **Magnitude:** 16276.3 | **LOC:** 19416 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **33**; blast radius 0.153; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.1%)
- **Documentation Coverage:** 99.4962% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dtrace_dif_subr` **(Many-Argument Workhorses)** (Impact: 948.8)
    * *Intent:* /* * Emulate the execution of DTrace ID subroutines invoked by the call opcode. * Notice that we don...
  * `dtrace_difo_validate` **(Many-Argument Workhorses)** (Impact: 527.9)
    * *Intent:* /* * Validate a DTrace DIF object by checking the IR instructions. The following * rules are current...
  * `dtrace_ioctl` **(Many-Argument Workhorses)** (Impact: 491.8)
    * *Intent:* /*ARGSUSED*/
  * `dtrace_dif_emulate` **(Many-Argument Workhorses)** (Impact: 418.7)
    * *Intent:* /* * Emulate the execution of DTrace IR instructions specified by the given * DIF object. This funct...
  * `dtrace_probe` **(Many-Argument Workhorses)** (Impact: 396.3)
    * *Intent:* /* * If you're looking for the epicenter of DTrace, you just found it. This * is the function called...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2609 instances
* *State Mutation (weighted view):* 8187
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3054`, `structural_boundaries: 1661`, `args: 521`, `func_start: 264`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 104`, `state_mutation: 2969`, `planned_debt: 5`, `fragile_debt: 14`, `unreferenced_by_name: 8`
* *Architecture:* `api: 54`, `import: 34`
* *Defense:* `safety: 143`, `doc: 6`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.108918
  * `Imports (Out-Degree: 65):` IOPlatformExpert.h, dtrace_xoroshiro128_plus.h, ast.h, cpu_data.h, monotonic.h, sched_prim.h, task.h, zalloc.h...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `bsd/net/pf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.037)
- **Top Global Matches:** file_cluster_8: 8.037, file_cluster_6: 10.675, file_cluster_4: 18.847
- **Magnitude:** 12571.84 | **LOC:** 10804 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **49**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pf_test_rule` **(Many-Argument Workhorses)** (Impact: 1382.8)
  * `pf_test_state_tcp` **(Many-Argument Workhorses)** (Impact: 486.2)
  * `pf_test_state_icmp` **(Many-Argument Workhorses)** (Impact: 469.9)
  * `pf_test6` **(Many-Argument Workhorses)** (Impact: 412.7)
  * `pf_test` **(Many-Argument Workhorses)** (Impact: 365.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1638 instances
* *State Mutation (weighted view):* 5135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2425`, `structural_boundaries: 1644`, `args: 256`, `func_start: 120`, `class_start: 380`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1859`, `planned_debt: 3`, `fragile_debt: 11`, `unreferenced_by_name: 17`
* *Architecture:* `api: 88`, `import: 49`
* *Defense:* `safety: 6`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.065939
  * `Imports (Out-Degree: 88):` randomdev.h, md5.h, libkern.h, thread_act.h, endian.h, bpf.h, dlil.h, ethernet.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `bsd/net/necp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.089)
- **Top Global Matches:** file_cluster_6: 6.089, file_cluster_4: 12.511, file_cluster_8: 12.84
- **Magnitude:** 11851.98 | **LOC:** 10831 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **45**; blast radius 0.124; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `necp_application_find_policy_match_internal` **(Many-Argument Workhorses)** (Impact: 1013.9)
  * `necp_socket_check_policy` **(Many-Argument Workhorses)** (Impact: 836.4)
  * `necp_socket_is_allowed_to_send_recv_internal` **(Many-Argument Workhorses)** (Impact: 367.6)
  * `necp_policy_apply` **(Many-Argument Workhorses)** (Impact: 345.8)
  * `necp_socket_find_policy_match_with_info_locked` **(Many-Argument Workhorses)** (Impact: 311.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1235 instances
* *State Mutation (weighted view):* 3891
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2647`, `structural_boundaries: 1892`, `args: 438`, `func_start: 187`, `class_start: 234`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 1421`, `unreferenced_by_name: 30`
* *Architecture:* `api: 56`, `import: 45`
* *Defense:* `safety: 81`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.124
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.084909
  * `Imports (Out-Degree: 91):` IOBSD.h, cchmac.h, ccsha2.h, cs_blobs.h, rand.h, loader.h, flowhash.h, if.h...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `bsd/vfs/vfs_syscalls.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.477)
- **Top Global Matches:** file_cluster_6: 6.477, file_cluster_4: 8.22, file_cluster_16: 16.304
- **Magnitude:** 10389.8 | **LOC:** 13443 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **59** in-repo importer(s); it depends on **57**; blast radius 0.531; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mount_common` **(Many-Argument Workhorses)** (Impact: 574.1)
    * *Intent:* /* * common mount implementation (final stage of mounting) * * Arguments: * fstypename file system t...
  * `renameat_internal` **(Many-Argument Workhorses)** (Impact: 427.5)
    * *Intent:* /* * Rename files. Source and destination must either both be directories, * or both not be director...
  * `fsctl_internal` **(Many-Argument Workhorses)** (Impact: 231.4)
    * *Intent:* /* * Make a filesystem-specific control call: */ /* ARGSUSED */
  * `unlinkat_internal` **(Many-Argument Workhorses)** (Impact: 150.7)
    * *Intent:* /* * Delete a name from the filesystem. */ /* ARGSUSED */
  * `open1` **(Many-Argument Workhorses)** (Impact: 143.8)
    * *Intent:* * * Returns: 0 Success * EINVAL * EINTR * falloc:ENFILE * falloc:EMFILE * falloc:ENOMEM * vn_open_au...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1504 instances
* *State Mutation (weighted view):* 4780
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1820`, `structural_boundaries: 1181`, `args: 406`, `func_start: 217`, `class_start: 255`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 1772`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 47`, `unreferenced_by_name: 92`
* *Architecture:* `io: 3`, `api: 163`, `concurrency: 1`, `import: 59`
* *Defense:* `safety: 47`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.111918
  * `Imports (Out-Degree: 109):` IOBSD.h, audit_kevents.h, host.h, ipc_misc.h, kalloc.h, kern_types.h, task.h, OSAtomic.h...
  * `Imported By (In-Degree: 59):` (Excluded from Brief to save tokens)

### `libkern/c++/OSKext.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.089)
- **Top Global Matches:** file_cluster_6: 7.089, file_cluster_4: 9.773, file_cluster_8: 16.848
- **Magnitude:** 10262.06 | **LOC:** 15434 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **44**; blast radius 0.21; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.5%), Guard Balance (formerly Safety Score) (69.4%)
- **Documentation Coverage:** 30.1158% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OSKext::load` **(Many-Argument Workhorses)** (Impact: 678.9)
    * *Intent:* /********************************************************************* *****************************...
  * `OSKext::jettisonLinkeditSegment` **(I/O & Config Routines)** (Impact: 424.4)
    * *Intent:* #endif /* VM_MAPPED_KEXTS */ /********************************************************************* ...
  * `OSKext::handleRequest` **(Many-Argument Workhorses)** (Impact: 396.4)
    * *Intent:* /********************************************************************* * XXX - this function is a bi...
  * `OSKext::copyInfo` **(Compute Cores)** (Impact: 284.5)
    * *Intent:* /********************************************************************* * Any info that needs to do a...
  * `OSKext::mapKCFileSet` **(Many-Argument Workhorses)** (Impact: 180.0)
    * *Intent:* #if defined(__x86_64__) || defined(__i386__) /******************************************************...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1385 instances
* *State Mutation (weighted view):* 4386
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2111`, `structural_boundaries: 1191`, `args: 752`, `func_start: 255`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 127`, `state_mutation: 1616`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 46`, `unreferenced_by_name: 131`
* *Architecture:* `io: 1`, `import: 44`
* *Defense:* `safety: 45`, `doc: 215`, `immutability_locks: 157`, `cleanup: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.21
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.107378
  * `Imports (Out-Degree: 101):` IOBSD.h, IOCatalogue.h, IOLib.h, IOPlatformExpert.h, IORegistryEntry.h, IOService.h, IOStatisticsPrivate.h, IOUserServer.h...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `osfmk/arm/pmap.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.006)
- **Top Global Matches:** file_cluster_4: 7.006, file_cluster_12: 10.673, file_cluster_16: 11.583
- **Magnitude:** 9437.1 | **LOC:** 15781 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **53**; blast radius 0.261; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.5%)
- **Documentation Coverage:** 97.454% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pmap_enter_options_internal` **(Many-Argument Workhorses)** (Impact: 341.5)
  * `pmap_page_protect_options_with_flush_range` **(Many-Argument Workhorses)** (Impact: 254.1)
    * *Intent:* /* * Routine: pmap_page_protect_options * * Function: * Lower the permission for all mappings to a g...
  * `pmap_protect_options_internal` **(Many-Argument Workhorses)** (Impact: 155.1)
  * `arm_force_fast_fault_with_flush_range` **(Many-Argument Workhorses)** (Impact: 141.4)
  * `pmap_nest_internal` **(Many-Argument Workhorses)** (Impact: 122.0)
    * *Intent:* #endif /* HAS_APPLE_PAC */ /* * kern_return_t pmap_nest(grand, subord, vstart, size) * * grand = the...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1301 instances
* *State Mutation (weighted view):* 4227
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1636`, `structural_boundaries: 1335`, `args: 775`, `func_start: 408`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 211`, `state_mutation: 1625`, `dead_code: 3`, `planned_debt: 7`, `fragile_debt: 6`, `unreferenced_by_name: 82`
* *Architecture:* `api: 326`, `import: 53`
* *Defense:* `safety: 165`, `doc: 23`, `test: 14`, `immutability_locks: 287`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.127202
  * `Imports (Out-Degree: 79):` IOHibernatePrivate.h, caches_internal.h, cpu_capabilities.h, cpu_data.h, cpu_data_internal.h, cpu_number.h, machine_cpu.h, misc_protos.h...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `bsd/nfs/nfs4_vnops.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.829)
- **Top Global Matches:** file_cluster_8: 5.829, file_cluster_6: 15.932, file_cluster_3: 21.041
- **Magnitude:** 9295.98 | **LOC:** 9101 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **43**; blast radius 0.105; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.1%), Guard Balance (formerly Safety Score) (75.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nfs4_named_attr_get` **(Many-Argument Workhorses)** (Impact: 581.8)
    * *Intent:* * * Also, in an attempt to reduce the number of copies/variations of this code, * parts of the RPC b...
  * `nfs_advlock_setlock` **(Many-Argument Workhorses)** (Impact: 462.9)
    * *Intent:* /* * Acquire a file lock for the given range. * * Add the lock (request) to the lock queue. * Scan t...
  * `nfs4_open_rpc_internal` **(Many-Argument Workhorses)** (Impact: 358.5)
    * *Intent:* /* * common OPEN RPC code * * If create is set, ctx must be passed in. * Returns a node on success i...
  * `nfs_advlock_unlock` **(Many-Argument Workhorses)** (Impact: 205.5)
    * *Intent:* /* * Release all (same style) locks within the given range. */
  * `nfs4_readdir_rpc` **(Many-Argument Workhorses)** (Impact: 173.6)
    * *Intent:* /* * NFS V4 readdir RPC. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1331 instances
* *State Mutation (weighted view):* 4211
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1895`, `structural_boundaries: 718`, `args: 173`, `func_start: 97`, `class_start: 294`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1549`, `dead_code: 10`, `fragile_debt: 22`, `unreferenced_by_name: 40`
* *Architecture:* `io: 18`, `api: 97`, `import: 43`
* *Defense:* `safety: 15`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.105
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.071544
  * `Imports (Out-Degree: 74):` clock.h, sched_prim.h, task.h, OSAtomic.h, fifo.h, specdev.h, if.h, in.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `osfmk/vm/vm_pageout.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.394)
- **Top Global Matches:** file_cluster_6: 5.394, file_cluster_4: 11.748, file_cluster_8: 13.023
- **Magnitude:** 8697.24 | **LOC:** 10937 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **43**; blast radius 0.188; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `upl_commit_range` **(Many-Argument Workhorses)** (Impact: 545.1)
  * `vm_object_iopl_request` **(Many-Argument Workhorses)** (Impact: 506.7)
  * `vm_object_upl_request` **(Many-Argument Workhorses)** (Impact: 494.2)
    * *Intent:* * the original object. If a page list structure * is not specified, this call is a no-op. * * Note: ...
  * `vm_map_create_upl` **(Many-Argument Workhorses)** (Impact: 250.9)
  * `upl_abort_range` **(Many-Argument Workhorses)** (Impact: 232.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1343 instances
* *State Mutation (weighted view):* 4342
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1553`, `structural_boundaries: 450`, `args: 229`, `func_start: 123`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 1656`, `dead_code: 6`, `planned_debt: 4`, `fragile_debt: 4`, `unreferenced_by_name: 57`
* *Architecture:* `api: 147`, `import: 43`
* *Defense:* `safety: 190`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.188
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.12068
  * `Imports (Out-Degree: 78):` debug.h, counter.h, host_statistics.h, kalloc.h, kern_types.h, machine.h, misc_protos.h, policy_internal.h...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `iokit/Kernel/IOPMrootDomain.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.668)
- **Top Global Matches:** file_cluster_6: 6.668, file_cluster_4: 8.706, file_cluster_12: 16.372
- **Magnitude:** 8646.62 | **LOC:** 12586 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **47**; blast radius 0.123; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.7%)
- **Documentation Coverage:** 97.153% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IOPMrootDomain::evaluatePolicy` **(Many-Argument Workhorses)** (Impact: 198.0)
    * *Intent:* //****************************************************************************** // evaluatePolicy /...
  * `IOPMrootDomain::evaluateSystemSleepPolicy` **(Many-Argument Workhorses)** (Impact: 175.8)
  * `IOPMrootDomain::powerChangeDone` **(Many-Argument Workhorses)** (Impact: 141.6)
    * *Intent:* //****************************************************************************** // powerChangeDone ...
  * `IOPMrootDomain::handleOurPowerChangeStart` **(Many-Argument Workhorses)** (Impact: 138.4)
  * `IOPMrootDomain::dispatchPowerEvent` **(Many-Argument Workhorses)** (Impact: 137.3)
    * *Intent:* //****************************************************************************** // dispatchPowerEve...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1169 instances
* *State Mutation (weighted view):* 3784
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2137`, `structural_boundaries: 799`, `args: 527`, `func_start: 275`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 124`, `state_mutation: 1446`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 185`
* *Architecture:* `api: 4`, `import: 47`
* *Defense:* `safety: 19`, `doc: 30`, `test: 26`, `sync_locks: 15`, `immutability_locks: 222`, `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.107489
  * `Imports (Out-Degree: 98):` AssertMacros.h, IOCPU.h, IOCatalogue.h, IOCommandGate.h, IODeviceTreeSupport.h, IOHibernatePrivate.h, IOKitDebug.h, IOKitKeys.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `bsd/vfs/vfs_subr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.423)
- **Top Global Matches:** file_cluster_6: 5.423, file_cluster_4: 10.094, file_cluster_8: 14.841
- **Magnitude:** 8615.84 | **LOC:** 11424 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **92** in-repo importer(s); it depends on **53**; blast radius 0.413; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vnode_authattr` **(Many-Argument Workhorses)** (Impact: 304.3)
    * *Intent:* /* * Check that the attribute information in vap can be legally written by the * context. * * Call t...
  * `vn_authorize_renamex_with_paths` **(Many-Argument Workhorses)** (Impact: 226.3)
  * `vnode_authorize_callback_int` **(Many-Argument Workhorses)** (Impact: 176.0)
  * `vnode_create_internal` **(Many-Argument Workhorses)** (Impact: 155.3)
  * `vnode_authattr_new_internal` **(Many-Argument Workhorses)** (Impact: 144.0)
    * *Intent:* /* * Check that the attribute information in vattr can be legally applied to * a new file by the con...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1150 instances
* *State Mutation (weighted view):* 3621
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1818`, `structural_boundaries: 923`, `args: 328`, `func_start: 229`, `class_start: 131`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1321`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 43`, `unreferenced_by_name: 88`
* *Architecture:* `api: 183`, `import: 56`
* *Defense:* `safety: 27`, `doc: 6`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.117651
  * `Imports (Out-Degree: 101):` video_console.h, panic_hooks.h, assert.h, clock.h, kalloc.h, sched_prim.h, thread.h, OSAtomic.h...
  * `Imported By (In-Degree: 92):` (Excluded from Brief to save tokens)

### `bsd/kern/uipc_mbuf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.169)
- **Top Global Matches:** file_cluster_6: 7.169, file_cluster_4: 12.644, file_cluster_8: 13.889
- **Magnitude:** 8390.06 | **LOC:** 8920 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **95** in-repo importer(s); it depends on **32**; blast radius 0.335; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `m_clalloc` **(Many-Argument Workhorses)** (Impact: 1248.7)
    * *Intent:* /* * Allocate some number of mbuf clusters and place on cluster freelist. */
  * `m_allocpacket_internal` **(Many-Argument Workhorses)** (Impact: 248.8)
    * *Intent:* /* * Return list of mbuf linked by m_nextpkt. Try for numlist, and if * wantall is not set, return w...
  * `slab_free` **(Many-Argument Workhorses)** (Impact: 130.8)
    * *Intent:* /* * Place a slab of object(s) back into a class's slab list. */
  * `m_copyback0` **(Many-Argument Workhorses)** (Impact: 126.8)
  * `m_copym_with_hdrs` **(Many-Argument Workhorses)** (Impact: 100.0)
    * *Intent:* /* * Equivalent to m_copym except that all necessary mbuf hdrs are allocated * within this routine a...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1245 instances
* *State Mutation (weighted view):* 3888
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1346`, `structural_boundaries: 820`, `args: 725`, `func_start: 153`, `class_start: 141`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 1398`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 44`
* *Architecture:* `api: 101`, `import: 32`
* *Defense:* `safety: 25`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.335
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.102169
  * `Imports (Out-Degree: 59):` IOMapper.h, randomdev.h, backtrace.h, kern_types.h, percpu.h, queue.h, sched_prim.h, simple_lock.h...
  * `Imported By (In-Degree: 95):` (Excluded from Brief to save tokens)

### `bsd/netkey/key.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.614)
- **Top Global Matches:** file_cluster_8: 5.614, file_cluster_6: 14.376, file_cluster_3: 22.591
- **Magnitude:** 8033.02 | **LOC:** 10513 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **43**; blast radius 0.127; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.2%), Guard Balance (formerly Safety Score) (73.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `key_spdadd` **(Many-Argument Workhorses)** (Impact: 224.2)
    * *Intent:* * add a entry to SP database, when received * <base, address(SD), (lifetime(H),) policy> * from the ...
  * `key_cmpspidx_withmask` **(Many-Argument Workhorses)** (Impact: 131.5)
    * *Intent:* /* * compare two secindex structure with mask. * IN: * spidx0: source, it is often in SPD. * spidx1:...
  * `key_setsaval` **(Many-Argument Workhorses)** (Impact: 128.6)
    * *Intent:* /* * copy SA values from PF_KEY message except *SPI, SEQ, PID, STATE and TYPE*. * You must update th...
  * `key_parse` **(Many-Argument Workhorses)** (Impact: 124.0)
    * *Intent:* /* * parse sadb_msg buffer to process PFKEYv2, * and create a data to response if needed. * I think ...
  * `key_timehandler` **(I/O & Config Routines)** (Impact: 122.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1230 instances
* *State Mutation (weighted view):* 3873
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1777`, `structural_boundaries: 1932`, `args: 280`, `func_start: 128`, `class_start: 401`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 1413`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 71`, `unreferenced_by_name: 19`
* *Architecture:* `api: 44`, `import: 44`
* *Defense:* `safety: 15`, `immutability_locks: 106`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.073933
  * `Imports (Out-Degree: 67):` locks.h, rand.h, endian.h, if.h, net_osdep.h, pfkeyv2.h, raw_cb.h, route.h...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `bsd/nfs/nfs_vnops.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.87)
- **Top Global Matches:** file_cluster_3: 11.87, file_cluster_8: 15.149, file_cluster_6: 27.319
- **Magnitude:** 7687.86 | **LOC:** 8840 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **43**; blast radius 0.105; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.8%), Complexity Load (formerly Cognitive Load) (77.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nfs_vnop_write` **(Many-Argument Workhorses)** (Impact: 220.6)
    * *Intent:* /* * NFS write call */
  * `nfs_close` **(Many-Argument Workhorses)** (Impact: 184.1)
    * *Intent:* /* * nfs_close(): common function that does all the heavy lifting of file closure * * Takes an open ...
  * `nfs_vnop_setattr` **(Compute Cores)** (Impact: 152.4)
    * *Intent:* /* * NFS setattr call. */
  * `nfs_vnop_pageout` **(Many-Argument Workhorses)** (Impact: 152.3)
    * *Intent:* /* * vnode OP for pageout using UPL * * No buffer I/O, just RPCs straight from the mapped pages. * F...
  * `nfs_dir_buf_cache_lookup` **(Many-Argument Workhorses)** (Impact: 148.3)
    * *Intent:* /* * Look up a name in a directory's buffers. * Note: should only be called with RDIRPLUS directory ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1261 instances
* *State Mutation (weighted view):* 3924
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1706`, `structural_boundaries: 657`, `args: 148`, `func_start: 76`, `class_start: 243`
* *Risk/State:* `safety_bypasses: 250`, `state_mutation: 1402`, `dead_code: 11`, `fragile_debt: 24`, `unreferenced_by_name: 14`
* *Architecture:* `api: 107`, `import: 43`
* *Defense:* `safety: 25`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.105
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.083238
  * `Imports (Out-Degree: 67):` clock.h, sched_prim.h, task.h, OSAtomic.h, fifo.h, specdev.h, if.h, in.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `bsd/nfs/nfs_socket.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.277)
- **Top Global Matches:** file_cluster_8: 7.277, file_cluster_3: 18.25, file_cluster_6: 18.712
- **Magnitude:** 7203.96 | **LOC:** 7122 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **37**; blast radius 0.12; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.4%), Guard Balance (formerly Safety Score) (76.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nfs_connect` **(Many-Argument Workhorses)** (Impact: 445.3)
    * *Intent:* * * Search for a location to connect a socket to and initialize the connection. * * An NFS mount may...
  * `nfs_request_finish` **(Many-Argument Workhorses)** (Impact: 224.4)
    * *Intent:* /* * Finish up an NFS request by dequeueing it and * doing the initial NFS request reply processing....
  * `nfs_aux_request` **(Many-Argument Workhorses)** (Impact: 189.0)
  * `nfs_send` **(Many-Argument Workhorses)** (Impact: 178.0)
    * *Intent:* * - send the request * * If sent successfully, R_MUSTRESEND and R_RESENDERR are cleared. * rexmit co...
  * `nfs4_cb_handler` **(Many-Argument Workhorses)** (Impact: 167.3)
    * *Intent:* /* * Handle an NFS callback channel request. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1107 instances
* *State Mutation (weighted view):* 3385
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1553`, `structural_boundaries: 726`, `args: 157`, `func_start: 83`, `class_start: 154`
* *Risk/State:* `state_mutation: 1171`, `fragile_debt: 13`, `unreferenced_by_name: 10`
* *Architecture:* `api: 112`, `import: 37`
* *Defense:* `safety: 15`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.083284
  * `Imports (Out-Degree: 72):` clock.h, task.h, thread.h, thread_call.h, OSAtomic.h, in.h, tcp.h, krpc.h...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `bsd/net/dlil.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.886)
- **Top Global Matches:** file_cluster_4: 5.886, file_cluster_6: 8.87, file_cluster_16: 12.81
- **Magnitude:** 7170.48 | **LOC:** 10702 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **70** in-repo importer(s); it depends on **83**; blast radius 0.26; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.3%), Guard Balance (formerly Safety Score) (69.3%)
- **Documentation Coverage:** 97.3214% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dlil_output` **(Many-Argument Workhorses)** (Impact: 313.1)
    * *Intent:* * Caller should have a lock on the protocol domain if the protocol * doesn't support finer grained l...
  * `dlil_input_packet_list_common` **(Many-Argument Workhorses)** (Impact: 181.2)
  * `ifnet_attach` **(Many-Argument Workhorses)** (Impact: 117.7)
  * `ifnet_enqueue_ifclassq` **(Many-Argument Workhorses)** (Impact: 108.4)
  * `dlil_rxpoll_input_thread_cont` **(Many-Argument Workhorses)** (Impact: 102.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1013 instances
* *State Mutation (weighted view):* 3252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1403`, `structural_boundaries: 1431`, `args: 486`, `func_start: 232`, `class_start: 240`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1226`, `dead_code: 3`, `fragile_debt: 4`, `unreferenced_by_name: 82`
* *Architecture:* `api: 155`, `import: 83`
* *Defense:* `safety: 26`, `doc: 7`, `immutability_locks: 111`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.26
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.088281
  * `Imports (Out-Degree: 152):` randomdev.h, assert.h, locks.h, sched_prim.h, task.h, thread.h, zalloc.h, OSAtomic.h...
  * `Imported By (In-Degree: 70):` (Excluded from Brief to save tokens)

### `osfmk/vm/vm_resident.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.59)
- **Top Global Matches:** file_cluster_6: 5.59, file_cluster_4: 12.251, file_cluster_8: 12.56
- **Magnitude:** 7045.2 | **LOC:** 9854 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **52** in-repo importer(s); it depends on **42**; blast radius 0.317; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.8%), Complexity Load (formerly Cognitive Load) (70.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vm_page_find_contiguous` **(Many-Argument Workhorses)** (Impact: 315.4)
    * *Intent:* #endif
  * `hibernate_page_list_setall` **(Many-Argument Workhorses)** (Impact: 248.2)
    * *Intent:* /* * Bits zero in the bitmaps => page needs to be saved. All pages default to be saved, * pages know...
  * `vm_page_insert_internal` **(Many-Argument Workhorses)** (Impact: 180.0)
  * `vm_page_free_list` **(Many-Argument Workhorses)** (Impact: 114.6)
    * *Intent:* /* * Free a list of pages. The list can be up to several hundred pages, * as blocked up by vm_pageou...
  * `vm_page_do_delayed_work` **(Many-Argument Workhorses)** (Impact: 99.4)
    * *Intent:* * collections of pages that don't require any work brokered by the * vm_page_queue_lock... to mitiga...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1162 instances
* *State Mutation (weighted view):* 3739
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1298`, `structural_boundaries: 419`, `args: 295`, `func_start: 139`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 1415`, `dead_code: 14`, `planned_debt: 4`, `fragile_debt: 7`, `unreferenced_by_name: 53`
* *Architecture:* `api: 133`, `import: 42`
* *Defense:* `safety: 292`, `test: 8`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.317
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.132736
  * `Imports (Out-Degree: 80):` IOHibernatePrivate.h, cpu_internal.h, debug.h, misc_protos.h, counter.h, host_statistics.h, kalloc.h, ledger.h...
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

### `bsd/vfs/vfs_cluster.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.695)
- **Top Global Matches:** file_cluster_8: 5.695, file_cluster_6: 13.837, file_cluster_4: 22.541
- **Magnitude:** 6873.2 | **LOC:** 7508 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **31**; blast radius 0.112; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cluster_io` **(Many-Argument Workhorses)** (Impact: 528.6)
  * `cluster_read_copy` **(Many-Argument Workhorses)** (Impact: 363.5)
  * `cluster_read_direct` **(Many-Argument Workhorses)** (Impact: 295.9)
  * `cluster_write_copy` **(Many-Argument Workhorses)** (Impact: 290.0)
  * `cluster_write_direct` **(Many-Argument Workhorses)** (Impact: 209.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1056 instances
* *State Mutation (weighted view):* 3256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1063`, `structural_boundaries: 455`, `args: 237`, `func_start: 70`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1144`, `dead_code: 2`, `fragile_debt: 5`, `unreferenced_by_name: 9`
* *Architecture:* `api: 35`, `import: 31`
* *Defense:* `safety: 19`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.112
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0934
  * `Imports (Out-Degree: 51):` kalloc.h, policy_internal.h, task.h, OSAtomic.h, libkern.h, mach_types.h, memory_object_types.h, upl.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `bsd/kern/uipc_socket.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.8)
- **Top Global Matches:** file_cluster_6: 5.8, file_cluster_4: 11.867, file_cluster_8: 13.214
- **Magnitude:** 6873.14 | **LOC:** 8016 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **57** in-repo importer(s); it depends on **57**; blast radius 0.223; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `soreceive` **(Many-Argument Workhorses)** (Impact: 524.5)
    * *Intent:* * sbwait:EBADF * sbwait:EINTR * sodelayed_copy:EFAULT * <pru_rcvoob>:EINVAL[TCP] * <pru_rcvoob>:EWOU...
  * `sosetoptlock` **(Many-Argument Workhorses)** (Impact: 458.6)
    * *Intent:* * sooptcopyin:EINVAL * sooptcopyin:EFAULT * sooptcopyin_timeval:EINVAL * sooptcopyin_timeval:EFAULT ...
  * `sosend` **(Many-Argument Workhorses)** (Impact: 300.0)
    * *Intent:* * <pru_send>:ENOBUFS[TCP] * <pru_send>:???[TCP] [ignorable: mostly IPSEC/firewall/DLIL] * <pru_send>...
  * `sogetoptlock` **(Many-Argument Workhorses)** (Impact: 240.8)
    * *Intent:* /* * Return: 0 Success * ENOPROTOOPT * <pr_ctloutput>:EOPNOTSUPP[AF_UNIX] * <pr_ctloutput>:??? * <sf...
  * `soreceive_list` **(Many-Argument Workhorses)** (Impact: 219.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 966 instances
* *State Mutation (weighted view):* 2987
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1427`, `structural_boundaries: 753`, `args: 214`, `func_start: 112`, `class_start: 133`
* *Risk/State:* `state_mutation: 1055`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 37`
* *Architecture:* `api: 87`, `import: 58`
* *Defense:* `safety: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.223
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.101511
  * `Imports (Out-Degree: 98):` assert.h, locks.h, policy_internal.h, task.h, zalloc.h, OSAtomic.h, section_keywords.h, limits.h...
  * `Imported By (In-Degree: 57):` (Excluded from Brief to save tokens)

### `bsd/nfs/nfs_vfsops.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.873)
- **Top Global Matches:** file_cluster_3: 10.873, file_cluster_8: 13.544, file_cluster_6: 26.237
- **Magnitude:** 6658.16 | **LOC:** 6775 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **40**; blast radius 0.1; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.3%), Guard Balance (formerly Safety Score) (74.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mountnfs` **(Many-Argument Workhorses)** (Impact: 559.3)
    * *Intent:* #define NFS_MAX_SUPPORTED_VERSION ((long)(sizeof (maxminorverstab) / sizeof (uint32_t) - 1)) #define...
  * `nfs_convert_old_nfs_args` **(Many-Argument Workhorses)** (Impact: 378.4)
    * *Intent:* #endif /* NO_MOUNT_PRIVATE */ #endif /* * Convert old style NFS mount args to XDR. */
  * `nfs_vfs_sysctl` **(Many-Argument Workhorses)** (Impact: 356.5)
    * *Intent:* /* * Do that sysctl thang... */
  * `nfs_mirror_mount_domount` **(Many-Argument Workhorses)** (Impact: 236.1)
    * *Intent:* #if CONFIG_TRIGGERS /* * We've detected a file system boundary on the server and * need to mount a n...
  * `nfs4_mount` **(Many-Argument Workhorses)** (Impact: 218.2)
    * *Intent:* /* Set up an NFSv4 mount */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 962 instances
* *State Mutation (weighted view):* 3047
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1366`, `structural_boundaries: 468`, `args: 136`, `func_start: 49`, `class_start: 107`
* *Risk/State:* `state_mutation: 1123`, `dead_code: 3`, `fragile_debt: 8`, `unreferenced_by_name: 6`
* *Architecture:* `api: 70`, `import: 40`
* *Defense:* `safety: 26`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.071534
  * `Imports (Out-Degree: 80):` OSAtomic.h, if.h, route.h, in.h, krpc.h, nfs.h, nfs_conf.h, nfs_gss.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `bsd/kern/kern_memorystatus.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.586)
- **Top Global Matches:** file_cluster_6: 6.586, file_cluster_4: 11.52, file_cluster_8: 14.577
- **Magnitude:** 6419.96 | **LOC:** 8574 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); it depends on **42**; blast radius 0.222; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.8%), Guard Balance (formerly Safety Score) (72.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `memorystatus_cmd_get_jetsam_snapshot` **(Many-Argument Workhorses)** (Impact: 650.8)
  * `memorystatus_update` **(Many-Argument Workhorses)** (Impact: 185.5)
    * *Intent:* * memlimit_active_is_fatal When a process is active and exceeds its memory footprint, * this describ...
  * `memorystatus_update_priority_locked` **(Many-Argument Workhorses)** (Impact: 154.8)
    * *Intent:* * - if the 'jetsam aging policy' is NOT 'legacy': * When this flag is TRUE, it means we are going * ...
  * `memorystatus_dirty_set` **(Many-Argument Workhorses)** (Impact: 128.8)
  * `memorystatus_kill_top_process` **(Many-Argument Workhorses)** (Impact: 106.4)
    * *Intent:* /* * Jetsam the first process in the queue. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 866 instances
* *State Mutation (weighted view):* 2764
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1208`, `structural_boundaries: 497`, `args: 276`, `func_start: 136`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1032`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 33`
* *Architecture:* `api: 85`, `concurrency: 1`, `import: 42`
* *Defense:* `safety: 113`, `sync_locks: 2`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.222
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.126706
  * `Imports (Out-Degree: 73):` IOBSD.h, task_corpse.h, assert.h, debug.h, host.h, kalloc.h, locks.h, policy_internal.h...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `iokit/Kernel/IOService.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.68)
- **Top Global Matches:** file_cluster_4: 6.68, file_cluster_6: 11.014, file_cluster_12: 11.518
- **Magnitude:** 6001.32 | **LOC:** 8388 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **38**; blast radius 0.185; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.5%), Debt Markers (formerly Tech Debt) (81.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IOService::matchInternal` **(Many-Argument Workhorses)** (Impact: 169.4)
  * `IOService::probeCandidates` **(Many-Argument Workhorses)** (Impact: 161.4)
    * *Intent:* /* * Alloc and probe matching classes, * called on the provider instance */
  * `IOService::updateConsoleUsers` **(Many-Argument Workhorses)** (Impact: 95.3)
  * `IOService::copyExistingServices` **(Many-Argument Workhorses)** (Impact: 95.0)
    * *Intent:* // internal - call with gNotificationLock
  * `IOService::errnoFromReturn` **(Compute Cores)** (Impact: 79.6)
    * *Intent:* /* * Convert an IOReturn to an errno. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 902 instances
* *State Mutation (weighted view):* 2857
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1319`, `structural_boundaries: 576`, `args: 415`, `func_start: 251`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 123`, `high_risk_execution: 2`, `state_mutation: 1053`, `dead_code: 8`, `planned_debt: 7`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 166`
* *Architecture:* `import: 39`
* *Defense:* `safety: 36`, `doc: 2`, `sync_locks: 13`, `immutability_locks: 192`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.100027
  * `Imports (Out-Degree: 76):` AppleKeyStoreInterface.h, IOBSD.h, IOCPU.h, IOCatalogue.h, IOCommand.h, IODeviceMemory.h, IODeviceTreeSupport.h, IOHibernatePrivate.h...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `osfmk/vm/vm_fault.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.609)
- **Top Global Matches:** file_cluster_8: 5.609, file_cluster_6: 13.117, file_cluster_4: 21.809
- **Magnitude:** 5830.34 | **LOC:** 8030 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **41**; blast radius 0.153; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.3%)
- **Documentation Coverage:** 96.1039% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vm_fault_internal` **(Many-Argument Workhorses)** (Impact: 1171.7)
  * `vm_fault_page` **(Many-Argument Workhorses)** (Impact: 730.4)
  * `vm_fault_cs_handle_violation` **(Many-Argument Workhorses)** (Impact: 184.9)
    * *Intent:* /* * Handles a code signing violation by either rejecting the page or forcing a disconnect. * @param...
  * `vm_fault_copy` **(Many-Argument Workhorses)** (Impact: 175.5)
    * *Intent:* * destination map. * * Results: * Returns KERN_SUCCESS if no errors were encountered in * reading or...
  * `vm_fault_enqueue_page` **(Many-Argument Workhorses)** (Impact: 114.0)
    * *Intent:* /* * Enqueue the page on the appropriate paging queue. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 642 instances
* *State Mutation (weighted view):* 2030
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1074`, `structural_boundaries: 328`, `args: 157`, `func_start: 58`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 746`, `dead_code: 15`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 43`, `import: 41`
* *Defense:* `safety: 136`, `doc: 7`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.121243
  * `Imports (Out-Degree: 79):` backtrace.h, counter.h, host.h, host_statistics.h, kern_types.h, mach_param.h, macro_help.h, misc_protos.h...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `bsd/kern/kern_event.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.42)
- **Top Global Matches:** file_cluster_4: 5.42, file_cluster_16: 8.711, file_cluster_15: 10.285
- **Magnitude:** 5580.46 | **LOC:** 9153 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **46** in-repo importer(s); it depends on **59**; blast radius 0.237; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.6%), Complexity Load (formerly Cognitive Load) (67.0%)
- **Documentation Coverage:** 91.1051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filt_wlupdate` **(Many-Argument Workhorses)** (Impact: 155.4)
    * *Intent:* #define EVFILT_WORKLOOP_EFAULT_RETRY_COUNT 100 #define FILT_WLATTACH 0 #define FILT_WLTOUCH 1 #defin...
  * `kevent_internal` **(Many-Argument Workhorses)** (Impact: 131.3)
    * *Intent:* * @brief * Common kevent code. * * @discussion * Needs to be inlined to specialize for legacy or mod...
  * `kevent_register` **(Many-Argument Workhorses)** (Impact: 130.4)
    * *Intent:* /* * kevent_register - add a new event to a kqueue * * Creates a mapping between the event source an...
  * `kqworkloop_update_threads_qos` **(Many-Argument Workhorses)** (Impact: 110.4)
  * `kqueue_process` **(Many-Argument Workhorses)** (Impact: 70.3)
    * *Intent:* * * caller holds a reference on the kqueue. * kqueue locked on entry and exit - but may be dropped *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 766 instances
* *State Mutation (weighted view):* 2408
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1102`, `structural_boundaries: 1256`, `args: 352`, `func_start: 232`, `class_start: 215`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 876`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 31`
* *Architecture:* `api: 106`, `import: 63`
* *Defense:* `safety: 128`, `doc: 48`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.237
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.122992
  * `Imports (Out-Degree: 99):` assert.h, ast.h, clock.h, cpu_data.h, kalloc.h, kcdata.h, locks.h, policy_internal.h...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `iokit/Kernel/IOMemoryDescriptor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.18)
- **Top Global Matches:** file_cluster_6: 5.18, file_cluster_4: 9.678, file_cluster_8: 15.033
- **Magnitude:** 5565.34 | **LOC:** 5964 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **33**; blast radius 0.226; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.7%), Guard Balance (formerly Safety Score) (75.3%), Debt Markers (formerly Tech Debt) (67.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IOGeneralMemoryDescriptor::initWithOptions` **(Many-Argument Workhorses)** (Impact: 317.6)
    * *Intent:* /* * initWithOptions: * * IOMemoryDescriptor. The buffer is made up of several virtual address range...
  * `IOGeneralMemoryDescriptor::dmaCommandOperation` **(Many-Argument Workhorses)** (Impact: 227.1)
  * `IOGeneralMemoryDescriptor::memoryReferenceMap` **(Many-Argument Workhorses)** (Impact: 166.3)
  * `IOGeneralMemoryDescriptor::memoryReferenceMapNew` **(Many-Argument Workhorses)** (Impact: 156.4)
    * *Intent:* #define LOGUNALIGN 0
  * `IOGeneralMemoryDescriptor::wireVirtual` **(Many-Argument Workhorses)** (Impact: 142.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 891 instances
* *State Mutation (weighted view):* 2717
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1129`, `structural_boundaries: 332`, `args: 235`, `func_start: 132`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 935`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 99`
* *Architecture:* `import: 33`
* *Defense:* `safety: 52`, `doc: 1`, `sync_locks: 22`, `immutability_locks: 25`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.226
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.101136
  * `Imports (Out-Degree: 62):` IODMACommand.h, IOKitDebug.h, IOKitKeysPrivate.h, IOLib.h, IOMapper.h, IOMemoryDescriptor.h, IOMultiMemoryDescriptor.h, IOSubMemoryDescriptor.h...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/safe_allocation_src/compare.equal.nullptr.cpp` (CPP) | Magnitude: 5.44 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 16, test: 8, structural_boundaries: 4, import: 3
- `tests/safe_allocation_src/data.cpp` (CPP) | Magnitude: 5.52 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 19, structural_boundaries: 4, core_var_decl: 4, design_snake_case: 4
- `tests/safe_allocation_src/usage.two_dimensions.cpp` (CPP) | Magnitude: 27.42 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 14, state_mutation: 7, branch: 4, structural_boundaries: 4
- `tests/bounded_ptr_src/compare.order.cpp` (CPP) | Magnitude: 18.72 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 97, immutability_locks: 34, structural_boundaries: 21, func_start: 7
- `libkern/libkern/c++/safe_allocation.h` (CPP) | Magnitude: 138.28 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 168, structural_boundaries: 109, core_var_decl: 32, func_start: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/safe_allocation_src/ctor.nullptr.cpp` (CPP) | Magnitude: 6.22 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 25, test: 12, structural_boundaries: 5, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `osfmk/i386/cpu_capabilities.h` (C) | Magnitude: 8.28 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: macros: 164, args: 58, structural_boundaries: 3, api: 3
- `tests/bounded_array_ref_src/test_policy.h` (CPP) | Magnitude: 13.58 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 19, structural_boundaries: 15, state_mutation: 7, import: 7
- `EXTERNAL_HEADERS/corecrypto/cc_runtime_config.h` (C) | Magnitude: 3.88 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 50, macros: 46, import: 5, structural_boundaries: 4
- `osfmk/arm/machdep_call.c` (C) | Magnitude: 16.94 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 15, macros: 11, structural_boundaries: 8, pointers: 7
- `osfmk/i386/vmx/vmx_shims.c` (C) | Magnitude: 12.58 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 10, structural_boundaries: 8, import: 7, pointers: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `iokit/IOKit/IORegistryEntry.h` (CPP) | Magnitude: 27.9 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 186, immutability_locks: 177, args: 153, doc: 149
- `tools/lldbmacros/ulock.py` (PYTHON) | Magnitude: 0.04 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 9, core_var_decl: 9, design_snake_case: 9
- `osfmk/i386/mp_desc.h` (C) | Magnitude: 24.9 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 12, macros: 12, pointers: 10, api: 9
- `iokit/IOKit/IOKernelReporters.h` (C) | Magnitude: 14.46 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 155, indent_tabs: 115, args: 79, structural_boundaries: 74
- `tests/ipsec.m` (OBJECTIVE-C) | Magnitude: 382.64 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 412, pointers: 143, state_mutation: 126, branch: 72

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/intrusive_shared_ptr_src/cast.reinterpret.cpp` (CPP) | Magnitude: 7.54 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 43, test: 16, immutability_locks: 10, structural_boundaries: 8
- `tests/intrusive_shared_ptr_src/cast.const.cpp` (CPP) | Magnitude: 7.24 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 40, test: 16, structural_boundaries: 6, explicit_casts: 6
- `tests/intrusive_shared_ptr_src/cast.static.cpp` (CPP) | Magnitude: 9.12 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 44, test: 16, structural_boundaries: 10, immutability_locks: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `iokit/IOKit/PassthruInterruptController.h` (CPP) | Magnitude: 16.62 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 22, indent_tabs: 16, pointers: 15, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `osfmk/kern/restartable.c` (C) | Magnitude: 215.3 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 187, pointers: 93, structural_boundaries: 54, branch: 52
- `tests/bounded_array_ref_src/begin_end.cpp` (CPP) | Magnitude: 6.04 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 6, core_var_decl: 5, test: 4
- `libsyscall/mach/exc_catcher_state.c` (C) | Magnitude: 19.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 19, import: 6, structural_boundaries: 4, args: 4
- `tests/bounded_array_src/begin_end.cpp` (CPP) | Magnitude: 6.92 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 34, core_var_decl: 13, design_snake_case: 12, test: 8
- `osfmk/arm64/caches_asm.s` (ASSEMBLY) | Magnitude: 84.1 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 224, args: 128, structural_boundaries: 73, concurrency: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `bsd/miscfs/devfs/devfsdefs.h` (C) | Magnitude: 45.0 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 68, structural_boundaries: 43, api: 26, pointers: 26
- `bsd/net/devtimer.c` (C) | Magnitude: 134.78 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 115, structural_boundaries: 52, pointers: 50, state_mutation: 23
- `bsd/netinet6/in6_proto.c` (C) | Magnitude: 113.84 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 269, pointers: 89, structural_boundaries: 88, indent_spaces: 72
- `tests/bounded_ptr_src/test_utils.h` (C) | Magnitude: 5.02 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 5, structural_boundaries: 3, api: 2, import: 2
- `tests/host_notifications.c` (C) | Magnitude: 4.86 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 8, args: 8, pointers: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `osfmk/i386/pal_routines.h` (C) | Magnitude: 45.62 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 40, api: 31, args: 24, pointers: 20
- `osfmk/vm/vm_object.h` (C) | Magnitude: 166.52 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 383, pointers: 134, macros: 122, api: 82
- `tools/tests/perf_index/perfindex-ram_file_read.c` (C) | Magnitude: 0.02 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 12, import: 6, structural_boundaries: 3, state_mutation: 3
- `tools/tests/perf_index/perfindex-ram_file_write.c` (C) | Magnitude: 0.02 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 12, import: 6, structural_boundaries: 3, state_mutation: 3
- `tests/net_tun_pr_35136664.c` (C) | Magnitude: 27.98 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 30, state_mutation: 12, structural_boundaries: 8, import: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/mach_port_mod_refs.c` (C) | Magnitude: 22.2 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 39, state_mutation: 18, core_var_decl: 18, design_snake_case: 18
- `tests/intrusive_shared_ptr_src/deref.cpp` (CPP) | Magnitude: 5.44 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 15, pointers: 7, structural_boundaries: 4, test: 4
- `tests/proc_uuid_policy_26567533.c` (C) | Magnitude: 37.64 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 23, state_mutation: 8, args: 4, import: 4
- `tests/ltable_exhaustion_test.c` (C) | Magnitude: 21.44 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 10, import: 6, pointers: 6, state_mutation: 2
- `tests/stackshot_translated_child.c` (C) | Magnitude: 2.86 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 4, import: 3, macros: 2, structural_boundaries: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `osfmk/kperf/action.c` (C) | Magnitude: 571.46 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 424, branch: 127, pointers: 94, structural_boundaries: 93
- `bsd/kern/sys_socket.c` (C) | Magnitude: 350.46 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 245, pointers: 126, branch: 85, structural_boundaries: 70
- `bsd/kern/kern_proc.c` (C) | Magnitude: 2845.62 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 2261, pointers: 786, branch: 565, structural_boundaries: 522
- `osfmk/vm/vm_shared_region_pager.c` (C) | Magnitude: 590.5 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 600, pointers: 251, state_mutation: 121, core_var_decl: 88
- `osfmk/ipc/ipc_voucher.c` (C) | Magnitude: 1656.02 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 1531, pointers: 556, state_mutation: 315, branch: 247

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `osfmk/kern/ipc_tt.c` (C) | Magnitude: 2908.06 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 2310, branch: 584, state_mutation: 446, pointers: 444
- `osfmk/kern/thread_policy.c` (C) | Magnitude: 2142.32 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1500, pointers: 418, branch: 405, state_mutation: 340
- `bsd/nfs/nfs_syscalls.c` (C) | Magnitude: 1313.96 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 1084, pointers: 552, branch: 283, state_mutation: 263
- `bsd/vfs/vfs_utfconv.c` (C) | Magnitude: 1292.72 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 673, state_mutation: 249, branch: 199, core_var_decl: 147
- `osfmk/kdp/kdp_udp.c` (C) | Magnitude: 1581.24 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1243, pointers: 377, structural_boundaries: 361, state_mutation: 338

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/scm_rights_leak.c` (C) | Magnitude: 60.5 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 55, state_mutation: 29, pointers: 18, core_var_decl: 9
- `EXTERNAL_HEADERS/stddef.h` (C) | Magnitude: 15.76 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: macros: 27, reflection_metaprogramming: 9, structural_boundaries: 5, args: 2
- `iokit/IOKit/IOMemoryCursor.h` (CPP) | Magnitude: 19.08 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: doc: 66, indent_tabs: 50, structural_boundaries: 27, args: 19
- `tests/phys_footprint_interval_max.c` (C) | Magnitude: 25.14 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 34, import: 10, core_var_decl: 9, design_snake_case: 9
- `tools/tests/perf_index/PerfIndex_COPS_Module/PITest.h` (OBJECTIVE-C) | Magnitude: 0.01 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 12, api: 4, func_start: 3, safety_bypasses: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `osfmk/arm/trustcache.c` (C) | Magnitude: 106.32 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 87, pointers: 39, structural_boundaries: 30, branch: 24
- `osfmk/ipc/ipc_init.c` (C) | Magnitude: 38.38 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: import: 35, indent_tabs: 33, macros: 15, state_mutation: 12
- `osfmk/arm64/alternate_debugger.c` (C) | Magnitude: 39.98 | Delta: **0.187** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 50, structural_boundaries: 15, pointers: 15, branch: 10
- `tests/text_corruption_helper.c` (C) | Magnitude: 34.4 | Delta: **0.19** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 28, branch: 9, import: 7, pointers: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `bsd/sys/cdefs.h` -> **Severity: 14.582** (Embedded: 0.2904 * Error Risk: 50.2149%)
- `libsyscall/wrappers/string/memcpy.c` -> **Severity: 12.445** (Embedded: 0.1378 * Error Risk: 90.2979%)
- `osfmk/kern/printf.c` -> **Severity: 12.304** (Embedded: 0.1531 * Error Risk: 80.3503%)
- `osfmk/vm/vm_kern.c` -> **Severity: 10.417** (Embedded: 0.1466 * Error Risk: 71.0509%)
- `iokit/Kernel/IOStringFuncs.c` -> **Severity: 10.236** (Embedded: 0.1129 * Error Risk: 90.6248%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `bsd/sys/types.h` -> **Severity: 901.5** (Blast Radius: 9.015 * Doc Risk: 100.0%)
- `libsyscall/wrappers/_libc_funcptr.c` -> **Severity: 475.3** (Blast Radius: 4.753 * Doc Risk: 100.0%)
- `osfmk/mach/port.h` -> **Severity: 386.2** (Blast Radius: 3.862 * Doc Risk: 100.0%)
- `libkern/libkern/c++/intrusive_shared_ptr.h` -> **Severity: 365.2** (Blast Radius: 3.652 * Doc Risk: 100.0%)
- `osfmk/mach/message.h` -> **Severity: 360.9** (Blast Radius: 3.609 * Doc Risk: 100.0%)

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 3947 literal sites + 63 sites through wrappers = 4010
- **`memory_alloc`:** 742 literal sites + 554 sites through wrappers = 1296
- **`panics_and_aborts`:** 1694 literal sites + 24 sites through wrappers = 1718

- `kfree` (macro, memory_alloc, primitive): 195 call sites in 70 files -- `osfmk/kern/bits.h`
- `kalloc` (macro, memory_alloc, primitive): 120 call sites in 65 files -- `osfmk/kern/bits.h`
- `GET_TOKEN_AREA` (macro, memory_alloc, primitive): 46 call sites in 1 files -- `bsd/security/audit/audit_bsm_token.c`
- `PROC_INFO_CALL` (macro, memory_alloc, primitive): 17 call sites in 1 files -- `tests/proc_info.c`
- `rs_free` (macro, memory_alloc, primitive): 14 call sites in 1 files -- `bsd/net/pf_ruleset.c`
- `path` (function, memory_alloc, primitive): 11 call sites in 3 files -- `SETUP/config/main.c`
- `ubc_cs_blob_deallocate` (function, memory_alloc, via kfree): 11 call sites in 3 files -- `bsd/kern/ubc_subr.c`
- `print_rw_hdr` (function, debug_prints, primitive): 9 call sites in 1 files -- `tools/lockstat/lockstat.c`
- `R_Free` (macro, memory_alloc, primitive): 8 call sites in 3 files -- `bsd/net/radix.h`
- `print_spin_hdr` (function, debug_prints, primitive): 8 call sites in 1 files -- `tools/lockstat/lockstat.c`
- `usage` (function, debug_prints, primitive): 8 call sites in 1 files -- `tools/lockstat/lockstat.c`
- `usage` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `tools/lockstat/lockstat.c`
*(+83 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 171860 call pairs -- scoped 19.1%, unique 29.5%, ambiguous 14.0%, external 37.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 145815 | 18.1% | 32.7% | 11.6% | 37.6% |
| cpp | 17951 | 22.6% | 16.1% | 29.3% | 32.0% |
| python | 5964 | 32.3% | 0.0% | 29.9% | 37.8% |
| objective-c | 1281 | 17.7% | 11.3% | 15.5% | 55.4% |
| swift | 343 | 30.0% | 0.0% | 0.0% | 70.0% |
| lua | 250 | 13.6% | 0.0% | 0.0% | 86.4% |
| shell | 167 | 20.4% | 0.0% | 0.0% | 79.6% |
| perl | 55 | 0.0% | 0.0% | 0.0% | 100.0% |
| yacc | 20 | 0.0% | 5.0% | 35.0% | 60.0% |
| rexx | 11 | 0.0% | 0.0% | 0.0% | 100.0% |

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
