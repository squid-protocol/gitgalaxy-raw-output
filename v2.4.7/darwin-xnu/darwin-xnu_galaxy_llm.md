# ARCHITECTURAL_BRIEF: darwin-xnu
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/OS/darwin-xnu` |
| **Timestamp** | `2026-08-07T03:30:23.330029+00:00` |
| **Scan Duration** | `28.59s` |
| **Git Branch** | `main` |
| **Git Commit** | `2ff845c2e033bd0ff64b5b6aa6063a1f8f65aa32` |
| **Git Remote** | `https://github.com/apple/darwin-xnu.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3296 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
| Cognitive Load Exposure | 0.0 | 100.0 | 27.7 | 9.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 43.8 | 56.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.7 | 2.3 | 2.3 |
| API Exposure | 0.0 | 19.3 | 7.3 | 8.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 35.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 44.8 | 21.7 | 0.0 |
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

- `soconnectxlocked` (@ `bsd/kern/uipc_socket.c`) -> Impact: **2853.8** | LOC: 2416
- `pf_test_rule` (@ `bsd/net/pf.c`) -> Impact: **2596.8** | LOC: 1984
- `nfs_advlock_setlock` (@ `bsd/nfs/nfs4_vnops.c`) -> Impact: **1778.3** | LOC: 1919
- `key_gather_mbuf` (@ `bsd/netkey/key.c`) -> Impact: **1555.9** | LOC: 2263
- `pf_src_connlimit` (@ `bsd/net/pf.c`) -> Impact: **1431.7** | LOC: 2113
- `IOPMrootDomain::tellChangeUp` (@ `iokit/Kernel/IOPMrootDomain.cpp`) -> Impact: **1323.3** | LOC: 2118
- `mount_common` (@ `bsd/vfs/vfs_syscalls.c`) -> Impact: **1322.0** | LOC: 1764
- `pf_route` (@ `bsd/net/pf.c`) -> Impact: **1288.1** | LOC: 1611
- `key_ismyaddr6` (@ `bsd/netkey/key.c`) -> Impact: **1232.8** | LOC: 2162
- `sys_fcntl_nocancel` (@ `bsd/kern/kern_descrip.c`) -> Impact: **1222.2** | LOC: 2240

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `bsd/kern` | 112 | 106130.76 | 73.6% | 43.48% |
| `bsd/net` | 149 | 88211.82 | 36.86% | 21.69% |
| `osfmk/kern` | 202 | 60901.42 | 39.57% | 29.95% |
| `iokit/Kernel` | 72 | 60639.82 | 64.3% | 78.22% |
| `bsd/netinet` | 95 | 52826.72 | 42.64% | 18.19% |
| `osfmk/vm` | 57 | 44827.44 | 41.76% | 19.7% |
| `bsd/nfs` | 31 | 40978.52 | 53.0% | 14.65% |
| `bsd/netinet6` | 66 | 36485.46 | 47.58% | 29.66% |
| `tests` | 253 | 36067.54 | 25.42% | 0.0% |
| `bsd/vfs` | 26 | 30985.42 | 71.22% | 42.1% |

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
- `iokit/Kernel/IOService.cpp` -> **115** Orphaned Functions | **19** Duplicates
- `iokit/Kernel/IOUserServer.cpp` -> **124** Orphaned Functions | **8** Duplicates
- `iokit/Kernel/IOServicePM.cpp` -> **112** Orphaned Functions | **2** Duplicates
- `iokit/Kernel/IOPMrootDomain.cpp` -> **98** Orphaned Functions | **10** Duplicates
- `tests/vm/vm_allocation.c` -> **103** Orphaned Functions | **0** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `25089` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `osfmk/kern/kern_monotonic.c` (C) -> Cumulative Risk: **768.81**
- **Archetype:** `file_cluster_4` (Distance: 13.159 IQR)
- **Magnitude:** 435.34 | **LOC:** 579 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.7546%), Tech Debt (98.3356%)
- **Heaviest Functions:** `mt_mtc_update_fixed_counts` (Impact: 11.3), `mt_fixed_thread_counts` (Impact: 11.1), `mt_update_thread` (Impact: 10.8)

### 2. `osfmk/kern/sched_amp_common.c` (C) -> Cumulative Risk: **719.42**
- **Archetype:** `file_cluster_13` (Distance: 13.342 IQR)
- **Magnitude:** 577.48 | **LOC:** 607 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.0255%), Safety Score (93.4274%)
- **Heaviest Functions:** `should_spill_to_ecores` (Impact: 117.2), `pset_signal_spill` (Impact: 17.9), `sched_amp_ipi_policy` (Impact: 17.6)

### 3. `osfmk/arm/commpage/commpage.c` (C) -> Cumulative Risk: **703.36**
- **Archetype:** `file_cluster_13` (Distance: 12.923 IQR)
- **Magnitude:** 264.68 | **LOC:** 643 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (94.8747%), Safety Score (90.9907%)
- **Heaviest Functions:** `commpage_populate` (Impact: 22.9), `commpage_update_dof` (Impact: 7.4), `commpage_is_in_pfz64` (Impact: 6.8)

### 4. `osfmk/i386/commpage/commpage.c` (C) -> Cumulative Risk: **699.46**
- **Archetype:** `file_cluster_4` (Distance: 13.495 IQR)
- **Magnitude:** 520.38 | **LOC:** 1019 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9323%), Safety Score (97.6078%)
- **Heaviest Functions:** `commpage_init_cpu_capabilities` (Impact: 53.5), `commpage_update_dof` (Impact: 13.2), `commpage_set_memory_pressure` (Impact: 8.4)

