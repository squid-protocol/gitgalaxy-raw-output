# ARCHITECTURAL_BRIEF: darwin-xnu
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/OS/darwin-xnu` |
| **Timestamp** | `2026-08-03T19:06:50.807388+00:00` |
| **Scan Duration** | `29.47s` |
| **Git Branch** | `main` |
| **Git Commit** | `2ff845c2e033bd0ff64b5b6aa6063a1f8f65aa32` |
| **Git Remote** | `https://github.com/apple/darwin-xnu.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3296 malicious artifacts.

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
| Total Artifacts | 4535 |
| Analyzed Artifacts (Scanned) | 3955 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 580 |
| Total LOC | 818234 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7107 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2046 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.9816 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 101 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 2714 | 669400 | 68.6% |
| CPP | 302 | 65681 | 7.6% |
| PLAINTEXT | 259 | 0 | 6.5% |
| HTML | 252 | 19134 | 6.4% |
| MAKEFILE | 161 | 7016 | 4.1% |
| ASSEMBLY | 92 | 22822 | 2.3% |
| PYTHON | 64 | 24236 | 1.6% |
| XML | 41 | 0 | 1.0% |
| OBJECTIVE-C | 25 | 5766 | 0.6% |
| SHELL | 20 | 2408 | 0.5% |
| MARKDOWN | 14 | 0 | 0.4% |
| LUA | 7 | 950 | 0.2% |
| YACC | 1 | 119 | 0.0% |
| PERL | 1 | 117 | 0.0% |
| SWIFT | 1 | 288 | 0.0% |
| BATCH | 1 | 297 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.389`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2302 | 58.2% |
| file_cluster_13 | 1144 | 28.9% |
| file_cluster_2 | 93 | 2.4% |
| file_cluster_9 | 76 | 1.9% |
| file_cluster_4 | 25 | 0.6% |
| file_cluster_12 | 12 | 0.3% |
| file_cluster_16 | 12 | 0.3% |
| file_cluster_17 | 6 | 0.2% |
| file_cluster_11 | 5 | 0.1% |
| file_cluster_0 | 4 | 0.1% |
| file_cluster_7 | 2 | 0.1% |
| file_cluster_6 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 273 | 6.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 580*

**Composition by Extension & Reason:**
- `.defs`: 84x Excluded (Unsupported Extension: '.defs')
- `.2`: 73x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Lexical Monotony: High structural repetition detected in 2261 LOC), 1x Excluded (Machine-Generated Source Code Signature: 254 LOC)
- `no_extension`: 33x Excluded (Binary Format Detected), 12x Excluded (Unsupported Extension: '.entitlements'), 9x Unsupported Format (.undeterminable)
- `.c`: 51x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 40 exceeds 500 chars), 1x Excluded (Embedded Array/Matrix Payload: 3779 commas in 1022 LOC)
- `.h`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 58 LOC)
- `.exports`: 41x Excluded (Unsupported Extension: '.exports')
- `.gz`: 34x Excluded (Explicitly Denied Extension: '.gz')
- `.d`: 18x Unsupported Format (.d)
- `.arm64`: 17x Excluded (Unsupported Extension: '.arm64')
- `.x86_64`: 17x Excluded (Unsupported Extension: '.x86_64')
- `.iig`: 14x Excluded (Unsupported Extension: '.iig')
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.template`: 9x Excluded (Unsupported Extension: '.template')
- `.map`: 8x Excluded (Unsupported Extension: '.map')
- `.pbxproj`: 5x Excluded (Unsupported Extension: '.pbxproj'), 2x Unsupported Format (.pbxproj)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 27.8 | 9.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 21.3 | 6.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 18.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.2 | 2.3 | 2.3 |
| API Exposure | 0.0 | 19.3 | 7.3 | 8.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 35.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 47.8 | 31.6 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 1.4 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `osfmk/man/index.html` (Hits: 424)
- `bsd/kern/makesyscalls.sh` (Hits: 202)
- `tests/vsock.c` (Hits: 125)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **stdint.h** (`EXTERNAL_HEADERS/stdint.h`) — 257 inbound connections
2. **unistd.h** (`bsd/sys/unistd.h`) — 189 inbound connections
3. **stdio.h** (`bsd/sys/stdio.h`) — 157 inbound connections
4. **stdbool.h** (`EXTERNAL_HEADERS/stdbool.h`) — 117 inbound connections
5. **errno.h** (`bsd/sys/errno.h`) — 87 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Tests.cpp** (`iokit/Tests/Tests.cpp`) — 144 outbound dependencies
2. **bsd_init.c** (`bsd/kern/bsd_init.c`) — 91 outbound dependencies
3. **kern_exec.c** (`bsd/kern/kern_exec.c`) — 89 outbound dependencies
4. **dlil.c** (`bsd/net/dlil.c`) — 83 outbound dependencies
5. **startup.c** (`osfmk/kern/startup.c`) — 70 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `pf_src_connlimit` (@ `bsd/net/pf.c`) -> Impact: **6735.6** | LOC: 2113
- `soconnectxlocked` (@ `bsd/kern/uipc_socket.c`) -> Impact: **5586.8** | LOC: 2416
- `GetSocketAddrAsStringLink` (@ `tools/lldbmacros/net.py`) -> Impact: **5441.7** | LOC: 1898
- `mount_common` (@ `bsd/vfs/vfs_syscalls.c`) -> Impact: **5023.3** | LOC: 1764
- `key_gather_mbuf` (@ `bsd/netkey/key.c`) -> Impact: **4441.4** | LOC: 2263
- `stackshot_trap` (@ `osfmk/kern/kern_stackshot.c`) -> Impact: **4429.9** | LOC: 1258
- `pf_route` (@ `bsd/net/pf.c`) -> Impact: **4350.1** | LOC: 1611
- `pf_test_rule` (@ `bsd/net/pf.c`) -> Impact: **3845.6** | LOC: 1984
- `nfs_advlock_setlock` (@ `bsd/nfs/nfs4_vnops.c`) -> Impact: **3460.6** | LOC: 1919
- `filt_wlupdate` (@ `bsd/kern/kern_event.c`) -> Impact: **3386.5** | LOC: 2182

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `ctl_getlock` (@ `bsd/kern/kern_control.c`) -> **O(2^N) [Recursive]**
- `stackshot_trap` (@ `osfmk/kern/kern_stackshot.c`) -> **O(2^N) [Recursive]**
- `get_fixed_address` (@ `tests/vm/vm_allocation.c`) -> **O(2^N) [Recursive]**
- `create_thread` (@ `tools/lldbmacros/core/operating_system.py`) -> **O(2^N) [Recursive]**
- `formatTurnstileInfo` (@ `tools/lldbmacros/kcdata.py`) -> **O(2^N) [Recursive]**
- `GetKtraceStatus` (@ `tools/lldbmacros/ktrace.py`) -> **O(2^N) [Recursive]**
- `FindVMEntriesForVnode` (@ `tools/lldbmacros/memory.py`) -> **O(2^N) [Recursive]**
- `CountMapTags` (@ `tools/lldbmacros/memory.py`) -> **O(2^N) [Recursive]**
- `ShowKernelDebugBufferCPU` (@ `tools/lldbmacros/misc.py`) -> **O(2^N) [Recursive]**
- `GetSocketAddrAsStringLink` (@ `tools/lldbmacros/net.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `soconnectxlocked` (@ `bsd/kern/uipc_socket.c`) -> DB Complexity: **641**
- `IOPMrootDomain::start` (@ `iokit/Kernel/IOPMrootDomain.cpp`) -> DB Complexity: **595**
- `IOService::lockForArbitration` (@ `iokit/Kernel/IOService.cpp`) -> DB Complexity: **529**
- `pmap_pages_reclaim` (@ `osfmk/arm/pmap.c`) -> DB Complexity: **497**
- `sys_fcntl_nocancel` (@ `bsd/kern/kern_descrip.c`) -> DB Complexity: **485**
- `pf_test_rule` (@ `bsd/net/pf.c`) -> DB Complexity: **475**
- `flow_divert_trie_insert` (@ `bsd/netinet/flow_divert.c`) -> DB Complexity: **469**
- `nfs4_access_rpc` (@ `bsd/nfs/nfs4_vnops.c`) -> DB Complexity: **465**
  * *Intent:* #include <sys/conf.h> #include <sys/vnode_internal.h> #include <sys/dirent.h> #include <sys/fcntl.h> #include <sys/lockf.h> #include <sys/ubc_internal...
- `nfs_advlock_setlock` (@ `bsd/nfs/nfs4_vnops.c`) -> DB Complexity: **450**
- `vfs_context_cwd` (@ `bsd/vfs/kpi_vfs.c`) -> DB Complexity: **443**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `bsd/kern` | 112 | 114490.96 | 73.33% | 38.14% |
| `bsd/net` | 149 | 98540.42 | 36.62% | 20.52% |
| `osfmk/kern` | 202 | 61239.22 | 39.2% | 25.84% |
| `iokit/Kernel` | 72 | 57123.22 | 64.73% | 72.24% |
| `bsd/netinet` | 95 | 54004.62 | 43.18% | 16.49% |
| `osfmk/vm` | 57 | 46683.14 | 40.9% | 16.33% |
| `bsd/netinet6` | 66 | 39772.06 | 47.04% | 27.49% |
| `bsd/nfs` | 31 | 38572.42 | 53.58% | 12.74% |
| `tests` | 253 | 37019.74 | 25.97% | 0.0% |
| `bsd/vfs` | 26 | 33853.02 | 70.46% | 33.62% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `libkdd/KCDEmbeddedBufferDescription.m` -> **100.0%** Exposure
- `libkdd/kdd.m` -> **100.0%** Exposure
- `bsd/kern/subr_xxx.c` -> **100.0%** Exposure
- `bsd/net/flowadv.c` -> **100.0%** Exposure
- `bsd/net/net_stubs.c` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `libkdd/KCDBasicTypeDescription.m` -> **100.0%** Exposure
- `libkdd/KCDStructTypeDescription.m` -> **100.0%** Exposure
- `libkdd/kcdata_core.m` -> **100.0%** Exposure
- `osfmk/console/art/progress.m` -> **100.0%** Exposure
- `bsd/conf/Makefile.arm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `bsd/net/kpi_interface.c` -> **101** Orphaned Functions | **0** Duplicates
- `security/mac_vfs.c` -> **94** Orphaned Functions | **2** Duplicates
- `iokit/Kernel/IOUserClient.cpp` -> **72** Orphaned Functions | **16** Duplicates
- `iokit/Kernel/IOUserServer.cpp` -> **76** Orphaned Functions | **4** Duplicates
- `bsd/vfs/vfs_bio.c` -> **70** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`tests/hvtest_x86.m`** -> AI Confidence: **99.48%**
2. **`tests/stackshot_accuracy.m`** -> AI Confidence: **99.48%**
3. **`tests/stackshot_block_owner_14362384.m`** -> AI Confidence: **99.48%**
4. **`tests/stackshot_idle_25570396.m`** -> AI Confidence: **99.48%**
5. **`tests/stackshot_tests.m`** -> AI Confidence: **99.48%**
6. **`tests/test_sysctl_kern_procargs_25397314.m`** -> AI Confidence: **99.48%**
7. **`tools/tests/kernpost_test_report/kernpost_test_report.m`** -> AI Confidence: **99.48%**
8. **`SETUP/replacecontents/replacecontents.c`** -> AI Confidence: **99.48%**
9. **`bsd/dev/arm/fasttrap_isa.c`** -> AI Confidence: **99.48%**
10. **`bsd/dev/arm/fbt_arm.c`** -> AI Confidence: **99.48%**
11. **`bsd/dev/arm64/fbt_arm.c`** -> AI Confidence: **99.48%**
12. **`bsd/dev/dtrace/dtrace.c`** -> AI Confidence: **99.48%**
13. **`bsd/dev/i386/fasttrap_isa.c`** -> AI Confidence: **99.48%**
14. **`bsd/dev/i386/fbt_x86.c`** -> AI Confidence: **99.48%**
15. **`bsd/dev/i386/systemcalls.c`** -> AI Confidence: **99.48%**
16. **`bsd/kern/kern_exec.c`** -> AI Confidence: **99.48%**
17. **`bsd/kern/kern_fork.c`** -> AI Confidence: **99.48%**
18. **`bsd/kern/kern_memorystatus_freeze.c`** -> AI Confidence: **99.48%**
19. **`bsd/kern/process_policy.c`** -> AI Confidence: **99.48%**
20. **`bsd/kern/subr_log.c`** -> AI Confidence: **99.48%**
21. **`bsd/miscfs/mockfs/mockfs_fsnode.c`** -> AI Confidence: **99.48%**
22. **`bsd/netinet/ip_ecn.c`** -> AI Confidence: **99.48%**
23. **`bsd/netinet/tcp_debug.c`** -> AI Confidence: **99.48%**
24. **`bsd/netinet/tcp_input.c`** -> AI Confidence: **99.48%**
25. **`bsd/netinet/tcp_output.c`** -> AI Confidence: **99.48%**
26. **`bsd/netinet/tcp_timer.c`** -> AI Confidence: **99.48%**
27. **`bsd/netinet6/nd6_send.c`** -> AI Confidence: **99.48%**
28. **`bsd/nfs/krpc_subr.c`** -> AI Confidence: **99.48%**
29. **`bsd/nfs/nfs4_subs.c`** -> AI Confidence: **99.48%**
30. **`bsd/nfs/nfs4_vnops.c`** -> AI Confidence: **99.48%**
31. **`bsd/nfs/nfs_bio.c`** -> AI Confidence: **99.48%**
32. **`bsd/nfs/nfs_node.c`** -> AI Confidence: **99.48%**
33. **`bsd/pgo/profile_runtime.c`** -> AI Confidence: **99.48%**
34. **`bsd/security/audit/audit_bsm.c`** -> AI Confidence: **99.48%**
35. **`bsd/sys/param.h`** -> AI Confidence: **99.48%**
36. **`bsd/vfs/vfs_attrlist.c`** -> AI Confidence: **99.48%**
37. **`bsd/vfs/vfs_utfconv.c`** -> AI Confidence: **99.48%**
38. **`bsd/vfs/vfs_xattr.c`** -> AI Confidence: **99.48%**
39. **`libkern/kxld/kxld_copyright.c`** -> AI Confidence: **99.48%**
40. **`libkern/kxld/kxld_reloc.c`** -> AI Confidence: **99.48%**
41. **`libkern/kxld/kxld_vtable.c`** -> AI Confidence: **99.48%**
42. **`libsyscall/custom/SYS.h`** -> AI Confidence: **99.48%**
43. **`libsyscall/mach/error_codes.c`** -> AI Confidence: **99.48%**
44. **`osfmk/arm/kpc_arm.c`** -> AI Confidence: **99.48%**
45. **`osfmk/arm64/alternate_debugger.c`** -> AI Confidence: **99.48%**
46. **`osfmk/arm64/kpc.c`** -> AI Confidence: **99.48%**
47. **`osfmk/i386/i386_vm_init.c`** -> AI Confidence: **99.48%**
48. **`osfmk/i386/pmap.h`** -> AI Confidence: **99.48%**
49. **`osfmk/i386/tsc.c`** -> AI Confidence: **99.48%**
50. **`osfmk/ipc/ipc_right.c`** -> AI Confidence: **99.48%**
51. **`osfmk/kern/hibernate.c`** -> AI Confidence: **99.48%**
52. **`osfmk/kern/kext_alloc.c`** -> AI Confidence: **99.48%**
53. **`osfmk/kern/mk_sp.c`** -> AI Confidence: **99.48%**
54. **`osfmk/kern/priority.c`** -> AI Confidence: **99.48%**
55. **`osfmk/kern/thread_policy.c`** -> AI Confidence: **99.48%**
56. **`osfmk/kern/tlock.c`** -> AI Confidence: **99.48%**
57. **`osfmk/vm/vm_debug.c`** -> AI Confidence: **99.48%**
58. **`osfmk/vm/vm_fault.c`** -> AI Confidence: **99.48%**
59. **`osfmk/vm/vm_map.c`** -> AI Confidence: **99.48%**
60. **`osfmk/vm/vm_object.c`** -> AI Confidence: **99.48%**
61. **`osfmk/vm/vm_purgeable.c`** -> AI Confidence: **99.48%**
62. **`osfmk/vm/vm_resident.c`** -> AI Confidence: **99.48%**
63. **`tests/extract_right_soft_fail.c`** -> AI Confidence: **99.48%**
64. **`tests/fp_exception.c`** -> AI Confidence: **99.48%**
65. **`tests/get_shared_cache_address.c`** -> AI Confidence: **99.48%**
66. **`tests/ioc_str.h`** -> AI Confidence: **99.48%**
67. **`tests/pipe_kevent.c`** -> AI Confidence: **99.48%**
68. **`tests/prioritize_process_launch_helper.c`** -> AI Confidence: **99.48%**
69. **`tests/read_inspect.c`** -> AI Confidence: **99.48%**
70. **`tests/vm_test_code_signing_helper.c`** -> AI Confidence: **99.48%**
71. **`tests/vm_test_mach_map.c`** -> AI Confidence: **99.48%**
72. **`tools/tests/affinity/pool.c`** -> AI Confidence: **99.48%**
73. **`tools/tests/affinity/sets.c`** -> AI Confidence: **99.48%**
74. **`tools/tests/affinity/tags.c`** -> AI Confidence: **99.48%**
75. **`tools/tests/perf_index/test_fault_helper.c`** -> AI Confidence: **99.48%**
76. **`tools/tests/personas/persona_mgr.c`** -> AI Confidence: **99.48%**
77. **`tools/tests/personas/persona_spawn.c`** -> AI Confidence: **99.48%**
78. **`tools/tests/superpages/measure_tlbs.c`** -> AI Confidence: **99.48%**
79. **`tools/tests/zero-to-n/zero-to-n.c`** -> AI Confidence: **99.48%**
80. **`EXTERNAL_HEADERS/corecrypto/cc.h`** -> AI Confidence: **99.48%**
81. **`bsd/net/contiki-net.h`** -> AI Confidence: **99.48%**
82. **`bsd/net/contiki.h`** -> AI Confidence: **99.48%**
83. **`bsd/sys/fsgetpath.h`** -> AI Confidence: **99.48%**
84. **`pexpert/pexpert/arm64/board_config.h`** -> AI Confidence: **99.48%**
85. **`iokit/Kernel/IODeviceTreeSupport.cpp`** -> AI Confidence: **99.48%**
86. **`iokit/Kernel/IOHibernateIO.cpp`** -> AI Confidence: **99.48%**
87. **`iokit/Kernel/IOMemoryDescriptor.cpp`** -> AI Confidence: **99.48%**
88. **`iokit/Kernel/IOPolledInterface.cpp`** -> AI Confidence: **99.48%**
89. **`iokit/Kernel/RootDomainUserClient.cpp`** -> AI Confidence: **99.48%**
90. **`iokit/Tests/TestCollections.cpp`** -> AI Confidence: **99.48%**
91. **`SETUP/json_compilation_db/json_compilation_db.c`** -> AI Confidence: **99.39%**
92. **`SETUP/kextsymboltool/kextsymboltool.c`** -> AI Confidence: **99.39%**
93. **`SETUP/setsegname/setsegname.c`** -> AI Confidence: **99.39%**
94. **`bsd/dev/unix_startup.c`** -> AI Confidence: **99.39%**
95. **`bsd/dev/vn/shadow.c`** -> AI Confidence: **99.39%**
96. **`bsd/kern/imageboot.c`** -> AI Confidence: **99.39%**
97. **`bsd/kern/kern_asl.c`** -> AI Confidence: **99.39%**
98. **`bsd/kern/kern_descrip.c`** -> AI Confidence: **99.39%**
99. **`bsd/kern/kern_exit.c`** -> AI Confidence: **99.39%**
100. **`bsd/kern/kern_memorystatus.c`** -> AI Confidence: **99.39%**
101. **`bsd/kern/kern_mman.c`** -> AI Confidence: **99.39%**
102. **`bsd/kern/kern_physio.c`** -> AI Confidence: **99.39%**
103. **`bsd/kern/kern_priv.c`** -> AI Confidence: **99.39%**
104. **`bsd/kern/kern_resource.c`** -> AI Confidence: **99.39%**
105. **`bsd/kern/kern_sfi.c`** -> AI Confidence: **99.39%**
106. **`bsd/kern/kern_subr.c`** -> AI Confidence: **99.39%**
107. **`bsd/kern/kern_synch.c`** -> AI Confidence: **99.39%**
108. **`bsd/kern/sys_coalition.c`** -> AI Confidence: **99.39%**
109. **`bsd/kern/tty.c`** -> AI Confidence: **99.39%**
110. **`bsd/kern/tty_dev.c`** -> AI Confidence: **99.39%**
111. **`bsd/kern/uipc_socket.c`** -> AI Confidence: **99.39%**
112. **`bsd/miscfs/devfs/devfs_tree.c`** -> AI Confidence: **99.39%**
113. **`bsd/net/classq/classq.c`** -> AI Confidence: **99.39%**
114. **`bsd/net/if.c`** -> AI Confidence: **99.39%**
115. **`bsd/net/pf_ioctl.c`** -> AI Confidence: **99.39%**
116. **`bsd/net/pktsched/pktsched_fq_codel.c`** -> AI Confidence: **99.39%**
117. **`bsd/netinet/ip_id.c`** -> AI Confidence: **99.39%**
118. **`bsd/netinet/ip_output.c`** -> AI Confidence: **99.39%**
119. **`bsd/netinet6/esp_input.c`** -> AI Confidence: **99.39%**
120. **`bsd/netinet6/ip6_forward.c`** -> AI Confidence: **99.39%**
121. **`bsd/netinet6/nd6.c`** -> AI Confidence: **99.39%**
122. **`bsd/nfs/nfs_serv.c`** -> AI Confidence: **99.39%**
123. **`bsd/nfs/nfs_vfsops.c`** -> AI Confidence: **99.39%**
124. **`bsd/vfs/vfs_cache.c`** -> AI Confidence: **99.39%**
125. **`bsd/vfs/vfs_cluster.c`** -> AI Confidence: **99.39%**
126. **`bsd/vfs/vfs_fsevents.c`** -> AI Confidence: **99.39%**
127. **`bsd/vfs/vfs_lookup.c`** -> AI Confidence: **99.39%**
128. **`bsd/vfs/vfs_subr.c`** -> AI Confidence: **99.39%**
129. **`bsd/vfs/vfs_syscalls.c`** -> AI Confidence: **99.39%**
130. **`bsd/vm/vm_compressor_backing_file.c`** -> AI Confidence: **99.39%**
131. **`libkern/kxld/kxld_object.c`** -> AI Confidence: **99.39%**
132. **`osfmk/arm/arm_vm_init.c`** -> AI Confidence: **99.39%**
133. **`osfmk/arm/locks_arm.c`** -> AI Confidence: **99.39%**
134. **`osfmk/arm64/arm_vm_init.c`** -> AI Confidence: **99.39%**
135. **`osfmk/device/iokit_rpc.c`** -> AI Confidence: **99.39%**
136. **`osfmk/i386/bsd_i386.c`** -> AI Confidence: **99.39%**
137. **`osfmk/i386/cpu_threads.c`** -> AI Confidence: **99.39%**
138. **`osfmk/i386/hibernate_i386.c`** -> AI Confidence: **99.39%**
139. **`osfmk/i386/locks_i386.c`** -> AI Confidence: **99.39%**
140. **`osfmk/i386/pcb_native.c`** -> AI Confidence: **99.39%**
141. **`osfmk/ipc/ipc_entry.c`** -> AI Confidence: **99.39%**
142. **`osfmk/ipc/ipc_importance.c`** -> AI Confidence: **99.39%**
143. **`osfmk/ipc/ipc_kmsg.c`** -> AI Confidence: **99.39%**
144. **`osfmk/ipc/ipc_object.c`** -> AI Confidence: **99.39%**
145. **`osfmk/kdp/ml/arm/kdp_vm.c`** -> AI Confidence: **99.39%**
146. **`osfmk/kdp/ml/i386/kdp_x86_common.c`** -> AI Confidence: **99.39%**
147. **`osfmk/kern/btlog.c`** -> AI Confidence: **99.39%**
148. **`osfmk/kern/gzalloc.c`** -> AI Confidence: **99.39%**
149. **`osfmk/kern/ipc_host.c`** -> AI Confidence: **99.39%**
150. **`osfmk/kern/ipc_tt.c`** -> AI Confidence: **99.39%**
151. **`osfmk/kern/sched_average.c`** -> AI Confidence: **99.39%**
152. **`osfmk/kern/sched_prim.c`** -> AI Confidence: **99.39%**
153. **`osfmk/kern/task_policy.c`** -> AI Confidence: **99.39%**
154. **`osfmk/vm/vm_compressor.c`** -> AI Confidence: **99.39%**
155. **`osfmk/vm/vm_fourk_pager.c`** -> AI Confidence: **99.39%**
156. **`osfmk/vm/vm_tests.c`** -> AI Confidence: **99.39%**
157. **`osfmk/x86_64/pmap.c`** -> AI Confidence: **99.39%**
158. **`pexpert/arm/pe_fiq.c`** -> AI Confidence: **99.39%**
159. **`tests/dirtiness_tracking.c`** -> AI Confidence: **99.39%**
160. **`tests/fd_aio_fsync_uaf.c`** -> AI Confidence: **99.39%**
161. **`tests/jumbo_va_spaces_28530648.c`** -> AI Confidence: **99.39%**
162. **`tests/task_info.c`** -> AI Confidence: **99.39%**
163. **`tests/testposixshm.c`** -> AI Confidence: **99.39%**
164. **`tests/text_corruption_helper.c`** -> AI Confidence: **99.39%**
165. **`tests/tty_hang.c`** -> AI Confidence: **99.39%**
166. **`tests/vm/entitlement_increased_memory_limit.c`** -> AI Confidence: **99.39%**
167. **`tools/lockstat/lockstat.c`** -> AI Confidence: **99.39%**
168. **`tools/tests/MPMMTest/KQMPMMtest.c`** -> AI Confidence: **99.39%**
169. **`tools/tests/MPMMTest/MPMMtest.c`** -> AI Confidence: **99.39%**
170. **`tools/tests/jitter/timer_jitter.c`** -> AI Confidence: **99.39%**
171. **`bsd/sys/wait.h`** -> AI Confidence: **99.39%**
172. **`libkern/libkern/OSKextLibPrivate.h`** -> AI Confidence: **99.39%**
173. **`iokit/Kernel/IOCatalogue.cpp`** -> AI Confidence: **99.39%**
174. **`iokit/Kernel/IODMACommand.cpp`** -> AI Confidence: **99.39%**
175. **`iokit/Kernel/IOInterruptEventSource.cpp`** -> AI Confidence: **99.39%**
176. **`iokit/Kernel/IOKitDebug.cpp`** -> AI Confidence: **99.39%**
177. **`iokit/Kernel/IONVRAM.cpp`** -> AI Confidence: **99.39%**
178. **`iokit/Kernel/IOPMrootDomain.cpp`** -> AI Confidence: **99.39%**
179. **`iokit/Kernel/IOServicePM.cpp`** -> AI Confidence: **99.39%**
180. **`iokit/Kernel/IOWorkLoop.cpp`** -> AI Confidence: **99.39%**
181. **`iokit/Tests/TestIOMemoryDescriptor.cpp`** -> AI Confidence: **99.39%**
182. **`libkern/c++/OSKext.cpp`** -> AI Confidence: **99.39%**
183. **`libkern/c++/OSRuntime.cpp`** -> AI Confidence: **99.39%**
184. **`SETUP/installfile/installfile.c`** -> AI Confidence: **99.35%**
185. **`bsd/dev/dtrace/fasttrap.c`** -> AI Confidence: **99.35%**
186. **`bsd/kern/kern_core.c`** -> AI Confidence: **99.35%**
187. **`bsd/kern/kern_memorystatus_notify.c`** -> AI Confidence: **99.35%**
188. **`bsd/kern/kern_symfile.c`** -> AI Confidence: **99.35%**
189. **`bsd/kern/tty_compat.c`** -> AI Confidence: **99.35%**
190. **`bsd/net/pf.c`** -> AI Confidence: **99.35%**
191. **`bsd/nfs/nfs_syscalls.c`** -> AI Confidence: **99.35%**
192. **`bsd/nfs/nfs_vnops.c`** -> AI Confidence: **99.35%**
193. **`osfmk/ipc/mach_kernelrpc.c`** -> AI Confidence: **99.35%**
194. **`osfmk/kdp/kdp_core.c`** -> AI Confidence: **99.35%**
195. **`osfmk/vm/vm_shared_region_pager.c`** -> AI Confidence: **99.35%**
196. **`tests/turnstile_multihop_helper.h`** -> AI Confidence: **99.35%**
197. **`libkdd/kcdata_core.m`** -> AI Confidence: **99.34%**
198. **`libkdd/kdd_main.m`** -> AI Confidence: **99.34%**
199. **`osfmk/console/art/progress.m`** -> AI Confidence: **99.34%**
200. **`bsd/dev/dtrace/blist.c`** -> AI Confidence: **99.34%**
201. **`bsd/dev/i386/dtrace_subr_x86.c`** -> AI Confidence: **99.34%**
202. **`bsd/net/flowhash.c`** -> AI Confidence: **99.34%**
203. **`bsd/security/audit/audit_bsm_domain.c`** -> AI Confidence: **99.34%**
204. **`bsd/security/audit/audit_bsm_errno.c`** -> AI Confidence: **99.34%**
205. **`iokit/Kernel/IOStringFuncs.c`** -> AI Confidence: **99.34%**
206. **`libkern/stdio/scanf.c`** -> AI Confidence: **99.34%**
207. **`osfmk/i386/pmap_x86_common.c`** -> AI Confidence: **99.34%**
208. **`osfmk/mach/semaphore.h`** -> AI Confidence: **99.34%**
209. **`tests/posix_spawn_archpref.c`** -> AI Confidence: **99.34%**
210. **`tests/sigcont_return.c`** -> AI Confidence: **99.34%**
211. **`tests/work_interval_test_unentitled.c`** -> AI Confidence: **99.34%**
212. **`EXTERNAL_HEADERS/corecrypto/cc_runtime_config.h`** -> AI Confidence: **99.34%**
213. **`EXTERNAL_HEADERS/img4/api.h`** -> AI Confidence: **99.34%**
214. **`iokit/IOKit/IOLocksPrivate.h`** -> AI Confidence: **99.34%**
215. **`osfmk/arm/machine_cpu.h`** -> AI Confidence: **99.34%**
216. **`osfmk/i386/pmap_internal.h`** -> AI Confidence: **99.34%**
217. **`iokit/Kernel/IOReporter.cpp`** -> AI Confidence: **99.34%**
218. **`iokit/bsddev/DINetBootHook.cpp`** -> AI Confidence: **99.34%**
219. **`libkern/c++/OSSerializeBinary.cpp`** -> AI Confidence: **99.34%**
220. **`tools/tests/perf_index/PerfIndex_COPS_Module/PITest.m`** -> AI Confidence: **99.32%**
221. **`SETUP/decomment/decomment.c`** -> AI Confidence: **99.32%**
222. **`bsd/dev/i386/dis_tables.c`** -> AI Confidence: **99.32%**
223. **`bsd/libkern/strsep.c`** -> AI Confidence: **99.32%**
224. **`bsd/sys/sfi.h`** -> AI Confidence: **99.32%**
225. **`libkern/mkext.c`** -> AI Confidence: **99.32%**
226. **`libkern/net/inet_aton.c`** -> AI Confidence: **99.32%**
227. **`osfmk/corecrypto/ccsha256_ltc_compress.c`** -> AI Confidence: **99.32%**
228. **`tests/vm/kern_max_task_pmem.c`** -> AI Confidence: **99.32%**
229. **`bsd/net/if_ppp.h`** -> AI Confidence: **99.32%**
230. **`bsd/sys/_select.h`** -> AI Confidence: **99.32%**
231. **`libkern/libkern/_OSByteOrder.h`** -> AI Confidence: **99.32%**
232. **`libkern/os/atomic_private.h`** -> AI Confidence: **99.32%**
233. **`osfmk/arm64/exception_asm.h`** -> AI Confidence: **99.32%**
234. **`osfmk/arm64/machine_routines_asm.h`** -> AI Confidence: **99.32%**
235. **`osfmk/i386/cpu_capabilities.h`** -> AI Confidence: **99.32%**
236. **`osfmk/kern/percpu.h`** -> AI Confidence: **99.32%**
237. **`osfmk/mach/machine/asm.h`** -> AI Confidence: **99.32%**
238. **`osfmk/machine/asm.h`** -> AI Confidence: **99.32%**
239. **`osfmk/machine/atomic.h`** -> AI Confidence: **99.32%**
240. **`osfmk/machine/lowglobals.h`** -> AI Confidence: **99.32%**
241. **`osfmk/machine/machine_kpc.h`** -> AI Confidence: **99.32%**
242. **`pexpert/pexpert/machine/boot.h`** -> AI Confidence: **99.32%**
243. **`iokit/Kernel/IOMultiMemoryDescriptor.cpp`** -> AI Confidence: **99.32%**
244. **`tools/lldbmacros/net.py`** -> AI Confidence: **99.32%**
245. **`tools/lldbmacros/scheduler.py`** -> AI Confidence: **99.32%**
246. **`tests/ipsec.m`** -> AI Confidence: **99.31%**
247. **`bsd/conf/param.c`** -> AI Confidence: **99.31%**
248. **`bsd/dev/arm/conf.c`** -> AI Confidence: **99.31%**
249. **`bsd/dev/arm/dtrace_isa.c`** -> AI Confidence: **99.31%**
250. **`bsd/dev/arm/dtrace_subr_arm.c`** -> AI Confidence: **99.31%**
251. **`bsd/dev/arm/sdt_arm.c`** -> AI Confidence: **99.31%**
252. **`bsd/dev/arm/sysctl.c`** -> AI Confidence: **99.31%**
253. **`bsd/dev/arm/systemcalls.c`** -> AI Confidence: **99.31%**
254. **`bsd/dev/arm/unix_signal.c`** -> AI Confidence: **99.31%**
255. **`bsd/dev/arm64/conf.c`** -> AI Confidence: **99.31%**
256. **`bsd/dev/arm64/dtrace_isa.c`** -> AI Confidence: **99.31%**
257. **`bsd/dev/arm64/dtrace_subr_arm.c`** -> AI Confidence: **99.31%**
258. **`bsd/dev/arm64/fasttrap_isa.c`** -> AI Confidence: **99.31%**
259. **`bsd/dev/dtrace/dtrace_subr.c`** -> AI Confidence: **99.31%**
260. **`bsd/dev/dtrace/fbt.c`** -> AI Confidence: **99.31%**
261. **`bsd/dev/dtrace/lockprof.c`** -> AI Confidence: **99.31%**
262. **`bsd/dev/dtrace/profile_prvd.c`** -> AI Confidence: **99.31%**
263. **`bsd/dev/dtrace/systrace.c`** -> AI Confidence: **99.31%**
264. **`bsd/dev/i386/conf.c`** -> AI Confidence: **99.31%**
265. **`bsd/dev/i386/dtrace_isa.c`** -> AI Confidence: **99.31%**
266. **`bsd/dev/i386/unix_signal.c`** -> AI Confidence: **99.31%**
267. **`bsd/dev/mem.c`** -> AI Confidence: **99.31%**
268. **`bsd/dev/memdev.c`** -> AI Confidence: **99.31%**
269. **`bsd/dev/monotonic.c`** -> AI Confidence: **99.31%**
270. **`bsd/dev/random/randomdev.c`** -> AI Confidence: **99.31%**
271. **`bsd/dev/vn/vn.c`** -> AI Confidence: **99.31%**
272. **`bsd/kern/bsd_init.c`** -> AI Confidence: **99.31%**
273. **`bsd/kern/bsd_stubs.c`** -> AI Confidence: **99.31%**
274. **`bsd/kern/chunklist.c`** -> AI Confidence: **99.31%**
275. **`bsd/kern/decmpfs.c`** -> AI Confidence: **99.31%**
276. **`bsd/kern/kdebug.c`** -> AI Confidence: **99.31%**
277. **`bsd/kern/kern_acct.c`** -> AI Confidence: **99.31%**
278. **`bsd/kern/kern_aio.c`** -> AI Confidence: **99.31%**
279. **`bsd/kern/kern_authorization.c`** -> AI Confidence: **99.31%**
280. **`bsd/kern/kern_credential.c`** -> AI Confidence: **99.31%**
281. **`bsd/kern/kern_csr.c`** -> AI Confidence: **99.31%**
282. **`bsd/kern/kern_event.c`** -> AI Confidence: **99.31%**
283. **`bsd/kern/kern_guarded.c`** -> AI Confidence: **99.31%**
284. **`bsd/kern/kern_lockf.c`** -> AI Confidence: **99.31%**
285. **`bsd/kern/kern_mib.c`** -> AI Confidence: **99.31%**
286. **`bsd/kern/kern_newsysctl.c`** -> AI Confidence: **99.31%**
287. **`bsd/kern/kern_ntptime.c`** -> AI Confidence: **99.31%**
288. **`bsd/kern/kern_overrides.c`** -> AI Confidence: **99.31%**
289. **`bsd/kern/kern_persona.c`** -> AI Confidence: **99.31%**
290. **`bsd/kern/kern_proc.c`** -> AI Confidence: **99.31%**
291. **`bsd/kern/kern_prot.c`** -> AI Confidence: **99.31%**
292. **`bsd/kern/kern_shutdown.c`** -> AI Confidence: **99.31%**
293. **`bsd/kern/kern_sig.c`** -> AI Confidence: **99.31%**
294. **`bsd/kern/kern_time.c`** -> AI Confidence: **99.31%**
295. **`bsd/kern/kern_xxx.c`** -> AI Confidence: **99.31%**
296. **`bsd/kern/kpi_mbuf.c`** -> AI Confidence: **99.31%**
297. **`bsd/kern/kpi_socket.c`** -> AI Confidence: **99.31%**
298. **`bsd/kern/kpi_socketfilter.c`** -> AI Confidence: **99.31%**
299. **`bsd/kern/mach_loader.c`** -> AI Confidence: **99.31%**
300. **`bsd/kern/mach_process.c`** -> AI Confidence: **99.31%**
301. **`bsd/kern/policy_check.c`** -> AI Confidence: **99.31%**
302. **`bsd/kern/posix_sem.c`** -> AI Confidence: **99.31%**
303. **`bsd/kern/posix_shm.c`** -> AI Confidence: **99.31%**
304. **`bsd/kern/proc_info.c`** -> AI Confidence: **99.31%**
305. **`bsd/kern/proc_uuid_policy.c`** -> AI Confidence: **99.31%**
306. **`bsd/kern/socket_info.c`** -> AI Confidence: **99.31%**
307. **`bsd/kern/stackshot.c`** -> AI Confidence: **99.31%**
308. **`bsd/kern/sys_generic.c`** -> AI Confidence: **99.31%**
309. **`bsd/kern/sys_persona.c`** -> AI Confidence: **99.31%**
310. **`bsd/kern/sys_socket.c`** -> AI Confidence: **99.31%**
311. **`bsd/kern/sys_ulock.c`** -> AI Confidence: **99.31%**
312. **`bsd/kern/sys_work_interval.c`** -> AI Confidence: **99.31%**
313. **`bsd/kern/sysv_msg.c`** -> AI Confidence: **99.31%**
314. **`bsd/kern/sysv_sem.c`** -> AI Confidence: **99.31%**
315. **`bsd/kern/sysv_shm.c`** -> AI Confidence: **99.31%**
316. **`bsd/kern/tty_pty.c`** -> AI Confidence: **99.31%**
317. **`bsd/kern/tty_tty.c`** -> AI Confidence: **99.31%**
318. **`bsd/kern/ubc_subr.c`** -> AI Confidence: **99.31%**
319. **`bsd/kern/uipc_mbuf.c`** -> AI Confidence: **99.31%**
320. **`bsd/kern/uipc_socket2.c`** -> AI Confidence: **99.31%**
321. **`bsd/kern/uipc_syscalls.c`** -> AI Confidence: **99.31%**
322. **`bsd/kern/uipc_usrreq.c`** -> AI Confidence: **99.31%**
323. **`bsd/miscfs/bindfs/bind_vfsops.c`** -> AI Confidence: **99.31%**
324. **`bsd/miscfs/bindfs/bind_vnops.c`** -> AI Confidence: **99.31%**
325. **`bsd/miscfs/devfs/devfs_vnops.c`** -> AI Confidence: **99.31%**
326. **`bsd/miscfs/fifofs/fifo_vnops.c`** -> AI Confidence: **99.31%**
327. **`bsd/miscfs/nullfs/null_vfsops.c`** -> AI Confidence: **99.31%**
328. **`bsd/miscfs/nullfs/null_vnops.c`** -> AI Confidence: **99.31%**
329. **`bsd/miscfs/specfs/spec_vnops.c`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `osfmk/kern/zalloc.c` -> **0.0064%** Exposure
### Exploit Generation Surface
- `libkdd/tests/Tests.swift` -> **100.0%** Exposure
- `tools/lldbmacros/apic.py` -> **100.0%** Exposure
- `tools/lldbmacros/core/caching.py` -> **100.0%** Exposure
- `tools/lldbmacros/core/cvalue.py` -> **100.0%** Exposure
- `tools/lldbmacros/core/kernelcore.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `libkern/kxld/Makefile` -> **100.0%** Exposure
- `tools/tests/perf_index/Makefile` -> **100.0%** Exposure
- `bsd/dev/dtrace/fasttrap.c` -> **100.0%** Exposure
- `osfmk/arm/arm_vm_init.c` -> **100.0%** Exposure
- `tests/extract_right_soft_fail.c` -> **100.0%** Exposure
### Raw Memory Manipulation
- `bsd/dev/arm/fasttrap_isa.c` -> **10.0%** Exposure
- `bsd/dev/arm/munge.c` -> **10.0%** Exposure
- `bsd/dev/dtrace/dtrace.c` -> **10.0%** Exposure
- `bsd/dev/dtrace/fasttrap.c` -> **10.0%** Exposure
- `bsd/dev/dtrace/fbt.c` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `libkdd/kcdata_core.m` -> **100.0%** Exposure
- `osfmk/console/art/progress.m` -> **100.0%** Exposure
- `tests/hvtest_x86.m` -> **100.0%** Exposure
- `tests/stackshot_tests.m` -> **100.0%** Exposure
- `SETUP/kextsymboltool/kextsymboltool.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `25089` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `bsd/kern/kern_prot.c` (C) -> Cumulative Risk: **762.82**
- **Archetype:** `file_cluster_13` (Distance: 13.399 IQR)
- **Magnitude:** 863.18 | **LOC:** 2165 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.5807%)
- **Heaviest Functions:** `gettid` (Impact: 98.2), `setregid` (Impact: 52.6), `setgroups_internal` (Impact: 32.8)

