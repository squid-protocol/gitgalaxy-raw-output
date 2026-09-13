# ARCHITECTURAL_BRIEF: freebsd-src
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/freebsd/freebsd-src.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 109673 |
| Analyzed Artifacts (Scanned) | 84671 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 25002 |
| Total LOC | 17542095 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 77.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0223 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3807 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 43330 | 12566020 | 51.2% |
| PLAINTEXT | 10102 | 8231 | 11.9% |
| CPP | 8588 | 2968379 | 10.1% |
| SHELL | 6444 | 398736 | 7.6% |
| MAKEFILE | 5961 | 229410 | 7.0% |
| YAML | 4591 | 387525 | 5.4% |
| PERL | 1828 | 371758 | 2.2% |
| M4 | 974 | 147630 | 1.2% |
| ASSEMBLY | 784 | 103833 | 0.9% |
| JSON | 536 | 102786 | 0.6% |
| MARKDOWN | 495 | 0 | 0.6% |
| PYTHON | 298 | 50061 | 0.4% |
| YACC | 172 | 61915 | 0.2% |
| TD | 117 | 80328 | 0.1% |
| HTML | 112 | 30901 | 0.1% |
| LUA | 65 | 10758 | 0.1% |
| XML | 63 | 49 | 0.1% |
| CSHARP | 33 | 3571 | 0.0% |
| CSS | 31 | 6258 | 0.0% |
| BINARY_THREAT | 26 | 26 | 0.0% |
| PHP | 17 | 216 | 0.0% |
| BATCH | 17 | 1206 | 0.0% |
| JAVA | 15 | 3211 | 0.0% |
| RUBY | 14 | 856 | 0.0% |
| TCL | 14 | 5517 | 0.0% |
| SQLITE | 11 | 1272 | 0.0% |
| CSV | 9 | 521 | 0.0% |
| OBJECTIVE-C | 9 | 134 | 0.0% |
| POWERSHELL | 4 | 379 | 0.0% |
| MATLAB | 3 | 241 | 0.0% |
| PROTO | 2 | 103 | 0.0% |
| DOCKERFILE | 2 | 45 | 0.0% |
| JAVASCRIPT | 2 | 215 | 0.0% |
| FORTRAN | 2 | 4 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 74006 | 87.4% |
| Unknown | 381 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10266 | 12.1% |
| Static: Minified & Vendor Opaque Mass | 18 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 25002*