### 5. `bsd/dev/arm/dtrace_isa.c` (C) -> Cumulative Risk: **690.47**
- **Archetype:** `file_cluster_13` (Distance: 13.776 IQR)
- **Magnitude:** 596.54 | **LOC:** 647 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9411%), Safety Score (98.6252%)
- **Heaviest Functions:** `dtrace_getpcstack` (Impact: 90.5), `dtrace_arm_condition_true` (Impact: 74.2), `dtrace_getupcstack` (Impact: 31.2)

### 6. `bsd/dev/i386/dtrace_isa.c` (C) -> Cumulative Risk: **690.22**
- **Archetype:** `file_cluster_13` (Distance: 13.455 IQR)
- **Magnitude:** 613.06 | **LOC:** 892 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.7249%), Safety Score (97.7037%)
- **Heaviest Functions:** `dtrace_getreg` (Impact: 64.8), `dtrace_getpcstack` (Impact: 40.1), `dtrace_getustack_common` (Impact: 25.9)

### 7. `osfmk/arm/machine_routines_common.c` (C) -> Cumulative Risk: **689.42**
- **Archetype:** `file_cluster_8` (Distance: 13.092 IQR)
- **Magnitude:** 875.18 | **LOC:** 1091 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.4671%), Cognitive Load (90.6692%)
- **Heaviest Functions:** `sched_perfcontrol_register_callbacks` (Impact: 47.4), `ml_set_interrupts_enabled` (Impact: 16.0), `machine_thread_group_blocked` (Impact: 13.1)

### 8. `osfmk/kern/locks.c` (C) -> Cumulative Risk: **688.03**
- **Archetype:** `file_cluster_8` (Distance: 12.976 IQR)
- **Magnitude:** 1546.78 | **LOC:** 3265 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9981%), Tech Debt (96.6275%), Documentation (95.829%)
- **Heaviest Functions:** `hw_lock_trylock_contended` (Impact: 426.1), `lck_mtx_sleep` (Impact: 16.5), `gate_handoff` (Impact: 15.8)

### 9. `bsd/dev/arm64/dtrace_isa.c` (C) -> Cumulative Risk: **682.08**
- **Archetype:** `file_cluster_13` (Distance: 13.537 IQR)
- **Magnitude:** 470.58 | **LOC:** 706 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8879%), Safety Score (97.6339%)
- **Heaviest Functions:** `dtrace_getpcstack` (Impact: 55.2), `dtrace_getupcstack` (Impact: 33.5), `dtrace_getustack_common` (Impact: 11.8)