### 2. `osfmk/kern/locks.c` (C) -> Cumulative Risk: **757.37**
- **Archetype:** `file_cluster_8` (Distance: 12.907 IQR)
- **Magnitude:** 2404.38 | **LOC:** 3265 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9982%), Documentation (96.1108%)
- **Heaviest Functions:** `hw_lock_trylock_contended` (Impact: 1494.1), `lck_grp_lckcnt_decr` (Impact: 23.4), `lck_grp_lckcnt_incr` (Impact: 23.3)

### 3. `bsd/dev/i386/fasttrap_isa.c` (C) -> Cumulative Risk: **752.05**
- **Archetype:** `file_cluster_8` (Distance: 14.07 IQR)
- **Magnitude:** 1676.88 | **LOC:** 2319 | **CtrlFlow:** 86.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.4935%)
- **Heaviest Functions:** `fasttrap_tracepoint_init` (Impact: 171.2), `fasttrap_do_seg` (Impact: 82.7), `fasttrap_return_common` (Impact: 50.9)

### 4. `bsd/net/classq/classq_subr.c` (C) -> Cumulative Risk: **744.51**
- **Archetype:** `file_cluster_13` (Distance: 13.355 IQR)
- **Magnitude:** 805.5 | **LOC:** 786 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.6294%)
- **Heaviest Functions:** `ifclassq_dequeue_common_default` (Impact: 100.2), `ifclassq_tbr_set` (Impact: 90.2), `ifclassq_tbr_dequeue_common` (Impact: 34.0)