**Composition by Extension & Reason:**
- `no_extension`: 2630x Unsupported Format (.undeterminable), 601x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 323x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.depend`: 1574x Excluded (Unsupported Extension: '.depend'), 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 920x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 94x Excluded: Neighborhood Micro-Mass Limit Exceeded, 24x Excluded (Machine-Generated Source Code Signature: 28 LOC)
- `.3`: 607x Excluded: Neighborhood Micro-Mass Limit Exceeded, 15x Excluded (Machine-Generated Source Code Signature: 111 LOC), 12x Excluded (Machine-Generated Source Code Signature: 117 LOC)
- `.cpp`: 1170x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1621 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1761 LOC)
- `.d`: 1070x Excluded (Unsupported Extension: '.d'), 32x Excluded: Neighborhood Micro-Mass Limit Exceeded, 8x Unsupported Format (.d)
- `.src`: 940x Excluded (Unsupported Extension: '.src')
- `.yaml`: 36x Zero-Density Threshold (LOC: 51, Signals: 0), 34x Zero-Density Threshold (LOC: 52, Signals: 0), 30x Zero-Density Threshold (LOC: 53, Signals: 0)
- `.bc`: 532x Unsupported Format (.bc), 2x Excluded (Unsupported Extension: '.bc')
- `.td`: 517x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 8282 LOC), 1x Excluded (Machine-Generated Source Code Signature: 99 LOC)
- `.uu`: 512x Excluded (Unsupported Extension: '.uu'), 6x Unsupported Format (.uu), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.0`: 447x Unsupported Format (.0), 40x Excluded: Neighborhood Micro-Mass Limit Exceeded, 31x Excluded (Unsupported Extension: '.0')
- `.exp`: 513x Excluded (Unsupported Extension: '.exp'), 1x Unsupported Format (.exp)
- `.t`: 300x Unsupported Format (.undeterminable), 24x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 16 LOC)
- `.c`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded: Neighborhood Micro-Mass Limit Exceeded, 4x Excluded (Machine-Generated Source Code Signature: 57 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 25.1 | 7.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 49.4 | 64.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 17.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.3 | 0.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 40.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 62.3 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 47.3 | 6.9 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4627915 | 44023 | 117 | `sys/netinet/tcp_stacks/rack.c` |
| cleanup | 51085 | 10787 | 1 | `contrib/unbound/util/configparser.c` |
| guards | 1021833 | 36926 | 30 | `contrib/bsnmp/tests/catch.hpp` |
| danger | 270749 | 20117 | 7 | `contrib/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_common_interceptors.inc` |
| concurrency | 36390 | 5382 | 0 | `sys/cam/ctl/ctl.c` |
| connectivity | 402014 | 38931 | 11 | `contrib/llvm-project/clang/lib/Headers/avx512vlintrin.h` |
| io | 121833 | 10403 | 1 | `usr.sbin/freebsd-update/freebsd-update.sh` |
| crypto | 6 | 4 | 0 | `tests/sys/geom/class/eli/gentestvect.py` |
| ipc | 21436 | 4387 | 0 | `crypto/openssl/crypto/bn/asm/ppc64-mont.pl` |
| time | 10326 | 3191 | 0 | `contrib/tzcode/localtime.c` |
| serialization | 591 | 192 | 0 | `contrib/ntp/scripts/calc_tickadj/Makefile.in` |
| regex | 17324 | 2972 | 0 | `crypto/openssl/crypto/chacha/asm/chacha-loongarch64.pl` |
| events | 23946 | 4919 | 0 | `crypto/openssh/configure.ac` |
| tests | 23573 | 1255 | 0 | `contrib/googletest/googletest/test/gtest_unittest.cc` |
| docs | 396434 | 16755 | 3 | `contrib/llvm-project/clang/include/clang/ASTMatchers/ASTMatchers.h` |
| debt | 145069 | 19246 | 3 | `contrib/netbsd-tests/kernel/t_ptrace_wait.c` |
| mutation | 4167229 | 54691 | 118 | `contrib/one-true-awk/testdir/funstack.in` |
| dead_code | 181885 | 24473 | 4 | `sys/dev/sfxge/common/efx_regs_mcdi.h` |
| credential | 1457 | 120 | 0 | `contrib/expat/tests/nsalloc_tests.c` |
| threat | 203145 | 23878 | 4 | `sys/dev/cxgbe/firmware/t4fw_interface.h` |
| ml_ai | 35072 | 5826 | 0 | `sys/netinet/tcp_stacks/rack.c` |
| ui | 2783 | 317 | 0 | `crypto/openssl/crypto/ec/asm/ecp_nistz256-sparcv9.pl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `usr.sbin/freebsd-update/freebsd-update.sh` (Hits: 1263)
- `contrib/lua/doc/contents.html` (Hits: 1094)
- `tests/sys/netinet6/frag6/frag6_05.sh` (Hits: 752)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **kernel.h** (`sys/sys/kernel.h`) — 3256 inbound connections
2. **malloc.h** (`sys/sys/malloc.h`) — 2268 inbound connections
3. **socket.h** (`sys/sys/socket.h`) — 2242 inbound connections
4. **bus.h** (`sys/sys/bus.h`) — 2220 inbound connections
5. **module.h** (`sys/sys/module.h`) — 2025 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **PassBuilder.cpp** (`contrib/llvm-project/llvm/lib/Passes/PassBuilder.cpp`) — 305 outbound dependencies
2. **sanitizer_platform_limits_netbsd.cpp** (`contrib/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.cpp`) — 202 outbound dependencies
3. **ASTReader.cpp** (`contrib/llvm-project/clang/lib/Serialization/ASTReader.cpp`) — 149 outbound dependencies
4. **PassBuilderPipelines.cpp** (`contrib/llvm-project/llvm/lib/Passes/PassBuilderPipelines.cpp`) — 125 outbound dependencies
5. **AsmPrinter.cpp** (`contrib/llvm-project/llvm/lib/CodeGen/AsmPrinter/AsmPrinter.cpp`) — 119 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `nfsv4_loadattr` (@ `sys/fs/nfs/nfs_commonsubs.c`) -> Impact: **2574.7** | LOC: 1268
  * *Intent:* /* * Get the attributes for V4. * If the compare flag is true, test for any attribute changes, * otherwise return the attribute values. * These attrib...
- `hostapd_config_fill` (@ `contrib/wpa/hostapd/config_file.c`) -> Impact: **1953.1** | LOC: 1389
  * *Intent:* #endif /* CONFIG_IEEE80211BE */
- `inheritsFrom` (@ `contrib/llvm-project/llvm/utils/TableGen/X86DisassemblerTables.cpp`) -> Impact: **1744.6** | LOC: 498
  * *Intent:* /// inheritsFrom - Indicates whether all instructions in one class also belong /// to another class. /// /// @param child - The class that may be the ...
- `process_server_config_line_depth` (@ `crypto/openssh/servconf.c`) -> Impact: **1666.3** | LOC: 1450
- `wpa_supplicant_ctrl_iface_process` (@ `contrib/wpa/wpa_supplicant/ctrl_iface.c`) -> Impact: **1637.7** | LOC: 1073
  * *Intent:* #endif /* CONFIG_NAN_USD */
- `process_config_line_depth` (@ `crypto/openssh/readconf.c`) -> Impact: **1631.7** | LOC: 1410
  * *Intent:* #define WHITESPACE " \t\r\n"
- `dtrace_dif_subr` (@ `sys/cddl/contrib/opensolaris/uts/common/dtrace/dtrace.c`) -> Impact: **1630.8** | LOC: 2634
  * *Intent:* /* * Emulate the execution of DTrace ID subroutines invoked by the call opcode. * Notice that we don't bother validating the proper number of argument...
- `elftc_reloc_type_str` (@ `contrib/elftoolchain/libelftc/elftc_reloc_type_str.c`) -> Impact: **1584.3** | LOC: 924
  * *Intent:* * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE * ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE ...
- `setoption` (@ `contrib/sendmail/src/readcf.c`) -> Impact: **1564.0** | LOC: 1740
  * *Intent:* #define OPTNAME o->o_name == NULL ? "<unknown>" : o->o_name
- `soreceive_generic_locked` (@ `sys/kern/uipc_socket.c`) -> Impact: **1528.2** | LOC: 2360
  * *Intent:* * records are added to the sockbuf by sbappend. In particular, each record * (mbufs linked through m_next) must begin with an address if the protocol ...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `secure/caroot/trusted` | 151 | 750009.32 | 0.06% | 0.0% |
| `secure/caroot/untrusted` | 43 | 210009.32 | 0.22% | 0.0% |
| `sys/kern` | 242 | 205262.82 | 66.88% | 46.61% |
| `crypto/openssh/regress/unittests/hostkeys/testdata` | 30 | 150000.0 | 0.0% | 0.0% |
| `crypto/openssh/regress/unittests/sshkey/testdata` | 25 | 125000.0 | 0.0% | 0.0% |
| `sys/netinet` | 146 | 112111.08 | 40.47% | 18.24% |
| `crypto/openssl/apps` | 79 | 110414.21 | 63.81% | 6.92% |
| `crypto/openssh/regress/misc/fuzz-harness/testdata` | 18 | 80000.02 | 1.74% | 4.89% |
| `crypto/openssh/regress/unittests/sshsig/testdata` | 14 | 70000.0 | 0.0% | 0.0% |
| `contrib/bearssl/samples` | 22 | 65004.74 | 5.28% | 4.93% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `contrib/bmake/mk/sys/NetBSD.mk` -> **100.0%** Exposure
- `contrib/bmake/mk/sys/UnixWare.mk` -> **100.0%** Exposure
- `contrib/bmake/unit-tests/deptgt-suffixes.mk` -> **100.0%** Exposure
- `contrib/bmake/unit-tests/directive-elif.mk` -> **100.0%** Exposure
- `contrib/bmake/unit-tests/directive-for-escape.mk` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cddl/usr.sbin/dwatch/libexec/Makefile` -> **100.0%** Exposure
- `contrib/bmake/unit-tests/Makefile` -> **100.0%** Exposure
- `contrib/bmake/unit-tests/varmod-hash.mk` -> **100.0%** Exposure
- `contrib/elftoolchain/libelf/os.Linux.mk` -> **100.0%** Exposure
- `contrib/kyua/cli/Makefile.am.inc` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `contrib/llvm-project/llvm/lib/IR/Core.cpp` -> **623** Orphaned Functions | **0** Duplicates
- `contrib/llvm-project/clang/include/clang/AST/OpenMPClause.h` -> **0** Orphaned Functions | **480** Duplicates
- `contrib/llvm-project/clang/lib/Serialization/ASTReader.cpp` -> **382** Orphaned Functions | **0** Duplicates
- `contrib/llvm-project/clang/lib/AST/StmtProfile.cpp` -> **371** Orphaned Functions | **0** Duplicates
- `contrib/llvm-project/clang/lib/AST/ASTContext.cpp` -> **353** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `contrib/wpa/hs20/client/osu_client.c` -> **100.0%** Exposure
- `contrib/wpa/src/tls/tlsv1_cred.c` -> **100.0%** Exposure
- `contrib/wpa/wpa_supplicant/eapol_test.c` -> **100.0%** Exposure
- `crypto/openssl/test/pemtest.c` -> **100.0%** Exposure
- `contrib/pam-krb5/ci/kdc-setup-heimdal` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1026` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `350885` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `sys/contrib/vchiq/interface/compat/vchi_bsd.c` (C) -> Cumulative Risk: **871.78**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3.51 | **LOC:** 527 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.996%), State Flux (99.9941%)
- **Heaviest Functions:** `wait_for_completion_interruptible_timeout` (Impact: 17.4), `vchiq_thread_create` (Impact: 10.6), `wait_for_completion_interruptible` (Impact: 8.1)

### 2. `sys/dev/sound/midi/midi.c` (C) -> Cumulative Risk: **813.37**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 444.5 | **LOC:** 540 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 95.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.6297%)
- **Heaviest Functions:** `midi_open` (Impact: 33.9), `midi_write` (Impact: 25.4), `midi_read` (Impact: 23.2)

### 3. `sys/dev/ichsmb/ichsmb.c` (C) -> Cumulative Risk: **812.08**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 428.68 | **LOC:** 718 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9949%), Documentation (95.2381%), Concurrency (94.0774%)
- **Heaviest Functions:** `ichsmb_device_intr` (Impact: 39.8), `ichsmb_bwrite` (Impact: 19.4), `ichsmb_bread` (Impact: 16.9)

### 4. `sys/kern/subr_rman.c` (C) -> Cumulative Risk: **811.6**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 885.88 | **LOC:** 1102 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (99.1475%)
- **Heaviest Functions:** `rman_reserve_resource` (Impact: 105.7), `rman_adjust_resource` (Impact: 78.0), `rman_manage_region` (Impact: 53.9)

### 5. `sys/dev/nvmf/controller/nvmft_qpair.c` (C) -> Cumulative Risk: **792.3**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 254.0 | **LOC:** 422 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9384%), Tech Debt (97.7438%)
- **Heaviest Functions:** `nvmft_receive_capsule` (Impact: 12.1), `_nvmft_send_response` (Impact: 10.3), `nvmft_datamove_task` (Impact: 8.0)

### 6. `contrib/ofed/libibverbs/device.c` (C) -> Cumulative Risk: **785.23**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3.42 | **LOC:** 462 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (95.8041%)
- **Heaviest Functions:** `__ibv_get_async_event` (Impact: 31.6), `__ibv_ack_async_event` (Impact: 24.4), `__ibv_open_device` (Impact: 21.7)

### 7. `sys/dev/hid/hidraw.c` (C) -> Cumulative Risk: **783.04**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1007.22 | **LOC:** 1069 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (98.5052%)
- **Heaviest Functions:** `hidraw_ioctl` (Impact: 249.4), `hidraw_read` (Impact: 36.0), `hidraw_write` (Impact: 26.4)

### 8. `sys/dev/sound/pci/spicds.c` (C) -> Cumulative Risk: **781.53**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 311.38 | **LOC:** 370 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9851%), Cognitive Load (96.4543%)
- **Heaviest Functions:** `spicds_set` (Impact: 101.0), `spicds_wrcd` (Impact: 35.1), `spicds_init` (Impact: 13.6)

### 9. `crypto/openssh/regress/test-exec.sh` (SHELL) -> Cumulative Risk: **772.68**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 8.97 | **LOC:** 1067 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Secrets Risk (100.0%)
- **Heaviest Functions:** `__global_context__` (Impact: 25.6), `Anonymous_Block` (Impact: 22.8), `puttysetup` (Impact: 16.8)

### 10. `sys/dev/sound/pcm/mixer.c` (C) -> Cumulative Risk: **772.63**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1441.92 | **LOC:** 1528 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.2862%), Documentation (92.8571%)
- **Heaviest Functions:** `mixer_ioctl_channel` (Impact: 90.0), `mixer_ioctl_cmd` (Impact: 89.8), `mixer_set` (Impact: 89.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `sys/netinet/tcp_stacks/rack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 26313.46 | **LOC:** 24750 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 71.4%
- **Risk Profile:** Cognitive Load (93.3025%), Tech Debt (8.1992%)
**Top Internal Functions/Classes:**
  * `rack_output` (Impact: 1065.8)
  * `rack_process_option` (Impact: 694.8)
  * `rack_do_segment_nounlock` (Impact: 492.0)
  * `rack_proc_sack_blk` (Impact: 485.5)
  * `rack_fast_rsm_output` (Impact: 450.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 4159 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 13430
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4875`, `structural_boundaries: 1978`, `args: 478`, `func_start: 218`, `class_start: 347`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 5112`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 9`
* *Architecture:* `api: 2`, `import: 75`
* *Defense:* `safety: 1`, `doc: 18`, `immutability_locks: 7`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 57):` cpu.h, in_cksum.h, route.h, nhop.h, vnet.h, cc.h, cc_newreno.h, in.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/pms/RefTisa/tisa/sassata/sata/host/sat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16044.66 | **LOC:** 23309 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.4417%), Tech Debt (9.2889%)
**Top Internal Functions/Classes:**
  * `satModeSense10` (Impact: 284.2)
    * *Intent:* * * \param tiRoot: Pointer to TISA initiator driver/port instance. * \param tiIORequest: Pointer to ...
  * `satAddSATAIDDevCB` (Impact: 214.9)
    * *Intent:* * new or old. If new, add it to the devicelist. * * \param agRoot: Handles for this instance of SAS/...
  * `satModeSelect10` (Impact: 211.1)
    * *Intent:* * * \param tiRoot: Pointer to TISA initiator driver/port instance. * \param tiIORequest: Pointer to ...
  * `tdsaDiscoveryStartIDDevCB` (Impact: 206.3)
    * *Intent:* * of discovery. * * \param agRoot: Handles for this instance of SAS/SATA hardware * \param agIOReque...
  * `satModeSelect6` (Impact: 179.8)
    * *Intent:* * * \param tiRoot: Pointer to TISA initiator driver/port instance. * \param tiIORequest: Pointer to ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2188 instances
* *State Mutation (weighted view):* 9926
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1747`, `structural_boundaries: 765`, `args: 184`, `func_start: 125`
* *Risk/State:* `safety_bypasses: 118`, `state_mutation: 5550`, `dead_code: 40`, `unreferenced_by_name: 35`
* *Architecture:* `api: 125`, `import: 31`
* *Defense:* `doc: 847`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` dm.h, dmapi.h, tddmapi.h, sa.h, saapi.h, saosapi.h, sm.h, smapi.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/pms/RefTisa/sat/src/smsat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15910.4 | **LOC:** 20820 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.9259%), Tech Debt (10.0751%)
**Top Internal Functions/Classes:**
  * `smsatModeSense10` (Impact: 284.3)
  * `smsatModeSelect10` (Impact: 217.7)
  * `smsatModeSelect6` (Impact: 186.4)
  * `smsatSendDiagnostic` (Impact: 162.0)
  * `smsatLogSense` (Impact: 155.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2186 instances
* *State Mutation (weighted view):* 10017
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1740`, `structural_boundaries: 751`, `args: 200`, `func_start: 126`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 5645`, `dead_code: 17`, `unreferenced_by_name: 48`
* *Architecture:* `api: 126`, `import: 15`
* *Defense:* `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` sa.h, saapi.h, saosapi.h, sm.h, smapi.h, tdsmapi.h, smdefs.h, smproto.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/fs/nfsclient/nfs_clrpcops.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15838.1 | **LOC:** 10019 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 90.9%
- **Risk Profile:** Cognitive Load (79.7546%), Tech Debt (17.0615%)
**Top Internal Functions/Classes:**
  * `nfsrpc_readdirplus` (Impact: 415.9)
    * *Intent:* /* * NFS V3 readdir plus RPC. Used in place of nfsrpc_readdir(). * (Also used for NFS V4 when mount ...
  * `nfsrpc_openrpc` (Impact: 325.5)
    * *Intent:* /* * the actual open rpc */
  * `nfsrpc_readdir` (Impact: 323.5)
    * *Intent:* * 3 - return them to userland in the "struct dirent", so future versions * of libc can use them and ...
  * `nfsrpc_createlayout` (Impact: 287.8)
    * *Intent:* /* * Similar nfsrpc_createv4(), but also does the LayoutGet operation. * Used only for mounts with p...
  * `nfsrpc_rename` (Impact: 277.6)
    * *Intent:* /* * Do an nfs rename rpc. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 25 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 2264 instances
* *Concurrency (weighted view):* 18
* *Memory Alloc (weighted view):* 26
* *State Mutation (weighted view):* 7262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2311`, `structural_boundaries: 1252`, `args: 441`, `func_start: 105`, `class_start: 407`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 2734`, `fragile_debt: 5`, `unreferenced_by_name: 44`
* *Architecture:* `api: 76`, `concurrency: 3`, `import: 7`
* *Defense:* `safety: 14`, `sync_locks: 6`, `immutability_locks: 4`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` nfsport.h, nfs.h, opt_inet6.h, cdefs.h, extattr.h, sysctl.h, taskqueue.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/tcp_stacks/bbr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14663.14 | **LOC:** 14818 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.7997%), Tech Debt (8.5718%)
**Top Internal Functions/Classes:**
  * `bbr_output_wtime` (Impact: 1056.2)
    * *Intent:* /* * Return 0 on success and a errno on failure to send. * Note that a 0 return may not mean we sent...
  * `bbr_set_sockopt` (Impact: 319.1)
    * *Intent:* /* * bbr_ctloutput() must drop the inpcb lock before performing copyin on * socket option arguments....
  * `bbr_do_segment_nounlock` (Impact: 290.1)
  * `bbr_process_data` (Impact: 270.2)
    * *Intent:* /* * Return value of 1, the TCB is unlocked and most * likely gone, return value of 0, the TCB is st...
  * `bbr_log_ack` (Impact: 195.3)
    * *Intent:* /* * Returns the number of bytes that were * acknowledged by SACK blocks. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 2196 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 7025
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2913`, `structural_boundaries: 1263`, `args: 291`, `func_start: 179`, `class_start: 180`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2633`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 8`
* *Architecture:* `import: 71`
* *Defense:* `doc: 8`, `immutability_locks: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 56):` in_cksum.h, ethernet.h, if.h, if_var.h, route.h, nhop.h, vnet.h, cc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/sctp_output.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14649.16 | **LOC:** 13929 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (72.8846%), Tech Debt (13.7546%)
**Top Internal Functions/Classes:**
  * `sctp_med_chunk_output` (Impact: 992.3)
  * `sctp_lower_sosend` (Impact: 976.2)
  * `sctp_lowlevel_chunk_output` (Impact: 652.0)
    * *Intent:* #endif
  * `sctp_send_initiate_ack` (Impact: 573.8)
    * *Intent:* /* * Given a MBUF chain that was sent into us containing an INIT. Build a * INIT-ACK with COOKIE and...
  * `sctp_chunk_retransmission` (Impact: 351.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2153 instances
* *State Mutation (weighted view):* 6804
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2355`, `structural_boundaries: 1707`, `args: 402`, `func_start: 85`, `class_start: 390`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 2498`, `dead_code: 9`, `planned_debt: 3`, `fragile_debt: 18`, `unreferenced_by_name: 22`
* *Architecture:* `api: 46`, `import: 21`
* *Defense:* `safety: 2`, `doc: 12`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` in_cksum.h, sctp_asconf.h, sctp_auth.h, sctp_bsd_addr.h, sctp_crc32.h, sctp_header.h, sctp_indata.h, sctp_input.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/cam/ctl/ctl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 12402.26 | **LOC:** 14553 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (82.7295%), Tech Debt (33.3952%)
**Top Internal Functions/Classes:**
  * `ctl_ioctl` (Impact: 496.0)
  * `ctl_pro_preempt` (Impact: 148.8)
    * *Intent:* /* * Returns 0 if ctl_persistent_reserve_out() should continue, non-zero if * it should return. */
  * `ctl_mode_sense` (Impact: 129.8)
  * `ctl_persistent_reserve_out` (Impact: 118.3)
  * `ctl_isc_event_handler` (Impact: 105.0)
    * *Intent:* /* * ISC (Inter Shelf Communication) event handler. Events from the HA * subsystem come in here. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 115 instances
* *Amplified Race Conditions:* 106 instances
* *Amplified Cascading Flux:* 2018 instances
* *Concurrency (weighted view):* 650
* *Memory Alloc (weighted view):* 50
* *State Mutation (weighted view):* 6714
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2165`, `structural_boundaries: 2476`, `args: 409`, `func_start: 226`, `class_start: 485`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 2678`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 42`, `unreferenced_by_name: 72`
* *Architecture:* `api: 107`, `concurrency: 120`, `import: 42`
* *Defense:* `safety: 39`, `sync_locks: 322`, `immutability_locks: 66`, `cleanup: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` cam.h, ctl.h, ctl_backend.h, ctl_debug.h, ctl_error.h, ctl_frontend.h, ctl_ha.h, ctl_io.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/bxe/bxe.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 12225.12 | **LOC:** 19454 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.6716%), Tech Debt (38.2873%)
**Top Internal Functions/Classes:**
  * `bxe_tx_encap` (Impact: 135.8)
    * *Intent:* /* * Encapsulte an mbuf cluster into the tx bd chain and makes the memory * visible to the controlle...
  * `bxe_alloc_hsi_mem` (Impact: 96.0)
  * `bxe_eioctl` (Impact: 95.7)
  * `bxe_init_hw_common` (Impact: 95.0)
    * *Intent:* /** * bxe_init_hw_common - initialize the HW at the COMMON phase. * * @sc: driver handle */
  * `bxe_ioctl` (Impact: 94.7)
    * *Intent:* /* * Handles any IOCTL calls from the operating system. * * Returns: * 0 = Success, >0 Failure */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 1890 instances
* *Concurrency (weighted view):* 18
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 6303
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2375`, `structural_boundaries: 1900`, `args: 680`, `func_start: 422`, `class_start: 276`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 2523`, `dead_code: 23`, `planned_debt: 3`, `fragile_debt: 105`, `unreferenced_by_name: 27`
* *Architecture:* `api: 51`, `concurrency: 3`, `import: 11`
* *Defense:* `safety: 39`, `doc: 67`, `sync_locks: 7`, `immutability_locks: 18`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` 57710_int_offsets.h, 57711_int_offsets.h, 57712_int_offsets.h, bxe.h, bxe_dump.h, bxe_ioctl.h, ecore_init.h, ecore_init_ops.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netpfil/pf/pf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 12063.96 | **LOC:** 12125 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 70.6%
- **Risk Profile:** Cognitive Load (93.428%), Tech Debt (13.693%)
**Top Internal Functions/Classes:**
  * `pf_test` (Impact: 518.0)
    * *Intent:* #if defined(INET) || defined(INET6)
  * `pf_test_state_icmp` (Impact: 462.9)
  * `pf_tcp_track_full` (Impact: 346.6)
  * `pf_test_rule` (Impact: 245.4)
  * `pf_route` (Impact: 235.7)
    * *Intent:* #ifdef INET
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 22 instances
* *Amplified Cascading Flux:* 1720 instances
* *Memory Alloc (weighted view):* 12
* *State Mutation (weighted view):* 5357
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2482`, `structural_boundaries: 2011`, `args: 496`, `func_start: 173`, `class_start: 405`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1917`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 12`, `unreferenced_by_name: 24`
* *Architecture:* `api: 86`, `concurrency: 3`, `import: 68`
* *Defense:* `safety: 11`, `doc: 1`, `sync_locks: 6`, `immutability_locks: 63`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 57):` sha512.h, in_cksum.h, if.h, if_pflog.h, if_pfsync.h, if_private.h, if_types.h, if_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/cxgbe/t4_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 11346.3 | **LOC:** 14378 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 53.3%
- **Risk Profile:** Cognitive Load (80.0876%), Tech Debt (9.7389%)
**Top Internal Functions/Classes:**
  * `cxgbe_ioctl` (Impact: 167.4)
  * `port_mword` (Impact: 166.1)
    * *Intent:* /* * Base media word (without ETHER, pause, link active, etc.) for the port at the * given speed. */
  * `sysctl_meminfo` (Impact: 137.5)
  * `t4_ioctl` (Impact: 132.8)
  * `t4_attach` (Impact: 130.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 64 instances
* *Amplified Race Conditions:* 66 instances
* *Amplified Cascading Flux:* 1963 instances
* *Concurrency (weighted view):* 399
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 6158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2182`, `structural_boundaries: 1683`, `args: 775`, `func_start: 259`, `class_start: 381`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 2232`, `fragile_debt: 6`, `unreferenced_by_name: 12`
* *Architecture:* `api: 47`, `concurrency: 69`, `import: 51`
* *Defense:* `safety: 25`, `test: 17`, `sync_locks: 139`, `immutability_locks: 78`, `cleanup: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` common.h, t4_msg.h, t4_regs.h, t4_regs_values.h, cudbg.h, db_lex.h, ddb.h, pcireg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/ufs/ffs/ffs_softdep.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10491.54 | **LOC:** 15021 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.6695%), Tech Debt (9.4419%)
**Top Internal Functions/Classes:**
  * `softdep_journal_freeblocks` (Impact: 144.2)
    * *Intent:* * disk through step 4. * 4) Reap unsatisfied dependencies that are beyond the truncated area, * elim...
  * `handle_written_inodeblock` (Impact: 139.1)
    * *Intent:* /* * Called from within softdep_disk_write_complete above to restore * in-memory inode block content...
  * `softdep_process_journal` (Impact: 109.2)
    * *Intent:* /* * Flush some journal records to disk. */
  * `softdep_check_suspend` (Impact: 100.2)
    * *Intent:* /* * Check if it is safe to suspend the file system now. On entry, * the vnode interlock for devvp s...
  * `initiate_write_inodeblock_ufs2` (Impact: 99.8)
    * *Intent:* /* * Version of initiate_write_inodeblock that handles UFS2 dinodes. * Note that any bug fixes made ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 14 instances
* *Amplified Cascading Flux:* 1675 instances
* *Memory Alloc (weighted view):* 38
* *State Mutation (weighted view):* 5360
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1916`, `structural_boundaries: 2638`, `args: 776`, `func_start: 316`, `class_start: 919`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 2010`, `planned_debt: 1`, `fragile_debt: 10`, `unreferenced_by_name: 1`
* *Architecture:* `api: 107`, `concurrency: 1`, `import: 42`
* *Defense:* `test: 11`, `sync_locks: 2`, `immutability_locks: 4`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` ddb.h, geom.h, geom_vfs.h, opt_ddb.h, opt_ffs.h, opt_quota.h, bio.h, buf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sbin/camcontrol/camcontrol.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10297.84 | **LOC:** 10824 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (81.0087%), Tech Debt (9.8598%)
**Top Internal Functions/Classes:**
  * `readdefects` (Impact: 383.8)
  * `sanitize` (Impact: 335.4)
  * `mmcsdcmd` (Impact: 308.9)
  * `ratecontrol` (Impact: 293.7)
  * `atacapprint` (Impact: 239.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 60 instances
* *Amplified Cascading Flux:* 1412 instances
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 4308
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2131`, `structural_boundaries: 1075`, `args: 183`, `func_start: 104`, `class_start: 190`
* *Risk/State:* `safety_bypasses: 38`, `high_risk_execution: 4`, `state_mutation: 1484`, `fragile_debt: 9`, `unreferenced_by_name: 3`
* *Architecture:* `io: 12`, `api: 20`, `import: 34`
* *Defense:* `safety: 9`, `test: 3`, `immutability_locks: 35`, `cleanup: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` ata_all.h, cam.h, cam_ccb.h, cam_debug.h, mmc_all.h, scsi_all.h, scsi_da.h, scsi_message.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/amd64/amd64/pmap.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10209.52 | **LOC:** 12332 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (74.3724%), Tech Debt (8.4731%)
**Top Internal Functions/Classes:**
  * `pmap_enter` (Impact: 204.1)
    * *Intent:* * the specified virtual address (v) in the * target physical map with the protection requested. * * ...
  * `pmap_change_props_locked` (Impact: 149.2)
  * `pmap_enter_pde` (Impact: 117.9)
    * *Intent:* * KERN_FAILURE if either (1) PMAP_ENTER_NOREPLACE was specified and a 4KB * page mapping already exi...
  * `pmap_copy` (Impact: 102.4)
    * *Intent:* /* * Copy the range specified by src_addr/len * from the source map to the range dst_addr/len * in t...
  * `pmap_enter_quick_locked` (Impact: 90.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 1779 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 5551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1741`, `structural_boundaries: 1313`, `args: 552`, `func_start: 307`, `class_start: 143`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 1993`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 6`
* *Architecture:* `api: 161`, `concurrency: 13`, `import: 59`
* *Defense:* `safety: 3`, `doc: 8`, `sync_locks: 21`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` ddb.h, asan.h, cpu.h, cputypes.h, intr_machdep.h, md_var.h, msan.h, pcb.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/fs/nfsserver/nfs_nfsdport.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9654.12 | **LOC:** 7622 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (79.8057%), Tech Debt (23.0639%)
**Top Internal Functions/Classes:**
  * `nfsrvd_readdirplus` (Impact: 371.3)
    * *Intent:* /* * Readdirplus for V3 and Readdir for V4. */
  * `nfsv4_sattr` (Impact: 340.8)
    * *Intent:* /* * Handle the setable attributes for V4. * Returns NFSERR_BADXDR if it can't be parsed, 0 otherwis...
  * `nfsrv_dsgetsockmnt` (Impact: 326.8)
    * *Intent:* /* * Get the DS mount point, fh and directory from the "pnfsd.dsfile" extended * attribute. * newnmp...
  * `nfsrv_proxyds` (Impact: 208.0)
  * `nfsvno_open` (Impact: 164.5)
    * *Intent:* /* * Do the vnode op stuff for Open. Similar to nfsvno_createsub(), but * must handle nfsrv_openchec...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 126 instances
* *Amplified Cascading Flux:* 1544 instances
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 4794
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1554`, `structural_boundaries: 943`, `args: 210`, `func_start: 106`, `class_start: 275`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 1706`, `planned_debt: 2`, `fragile_debt: 7`, `unreferenced_by_name: 39`
* *Architecture:* `api: 85`, `import: 13`
* *Defense:* `safety: 3`, `test: 7`, `immutability_locks: 3`, `cleanup: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` nfsport.h, nlm.h, nlm_prot.h, mac_framework.h, callout.h, capsicum.h, extattr.h, filio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/fs/nfs/nfs_commonsubs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9633.98 | **LOC:** 5610 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (97.8007%), Tech Debt (19.6047%)
**Top Internal Functions/Classes:**
  * `nfsv4_loadattr` (Impact: 2574.7)
    * *Intent:* /* * Get the attributes for V4. * If the compare flag is true, test for any attribute changes, * oth...
  * `nfsv4_fillattr` (Impact: 1000.2)
    * *Intent:* /* * Fill in the attributes as marked by the bitmap (V4). */
  * `nfscl_reqstart` (Impact: 163.5)
    * *Intent:* /* * Start building a request. Mostly just put the first file handle in * place. */
  * `nfscl_fillsattr` (Impact: 141.6)
    * *Intent:* /* * Fill in the setable attributes. The full argument indicates whether * to fill in them all or ju...
  * `nfssvc_idname` (Impact: 139.9)
    * *Intent:* /* * This function is called from the nfssvc(2) system call, to update the * kernel user/group name ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 53 instances
* *Amplified Race Conditions:* 27 instances
* *Amplified Cascading Flux:* 1359 instances
* *Concurrency (weighted view):* 162
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 4120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1391`, `structural_boundaries: 526`, `args: 211`, `func_start: 59`, `class_start: 80`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1402`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 30`
* *Architecture:* `api: 56`, `concurrency: 27`, `import: 8`
* *Defense:* `sync_locks: 59`, `immutability_locks: 3`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` nfsport.h, nfsmount.h, opt_inet.h, opt_inet6.h, mac_framework.h, cdefs.h, extattr.h, vm_param.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/bxe/bxe_elink.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9537.0 | **LOC:** 15119 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.7752%), Tech Debt (10.0759%)
**Top Internal Functions/Classes:**
  * `elink_set_led` (Impact: 101.4)
  * `elink_link_update` (Impact: 96.7)
    * *Intent:* /* The elink_link_update function should be called upon link * interrupt. * Link is considered up as...
  * `elink_populate_ext_phy` (Impact: 88.4)
  * `elink_get_link_speed_duplex` (Impact: 81.3)
  * `elink_848x3_config_init` (Impact: 80.7)
    * *Intent:* #define PHY84833_CONSTANT_LATENCY 1193
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1358 instances
* *State Mutation (weighted view):* 4347
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1850`, `structural_boundaries: 1548`, `args: 384`, `func_start: 281`, `class_start: 456`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1631`, `dead_code: 5`, `fragile_debt: 2`, `unreferenced_by_name: 21`
* *Architecture:* `api: 31`, `import: 7`
* *Defense:* `doc: 79`, `immutability_locks: 90`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` bxe.h, bxe_elink.h, ecore_fw_defs.h, ecore_hsi.h, ecore_mfw_req.h, ecore_reg.h, cdefs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netpfil/ipfilter/netinet/fil.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9347.64 | **LOC:** 10060 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (94.1075%), Tech Debt (22.0599%)
**Top Internal Functions/Classes:**
  * `ipf_checkl4sum` (Impact: 955.9)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* Function: ipf_chec...
  * `frrequest` (Impact: 568.2)
    * *Intent:* /* Parameters: unit(I) - device for which this is for */ /* req(I) - ioctl command (SIOC*) */ /* dat...
  * `ipf_ipf_ioctl` (Impact: 230.9)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* Function: ipf_ipf_...
  * `ipf_scanlist` (Impact: 126.3)
    * *Intent:* /* Returns: int - result flags of scanning filter list */ /* Parameters: fin(I) - pointer to packet ...
  * `ipf_ipftune` (Impact: 102.3)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* Function: ipf_tune...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1459 instances
* *State Mutation (weighted view):* 4510
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1686`, `structural_boundaries: 869`, `args: 310`, `func_start: 154`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 1592`, `dead_code: 15`, `planned_debt: 1`, `fragile_debt: 7`, `unreferenced_by_name: 41`
* *Architecture:* `api: 103`, `import: 51`
* *Defense:* `safety: 16`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` ipf.h, ipt.h, af.h, bpf.h, if.h, icmp6.h, in.h, in_systm.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/fs/nfsserver/nfs_nfsdstate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9139.76 | **LOC:** 9058 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (78.676%), Tech Debt (18.2011%)
**Top Internal Functions/Classes:**
  * `nfsrv_lockctrl` (Impact: 640.8)
    * *Intent:* /* * Lock control function called to update lock status. * Returns 0 upon success, -1 if there is no...
  * `nfsrv_openctrl` (Impact: 390.2)
    * *Intent:* /* * Open control function to create/update open state for an open. */
  * `nfsrv_getclient` (Impact: 270.5)
    * *Intent:* /* * Check to see if the client id exists and optionally confirm it. */
  * `nfsrv_opencheck` (Impact: 170.9)
    * *Intent:* /* * Check for state errors for Open. * repstat is passed back out as an error if more critical erro...
  * `nfsrv_mdscopymr` (Impact: 168.6)
    * *Intent:* /* * Look up the MDS file shared locked, and then get the extended attribute * to find the extant DS...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 77 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1328 instances
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 4244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1563`, `structural_boundaries: 931`, `args: 275`, `func_start: 119`, `class_start: 243`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1588`, `fragile_debt: 3`, `unreferenced_by_name: 38`
* *Architecture:* `api: 69`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 2`, `test: 11`, `sync_locks: 2`, `immutability_locks: 2`, `cleanup: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` nfsport.h, opt_inet.h, opt_inet6.h, cdefs.h, extattr.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/fs/nfsserver/nfs_nfsdserv.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 8967.06 | **LOC:** 6703 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.646%), Tech Debt (31.4919%)
**Top Internal Functions/Classes:**
  * `nfsrvd_open` (Impact: 517.8)
    * *Intent:* /* * nfsv4 open service */
  * `nfsrvd_setattr` (Impact: 231.0)
    * *Intent:* /* * nfs setattr service */
  * `nfsrvd_read` (Impact: 166.8)
    * *Intent:* /* * nfs read service */
  * `nfsrvd_clone` (Impact: 163.6)
    * *Intent:* /* * nfs clone service */
  * `nfsrvd_mknod` (Impact: 159.9)
    * *Intent:* /* * nfs v3 mknod service (and v4 create) */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 50 instances
* *Amplified Cascading Flux:* 1459 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 4700
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1512`, `structural_boundaries: 538`, `args: 276`, `func_start: 64`, `class_start: 151`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1782`, `fragile_debt: 2`, `unreferenced_by_name: 62`
* *Architecture:* `api: 77`, `import: 6`
* *Defense:* `safety: 4`, `cleanup: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` nfsport.h, opt_inet.h, opt_inet6.h, cdefs.h, extattr.h, filio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/ocs_fc/ocs_hw.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 8558.96 | **LOC:** 12703 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.2159%), Tech Debt (32.641%)
**Top Internal Functions/Classes:**
  * `ocs_hw_get` (Impact: 212.3)
  * `ocs_hw_io_send` (Impact: 176.2)
    * *Intent:* * @param type Type of IO (target read, target response, and so on). * @param io Previously-allocated...
  * `ocs_hw_init` (Impact: 159.4)
    * *Intent:* * @ingroup devInitShutdown * @brief Allocate memory structures to prepare for the device operation. ...
  * `ocs_hw_set` (Impact: 157.1)
  * `ocs_hw_srrs_send` (Impact: 148.4)
    * *Intent:* * * @param hw Hardware context. * @param type Type of sequence (ELS request/response, FC-CT). * @par...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1228 instances