### 10. `bsd/vfs/kpi_vfs.c` (C) -> Cumulative Risk: **680.51**
- **Archetype:** `file_cluster_13` (Distance: 14.205 IQR)
- **Magnitude:** 4319.22 | **LOC:** 6221 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.427%), Tech Debt (98.4688%)
- **Heaviest Functions:** `vnode_lookup_continue_needed` (Impact: 721.2), `vfs_context_cwd` (Impact: 610.4), `vnode_setattr` (Impact: 567.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `EXTERNAL_HEADERS/AvailabilityInternal.h` (C | Tier 4 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.01 IQR)
- **Top Global Matches:** file_cluster_8: 15.01, file_cluster_0: 15.188, file_cluster_7: 15.493
- **Magnitude:** 14638.52 | **LOC:** 23427 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
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

### `bsd/net/pf.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.224 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.839 IQR)
- **Top Global Matches:** file_cluster_8: 15.224, file_cluster_13: 15.384, file_cluster_11: 15.438
- **Magnitude:** 14381.06 | **LOC:** 10804 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.1441%), Tech Debt (17.5313%)
**Top Internal Functions/Classes:**
  * `pf_test_rule` (Impact: 2596.8)
  * `pf_src_connlimit` (Impact: 1431.7)
  * `pf_route` (Impact: 1288.1)
  * `pf_test6` (Impact: 534.8)
  * `pf_test` (Impact: 478.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2223`, `structural_boundaries: 990`, `args: 119`, `func_start: 93`, `class_start: 299`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4260`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 10`, `orphaned_logic: 24`
* *Architecture:* `io: 1`, `api: 1084`, `import: 49`
* *Defense:* `safety: 4`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dlil.h, tcp_var.h, ip6.h, if_pfsync.h, nd6.h, socketvar.h, if.h, icmp_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `iokit/Kernel/IOPMrootDomain.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.279 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.818 IQR)
- **Top Global Matches:** file_cluster_8: 15.279, file_cluster_13: 15.418, file_cluster_11: 15.505
- **Magnitude:** 10970.18 | **LOC:** 12586 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.3827%), Tech Debt (80.8462%)
**Top Internal Functions/Classes:**
  * `IOPMrootDomain::tellChangeUp` (Impact: 1323.3)
  * `IOPMrootDomain::powerChangeDone` (Impact: 1174.4)
  * `IOPMrootDomain::start` (Impact: 1006.5)
  * `PMAssertionsTracker::reportCPUBitAccount` (Impact: 512.0)
    * *Intent:* *hibMode |= (kIOHibernateModeOn | kIOHibernateModeSleep);
  * `IOPMrootDomain::informCPUStateChange` (Impact: 456.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1200`, `structural_boundaries: 410`, `args: 279`, `func_start: 133`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 22`, `state_mutation: 4410`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 10`, `orphaned_logic: 98`
* *Architecture:* `api: 4`, `import: 47`
* *Defense:* `safety: 9`, `doc: 81`, `test: 12`, `sync_locks: 1`, `immutability_locks: 132`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` vnode_internal.h, IOKitDebug.h, sysctl.h, cpp_util.h, IOPMrootDomainInternal.h, RootDomainUserClient.h, IOPMPowerStateQueue.h, IOUserServer.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/nfs/nfs4_vnops.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.919 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.678 IQR)
- **Top Global Matches:** file_cluster_8: 14.919, file_cluster_13: 14.976, file_cluster_11: 15.028
- **Magnitude:** 10292.68 | **LOC:** 9101 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.5768%), Tech Debt (26.4085%)
**Top Internal Functions/Classes:**
  * `nfs_advlock_setlock` (Impact: 1778.3)
  * `nfs4_open_rpc_internal` (Impact: 1111.2)
  * `nfs4_rename_rpc` (Impact: 1105.1)
  * `nfs4_access_rpc` (Impact: 1095.2)
    * *Intent:* #include <sys/conf.h> #include <sys/vnode_internal.h> #include <sys/dirent.h> #include <sys/fcntl.h>...
  * `nfs4_setattr_rpc` (Impact: 417.0)
    * *Intent:* /* * Loop around doing readdir(plus) RPCs of size nm_readdirsize until * the buffer is full (or we h...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1118`, `structural_boundaries: 309`, `args: 28`, `func_start: 49`, `class_start: 146`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2559`, `dead_code: 9`, `fragile_debt: 11`, `orphaned_logic: 21`
* *Architecture:* `io: 31`, `api: 594`, `import: 43`
* *Defense:* `safety: 8`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vnode_internal.h, nfsm_subs.h, malloc.h, xdr_subs.h, if.h, vfs_support.h, in.h, nfsproto.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/netkey/key.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.519 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.79 IQR)
- **Top Global Matches:** file_cluster_8: 14.519, file_cluster_13: 14.629, file_cluster_11: 14.688
- **Magnitude:** 10108.56 | **LOC:** 10513 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.9374%), Tech Debt (41.675%)
**Top Internal Functions/Classes:**
  * `key_gather_mbuf` (Impact: 1555.9)
  * `key_ismyaddr6` (Impact: 1232.8)
  * `key_alloc_outbound_sav_for_interface` (Impact: 452.0)
  * `key_setdumpsa` (Impact: 182.6)
  * `key_delsav` (Impact: 179.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1428`, `structural_boundaries: 1163`, `args: 134`, `func_start: 81`, `class_start: 248`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 2947`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 43`, `orphaned_logic: 11`
* *Architecture:* `io: 42`, `api: 940`, `import: 44`
* *Defense:* `safety: 10`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ip6.h, sysctl.h, malloc.h, socketvar.h, if.h, ah.h, types.h, esp6.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `osfmk/vm/vm_map.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.781 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.139 IQR)
- **Top Global Matches:** file_cluster_8: 14.781, file_cluster_13: 14.941, file_cluster_11: 14.983
- **Magnitude:** 8835.5 | **LOC:** 21972 | **CtrlFlow:** 81.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.89%), Tech Debt (27.1951%)
**Top Internal Functions/Classes:**
  * `vm_map_remap` (Impact: 581.6)
    * *Intent:* /* We unwired what the caller asked for: zero pages */
  * `vm_map_page_range_info_internal` (Impact: 456.7)
    * *Intent:* /* * We might have fragmented the address space when we wired this * range of addresses. Attempt to ...
  * `vm_map_msync` (Impact: 363.4)
  * `vm_map_enter_mem_object_control` (Impact: 263.8)
  * `vm_map_enter_cpm` (Impact: 194.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1563`, `structural_boundaries: 360`, `args: 20`, `func_start: 111`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3948`, `dead_code: 12`, `planned_debt: 3`, `fragile_debt: 15`, `orphaned_logic: 50`
* *Architecture:* `io: 2`, `api: 1433`, `import: 44`
* *Defense:* `safety: 170`, `test: 169`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vm_object.h, vm_init.h, cpm.h, vm_map_store.h, ipc_port.h, vm_purgeable_internal.h, assert.h, exc_guard.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/dev/dtrace/dtrace.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.137 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.532 IQR)
- **Top Global Matches:** file_cluster_8: 15.137, file_cluster_13: 15.297, file_cluster_11: 15.319
- **Magnitude:** 7674.38 | **LOC:** 19416 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.7375%), Tech Debt (19.349%)
**Top Internal Functions/Classes:**
  * `dtrace_canload_remains` (Impact: 275.1)
    * *Intent:* #define DTRACE_HASHPREV(hash, elm) \
  * `dtrace_speculation_buffer` (Impact: 261.8)
    * *Intent:* /* * Convenience routine to check to see if the address is within a memory * region in which a load ...
  * `dtrace_state_destroy` (Impact: 167.4)
  * `dtrace_dif_varstr` (Impact: 138.6)
    * *Intent:* /*
  * `dtrace_dif_subr` (Impact: 106.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1882`, `structural_boundaries: 530`, `args: 44`, `func_start: 144`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 4796`, `planned_debt: 4`, `fragile_debt: 8`, `orphaned_logic: 28`
* *Architecture:* `io: 1`, `api: 902`, `import: 34`
* *Defense:* `safety: 78`, `doc: 3`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` kernel_types.h, malloc.h, dtrace_xoroshiro128_plus.h, cpu_data.h, types.h, dtrace_impl.h, in.h, devfs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/kern/uipc_socket.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.886 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.942 IQR)
- **Top Global Matches:** file_cluster_8: 14.886, file_cluster_13: 14.899, file_cluster_11: 15.011
- **Magnitude:** 7297.78 | **LOC:** 8016 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.1509%), Tech Debt (22.6115%)
**Top Internal Functions/Classes:**
  * `soconnectxlocked` (Impact: 2853.8)
  * `sosendcheck` (Impact: 717.2)
  * `sosend_list` (Impact: 190.5)
  * `filt_sockev_common` (Impact: 80.2)
    * *Intent:* /*
  * `soreceive_addr` (Impact: 79.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 976`, `structural_boundaries: 403`, `args: 114`, `func_start: 69`, `class_start: 74`
* *Risk/State:* `state_mutation: 2044`, `planned_debt: 2`, `orphaned_logic: 26`
* *Architecture:* `io: 96`, `api: 460`, `import: 58`
* *Defense:* `safety: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` policy_internal.h, tcp_var.h, sysctl.h, malloc.h, ip6.h, priv.h, assert.h, socketvar.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `iokit/Kernel/IOService.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.814 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.831 IQR)
- **Top Global Matches:** file_cluster_8: 14.814, file_cluster_13: 14.996, file_cluster_11: 15.112
- **Magnitude:** 7108.14 | **LOC:** 8388 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.1572%), Tech Debt (97.2935%)
**Top Internal Functions/Classes:**
  * `IOService::lockForArbitration` (Impact: 850.4)
  * `IOService::probeCandidates` (Impact: 617.6)
  * `IOService::newUserClient` (Impact: 483.0)
  * `IOService::errnoFromReturn` (Impact: 123.2)
  * `IOService::updateConsoleUsers` (Impact: 103.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 818`, `structural_boundaries: 369`, `args: 272`, `func_start: 145`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 87`, `high_risk_execution: 1`, `state_mutation: 3106`, `dead_code: 2`, `planned_debt: 3`, `duplicate_logic: 19`, `orphaned_logic: 115`
* *Architecture:* `import: 39`
* *Defense:* `safety: 23`, `doc: 2`, `sync_locks: 2`, `immutability_locks: 148`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` string.h, assert.h, system.h, IOUserServer.h, sync_policy.h, IOMessage.h, IOService.h, IOKitKeysPrivate.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/kern/kern_event.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.783 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.629 IQR)
- **Top Global Matches:** file_cluster_13: 14.783, file_cluster_8: 14.811, file_cluster_11: 14.956
- **Magnitude:** 7080.02 | **LOC:** 9153 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.9595%), Tech Debt (21.8305%)
**Top Internal Functions/Classes:**
  * `filt_wlupdate` (Impact: 1201.6)
  * `kqueue_workloop_ctl_internal` (Impact: 964.9)
  * `kevent_internal` (Impact: 287.7)
  * `kqueue_destroy` (Impact: 177.3)
  * `knote_adjust_qos` (Impact: 130.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 761`, `structural_boundaries: 697`, `args: 135`, `func_start: 143`, `class_start: 114`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2050`, `dead_code: 2`, `orphaned_logic: 42`
* *Architecture:* `io: 5`, `api: 580`, `import: 54`
* *Defense:* `safety: 85`, `doc: 21`, `test: 74`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` waitq.h, vnode_internal.h, string.h, policy_internal.h, atomic.h, malloc.h, sysctl.h, kern_memorystatus.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/netinet/flow_divert.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.619 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.272 IQR)
- **Top Global Matches:** file_cluster_8: 14.619, file_cluster_13: 14.658, file_cluster_11: 14.721
- **Magnitude:** 6648.52 | **LOC:** 4394 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.5719%), Tech Debt (12.8505%)
**Top Internal Functions/Classes:**
  * `flow_divert_trie_insert` (Impact: 1032.4)
  * `flow_divert_send_app_data` (Impact: 1001.7)
  * `flow_divert_handle_connect_result` (Impact: 145.7)
  * `flow_divert_create_connect_packet` (Impact: 144.7)
  * `flow_divert_connect_out_internal` (Impact: 131.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 920`, `structural_boundaries: 426`, `args: 61`, `func_start: 77`, `class_start: 85`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2117`, `dead_code: 1`, `fragile_debt: 4`, `orphaned_logic: 6`
* *Architecture:* `io: 72`, `api: 495`, `import: 42`
* *Defense:* `safety: 27`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` string.h, tcp_var.h, malloc.h, socketvar.h, necp.h, types.h, tcp.h, ubc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `osfmk/arm/pmap.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.161 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.436 IQR)
- **Top Global Matches:** file_cluster_8: 14.161, file_cluster_13: 14.336, file_cluster_7: 14.444
- **Magnitude:** 6629.6 | **LOC:** 15781 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.7126%), Tech Debt (10.4299%)
**Top Internal Functions/Classes:**
  * `pmap_pages_reclaim` (Impact: 734.1)
  * `pmap_remove_range_options` (Impact: 549.7)
  * `pmap_change_wiring_internal` (Impact: 210.8)
  * `pmap_page_protect_options_with_flush_ran` (Impact: 134.7)
  * `pmap_protect_options_internal` (Impact: 87.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 907`, `structural_boundaries: 532`, `args: 74`, `func_start: 188`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 2797`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 19`, `api: 1103`, `import: 53`
* *Defense:* `safety: 63`, `doc: 22`, `test: 90`, `immutability_locks: 184`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` vm_object.h, string.h, vm_param.h, overflow.h, cpm.h, atomic.h, amcc_rorgn.h, stdint.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/nfs/nfs_vfsops.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.534 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.579 IQR)
- **Top Global Matches:** file_cluster_8: 14.534, file_cluster_13: 14.601, file_cluster_11: 14.718
- **Magnitude:** 6238.12 | **LOC:** 6775 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.0777%), Tech Debt (14.3018%)
**Top Internal Functions/Classes:**
  * `mountnfs` (Impact: 993.3)
    * *Intent:* /* fs location */ xb_add_32(error, &xb, 1); /* fs location count */ xb_add_32(error, &xb, 1); /* ser...
  * `nfs4_mount` (Impact: 937.6)
  * `nfs_convert_old_nfs_args` (Impact: 920.9)
  * `nfs_mountinfo_assemble` (Impact: 328.8)
  * `nfs_mount_diskless` (Impact: 106.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 852`, `structural_boundaries: 243`, `args: 36`, `func_start: 30`, `class_start: 56`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1956`, `dead_code: 7`, `fragile_debt: 5`, `orphaned_logic: 7`
* *Architecture:* `io: 5`, `api: 444`, `import: 40`
* *Defense:* `safety: 11`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vnode_internal.h, nfsm_subs.h, sysctl.h, malloc.h, xdr_subs.h, priv.h, socketvar.h, if.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/net/if_bridge.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.473 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.016 IQR)
- **Top Global Matches:** file_cluster_8: 14.473, file_cluster_11: 14.739, file_cluster_0: 14.771
- **Magnitude:** 6142.9 | **LOC:** 8838 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.5617%), Tech Debt (34.3349%)
**Top Internal Functions/Classes:**
  * `bridge_input` (Impact: 971.5)
  * `bridge_mac_nat_udp_output` (Impact: 588.7)
  * `bridge_pf` (Impact: 140.7)
    * *Intent:* /*
  * `bridge_host_filter` (Impact: 123.4)
  * `bridge_broadcast` (Impact: 117.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 910`, `structural_boundaries: 676`, `args: 90`, `func_start: 99`, `class_start: 179`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 1907`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 14`, `orphaned_logic: 22`
* *Architecture:* `api: 597`
* *Defense:* `safety: 19`, `test: 4`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ip6.h, sysctl.h, malloc.h, dlil.h, nd6.h, if.h, tcp.h, mcache.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `iokit/Kernel/IOServicePM.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.069 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.856 IQR)
- **Top Global Matches:** file_cluster_8: 15.069, file_cluster_13: 15.208, file_cluster_7: 15.273
- **Magnitude:** 6064.54 | **LOC:** 9056 | **CtrlFlow:** 75.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.2708%), Tech Debt (91.0541%)
**Top Internal Functions/Classes:**
  * `IOService::ackTimerTick` (Impact: 1050.3)
    * *Intent:* // Invalidate cached tickle power state when desires change, and not // due to a tickle request. In ...
  * `IOService::actionPMWorkQueueInvoke` (Impact: 177.6)
  * `IOService::executePMRequest` (Impact: 97.0)
  * `IOService::actionPMReplyQueue` (Impact: 79.3)
    * *Intent:* // Not root domain and advisory tickle target. // Re-adjust power after power tree sync at the 'did'...
  * `IOService::addPowerChild` (Impact: 77.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 921`, `structural_boundaries: 305`, `args: 182`, `func_start: 118`
* *Risk/State:* `safety_bypasses: 60`, `high_risk_execution: 2`, `state_mutation: 2866`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 112`
* *Architecture:* `import: 27`
* *Defense:* `safety: 73`, `doc: 167`, `immutability_locks: 43`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` IOKitDebug.h, sysctl.h, assert.h, IOUserServer.h, IOMessage.h, IOService.h, IOEventSource.h, IODeviceTreeSupport.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libkern/c++/OSKext.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.807 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.822 IQR)
- **Top Global Matches:** file_cluster_8: 14.807, file_cluster_13: 14.926, file_cluster_7: 15.05
- **Magnitude:** 5818.02 | **LOC:** 15434 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.0308%), Tech Debt (52.1013%)
**Top Internal Functions/Classes:**
  * `OSKext_protect` (Impact: 851.7)
    * *Intent:* /* Exclude builtin and codeless kexts */
  * `OSKext::removeKextBootstrap` (Impact: 445.6)
  * `OSKext::copyPersonalitiesArray` (Impact: 415.8)
  * `compactIdentifier` (Impact: 267.0)
  * `OSKextSystemSleepOrWake` (Impact: 120.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 816`, `structural_boundaries: 319`, `args: 283`, `func_start: 106`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 59`, `high_risk_execution: 7`, `state_mutation: 2713`, `dead_code: 4`, `fragile_debt: 4`, `duplicate_logic: 6`, `orphaned_logic: 42`
* *Architecture:* `import: 44`
* *Defense:* `safety: 24`, `doc: 86`, `immutability_locks: 65`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` OSKextLibPrivate.h, string.h, tracepoint_private.h, sysctl.h, cpp_util.h, firehose_buffer_private.h, mac_framework.h, host_special_ports.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `osfmk/vm/vm_page.h` (C | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.278 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.092 IQR)
- **Top Global Matches:** file_cluster_8: 12.278, file_cluster_13: 12.549, file_cluster_0: 12.613
- **Magnitude:** 5436.68 | **LOC:** 1858 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.2938%), Tech Debt (10.9639%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 128`, `args: 17`, `func_start: 9`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 235`, `dead_code: 3`, `fragile_debt: 2`
* *Architecture:* `api: 383`, `import: 7`
* *Defense:* `safety: 5`, `test: 5`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vm_prot.h, vm_param.h, vm_object.h, debug.h, macro_help.h, memory_object_types.h, boolean.h, vm_options.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `iokit/Kernel/IOUserServer.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.812 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.657 IQR)
- **Top Global Matches:** file_cluster_8: 14.812, file_cluster_13: 14.998, file_cluster_11: 15.156
- **Magnitude:** 5198.76 | **LOC:** 4698 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.9985%), Tech Debt (97.7884%)
**Top Internal Functions/Classes:**
  * `IOUserServer::target` (Impact: 588.3)
  * `IOUserServer::objectInstantiate` (Impact: 111.0)
  * `IOUserServer::copyOutObjects` (Impact: 89.6)
  * `IODMACommand::PerformOperation_Impl` (Impact: 80.6)
  * `IOUserServer::copyInObjects` (Impact: 70.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 650`, `structural_boundaries: 344`, `args: 244`, `func_start: 135`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 5`, `state_mutation: 2767`, `dead_code: 2`, `fragile_debt: 2`, `duplicate_logic: 8`, `orphaned_logic: 124`
* *Architecture:* `api: 2`, `import: 38`
* *Defense:* `safety: 50`, `sync_locks: 36`, `immutability_locks: 49`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` IODispatchSource.h, IORPC.h, IODataQueueDispatchSource.h, IODataQueueDispatchSourceShared.h, system.h, IOInterruptDispatchSource.h, IOMemoryMap.h, IORegistryEntry.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libkern/libkern/c++/OSMetaClass.h` (CPP | Tier 0 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.918 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.445 IQR)
- **Top Global Matches:** file_cluster_8: 11.918, file_cluster_12: 11.942, file_cluster_7: 12.148
- **Magnitude:** 5127.46 | **LOC:** 2621 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.9901%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 122`, `args: 61`, `func_start: 1`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 74`
* *Architecture:* `api: 8`, `import: 7`
* *Defense:* `doc: 74`, `immutability_locks: 87`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` kalloc.h, OSReturn.h, zalloc.h, TargetConditionals.h, types.h, debug.h, ptrauth.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/kern/kern_exec.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.675 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.728 IQR)
- **Top Global Matches:** file_cluster_8: 14.675, file_cluster_13: 14.703, file_cluster_11: 14.849
- **Magnitude:** 5082.22 | **LOC:** 7292 | **CtrlFlow:** 82.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.1218%), Tech Debt (12.1074%)
**Top Internal Functions/Classes:**
  * `exec_handle_port_actions` (Impact: 861.1)
  * `exec_add_apple_strings` (Impact: 140.4)
  * `exec_handle_sugid` (Impact: 126.1)
    * *Intent:* /* * If we have a spawn attr, and it contains signal related flags, * the we need to process them in...
  * `exec_extract_strings` (Impact: 122.1)
  * `__mac_execve` (Impact: 94.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1114`, `structural_boundaries: 229`, `args: 42`, `func_start: 39`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 8`, `state_mutation: 2468`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 6`, `orphaned_logic: 3`
* *Architecture:* `io: 8`, `api: 535`, `concurrency: 6`, `import: 92`
* *Defense:* `safety: 50`, `test: 21`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` vnode_internal.h, assert.h, audit.h, sysproto.h, arcade.h, dtrace_ptss.h, cdefs.h, vm_param.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/net/dlil.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.122 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.047 IQR)
- **Top Global Matches:** file_cluster_13: 14.122, file_cluster_8: 14.125, file_cluster_11: 14.411
- **Magnitude:** 5011.0 | **LOC:** 10702 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.0753%), Tech Debt (52.641%)
**Top Internal Functions/Classes:**
  * `dlil_output` (Impact: 679.1)
  * `dlil_event_internal` (Impact: 620.0)
  * `ifnet_ioctl` (Impact: 569.1)
  * `ifnet_detach_final` (Impact: 95.0)
  * `dlil_rxpoll_update_params` (Impact: 62.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 540`, `structural_boundaries: 731`, `args: 181`, `func_start: 122`, `class_start: 119`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1438`, `dead_code: 4`, `fragile_debt: 2`, `orphaned_logic: 54`
* *Architecture:* `io: 3`, `api: 552`, `import: 83`
* *Defense:* `safety: 8`, `immutability_locks: 92`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` if_arp.h, dlil.h, assert.h, in.h, in_tclass.h, kauth.h, kpi_protocol.h, locks.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/vfs/vfs_syscalls.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.497 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.423 IQR)
- **Top Global Matches:** file_cluster_13: 14.497, file_cluster_8: 14.511, file_cluster_11: 14.62
- **Magnitude:** 4979.62 | **LOC:** 13443 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.8093%), Tech Debt (45.7969%)
**Top Internal Functions/Classes:**
  * `mount_common` (Impact: 1322.0)
  * `fsetxattr` (Impact: 203.7)
  * `dounmount_submounts` (Impact: 111.6)
  * `rmdirat_internal` (Impact: 96.2)
  * `clonefile_internal` (Impact: 90.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 816`, `structural_boundaries: 340`, `args: 27`, `func_start: 59`, `class_start: 79`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1766`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 11`, `orphaned_logic: 30`
* *Architecture:* `io: 3`, `api: 669`, `concurrency: 6`, `import: 59`
* *Defense:* `safety: 9`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` vnode_internal.h, disk.h, atomic_private.h, sysctl.h, priv.h, mac_framework.h, audit.h, sysproto.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/net/pf_ioctl.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.544 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.859 IQR)
- **Top Global Matches:** file_cluster_11: 15.544, file_cluster_13: 15.552, file_cluster_0: 15.613
- **Magnitude:** 4837.84 | **LOC:** 4894 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.9856%), Tech Debt (14.275%)
**Top Internal Functions/Classes:**
  * `pfioctl` (Impact: 267.3)
  * `pf_inet6_hook` (Impact: 167.4)
  * `pfioctl_ioc_rule` (Impact: 162.9)
  * `pfioctl_ioc_table` (Impact: 155.2)
  * `pfioctl_ioc_trans` (Impact: 95.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1212`, `structural_boundaries: 505`, `args: 68`, `func_start: 60`, `class_start: 140`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 2413`, `dead_code: 55`, `fragile_debt: 9`, `orphaned_logic: 4`
* *Architecture:* `io: 8`, `api: 618`, `import: 40`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dlil.h, ip6.h, malloc.h, if_pfsync.h, socketvar.h, if.h, mcache.h, queue.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/kern/uipc_mbuf.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.55 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.795 IQR)
- **Top Global Matches:** file_cluster_8: 14.55, file_cluster_13: 14.663, file_cluster_11: 14.76
- **Magnitude:** 4610.24 | **LOC:** 8920 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.0076%), Tech Debt (32.9271%)
**Top Internal Functions/Classes:**
  * `m_allocpacket_internal` (Impact: 581.6)
    * *Intent:* /*
  * `m_copyback0` (Impact: 81.2)
    * *Intent:* /* * If auditing is enabled, construct the shadow mbuf * in the audit structure instead of in the ac...
  * `cslab_free` (Impact: 56.1)
  * `m_split0` (Impact: 55.2)
    * *Intent:* /*
  * `m_pullup` (Impact: 48.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 709`, `structural_boundaries: 465`, `args: 99`, `func_start: 81`, `class_start: 83`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 2326`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`, `orphaned_logic: 34`
* *Architecture:* `io: 5`, `api: 467`, `import: 32`
* *Defense:* `safety: 20`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sysctl.h, malloc.h, ptrtools.h, mcache.h, queue.h, backtrace.h, machine_routines.h, IOMapper.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bsd/kern/uipc_syscalls.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.775 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.887 IQR)
- **Top Global Matches:** file_cluster_8: 14.775, file_cluster_13: 14.788, file_cluster_11: 14.813
- **Magnitude:** 4440.96 | **LOC:** 3738 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.2864%), Tech Debt (26.204%)
**Top Internal Functions/Classes:**
  * `getpeername` (Impact: 423.3)
  * `sendmsg_x` (Impact: 123.3)
  * `recvmsg_x` (Impact: 121.0)
  * `connectx_nocancel` (Impact: 114.6)
  * `accept_nocancel` (Impact: 111.0)
    * *Intent:* /* * Returns: 0 Success * EDESTADDRREQ Destination address required * EBADF Bad file descriptor * EA...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 663`, `structural_boundaries: 406`, `args: 63`, `func_start: 50`, `class_start: 105`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1909`, `dead_code: 3`, `fragile_debt: 3`, `orphaned_logic: 19`
* *Architecture:* `io: 39`, `api: 517`, `import: 30`
* *Defense:* `safety: 12`, `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vnode_internal.h, sysctl.h, malloc.h, priv.h, ptrtools.h, socketvar.h, mac_framework.h, audit.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `osfmk/kern/kcdata.h` (C) | Magnitude: 392.88 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 267, api: 208, macros: 184, structural_boundaries: 103
- `tools/lldbmacros/turnstile.py` (PYTHON) | Magnitude: 0.1 | Delta: **0.165 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, branch: 35, structural_boundaries: 27, doc: 18
- `config/newvers.pl` (PERL) | Magnitude: 227.54 | Delta: **0.405 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 202, indent_spaces: 58, branch: 53, regex_execution: 38
- `tools/lldbmacros/bank.py` (PYTHON) | Magnitude: 0.05 | Delta: **0.509 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 21, branch: 14, doc: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `bsd/net/pf_ioctl.c` (C) | Magnitude: 4837.84 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 3048, state_mutation: 2413, pointers: 1880, branch: 1212
- `libsyscall/wrappers/libproc/proc_listpidspath.c` (C) | Magnitude: 295.76 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 229, state_mutation: 152, branch: 76, pointers: 65
- `osfmk/vm/lz4.c` (C) | Magnitude: 697.74 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 439, indent_tabs: 304, branch: 116, api: 102
- `bsd/net/if.c` (C) | Magnitude: 4045.9 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 1916, state_mutation: 1369, branch: 941, api: 685
- `tools/remote_build.sh` (SHELL) | Magnitude: 0.32 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 168, branch: 101, io: 70, reflection_metaprogramming: 69

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `EXTERNAL_HEADERS/corecrypto/cccmac.h` (C) | Magnitude: 42.02 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: pointers: 35, doc: 27, api: 26, macros: 20
- `osfmk/x86_64/boot_pt.c` (C) | Magnitude: 34.78 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 22, state_mutation: 16, reflection_metaprogramming: 14, indent_tabs: 7
- `EXTERNAL_HEADERS/corecrypto/ccn.h` (C) | Magnitude: 152.4 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 138, pointers: 92, indent_spaces: 86, api: 85
- `bsd/sys/_endian.h` (C) | Magnitude: 26.1 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 44, reflection_metaprogramming: 30, branch: 10, state_mutation: 6
- `tools/tests/personas/persona_test_run_src.sh` (SHELL) | Magnitude: 0.58 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 267, branch: 245, safety_bypasses: 222, state_mutation: 201

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `bsd/net/rtsock.c` (C) | Magnitude: 1973.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 986, state_mutation: 962, pointers: 483, branch: 329
- `tests/thread_call_race_71455282.c` (C) | Magnitude: 39.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 20, state_mutation: 19, concurrency: 12, import: 8
- `osfmk/UserNotification/KUNCUserNotifications.c` (C) | Magnitude: 284.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 205, api: 110, state_mutation: 93, pointers: 56
- `tools/tests/MPMMTest/KQMPMMtest.c` (C) | Magnitude: 0.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 572, state_mutation: 485, branch: 159, pointers: 117
- `tests/bounded_array_src/ctor.default.cpp` (CPP) | Magnitude: 58.58 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 46, state_mutation: 45, structural_boundaries: 10, test: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `libkern/libkern/c++/intrusive_shared_ptr.h` (CPP) | Magnitude: 219.46 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 174, structural_boundaries: 169, indent_tabs: 66, generics: 36
- `iokit/IOKit/IOMessage.h` (C) | Magnitude: 15.2 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: sec_high_risk_execution: 14, macros: 8, doc: 7, generics: 2
- `libkern/os/atomic.h` (C) | Magnitude: 23.36 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 29, generics: 16, explicit_casts: 11, branch: 10
- `libkern/libkern/c++/OSSharedPtr.h` (C) | Magnitude: 39.56 | Delta: **0.154 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 50, generics: 31, state_mutation: 25, branch: 20
- `iokit/IOKitUser/IOBlockStorageDevice.h` (C) | Magnitude: 10.52 | Delta: **0.226 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: generics: 1, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tools/tests/Makefile` (MAKEFILE) | Magnitude: 0.01 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 21, branch: 14, structural_boundaries: 12, io: 7
- `tools/tests/affinity/Makefile` (MAKEFILE) | Magnitude: 0.06 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_tabs: 6, reflection_metaprogramming: 5, branch: 4
- `config/generate_linker_exports.sh` (SHELL) | Magnitude: 9.5 | Delta: **0.115 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: branch: 3, state_mutation: 3, structural_boundaries: 2, args: 2
- `tools/tests/MPMMTest/Makefile` (MAKEFILE) | Magnitude: 0.01 | Delta: **0.206 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 15, branch: 8, structural_boundaries: 7, comprehensions: 3
- `makedefs/MakeInc.def` (MAKEFILE) | Magnitude: 120.64 | Delta: **0.322 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 308, indent_tabs: 175, safety_bypasses: 147, branch: 135

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
- `bsd/security/audit/audit_bsd.c` (C) | Magnitude: 503.22 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 245, pointers: 216, state_mutation: 193, structural_boundaries: 85
- `tools/tests/execperf/run.c` (C) | Magnitude: 0.11 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 52, state_mutation: 42, branch: 16, api: 15
- `tests/kqueue_close.c` (C) | Magnitude: 68.46 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 33, state_mutation: 30, concurrency: 12, events: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `bsd/net/kpi_interface.h` (C) | Magnitude: 381.24 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 278, indent_tabs: 231, doc: 158, structural_boundaries: 103

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tools/lldbmacros/core/kernelcore.py` (PYTHON) | Magnitude: 0.62 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 403, encapsulation: 162, state_mutation: 137, structural_boundaries: 127
- `tools/lldbmacros/kevent.py` (PYTHON) | Magnitude: 0.1 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
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
- `osfmk/vm/vm_purgeable.c` (C) | Magnitude: 582.54 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 317, state_mutation: 217, pointers: 125, branch: 95

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

- `EXTERNAL_HEADERS/stdint.h` -> **Severity: 4124.358** (Blast Radius: 42.161 * Doc Risk: 97.824%)
- `bsd/sys/unistd.h` -> **Severity: 837.017** (Blast Radius: 13.983 * Doc Risk: 59.8596%)
- `EXTERNAL_HEADERS/stdatomic.h` -> **Severity: 480.993** (Blast Radius: 4.81 * Doc Risk: 99.9986%)
- `san/kasan.h` -> **Severity: 450.0** (Blast Radius: 4.5 * Doc Risk: 100.0%)
- `EXTERNAL_HEADERS/Availability.h` -> **Severity: 376.836** (Blast Radius: 31.613 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