### 5. `osfmk/i386/hibernate_i386.c` (C) -> Cumulative Risk: **744.37**
- **Archetype:** `file_cluster_13` (Distance: 12.935 IQR)
- **Magnitude:** 289.6 | **LOC:** 306 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.8433%)
- **Heaviest Functions:** `hibernate_page_list_allocate` (Impact: 79.8), `hibernate_vm_unlock` (Impact: 3.3), `hibernate_vm_lock` (Impact: 3.2)

### 6. `osfmk/arm/machine_routines_common.c` (C) -> Cumulative Risk: **742.6**
- **Archetype:** `file_cluster_8` (Distance: 13.099 IQR)
- **Magnitude:** 910.18 | **LOC:** 1091 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.6141%), Algorithmic Dos (98.1817%)
- **Heaviest Functions:** `sched_perfcontrol_register_callbacks` (Impact: 77.4), `ml_set_interrupts_enabled` (Impact: 16.0), `__ml_check_interrupts_disabled_duration` (Impact: 13.8)

### 7. `bsd/vfs/vfs_vnops.c` (C) -> Cumulative Risk: **741.9**
- **Archetype:** `file_cluster_13` (Distance: 13.972 IQR)
- **Magnitude:** 1983.56 | **LOC:** 2111 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (97.9799%)
- **Heaviest Functions:** `vn_read` (Impact: 691.6), `vn_open_auth_do_create` (Impact: 100.4), `vn_rdwr_64` (Impact: 66.4)