* *State Mutation (weighted view):* 3842
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1747`, `structural_boundaries: 1188`, `args: 323`, `func_start: 225`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 1386`, `dead_code: 18`, `planned_debt: 5`, `fragile_debt: 19`, `unreferenced_by_name: 64`
* *Architecture:* `api: 114`, `import: 4`
* *Defense:* `safety: 2`, `doc: 179`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ocs.h, ocs_hw.h, ocs_hw_queues.h, ocs_os.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/arm64/arm64/pmap.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 8519.14 | **LOC:** 10232 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (75.3533%), Tech Debt (8.3511%)
**Top Internal Functions/Classes:**
  * `pmap_enter` (Impact: 260.8)
    * *Intent:* /* * Insert the given physical page (p) at * the specified virtual address (v) in the * target physi...
  * `pmap_change_props_locked` (Impact: 131.9)
  * `pmap_enter_l2` (Impact: 123.4)
    * *Intent:* /* * Tries to create the specified L2 page mapping. Returns KERN_SUCCESS if * the mapping was create...
  * `pmap_enter_quick_locked` (Impact: 119.1)
  * `pmap_enter_l3c` (Impact: 114.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 1388 instances
* *Concurrency (weighted view):* 61
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 4298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1481`, `structural_boundaries: 1072`, `args: 487`, `func_start: 212`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 1522`, `planned_debt: 5`, `fragile_debt: 3`
* *Architecture:* `api: 135`, `concurrency: 11`, `import: 49`
* *Defense:* `safety: 3`, `doc: 7`, `sync_locks: 17`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` asan.h, cpu_feat.h, elf.h, ifunc.h, machdep.h, md_var.h, pcb.h, opt_vm.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netpfil/ipfilter/netinet/ip_nat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 8464.84 | **LOC:** 8417 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (78.7591%), Tech Debt (12.2684%)
**Top Internal Functions/Classes:**
  * `ipf_nat_ioctl` (Impact: 353.8)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* Function: ipf_nat_...
  * `ipf_nat_inlookup` (Impact: 202.1)
    * *Intent:* /* mapdst(I) - destination IP address */ /* */ /* Lookup a nat entry based on the mapped destination...
  * `ipf_nat_outlookup` (Impact: 191.8)
    * *Intent:* /* rw(I) - 1 == write lock on held, 0 == read lock. */ /* */ /* Lookup a nat entry based on the sour...
  * `ipf_nat_matcharray` (Impact: 151.1)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* Function: ipf_nat_...
  * `ipf_nat_newmap` (Impact: 148.5)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* Function: ipf_nat_...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1464 instances
* *State Mutation (weighted view):* 4499
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1621`, `structural_boundaries: 570`, `args: 181`, `func_start: 80`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 68`, `state_mutation: 1571`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 3`, `unreferenced_by_name: 15`
* *Architecture:* `api: 46`, `import: 51`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` md5.h, af.h, if.h, if_var.h, in.h, in_systm.h, ip.h, ip_compat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/pms/RefTisa/sat/src/smsatcb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 8329.3 | **LOC:** 13769 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.4261%), Tech Debt (11.1689%)
**Top Internal Functions/Classes:**
  * `smsatLogSenseCB` (Impact: 282.8)
  * `smsatDelayedProcessAbnormalCompletion` (Impact: 272.7)
  * `smsatProcessAbnormalCompletion` (Impact: 266.9)
  * `smsatStartStopUnitCB` (Impact: 204.0)
  * `smsatRequestSenseCB` (Impact: 193.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 772 instances
* *State Mutation (weighted view):* 2886
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1558`, `structural_boundaries: 649`, `args: 80`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 240`, `state_mutation: 1342`, `dead_code: 46`, `unreferenced_by_name: 47`
* *Architecture:* `api: 60`, `import: 15`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` sa.h, saapi.h, saosapi.h, sm.h, smapi.h, tdsmapi.h, smdefs.h, smproto.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/sound/pci/hda/hdaa.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 8082.08 | **LOC:** 7175 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.9737%), Tech Debt (8.5893%)
**Top Internal Functions/Classes:**
  * `hdaa_audio_trace_dac` (Impact: 131.3)
    * *Intent:* /* * Trace path from DAC to pin. */
  * `hdaa_audio_trace_adc` (Impact: 130.6)
    * *Intent:* /* * Trace path from widget to ADC. */
  * `hdaa_audio_ctl_source_amp` (Impact: 110.0)
    * *Intent:* /* * Find controls to control amplification for source and calculate possible * amplification range....
  * `hdaa_pcmchannel_setup` (Impact: 107.7)
  * `hdaa_audio_ctl_dest_amp` (Impact: 97.8)
    * *Intent:* /* * Find controls to control amplification for destination and calculate * possible amplification r...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 1394 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 4269
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1805`, `structural_boundaries: 857`, `args: 177`, `func_start: 128`, `class_start: 177`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1481`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 5`
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 29`, `doc: 2`, `sync_locks: 2`, `immutability_locks: 30`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` hda_reg.h, hdaa.h, hdac.h, sound.h, mixer_if.h, opt_snd.h, ctype.h, taskqueue.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/cxgbe/common/t4_hw.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 8059.08 | **LOC:** 13642 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (54.7778%), Tech Debt (37.3696%)
**Top Internal Functions/Classes:**
  * `t4_wr_mbox_meat_timeout` (Impact: 105.2)
    * *Intent:* * store the FW's reply to the command. The command and its optional * reply are of the same length. ...
  * `t4_link_l1cfg` (Impact: 73.6)
    * *Intent:* /** * t4_link_l1cfg - apply link configuration to MAC/PHY * @phy: the PHY to setup * @mac: the MAC t...
  * `sge_intr_handler` (Impact: 63.0)
    * *Intent:* /* * SGE interrupt handler. */
  * `t4_fw_hello` (Impact: 62.1)
    * *Intent:* /** * t4_fw_hello - establish communication with FW * @adap: the adapter * @mbox: mailbox to use for...
  * `t4_filter_field_shift` (Impact: 58.4)
    * *Intent:* /** * t4_filter_field_shift - calculate filter field shift * @adap: the adapter * @filter_sel: the d...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1316 instances
* *State Mutation (weighted view):* 4363
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1092`, `structural_boundaries: 1209`, `args: 663`, `func_start: 256`, `class_start: 113`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1731`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 129`
* *Architecture:* `api: 191`, `import: 8`
* *Defense:* `safety: 21`, `doc: 164`, `test: 1`, `immutability_locks: 253`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` common.h, t4fw_interface.h, opt_inet.h, cdefs.h, eventhandler.h, param.h, t4_regs.h, t4_regs_values.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `sys/dev/acpica/acpi.c` -> Churn: **100.0%** | Cog Load: 73.524% | Debt: 44.1668%
- `sys/x86/cpufreq/hwpstate_amd.c` -> Churn: **96.38%** | Cog Load: 72.7009% | Debt: 9.3451%
- `sys/compat/linuxkpi/common/src/linux_80211.c` -> Churn: **92.76%** | Cog Load: 73.6069% | Debt: 53.8765%
- `sys/dev/asmc/asmc.c` -> Churn: **86.74%** | Cog Load: 60.3744% | Debt: 0.0%
- `sys/dev/vmm/vmm_dev.c` -> Churn: **80.19%** | Cog Load: 68.9217% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `sys/fs/nfsclient/nfs_clrpcops.c` -> **Rick Macklem** (90.9% isolated ownership) | Magnitude: 15838.1
- `sys/netinet/tcp_stacks/bbr.c` -> **Randall Stewart** (100.0% isolated ownership) | Magnitude: 14663.14
- `sys/netinet/sctp_output.c` -> **Gleb Smirnoff** (100.0% isolated ownership) | Magnitude: 14649.16
- `sys/cam/ctl/ctl.c` -> **Gordon Bergling** (100.0% isolated ownership) | Magnitude: 12402.26
- `sys/amd64/amd64/pmap.c` -> **Konstantin Belousov** (100.0% isolated ownership) | Magnitude: 10209.52

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `contrib/llvm-project/libcxx/include/__functional/hash.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 98.8205%)
- `contrib/llvm-project/libcxx/include/__algorithm/stable_sort.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9999%)
- `contrib/llvm-project/libcxx/include/__pstl/cpu_algos/find_if.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.1896%)
- `contrib/llvm-project/llvm/include/llvm/ADT/DenseMap.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 95.7543%)
- `contrib/llvm-project/lldb/include/lldb/Interpreter/CommandInterpreter.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 67.8321%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `contrib/llvm-project/llvm/include/llvm/ADT/SmallVector.h` -> **Severity: 224.611** (Blast Radius: 3.199 * Doc Risk: 70.2128%)
- `contrib/llvm-project/llvm/include/llvm/ADT/iterator_range.h` -> **Severity: 218.9** (Blast Radius: 2.189 * Doc Risk: 100.0%)
- `sys/sys/malloc.h` -> **Severity: 215.8** (Blast Radius: 2.158 * Doc Risk: 100.0%)
- `sys/sys/bus.h` -> **Severity: 207.3** (Blast Radius: 2.073 * Doc Risk: 100.0%)
- `contrib/llvm-project/llvm/include/llvm/ADT/ArrayRef.h` -> **Severity: 194.8** (Blast Radius: 1.948 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