### 8. `bsd/net/if.c` (C) -> Cumulative Risk: **739.95**
- **Archetype:** `file_cluster_11` (Distance: 18.881 IQR)
- **Magnitude:** 4383.2 | **LOC:** 5812 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.823%)
- **Heaviest Functions:** `ifioctl_get_protolist` (Impact: 1048.8), `if_addmulti_common` (Impact: 530.1), `if_detach_ifma` (Impact: 51.5)

### 9. `libkern/kernel_mach_header.c` (C) -> Cumulative Risk: **738.76**
- **Archetype:** `file_cluster_8` (Distance: 12.866 IQR)
- **Magnitude:** 282.48 | **LOC:** 374 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9935%)
- **Heaviest Functions:** `getsectbynamefromheader` (Impact: 13.7), `getlastaddr` (Impact: 6.7), `nextsegfromheader` (Impact: 6.5)

### 10. `osfmk/arm/locks_arm.c` (C) -> Cumulative Risk: **738.56**
- **Archetype:** `file_cluster_8` (Distance: 13.518 IQR)
- **Magnitude:** 1544.74 | **LOC:** 3082 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (97.2373%)
- **Heaviest Functions:** `kernel_preempt_check` (Impact: 405.6), `lck_spin_assert` (Impact: 23.6), `lck_mtx_assert` (Impact: 17.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `bsd/net/pf.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.227 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.845 IQR)
- **Top Global Matches:** file_cluster_8: 15.227, file_cluster_13: 15.387, file_cluster_11: 15.442
- **Magnitude:** 21191.36 | **LOC:** 10804 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 475
- **Risk Profile:** Cognitive Load (97.0658%), Tech Debt (12.2798%)
**Top Internal Functions/Classes:**
  * `pf_src_connlimit` (Impact: 6735.6 | O(2^N) | DB: 415)
  * `pf_route` (Impact: 4350.1 | O(2^N) | DB: 391)
  * `pf_test_rule` (Impact: 3845.6 | O(N^2) | DB: 475)
  * `pf_translate_icmp_af` (Impact: 295.6 | O(N^2) | DB: 60)
  * `pf_state_compare_lan_ext` (Impact: 87.3 | O(N^1) | DB: 18)
    * *Intent:* #define PF_IKE_PACKET_MINSIZE (sizeof (struct pf_ike_hdr)) #define PF_IKEv1_EXCHTYPE_BASE 1 #define ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2223`, `structural_boundaries: 990`, `args: 149`, `func_start: 93`, `class_start: 299`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4266`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 10`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 1084`, `import: 49`
* *Defense:* `safety: 4`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tcp.h, param.h, protosw.h, proc.h, random.h, nat464_utils.h, udp_var.h, endian.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `EXTERNAL_HEADERS/AvailabilityInternal.h` (C | Tier 4 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.01 IQR)
- **Top Global Matches:** file_cluster_8: 15.01, file_cluster_0: 15.188, file_cluster_7: 15.493
- **Magnitude:** 14638.52 | **LOC:** 23427 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (48.1307%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1546`
* *Risk/State:* `state_mutation: 14158`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bsd/netkey/key.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.589 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.805 IQR)
- **Top Global Matches:** file_cluster_8: 14.589, file_cluster_13: 14.698, file_cluster_11: 14.757
- **Magnitude:** 11393.36 | **LOC:** 10513 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 426
- **Risk Profile:** Cognitive Load (96.1268%), Tech Debt (40.3067%)
**Top Internal Functions/Classes:**
  * `key_gather_mbuf` (Impact: 4441.4 | O(2^N) | DB: 426)
  * `key_alloc_outbound_sav_for_interface` (Impact: 657.7 | O(N^2) | DB: 144)
  * `key_parse` (Impact: 292.0 | O(2^N) | DB: 38)
    * *Intent:* #endif
  * `key_register` (Impact: 224.9 | O(2^N) | DB: 56)
  * `key_align` (Impact: 224.6 | O(2^N) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1428`, `structural_boundaries: 1163`, `args: 277`, `func_start: 81`, `class_start: 248`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 2953`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 43`, `orphaned_logic: 9`
* *Architecture:* `io: 42`, `api: 940`, `import: 44`
* *Defense:* `safety: 10`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` param.h, protosw.h, proc.h, esp.h, random.h, raw_cb.h, endian.h, ip6_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `osfmk/vm/vm_map.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.779 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.152 IQR)
- **Top Global Matches:** file_cluster_8: 14.779, file_cluster_13: 14.94, file_cluster_11: 14.982
- **Magnitude:** 9540.2 | **LOC:** 21972 | **CtrlFlow:** 81.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 362
- **Risk Profile:** Cognitive Load (92.2426%), Tech Debt (16.586%)
**Top Internal Functions/Classes:**
  * `vm_map_remap` (Impact: 2161.9 | O(N^6) | DB: 362)
    * *Intent:* /* We unwired what the caller asked for: zero pages */
  * `vm_map_enter_mem_object_control` (Impact: 378.8 | O(N^2) | DB: 77)
  * `vm_map_enter_fourk` (Impact: 216.0 | O(N^2) | DB: 101)
  * `vm_map_remap_extract` (Impact: 145.8 | O(N^2) | DB: 78)
  * `vm_map_copy_validate_size` (Impact: 122.1 | O(N^3) | DB: 50)
    * *Intent:* /* * We need to resolve our side of this * "symmetric" copy-on-write now; we * need a new object to ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1563`, `structural_boundaries: 360`, `args: 36`, `func_start: 111`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3952`, `dead_code: 12`, `planned_debt: 3`, `fragile_debt: 15`, `orphaned_logic: 19`
* *Architecture:* `io: 2`, `api: 1433`, `import: 44`
* *Defense:* `safety: 170`, `test: 169`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sched_prim.h, OSAtomic.h, cpu_capabilities.h, kalloc.h, exc_guard.h, vm_map_server.h, kern_return.h, vm_kern.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/kern/uipc_socket.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.893 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.945 IQR)
- **Top Global Matches:** file_cluster_8: 14.893, file_cluster_13: 14.906, file_cluster_11: 15.018
- **Magnitude:** 8712.88 | **LOC:** 8016 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 641
- **Risk Profile:** Cognitive Load (98.2032%), Tech Debt (16.802%)
**Top Internal Functions/Classes:**
  * `soconnectxlocked` (Impact: 5586.8 | O(N^3) | DB: 641)
  * `sosetdefunct` (Impact: 92.7 | O(N^2) | DB: 19)
    * *Intent:* /* * Let's try to get normal data: * EWOULDBLOCK: out-of-band data not
  * `so_set_restrictions` (Impact: 56.9 | O(N^1) | DB: 46)
  * `sodefunct` (Impact: 40.9 | O(N^1) | DB: 11)
  * `soconnectlock` (Impact: 39.2 | O(N^1) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 976`, `structural_boundaries: 403`, `args: 128`, `func_start: 69`, `class_start: 74`
* *Risk/State:* `state_mutation: 2050`, `planned_debt: 2`, `orphaned_logic: 18`
* *Architecture:* `io: 96`, `api: 460`, `import: 58`
* *Defense:* `safety: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` param.h, un.h, protosw.h, OSAtomic.h, proc.h, mptcp_var.h, flow_divert.h, ip6_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `iokit/Kernel/IOPMrootDomain.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.231 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.836 IQR)
- **Top Global Matches:** file_cluster_8: 15.231, file_cluster_13: 15.377, file_cluster_11: 15.465
- **Magnitude:** 8297.28 | **LOC:** 12586 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 595
- **Risk Profile:** Cognitive Load (82.7091%), Tech Debt (31.9947%)
**Top Internal Functions/Classes:**
  * `IOPMrootDomain::start` (Impact: 1915.3 | O(N^3) | DB: 595)
  * `PMAssertionsTracker::reportCPUBitAccount` (Impact: 740.0 | O(N^2) | DB: 307)
    * *Intent:* *hibMode |= (kIOHibernateModeOn | kIOHibernateModeSleep);
  * `IOPMrootDomain::evaluatePolicy` (Impact: 215.4 | O(N^1) | DB: 93)
  * `IOPMrootDomain::overridePowerChangeForSe` (Impact: 186.5 | O(N^2) | DB: 89)
  * `IOPMrootDomain::evaluateSystemSleepPolic` (Impact: 113.3 | O(N^1) | DB: 63)
    * *Intent:* *cancel = true;
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1200`, `structural_boundaries: 410`, `args: 278`, `func_start: 133`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 22`, `state_mutation: 4412`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 4`, `orphaned_logic: 42`
* *Architecture:* `api: 4`, `import: 47`
* *Defense:* `safety: 9`, `doc: 81`, `test: 12`, `sync_locks: 1`, `immutability_locks: 132`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` IOKitDebug.h, OSAtomic.h, IOCatalogue.h, IOServicePMPrivate.h, IOCPU.h, zlib.h, OSBoundedArrayRef.h, log.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/vfs/vfs_syscalls.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.515 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.423 IQR)
- **Top Global Matches:** file_cluster_13: 14.515, file_cluster_8: 14.53, file_cluster_11: 14.638
- **Magnitude:** 8255.62 | **LOC:** 13443 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 300
- **Risk Profile:** Cognitive Load (97.9969%), Tech Debt (32.9943%)
**Top Internal Functions/Classes:**
  * `mount_common` (Impact: 5023.3 | O(2^N) | DB: 300)
  * `rmdirat_internal` (Impact: 224.0 | O(N^2) | DB: 78)
  * `fsetxattr` (Impact: 203.7 | O(N^1) | DB: 62)
  * `clonefile_internal` (Impact: 90.9 | O(N^1) | DB: 27)
  * `renameat_internal` (Impact: 48.9 | O(N^1) | DB: 50)
    * *Intent:* #endif
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 816`, `structural_boundaries: 340`, `args: 41`, `func_start: 59`, `class_start: 79`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1770`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 11`, `orphaned_logic: 19`
* *Architecture:* `io: 3`, `api: 669`, `concurrency: 6`, `import: 59`
* *Defense:* `safety: 9`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` param.h, stat.h, ubc_internal.h, OSAtomic.h, fsevents.h, namei.h, kalloc.h, ubc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/nfs/nfs4_vnops.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.931 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.682 IQR)
- **Top Global Matches:** file_cluster_8: 14.931, file_cluster_13: 14.987, file_cluster_11: 15.039
- **Magnitude:** 7856.48 | **LOC:** 9101 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 465
- **Risk Profile:** Cognitive Load (96.354%), Tech Debt (16.6986%)
**Top Internal Functions/Classes:**
  * `nfs_advlock_setlock` (Impact: 3460.6 | O(N^3) | DB: 450)
  * `nfs4_access_rpc` (Impact: 868.9 | O(N^1) | DB: 465)
    * *Intent:* #include <sys/conf.h> #include <sys/vnode_internal.h> #include <sys/dirent.h> #include <sys/fcntl.h>...
  * `nfs4_vnop_listxattr` (Impact: 196.2 | O(N^1) | DB: 64)
  * `nfs_file_lock_conflict` (Impact: 27.8 | O(N^1) | DB: 2)
  * `nfs4_getlock_rpc` (Impact: 15.1 | O(N^1) | DB: 18)
    * *Intent:* /* * Mark an open owner as busy because we are about to * start an operation that uses and updates o...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1118`, `structural_boundaries: 309`, `args: 34`, `func_start: 49`, `class_start: 146`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2567`, `dead_code: 9`, `fragile_debt: 11`, `orphaned_logic: 6`
* *Architecture:* `io: 31`, `api: 594`, `import: 43`
* *Defense:* `safety: 8`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sched_prim.h, param.h, nfsproto.h, ubc_internal.h, OSAtomic.h, nfsmount.h, lockf.h, nfs_gss.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/dev/dtrace/dtrace.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.14 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.534 IQR)
- **Top Global Matches:** file_cluster_8: 15.14, file_cluster_13: 15.301, file_cluster_11: 15.322
- **Magnitude:** 7626.48 | **LOC:** 19416 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 161
- **Risk Profile:** Cognitive Load (95.9501%), Tech Debt (14.4206%)
**Top Internal Functions/Classes:**
  * `dtrace_canload_remains` (Impact: 529.8 | O(2^N) | DB: 104)
    * *Intent:* #define DTRACE_HASHPREV(hash, elm) \
  * `dtrace_speculation_buffer` (Impact: 375.8 | O(N^2) | DB: 161)
    * *Intent:* /* * Convenience routine to check to see if the address is within a memory * region in which a load ...
  * `dtrace_state_destroy` (Impact: 308.8 | O(N^3) | DB: 100)
  * `dtrace_detach` (Impact: 175.2 | O(N^3) | DB: 29)
  * `dtrace_close` (Impact: 55.5 | O(N^1) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1882`, `structural_boundaries: 530`, `args: 54`, `func_start: 144`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 4800`, `planned_debt: 4`, `fragile_debt: 8`, `orphaned_logic: 14`
* *Architecture:* `io: 1`, `api: 902`, `import: 34`
* *Defense:* `safety: 78`, `doc: 3`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sched_prim.h, param.h, monotonic.h, stat.h, random.h, ioctl.h, kernel_types.h, zalloc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/kern/kern_event.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.771 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.668 IQR)
- **Top Global Matches:** file_cluster_13: 14.771, file_cluster_8: 14.798, file_cluster_11: 14.945
- **Magnitude:** 7057.82 | **LOC:** 9153 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 385
- **Risk Profile:** Cognitive Load (90.2266%), Tech Debt (8.5461%)
**Top Internal Functions/Classes:**
  * `filt_wlupdate` (Impact: 3386.5 | O(2^N) | DB: 385)
  * `kevent_internal` (Impact: 537.7 | O(N^3) | DB: 200)
  * `knote_post` (Impact: 133.0 | O(N^2) | DB: 53)
  * `knote_apply_touch` (Impact: 51.4 | O(N^1) | DB: 21)
  * `kqueue_process` (Impact: 40.7 | O(N^1) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 761`, `structural_boundaries: 697`, `args: 152`, `func_start: 143`, `class_start: 114`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2058`, `dead_code: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 5`, `api: 580`, `import: 54`
* *Defense:* `safety: 85`, `doc: 21`, `test: 74`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string.h, param.h, sched_prim.h, protosw.h, stat.h, net_str_id.h, kalloc.h, select.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/net/if_bridge.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.52 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.027 IQR)
- **Top Global Matches:** file_cluster_8: 14.52, file_cluster_11: 14.785, file_cluster_0: 14.819
- **Magnitude:** 6791.3 | **LOC:** 8838 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 361
- **Risk Profile:** Cognitive Load (96.8512%), Tech Debt (24.0907%)
**Top Internal Functions/Classes:**
  * `bridge_input` (Impact: 3114.9 | O(N^6) | DB: 361)
  * `bridge_iff_input` (Impact: 188.8 | O(2^N) | DB: 15)
  * `bridge_ioctl` (Impact: 164.4 | O(N^2) | DB: 25)
    * *Intent:* #define BRIDGE_RTABLE_PRUNE_PERIOD (5 * 60) #endif /* * Number of MAC NAT entries * - sized based on...
  * `bridge_iff_event` (Impact: 93.9 | O(N^2) | DB: 4)
  * `bridge_set_tso` (Impact: 88.8 | O(N^2) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 910`, `structural_boundaries: 676`, `args: 145`, `func_start: 99`, `class_start: 179`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 1919`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 14`, `orphaned_logic: 10`
* *Architecture:* `api: 597`
* *Defense:* `safety: 19`, `test: 4`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tcp.h, param.h, bootp.h, protosw.h, random.h, proc.h, ip6_var.h, nd6.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `osfmk/arm/pmap.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.162 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.434 IQR)
- **Top Global Matches:** file_cluster_8: 14.162, file_cluster_13: 14.339, file_cluster_7: 14.446
- **Magnitude:** 6676.7 | **LOC:** 15781 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 497
- **Risk Profile:** Cognitive Load (90.2065%), Tech Debt (10.4299%)
**Top Internal Functions/Classes:**
  * `pmap_pages_reclaim` (Impact: 1988.1 | O(2^N) | DB: 497)
  * `pmap_change_wiring_internal` (Impact: 300.2 | O(N^2) | DB: 63)
  * `pmap_protect_options_internal` (Impact: 87.0 | O(N^1) | DB: 54)
  * `wimg_to_pte` (Impact: 59.1 | O(N^1) | DB: 22)
    * *Intent:* /* * Routines to track and allocate physical pages during early boot. * On most systems that memory ...
  * `pmap_protect_options` (Impact: 41.3 | O(2^N) | DB: 6)
    * *Intent:* /*
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 907`, `structural_boundaries: 532`, `args: 81`, `func_start: 188`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 2801`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 19`, `api: 1068`, `import: 53`
* *Defense:* `safety: 63`, `doc: 22`, `test: 90`, `immutability_locks: 184`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` string.h, pgtrace.h, kalloc.h, ptrauth.h, spl.h, cpu_data.h, vm_kern.h, zalloc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/kern/kern_exec.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.684 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.729 IQR)
- **Top Global Matches:** file_cluster_8: 14.684, file_cluster_13: 14.71, file_cluster_11: 14.856
- **Magnitude:** 6651.12 | **LOC:** 7292 | **CtrlFlow:** 82.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 313
- **Risk Profile:** Cognitive Load (96.2804%), Tech Debt (11.7565%)
**Top Internal Functions/Classes:**
  * `exec_handle_port_actions` (Impact: 2409.5 | O(2^N) | DB: 313)
  * `exec_handle_sugid` (Impact: 181.1 | O(N^2) | DB: 41)
    * *Intent:* /* * If we have a spawn attr, and it contains signal related flags, * the we need to process them in...
  * `exec_add_apple_strings` (Impact: 140.4 | O(N^1) | DB: 65)
  * `exec_extract_strings` (Impact: 122.0 | O(N^1) | DB: 57)
  * `check_for_signature` (Impact: 111.8 | O(N^2) | DB: 41)
    * *Intent:* #endif
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1114`, `structural_boundaries: 229`, `args: 44`, `func_start: 38`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 8`, `state_mutation: 2468`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 6`, `orphaned_logic: 2`
* *Architecture:* `io: 8`, `api: 535`, `concurrency: 6`, `import: 92`
* *Defense:* `safety: 50`, `test: 21`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cpu_capabilities.h, shm_internal.h, dtrace_ptss.h, exec.h, sysctl.h, thread.h, assert.h, kern_memorystatus.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `iokit/Kernel/IOService.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.785 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.844 IQR)
- **Top Global Matches:** file_cluster_8: 14.785, file_cluster_13: 14.969, file_cluster_11: 15.086
- **Magnitude:** 6140.94 | **LOC:** 8388 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 529
- **Risk Profile:** Cognitive Load (92.8347%), Tech Debt (66.3669%)
**Top Internal Functions/Classes:**
  * `IOService::lockForArbitration` (Impact: 1597.2 | O(N^3) | DB: 529)
  * `IOService::newUserClient` (Impact: 509.8 | O(N^2) | DB: 121)
  * `IOService::initialize` (Impact: 120.8 | O(N^2) | DB: 171)
  * `IOService::updateConsoleUsers` (Impact: 103.3 | O(N^1) | DB: 45)
  * `IOService::startMatching` (Impact: 81.4 | O(N^2) | DB: 33)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 818`, `structural_boundaries: 369`, `args: 279`, `func_start: 145`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 87`, `high_risk_execution: 1`, `state_mutation: 3116`, `dead_code: 2`, `planned_debt: 3`, `duplicate_logic: 14`, `orphaned_logic: 49`
* *Architecture:* `import: 39`
* *Defense:* `safety: 23`, `doc: 2`, `sync_locks: 2`, `immutability_locks: 148`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` string.h, IOCatalogue.h, IOCPU.h, RootDomain.h, IOKernelReporters.h, OSContainers.h, OSSharedPtr.h, IOMessage.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libkern/c++/OSKext.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.766 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.85 IQR)
- **Top Global Matches:** file_cluster_8: 14.766, file_cluster_13: 14.889, file_cluster_7: 15.01
- **Magnitude:** 6014.12 | **LOC:** 15434 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 344
- **Risk Profile:** Cognitive Load (59.9729%), Tech Debt (11.1778%)
**Top Internal Functions/Classes:**
  * `OSKext_protect` (Impact: 1975.0 | O(2^N) | DB: 328)
    * *Intent:* /* Exclude builtin and codeless kexts */
  * `OSKext::removeKextBootstrap` (Impact: 630.9 | O(N^2) | DB: 262)
  * `OSKext::copyPersonalitiesArray` (Impact: 594.7 | O(N^2) | DB: 344)
  * `OSKext::sendAllKextPersonalitiesToCatalo` (Impact: 10.1 | O(N^1) | DB: 3)
  * `OSKext::unregisterWithDTrace` (Impact: 4.7 | O(N^1) | DB: 3)
    * *Intent:* /* If the plist has a UUID for an interface, save that off.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 816`, `structural_boundaries: 319`, `args: 260`, `func_start: 106`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 59`, `high_risk_execution: 7`, `state_mutation: 2725`, `dead_code: 4`, `fragile_debt: 4`, `orphaned_logic: 4`
* *Architecture:* `import: 44`
* *Defense:* `safety: 24`, `doc: 86`, `immutability_locks: 65`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` string.h, stat.h, random.h, IOCatalogue.h, zlib.h, host_special_ports.h, vm_kern.h, pexpert.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/nfs/nfs_vfsops.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.532 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.576 IQR)
- **Top Global Matches:** file_cluster_8: 14.532, file_cluster_13: 14.601, file_cluster_11: 14.719
- **Magnitude:** 5832.02 | **LOC:** 6775 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 436
- **Risk Profile:** Cognitive Load (95.627%), Tech Debt (13.7318%)
**Top Internal Functions/Classes:**
  * `nfs_convert_old_nfs_args` (Impact: 2165.3 | O(N^4) | DB: 436)
  * `nfs_mountinfo_assemble` (Impact: 921.2 | O(2^N) | DB: 93)
  * `nfs_mount_diskless` (Impact: 204.0 | O(2^N) | DB: 38)
  * `nfs_mount_cleanup` (Impact: 29.1 | O(N^1) | DB: 6)
  * `nfs_vfs_quotactl` (Impact: 20.0 | O(N^1) | DB: 9)
    * *Intent:* /* looks like we got an answer... */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 852`, `structural_boundaries: 243`, `args: 61`, `func_start: 30`, `class_start: 56`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1958`, `dead_code: 7`, `fragile_debt: 5`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 5`, `api: 444`, `import: 40`
* *Defense:* `safety: 11`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` param.h, un.h, nfsproto.h, OSAtomic.h, ioctl.h, nfsmount.h, nfs_gss.h, pexpert.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/nfs/nfs_vnops.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.572 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.246 IQR)
- **Top Global Matches:** file_cluster_13: 14.572, file_cluster_8: 14.6, file_cluster_11: 14.734
- **Magnitude:** 5680.5 | **LOC:** 8840 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 361
- **Risk Profile:** Cognitive Load (94.3868%), Tech Debt (13.4131%)
**Top Internal Functions/Classes:**
  * `nfs_dir_buf_search` (Impact: 3318.1 | O(2^N) | DB: 361)
  * `nfs_vnop_open` (Impact: 153.8 | O(2^N) | DB: 51)
  * `nfs_dir_buf_cache_lookup_boundaries` (Impact: 12.7 | O(N^1) | DB: 3)
    * *Intent:* { &vnop_readdir_desc, (vnop_t *)fifo_readdir }, /* readdir */ { &vnop_readlink_desc, (vnop_t *)fifo_...
  * `nfs3_access_rpc` (Impact: 11.9 | O(N^1) | DB: 19)
  * `nfs_rdirplus_update_node_attrs` (Impact: 10.7 | O(N^1) | DB: 11)
    * *Intent:* { &vnop_lookup_desc, (vnop_t *)fifo_lookup }, /* lookup */ { &vnop_create_desc, (vnop_t *)fifo_creat...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 577`, `structural_boundaries: 254`, `args: 49`, `func_start: 34`, `class_start: 85`
* *Risk/State:* `safety_bypasses: 243`, `state_mutation: 1677`, `dead_code: 3`, `fragile_debt: 4`, `orphaned_logic: 4`
* *Architecture:* `io: 9`, `api: 414`, `import: 43`
* *Defense:* `safety: 10`, `test: 2`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sched_prim.h, param.h, nfsproto.h, ubc_internal.h, OSAtomic.h, nfsmount.h, lockf.h, nfs_gss.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `iokit/Kernel/IOUserServer.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.763 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.668 IQR)
- **Top Global Matches:** file_cluster_8: 14.763, file_cluster_13: 14.952, file_cluster_11: 15.11
- **Magnitude:** 5591.56 | **LOC:** 4698 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 420
- **Risk Profile:** Cognitive Load (91.062%), Tech Debt (78.853%)
**Top Internal Functions/Classes:**
  * `IOUserServer::target` (Impact: 1592.9 | O(N^5) | DB: 420)
  * `IOUserServer::objectInstantiate` (Impact: 161.0 | O(N^2) | DB: 104)
  * `IOServiceNotificationDispatchSource::Cre` (Impact: 123.1 | O(N^4) | DB: 24)
  * `IOService::SetProperties_Impl` (Impact: 75.8 | O(N^5) | DB: 15)
  * `IODMACommand::PerformOperation_Impl` (Impact: 74.0 | O(N^1) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 650`, `structural_boundaries: 344`, `args: 217`, `func_start: 135`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 5`, `state_mutation: 2779`, `dead_code: 2`, `fragile_debt: 2`, `duplicate_logic: 4`, `orphaned_logic: 76`
* *Architecture:* `api: 2`, `import: 38`
* *Defense:* `safety: 50`, `sync_locks: 36`, `immutability_locks: 49`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` IOMultiMemoryDescriptor.h, IOInterruptDispatchSource.h, IOCatalogue.h, proc.h, IOUserServer.h, IOServiceNotificationDispatchSource.h, IODataQueueDispatchSource.h, IORegistryEntry.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/netinet/flow_divert.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.629 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.273 IQR)
- **Top Global Matches:** file_cluster_8: 14.629, file_cluster_13: 14.669, file_cluster_11: 14.732
- **Magnitude:** 5583.92 | **LOC:** 4394 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 469
- **Risk Profile:** Cognitive Load (97.704%), Tech Debt (12.8505%)
**Top Internal Functions/Classes:**
  * `flow_divert_trie_insert` (Impact: 1976.4 | O(2^N) | DB: 469)
  * `flow_divert_connect_out_internal` (Impact: 131.3 | O(N^1) | DB: 58)
  * `flow_divert_data_out` (Impact: 83.9 | O(N^1) | DB: 21)
  * `flow_divert_token_set` (Impact: 82.2 | O(N^1) | DB: 42)
  * `flow_divert_token_get` (Impact: 60.3 | O(N^1) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 920`, `structural_boundaries: 426`, `args: 76`, `func_start: 77`, `class_start: 85`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2117`, `dead_code: 1`, `fragile_debt: 4`, `orphaned_logic: 6`
* *Architecture:* `io: 72`, `api: 495`, `import: 42`
* *Defense:* `safety: 27`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tcp.h, string.h, protosw.h, ubc.h, flow_divert.h, log.h, ntstat.h, kpi_mbuf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `iokit/Kernel/IOServicePM.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.042 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.866 IQR)
- **Top Global Matches:** file_cluster_8: 15.042, file_cluster_13: 15.182, file_cluster_7: 15.246
- **Magnitude:** 5552.54 | **LOC:** 9056 | **CtrlFlow:** 75.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 411
- **Risk Profile:** Cognitive Load (58.4247%), Tech Debt (44.7094%)
**Top Internal Functions/Classes:**
  * `IOService::ackTimerTick` (Impact: 1519.3 | O(N^2) | DB: 411)
    * *Intent:* // Invalidate cached tickle power state when desires change, and not // due to a tickle request. In ...
  * `IOService::addPowerChild` (Impact: 111.8 | O(N^2) | DB: 31)
  * `IOService::PMinit` (Impact: 83.8 | O(N^2) | DB: 89)
  * `IOService::notifyChildren` (Impact: 82.7 | O(N^2) | DB: 26)
    * *Intent:* //********************************************************************************* // [protected] c...
  * `IOService::all_done` (Impact: 71.8 | O(N^1) | DB: 54)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 921`, `structural_boundaries: 305`, `args: 185`, `func_start: 118`
* *Risk/State:* `safety_bypasses: 60`, `high_risk_execution: 2`, `state_mutation: 2876`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 55`
* *Architecture:* `import: 27`
* *Defense:* `safety: 73`, `doc: 167`, `immutability_locks: 43`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` IOKitDebug.h, proc.h, IOServicePMPrivate.h, RootDomain.h, IOMessage.h, OSDebug.h, sysctl.h, IOPowerConnection.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `osfmk/kern/kern_stackshot.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.364 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.614 IQR)
- **Top Global Matches:** file_cluster_13: 14.364, file_cluster_8: 14.514, file_cluster_11: 14.628
- **Magnitude:** 5516.1 | **LOC:** 3272 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 317
- **Risk Profile:** Cognitive Load (78.3803%), Tech Debt (8.5059%)
**Top Internal Functions/Classes:**
  * `stackshot_trap` (Impact: 4429.9 | O(2^N) | DB: 317)
  * `safe_grab_timer_value` (Impact: 6.5 | O(N^1) | DB: 2)
  * `stackshot_init` (Impact: 2.6 | O(N^1) | DB: 2)
    * *Intent:* #if CONFIG_KDP_INTERACTIVE_DEBUGGING
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 291`, `structural_boundaries: 172`, `args: 60`, `func_start: 34`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 821`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 232`, `import: 41`
* *Defense:* `safety: 23`, `test: 6`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ipc_importance.h, stackshot.h, string.h, monotonic.h, host_statistics.h, log.h, vm_kern.h, pexpert.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `osfmk/vm/vm_page.h` (C | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.278 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.092 IQR)
- **Top Global Matches:** file_cluster_8: 12.278, file_cluster_13: 12.549, file_cluster_0: 12.613
- **Magnitude:** 5436.68 | **LOC:** 1858 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (57.2938%), Tech Debt (10.9639%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 128`, `args: 17`, `func_start: 9`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 235`, `dead_code: 3`, `fragile_debt: 2`
* *Architecture:* `api: 383`, `import: 7`
* *Defense:* `safety: 5`, `test: 5`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` OSAtomic.h, vm_prot.h, vm_object.h, boolean.h, vm_options.h, queue.h, macro_help.h, locks.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/net/pf_ioctl.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.582 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.866 IQR)
- **Top Global Matches:** file_cluster_11: 15.582, file_cluster_13: 15.59, file_cluster_0: 15.651
- **Magnitude:** 5377.94 | **LOC:** 4894 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 126
- **Risk Profile:** Cognitive Load (95.9856%), Tech Debt (14.275%)
**Top Internal Functions/Classes:**
  * `pfioctl` (Impact: 387.3 | O(N^2) | DB: 82)
  * `pfioctl_ioc_table` (Impact: 255.5 | O(N^1) | DB: 66)
  * `pfioctl_ioc_rule` (Impact: 233.4 | O(N^2) | DB: 126)
  * `pf_inet6_hook` (Impact: 167.4 | O(N^1) | DB: 1)
  * `pfioctl_ioc_trans` (Impact: 137.2 | O(N^2) | DB: 54)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1212`, `structural_boundaries: 505`, `args: 123`, `func_start: 60`, `class_start: 141`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 2413`, `dead_code: 55`, `fragile_debt: 9`, `orphaned_logic: 4`
* *Architecture:* `io: 8`, `api: 618`, `import: 40`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` param.h, endian.h, log.h, mcache.h, ip6.h, if_pflog.h, conf.h, net_api_stats.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/kern/kern_descrip.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.632 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.435 IQR)
- **Top Global Matches:** file_cluster_13: 14.632, file_cluster_8: 14.671, file_cluster_11: 14.697
- **Magnitude:** 5018.34 | **LOC:** 5790 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 485
- **Risk Profile:** Cognitive Load (99.3347%), Tech Debt (39.0407%)
**Top Internal Functions/Classes:**
  * `sys_fcntl_nocancel` (Impact: 2332.5 | O(N^3) | DB: 485)
  * `fd_rdwr` (Impact: 82.0 | O(N^1) | DB: 19)
    * *Intent:* /* * check_file_seek_range * * Description: Checks if seek offsets are in the range of 0 to LLONG_MA...
  * `dup2` (Impact: 76.5 | O(2^N) | DB: 9)
  * `dupfdopen` (Impact: 44.7 | O(N^1) | DB: 7)
  * `fdfree` (Impact: 33.9 | O(2^N) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 800`, `structural_boundaries: 330`, `args: 39`, `func_start: 61`, `class_start: 75`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1623`, `dead_code: 5`, `fragile_debt: 8`, `orphaned_logic: 23`
* *Architecture:* `io: 15`, `api: 545`, `import: 45`
* *Defense:* `safety: 7`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` param.h, stat.h, ioctl.h, ubc_internal.h, atomic_private.h, kalloc.h, cprotect.h, fsctl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libkern/libkern/c++/OSMetaClass.h` (CPP | Tier 0 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.9 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.446 IQR)
- **Top Global Matches:** file_cluster_8: 11.9, file_cluster_12: 11.925, file_cluster_7: 12.131
- **Magnitude:** 4929.72 | **LOC:** 2621 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (38.9901%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 122`, `args: 56`, `func_start: 1`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 74`
* *Architecture:* `api: 8`, `import: 7`
* *Defense:* `doc: 74`, `immutability_locks: 87`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` TargetConditionals.h, types.h, kalloc.h, ptrauth.h, zalloc.h, debug.h, OSReturn.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `osfmk/kern/kcdata.h` (C) | Magnitude: 424.08 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 267, api: 208, macros: 184, structural_boundaries: 103
- `tools/lldbmacros/turnstile.py` (PYTHON) | Magnitude: 0.16 | Delta: **0.165 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, branch: 35, structural_boundaries: 27, doc: 18
- `config/newvers.pl` (PERL) | Magnitude: 238.74 | Delta: **0.404 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 202, indent_spaces: 58, branch: 55, regex_execution: 38
- `tools/lldbmacros/bank.py` (PYTHON) | Magnitude: 0.05 | Delta: **0.509 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 21, branch: 14, doc: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `bsd/net/pf_ioctl.c` (C) | Magnitude: 5377.94 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 3048, state_mutation: 2413, pointers: 1880, branch: 1212
- `libsyscall/wrappers/libproc/proc_listpidspath.c` (C) | Magnitude: 309.86 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 229, state_mutation: 152, branch: 76, pointers: 65
- `osfmk/vm/lz4.c` (C) | Magnitude: 697.74 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 439, indent_tabs: 304, branch: 116, api: 102
- `bsd/net/if.c` (C) | Magnitude: 4383.2 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 1916, state_mutation: 1369, branch: 941, api: 685
- `tools/remote_build.sh` (SHELL) | Magnitude: 0.28 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 168, branch: 71, io: 70, reflection_metaprogramming: 69

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `EXTERNAL_HEADERS/corecrypto/cccmac.h` (C) | Magnitude: 42.02 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: pointers: 35, doc: 27, api: 26, macros: 20
- `osfmk/x86_64/boot_pt.c` (C) | Magnitude: 34.78 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 22, state_mutation: 16, reflection_metaprogramming: 14, indent_tabs: 7
- `EXTERNAL_HEADERS/corecrypto/ccn.h` (C) | Magnitude: 157.5 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 138, pointers: 92, indent_spaces: 86, api: 85
- `bsd/sys/_endian.h` (C) | Magnitude: 26.1 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 44, reflection_metaprogramming: 30, branch: 10, state_mutation: 6
- `tools/tests/personas/persona_test_run_src.sh` (SHELL) | Magnitude: 0.38 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 267, safety_bypasses: 222, state_mutation: 156, branch: 128

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/thread_call_race_71455282.c` (C) | Magnitude: 39.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 20, state_mutation: 19, concurrency: 12, import: 8
- `tools/tests/MPMMTest/KQMPMMtest.c` (C) | Magnitude: 1.03 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 572, state_mutation: 485, branch: 159, pointers: 117
- `bsd/net/dlil.c` (C) | Magnitude: 3587.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 2014, state_mutation: 1440, pointers: 1267, structural_boundaries: 731
- `bsd/net/rtsock.c` (C) | Magnitude: 1974.18 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 986, state_mutation: 966, pointers: 483, branch: 329
- `tests/bounded_array_src/ctor.default.cpp` (CPP) | Magnitude: 58.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 46, state_mutation: 45, structural_boundaries: 10, test: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `libkern/libkern/c++/intrusive_shared_ptr.h` (CPP) | Magnitude: 218.66 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 174, structural_boundaries: 169, indent_tabs: 66, generics: 36
- `iokit/IOKit/IOMessage.h` (C) | Magnitude: 15.2 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: sec_high_risk_execution: 14, macros: 8, doc: 7, generics: 2
- `libkern/os/atomic.h` (C) | Magnitude: 23.36 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 29, generics: 16, explicit_casts: 11, branch: 10
- `libkern/libkern/c++/OSSharedPtr.h` (C) | Magnitude: 43.96 | Delta: **0.154 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 50, generics: 31, state_mutation: 25, branch: 20
- `iokit/IOKitUser/IOBlockStorageDevice.h` (C) | Magnitude: 10.52 | Delta: **0.226 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: generics: 1, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tools/tests/Makefile` (MAKEFILE) | Magnitude: 0.01 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 21, branch: 14, structural_boundaries: 12, io: 7
- `tools/tests/affinity/Makefile` (MAKEFILE) | Magnitude: 0.06 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_tabs: 6, reflection_metaprogramming: 5, branch: 4
- `config/generate_linker_exports.sh` (SHELL) | Magnitude: 8.5 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 3, branch: 2, structural_boundaries: 2, args: 2
- `tools/tests/MPMMTest/Makefile` (MAKEFILE) | Magnitude: 0.01 | Delta: **0.206 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 15, branch: 8, structural_boundaries: 7, comprehensions: 3
- `makedefs/MakeInc.def` (MAKEFILE) | Magnitude: 120.64 | Delta: **0.322 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 306, indent_tabs: 175, safety_bypasses: 147, branch: 135

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `osfmk/man/thread_assign_default.html` (HTML) | Magnitude: 15.8 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 16, ui_framework: 11, io: 10, args: 2
- `osfmk/man/thread_depress_abort.html` (HTML) | Magnitude: 15.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 14, ui_framework: 8, io: 4, args: 2
- `osfmk/man/MO_SY_completed.html` (HTML) | Magnitude: 16.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 20, ui_framework: 14, io: 6, args: 3
- `osfmk/man/thread_get_assignment.html` (HTML) | Magnitude: 15.8 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 17, ui_framework: 11, io: 10, args: 5
- `osfmk/man/thread_suspend.html` (HTML) | Magnitude: 16.14 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 18, io: 16, ui_framework: 16, sec_high_risk_execution: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `osfmk/x86_64/machine_remote_time.c` (C) | Magnitude: 43.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 22, indent_tabs: 21, api: 6, concurrency: 6
- `tests/exec-race-58566604.c` (C) | Magnitude: 172.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 111, indent_tabs: 89, branch: 18, api: 17
- `bsd/security/audit/audit_bsd.c` (C) | Magnitude: 462.42 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 245, pointers: 216, state_mutation: 197, structural_boundaries: 85
- `tools/tests/execperf/run.c` (C) | Magnitude: 0.11 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 52, state_mutation: 42, branch: 16, api: 15
- `tests/kqueue_close.c` (C) | Magnitude: 68.46 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 33, state_mutation: 30, concurrency: 12, events: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `bsd/net/kpi_interface.h` (C) | Magnitude: 381.24 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 278, indent_tabs: 231, doc: 158, structural_boundaries: 103

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tools/lldbmacros/core/kernelcore.py` (PYTHON) | Magnitude: 1.29 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 403, encapsulation: 162, state_mutation: 137, structural_boundaries: 127
- `tools/lldbmacros/kevent.py` (PYTHON) | Magnitude: 0.19 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 165, branch: 60, structural_boundaries: 50, doc: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `bsd/crypto/entropy/Makefile` (MAKEFILE) | Magnitude: 0.19 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 4, import: 4, structural_boundaries: 3
- `iokit/Makefile` (MAKEFILE) | Magnitude: 19.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 4, import: 4, structural_boundaries: 3, sec_high_risk_execution: 1
- `libsyscall/wrappers/cancelable/fcntl-cancel.c` (C) | Magnitude: 12.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 3, import: 2, branch: 1, ownership: 1
- `osfmk/arm64/machine_task.c` (C) | Magnitude: 96.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 73, api: 34, state_mutation: 27, branch: 24
- `security/mac_iokit.c` (C) | Magnitude: 27.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 18, indent_tabs: 18, import: 11, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `osfmk/arm/setjmp.h` (C) | Magnitude: 15.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ownership: 3, sec_high_risk_execution: 3, structural_boundaries: 2, api: 2
- `osfmk/i386/setjmp.h` (C) | Magnitude: 15.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ownership: 3, sec_high_risk_execution: 3, structural_boundaries: 2, api: 2
- `bsd/netinet/in_var.h` (C) | Magnitude: 154.72 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 124, api: 117, indent_tabs: 79, class_start: 43
- `libsyscall/wrappers/rename.c` (C) | Magnitude: 12.12 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 5, indent_tabs: 5, pointers: 4, immutability_locks: 4
- `osfmk/mach_debug/page_info.h` (C) | Magnitude: 13.6 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ownership: 3, sec_high_risk_execution: 3, macros: 2, structural_boundaries: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `security/mac_internal.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9013%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `EXTERNAL_HEADERS/stdint.h` -> **Severity: 4174.411** (Blast Radius: 42.161 * Doc Risk: 99.0112%)
- `bsd/sys/unistd.h` -> **Severity: 974.299** (Blast Radius: 13.983 * Doc Risk: 69.6774%)
- `bsd/sys/stdio.h` -> **Severity: 604.093** (Blast Radius: 10.554 * Doc Risk: 57.2383%)
- `EXTERNAL_HEADERS/stdatomic.h` -> **Severity: 480.999** (Blast Radius: 4.81 * Doc Risk: 99.9998%)
- `EXTERNAL_HEADERS/stddef.h` -> **Severity: 456.406** (Blast Radius: 6.229 * Doc Risk: 73.2711%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
