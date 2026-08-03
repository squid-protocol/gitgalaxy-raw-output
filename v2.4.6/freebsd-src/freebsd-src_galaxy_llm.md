# ARCHITECTURAL_BRIEF: freebsd-src
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/freebsd-src` |
| **Timestamp** | `2026-08-03T20:54:03.180810+00:00` |
| **Scan Duration** | `2265.25s` |
| **Git Branch** | `main` |
| **Git Commit** | `c70755bc0d8f703dbaa1520c15e8213a95847dd5` |
| **Git Remote** | `https://github.com/freebsd/freebsd-src.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 53637 malicious artifacts.

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
| Total Artifacts | 109673 |
| Analyzed Artifacts (Scanned) | 68804 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 40869 |
| Total LOC | 11215038 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 62.7% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1528 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3193 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 37656 | 8963163 | 54.7% |
| PLAINTEXT | 7544 | 366 | 11.0% |
| MAKEFILE | 5615 | 192833 | 8.2% |
| SHELL | 5584 | 323469 | 8.1% |
| YAML | 5207 | 432636 | 7.6% |
| CPP | 3278 | 588733 | 4.8% |
| PERL | 1441 | 344429 | 2.1% |
| M4 | 944 | 144791 | 1.4% |
| MARKDOWN | 458 | 0 | 0.7% |
| ASSEMBLY | 301 | 83799 | 0.4% |
| PYTHON | 214 | 32135 | 0.3% |
| HTML | 109 | 30631 | 0.2% |
| TD | 108 | 46627 | 0.2% |
| XML | 62 | 49 | 0.1% |
| LUA | 55 | 6995 | 0.1% |
| CSHARP | 33 | 3509 | 0.0% |
| YACC | 32 | 5056 | 0.0% |
| JSON | 29 | 2062 | 0.0% |
| BINARY_THREAT | 26 | 26 | 0.0% |
| PHP | 16 | 203 | 0.0% |
| CSS | 16 | 2390 | 0.0% |
| BATCH | 14 | 1133 | 0.0% |
| RUBY | 14 | 854 | 0.0% |
| JAVA | 13 | 2070 | 0.0% |
| TCL | 12 | 5389 | 0.0% |
| SQLITE | 11 | 1272 | 0.0% |
| POWERSHELL | 3 | 166 | 0.0% |
| MATLAB | 3 | 85 | 0.0% |
| PROTO | 2 | 99 | 0.0% |
| FORTRAN | 2 | 4 | 0.0% |
| DOCKERFILE | 1 | 11 | 0.0% |
| JAVASCRIPT | 1 | 53 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.275`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 40341 | 58.6% |
| file_cluster_13 | 16944 | 24.6% |
| file_cluster_9 | 1492 | 2.2% |
| file_cluster_4 | 795 | 1.2% |
| file_cluster_12 | 448 | 0.7% |
| Unknown | 381 | 0.6% |
| file_cluster_0 | 159 | 0.2% |
| file_cluster_17 | 124 | 0.2% |
| file_cluster_7 | 118 | 0.2% |
| file_cluster_6 | 111 | 0.2% |
| file_cluster_11 | 105 | 0.2% |
| file_cluster_16 | 83 | 0.1% |
| file_cluster_2 | 9 | 0.0% |
| file_cluster_1 | 3 | 0.0% |
| file_cluster_15 | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7682 | 11.2% |
| Static: Minified & Vendor Opaque Mass | 7 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 40869*

**Composition by Extension & Reason:**
- `.c`: 5373x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded: Neighborhood Micro-Mass Limit Exceeded, 4x Excluded (Machine-Generated Source Code Signature: 57 LOC)
- `no_extension`: 2341x Unsupported Format (.undeterminable), 1018x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 271x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.cpp`: 4117x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1350 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2691 LOC)
- `.h`: 3603x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 60x Excluded: Neighborhood Micro-Mass Limit Exceeded, 24x Excluded (Machine-Generated Source Code Signature: 28 LOC)
- `.3`: 2278x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3824 LOC), 1x Excluded (Machine-Generated Source Code Signature: 121 LOC)
- `.depend`: 1173x Excluded (Unsupported Extension: '.depend'), 411x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.out`: 1128x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.d`: 1065x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 32x Excluded: Neighborhood Micro-Mass Limit Exceeded, 8x Unsupported Format (.d)
- `.src`: 940x Excluded (Unsupported Extension: '.src')
- `.t`: 576x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 70x Unsupported Format (.undeterminable), 24x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.s`: 487x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Machine-Generated Source Code Signature: 1877 LOC), 3x Excluded (Machine-Generated Source Code Signature: 1480 LOC)
- `.sh`: 566x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 60x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 102 LOC)
- `.json`: 578x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3668 LOC), 1x Excluded (Massive Static Asset Blob: 7730 LOC)
- `.td`: 531x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 2638 commas in 821 LOC), 1x Excluded (Embedded Array/Matrix Payload: 8044 commas in 2404 LOC)
- `.bc`: 532x Unsupported Format (.bc), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 34.1 | 15.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 31.5 | 17.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 18.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.8 | 2.3 | 2.3 |
| API Exposure | 0.0 | 20.0 | 5.2 | 3.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 50.2 | 54.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 91.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 50.6 | 41.5 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 17.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.5 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `usr.sbin/freebsd-update/freebsd-update.sh` (Hits: 1245)
- `contrib/lua/doc/contents.html` (Hits: 1094)
- `tests/sys/netinet6/frag6/frag6_05.sh` (Hits: 752)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **code.c** (`crypto/krb5/src/lib/krad/code.c`) — 1514 inbound connections
2. **k5-int.h** (`crypto/krb5/src/include/k5-int.h`) — 408 inbound connections
3. **syslog.h** (`sys/sys/syslog.h`) — 356 inbound connections
4. **inner.h** (`contrib/bearssl/src/inner.h`) — 288 inbound connections
5. **atf-c.h** (`contrib/atf/atf-c.h`) — 236 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **env.c** (`stand/efi/libefi/env.c`) — 99 outbound dependencies
2. **nfsport.h** (`sys/fs/nfs/nfsport.h`) — 90 outbound dependencies
3. **ClangExpressionParser.cpp** (`contrib/llvm-project/lldb/source/Plugins/ExpressionParser/Clang/ClangExpressionParser.cpp`) — 80 outbound dependencies
4. **freebsd32_misc.c** (`sys/compat/freebsd32/freebsd32_misc.c`) — 79 outbound dependencies
5. **ProcessGDBRemote.cpp** (`contrib/llvm-project/lldb/source/Plugins/Process/gdb-remote/ProcessGDBRemote.cpp`) — 79 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `inheritsFrom` (@ `contrib/llvm-project/llvm/utils/TableGen/X86DisassemblerTables.cpp`) -> Impact: **12063.1** | LOC: 498
  * *Intent:* /// inheritsFrom - Indicates whether all instructions in one class also belong /// to another class. /// /// @param child - The class that may be the ...
- `printInst` (@ `contrib/llvm-project/llvm/tools/llvm-objdump/llvm-objdump.cpp`) -> Impact: **10673.6** | LOC: 1539
- `warn` (@ `contrib/llvm-project/llvm/tools/llvm-nm/llvm-nm.cpp`) -> Impact: **7665.9** | LOC: 1559
- `FoldCondBranchOnValueKnownInPredecessorI` (@ `contrib/llvm-project/llvm/lib/Transforms/Utils/SimplifyCFG.cpp`) -> Impact: **6605.7** | LOC: 1886
- `sigchld` (@ `contrib/ntp/scripts/monitoring/ntploopwatch`) -> Impact: **5953.4** | LOC: 1462
  * *Intent:* ;# stop operation if plot command dies
- `process_server_config_line_depth` (@ `crypto/openssh/servconf.c`) -> Impact: **5701.6** | LOC: 1621
- `pf_insert_src_node` (@ `sys/netpfil/pf/pf.c`) -> Impact: **5527.1** | LOC: 2013
- `rsa_setup_md` (@ `crypto/openssl/providers/implementations/signature/rsa_sig.c`) -> Impact: **5043.8** | LOC: 1238
- `nfsv4_loadattr` (@ `sys/fs/nfs/nfs_commonsubs.c`) -> Impact: **5005.8** | LOC: 1958
  * *Intent:* { 0, 0, 0, 0, LK_EXCLUSIVE, 1, 1 }, /* RestoreFH */ { 0, 1, 0, 0, LK_EXCLUSIVE, 1, 1 }, /* SaveFH */ { 0, 1, 0, 0, LK_EXCLUSIVE, 1, 1 }, /* SecInfo */...
- `header_common` (@ `contrib/libarchive/libarchive/archive_read_support_format_tar.c`) -> Impact: **4869.7** | LOC: 1466

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `all-math` (@ `contrib/arm-optimized-routines/math/Dir.mk`) -> **O(2^N) [Recursive]**
- `bc_num_cmp` (@ `contrib/bc/src/num.c`) -> **O(2^N) [Recursive]**
- `test_alloc_dtd_copy_default_atts` (@ `contrib/expat/tests/alloc_tests.c`) -> **O(2^N) [Recursive]**
- `_XML_Parse_SINGLE_BYTES` (@ `contrib/expat/tests/common.c`) -> **O(2^N) [Recursive]**
- `ldns_dname2buffer_wire_compress` (@ `contrib/ldns/host2wire.c`) -> **O(2^N) [Recursive]**
  * *Intent:* /* * host2wire.c * * conversion routines from the host to the wire format. * This will usually just a re-ordering of the * data (as we store it in net...
- `ldns_pkt_push_rr` (@ `contrib/ldns/packet.c`) -> **O(2^N) [Recursive]**
- `make_table_recurse` (@ `contrib/libarchive/libarchive/archive_read_support_format_rar.c`) -> **O(2^N) [Recursive]**
- `archive_read_support_format_rar` (@ `contrib/libarchive/libarchive/archive_read_support_format_rar.c`) -> **O(2^N) [Recursive]**
- `cbor_to_cjson` (@ `contrib/libcbor/examples/cbor2cjson.c`) -> **O(2^N) [Recursive]**
  * *Intent:* /* * Copyright (c) 2014-2020 Pavel Kalvoda <me@pavelkalvoda.com> * * libcbor is free software; you can redistribute it and/or modify * it under the te...
- `cjson_cbor_stream_decode` (@ `contrib/libcbor/examples/cjson2cbor.c`) -> **O(2^N) [Recursive]**
  * *Intent:* /* Context stack */

### Highest Data Gravity (Database Complexity)
- `usage_[Truncated]` (@ `usr.sbin/freebsd-update/freebsd-update.sh`) -> DB Complexity: **3973**
  * *Intent:* # ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY # DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL # DAMAGES (INCLU...
- `frag6_05_check_stats_0_[Truncated]` (@ `tests/sys/netinet6/frag6/frag6_05.sh`) -> DB Complexity: **2280**
- `usage_[Truncated]` (@ `contrib/bc/configure`) -> DB Complexity: **1491**
  * *Intent:* # Simply prints the help message and quits based on the argument. # @param msg The help message to print.
- `usage_[Truncated]` (@ `contrib/bc/configure.sh`) -> DB Complexity: **1491**
  * *Intent:* # Simply prints the help message and quits based on the argument. # @param msg The help message to print.
- `Anonymous_Block_[Truncated]` (@ `contrib/netbsd-tests/bin/sh/t_redir.sh`) -> DB Complexity: **1421**
- `Anonymous_Block_[Truncated]` (@ `tests/sys/netpfil/pf/counters.sh`) -> DB Complexity: **1271**
- `frag6_06_check_stats_0_[Truncated]` (@ `tests/sys/netinet6/frag6/frag6_06.sh`) -> DB Complexity: **1132**
- `frag6_15_check_stats_[Truncated]` (@ `tests/sys/netinet6/frag6/frag6_15.sh`) -> DB Complexity: **1132**
- `frag6_01_check_stats_[Truncated]` (@ `tests/sys/netinet6/frag6/frag6_01.sh`) -> DB Complexity: **1131**
- `frag6_02_check_stats_[Truncated]` (@ `tests/sys/netinet6/frag6/frag6_02.sh`) -> DB Complexity: **1131**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `secure/caroot/trusted` | 151 | 750008.22 | 0.03% | 0.0% |
| `secure/caroot/untrusted` | 43 | 210008.22 | 0.12% | 0.0% |
| `sys/kern` | 239 | 165088.42 | 70.7% | 44.17% |
| `crypto/openssh/regress/unittests/hostkeys/testdata` | 30 | 150000.0 | 0.0% | 0.0% |
| `crypto/openssh/regress/unittests/sshkey/testdata` | 25 | 125000.0 | 0.0% | 0.0% |
| `crypto/openssl/apps` | 79 | 110835.89 | 65.15% | 8.23% |
| `sys/netinet` | 145 | 85462.77 | 43.9% | 17.02% |
| `crypto/openssh/regress/misc/fuzz-harness/testdata` | 18 | 80000.02 | 5.56% | 5.56% |
| `crypto/openssh/regress/unittests/sshsig/testdata` | 14 | 70000.0 | 0.0% | 0.0% |
| `sys/dev/qlnx/qlnxe` | 101 | 66289.21 | 22.63% | 11.49% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cddl/lib/libctf/Makefile` -> **100.0%** Exposure
- `cddl/lib/libdtrace/Makefile` -> **100.0%** Exposure
- `cddl/lib/libnvpair/Makefile` -> **100.0%** Exposure
- `cddl/lib/libzdb/Makefile` -> **100.0%** Exposure
- `cddl/lib/libzfs/Makefile` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Makefile.sys.inc` -> **100.0%** Exposure
- `bin/ls/Makefile` -> **100.0%** Exposure
- `cddl/lib/libavl/Makefile` -> **100.0%** Exposure
- `cddl/lib/libdtrace/Makefile` -> **100.0%** Exposure
- `cddl/lib/libzdb/Makefile` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sys/dev/aq/aq_hw_llh.c` -> **246** Orphaned Functions | **0** Duplicates
- `contrib/kyua/store/testdata_v2.sql` -> **0** Orphaned Functions | **211** Duplicates
- `crypto/openssh/libcrux_mlkem768_sha3.h` -> **0** Orphaned Functions | **159** Duplicates
- `sys/contrib/dev/ath/ath_hal/ar9300/ar9300_stub_funcs.c` -> **150** Orphaned Functions | **0** Duplicates
- `contrib/llvm-project/clang/utils/TableGen/ClangAttrEmitter.cpp` -> **20** Orphaned Functions | **123** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`bin/cat/cat.c`** -> AI Confidence: **99.48%**
2. **`bin/chflags/chflags.c`** -> AI Confidence: **99.48%**
3. **`bin/chmod/chmod.c`** -> AI Confidence: **99.48%**
4. **`bin/cpuset/cpuset.c`** -> AI Confidence: **99.48%**
5. **`bin/dd/dd.c`** -> AI Confidence: **99.48%**
6. **`bin/dd/position.c`** -> AI Confidence: **99.48%**
7. **`bin/echo/echo.c`** -> AI Confidence: **99.48%**
8. **`bin/kenv/kenv.c`** -> AI Confidence: **99.48%**
9. **`bin/ls/ls.c`** -> AI Confidence: **99.48%**
10. **`bin/ls/util.c`** -> AI Confidence: **99.48%**
11. **`bin/mkdir/mkdir.c`** -> AI Confidence: **99.48%**
12. **`bin/pax/ar_subs.c`** -> AI Confidence: **99.48%**
13. **`bin/pax/gen_subs.c`** -> AI Confidence: **99.48%**
14. **`bin/pax/options.c`** -> AI Confidence: **99.48%**
15. **`bin/pax/pax.c`** -> AI Confidence: **99.48%**
16. **`bin/pax/tar.c`** -> AI Confidence: **99.48%**
17. **`bin/pkill/pkill.c`** -> AI Confidence: **99.48%**
18. **`bin/pkill/tests/spin_helper.c`** -> AI Confidence: **99.48%**
19. **`bin/ps/fmt.c`** -> AI Confidence: **99.48%**
20. **`bin/rm/rm.c`** -> AI Confidence: **99.48%**
21. **`bin/setfacl/setfacl.c`** -> AI Confidence: **99.48%**
22. **`bin/sh/arith_yylex.c`** -> AI Confidence: **99.48%**
23. **`bin/sh/cd.c`** -> AI Confidence: **99.48%**
24. **`bin/sh/expand.c`** -> AI Confidence: **99.48%**
25. **`bin/sh/histedit.c`** -> AI Confidence: **99.48%**
26. **`bin/sh/mail.c`** -> AI Confidence: **99.48%**
27. **`bin/sh/miscbltin.c`** -> AI Confidence: **99.48%**
28. **`bin/sh/options.c`** -> AI Confidence: **99.48%**
29. **`bin/sh/show.c`** -> AI Confidence: **99.48%**
30. **`bin/sh/trap.c`** -> AI Confidence: **99.48%**
31. **`bin/stty/stty.c`** -> AI Confidence: **99.48%**
32. **`bin/timeout/timeout.c`** -> AI Confidence: **99.48%**
33. **`bin/uuidgen/uuidgen.c`** -> AI Confidence: **99.48%**
34. **`cddl/contrib/opensolaris/tools/ctf/cvt/ctfconvert.c`** -> AI Confidence: **99.48%**
35. **`cddl/contrib/opensolaris/tools/ctf/cvt/output.c`** -> AI Confidence: **99.48%**
36. **`contrib/bc/src/args.c`** -> AI Confidence: **99.48%**
37. **`contrib/bc/src/bc_parse.c`** -> AI Confidence: **99.48%**
38. **`contrib/bc/src/main.c`** -> AI Confidence: **99.48%**
39. **`contrib/bearssl/tools/chain.c`** -> AI Confidence: **99.48%**
40. **`contrib/bearssl/tools/client.c`** -> AI Confidence: **99.48%**
41. **`contrib/bearssl/tools/keys.c`** -> AI Confidence: **99.48%**
42. **`contrib/bearssl/tools/server.c`** -> AI Confidence: **99.48%**
43. **`contrib/bearssl/tools/skey.c`** -> AI Confidence: **99.48%**
44. **`contrib/bearssl/tools/sslio.c`** -> AI Confidence: **99.48%**
45. **`contrib/bearssl/tools/twrch.c`** -> AI Confidence: **99.48%**
46. **`contrib/bearssl/tools/verify.c`** -> AI Confidence: **99.48%**
47. **`contrib/blocklist/bin/blacklistctl.c`** -> AI Confidence: **99.48%**
48. **`contrib/blocklist/bin/blocklistctl.c`** -> AI Confidence: **99.48%**
49. **`contrib/blocklist/port/fparseln.c`** -> AI Confidence: **99.48%**
50. **`contrib/blocklist/port/strlcat.c`** -> AI Confidence: **99.48%**
51. **`contrib/blocklist/port/strlcpy.c`** -> AI Confidence: **99.48%**
52. **`contrib/blocklist/port/strtoi.c`** -> AI Confidence: **99.48%**
53. **`contrib/bmake/dirname.c`** -> AI Confidence: **99.48%**
54. **`contrib/bmake/realpath.c`** -> AI Confidence: **99.48%**
55. **`contrib/bsddialog/utility/util_cli.c`** -> AI Confidence: **99.48%**
56. **`contrib/bsnmp/snmp_mibII/mibII_ip.c`** -> AI Confidence: **99.48%**
57. **`contrib/byacc/main.c`** -> AI Confidence: **99.48%**
58. **`contrib/dialog/ui_getc.c`** -> AI Confidence: **99.48%**
59. **`contrib/dma/conf.c`** -> AI Confidence: **99.48%**
60. **`contrib/dma/dma-mbox-create.c`** -> AI Confidence: **99.48%**
61. **`contrib/dma/local.c`** -> AI Confidence: **99.48%**
62. **`contrib/dma/mail.c`** -> AI Confidence: **99.48%**
63. **`contrib/elftoolchain/addr2line/addr2line.c`** -> AI Confidence: **99.48%**
64. **`contrib/elftoolchain/ar/ar.c`** -> AI Confidence: **99.48%**
65. **`contrib/elftoolchain/ar/read.c`** -> AI Confidence: **99.48%**
66. **`contrib/elftoolchain/elfcopy/binary.c`** -> AI Confidence: **99.48%**
67. **`contrib/elftoolchain/elfcopy/main.c`** -> AI Confidence: **99.48%**
68. **`contrib/elftoolchain/elfcopy/pe.c`** -> AI Confidence: **99.48%**
69. **`contrib/elftoolchain/elfcopy/segments.c`** -> AI Confidence: **99.48%**
70. **`contrib/elftoolchain/libpe/libpe_coff.c`** -> AI Confidence: **99.48%**
71. **`contrib/elftoolchain/strings/strings.c`** -> AI Confidence: **99.48%**
72. **`contrib/expat/tests/alloc_tests.c`** -> AI Confidence: **99.48%**
73. **`contrib/expat/tests/basic_tests.c`** -> AI Confidence: **99.48%**
74. **`contrib/expat/tests/nsalloc_tests.c`** -> AI Confidence: **99.48%**
75. **`contrib/expat/xmlwf/xmlfile.c`** -> AI Confidence: **99.48%**
76. **`contrib/file/src/getopt_long.c`** -> AI Confidence: **99.48%**
77. **`contrib/file/src/is_json.c`** -> AI Confidence: **99.48%**
78. **`contrib/file/src/seccomp.c`** -> AI Confidence: **99.48%**
79. **`contrib/hyperv/tools/hv_vss_daemon.c`** -> AI Confidence: **99.48%**
80. **`contrib/ldns/compat/snprintf.c`** -> AI Confidence: **99.48%**
81. **`contrib/lib9p/pack.c`** -> AI Confidence: **99.48%**
82. **`contrib/libarchive/libarchive/archive_acl.c`** -> AI Confidence: **99.48%**
83. **`contrib/libarchive/libarchive/archive_disk_acl_freebsd.c`** -> AI Confidence: **99.48%**
84. **`contrib/libarchive/libarchive/archive_parse_date.c`** -> AI Confidence: **99.48%**
85. **`contrib/libarchive/libarchive/archive_util.c`** -> AI Confidence: **99.48%**
86. **`contrib/libarchive/libarchive/filter_fork_posix.c`** -> AI Confidence: **99.48%**
87. **`contrib/libarchive/tar/bsdtar.c`** -> AI Confidence: **99.48%**
88. **`contrib/libarchive/tar/util.c`** -> AI Confidence: **99.48%**
89. **`contrib/libarchive/test_utils/test_main.c`** -> AI Confidence: **99.48%**
90. **`contrib/libevent/sample/https-client.c`** -> AI Confidence: **99.48%**
91. **`contrib/libfido2/examples/assert.c`** -> AI Confidence: **99.48%**
92. **`contrib/libfido2/examples/cred.c`** -> AI Confidence: **99.48%**
93. **`contrib/libfido2/examples/util.c`** -> AI Confidence: **99.48%**
94. **`contrib/libfido2/openbsd-compat/readpassphrase_win32.c`** -> AI Confidence: **99.48%**
95. **`contrib/libfido2/tools/assert_get.c`** -> AI Confidence: **99.48%**
96. **`contrib/libfido2/tools/assert_verify.c`** -> AI Confidence: **99.48%**
97. **`contrib/libfido2/tools/config.c`** -> AI Confidence: **99.48%**
98. **`contrib/libfido2/tools/cred_make.c`** -> AI Confidence: **99.48%**
99. **`contrib/libfido2/tools/cred_verify.c`** -> AI Confidence: **99.48%**
100. **`contrib/libfido2/tools/credman.c`** -> AI Confidence: **99.48%**
101. **`contrib/libfido2/tools/pin.c`** -> AI Confidence: **99.48%**
102. **`contrib/libfido2/tools/token.c`** -> AI Confidence: **99.48%**
103. **`contrib/libpcap/bpf_filter.c`** -> AI Confidence: **99.48%**
104. **`contrib/libpcap/fad-gifc.c`** -> AI Confidence: **99.48%**
105. **`contrib/libpcap/pcap-dag.c`** -> AI Confidence: **99.48%**
106. **`contrib/libpcap/pcap-dlpi.c`** -> AI Confidence: **99.48%**
107. **`contrib/libpcap/rpcapd/fileconf.c`** -> AI Confidence: **99.48%**
108. **`contrib/libpcap/rpcapd/rpcapd.c`** -> AI Confidence: **99.48%**
109. **`contrib/libxo/encoder/cbor/enc_cbor.c`** -> AI Confidence: **99.48%**
110. **`contrib/libxo/encoder/csv/enc_csv.c`** -> AI Confidence: **99.48%**
111. **`contrib/libxo/libxo/libxo.c`** -> AI Confidence: **99.48%**
112. **`contrib/libxo/tests/core/test_02.c`** -> AI Confidence: **99.48%**
113. **`contrib/libxo/tests/core/test_08.c`** -> AI Confidence: **99.48%**
114. **`contrib/libxo/tests/core/test_09.c`** -> AI Confidence: **99.48%**
115. **`contrib/libxo/tests/core/test_10.c`** -> AI Confidence: **99.48%**
116. **`contrib/libxo/tests/core/test_12.c`** -> AI Confidence: **99.48%**
117. **`contrib/libxo/xo/xo.c`** -> AI Confidence: **99.48%**
118. **`contrib/lua/src/luac.c`** -> AI Confidence: **99.48%**
119. **`contrib/lua/src/lvm.c`** -> AI Confidence: **99.48%**
120. **`contrib/mandoc/catman.c`** -> AI Confidence: **99.48%**
121. **`contrib/mandoc/eqn_html.c`** -> AI Confidence: **99.48%**
122. **`contrib/mandoc/eqn_term.c`** -> AI Confidence: **99.48%**
123. **`contrib/mandoc/main.c`** -> AI Confidence: **99.48%**
124. **`contrib/mandoc/preconv.c`** -> AI Confidence: **99.48%**
125. **`contrib/mandoc/roff_escape.c`** -> AI Confidence: **99.48%**
126. **`contrib/mandoc/tbl_opts.c`** -> AI Confidence: **99.48%**
127. **`contrib/mandoc/term.c`** -> AI Confidence: **99.48%**
128. **`contrib/mandoc/tree.c`** -> AI Confidence: **99.48%**
129. **`contrib/mtree/compare.c`** -> AI Confidence: **99.48%**
130. **`contrib/mtree/crc.c`** -> AI Confidence: **99.48%**
131. **`contrib/mtree/create.c`** -> AI Confidence: **99.48%**
132. **`contrib/mtree/mtree.c`** -> AI Confidence: **99.48%**
133. **`contrib/mtree/verify.c`** -> AI Confidence: **99.48%**
134. **`contrib/ncurses/ncurses/base/lib_mouse.c`** -> AI Confidence: **99.48%**
135. **`contrib/ncurses/ncurses/tinfo/access.c`** -> AI Confidence: **99.48%**
136. **`contrib/ncurses/ncurses/tty/tty_update.c`** -> AI Confidence: **99.48%**
137. **`contrib/ncurses/progs/tic.c`** -> AI Confidence: **99.48%**
138. **`contrib/netbsd-tests/dev/audio/h_pad.c`** -> AI Confidence: **99.48%**
139. **`contrib/netbsd-tests/fs/ffs/h_quota2_tests.c`** -> AI Confidence: **99.48%**
140. **`contrib/netbsd-tests/fs/ffs/t_quota2_remount.c`** -> AI Confidence: **99.48%**
141. **`contrib/netbsd-tests/fs/vfs/t_full.c`** -> AI Confidence: **99.48%**
142. **`contrib/netbsd-tests/fs/vfs/t_unpriv.c`** -> AI Confidence: **99.48%**
143. **`contrib/netbsd-tests/include/sys/t_bitops.c`** -> AI Confidence: **99.48%**
144. **`contrib/netbsd-tests/kernel/t_ptrace.c`** -> AI Confidence: **99.48%**
145. **`contrib/netbsd-tests/net/sys/t_rfc6056.c`** -> AI Confidence: **99.48%**
146. **`contrib/netbsd-tests/rump/rumpkern/h_client/h_sigcli.c`** -> AI Confidence: **99.48%**
147. **`contrib/netbsd-tests/rump/rumpkern/h_client/h_simplecli.c`** -> AI Confidence: **99.48%**
148. **`contrib/netbsd-tests/rump/rumpkern/h_client/h_stresscli.c`** -> AI Confidence: **99.48%**
149. **`contrib/netbsd-tests/rump/rumpkern/t_kern.c`** -> AI Confidence: **99.48%**
150. **`contrib/netbsd-tests/rump/rumpvfs/t_etfs.c`** -> AI Confidence: **99.48%**
151. **`contrib/netcat/socks.c`** -> AI Confidence: **99.48%**
152. **`contrib/ntp/libntp/audio.c`** -> AI Confidence: **99.48%**
153. **`contrib/ntp/libntp/msyslog.c`** -> AI Confidence: **99.48%**
154. **`contrib/ntp/libntp/netof.c`** -> AI Confidence: **99.48%**
155. **`contrib/ntp/libntp/ntp_intres.c`** -> AI Confidence: **99.48%**
156. **`contrib/ntp/libntp/ntp_lineedit.c`** -> AI Confidence: **99.48%**
157. **`contrib/ntp/libntp/timetoa.c`** -> AI Confidence: **99.48%**
158. **`contrib/ntp/libntp/vint64ops.c`** -> AI Confidence: **99.48%**
159. **`contrib/ntp/libparse/clk_schmid.c`** -> AI Confidence: **99.48%**
160. **`contrib/ntp/libparse/clk_trimtaip.c`** -> AI Confidence: **99.48%**
161. **`contrib/ntp/ntpd/check_y2k.c`** -> AI Confidence: **99.48%**
162. **`contrib/ntp/ntpd/ntp_control.c`** -> AI Confidence: **99.48%**
163. **`contrib/ntp/ntpd/ntp_crypto.c`** -> AI Confidence: **99.48%**
164. **`contrib/ntp/ntpd/ntp_loopfilter.c`** -> AI Confidence: **99.48%**
165. **`contrib/ntp/ntpd/ntp_parser.c`** -> AI Confidence: **99.48%**
166. **`contrib/ntp/ntpd/ntp_timer.c`** -> AI Confidence: **99.48%**
167. **`contrib/ntp/ntpd/refclock_datum.c`** -> AI Confidence: **99.48%**
168. **`contrib/ntp/ntpd/refclock_gpsdjson.c`** -> AI Confidence: **99.48%**
169. **`contrib/ntp/ntpd/refclock_heath.c`** -> AI Confidence: **99.48%**
170. **`contrib/ntp/ntpd/refclock_ulink.c`** -> AI Confidence: **99.48%**
171. **`contrib/ntp/ntpd/refclock_zyfer.c`** -> AI Confidence: **99.48%**
172. **`contrib/ntp/ntpsnmpd/netsnmp_daemonize.c`** -> AI Confidence: **99.48%**
173. **`contrib/ntp/parseutil/dcfd.c`** -> AI Confidence: **99.48%**
174. **`contrib/ntp/sntp/libevent/sample/https-client.c`** -> AI Confidence: **99.48%**
175. **`contrib/ntp/util/audio-pcm.c`** -> AI Confidence: **99.48%**
176. **`contrib/ntp/util/ntptime.c`** -> AI Confidence: **99.48%**
177. **`contrib/ntp/util/tg.c`** -> AI Confidence: **99.48%**
178. **`contrib/ntp/util/tg2.c`** -> AI Confidence: **99.48%**
179. **`contrib/nvi/common/conv.c`** -> AI Confidence: **99.48%**
180. **`contrib/nvi/common/cut.c`** -> AI Confidence: **99.48%**
181. **`contrib/nvi/common/delete.c`** -> AI Confidence: **99.48%**
182. **`contrib/nvi/common/log.c`** -> AI Confidence: **99.48%**
183. **`contrib/nvi/common/main.c`** -> AI Confidence: **99.48%**
184. **`contrib/nvi/common/msg.c`** -> AI Confidence: **99.48%**
185. **`contrib/nvi/common/options.c`** -> AI Confidence: **99.48%**
186. **`contrib/nvi/common/put.c`** -> AI Confidence: **99.48%**
187. **`contrib/nvi/common/screen.c`** -> AI Confidence: **99.48%**
188. **`contrib/nvi/common/search.c`** -> AI Confidence: **99.48%**
189. **`contrib/nvi/ex/ex.c`** -> AI Confidence: **99.48%**
190. **`contrib/nvi/ex/ex_argv.c`** -> AI Confidence: **99.48%**
191. **`contrib/nvi/ex/ex_cd.c`** -> AI Confidence: **99.48%**
192. **`contrib/nvi/ex/ex_join.c`** -> AI Confidence: **99.48%**
193. **`contrib/nvi/ex/ex_mkexrc.c`** -> AI Confidence: **99.48%**
194. **`contrib/nvi/ex/ex_subst.c`** -> AI Confidence: **99.48%**
195. **`contrib/nvi/ex/ex_txt.c`** -> AI Confidence: **99.48%**
196. **`contrib/nvi/ex/ex_util.c`** -> AI Confidence: **99.48%**
197. **`contrib/nvi/vi/getc.c`** -> AI Confidence: **99.48%**
198. **`contrib/nvi/vi/v_cmd.c`** -> AI Confidence: **99.48%**
199. **`contrib/nvi/vi/v_increment.c`** -> AI Confidence: **99.48%**
200. **`contrib/nvi/vi/v_paragraph.c`** -> AI Confidence: **99.48%**
201. **`contrib/nvi/vi/v_put.c`** -> AI Confidence: **99.48%**
202. **`contrib/nvi/vi/v_replace.c`** -> AI Confidence: **99.48%**
203. **`contrib/nvi/vi/v_section.c`** -> AI Confidence: **99.48%**
204. **`contrib/nvi/vi/v_sentence.c`** -> AI Confidence: **99.48%**
205. **`contrib/nvi/vi/v_txt.c`** -> AI Confidence: **99.48%**
206. **`contrib/nvi/vi/vi.c`** -> AI Confidence: **99.48%**
207. **`contrib/nvi/vi/vs_line.c`** -> AI Confidence: **99.48%**
208. **`contrib/nvi/vi/vs_split.c`** -> AI Confidence: **99.48%**
209. **`contrib/ofed/infiniband-diags/src/iblinkinfo.c`** -> AI Confidence: **99.48%**
210. **`contrib/ofed/infiniband-diags/src/ibnetdiscover.c`** -> AI Confidence: **99.48%**
211. **`contrib/ofed/infiniband-diags/src/ibportstate.c`** -> AI Confidence: **99.48%**
212. **`contrib/ofed/infiniband-diags/src/ibqueryerrors.c`** -> AI Confidence: **99.48%**
213. **`contrib/ofed/infiniband-diags/src/ibroute.c`** -> AI Confidence: **99.48%**
214. **`contrib/ofed/infiniband-diags/src/ibstat.c`** -> AI Confidence: **99.48%**
215. **`contrib/ofed/infiniband-diags/src/perfquery.c`** -> AI Confidence: **99.48%**
216. **`contrib/ofed/infiniband-diags/src/sminfo.c`** -> AI Confidence: **99.48%**
217. **`contrib/ofed/librdmacm/examples/rdma_client.c`** -> AI Confidence: **99.48%**
218. **`contrib/ofed/librdmacm/examples/rdma_server.c`** -> AI Confidence: **99.48%**
219. **`contrib/ofed/opensm/opensm/main.c`** -> AI Confidence: **99.48%**
220. **`contrib/ofed/opensm/opensm/osm_drop_mgr.c`** -> AI Confidence: **99.48%**
221. **`contrib/ofed/opensm/opensm/osm_dump.c`** -> AI Confidence: **99.48%**
222. **`contrib/ofed/opensm/opensm/osm_inform.c`** -> AI Confidence: **99.48%**
223. **`contrib/ofed/opensm/opensm/osm_lid_mgr.c`** -> AI Confidence: **99.48%**
224. **`contrib/ofed/opensm/opensm/osm_link_mgr.c`** -> AI Confidence: **99.48%**
225. **`contrib/ofed/opensm/opensm/osm_mcast_mgr.c`** -> AI Confidence: **99.48%**
226. **`contrib/ofed/opensm/opensm/osm_mesh.c`** -> AI Confidence: **99.48%**
227. **`contrib/ofed/opensm/opensm/osm_mlnx_ext_port_info_rcv.c`** -> AI Confidence: **99.48%**
228. **`contrib/ofed/opensm/opensm/osm_node_info_rcv.c`** -> AI Confidence: **99.48%**
229. **`contrib/ofed/opensm/opensm/osm_perfmgr.c`** -> AI Confidence: **99.48%**
230. **`contrib/ofed/opensm/opensm/osm_pkey_mgr.c`** -> AI Confidence: **99.48%**
231. **`contrib/ofed/opensm/opensm/osm_pkey_rcv.c`** -> AI Confidence: **99.48%**
232. **`contrib/ofed/opensm/opensm/osm_port_info_rcv.c`** -> AI Confidence: **99.48%**
233. **`contrib/ofed/opensm/opensm/osm_req.c`** -> AI Confidence: **99.48%**
234. **`contrib/ofed/opensm/opensm/osm_resp.c`** -> AI Confidence: **99.48%**
235. **`contrib/ofed/opensm/opensm/osm_sa_class_port_info.c`** -> AI Confidence: **99.48%**
236. **`contrib/ofed/opensm/opensm/osm_sa_guidinfo_record.c`** -> AI Confidence: **99.48%**
237. **`contrib/ofed/opensm/opensm/osm_sa_informinfo.c`** -> AI Confidence: **99.48%**
238. **`contrib/ofed/opensm/opensm/osm_sa_link_record.c`** -> AI Confidence: **99.48%**
239. **`contrib/ofed/opensm/opensm/osm_sa_mad_ctrl.c`** -> AI Confidence: **99.48%**
240. **`contrib/ofed/opensm/opensm/osm_sa_mcmember_record.c`** -> AI Confidence: **99.48%**
241. **`contrib/ofed/opensm/opensm/osm_sa_multipath_record.c`** -> AI Confidence: **99.48%**
242. **`contrib/ofed/opensm/opensm/osm_sa_node_record.c`** -> AI Confidence: **99.48%**
243. **`contrib/ofed/opensm/opensm/osm_sa_path_record.c`** -> AI Confidence: **99.48%**
244. **`contrib/ofed/opensm/opensm/osm_sa_pkey_record.c`** -> AI Confidence: **99.48%**
245. **`contrib/ofed/opensm/opensm/osm_sa_portinfo_record.c`** -> AI Confidence: **99.48%**
246. **`contrib/ofed/opensm/opensm/osm_sa_slvl_record.c`** -> AI Confidence: **99.48%**
247. **`contrib/ofed/opensm/opensm/osm_sa_sminfo_record.c`** -> AI Confidence: **99.48%**
248. **`contrib/ofed/opensm/opensm/osm_slvl_map_rcv.c`** -> AI Confidence: **99.48%**
249. **`contrib/ofed/opensm/opensm/osm_sm_mad_ctrl.c`** -> AI Confidence: **99.48%**
250. **`contrib/ofed/opensm/opensm/osm_sm_state_mgr.c`** -> AI Confidence: **99.48%**
251. **`contrib/ofed/opensm/opensm/osm_sminfo_rcv.c`** -> AI Confidence: **99.48%**
252. **`contrib/ofed/opensm/opensm/osm_sw_info_rcv.c`** -> AI Confidence: **99.48%**
253. **`contrib/ofed/opensm/opensm/osm_switch.c`** -> AI Confidence: **99.48%**
254. **`contrib/ofed/opensm/opensm/osm_trap_rcv.c`** -> AI Confidence: **99.48%**
255. **`contrib/ofed/opensm/opensm/osm_ucast_cache.c`** -> AI Confidence: **99.48%**
256. **`contrib/ofed/opensm/opensm/osm_ucast_file.c`** -> AI Confidence: **99.48%**
257. **`contrib/ofed/opensm/opensm/osm_ucast_lash.c`** -> AI Confidence: **99.48%**
258. **`contrib/ofed/opensm/opensm/osm_vl_arb_rcv.c`** -> AI Confidence: **99.48%**
259. **`contrib/one-true-awk/b.c`** -> AI Confidence: **99.48%**
260. **`contrib/one-true-awk/run.c`** -> AI Confidence: **99.48%**
261. **`contrib/openbsm/bin/auditd/auditd.c`** -> AI Confidence: **99.48%**
262. **`contrib/openbsm/bin/auditfilterd/auditfilterd.c`** -> AI Confidence: **99.48%**
263. **`contrib/openbsm/bin/praudit/praudit.c`** -> AI Confidence: **99.48%**
264. **`contrib/openbsm/libbsm/bsm_io.c`** -> AI Confidence: **99.48%**
265. **`contrib/openpam/bin/pamtest/pamtest.c`** -> AI Confidence: **99.48%**
266. **`contrib/openpam/bin/su/su.c`** -> AI Confidence: **99.48%**
267. **`contrib/pam-krb5/module/setcred.c`** -> AI Confidence: **99.48%**
268. **`contrib/pam-krb5/tests/module/cache-cleanup-t.c`** -> AI Confidence: **99.48%**
269. **`contrib/pam_modules/pam_passwdqc/pam_passwdqc.c`** -> AI Confidence: **99.48%**
270. **`contrib/pnpinfo/pnpinfo.c`** -> AI Confidence: **99.48%**
271. **`contrib/sendmail/libsm/b-strl.c`** -> AI Confidence: **99.48%**
272. **`contrib/sendmail/libsm/fseek.c`** -> AI Confidence: **99.48%**
273. **`contrib/sendmail/libsm/fvwrite.c`** -> AI Confidence: **99.48%**
274. **`contrib/sendmail/libsm/setvbuf.c`** -> AI Confidence: **99.48%**
275. **`contrib/sendmail/libsm/strto.c`** -> AI Confidence: **99.48%**
276. **`contrib/sendmail/libsm/t-memstat.c`** -> AI Confidence: **99.48%**
277. **`contrib/sendmail/libsm/t-qic.c`** -> AI Confidence: **99.48%**
278. **`contrib/sendmail/libsm/t-streq.c`** -> AI Confidence: **99.48%**
279. **`contrib/sendmail/libsm/vfscanf.c`** -> AI Confidence: **99.48%**
280. **`contrib/sendmail/praliases/praliases.c`** -> AI Confidence: **99.48%**
281. **`contrib/sendmail/src/conf.h`** -> AI Confidence: **99.48%**
282. **`contrib/sendmail/src/deliver.c`** -> AI Confidence: **99.48%**
283. **`contrib/sendmail/src/domain.c`** -> AI Confidence: **99.48%**
284. **`contrib/sendmail/src/sm_resolve.c`** -> AI Confidence: **99.48%**
285. **`contrib/sendmail/src/tls.c`** -> AI Confidence: **99.48%**
286. **`contrib/smbfs/mount_smbfs/mount_smbfs.c`** -> AI Confidence: **99.48%**
287. **`contrib/smbfs/smbutil/login.c`** -> AI Confidence: **99.48%**
288. **`contrib/smbfs/smbutil/print.c`** -> AI Confidence: **99.48%**
289. **`contrib/tcp_wrappers/misc.c`** -> AI Confidence: **99.48%**
290. **`contrib/tcp_wrappers/tcpdchk.c`** -> AI Confidence: **99.48%**
291. **`contrib/tcpdump/print-babel.c`** -> AI Confidence: **99.48%**
292. **`contrib/tcpdump/print-bgp.c`** -> AI Confidence: **99.48%**
293. **`contrib/tcpdump/print-domain.c`** -> AI Confidence: **99.48%**
294. **`contrib/tcpdump/print-ip-demux.c`** -> AI Confidence: **99.48%**
295. **`contrib/tcpdump/print-isoclns.c`** -> AI Confidence: **99.48%**
296. **`contrib/tcpdump/print-juniper.c`** -> AI Confidence: **99.48%**
297. **`contrib/tcpdump/print-ldp.c`** -> AI Confidence: **99.48%**
298. **`contrib/tcpdump/print-pim.c`** -> AI Confidence: **99.48%**
299. **`contrib/tcpdump/print-ppp.c`** -> AI Confidence: **99.48%**
300. **`contrib/tcpdump/print-rsvp.c`** -> AI Confidence: **99.48%**
301. **`contrib/tcpdump/print-sll.c`** -> AI Confidence: **99.48%**
302. **`contrib/tcpdump/print-udp.c`** -> AI Confidence: **99.48%**
303. **`contrib/telnet/telnet/main.c`** -> AI Confidence: **99.48%**
304. **`contrib/telnet/telnet/telnet.c`** -> AI Confidence: **99.48%**
305. **`contrib/telnet/telnet/utilities.c`** -> AI Confidence: **99.48%**
306. **`contrib/tnftp/src/fetch.c`** -> AI Confidence: **99.48%**
307. **`contrib/tnftp/src/main.c`** -> AI Confidence: **99.48%**
308. **`contrib/tnftp/src/ruserpass.c`** -> AI Confidence: **99.48%**
309. **`contrib/ts/ts.c`** -> AI Confidence: **99.48%**
310. **`contrib/unbound/compat/snprintf.c`** -> AI Confidence: **99.48%**
311. **`contrib/unbound/smallapp/unbound-checkconf.c`** -> AI Confidence: **99.48%**
312. **`contrib/unbound/testcode/unitldns.c`** -> AI Confidence: **99.48%**
313. **`contrib/unbound/util/config_file.c`** -> AI Confidence: **99.48%**
314. **`contrib/unbound/util/configparser.c`** -> AI Confidence: **99.48%**
315. **`contrib/unbound/util/storage/lookup3.c`** -> AI Confidence: **99.48%**
316. **`contrib/vis/vis.c`** -> AI Confidence: **99.48%**
317. **`contrib/wireguard-tools/showconf.c`** -> AI Confidence: **99.48%**
318. **`contrib/wpa/hostapd/config_file.c`** -> AI Confidence: **99.48%**
319. **`contrib/wpa/hs20/client/est.c`** -> AI Confidence: **99.48%**
320. **`contrib/wpa/src/common/dpp_auth.c`** -> AI Confidence: **99.48%**
321. **`contrib/wpa/src/common/dpp_reconfig.c`** -> AI Confidence: **99.48%**
322. **`contrib/wpa/src/crypto/fips_prf_openssl.c`** -> AI Confidence: **99.48%**
323. **`contrib/wpa/src/p2p/p2p_pd.c`** -> AI Confidence: **99.48%**
324. **`contrib/xz/src/common/tuklib_cpucores.c`** -> AI Confidence: **99.48%**
325. **`contrib/xz/src/common/tuklib_exit.c`** -> AI Confidence: **99.48%**
326. **`contrib/xz/src/common/tuklib_physmem.c`** -> AI Confidence: **99.48%**
327. **`crypto/heimdal/appl/afsutil/pagsh.c`** -> AI Confidence: **99.48%**
328. **`crypto/heimdal/appl/ftp/ftpd/ftpcmd.c`** -> AI Confidence: **99.48%**
329. **`crypto/heimdal/appl/ftp/ftpd/ls.c`** -> AI Confidence: **99.48%**
330. **`crypto/heimdal/appl/ftp/ftpd/popen.c`** -> AI Confidence: **99.48%**
331. **`crypto/heimdal/appl/gssmask/common.h`** -> AI Confidence: **99.48%**
332. **`crypto/heimdal/appl/telnet/telnetd/telnetd.c`** -> AI Confidence: **99.48%**
333. **`crypto/krb5/src/appl/gss-sample/gss-client.c`** -> AI Confidence: **99.48%**
334. **`crypto/krb5/src/appl/sample/sclient/sclient.c`** -> AI Confidence: **99.48%**
335. **`crypto/krb5/src/appl/sample/sserver/sserver.c`** -> AI Confidence: **99.48%**
336. **`crypto/krb5/src/appl/simple/client/sim_client.c`** -> AI Confidence: **99.48%**
337. **`crypto/krb5/src/appl/user_user/client.c`** -> AI Confidence: **99.48%**
338. **`crypto/krb5/src/ccapi/lib/ccapi_context.c`** -> AI Confidence: **99.48%**
339. **`crypto/krb5/src/ccapi/lib/ccapi_v2.c`** -> AI Confidence: **99.48%**
340. **`crypto/krb5/src/ccapi/test/test_ccapi_ccache.c`** -> AI Confidence: **99.48%**
341. **`crypto/krb5/src/ccapi/test/test_ccapi_util.c`** -> AI Confidence: **99.48%**
342. **`crypto/krb5/src/ccapi/test/test_ccapi_v2.c`** -> AI Confidence: **99.48%**
343. **`crypto/krb5/src/clients/kinit/kinit.c`** -> AI Confidence: **99.48%**
344. **`crypto/krb5/src/clients/klist/klist.c`** -> AI Confidence: **99.48%**
345. **`crypto/krb5/src/clients/kvno/kvno.c`** -> AI Confidence: **99.48%**
346. **`crypto/krb5/src/kadmin/cli/kadmin.c`** -> AI Confidence: **99.48%**
347. **`crypto/krb5/src/kadmin/dbutil/dump.c`** -> AI Confidence: **99.48%**
348. **`crypto/krb5/src/kadmin/dbutil/kdb5_mkey.c`** -> AI Confidence: **99.48%**
349. **`crypto/krb5/src/kdc/do_tgs_req.c`** -> AI Confidence: **99.48%**
350. **`crypto/krb5/src/kdc/main.c`** -> AI Confidence: **99.48%**
351. **`crypto/krb5/src/kdc/policy.c`** -> AI Confidence: **99.48%**
352. **`crypto/krb5/src/kprop/kprop.c`** -> AI Confidence: **99.48%**
353. **`crypto/krb5/src/kprop/kpropd.c`** -> AI Confidence: **99.48%**
354. **`crypto/krb5/src/kprop/kproplog.c`** -> AI Confidence: **99.48%**
355. **`crypto/krb5/src/lib/kadm5/alt_prof.c`** -> AI Confidence: **99.48%**
356. **`crypto/krb5/src/lib/kadm5/logger.c`** -> AI Confidence: **99.48%**
357. **`crypto/krb5/src/lib/kdb/kdb_convert.c`** -> AI Confidence: **99.48%**
358. **`crypto/krb5/src/lib/krb5/ccache/ccapi/stdcc.c`** -> AI Confidence: **99.48%**
359. **`crypto/krb5/src/lib/krb5/ccache/t_cc.c`** -> AI Confidence: **99.48%**
360. **`crypto/krb5/src/lib/krb5/krb/deltat.c`** -> AI Confidence: **99.48%**
361. **`crypto/krb5/src/lib/krb5/krb/sendauth.c`** -> AI Confidence: **99.48%**
362. **`crypto/krb5/src/lib/krb5/os/t_gifconf.c`** -> AI Confidence: **99.48%**
363. **`crypto/krb5/src/lib/rpc/unit-test/client.c`** -> AI Confidence: **99.48%**
364. **`crypto/krb5/src/plugins/kdb/db2/libdb2/btree/bt_open.c`** -> AI Confidence: **99.48%**
365. **`crypto/krb5/src/plugins/kdb/db2/libdb2/btree/bt_put.c`** -> AI Confidence: **99.48%**
366. **`crypto/krb5/src/plugins/kdb/db2/libdb2/btree/bt_split.c`** -> AI Confidence: **99.48%**
367. **`crypto/krb5/src/plugins/kdb/db2/libdb2/recno/rec_open.c`** -> AI Confidence: **99.48%**
368. **`crypto/krb5/src/plugins/kdb/db2/libdb2/recno/rec_put.c`** -> AI Confidence: **99.48%**
369. **`crypto/krb5/src/plugins/kdb/db2/libdb2/recno/rec_seq.c`** -> AI Confidence: **99.48%**
370. **`crypto/krb5/src/plugins/kdb/db2/libdb2/test/SEQ_TEST/t.c`** -> AI Confidence: **99.48%**
371. **`crypto/krb5/src/plugins/kdb/ldap/ldap_exp.c`** -> AI Confidence: **99.48%**
372. **`crypto/krb5/src/plugins/kdb/ldap/ldap_util/kdb5_ldap_realm.c`** -> AI Confidence: **99.48%**
373. **`crypto/krb5/src/plugins/preauth/securid_sam2/securid2.c`** -> AI Confidence: **99.48%**
374. **`crypto/krb5/src/plugins/preauth/spake/openssl.c`** -> AI Confidence: **99.48%**
375. **`crypto/krb5/src/util/support/mkstemp.c`** -> AI Confidence: **99.48%**
376. **`crypto/krb5/src/util/verto/verto-k5ev.c`** -> AI Confidence: **99.48%**
377. **`crypto/krb5/src/windows/kfwlogon/kfwcommon.c`** -> AI Confidence: **99.48%**
378. **`crypto/krb5/src/windows/leashdll/krb5routines.c`** -> AI Confidence: **99.48%**
379. **`crypto/krb5/src/windows/leashdll/lsh_pwd.c`** -> AI Confidence: **99.48%**
380. **`crypto/libecc/src/arithmetic_tests/arithmetic_tests.c`** -> AI Confidence: **99.48%**
381. **`crypto/libecc/src/external_deps/rand.c`** -> AI Confidence: **99.48%**
382. **`crypto/libecc/src/nn/nn_mul_redc1.c`** -> AI Confidence: **99.48%**
383. **`crypto/libecc/src/sig/bign_common.c`** -> AI Confidence: **99.48%**
384. **`crypto/libecc/src/sig/bip0340.c`** -> AI Confidence: **99.48%**
385. **`crypto/libecc/src/sig/eddsa.c`** -> AI Confidence: **99.48%**
386. **`crypto/libecc/src/tests/ec_self_tests_core.c`** -> AI Confidence: **99.48%**
387. **`crypto/openssh/addrmatch.c`** -> AI Confidence: **99.48%**
388. **`crypto/openssh/auth-krb5.c`** -> AI Confidence: **99.48%**
389. **`crypto/openssh/auth-options.c`** -> AI Confidence: **99.48%**
390. **`crypto/openssh/auth-rhosts.c`** -> AI Confidence: **99.48%**
391. **`crypto/openssh/auth2-hostbased.c`** -> AI Confidence: **99.48%**
392. **`crypto/openssh/auth2-pubkey.c`** -> AI Confidence: **99.48%**
393. **`crypto/openssh/contrib/gnome-ssh-askpass2.c`** -> AI Confidence: **99.48%**
394. **`crypto/openssh/contrib/gnome-ssh-askpass3.c`** -> AI Confidence: **99.48%**
395. **`crypto/openssh/includes.h`** -> AI Confidence: **99.48%**
396. **`crypto/openssh/kexgexc.c`** -> AI Confidence: **99.48%**
397. **`crypto/openssh/moduli.c`** -> AI Confidence: **99.48%**
398. **`crypto/openssh/openbsd-compat/base64.c`** -> AI Confidence: **99.48%**
399. **`crypto/openssh/openbsd-compat/bsd-poll.c`** -> AI Confidence: **99.48%**
400. **`crypto/openssh/openbsd-compat/bsd-snprintf.c`** -> AI Confidence: **99.48%**
401. **`crypto/openssh/openbsd-compat/getcwd.c`** -> AI Confidence: **99.48%**
402. **`crypto/openssh/openbsd-compat/getrrsetbyname-ldns.c`** -> AI Confidence: **99.48%**
403. **`crypto/openssh/openbsd-compat/port-irix.c`** -> AI Confidence: **99.48%**
404. **`crypto/openssh/openbsd-compat/setproctitle.c`** -> AI Confidence: **99.48%**
405. **`crypto/openssh/openbsd-compat/vis.c`** -> AI Confidence: **99.48%**
406. **`crypto/openssh/platform-tracing.c`** -> AI Confidence: **99.48%**
407. **`crypto/openssh/readconf.c`** -> AI Confidence: **99.48%**
408. **`crypto/openssh/regress/misc/ssh-verify-attestation/ssh-verify-attestation.c`** -> AI Confidence: **99.48%**
409. **`crypto/openssh/regress/modpipe.c`** -> AI Confidence: **99.48%**
410. **`crypto/openssh/regress/netcat.c`** -> AI Confidence: **99.48%**
411. **`crypto/openssh/regress/unittests/bitmap/tests.c`** -> AI Confidence: **99.48%**
412. **`crypto/openssh/regress/unittests/match/tests.c`** -> AI Confidence: **99.48%**
413. **`crypto/openssh/regress/unittests/sshbuf/test_sshbuf_fuzz.c`** -> AI Confidence: **99.48%**
414. **`crypto/openssh/servconf.c`** -> AI Confidence: **99.48%**
415. **`crypto/openssh/serverloop.c`** -> AI Confidence: **99.48%**
416. **`crypto/openssh/sftp.c`** -> AI Confidence: **99.48%**
417. **`crypto/openssh/ssh-add.c`** -> AI Confidence: **99.48%**
418. **`crypto/openssh/ssh-keyscan.c`** -> AI Confidence: **99.48%**
419. **`crypto/openssh/ssh-keysign.c`** -> AI Confidence: **99.48%**
420. **`crypto/openssh/ssh-sk-helper.c`** -> AI Confidence: **99.48%**
421. **`crypto/openssh/ssh.c`** -> AI Confidence: **99.48%**
422. **`crypto/openssh/sshconnect.c`** -> AI Confidence: **99.48%**
423. **`crypto/openssh/uidswap.c`** -> AI Confidence: **99.48%**
424. **`crypto/openssl/apps/asn1parse.c`** -> AI Confidence: **99.48%**
425. **`crypto/openssl/apps/ca.c`** -> AI Confidence: **99.48%**
426. **`crypto/openssl/apps/cmp.c`** -> AI Confidence: **99.48%**
427. **`crypto/openssl/apps/cms.c`** -> AI Confidence: **99.48%**
428. **`crypto/openssl/apps/crl.c`** -> AI Confidence: **99.48%**
429. **`crypto/openssl/apps/crl2pkcs7.c`** -> AI Confidence: **99.48%**
430. **`crypto/openssl/apps/dgst.c`** -> AI Confidence: **99.48%**
431. **`crypto/openssl/apps/dhparam.c`** -> AI Confidence: **99.48%**
432. **`crypto/openssl/apps/dsa.c`** -> AI Confidence: **99.48%**
433. **`crypto/openssl/apps/dsaparam.c`** -> AI Confidence: **99.48%**
434. **`crypto/openssl/apps/ec.c`** -> AI Confidence: **99.48%**
435. **`crypto/openssl/apps/ecparam.c`** -> AI Confidence: **99.48%**
436. **`crypto/openssl/apps/enc.c`** -> AI Confidence: **99.48%**
437. **`crypto/openssl/apps/errstr.c`** -> AI Confidence: **99.48%**
438. **`crypto/openssl/apps/fipsinstall.c`** -> AI Confidence: **99.48%**
439. **`crypto/openssl/apps/gendsa.c`** -> AI Confidence: **99.48%**
440. **`crypto/openssl/apps/genpkey.c`** -> AI Confidence: **99.48%**
441. **`crypto/openssl/apps/genrsa.c`** -> AI Confidence: **99.48%**
442. **`crypto/openssl/apps/kdf.c`** -> AI Confidence: **99.48%**
443. **`crypto/openssl/apps/mac.c`** -> AI Confidence: **99.48%**
444. **`crypto/openssl/apps/ocsp.c`** -> AI Confidence: **99.48%**
445. **`crypto/openssl/apps/passwd.c`** -> AI Confidence: **99.48%**
446. **`crypto/openssl/apps/pkcs12.c`** -> AI Confidence: **99.48%**
447. **`crypto/openssl/apps/pkcs7.c`** -> AI Confidence: **99.48%**
448. **`crypto/openssl/apps/pkcs8.c`** -> AI Confidence: **99.48%**
449. **`crypto/openssl/apps/pkey.c`** -> AI Confidence: **99.48%**
450. **`crypto/openssl/apps/pkeyparam.c`** -> AI Confidence: **99.48%**
451. **`crypto/openssl/apps/pkeyutl.c`** -> AI Confidence: **99.48%**
452. **`crypto/openssl/apps/rand.c`** -> AI Confidence: **99.48%**
453. **`crypto/openssl/apps/rehash.c`** -> AI Confidence: **99.48%**
454. **`crypto/openssl/apps/req.c`** -> AI Confidence: **99.48%**
455. **`crypto/openssl/apps/rsa.c`** -> AI Confidence: **99.48%**
456. **`crypto/openssl/apps/rsautl.c`** -> AI Confidence: **99.48%**
457. **`crypto/openssl/apps/s_client.c`** -> AI Confidence: **99.48%**
458. **`crypto/openssl/apps/s_time.c`** -> AI Confidence: **99.48%**
459. **`crypto/openssl/apps/sess_id.c`** -> AI Confidence: **99.48%**
460. **`crypto/openssl/apps/skeyutl.c`** -> AI Confidence: **99.48%**
461. **`crypto/openssl/apps/smime.c`** -> AI Confidence: **99.48%**
462. **`crypto/openssl/apps/speed.c`** -> AI Confidence: **99.48%**
463. **`crypto/openssl/apps/spkac.c`** -> AI Confidence: **99.48%**
464. **`crypto/openssl/apps/srp.c`** -> AI Confidence: **99.48%**
465. **`crypto/openssl/apps/storeutl.c`** -> AI Confidence: **99.48%**
466. **`crypto/openssl/apps/ts.c`** -> AI Confidence: **99.48%**
467. **`crypto/openssl/apps/verify.c`** -> AI Confidence: **99.48%**
468. **`crypto/openssl/apps/version.c`** -> AI Confidence: **99.48%**
469. **`crypto/openssl/apps/x509.c`** -> AI Confidence: **99.48%**
470. **`crypto/openssl/crypto/armcap.c`** -> AI Confidence: **99.48%**
471. **`crypto/openssl/crypto/asn1/a_object.c`** -> AI Confidence: **99.48%**
472. **`crypto/openssl/crypto/asn1/a_sign.c`** -> AI Confidence: **99.48%**
473. **`crypto/openssl/crypto/asn1/a_verify.c`** -> AI Confidence: **99.48%**
474. **`crypto/openssl/crypto/asn1/d2i_pu.c`** -> AI Confidence: **99.48%**
475. **`crypto/openssl/crypto/asn1/p5_pbev2.c`** -> AI Confidence: **99.48%**
476. **`crypto/openssl/crypto/asn1/p5_scrypt.c`** -> AI Confidence: **99.48%**
477. **`crypto/openssl/crypto/asn1/t_spki.c`** -> AI Confidence: **99.48%**
478. **`crypto/openssl/crypto/asn1/tasn_new.c`** -> AI Confidence: **99.48%**
479. **`crypto/openssl/crypto/bio/bio_print.c`** -> AI Confidence: **99.48%**
480. **`crypto/openssl/crypto/bn/bn_exp.c`** -> AI Confidence: **99.48%**
481. **`crypto/openssl/crypto/cmp/cmp_client.c`** -> AI Confidence: **99.48%**
482. **`crypto/openssl/crypto/cmp/cmp_http.c`** -> AI Confidence: **99.48%**
483. **`crypto/openssl/crypto/cms/cms_dh.c`** -> AI Confidence: **99.48%**
484. **`crypto/openssl/crypto/cms/cms_ec.c`** -> AI Confidence: **99.48%**
485. **`crypto/openssl/crypto/cms/cms_enc.c`** -> AI Confidence: **99.48%**
486. **`crypto/openssl/crypto/cms/cms_pwri.c`** -> AI Confidence: **99.48%**
487. **`crypto/openssl/crypto/cms/cms_sd.c`** -> AI Confidence: **99.48%**
488. **`crypto/openssl/crypto/conf/conf_def.c`** -> AI Confidence: **99.48%**
489. **`crypto/openssl/crypto/crmf/crmf_pbm.c`** -> AI Confidence: **99.48%**
490. **`crypto/openssl/crypto/dh/dh_check.c`** -> AI Confidence: **99.48%**
491. **`crypto/openssl/crypto/dh/dh_key.c`** -> AI Confidence: **99.48%**
492. **`crypto/openssl/crypto/dsa/dsa_ossl.c`** -> AI Confidence: **99.48%**
493. **`crypto/openssl/crypto/ec/ec_asn1.c`** -> AI Confidence: **99.48%**
494. **`crypto/openssl/crypto/ec/ec_mult.c`** -> AI Confidence: **99.48%**
495. **`crypto/openssl/crypto/ec/ecdh_ossl.c`** -> AI Confidence: **99.48%**
496. **`crypto/openssl/crypto/ec/ecdsa_ossl.c`** -> AI Confidence: **99.48%**
497. **`crypto/openssl/crypto/ec/ecp_nistp256.c`** -> AI Confidence: **99.48%**
498. **`crypto/openssl/crypto/ec/ecp_nistp521.c`** -> AI Confidence: **99.48%**
499. **`crypto/openssl/crypto/ec/ecp_s390x_nistp.c`** -> AI Confidence: **99.48%**
500. **`crypto/openssl/crypto/err/err_all.c`** -> AI Confidence: **99.48%**
501. **`crypto/openssl/crypto/evp/p5_crpt.c`** -> AI Confidence: **99.48%**
502. **`crypto/openssl/crypto/evp/p_dec.c`** -> AI Confidence: **99.48%**
503. **`crypto/openssl/crypto/evp/p_enc.c`** -> AI Confidence: **99.48%**
504. **`crypto/openssl/crypto/evp/p_seal.c`** -> AI Confidence: **99.48%**
505. **`crypto/openssl/crypto/evp/pmeth_gn.c`** -> AI Confidence: **99.48%**
506. **`crypto/openssl/crypto/evp/signature.c`** -> AI Confidence: **99.48%**
507. **`crypto/openssl/crypto/ffc/ffc_params_generate.c`** -> AI Confidence: **99.48%**
508. **`crypto/openssl/crypto/info.c`** -> AI Confidence: **99.48%**
509. **`crypto/openssl/crypto/ml_dsa/ml_dsa_sign.c`** -> AI Confidence: **99.48%**
510. **`crypto/openssl/crypto/modes/gcm128.c`** -> AI Confidence: **99.48%**
511. **`crypto/openssl/crypto/o_dir.c`** -> AI Confidence: **99.48%**
512. **`crypto/openssl/crypto/pem/pem_info.c`** -> AI Confidence: **99.48%**
513. **`crypto/openssl/crypto/pkcs12/p12_npas.c`** -> AI Confidence: **99.48%**
514. **`crypto/openssl/crypto/pkcs7/pk7_doit.c`** -> AI Confidence: **99.48%**
515. **`crypto/openssl/crypto/property/property_parse.c`** -> AI Confidence: **99.48%**
516. **`crypto/openssl/crypto/rand/randfile.c`** -> AI Confidence: **99.48%**
517. **`crypto/openssl/crypto/rsa/rsa_ossl.c`** -> AI Confidence: **99.48%**
518. **`crypto/openssl/crypto/rsa/rsa_pss.c`** -> AI Confidence: **99.48%**
519. **`crypto/openssl/crypto/rsa/rsa_sign.c`** -> AI Confidence: **99.48%**
520. **`crypto/openssl/crypto/sha/sha512.c`** -> AI Confidence: **99.48%**
521. **`crypto/openssl/crypto/sleep.c`** -> AI Confidence: **99.48%**
522. **`crypto/openssl/crypto/sm2/sm2_crypt.c`** -> AI Confidence: **99.48%**
523. **`crypto/openssl/crypto/sm2/sm2_sign.c`** -> AI Confidence: **99.48%**
524. **`crypto/openssl/crypto/ts/ts_conf.c`** -> AI Confidence: **99.48%**
525. **`crypto/openssl/crypto/ts/ts_rsp_verify.c`** -> AI Confidence: **99.48%**
526. **`crypto/openssl/crypto/x509/by_file.c`** -> AI Confidence: **99.48%**
527. **`crypto/openssl/crypto/x509/t_req.c`** -> AI Confidence: **99.48%**
528. **`crypto/openssl/crypto/x509/t_x509.c`** -> AI Confidence: **99.48%**
529. **`crypto/openssl/crypto/x509/v3_akid.c`** -> AI Confidence: **99.48%**
530. **`crypto/openssl/crypto/x509/v3_asid.c`** -> AI Confidence: **99.48%**
531. **`crypto/openssl/crypto/x509/v3_cpols.c`** -> AI Confidence: **99.48%**
532. **`crypto/openssl/crypto/x509/v3_ist.c`** -> AI Confidence: **99.48%**
533. **`crypto/openssl/crypto/x509/v3_san.c`** -> AI Confidence: **99.48%**
534. **`crypto/openssl/crypto/x509/v3_tlsf.c`** -> AI Confidence: **99.48%**
535. **`crypto/openssl/crypto/x509/x509_obj.c`** -> AI Confidence: **99.48%**
536. **`crypto/openssl/crypto/x509/x509_r2x.c`** -> AI Confidence: **99.48%**
537. **`crypto/openssl/demos/bio/sconnect.c`** -> AI Confidence: **99.48%**
538. **`crypto/openssl/demos/bio/server-conf.c`** -> AI Confidence: **99.48%**
539. **`crypto/openssl/demos/encrypt/rsa_encrypt.c`** -> AI Confidence: **99.48%**
540. **`crypto/openssl/demos/guide/quic-client-non-block.c`** -> AI Confidence: **99.48%**
541. **`crypto/openssl/demos/guide/tls-client-non-block.c`** -> AI Confidence: **99.48%**
542. **`crypto/openssl/demos/guide/tls-server-block.c`** -> AI Confidence: **99.48%**
543. **`crypto/openssl/demos/mac/cmac-aes256.c`** -> AI Confidence: **99.48%**
544. **`crypto/openssl/demos/mac/hmac-sha512.c`** -> AI Confidence: **99.48%**
545. **`crypto/openssl/demos/mac/poly1305.c`** -> AI Confidence: **99.48%**
546. **`crypto/openssl/demos/signature/rsa_pss_direct.c`** -> AI Confidence: **99.48%**
547. **`crypto/openssl/demos/signature/rsa_pss_hash.c`** -> AI Confidence: **99.48%**
548. **`crypto/openssl/fuzz/asn1.c`** -> AI Confidence: **99.48%**
549. **`crypto/openssl/fuzz/provider.c`** -> AI Confidence: **99.48%**
550. **`crypto/openssl/fuzz/quic-client.c`** -> AI Confidence: **99.48%**
551. **`crypto/openssl/fuzz/quic-server.c`** -> AI Confidence: **99.48%**
552. **`crypto/openssl/providers/fips/self_test_kats.c`** -> AI Confidence: **99.48%**
553. **`crypto/openssl/providers/implementations/ciphers/cipher_aes_ccm_hw.c`** -> AI Confidence: **99.48%**
554. **`crypto/openssl/providers/implementations/ciphers/cipher_aes_hw.c`** -> AI Confidence: **99.48%**
555. **`crypto/openssl/providers/implementations/encode_decode/ml_dsa_codecs.c`** -> AI Confidence: **99.48%**
556. **`crypto/openssl/providers/implementations/encode_decode/ml_kem_codecs.c`** -> AI Confidence: **99.48%**
557. **`crypto/openssl/ssl/bio_ssl.c`** -> AI Confidence: **99.48%**
558. **`crypto/openssl/ssl/record/methods/ssl3_cbc.c`** -> AI Confidence: **99.48%**
559. **`crypto/openssl/ssl/rio/poll_immediate.c`** -> AI Confidence: **99.48%**
560. **`crypto/openssl/ssl/ssl_ciph.c`** -> AI Confidence: **99.48%**
561. **`crypto/openssl/ssl/statem/statem_srvr.c`** -> AI Confidence: **99.48%**
562. **`crypto/openssl/ssl/tls13_enc.c`** -> AI Confidence: **99.48%**
563. **`lib/msun/src/s_sincosl.c`** -> AI Confidence: **99.48%**
564. **`libexec/atrun/atrun.c`** -> AI Confidence: **99.48%**
565. **`libexec/bootpd/dovend.c`** -> AI Confidence: **99.48%**
566. **`libexec/bootpd/trygetea.c`** -> AI Confidence: **99.48%**
567. **`libexec/fingerd/fingerd.c`** -> AI Confidence: **99.48%**
568. **`libexec/getty/chat.c`** -> AI Confidence: **99.48%**
569. **`libexec/getty/main.c`** -> AI Confidence: **99.48%**
570. **`libexec/mknetid/mknetid.c`** -> AI Confidence: **99.48%**
571. **`libexec/phttpget/phttpget.c`** -> AI Confidence: **99.48%**
572. **`libexec/rtld-elf/rtld_printf.c`** -> AI Confidence: **99.48%**
573. **`libexec/talkd/table.c`** -> AI Confidence: **99.48%**
574. **`libexec/talkd/talkd.c`** -> AI Confidence: **99.48%**
575. **`libexec/tftpd/tftp-file.c`** -> AI Confidence: **99.48%**
576. **`libexec/ypxfr/ypxfr_main.c`** -> AI Confidence: **99.48%**
577. **`sbin/bsdlabel/bsdlabel.c`** -> AI Confidence: **99.48%**
578. **`sbin/camcontrol/attrib.c`** -> AI Confidence: **99.48%**
579. **`sbin/camcontrol/camcontrol.c`** -> AI Confidence: **99.48%**
580. **`sbin/camcontrol/epc.c`** -> AI Confidence: **99.48%**
581. **`sbin/camcontrol/timestamp.c`** -> AI Confidence: **99.48%**
582. **`sbin/camcontrol/util.c`** -> AI Confidence: **99.48%**
583. **`sbin/camcontrol/zone.c`** -> AI Confidence: **99.48%**
584. **`sbin/ddb/ddb_script.c`** -> AI Confidence: **99.48%**
585. **`sbin/decryptcore/decryptcore.c`** -> AI Confidence: **99.48%**
586. **`sbin/devmatch/devmatch.c`** -> AI Confidence: **99.48%**
587. **`sbin/dhclient/dhclient.c`** -> AI Confidence: **99.48%**
588. **`sbin/dump/main.c`** -> AI Confidence: **99.48%**
589. **`sbin/dump/traverse.c`** -> AI Confidence: **99.48%**
590. **`sbin/fsck_ffs/main.c`** -> AI Confidence: **99.48%**
591. **`sbin/fsck_ffs/pass1.c`** -> AI Confidence: **99.48%**
592. **`sbin/fsck_ffs/pass4.c`** -> AI Confidence: **99.48%**
593. **`sbin/fsck_ffs/pass5.c`** -> AI Confidence: **99.48%**
594. **`sbin/fsck_msdosfs/check.c`** -> AI Confidence: **99.48%**
595. **`sbin/fsck_msdosfs/main.c`** -> AI Confidence: **99.48%**
596. **`sbin/ggate/ggatel/ggatel.c`** -> AI Confidence: **99.48%**
597. **`sbin/hastctl/hastctl.c`** -> AI Confidence: **99.48%**
598. **`sbin/hastd/control.c`** -> AI Confidence: **99.48%**
599. **`sbin/hastd/event.c`** -> AI Confidence: **99.48%**
600. **`sbin/ipf/common/lexer.c`** -> AI Confidence: **99.48%**
601. **`sbin/ipf/ipf/bpf_filter.c`** -> AI Confidence: **99.48%**
602. **`sbin/ipf/ipfs/ipfs.c`** -> AI Confidence: **99.48%**
603. **`sbin/ipf/ipfsync/ipsyncm.c`** -> AI Confidence: **99.48%**
604. **`sbin/ipf/ipfsync/ipsyncs.c`** -> AI Confidence: **99.48%**
605. **`sbin/ipf/ipmon/ipmon.c`** -> AI Confidence: **99.48%**
606. **`sbin/ipf/ipnat/ipnat.c`** -> AI Confidence: **99.48%**
607. **`sbin/ipf/ippool/ippool.c`** -> AI Confidence: **99.48%**
608. **`sbin/ipf/ipsend/ipresend.c`** -> AI Confidence: **99.48%**
609. **`sbin/ipf/ipsend/ipsend.c`** -> AI Confidence: **99.48%**
610. **`sbin/ipf/ipsend/ipsopt.c`** -> AI Confidence: **99.48%**
611. **`sbin/ipfw/dummynet.c`** -> AI Confidence: **99.48%**
612. **`sbin/ipfw/ipfw2.c`** -> AI Confidence: **99.48%**
613. **`sbin/ipfw/main.c`** -> AI Confidence: **99.48%**
614. **`sbin/kldload/kldload.c`** -> AI Confidence: **99.48%**
615. **`sbin/kldunload/kldunload.c`** -> AI Confidence: **99.48%**
616. **`sbin/mdconfig/mdconfig.c`** -> AI Confidence: **99.48%**
617. **`sbin/mount/mount.c`** -> AI Confidence: **99.48%**
618. **`sbin/mount_fusefs/mount_fusefs.c`** -> AI Confidence: **99.48%**
619. **`sbin/mount_msdosfs/mount_msdosfs.c`** -> AI Confidence: **99.48%**
620. **`sbin/newfs/newfs.c`** -> AI Confidence: **99.48%**
621. **`sbin/newfs_msdos/mkfs_msdos.c`** -> AI Confidence: **99.48%**
622. **`sbin/newfs_msdos/newfs_msdos.c`** -> AI Confidence: **99.48%**
623. **`sbin/nfsiod/nfsiod.c`** -> AI Confidence: **99.48%**
624. **`sbin/nvmecontrol/identify_ext.c`** -> AI Confidence: **99.48%**
625. **`sbin/nvmecontrol/modules/micron/micron.c`** -> AI Confidence: **99.48%**
626. **`sbin/pfctl/pf_print_state.c`** -> AI Confidence: **99.48%**
627. **`sbin/pfctl/pfctl_optimize.c`** -> AI Confidence: **99.48%**
628. **`sbin/ping/main.c`** -> AI Confidence: **99.48%**
629. **`sbin/restore/main.c`** -> AI Confidence: **99.48%**
630. **`sbin/restore/tape.c`** -> AI Confidence: **99.48%**
631. **`sbin/setkey/setkey.c`** -> AI Confidence: **99.48%**
632. **`sbin/swapon/swapon.c`** -> AI Confidence: **99.48%**
633. **`sbin/tunefs/tunefs.c`** -> AI Confidence: **99.48%**
634. **`sbin/veriexec/veriexec.c`** -> AI Confidence: **99.48%**
635. **`sbin/zfsbootcfg/zfsbootcfg.c`** -> AI Confidence: **99.48%**
636. **`share/examples/ipfilter/l4check/l4check.c`** -> AI Confidence: **99.48%**
637. **`share/examples/ipfilter/mlfk_rule.c`** -> AI Confidence: **99.48%**
638. **`share/examples/ipfilter/samples/proxy.c`** -> AI Confidence: **99.48%**
639. **`share/examples/ipfilter/samples/userauth.c`** -> AI Confidence: **99.48%**
640. **`share/examples/libifconfig/ifchangevlan.c`** -> AI Confidence: **99.48%**
641. **`share/examples/libifconfig/ifcreate.c`** -> AI Confidence: **99.48%**
642. **`share/examples/libifconfig/ifcreatevlan.c`** -> AI Confidence: **99.48%**
643. **`share/examples/libifconfig/ifdestroy.c`** -> AI Confidence: **99.48%**
644. **`share/examples/libifconfig/setdescription.c`** -> AI Confidence: **99.48%**
645. **`share/examples/libifconfig/setmtu.c`** -> AI Confidence: **99.48%**
646. **`share/examples/perfmon/perfmon.c`** -> AI Confidence: **99.48%**
647. **`share/examples/ses/srcs/eltsub.c`** -> AI Confidence: **99.48%**
648. **`share/examples/ses/srcs/getnobj.c`** -> AI Confidence: **99.48%**
649. **`share/examples/ses/srcs/sesd.c`** -> AI Confidence: **99.48%**
650. **`share/examples/sound/sndstat_nv.c`** -> AI Confidence: **99.48%**
651. **`stand/common/modinfo.c`** -> AI Confidence: **99.48%**
652. **`stand/efi/boot1/proto.c`** -> AI Confidence: **99.48%**
653. **`stand/efi/libefi/efichar.c`** -> AI Confidence: **99.48%**
654. **`stand/i386/libi386/bootinfo.c`** -> AI Confidence: **99.48%**
655. **`stand/userboot/userboot/bootinfo.c`** -> AI Confidence: **99.48%**
656. **`sys/amd64/amd64/initcpu.c`** -> AI Confidence: **99.48%**
657. **`sys/amd64/vmm/x86.c`** -> AI Confidence: **99.48%**
658. **`sys/arm/allwinner/aw_mp.c`** -> AI Confidence: **99.48%**
659. **`sys/arm/arm/identcpu-v6.c`** -> AI Confidence: **99.48%**
660. **`sys/arm/arm/pmu.c`** -> AI Confidence: **99.48%**
661. **`sys/arm/broadcom/bcm2835/bcm2836_mp.c`** -> AI Confidence: **99.48%**
662. **`sys/arm/nvidia/tegra124/tegra124_mp.c`** -> AI Confidence: **99.48%**
663. **`sys/arm/ti/ti_cpuid.c`** -> AI Confidence: **99.48%**
664. **`sys/arm64/vmm/vmm_reset.c`** -> AI Confidence: **99.48%**
665. **`sys/compat/linprocfs/linprocfs.c`** -> AI Confidence: **99.48%**
666. **`sys/contrib/dev/acpica/components/disassembler/dmopcode.c`** -> AI Confidence: **99.48%**
667. **`sys/contrib/dev/acpica/components/dispatcher/dsfield.c`** -> AI Confidence: **99.48%**
668. **`sys/contrib/dev/acpica/components/dispatcher/dsmethod.c`** -> AI Confidence: **99.48%**
669. **`sys/contrib/dev/acpica/components/dispatcher/dsobject.c`** -> AI Confidence: **99.48%**
670. **`sys/contrib/dev/acpica/components/dispatcher/dsopcode.c`** -> AI Confidence: **99.48%**
671. **`sys/contrib/dev/acpica/components/dispatcher/dspkginit.c`** -> AI Confidence: **99.48%**
672. **`sys/contrib/dev/acpica/components/dispatcher/dsutils.c`** -> AI Confidence: **99.48%**
673. **`sys/contrib/dev/acpica/components/dispatcher/dswexec.c`** -> AI Confidence: **99.48%**
674. **`sys/contrib/dev/acpica/components/dispatcher/dswload.c`** -> AI Confidence: **99.48%**
675. **`sys/contrib/dev/acpica/components/dispatcher/dswload2.c`** -> AI Confidence: **99.48%**
676. **`sys/contrib/dev/acpica/components/executer/exconfig.c`** -> AI Confidence: **99.48%**
677. **`sys/contrib/dev/acpica/components/executer/exoparg1.c`** -> AI Confidence: **99.48%**
678. **`sys/contrib/dev/acpica/components/namespace/nsparse.c`** -> AI Confidence: **99.48%**
679. **`sys/contrib/dev/acpica/components/parser/psargs.c`** -> AI Confidence: **99.48%**
680. **`sys/contrib/dev/acpica/components/parser/psloop.c`** -> AI Confidence: **99.48%**
681. **`sys/contrib/dev/acpica/components/parser/psparse.c`** -> AI Confidence: **99.48%**
682. **`sys/contrib/dev/acpica/components/parser/psxface.c`** -> AI Confidence: **99.48%**
683. **`sys/contrib/dev/ath/ath_hal/ar9300/ar9300_attach.c`** -> AI Confidence: **99.48%**
684. **`sys/contrib/dev/broadcom/brcm80211/brcmfmac/proto.c`** -> AI Confidence: **99.48%**
685. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-dserve-dsrv9703c.dts`** -> AI Confidence: **99.48%**
686. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-inet1.dts`** -> AI Confidence: **99.48%**
687. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-pov-protab2-ips9.dts`** -> AI Confidence: **99.48%**
688. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-topwise-a721.dts`** -> AI Confidence: **99.48%**
689. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-a13-empire-electronix-d709.dts`** -> AI Confidence: **99.48%**
690. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-a13-pocketbook-614-plus.dts`** -> AI Confidence: **99.48%**
691. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-a13-pocketbook-touch-lux-3.dts`** -> AI Confidence: **99.48%**
692. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-wexler-tab7200.dts`** -> AI Confidence: **99.48%**
693. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-asrock-e3c256d4i.dts`** -> AI Confidence: **99.48%**
694. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-facebook-bletchley.dts`** -> AI Confidence: **99.48%**
695. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-facebook-catalina.dts`** -> AI Confidence: **99.48%**
696. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-ibm-sbp1.dts`** -> AI Confidence: **99.48%**
697. **`sys/contrib/device-tree/src/arm/mediatek/mt7629.dtsi`** -> AI Confidence: **99.48%**
698. **`sys/contrib/device-tree/src/arm/microchip/at91-sama5d2_xplained.dts`** -> AI Confidence: **99.48%**
699. **`sys/contrib/device-tree/src/arm/microchip/at91-sama7g5ek.dts`** -> AI Confidence: **99.48%**
700. **`sys/contrib/device-tree/src/arm/nvidia/tegra20-acer-a500-picasso.dts`** -> AI Confidence: **99.48%**
701. **`sys/contrib/device-tree/src/arm/nvidia/tegra20-asus-tf101.dts`** -> AI Confidence: **99.48%**
702. **`sys/contrib/device-tree/src/arm/nvidia/tegra30-pegatron-chagall.dts`** -> AI Confidence: **99.48%**
703. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6dl-prtmvt.dts`** -> AI Confidence: **99.48%**
704. **`sys/contrib/device-tree/src/arm/qcom/qcom-apq8060-dragonboard.dts`** -> AI Confidence: **99.48%**
705. **`sys/contrib/device-tree/src/arm/qcom/qcom-apq8064-asus-nexus7-flo.dts`** -> AI Confidence: **99.48%**
706. **`sys/contrib/device-tree/src/arm/qcom/qcom-apq8064-ifc6410.dts`** -> AI Confidence: **99.48%**
707. **`sys/contrib/device-tree/src/arm/qcom/qcom-apq8064-lg-nexus4-mako.dts`** -> AI Confidence: **99.48%**
708. **`sys/contrib/device-tree/src/arm/qcom/qcom-apq8064-sony-xperia-lagan-yuga.dts`** -> AI Confidence: **99.48%**
709. **`sys/contrib/device-tree/src/arm/qcom/qcom-apq8074-dragonboard.dts`** -> AI Confidence: **99.48%**
710. **`sys/contrib/device-tree/src/arm/qcom/qcom-msm8960-samsung-expressatt.dts`** -> AI Confidence: **99.48%**
711. **`sys/contrib/device-tree/src/arm/qcom/qcom-msm8974-lge-nexus5-hammerhead.dts`** -> AI Confidence: **99.48%**
712. **`sys/contrib/device-tree/src/arm/qcom/qcom-msm8974-samsung-hlte.dts`** -> AI Confidence: **99.48%**
713. **`sys/contrib/device-tree/src/arm/qcom/qcom-msm8974pro-fairphone-fp2.dts`** -> AI Confidence: **99.48%**
714. **`sys/contrib/device-tree/src/arm/samsung/exynos4412-itop-scp-core.dtsi`** -> AI Confidence: **99.48%**
715. **`sys/contrib/device-tree/src/arm/samsung/exynos4412-p4note.dtsi`** -> AI Confidence: **99.48%**
716. **`sys/contrib/device-tree/src/arm/samsung/exynos5250-arndale.dts`** -> AI Confidence: **99.48%**
717. **`sys/contrib/device-tree/src/arm/samsung/exynos5250-spring.dts`** -> AI Confidence: **99.48%**
718. **`sys/contrib/device-tree/src/arm/samsung/exynos5410-odroidxu.dts`** -> AI Confidence: **99.48%**
719. **`sys/contrib/device-tree/src/arm/samsung/exynos5420-arndale-octa.dts`** -> AI Confidence: **99.48%**
720. **`sys/contrib/device-tree/src/arm/samsung/exynos5420-peach-pit.dts`** -> AI Confidence: **99.48%**
721. **`sys/contrib/device-tree/src/arm/samsung/exynos5800-peach-pi.dts`** -> AI Confidence: **99.48%**
722. **`sys/contrib/device-tree/src/arm/st/ste-ux500-samsung-codina-tmo.dts`** -> AI Confidence: **99.48%**
723. **`sys/contrib/device-tree/src/arm/st/ste-ux500-samsung-codina.dts`** -> AI Confidence: **99.48%**
724. **`sys/contrib/device-tree/src/arm/st/ste-ux500-samsung-gavini.dts`** -> AI Confidence: **99.48%**
725. **`sys/contrib/device-tree/src/arm/st/ste-ux500-samsung-golden.dts`** -> AI Confidence: **99.48%**
726. **`sys/contrib/device-tree/src/arm/st/ste-ux500-samsung-janice.dts`** -> AI Confidence: **99.48%**
727. **`sys/contrib/device-tree/src/arm/st/ste-ux500-samsung-kyle.dts`** -> AI Confidence: **99.48%**
728. **`sys/contrib/device-tree/src/arm/st/ste-ux500-samsung-skomer.dts`** -> AI Confidence: **99.48%**
729. **`sys/contrib/device-tree/src/arm/st/stm32mp133c-prihmb.dts`** -> AI Confidence: **99.48%**
730. **`sys/contrib/device-tree/src/arm/st/stm32mp135f-dk.dts`** -> AI Confidence: **99.48%**
731. **`sys/contrib/device-tree/src/arm/st/stm32mp13xx-dhcor-som.dtsi`** -> AI Confidence: **99.48%**
732. **`sys/contrib/device-tree/src/arm/st/stm32mp151c-mecio1r0.dts`** -> AI Confidence: **99.48%**
733. **`sys/contrib/device-tree/src/arm/st/stm32mp151c-mect1s.dts`** -> AI Confidence: **99.48%**
734. **`sys/contrib/device-tree/src/arm/st/stm32mp151c-plyaqm.dts`** -> AI Confidence: **99.48%**
735. **`sys/contrib/device-tree/src/arm/st/stm32mp153c-mecio1r1.dts`** -> AI Confidence: **99.48%**
736. **`sys/contrib/device-tree/src/arm/st/stm32mp157c-emstamp-argon.dtsi`** -> AI Confidence: **99.48%**
737. **`sys/contrib/device-tree/src/arm/st/stm32mp157c-odyssey-som.dtsi`** -> AI Confidence: **99.48%**
738. **`sys/contrib/device-tree/src/arm/st/stm32mp157c-phycore-stm32mp15-som.dtsi`** -> AI Confidence: **99.48%**
739. **`sys/contrib/device-tree/src/arm/st/stm32mp157c-ultra-fly-sbc.dts`** -> AI Confidence: **99.48%**
740. **`sys/contrib/device-tree/src/arm/ti/omap/am571x-idk.dts`** -> AI Confidence: **99.48%**
741. **`sys/contrib/device-tree/src/arm/ti/omap/am5729-beagleboneai.dts`** -> AI Confidence: **99.48%**
742. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-a64-pinebook.dts`** -> AI Confidence: **99.48%**
743. **`sys/contrib/device-tree/src/arm64/exynos/exynosautov9.dtsi`** -> AI Confidence: **99.48%**
744. **`sys/contrib/device-tree/src/arm64/hisilicon/hi6220.dtsi`** -> AI Confidence: **99.48%**
745. **`sys/contrib/device-tree/src/arm64/mediatek/mt8195-demo.dts`** -> AI Confidence: **99.48%**
746. **`sys/contrib/device-tree/src/arm64/mediatek/mt8395-genio-1200-evk.dts`** -> AI Confidence: **99.48%**
747. **`sys/contrib/device-tree/src/arm64/mediatek/mt8395-kontron-3-5-sbc-i1200.dts`** -> AI Confidence: **99.48%**
748. **`sys/contrib/device-tree/src/arm64/mediatek/mt8395-radxa-nio-12l.dts`** -> AI Confidence: **99.48%**
749. **`sys/contrib/device-tree/src/arm64/qcom/apq8016-sbc.dts`** -> AI Confidence: **99.48%**
750. **`sys/contrib/device-tree/src/arm64/qcom/apq8016-sbc.dtsi`** -> AI Confidence: **99.48%**
751. **`sys/contrib/device-tree/src/arm64/qcom/apq8016-schneider-hmibsc.dts`** -> AI Confidence: **99.48%**
752. **`sys/contrib/device-tree/src/arm64/qcom/apq8039-t2.dts`** -> AI Confidence: **99.48%**
753. **`sys/contrib/device-tree/src/arm64/qcom/apq8096-db820c.dts`** -> AI Confidence: **99.48%**
754. **`sys/contrib/device-tree/src/arm64/qcom/apq8096-db820c.dtsi`** -> AI Confidence: **99.48%**
755. **`sys/contrib/device-tree/src/arm64/qcom/apq8096-ifc6640.dts`** -> AI Confidence: **99.48%**
756. **`sys/contrib/device-tree/src/arm64/qcom/msm8916-longcheer-l8910.dts`** -> AI Confidence: **99.48%**
757. **`sys/contrib/device-tree/src/arm64/qcom/msm8917.dtsi`** -> AI Confidence: **99.48%**
758. **`sys/contrib/device-tree/src/arm64/qcom/msm8939-longcheer-l9100.dts`** -> AI Confidence: **99.48%**
759. **`sys/contrib/device-tree/src/arm64/qcom/msm8939-sony-xperia-kanuti-tulip.dts`** -> AI Confidence: **99.48%**
760. **`sys/contrib/device-tree/src/arm64/qcom/msm8996-xiaomi-gemini.dts`** -> AI Confidence: **99.48%**
761. **`sys/contrib/device-tree/src/arm64/qcom/msm8996pro-xiaomi-scorpio.dts`** -> AI Confidence: **99.48%**
762. **`sys/contrib/device-tree/src/arm64/qcom/msm8998-fxtec-pro1.dts`** -> AI Confidence: **99.48%**
763. **`sys/contrib/device-tree/src/arm64/qcom/msm8998-xiaomi-sagit.dts`** -> AI Confidence: **99.48%**
764. **`sys/contrib/device-tree/src/arm64/qcom/qcm2290.dtsi`** -> AI Confidence: **99.48%**
765. **`sys/contrib/device-tree/src/arm64/qcom/qcm6490-fairphone-fp5.dts`** -> AI Confidence: **99.48%**
766. **`sys/contrib/device-tree/src/arm64/qcom/qcm6490-idp.dts`** -> AI Confidence: **99.48%**
767. **`sys/contrib/device-tree/src/arm64/qcom/qcm6490-shift-otter.dts`** -> AI Confidence: **99.48%**
768. **`sys/contrib/device-tree/src/arm64/qcom/qcs615.dtsi`** -> AI Confidence: **99.48%**
769. **`sys/contrib/device-tree/src/arm64/qcom/qcs6490-rb3gen2.dts`** -> AI Confidence: **99.48%**
770. **`sys/contrib/device-tree/src/arm64/qcom/qcs8300.dtsi`** -> AI Confidence: **99.48%**
771. **`sys/contrib/device-tree/src/arm64/qcom/qcs8550-aim300.dtsi`** -> AI Confidence: **99.48%**
772. **`sys/contrib/device-tree/src/arm64/qcom/qrb4210-rb2.dts`** -> AI Confidence: **99.48%**
773. **`sys/contrib/device-tree/src/arm64/qcom/qrb5165-rb5.dts`** -> AI Confidence: **99.48%**
774. **`sys/contrib/device-tree/src/arm64/qcom/sa8295p-adp.dts`** -> AI Confidence: **99.48%**
775. **`sys/contrib/device-tree/src/arm64/qcom/sar2130p.dtsi`** -> AI Confidence: **99.48%**
776. **`sys/contrib/device-tree/src/arm64/qcom/sc7180-acer-aspire1.dts`** -> AI Confidence: **99.48%**
777. **`sys/contrib/device-tree/src/arm64/qcom/sc7180-idp.dts`** -> AI Confidence: **99.48%**
778. **`sys/contrib/device-tree/src/arm64/qcom/sc7280-herobrine-herobrine-r0.dts`** -> AI Confidence: **99.48%**
779. **`sys/contrib/device-tree/src/arm64/qcom/sc8180x-lenovo-flex-5g.dts`** -> AI Confidence: **99.48%**
780. **`sys/contrib/device-tree/src/arm64/qcom/sc8180x-primus.dts`** -> AI Confidence: **99.48%**
781. **`sys/contrib/device-tree/src/arm64/qcom/sc8280xp-huawei-gaokun3.dts`** -> AI Confidence: **99.48%**
782. **`sys/contrib/device-tree/src/arm64/qcom/sc8280xp-lenovo-thinkpad-x13s.dts`** -> AI Confidence: **99.48%**
783. **`sys/contrib/device-tree/src/arm64/qcom/sc8280xp-microsoft-blackrock.dts`** -> AI Confidence: **99.48%**
784. **`sys/contrib/device-tree/src/arm64/qcom/sdm670-google-sargo.dts`** -> AI Confidence: **99.48%**
785. **`sys/contrib/device-tree/src/arm64/qcom/sdm670.dtsi`** -> AI Confidence: **99.48%**
786. **`sys/contrib/device-tree/src/arm64/qcom/sdm845-db845c.dts`** -> AI Confidence: **99.48%**
787. **`sys/contrib/device-tree/src/arm64/qcom/sdm845-samsung-starqltechn.dts`** -> AI Confidence: **99.48%**
788. **`sys/contrib/device-tree/src/arm64/qcom/sdm845-shift-axolotl.dts`** -> AI Confidence: **99.48%**
789. **`sys/contrib/device-tree/src/arm64/qcom/sdm845-xiaomi-beryllium.dts`** -> AI Confidence: **99.48%**
790. **`sys/contrib/device-tree/src/arm64/qcom/sdm845-xiaomi-polaris.dts`** -> AI Confidence: **99.48%**
791. **`sys/contrib/device-tree/src/arm64/qcom/sdm850-lenovo-yoga-c630.dts`** -> AI Confidence: **99.48%**
792. **`sys/contrib/device-tree/src/arm64/qcom/sdm850-samsung-w737.dts`** -> AI Confidence: **99.48%**
793. **`sys/contrib/device-tree/src/arm64/qcom/sdx75.dtsi`** -> AI Confidence: **99.48%**
794. **`sys/contrib/device-tree/src/arm64/qcom/sm4450.dtsi`** -> AI Confidence: **99.48%**
795. **`sys/contrib/device-tree/src/arm64/qcom/sm6115-fxtec-pro1x.dts`** -> AI Confidence: **99.48%**
796. **`sys/contrib/device-tree/src/arm64/qcom/sm6125-xiaomi-ginkgo.dts`** -> AI Confidence: **99.48%**
797. **`sys/contrib/device-tree/src/arm64/qcom/sm6125-xiaomi-laurel-sprout.dts`** -> AI Confidence: **99.48%**
798. **`sys/contrib/device-tree/src/arm64/qcom/sm6375.dtsi`** -> AI Confidence: **99.48%**
799. **`sys/contrib/device-tree/src/arm64/qcom/sm7225-fairphone-fp4.dts`** -> AI Confidence: **99.48%**
800. **`sys/contrib/device-tree/src/arm64/qcom/sm7325-nothing-spacewar.dts`** -> AI Confidence: **99.48%**
801. **`sys/contrib/device-tree/src/arm64/qcom/sm8150-hdk.dts`** -> AI Confidence: **99.48%**
802. **`sys/contrib/device-tree/src/arm64/qcom/sm8150-microsoft-surface-duo.dts`** -> AI Confidence: **99.48%**
803. **`sys/contrib/device-tree/src/arm64/qcom/sm8250-mtp.dts`** -> AI Confidence: **99.48%**
804. **`sys/contrib/device-tree/src/arm64/qcom/sm8250-xiaomi-elish.dts`** -> AI Confidence: **99.48%**
805. **`sys/contrib/device-tree/src/arm64/qcom/sm8250-xiaomi-pipa.dts`** -> AI Confidence: **99.48%**
806. **`sys/contrib/device-tree/src/arm64/qcom/sm8350-hdk.dts`** -> AI Confidence: **99.48%**
807. **`sys/contrib/device-tree/src/arm64/qcom/sm8450-hdk.dts`** -> AI Confidence: **99.48%**
808. **`sys/contrib/device-tree/src/arm64/qcom/sm8450-qrd.dts`** -> AI Confidence: **99.48%**
809. **`sys/contrib/device-tree/src/arm64/qcom/sm8550-hdk.dts`** -> AI Confidence: **99.48%**
810. **`sys/contrib/device-tree/src/arm64/qcom/sm8550-mtp.dts`** -> AI Confidence: **99.48%**
811. **`sys/contrib/device-tree/src/arm64/qcom/sm8550-qrd.dts`** -> AI Confidence: **99.48%**
812. **`sys/contrib/device-tree/src/arm64/qcom/sm8550-samsung-q5q.dts`** -> AI Confidence: **99.48%**
813. **`sys/contrib/device-tree/src/arm64/qcom/sm8550-sony-xperia-yodo-pdx234.dts`** -> AI Confidence: **99.48%**
814. **`sys/contrib/device-tree/src/arm64/qcom/sm8650-hdk.dts`** -> AI Confidence: **99.48%**
815. **`sys/contrib/device-tree/src/arm64/qcom/sm8650-mtp.dts`** -> AI Confidence: **99.48%**
816. **`sys/contrib/device-tree/src/arm64/qcom/sm8650-qrd.dts`** -> AI Confidence: **99.48%**
817. **`sys/contrib/device-tree/src/arm64/qcom/sm8750-mtp.dts`** -> AI Confidence: **99.48%**
818. **`sys/contrib/device-tree/src/arm64/qcom/sm8750-qrd.dts`** -> AI Confidence: **99.48%**
819. **`sys/contrib/device-tree/src/arm64/qcom/x1e80100-asus-vivobook-s15.dts`** -> AI Confidence: **99.48%**
820. **`sys/contrib/device-tree/src/arm64/qcom/x1e80100-dell-xps13-9345.dts`** -> AI Confidence: **99.48%**
821. **`sys/contrib/device-tree/src/arm64/qcom/x1e80100-hp-omnibook-x14.dts`** -> AI Confidence: **99.48%**
822. **`sys/contrib/device-tree/src/arm64/renesas/r9a09g047e57-smarc.dts`** -> AI Confidence: **99.48%**
823. **`sys/contrib/device-tree/src/arm64/rockchip/rk3528.dtsi`** -> AI Confidence: **99.48%**
824. **`sys/contrib/device-tree/src/arm64/rockchip/rk3562.dtsi`** -> AI Confidence: **99.48%**
825. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-lckfb-tspi.dts`** -> AI Confidence: **99.48%**
826. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-nanopi-r3s.dts`** -> AI Confidence: **99.48%**
827. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-powkiddy-x55.dts`** -> AI Confidence: **99.48%**
828. **`sys/contrib/device-tree/src/arm64/rockchip/rk3568-wolfvision-pf5.dts`** -> AI Confidence: **99.48%**
829. **`sys/contrib/device-tree/src/arm64/rockchip/rk356x.dtsi`** -> AI Confidence: **99.48%**
830. **`sys/contrib/device-tree/src/arm64/rockchip/rk3576-armsom-sige5.dts`** -> AI Confidence: **99.48%**
831. **`sys/contrib/device-tree/src/arm64/rockchip/rk3576-evb1-v10.dts`** -> AI Confidence: **99.48%**
832. **`sys/contrib/device-tree/src/arm64/rockchip/rk3576-nanopi-m5.dts`** -> AI Confidence: **99.48%**
833. **`sys/contrib/device-tree/src/arm64/rockchip/rk3576-roc-pc.dts`** -> AI Confidence: **99.48%**
834. **`sys/contrib/device-tree/src/arm64/rockchip/rk3576-rock-4d.dts`** -> AI Confidence: **99.48%**
835. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-evb1-v10.dts`** -> AI Confidence: **99.48%**
836. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-evb2-v10.dts`** -> AI Confidence: **99.48%**
837. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-firefly-itx-3588j.dts`** -> AI Confidence: **99.48%**
838. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-friendlyelec-cm3588-nas.dts`** -> AI Confidence: **99.48%**
839. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-jaguar.dts`** -> AI Confidence: **99.48%**
840. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-mnt-reform2.dts`** -> AI Confidence: **99.48%**
841. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-rock-5-itx.dts`** -> AI Confidence: **99.48%**
842. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588s-evb1-v10.dts`** -> AI Confidence: **99.48%**
843. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588s-gameforce-ace.dts`** -> AI Confidence: **99.48%**
844. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588s-indiedroid-nova.dts`** -> AI Confidence: **99.48%**
845. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588s-khadas-edge2.dts`** -> AI Confidence: **99.48%**
846. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588s-odroid-m2.dts`** -> AI Confidence: **99.48%**
847. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588s-roc-pc.dts`** -> AI Confidence: **99.48%**
848. **`sys/contrib/device-tree/src/arm64/st/stm32mp235f-dk.dts`** -> AI Confidence: **99.48%**
849. **`sys/contrib/device-tree/src/arm64/st/stm32mp257f-dk.dts`** -> AI Confidence: **99.48%**
850. **`sys/contrib/device-tree/src/arm64/st/stm32mp257f-ev1.dts`** -> AI Confidence: **99.48%**
851. **`sys/contrib/device-tree/src/arm64/ti/k3-am642-phyboard-electra-rdk.dts`** -> AI Confidence: **99.48%**
852. **`sys/contrib/device-tree/src/arm64/ti/k3-am642-tqma64xxl-mbax4xxl.dts`** -> AI Confidence: **99.48%**
853. **`sys/contrib/device-tree/src/arm64/xilinx/zynqmp-zcu100-revC.dts`** -> AI Confidence: **99.48%**
854. **`sys/contrib/device-tree/src/mips/ingenic/ci20.dts`** -> AI Confidence: **99.48%**
855. **`sys/contrib/device-tree/src/mips/ingenic/gcw0.dts`** -> AI Confidence: **99.48%**
856. **`sys/contrib/device-tree/src/mips/ingenic/qi_lb60.dts`** -> AI Confidence: **99.48%**
857. **`sys/contrib/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-compress-avx2.c`** -> AI Confidence: **99.48%**
858. **`sys/contrib/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-fill-block-avx2.c`** -> AI Confidence: **99.48%**
859. **`sys/contrib/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-fill-block-avx512f.c`** -> AI Confidence: **99.48%**
860. **`sys/contrib/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-fill-block-ref.c`** -> AI Confidence: **99.48%**
861. **`sys/contrib/libsodium/src/libsodium/crypto_pwhash/argon2/argon2-fill-block-ssse3.c`** -> AI Confidence: **99.48%**
862. **`sys/contrib/libsodium/src/libsodium/sodium/codecs.c`** -> AI Confidence: **99.48%**
863. **`sys/contrib/ncsw/Peripherals/FM/Pcd/fm_cc.c`** -> AI Confidence: **99.48%**
864. **`sys/contrib/ncsw/Peripherals/FM/Pcd/fm_manip.c`** -> AI Confidence: **99.48%**
865. **`sys/contrib/ncsw/Peripherals/FM/Pcd/fm_pcd.c`** -> AI Confidence: **99.48%**
866. **`sys/contrib/ncsw/Peripherals/FM/Port/fm_port.c`** -> AI Confidence: **99.48%**
867. **`sys/contrib/ncsw/Peripherals/QM/qm.c`** -> AI Confidence: **99.48%**
868. **`sys/contrib/ncsw/etc/ncsw_mem.c`** -> AI Confidence: **99.48%**
869. **`sys/contrib/openzfs/cmd/zed/agents/zfs_diagnosis.c`** -> AI Confidence: **99.48%**
870. **`sys/contrib/openzfs/cmd/zgenhostid.c`** -> AI Confidence: **99.48%**
871. **`sys/contrib/openzfs/module/lua/lvm.c`** -> AI Confidence: **99.48%**
872. **`sys/contrib/openzfs/module/os/freebsd/spl/acl_common.c`** -> AI Confidence: **99.48%**
873. **`sys/contrib/openzfs/module/os/freebsd/zfs/dmu_os.c`** -> AI Confidence: **99.48%**
874. **`sys/contrib/openzfs/module/unicode/u8_textprep.c`** -> AI Confidence: **99.48%**
875. **`sys/contrib/openzfs/module/zcommon/zfeature_common.c`** -> AI Confidence: **99.48%**
876. **`sys/contrib/openzfs/module/zfs/dmu_zfetch.c`** -> AI Confidence: **99.48%**
877. **`sys/contrib/openzfs/module/zfs/spa_config.c`** -> AI Confidence: **99.48%**
878. **`sys/contrib/openzfs/module/zfs/vdev.c`** -> AI Confidence: **99.48%**
879. **`sys/contrib/openzfs/module/zfs/vdev_label.c`** -> AI Confidence: **99.48%**
880. **`sys/contrib/openzfs/module/zfs/vdev_trim.c`** -> AI Confidence: **99.48%**
881. **`sys/contrib/openzfs/module/zfs/zfs_vnops.c`** -> AI Confidence: **99.48%**
882. **`sys/contrib/openzfs/module/zfs/zio_checksum.c`** -> AI Confidence: **99.48%**
883. **`sys/contrib/openzfs/tests/zfs-tests/cmd/cp_files.c`** -> AI Confidence: **99.48%**
884. **`sys/contrib/openzfs/tests/zfs-tests/cmd/linux_dos_attributes/write_dos_attributes.c`** -> AI Confidence: **99.48%**
885. **`sys/contrib/openzfs/tests/zfs-tests/cmd/suid_write_to_file.c`** -> AI Confidence: **99.48%**
886. **`sys/contrib/openzfs/tests/zfs-tests/tests/functional/cp_files/seekflood.c`** -> AI Confidence: **99.48%**
887. **`sys/contrib/zstd/programs/dibio.c`** -> AI Confidence: **99.48%**
888. **`sys/contrib/zstd/programs/zstdcli.c`** -> AI Confidence: **99.48%**
889. **`sys/contrib/zstd/zlibWrapper/examples/minigzip.c`** -> AI Confidence: **99.48%**
890. **`sys/contrib/zstd/zlibWrapper/examples/zwrapbench.c`** -> AI Confidence: **99.48%**
891. **`sys/crypto/openssl/ossl_chacha20.c`** -> AI Confidence: **99.48%**
892. **`sys/ddb/db_ps.c`** -> AI Confidence: **99.48%**
893. **`sys/dev/aac/aac_debug.c`** -> AI Confidence: **99.48%**
894. **`sys/dev/aacraid/aacraid_debug.c`** -> AI Confidence: **99.48%**
895. **`sys/dev/acpica/acpi_resource.c`** -> AI Confidence: **99.48%**
896. **`sys/dev/aic7xxx/aicasm/aicasm_symbol.c`** -> AI Confidence: **99.48%**
897. **`sys/dev/aq/aq_media.c`** -> AI Confidence: **99.48%**
898. **`sys/dev/ata/ata-lowlevel.c`** -> AI Confidence: **99.48%**
899. **`sys/dev/ath/ath_hal/ar9002/ar9285_btcoex.c`** -> AI Confidence: **99.48%**
900. **`sys/dev/ath/ath_hal/ar9002/ar9285_diversity.c`** -> AI Confidence: **99.48%**
901. **`sys/dev/ath/if_ath_dfs.c`** -> AI Confidence: **99.48%**
902. **`sys/dev/ath/if_ath_drv.c`** -> AI Confidence: **99.48%**
903. **`sys/dev/ath/if_ath_lna_div.c`** -> AI Confidence: **99.48%**
904. **`sys/dev/ath/if_ath_rate.c`** -> AI Confidence: **99.48%**
905. **`sys/dev/bnxt/bnxt_en/bnxt_auxbus_compat.c`** -> AI Confidence: **99.48%**
906. **`sys/dev/cyapa/cyapa.c`** -> AI Confidence: **99.48%**
907. **`sys/dev/hptmv/hptproc.c`** -> AI Confidence: **99.48%**
908. **`sys/dev/hptmv/ioctl.c`** -> AI Confidence: **99.48%**
909. **`sys/dev/hwpmc/hwpmc_intel.c`** -> AI Confidence: **99.48%**
910. **`sys/dev/hyperv/input/hv_kbd.c`** -> AI Confidence: **99.48%**
911. **`sys/dev/ipmi/ipmi_isa.c`** -> AI Confidence: **99.48%**
912. **`sys/dev/isci/scil/sati.c`** -> AI Confidence: **99.48%**
913. **`sys/dev/isci/scil/scic_sds_stp_remote_device.c`** -> AI Confidence: **99.48%**
914. **`sys/dev/isci/scil/scif_sas_stp_task_request.c`** -> AI Confidence: **99.48%**
915. **`sys/dev/isp/isp_pci.c`** -> AI Confidence: **99.48%**
916. **`sys/dev/ispfw/ispfw.c`** -> AI Confidence: **99.48%**
917. **`sys/dev/mii/icsphy.c`** -> AI Confidence: **99.48%**
918. **`sys/dev/mii/nsgphy.c`** -> AI Confidence: **99.48%**
919. **`sys/dev/mii/nsphyter.c`** -> AI Confidence: **99.48%**
920. **`sys/dev/mii/tdkphy.c`** -> AI Confidence: **99.48%**
921. **`sys/dev/mii/ukphy_subr.c`** -> AI Confidence: **99.48%**
922. **`sys/dev/mpr/mpr_config.c`** -> AI Confidence: **99.48%**
923. **`sys/dev/mps/mps_config.c`** -> AI Confidence: **99.48%**
924. **`sys/dev/mpt/mpt_cam.c`** -> AI Confidence: **99.48%**
925. **`sys/dev/netmap/netmap.c`** -> AI Confidence: **99.48%**
926. **`sys/dev/pms/RefTisa/discovery/dm/dmsmp.c`** -> AI Confidence: **99.48%**
927. **`sys/dev/pms/RefTisa/sallsdk/spc/sahw.c`** -> AI Confidence: **99.48%**
928. **`sys/dev/pms/RefTisa/sat/src/smsatcb.c`** -> AI Confidence: **99.48%**
929. **`sys/dev/pms/RefTisa/sat/src/smsathw.c`** -> AI Confidence: **99.48%**
930. **`sys/dev/pms/RefTisa/tisa/sassata/common/tdinit.c`** -> AI Confidence: **99.48%**
931. **`sys/dev/pms/RefTisa/tisa/sassata/common/tdport.c`** -> AI Confidence: **99.48%**
932. **`sys/dev/pms/RefTisa/tisa/sassata/sas/tgt/ttdio.c`** -> AI Confidence: **99.48%**
933. **`sys/dev/pms/RefTisa/tisa/sassata/sata/host/ossasat.c`** -> AI Confidence: **99.48%**
934. **`sys/dev/pms/RefTisa/tisa/sassata/sata/host/sathw.c`** -> AI Confidence: **99.48%**
935. **`sys/dev/ppbus/ppb_1284.c`** -> AI Confidence: **99.48%**
936. **`sys/dev/ppc/ppc.c`** -> AI Confidence: **99.48%**
937. **`sys/dev/qat/qat_api/common/compression/dc_session.c`** -> AI Confidence: **99.48%**
938. **`sys/dev/qat/qat_api/common/crypto/sym/lac_sym_alg_chain.c`** -> AI Confidence: **99.48%**
939. **`sys/dev/qat/qat_api/common/crypto/sym/lac_sym_cb.c`** -> AI Confidence: **99.48%**
940. **`sys/dev/qat/qat_api/common/crypto/sym/lac_sym_cipher.c`** -> AI Confidence: **99.48%**
941. **`sys/dev/qat/qat_api/common/crypto/sym/lac_sym_dp.c`** -> AI Confidence: **99.48%**
942. **`sys/dev/qat/qat_api/common/crypto/sym/lac_sym_partial.c`** -> AI Confidence: **99.48%**
943. **`sys/dev/qat/qat_api/common/crypto/sym/lac_sym_queue.c`** -> AI Confidence: **99.48%**
944. **`sys/dev/qat/qat_api/common/ctrl/sal_get_instances.c`** -> AI Confidence: **99.48%**
945. **`sys/dev/qlnx/qlnxe/ecore_mng_tlv.c`** -> AI Confidence: **99.48%**
946. **`sys/dev/qlxgb/qla_dbg.c`** -> AI Confidence: **99.48%**
947. **`sys/dev/qlxgbe/ql_dbg.c`** -> AI Confidence: **99.48%**
948. **`sys/dev/qlxge/qls_dbg.c`** -> AI Confidence: **99.48%**
949. **`sys/dev/qlxge/qls_isr.c`** -> AI Confidence: **99.48%**
950. **`sys/dev/rtwn/if_rtwn_fw.c`** -> AI Confidence: **99.48%**
951. **`sys/dev/rtwn/rtl8812a/r12a_chan.c`** -> AI Confidence: **99.48%**
952. **`sys/dev/sound/pci/hda/hdaa.c`** -> AI Confidence: **99.48%**
953. **`sys/dev/sound/pci/hda/hdaa_patches.c`** -> AI Confidence: **99.48%**
954. **`sys/dev/syscons/daemon/daemon_saver.c`** -> AI Confidence: **99.48%**
955. **`sys/dev/syscons/rain/rain_saver.c`** -> AI Confidence: **99.48%**
956. **`sys/dev/syscons/scmouse.c`** -> AI Confidence: **99.48%**
957. **`sys/dev/syscons/scterm-sc.c`** -> AI Confidence: **99.48%**
958. **`sys/dev/uart/uart_subr.c`** -> AI Confidence: **99.48%**
959. **`sys/dev/usb/controller/generic_ehci.c`** -> AI Confidence: **99.48%**
960. **`sys/dev/usb/usb_handle_request.c`** -> AI Confidence: **99.48%**
961. **`sys/dev/virtio/mmio/virtio_mmio_cmdline.c`** -> AI Confidence: **99.48%**
962. **`sys/fs/ext2fs/ext2_hash.c`** -> AI Confidence: **99.48%**
963. **`sys/fs/nfs/nfs_commonsubs.c`** -> AI Confidence: **99.48%**
964. **`sys/fs/nfsclient/nfs_clkdtrace.c`** -> AI Confidence: **99.48%**
965. **`sys/fs/nfsserver/nfs_nfsdkrpc.c`** -> AI Confidence: **99.48%**
966. **`sys/fs/procfs/procfs_map.c`** -> AI Confidence: **99.48%**
967. **`sys/fs/procfs/procfs_type.c`** -> AI Confidence: **99.48%**
968. **`sys/fs/pseudofs/pseudofs_fileno.c`** -> AI Confidence: **99.48%**
969. **`sys/fs/tmpfs/tmpfs_vnops.c`** -> AI Confidence: **99.48%**
970. **`sys/geom/label/g_label_msdosfs.c`** -> AI Confidence: **99.48%**
971. **`sys/isa/isahint.c`** -> AI Confidence: **99.48%**
972. **`sys/kern/kern_kexec.c`** -> AI Confidence: **99.48%**
973. **`sys/kern/kern_physio.c`** -> AI Confidence: **99.48%**
974. **`sys/kern/subr_acl_nfs4.c`** -> AI Confidence: **99.48%**
975. **`sys/kern/subr_acl_posix1e.c`** -> AI Confidence: **99.48%**
976. **`sys/kern/subr_boot.c`** -> AI Confidence: **99.48%**
977. **`sys/kern/subr_param.c`** -> AI Confidence: **99.48%**
978. **`sys/kern/subr_prf.c`** -> AI Confidence: **99.48%**
979. **`sys/kern/subr_stats.c`** -> AI Confidence: **99.48%**
980. **`sys/kern/subr_syscall.c`** -> AI Confidence: **99.48%**
981. **`sys/kern/uipc_debug.c`** -> AI Confidence: **99.48%**
982. **`sys/modules/dtrace/dtraceall/dtraceall.c`** -> AI Confidence: **99.48%**
983. **`sys/net80211/ieee80211_sta.c`** -> AI Confidence: **99.48%**
984. **`sys/netgraph/bluetooth/hci/ng_hci_cmds.c`** -> AI Confidence: **99.48%**
985. **`sys/netgraph/bluetooth/hci/ng_hci_main.c`** -> AI Confidence: **99.48%**
986. **`sys/netgraph/bluetooth/hci/ng_hci_ulpi.c`** -> AI Confidence: **99.48%**
987. **`sys/netgraph/bluetooth/l2cap/ng_l2cap_cmds.c`** -> AI Confidence: **99.48%**
988. **`sys/netgraph/bluetooth/l2cap/ng_l2cap_ulpi.c`** -> AI Confidence: **99.48%**
989. **`sys/netgraph/ng_lmi.c`** -> AI Confidence: **99.48%**
990. **`sys/netgraph/ng_rfc1490.c`** -> AI Confidence: **99.48%**
991. **`sys/netgraph/ng_vlan.c`** -> AI Confidence: **99.48%**
992. **`sys/netinet/cc/cc_cdg.c`** -> AI Confidence: **99.48%**
993. **`sys/netinet/cc/cc_newreno.c`** -> AI Confidence: **99.48%**
994. **`sys/netinet/ip_ecn.c`** -> AI Confidence: **99.48%**
995. **`sys/netinet/libalias/alias_proxy.c`** -> AI Confidence: **99.48%**
996. **`sys/netinet/tcp_ecn.c`** -> AI Confidence: **99.48%**
997. **`sys/netinet/tcp_input.c`** -> AI Confidence: **99.48%**
998. **`sys/netinet/tcp_output.c`** -> AI Confidence: **99.48%**
999. **`sys/netinet/tcp_stacks/sack_filter.c`** -> AI Confidence: **99.48%**
1000. **`sys/netinet6/ip6_forward.c`** -> AI Confidence: **99.48%**
1001. **`sys/netlink/netlink_route.h`** -> AI Confidence: **99.48%**
1002. **`sys/netpfil/ipfilter/netinet/ip_nat.c`** -> AI Confidence: **99.48%**
1003. **`sys/netpfil/ipfilter/netinet/ip_nat6.c`** -> AI Confidence: **99.48%**
1004. **`sys/netpfil/ipfilter/netinet/ip_state.c`** -> AI Confidence: **99.48%**
1005. **`sys/netpfil/ipfw/ip_fw2.c`** -> AI Confidence: **99.48%**
1006. **`sys/netpfil/pf/pf_lb.c`** -> AI Confidence: **99.48%**
1007. **`sys/powerpc/fpu/fpu_emu.c`** -> AI Confidence: **99.48%**
1008. **`sys/powerpc/powerpc/cpu.c`** -> AI Confidence: **99.48%**
1009. **`sys/powerpc/powerpc/db_trace.c`** -> AI Confidence: **99.48%**
1010. **`sys/security/audit/audit_bsm.c`** -> AI Confidence: **99.48%**
1011. **`sys/ufs/ffs/ffs_balloc.c`** -> AI Confidence: **99.48%**
1012. **`sys/vm/vm_unix.c`** -> AI Confidence: **99.48%**
1013. **`sys/x86/linux/linux_dummy_x86.c`** -> AI Confidence: **99.48%**
1014. **`sys/x86/x86/identcpu.c`** -> AI Confidence: **99.48%**
1015. **`tests/sys/file/flock_helper.c`** -> AI Confidence: **99.48%**
1016. **`tests/sys/geom/class/eli/unaligned_io.c`** -> AI Confidence: **99.48%**
1017. **`tests/sys/kern/reaper.c`** -> AI Confidence: **99.48%**
1018. **`tests/sys/kern/tty/readsz.c`** -> AI Confidence: **99.48%**
1019. **`tests/sys/mqueue/mqtest3.c`** -> AI Confidence: **99.48%**
1020. **`tests/sys/netgraph/bridge.c`** -> AI Confidence: **99.48%**
1021. **`tests/sys/sound/sndstat.c`** -> AI Confidence: **99.48%**
1022. **`tools/regression/capsicum/syscalls/cap_getmode.c`** -> AI Confidence: **99.48%**
1023. **`tools/regression/capsicum/syscalls/cap_ioctls_limit.c`** -> AI Confidence: **99.48%**
1024. **`tools/regression/environ/envctl.c`** -> AI Confidence: **99.48%**
1025. **`tools/regression/fsx/fsx.c`** -> AI Confidence: **99.48%**
1026. **`tools/regression/kgssapi/gsstest.c`** -> AI Confidence: **99.48%**
1027. **`tools/regression/mlock/mlock.c`** -> AI Confidence: **99.48%**
1028. **`tools/regression/netinet/tcpconnect/tcpconnect.c`** -> AI Confidence: **99.48%**
1029. **`tools/regression/p1003_1b/yield.c`** -> AI Confidence: **99.48%**
1030. **`tools/regression/poll/pipepoll.c`** -> AI Confidence: **99.48%**
1031. **`tools/regression/poll/pipeselect.c`** -> AI Confidence: **99.48%**
1032. **`tools/regression/poll/sockpoll.c`** -> AI Confidence: **99.48%**
1033. **`tools/regression/security/cap_test/cap_test_capabilities.c`** -> AI Confidence: **99.48%**
1034. **`tools/regression/security/cap_test/cap_test_capmode.c`** -> AI Confidence: **99.48%**
1035. **`tools/regression/sockets/accept_fd_leak/accept_fd_leak.c`** -> AI Confidence: **99.48%**
1036. **`tools/regression/sockets/kqueue/kqueue.c`** -> AI Confidence: **99.48%**
1037. **`tools/regression/sockets/listen_kqueue/listen_kqueue.c`** -> AI Confidence: **99.48%**
1038. **`tools/regression/sockets/unix_cmsg/t_generic.c`** -> AI Confidence: **99.48%**
1039. **`tools/regression/sockets/unix_cmsg/t_sockcred.c`** -> AI Confidence: **99.48%**
1040. **`tools/test/arc4random/biastest.c`** -> AI Confidence: **99.48%**
1041. **`tools/test/netfibs/reflect.c`** -> AI Confidence: **99.48%**
1042. **`tools/test/popss/popss.c`** -> AI Confidence: **99.48%**
1043. **`tools/test/ppsapi/ppsapitest.c`** -> AI Confidence: **99.48%**
1044. **`tools/test/stress2/lib/options.c`** -> AI Confidence: **99.48%**
1045. **`tools/test/stress2/testcases/creat/creat.c`** -> AI Confidence: **99.48%**
1046. **`tools/test/stress2/testcases/dirnprename/dirnprename.c`** -> AI Confidence: **99.48%**
1047. **`tools/test/stress2/testcases/fts/fts.c`** -> AI Confidence: **99.48%**
1048. **`tools/test/stress2/testcases/link/link.c`** -> AI Confidence: **99.48%**
1049. **`tools/test/stress2/testcases/lockf/lockf.c`** -> AI Confidence: **99.48%**
1050. **`tools/test/stress2/testcases/lockf2/lockf2.c`** -> AI Confidence: **99.48%**
1051. **`tools/test/stress2/testcases/rw/rw.c`** -> AI Confidence: **99.48%**
1052. **`tools/test/stress2/testcases/shm/shm.c`** -> AI Confidence: **99.48%**
1053. **`tools/test/stress2/testcases/swap/swap.c`** -> AI Confidence: **99.48%**
1054. **`tools/test/stress2/testcases/symlink/symlink.c`** -> AI Confidence: **99.48%**
1055. **`tools/test/stress2/tools/flip.c`** -> AI Confidence: **99.48%**
1056. **`tools/test/stress2/tools/fstool.c`** -> AI Confidence: **99.48%**
1057. **`tools/test/stress2/tools/lsholes.c`** -> AI Confidence: **99.48%**
1058. **`tools/test/stress2/tools/serial.c`** -> AI Confidence: **99.48%**
1059. **`tools/tools/ath/ath_ee_9287_print/eeprom.c`** -> AI Confidence: **99.48%**
1060. **`tools/tools/ath/ath_ee_v4k_print/eeprom.c`** -> AI Confidence: **99.48%**
1061. **`tools/tools/ath/ath_prom_read/ath_prom_read.c`** -> AI Confidence: **99.48%**
1062. **`tools/tools/ath/athaggrstats/main.c`** -> AI Confidence: **99.48%**
1063. **`tools/tools/ath/athdebug/athdebug.c`** -> AI Confidence: **99.48%**
1064. **`tools/tools/ath/athdecode/main.c`** -> AI Confidence: **99.48%**
1065. **`tools/tools/ath/athprom/athprom.c`** -> AI Confidence: **99.48%**
1066. **`tools/tools/ath/athradar/athradar.c`** -> AI Confidence: **99.48%**
1067. **`tools/tools/ath/athstats/athstats.c`** -> AI Confidence: **99.48%**
1068. **`tools/tools/ath/athstats/main.c`** -> AI Confidence: **99.48%**
1069. **`tools/tools/ath/athsurvey/athsurvey.c`** -> AI Confidence: **99.48%**
1070. **`tools/tools/cxgbtool/cxgbtool.c`** -> AI Confidence: **99.48%**
1071. **`tools/tools/decioctl/decioctl.c`** -> AI Confidence: **99.48%**
1072. **`tools/tools/ether_reflect/ether_reflect.c`** -> AI Confidence: **99.48%**
1073. **`tools/tools/find-sb/find-sb.c`** -> AI Confidence: **99.48%**
1074. **`tools/tools/indent_wrapper/indent_wrapper.c`** -> AI Confidence: **99.48%**
1075. **`tools/tools/kttcp/kttcp.c`** -> AI Confidence: **99.48%**
1076. **`tools/tools/mwl/mwldebug/mwldebug.c`** -> AI Confidence: **99.48%**
1077. **`tools/tools/netmap/bridge.c`** -> AI Confidence: **99.48%**
1078. **`tools/tools/netmap/pkt-gen.c`** -> AI Confidence: **99.48%**
1079. **`tools/tools/netrate/juggle/juggle.c`** -> AI Confidence: **99.48%**
1080. **`tools/tools/netrate/tcpp/tcpp.c`** -> AI Confidence: **99.48%**
1081. **`tools/tools/npe/npestats/main.c`** -> AI Confidence: **99.48%**
1082. **`tools/tools/so_splice/pingpong.c`** -> AI Confidence: **99.48%**
1083. **`tools/tools/tionxcl/tionxcl.c`** -> AI Confidence: **99.48%**
1084. **`tools/tools/tscdrift/tscdrift.c`** -> AI Confidence: **99.48%**
1085. **`tools/tools/usbtest/usbtest.c`** -> AI Confidence: **99.48%**
1086. **`tools/tools/vimage/vimage.c`** -> AI Confidence: **99.48%**
1087. **`usr.bin/ar/read.c`** -> AI Confidence: **99.48%**
1088. **`usr.bin/backlight/backlight.c`** -> AI Confidence: **99.48%**
1089. **`usr.bin/beep/beep.c`** -> AI Confidence: **99.48%**
1090. **`usr.bin/bluetooth/rfcomm_sppd/rfcomm_sppd.c`** -> AI Confidence: **99.48%**
1091. **`usr.bin/bsdiff/bsdiff/bsdiff.c`** -> AI Confidence: **99.48%**
1092. **`usr.bin/bsdiff/bspatch/bspatch.c`** -> AI Confidence: **99.48%**
1093. **`usr.bin/caesar/caesar.c`** -> AI Confidence: **99.48%**
1094. **`usr.bin/calendar/parsedata.c`** -> AI Confidence: **99.48%**
1095. **`usr.bin/calendar/sunpos.c`** -> AI Confidence: **99.48%**
1096. **`usr.bin/cap_mkdb/cap_mkdb.c`** -> AI Confidence: **99.48%**
1097. **`usr.bin/chpass/chpass.c`** -> AI Confidence: **99.48%**
1098. **`usr.bin/cmp/link.c`** -> AI Confidence: **99.48%**
1099. **`usr.bin/col/col.c`** -> AI Confidence: **99.48%**
1100. **`usr.bin/colrm/colrm.c`** -> AI Confidence: **99.48%**
1101. **`usr.bin/comm/comm.c`** -> AI Confidence: **99.48%**
1102. **`usr.bin/cut/cut.c`** -> AI Confidence: **99.48%**
1103. **`usr.bin/diff/diff.c`** -> AI Confidence: **99.48%**
1104. **`usr.bin/diff/diffreg.c`** -> AI Confidence: **99.48%**
1105. **`usr.bin/dpv/dpv.c`** -> AI Confidence: **99.48%**
1106. **`usr.bin/expand/expand.c`** -> AI Confidence: **99.48%**
1107. **`usr.bin/fetch/fetch.c`** -> AI Confidence: **99.48%**
1108. **`usr.bin/find/find.c`** -> AI Confidence: **99.48%**
1109. **`usr.bin/find/printf.c`** -> AI Confidence: **99.48%**
1110. **`usr.bin/finger/finger.c`** -> AI Confidence: **99.48%**
1111. **`usr.bin/fmt/fmt.c`** -> AI Confidence: **99.48%**
1112. **`usr.bin/fold/fold.c`** -> AI Confidence: **99.48%**
1113. **`usr.bin/fortune/unstr/unstr.c`** -> AI Confidence: **99.48%**
1114. **`usr.bin/getopt/getopt.c`** -> AI Confidence: **99.48%**
1115. **`usr.bin/gprof/kernel.c`** -> AI Confidence: **99.48%**
1116. **`usr.bin/hesinfo/hesinfo.c`** -> AI Confidence: **99.48%**
1117. **`usr.bin/hexdump/conv.c`** -> AI Confidence: **99.48%**
1118. **`usr.bin/hexdump/hexsyntax.c`** -> AI Confidence: **99.48%**
1119. **`usr.bin/hexdump/odsyntax.c`** -> AI Confidence: **99.48%**
1120. **`usr.bin/hexdump/parse.c`** -> AI Confidence: **99.48%**
1121. **`usr.bin/ident/ident.c`** -> AI Confidence: **99.48%**
1122. **`usr.bin/indent/indent.c`** -> AI Confidence: **99.48%**
1123. **`usr.bin/indent/io.c`** -> AI Confidence: **99.48%**
1124. **`usr.bin/ipcrm/ipcrm.c`** -> AI Confidence: **99.48%**
1125. **`usr.bin/iscsictl/iscsictl.c`** -> AI Confidence: **99.48%**
1126. **`usr.bin/iscsictl/periphs.c`** -> AI Confidence: **99.48%**
1127. **`usr.bin/join/join.c`** -> AI Confidence: **99.48%**
1128. **`usr.bin/jot/jot.c`** -> AI Confidence: **99.48%**
1129. **`usr.bin/kdump/linux.c`** -> AI Confidence: **99.48%**
1130. **`usr.bin/killall/killall.c`** -> AI Confidence: **99.48%**
1131. **`usr.bin/ktrdump/ktrdump.c`** -> AI Confidence: **99.48%**
1132. **`usr.bin/locale/locale.c`** -> AI Confidence: **99.48%**
1133. **`usr.bin/localedef/ctype.c`** -> AI Confidence: **99.48%**
1134. **`usr.bin/localedef/monetary.c`** -> AI Confidence: **99.48%**
1135. **`usr.bin/login/login_fbtab.c`** -> AI Confidence: **99.48%**
1136. **`usr.bin/look/look.c`** -> AI Confidence: **99.48%**
1137. **`usr.bin/m4/eval.c`** -> AI Confidence: **99.48%**
1138. **`usr.bin/mdo/mdo.c`** -> AI Confidence: **99.48%**
1139. **`usr.bin/mididump/mididump.c`** -> AI Confidence: **99.48%**
1140. **`usr.bin/mkimg/mkimg.c`** -> AI Confidence: **99.48%**
1141. **`usr.bin/mkimg/qcow.c`** -> AI Confidence: **99.48%**
1142. **`usr.bin/mktemp/mktemp.c`** -> AI Confidence: **99.48%**
1143. **`usr.bin/morse/morse.c`** -> AI Confidence: **99.48%**
1144. **`usr.bin/msgs/msgs.c`** -> AI Confidence: **99.48%**
1145. **`usr.bin/netstat/inet6.c`** -> AI Confidence: **99.48%**
1146. **`usr.bin/netstat/mbuf.c`** -> AI Confidence: **99.48%**
1147. **`usr.bin/nfsstat/nfsstat.c`** -> AI Confidence: **99.48%**
1148. **`usr.bin/nice/nice.c`** -> AI Confidence: **99.48%**
1149. **`usr.bin/passwd/passwd.c`** -> AI Confidence: **99.48%**
1150. **`usr.bin/paste/paste.c`** -> AI Confidence: **99.48%**
1151. **`usr.bin/pathchk/pathchk.c`** -> AI Confidence: **99.48%**
1152. **`usr.bin/primes/primes.c`** -> AI Confidence: **99.48%**
1153. **`usr.bin/printf/printf.c`** -> AI Confidence: **99.48%**
1154. **`usr.bin/proccontrol/proccontrol.c`** -> AI Confidence: **99.48%**
1155. **`usr.bin/procstat/procstat.c`** -> AI Confidence: **99.48%**
1156. **`usr.bin/procstat/procstat_advlock.c`** -> AI Confidence: **99.48%**
1157. **`usr.bin/procstat/procstat_auxv.c`** -> AI Confidence: **99.48%**
1158. **`usr.bin/procstat/procstat_cs.c`** -> AI Confidence: **99.48%**
1159. **`usr.bin/procstat/procstat_files.c`** -> AI Confidence: **99.48%**
1160. **`usr.bin/procstat/procstat_threads.c`** -> AI Confidence: **99.48%**
1161. **`usr.bin/random/random.c`** -> AI Confidence: **99.48%**
1162. **`usr.bin/resizewin/resizewin.c`** -> AI Confidence: **99.48%**
1163. **`usr.bin/sdiff/edit.c`** -> AI Confidence: **99.48%**
1164. **`usr.bin/sed/compile.c`** -> AI Confidence: **99.48%**
1165. **`usr.bin/sed/process.c`** -> AI Confidence: **99.48%**
1166. **`usr.bin/seq/seq.c`** -> AI Confidence: **99.48%**
1167. **`usr.bin/split/split.c`** -> AI Confidence: **99.48%**
1168. **`usr.bin/su/su.c`** -> AI Confidence: **99.48%**
1169. **`usr.bin/systat/cmds.c`** -> AI Confidence: **99.48%**
1170. **`usr.bin/tabs/tabs.c`** -> AI Confidence: **99.48%**
1171. **`usr.bin/tail/read.c`** -> AI Confidence: **99.48%**
1172. **`usr.bin/tail/tail.c`** -> AI Confidence: **99.48%**
1173. **`usr.bin/tr/tr.c`** -> AI Confidence: **99.48%**
1174. **`usr.bin/truncate/truncate.c`** -> AI Confidence: **99.48%**
1175. **`usr.bin/ul/ul.c`** -> AI Confidence: **99.48%**
1176. **`usr.bin/unexpand/unexpand.c`** -> AI Confidence: **99.48%**
1177. **`usr.bin/uniq/uniq.c`** -> AI Confidence: **99.48%**
1178. **`usr.bin/usbhidaction/usbhidaction.c`** -> AI Confidence: **99.48%**
1179. **`usr.bin/usbhidctl/usbhid.c`** -> AI Confidence: **99.48%**
1180. **`usr.bin/w/pr_time.c`** -> AI Confidence: **99.48%**
1181. **`usr.bin/whereis/whereis.c`** -> AI Confidence: **99.48%**
1182. **`usr.bin/whois/whois.c`** -> AI Confidence: **99.48%**
1183. **`usr.bin/xinstall/xinstall.c`** -> AI Confidence: **99.48%**
1184. **`usr.bin/ypmatch/ypmatch.c`** -> AI Confidence: **99.48%**
1185. **`usr.bin/ypwhich/ypwhich.c`** -> AI Confidence: **99.48%**
1186. **`usr.sbin/acpi/acpidump/acpidump.c`** -> AI Confidence: **99.48%**
1187. **`usr.sbin/apm/apm.c`** -> AI Confidence: **99.48%**
1188. **`usr.sbin/apmd/contrib/pccardq.c`** -> AI Confidence: **99.48%**
1189. **`usr.sbin/bhyve/amd64/pci_irq.c`** -> AI Confidence: **99.48%**
1190. **`usr.sbin/bhyve/amd64/vga.c`** -> AI Confidence: **99.48%**
1191. **`usr.sbin/bhyve/amd64/xmsr.c`** -> AI Confidence: **99.48%**
1192. **`usr.sbin/bhyve/pci_e82545.c`** -> AI Confidence: **99.48%**
1193. **`usr.sbin/bhyvectl/bhyvectl.c`** -> AI Confidence: **99.48%**
1194. **`usr.sbin/bluetooth/bcmfw/bcmfw.c`** -> AI Confidence: **99.48%**
1195. **`usr.sbin/bluetooth/bthidd/hid.c`** -> AI Confidence: **99.48%**
1196. **`usr.sbin/bluetooth/bthidd/kbd.c`** -> AI Confidence: **99.48%**
1197. **`usr.sbin/bluetooth/btpand/btpand.c`** -> AI Confidence: **99.48%**
1198. **`usr.sbin/bluetooth/rfcomm_pppd/rfcomm_pppd.c`** -> AI Confidence: **99.48%**
1199. **`usr.sbin/bluetooth/rtlbtfw/main.c`** -> AI Confidence: **99.48%**
1200. **`usr.sbin/bluetooth/sdpcontrol/search.c`** -> AI Confidence: **99.48%**
1201. **`usr.sbin/bluetooth/sdpd/ssar.c`** -> AI Confidence: **99.48%**
1202. **`usr.sbin/boot0cfg/boot0cfg.c`** -> AI Confidence: **99.48%**
1203. **`usr.sbin/bootparamd/bootparamd/bootparamd.c`** -> AI Confidence: **99.48%**
1204. **`usr.sbin/bsdinstall/distfetch/distfetch.c`** -> AI Confidence: **99.48%**
1205. **`usr.sbin/chkgrp/chkgrp.c`** -> AI Confidence: **99.48%**
1206. **`usr.sbin/chown/chown.c`** -> AI Confidence: **99.48%**
1207. **`usr.sbin/chroot/chroot.c`** -> AI Confidence: **99.48%**
1208. **`usr.sbin/cpucontrol/intel.c`** -> AI Confidence: **99.48%**
1209. **`usr.sbin/crunch/crunchide/crunchide.c`** -> AI Confidence: **99.48%**
1210. **`usr.sbin/crunch/crunchide/exec_elf32.c`** -> AI Confidence: **99.48%**
1211. **`usr.sbin/ctladm/ctladm.c`** -> AI Confidence: **99.48%**
1212. **`usr.sbin/cxgbetool/cxgbetool.c`** -> AI Confidence: **99.48%**
1213. **`usr.sbin/diskinfo/diskinfo.c`** -> AI Confidence: **99.48%**
1214. **`usr.sbin/dumpcis/printcis.c`** -> AI Confidence: **99.48%**
1215. **`usr.sbin/extattr/rmextattr.c`** -> AI Confidence: **99.48%**
1216. **`usr.sbin/fdformat/fdformat.c`** -> AI Confidence: **99.48%**
1217. **`usr.sbin/fdread/fdread.c`** -> AI Confidence: **99.48%**
1218. **`usr.sbin/fdwrite/fdwrite.c`** -> AI Confidence: **99.48%**
1219. **`usr.sbin/fifolog/fifolog_create/fifolog_create.c`** -> AI Confidence: **99.48%**
1220. **`usr.sbin/fifolog/fifolog_writer/fifolog_writer.c`** -> AI Confidence: **99.48%**
1221. **`usr.sbin/getfmac/getfmac.c`** -> AI Confidence: **99.48%**
1222. **`usr.sbin/getpmac/getpmac.c`** -> AI Confidence: **99.48%**
1223. **`usr.sbin/gpioctl/gpioctl.c`** -> AI Confidence: **99.48%**
1224. **`usr.sbin/gstat/gstat.c`** -> AI Confidence: **99.48%**
1225. **`usr.sbin/iostat/iostat.c`** -> AI Confidence: **99.48%**
1226. **`usr.sbin/iovctl/iovctl.c`** -> AI Confidence: **99.48%**
1227. **`usr.sbin/iovctl/parse.c`** -> AI Confidence: **99.48%**
1228. **`usr.sbin/ipfwpcap/ipfwpcap.c`** -> AI Confidence: **99.48%**
1229. **`usr.sbin/jexec/jexec.c`** -> AI Confidence: **99.48%**
1230. **`usr.sbin/lpr/chkprintcap/skimprintcap.c`** -> AI Confidence: **99.48%**
1231. **`usr.sbin/lpr/lpd/lpd.c`** -> AI Confidence: **99.48%**
1232. **`usr.sbin/lpr/lpq/lpq.c`** -> AI Confidence: **99.48%**
1233. **`usr.sbin/lpr/lpr/lpr.c`** -> AI Confidence: **99.48%**
1234. **`usr.sbin/lpr/lprm/lprm.c`** -> AI Confidence: **99.48%**
1235. **`usr.sbin/lptcontrol/lptcontrol.c`** -> AI Confidence: **99.48%**
1236. **`usr.sbin/makefs/ffs/mkfs.c`** -> AI Confidence: **99.48%**
1237. **`usr.sbin/makefs/makefs.c`** -> AI Confidence: **99.48%**
1238. **`usr.sbin/makefs/mtree.c`** -> AI Confidence: **99.48%**
1239. **`usr.sbin/mfiutil/mfi_bbu.c`** -> AI Confidence: **99.48%**
1240. **`usr.sbin/newsyslog/newsyslog.c`** -> AI Confidence: **99.48%**
1241. **`usr.sbin/nfsrevoke/nfsrevoke.c`** -> AI Confidence: **99.48%**
1242. **`usr.sbin/nghook/main.c`** -> AI Confidence: **99.48%**
1243. **`usr.sbin/pmc/cmd_pmc_list.c`** -> AI Confidence: **99.48%**
1244. **`usr.sbin/pmc/cmd_pmc_stat.c`** -> AI Confidence: **99.48%**
1245. **`usr.sbin/pmccontrol/pmccontrol.c`** -> AI Confidence: **99.48%**
1246. **`usr.sbin/pmcstat/pmcstat.c`** -> AI Confidence: **99.48%**
1247. **`usr.sbin/pnfsdscopymr/pnfsdscopymr.c`** -> AI Confidence: **99.48%**
1248. **`usr.sbin/pnfsdsfile/pnfsdsfile.c`** -> AI Confidence: **99.48%**
1249. **`usr.sbin/ppp/systems.c`** -> AI Confidence: **99.48%**
1250. **`usr.sbin/pppctl/pppctl.c`** -> AI Confidence: **99.48%**
1251. **`usr.sbin/pw/cpdir.c`** -> AI Confidence: **99.48%**
1252. **`usr.sbin/pw/pw.c`** -> AI Confidence: **99.48%**
1253. **`usr.sbin/pwm/pwm.c`** -> AI Confidence: **99.48%**
1254. **`usr.sbin/rpc.lockd/kern.c`** -> AI Confidence: **99.48%**
1255. **`usr.sbin/rtadvd/advcap.c`** -> AI Confidence: **99.48%**
1256. **`usr.sbin/rtadvd/config.c`** -> AI Confidence: **99.48%**
1257. **`usr.sbin/rtprio/rtprio.c`** -> AI Confidence: **99.48%**
1258. **`usr.sbin/services_mkdb/uniq.c`** -> AI Confidence: **99.48%**
1259. **`usr.sbin/sesutil/sesutil.c`** -> AI Confidence: **99.48%**
1260. **`usr.sbin/setfib/setfib.c`** -> AI Confidence: **99.48%**
1261. **`usr.sbin/setfmac/setfmac.c`** -> AI Confidence: **99.48%**
1262. **`usr.sbin/smbmsg/smbmsg.c`** -> AI Confidence: **99.48%**
1263. **`usr.sbin/usbconfig/usbconfig.c`** -> AI Confidence: **99.48%**
1264. **`usr.sbin/vidcontrol/vidcontrol.c`** -> AI Confidence: **99.48%**
1265. **`usr.sbin/virtual_oss/virtual_oss/audio_delay.c`** -> AI Confidence: **99.48%**
1266. **`usr.sbin/virtual_oss/virtual_oss/ctl.c`** -> AI Confidence: **99.48%**
1267. **`usr.sbin/virtual_oss/virtual_oss/main.c`** -> AI Confidence: **99.48%**
1268. **`usr.sbin/virtual_oss/virtual_oss/virtual_oss.c`** -> AI Confidence: **99.48%**
1269. **`usr.sbin/wlandebug/wlandebug.c`** -> AI Confidence: **99.48%**
1270. **`usr.sbin/yp_mkdb/yp_mkdb.c`** -> AI Confidence: **99.48%**
1271. **`usr.sbin/zonectl/zonectl.c`** -> AI Confidence: **99.48%**
1272. **`contrib/jemalloc/include/jemalloc/internal/jemalloc_internal_decls.h`** -> AI Confidence: **99.48%**
1273. **`contrib/libdivsufsort/include/divsufsort_private.h`** -> AI Confidence: **99.48%**
1274. **`contrib/llvm-project/clang/include/clang/AST/GlobalDecl.h`** -> AI Confidence: **99.48%**
1275. **`contrib/llvm-project/clang/include/clang/AST/StmtVisitor.h`** -> AI Confidence: **99.48%**
1276. **`contrib/llvm-project/clang/include/clang/ASTMatchers/ASTMatchers.h`** -> AI Confidence: **99.48%**
1277. **`contrib/llvm-project/clang/include/clang/Analysis/FlowSensitive/AdornedCFG.h`** -> AI Confidence: **99.48%**
1278. **`contrib/llvm-project/clang/include/clang/Analysis/FlowSensitive/DataflowAnalysis.h`** -> AI Confidence: **99.48%**
1279. **`contrib/llvm-project/clang/include/clang/Analysis/FlowSensitive/MapLattice.h`** -> AI Confidence: **99.48%**
1280. **`contrib/llvm-project/clang/include/clang/Analysis/FlowSensitive/MatchSwitch.h`** -> AI Confidence: **99.48%**
1281. **`contrib/llvm-project/clang/include/clang/Basic/CustomizableOptional.h`** -> AI Confidence: **99.48%**
1282. **`contrib/llvm-project/clang/include/clang/Basic/PlistSupport.h`** -> AI Confidence: **99.48%**
1283. **`contrib/llvm-project/clang/include/clang/ExtractAPI/DeclarationFragments.h`** -> AI Confidence: **99.48%**
1284. **`contrib/llvm-project/clang/include/clang/InstallAPI/Frontend.h`** -> AI Confidence: **99.48%**
1285. **`contrib/llvm-project/clang/include/clang/Sema/SemaBase.h`** -> AI Confidence: **99.48%**
1286. **`contrib/llvm-project/clang/include/clang/Sema/SemaOpenACC.h`** -> AI Confidence: **99.48%**
1287. **`contrib/llvm-project/clang/include/clang/StaticAnalyzer/Core/PathSensitive/BasicValueFactory.h`** -> AI Confidence: **99.48%**
1288. **`contrib/llvm-project/clang/include/clang/Tooling/Core/Replacement.h`** -> AI Confidence: **99.48%**
1289. **`contrib/llvm-project/clang/include/clang/Tooling/Refactoring/RefactoringActionRuleRequirements.h`** -> AI Confidence: **99.48%**
1290. **`contrib/llvm-project/clang/include/clang/Tooling/Transformer/Stencil.h`** -> AI Confidence: **99.48%**
1291. **`contrib/llvm-project/compiler-rt/include/fuzzer/FuzzedDataProvider.h`** -> AI Confidence: **99.48%**
1292. **`contrib/llvm-project/libcxx/include/__algorithm/minmax.h`** -> AI Confidence: **99.48%**
1293. **`contrib/llvm-project/libcxx/include/__algorithm/set_difference.h`** -> AI Confidence: **99.48%**
1294. **`contrib/llvm-project/libcxx/include/__atomic/aliases.h`** -> AI Confidence: **99.48%**
1295. **`contrib/llvm-project/libcxx/include/__chrono/convert_to_tm.h`** -> AI Confidence: **99.48%**
1296. **`contrib/llvm-project/libcxx/include/__compare/three_way_comparable.h`** -> AI Confidence: **99.48%**
1297. **`contrib/llvm-project/libcxx/include/__concepts/common_with.h`** -> AI Confidence: **99.48%**
1298. **`contrib/llvm-project/libcxx/include/__format/concepts.h`** -> AI Confidence: **99.48%**
1299. **`contrib/llvm-project/libcxx/include/__format/range_formatter.h`** -> AI Confidence: **99.48%**
1300. **`contrib/llvm-project/libcxx/include/__iterator/concepts.h`** -> AI Confidence: **99.48%**
1301. **`contrib/llvm-project/libcxx/include/__locale_dir/locale_base_api.h`** -> AI Confidence: **99.48%**
1302. **`contrib/llvm-project/libcxx/include/__memory/concepts.h`** -> AI Confidence: **99.48%**
1303. **`contrib/llvm-project/libcxx/include/__mutex/unique_lock.h`** -> AI Confidence: **99.48%**
1304. **`contrib/llvm-project/libcxx/include/__ostream/basic_ostream.h`** -> AI Confidence: **99.48%**
1305. **`contrib/llvm-project/libcxx/include/__random/discrete_distribution.h`** -> AI Confidence: **99.48%**
1306. **`contrib/llvm-project/libcxx/include/__random/gamma_distribution.h`** -> AI Confidence: **99.48%**
1307. **`contrib/llvm-project/libcxx/include/__random/lognormal_distribution.h`** -> AI Confidence: **99.48%**
1308. **`contrib/llvm-project/libcxx/include/__random/negative_binomial_distribution.h`** -> AI Confidence: **99.48%**
1309. **`contrib/llvm-project/libcxx/include/__random/normal_distribution.h`** -> AI Confidence: **99.48%**
1310. **`contrib/llvm-project/libcxx/include/__random/piecewise_constant_distribution.h`** -> AI Confidence: **99.48%**
1311. **`contrib/llvm-project/libcxx/include/__random/uniform_random_bit_generator.h`** -> AI Confidence: **99.48%**
1312. **`contrib/llvm-project/libcxx/include/__ranges/concepts.h`** -> AI Confidence: **99.48%**
1313. **`contrib/llvm-project/libcxx/include/__stop_token/intrusive_shared_ptr.h`** -> AI Confidence: **99.48%**
1314. **`contrib/llvm-project/libcxx/include/__stop_token/stop_callback.h`** -> AI Confidence: **99.48%**
1315. **`contrib/llvm-project/libcxx/include/__thread/jthread.h`** -> AI Confidence: **99.48%**
1316. **`contrib/llvm-project/libcxx/include/__thread/support/pthread.h`** -> AI Confidence: **99.48%**
1317. **`contrib/llvm-project/libcxx/include/__thread/this_thread.h`** -> AI Confidence: **99.48%**
1318. **`contrib/llvm-project/libcxx/include/math.h`** -> AI Confidence: **99.48%**
1319. **`contrib/llvm-project/lldb/include/lldb/Host/HostInfo.h`** -> AI Confidence: **99.48%**
1320. **`contrib/llvm-project/llvm/include/llvm-c/DataTypes.h`** -> AI Confidence: **99.48%**
1321. **`contrib/llvm-project/llvm/include/llvm/ADT/DepthFirstIterator.h`** -> AI Confidence: **99.48%**
1322. **`contrib/llvm-project/llvm/include/llvm/ADT/MapVector.h`** -> AI Confidence: **99.48%**
1323. **`contrib/llvm-project/llvm/include/llvm/ADT/PostOrderIterator.h`** -> AI Confidence: **99.48%**
1324. **`contrib/llvm-project/llvm/include/llvm/ADT/TinyPtrVector.h`** -> AI Confidence: **99.48%**
1325. **`contrib/llvm-project/llvm/include/llvm/Analysis/LazyCallGraph.h`** -> AI Confidence: **99.48%**
1326. **`contrib/llvm-project/llvm/include/llvm/Analysis/ModelUnderTrainingRunner.h`** -> AI Confidence: **99.48%**
1327. **`contrib/llvm-project/llvm/include/llvm/AsmParser/LLParser.h`** -> AI Confidence: **99.48%**
1328. **`contrib/llvm-project/llvm/include/llvm/DebugInfo/CodeView/AppendingTypeTableBuilder.h`** -> AI Confidence: **99.48%**
1329. **`contrib/llvm-project/llvm/include/llvm/DebugInfo/CodeView/GlobalTypeTableBuilder.h`** -> AI Confidence: **99.48%**
1330. **`contrib/llvm-project/llvm/include/llvm/DebugInfo/CodeView/RecordSerialization.h`** -> AI Confidence: **99.48%**
1331. **`contrib/llvm-project/llvm/include/llvm/DebugInfo/CodeView/SymbolSerializer.h`** -> AI Confidence: **99.48%**
1332. **`contrib/llvm-project/llvm/include/llvm/DebugInfo/LogicalView/LVReaderHandler.h`** -> AI Confidence: **99.48%**
1333. **`contrib/llvm-project/llvm/include/llvm/DebugInfo/MSF/MappedBlockStream.h`** -> AI Confidence: **99.48%**
1334. **`contrib/llvm-project/llvm/include/llvm/DebugInfo/PDB/Native/FormatUtil.h`** -> AI Confidence: **99.48%**
1335. **`contrib/llvm-project/llvm/include/llvm/DebugInfo/PDB/Native/NativeSession.h`** -> AI Confidence: **99.48%**
1336. **`contrib/llvm-project/llvm/include/llvm/DebugInfo/PDB/Native/PDBFile.h`** -> AI Confidence: **99.48%**
1337. **`contrib/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/COFFPlatform.h`** -> AI Confidence: **99.48%**
1338. **`contrib/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/ELFNixPlatform.h`** -> AI Confidence: **99.48%**
1339. **`contrib/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/LLJIT.h`** -> AI Confidence: **99.48%**
1340. **`contrib/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/Layer.h`** -> AI Confidence: **99.48%**
1341. **`contrib/llvm-project/llvm/include/llvm/Frontend/OpenMP/ConstructCompositionT.h`** -> AI Confidence: **99.48%**
1342. **`contrib/llvm-project/llvm/include/llvm/LinkAllIR.h`** -> AI Confidence: **99.48%**
1343. **`contrib/llvm-project/llvm/include/llvm/MCA/CodeEmitter.h`** -> AI Confidence: **99.48%**
1344. **`contrib/llvm-project/llvm/include/llvm/MCA/InstrBuilder.h`** -> AI Confidence: **99.48%**
1345. **`contrib/llvm-project/llvm/include/llvm/Passes/CodeGenPassBuilder.h`** -> AI Confidence: **99.48%**
1346. **`contrib/llvm-project/llvm/include/llvm/ProfileData/MemProfReader.h`** -> AI Confidence: **99.48%**
1347. **`contrib/llvm-project/llvm/include/llvm/Support/BinaryByteStream.h`** -> AI Confidence: **99.48%**
1348. **`contrib/llvm-project/llvm/include/llvm/Support/BinaryStreamRef.h`** -> AI Confidence: **99.48%**
1349. **`contrib/llvm-project/llvm/include/llvm/Support/BinaryStreamWriter.h`** -> AI Confidence: **99.48%**
1350. **`contrib/llvm-project/llvm/include/llvm/Support/FormatProviders.h`** -> AI Confidence: **99.48%**
1351. **`contrib/llvm-project/llvm/include/llvm/Support/GraphWriter.h`** -> AI Confidence: **99.48%**
1352. **`contrib/llvm-project/llvm/include/llvm/Support/HashBuilder.h`** -> AI Confidence: **99.48%**
1353. **`contrib/llvm-project/llvm/include/llvm/Support/ScopedPrinter.h`** -> AI Confidence: **99.48%**
1354. **`contrib/llvm-project/llvm/include/llvm/Testing/Support/SupportHelpers.h`** -> AI Confidence: **99.48%**
1355. **`contrib/llvm-project/llvm/include/llvm/Transforms/Scalar/LoopPassManager.h`** -> AI Confidence: **99.48%**
1356. **`contrib/openbsm/bin/auditdistd/synch.h`** -> AI Confidence: **99.48%**
1357. **`contrib/wireguard-tools/ipc-uapi.h`** -> AI Confidence: **99.48%**
1358. **`crypto/heimdal/include/crypto-headers.h`** -> AI Confidence: **99.48%**
1359. **`crypto/openssl/include/internal/e_os.h`** -> AI Confidence: **99.48%**
1360. **`crypto/openssl/include/internal/sockets.h`** -> AI Confidence: **99.48%**
1361. **`sbin/hastd/synch.h`** -> AI Confidence: **99.48%**
1362. **`sys/compat/linuxkpi/common/include/linux/spinlock.h`** -> AI Confidence: **99.48%**
1363. **`sys/contrib/ck/include/ck_pr.h`** -> AI Confidence: **99.48%**
1364. **`sys/contrib/dev/acpica/include/platform/acenv.h`** -> AI Confidence: **99.48%**
1365. **`sys/contrib/dev/acpica/include/platform/acfreebsd.h`** -> AI Confidence: **99.48%**
1366. **`sys/contrib/ncsw/inc/stdlib_ext.h`** -> AI Confidence: **99.48%**
1367. **`sys/contrib/openzfs/include/os/linux/kernel/linux/simd_powerpc.h`** -> AI Confidence: **99.48%**
1368. **`sys/contrib/openzfs/include/os/linux/spl/sys/sysmacros.h`** -> AI Confidence: **99.48%**
1369. **`sys/contrib/openzfs/include/sys/zfs_context.h`** -> AI Confidence: **99.48%**
1370. **`sys/dev/isci/scil/scif_sas_sati_binding.h`** -> AI Confidence: **99.48%**
1371. **`sys/net80211/ieee80211_var.h`** -> AI Confidence: **99.48%**
1372. **`sys/netinet/sctp_os_bsd.h`** -> AI Confidence: **99.48%**
1373. **`tests/freebsd_test_suite/macros.h`** -> AI Confidence: **99.48%**
1374. **`tools/tools/kdrv/KernelDriver`** -> AI Confidence: **99.48%**
1375. **`contrib/kyua/engine/atf_helpers.cpp`** -> AI Confidence: **99.48%**
1376. **`contrib/kyua/engine/atf_list.cpp`** -> AI Confidence: **99.48%**
1377. **`contrib/kyua/utils/fs/directory_test.cpp`** -> AI Confidence: **99.48%**
1378. **`contrib/kyua/utils/sqlite/statement_test.cpp`** -> AI Confidence: **99.48%**
1379. **`contrib/kyua/utils/text/templates_test.cpp`** -> AI Confidence: **99.48%**
1380. **`contrib/llvm-project/clang/utils/TableGen/TableGen.cpp`** -> AI Confidence: **99.48%**
1381. **`contrib/llvm-project/lld/ELF/Arch/AVR.cpp`** -> AI Confidence: **99.48%**
1382. **`contrib/llvm-project/lldb/source/Commands/CommandObjectDisassemble.cpp`** -> AI Confidence: **99.48%**
1383. **`contrib/llvm-project/lldb/source/Commands/CommandObjectMemory.cpp`** -> AI Confidence: **99.48%**
1384. **`contrib/llvm-project/lldb/source/Commands/CommandObjectPlatform.cpp`** -> AI Confidence: **99.48%**
1385. **`contrib/llvm-project/lldb/source/Commands/CommandObjectProcess.cpp`** -> AI Confidence: **99.48%**
1386. **`contrib/llvm-project/lldb/source/Commands/CommandOptionsProcessLaunch.cpp`** -> AI Confidence: **99.48%**
1387. **`contrib/llvm-project/lldb/source/Core/DumpDataExtractor.cpp`** -> AI Confidence: **99.48%**
1388. **`contrib/llvm-project/lldb/source/Core/Opcode.cpp`** -> AI Confidence: **99.48%**
1389. **`contrib/llvm-project/lldb/source/Expression/DWARFExpression.cpp`** -> AI Confidence: **99.48%**
1390. **`contrib/llvm-project/lldb/source/Expression/REPL.cpp`** -> AI Confidence: **99.48%**
1391. **`contrib/llvm-project/lldb/source/Interpreter/OptionGroupValueObjectDisplay.cpp`** -> AI Confidence: **99.48%**
1392. **`contrib/llvm-project/lldb/source/Interpreter/Property.cpp`** -> AI Confidence: **99.48%**
1393. **`contrib/llvm-project/lldb/source/Plugins/ABI/ARM/ABISysV_arm.cpp`** -> AI Confidence: **99.48%**
1394. **`contrib/llvm-project/lldb/source/Plugins/Process/Utility/StopInfoMachException.cpp`** -> AI Confidence: **99.48%**
1395. **`contrib/llvm-project/lldb/source/Plugins/Process/elf-core/RegisterContextPOSIXCore_arm64.cpp`** -> AI Confidence: **99.48%**
1396. **`contrib/llvm-project/lldb/source/Plugins/Process/elf-core/ThreadElfCore.cpp`** -> AI Confidence: **99.48%**
1397. **`contrib/llvm-project/lldb/source/Plugins/Process/gdb-remote/GDBRemoteCommunication.cpp`** -> AI Confidence: **99.48%**
1398. **`contrib/llvm-project/lldb/source/Plugins/SymbolFile/DWARF/DWARFFormValue.cpp`** -> AI Confidence: **99.48%**
1399. **`contrib/llvm-project/lldb/source/Plugins/SymbolLocator/DebugSymbols/SymbolLocatorDebugSymbols.cpp`** -> AI Confidence: **99.48%**
1400. **`contrib/llvm-project/lldb/source/Plugins/UnwindAssembly/x86/x86AssemblyInspectionEngine.cpp`** -> AI Confidence: **99.48%**
1401. **`contrib/llvm-project/lldb/source/Symbol/SymbolContext.cpp`** -> AI Confidence: **99.48%**
1402. **`contrib/llvm-project/lldb/source/Symbol/Variable.cpp`** -> AI Confidence: **99.48%**
1403. **`contrib/llvm-project/lldb/source/Utility/RegisterValue.cpp`** -> AI Confidence: **99.48%**
1404. **`contrib/llvm-project/lldb/tools/lldb-server/SystemInitializerLLGS.cpp`** -> AI Confidence: **99.48%**
1405. **`contrib/llvm-project/lldb/tools/lldb-server/lldb-platform.cpp`** -> AI Confidence: **99.48%**
1406. **`contrib/llvm-project/llvm/lib/Transforms/Utils/BuildLibCalls.cpp`** -> AI Confidence: **99.48%**
1407. **`contrib/llvm-project/llvm/lib/Transforms/Utils/DemoteRegToStack.cpp`** -> AI Confidence: **99.48%**
1408. **`contrib/llvm-project/llvm/lib/Transforms/Utils/LoopSimplify.cpp`** -> AI Confidence: **99.48%**
1409. **`contrib/llvm-project/llvm/lib/Transforms/Utils/LoopUnrollRuntime.cpp`** -> AI Confidence: **99.48%**
1410. **`contrib/llvm-project/llvm/tools/bugpoint/OptimizerDriver.cpp`** -> AI Confidence: **99.48%**
1411. **`contrib/llvm-project/llvm/tools/llvm-ar/llvm-ar.cpp`** -> AI Confidence: **99.48%**
1412. **`contrib/llvm-project/llvm/tools/llvm-objdump/MachODump.cpp`** -> AI Confidence: **99.48%**
1413. **`contrib/llvm-project/llvm/tools/llvm-pdbutil/StreamUtil.cpp`** -> AI Confidence: **99.48%**
1414. **`contrib/llvm-project/llvm/tools/llvm-size/llvm-size.cpp`** -> AI Confidence: **99.48%**
1415. **`contrib/llvm-project/llvm/tools/llvm-xray/xray-stacks.cpp`** -> AI Confidence: **99.48%**
1416. **`contrib/llvm-project/llvm/utils/TableGen/CodeEmitterGen.cpp`** -> AI Confidence: **99.48%**
1417. **`contrib/llvm-project/llvm/utils/TableGen/Common/CodeGenInstAlias.cpp`** -> AI Confidence: **99.48%**
1418. **`contrib/llvm-project/llvm/utils/TableGen/DAGISelMatcherGen.cpp`** -> AI Confidence: **99.48%**
1419. **`contrib/llvm-project/llvm/utils/TableGen/InstrDocsEmitter.cpp`** -> AI Confidence: **99.48%**
1420. **`contrib/llvm-project/llvm/utils/TableGen/X86DisassemblerTables.cpp`** -> AI Confidence: **99.48%**
1421. **`contrib/llvm-project/openmp/runtime/src/kmp_barrier.cpp`** -> AI Confidence: **99.48%**
1422. **`contrib/llvm-project/openmp/runtime/src/kmp_csupport.cpp`** -> AI Confidence: **99.48%**
1423. **`contrib/llvm-project/openmp/runtime/src/kmp_itt.cpp`** -> AI Confidence: **99.48%**
1424. **`contrib/llvm-project/openmp/runtime/src/kmp_runtime.cpp`** -> AI Confidence: **99.48%**
1425. **`contrib/llvm-project/openmp/runtime/src/kmp_sched.cpp`** -> AI Confidence: **99.48%**
1426. **`crypto/krb5/src/ccapi/server/win/ccs_os_server.cpp`** -> AI Confidence: **99.48%**
1427. **`crypto/krb5/src/windows/leash/LeashView.cpp`** -> AI Confidence: **99.48%**
1428. **`crypto/krb5/src/windows/leash/StdAfx.h`** -> AI Confidence: **99.48%**
1429. **`tests/sys/capsicum/capability-fd.cc`** -> AI Confidence: **99.48%**
1430. **`tests/sys/capsicum/ioctl.cc`** -> AI Confidence: **99.48%**
1431. **`tests/sys/fs/fusefs/mockfs.cc`** -> AI Confidence: **99.48%**
1432. **`tools/tools/mcgrab/mcgrab.cc`** -> AI Confidence: **99.48%**
1433. **`usr.bin/rs/rs.cc`** -> AI Confidence: **99.48%**
1434. **`crypto/heimdal/appl/ftp/ftpd/ftpd_locl.h`** -> AI Confidence: **99.44%**
1435. **`crypto/heimdal/appl/telnet/telnet/telnet_locl.h`** -> AI Confidence: **99.44%**
1436. **`crypto/heimdal/kuser/kuser_locl.h`** -> AI Confidence: **99.44%**
1437. **`sys/contrib/device-tree/src/arm/qcom/qcom-apq8064.dtsi`** -> AI Confidence: **99.44%**
1438. **`sys/contrib/device-tree/src/arm/rockchip/rv1126.dtsi`** -> AI Confidence: **99.44%**
1439. **`sys/contrib/device-tree/src/arm/samsung/exynos4212-tab3.dtsi`** -> AI Confidence: **99.44%**
1440. **`sys/contrib/device-tree/src/arm64/amlogic/meson-axg.dtsi`** -> AI Confidence: **99.44%**
1441. **`sys/contrib/device-tree/src/arm64/mediatek/mt6795.dtsi`** -> AI Confidence: **99.44%**
1442. **`sys/contrib/device-tree/src/arm64/qcom/msm8939.dtsi`** -> AI Confidence: **99.44%**
1443. **`sys/contrib/device-tree/src/arm64/qcom/msm8953.dtsi`** -> AI Confidence: **99.44%**
1444. **`sys/contrib/device-tree/src/arm64/qcom/msm8996-oneplus-common.dtsi`** -> AI Confidence: **99.44%**
1445. **`sys/contrib/device-tree/src/arm64/qcom/msm8996.dtsi`** -> AI Confidence: **99.44%**
1446. **`sys/contrib/device-tree/src/arm64/qcom/msm8998.dtsi`** -> AI Confidence: **99.44%**
1447. **`sys/contrib/device-tree/src/arm64/qcom/qdu1000.dtsi`** -> AI Confidence: **99.44%**
1448. **`sys/contrib/device-tree/src/arm64/qcom/sa8775p.dtsi`** -> AI Confidence: **99.44%**
1449. **`sys/contrib/device-tree/src/arm64/qcom/sc7280-qcard.dtsi`** -> AI Confidence: **99.44%**
1450. **`sys/contrib/device-tree/src/arm64/qcom/sc8280xp.dtsi`** -> AI Confidence: **99.44%**
1451. **`sys/contrib/device-tree/src/arm64/qcom/sdm630.dtsi`** -> AI Confidence: **99.44%**
1452. **`sys/contrib/device-tree/src/arm64/qcom/sdm845-oneplus-common.dtsi`** -> AI Confidence: **99.44%**
1453. **`sys/contrib/device-tree/src/arm64/qcom/sdm845-xiaomi-beryllium-common.dtsi`** -> AI Confidence: **99.44%**
1454. **`sys/contrib/device-tree/src/arm64/qcom/sdm845.dtsi`** -> AI Confidence: **99.44%**
1455. **`sys/contrib/device-tree/src/arm64/qcom/sm6115.dtsi`** -> AI Confidence: **99.44%**
1456. **`sys/contrib/device-tree/src/arm64/qcom/sm6350.dtsi`** -> AI Confidence: **99.44%**
1457. **`sys/contrib/device-tree/src/arm64/qcom/sm8150.dtsi`** -> AI Confidence: **99.44%**
1458. **`sys/contrib/device-tree/src/arm64/qcom/sm8250-xiaomi-elish-common.dtsi`** -> AI Confidence: **99.44%**
1459. **`sys/contrib/device-tree/src/arm64/qcom/sm8250.dtsi`** -> AI Confidence: **99.44%**
1460. **`sys/contrib/device-tree/src/arm64/qcom/sm8350-sony-xperia-sagami.dtsi`** -> AI Confidence: **99.44%**
1461. **`sys/contrib/device-tree/src/arm64/qcom/sm8350.dtsi`** -> AI Confidence: **99.44%**
1462. **`sys/contrib/device-tree/src/arm64/qcom/sm8450-sony-xperia-nagara.dtsi`** -> AI Confidence: **99.44%**
1463. **`sys/contrib/device-tree/src/arm64/qcom/sm8450.dtsi`** -> AI Confidence: **99.44%**
1464. **`sys/contrib/device-tree/src/arm64/qcom/sm8550.dtsi`** -> AI Confidence: **99.44%**
1465. **`sys/contrib/device-tree/src/arm64/qcom/sm8650.dtsi`** -> AI Confidence: **99.44%**
1466. **`sys/contrib/device-tree/src/arm64/qcom/sm8750.dtsi`** -> AI Confidence: **99.44%**
1467. **`sys/contrib/device-tree/src/arm64/qcom/x1e80100.dtsi`** -> AI Confidence: **99.44%**
1468. **`sys/contrib/device-tree/src/arm64/rockchip/rk3576.dtsi`** -> AI Confidence: **99.44%**
1469. **`sys/i386/i386/minidump_machdep_base.c`** -> AI Confidence: **99.44%**
1470. **`sys/netpfil/ipfilter/netinet/ip_compat.h`** -> AI Confidence: **99.44%**
1471. **`usr.bin/gzip/gzip.c`** -> AI Confidence: **99.44%**
1472. **`usr.sbin/rpc.statd/file.c`** -> AI Confidence: **99.44%**
1473. **`contrib/libxo/libxo/xo_humanize.h`** -> AI Confidence: **99.44%**
1474. **`contrib/tnftp/tnftp.h`** -> AI Confidence: **99.44%**
1475. **`contrib/xz/src/xz/private.h`** -> AI Confidence: **99.44%**
1476. **`sys/dev/enic/enic_compat.h`** -> AI Confidence: **99.44%**
1477. **`usr.sbin/cron/cron/externs.h`** -> AI Confidence: **99.44%**
1478. **`contrib/bc/include/program.h`** -> AI Confidence: **99.43%**
1479. **`contrib/libarchive/tar/bsdtar_platform.h`** -> AI Confidence: **99.43%**
1480. **`contrib/ncurses/progs/progs.priv.h`** -> AI Confidence: **99.43%**
1481. **`crypto/openssl/apps/ciphers.c`** -> AI Confidence: **99.43%**
1482. **`share/examples/sound/oss.h`** -> AI Confidence: **99.43%**
1483. **`sys/contrib/device-tree/src/arm/allwinner/sun8i-a83t.dtsi`** -> AI Confidence: **99.43%**
1484. **`sys/contrib/device-tree/src/arm/allwinner/sun8i-r40.dtsi`** -> AI Confidence: **99.43%**
1485. **`sys/contrib/device-tree/src/arm/allwinner/sun9i-a80.dtsi`** -> AI Confidence: **99.43%**
1486. **`sys/contrib/device-tree/src/arm/allwinner/sunxi-h3-h5.dtsi`** -> AI Confidence: **99.43%**
1487. **`sys/contrib/device-tree/src/arm/mediatek/mt7623.dtsi`** -> AI Confidence: **99.43%**
1488. **`sys/contrib/device-tree/src/arm/microchip/lan966x.dtsi`** -> AI Confidence: **99.43%**
1489. **`sys/contrib/device-tree/src/arm/nvidia/tegra30-asus-nexus7-grouper-common.dtsi`** -> AI Confidence: **99.43%**
1490. **`sys/contrib/device-tree/src/arm/nvidia/tegra30-lg-x3.dtsi`** -> AI Confidence: **99.43%**
1491. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6ull-dhcor-som.dtsi`** -> AI Confidence: **99.43%**
1492. **`sys/contrib/device-tree/src/arm/qcom/qcom-ipq8064.dtsi`** -> AI Confidence: **99.43%**
1493. **`sys/contrib/device-tree/src/arm/qcom/qcom-msm8226.dtsi`** -> AI Confidence: **99.43%**
1494. **`sys/contrib/device-tree/src/arm/qcom/qcom-msm8960.dtsi`** -> AI Confidence: **99.43%**
1495. **`sys/contrib/device-tree/src/arm/qcom/qcom-msm8974-sony-xperia-rhine.dtsi`** -> AI Confidence: **99.43%**
1496. **`sys/contrib/device-tree/src/arm/qcom/qcom-msm8974.dtsi`** -> AI Confidence: **99.43%**
1497. **`sys/contrib/device-tree/src/arm/qcom/qcom-msm8974pro-sony-xperia-shinano-common.dtsi`** -> AI Confidence: **99.43%**
1498. **`sys/contrib/device-tree/src/arm/rockchip/rk3036.dtsi`** -> AI Confidence: **99.43%**
1499. **`sys/contrib/device-tree/src/arm/rockchip/rk322x.dtsi`** -> AI Confidence: **99.43%**
1500. **`sys/contrib/device-tree/src/arm/rockchip/rk3288-veyron-chromebook.dtsi`** -> AI Confidence: **99.43%**
1501. **`sys/contrib/device-tree/src/arm/samsung/exynos4412-midas.dtsi`** -> AI Confidence: **99.43%**
1502. **`sys/contrib/device-tree/src/arm/samsung/exynos4412-odroid-common.dtsi`** -> AI Confidence: **99.43%**
1503. **`sys/contrib/device-tree/src/arm/samsung/exynos5250-snow-common.dtsi`** -> AI Confidence: **99.43%**
1504. **`sys/contrib/device-tree/src/arm/samsung/exynos5410.dtsi`** -> AI Confidence: **99.43%**
1505. **`sys/contrib/device-tree/src/arm/samsung/exynos5420.dtsi`** -> AI Confidence: **99.43%**
1506. **`sys/contrib/device-tree/src/arm/st/stm32mp153c-lxa-fairytux2.dtsi`** -> AI Confidence: **99.43%**
1507. **`sys/contrib/device-tree/src/arm/st/stm32mp157c-ed1.dts`** -> AI Confidence: **99.43%**
1508. **`sys/contrib/device-tree/src/arm/st/stm32mp15xc-lxa-tac.dtsi`** -> AI Confidence: **99.43%**
1509. **`sys/contrib/device-tree/src/arm/sunplus/sunplus-sp7021.dtsi`** -> AI Confidence: **99.43%**
1510. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-a64-pinephone.dtsi`** -> AI Confidence: **99.43%**
1511. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-a64.dtsi`** -> AI Confidence: **99.43%**
1512. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-h6.dtsi`** -> AI Confidence: **99.43%**
1513. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-h616.dtsi`** -> AI Confidence: **99.43%**
1514. **`sys/contrib/device-tree/src/arm64/allwinner/sun55i-a523.dtsi`** -> AI Confidence: **99.43%**
1515. **`sys/contrib/device-tree/src/arm64/amlogic/meson-a1.dtsi`** -> AI Confidence: **99.43%**
1516. **`sys/contrib/device-tree/src/arm64/amlogic/meson-libretech-cottonwood.dtsi`** -> AI Confidence: **99.43%**
1517. **`sys/contrib/device-tree/src/arm64/exynos/exynos5433-tm2-common.dtsi`** -> AI Confidence: **99.43%**
1518. **`sys/contrib/device-tree/src/arm64/exynos/google/gs101.dtsi`** -> AI Confidence: **99.43%**
1519. **`sys/contrib/device-tree/src/arm64/mediatek/mt7622.dtsi`** -> AI Confidence: **99.43%**
1520. **`sys/contrib/device-tree/src/arm64/mediatek/mt7988a.dtsi`** -> AI Confidence: **99.43%**
1521. **`sys/contrib/device-tree/src/arm64/mediatek/mt8173-elm.dtsi`** -> AI Confidence: **99.43%**
1522. **`sys/contrib/device-tree/src/arm64/mediatek/mt8173.dtsi`** -> AI Confidence: **99.43%**
1523. **`sys/contrib/device-tree/src/arm64/mediatek/mt8186-corsola.dtsi`** -> AI Confidence: **99.43%**
1524. **`sys/contrib/device-tree/src/arm64/mediatek/mt8390-genio-common.dtsi`** -> AI Confidence: **99.43%**
1525. **`sys/contrib/device-tree/src/arm64/nvidia/tegra186.dtsi`** -> AI Confidence: **99.43%**
1526. **`sys/contrib/device-tree/src/arm64/nvidia/tegra194.dtsi`** -> AI Confidence: **99.43%**
1527. **`sys/contrib/device-tree/src/arm64/nvidia/tegra210.dtsi`** -> AI Confidence: **99.43%**
1528. **`sys/contrib/device-tree/src/arm64/nvidia/tegra234.dtsi`** -> AI Confidence: **99.43%**
1529. **`sys/contrib/device-tree/src/arm64/qcom/msm8916-samsung-a2015-common.dtsi`** -> AI Confidence: **99.43%**
1530. **`sys/contrib/device-tree/src/arm64/qcom/msm8916-samsung-fortuna-common.dtsi`** -> AI Confidence: **99.43%**
1531. **`sys/contrib/device-tree/src/arm64/qcom/msm8976.dtsi`** -> AI Confidence: **99.43%**
1532. **`sys/contrib/device-tree/src/arm64/qcom/msm8994.dtsi`** -> AI Confidence: **99.43%**
1533. **`sys/contrib/device-tree/src/arm64/qcom/msm8996-sony-xperia-tone.dtsi`** -> AI Confidence: **99.43%**
1534. **`sys/contrib/device-tree/src/arm64/qcom/msm8996-xiaomi-common.dtsi`** -> AI Confidence: **99.43%**
1535. **`sys/contrib/device-tree/src/arm64/qcom/msm8998-oneplus-common.dtsi`** -> AI Confidence: **99.43%**
1536. **`sys/contrib/device-tree/src/arm64/qcom/msm8998-sony-xperia-yoshino.dtsi`** -> AI Confidence: **99.43%**
1537. **`sys/contrib/device-tree/src/arm64/qcom/qcs404.dtsi`** -> AI Confidence: **99.43%**
1538. **`sys/contrib/device-tree/src/arm64/qcom/sc7280-herobrine.dtsi`** -> AI Confidence: **99.43%**
1539. **`sys/contrib/device-tree/src/arm64/qcom/sc7280-idp.dtsi`** -> AI Confidence: **99.43%**
1540. **`sys/contrib/device-tree/src/arm64/qcom/sdm845-cheza.dtsi`** -> AI Confidence: **99.43%**
1541. **`sys/contrib/device-tree/src/arm64/qcom/sdm845-lg-common.dtsi`** -> AI Confidence: **99.43%**
1542. **`sys/contrib/device-tree/src/arm64/qcom/sdm845-sony-xperia-tama.dtsi`** -> AI Confidence: **99.43%**
1543. **`sys/contrib/device-tree/src/arm64/qcom/sm6125.dtsi`** -> AI Confidence: **99.43%**
1544. **`sys/contrib/device-tree/src/arm64/qcom/sm7125-xiaomi-common.dtsi`** -> AI Confidence: **99.43%**
1545. **`sys/contrib/device-tree/src/arm64/qcom/sm8150-sony-xperia-kumano.dtsi`** -> AI Confidence: **99.43%**
1546. **`sys/contrib/device-tree/src/arm64/qcom/sm8250-sony-xperia-edo.dtsi`** -> AI Confidence: **99.43%**
1547. **`sys/contrib/device-tree/src/arm64/qcom/x1-asus-zenbook-a14.dtsi`** -> AI Confidence: **99.43%**
1548. **`sys/contrib/device-tree/src/arm64/qcom/x1-crd.dtsi`** -> AI Confidence: **99.43%**
1549. **`sys/contrib/device-tree/src/arm64/qcom/x1e78100-lenovo-thinkpad-t14s.dtsi`** -> AI Confidence: **99.43%**
1550. **`sys/contrib/device-tree/src/arm64/qcom/x1e80100-microsoft-romulus.dtsi`** -> AI Confidence: **99.43%**
1551. **`sys/contrib/device-tree/src/arm64/rockchip/px30.dtsi`** -> AI Confidence: **99.43%**
1552. **`sys/contrib/device-tree/src/arm64/rockchip/rk3308.dtsi`** -> AI Confidence: **99.43%**
1553. **`sys/contrib/device-tree/src/arm64/rockchip/rk3328.dtsi`** -> AI Confidence: **99.43%**
1554. **`sys/contrib/device-tree/src/arm64/rockchip/rk3368.dtsi`** -> AI Confidence: **99.43%**
1555. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-anbernic-rgxx3.dtsi`** -> AI Confidence: **99.43%**
1556. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-bigtreetech-cb2.dtsi`** -> AI Confidence: **99.43%**
1557. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-pinetab2.dtsi`** -> AI Confidence: **99.43%**
1558. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-powkiddy-rk2023.dtsi`** -> AI Confidence: **99.43%**
1559. **`sys/contrib/device-tree/src/arm64/rockchip/rk3568-fastrhino-r66s.dtsi`** -> AI Confidence: **99.43%**
1560. **`sys/contrib/device-tree/src/arm64/rockchip/rk3568-nanopi-r5s.dtsi`** -> AI Confidence: **99.43%**
1561. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-nanopc-t6.dtsi`** -> AI Confidence: **99.43%**
1562. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588s-orangepi-5.dtsi`** -> AI Confidence: **99.43%**
1563. **`sys/contrib/device-tree/src/riscv/allwinner/sunxi-d1s-t113.dtsi`** -> AI Confidence: **99.43%**
1564. **`usr.bin/from/from.c`** -> AI Confidence: **99.43%**
1565. **`usr.bin/gzip/unxz.c`** -> AI Confidence: **99.43%**
1566. **`contrib/llvm-project/libcxx/include/__pstl/backend.h`** -> AI Confidence: **99.43%**
1567. **`sys/contrib/ncsw/inc/etc/sprint_ext.h`** -> AI Confidence: **99.43%**
1568. **`contrib/llvm-project/libunwind/src/DwarfInstructions.hpp`** -> AI Confidence: **99.43%**
1569. **`contrib/llvm-project/openmp/runtime/src/kmp_wrapper_getpid.h`** -> AI Confidence: **99.43%**
1570. **`crypto/krb5/src/ccapi/lib/win/OldCC/client.cxx`** -> AI Confidence: **99.43%**
1571. **`contrib/bc/include/status.h`** -> AI Confidence: **99.42%**
1572. **`contrib/tcsh/tc.os.h`** -> AI Confidence: **99.42%**
1573. **`crypto/heimdal/appl/telnet/telnetd/telnetd.h`** -> AI Confidence: **99.42%**
1574. **`crypto/heimdal/kdc/headers.h`** -> AI Confidence: **99.42%**
1575. **`sys/contrib/device-tree/src/arm/rockchip/rk3288.dtsi`** -> AI Confidence: **99.42%**
1576. **`sys/contrib/device-tree/src/arm64/amlogic/meson-g12-common.dtsi`** -> AI Confidence: **99.42%**
1577. **`sys/contrib/device-tree/src/arm64/qcom/msm8916.dtsi`** -> AI Confidence: **99.42%**
1578. **`sys/contrib/device-tree/src/arm64/qcom/sc7180-trogdor.dtsi`** -> AI Confidence: **99.42%**
1579. **`sys/contrib/device-tree/src/arm64/qcom/sc7180.dtsi`** -> AI Confidence: **99.42%**
1580. **`sys/contrib/device-tree/src/arm64/qcom/sc7280.dtsi`** -> AI Confidence: **99.42%**
1581. **`sys/contrib/device-tree/src/arm64/rockchip/rk3399-base.dtsi`** -> AI Confidence: **99.42%**
1582. **`sys/contrib/device-tree/src/arm64/rockchip/rk356x-base.dtsi`** -> AI Confidence: **99.42%**
1583. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-base.dtsi`** -> AI Confidence: **99.42%**
1584. **`tests/sys/aio/local.h`** -> AI Confidence: **99.42%**
1585. **`contrib/bearssl/src/inner.h`** -> AI Confidence: **99.42%**
1586. **`contrib/llvm-project/llvm/include/llvm/ADT/bit.h`** -> AI Confidence: **99.42%**
1587. **`crypto/krb5/src/ccapi/common/cci_common.h`** -> AI Confidence: **99.42%**
1588. **`crypto/krb5/src/plugins/kdb/db2/libdb2/include/db-int.h`** -> AI Confidence: **99.42%**
1589. **`kerberos5/include/crypto-headers.h`** -> AI Confidence: **99.42%**
1590. **`sys/contrib/ncsw/inc/string_ext.h`** -> AI Confidence: **99.42%**
1591. **`sys/contrib/ncsw/inc/types_ext.h`** -> AI Confidence: **99.42%**
1592. **`contrib/xz/src/liblzma/api/lzma.h`** -> AI Confidence: **99.42%**
1593. **`usr.bin/dtc/string.cc`** -> AI Confidence: **99.42%**
1594. **`bin/chio/chio.c`** -> AI Confidence: **99.39%**
1595. **`bin/cp/cp.c`** -> AI Confidence: **99.39%**
1596. **`bin/kill/kill.c`** -> AI Confidence: **99.39%**
1597. **`bin/pax/ar_io.c`** -> AI Confidence: **99.39%**
1598. **`bin/pax/cpio.c`** -> AI Confidence: **99.39%**
1599. **`bin/pax/ftree.c`** -> AI Confidence: **99.39%**
1600. **`bin/pax/pat_rep.c`** -> AI Confidence: **99.39%**
1601. **`bin/pax/sel_subs.c`** -> AI Confidence: **99.39%**
1602. **`bin/pwait/pwait.c`** -> AI Confidence: **99.39%**
1603. **`bin/sh/eval.c`** -> AI Confidence: **99.39%**
1604. **`bin/sh/jobs.c`** -> AI Confidence: **99.39%**
1605. **`bin/sh/parser.c`** -> AI Confidence: **99.39%**
1606. **`bin/sh/redir.c`** -> AI Confidence: **99.39%**
1607. **`bin/sleep/sleep.c`** -> AI Confidence: **99.39%**
1608. **`cddl/contrib/opensolaris/tests/os-tests/tests/oclo/oclo.c`** -> AI Confidence: **99.39%**
1609. **`cddl/contrib/opensolaris/tools/ctf/cvt/ctfmerge.c`** -> AI Confidence: **99.39%**
1610. **`contrib/atf/atf-c/detail/tp_main.c`** -> AI Confidence: **99.39%**
1611. **`contrib/atf/atf-c/utils.c`** -> AI Confidence: **99.39%**
1612. **`contrib/bc/src/program.c`** -> AI Confidence: **99.39%**
1613. **`contrib/bearssl/samples/server_basic.c`** -> AI Confidence: **99.39%**
1614. **`contrib/bearssl/tools/errors.c`** -> AI Confidence: **99.39%**
1615. **`contrib/blocklist/bin/blacklistd.c`** -> AI Confidence: **99.39%**
1616. **`contrib/blocklist/bin/blocklistd.c`** -> AI Confidence: **99.39%**
1617. **`contrib/blocklist/bin/run.c`** -> AI Confidence: **99.39%**
1618. **`contrib/bmake/compat.c`** -> AI Confidence: **99.39%**
1619. **`contrib/bmake/util.c`** -> AI Confidence: **99.39%**
1620. **`contrib/bsnmp/gensnmpdef/gensnmpdef.c`** -> AI Confidence: **99.39%**
1621. **`contrib/bsnmp/snmpd/config.c`** -> AI Confidence: **99.39%**
1622. **`contrib/dialog/fselect.c`** -> AI Confidence: **99.39%**
1623. **`contrib/dialog/util.c`** -> AI Confidence: **99.39%**
1624. **`contrib/dma/dma.c`** -> AI Confidence: **99.39%**
1625. **`contrib/dma/net.c`** -> AI Confidence: **99.39%**
1626. **`contrib/elftoolchain/brandelf/brandelf.c`** -> AI Confidence: **99.39%**
1627. **`contrib/elftoolchain/cxxfilt/cxxfilt.c`** -> AI Confidence: **99.39%**
1628. **`contrib/elftoolchain/elfcopy/ascii.c`** -> AI Confidence: **99.39%**
1629. **`contrib/elftoolchain/elfcopy/symbols.c`** -> AI Confidence: **99.39%**
1630. **`contrib/elftoolchain/elfdump/elfdump.c`** -> AI Confidence: **99.39%**
1631. **`contrib/elftoolchain/libelf/elf_update.c`** -> AI Confidence: **99.39%**
1632. **`contrib/elftoolchain/libelf/libelf_open.c`** -> AI Confidence: **99.39%**
1633. **`contrib/elftoolchain/libpe/libpe_dos.c`** -> AI Confidence: **99.39%**
1634. **`contrib/elftoolchain/libpe/libpe_section.c`** -> AI Confidence: **99.39%**
1635. **`contrib/elftoolchain/size/size.c`** -> AI Confidence: **99.39%**
1636. **`contrib/expat/tests/misc_tests.c`** -> AI Confidence: **99.39%**
1637. **`contrib/expat/tests/runtests.c`** -> AI Confidence: **99.39%**
1638. **`contrib/expat/xmlwf/xmlwf.c`** -> AI Confidence: **99.39%**
1639. **`contrib/file/src/file.c`** -> AI Confidence: **99.39%**
1640. **`contrib/file/src/fsmagic.c`** -> AI Confidence: **99.39%**
1641. **`contrib/file/src/readcdf.c`** -> AI Confidence: **99.39%**
1642. **`contrib/file/src/softmagic.c`** -> AI Confidence: **99.39%**
1643. **`contrib/ldns/compat/inet_ntop.c`** -> AI Confidence: **99.39%**
1644. **`contrib/ldns/dane.c`** -> AI Confidence: **99.39%**
1645. **`contrib/less/charset.c`** -> AI Confidence: **99.39%**
1646. **`contrib/less/filename.c`** -> AI Confidence: **99.39%**
1647. **`contrib/less/lesskey_parse.c`** -> AI Confidence: **99.39%**
1648. **`contrib/less/screen.c`** -> AI Confidence: **99.39%**
1649. **`contrib/lib9p/example/server.c`** -> AI Confidence: **99.39%**
1650. **`contrib/libarchive/libarchive/archive_pack_dev.c`** -> AI Confidence: **99.39%**
1651. **`contrib/libarchive/libarchive/archive_read_support_format_cab.c`** -> AI Confidence: **99.39%**
1652. **`contrib/libarchive/libarchive/archive_read_support_format_lha.c`** -> AI Confidence: **99.39%**
1653. **`contrib/libarchive/tar/read.c`** -> AI Confidence: **99.39%**
1654. **`contrib/libarchive/unzip/bsdunzip.c`** -> AI Confidence: **99.39%**
1655. **`contrib/libc-vis/unvis.c`** -> AI Confidence: **99.39%**
1656. **`contrib/libedit/el.c`** -> AI Confidence: **99.39%**
1657. **`contrib/libedit/filecomplete.c`** -> AI Confidence: **99.39%**
1658. **`contrib/libedit/read.c`** -> AI Confidence: **99.39%**
1659. **`contrib/libedit/search.c`** -> AI Confidence: **99.39%**
1660. **`contrib/libedit/terminal.c`** -> AI Confidence: **99.39%**
1661. **`contrib/libevent/epoll.c`** -> AI Confidence: **99.39%**
1662. **`contrib/libevent/util-internal.h`** -> AI Confidence: **99.39%**
1663. **`contrib/libfido2/fuzz/fuzz_assert.c`** -> AI Confidence: **99.39%**
1664. **`contrib/libfido2/fuzz/fuzz_cred.c`** -> AI Confidence: **99.39%**
1665. **`contrib/libfido2/fuzz/libfuzzer.c`** -> AI Confidence: **99.39%**
1666. **`contrib/libfido2/openbsd-compat/getopt_long.c`** -> AI Confidence: **99.39%**
1667. **`contrib/libfido2/openbsd-compat/openbsd-compat.h`** -> AI Confidence: **99.39%**
1668. **`contrib/libfido2/src/pcsc.c`** -> AI Confidence: **99.39%**
1669. **`contrib/libfido2/src/u2f.c`** -> AI Confidence: **99.39%**
1670. **`contrib/libfido2/tools/base64.c`** -> AI Confidence: **99.39%**
1671. **`contrib/libfido2/tools/largeblob.c`** -> AI Confidence: **99.39%**
1672. **`contrib/libfido2/tools/util.c`** -> AI Confidence: **99.39%**
1673. **`contrib/libpcap/bpf_image.c`** -> AI Confidence: **99.39%**
1674. **`contrib/libpcap/dlpisubs.c`** -> AI Confidence: **99.39%**
1675. **`contrib/libpcap/etherent.c`** -> AI Confidence: **99.39%**
1676. **`contrib/libpcap/fmtutils.c`** -> AI Confidence: **99.39%**
1677. **`contrib/libpcap/pcap-new.c`** -> AI Confidence: **99.39%**
1678. **`contrib/libpcap/pcap-pf.c`** -> AI Confidence: **99.39%**
1679. **`contrib/libpcap/rpcapd/log.c`** -> AI Confidence: **99.39%**
1680. **`contrib/libsamplerate/src_sinc.c`** -> AI Confidence: **99.39%**
1681. **`contrib/libucl/tests/test_streamline.c`** -> AI Confidence: **99.39%**
1682. **`contrib/libxo/xopo/xopo.c`** -> AI Confidence: **99.39%**
1683. **`contrib/llvm-project/libcxx/include/__utility/swap.h`** -> AI Confidence: **99.39%**
1684. **`contrib/lua/src/lcode.c`** -> AI Confidence: **99.39%**
1685. **`contrib/lua/src/ldebug.c`** -> AI Confidence: **99.39%**
1686. **`contrib/lua/src/lgc.c`** -> AI Confidence: **99.39%**
1687. **`contrib/lua/src/llex.c`** -> AI Confidence: **99.39%**
1688. **`contrib/lua/src/ltablib.c`** -> AI Confidence: **99.39%**
1689. **`contrib/lua/src/ltests.c`** -> AI Confidence: **99.39%**
1690. **`contrib/lua/src/ltm.c`** -> AI Confidence: **99.39%**
1691. **`contrib/mandoc/demandoc.c`** -> AI Confidence: **99.39%**
1692. **`contrib/mandoc/eqn.c`** -> AI Confidence: **99.39%**
1693. **`contrib/mandoc/html.c`** -> AI Confidence: **99.39%**
1694. **`contrib/mandoc/man.c`** -> AI Confidence: **99.39%**
1695. **`contrib/mandoc/man_validate.c`** -> AI Confidence: **99.39%**
1696. **`contrib/mandoc/mandocd.c`** -> AI Confidence: **99.39%**
1697. **`contrib/mandoc/mdoc_html.c`** -> AI Confidence: **99.39%**
1698. **`contrib/mandoc/mdoc_man.c`** -> AI Confidence: **99.39%**
1699. **`contrib/mandoc/mdoc_term.c`** -> AI Confidence: **99.39%**
1700. **`contrib/mandoc/mdoc_validate.c`** -> AI Confidence: **99.39%**
1701. **`contrib/mandoc/read.c`** -> AI Confidence: **99.39%**
1702. **`contrib/mandoc/soelim.c`** -> AI Confidence: **99.39%**
1703. **`contrib/mandoc/tag.c`** -> AI Confidence: **99.39%**
1704. **`contrib/mandoc/tbl_data.c`** -> AI Confidence: **99.39%**
1705. **`contrib/mandoc/tbl_html.c`** -> AI Confidence: **99.39%**
1706. **`contrib/mknod/pack_dev.c`** -> AI Confidence: **99.39%**
1707. **`contrib/mtree/excludes.c`** -> AI Confidence: **99.39%**
1708. **`contrib/netbsd-tests/crypto/opencrypto/h_comp_zlib_rnd.c`** -> AI Confidence: **99.39%**
1709. **`contrib/netbsd-tests/crypto/opencrypto/h_gcm.c`** -> AI Confidence: **99.39%**
1710. **`contrib/netbsd-tests/dev/md/h_mdserv.c`** -> AI Confidence: **99.39%**
1711. **`contrib/netbsd-tests/fs/common/snapshot.c`** -> AI Confidence: **99.39%**
1712. **`contrib/netbsd-tests/fs/ffs/h_ffs_server.c`** -> AI Confidence: **99.39%**
1713. **`contrib/netbsd-tests/fs/fifofs/t_fifo.c`** -> AI Confidence: **99.39%**
1714. **`contrib/netbsd-tests/fs/nfs/nfsservice/rumpnfsd.c`** -> AI Confidence: **99.39%**
1715. **`contrib/netbsd-tests/fs/puffs/h_dtfs/dtfs.c`** -> AI Confidence: **99.39%**
1716. **`contrib/netbsd-tests/fs/vfs/t_vnops.c`** -> AI Confidence: **99.39%**
1717. **`contrib/netbsd-tests/include/t_paths.c`** -> AI Confidence: **99.39%**
1718. **`contrib/netbsd-tests/kernel/t_lockf.c`** -> AI Confidence: **99.39%**
1719. **`contrib/netbsd-tests/net/icmp/t_ping.c`** -> AI Confidence: **99.39%**
1720. **`contrib/netbsd-tests/rump/rumpkern/h_client/h_forkcli.c`** -> AI Confidence: **99.39%**
1721. **`contrib/netbsd-tests/rump/rumpkern/t_signals.c`** -> AI Confidence: **99.39%**
1722. **`contrib/netcat/netcat.c`** -> AI Confidence: **99.39%**
1723. **`contrib/ntp/libntp/caltontp.c`** -> AI Confidence: **99.39%**
1724. **`contrib/ntp/libntp/decodenetnum.c`** -> AI Confidence: **99.39%**
1725. **`contrib/ntp/libntp/findconfig.c`** -> AI Confidence: **99.39%**
1726. **`contrib/ntp/libntp/ntp_realpath.c`** -> AI Confidence: **99.39%**
1727. **`contrib/ntp/libntp/ntp_worker.c`** -> AI Confidence: **99.39%**
1728. **`contrib/ntp/libntp/socktoa.c`** -> AI Confidence: **99.39%**
1729. **`contrib/ntp/libparse/clk_hopf6021.c`** -> AI Confidence: **99.39%**
1730. **`contrib/ntp/libparse/clk_rcc8000.c`** -> AI Confidence: **99.39%**
1731. **`contrib/ntp/libparse/clk_sel240x.c`** -> AI Confidence: **99.39%**
1732. **`contrib/ntp/libparse/clk_trimtsip.c`** -> AI Confidence: **99.39%**
1733. **`contrib/ntp/ntpd/ntp_monitor.c`** -> AI Confidence: **99.39%**
1734. **`contrib/ntp/ntpd/ntp_ppsdev.c`** -> AI Confidence: **99.39%**
1735. **`contrib/ntp/ntpd/ntp_proto.c`** -> AI Confidence: **99.39%**
1736. **`contrib/ntp/ntpd/refclock_arc.c`** -> AI Confidence: **99.39%**
1737. **`contrib/ntp/ntpd/refclock_true.c`** -> AI Confidence: **99.39%**
1738. **`contrib/ntp/ntpd/refclock_wwv.c`** -> AI Confidence: **99.39%**
1739. **`contrib/ntp/ntpdate/ntpdate.c`** -> AI Confidence: **99.39%**
1740. **`contrib/ntp/ntpq/ntpq-subs.c`** -> AI Confidence: **99.39%**
1741. **`contrib/ntp/sntp/libevent/epoll.c`** -> AI Confidence: **99.39%**
1742. **`contrib/ntp/util/sht.c`** -> AI Confidence: **99.39%**
1743. **`contrib/ntp/util/tickadj.c`** -> AI Confidence: **99.39%**
1744. **`contrib/nvi/cl/cl_read.c`** -> AI Confidence: **99.39%**
1745. **`contrib/nvi/ex/ex_abbrev.c`** -> AI Confidence: **99.39%**
1746. **`contrib/nvi/ex/ex_cmd.c`** -> AI Confidence: **99.39%**
1747. **`contrib/nvi/ex/ex_filter.c`** -> AI Confidence: **99.39%**
1748. **`contrib/nvi/ex/ex_global.c`** -> AI Confidence: **99.39%**
1749. **`contrib/nvi/ex/ex_init.c`** -> AI Confidence: **99.39%**
1750. **`contrib/nvi/ex/ex_map.c`** -> AI Confidence: **99.39%**
1751. **`contrib/nvi/ex/ex_move.c`** -> AI Confidence: **99.39%**
1752. **`contrib/nvi/ex/ex_read.c`** -> AI Confidence: **99.39%**
1753. **`contrib/nvi/ex/ex_set.c`** -> AI Confidence: **99.39%**
1754. **`contrib/nvi/ex/ex_shift.c`** -> AI Confidence: **99.39%**
1755. **`contrib/nvi/ex/ex_tag.c`** -> AI Confidence: **99.39%**
1756. **`contrib/nvi/ex/ex_undo.c`** -> AI Confidence: **99.39%**
1757. **`contrib/nvi/ex/ex_usage.c`** -> AI Confidence: **99.39%**
1758. **`contrib/nvi/ex/ex_visual.c`** -> AI Confidence: **99.39%**
1759. **`contrib/nvi/vi/v_itxt.c`** -> AI Confidence: **99.39%**
1760. **`contrib/nvi/vi/v_left.c`** -> AI Confidence: **99.39%**
1761. **`contrib/nvi/vi/v_match.c`** -> AI Confidence: **99.39%**
1762. **`contrib/nvi/vi/v_ulcase.c`** -> AI Confidence: **99.39%**
1763. **`contrib/nvi/vi/v_undo.c`** -> AI Confidence: **99.39%**
1764. **`contrib/nvi/vi/v_util.c`** -> AI Confidence: **99.39%**
1765. **`contrib/nvi/vi/v_word.c`** -> AI Confidence: **99.39%**
1766. **`contrib/nvi/vi/v_yank.c`** -> AI Confidence: **99.39%**
1767. **`contrib/nvi/vi/vs_refresh.c`** -> AI Confidence: **99.39%**
1768. **`contrib/nvi/vi/vs_smap.c`** -> AI Confidence: **99.39%**
1769. **`contrib/ofed/infiniband-diags/src/dump_fts.c`** -> AI Confidence: **99.39%**
1770. **`contrib/ofed/infiniband-diags/src/ibaddr.c`** -> AI Confidence: **99.39%**
1771. **`contrib/ofed/infiniband-diags/src/ibmirror.c`** -> AI Confidence: **99.39%**
1772. **`contrib/ofed/infiniband-diags/src/ibping.c`** -> AI Confidence: **99.39%**
1773. **`contrib/ofed/infiniband-diags/src/ibsysstat.c`** -> AI Confidence: **99.39%**
1774. **`contrib/ofed/infiniband-diags/src/ibtracert.c`** -> AI Confidence: **99.39%**
1775. **`contrib/ofed/libcxgb4/cq.c`** -> AI Confidence: **99.39%**
1776. **`contrib/ofed/libibmad/mad.c`** -> AI Confidence: **99.39%**
1777. **`contrib/ofed/librdmacm/examples/riostream.c`** -> AI Confidence: **99.39%**
1778. **`contrib/ofed/librdmacm/examples/rstream.c`** -> AI Confidence: **99.39%**
1779. **`contrib/ofed/opensm/opensm/osm_congestion_control.c`** -> AI Confidence: **99.39%**
1780. **`contrib/ofed/opensm/opensm/osm_console.c`** -> AI Confidence: **99.39%**
1781. **`contrib/ofed/opensm/opensm/osm_lin_fwd_rcv.c`** -> AI Confidence: **99.39%**
1782. **`contrib/ofed/opensm/opensm/osm_log.c`** -> AI Confidence: **99.39%**
1783. **`contrib/ofed/opensm/opensm/osm_perfmgr_db.c`** -> AI Confidence: **99.39%**
1784. **`contrib/ofed/opensm/opensm/osm_pkey.c`** -> AI Confidence: **99.39%**
1785. **`contrib/ofed/opensm/opensm/osm_port.c`** -> AI Confidence: **99.39%**
1786. **`contrib/ofed/opensm/opensm/osm_prtn.c`** -> AI Confidence: **99.39%**
1787. **`contrib/ofed/opensm/opensm/osm_prtn_config.c`** -> AI Confidence: **99.39%**
1788. **`contrib/ofed/opensm/opensm/osm_qos.c`** -> AI Confidence: **99.39%**
1789. **`contrib/ofed/opensm/opensm/osm_qos_policy.c`** -> AI Confidence: **99.39%**
1790. **`contrib/ofed/opensm/opensm/osm_sa_service_record.c`** -> AI Confidence: **99.39%**
1791. **`contrib/ofed/opensm/opensm/osm_sa_sw_info_record.c`** -> AI Confidence: **99.39%**
1792. **`contrib/ofed/opensm/opensm/osm_ucast_dfsssp.c`** -> AI Confidence: **99.39%**
1793. **`contrib/ofed/opensm/opensm/osm_vl15intf.c`** -> AI Confidence: **99.39%**
1794. **`contrib/one-true-awk/main.c`** -> AI Confidence: **99.39%**
1795. **`contrib/openbsm/bin/audit/audit.c`** -> AI Confidence: **99.39%**
1796. **`contrib/openbsm/bin/auditdistd/auditdistd.c`** -> AI Confidence: **99.39%**
1797. **`contrib/openbsm/bin/auditdistd/sandbox.c`** -> AI Confidence: **99.39%**
1798. **`contrib/openbsm/bin/auditreduce/auditreduce.c`** -> AI Confidence: **99.39%**
1799. **`contrib/openpam/t/t_pam_conv.c`** -> AI Confidence: **99.39%**
1800. **`contrib/openpam/t/t_pam_err.c`** -> AI Confidence: **99.39%**
1801. **`contrib/pam-krb5/module/alt-auth.c`** -> AI Confidence: **99.39%**
1802. **`contrib/pam-krb5/module/auth.c`** -> AI Confidence: **99.39%**
1803. **`contrib/pam-krb5/module/options.c`** -> AI Confidence: **99.39%**
1804. **`contrib/pam-krb5/module/password.c`** -> AI Confidence: **99.39%**
1805. **`contrib/pam-krb5/portable/pam.h`** -> AI Confidence: **99.39%**
1806. **`contrib/pam-krb5/tests/fakepam/config.c`** -> AI Confidence: **99.39%**
1807. **`contrib/pam-krb5/tests/runtests.c`** -> AI Confidence: **99.39%**
1808. **`contrib/pam-krb5/tests/tap/kerberos.c`** -> AI Confidence: **99.39%**
1809. **`contrib/pf/authpf/authpf.c`** -> AI Confidence: **99.39%**
1810. **`contrib/sendmail/contrib/bitdomain.c`** -> AI Confidence: **99.39%**
1811. **`contrib/sendmail/editmap/editmap.c`** -> AI Confidence: **99.39%**
1812. **`contrib/sendmail/libsm/cf.c`** -> AI Confidence: **99.39%**
1813. **`contrib/sendmail/libsm/exc.c`** -> AI Confidence: **99.39%**
1814. **`contrib/sendmail/libsm/fflush.c`** -> AI Confidence: **99.39%**
1815. **`contrib/sendmail/libsm/ldap.c`** -> AI Confidence: **99.39%**
1816. **`contrib/sendmail/libsm/makebuf.c`** -> AI Confidence: **99.39%**
1817. **`contrib/sendmail/libsm/refill.c`** -> AI Confidence: **99.39%**
1818. **`contrib/sendmail/libsm/t-notify.c`** -> AI Confidence: **99.39%**
1819. **`contrib/sendmail/libsm/util.c`** -> AI Confidence: **99.39%**
1820. **`contrib/sendmail/libsm/vfprintf.c`** -> AI Confidence: **99.39%**
1821. **`contrib/sendmail/mail.local/mail.local.c`** -> AI Confidence: **99.39%**
1822. **`contrib/sendmail/makemap/makemap.c`** -> AI Confidence: **99.39%**
1823. **`contrib/sendmail/src/conf.c`** -> AI Confidence: **99.39%**
1824. **`contrib/sendmail/src/daemon.c`** -> AI Confidence: **99.39%**
1825. **`contrib/sendmail/src/map.c`** -> AI Confidence: **99.39%**
1826. **`contrib/sendmail/src/srvrsmtp.c`** -> AI Confidence: **99.39%**
1827. **`contrib/smbfs/smbutil/view.c`** -> AI Confidence: **99.39%**
1828. **`contrib/sqlite3/autosetup/jimsh0.c`** -> AI Confidence: **99.39%**
1829. **`contrib/sqlite3/tea/generic/tclsqlite3.c`** -> AI Confidence: **99.39%**
1830. **`contrib/tcp_wrappers/inetcf.c`** -> AI Confidence: **99.39%**
1831. **`contrib/tcpdump/missing/snprintf.c`** -> AI Confidence: **99.39%**
1832. **`contrib/tcpdump/print-802_11.c`** -> AI Confidence: **99.39%**
1833. **`contrib/tcpdump/print-cdp.c`** -> AI Confidence: **99.39%**
1834. **`contrib/tcpdump/print-chdlc.c`** -> AI Confidence: **99.39%**
1835. **`contrib/tcpdump/print-fr.c`** -> AI Confidence: **99.39%**
1836. **`contrib/tcpdump/print-icmp6.c`** -> AI Confidence: **99.39%**
1837. **`contrib/tcpdump/print-ip.c`** -> AI Confidence: **99.39%**
1838. **`contrib/tcpdump/print-lldp.c`** -> AI Confidence: **99.39%**
1839. **`contrib/tcpdump/print-nfs.c`** -> AI Confidence: **99.39%**
1840. **`contrib/tcpdump/print-ospf.c`** -> AI Confidence: **99.39%**
1841. **`contrib/tcpdump/print-pgm.c`** -> AI Confidence: **99.39%**
1842. **`contrib/tcpdump/print-snmp.c`** -> AI Confidence: **99.39%**
1843. **`contrib/tcpdump/print-vrrp.c`** -> AI Confidence: **99.39%**
1844. **`contrib/telnet/libtelnet/kerberos.c`** -> AI Confidence: **99.39%**
1845. **`contrib/telnet/libtelnet/kerberos5.c`** -> AI Confidence: **99.39%**
1846. **`contrib/telnet/telnet/sys_bsd.c`** -> AI Confidence: **99.39%**
1847. **`contrib/telnet/telnet/terminal.c`** -> AI Confidence: **99.39%**
1848. **`contrib/tnftp/src/cmds.c`** -> AI Confidence: **99.39%**
1849. **`contrib/tnftp/src/ftp.c`** -> AI Confidence: **99.39%**
1850. **`contrib/tnftp/src/progressbar.c`** -> AI Confidence: **99.39%**
1851. **`contrib/tnftp/src/util.c`** -> AI Confidence: **99.39%**
1852. **`contrib/unbound/compat/inet_ntop.c`** -> AI Confidence: **99.39%**
1853. **`contrib/unbound/daemon/daemon.c`** -> AI Confidence: **99.39%**
1854. **`contrib/unbound/daemon/unbound.c`** -> AI Confidence: **99.39%**
1855. **`contrib/unbound/smallapp/unbound-control.c`** -> AI Confidence: **99.39%**
1856. **`contrib/unbound/smallapp/unbound-host.c`** -> AI Confidence: **99.39%**
1857. **`contrib/wireguard-tools/show.c`** -> AI Confidence: **99.39%**
1858. **`contrib/wpa/hostapd/main.c`** -> AI Confidence: **99.39%**
1859. **`contrib/wpa/src/ap/acs.c`** -> AI Confidence: **99.39%**
1860. **`contrib/wpa/src/ap/drv_callbacks.c`** -> AI Confidence: **99.39%**
1861. **`contrib/wpa/src/ap/eap_user_db.c`** -> AI Confidence: **99.39%**
1862. **`contrib/wpa/src/ap/wpa_auth_ie.c`** -> AI Confidence: **99.39%**
1863. **`contrib/wpa/src/common/dpp_pkex.c`** -> AI Confidence: **99.39%**
1864. **`contrib/wpa/src/common/ieee802_11_common.c`** -> AI Confidence: **99.39%**
1865. **`contrib/wpa/src/p2p/p2p_go_neg.c`** -> AI Confidence: **99.39%**
1866. **`contrib/wpa/src/rsn_supp/wpa_ie.c`** -> AI Confidence: **99.39%**
1867. **`contrib/wpa/wpa_supplicant/config_file.c`** -> AI Confidence: **99.39%**
1868. **`contrib/wpa/wpa_supplicant/ctrl_iface.c`** -> AI Confidence: **99.39%**
1869. **`contrib/wpa/wpa_supplicant/dbus/dbus_new_helpers.c`** -> AI Confidence: **99.39%**
1870. **`contrib/xz/src/xzdec/xzdec.c`** -> AI Confidence: **99.39%**
1871. **`crypto/heimdal/appl/afsutil/afslog.c`** -> AI Confidence: **99.39%**
1872. **`crypto/heimdal/appl/su/su.c`** -> AI Confidence: **99.39%**
1873. **`crypto/heimdal/appl/telnet/libtelnet/kerberos5.c`** -> AI Confidence: **99.39%**
1874. **`crypto/heimdal/include/bits.c`** -> AI Confidence: **99.39%**
1875. **`crypto/heimdal/kdc/pkinit.c`** -> AI Confidence: **99.39%**
1876. **`crypto/krb5/src/appl/simple/server/sim_server.c`** -> AI Confidence: **99.39%**
1877. **`crypto/krb5/src/kadmin/ktutil/ktutil.c`** -> AI Confidence: **99.39%**
1878. **`crypto/krb5/src/kadmin/server/ipropd_svc.c`** -> AI Confidence: **99.39%**
1879. **`crypto/krb5/src/kadmin/server/ovsec_kadmd.c`** -> AI Confidence: **99.39%**
1880. **`crypto/krb5/src/kadmin/server/schpw.c`** -> AI Confidence: **99.39%**
1881. **`crypto/krb5/src/kadmin/server/server_stubs.c`** -> AI Confidence: **99.39%**
1882. **`crypto/krb5/src/kdc/do_as_req.c`** -> AI Confidence: **99.39%**
1883. **`crypto/krb5/src/lib/kadm5/srv/svr_principal.c`** -> AI Confidence: **99.39%**
1884. **`crypto/krb5/src/lib/krb5/os/changepw.c`** -> AI Confidence: **99.39%**
1885. **`crypto/krb5/src/lib/krb5/os/lock_file.c`** -> AI Confidence: **99.39%**
1886. **`crypto/krb5/src/lib/krb5/os/t_locate_kdc.c`** -> AI Confidence: **99.39%**
1887. **`crypto/krb5/src/lib/rpc/auth_gssapi.c`** -> AI Confidence: **99.39%**
1888. **`crypto/krb5/src/lib/rpc/authgss_prot.c`** -> AI Confidence: **99.39%**
1889. **`crypto/krb5/src/lib/win_glue.c`** -> AI Confidence: **99.39%**
1890. **`crypto/krb5/src/plugins/kdb/db2/libdb2/btree/bt_seq.c`** -> AI Confidence: **99.39%**
1891. **`crypto/krb5/src/plugins/kdb/db2/libdb2/recno/rec_get.c`** -> AI Confidence: **99.39%**
1892. **`crypto/krb5/src/plugins/kdb/db2/libdb2/test/dbtest.c`** -> AI Confidence: **99.39%**
1893. **`crypto/krb5/src/plugins/kdb/db2/lockout.c`** -> AI Confidence: **99.39%**
1894. **`crypto/krb5/src/plugins/kdb/ldap/libkdb_ldap/ldap_misc.c`** -> AI Confidence: **99.39%**
1895. **`crypto/krb5/src/plugins/kdb/ldap/libkdb_ldap/lockout.c`** -> AI Confidence: **99.39%**
1896. **`crypto/krb5/src/plugins/preauth/pkinit/pkinit_crypto_openssl.c`** -> AI Confidence: **99.39%**
1897. **`crypto/krb5/src/plugins/preauth/spake/spake_kdc.c`** -> AI Confidence: **99.39%**
1898. **`crypto/krb5/src/windows/kfwlogon/kfwlogon.c`** -> AI Confidence: **99.39%**
1899. **`crypto/krb5/src/windows/leashdll/lshfunc.c`** -> AI Confidence: **99.39%**
1900. **`crypto/libecc/include/libecc/hash/hash_algs.h`** -> AI Confidence: **99.39%**
1901. **`crypto/libecc/src/sig/fuzzing_ecgdsa.c`** -> AI Confidence: **99.39%**
1902. **`crypto/libecc/src/sig/fuzzing_ecrdsa.c`** -> AI Confidence: **99.39%**
1903. **`crypto/openssh/auth-shadow.c`** -> AI Confidence: **99.39%**
1904. **`crypto/openssh/auth2-chall.c`** -> AI Confidence: **99.39%**
1905. **`crypto/openssh/auth2-passwd.c`** -> AI Confidence: **99.39%**
1906. **`crypto/openssh/auth2-pubkeyfile.c`** -> AI Confidence: **99.39%**
1907. **`crypto/openssh/auth2.c`** -> AI Confidence: **99.39%**
1908. **`crypto/openssh/authfd.c`** -> AI Confidence: **99.39%**
1909. **`crypto/openssh/dns.c`** -> AI Confidence: **99.39%**
1910. **`crypto/openssh/groupaccess.c`** -> AI Confidence: **99.39%**
1911. **`crypto/openssh/kex.c`** -> AI Confidence: **99.39%**
1912. **`crypto/openssh/kexgexs.c`** -> AI Confidence: **99.39%**
1913. **`crypto/openssh/log.c`** -> AI Confidence: **99.39%**
1914. **`crypto/openssh/mux.c`** -> AI Confidence: **99.39%**
1915. **`crypto/openssh/openbsd-compat/bsd-getentropy.c`** -> AI Confidence: **99.39%**
1916. **`crypto/openssh/openbsd-compat/fmt_scaled.c`** -> AI Confidence: **99.39%**
1917. **`crypto/openssh/openbsd-compat/getopt_long.c`** -> AI Confidence: **99.39%**
1918. **`crypto/openssh/openbsd-compat/inet_ntop.c`** -> AI Confidence: **99.39%**
1919. **`crypto/openssh/openbsd-compat/port-aix.c`** -> AI Confidence: **99.39%**
1920. **`crypto/openssh/openbsd-compat/port-linux.c`** -> AI Confidence: **99.39%**
1921. **`crypto/openssh/openbsd-compat/port-prngd.c`** -> AI Confidence: **99.39%**
1922. **`crypto/openssh/openbsd-compat/port-solaris.c`** -> AI Confidence: **99.39%**
1923. **`crypto/openssh/openbsd-compat/xcrypt.c`** -> AI Confidence: **99.39%**
1924. **`crypto/openssh/platform.c`** -> AI Confidence: **99.39%**
1925. **`crypto/openssh/readpass.c`** -> AI Confidence: **99.39%**
1926. **`crypto/openssh/regress/check-perm.c`** -> AI Confidence: **99.39%**
1927. **`crypto/openssh/regress/misc/sk-dummy/sk-dummy.c`** -> AI Confidence: **99.39%**
1928. **`crypto/openssh/regress/unittests/sshkey/test_fuzz.c`** -> AI Confidence: **99.39%**
1929. **`crypto/openssh/scp.c`** -> AI Confidence: **99.39%**
1930. **`crypto/openssh/session.c`** -> AI Confidence: **99.39%**
1931. **`crypto/openssh/sftp-client.c`** -> AI Confidence: **99.39%**
1932. **`crypto/openssh/sftp-realpath.c`** -> AI Confidence: **99.39%**
1933. **`crypto/openssh/sk-usbhid.c`** -> AI Confidence: **99.39%**
1934. **`crypto/openssh/ssh-agent.c`** -> AI Confidence: **99.39%**
1935. **`crypto/openssh/ssh-pkcs11-client.c`** -> AI Confidence: **99.39%**
1936. **`crypto/openssh/ssh-pkcs11-helper.c`** -> AI Confidence: **99.39%**
1937. **`crypto/openssh/ssh-pkcs11.c`** -> AI Confidence: **99.39%**
1938. **`crypto/openssh/ssh-sk-client.c`** -> AI Confidence: **99.39%**
1939. **`crypto/openssh/sshconnect2.c`** -> AI Confidence: **99.39%**
1940. **`crypto/openssh/sshd-auth.c`** -> AI Confidence: **99.39%**
1941. **`crypto/openssh/sshd-session.c`** -> AI Confidence: **99.39%**
1942. **`crypto/openssh/sshd.c`** -> AI Confidence: **99.39%**
1943. **`crypto/openssh/sshsig.c`** -> AI Confidence: **99.39%**
1944. **`crypto/openssh/utf8.c`** -> AI Confidence: **99.39%**
1945. **`crypto/openssl/apps/engine.c`** -> AI Confidence: **99.39%**
1946. **`crypto/openssl/apps/list.c`** -> AI Confidence: **99.39%**
1947. **`crypto/openssl/crypto/LPdir_unix.c`** -> AI Confidence: **99.39%**
1948. **`crypto/openssl/crypto/asn1/asn_mime.c`** -> AI Confidence: **99.39%**
1949. **`crypto/openssl/crypto/asn1/d2i_param.c`** -> AI Confidence: **99.39%**
1950. **`crypto/openssl/crypto/asn1/d2i_pr.c`** -> AI Confidence: **99.39%**
1951. **`crypto/openssl/crypto/asn1/tasn_dec.c`** -> AI Confidence: **99.39%**
1952. **`crypto/openssl/crypto/asn1/tasn_enc.c`** -> AI Confidence: **99.39%**
1953. **`crypto/openssl/crypto/bio/bio_addr.c`** -> AI Confidence: **99.39%**
1954. **`crypto/openssl/crypto/bio/bio_sock.c`** -> AI Confidence: **99.39%**
1955. **`crypto/openssl/crypto/bio/bss_bio.c`** -> AI Confidence: **99.39%**
1956. **`crypto/openssl/crypto/bio/bss_sock.c`** -> AI Confidence: **99.39%**
1957. **`crypto/openssl/crypto/bn/bn_rand.c`** -> AI Confidence: **99.39%**
1958. **`crypto/openssl/crypto/bn/bn_s390x.c`** -> AI Confidence: **99.39%**
1959. **`crypto/openssl/crypto/cmp/cmp_msg.c`** -> AI Confidence: **99.39%**
1960. **`crypto/openssl/crypto/cmp/cmp_protect.c`** -> AI Confidence: **99.39%**
1961. **`crypto/openssl/crypto/cmp/cmp_vfy.c`** -> AI Confidence: **99.39%**
1962. **`crypto/openssl/crypto/cms/cms_dd.c`** -> AI Confidence: **99.39%**
1963. **`crypto/openssl/crypto/cms/cms_ess.c`** -> AI Confidence: **99.39%**
1964. **`crypto/openssl/crypto/conf/conf_sap.c`** -> AI Confidence: **99.39%**
1965. **`crypto/openssl/crypto/ct/ct_oct.c`** -> AI Confidence: **99.39%**
1966. **`crypto/openssl/crypto/dh/dh_backend.c`** -> AI Confidence: **99.39%**
1967. **`crypto/openssl/crypto/dsa/dsa_key.c`** -> AI Confidence: **99.39%**
1968. **`crypto/openssl/crypto/dso/dso_vms.c`** -> AI Confidence: **99.39%**
1969. **`crypto/openssl/crypto/ec/ec_backend.c`** -> AI Confidence: **99.39%**
1970. **`crypto/openssl/crypto/ec/ecp_nistp224.c`** -> AI Confidence: **99.39%**
1971. **`crypto/openssl/crypto/ec/ecx_backend.c`** -> AI Confidence: **99.39%**
1972. **`crypto/openssl/crypto/evp/bio_ok.c`** -> AI Confidence: **99.39%**
1973. **`crypto/openssl/crypto/evp/e_aes_cbc_hmac_sha1.c`** -> AI Confidence: **99.39%**
1974. **`crypto/openssl/crypto/evp/e_aes_cbc_hmac_sha256.c`** -> AI Confidence: **99.39%**
1975. **`crypto/openssl/crypto/evp/e_camellia.c`** -> AI Confidence: **99.39%**
1976. **`crypto/openssl/crypto/evp/e_rc4_hmac_md5.c`** -> AI Confidence: **99.39%**
1977. **`crypto/openssl/crypto/evp/e_sm4.c`** -> AI Confidence: **99.39%**
1978. **`crypto/openssl/crypto/evp/evp_enc.c`** -> AI Confidence: **99.39%**
1979. **`crypto/openssl/crypto/evp/kem.c`** -> AI Confidence: **99.39%**
1980. **`crypto/openssl/crypto/evp/m_sigver.c`** -> AI Confidence: **99.39%**
1981. **`crypto/openssl/crypto/evp/p5_crpt2.c`** -> AI Confidence: **99.39%**
1982. **`crypto/openssl/crypto/ml_dsa/ml_dsa_encoders.c`** -> AI Confidence: **99.39%**
1983. **`crypto/openssl/crypto/ocsp/ocsp_srv.c`** -> AI Confidence: **99.39%**
1984. **`crypto/openssl/crypto/pem/pvkfmt.c`** -> AI Confidence: **99.39%**
1985. **`crypto/openssl/crypto/pkcs12/p12_mutl.c`** -> AI Confidence: **99.39%**
1986. **`crypto/openssl/crypto/property/property.c`** -> AI Confidence: **99.39%**
1987. **`crypto/openssl/crypto/rand/rand_egd.c`** -> AI Confidence: **99.39%**
1988. **`crypto/openssl/crypto/rsa/rsa_ameth.c`** -> AI Confidence: **99.39%**
1989. **`crypto/openssl/crypto/rsa/rsa_backend.c`** -> AI Confidence: **99.39%**
1990. **`crypto/openssl/crypto/rsa/rsa_oaep.c`** -> AI Confidence: **99.39%**
1991. **`crypto/openssl/crypto/rsa/rsa_saos.c`** -> AI Confidence: **99.39%**
1992. **`crypto/openssl/crypto/srp/srp_vfy.c`** -> AI Confidence: **99.39%**
1993. **`crypto/openssl/crypto/ts/ts_req_print.c`** -> AI Confidence: **99.39%**
1994. **`crypto/openssl/crypto/ts/ts_rsp_print.c`** -> AI Confidence: **99.39%**
1995. **`crypto/openssl/crypto/ts/ts_rsp_sign.c`** -> AI Confidence: **99.39%**
1996. **`crypto/openssl/crypto/ui/ui_openssl.c`** -> AI Confidence: **99.39%**
1997. **`crypto/openssl/crypto/x509/by_dir.c`** -> AI Confidence: **99.39%**
1998. **`crypto/openssl/crypto/x509/v3_bcons.c`** -> AI Confidence: **99.39%**
1999. **`crypto/openssl/crypto/x509/v3_crld.c`** -> AI Confidence: **99.39%**
2000. **`crypto/openssl/crypto/x509/v3_info.c`** -> AI Confidence: **99.39%**
2001. **`crypto/openssl/crypto/x509/v3_ncons.c`** -> AI Confidence: **99.39%**
2002. **`crypto/openssl/crypto/x509/v3_sxnet.c`** -> AI Confidence: **99.39%**
2003. **`crypto/openssl/demos/guide/quic-server-block.c`** -> AI Confidence: **99.39%**
2004. **`crypto/openssl/demos/guide/quic-server-non-block.c`** -> AI Confidence: **99.39%**
2005. **`crypto/openssl/demos/quic/server/server.c`** -> AI Confidence: **99.39%**
2006. **`crypto/openssl/demos/sslecho/main.c`** -> AI Confidence: **99.39%**
2007. **`crypto/openssl/engines/e_capi.c`** -> AI Confidence: **99.39%**
2008. **`crypto/openssl/fuzz/client.c`** -> AI Confidence: **99.39%**
2009. **`crypto/openssl/fuzz/dtlsclient.c`** -> AI Confidence: **99.39%**
2010. **`crypto/openssl/providers/defltprov.c`** -> AI Confidence: **99.39%**
2011. **`crypto/openssl/providers/implementations/ciphers/cipher_aes_gcm_hw.c`** -> AI Confidence: **99.39%**
2012. **`crypto/openssl/providers/implementations/ciphers/ciphercommon_block.c`** -> AI Confidence: **99.39%**
2013. **`crypto/openssl/providers/implementations/encode_decode/encode_key2text.c`** -> AI Confidence: **99.39%**
2014. **`crypto/openssl/ssl/record/methods/tls1_meth.c`** -> AI Confidence: **99.39%**
2015. **`crypto/openssl/ssl/record/methods/tls_common.c`** -> AI Confidence: **99.39%**
2016. **`crypto/openssl/ssl/record/rec_layer_d1.c`** -> AI Confidence: **99.39%**
2017. **`crypto/openssl/ssl/record/rec_layer_s3.c`** -> AI Confidence: **99.39%**
2018. **`crypto/openssl/ssl/ssl_cert.c`** -> AI Confidence: **99.39%**
2019. **`crypto/openssl/ssl/ssl_rsa.c`** -> AI Confidence: **99.39%**
2020. **`crypto/openssl/ssl/statem/statem_clnt.c`** -> AI Confidence: **99.39%**
2021. **`lib/msun/src/s_cosl.c`** -> AI Confidence: **99.39%**
2022. **`lib/msun/src/s_nan.c`** -> AI Confidence: **99.39%**
2023. **`libexec/bootpd/dumptab.c`** -> AI Confidence: **99.39%**
2024. **`libexec/bootpd/getether.c`** -> AI Confidence: **99.39%**
2025. **`libexec/bootpd/readfile.c`** -> AI Confidence: **99.39%**
2026. **`libexec/bootpd/tools/bootpef/bootpef.c`** -> AI Confidence: **99.39%**
2027. **`libexec/bootpd/tools/bootptest/bootptest.c`** -> AI Confidence: **99.39%**
2028. **`libexec/bootpd/tools/bootptest/print-bootp.c`** -> AI Confidence: **99.39%**
2029. **`libexec/getty/subr.c`** -> AI Confidence: **99.39%**
2030. **`libexec/pppoed/pppoed.c`** -> AI Confidence: **99.39%**
2031. **`libexec/rbootd/parseconf.c`** -> AI Confidence: **99.39%**
2032. **`libexec/rbootd/rbootd.c`** -> AI Confidence: **99.39%**
2033. **`libexec/rtld-elf/map_object.c`** -> AI Confidence: **99.39%**
2034. **`libexec/tftpd/tftp-transfer.c`** -> AI Confidence: **99.39%**
2035. **`libexec/tftpd/tftpd.c`** -> AI Confidence: **99.39%**
2036. **`libexec/ypxfr/yp_dbwrite.c`** -> AI Confidence: **99.39%**
2037. **`sbin/camcontrol/depop.c`** -> AI Confidence: **99.39%**
2038. **`sbin/camcontrol/persist.c`** -> AI Confidence: **99.39%**
2039. **`sbin/camcontrol/progress.c`** -> AI Confidence: **99.39%**
2040. **`sbin/comcontrol/comcontrol.c`** -> AI Confidence: **99.39%**
2041. **`sbin/conscontrol/conscontrol.c`** -> AI Confidence: **99.39%**
2042. **`sbin/ddb/ddb.c`** -> AI Confidence: **99.39%**
2043. **`sbin/ddb/ddb_capture.c`** -> AI Confidence: **99.39%**
2044. **`sbin/devfs/rule.c`** -> AI Confidence: **99.39%**
2045. **`sbin/dmesg/dmesg.c`** -> AI Confidence: **99.39%**
2046. **`sbin/dumpfs/dumpfs.c`** -> AI Confidence: **99.39%**
2047. **`sbin/dumpon/dumpon.c`** -> AI Confidence: **99.39%**
2048. **`sbin/etherswitchcfg/etherswitchcfg.c`** -> AI Confidence: **99.39%**
2049. **`sbin/fdisk/fdisk.c`** -> AI Confidence: **99.39%**
2050. **`sbin/fsck_ffs/setup.c`** -> AI Confidence: **99.39%**
2051. **`sbin/fsdb/fsdbutil.c`** -> AI Confidence: **99.39%**
2052. **`sbin/ggate/ggatec/ggatec.c`** -> AI Confidence: **99.39%**
2053. **`sbin/hastd/hastd.c`** -> AI Confidence: **99.39%**
2054. **`sbin/hastd/metadata.c`** -> AI Confidence: **99.39%**
2055. **`sbin/ipf/ipfstat/ipfstat.c`** -> AI Confidence: **99.39%**
2056. **`sbin/ipf/ipsend/resend.c`** -> AI Confidence: **99.39%**
2057. **`sbin/ipfw/ipv6.c`** -> AI Confidence: **99.39%**
2058. **`sbin/ipfw/tables.c`** -> AI Confidence: **99.39%**
2059. **`sbin/ldconfig/ldconfig.c`** -> AI Confidence: **99.39%**
2060. **`sbin/md5/md5.c`** -> AI Confidence: **99.39%**
2061. **`sbin/mdmfs/mdmfs.c`** -> AI Confidence: **99.39%**
2062. **`sbin/mknod/mknod.c`** -> AI Confidence: **99.39%**
2063. **`sbin/mount_cd9660/mount_cd9660.c`** -> AI Confidence: **99.39%**
2064. **`sbin/mount_nfs/mount_nfs.c`** -> AI Confidence: **99.39%**
2065. **`sbin/mount_unionfs/mount_unionfs.c`** -> AI Confidence: **99.39%**
2066. **`sbin/natd/natd.c`** -> AI Confidence: **99.39%**
2067. **`sbin/nvmecontrol/firmware.c`** -> AI Confidence: **99.39%**
2068. **`sbin/nvmecontrol/identify.c`** -> AI Confidence: **99.39%**
2069. **`sbin/nvmecontrol/sanitize.c`** -> AI Confidence: **99.39%**
2070. **`sbin/nvmecontrol/telemetry.c`** -> AI Confidence: **99.39%**
2071. **`sbin/pfctl/pfctl_osfp.c`** -> AI Confidence: **99.39%**
2072. **`sbin/pfctl/pfctl_table.c`** -> AI Confidence: **99.39%**
2073. **`sbin/ping/ping.c`** -> AI Confidence: **99.39%**
2074. **`sbin/ping/ping6.c`** -> AI Confidence: **99.39%**
2075. **`sbin/recoverdisk/recoverdisk.c`** -> AI Confidence: **99.39%**
2076. **`sbin/restore/interactive.c`** -> AI Confidence: **99.39%**
2077. **`sbin/restore/restore.c`** -> AI Confidence: **99.39%**
2078. **`sbin/routed/rtquery/rtquery.c`** -> AI Confidence: **99.39%**
2079. **`sbin/savecore/savecore.c`** -> AI Confidence: **99.39%**
2080. **`sbin/sysctl/sysctl.c`** -> AI Confidence: **99.39%**
2081. **`share/examples/ipfilter/samples/relay.c`** -> AI Confidence: **99.39%**
2082. **`share/examples/libusb20/control.c`** -> AI Confidence: **99.39%**
2083. **`share/examples/ppi/ppilcd.c`** -> AI Confidence: **99.39%**
2084. **`share/examples/ses/srcs/chpmon.c`** -> AI Confidence: **99.39%**
2085. **`share/examples/ses/srcs/getencstat.c`** -> AI Confidence: **99.39%**
2086. **`stand/common/install.c`** -> AI Confidence: **99.39%**
2087. **`stand/common/metadata.c`** -> AI Confidence: **99.39%**
2088. **`stand/efi/libefi/devpath.c`** -> AI Confidence: **99.39%**
2089. **`stand/efi/loader/bootinfo.c`** -> AI Confidence: **99.39%**
2090. **`stand/i386/common/cons.c`** -> AI Confidence: **99.39%**
2091. **`stand/i386/isoboot/isoboot.c`** -> AI Confidence: **99.39%**
2092. **`sys/amd64/vmm/amd/svm_msr.c`** -> AI Confidence: **99.39%**
2093. **`sys/amd64/vmm/amd/vmcb.c`** -> AI Confidence: **99.39%**
2094. **`sys/amd64/vmm/intel/vmcs.c`** -> AI Confidence: **99.39%**
2095. **`sys/arm/allwinner/aw_cir.c`** -> AI Confidence: **99.39%**
2096. **`sys/arm/arm/cpuinfo.c`** -> AI Confidence: **99.39%**
2097. **`sys/arm/broadcom/bcm2835/bcm2835_sdhost.c`** -> AI Confidence: **99.39%**
2098. **`sys/arm/mv/clk/a37x0_periph_clk_driver.c`** -> AI Confidence: **99.39%**
2099. **`sys/arm/nvidia/tegra_ehci.c`** -> AI Confidence: **99.39%**
2100. **`sys/arm/ti/am335x/am335x_gpio.c`** -> AI Confidence: **99.39%**
2101. **`sys/cam/ata/ata_da.c`** -> AI Confidence: **99.39%**
2102. **`sys/cam/cam.c`** -> AI Confidence: **99.39%**
2103. **`sys/cam/scsi/scsi_da.c`** -> AI Confidence: **99.39%**
2104. **`sys/cddl/compat/opensolaris/kern/opensolaris_acl.c`** -> AI Confidence: **99.39%**
2105. **`sys/cddl/contrib/opensolaris/common/lz4/lz4.c`** -> AI Confidence: **99.39%**
2106. **`sys/cddl/contrib/opensolaris/uts/common/dtrace/dtrace.c`** -> AI Confidence: **99.39%**
2107. **`sys/contrib/dev/acpica/common/adwalk.c`** -> AI Confidence: **99.39%**
2108. **`sys/contrib/dev/acpica/common/dmextern.c`** -> AI Confidence: **99.39%**
2109. **`sys/contrib/dev/acpica/common/dmswitch.c`** -> AI Confidence: **99.39%**
2110. **`sys/contrib/dev/ath/ath_hal/ar9300/ar9300_eeprom.c`** -> AI Confidence: **99.39%**
2111. **`sys/contrib/dev/ath/ath_hal/ar9300/ar9300_reset.c`** -> AI Confidence: **99.39%**
2112. **`sys/contrib/dev/iwlwifi/iwl-drv.c`** -> AI Confidence: **99.39%**
2113. **`sys/contrib/dev/rtw88/rtw88xxa.c`** -> AI Confidence: **99.39%**
2114. **`sys/contrib/libsodium/src/libsodium/crypto_generichash/blake2b/ref/blake2b-compress-sse41.c`** -> AI Confidence: **99.39%**
2115. **`sys/contrib/libsodium/src/libsodium/crypto_pwhash/scryptsalsa208sha256/pbkdf2-sha256.c`** -> AI Confidence: **99.39%**
2116. **`sys/contrib/libsodium/src/libsodium/crypto_secretbox/crypto_secretbox_easy.c`** -> AI Confidence: **99.39%**
2117. **`sys/contrib/ncsw/Peripherals/BM/bm.c`** -> AI Confidence: **99.39%**
2118. **`sys/contrib/ncsw/Peripherals/FM/Pcd/fm_kg.c`** -> AI Confidence: **99.39%**
2119. **`sys/contrib/ncsw/Peripherals/FM/SP/fm_sp.c`** -> AI Confidence: **99.39%**
2120. **`sys/contrib/ncsw/Peripherals/FM/fm_ncsw.c`** -> AI Confidence: **99.39%**
2121. **`sys/contrib/openzfs/cmd/zed/zed.c`** -> AI Confidence: **99.39%**
2122. **`sys/contrib/openzfs/cmd/zed/zed_conf.c`** -> AI Confidence: **99.39%**
2123. **`sys/contrib/openzfs/cmd/zed/zed_event.c`** -> AI Confidence: **99.39%**
2124. **`sys/contrib/openzfs/cmd/zfs/zfs_iter.c`** -> AI Confidence: **99.39%**
2125. **`sys/contrib/openzfs/cmd/zpool/zpool_vdev.c`** -> AI Confidence: **99.39%**
2126. **`sys/contrib/openzfs/cmd/zstream/zstream_decompress.c`** -> AI Confidence: **99.39%**
2127. **`sys/contrib/openzfs/cmd/zstream/zstream_recompress.c`** -> AI Confidence: **99.39%**
2128. **`sys/contrib/openzfs/module/icp/io/aes.c`** -> AI Confidence: **99.39%**
2129. **`sys/contrib/openzfs/module/lua/lcode.c`** -> AI Confidence: **99.39%**
2130. **`sys/contrib/openzfs/module/lua/ldebug.c`** -> AI Confidence: **99.39%**
2131. **`sys/contrib/openzfs/module/lua/ldo.c`** -> AI Confidence: **99.39%**
2132. **`sys/contrib/openzfs/module/lua/lgc.c`** -> AI Confidence: **99.39%**
2133. **`sys/contrib/openzfs/module/lua/llex.c`** -> AI Confidence: **99.39%**
2134. **`sys/contrib/openzfs/module/lua/ltable.c`** -> AI Confidence: **99.39%**
2135. **`sys/contrib/openzfs/module/os/freebsd/spl/spl_acl.c`** -> AI Confidence: **99.39%**
2136. **`sys/contrib/openzfs/module/os/freebsd/zfs/zfs_dir.c`** -> AI Confidence: **99.39%**
2137. **`sys/contrib/openzfs/module/os/freebsd/zfs/zfs_znode_os.c`** -> AI Confidence: **99.39%**
2138. **`sys/contrib/openzfs/module/os/linux/zfs/qat_compress.c`** -> AI Confidence: **99.39%**
2139. **`sys/contrib/openzfs/module/os/linux/zfs/qat_crypt.c`** -> AI Confidence: **99.39%**
2140. **`sys/contrib/openzfs/module/os/linux/zfs/zfs_vnops_os.c`** -> AI Confidence: **99.39%**
2141. **`sys/contrib/openzfs/module/os/linux/zfs/zfs_znode_os.c`** -> AI Confidence: **99.39%**
2142. **`sys/contrib/openzfs/module/os/linux/zfs/zio_crypt.c`** -> AI Confidence: **99.39%**
2143. **`sys/contrib/openzfs/module/zfs/dbuf.c`** -> AI Confidence: **99.39%**
2144. **`sys/contrib/openzfs/module/zfs/dnode.c`** -> AI Confidence: **99.39%**
2145. **`sys/contrib/openzfs/module/zfs/dnode_sync.c`** -> AI Confidence: **99.39%**
2146. **`sys/contrib/openzfs/module/zfs/dsl_crypt.c`** -> AI Confidence: **99.39%**
2147. **`sys/contrib/openzfs/module/zfs/dsl_prop.c`** -> AI Confidence: **99.39%**
2148. **`sys/contrib/openzfs/module/zfs/spa.c`** -> AI Confidence: **99.39%**
2149. **`sys/contrib/openzfs/module/zfs/vdev_raidz.c`** -> AI Confidence: **99.39%**
2150. **`sys/contrib/openzfs/module/zfs/vdev_raidz_math.c`** -> AI Confidence: **99.39%**
2151. **`sys/contrib/openzfs/module/zfs/zcp.c`** -> AI Confidence: **99.39%**
2152. **`sys/contrib/openzfs/module/zfs/zcp_get.c`** -> AI Confidence: **99.39%**
2153. **`sys/contrib/openzfs/module/zfs/zfs_log.c`** -> AI Confidence: **99.39%**
2154. **`sys/contrib/openzfs/module/zfs/zfs_sa.c`** -> AI Confidence: **99.39%**
2155. **`sys/contrib/openzfs/module/zfs/zfs_znode.c`** -> AI Confidence: **99.39%**
2156. **`sys/contrib/openzfs/module/zfs/zio.c`** -> AI Confidence: **99.39%**
2157. **`sys/contrib/openzfs/module/zfs/zio_inject.c`** -> AI Confidence: **99.39%**
2158. **`sys/contrib/openzfs/tests/zfs-tests/cmd/dosmode_readonly_write.c`** -> AI Confidence: **99.39%**
2159. **`sys/contrib/openzfs/tests/zfs-tests/cmd/file/file_write.c`** -> AI Confidence: **99.39%**
2160. **`sys/contrib/openzfs/tests/zfs-tests/cmd/idmap_util.c`** -> AI Confidence: **99.39%**
2161. **`sys/contrib/openzfs/tests/zfs-tests/cmd/mkfile.c`** -> AI Confidence: **99.39%**
2162. **`sys/contrib/openzfs/tests/zfs-tests/cmd/mmapwrite.c`** -> AI Confidence: **99.39%**
2163. **`sys/contrib/openzfs/tests/zfs-tests/cmd/readmmap.c`** -> AI Confidence: **99.39%**
2164. **`sys/contrib/openzfs/tests/zfs-tests/cmd/renameat2.c`** -> AI Confidence: **99.39%**
2165. **`sys/contrib/openzfs/tests/zfs-tests/cmd/statx.c`** -> AI Confidence: **99.39%**
2166. **`sys/contrib/openzfs/tests/zfs-tests/cmd/stride_dd.c`** -> AI Confidence: **99.39%**
2167. **`sys/contrib/openzfs/tests/zfs-tests/tests/functional/libzfs/many_fds.c`** -> AI Confidence: **99.39%**
2168. **`sys/contrib/openzfs/tests/zfs-tests/tests/functional/tmpfile/tmpfile_stat_mode.c`** -> AI Confidence: **99.39%**
2169. **`sys/crypto/aesni/aesni_ccm.c`** -> AI Confidence: **99.39%**
2170. **`sys/crypto/openssl/ossl_x86.c`** -> AI Confidence: **99.39%**
2171. **`sys/ddb/db_examine.c`** -> AI Confidence: **99.39%**
2172. **`sys/ddb/db_output.c`** -> AI Confidence: **99.39%**
2173. **`sys/dev/acpi_support/acpi_asus.c`** -> AI Confidence: **99.39%**
2174. **`sys/dev/acpi_support/acpi_hp.c`** -> AI Confidence: **99.39%**
2175. **`sys/dev/acpica/Osd/OsdSynch.c`** -> AI Confidence: **99.39%**
2176. **`sys/dev/acpica/acpi_smbat.c`** -> AI Confidence: **99.39%**
2177. **`sys/dev/adb/adb_buttons.c`** -> AI Confidence: **99.39%**
2178. **`sys/dev/ata/ata-sata.c`** -> AI Confidence: **99.39%**
2179. **`sys/dev/ath/ah_osdep_ar5210.c`** -> AI Confidence: **99.39%**
2180. **`sys/dev/ath/ah_osdep_ar5211.c`** -> AI Confidence: **99.39%**
2181. **`sys/dev/ath/ah_osdep_ar9300.c`** -> AI Confidence: **99.39%**
2182. **`sys/dev/ath/ath_hal/ar5212/ar5212_ani.c`** -> AI Confidence: **99.39%**
2183. **`sys/dev/ath/ath_hal/ar5212/ar5212_attach.c`** -> AI Confidence: **99.39%**
2184. **`sys/dev/ath/ath_hal/ar5212/ar5212_reset.c`** -> AI Confidence: **99.39%**
2185. **`sys/dev/ath/ath_hal/ar5312/ar5312_attach.c`** -> AI Confidence: **99.39%**
2186. **`sys/dev/ath/ath_hal/ar5312/ar5312_reset.c`** -> AI Confidence: **99.39%**
2187. **`sys/dev/ath/ath_hal/ar5416/ar5416_radar.c`** -> AI Confidence: **99.39%**
2188. **`sys/dev/ath/ath_hal/ar9002/ar9280_attach.c`** -> AI Confidence: **99.39%**
2189. **`sys/dev/ath/ath_hal/ar9002/ar9285_reset.c`** -> AI Confidence: **99.39%**
2190. **`sys/dev/ath/if_ath_btcoex_mci.c`** -> AI Confidence: **99.39%**
2191. **`sys/dev/atkbdc/atkbdc_subr.c`** -> AI Confidence: **99.39%**
2192. **`sys/dev/bhnd/cores/chipc/pwrctl/bhnd_pwrctl_subr.c`** -> AI Confidence: **99.39%**
2193. **`sys/dev/bhnd/cores/pmu/bhnd_pmu_subr.c`** -> AI Confidence: **99.39%**
2194. **`sys/dev/bhnd/nvram/bhnd_nvram_subr.c`** -> AI Confidence: **99.39%**
2195. **`sys/dev/cfi/cfi_core.c`** -> AI Confidence: **99.39%**
2196. **`sys/dev/cxgb/sys/uipc_mvec.c`** -> AI Confidence: **99.39%**
2197. **`sys/dev/dc/dcphy.c`** -> AI Confidence: **99.39%**
2198. **`sys/dev/dc/if_dc.c`** -> AI Confidence: **99.39%**
2199. **`sys/dev/etherswitch/ip17x/ip17x_vlans.c`** -> AI Confidence: **99.39%**
2200. **`sys/dev/fb/fb.c`** -> AI Confidence: **99.39%**
2201. **`sys/dev/fb/splash_bmp.c`** -> AI Confidence: **99.39%**
2202. **`sys/dev/fb/vga.c`** -> AI Confidence: **99.39%**
2203. **`sys/dev/fdc/fdc_acpi.c`** -> AI Confidence: **99.39%**
2204. **`sys/dev/gem/if_gem_pci.c`** -> AI Confidence: **99.39%**
2205. **`sys/dev/gpio/gpiospi.c`** -> AI Confidence: **99.39%**
2206. **`sys/dev/hid/hkbd.c`** -> AI Confidence: **99.39%**
2207. **`sys/dev/ichiic/ig4_iic.c`** -> AI Confidence: **99.39%**
2208. **`sys/dev/ichsmb/ichsmb.c`** -> AI Confidence: **99.39%**
2209. **`sys/dev/iicbus/rtc/ds13rtc.c`** -> AI Confidence: **99.39%**
2210. **`sys/dev/ipmi/ipmi_acpi.c`** -> AI Confidence: **99.39%**
2211. **`sys/dev/ipmi/ipmi_pci.c`** -> AI Confidence: **99.39%**
2212. **`sys/dev/ipmi/ipmi_ssif.c`** -> AI Confidence: **99.39%**
2213. **`sys/dev/isci/scil/sati_mode_select.c`** -> AI Confidence: **99.39%**
2214. **`sys/dev/isci/scil/sati_mode_sense.c`** -> AI Confidence: **99.39%**
2215. **`sys/dev/isci/scil/sati_request_sense.c`** -> AI Confidence: **99.39%**
2216. **`sys/dev/isci/scil/scic_sds_phy.c`** -> AI Confidence: **99.39%**
2217. **`sys/dev/isci/scil/scic_sds_stp_request.c`** -> AI Confidence: **99.39%**
2218. **`sys/dev/isci/scil/scif_sas_smp_remote_device.c`** -> AI Confidence: **99.39%**
2219. **`sys/dev/isci/scil/scif_sas_stp_io_request.c`** -> AI Confidence: **99.39%**
2220. **`sys/dev/isp/isp.c`** -> AI Confidence: **99.39%**
2221. **`sys/dev/kbd/kbd.c`** -> AI Confidence: **99.39%**
2222. **`sys/dev/kbdmux/kbdmux.c`** -> AI Confidence: **99.39%**
2223. **`sys/dev/liquidio/lio_core.c`** -> AI Confidence: **99.39%**
2224. **`sys/dev/mfi/mfi_debug.c`** -> AI Confidence: **99.39%**
2225. **`sys/dev/mii/nsphy.c`** -> AI Confidence: **99.39%**
2226. **`sys/dev/mmc/host/dwmmc.c`** -> AI Confidence: **99.39%**
2227. **`sys/dev/mmc/mmc_helpers.c`** -> AI Confidence: **99.39%**
2228. **`sys/dev/mpr/mpr_mapping.c`** -> AI Confidence: **99.39%**
2229. **`sys/dev/mpr/mpr_sas_lsi.c`** -> AI Confidence: **99.39%**
2230. **`sys/dev/mps/mps_sas_lsi.c`** -> AI Confidence: **99.39%**
2231. **`sys/dev/mrsas/mrsas_fp.c`** -> AI Confidence: **99.39%**
2232. **`sys/dev/mxge/if_mxge.c`** -> AI Confidence: **99.39%**
2233. **`sys/dev/netmap/netmap_pipe.c`** -> AI Confidence: **99.39%**
2234. **`sys/dev/ofw/ofw_subr.c`** -> AI Confidence: **99.39%**
2235. **`sys/dev/ofw/openfirmio.c`** -> AI Confidence: **99.39%**
2236. **`sys/dev/pci/fixup_pci.c`** -> AI Confidence: **99.39%**
2237. **`sys/dev/pms/RefTisa/discovery/dm/dmdisc.c`** -> AI Confidence: **99.39%**
2238. **`sys/dev/pms/RefTisa/sat/src/smsat.c`** -> AI Confidence: **99.39%**
2239. **`sys/dev/pms/RefTisa/tisa/sassata/common/ossacmnapi.c`** -> AI Confidence: **99.39%**
2240. **`sys/dev/pms/RefTisa/tisa/sassata/common/tddmcmnapi.c`** -> AI Confidence: **99.39%**
2241. **`sys/dev/pms/RefTisa/tisa/sassata/common/tdmisc.c`** -> AI Confidence: **99.39%**
2242. **`sys/dev/pms/RefTisa/tisa/sassata/sas/ini/itddisc.c`** -> AI Confidence: **99.39%**
2243. **`sys/dev/pms/RefTisa/tisa/sassata/sata/host/sat.c`** -> AI Confidence: **99.39%**
2244. **`sys/dev/qat/qat_api/common/compression/dc_datapath.c`** -> AI Confidence: **99.39%**
2245. **`sys/dev/qat/qat_api/common/crypto/sym/lac_sym_api.c`** -> AI Confidence: **99.39%**
2246. **`sys/dev/qat/qat_api/common/crypto/sym/lac_sym_auth_enc.c`** -> AI Confidence: **99.39%**
2247. **`sys/dev/qat/qat_api/common/crypto/sym/lac_sym_hash.c`** -> AI Confidence: **99.39%**
2248. **`sys/dev/qat/qat_api/common/crypto/sym/lac_sym_hash_sw_precomputes.c`** -> AI Confidence: **99.39%**
2249. **`sys/dev/qat/qat_api/common/crypto/sym/qat/lac_sym_qat.c`** -> AI Confidence: **99.39%**
2250. **`sys/dev/qat/qat_api/common/crypto/sym/qat/lac_sym_qat_hash.c`** -> AI Confidence: **99.39%**
2251. **`sys/dev/qat/qat_api/common/crypto/sym/qat/lac_sym_qat_key.c`** -> AI Confidence: **99.39%**
2252. **`sys/dev/qat/qat_api/common/ctrl/sal_compression.c`** -> AI Confidence: **99.39%**
2253. **`sys/dev/qat/qat_api/common/ctrl/sal_crypto.c`** -> AI Confidence: **99.39%**
2254. **`sys/dev/qat/qat_api/common/ctrl/sal_ctrl_services.c`** -> AI Confidence: **99.39%**
2255. **`sys/dev/qat/qat_api/common/utils/sal_versions.c`** -> AI Confidence: **99.39%**
2256. **`sys/dev/qat/qat_api/device/dev_info.c`** -> AI Confidence: **99.39%**
2257. **`sys/dev/qat/qat_hw/qat_200xx/adf_drv.c`** -> AI Confidence: **99.39%**
2258. **`sys/dev/qat/qat_hw/qat_c3xxx/adf_drv.c`** -> AI Confidence: **99.39%**
2259. **`sys/dev/qat/qat_hw/qat_c4xxx/adf_drv.c`** -> AI Confidence: **99.39%**
2260. **`sys/dev/qat/qat_hw/qat_c62x/adf_drv.c`** -> AI Confidence: **99.39%**
2261. **`sys/dev/qcom_tcsr/qcom_tcsr.c`** -> AI Confidence: **99.39%**
2262. **`sys/dev/qlxgb/qla_ioctl.c`** -> AI Confidence: **99.39%**
2263. **`sys/dev/qlxgb/qla_isr.c`** -> AI Confidence: **99.39%**
2264. **`sys/dev/qlxgbe/ql_ioctl.c`** -> AI Confidence: **99.39%**
2265. **`sys/dev/qlxgbe/ql_isr.c`** -> AI Confidence: **99.39%**
2266. **`sys/dev/random/darn.c`** -> AI Confidence: **99.39%**
2267. **`sys/dev/rtwn/rtl8821a/r21a_rx.c`** -> AI Confidence: **99.39%**
2268. **`sys/dev/sfxge/sfxge_rx.c`** -> AI Confidence: **99.39%**
2269. **`sys/dev/smbus/smbconf.c`** -> AI Confidence: **99.39%**
2270. **`sys/dev/sound/pci/maestro3.c`** -> AI Confidence: **99.39%**
2271. **`sys/dev/sound/pcm/dsp.c`** -> AI Confidence: **99.39%**
2272. **`sys/dev/sym/sym_hipd.c`** -> AI Confidence: **99.39%**
2273. **`sys/dev/syscons/dragon/dragon_saver.c`** -> AI Confidence: **99.39%**
2274. **`sys/dev/syscons/fade/fade_saver.c`** -> AI Confidence: **99.39%**
2275. **`sys/dev/syscons/fire/fire_saver.c`** -> AI Confidence: **99.39%**
2276. **`sys/dev/syscons/logo/logo_saver.c`** -> AI Confidence: **99.39%**
2277. **`sys/dev/syscons/plasma/plasma_saver.c`** -> AI Confidence: **99.39%**
2278. **`sys/dev/syscons/scgfbrndr.c`** -> AI Confidence: **99.39%**
2279. **`sys/dev/syscons/scvesactl.c`** -> AI Confidence: **99.39%**
2280. **`sys/dev/syscons/scvgarndr.c`** -> AI Confidence: **99.39%**
2281. **`sys/dev/syscons/snake/snake_saver.c`** -> AI Confidence: **99.39%**
2282. **`sys/dev/syscons/syscons.c`** -> AI Confidence: **99.39%**
2283. **`sys/dev/syscons/sysmouse.c`** -> AI Confidence: **99.39%**
2284. **`sys/dev/syscons/warp/warp_saver.c`** -> AI Confidence: **99.39%**
2285. **`sys/dev/uart/uart_cpu_acpi.c`** -> AI Confidence: **99.39%**
2286. **`sys/dev/uart/uart_cpu_x86.c`** -> AI Confidence: **99.39%**
2287. **`sys/dev/usb/controller/dwc_otg.c`** -> AI Confidence: **99.39%**
2288. **`sys/dev/usb/controller/ehci_imx.c`** -> AI Confidence: **99.39%**
2289. **`sys/dev/usb/controller/ehci_pci.c`** -> AI Confidence: **99.39%**
2290. **`sys/dev/usb/storage/ustorage_fs.c`** -> AI Confidence: **99.39%**
2291. **`sys/dev/usb/usb_lookup.c`** -> AI Confidence: **99.39%**
2292. **`sys/dev/usb/usb_pf.c`** -> AI Confidence: **99.39%**
2293. **`sys/dev/vnic/thunder_bgx_fdt.c`** -> AI Confidence: **99.39%**
2294. **`sys/dev/wbwd/wbwd.c`** -> AI Confidence: **99.39%**
2295. **`sys/dev/xl/if_xl.c`** -> AI Confidence: **99.39%**
2296. **`sys/fs/cd9660/cd9660_rrip.c`** -> AI Confidence: **99.39%**
2297. **`sys/fs/cd9660/cd9660_util.c`** -> AI Confidence: **99.39%**
2298. **`sys/fs/ext2fs/ext2_subr.c`** -> AI Confidence: **99.39%**
2299. **`sys/fs/fuse/fuse_io.c`** -> AI Confidence: **99.39%**
2300. **`sys/fs/msdosfs/msdosfs_conv.c`** -> AI Confidence: **99.39%**
2301. **`sys/fs/nfsclient/nfs_clbio.c`** -> AI Confidence: **99.39%**
2302. **`sys/fs/nfsclient/nfs_clvfsops.c`** -> AI Confidence: **99.39%**
2303. **`sys/fs/procfs/procfs_rlimit.c`** -> AI Confidence: **99.39%**
2304. **`sys/gdb/gdb_main.c`** -> AI Confidence: **99.39%**
2305. **`sys/gnu/dev/bwn/phy_n/if_bwn_phy_n_core.c`** -> AI Confidence: **99.39%**
2306. **`sys/i386/i386/bios.c`** -> AI Confidence: **99.39%**
2307. **`sys/i386/i386/elan-mmcr.c`** -> AI Confidence: **99.39%**
2308. **`sys/isa/isa_common.c`** -> AI Confidence: **99.39%**
2309. **`sys/isa/pnpparse.c`** -> AI Confidence: **99.39%**
2310. **`sys/kern/imgact_shell.c`** -> AI Confidence: **99.39%**
2311. **`sys/kern/kern_malloc.c`** -> AI Confidence: **99.39%**
2312. **`sys/kern/kern_ntptime.c`** -> AI Confidence: **99.39%**
2313. **`sys/kern/subr_blist.c`** -> AI Confidence: **99.39%**
2314. **`sys/kern/subr_hints.c`** -> AI Confidence: **99.39%**
2315. **`sys/kern/sys_process.c`** -> AI Confidence: **99.39%**
2316. **`sys/kern/tty_compat.c`** -> AI Confidence: **99.39%**
2317. **`sys/kern/vfs_cluster.c`** -> AI Confidence: **99.39%**
2318. **`sys/kgssapi/gssd_prot.c`** -> AI Confidence: **99.39%**
2319. **`sys/net/altq/altq_rio.c`** -> AI Confidence: **99.39%**
2320. **`sys/net/if_mib.c`** -> AI Confidence: **99.39%**
2321. **`sys/net/slcompress.c`** -> AI Confidence: **99.39%**
2322. **`sys/net80211/ieee80211_action.c`** -> AI Confidence: **99.39%**
2323. **`sys/net80211/ieee80211_adhoc.c`** -> AI Confidence: **99.39%**
2324. **`sys/net80211/ieee80211_ioctl.c`** -> AI Confidence: **99.39%**
2325. **`sys/netgraph/bluetooth/hci/ng_hci_evnt.c`** -> AI Confidence: **99.39%**
2326. **`sys/netgraph/ng_async.c`** -> AI Confidence: **99.39%**
2327. **`sys/netgraph/ng_mppc.c`** -> AI Confidence: **99.39%**
2328. **`sys/netgraph/ng_one2many.c`** -> AI Confidence: **99.39%**
2329. **`sys/netgraph/ng_pppoe.c`** -> AI Confidence: **99.39%**
2330. **`sys/netgraph/ng_pptpgre.c`** -> AI Confidence: **99.39%**
2331. **`sys/netinet/sctp_usrreq.c`** -> AI Confidence: **99.39%**
2332. **`sys/netinet/tcp_ratelimit.c`** -> AI Confidence: **99.39%**
2333. **`sys/netinet/tcp_stacks/bbr.c`** -> AI Confidence: **99.39%**
2334. **`sys/netinet/tcp_stacks/rack.c`** -> AI Confidence: **99.39%**
2335. **`sys/netinet/tcp_subr.c`** -> AI Confidence: **99.39%**
2336. **`sys/netinet6/ip6_output.c`** -> AI Confidence: **99.39%**
2337. **`sys/netipsec/xform_esp.c`** -> AI Confidence: **99.39%**
2338. **`sys/netpfil/ipfilter/netinet/fil.c`** -> AI Confidence: **99.39%**
2339. **`sys/netpfil/ipfilter/netinet/ip_auth.c`** -> AI Confidence: **99.39%**
2340. **`sys/netpfil/ipfilter/netinet/ip_proxy.c`** -> AI Confidence: **99.39%**
2341. **`sys/netpfil/ipfilter/netinet/ip_sync.c`** -> AI Confidence: **99.39%**
2342. **`sys/opencrypto/cryptodeflate.c`** -> AI Confidence: **99.39%**
2343. **`sys/powerpc/powerpc/interrupt.c`** -> AI Confidence: **99.39%**
2344. **`sys/powerpc/powerpc/syncicache.c`** -> AI Confidence: **99.39%**
2345. **`sys/riscv/riscv/busdma_bounce.c`** -> AI Confidence: **99.39%**
2346. **`sys/rpc/clnt_vc.c`** -> AI Confidence: **99.39%**
2347. **`sys/security/mac_bsdextended/mac_bsdextended.c`** -> AI Confidence: **99.39%**
2348. **`sys/security/mac_ntpd/mac_ntpd.c`** -> AI Confidence: **99.39%**
2349. **`sys/ufs/ffs/ffs_inode.c`** -> AI Confidence: **99.39%**
2350. **`sys/vm/vm_mmap.c`** -> AI Confidence: **99.39%**
2351. **`sys/x86/isa/isa_dma.c`** -> AI Confidence: **99.39%**
2352. **`sys/x86/pci/pci_bus.c`** -> AI Confidence: **99.39%**
2353. **`tests/sys/cddl/zfs/bin/readmmap.c`** -> AI Confidence: **99.39%**
2354. **`tests/sys/fs/tarfs/mktar.c`** -> AI Confidence: **99.39%**
2355. **`tests/sys/fs/tarfs/tarsum.c`** -> AI Confidence: **99.39%**
2356. **`tests/sys/mqueue/mqtest2.c`** -> AI Confidence: **99.39%**
2357. **`tests/sys/mqueue/mqtest4.c`** -> AI Confidence: **99.39%**
2358. **`tests/sys/mqueue/mqtest5.c`** -> AI Confidence: **99.39%**
2359. **`tests/sys/net/transient_tuntap.c`** -> AI Confidence: **99.39%**
2360. **`tests/sys/netinet/tcp_user_cookie.c`** -> AI Confidence: **99.39%**
2361. **`tools/regression/aio/aiop/aiop.c`** -> AI Confidence: **99.39%**
2362. **`tools/regression/bpf/bpf_filter/bpf_test.c`** -> AI Confidence: **99.39%**
2363. **`tools/regression/capsicum/syscalls/cap_fcntls_limit.c`** -> AI Confidence: **99.39%**
2364. **`tools/regression/environ/timings.c`** -> AI Confidence: **99.39%**
2365. **`tools/regression/gaithrstress/gaithrstress.c`** -> AI Confidence: **99.39%**
2366. **`tools/regression/netinet/ipmulticast/ipmulticast.c`** -> AI Confidence: **99.39%**
2367. **`tools/regression/netinet/ipsockopt/ipsockopt.c`** -> AI Confidence: **99.39%**
2368. **`tools/regression/netinet/tcpstream/tcpstream.c`** -> AI Confidence: **99.39%**
2369. **`tools/regression/netinet6/icmp6_filter/icmp6_filter.c`** -> AI Confidence: **99.39%**
2370. **`tools/regression/posixsem2/semtest.c`** -> AI Confidence: **99.39%**
2371. **`tools/regression/priv/main.c`** -> AI Confidence: **99.39%**
2372. **`tools/regression/priv/priv_sched_rtprio.c`** -> AI Confidence: **99.39%**
2373. **`tools/regression/priv/priv_sched_setpriority.c`** -> AI Confidence: **99.39%**
2374. **`tools/regression/rpcsec_gss/rpctest.c`** -> AI Confidence: **99.39%**
2375. **`tools/regression/security/cap_test/cap_test_pdfork.c`** -> AI Confidence: **99.39%**
2376. **`tools/regression/security/open_to_operation/open_to_operation.c`** -> AI Confidence: **99.39%**
2377. **`tools/regression/sockets/shutdown/shutdown.c`** -> AI Confidence: **99.39%**
2378. **`tools/regression/sockets/unix_cmsg/t_cmsgcred_sockcred.c`** -> AI Confidence: **99.39%**
2379. **`tools/regression/ufs/uprintf/ufs_uprintf.c`** -> AI Confidence: **99.39%**
2380. **`tools/test/net/listen.c`** -> AI Confidence: **99.39%**
2381. **`tools/test/stress2/lib/main.c`** -> AI Confidence: **99.39%**
2382. **`tools/test/stress2/lib/resources.c`** -> AI Confidence: **99.39%**
2383. **`tools/test/stress2/testcases/dirrename/dirrename.c`** -> AI Confidence: **99.39%**
2384. **`tools/test/stress2/testcases/mkfifo/mkfifo.c`** -> AI Confidence: **99.39%**
2385. **`tools/test/stress2/testcases/mmap/mmap.c`** -> AI Confidence: **99.39%**
2386. **`tools/test/stress2/testcases/pty/pty.c`** -> AI Confidence: **99.39%**
2387. **`tools/test/stress2/testcases/rename/rename.c`** -> AI Confidence: **99.39%**
2388. **`tools/test/stress2/tools/swap.c`** -> AI Confidence: **99.39%**
2389. **`tools/tools/ath/athalq/main.c`** -> AI Confidence: **99.39%**
2390. **`tools/tools/ath/athkey/athkey.c`** -> AI Confidence: **99.39%**
2391. **`tools/tools/ath/athpow/athpow.c`** -> AI Confidence: **99.39%**
2392. **`tools/tools/ath/athrd/athrd.c`** -> AI Confidence: **99.39%**
2393. **`tools/tools/ath/athspectral/athspectral.c`** -> AI Confidence: **99.39%**
2394. **`tools/tools/fib_multibind/sink.c`** -> AI Confidence: **99.39%**
2395. **`tools/tools/intel-ucode-split/intel-ucode-split.c`** -> AI Confidence: **99.39%**
2396. **`tools/tools/mwl/mwlstats/mwlstats.c`** -> AI Confidence: **99.39%**
2397. **`tools/tools/net80211/stumbler/stumbler.c`** -> AI Confidence: **99.39%**
2398. **`tools/tools/net80211/wlaninject/wlaninject.c`** -> AI Confidence: **99.39%**
2399. **`tools/tools/net80211/wlanwatch/wlanwatch.c`** -> AI Confidence: **99.39%**
2400. **`tools/tools/usbtest/usb_modem_test.c`** -> AI Confidence: **99.39%**
2401. **`tools/tools/usbtest/usb_msc_test.c`** -> AI Confidence: **99.39%**
2402. **`tools/tools/zfsboottest/zfsboottest.c`** -> AI Confidence: **99.39%**
2403. **`usr.bin/apply/apply.c`** -> AI Confidence: **99.39%**
2404. **`usr.bin/ar/ar.c`** -> AI Confidence: **99.39%**
2405. **`usr.bin/at/at.c`** -> AI Confidence: **99.39%**
2406. **`usr.bin/basename/basename.c`** -> AI Confidence: **99.39%**
2407. **`usr.bin/bintrans/uuencode.c`** -> AI Confidence: **99.39%**
2408. **`usr.bin/calendar/calendar.c`** -> AI Confidence: **99.39%**
2409. **`usr.bin/calendar/pom.c`** -> AI Confidence: **99.39%**
2410. **`usr.bin/chat/chat.c`** -> AI Confidence: **99.39%**
2411. **`usr.bin/chpass/util.c`** -> AI Confidence: **99.39%**
2412. **`usr.bin/cksum/cksum.c`** -> AI Confidence: **99.39%**
2413. **`usr.bin/column/column.c`** -> AI Confidence: **99.39%**
2414. **`usr.bin/compress/compress.c`** -> AI Confidence: **99.39%**
2415. **`usr.bin/csplit/csplit.c`** -> AI Confidence: **99.39%**
2416. **`usr.bin/ctags/ctags.c`** -> AI Confidence: **99.39%**
2417. **`usr.bin/ctags/tree.c`** -> AI Confidence: **99.39%**
2418. **`usr.bin/ctlstat/ctlstat.c`** -> AI Confidence: **99.39%**
2419. **`usr.bin/diff/pr.c`** -> AI Confidence: **99.39%**
2420. **`usr.bin/du/du.c`** -> AI Confidence: **99.39%**
2421. **`usr.bin/find/main.c`** -> AI Confidence: **99.39%**
2422. **`usr.bin/gcore/gcore.c`** -> AI Confidence: **99.39%**
2423. **`usr.bin/getconf/getconf.c`** -> AI Confidence: **99.39%**
2424. **`usr.bin/getent/getent.c`** -> AI Confidence: **99.39%**
2425. **`usr.bin/gprof/elf.c`** -> AI Confidence: **99.39%**
2426. **`usr.bin/head/head.c`** -> AI Confidence: **99.39%**
2427. **`usr.bin/hexdump/display.c`** -> AI Confidence: **99.39%**
2428. **`usr.bin/hexdump/hexdump.c`** -> AI Confidence: **99.39%**
2429. **`usr.bin/indent/pr_comment.c`** -> AI Confidence: **99.39%**
2430. **`usr.bin/ipcs/ipcs.c`** -> AI Confidence: **99.39%**
2431. **`usr.bin/kdump/kdump.c`** -> AI Confidence: **99.39%**
2432. **`usr.bin/ktrace/ktrace.c`** -> AI Confidence: **99.39%**
2433. **`usr.bin/lam/lam.c`** -> AI Confidence: **99.39%**
2434. **`usr.bin/last/last.c`** -> AI Confidence: **99.39%**
2435. **`usr.bin/ldd/ldd.c`** -> AI Confidence: **99.39%**
2436. **`usr.bin/leave/leave.c`** -> AI Confidence: **99.39%**
2437. **`usr.bin/localedef/time.c`** -> AI Confidence: **99.39%**
2438. **`usr.bin/locate/code/locate.code.c`** -> AI Confidence: **99.39%**
2439. **`usr.bin/locate/locate/locate.c`** -> AI Confidence: **99.39%**
2440. **`usr.bin/locate/locate/util.c`** -> AI Confidence: **99.39%**
2441. **`usr.bin/logger/logger.c`** -> AI Confidence: **99.39%**
2442. **`usr.bin/login/login_audit.c`** -> AI Confidence: **99.39%**
2443. **`usr.bin/mkimg/vmdk.c`** -> AI Confidence: **99.39%**
2444. **`usr.bin/mt/mt.c`** -> AI Confidence: **99.39%**
2445. **`usr.bin/ncal/ncal.c`** -> AI Confidence: **99.39%**
2446. **`usr.bin/netstat/bpf.c`** -> AI Confidence: **99.39%**
2447. **`usr.bin/netstat/inet.c`** -> AI Confidence: **99.39%**
2448. **`usr.bin/netstat/pfkey.c`** -> AI Confidence: **99.39%**
2449. **`usr.bin/netstat/sctp.c`** -> AI Confidence: **99.39%**
2450. **`usr.bin/number/number.c`** -> AI Confidence: **99.39%**
2451. **`usr.bin/patch/pch.c`** -> AI Confidence: **99.39%**
2452. **`usr.bin/posixshmcontrol/posixshmcontrol.c`** -> AI Confidence: **99.39%**
2453. **`usr.bin/pr/pr.c`** -> AI Confidence: **99.39%**
2454. **`usr.bin/random/randomize_fd.c`** -> AI Confidence: **99.39%**
2455. **`usr.bin/rctl/rctl.c`** -> AI Confidence: **99.39%**
2456. **`usr.bin/runat/runat.c`** -> AI Confidence: **99.39%**
2457. **`usr.bin/sockstat/main.c`** -> AI Confidence: **99.39%**
2458. **`usr.bin/soelim/soelim.c`** -> AI Confidence: **99.39%**
2459. **`usr.bin/stat/stat.c`** -> AI Confidence: **99.39%**
2460. **`usr.bin/systat/keyboard.c`** -> AI Confidence: **99.39%**
2461. **`usr.bin/tail/forward.c`** -> AI Confidence: **99.39%**
2462. **`usr.bin/tail/reverse.c`** -> AI Confidence: **99.39%**
2463. **`usr.bin/talk/get_names.c`** -> AI Confidence: **99.39%**
2464. **`usr.bin/top/display.c`** -> AI Confidence: **99.39%**
2465. **`usr.bin/truss/main.c`** -> AI Confidence: **99.39%**
2466. **`usr.bin/truss/syscalls.c`** -> AI Confidence: **99.39%**
2467. **`usr.bin/vgrind/vfontedpr.c`** -> AI Confidence: **99.39%**
2468. **`usr.bin/vmstat/vmstat.c`** -> AI Confidence: **99.39%**
2469. **`usr.bin/vtfontcvt/vtfontcvt.c`** -> AI Confidence: **99.39%**
2470. **`usr.bin/which/which.c`** -> AI Confidence: **99.39%**
2471. **`usr.bin/xargs/xargs.c`** -> AI Confidence: **99.39%**
2472. **`usr.bin/xstr/xstr.c`** -> AI Confidence: **99.39%**
2473. **`usr.bin/ypcat/ypcat.c`** -> AI Confidence: **99.39%**
2474. **`usr.sbin/acpi/acpiconf/acpiconf.c`** -> AI Confidence: **99.39%**
2475. **`usr.sbin/acpi/acpidump/acpi.c`** -> AI Confidence: **99.39%**
2476. **`usr.sbin/bhyve/bhyverun.c`** -> AI Confidence: **99.39%**
2477. **`usr.sbin/bhyve/uart_pl011.c`** -> AI Confidence: **99.39%**
2478. **`usr.sbin/bhyve/usb_mouse.c`** -> AI Confidence: **99.39%**
2479. **`usr.sbin/binmiscctl/binmiscctl.c`** -> AI Confidence: **99.39%**
2480. **`usr.sbin/bluetooth/bthidcontrol/sdp.c`** -> AI Confidence: **99.39%**
2481. **`usr.sbin/bluetooth/bthidd/btuinput.c`** -> AI Confidence: **99.39%**
2482. **`usr.sbin/bluetooth/iwmbtfw/main.c`** -> AI Confidence: **99.39%**
2483. **`usr.sbin/bluetooth/l2ping/l2ping.c`** -> AI Confidence: **99.39%**
2484. **`usr.sbin/bluetooth/sdpd/ssr.c`** -> AI Confidence: **99.39%**
2485. **`usr.sbin/bootparamd/bootparamd/main.c`** -> AI Confidence: **99.39%**
2486. **`usr.sbin/bsdinstall/partedit/scripted.c`** -> AI Confidence: **99.39%**
2487. **`usr.sbin/bsnmpd/modules/snmp_wlan/wlan_snmp.c`** -> AI Confidence: **99.39%**
2488. **`usr.sbin/bsnmpd/modules/snmp_wlan/wlan_sys.c`** -> AI Confidence: **99.39%**
2489. **`usr.sbin/btxld/btxld.c`** -> AI Confidence: **99.39%**
2490. **`usr.sbin/cpucontrol/cpucontrol.c`** -> AI Confidence: **99.39%**
2491. **`usr.sbin/cpucontrol/via.c`** -> AI Confidence: **99.39%**
2492. **`usr.sbin/ctladm/util.c`** -> AI Confidence: **99.39%**
2493. **`usr.sbin/dconschat/dconschat.c`** -> AI Confidence: **99.39%**
2494. **`usr.sbin/efidp/efidp.c`** -> AI Confidence: **99.39%**
2495. **`usr.sbin/efivar/efivar.c`** -> AI Confidence: **99.39%**
2496. **`usr.sbin/fdcontrol/fdcontrol.c`** -> AI Confidence: **99.39%**
2497. **`usr.sbin/fdread/fdutil.c`** -> AI Confidence: **99.39%**
2498. **`usr.sbin/fifolog/fifolog_reader/fifolog_reader.c`** -> AI Confidence: **99.39%**
2499. **`usr.sbin/fstyp/hammer.c`** -> AI Confidence: **99.39%**
2500. **`usr.sbin/fstyp/hammer2.c`** -> AI Confidence: **99.39%**
2501. **`usr.sbin/fwcontrol/fwdv.c`** -> AI Confidence: **99.39%**
2502. **`usr.sbin/i2c/i2c.c`** -> AI Confidence: **99.39%**
2503. **`usr.sbin/jail/command.c`** -> AI Confidence: **99.39%**
2504. **`usr.sbin/jail/jail.c`** -> AI Confidence: **99.39%**
2505. **`usr.sbin/jls/jls.c`** -> AI Confidence: **99.39%**
2506. **`usr.sbin/kbdcontrol/kbdcontrol.c`** -> AI Confidence: **99.39%**
2507. **`usr.sbin/kbdmap/kbdmap.c`** -> AI Confidence: **99.39%**
2508. **`usr.sbin/kldxref/kldxref.c`** -> AI Confidence: **99.39%**
2509. **`usr.sbin/lpr/common_source/ctlinfo.c`** -> AI Confidence: **99.39%**
2510. **`usr.sbin/lpr/common_source/displayq.c`** -> AI Confidence: **99.39%**
2511. **`usr.sbin/lpr/lpc/lpc.c`** -> AI Confidence: **99.39%**
2512. **`usr.sbin/lpr/lpd/recvjob.c`** -> AI Confidence: **99.39%**
2513. **`usr.sbin/mailwrapper/mailwrapper.c`** -> AI Confidence: **99.39%**
2514. **`usr.sbin/makefs/cd9660.c`** -> AI Confidence: **99.39%**
2515. **`usr.sbin/makefs/ffs/ufs_bmap.c`** -> AI Confidence: **99.39%**
2516. **`usr.sbin/makefs/zfs/fs.c`** -> AI Confidence: **99.39%**
2517. **`usr.sbin/memcontrol/memcontrol.c`** -> AI Confidence: **99.39%**
2518. **`usr.sbin/mfiutil/mfi_flash.c`** -> AI Confidence: **99.39%**
2519. **`usr.sbin/mfiutil/mfiutil.c`** -> AI Confidence: **99.39%**
2520. **`usr.sbin/mlx5tool/mlx5tool.c`** -> AI Confidence: **99.39%**
2521. **`usr.sbin/mlxcontrol/command.c`** -> AI Confidence: **99.39%**
2522. **`usr.sbin/mlxcontrol/util.c`** -> AI Confidence: **99.39%**
2523. **`usr.sbin/mpsutil/mpsutil.c`** -> AI Confidence: **99.39%**
2524. **`usr.sbin/mptable/mptable.c`** -> AI Confidence: **99.39%**
2525. **`usr.sbin/mptutil/mpt_show.c`** -> AI Confidence: **99.39%**
2526. **`usr.sbin/ndp/ndp.c`** -> AI Confidence: **99.39%**
2527. **`usr.sbin/nfsd/nfsd.c`** -> AI Confidence: **99.39%**
2528. **`usr.sbin/nfsdumpstate/nfsdumpstate.c`** -> AI Confidence: **99.39%**
2529. **`usr.sbin/ngctl/dot.c`** -> AI Confidence: **99.39%**
2530. **`usr.sbin/ngctl/main.c`** -> AI Confidence: **99.39%**
2531. **`usr.sbin/nvram/nvram.c`** -> AI Confidence: **99.39%**
2532. **`usr.sbin/pciconf/cap.c`** -> AI Confidence: **99.39%**
2533. **`usr.sbin/pciconf/pciconf.c`** -> AI Confidence: **99.39%**
2534. **`usr.sbin/pmcstudy/eval_expr.c`** -> AI Confidence: **99.39%**
2535. **`usr.sbin/pmcstudy/pmcstudy.c`** -> AI Confidence: **99.39%**
2536. **`usr.sbin/powerd/powerd.c`** -> AI Confidence: **99.39%**
2537. **`usr.sbin/ppp/chap.c`** -> AI Confidence: **99.39%**
2538. **`usr.sbin/ppp/chat.c`** -> AI Confidence: **99.39%**
2539. **`usr.sbin/ppp/filter.c`** -> AI Confidence: **99.39%**
2540. **`usr.sbin/ppp/ip.c`** -> AI Confidence: **99.39%**
2541. **`usr.sbin/ppp/lcp.c`** -> AI Confidence: **99.39%**
2542. **`usr.sbin/ppp/main.c`** -> AI Confidence: **99.39%**
2543. **`usr.sbin/ppp/radius.c`** -> AI Confidence: **99.39%**
2544. **`usr.sbin/quotaon/quotaon.c`** -> AI Confidence: **99.39%**
2545. **`usr.sbin/rmt/rmt.c`** -> AI Confidence: **99.39%**
2546. **`usr.sbin/rpc.umntall/rpc.umntall.c`** -> AI Confidence: **99.39%**
2547. **`usr.sbin/rpc.ypupdated/yp_dbupdate.c`** -> AI Confidence: **99.39%**
2548. **`usr.sbin/rpcbind/pmap_svc.c`** -> AI Confidence: **99.39%**
2549. **`usr.sbin/rpcbind/rpcbind.c`** -> AI Confidence: **99.39%**
2550. **`usr.sbin/rtsold/rtsold.c`** -> AI Confidence: **99.39%**
2551. **`usr.sbin/sa/db.c`** -> AI Confidence: **99.39%**
2552. **`usr.sbin/sa/main.c`** -> AI Confidence: **99.39%**
2553. **`usr.sbin/services_mkdb/services_mkdb.c`** -> AI Confidence: **99.39%**
2554. **`usr.sbin/syslogd/syslogd.c`** -> AI Confidence: **99.39%**
2555. **`usr.sbin/traceroute/traceroute.c`** -> AI Confidence: **99.39%**
2556. **`usr.sbin/uathload/uathload.c`** -> AI Confidence: **99.39%**
2557. **`usr.sbin/uefisign/uefisign.c`** -> AI Confidence: **99.39%**
2558. **`usr.sbin/valectl/valectl.c`** -> AI Confidence: **99.39%**
2559. **`usr.sbin/vipw/vipw.c`** -> AI Confidence: **99.39%**
2560. **`usr.sbin/virtual_oss/virtual_equalizer/equalizer.c`** -> AI Confidence: **99.39%**
2561. **`usr.sbin/watchdogd/watchdogd.c`** -> AI Confidence: **99.39%**
2562. **`usr.sbin/ypldap/aldap.c`** -> AI Confidence: **99.39%**
2563. **`bin/sh/bltin/bltin.h`** -> AI Confidence: **99.39%**
2564. **`contrib/llvm-project/clang/include/clang/Tooling/Refactoring/RefactoringActionRulesInternal.h`** -> AI Confidence: **99.39%**
2565. **`contrib/llvm-project/clang/include/clang/Tooling/Transformer/RewriteRule.h`** -> AI Confidence: **99.39%**
2566. **`contrib/llvm-project/libcxx/include/__algorithm/ranges_partition_copy.h`** -> AI Confidence: **99.39%**
2567. **`contrib/llvm-project/libcxx/include/__algorithm/ranges_sample.h`** -> AI Confidence: **99.39%**
2568. **`contrib/llvm-project/libcxx/include/__concepts/swappable.h`** -> AI Confidence: **99.39%**
2569. **`contrib/llvm-project/libcxx/include/__iterator/iter_swap.h`** -> AI Confidence: **99.39%**
2570. **`contrib/llvm-project/libcxx/include/__mutex/once_flag.h`** -> AI Confidence: **99.39%**
2571. **`contrib/llvm-project/libcxx/include/__random/cauchy_distribution.h`** -> AI Confidence: **99.39%**
2572. **`contrib/llvm-project/libcxx/include/__random/extreme_value_distribution.h`** -> AI Confidence: **99.39%**
2573. **`contrib/llvm-project/libcxx/include/__random/seed_seq.h`** -> AI Confidence: **99.39%**
2574. **`contrib/llvm-project/libcxx/include/__random/weibull_distribution.h`** -> AI Confidence: **99.39%**
2575. **`contrib/llvm-project/libcxx/include/__type_traits/make_32_64_or_128_bit.h`** -> AI Confidence: **99.39%**
2576. **`contrib/llvm-project/libcxx/src/include/to_chars_floating_point.h`** -> AI Confidence: **99.39%**
2577. **`contrib/llvm-project/llvm/include/llvm/DebugInfo/Symbolize/Symbolize.h`** -> AI Confidence: **99.39%**
2578. **`contrib/tzcode/private.h`** -> AI Confidence: **99.39%**
2579. **`crypto/openssl/include/openssl/e_os2.h`** -> AI Confidence: **99.39%**
2580. **`cddl/usr.sbin/zfsd/zfsd.cc`** -> AI Confidence: **99.39%**
2581. **`cddl/usr.sbin/zfsd/zfsd_main.cc`** -> AI Confidence: **99.39%**
2582. **`contrib/atf/atf-c++/detail/text.cpp`** -> AI Confidence: **99.39%**
2583. **`contrib/atf/atf-sh/atf-check.cpp`** -> AI Confidence: **99.39%**
2584. **`contrib/kyua/cli/cmd_help.cpp`** -> AI Confidence: **99.39%**
2585. **`contrib/kyua/utils/cmdline/parser.cpp`** -> AI Confidence: **99.39%**
2586. **`contrib/kyua/utils/fs/operations_test.cpp`** -> AI Confidence: **99.39%**
2587. **`contrib/llvm-project/libcxx/src/filesystem/directory_entry.cpp`** -> AI Confidence: **99.39%**
2588. **`contrib/llvm-project/libcxx/src/random.cpp`** -> AI Confidence: **99.39%**
2589. **`contrib/llvm-project/libcxx/src/strstream.cpp`** -> AI Confidence: **99.39%**
2590. **`contrib/llvm-project/libcxx/src/verbose_abort.cpp`** -> AI Confidence: **99.39%**
2591. **`contrib/llvm-project/libunwind/src/Unwind-EHABI.cpp`** -> AI Confidence: **99.39%**
2592. **`contrib/llvm-project/lld/COFF/Driver.cpp`** -> AI Confidence: **99.39%**
2593. **`contrib/llvm-project/lld/ELF/Arch/Mips.cpp`** -> AI Confidence: **99.39%**
2594. **`contrib/llvm-project/lld/ELF/Arch/SystemZ.cpp`** -> AI Confidence: **99.39%**
2595. **`contrib/llvm-project/lld/ELF/Driver.cpp`** -> AI Confidence: **99.39%**
2596. **`contrib/llvm-project/lld/ELF/LTO.cpp`** -> AI Confidence: **99.39%**
2597. **`contrib/llvm-project/lldb/source/API/SBFrame.cpp`** -> AI Confidence: **99.39%**
2598. **`contrib/llvm-project/lldb/source/Commands/CommandObjectBreakpoint.cpp`** -> AI Confidence: **99.39%**
2599. **`contrib/llvm-project/lldb/source/Commands/CommandObjectExpression.cpp`** -> AI Confidence: **99.39%**
2600. **`contrib/llvm-project/lldb/source/Commands/CommandObjectLog.cpp`** -> AI Confidence: **99.39%**
2601. **`contrib/llvm-project/lldb/source/Commands/CommandObjectRegister.cpp`** -> AI Confidence: **99.39%**
2602. **`contrib/llvm-project/lldb/source/Commands/CommandObjectSession.cpp`** -> AI Confidence: **99.39%**
2603. **`contrib/llvm-project/lldb/source/Commands/CommandObjectSource.cpp`** -> AI Confidence: **99.39%**
2604. **`contrib/llvm-project/lldb/source/Core/DynamicLoader.cpp`** -> AI Confidence: **99.39%**
2605. **`contrib/llvm-project/lldb/source/Core/ValueObject.cpp`** -> AI Confidence: **99.39%**
2606. **`contrib/llvm-project/lldb/source/Core/ValueObjectChild.cpp`** -> AI Confidence: **99.39%**
2607. **`contrib/llvm-project/lldb/source/DataFormatters/CXXFunctionPointer.cpp`** -> AI Confidence: **99.39%**
2608. **`contrib/llvm-project/lldb/source/DataFormatters/ValueObjectPrinter.cpp`** -> AI Confidence: **99.39%**
2609. **`contrib/llvm-project/lldb/source/Expression/IRMemoryMap.cpp`** -> AI Confidence: **99.39%**
2610. **`contrib/llvm-project/lldb/source/Initialization/SystemInitializerCommon.cpp`** -> AI Confidence: **99.39%**
2611. **`contrib/llvm-project/lldb/source/Interpreter/CommandObject.cpp`** -> AI Confidence: **99.39%**
2612. **`contrib/llvm-project/lldb/source/Interpreter/OptionArgParser.cpp`** -> AI Confidence: **99.39%**
2613. **`contrib/llvm-project/lldb/source/Interpreter/Options.cpp`** -> AI Confidence: **99.39%**
2614. **`contrib/llvm-project/lldb/source/Plugins/ABI/AArch64/ABIMacOSX_arm64.cpp`** -> AI Confidence: **99.39%**
2615. **`contrib/llvm-project/lldb/source/Plugins/ABI/AArch64/ABISysV_arm64.cpp`** -> AI Confidence: **99.39%**
2616. **`contrib/llvm-project/lldb/source/Plugins/ABI/ARM/ABIMacOSX_arm.cpp`** -> AI Confidence: **99.39%**
2617. **`contrib/llvm-project/lldb/source/Plugins/ABI/X86/ABISysV_i386.cpp`** -> AI Confidence: **99.39%**
2618. **`contrib/llvm-project/lldb/source/Plugins/Disassembler/LLVMC/DisassemblerLLVMC.cpp`** -> AI Confidence: **99.39%**
2619. **`contrib/llvm-project/lldb/source/Plugins/Instruction/ARM/EmulateInstructionARM.cpp`** -> AI Confidence: **99.39%**
2620. **`contrib/llvm-project/lldb/source/Plugins/Instruction/MIPS64/EmulateInstructionMIPS64.cpp`** -> AI Confidence: **99.39%**
2621. **`contrib/llvm-project/lldb/source/Plugins/Language/CPlusPlus/CPlusPlusNameParser.cpp`** -> AI Confidence: **99.39%**
2622. **`contrib/llvm-project/lldb/source/Plugins/ObjectFile/ELF/ObjectFileELF.cpp`** -> AI Confidence: **99.39%**
2623. **`contrib/llvm-project/lldb/source/Plugins/Process/Utility/RegisterContextDarwin_arm64.cpp`** -> AI Confidence: **99.39%**
2624. **`contrib/llvm-project/lldb/source/Plugins/Process/Utility/RegisterContextDarwin_x86_64.cpp`** -> AI Confidence: **99.39%**
2625. **`contrib/llvm-project/lldb/source/Plugins/Process/elf-core/ProcessElfCore.cpp`** -> AI Confidence: **99.39%**
2626. **`contrib/llvm-project/lldb/source/Plugins/Process/gdb-remote/GDBRemoteCommunicationClient.cpp`** -> AI Confidence: **99.39%**
2627. **`contrib/llvm-project/lldb/source/Plugins/Process/gdb-remote/GDBRemoteCommunicationServerCommon.cpp`** -> AI Confidence: **99.39%**
2628. **`contrib/llvm-project/lldb/source/Plugins/SymbolFile/DWARF/DWARFASTParserClang.cpp`** -> AI Confidence: **99.39%**
2629. **`contrib/llvm-project/lldb/source/Plugins/UnwindAssembly/InstEmulation/UnwindAssemblyInstEmulation.cpp`** -> AI Confidence: **99.39%**
2630. **`contrib/llvm-project/lldb/source/Symbol/ArmUnwindInfo.cpp`** -> AI Confidence: **99.39%**
2631. **`contrib/llvm-project/lldb/source/Symbol/CompactUnwindInfo.cpp`** -> AI Confidence: **99.39%**
2632. **`contrib/llvm-project/lldb/source/Symbol/DWARFCallFrameInfo.cpp`** -> AI Confidence: **99.39%**
2633. **`contrib/llvm-project/llvm/lib/Transforms/Utils/CloneFunction.cpp`** -> AI Confidence: **99.39%**
2634. **`contrib/llvm-project/llvm/lib/Transforms/Utils/GlobalStatus.cpp`** -> AI Confidence: **99.39%**
2635. **`contrib/llvm-project/llvm/lib/Transforms/Utils/InlineFunction.cpp`** -> AI Confidence: **99.39%**
2636. **`contrib/llvm-project/llvm/lib/Transforms/Utils/LCSSA.cpp`** -> AI Confidence: **99.39%**
2637. **`contrib/llvm-project/llvm/lib/Transforms/Utils/LibCallsShrinkWrap.cpp`** -> AI Confidence: **99.39%**
2638. **`contrib/llvm-project/llvm/lib/Transforms/Utils/LoopRotationUtils.cpp`** -> AI Confidence: **99.39%**
2639. **`contrib/llvm-project/llvm/lib/Transforms/Utils/SSAUpdaterBulk.cpp`** -> AI Confidence: **99.39%**
2640. **`contrib/llvm-project/llvm/lib/Transforms/Utils/SimplifyCFG.cpp`** -> AI Confidence: **99.39%**
2641. **`contrib/llvm-project/llvm/tools/bugpoint/ExecutionDriver.cpp`** -> AI Confidence: **99.39%**
2642. **`contrib/llvm-project/llvm/tools/llvm-nm/llvm-nm.cpp`** -> AI Confidence: **99.39%**
2643. **`contrib/llvm-project/llvm/tools/llvm-objdump/llvm-objdump.cpp`** -> AI Confidence: **99.39%**
2644. **`contrib/llvm-project/llvm/tools/llvm-readobj/llvm-readobj.cpp`** -> AI Confidence: **99.39%**
2645. **`contrib/llvm-project/llvm/tools/opt/optdriver.cpp`** -> AI Confidence: **99.39%**
2646. **`contrib/llvm-project/llvm/utils/TableGen/AsmWriterEmitter.cpp`** -> AI Confidence: **99.39%**
2647. **`contrib/llvm-project/llvm/utils/TableGen/CompressInstEmitter.cpp`** -> AI Confidence: **99.39%**
2648. **`contrib/llvm-project/llvm/utils/TableGen/SubtargetEmitter.cpp`** -> AI Confidence: **99.39%**
2649. **`contrib/llvm-project/llvm/utils/TableGen/VTEmitter.cpp`** -> AI Confidence: **99.39%**
2650. **`contrib/llvm-project/openmp/runtime/src/kmp_affinity.cpp`** -> AI Confidence: **99.39%**
2651. **`contrib/llvm-project/openmp/runtime/src/kmp_dispatch.cpp`** -> AI Confidence: **99.39%**
2652. **`contrib/llvm-project/openmp/runtime/src/kmp_i18n.cpp`** -> AI Confidence: **99.39%**
2653. **`contrib/llvm-project/openmp/runtime/src/kmp_settings.cpp`** -> AI Confidence: **99.39%**
2654. **`contrib/llvm-project/openmp/runtime/src/kmp_stats_timing.cpp`** -> AI Confidence: **99.39%**
2655. **`contrib/llvm-project/openmp/runtime/src/kmp_tasking.cpp`** -> AI Confidence: **99.39%**
2656. **`contrib/llvm-project/openmp/runtime/src/thirdparty/ittnotify/ittnotify_static.cpp`** -> AI Confidence: **99.39%**
2657. **`contrib/pam-krb5/portable/system.h`** -> AI Confidence: **99.39%**
2658. **`crypto/krb5/src/ccapi/common/win/OldCC/util.cxx`** -> AI Confidence: **99.39%**
2659. **`crypto/krb5/src/ccapi/lib/win/ccapi_os_ipc.cxx`** -> AI Confidence: **99.39%**
2660. **`crypto/krb5/src/windows/leash/Leash.cpp`** -> AI Confidence: **99.39%**
2661. **`libexec/atf/atf-pytest-wrapper/atf_pytest_wrapper.cpp`** -> AI Confidence: **99.39%**
2662. **`sbin/devd/devd.cc`** -> AI Confidence: **99.39%**
2663. **`usr.bin/dtc/dtc.cc`** -> AI Confidence: **99.39%**
2664. **`usr.sbin/config/main.cc`** -> AI Confidence: **99.39%**
2665. **`usr.sbin/config/mkmakefile.cc`** -> AI Confidence: **99.39%**
2666. **`usr.sbin/pmc/cmd_pmc_filter.cc`** -> AI Confidence: **99.39%**
2667. **`cddl/contrib/opensolaris/cmd/plockstat/plockstat.c`** -> AI Confidence: **99.35%**
2668. **`contrib/bc/src/vm.c`** -> AI Confidence: **99.35%**
2669. **`contrib/bzip2/bzip2.c`** -> AI Confidence: **99.35%**
2670. **`contrib/elftoolchain/ar/write.c`** -> AI Confidence: **99.35%**
2671. **`contrib/ldns/host2str.c`** -> AI Confidence: **99.35%**
2672. **`contrib/libarchive/cpio/cpio.c`** -> AI Confidence: **99.35%**
2673. **`contrib/libarchive/libarchive/archive_write_set_format_zip.c`** -> AI Confidence: **99.35%**
2674. **`contrib/libpcap/fad-glifc.c`** -> AI Confidence: **99.35%**
2675. **`contrib/lua/src/ldo.c`** -> AI Confidence: **99.35%**
2676. **`contrib/mandoc/mdoc.c`** -> AI Confidence: **99.35%**
2677. **`contrib/netbsd-tests/fs/ptyfs/t_nullpts.c`** -> AI Confidence: **99.35%**
2678. **`contrib/netbsd-tests/kernel/arch/i386/t_ptrace_wait.c`** -> AI Confidence: **99.35%**
2679. **`contrib/ntp/libntp/iosignal.c`** -> AI Confidence: **99.35%**
2680. **`contrib/ntp/libparse/clk_meinberg.c`** -> AI Confidence: **99.35%**
2681. **`contrib/ntp/ntpd/ntp_scanner.c`** -> AI Confidence: **99.35%**
2682. **`contrib/ntp/ntpd/refclock_msfees.c`** -> AI Confidence: **99.35%**
2683. **`contrib/nvi/common/recover.c`** -> AI Confidence: **99.35%**
2684. **`contrib/nvi/ex/ex_at.c`** -> AI Confidence: **99.35%**
2685. **`contrib/nvi/vi/v_search.c`** -> AI Confidence: **99.35%**
2686. **`contrib/ofed/infiniband-diags/src/ibdiag_common.c`** -> AI Confidence: **99.35%**
2687. **`contrib/ofed/opensm/opensm/osm_mcast_fwd_rcv.c`** -> AI Confidence: **99.35%**
2688. **`contrib/sendmail/src/milter.c`** -> AI Confidence: **99.35%**
2689. **`contrib/tcp_wrappers/tcpdmatch.c`** -> AI Confidence: **99.35%**
2690. **`contrib/tcpdump/print-sunrpc.c`** -> AI Confidence: **99.35%**
2691. **`contrib/tcpdump/tcpdump.c`** -> AI Confidence: **99.35%**
2692. **`contrib/wpa/hs20/client/osu_client.c`** -> AI Confidence: **99.35%**
2693. **`contrib/wpa/src/rsn_supp/wpa_ft.c`** -> AI Confidence: **99.35%**
2694. **`contrib/wpa/wpa_supplicant/scan.c`** -> AI Confidence: **99.35%**
2695. **`crypto/heimdal/appl/telnet/libtelnet/rsaencpwd.c`** -> AI Confidence: **99.35%**
2696. **`crypto/krb5/src/lib/rpc/svc_auth_gssapi.c`** -> AI Confidence: **99.35%**
2697. **`crypto/krb5/src/plugins/kdb/db2/libdb2/hash/hash.c`** -> AI Confidence: **99.35%**
2698. **`crypto/openssh/auth.c`** -> AI Confidence: **99.35%**
2699. **`crypto/openssh/clientloop.c`** -> AI Confidence: **99.35%**
2700. **`crypto/openssh/dh.c`** -> AI Confidence: **99.35%**
2701. **`crypto/openssh/openbsd-compat/glob.c`** -> AI Confidence: **99.35%**
2702. **`crypto/openssh/sshpty.c`** -> AI Confidence: **99.35%**
2703. **`crypto/openssl/crypto/dsa/dsa_ameth.c`** -> AI Confidence: **99.35%**
2704. **`crypto/openssl/crypto/rsa/rsa_pk1.c`** -> AI Confidence: **99.35%**
2705. **`crypto/openssl/crypto/x509/v3_ac_tgt.c`** -> AI Confidence: **99.35%**
2706. **`crypto/openssl/engines/e_loader_attic.c`** -> AI Confidence: **99.35%**
2707. **`sbin/hastd/primary.c`** -> AI Confidence: **99.35%**
2708. **`sbin/ipfw/nat64lsn.c`** -> AI Confidence: **99.35%**
2709. **`sbin/pfctl/pfctl_parser.c`** -> AI Confidence: **99.35%**
2710. **`stand/efi/libefi/env.c`** -> AI Confidence: **99.35%**
2711. **`sys/amd64/vmm/intel/vmx_msr.c`** -> AI Confidence: **99.35%**
2712. **`sys/arm/allwinner/aw_rsb.c`** -> AI Confidence: **99.35%**
2713. **`sys/arm/arm/pmap-v6.c`** -> AI Confidence: **99.35%**
2714. **`sys/arm/freescale/imx/imx6_mp.c`** -> AI Confidence: **99.35%**
2715. **`sys/contrib/openzfs/cmd/zfs/zfs_main.c`** -> AI Confidence: **99.35%**
2716. **`sys/contrib/openzfs/cmd/zpool/zpool_main.c`** -> AI Confidence: **99.35%**
2717. **`sys/contrib/openzfs/module/os/freebsd/spl/spl_sysevent.c`** -> AI Confidence: **99.35%**
2718. **`sys/contrib/openzfs/module/os/freebsd/zfs/zfs_acl.c`** -> AI Confidence: **99.35%**
2719. **`sys/contrib/openzfs/module/os/linux/zfs/zfs_acl.c`** -> AI Confidence: **99.35%**
2720. **`sys/contrib/openzfs/module/os/linux/zfs/zfs_dir.c`** -> AI Confidence: **99.35%**
2721. **`sys/contrib/openzfs/module/zfs/arc.c`** -> AI Confidence: **99.35%**
2722. **`sys/contrib/openzfs/module/zfs/dmu_tx.c`** -> AI Confidence: **99.35%**
2723. **`sys/contrib/openzfs/module/zfs/dsl_bookmark.c`** -> AI Confidence: **99.35%**
2724. **`sys/contrib/openzfs/module/zfs/zfs_replay.c`** -> AI Confidence: **99.35%**
2725. **`sys/contrib/openzfs/tests/zfs-tests/cmd/manipulate_user_buffer.c`** -> AI Confidence: **99.35%**
2726. **`sys/contrib/openzfs/tests/zfs-tests/tests/functional/tmpfile/tmpfile_001_pos.c`** -> AI Confidence: **99.35%**
2727. **`sys/dev/aac/aac_pci.c`** -> AI Confidence: **99.35%**
2728. **`sys/dev/acpica/acpi_ec.c`** -> AI Confidence: **99.35%**
2729. **`sys/dev/ata/chipsets/ata-sis.c`** -> AI Confidence: **99.35%**
2730. **`sys/dev/ath/ath_hal/ar9002/ar9287_reset.c`** -> AI Confidence: **99.35%**
2731. **`sys/dev/bwn/if_bwn_phy_common.c`** -> AI Confidence: **99.35%**
2732. **`sys/dev/eqos/if_eqos_fdt.c`** -> AI Confidence: **99.35%**
2733. **`sys/dev/etherswitch/ar40xx/ar40xx_hw_mirror.c`** -> AI Confidence: **99.35%**
2734. **`sys/dev/mii/bmtphy.c`** -> AI Confidence: **99.35%**
2735. **`sys/dev/mii/ciphy.c`** -> AI Confidence: **99.35%**
2736. **`sys/dev/mii/mii_physubr.c`** -> AI Confidence: **99.35%**
2737. **`sys/dev/netmap/netmap_legacy.c`** -> AI Confidence: **99.35%**
2738. **`sys/dev/pms/RefTisa/tisa/sassata/sas/ini/itdio.c`** -> AI Confidence: **99.35%**
2739. **`sys/dev/qat/qat_api/common/crypto/sym/key/lac_sym_key.c`** -> AI Confidence: **99.35%**
2740. **`sys/dev/qat/qat_hw/qat_dh895xcc/adf_drv.c`** -> AI Confidence: **99.35%**
2741. **`sys/dev/qcom_tlmm/qcom_tlmm_pinmux.c`** -> AI Confidence: **99.35%**
2742. **`sys/dev/rtwn/usb/rtwn_usb_ep.c`** -> AI Confidence: **99.35%**
2743. **`sys/dev/syscons/scterm-teken.c`** -> AI Confidence: **99.35%**
2744. **`sys/dev/usb/controller/musb_otg.c`** -> AI Confidence: **99.35%**
2745. **`sys/dev/usb/controller/ohci.c`** -> AI Confidence: **99.35%**
2746. **`sys/dev/usb/usb_hub.c`** -> AI Confidence: **99.35%**
2747. **`sys/dev/veriexec/verified_exec.c`** -> AI Confidence: **99.35%**
2748. **`sys/fs/msdosfs/msdosfs_vnops.c`** -> AI Confidence: **99.35%**
2749. **`sys/kern/kern_sendfile.c`** -> AI Confidence: **99.35%**
2750. **`sys/netinet/sctp_cc_functions.c`** -> AI Confidence: **99.35%**
2751. **`sys/netinet/tcp_sack.c`** -> AI Confidence: **99.35%**
2752. **`sys/netinet/tcp_timewait.c`** -> AI Confidence: **99.35%**
2753. **`sys/netpfil/ipfilter/netinet/ip_log.c`** -> AI Confidence: **99.35%**
2754. **`sys/powerpc/aim/mmu_radix.c`** -> AI Confidence: **99.35%**
2755. **`sys/ufs/ufs/ufs_bmap.c`** -> AI Confidence: **99.35%**
2756. **`sys/x86/x86/mp_x86.c`** -> AI Confidence: **99.35%**
2757. **`tools/regression/netinet/ipbroadcast/ipbroadcast.c`** -> AI Confidence: **99.35%**
2758. **`tools/regression/security/cap_test/cap_test_pdkill.c`** -> AI Confidence: **99.35%**
2759. **`tools/tools/ath/athregs/dumpregs.c`** -> AI Confidence: **99.35%**
2760. **`tools/tools/net80211/wlantxtime/wlantxtime.c`** -> AI Confidence: **99.35%**
2761. **`tools/tools/netrate/http/http.c`** -> AI Confidence: **99.35%**
2762. **`usr.bin/cmp/cmp.c`** -> AI Confidence: **99.35%**
2763. **`usr.bin/factor/factor.c`** -> AI Confidence: **99.35%**
2764. **`usr.bin/m4/gnum4.c`** -> AI Confidence: **99.35%**
2765. **`usr.bin/ministat/ministat.c`** -> AI Confidence: **99.35%**
2766. **`usr.bin/netstat/if.c`** -> AI Confidence: **99.35%**
2767. **`usr.bin/rpcinfo/rpcinfo.c`** -> AI Confidence: **99.35%**
2768. **`usr.bin/sdiff/sdiff.c`** -> AI Confidence: **99.35%**
2769. **`usr.bin/tr/str.c`** -> AI Confidence: **99.35%**
2770. **`usr.bin/w/w.c`** -> AI Confidence: **99.35%**
2771. **`usr.sbin/autofs/popen.c`** -> AI Confidence: **99.35%**
2772. **`usr.sbin/bluetooth/bthidd/bthidd.c`** -> AI Confidence: **99.35%**
2773. **`usr.sbin/bluetooth/sdpd/main.c`** -> AI Confidence: **99.35%**
2774. **`usr.sbin/cdcontrol/cdcontrol.c`** -> AI Confidence: **99.35%**
2775. **`usr.sbin/lpr/common_source/matchjobs.c`** -> AI Confidence: **99.35%**
2776. **`usr.sbin/lpr/common_source/net.c`** -> AI Confidence: **99.35%**
2777. **`usr.sbin/moused/msconvd/msconvd.c`** -> AI Confidence: **99.35%**
2778. **`usr.sbin/ppp/command.c`** -> AI Confidence: **99.35%**
2779. **`usr.sbin/ppp/defs.c`** -> AI Confidence: **99.35%**
2780. **`usr.sbin/ppp/route.c`** -> AI Confidence: **99.35%**
2781. **`usr.sbin/ppp/slcompress.c`** -> AI Confidence: **99.35%**
2782. **`usr.sbin/spi/spi.c`** -> AI Confidence: **99.35%**
2783. **`usr.sbin/usbconfig/dump.c`** -> AI Confidence: **99.35%**
2784. **`usr.sbin/watch/watch.c`** -> AI Confidence: **99.35%**
2785. **`contrib/llvm-project/libcxx/include/__algorithm/ranges_merge.h`** -> AI Confidence: **99.35%**
2786. **`contrib/kyua/integration/helpers/race.cpp`** -> AI Confidence: **99.35%**
2787. **`contrib/kyua/utils/fs/operations.cpp`** -> AI Confidence: **99.35%**
2788. **`contrib/llvm-project/lld/ELF/Arch/RISCV.cpp`** -> AI Confidence: **99.35%**
2789. **`contrib/llvm-project/lldb/source/Core/Disassembler.cpp`** -> AI Confidence: **99.35%**
2790. **`contrib/llvm-project/lldb/source/Expression/IRInterpreter.cpp`** -> AI Confidence: **99.35%**
2791. **`contrib/llvm-project/lldb/source/Interpreter/CommandInterpreter.cpp`** -> AI Confidence: **99.35%**
2792. **`contrib/llvm-project/lldb/source/Plugins/ABI/Mips/ABISysV_mips.cpp`** -> AI Confidence: **99.35%**
2793. **`contrib/llvm-project/lldb/source/Plugins/ABI/PowerPC/ABISysV_ppc.cpp`** -> AI Confidence: **99.35%**
2794. **`contrib/llvm-project/lldb/source/Plugins/Process/Utility/RegisterContextDarwin_i386.cpp`** -> AI Confidence: **99.35%**
2795. **`contrib/llvm-project/lldb/source/Plugins/SymbolFile/DWARF/ManualDWARFIndex.cpp`** -> AI Confidence: **99.35%**
2796. **`contrib/llvm-project/llvm/lib/Transforms/Utils/CodeExtractor.cpp`** -> AI Confidence: **99.35%**
2797. **`contrib/llvm-project/llvm/lib/Transforms/Utils/ModuleUtils.cpp`** -> AI Confidence: **99.35%**
2798. **`contrib/llvm-project/llvm/lib/Transforms/Utils/PromoteMemoryToRegister.cpp`** -> AI Confidence: **99.35%**
2799. **`contrib/llvm-project/llvm/tools/bugpoint/ExtractFunction.cpp`** -> AI Confidence: **99.35%**
2800. **`contrib/llvm-project/llvm/tools/llvm-dis/llvm-dis.cpp`** -> AI Confidence: **99.35%**
2801. **`contrib/llvm-project/llvm/tools/llvm-mca/llvm-mca.cpp`** -> AI Confidence: **99.35%**
2802. **`bin/hostname/hostname.c`** -> AI Confidence: **99.34%**
2803. **`bin/setfacl/file.c`** -> AI Confidence: **99.34%**
2804. **`bin/stty/gfmt.c`** -> AI Confidence: **99.34%**
2805. **`contrib/arm-optimized-routines/math/sincosf.c`** -> AI Confidence: **99.34%**
2806. **`contrib/bc/src/bc_lex.c`** -> AI Confidence: **99.34%**
2807. **`contrib/bc/src/lang.c`** -> AI Confidence: **99.34%**
2808. **`contrib/bmake/getopt.c`** -> AI Confidence: **99.34%**
2809. **`contrib/elftoolchain/libelf/elf_end.c`** -> AI Confidence: **99.34%**
2810. **`contrib/elftoolchain/libelf/libelf_memory.c`** -> AI Confidence: **99.34%**
2811. **`contrib/elftoolchain/libelftc/elftc_copyfile.c`** -> AI Confidence: **99.34%**
2812. **`contrib/expat/tests/benchmark/benchmark.c`** -> AI Confidence: **99.34%**
2813. **`contrib/expat/tests/handlers.c`** -> AI Confidence: **99.34%**
2814. **`contrib/file/src/ascmagic.c`** -> AI Confidence: **99.34%**
2815. **`contrib/file/src/readelf.c`** -> AI Confidence: **99.34%**
2816. **`contrib/ldns/compat/inet_aton.c`** -> AI Confidence: **99.34%**
2817. **`contrib/ldns/str2host.c`** -> AI Confidence: **99.34%**
2818. **`contrib/less/lsystem.c`** -> AI Confidence: **99.34%**
2819. **`contrib/less/main.c`** -> AI Confidence: **99.34%**
2820. **`contrib/less/regexp.c`** -> AI Confidence: **99.34%**
2821. **`contrib/libarchive/cpio/cmdline.c`** -> AI Confidence: **99.34%**
2822. **`contrib/libarchive/libarchive/archive_entry_strmode.c`** -> AI Confidence: **99.34%**
2823. **`contrib/libarchive/libarchive/archive_read_set_format.c`** -> AI Confidence: **99.34%**
2824. **`contrib/libarchive/libarchive/archive_read_support_filter_uu.c`** -> AI Confidence: **99.34%**
2825. **`contrib/libedit/parse.c`** -> AI Confidence: **99.34%**
2826. **`contrib/libedit/refresh.c`** -> AI Confidence: **99.34%**
2827. **`contrib/libevent/sample/openssl_hostname_validation.c`** -> AI Confidence: **99.34%**
2828. **`contrib/libfido2/examples/reset.c`** -> AI Confidence: **99.34%**
2829. **`contrib/libfido2/openbsd-compat/bsd-asprintf.c`** -> AI Confidence: **99.34%**
2830. **`contrib/libfido2/src/ecdh.c`** -> AI Confidence: **99.34%**
2831. **`contrib/libfido2/src/es256.c`** -> AI Confidence: **99.34%**
2832. **`contrib/libfido2/src/fido/config.h`** -> AI Confidence: **99.34%**
2833. **`contrib/libucl/tests/test_basic.c`** -> AI Confidence: **99.34%**
2834. **`contrib/libxo/tests/core/test_01.c`** -> AI Confidence: **99.34%**
2835. **`contrib/libxo/tests/core/test_03.c`** -> AI Confidence: **99.34%**
2836. **`contrib/libyaml/tests/run-dumper.c`** -> AI Confidence: **99.34%**
2837. **`contrib/llvm-project/libcxx/include/__algorithm/remove.h`** -> AI Confidence: **99.34%**
2838. **`contrib/llvm-project/libcxx/include/__utility/exchange.h`** -> AI Confidence: **99.34%**
2839. **`contrib/llvm-project/libunwind/src/config.h`** -> AI Confidence: **99.34%**
2840. **`contrib/ncurses/ncurses/report_ctype.c`** -> AI Confidence: **99.34%**
2841. **`contrib/ncurses/ncurses/tinfo/lib_termcap.c`** -> AI Confidence: **99.34%**
2842. **`contrib/ncurses/ncurses/tinfo/tinfo_driver.c`** -> AI Confidence: **99.34%**
2843. **`contrib/ncurses/ncurses/tty/lib_twait.c`** -> AI Confidence: **99.34%**
2844. **`contrib/ncurses/progs/dump_entry.c`** -> AI Confidence: **99.34%**
2845. **`contrib/ncurses/progs/tset.c`** -> AI Confidence: **99.34%**
2846. **`contrib/netbsd-tests/fs/ffs/t_quota2_1.c`** -> AI Confidence: **99.34%**
2847. **`contrib/netbsd-tests/kernel/t_ptrace_wait.c`** -> AI Confidence: **99.34%**
2848. **`contrib/netbsd-tests/modules/k_helper/k_helper.c`** -> AI Confidence: **99.34%**
2849. **`contrib/netbsd-tests/rump/kernspace/lockme.c`** -> AI Confidence: **99.34%**
2850. **`contrib/ntp/libntp/atolfp.c`** -> AI Confidence: **99.34%**
2851. **`contrib/ntp/libntp/hextolfp.c`** -> AI Confidence: **99.34%**
2852. **`contrib/ntp/libntp/mstolfp.c`** -> AI Confidence: **99.34%**
2853. **`contrib/ntp/libntp/numtoa.c`** -> AI Confidence: **99.34%**
2854. **`contrib/ntp/libparse/ieee754io.c`** -> AI Confidence: **99.34%**
2855. **`contrib/ntp/libparse/mfp_mul.c`** -> AI Confidence: **99.34%**
2856. **`contrib/ntp/libparse/parse_conf.c`** -> AI Confidence: **99.34%**
2857. **`contrib/ntp/ntpd/cmd_args.c`** -> AI Confidence: **99.34%**
2858. **`contrib/ntp/ntpsnmpd/ntpsnmpd.c`** -> AI Confidence: **99.34%**
2859. **`contrib/ntp/sntp/libevent/sample/openssl_hostname_validation.c`** -> AI Confidence: **99.34%**
2860. **`contrib/ntp/util/jitter.c`** -> AI Confidence: **99.34%**
2861. **`contrib/ntp/util/timetrim.c`** -> AI Confidence: **99.34%**
2862. **`contrib/nvi/vi/v_right.c`** -> AI Confidence: **99.34%**
2863. **`contrib/nvi/vi/v_xchar.c`** -> AI Confidence: **99.34%**
2864. **`contrib/one-true-awk/lex.c`** -> AI Confidence: **99.34%**
2865. **`contrib/one-true-awk/maketab.c`** -> AI Confidence: **99.34%**
2866. **`contrib/openbsm/libbsm/bsm_domain.c`** -> AI Confidence: **99.34%**
2867. **`contrib/openbsm/libbsm/bsm_errno.c`** -> AI Confidence: **99.34%**
2868. **`contrib/openbsm/libbsm/bsm_flags.c`** -> AI Confidence: **99.34%**
2869. **`contrib/pam_modules/pam_passwdqc/passwdqc_check.c`** -> AI Confidence: **99.34%**
2870. **`contrib/sendmail/libsm/config.c`** -> AI Confidence: **99.34%**
2871. **`contrib/sendmail/libsm/flags.c`** -> AI Confidence: **99.34%**
2872. **`contrib/sendmail/libsm/snprintf.c`** -> AI Confidence: **99.34%**
2873. **`contrib/sendmail/libsm/t-cf.c`** -> AI Confidence: **99.34%**
2874. **`contrib/sendmail/libsm/uxtext_unquote.c`** -> AI Confidence: **99.34%**
2875. **`contrib/sendmail/libsm/wsetup.c`** -> AI Confidence: **99.34%**
2876. **`contrib/sendmail/src/readcf.c`** -> AI Confidence: **99.34%**
2877. **`contrib/tcp_wrappers/percent_x.c`** -> AI Confidence: **99.34%**
2878. **`contrib/tcpdump/addrtostr.c`** -> AI Confidence: **99.34%**
2879. **`contrib/tcpdump/checksum.c`** -> AI Confidence: **99.34%**
2880. **`contrib/tcpdump/print-802_15_4.c`** -> AI Confidence: **99.34%**
2881. **`contrib/tcpdump/print-bootp.c`** -> AI Confidence: **99.34%**
2882. **`contrib/tcpdump/print-cfm.c`** -> AI Confidence: **99.34%**
2883. **`contrib/tcpdump/print-dhcp6.c`** -> AI Confidence: **99.34%**
2884. **`contrib/tcpdump/print-dsa.c`** -> AI Confidence: **99.34%**
2885. **`contrib/tcpdump/print-dtp.c`** -> AI Confidence: **99.34%**
2886. **`contrib/tcpdump/print-dvmrp.c`** -> AI Confidence: **99.34%**
2887. **`contrib/tcpdump/print-egp.c`** -> AI Confidence: **99.34%**
2888. **`contrib/tcpdump/print-enc.c`** -> AI Confidence: **99.34%**
2889. **`contrib/tcpdump/print-geonet.c`** -> AI Confidence: **99.34%**
2890. **`contrib/tcpdump/print-gre.c`** -> AI Confidence: **99.34%**
2891. **`contrib/tcpdump/print-hncp.c`** -> AI Confidence: **99.34%**
2892. **`contrib/tcpdump/print-ip6.c`** -> AI Confidence: **99.34%**
2893. **`contrib/tcpdump/print-ip6opts.c`** -> AI Confidence: **99.34%**
2894. **`contrib/tcpdump/print-ipx.c`** -> AI Confidence: **99.34%**
2895. **`contrib/tcpdump/print-lmp.c`** -> AI Confidence: **99.34%**
2896. **`contrib/tcpdump/print-loopback.c`** -> AI Confidence: **99.34%**
2897. **`contrib/tcpdump/print-mobility.c`** -> AI Confidence: **99.34%**
2898. **`contrib/tcpdump/print-mpls.c`** -> AI Confidence: **99.34%**
2899. **`contrib/tcpdump/print-msdp.c`** -> AI Confidence: **99.34%**
2900. **`contrib/tcpdump/print-null.c`** -> AI Confidence: **99.34%**
2901. **`contrib/tcpdump/print-realtek.c`** -> AI Confidence: **99.34%**
2902. **`contrib/tcpdump/print-rpki-rtr.c`** -> AI Confidence: **99.34%**
2903. **`contrib/tcpdump/print-rx.c`** -> AI Confidence: **99.34%**
2904. **`contrib/tcpdump/print-smb.c`** -> AI Confidence: **99.34%**
2905. **`contrib/tcpdump/print-sunatm.c`** -> AI Confidence: **99.34%**
2906. **`contrib/tcpdump/print-telnet.c`** -> AI Confidence: **99.34%**
2907. **`contrib/tcpdump/print-vtp.c`** -> AI Confidence: **99.34%**
2908. **`contrib/tcsh/sh.sem.c`** -> AI Confidence: **99.34%**
2909. **`contrib/tcsh/tw.parse.c`** -> AI Confidence: **99.34%**
2910. **`contrib/tnftp/src/domacro.c`** -> AI Confidence: **99.34%**
2911. **`contrib/tzcode/strftime.c`** -> AI Confidence: **99.34%**
2912. **`contrib/unbound/compat/inet_aton.c`** -> AI Confidence: **99.34%**
2913. **`contrib/unbound/sldns/parse.c`** -> AI Confidence: **99.34%**
2914. **`contrib/unifdef/tests/NetBSD-42628.c`** -> AI Confidence: **99.34%**
2915. **`contrib/unvis/unvis.c`** -> AI Confidence: **99.34%**
2916. **`contrib/wpa/wpa_supplicant/eap_register.c`** -> AI Confidence: **99.34%**
2917. **`contrib/wpa/wpa_supplicant/wpas_module_tests.c`** -> AI Confidence: **99.34%**
2918. **`crypto/krb5/src/ccapi/common/win/OldCC/ccutils.c`** -> AI Confidence: **99.34%**
2919. **`crypto/krb5/src/ccapi/lib/ccapi_ccache.c`** -> AI Confidence: **99.34%**
2920. **`crypto/krb5/src/ccapi/server/win/ccs_request_proc.c`** -> AI Confidence: **99.34%**
2921. **`crypto/krb5/src/ccapi/test/test_ccapi_context.c`** -> AI Confidence: **99.34%**
2922. **`crypto/krb5/src/clients/kcpytkt/kcpytkt.c`** -> AI Confidence: **99.34%**
2923. **`crypto/krb5/src/clients/kdeltkt/kdeltkt.c`** -> AI Confidence: **99.34%**
2924. **`crypto/krb5/src/clients/kdestroy/kdestroy.c`** -> AI Confidence: **99.34%**
2925. **`crypto/krb5/src/clients/kpasswd/kpasswd.c`** -> AI Confidence: **99.34%**
2926. **`crypto/krb5/src/clients/ksu/main.c`** -> AI Confidence: **99.34%**
2927. **`crypto/krb5/src/kadmin/cli/ss_wrapper.c`** -> AI Confidence: **99.34%**
2928. **`crypto/krb5/src/kadmin/ktutil/ktutil_funcs.c`** -> AI Confidence: **99.34%**
2929. **`crypto/krb5/src/kdc/kdc_util.c`** -> AI Confidence: **99.34%**
2930. **`crypto/krb5/src/lib/crypto/builtin/aes/aeskey.c`** -> AI Confidence: **99.34%**
2931. **`crypto/krb5/src/lib/gssapi/krb5/accept_sec_context.c`** -> AI Confidence: **99.34%**
2932. **`crypto/krb5/src/lib/gssapi/krb5/import_name.c`** -> AI Confidence: **99.34%**
2933. **`crypto/krb5/src/lib/gssapi/mechglue/g_acquire_cred.c`** -> AI Confidence: **99.34%**
2934. **`crypto/krb5/src/lib/kdb/kdb_default.c`** -> AI Confidence: **99.34%**
2935. **`crypto/krb5/src/lib/krb5/ccache/t_marshal.c`** -> AI Confidence: **99.34%**
2936. **`crypto/krb5/src/lib/krb5/keytab/t_keytab.c`** -> AI Confidence: **99.34%**
2937. **`crypto/krb5/src/lib/krb5/krb/get_in_tkt.c`** -> AI Confidence: **99.34%**
2938. **`crypto/krb5/src/lib/krb5/krb/rd_req_dec.c`** -> AI Confidence: **99.34%**
2939. **`crypto/krb5/src/lib/krb5/krb/recvauth.c`** -> AI Confidence: **99.34%**
2940. **`crypto/krb5/src/lib/krb5/os/localauth_k5login.c`** -> AI Confidence: **99.34%**
2941. **`crypto/krb5/src/lib/rpc/dyntest.c`** -> AI Confidence: **99.34%**
2942. **`crypto/krb5/src/plugins/audit/kdc_j_encode.c`** -> AI Confidence: **99.34%**
2943. **`crypto/krb5/src/plugins/kdb/db2/kdb_xdr.c`** -> AI Confidence: **99.34%**
2944. **`crypto/krb5/src/plugins/kdb/db2/libdb2/recno/rec_search.c`** -> AI Confidence: **99.34%**
2945. **`crypto/krb5/src/plugins/kdb/db2/libdb2/test/hash1.tests/thash4.c`** -> AI Confidence: **99.34%**
2946. **`crypto/krb5/src/plugins/kdb/db2/libdb2/test/hash2.tests/bigtest.c`** -> AI Confidence: **99.34%**
2947. **`crypto/krb5/src/plugins/kdb/ldap/ldap_util/kdb5_ldap_policy.c`** -> AI Confidence: **99.34%**
2948. **`crypto/krb5/src/plugins/kdb/ldap/ldap_util/kdb5_ldap_util.c`** -> AI Confidence: **99.34%**
2949. **`crypto/krb5/src/plugins/kdb/ldap/libkdb_ldap/ldap_create.c`** -> AI Confidence: **99.34%**
2950. **`crypto/krb5/src/plugins/kdb/ldap/libkdb_ldap/ldap_principal.c`** -> AI Confidence: **99.34%**
2951. **`crypto/krb5/src/plugins/kdb/ldap/libkdb_ldap/ldap_realm.c`** -> AI Confidence: **99.34%**
2952. **`crypto/krb5/src/plugins/kdb/lmdb/lockout.c`** -> AI Confidence: **99.34%**
2953. **`crypto/krb5/src/plugins/preauth/pkinit/pkinit_matching.c`** -> AI Confidence: **99.34%**
2954. **`crypto/krb5/src/plugins/preauth/securid_sam2/grail.c`** -> AI Confidence: **99.34%**
2955. **`crypto/krb5/src/util/profile/argv_parse.c`** -> AI Confidence: **99.34%**
2956. **`crypto/krb5/src/util/profile/test_profile.c`** -> AI Confidence: **99.34%**
2957. **`crypto/krb5/src/windows/ms2mit/ms2mit.c`** -> AI Confidence: **99.34%**
2958. **`crypto/libecc/include/libecc/ecdh/ecccdh.h`** -> AI Confidence: **99.34%**
2959. **`crypto/libecc/src/examples/sig/rsa/rsa.c`** -> AI Confidence: **99.34%**
2960. **`crypto/libecc/src/nn/nn_mod_pow.c`** -> AI Confidence: **99.34%**
2961. **`crypto/libecc/src/sig/ecdsa_common.c`** -> AI Confidence: **99.34%**
2962. **`crypto/libecc/src/tests/ec_utils.c`** -> AI Confidence: **99.34%**
2963. **`crypto/openssh/audit-linux.c`** -> AI Confidence: **99.34%**
2964. **`crypto/openssh/openbsd-compat/bcrypt_pbkdf.c`** -> AI Confidence: **99.34%**
2965. **`crypto/openssh/openbsd-compat/bsd-setres_id.c`** -> AI Confidence: **99.34%**
2966. **`crypto/openssh/openbsd-compat/fnmatch.c`** -> AI Confidence: **99.34%**
2967. **`crypto/openssh/openbsd-compat/getgrouplist.c`** -> AI Confidence: **99.34%**
2968. **`crypto/openssh/openbsd-compat/inet_aton.c`** -> AI Confidence: **99.34%**
2969. **`crypto/openssl/apps/nseq.c`** -> AI Confidence: **99.34%**
2970. **`crypto/openssl/crypto/asn1/a_bitstr.c`** -> AI Confidence: **99.34%**
2971. **`crypto/openssl/crypto/asn1/a_time.c`** -> AI Confidence: **99.34%**
2972. **`crypto/openssl/crypto/asn1/asn1_parse.c`** -> AI Confidence: **99.34%**
2973. **`crypto/openssl/crypto/asn1/asn_mstbl.c`** -> AI Confidence: **99.34%**
2974. **`crypto/openssl/crypto/asn1/f_int.c`** -> AI Confidence: **99.34%**
2975. **`crypto/openssl/crypto/asn1/f_string.c`** -> AI Confidence: **99.34%**
2976. **`crypto/openssl/crypto/asn1/tasn_fre.c`** -> AI Confidence: **99.34%**
2977. **`crypto/openssl/crypto/bf/bf_skey.c`** -> AI Confidence: **99.34%**
2978. **`crypto/openssl/crypto/bio/bio_cb.c`** -> AI Confidence: **99.34%**
2979. **`crypto/openssl/crypto/bio/bss_conn.c`** -> AI Confidence: **99.34%**
2980. **`crypto/openssl/crypto/bn/bn_gf2m.c`** -> AI Confidence: **99.34%**
2981. **`crypto/openssl/crypto/bn/bn_prime.c`** -> AI Confidence: **99.34%**
2982. **`crypto/openssl/crypto/bn/bn_rsa_fips186_4.c`** -> AI Confidence: **99.34%**
2983. **`crypto/openssl/crypto/cms/cms_kari.c`** -> AI Confidence: **99.34%**
2984. **`crypto/openssl/crypto/ec/eck_prn.c`** -> AI Confidence: **99.34%**
2985. **`crypto/openssl/crypto/ec/ecp_nist.c`** -> AI Confidence: **99.34%**
2986. **`crypto/openssl/crypto/evp/evp_key.c`** -> AI Confidence: **99.34%**
2987. **`crypto/openssl/crypto/evp/p_open.c`** -> AI Confidence: **99.34%**
2988. **`crypto/openssl/crypto/evp/p_sign.c`** -> AI Confidence: **99.34%**
2989. **`crypto/openssl/crypto/ocsp/ocsp_prn.c`** -> AI Confidence: **99.34%**
2990. **`crypto/openssl/crypto/params_from_text.c`** -> AI Confidence: **99.34%**
2991. **`crypto/openssl/crypto/rsa/rsa_chk.c`** -> AI Confidence: **99.34%**
2992. **`crypto/openssl/crypto/rsa/rsa_crpt.c`** -> AI Confidence: **99.34%**
2993. **`crypto/openssl/crypto/rsa/rsa_x931g.c`** -> AI Confidence: **99.34%**
2994. **`crypto/openssl/crypto/sha/keccak1600.c`** -> AI Confidence: **99.34%**
2995. **`crypto/openssl/crypto/slh_dsa/slh_dsa_hash_ctx.c`** -> AI Confidence: **99.34%**
2996. **`crypto/openssl/crypto/sm2/sm2_key.c`** -> AI Confidence: **99.34%**
2997. **`crypto/openssl/crypto/txt_db/txt_db.c`** -> AI Confidence: **99.34%**
2998. **`crypto/openssl/crypto/x509/pcy_map.c`** -> AI Confidence: **99.34%**
2999. **`crypto/openssl/crypto/x509/t_acert.c`** -> AI Confidence: **99.34%**
3000. **`crypto/openssl/crypto/x509/t_crl.c`** -> AI Confidence: **99.34%**
3001. **`crypto/openssl/crypto/x509/v3_pci.c`** -> AI Confidence: **99.34%**
3002. **`crypto/openssl/crypto/x509/v3_purp.c`** -> AI Confidence: **99.34%**
3003. **`crypto/openssl/crypto/x509/x509type.c`** -> AI Confidence: **99.34%**
3004. **`crypto/openssl/demos/bio/server-arg.c`** -> AI Confidence: **99.34%**
3005. **`crypto/openssl/demos/bio/server-cmod.c`** -> AI Confidence: **99.34%**
3006. **`crypto/openssl/demos/cipher/aesccm.c`** -> AI Confidence: **99.34%**
3007. **`crypto/openssl/demos/cipher/aesgcm.c`** -> AI Confidence: **99.34%**
3008. **`crypto/openssl/demos/cipher/aeskeywrap.c`** -> AI Confidence: **99.34%**
3009. **`crypto/openssl/demos/cipher/ariacbc.c`** -> AI Confidence: **99.34%**
3010. **`crypto/openssl/demos/digest/BIO_f_md.c`** -> AI Confidence: **99.34%**
3011. **`crypto/openssl/demos/digest/EVP_MD_xof.c`** -> AI Confidence: **99.34%**
3012. **`crypto/openssl/demos/guide/quic-client-block.c`** -> AI Confidence: **99.34%**
3013. **`crypto/openssl/demos/guide/quic-multi-stream.c`** -> AI Confidence: **99.34%**
3014. **`crypto/openssl/demos/kdf/argon2.c`** -> AI Confidence: **99.34%**
3015. **`crypto/openssl/demos/kdf/hkdf.c`** -> AI Confidence: **99.34%**
3016. **`crypto/openssl/demos/kdf/pbkdf2.c`** -> AI Confidence: **99.34%**
3017. **`crypto/openssl/demos/kdf/scrypt.c`** -> AI Confidence: **99.34%**
3018. **`crypto/openssl/demos/mac/gmac.c`** -> AI Confidence: **99.34%**
3019. **`crypto/openssl/demos/mac/siphash.c`** -> AI Confidence: **99.34%**
3020. **`crypto/openssl/demos/pkcs12/pkread.c`** -> AI Confidence: **99.34%**
3021. **`crypto/openssl/demos/pkcs12/pkwrite.c`** -> AI Confidence: **99.34%**
3022. **`crypto/openssl/demos/signature/EVP_DSA_Signature_demo.c`** -> AI Confidence: **99.34%**
3023. **`crypto/openssl/demos/signature/EVP_EC_Signature_demo.c`** -> AI Confidence: **99.34%**
3024. **`crypto/openssl/demos/signature/EVP_ED_Signature_demo.c`** -> AI Confidence: **99.34%**
3025. **`crypto/openssl/fuzz/quic-rcidm.c`** -> AI Confidence: **99.34%**
3026. **`crypto/openssl/fuzz/quic-srtm.c`** -> AI Confidence: **99.34%**
3027. **`crypto/openssl/fuzz/x509.c`** -> AI Confidence: **99.34%**
3028. **`crypto/openssl/providers/implementations/ciphers/cipher_aes_gcm_siv_polyval.c`** -> AI Confidence: **99.34%**
3029. **`crypto/openssl/ssl/quic/qlog_event_helpers.c`** -> AI Confidence: **99.34%**
3030. **`crypto/openssl/ssl/ssl_asn1.c`** -> AI Confidence: **99.34%**
3031. **`crypto/openssl/ssl/statem/statem.c`** -> AI Confidence: **99.34%**
3032. **`lib/msun/src/e_acoshl.c`** -> AI Confidence: **99.34%**
3033. **`lib/msun/src/e_atanhl.c`** -> AI Confidence: **99.34%**
3034. **`lib/msun/src/e_coshl.c`** -> AI Confidence: **99.34%**
3035. **`lib/msun/src/e_sinhl.c`** -> AI Confidence: **99.34%**
3036. **`lib/msun/src/s_asinhl.c`** -> AI Confidence: **99.34%**
3037. **`lib/msun/src/s_cbrtl.c`** -> AI Confidence: **99.34%**
3038. **`lib/msun/src/s_clogl.c`** -> AI Confidence: **99.34%**
3039. **`lib/msun/src/s_remquol.c`** -> AI Confidence: **99.34%**
3040. **`lib/msun/src/s_roundl.c`** -> AI Confidence: **99.34%**
3041. **`lib/msun/src/s_sincosf.c`** -> AI Confidence: **99.34%**
3042. **`lib/msun/src/s_sinl.c`** -> AI Confidence: **99.34%**
3043. **`lib/msun/src/s_tanhl.c`** -> AI Confidence: **99.34%**
3044. **`lib/msun/src/s_tanl.c`** -> AI Confidence: **99.34%**
3045. **`libexec/bootpd/trylook.c`** -> AI Confidence: **99.34%**
3046. **`libexec/revnetgroup/revnetgroup.c`** -> AI Confidence: **99.34%**
3047. **`sbin/dhclient/packet.c`** -> AI Confidence: **99.34%**
3048. **`sbin/fsck_ffs/pass3.c`** -> AI Confidence: **99.34%**
3049. **`sbin/ipf/libipf/load_hash.c`** -> AI Confidence: **99.34%**
3050. **`share/doc/psd/20.ipctut/strchkread.c`** -> AI Confidence: **99.34%**
3051. **`share/doc/psd/20.ipctut/streamread.c`** -> AI Confidence: **99.34%**
3052. **`share/examples/hwpmc/overhead.c`** -> AI Confidence: **99.34%**
3053. **`share/examples/libusb20/util.c`** -> AI Confidence: **99.34%**
3054. **`share/examples/libvgl/demo.c`** -> AI Confidence: **99.34%**
3055. **`share/examples/sound/midi.c`** -> AI Confidence: **99.34%**
3056. **`stand/common/ls.c`** -> AI Confidence: **99.34%**
3057. **`stand/efi/loader/efi_main.c`** -> AI Confidence: **99.34%**
3058. **`stand/i386/libi386/biosmemdisk.c`** -> AI Confidence: **99.34%**
3059. **`sys/amd64/amd64/bios.c`** -> AI Confidence: **99.34%**
3060. **`sys/amd64/amd64/db_disasm.c`** -> AI Confidence: **99.34%**
3061. **`sys/arm/broadcom/bcm2835/bcm2835_vcio.c`** -> AI Confidence: **99.34%**
3062. **`sys/arm64/arm64/disassem.c`** -> AI Confidence: **99.34%**
3063. **`sys/cddl/dev/fbt/x86/fbt_isa.c`** -> AI Confidence: **99.34%**
3064. **`sys/contrib/dev/acpica/common/acfileio.c`** -> AI Confidence: **99.34%**
3065. **`sys/contrib/dev/acpica/common/dmtable.c`** -> AI Confidence: **99.34%**
3066. **`sys/contrib/dev/acpica/common/dmtbdump2.c`** -> AI Confidence: **99.34%**
3067. **`sys/contrib/dev/acpica/compiler/aslcompile.c`** -> AI Confidence: **99.34%**
3068. **`sys/contrib/dev/acpica/compiler/asllisting.c`** -> AI Confidence: **99.34%**
3069. **`sys/contrib/dev/acpica/compiler/aslload.c`** -> AI Confidence: **99.34%**
3070. **`sys/contrib/dev/acpica/compiler/aslmethod.c`** -> AI Confidence: **99.34%**
3071. **`sys/contrib/dev/acpica/compiler/aslopt.c`** -> AI Confidence: **99.34%**
3072. **`sys/contrib/dev/acpica/compiler/aslxref.c`** -> AI Confidence: **99.34%**
3073. **`sys/contrib/dev/acpica/compiler/cvcompiler.c`** -> AI Confidence: **99.34%**
3074. **`sys/contrib/dev/acpica/components/debugger/dbxface.c`** -> AI Confidence: **99.34%**
3075. **`sys/contrib/dev/acpica/components/disassembler/dmcstyle.c`** -> AI Confidence: **99.34%**
3076. **`sys/contrib/dev/acpica/components/disassembler/dmdeferred.c`** -> AI Confidence: **99.34%**
3077. **`sys/contrib/dev/acpica/components/disassembler/dmnames.c`** -> AI Confidence: **99.34%**
3078. **`sys/contrib/dev/acpica/components/disassembler/dmutils.c`** -> AI Confidence: **99.34%**
3079. **`sys/contrib/dev/acpica/components/disassembler/dmwalk.c`** -> AI Confidence: **99.34%**
3080. **`sys/contrib/dev/acpica/components/dispatcher/dsargs.c`** -> AI Confidence: **99.34%**
3081. **`sys/contrib/dev/acpica/components/dispatcher/dscontrol.c`** -> AI Confidence: **99.34%**
3082. **`sys/contrib/dev/acpica/components/dispatcher/dsinit.c`** -> AI Confidence: **99.34%**
3083. **`sys/contrib/dev/acpica/components/dispatcher/dsmthdat.c`** -> AI Confidence: **99.34%**
3084. **`sys/contrib/dev/acpica/components/events/evregion.c`** -> AI Confidence: **99.34%**
3085. **`sys/contrib/dev/acpica/components/events/evxface.c`** -> AI Confidence: **99.34%**
3086. **`sys/contrib/dev/acpica/components/executer/excreate.c`** -> AI Confidence: **99.34%**
3087. **`sys/contrib/dev/acpica/components/executer/exdump.c`** -> AI Confidence: **99.34%**
3088. **`sys/contrib/dev/acpica/components/executer/exfield.c`** -> AI Confidence: **99.34%**
3089. **`sys/contrib/dev/acpica/components/executer/exfldio.c`** -> AI Confidence: **99.34%**
3090. **`sys/contrib/dev/acpica/components/executer/exoparg2.c`** -> AI Confidence: **99.34%**
3091. **`sys/contrib/dev/acpica/components/executer/exoparg3.c`** -> AI Confidence: **99.34%**
3092. **`sys/contrib/dev/acpica/components/executer/exoparg6.c`** -> AI Confidence: **99.34%**
3093. **`sys/contrib/dev/acpica/components/executer/exprep.c`** -> AI Confidence: **99.34%**
3094. **`sys/contrib/dev/acpica/components/executer/exresnte.c`** -> AI Confidence: **99.34%**
3095. **`sys/contrib/dev/acpica/components/executer/exresolv.c`** -> AI Confidence: **99.34%**
3096. **`sys/contrib/dev/acpica/components/executer/exresop.c`** -> AI Confidence: **99.34%**
3097. **`sys/contrib/dev/acpica/components/executer/exserial.c`** -> AI Confidence: **99.34%**
3098. **`sys/contrib/dev/acpica/components/executer/exstore.c`** -> AI Confidence: **99.34%**
3099. **`sys/contrib/dev/acpica/components/namespace/nsaccess.c`** -> AI Confidence: **99.34%**
3100. **`sys/contrib/dev/acpica/components/namespace/nseval.c`** -> AI Confidence: **99.34%**
3101. **`sys/contrib/dev/acpica/components/namespace/nsload.c`** -> AI Confidence: **99.34%**
3102. **`sys/contrib/dev/acpica/components/parser/psobject.c`** -> AI Confidence: **99.34%**
3103. **`sys/contrib/dev/acpica/components/parser/psopinfo.c`** -> AI Confidence: **99.34%**
3104. **`sys/contrib/dev/acpica/components/parser/pstree.c`** -> AI Confidence: **99.34%**
3105. **`sys/contrib/dev/acpica/components/utilities/utdelete.c`** -> AI Confidence: **99.34%**
3106. **`sys/contrib/dev/acpica/components/utilities/utxfinit.c`** -> AI Confidence: **99.34%**
3107. **`sys/contrib/dev/ath/ath_hal/ar9300/ar9300_interrupts.c`** -> AI Confidence: **99.34%**
3108. **`sys/contrib/dev/ath/ath_hal/ar9300/ar9300_paprd.c`** -> AI Confidence: **99.34%**
3109. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-chuwi-v7-cw0825.dts`** -> AI Confidence: **99.34%**
3110. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-gemei-g9.dts`** -> AI Confidence: **99.34%**
3111. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-inet97fv2.dts`** -> AI Confidence: **99.34%**
3112. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-inet9f-rev03.dts`** -> AI Confidence: **99.34%**
3113. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-pcduino.dts`** -> AI Confidence: **99.34%**
3114. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-a10s-olinuxino-micro.dts`** -> AI Confidence: **99.34%**
3115. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-a10s-wobo-i5.dts`** -> AI Confidence: **99.34%**
3116. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-a13-hsg-h702.dts`** -> AI Confidence: **99.34%**
3117. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-a13-licheepi-one.dts`** -> AI Confidence: **99.34%**
3118. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-gr8-chip-pro.dts`** -> AI Confidence: **99.34%**
3119. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-gr8-evb.dts`** -> AI Confidence: **99.34%**
3120. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-r8-chip.dts`** -> AI Confidence: **99.34%**
3121. **`sys/contrib/device-tree/src/arm/allwinner/sun6i-a31s-primo81.dts`** -> AI Confidence: **99.34%**
3122. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-bananapi-m1-plus.dts`** -> AI Confidence: **99.34%**
3123. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-bananapi.dts`** -> AI Confidence: **99.34%**
3124. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-cubieboard2.dts`** -> AI Confidence: **99.34%**
3125. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-cubietruck.dts`** -> AI Confidence: **99.34%**
3126. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-haoyu-marsboard.dts`** -> AI Confidence: **99.34%**
3127. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-icnova-swac.dts`** -> AI Confidence: **99.34%**
3128. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-lamobo-r1.dts`** -> AI Confidence: **99.34%**
3129. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-olimex-som-evb.dts`** -> AI Confidence: **99.34%**
3130. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-olimex-som204-evb.dts`** -> AI Confidence: **99.34%**
3131. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-olinuxino-lime2.dts`** -> AI Confidence: **99.34%**
3132. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-olinuxino-micro.dts`** -> AI Confidence: **99.34%**
3133. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-orangepi-mini.dts`** -> AI Confidence: **99.34%**
3134. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-orangepi.dts`** -> AI Confidence: **99.34%**
3135. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-pcduino3-nano.dts`** -> AI Confidence: **99.34%**
3136. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-pcduino3.dts`** -> AI Confidence: **99.34%**
3137. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-wits-pro-a20-dkt.dts`** -> AI Confidence: **99.34%**
3138. **`sys/contrib/device-tree/src/arm/allwinner/sun8i-a33-sinlinx-sina33.dts`** -> AI Confidence: **99.34%**
3139. **`sys/contrib/device-tree/src/arm/allwinner/sun8i-a83t-tbs-a711.dts`** -> AI Confidence: **99.34%**
3140. **`sys/contrib/device-tree/src/arm/allwinner/sun8i-r16-parrot.dts`** -> AI Confidence: **99.34%**
3141. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-ampere-mtjefferson.dts`** -> AI Confidence: **99.34%**
3142. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-ampere-mtmitchell.dts`** -> AI Confidence: **99.34%**
3143. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-asrock-e3c246d4i.dts`** -> AI Confidence: **99.34%**
3144. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-asrock-spc621d8hm3.dts`** -> AI Confidence: **99.34%**
3145. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-asus-x4tf.dts`** -> AI Confidence: **99.34%**
3146. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-bytedance-g220a.dts`** -> AI Confidence: **99.34%**
3147. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-facebook-greatlakes.dts`** -> AI Confidence: **99.34%**
3148. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-facebook-yosemite4.dts`** -> AI Confidence: **99.34%**
3149. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-ibm-blueridge.dts`** -> AI Confidence: **99.34%**
3150. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-ibm-bonnell.dts`** -> AI Confidence: **99.34%**
3151. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-ibm-everest.dts`** -> AI Confidence: **99.34%**
3152. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-ibm-fuji.dts`** -> AI Confidence: **99.34%**
3153. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-inspur-fp5280g2.dts`** -> AI Confidence: **99.34%**
3154. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-inspur-nf5280m6.dts`** -> AI Confidence: **99.34%**
3155. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-inventec-starscream.dts`** -> AI Confidence: **99.34%**
3156. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-inventec-transformers.dts`** -> AI Confidence: **99.34%**
3157. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-opp-tacoma.dts`** -> AI Confidence: **99.34%**
3158. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-ufispace-ncplite.dts`** -> AI Confidence: **99.34%**
3159. **`sys/contrib/device-tree/src/arm/broadcom/bcm2711-rpi-4-b.dts`** -> AI Confidence: **99.34%**
3160. **`sys/contrib/device-tree/src/arm/broadcom/bcm2835-rpi-a-plus.dts`** -> AI Confidence: **99.34%**
3161. **`sys/contrib/device-tree/src/arm/broadcom/bcm2835-rpi-a.dts`** -> AI Confidence: **99.34%**
3162. **`sys/contrib/device-tree/src/arm/broadcom/bcm2835-rpi-b-plus.dts`** -> AI Confidence: **99.34%**
3163. **`sys/contrib/device-tree/src/arm/broadcom/bcm2835-rpi-b-rev2.dts`** -> AI Confidence: **99.34%**
3164. **`sys/contrib/device-tree/src/arm/broadcom/bcm2835-rpi-b.dts`** -> AI Confidence: **99.34%**
3165. **`sys/contrib/device-tree/src/arm/broadcom/bcm2835-rpi-zero-w.dts`** -> AI Confidence: **99.34%**
3166. **`sys/contrib/device-tree/src/arm/broadcom/bcm2835-rpi-zero.dts`** -> AI Confidence: **99.34%**
3167. **`sys/contrib/device-tree/src/arm/broadcom/bcm2836-rpi-2-b.dts`** -> AI Confidence: **99.34%**
3168. **`sys/contrib/device-tree/src/arm/broadcom/bcm2837-rpi-2-b.dts`** -> AI Confidence: **99.34%**
3169. **`sys/contrib/device-tree/src/arm/broadcom/bcm2837-rpi-3-a-plus.dts`** -> AI Confidence: **99.34%**
3170. **`sys/contrib/device-tree/src/arm/broadcom/bcm2837-rpi-3-b-plus.dts`** -> AI Confidence: **99.34%**
3171. **`sys/contrib/device-tree/src/arm/broadcom/bcm2837-rpi-3-b.dts`** -> AI Confidence: **99.34%**
3172. **`sys/contrib/device-tree/src/arm/broadcom/bcm2837-rpi-zero-2-w.dts`** -> AI Confidence: **99.34%**
3173. **`sys/contrib/device-tree/src/arm/marvell/armada-370-c200-v2.dts`** -> AI Confidence: **99.34%**
3174. **`sys/contrib/device-tree/src/arm/marvell/armada-370-rd.dts`** -> AI Confidence: **99.34%**
3175. **`sys/contrib/device-tree/src/arm/microchip/at91-kizbox3_common.dtsi`** -> AI Confidence: **99.34%**
3176. **`sys/contrib/device-tree/src/arm/microchip/at91-sama5d27_wlsom1.dtsi`** -> AI Confidence: **99.34%**
3177. **`sys/contrib/device-tree/src/arm/microchip/at91-sama5d29_curiosity.dts`** -> AI Confidence: **99.34%**
3178. **`sys/contrib/device-tree/src/arm/microchip/at91-sama5d2_icp.dts`** -> AI Confidence: **99.34%**
3179. **`sys/contrib/device-tree/src/arm/microchip/at91-sama5d2_ptc_ek.dts`** -> AI Confidence: **99.34%**
3180. **`sys/contrib/device-tree/src/arm/microchip/at91-sama7g54_curiosity.dts`** -> AI Confidence: **99.34%**
3181. **`sys/contrib/device-tree/src/arm/microchip/at91sam9261.dtsi`** -> AI Confidence: **99.34%**
3182. **`sys/contrib/device-tree/src/arm/microchip/at91sam9n12.dtsi`** -> AI Confidence: **99.34%**
3183. **`sys/contrib/device-tree/src/arm/microchip/at91sam9rl.dtsi`** -> AI Confidence: **99.34%**
3184. **`sys/contrib/device-tree/src/arm/nvidia/tegra20-paz00.dts`** -> AI Confidence: **99.34%**
3185. **`sys/contrib/device-tree/src/arm/nvidia/tegra20-ventana.dts`** -> AI Confidence: **99.34%**
3186. **`sys/contrib/device-tree/src/arm/nvidia/tegra30-asus-transformer-common.dtsi`** -> AI Confidence: **99.34%**
3187. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6dl-prtvt7.dts`** -> AI Confidence: **99.34%**
3188. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-apalis-ixora.dts`** -> AI Confidence: **99.34%**
3189. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6ull-uti260b.dts`** -> AI Confidence: **99.34%**
3190. **`sys/contrib/device-tree/src/arm/nxp/ls/ls1021a-tqmls1021a-mbls1021a.dts`** -> AI Confidence: **99.34%**
3191. **`sys/contrib/device-tree/src/arm/qcom/qcom-apq8026-samsung-milletwifi.dts`** -> AI Confidence: **99.34%**
3192. **`sys/contrib/device-tree/src/arm/qcom/qcom-apq8064-cm-qs600.dts`** -> AI Confidence: **99.34%**
3193. **`sys/contrib/device-tree/src/arm/qcom/qcom-msm8974pro-oneplus-bacon.dts`** -> AI Confidence: **99.34%**
3194. **`sys/contrib/device-tree/src/arm/qcom/qcom-sdx55-t55.dts`** -> AI Confidence: **99.34%**
3195. **`sys/contrib/device-tree/src/arm/qcom/qcom-sdx55-telit-fn980-tlb.dts`** -> AI Confidence: **99.34%**
3196. **`sys/contrib/device-tree/src/arm/qcom/qcom-sdx65-mtp.dts`** -> AI Confidence: **99.34%**
3197. **`sys/contrib/device-tree/src/arm/renesas/r8a7740-armadillo800eva.dts`** -> AI Confidence: **99.34%**
3198. **`sys/contrib/device-tree/src/arm/renesas/r9a06g032-rzn1d400-db.dts`** -> AI Confidence: **99.34%**
3199. **`sys/contrib/device-tree/src/arm/samsung/exynos3250-artik5.dtsi`** -> AI Confidence: **99.34%**
3200. **`sys/contrib/device-tree/src/arm/samsung/exynos3250-monk.dts`** -> AI Confidence: **99.34%**
3201. **`sys/contrib/device-tree/src/arm/samsung/exynos3250-rinato.dts`** -> AI Confidence: **99.34%**
3202. **`sys/contrib/device-tree/src/arm/samsung/exynos4210-origen.dts`** -> AI Confidence: **99.34%**
3203. **`sys/contrib/device-tree/src/arm/samsung/exynos4412-origen.dts`** -> AI Confidence: **99.34%**
3204. **`sys/contrib/device-tree/src/arm/samsung/exynos5250-smdk5250.dts`** -> AI Confidence: **99.34%**
3205. **`sys/contrib/device-tree/src/arm/samsung/exynos5420-smdk5420.dts`** -> AI Confidence: **99.34%**
3206. **`sys/contrib/device-tree/src/arm/samsung/exynos5422-samsung-k3g.dts`** -> AI Confidence: **99.34%**
3207. **`sys/contrib/device-tree/src/arm/st/stm32429i-eval.dts`** -> AI Confidence: **99.34%**
3208. **`sys/contrib/device-tree/src/arm/st/stm32f429-disco.dts`** -> AI Confidence: **99.34%**
3209. **`sys/contrib/device-tree/src/arm/st/stm32f746-disco.dts`** -> AI Confidence: **99.34%**
3210. **`sys/contrib/device-tree/src/arm/st/stm32mp135f-dhcor-dhsbc.dts`** -> AI Confidence: **99.34%**
3211. **`sys/contrib/device-tree/src/arm/st/stm32mp157a-icore-stm32mp1-ctouch2-of10.dts`** -> AI Confidence: **99.34%**
3212. **`sys/contrib/device-tree/src/arm/st/stm32mp157a-icore-stm32mp1-ctouch2.dts`** -> AI Confidence: **99.34%**
3213. **`sys/contrib/device-tree/src/arm/st/stm32mp157a-icore-stm32mp1-edimm2.2.dts`** -> AI Confidence: **99.34%**
3214. **`sys/contrib/device-tree/src/arm/st/stm32mp157a-microgea-stm32mp1-microdev2.0-of7.dts`** -> AI Confidence: **99.34%**
3215. **`sys/contrib/device-tree/src/arm/st/stm32mp157a-microgea-stm32mp1-microdev2.0.dts`** -> AI Confidence: **99.34%**
3216. **`sys/contrib/device-tree/src/arm/st/stm32mp157c-dk2.dts`** -> AI Confidence: **99.34%**
3217. **`sys/contrib/device-tree/src/arm/st/stm32mp157c-lxa-mc1.dts`** -> AI Confidence: **99.34%**
3218. **`sys/contrib/device-tree/src/arm/st/stm32mp157c-osd32mp1-red.dts`** -> AI Confidence: **99.34%**
3219. **`sys/contrib/device-tree/src/arm/ti/omap/am335x-boneblack-wireless.dts`** -> AI Confidence: **99.34%**
3220. **`sys/contrib/device-tree/src/arm/ti/omap/am335x-sancloud-bbe-extended-wifi.dts`** -> AI Confidence: **99.34%**
3221. **`sys/contrib/device-tree/src/arm/ti/omap/am335x-sancloud-bbe.dts`** -> AI Confidence: **99.34%**
3222. **`sys/contrib/device-tree/src/arm/ti/omap/am437x-idk-evm.dts`** -> AI Confidence: **99.34%**
3223. **`sys/contrib/device-tree/src/arm/ti/omap/am437x-sk-evm.dts`** -> AI Confidence: **99.34%**
3224. **`sys/contrib/device-tree/src/arm/ti/omap/am43x-epos-evm.dts`** -> AI Confidence: **99.34%**
3225. **`sys/contrib/device-tree/src/arm/ti/omap/omap3-ldp.dts`** -> AI Confidence: **99.34%**
3226. **`sys/contrib/device-tree/src/arm/ti/omap/omap3-n900.dts`** -> AI Confidence: **99.34%**
3227. **`sys/contrib/device-tree/src/arm/ti/omap/omap4-sdp.dts`** -> AI Confidence: **99.34%**
3228. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-a133-liontron-h-a133l.dts`** -> AI Confidence: **99.34%**
3229. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-a64-pinetab.dts`** -> AI Confidence: **99.34%**
3230. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-a64-teres-i.dts`** -> AI Confidence: **99.34%**
3231. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-h313-tanix-tx1.dts`** -> AI Confidence: **99.34%**
3232. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-h5-nanopi-r1s-h5.dts`** -> AI Confidence: **99.34%**
3233. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-h5-orangepi-pc2.dts`** -> AI Confidence: **99.34%**
3234. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-h618-orangepi-zero2w.dts`** -> AI Confidence: **99.34%**
3235. **`sys/contrib/device-tree/src/arm64/amlogic/meson-g12a-fbx8am.dts`** -> AI Confidence: **99.34%**
3236. **`sys/contrib/device-tree/src/arm64/amlogic/meson-g12a-sei510.dts`** -> AI Confidence: **99.34%**
3237. **`sys/contrib/device-tree/src/arm64/amlogic/meson-g12a-u200.dts`** -> AI Confidence: **99.34%**
3238. **`sys/contrib/device-tree/src/arm64/amlogic/meson-g12b-odroid-go-ultra.dts`** -> AI Confidence: **99.34%**
3239. **`sys/contrib/device-tree/src/arm64/amlogic/meson-g12b-radxa-zero2.dts`** -> AI Confidence: **99.34%**
3240. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxbb-kii-pro.dts`** -> AI Confidence: **99.34%**
3241. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxm-ugoos-am3.dts`** -> AI Confidence: **99.34%**
3242. **`sys/contrib/device-tree/src/arm64/amlogic/meson-sm1-sei610.dts`** -> AI Confidence: **99.34%**
3243. **`sys/contrib/device-tree/src/arm64/exynos/exynos7-espresso.dts`** -> AI Confidence: **99.34%**
3244. **`sys/contrib/device-tree/src/arm64/exynos/exynos7.dtsi`** -> AI Confidence: **99.34%**
3245. **`sys/contrib/device-tree/src/arm64/exynos/exynos850.dtsi`** -> AI Confidence: **99.34%**
3246. **`sys/contrib/device-tree/src/arm64/exynos/exynos8895-dreamlte.dts`** -> AI Confidence: **99.34%**
3247. **`sys/contrib/device-tree/src/arm64/exynos/exynos8895.dtsi`** -> AI Confidence: **99.34%**
3248. **`sys/contrib/device-tree/src/arm64/exynos/exynosautov920.dtsi`** -> AI Confidence: **99.34%**
3249. **`sys/contrib/device-tree/src/arm64/freescale/imx8mm-venice-gw7901.dts`** -> AI Confidence: **99.34%**
3250. **`sys/contrib/device-tree/src/arm64/freescale/imx8mm-venice-gw7902.dts`** -> AI Confidence: **99.34%**
3251. **`sys/contrib/device-tree/src/arm64/freescale/imx8mm-venice-gw7903.dts`** -> AI Confidence: **99.34%**
3252. **`sys/contrib/device-tree/src/arm64/freescale/imx8mm-venice-gw7904.dts`** -> AI Confidence: **99.34%**
3253. **`sys/contrib/device-tree/src/arm64/freescale/imx8mn-venice-gw7902.dts`** -> AI Confidence: **99.34%**
3254. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-phyboard-pollux-rdk.dts`** -> AI Confidence: **99.34%**
3255. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-tqma8mpql-mba8mp-ras314.dts`** -> AI Confidence: **99.34%**
3256. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-tqma8mpql-mba8mpxl.dts`** -> AI Confidence: **99.34%**
3257. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-venice-gw74xx.dts`** -> AI Confidence: **99.34%**
3258. **`sys/contrib/device-tree/src/arm64/freescale/imx8mq-librem5-devkit.dts`** -> AI Confidence: **99.34%**
3259. **`sys/contrib/device-tree/src/arm64/freescale/imx93-tqma9352-mba91xxca.dts`** -> AI Confidence: **99.34%**
3260. **`sys/contrib/device-tree/src/arm64/freescale/imx93-tqma9352-mba93xxca.dts`** -> AI Confidence: **99.34%**
3261. **`sys/contrib/device-tree/src/arm64/freescale/imx93-tqma9352-mba93xxla.dts`** -> AI Confidence: **99.34%**
3262. **`sys/contrib/device-tree/src/arm64/freescale/imx95-15x15-evk.dts`** -> AI Confidence: **99.34%**
3263. **`sys/contrib/device-tree/src/arm64/hisilicon/hi3660-hikey960.dts`** -> AI Confidence: **99.34%**
3264. **`sys/contrib/device-tree/src/arm64/marvell/cn9130-cf-base.dts`** -> AI Confidence: **99.34%**
3265. **`sys/contrib/device-tree/src/arm64/marvell/cn9130-cf-pro.dts`** -> AI Confidence: **99.34%**
3266. **`sys/contrib/device-tree/src/arm64/marvell/cn9131-cf-solidwan.dts`** -> AI Confidence: **99.34%**
3267. **`sys/contrib/device-tree/src/arm64/mediatek/mt7622-bananapi-bpi-r64.dts`** -> AI Confidence: **99.34%**
3268. **`sys/contrib/device-tree/src/arm64/mediatek/mt7986a-bananapi-bpi-r3-mini.dts`** -> AI Confidence: **99.34%**
3269. **`sys/contrib/device-tree/src/arm64/mediatek/mt7986a-bananapi-bpi-r3.dts`** -> AI Confidence: **99.34%**
3270. **`sys/contrib/device-tree/src/arm64/mediatek/mt8365-evk.dts`** -> AI Confidence: **99.34%**
3271. **`sys/contrib/device-tree/src/arm64/nvidia/tegra210-p2894.dtsi`** -> AI Confidence: **99.34%**
3272. **`sys/contrib/device-tree/src/arm64/qcom/msm8916-acer-a1-724.dts`** -> AI Confidence: **99.34%**
3273. **`sys/contrib/device-tree/src/arm64/qcom/msm8916-alcatel-idol347.dts`** -> AI Confidence: **99.34%**
3274. **`sys/contrib/device-tree/src/arm64/qcom/msm8916-asus-z00l.dts`** -> AI Confidence: **99.34%**
3275. **`sys/contrib/device-tree/src/arm64/qcom/msm8916-gplus-fl8005a.dts`** -> AI Confidence: **99.34%**
3276. **`sys/contrib/device-tree/src/arm64/qcom/msm8916-huawei-g7.dts`** -> AI Confidence: **99.34%**
3277. **`sys/contrib/device-tree/src/arm64/qcom/msm8916-longcheer-l8150.dts`** -> AI Confidence: **99.34%**
3278. **`sys/contrib/device-tree/src/arm64/qcom/msm8916-samsung-serranove.dts`** -> AI Confidence: **99.34%**
3279. **`sys/contrib/device-tree/src/arm64/qcom/msm8916-wingtech-wt88047.dts`** -> AI Confidence: **99.34%**
3280. **`sys/contrib/device-tree/src/arm64/qcom/msm8917-xiaomi-riva.dts`** -> AI Confidence: **99.34%**
3281. **`sys/contrib/device-tree/src/arm64/qcom/msm8939-samsung-a7.dts`** -> AI Confidence: **99.34%**
3282. **`sys/contrib/device-tree/src/arm64/qcom/msm8996-xiaomi-natrium.dts`** -> AI Confidence: **99.34%**
3283. **`sys/contrib/device-tree/src/arm64/qcom/msm8996-xiaomi-scorpio.dts`** -> AI Confidence: **99.34%**
3284. **`sys/contrib/device-tree/src/arm64/qcom/msm8996pro-xiaomi-natrium.dts`** -> AI Confidence: **99.34%**
3285. **`sys/contrib/device-tree/src/arm64/qcom/qcs615-ride.dts`** -> AI Confidence: **99.34%**
3286. **`sys/contrib/device-tree/src/arm64/qcom/qcs8300-ride.dts`** -> AI Confidence: **99.34%**
3287. **`sys/contrib/device-tree/src/arm64/qcom/qcs8550-aim300-aiot.dts`** -> AI Confidence: **99.34%**
3288. **`sys/contrib/device-tree/src/arm64/qcom/sa8155p-adp.dts`** -> AI Confidence: **99.34%**
3289. **`sys/contrib/device-tree/src/arm64/qcom/sa8540p-ride.dts`** -> AI Confidence: **99.34%**
3290. **`sys/contrib/device-tree/src/arm64/qcom/sar2130p-qar2130p.dts`** -> AI Confidence: **99.34%**
3291. **`sys/contrib/device-tree/src/arm64/qcom/sc7180-trogdor-kingoftown.dts`** -> AI Confidence: **99.34%**
3292. **`sys/contrib/device-tree/src/arm64/qcom/sc7180-trogdor-lazor-limozeen-r10.dts`** -> AI Confidence: **99.34%**
3293. **`sys/contrib/device-tree/src/arm64/qcom/sc7180-trogdor-lazor-limozeen-r4.dts`** -> AI Confidence: **99.34%**
3294. **`sys/contrib/device-tree/src/arm64/qcom/sc7180-trogdor-lazor-limozeen-r9.dts`** -> AI Confidence: **99.34%**
3295. **`sys/contrib/device-tree/src/arm64/qcom/sc8280xp-crd.dts`** -> AI Confidence: **99.34%**
3296. **`sys/contrib/device-tree/src/arm64/qcom/sc8280xp-microsoft-arcata.dts`** -> AI Confidence: **99.34%**
3297. **`sys/contrib/device-tree/src/arm64/qcom/sdm845-mtp.dts`** -> AI Confidence: **99.34%**
3298. **`sys/contrib/device-tree/src/arm64/qcom/sdx75-idp.dts`** -> AI Confidence: **99.34%**
3299. **`sys/contrib/device-tree/src/arm64/qcom/sm6125-sony-xperia-seine-pdx201.dts`** -> AI Confidence: **99.34%**
3300. **`sys/contrib/device-tree/src/arm64/qcom/sm6350-sony-xperia-lena-pdx213.dts`** -> AI Confidence: **99.34%**
3301. **`sys/contrib/device-tree/src/arm64/qcom/sm6375-sony-xperia-murray-pdx225.dts`** -> AI Confidence: **99.34%**
3302. **`sys/contrib/device-tree/src/arm64/qcom/x1e001de-devkit.dts`** -> AI Confidence: **99.34%**
3303. **`sys/contrib/device-tree/src/arm64/qcom/x1e80100-lenovo-yoga-slim7x.dts`** -> AI Confidence: **99.34%**
3304. **`sys/contrib/device-tree/src/arm64/qcom/x1e80100-qcp.dts`** -> AI Confidence: **99.34%**
3305. **`sys/contrib/device-tree/src/arm64/renesas/r9a07g044l2-smarc.dts`** -> AI Confidence: **99.34%**
3306. **`sys/contrib/device-tree/src/arm64/renesas/r9a07g054l2-smarc.dts`** -> AI Confidence: **99.34%**
3307. **`sys/contrib/device-tree/src/arm64/renesas/rzg3s-smarc-som.dtsi`** -> AI Confidence: **99.34%**
3308. **`sys/contrib/device-tree/src/arm64/rockchip/rk3326-gameforce-chi.dts`** -> AI Confidence: **99.34%**
3309. **`sys/contrib/device-tree/src/arm64/rockchip/rk3328-rock-pi-e.dts`** -> AI Confidence: **99.34%**
3310. **`sys/contrib/device-tree/src/arm64/rockchip/rk3368-lba3368.dts`** -> AI Confidence: **99.34%**
3311. **`sys/contrib/device-tree/src/arm64/rockchip/rk3399-firefly.dts`** -> AI Confidence: **99.34%**
3312. **`sys/contrib/device-tree/src/arm64/rockchip/rk3399-orangepi.dts`** -> AI Confidence: **99.34%**
3313. **`sys/contrib/device-tree/src/arm64/rockchip/rk3399-pinebook-pro.dts`** -> AI Confidence: **99.34%**
3314. **`sys/contrib/device-tree/src/arm64/rockchip/rk3562-evb2-v10.dts`** -> AI Confidence: **99.34%**
3315. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-box-demo.dts`** -> AI Confidence: **99.34%**
3316. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-lubancat-1.dts`** -> AI Confidence: **99.34%**
3317. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-odroid-m1s.dts`** -> AI Confidence: **99.34%**
3318. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-quartz64-a.dts`** -> AI Confidence: **99.34%**
3319. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-quartz64-b.dts`** -> AI Confidence: **99.34%**
3320. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-roc-pc.dts`** -> AI Confidence: **99.34%**
3321. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-rock-3c.dts`** -> AI Confidence: **99.34%**
3322. **`sys/contrib/device-tree/src/arm64/rockchip/rk3566-soquartz-blade.dts`** -> AI Confidence: **99.34%**
3323. **`sys/contrib/device-tree/src/arm64/rockchip/rk3568-bpi-r2-pro.dts`** -> AI Confidence: **99.34%**
3324. **`sys/contrib/device-tree/src/arm64/rockchip/rk3568-evb1-v10.dts`** -> AI Confidence: **99.34%**
3325. **`sys/contrib/device-tree/src/arm64/rockchip/rk3568-lubancat-2.dts`** -> AI Confidence: **99.34%**
3326. **`sys/contrib/device-tree/src/arm64/rockchip/rk3568-mecsbc.dts`** -> AI Confidence: **99.34%**
3327. **`sys/contrib/device-tree/src/arm64/rockchip/rk3568-odroid-m1.dts`** -> AI Confidence: **99.34%**
3328. **`sys/contrib/device-tree/src/arm64/rockchip/rk3568-photonicat.dts`** -> AI Confidence: **99.34%**
3329. **`sys/contrib/device-tree/src/arm64/rockchip/rk3568-roc-pc.dts`** -> AI Confidence: **99.34%**
3330. **`sys/contrib/device-tree/src/arm64/rockchip/rk3568-rock-3a.dts`** -> AI Confidence: **99.34%**
3331. **`sys/contrib/device-tree/src/arm64/rockchip/rk3568-rock-3b.dts`** -> AI Confidence: **99.34%**
3332. **`sys/contrib/device-tree/src/arm64/rockchip/rk3568-wolfvision-pf5-display.dtsi`** -> AI Confidence: **99.34%**
3333. **`sys/contrib/device-tree/src/arm64/rockchip/rk3576-luckfox-core3576.dtsi`** -> AI Confidence: **99.34%**
3334. **`sys/contrib/device-tree/src/arm64/rockchip/rk3582-radxa-e52c.dts`** -> AI Confidence: **99.34%**
3335. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-armsom-sige7.dts`** -> AI Confidence: **99.34%**
3336. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-armsom-w3.dts`** -> AI Confidence: **99.34%**
3337. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-h96-max-v58.dts`** -> AI Confidence: **99.34%**
3338. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-orangepi-5-max.dts`** -> AI Confidence: **99.34%**
3339. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-orangepi-5-plus.dts`** -> AI Confidence: **99.34%**
3340. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-orangepi-5-ultra.dts`** -> AI Confidence: **99.34%**
3341. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-quartzpro64.dts`** -> AI Confidence: **99.34%**
3342. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-tiger.dtsi`** -> AI Confidence: **99.34%**
3343. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588s-coolpi-4b.dts`** -> AI Confidence: **99.34%**
3344. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588s-rock-5a.dts`** -> AI Confidence: **99.34%**
3345. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588s-rock-5c.dts`** -> AI Confidence: **99.34%**
3346. **`sys/contrib/device-tree/src/arm64/ti/k3-am642-evm.dts`** -> AI Confidence: **99.34%**
3347. **`sys/contrib/device-tree/src/arm64/ti/k3-am642-sk.dts`** -> AI Confidence: **99.34%**
3348. **`sys/contrib/device-tree/src/arm64/ti/k3-am68-phyboard-izar.dts`** -> AI Confidence: **99.34%**
3349. **`sys/contrib/device-tree/src/arm64/ti/k3-am68-sk-base-board.dts`** -> AI Confidence: **99.34%**
3350. **`sys/contrib/device-tree/src/arm64/ti/k3-j7200-common-proc-board.dts`** -> AI Confidence: **99.34%**
3351. **`sys/contrib/device-tree/src/arm64/ti/k3-j721e-beagleboneai64.dts`** -> AI Confidence: **99.34%**
3352. **`sys/contrib/device-tree/src/arm64/ti/k3-j721e-common-proc-board.dts`** -> AI Confidence: **99.34%**
3353. **`sys/contrib/device-tree/src/arm64/ti/k3-j721s2-common-proc-board.dts`** -> AI Confidence: **99.34%**
3354. **`sys/contrib/device-tree/src/arm64/xilinx/zynqmp-sm-k26-revA.dts`** -> AI Confidence: **99.34%**
3355. **`sys/contrib/device-tree/src/arm64/xilinx/zynqmp-zc1751-xm015-dc1.dts`** -> AI Confidence: **99.34%**
3356. **`sys/contrib/device-tree/src/arm64/xilinx/zynqmp-zcu104-revA.dts`** -> AI Confidence: **99.34%**
3357. **`sys/contrib/device-tree/src/arm64/xilinx/zynqmp-zcu104-revC.dts`** -> AI Confidence: **99.34%**
3358. **`sys/contrib/device-tree/src/arm64/xilinx/zynqmp-zcu106-revA.dts`** -> AI Confidence: **99.34%**
3359. **`sys/contrib/device-tree/src/arm64/xilinx/zynqmp-zcu111-revA.dts`** -> AI Confidence: **99.34%**
3360. **`sys/contrib/device-tree/src/mips/img/pistachio.dtsi`** -> AI Confidence: **99.34%**
3361. **`sys/contrib/device-tree/src/mips/ingenic/cu1000-neo.dts`** -> AI Confidence: **99.34%**
3362. **`sys/contrib/device-tree/src/mips/ingenic/cu1830-neo.dts`** -> AI Confidence: **99.34%**
3363. **`sys/contrib/device-tree/src/mips/ingenic/rs90.dts`** -> AI Confidence: **99.34%**
3364. **`sys/contrib/libsodium/src/libsodium/crypto_pwhash/argon2/blake2b-long.c`** -> AI Confidence: **99.34%**
3365. **`sys/contrib/ncsw/Peripherals/FM/fm.h`** -> AI Confidence: **99.34%**
3366. **`sys/contrib/openzfs/include/os/linux/spl/sys/timer.h`** -> AI Confidence: **99.34%**
3367. **`sys/contrib/openzfs/module/icp/api/kcf_cipher.c`** -> AI Confidence: **99.34%**
3368. **`sys/contrib/openzfs/module/icp/io/sha2_mod.c`** -> AI Confidence: **99.34%**
3369. **`sys/contrib/openzfs/module/lua/lobject.c`** -> AI Confidence: **99.34%**
3370. **`sys/contrib/openzfs/module/zfs/dmu_direct.c`** -> AI Confidence: **99.34%**
3371. **`sys/contrib/openzfs/module/zfs/lz4.c`** -> AI Confidence: **99.34%**
3372. **`sys/contrib/openzfs/module/zfs/vdev_raidz_math_avx2.c`** -> AI Confidence: **99.34%**
3373. **`sys/contrib/openzfs/module/zfs/vdev_raidz_math_avx512bw.c`** -> AI Confidence: **99.34%**
3374. **`sys/contrib/openzfs/module/zfs/vdev_raidz_math_avx512f.c`** -> AI Confidence: **99.34%**
3375. **`sys/contrib/openzfs/module/zfs/vdev_raidz_math_sse2.c`** -> AI Confidence: **99.34%**
3376. **`sys/contrib/openzfs/module/zfs/zfs_quota.c`** -> AI Confidence: **99.34%**
3377. **`sys/contrib/openzfs/tests/zfs-tests/cmd/mmap_ftruncate.c`** -> AI Confidence: **99.34%**
3378. **`sys/contrib/openzfs/tests/zfs-tests/cmd/mmap_write_sync.c`** -> AI Confidence: **99.34%**
3379. **`sys/contrib/zstd/programs/platform.h`** -> AI Confidence: **99.34%**
3380. **`sys/contrib/zstd/zlibWrapper/gzguts.h`** -> AI Confidence: **99.34%**
3381. **`sys/crypto/aesni/aesni_ghash.c`** -> AI Confidence: **99.34%**
3382. **`sys/crypto/camellia/camellia.c`** -> AI Confidence: **99.34%**
3383. **`sys/crypto/rijndael/rijndael-api-fst.c`** -> AI Confidence: **99.34%**
3384. **`sys/crypto/skein/skein_block.c`** -> AI Confidence: **99.34%**
3385. **`sys/ddb/db_access.c`** -> AI Confidence: **99.34%**
3386. **`sys/ddb/db_input.c`** -> AI Confidence: **99.34%**
3387. **`sys/dev/ath/ath_hal/ar5212/ar5413.c`** -> AI Confidence: **99.34%**
3388. **`sys/dev/ath/ath_hal/ar5416/ar5416_btcoex.c`** -> AI Confidence: **99.34%**
3389. **`sys/dev/chromebook_platform/chromebook_platform.c`** -> AI Confidence: **99.34%**
3390. **`sys/dev/fb/splash_pcx.c`** -> AI Confidence: **99.34%**
3391. **`sys/dev/isci/scil/sati_device.c`** -> AI Confidence: **99.34%**
3392. **`sys/dev/isci/scil/sati_start_stop_unit.c`** -> AI Confidence: **99.34%**
3393. **`sys/dev/isp/isp_target.c`** -> AI Confidence: **99.34%**
3394. **`sys/dev/mlx4/mlx4_core/mlx4_reset.c`** -> AI Confidence: **99.34%**
3395. **`sys/dev/mpi3mr/mpi3mr_app.c`** -> AI Confidence: **99.34%**
3396. **`sys/dev/mthca/mthca_reset.c`** -> AI Confidence: **99.34%**
3397. **`sys/dev/ocs_fc/ocs_ioctl.c`** -> AI Confidence: **99.34%**
3398. **`sys/dev/qlxgbe/ql_misc.c`** -> AI Confidence: **99.34%**
3399. **`sys/dev/qlxge/qls_dump.c`** -> AI Confidence: **99.34%**
3400. **`sys/dev/sfxge/common/ef10_nic.c`** -> AI Confidence: **99.34%**
3401. **`sys/dev/sfxge/common/hunt_nic.c`** -> AI Confidence: **99.34%**
3402. **`sys/dev/sound/pci/vibes.c`** -> AI Confidence: **99.34%**
3403. **`sys/dts/arm/qcom-ipq4018-rt-ac58u.dts`** -> AI Confidence: **99.34%**
3404. **`sys/fs/nfsserver/nfs_nfsdserv.c`** -> AI Confidence: **99.34%**
3405. **`sys/i386/i386/db_disasm.c`** -> AI Confidence: **99.34%**
3406. **`sys/kern/subr_scanf.c`** -> AI Confidence: **99.34%**
3407. **`sys/libkern/inet_aton.c`** -> AI Confidence: **99.34%**
3408. **`sys/powerpc/fpu/fpu_compare.c`** -> AI Confidence: **99.34%**
3409. **`sys/powerpc/fpu/fpu_implode.c`** -> AI Confidence: **99.34%**
3410. **`sys/powerpc/fpu/fpu_mul.c`** -> AI Confidence: **99.34%**
3411. **`sys/riscv/riscv/db_disasm.c`** -> AI Confidence: **99.34%**
3412. **`sys/security/audit/bsm_domain.c`** -> AI Confidence: **99.34%**
3413. **`sys/security/audit/bsm_errno.c`** -> AI Confidence: **99.34%**
3414. **`sys/xdr/xdr_array.c`** -> AI Confidence: **99.34%**
3415. **`tests/sys/cddl/zfs/bin/devname2devid.c`** -> AI Confidence: **99.34%**
3416. **`tests/sys/kern/execve/execve_helper.c`** -> AI Confidence: **99.34%**
3417. **`tests/sys/netinet/libalias/perf.c`** -> AI Confidence: **99.34%**
3418. **`tests/sys/vm/mmap_map_32bit_helper.c`** -> AI Confidence: **99.34%**
3419. **`tools/regression/audit/audit_pipe_ioctl/audit_pipe_ioctl.c`** -> AI Confidence: **99.34%**
3420. **`tools/regression/priv/priv_acct.c`** -> AI Confidence: **99.34%**
3421. **`tools/regression/security/cap_test/cap_test.c`** -> AI Confidence: **99.34%**
3422. **`tools/regression/sockets/listenclose/listenclose.c`** -> AI Confidence: **99.34%**
3423. **`tools/regression/sockets/rtsocket/rtsocket.c`** -> AI Confidence: **99.34%**
3424. **`tools/regression/sockets/unix_socket/unix_socket.c`** -> AI Confidence: **99.34%**
3425. **`tools/regression/usr.bin/cc/float.c`** -> AI Confidence: **99.34%**
3426. **`tools/test/stress2/testcases/mkdir/mkdir.c`** -> AI Confidence: **99.34%**
3427. **`tools/test/stress2/testcases/openat/openat.c`** -> AI Confidence: **99.34%**
3428. **`tools/tools/bhyve/fwctl_fetch.c`** -> AI Confidence: **99.34%**
3429. **`tools/tools/cfi/cfi.c`** -> AI Confidence: **99.34%**
3430. **`tools/tools/mwl/mwlstats/main.c`** -> AI Confidence: **99.34%**
3431. **`usr.bin/asa/asa.c`** -> AI Confidence: **99.34%**
3432. **`usr.bin/ctags/fortran.c`** -> AI Confidence: **99.34%**
3433. **`usr.bin/ctags/lisp.c`** -> AI Confidence: **99.34%**
3434. **`usr.bin/ctags/print.c`** -> AI Confidence: **99.34%**
3435. **`usr.bin/enigma/enigma.c`** -> AI Confidence: **99.34%**
3436. **`usr.bin/file2c/file2c.c`** -> AI Confidence: **99.34%**
3437. **`usr.bin/find/function.c`** -> AI Confidence: **99.34%**
3438. **`usr.bin/gprof/gprof.c`** -> AI Confidence: **99.34%**
3439. **`usr.bin/indent/parse.c`** -> AI Confidence: **99.34%**
3440. **`usr.bin/lex/initparse.c`** -> AI Confidence: **99.34%**
3441. **`usr.bin/locate/bigram/locate.bigram.c`** -> AI Confidence: **99.34%**
3442. **`usr.bin/lsvfs/lsvfs.c`** -> AI Confidence: **99.34%**
3443. **`usr.bin/mkfifo/mkfifo.c`** -> AI Confidence: **99.34%**
3444. **`usr.bin/pr/egetopt.c`** -> AI Confidence: **99.34%**
3445. **`usr.bin/procstat/procstat_basic.c`** -> AI Confidence: **99.34%**
3446. **`usr.bin/rev/rev.c`** -> AI Confidence: **99.34%**
3447. **`usr.bin/systat/ifcmds.c`** -> AI Confidence: **99.34%**
3448. **`usr.bin/talk/ctl_transact.c`** -> AI Confidence: **99.34%**
3449. **`usr.bin/tsort/tsort.c`** -> AI Confidence: **99.34%**
3450. **`usr.bin/vgrind/regexp.c`** -> AI Confidence: **99.34%**
3451. **`usr.bin/yes/yes.c`** -> AI Confidence: **99.34%**
3452. **`usr.sbin/bluetooth/bthidcontrol/hid.c`** -> AI Confidence: **99.34%**
3453. **`usr.sbin/bluetooth/hccontrol/send_recv.c`** -> AI Confidence: **99.34%**
3454. **`usr.sbin/boottrace/boottrace.c`** -> AI Confidence: **99.34%**
3455. **`usr.sbin/fstyp/msdosfs.c`** -> AI Confidence: **99.34%**
3456. **`usr.sbin/lpr/filters.ru/koi2855/koi2855.c`** -> AI Confidence: **99.34%**
3457. **`usr.sbin/lpr/filters.ru/koi2alt/koi2alt.c`** -> AI Confidence: **99.34%**
3458. **`usr.sbin/lpr/filters/lpf.c`** -> AI Confidence: **99.34%**
3459. **`usr.sbin/mfiutil/mfi_show.c`** -> AI Confidence: **99.34%**
3460. **`usr.sbin/mpsutil/mps_show.c`** -> AI Confidence: **99.34%**
3461. **`usr.sbin/pw/psdate.c`** -> AI Confidence: **99.34%**
3462. **`usr.sbin/pw/pw_conf.c`** -> AI Confidence: **99.34%**
3463. **`usr.sbin/rpcbind/security.c`** -> AI Confidence: **99.34%**
3464. **`usr.sbin/syslogd/syslogd_cap.c`** -> AI Confidence: **99.34%**
3465. **`usr.sbin/virtual_oss/virtual_oss/eq.c`** -> AI Confidence: **99.34%**
3466. **`usr.sbin/virtual_oss/virtual_oss/format.c`** -> AI Confidence: **99.34%**
3467. **`contrib/llvm-project/clang/include/clang/AST/CommentParser.h`** -> AI Confidence: **99.34%**
3468. **`contrib/llvm-project/clang/include/clang/AST/EvaluatedExprVisitor.h`** -> AI Confidence: **99.34%**
3469. **`contrib/llvm-project/clang/include/clang/Analysis/FlowSensitive/CFGMatchSwitch.h`** -> AI Confidence: **99.34%**
3470. **`contrib/llvm-project/clang/include/clang/Analysis/FlowSensitive/NoopAnalysis.h`** -> AI Confidence: **99.34%**
3471. **`contrib/llvm-project/clang/include/clang/StaticAnalyzer/Core/PathSensitive/RangedConstraintManager.h`** -> AI Confidence: **99.34%**
3472. **`contrib/llvm-project/clang/include/clang/Testing/TestAST.h`** -> AI Confidence: **99.34%**
3473. **`contrib/llvm-project/clang/include/clang/Tooling/Transformer/RangeSelector.h`** -> AI Confidence: **99.34%**
3474. **`contrib/llvm-project/libcxx/include/__algorithm/binary_search.h`** -> AI Confidence: **99.34%**
3475. **`contrib/llvm-project/libcxx/include/__algorithm/max.h`** -> AI Confidence: **99.34%**
3476. **`contrib/llvm-project/libcxx/include/__algorithm/min.h`** -> AI Confidence: **99.34%**
3477. **`contrib/llvm-project/libcxx/include/__concepts/arithmetic.h`** -> AI Confidence: **99.34%**
3478. **`contrib/llvm-project/libcxx/include/__concepts/assignable.h`** -> AI Confidence: **99.34%**
3479. **`contrib/llvm-project/libcxx/include/__concepts/class_or_enum.h`** -> AI Confidence: **99.34%**
3480. **`contrib/llvm-project/libcxx/include/__concepts/equality_comparable.h`** -> AI Confidence: **99.34%**
3481. **`contrib/llvm-project/libcxx/include/__concepts/movable.h`** -> AI Confidence: **99.34%**
3482. **`contrib/llvm-project/libcxx/include/__concepts/totally_ordered.h`** -> AI Confidence: **99.34%**
3483. **`contrib/llvm-project/libcxx/include/__iterator/mergeable.h`** -> AI Confidence: **99.34%**
3484. **`contrib/llvm-project/libcxx/include/__iterator/sortable.h`** -> AI Confidence: **99.34%**
3485. **`contrib/llvm-project/libcxx/include/__memory/swap_allocator.h`** -> AI Confidence: **99.34%**
3486. **`contrib/llvm-project/libcxx/include/__random/exponential_distribution.h`** -> AI Confidence: **99.34%**
3487. **`contrib/llvm-project/libcxx/include/__random/generate_canonical.h`** -> AI Confidence: **99.34%**
3488. **`contrib/llvm-project/libcxx/include/__random/student_t_distribution.h`** -> AI Confidence: **99.34%**
3489. **`contrib/llvm-project/libcxx/include/__stop_token/stop_source.h`** -> AI Confidence: **99.34%**
3490. **`contrib/llvm-project/libcxx/src/experimental/include/tzdb/tzdb_list_private.h`** -> AI Confidence: **99.34%**
3491. **`contrib/llvm-project/llvm/include/llvm/ADT/APFloat.h`** -> AI Confidence: **99.34%**
3492. **`contrib/llvm-project/llvm/include/llvm/ADT/DirectedGraph.h`** -> AI Confidence: **99.34%**
3493. **`contrib/llvm-project/llvm/include/llvm/ADT/ImmutableList.h`** -> AI Confidence: **99.34%**
3494. **`contrib/llvm-project/llvm/include/llvm/DebugInfo/PDB/ConcreteSymbolEnumerator.h`** -> AI Confidence: **99.34%**
3495. **`contrib/llvm-project/llvm/include/llvm/IR/ConstantRangeList.h`** -> AI Confidence: **99.34%**
3496. **`contrib/llvm-project/llvm/include/llvm/IR/InstVisitor.h`** -> AI Confidence: **99.34%**
3497. **`contrib/llvm-project/llvm/include/llvm/MC/MCLinkerOptimizationHint.h`** -> AI Confidence: **99.34%**
3498. **`contrib/llvm-project/llvm/include/llvm/MCA/CustomBehaviour.h`** -> AI Confidence: **99.34%**
3499. **`contrib/llvm-project/llvm/include/llvm/MCA/HardwareUnits/ResourceManager.h`** -> AI Confidence: **99.34%**
3500. **`contrib/llvm-project/llvm/include/llvm/MCA/Stages/InstructionTables.h`** -> AI Confidence: **99.34%**
3501. **`contrib/llvm-project/llvm/include/llvm/MCA/Stages/RetireStage.h`** -> AI Confidence: **99.34%**
3502. **`contrib/llvm-project/llvm/include/llvm/Remarks/RemarkStreamer.h`** -> AI Confidence: **99.34%**
3503. **`contrib/llvm-project/llvm/include/llvm/Support/Compiler.h`** -> AI Confidence: **99.34%**
3504. **`contrib/llvm-project/llvm/include/llvm/Support/ErrorOr.h`** -> AI Confidence: **99.34%**
3505. **`contrib/llvm-project/llvm/include/llvm/Testing/ADT/StringMap.h`** -> AI Confidence: **99.34%**
3506. **`contrib/llvm-project/llvm/include/llvm/XRay/FDRRecordConsumer.h`** -> AI Confidence: **99.34%**
3507. **`contrib/lua/src/luaconf.h`** -> AI Confidence: **99.34%**
3508. **`crypto/krb5/src/lib/crypto/builtin/aes/brg_endian.h`** -> AI Confidence: **99.34%**
3509. **`crypto/openssl/include/openssl/e_ostime.h`** -> AI Confidence: **99.34%**
3510. **`crypto/openssl/include/openssl/ssl3.h`** -> AI Confidence: **99.34%**
3511. **`stand/liblua/luaconf.h`** -> AI Confidence: **99.34%**
3512. **`sys/compat/linuxkpi/common/include/linux/jiffies.h`** -> AI Confidence: **99.34%**
3513. **`sys/contrib/ck/include/ck_swlock.h`** -> AI Confidence: **99.34%**
3514. **`sys/contrib/dev/acpica/include/platform/acenvex.h`** -> AI Confidence: **99.34%**
3515. **`sys/contrib/openzfs/include/os/freebsd/spl/sys/sysmacros.h`** -> AI Confidence: **99.34%**
3516. **`sys/contrib/openzfs/include/os/linux/zfs/sys/trace_arc.h`** -> AI Confidence: **99.34%**
3517. **`sys/contrib/openzfs/include/os/linux/zfs/sys/trace_zio.h`** -> AI Confidence: **99.34%**
3518. **`sys/netinet/netdump/netdump.h`** -> AI Confidence: **99.34%**
3519. **`libexec/rc/rc.firewall`** -> AI Confidence: **99.34%**
3520. **`tools/tools/nanobsd/nanobsd.sh`** -> AI Confidence: **99.34%**
3521. **`contrib/kyua/integration/helpers/expect_all_pass.cpp`** -> AI Confidence: **99.34%**
3522. **`contrib/kyua/utils/memory_test.cpp`** -> AI Confidence: **99.34%**
3523. **`contrib/kyua/utils/stream_test.cpp`** -> AI Confidence: **99.34%**
3524. **`contrib/llvm-project/clang/utils/TableGen/ClangBuiltinsEmitter.cpp`** -> AI Confidence: **99.34%**
3525. **`contrib/llvm-project/lld/ELF/Arch/AArch64.cpp`** -> AI Confidence: **99.34%**
3526. **`contrib/llvm-project/lld/ELF/Arch/PPC.cpp`** -> AI Confidence: **99.34%**
3527. **`contrib/llvm-project/lldb/source/Breakpoint/BreakpointIDList.cpp`** -> AI Confidence: **99.34%**
3528. **`contrib/llvm-project/lldb/source/Interpreter/OptionValuePathMappings.cpp`** -> AI Confidence: **99.34%**
3529. **`contrib/llvm-project/lldb/source/Plugins/ObjectFile/Minidump/MinidumpFileBuilder.h`** -> AI Confidence: **99.34%**
3530. **`contrib/llvm-project/lldb/source/Utility/Args.cpp`** -> AI Confidence: **99.34%**
3531. **`contrib/llvm-project/llvm/lib/Transforms/Utils/LoopConstrainer.cpp`** -> AI Confidence: **99.34%**
3532. **`contrib/llvm-project/llvm/utils/TableGen/Common/AsmWriterInst.cpp`** -> AI Confidence: **99.34%**
3533. **`contrib/llvm-project/llvm/utils/TableGen/Common/CodeGenInstruction.cpp`** -> AI Confidence: **99.34%**
3534. **`contrib/llvm-project/llvm/utils/TableGen/DAGISelMatcherOpt.cpp`** -> AI Confidence: **99.34%**
3535. **`contrib/llvm-project/llvm/utils/TableGen/OptRSTEmitter.cpp`** -> AI Confidence: **99.34%**
3536. **`contrib/llvm-project/openmp/runtime/src/kmp_cancel.cpp`** -> AI Confidence: **99.34%**
3537. **`contrib/llvm-project/openmp/runtime/src/kmp_collapse.cpp`** -> AI Confidence: **99.34%**
3538. **`contrib/llvm-project/openmp/runtime/src/kmp_str.cpp`** -> AI Confidence: **99.34%**
3539. **`contrib/llvm-project/openmp/runtime/src/kmp_taskdeps.cpp`** -> AI Confidence: **99.34%**
3540. **`contrib/llvm-project/openmp/runtime/src/kmp_utility.cpp`** -> AI Confidence: **99.34%**
3541. **`contrib/opencsd/decoder/source/mem_acc/trc_mem_acc_base.cpp`** -> AI Confidence: **99.34%**
3542. **`tests/sys/capsicum/fcntl.cc`** -> AI Confidence: **99.34%**
3543. **`crypto/openssh/openbsd-compat/openssl-compat.h`** -> AI Confidence: **99.33%**
3544. **`crypto/openssl/ssl/statem/extensions.c`** -> AI Confidence: **99.33%**
3545. **`usr.bin/cmp/special.c`** -> AI Confidence: **99.33%**
3546. **`contrib/openbsm/bin/auditdistd/sigtimedwait.h`** -> AI Confidence: **99.33%**
3547. **`sys/compat/linuxkpi/common/include/linux/page.h`** -> AI Confidence: **99.33%**
3548. **`contrib/bc/src/dc_lex.c`** -> AI Confidence: **99.32%**
3549. **`contrib/bmake/metachar.c`** -> AI Confidence: **99.32%**
3550. **`contrib/bmake/pathnames.h`** -> AI Confidence: **99.32%**
3551. **`contrib/bzip2/unzcrash.c`** -> AI Confidence: **99.32%**
3552. **`contrib/dialog/dlg_keys.c`** -> AI Confidence: **99.32%**
3553. **`contrib/dialog/editbox.c`** -> AI Confidence: **99.32%**
3554. **`contrib/dialog/timebox.c`** -> AI Confidence: **99.32%**
3555. **`contrib/file/src/strlcpy.c`** -> AI Confidence: **99.32%**
3556. **`contrib/flex/src/yylex.c`** -> AI Confidence: **99.32%**
3557. **`contrib/gdtoa/strtod.c`** -> AI Confidence: **99.32%**
3558. **`contrib/ldns/compat/strlcpy.c`** -> AI Confidence: **99.32%**
3559. **`contrib/less/less.h`** -> AI Confidence: **99.32%**
3560. **`contrib/less/optfunc.c`** -> AI Confidence: **99.32%**
3561. **`contrib/libfido2/openbsd-compat/strlcat.c`** -> AI Confidence: **99.32%**
3562. **`contrib/libfido2/openbsd-compat/strlcpy.c`** -> AI Confidence: **99.32%**
3563. **`contrib/libfido2/openbsd-compat/strsep.c`** -> AI Confidence: **99.32%**
3564. **`contrib/libyaml/tests/example-deconstructor-alt.c`** -> AI Confidence: **99.32%**
3565. **`contrib/libyaml/tests/example-deconstructor.c`** -> AI Confidence: **99.32%**
3566. **`contrib/libyaml/tests/example-reformatter-alt.c`** -> AI Confidence: **99.32%**
3567. **`contrib/libyaml/tests/example-reformatter.c`** -> AI Confidence: **99.32%**
3568. **`contrib/llvm-project/libcxx/include/__concepts/regular.h`** -> AI Confidence: **99.32%**
3569. **`contrib/llvm-project/libcxx/include/stdatomic.h`** -> AI Confidence: **99.32%**
3570. **`contrib/lua/src/lctype.c`** -> AI Confidence: **99.32%**
3571. **`contrib/mandoc/compat_strlcpy.c`** -> AI Confidence: **99.32%**
3572. **`contrib/ncurses/menu/mf_common.h`** -> AI Confidence: **99.32%**
3573. **`contrib/ncurses/ncurses/base/lib_slkset.c`** -> AI Confidence: **99.32%**
3574. **`contrib/ncurses/ncurses/tinfo/captoinfo.c`** -> AI Confidence: **99.32%**
3575. **`contrib/ncurses/ncurses/tinfo/comp_expand.c`** -> AI Confidence: **99.32%**
3576. **`contrib/ncurses/ncurses/tinfo/comp_scan.c`** -> AI Confidence: **99.32%**
3577. **`contrib/ncurses/ncurses/tinfo/lib_napms.c`** -> AI Confidence: **99.32%**
3578. **`contrib/ncurses/ncurses/tinfo/lib_tgoto.c`** -> AI Confidence: **99.32%**
3579. **`contrib/ncurses/ncurses/tinfo/read_entry.c`** -> AI Confidence: **99.32%**
3580. **`contrib/ncurses/ncurses/tinfo/trim_sgr0.c`** -> AI Confidence: **99.32%**
3581. **`contrib/ncurses/ncurses/tinfo/write_entry.c`** -> AI Confidence: **99.32%**
3582. **`contrib/ntp/libntp/getopt.c`** -> AI Confidence: **99.32%**
3583. **`contrib/ntp/ntpd/rc_cmdlength.c`** -> AI Confidence: **99.32%**
3584. **`contrib/ntp/sntp/libevent/util-internal.h`** -> AI Confidence: **99.32%**
3585. **`contrib/sendmail/include/sm/limits.h`** -> AI Confidence: **99.32%**
3586. **`contrib/sendmail/libsmutil/safefile.c`** -> AI Confidence: **99.32%**
3587. **`contrib/sendmail/src/headers.c`** -> AI Confidence: **99.32%**
3588. **`contrib/sendmail/src/mime.c`** -> AI Confidence: **99.32%**
3589. **`contrib/sendmail/src/trace.c`** -> AI Confidence: **99.32%**
3590. **`contrib/tcpdump/netdissect-stdinc.h`** -> AI Confidence: **99.32%**
3591. **`contrib/tcsh/ed.term.c`** -> AI Confidence: **99.32%**
3592. **`contrib/tcsh/sh.init.c`** -> AI Confidence: **99.32%**
3593. **`contrib/tcsh/tc.prompt.c`** -> AI Confidence: **99.32%**
3594. **`contrib/tcsh/tc.vers.c`** -> AI Confidence: **99.32%**
3595. **`contrib/unbound/compat/strlcpy.c`** -> AI Confidence: **99.32%**
3596. **`contrib/wpa/src/crypto/rc4.c`** -> AI Confidence: **99.32%**
3597. **`contrib/wpa/src/utils/config.c`** -> AI Confidence: **99.32%**
3598. **`contrib/xz/src/xz/util.c`** -> AI Confidence: **99.32%**
3599. **`crypto/heimdal/appl/rcp/rcp.c`** -> AI Confidence: **99.32%**
3600. **`crypto/heimdal/kadmin/dump.c`** -> AI Confidence: **99.32%**
3601. **`crypto/heimdal/kadmin/kadmin.c`** -> AI Confidence: **99.32%**
3602. **`crypto/heimdal/kdc/config.c`** -> AI Confidence: **99.32%**
3603. **`crypto/heimdal/kdc/default_config.c`** -> AI Confidence: **99.32%**
3604. **`crypto/heimdal/kdc/main.c`** -> AI Confidence: **99.32%**
3605. **`crypto/heimdal/kuser/kinit.c`** -> AI Confidence: **99.32%**
3606. **`crypto/krb5/src/ccapi/common/cci_array_internal.c`** -> AI Confidence: **99.32%**
3607. **`crypto/krb5/src/ccapi/lib/ccapi_ccache_iterator.c`** -> AI Confidence: **99.32%**
3608. **`crypto/krb5/src/ccapi/server/ccs_cache_collection.c`** -> AI Confidence: **99.32%**
3609. **`crypto/krb5/src/kadmin/dbutil/strtok.c`** -> AI Confidence: **99.32%**
3610. **`crypto/krb5/src/kdc/fast_util.c`** -> AI Confidence: **99.32%**
3611. **`crypto/krb5/src/kdc/kdc_preauth_ec.c`** -> AI Confidence: **99.32%**
3612. **`crypto/krb5/src/kdc/kdc_preauth_encts.c`** -> AI Confidence: **99.32%**
3613. **`crypto/krb5/src/lib/crypto/builtin/des/f_cksum.c`** -> AI Confidence: **99.32%**
3614. **`crypto/krb5/src/lib/crypto/builtin/sha1/shs.c`** -> AI Confidence: **99.32%**
3615. **`crypto/krb5/src/lib/gssapi/krb5/k5unsealiov.c`** -> AI Confidence: **99.32%**
3616. **`crypto/krb5/src/lib/krb5/ccache/ccdefops.c`** -> AI Confidence: **99.32%**
3617. **`crypto/krb5/src/lib/krb5/krb/conv_princ.c`** -> AI Confidence: **99.32%**
3618. **`crypto/krb5/src/lib/krb5/krb/copy_ctx.c`** -> AI Confidence: **99.32%**
3619. **`crypto/krb5/src/lib/krb5/krb/decode_kdc.c`** -> AI Confidence: **99.32%**
3620. **`crypto/krb5/src/lib/krb5/krb/mk_cred.c`** -> AI Confidence: **99.32%**
3621. **`crypto/krb5/src/lib/krb5/krb/mk_priv.c`** -> AI Confidence: **99.32%**
3622. **`crypto/krb5/src/lib/krb5/krb/mk_req_ext.c`** -> AI Confidence: **99.32%**
3623. **`crypto/krb5/src/lib/krb5/krb/preauth_ec.c`** -> AI Confidence: **99.32%**
3624. **`crypto/krb5/src/lib/krb5/krb/rd_cred.c`** -> AI Confidence: **99.32%**
3625. **`crypto/krb5/src/lib/krb5/krb/rd_priv.c`** -> AI Confidence: **99.32%**
3626. **`crypto/krb5/src/lib/krb5/krb/rd_safe.c`** -> AI Confidence: **99.32%**
3627. **`crypto/krb5/src/lib/krb5/krb/s4u_creds.c`** -> AI Confidence: **99.32%**
3628. **`crypto/krb5/src/lib/krb5/krb/send_tgs.c`** -> AI Confidence: **99.32%**
3629. **`crypto/krb5/src/lib/krb5/krb/strptime.c`** -> AI Confidence: **99.32%**
3630. **`crypto/krb5/src/lib/krb5/krb/t_get_etype_info.c`** -> AI Confidence: **99.32%**
3631. **`crypto/krb5/src/lib/krb5/krb/t_walk_rtree.c`** -> AI Confidence: **99.32%**
3632. **`crypto/krb5/src/lib/krb5/os/accessor.c`** -> AI Confidence: **99.32%**
3633. **`crypto/krb5/src/lib/krb5/rcache/t_rcfile2.c`** -> AI Confidence: **99.32%**
3634. **`crypto/krb5/src/lib/krb5/unicode/ucdata/ucgendat.c`** -> AI Confidence: **99.32%**
3635. **`crypto/krb5/src/plugins/kdb/db2/adb_policy.c`** -> AI Confidence: **99.32%**
3636. **`crypto/krb5/src/plugins/kdb/ldap/libkdb_ldap/ldap_krbcontainer.c`** -> AI Confidence: **99.32%**
3637. **`crypto/krb5/src/util/ss/parse.c`** -> AI Confidence: **99.32%**
3638. **`crypto/krb5/src/util/verto/ev_select.c`** -> AI Confidence: **99.32%**
3639. **`crypto/libecc/include/libecc/ecdh/x25519_448.h`** -> AI Confidence: **99.32%**
3640. **`crypto/libecc/include/libecc/utils/utils.h`** -> AI Confidence: **99.32%**
3641. **`crypto/libecc/src/examples/basic/curve_basic_examples.c`** -> AI Confidence: **99.32%**
3642. **`crypto/libecc/src/examples/sss/sss.c`** -> AI Confidence: **99.32%**
3643. **`crypto/libecc/src/fp/fp_sqrt.c`** -> AI Confidence: **99.32%**
3644. **`crypto/libecc/src/hash/bash.c`** -> AI Confidence: **99.32%**
3645. **`crypto/libecc/src/hash/sha3.c`** -> AI Confidence: **99.32%**
3646. **`crypto/openssh/openbsd-compat/bsd-flock.c`** -> AI Confidence: **99.32%**
3647. **`crypto/openssh/openbsd-compat/strlcpy.c`** -> AI Confidence: **99.32%**
3648. **`crypto/openssh/openbsd-compat/strnlen.c`** -> AI Confidence: **99.32%**
3649. **`crypto/openssh/openbsd-compat/strsep.c`** -> AI Confidence: **99.32%**
3650. **`crypto/openssl/apps/info.c`** -> AI Confidence: **99.32%**
3651. **`crypto/openssl/crypto/bf/bf_cfb64.c`** -> AI Confidence: **99.32%**
3652. **`crypto/openssl/crypto/bio/bss_acpt.c`** -> AI Confidence: **99.32%**
3653. **`crypto/openssl/crypto/bn/bn_conv.c`** -> AI Confidence: **99.32%**
3654. **`crypto/openssl/crypto/bn/bn_exp2.c`** -> AI Confidence: **99.32%**
3655. **`crypto/openssl/crypto/bn/bn_gcd.c`** -> AI Confidence: **99.32%**
3656. **`crypto/openssl/crypto/bn/bn_mul.c`** -> AI Confidence: **99.32%**
3657. **`crypto/openssl/crypto/bn/bn_x931p.c`** -> AI Confidence: **99.32%**
3658. **`crypto/openssl/crypto/cast/c_cfb64.c`** -> AI Confidence: **99.32%**
3659. **`crypto/openssl/crypto/des/str2key.c`** -> AI Confidence: **99.32%**
3660. **`crypto/openssl/crypto/dllmain.c`** -> AI Confidence: **99.32%**
3661. **`crypto/openssl/crypto/ec/ec2_oct.c`** -> AI Confidence: **99.32%**
3662. **`crypto/openssl/crypto/ec/ec_check.c`** -> AI Confidence: **99.32%**
3663. **`crypto/openssl/crypto/engine/eng_cnf.c`** -> AI Confidence: **99.32%**
3664. **`crypto/openssl/crypto/ffc/ffc_backend.c`** -> AI Confidence: **99.32%**
3665. **`crypto/openssl/crypto/getenv.c`** -> AI Confidence: **99.32%**
3666. **`crypto/openssl/crypto/idea/i_skey.c`** -> AI Confidence: **99.32%**
3667. **`crypto/openssl/crypto/modes/cbc128.c`** -> AI Confidence: **99.32%**
3668. **`crypto/openssl/crypto/rc2/rc2_cbc.c`** -> AI Confidence: **99.32%**
3669. **`crypto/openssl/crypto/rc2/rc2_skey.c`** -> AI Confidence: **99.32%**
3670. **`crypto/openssl/crypto/rc2/rc2cfb64.c`** -> AI Confidence: **99.32%**
3671. **`crypto/openssl/crypto/rc4/rc4_enc.c`** -> AI Confidence: **99.32%**
3672. **`crypto/openssl/crypto/rc5/rc5_skey.c`** -> AI Confidence: **99.32%**
3673. **`crypto/openssl/crypto/rc5/rc5cfb64.c`** -> AI Confidence: **99.32%**
3674. **`crypto/openssl/demos/bio/client-arg.c`** -> AI Confidence: **99.32%**
3675. **`crypto/openssl/demos/cms/cms_comp.c`** -> AI Confidence: **99.32%**
3676. **`crypto/openssl/demos/cms/cms_ddec.c`** -> AI Confidence: **99.32%**
3677. **`crypto/openssl/demos/cms/cms_dec.c`** -> AI Confidence: **99.32%**
3678. **`crypto/openssl/demos/cms/cms_denc.c`** -> AI Confidence: **99.32%**
3679. **`crypto/openssl/demos/cms/cms_enc.c`** -> AI Confidence: **99.32%**
3680. **`crypto/openssl/demos/cms/cms_sign.c`** -> AI Confidence: **99.32%**
3681. **`crypto/openssl/demos/cms/cms_sign2.c`** -> AI Confidence: **99.32%**
3682. **`crypto/openssl/demos/cms/cms_uncomp.c`** -> AI Confidence: **99.32%**
3683. **`crypto/openssl/demos/cms/cms_ver.c`** -> AI Confidence: **99.32%**
3684. **`crypto/openssl/demos/smime/smdec.c`** -> AI Confidence: **99.32%**
3685. **`crypto/openssl/demos/smime/smenc.c`** -> AI Confidence: **99.32%**
3686. **`crypto/openssl/demos/smime/smsign.c`** -> AI Confidence: **99.32%**
3687. **`crypto/openssl/demos/smime/smsign2.c`** -> AI Confidence: **99.32%**
3688. **`crypto/openssl/demos/smime/smver.c`** -> AI Confidence: **99.32%**
3689. **`crypto/openssl/include/crypto/sm2.h`** -> AI Confidence: **99.32%**
3690. **`crypto/openssl/providers/common/der/der_ml_dsa_key.c`** -> AI Confidence: **99.32%**
3691. **`crypto/openssl/providers/implementations/ciphers/cipher_sm4_ccm_hw.c`** -> AI Confidence: **99.32%**
3692. **`include/limits.h`** -> AI Confidence: **99.32%**
3693. **`lib/msun/src/e_fmod.c`** -> AI Confidence: **99.32%**
3694. **`lib/msun/src/e_lgamma_r.c`** -> AI Confidence: **99.32%**
3695. **`lib/msun/src/e_remainder.c`** -> AI Confidence: **99.32%**
3696. **`lib/msun/src/e_sqrt.c`** -> AI Confidence: **99.32%**
3697. **`lib/msun/src/k_rem_pio2.c`** -> AI Confidence: **99.32%**
3698. **`lib/msun/src/math.h`** -> AI Confidence: **99.32%**
3699. **`lib/msun/src/s_ceil.c`** -> AI Confidence: **99.32%**
3700. **`lib/msun/src/s_floor.c`** -> AI Confidence: **99.32%**
3701. **`lib/msun/src/s_frexpl.c`** -> AI Confidence: **99.32%**
3702. **`lib/msun/src/s_nextafter.c`** -> AI Confidence: **99.32%**
3703. **`lib/msun/src/s_remquo.c`** -> AI Confidence: **99.32%**
3704. **`lib/msun/src/s_scalbn.c`** -> AI Confidence: **99.32%**
3705. **`lib/msun/src/s_tanpi.c`** -> AI Confidence: **99.32%**
3706. **`sbin/ipf/libipf/interror.c`** -> AI Confidence: **99.32%**
3707. **`sbin/ipf/libipf/ipft_hx.c`** -> AI Confidence: **99.32%**
3708. **`sbin/ipf/libipf/printhash_live.c`** -> AI Confidence: **99.32%**
3709. **`sbin/ipf/libipf/printpool_live.c`** -> AI Confidence: **99.32%**
3710. **`share/doc/psd/20.ipctut/socketpair.c`** -> AI Confidence: **99.32%**
3711. **`stand/common/commands.c`** -> AI Confidence: **99.32%**
3712. **`stand/common/interp_backslash.c`** -> AI Confidence: **99.32%**
3713. **`stand/common/self_reloc.c`** -> AI Confidence: **99.32%**
3714. **`stand/libsa/in_cksum.c`** -> AI Confidence: **99.32%**
3715. **`sys/cddl/contrib/opensolaris/uts/common/sys/bitmap.h`** -> AI Confidence: **99.32%**
3716. **`sys/cddl/dev/fbt/aarch64/fbt_isa.c`** -> AI Confidence: **99.32%**
3717. **`sys/compat/linuxkpi/common/include/asm/byteorder.h`** -> AI Confidence: **99.32%**
3718. **`sys/compat/linuxkpi/common/include/linux/sort.h`** -> AI Confidence: **99.32%**
3719. **`sys/contrib/dev/acpica/common/ahuuids.c`** -> AI Confidence: **99.32%**
3720. **`sys/contrib/dev/acpica/common/getopt.c`** -> AI Confidence: **99.32%**
3721. **`sys/contrib/dev/acpica/compiler/aslnamesp.c`** -> AI Confidence: **99.32%**
3722. **`sys/contrib/dev/acpica/compiler/asloperands.c`** -> AI Confidence: **99.32%**
3723. **`sys/contrib/dev/acpica/compiler/aslpld.c`** -> AI Confidence: **99.32%**
3724. **`sys/contrib/dev/acpica/compiler/aslprepkg.c`** -> AI Confidence: **99.32%**
3725. **`sys/contrib/dev/acpica/compiler/aslresource.c`** -> AI Confidence: **99.32%**
3726. **`sys/contrib/dev/acpica/compiler/aslrestype2.c`** -> AI Confidence: **99.32%**
3727. **`sys/contrib/dev/acpica/compiler/aslrestype2s.c`** -> AI Confidence: **99.32%**
3728. **`sys/contrib/dev/acpica/compiler/asltree.c`** -> AI Confidence: **99.32%**
3729. **`sys/contrib/dev/acpica/components/dispatcher/dswscope.c`** -> AI Confidence: **99.32%**
3730. **`sys/contrib/dev/acpica/components/events/evgpeutil.c`** -> AI Confidence: **99.32%**
3731. **`sys/contrib/dev/acpica/components/events/evxfevnt.c`** -> AI Confidence: **99.32%**
3732. **`sys/contrib/dev/acpica/components/executer/exdebug.c`** -> AI Confidence: **99.32%**
3733. **`sys/contrib/dev/acpica/components/executer/exstorob.c`** -> AI Confidence: **99.32%**
3734. **`sys/contrib/dev/acpica/components/hardware/hwregs.c`** -> AI Confidence: **99.32%**
3735. **`sys/contrib/dev/acpica/components/hardware/hwxface.c`** -> AI Confidence: **99.32%**
3736. **`sys/contrib/dev/acpica/components/namespace/nsobject.c`** -> AI Confidence: **99.32%**
3737. **`sys/contrib/dev/acpica/components/namespace/nswalk.c`** -> AI Confidence: **99.32%**
3738. **`sys/contrib/dev/acpica/components/resources/rsinfo.c`** -> AI Confidence: **99.32%**
3739. **`sys/contrib/dev/acpica/components/resources/rslist.c`** -> AI Confidence: **99.32%**
3740. **`sys/contrib/dev/acpica/components/resources/rsmisc.c`** -> AI Confidence: **99.32%**
3741. **`sys/contrib/dev/acpica/components/tables/tbfind.c`** -> AI Confidence: **99.32%**
3742. **`sys/contrib/dev/acpica/components/utilities/utaddress.c`** -> AI Confidence: **99.32%**
3743. **`sys/contrib/dev/acpica/components/utilities/utcopy.c`** -> AI Confidence: **99.32%**
3744. **`sys/contrib/dev/acpica/components/utilities/uteval.c`** -> AI Confidence: **99.32%**
3745. **`sys/contrib/dev/acpica/components/utilities/utids.c`** -> AI Confidence: **99.32%**
3746. **`sys/contrib/dev/acpica/components/utilities/utobject.c`** -> AI Confidence: **99.32%**
3747. **`sys/contrib/dev/acpica/components/utilities/utownerid.c`** -> AI Confidence: **99.32%**
3748. **`sys/contrib/dev/acpica/components/utilities/utresdecode.c`** -> AI Confidence: **99.32%**
3749. **`sys/contrib/dev/acpica/components/utilities/utstring.c`** -> AI Confidence: **99.32%**
3750. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-ba10-tvbox.dts`** -> AI Confidence: **99.32%**
3751. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-hackberry.dts`** -> AI Confidence: **99.32%**
3752. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-hyundai-a7hd.dts`** -> AI Confidence: **99.32%**
3753. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-jesurun-q5.dts`** -> AI Confidence: **99.32%**
3754. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-marsboard.dts`** -> AI Confidence: **99.32%**
3755. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-mini-xplus.dts`** -> AI Confidence: **99.32%**
3756. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-mk802.dts`** -> AI Confidence: **99.32%**
3757. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-mk802ii.dts`** -> AI Confidence: **99.32%**
3758. **`sys/contrib/device-tree/src/arm/allwinner/sun4i-a10-olinuxino-lime.dts`** -> AI Confidence: **99.32%**
3759. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-a10s-auxtek-t003.dts`** -> AI Confidence: **99.32%**
3760. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-a10s-auxtek-t004.dts`** -> AI Confidence: **99.32%**
3761. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-a10s-mk802.dts`** -> AI Confidence: **99.32%**
3762. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-a10s-r7-tv-dongle.dts`** -> AI Confidence: **99.32%**
3763. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-a13-olinuxino-micro.dts`** -> AI Confidence: **99.32%**
3764. **`sys/contrib/device-tree/src/arm/allwinner/sun5i-a13-utoo-p66.dts`** -> AI Confidence: **99.32%**
3765. **`sys/contrib/device-tree/src/arm/allwinner/sun6i-a31-app4-evb1.dts`** -> AI Confidence: **99.32%**
3766. **`sys/contrib/device-tree/src/arm/allwinner/sun6i-a31-colombus.dts`** -> AI Confidence: **99.32%**
3767. **`sys/contrib/device-tree/src/arm/allwinner/sun6i-a31-i7.dts`** -> AI Confidence: **99.32%**
3768. **`sys/contrib/device-tree/src/arm/allwinner/sun6i-a31s-sinovoip-bpi-m2.dts`** -> AI Confidence: **99.32%**
3769. **`sys/contrib/device-tree/src/arm/allwinner/sun7i-a20-icnova-a20-adb4006.dts`** -> AI Confidence: **99.32%**
3770. **`sys/contrib/device-tree/src/arm/allwinner/sun8i-a33-vstar.dts`** -> AI Confidence: **99.32%**
3771. **`sys/contrib/device-tree/src/arm/allwinner/sun8i-a83t-allwinner-h8homlet-v2.dts`** -> AI Confidence: **99.32%**
3772. **`sys/contrib/device-tree/src/arm/allwinner/sun8i-a83t-bananapi-m3.dts`** -> AI Confidence: **99.32%**
3773. **`sys/contrib/device-tree/src/arm/allwinner/sun8i-a83t-cubietruck-plus.dts`** -> AI Confidence: **99.32%**
3774. **`sys/contrib/device-tree/src/arm/allwinner/sun8i-h3-nanopi-neo-air.dts`** -> AI Confidence: **99.32%**
3775. **`sys/contrib/device-tree/src/arm/allwinner/sun8i-r16-bananapi-m2m.dts`** -> AI Confidence: **99.32%**
3776. **`sys/contrib/device-tree/src/arm/allwinner/sun8i-r40-feta40i.dtsi`** -> AI Confidence: **99.32%**
3777. **`sys/contrib/device-tree/src/arm/allwinner/sun8i-r40-oka40i-c.dts`** -> AI Confidence: **99.32%**
3778. **`sys/contrib/device-tree/src/arm/allwinner/sun9i-a80-cubieboard4.dts`** -> AI Confidence: **99.32%**
3779. **`sys/contrib/device-tree/src/arm/allwinner/sun9i-a80-optimus.dts`** -> AI Confidence: **99.32%**
3780. **`sys/contrib/device-tree/src/arm/allwinner/suniv-f1c200s-popstick-v1.1.dts`** -> AI Confidence: **99.32%**
3781. **`sys/contrib/device-tree/src/arm/amlogic/meson8b-ec100.dts`** -> AI Confidence: **99.32%**
3782. **`sys/contrib/device-tree/src/arm/amlogic/meson8m2-mxiii-plus.dts`** -> AI Confidence: **99.32%**
3783. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-ast2600-evb.dts`** -> AI Confidence: **99.32%**
3784. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-arm-stardragon4800-rep2.dts`** -> AI Confidence: **99.32%**
3785. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-delta-ahe50dc.dts`** -> AI Confidence: **99.32%**
3786. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-facebook-wedge400.dts`** -> AI Confidence: **99.32%**
3787. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-facebook-yosemitev2.dts`** -> AI Confidence: **99.32%**
3788. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-inspur-on5263m5.dts`** -> AI Confidence: **99.32%**
3789. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-lenovo-hr630.dts`** -> AI Confidence: **99.32%**
3790. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-lenovo-hr855xg2.dts`** -> AI Confidence: **99.32%**
3791. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-microsoft-olympus.dts`** -> AI Confidence: **99.32%**
3792. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-opp-palmetto.dts`** -> AI Confidence: **99.32%**
3793. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-opp-vesnin.dts`** -> AI Confidence: **99.32%**
3794. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-portwell-neptune.dts`** -> AI Confidence: **99.32%**
3795. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-qcom-dc-scm-v1.dts`** -> AI Confidence: **99.32%**
3796. **`sys/contrib/device-tree/src/arm/aspeed/aspeed-bmc-quanta-q71l.dts`** -> AI Confidence: **99.32%**
3797. **`sys/contrib/device-tree/src/arm/broadcom/bcm2711-rpi-cm4.dtsi`** -> AI Confidence: **99.32%**
3798. **`sys/contrib/device-tree/src/arm/broadcom/bcm4709-asus-rt-ac3200.dts`** -> AI Confidence: **99.32%**
3799. **`sys/contrib/device-tree/src/arm/broadcom/bcm47094-asus-rt-ac5300.dts`** -> AI Confidence: **99.32%**
3800. **`sys/contrib/device-tree/src/arm/broadcom/bcm53015-meraki-mr26.dts`** -> AI Confidence: **99.32%**
3801. **`sys/contrib/device-tree/src/arm/broadcom/bcm53016-meraki-mr32.dts`** -> AI Confidence: **99.32%**
3802. **`sys/contrib/device-tree/src/arm/gemini/gemini-dlink-dns-313.dts`** -> AI Confidence: **99.32%**
3803. **`sys/contrib/device-tree/src/arm/marvell/armada-370-dlink-dns327l.dts`** -> AI Confidence: **99.32%**
3804. **`sys/contrib/device-tree/src/arm/marvell/armada-370-netgear-rn102.dts`** -> AI Confidence: **99.32%**
3805. **`sys/contrib/device-tree/src/arm/marvell/armada-370-netgear-rn104.dts`** -> AI Confidence: **99.32%**
3806. **`sys/contrib/device-tree/src/arm/marvell/armada-370-synology-ds213j.dts`** -> AI Confidence: **99.32%**
3807. **`sys/contrib/device-tree/src/arm/marvell/armada-381-netgear-gs110emx.dts`** -> AI Confidence: **99.32%**
3808. **`sys/contrib/device-tree/src/arm/marvell/armada-385-linksys-rango.dts`** -> AI Confidence: **99.32%**
3809. **`sys/contrib/device-tree/src/arm/marvell/armada-xp-axpwifiap.dts`** -> AI Confidence: **99.32%**
3810. **`sys/contrib/device-tree/src/arm/marvell/armada-xp-lenovo-ix4-300d.dts`** -> AI Confidence: **99.32%**
3811. **`sys/contrib/device-tree/src/arm/marvell/armada-xp-linksys-mamba.dts`** -> AI Confidence: **99.32%**
3812. **`sys/contrib/device-tree/src/arm/marvell/armada-xp-netgear-rn2120.dts`** -> AI Confidence: **99.32%**
3813. **`sys/contrib/device-tree/src/arm/marvell/armada-xp-openblocks-ax3-4.dts`** -> AI Confidence: **99.32%**
3814. **`sys/contrib/device-tree/src/arm/marvell/kirkwood-4i-edge-200.dts`** -> AI Confidence: **99.32%**
3815. **`sys/contrib/device-tree/src/arm/marvell/kirkwood-c200-v1.dts`** -> AI Confidence: **99.32%**
3816. **`sys/contrib/device-tree/src/arm/marvell/kirkwood-nsa310s.dts`** -> AI Confidence: **99.32%**
3817. **`sys/contrib/device-tree/src/arm/marvell/kirkwood-pogoplug-series-4.dts`** -> AI Confidence: **99.32%**
3818. **`sys/contrib/device-tree/src/arm/marvell/kirkwood-ts219-6281.dts`** -> AI Confidence: **99.32%**
3819. **`sys/contrib/device-tree/src/arm/marvell/kirkwood-ts219-6282.dts`** -> AI Confidence: **99.32%**
3820. **`sys/contrib/device-tree/src/arm/marvell/orion5x-netgear-wnr854t.dts`** -> AI Confidence: **99.32%**
3821. **`sys/contrib/device-tree/src/arm/mediatek/mt7623a-rfb-emmc.dts`** -> AI Confidence: **99.32%**
3822. **`sys/contrib/device-tree/src/arm/mediatek/mt7623a-rfb-nand.dts`** -> AI Confidence: **99.32%**
3823. **`sys/contrib/device-tree/src/arm/mediatek/mt7623n-bananapi-bpi-r2.dts`** -> AI Confidence: **99.32%**
3824. **`sys/contrib/device-tree/src/arm/mediatek/mt7623n-rfb-emmc.dts`** -> AI Confidence: **99.32%**
3825. **`sys/contrib/device-tree/src/arm/microchip/at91-sama5d27_som1.dtsi`** -> AI Confidence: **99.32%**
3826. **`sys/contrib/device-tree/src/arm/microchip/at91sam9g25-gardena-smart-gateway.dts`** -> AI Confidence: **99.32%**
3827. **`sys/contrib/device-tree/src/arm/nuvoton/nuvoton-npcm730-gsj.dts`** -> AI Confidence: **99.32%**
3828. **`sys/contrib/device-tree/src/arm/nuvoton/nuvoton-npcm750-evb.dts`** -> AI Confidence: **99.32%**
3829. **`sys/contrib/device-tree/src/arm/nuvoton/nuvoton-wpcm450-supermicro-x9sci-ln4f.dts`** -> AI Confidence: **99.32%**
3830. **`sys/contrib/device-tree/src/arm/nvidia/tegra114-asus-tf701t.dts`** -> AI Confidence: **99.32%**
3831. **`sys/contrib/device-tree/src/arm/nvidia/tegra124-jetson-tk1.dts`** -> AI Confidence: **99.32%**
3832. **`sys/contrib/device-tree/src/arm/nvidia/tegra124-venice2.dts`** -> AI Confidence: **99.32%**
3833. **`sys/contrib/device-tree/src/arm/nvidia/tegra30-beaver.dts`** -> AI Confidence: **99.32%**
3834. **`sys/contrib/device-tree/src/arm/nxp/imx/imx25-pdk.dts`** -> AI Confidence: **99.32%**
3835. **`sys/contrib/device-tree/src/arm/nxp/imx/imx35-eukrea-mbimxsd35-baseboard.dts`** -> AI Confidence: **99.32%**
3836. **`sys/contrib/device-tree/src/arm/nxp/imx/imx50-kobo-aura.dts`** -> AI Confidence: **99.32%**
3837. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6dl-lanmcu.dts`** -> AI Confidence: **99.32%**
3838. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6dl-plybas.dts`** -> AI Confidence: **99.32%**
3839. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6dl-plym2m.dts`** -> AI Confidence: **99.32%**
3840. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6dl-prtrvt.dts`** -> AI Confidence: **99.32%**
3841. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6dl-skov-revc-lt6.dts`** -> AI Confidence: **99.32%**
3842. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6dl-tx6s-8035.dts`** -> AI Confidence: **99.32%**
3843. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6dl-tx6u-8033.dts`** -> AI Confidence: **99.32%**
3844. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-bosch-acc.dts`** -> AI Confidence: **99.32%**
3845. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-cm-fx6.dts`** -> AI Confidence: **99.32%**
3846. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-evi.dts`** -> AI Confidence: **99.32%**
3847. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-gk802.dts`** -> AI Confidence: **99.32%**
3848. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-gw54xx.dts`** -> AI Confidence: **99.32%**
3849. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-h100.dts`** -> AI Confidence: **99.32%**
3850. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-logicpd.dts`** -> AI Confidence: **99.32%**
3851. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-mccmon6.dts`** -> AI Confidence: **99.32%**
3852. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-novena.dts`** -> AI Confidence: **99.32%**
3853. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-pistachio.dts`** -> AI Confidence: **99.32%**
3854. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-prtwd2.dts`** -> AI Confidence: **99.32%**
3855. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-skov-revc-lt6.dts`** -> AI Confidence: **99.32%**
3856. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-tbs2910.dts`** -> AI Confidence: **99.32%**
3857. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-tx6q-1020-comtft.dts`** -> AI Confidence: **99.32%**
3858. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-tx6q-1020.dts`** -> AI Confidence: **99.32%**
3859. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-tx6q-1036.dts`** -> AI Confidence: **99.32%**
3860. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6q-var-dt6customboard.dts`** -> AI Confidence: **99.32%**
3861. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6qdl-ds.dtsi`** -> AI Confidence: **99.32%**
3862. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6qp-tx6qp-8037.dts`** -> AI Confidence: **99.32%**
3863. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6qp-tx6qp-8137.dts`** -> AI Confidence: **99.32%**
3864. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6sl-evk.dts`** -> AI Confidence: **99.32%**
3865. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6sl-tolino-shine2hd.dts`** -> AI Confidence: **99.32%**
3866. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6sll-evk.dts`** -> AI Confidence: **99.32%**
3867. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6sx-softing-vining-2000.dts`** -> AI Confidence: **99.32%**
3868. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6ul-geam.dts`** -> AI Confidence: **99.32%**
3869. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6ul-tqma6ul1-mba6ulx.dts`** -> AI Confidence: **99.32%**
3870. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6ul-var-som.dtsi`** -> AI Confidence: **99.32%**
3871. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6ull-jozacp.dts`** -> AI Confidence: **99.32%**
3872. **`sys/contrib/device-tree/src/arm/nxp/imx/imx6ull-myir-mys-6ulx.dtsi`** -> AI Confidence: **99.32%**
3873. **`sys/contrib/device-tree/src/arm/nxp/lpc/lpc4337-ciaa.dts`** -> AI Confidence: **99.32%**
3874. **`sys/contrib/device-tree/src/arm/nxp/lpc/lpc4357-myd-lpc4357.dts`** -> AI Confidence: **99.32%**
3875. **`sys/contrib/device-tree/src/arm/nxp/ls/ls1021a-moxa-uc-8410a.dts`** -> AI Confidence: **99.32%**
3876. **`sys/contrib/device-tree/src/arm/nxp/mxs/imx28-amarula-rmm.dts`** -> AI Confidence: **99.32%**
3877. **`sys/contrib/device-tree/src/arm/nxp/mxs/imx28-tx28.dts`** -> AI Confidence: **99.32%**
3878. **`sys/contrib/device-tree/src/arm/qcom/qcom-apq8026-huawei-sturgeon.dts`** -> AI Confidence: **99.32%**
3879. **`sys/contrib/device-tree/src/arm/qcom/qcom-ipq4018-jalapeno.dts`** -> AI Confidence: **99.32%**
3880. **`sys/contrib/device-tree/src/arm/qcom/qcom-ipq8064-rb3011.dts`** -> AI Confidence: **99.32%**
3881. **`sys/contrib/device-tree/src/arm/qcom/qcom-ipq8064-v1.0.dtsi`** -> AI Confidence: **99.32%**
3882. **`sys/contrib/device-tree/src/arm/qcom/qcom-msm8960-cdp.dts`** -> AI Confidence: **99.32%**
3883. **`sys/contrib/device-tree/src/arm/renesas/gr-peach-audiocamerashield.dtsi`** -> AI Confidence: **99.32%**
3884. **`sys/contrib/device-tree/src/arm/renesas/r7s72100-gr-peach.dts`** -> AI Confidence: **99.32%**
3885. **`sys/contrib/device-tree/src/arm/renesas/r8a73a4-ape6evm.dts`** -> AI Confidence: **99.32%**
3886. **`sys/contrib/device-tree/src/arm/renesas/r8a7742-iwg21d-q7-dbcm-ca.dts`** -> AI Confidence: **99.32%**
3887. **`sys/contrib/device-tree/src/arm/renesas/r8a7778-bockw.dts`** -> AI Confidence: **99.32%**
3888. **`sys/contrib/device-tree/src/arm/renesas/r8a7790-lager.dts`** -> AI Confidence: **99.32%**
3889. **`sys/contrib/device-tree/src/arm/renesas/r8a7790-stout.dts`** -> AI Confidence: **99.32%**
3890. **`sys/contrib/device-tree/src/arm/renesas/r8a7791-koelsch.dts`** -> AI Confidence: **99.32%**
3891. **`sys/contrib/device-tree/src/arm/renesas/r8a7792-blanche.dts`** -> AI Confidence: **99.32%**
3892. **`sys/contrib/device-tree/src/arm/renesas/r8a7792-wheat.dts`** -> AI Confidence: **99.32%**
3893. **`sys/contrib/device-tree/src/arm/renesas/r8a7793-gose.dts`** -> AI Confidence: **99.32%**
3894. **`sys/contrib/device-tree/src/arm/renesas/r8a7794-alt.dts`** -> AI Confidence: **99.32%**
3895. **`sys/contrib/device-tree/src/arm/renesas/r8a7794-silk.dts`** -> AI Confidence: **99.32%**
3896. **`sys/contrib/device-tree/src/arm/rockchip/rk3066a-bqcurie2.dts`** -> AI Confidence: **99.32%**
3897. **`sys/contrib/device-tree/src/arm/rockchip/rk3066a-rayeager.dts`** -> AI Confidence: **99.32%**
3898. **`sys/contrib/device-tree/src/arm/rockchip/rk3128-xpi-3128.dts`** -> AI Confidence: **99.32%**
3899. **`sys/contrib/device-tree/src/arm/rockchip/rk3288-phycore-rdk.dts`** -> AI Confidence: **99.32%**
3900. **`sys/contrib/device-tree/src/arm/rockchip/rk3288-r89.dts`** -> AI Confidence: **99.32%**
3901. **`sys/contrib/device-tree/src/arm/rockchip/rk3288-veyron-speedy.dts`** -> AI Confidence: **99.32%**
3902. **`sys/contrib/device-tree/src/arm/rockchip/rv1109-relfor-saib.dts`** -> AI Confidence: **99.32%**
3903. **`sys/contrib/device-tree/src/arm/samsung/exynos4210-smdkv310.dts`** -> AI Confidence: **99.32%**
3904. **`sys/contrib/device-tree/src/arm/samsung/exynos4412-odroidu3.dts`** -> AI Confidence: **99.32%**
3905. **`sys/contrib/device-tree/src/arm/samsung/exynos4412-tiny4412.dts`** -> AI Confidence: **99.32%**
3906. **`sys/contrib/device-tree/src/arm/samsung/exynos5422-odroidxu3-lite.dts`** -> AI Confidence: **99.32%**
3907. **`sys/contrib/device-tree/src/arm/samsung/exynos5422-odroidxu3.dts`** -> AI Confidence: **99.32%**
3908. **`sys/contrib/device-tree/src/arm/samsung/exynos5422-odroidxu4.dts`** -> AI Confidence: **99.32%**
3909. **`sys/contrib/device-tree/src/arm/samsung/s3c6410-mini6410.dts`** -> AI Confidence: **99.32%**
3910. **`sys/contrib/device-tree/src/arm/samsung/s3c6410-smdk6410.dts`** -> AI Confidence: **99.32%**
3911. **`sys/contrib/device-tree/src/arm/samsung/s5pv210-aquila.dts`** -> AI Confidence: **99.32%**
3912. **`sys/contrib/device-tree/src/arm/samsung/s5pv210-fascinate4g.dts`** -> AI Confidence: **99.32%**
3913. **`sys/contrib/device-tree/src/arm/samsung/s5pv210-galaxys.dts`** -> AI Confidence: **99.32%**
3914. **`sys/contrib/device-tree/src/arm/samsung/s5pv210-smdkv210.dts`** -> AI Confidence: **99.32%**
3915. **`sys/contrib/device-tree/src/arm/socionext/uniphier-ld4.dtsi`** -> AI Confidence: **99.32%**
3916. **`sys/contrib/device-tree/src/arm/socionext/uniphier-sld8.dtsi`** -> AI Confidence: **99.32%**
3917. **`sys/contrib/device-tree/src/arm/st/ste-nomadik-nhk15.dts`** -> AI Confidence: **99.32%**
3918. **`sys/contrib/device-tree/src/arm/st/ste-snowball.dts`** -> AI Confidence: **99.32%**
3919. **`sys/contrib/device-tree/src/arm/st/stm32mp157a-dhcor-avenger96.dts`** -> AI Confidence: **99.32%**
3920. **`sys/contrib/device-tree/src/arm/ti/davinci/da850-lcdk.dts`** -> AI Confidence: **99.32%**
3921. **`sys/contrib/device-tree/src/arm/ti/omap/am335x-boneblue.dts`** -> AI Confidence: **99.32%**
3922. **`sys/contrib/device-tree/src/arm/ti/omap/am335x-evm.dts`** -> AI Confidence: **99.32%**
3923. **`sys/contrib/device-tree/src/arm/ti/omap/am335x-igep0033.dtsi`** -> AI Confidence: **99.32%**
3924. **`sys/contrib/device-tree/src/arm/ti/omap/am335x-myirtech-myc.dtsi`** -> AI Confidence: **99.32%**
3925. **`sys/contrib/device-tree/src/arm/ti/omap/am335x-myirtech-myd.dts`** -> AI Confidence: **99.32%**
3926. **`sys/contrib/device-tree/src/arm/ti/omap/am335x-pocketbeagle.dts`** -> AI Confidence: **99.32%**
3927. **`sys/contrib/device-tree/src/arm/ti/omap/am57xx-cl-som-am57x.dts`** -> AI Confidence: **99.32%**
3928. **`sys/contrib/device-tree/src/arm/ti/omap/dra7-evm.dts`** -> AI Confidence: **99.32%**
3929. **`sys/contrib/device-tree/src/arm/ti/omap/dra72-evm.dts`** -> AI Confidence: **99.32%**
3930. **`sys/contrib/device-tree/src/arm/ti/omap/omap3-beagle-xm.dts`** -> AI Confidence: **99.32%**
3931. **`sys/contrib/device-tree/src/arm/ti/omap/omap3-beagle.dts`** -> AI Confidence: **99.32%**
3932. **`sys/contrib/device-tree/src/arm/ti/omap/omap3-evm-37xx.dts`** -> AI Confidence: **99.32%**
3933. **`sys/contrib/device-tree/src/arm/ti/omap/omap3-evm.dts`** -> AI Confidence: **99.32%**
3934. **`sys/contrib/device-tree/src/arm/ti/omap/omap3-lilly-a83x.dtsi`** -> AI Confidence: **99.32%**
3935. **`sys/contrib/device-tree/src/arm/ti/omap/omap3-zoom3.dts`** -> AI Confidence: **99.32%**
3936. **`sys/contrib/device-tree/src/arm/ti/omap/omap4-duovero-parlor.dts`** -> AI Confidence: **99.32%**
3937. **`sys/contrib/device-tree/src/arm/ti/omap/omap4-kc1.dts`** -> AI Confidence: **99.32%**
3938. **`sys/contrib/device-tree/src/arm/ti/omap/omap4-var-dvk-om44.dts`** -> AI Confidence: **99.32%**
3939. **`sys/contrib/device-tree/src/arm/ti/omap/omap5-cm-t54.dts`** -> AI Confidence: **99.32%**
3940. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-h5-orangepi-prime.dts`** -> AI Confidence: **99.32%**
3941. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-h6-orangepi-3.dts`** -> AI Confidence: **99.32%**
3942. **`sys/contrib/device-tree/src/arm64/allwinner/sun50i-h6-pine-h64.dts`** -> AI Confidence: **99.32%**
3943. **`sys/contrib/device-tree/src/arm64/allwinner/sun55i-t527-orangepi-4a.dts`** -> AI Confidence: **99.32%**
3944. **`sys/contrib/device-tree/src/arm64/amlogic/meson-g12a-radxa-zero.dts`** -> AI Confidence: **99.32%**
3945. **`sys/contrib/device-tree/src/arm64/amlogic/meson-g12b-gsking-x.dts`** -> AI Confidence: **99.32%**
3946. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxbb-nanopi-k2.dts`** -> AI Confidence: **99.32%**
3947. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxbb-odroidc2.dts`** -> AI Confidence: **99.32%**
3948. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxbb-p200.dts`** -> AI Confidence: **99.32%**
3949. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxbb-wetek-play2.dts`** -> AI Confidence: **99.32%**
3950. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxl-s805x-libretech-ac.dts`** -> AI Confidence: **99.32%**
3951. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxl-s805x-p241.dts`** -> AI Confidence: **99.32%**
3952. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxl-s905d-p230.dts`** -> AI Confidence: **99.32%**
3953. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxl-s905d-sml5442tw.dts`** -> AI Confidence: **99.32%**
3954. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxl-s905x-khadas-vim.dts`** -> AI Confidence: **99.32%**
3955. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxl-s905x-libretech-cc.dts`** -> AI Confidence: **99.32%**
3956. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxm-khadas-vim2.dts`** -> AI Confidence: **99.32%**
3957. **`sys/contrib/device-tree/src/arm64/amlogic/meson-gxm-q200.dts`** -> AI Confidence: **99.32%**
3958. **`sys/contrib/device-tree/src/arm64/amlogic/meson-sm1-khadas-vim3l.dts`** -> AI Confidence: **99.32%**
3959. **`sys/contrib/device-tree/src/arm64/apple/t8103-j293.dts`** -> AI Confidence: **99.32%**
3960. **`sys/contrib/device-tree/src/arm64/apple/t8103-j313.dts`** -> AI Confidence: **99.32%**
3961. **`sys/contrib/device-tree/src/arm64/apple/t8112-j413.dts`** -> AI Confidence: **99.32%**
3962. **`sys/contrib/device-tree/src/arm64/apple/t8112-j493.dts`** -> AI Confidence: **99.32%**
3963. **`sys/contrib/device-tree/src/arm64/exynos/exynos9810-starlte.dts`** -> AI Confidence: **99.32%**
3964. **`sys/contrib/device-tree/src/arm64/exynos/exynosautov9-sadk.dts`** -> AI Confidence: **99.32%**
3965. **`sys/contrib/device-tree/src/arm64/freescale/imx8mm-beacon-kit.dts`** -> AI Confidence: **99.32%**
3966. **`sys/contrib/device-tree/src/arm64/freescale/imx8mm-data-modul-edm-sbc.dts`** -> AI Confidence: **99.32%**
3967. **`sys/contrib/device-tree/src/arm64/freescale/imx8mm-kontron-osm-s.dtsi`** -> AI Confidence: **99.32%**
3968. **`sys/contrib/device-tree/src/arm64/freescale/imx8mm-tqma8mqml-mba8mx.dts`** -> AI Confidence: **99.32%**
3969. **`sys/contrib/device-tree/src/arm64/freescale/imx8mm-venice-gw71xx.dtsi`** -> AI Confidence: **99.32%**
3970. **`sys/contrib/device-tree/src/arm64/freescale/imx8mm-venice-gw72xx.dtsi`** -> AI Confidence: **99.32%**
3971. **`sys/contrib/device-tree/src/arm64/freescale/imx8mm-venice-gw73xx.dtsi`** -> AI Confidence: **99.32%**
3972. **`sys/contrib/device-tree/src/arm64/freescale/imx8mm-venice-gw75xx.dtsi`** -> AI Confidence: **99.32%**
3973. **`sys/contrib/device-tree/src/arm64/freescale/imx8mm-venice-gw7905.dtsi`** -> AI Confidence: **99.32%**
3974. **`sys/contrib/device-tree/src/arm64/freescale/imx8mn-beacon-kit.dts`** -> AI Confidence: **99.32%**
3975. **`sys/contrib/device-tree/src/arm64/freescale/imx8mn-ddr3l-evk.dts`** -> AI Confidence: **99.32%**
3976. **`sys/contrib/device-tree/src/arm64/freescale/imx8mn-evk.dts`** -> AI Confidence: **99.32%**
3977. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-aristainetos3-helios.dts`** -> AI Confidence: **99.32%**
3978. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-aristainetos3-proton2s.dts`** -> AI Confidence: **99.32%**
3979. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-data-modul-edm-sbc.dts`** -> AI Confidence: **99.32%**
3980. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-dhcom-drc02.dts`** -> AI Confidence: **99.32%**
3981. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-dhcom-pdk2.dts`** -> AI Confidence: **99.32%**
3982. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-dhcom-pdk3.dts`** -> AI Confidence: **99.32%**
3983. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-icore-mx8mp-edimm2.2.dts`** -> AI Confidence: **99.32%**
3984. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-msc-sm2s-ep1.dts`** -> AI Confidence: **99.32%**
3985. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-navqp.dts`** -> AI Confidence: **99.32%**
3986. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-toradex-smarc.dtsi`** -> AI Confidence: **99.32%**
3987. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-venice-gw71xx.dtsi`** -> AI Confidence: **99.32%**
3988. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-venice-gw72xx.dtsi`** -> AI Confidence: **99.32%**
3989. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-venice-gw73xx.dtsi`** -> AI Confidence: **99.32%**
3990. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-venice-gw75xx.dtsi`** -> AI Confidence: **99.32%**
3991. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-venice-gw7905.dtsi`** -> AI Confidence: **99.32%**
3992. **`sys/contrib/device-tree/src/arm64/freescale/imx8mp-venice-gw82xx.dtsi`** -> AI Confidence: **99.32%**
3993. **`sys/contrib/device-tree/src/arm64/freescale/imx95-19x19-evk.dts`** -> AI Confidence: **99.32%**
3994. **`sys/contrib/device-tree/src/arm64/freescale/imx95-libra-rdk-fpsc.dts`** -> AI Confidence: **99.32%**
3995. **`sys/contrib/device-tree/src/arm64/hisilicon/hi3798cv200-poplar.dts`** -> AI Confidence: **99.32%**
3996. **`sys/contrib/device-tree/src/arm64/hisilicon/hi6220-hikey.dts`** -> AI Confidence: **99.32%**
3997. **`sys/contrib/device-tree/src/arm64/marvell/armada-3720-gl-mv1000.dts`** -> AI Confidence: **99.32%**
3998. **`sys/contrib/device-tree/src/arm64/marvell/armada-8040-clearfog-gt-8k.dts`** -> AI Confidence: **99.32%**
3999. **`sys/contrib/device-tree/src/arm64/marvell/armada-8040-puzzle-m801.dts`** -> AI Confidence: **99.32%**
4000. **`sys/contrib/device-tree/src/arm64/marvell/mmp/pxa1908-samsung-coreprimevelte.dts`** -> AI Confidence: **99.32%**
4001. **`sys/contrib/device-tree/src/arm64/mediatek/mt6795-sony-xperia-m5.dts`** -> AI Confidence: **99.32%**
4002. **`sys/contrib/device-tree/src/arm64/nvidia/tegra186-p2771-0000.dts`** -> AI Confidence: **99.32%**
4003. **`sys/contrib/device-tree/src/arm64/nvidia/tegra194-p2972-0000.dts`** -> AI Confidence: **99.32%**
4004. **`sys/contrib/device-tree/src/arm64/nvidia/tegra210-p2597.dtsi`** -> AI Confidence: **99.32%**
4005. **`sys/contrib/device-tree/src/arm64/qcom/ipq5424-rdp466.dts`** -> AI Confidence: **99.32%**
4006. **`sys/contrib/device-tree/src/arm64/qcom/msm8916-lg-m216.dts`** -> AI Confidence: **99.32%**
4007. **`sys/contrib/device-tree/src/arm64/qcom/msm8953-motorola-potter.dts`** -> AI Confidence: **99.32%**
4008. **`sys/contrib/device-tree/src/arm64/qcom/msm8953-xiaomi-daisy.dts`** -> AI Confidence: **99.32%**
4009. **`sys/contrib/device-tree/src/arm64/qcom/msm8998-lenovo-miix-630.dts`** -> AI Confidence: **99.32%**
4010. **`sys/contrib/device-tree/src/arm64/qcom/qrb2210-rb1.dts`** -> AI Confidence: **99.32%**
4011. **`sys/contrib/device-tree/src/arm64/qcom/sc7180-trogdor-kingoftown-r0.dts`** -> AI Confidence: **99.32%**
4012. **`sys/contrib/device-tree/src/arm64/qcom/sc7280-herobrine-crd.dts`** -> AI Confidence: **99.32%**
4013. **`sys/contrib/device-tree/src/arm64/qcom/sc7280-herobrine-herobrine-r1.dts`** -> AI Confidence: **99.32%**
4014. **`sys/contrib/device-tree/src/arm64/qcom/sdm450-lenovo-tbx605f.dts`** -> AI Confidence: **99.32%**
4015. **`sys/contrib/device-tree/src/arm64/qcom/sdm450-motorola-ali.dts`** -> AI Confidence: **99.32%**
4016. **`sys/contrib/device-tree/src/arm64/qcom/sdm632-motorola-ocean.dts`** -> AI Confidence: **99.32%**
4017. **`sys/contrib/device-tree/src/arm64/renesas/r8a774a1-beacon-rzg2m-kit.dts`** -> AI Confidence: **99.32%**
4018. **`sys/contrib/device-tree/src/arm64/renesas/r8a774a1-hihope-rzg2m-ex-idk-1110wr.dts`** -> AI Confidence: **99.32%**
4019. **`sys/contrib/device-tree/src/arm64/renesas/r8a774a1-hihope-rzg2m-rev2-ex-idk-1110wr.dts`** -> AI Confidence: **99.32%**
4020. **`sys/contrib/device-tree/src/arm64/renesas/r8a774b1-beacon-rzg2n-kit.dts`** -> AI Confidence: **99.32%**
4021. **`sys/contrib/device-tree/src/arm64/renesas/r8a774b1-hihope-rzg2n-ex-idk-1110wr.dts`** -> AI Confidence: **99.32%**
4022. **`sys/contrib/device-tree/src/arm64/renesas/r8a774b1-hihope-rzg2n-rev2-ex-idk-1110wr.dts`** -> AI Confidence: **99.32%**
4023. **`sys/contrib/device-tree/src/arm64/renesas/r8a774e1-beacon-rzg2h-kit.dts`** -> AI Confidence: **99.32%**
4024. **`sys/contrib/device-tree/src/arm64/renesas/r8a774e1-hihope-rzg2h-ex-idk-1110wr.dts`** -> AI Confidence: **99.32%**
4025. **`sys/contrib/device-tree/src/arm64/renesas/r8a779a0-falcon.dts`** -> AI Confidence: **99.32%**
4026. **`sys/contrib/device-tree/src/arm64/renesas/r8a779f0-spider-cpu.dtsi`** -> AI Confidence: **99.32%**
4027. **`sys/contrib/device-tree/src/arm64/renesas/r9a07g043u11-smarc.dts`** -> AI Confidence: **99.32%**
4028. **`sys/contrib/device-tree/src/arm64/renesas/r9a07g044c2-smarc.dts`** -> AI Confidence: **99.32%**
4029. **`sys/contrib/device-tree/src/arm64/renesas/r9a07g044l2-remi-pi.dts`** -> AI Confidence: **99.32%**
4030. **`sys/contrib/device-tree/src/arm64/renesas/r9a09g011-v2mevk2.dts`** -> AI Confidence: **99.32%**
4031. **`sys/contrib/device-tree/src/arm64/renesas/rzg2lc-smarc-som.dtsi`** -> AI Confidence: **99.32%**
4032. **`sys/contrib/device-tree/src/arm64/renesas/rzg2ul-smarc-som.dtsi`** -> AI Confidence: **99.32%**
4033. **`sys/contrib/device-tree/src/arm64/renesas/rzg2ul-smarc.dtsi`** -> AI Confidence: **99.32%**
4034. **`sys/contrib/device-tree/src/arm64/renesas/rzg3s-smarc.dtsi`** -> AI Confidence: **99.32%**
4035. **`sys/contrib/device-tree/src/arm64/rockchip/px30-firefly-jd4-core-mb.dts`** -> AI Confidence: **99.32%**
4036. **`sys/contrib/device-tree/src/arm64/rockchip/px30-firefly-jd4-core.dtsi`** -> AI Confidence: **99.32%**
4037. **`sys/contrib/device-tree/src/arm64/rockchip/px30-ringneck-haikou.dts`** -> AI Confidence: **99.32%**
4038. **`sys/contrib/device-tree/src/arm64/rockchip/rk3308-bpi-p2-pro.dts`** -> AI Confidence: **99.32%**
4039. **`sys/contrib/device-tree/src/arm64/rockchip/rk3368-evb.dtsi`** -> AI Confidence: **99.32%**
4040. **`sys/contrib/device-tree/src/arm64/rockchip/rk3399pro-vmarc-som.dtsi`** -> AI Confidence: **99.32%**
4041. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-armsom-lm7.dtsi`** -> AI Confidence: **99.32%**
4042. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-firefly-core-3588j.dtsi`** -> AI Confidence: **99.32%**
4043. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-firefly-icore-3588q.dtsi`** -> AI Confidence: **99.32%**
4044. **`sys/contrib/device-tree/src/arm64/rockchip/rk3588-turing-rk1.dtsi`** -> AI Confidence: **99.32%**
4045. **`sys/contrib/device-tree/src/arm64/tesla/fsd.dtsi`** -> AI Confidence: **99.32%**
4046. **`sys/contrib/device-tree/src/arm64/ti/k3-am62-phycore-som.dtsi`** -> AI Confidence: **99.32%**
4047. **`sys/contrib/device-tree/src/arm64/ti/k3-am62a-phycore-som.dtsi`** -> AI Confidence: **99.32%**
4048. **`sys/contrib/device-tree/src/arm64/ti/k3-am64-phycore-som.dtsi`** -> AI Confidence: **99.32%**
4049. **`sys/contrib/device-tree/src/arm64/ti/k3-am654-base-board.dts`** -> AI Confidence: **99.32%**
4050. **`sys/contrib/device-tree/src/arm64/ti/k3-am67a-beagley-ai.dts`** -> AI Confidence: **99.32%**
4051. **`sys/contrib/device-tree/src/arm64/ti/k3-am68-phycore-som.dtsi`** -> AI Confidence: **99.32%**
4052. **`sys/contrib/device-tree/src/arm64/ti/k3-am69-sk.dts`** -> AI Confidence: **99.32%**
4053. **`sys/contrib/device-tree/src/mips/pic32/pic32mzda_sk.dts`** -> AI Confidence: **99.32%**
4054. **`sys/contrib/device-tree/src/mips/qca/ar9132_tl_wr1043nd_v1.dts`** -> AI Confidence: **99.32%**
4055. **`sys/contrib/device-tree/src/mips/qca/ar9331_dragino_ms14.dts`** -> AI Confidence: **99.32%**
4056. **`sys/contrib/device-tree/src/mips/qca/ar9331_omega.dts`** -> AI Confidence: **99.32%**
4057. **`sys/contrib/device-tree/src/mips/qca/ar9331_tl_mr3020.dts`** -> AI Confidence: **99.32%**
4058. **`sys/contrib/device-tree/src/mips/ralink/gardena_smart_gateway_mt7688.dts`** -> AI Confidence: **99.32%**
4059. **`sys/contrib/device-tree/src/mips/ralink/mt7621-gnubee-gb-pc1.dts`** -> AI Confidence: **99.32%**
4060. **`sys/contrib/device-tree/src/mips/ralink/mt7621-gnubee-gb-pc2.dts`** -> AI Confidence: **99.32%**
4061. **`sys/contrib/device-tree/src/powerpc/turris1x.dts`** -> AI Confidence: **99.32%**
4062. **`sys/contrib/device-tree/src/riscv/allwinner/sun20i-d1-clockworkpi-v3.14.dts`** -> AI Confidence: **99.32%**
4063. **`sys/contrib/device-tree/src/riscv/canaan/canaan_kd233.dts`** -> AI Confidence: **99.32%**
4064. **`sys/contrib/device-tree/src/riscv/canaan/k210_generic.dts`** -> AI Confidence: **99.32%**
4065. **`sys/contrib/device-tree/src/riscv/canaan/sipeed_maixduino.dts`** -> AI Confidence: **99.32%**
4066. **`sys/contrib/device-tree/src/riscv/sophgo/sg2042-evb-v1.dts`** -> AI Confidence: **99.32%**
4067. **`sys/contrib/device-tree/src/riscv/sophgo/sg2042-evb-v2.dts`** -> AI Confidence: **99.32%**
4068. **`sys/contrib/device-tree/src/riscv/sophgo/sg2042-milkv-pioneer.dts`** -> AI Confidence: **99.32%**
4069. **`sys/contrib/device-tree/src/riscv/thead/th1520-beaglev-ahead.dts`** -> AI Confidence: **99.32%**
4070. **`sys/contrib/libsodium/src/libsodium/crypto_shorthash/siphash24/ref/shorthash_siphash24_ref.c`** -> AI Confidence: **99.32%**
4071. **`sys/contrib/libsodium/src/libsodium/crypto_shorthash/siphash24/ref/shorthash_siphashx24_ref.c`** -> AI Confidence: **99.32%**
4072. **`sys/contrib/openzfs/include/sys/u8_textprep.h`** -> AI Confidence: **99.32%**
4073. **`sys/contrib/openzfs/module/icp/algs/edonr/edonr.c`** -> AI Confidence: **99.32%**
4074. **`sys/contrib/openzfs/module/icp/algs/skein/skein_block.c`** -> AI Confidence: **99.32%**
4075. **`sys/contrib/openzfs/module/zstd/include/limits.h`** -> AI Confidence: **99.32%**
4076. **`sys/contrib/openzfs/module/zstd/include/string.h`** -> AI Confidence: **99.32%**
4077. **`sys/contrib/zstd/examples/streaming_memory_usage.c`** -> AI Confidence: **99.32%**
4078. **`sys/dev/al_eth/al_init_eth_kr.c`** -> AI Confidence: **99.32%**
4079. **`sys/dev/axgbe/xgbe-drv.c`** -> AI Confidence: **99.32%**
4080. **`sys/dev/ocs_fc/ocs_hw_queues.c`** -> AI Confidence: **99.32%**
4081. **`sys/dev/pms/RefTisa/sallsdk/spc/sainit.c`** -> AI Confidence: **99.32%**
4082. **`sys/dev/pms/RefTisa/sallsdk/spc/saint.c`** -> AI Confidence: **99.32%**
4083. **`sys/dev/pms/RefTisa/sallsdk/spc/sampirsp.c`** -> AI Confidence: **99.32%**
4084. **`sys/dev/sfxge/common/ef10_image.c`** -> AI Confidence: **99.32%**
4085. **`sys/dev/sfxge/common/ef10_phy.c`** -> AI Confidence: **99.32%**
4086. **`sys/dev/sfxge/common/ef10_rx.c`** -> AI Confidence: **99.32%**
4087. **`sys/dev/sfxge/common/efsys.h`** -> AI Confidence: **99.32%**
4088. **`sys/dev/sfxge/common/efx_bootcfg.c`** -> AI Confidence: **99.32%**
4089. **`sys/dev/sfxge/common/efx_filter.c`** -> AI Confidence: **99.32%**
4090. **`sys/dev/sfxge/common/efx_hash.c`** -> AI Confidence: **99.32%**
4091. **`sys/dev/sfxge/common/efx_mcdi.c`** -> AI Confidence: **99.32%**
4092. **`sys/dev/sfxge/common/efx_vpd.c`** -> AI Confidence: **99.32%**
4093. **`sys/dev/sfxge/common/medford2_nic.c`** -> AI Confidence: **99.32%**
4094. **`sys/dev/sfxge/common/medford_nic.c`** -> AI Confidence: **99.32%**
4095. **`sys/dev/sfxge/common/siena_phy.c`** -> AI Confidence: **99.32%**
4096. **`sys/dev/sfxge/common/siena_sram.c`** -> AI Confidence: **99.32%**
4097. **`sys/dev/sfxge/common/siena_vpd.c`** -> AI Confidence: **99.32%**
4098. **`sys/libkern/strlen.c`** -> AI Confidence: **99.32%**
4099. **`usr.bin/chpass/table.c`** -> AI Confidence: **99.32%**
4100. **`usr.bin/gprof/arcs.c`** -> AI Confidence: **99.32%**
4101. **`usr.sbin/ifmcstat/printb.c`** -> AI Confidence: **99.32%**
4102. **`usr.sbin/vidcontrol/decode.c`** -> AI Confidence: **99.32%**
4103. **`contrib/elftoolchain/common/utarray.h`** -> AI Confidence: **99.32%**
4104. **`contrib/llvm-project/clang/include/clang/AST/DependenceFlags.h`** -> AI Confidence: **99.32%**
4105. **`contrib/llvm-project/clang/include/clang/AST/StmtGraphTraits.h`** -> AI Confidence: **99.32%**
4106. **`contrib/llvm-project/clang/include/clang/Basic/DiagnosticError.h`** -> AI Confidence: **99.32%**
4107. **`contrib/llvm-project/clang/include/clang/StaticAnalyzer/Frontend/FrontendActions.h`** -> AI Confidence: **99.32%**
4108. **`contrib/llvm-project/clang/include/clang/Tooling/AllTUsExecution.h`** -> AI Confidence: **99.32%**
4109. **`contrib/llvm-project/clang/include/clang/Tooling/Refactoring/Extract/Extract.h`** -> AI Confidence: **99.32%**
4110. **`contrib/llvm-project/libcxx/include/__algorithm/clamp.h`** -> AI Confidence: **99.32%**
4111. **`contrib/llvm-project/libcxx/include/__algorithm/fill.h`** -> AI Confidence: **99.32%**
4112. **`contrib/llvm-project/libcxx/include/__algorithm/partition_copy.h`** -> AI Confidence: **99.32%**
4113. **`contrib/llvm-project/libcxx/include/__atomic/contention_t.h`** -> AI Confidence: **99.32%**
4114. **`contrib/llvm-project/libcxx/include/__charconv/to_chars.h`** -> AI Confidence: **99.32%**
4115. **`contrib/llvm-project/libcxx/include/__charconv/to_chars_floating_point.h`** -> AI Confidence: **99.32%**
4116. **`contrib/llvm-project/libcxx/include/__concepts/boolean_testable.h`** -> AI Confidence: **99.32%**
4117. **`contrib/llvm-project/libcxx/include/__concepts/convertible_to.h`** -> AI Confidence: **99.32%**
4118. **`contrib/llvm-project/libcxx/include/__concepts/derived_from.h`** -> AI Confidence: **99.32%**
4119. **`contrib/llvm-project/libcxx/include/__concepts/different_from.h`** -> AI Confidence: **99.32%**
4120. **`contrib/llvm-project/libcxx/include/__concepts/invocable.h`** -> AI Confidence: **99.32%**
4121. **`contrib/llvm-project/libcxx/include/__concepts/semiregular.h`** -> AI Confidence: **99.32%**
4122. **`contrib/llvm-project/libcxx/include/__configuration/abi.h`** -> AI Confidence: **99.32%**
4123. **`contrib/llvm-project/libcxx/include/__format/format_error.h`** -> AI Confidence: **99.32%**
4124. **`contrib/llvm-project/libcxx/include/__functional/mem_fun_ref.h`** -> AI Confidence: **99.32%**
4125. **`contrib/llvm-project/libcxx/include/__fwd/pair.h`** -> AI Confidence: **99.32%**
4126. **`contrib/llvm-project/libcxx/include/__iterator/permutable.h`** -> AI Confidence: **99.32%**
4127. **`contrib/llvm-project/libcxx/include/__ranges/container_compatible_range.h`** -> AI Confidence: **99.32%**
4128. **`contrib/llvm-project/libcxx/include/__type_traits/remove_const_ref.h`** -> AI Confidence: **99.32%**
4129. **`contrib/llvm-project/libcxx/include/uchar.h`** -> AI Confidence: **99.32%**
4130. **`contrib/llvm-project/libcxx/src/include/config_elast.h`** -> AI Confidence: **99.32%**
4131. **`contrib/llvm-project/lldb/include/lldb/Host/HostGetOpt.h`** -> AI Confidence: **99.32%**
4132. **`contrib/llvm-project/lldb/include/lldb/Host/PosixApi.h`** -> AI Confidence: **99.32%**
4133. **`contrib/llvm-project/llvm/include/llvm/ADT/ADL.h`** -> AI Confidence: **99.32%**
4134. **`contrib/llvm-project/llvm/include/llvm/ADT/ScopeExit.h`** -> AI Confidence: **99.32%**
4135. **`contrib/llvm-project/llvm/include/llvm/ADT/iterator_range.h`** -> AI Confidence: **99.32%**
4136. **`contrib/llvm-project/llvm/include/llvm/Analysis/InlineModelFeatureMaps.h`** -> AI Confidence: **99.32%**
4137. **`contrib/llvm-project/llvm/include/llvm/DebugInfo/CodeView/SymbolVisitorCallbacks.h`** -> AI Confidence: **99.32%**
4138. **`contrib/llvm-project/llvm/include/llvm/DebugInfo/CodeView/TypeVisitorCallbacks.h`** -> AI Confidence: **99.32%**
4139. **`contrib/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/Debugging/DebugInfoSupport.h`** -> AI Confidence: **99.32%**
4140. **`contrib/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/Debugging/DebuggerSupportPlugin.h`** -> AI Confidence: **99.32%**
4141. **`contrib/llvm-project/llvm/include/llvm/Support/CheckedArithmetic.h`** -> AI Confidence: **99.32%**
4142. **`contrib/llvm-project/llvm/include/llvm/Transforms/IPO/ModuleInliner.h`** -> AI Confidence: **99.32%**
4143. **`contrib/llvm-project/llvm/include/llvm/Transforms/IPO/OpenMPOpt.h`** -> AI Confidence: **99.32%**
4144. **`contrib/llvm-project/llvm/include/llvm/Transforms/Instrumentation/DataFlowSanitizer.h`** -> AI Confidence: **99.32%**
4145. **`contrib/ntp/include/ntp_net.h`** -> AI Confidence: **99.32%**
4146. **`contrib/openpam/include/security/pam_modules.h`** -> AI Confidence: **99.32%**
4147. **`contrib/xz/src/common/sysdefs.h`** -> AI Confidence: **99.32%**
4148. **`crypto/krb5/src/lib/crypto/builtin/aes/aesopt.h`** -> AI Confidence: **99.32%**
4149. **`crypto/libecc/include/libecc/utils/dbg_sig.h`** -> AI Confidence: **99.32%**
4150. **`include/_ctype.h`** -> AI Confidence: **99.32%**
4151. **`sys/cddl/compat/opensolaris/sys/assfail.h`** -> AI Confidence: **99.32%**
4152. **`sys/cddl/contrib/opensolaris/uts/common/sys/sysmacros.h`** -> AI Confidence: **99.32%**
4153. **`sys/compat/linuxkpi/common/include/linux/compiler.h`** -> AI Confidence: **99.32%**
4154. **`sys/compat/linuxkpi/common/include/linux/container_of.h`** -> AI Confidence: **99.32%**
4155. **`sys/compat/linuxkpi/common/include/linux/iopoll.h`** -> AI Confidence: **99.32%**
4156. **`sys/compat/linuxkpi/common/include/linux/minmax.h`** -> AI Confidence: **99.32%**
4157. **`sys/compat/linuxkpi/common/include/linux/moduleparam.h`** -> AI Confidence: **99.32%**
4158. **`sys/contrib/openzfs/include/os/linux/spl/sys/cmn_err.h`** -> AI Confidence: **99.32%**
4159. **`sys/contrib/openzfs/include/os/linux/spl/sys/trace_taskq.h`** -> AI Confidence: **99.32%**
4160. **`sys/contrib/openzfs/include/os/linux/zfs/sys/trace_dbgmsg.h`** -> AI Confidence: **99.32%**
4161. **`sys/contrib/openzfs/include/os/linux/zfs/sys/trace_dbuf.h`** -> AI Confidence: **99.32%**
4162. **`sys/contrib/openzfs/include/os/linux/zfs/sys/trace_dmu.h`** -> AI Confidence: **99.32%**
4163. **`sys/contrib/openzfs/include/os/linux/zfs/sys/trace_dnode.h`** -> AI Confidence: **99.32%**
4164. **`sys/contrib/openzfs/include/os/linux/zfs/sys/trace_txg.h`** -> AI Confidence: **99.32%**
4165. **`sys/contrib/openzfs/include/os/linux/zfs/sys/trace_vdev.h`** -> AI Confidence: **99.32%**
4166. **`sys/contrib/openzfs/include/os/linux/zfs/sys/trace_zil.h`** -> AI Confidence: **99.32%**
4167. **`sys/contrib/openzfs/include/os/linux/zfs/sys/trace_zrlock.h`** -> AI Confidence: **99.32%**
4168. **`sys/dev/ofw/ofw_bus.h`** -> AI Confidence: **99.32%**
4169. **`sys/dev/sound/pcm/pcm.h`** -> AI Confidence: **99.32%**
4170. **`sys/sys/ck.h`** -> AI Confidence: **99.32%**
4171. **`sys/sys/ktr.h`** -> AI Confidence: **99.32%**
4172. **`contrib/atf/atf-sh/misc_helpers.sh`** -> AI Confidence: **99.32%**
4173. **`contrib/bc/scripts/exec-install.sh`** -> AI Confidence: **99.32%**
4174. **`contrib/bc/tests/all.sh`** -> AI Confidence: **99.32%**
4175. **`contrib/bc/tests/history.sh`** -> AI Confidence: **99.32%**
4176. **`contrib/bc/tests/script.sh`** -> AI Confidence: **99.32%**
4177. **`contrib/bearssl/mk/mkrules.sh`** -> AI Confidence: **99.32%**
4178. **`libexec/rc/rc.d/geli`** -> AI Confidence: **99.32%**
4179. **`libexec/rc/rc.d/geli2`** -> AI Confidence: **99.32%**
4180. **`libexec/rc/rc.d/growfs`** -> AI Confidence: **99.32%**
4181. **`libexec/rc/rc.d/mdconfig`** -> AI Confidence: **99.32%**
4182. **`libexec/rc/rc.d/mdconfig2`** -> AI Confidence: **99.32%**
4183. **`libexec/rc/rc.d/syscons`** -> AI Confidence: **99.32%**
4184. **`sbin/route/tests/basic.sh`** -> AI Confidence: **99.32%**
4185. **`sys/contrib/openzfs/tests/zfs-tests/tests/functional/cachefile/cachefile_003_pos.ksh`** -> AI Confidence: **99.32%**
4186. **`tests/sys/cam/ctl/read_buffer.sh`** -> AI Confidence: **99.32%**
4187. **`tests/sys/netpfil/ipfw/table.sh`** -> AI Confidence: **99.32%**
4188. **`tests/sys/netpfil/pf/rules_counter.sh`** -> AI Confidence: **99.32%**
4189. **`tools/test/netfibs/initiator.sh`** -> AI Confidence: **99.32%**
4190. **`tools/test/stress2/misc/umountf2.sh`** -> AI Confidence: **99.32%**
4191. **`tools/tinder.sh`** -> AI Confidence: **99.32%**
4192. **`usr.sbin/bsdconfig/dot/dot`** -> AI Confidence: **99.32%**
4193. **`usr.sbin/bsdconfig/timezone/timezone`** -> AI Confidence: **99.32%**
4194. **`usr.sbin/bsdinstall/scripts/netconfig`** -> AI Confidence: **99.32%**
4195. **`usr.sbin/bsdinstall/scripts/services`** -> AI Confidence: **99.32%**
4196. **`usr.sbin/fwget/fwget.sh`** -> AI Confidence: **99.32%**
4197. **`usr.sbin/service/service.sh`** -> AI Confidence: **99.32%**
4198. **`contrib/kyua/bootstrap/atf_helpers.cpp`** -> AI Confidence: **99.32%**
4199. **`contrib/kyua/drivers/list_tests_helpers.cpp`** -> AI Confidence: **99.32%**
4200. **`contrib/kyua/integration/helpers/interrupts.cpp`** -> AI Confidence: **99.32%**
4201. **`contrib/llvm-project/lldb/source/Interpreter/OptionValueArray.cpp`** -> AI Confidence: **99.32%**
4202. **`contrib/llvm-project/lldb/source/Interpreter/OptionValueFileSpecList.cpp`** -> AI Confidence: **99.32%**
4203. **`contrib/llvm-project/openmp/runtime/src/kmp_ftn_stdcall.cpp`** -> AI Confidence: **99.32%**
4204. **`contrib/opencsd/decoder/source/etmv4/trc_pkt_elem_etmv4i.cpp`** -> AI Confidence: **99.32%**
4205. **`contrib/opencsd/decoder/source/i_dec/trc_i_decode.cpp`** -> AI Confidence: **99.32%**
4206. **`contrib/opencsd/decoder/source/mem_acc/trc_mem_acc_file.cpp`** -> AI Confidence: **99.32%**
4207. **`contrib/opencsd/decoder/source/ptm/trc_pkt_elem_ptm.cpp`** -> AI Confidence: **99.32%**
4208. **`contrib/opencsd/decoder/source/ptm/trc_pkt_proc_ptm.cpp`** -> AI Confidence: **99.32%**
4209. **`contrib/opencsd/decoder/source/stm/trc_pkt_elem_stm.cpp`** -> AI Confidence: **99.32%**
4210. **`contrib/ntp/sntp/unity/auto/generate_module.rb`** -> AI Confidence: **99.32%**
4211. **`bin/cp/utils.c`** -> AI Confidence: **99.31%**
4212. **`bin/date/date.c`** -> AI Confidence: **99.31%**
4213. **`bin/date/vary.c`** -> AI Confidence: **99.31%**
4214. **`bin/dd/args.c`** -> AI Confidence: **99.31%**
4215. **`bin/df/df.c`** -> AI Confidence: **99.31%**
4216. **`bin/ed/main.c`** -> AI Confidence: **99.31%**
4217. **`bin/getfacl/getfacl.c`** -> AI Confidence: **99.31%**
4218. **`bin/ln/ln.c`** -> AI Confidence: **99.31%**
4219. **`bin/ls/print.c`** -> AI Confidence: **99.31%**
4220. **`bin/mv/mv.c`** -> AI Confidence: **99.31%**
4221. **`bin/nproc/nproc.c`** -> AI Confidence: **99.31%**
4222. **`bin/pax/buf_subs.c`** -> AI Confidence: **99.31%**
4223. **`bin/pax/cache.c`** -> AI Confidence: **99.31%**
4224. **`bin/pax/file_subs.c`** -> AI Confidence: **99.31%**
4225. **`bin/pax/tables.c`** -> AI Confidence: **99.31%**
4226. **`bin/ps/keyword.c`** -> AI Confidence: **99.31%**
4227. **`bin/ps/print.c`** -> AI Confidence: **99.31%**
4228. **`bin/ps/ps.c`** -> AI Confidence: **99.31%**
4229. **`bin/pwd/pwd.c`** -> AI Confidence: **99.31%**
4230. **`bin/sh/alias.c`** -> AI Confidence: **99.31%**
4231. **`bin/sh/arith_yacc.c`** -> AI Confidence: **99.31%**
4232. **`bin/sh/error.c`** -> AI Confidence: **99.31%**
4233. **`bin/sh/exec.c`** -> AI Confidence: **99.31%**
4234. **`bin/sh/input.c`** -> AI Confidence: **99.31%**
4235. **`bin/sh/main.c`** -> AI Confidence: **99.31%**
4236. **`bin/sh/var.c`** -> AI Confidence: **99.31%**
4237. **`bin/stty/cchar.c`** -> AI Confidence: **99.31%**
4238. **`bin/test/test.c`** -> AI Confidence: **99.31%**
4239. **`cddl/contrib/opensolaris/cmd/dtrace/dtrace.c`** -> AI Confidence: **99.31%**
4240. **`cddl/contrib/opensolaris/cmd/lockstat/lockstat.c`** -> AI Confidence: **99.31%**
4241. **`cddl/contrib/opensolaris/cmd/lockstat/sym.c`** -> AI Confidence: **99.31%**
4242. **`cddl/contrib/opensolaris/tests/os-tests/tests/oclo/ocloexec_verify.c`** -> AI Confidence: **99.31%**
4243. **`cddl/contrib/opensolaris/tools/ctf/cvt/ctf.c`** -> AI Confidence: **99.31%**
4244. **`cddl/contrib/opensolaris/tools/ctf/cvt/dwarf.c`** -> AI Confidence: **99.31%**
4245. **`cddl/contrib/opensolaris/tools/ctf/cvt/input.c`** -> AI Confidence: **99.31%**
4246. **`cddl/contrib/opensolaris/tools/ctf/cvt/merge.c`** -> AI Confidence: **99.31%**
4247. **`cddl/contrib/opensolaris/tools/ctf/cvt/strtab.c`** -> AI Confidence: **99.31%**
4248. **`cddl/contrib/opensolaris/tools/ctf/cvt/util.c`** -> AI Confidence: **99.31%**
4249. **`cddl/contrib/opensolaris/tools/ctf/dump/dump.c`** -> AI Confidence: **99.31%**
4250. **`contrib/atf/atf-c/check.c`** -> AI Confidence: **99.31%**
4251. **`contrib/atf/atf-c/detail/dynstr.c`** -> AI Confidence: **99.31%**
4252. **`contrib/atf/atf-c/detail/env.c`** -> AI Confidence: **99.31%**
4253. **`contrib/atf/atf-c/detail/fs.c`** -> AI Confidence: **99.31%**
4254. **`contrib/atf/atf-c/detail/process.c`** -> AI Confidence: **99.31%**
4255. **`contrib/atf/atf-c/detail/process_helpers.c`** -> AI Confidence: **99.31%**
4256. **`contrib/atf/atf-c/detail/text.c`** -> AI Confidence: **99.31%**
4257. **`contrib/bc/src/bc_fuzzer.c`** -> AI Confidence: **99.31%**
4258. **`contrib/bc/src/dc_fuzzer.c`** -> AI Confidence: **99.31%**
4259. **`contrib/bc/src/dc_parse.c`** -> AI Confidence: **99.31%**
4260. **`contrib/bc/src/history.c`** -> AI Confidence: **99.31%**
4261. **`contrib/bc/src/lex.c`** -> AI Confidence: **99.31%**
4262. **`contrib/bc/src/num.c`** -> AI Confidence: **99.31%**
4263. **`contrib/bc/src/opt.c`** -> AI Confidence: **99.31%**
4264. **`contrib/bc/src/parse.c`** -> AI Confidence: **99.31%**
4265. **`contrib/bc/src/rand.c`** -> AI Confidence: **99.31%**
4266. **`contrib/bc/src/read.c`** -> AI Confidence: **99.31%**
4267. **`contrib/bc/src/vector.c`** -> AI Confidence: **99.31%**
4268. **`contrib/bearssl/samples/client_basic.c`** -> AI Confidence: **99.31%**
4269. **`contrib/bearssl/src/rand/sysrng.c`** -> AI Confidence: **99.31%**
4270. **`contrib/bearssl/src/ssl/ssl_engine.c`** -> AI Confidence: **99.31%**
4271. **`contrib/bearssl/tools/brssl.c`** -> AI Confidence: **99.31%**
4272. **`contrib/bearssl/tools/ta.c`** -> AI Confidence: **99.31%**
4273. **`contrib/blocklist/bin/conf.c`** -> AI Confidence: **99.31%**
4274. **`contrib/blocklist/bin/state.c`** -> AI Confidence: **99.31%**
4275. **`contrib/blocklist/port/popenve.c`** -> AI Confidence: **99.31%**
4276. **`contrib/blocklist/port/sockaddr_snprintf.c`** -> AI Confidence: **99.31%**
4277. **`contrib/bmake/arch.c`** -> AI Confidence: **99.31%**
4278. **`contrib/bmake/dir.c`** -> AI Confidence: **99.31%**
4279. **`contrib/bmake/job.c`** -> AI Confidence: **99.31%**
4280. **`contrib/bmake/main.c`** -> AI Confidence: **99.31%**
4281. **`contrib/bmake/meta.c`** -> AI Confidence: **99.31%**
4282. **`contrib/bmake/parse.c`** -> AI Confidence: **99.31%**
4283. **`contrib/bmake/sigcompat.c`** -> AI Confidence: **99.31%**
4284. **`contrib/bmake/var.c`** -> AI Confidence: **99.31%**
4285. **`contrib/bsddialog/utility/bsddialog.c`** -> AI Confidence: **99.31%**
4286. **`contrib/bsddialog/utility/util_builders.c`** -> AI Confidence: **99.31%**
4287. **`contrib/bsddialog/utility/util_theme.c`** -> AI Confidence: **99.31%**
4288. **`contrib/bsnmp/gensnmptree/gensnmptree.c`** -> AI Confidence: **99.31%**
4289. **`contrib/bsnmp/snmp_mibII/mibII_tcp.c`** -> AI Confidence: **99.31%**
4290. **`contrib/bsnmp/snmp_mibII/mibII_udp.c`** -> AI Confidence: **99.31%**
4291. **`contrib/bsnmp/snmp_ntp/snmp_ntp.c`** -> AI Confidence: **99.31%**
4292. **`contrib/bsnmp/snmp_target/target_snmp.c`** -> AI Confidence: **99.31%**
4293. **`contrib/bsnmp/snmp_usm/usm_snmp.c`** -> AI Confidence: **99.31%**
4294. **`contrib/bsnmp/snmp_vacm/vacm_snmp.c`** -> AI Confidence: **99.31%**
4295. **`contrib/bsnmp/snmpd/export.c`** -> AI Confidence: **99.31%**
4296. **`contrib/bsnmp/snmpd/trap.c`** -> AI Confidence: **99.31%**
4297. **`contrib/dialog/dialog.c`** -> AI Confidence: **99.31%**
4298. **`contrib/dma/crypto.c`** -> AI Confidence: **99.31%**
4299. **`contrib/dma/dns.c`** -> AI Confidence: **99.31%**
4300. **`contrib/dma/spool.c`** -> AI Confidence: **99.31%**
4301. **`contrib/dma/util.c`** -> AI Confidence: **99.31%**
4302. **`contrib/ee/ee.c`** -> AI Confidence: **99.31%**
4303. **`contrib/elftoolchain/elfcopy/sections.c`** -> AI Confidence: **99.31%**
4304. **`contrib/elftoolchain/libelf/elf_scn.c`** -> AI Confidence: **99.31%**
4305. **`contrib/elftoolchain/libelf/libelf_ar.c`** -> AI Confidence: **99.31%**
4306. **`contrib/elftoolchain/libelftc/elftc_demangle.c`** -> AI Confidence: **99.31%**
4307. **`contrib/elftoolchain/libelftc/elftc_string_table.c`** -> AI Confidence: **99.31%**
4308. **`contrib/elftoolchain/libelftc/libelftc_dem_gnu2.c`** -> AI Confidence: **99.31%**
4309. **`contrib/elftoolchain/libelftc/libelftc_dem_gnu3.c`** -> AI Confidence: **99.31%**
4310. **`contrib/elftoolchain/nm/nm.c`** -> AI Confidence: **99.31%**
4311. **`contrib/elftoolchain/readelf/readelf.c`** -> AI Confidence: **99.31%**
4312. **`contrib/expat/tests/common.c`** -> AI Confidence: **99.31%**
4313. **`contrib/expat/tests/minicheck.c`** -> AI Confidence: **99.31%**
4314. **`contrib/expat/tests/ns_tests.c`** -> AI Confidence: **99.31%**
4315. **`contrib/expat/tests/structdata.c`** -> AI Confidence: **99.31%**
4316. **`contrib/expat/xmlwf/readfilemap.c`** -> AI Confidence: **99.31%**
4317. **`contrib/file/src/apprentice.c`** -> AI Confidence: **99.31%**
4318. **`contrib/file/src/cdf.c`** -> AI Confidence: **99.31%**
4319. **`contrib/file/src/compress.c`** -> AI Confidence: **99.31%**
4320. **`contrib/file/src/der.c`** -> AI Confidence: **99.31%**
4321. **`contrib/file/src/funcs.c`** -> AI Confidence: **99.31%**
4322. **`contrib/file/src/is_csv.c`** -> AI Confidence: **99.31%**
4323. **`contrib/file/src/is_simh.c`** -> AI Confidence: **99.31%**
4324. **`contrib/file/src/magic.c`** -> AI Confidence: **99.31%**
4325. **`contrib/file/src/print.c`** -> AI Confidence: **99.31%**
4326. **`contrib/file/src/vasprintf.c`** -> AI Confidence: **99.31%**
4327. **`contrib/hyperv/tools/hv_kvp_daemon.c`** -> AI Confidence: **99.31%**
4328. **`contrib/jemalloc/include/jemalloc/internal/tsd.h`** -> AI Confidence: **99.31%**
4329. **`contrib/jemalloc/src/arena.c`** -> AI Confidence: **99.31%**
4330. **`contrib/jemalloc/src/ctl.c`** -> AI Confidence: **99.31%**
4331. **`contrib/jemalloc/src/jemalloc.c`** -> AI Confidence: **99.31%**
4332. **`contrib/jemalloc/src/pages.c`** -> AI Confidence: **99.31%**
4333. **`contrib/jemalloc/src/prof_recent.c`** -> AI Confidence: **99.31%**
4334. **`contrib/jemalloc/src/stats.c`** -> AI Confidence: **99.31%**
4335. **`contrib/ldns-host/ldns-host.c`** -> AI Confidence: **99.31%**
4336. **`contrib/ldns/compat/fake-rfc2553.c`** -> AI Confidence: **99.31%**
4337. **`contrib/ldns/dnssec.c`** -> AI Confidence: **99.31%**
4338. **`contrib/ldns/dnssec_sign.c`** -> AI Confidence: **99.31%**
4339. **`contrib/ldns/dnssec_verify.c`** -> AI Confidence: **99.31%**
4340. **`contrib/ldns/keys.c`** -> AI Confidence: **99.31%**
4341. **`contrib/ldns/net.c`** -> AI Confidence: **99.31%**
4342. **`contrib/ldns/util.c`** -> AI Confidence: **99.31%**
4343. **`contrib/less/os.c`** -> AI Confidence: **99.31%**
4344. **`contrib/lib9p/genacl.c`** -> AI Confidence: **99.31%**
4345. **`contrib/lib9p/rfuncs.c`** -> AI Confidence: **99.31%**
4346. **`contrib/lib9p/threadpool.c`** -> AI Confidence: **99.31%**
4347. **`contrib/lib9p/utils.c`** -> AI Confidence: **99.31%**
4348. **`contrib/libarchive/cat/bsdcat.c`** -> AI Confidence: **99.31%**
4349. **`contrib/libarchive/libarchive/archive_blake2s_ref.c`** -> AI Confidence: **99.31%**
4350. **`contrib/libarchive/libarchive/archive_blake2sp_ref.c`** -> AI Confidence: **99.31%**
4351. **`contrib/libarchive/libarchive/archive_check_magic.c`** -> AI Confidence: **99.31%**
4352. **`contrib/libarchive/libarchive/archive_entry_link_resolver.c`** -> AI Confidence: **99.31%**
4353. **`contrib/libarchive/libarchive/archive_random.c`** -> AI Confidence: **99.31%**
4354. **`contrib/libarchive/libarchive/archive_read.c`** -> AI Confidence: **99.31%**
4355. **`contrib/libarchive/libarchive/archive_read_disk_posix.c`** -> AI Confidence: **99.31%**
4356. **`contrib/libarchive/libarchive/archive_read_open_filename.c`** -> AI Confidence: **99.31%**
4357. **`contrib/libarchive/libarchive/archive_read_support_filter_bzip2.c`** -> AI Confidence: **99.31%**
4358. **`contrib/libarchive/libarchive/archive_read_support_filter_gzip.c`** -> AI Confidence: **99.31%**
4359. **`contrib/libarchive/libarchive/archive_read_support_filter_lzop.c`** -> AI Confidence: **99.31%**
4360. **`contrib/libarchive/libarchive/archive_read_support_filter_rpm.c`** -> AI Confidence: **99.31%**
4361. **`contrib/libarchive/libarchive/archive_read_support_filter_xz.c`** -> AI Confidence: **99.31%**
4362. **`contrib/libarchive/libarchive/archive_read_support_filter_zstd.c`** -> AI Confidence: **99.31%**
4363. **`contrib/libarchive/libarchive/archive_read_support_format_7zip.c`** -> AI Confidence: **99.31%**
4364. **`contrib/libarchive/libarchive/archive_read_support_format_ar.c`** -> AI Confidence: **99.31%**
4365. **`contrib/libarchive/libarchive/archive_read_support_format_iso9660.c`** -> AI Confidence: **99.31%**
4366. **`contrib/libarchive/libarchive/archive_read_support_format_mtree.c`** -> AI Confidence: **99.31%**
4367. **`contrib/libarchive/libarchive/archive_read_support_format_rar.c`** -> AI Confidence: **99.31%**
4368. **`contrib/libarchive/libarchive/archive_read_support_format_rar5.c`** -> AI Confidence: **99.31%**
4369. **`contrib/libarchive/libarchive/archive_read_support_format_tar.c`** -> AI Confidence: **99.31%**
4370. **`contrib/libarchive/libarchive/archive_read_support_format_zip.c`** -> AI Confidence: **99.31%**
4371. **`contrib/libarchive/libarchive/archive_time.c`** -> AI Confidence: **99.31%**
4372. **`contrib/libarchive/libarchive/archive_version_details.c`** -> AI Confidence: **99.31%**
4373. **`contrib/libarchive/libarchive/archive_write_add_filter_compress.c`** -> AI Confidence: **99.31%**
4374. **`contrib/libarchive/libarchive/archive_write_add_filter_lrzip.c`** -> AI Confidence: **99.31%**
4375. **`contrib/libarchive/libarchive/archive_write_add_filter_program.c`** -> AI Confidence: **99.31%**
4376. **`contrib/libarchive/libarchive/archive_write_add_filter_xz.c`** -> AI Confidence: **99.31%**
4377. **`contrib/libarchive/libarchive/archive_write_add_filter_zstd.c`** -> AI Confidence: **99.31%**
4378. **`contrib/libarchive/libarchive/archive_write_disk_posix.c`** -> AI Confidence: **99.31%**
4379. **`contrib/libarchive/libarchive/archive_write_disk_set_standard_lookup.c`** -> AI Confidence: **99.31%**
4380. **`contrib/libarchive/libarchive/archive_write_set_format_ar.c`** -> AI Confidence: **99.31%**
4381. **`contrib/libarchive/libarchive/archive_write_set_format_cpio_binary.c`** -> AI Confidence: **99.31%**
4382. **`contrib/libarchive/libarchive/archive_write_set_format_cpio_newc.c`** -> AI Confidence: **99.31%**
4383. **`contrib/libarchive/libarchive/archive_write_set_format_pax.c`** -> AI Confidence: **99.31%**
4384. **`contrib/libarchive/libarchive/archive_write_set_format_shar.c`** -> AI Confidence: **99.31%**
4385. **`contrib/libarchive/libarchive_fe/line_reader.c`** -> AI Confidence: **99.31%**
4386. **`contrib/libarchive/libarchive_fe/passphrase.c`** -> AI Confidence: **99.31%**
4387. **`contrib/libarchive/tar/subst.c`** -> AI Confidence: **99.31%**
4388. **`contrib/libbegemot/rpoll.c`** -> AI Confidence: **99.31%**
4389. **`contrib/libc-pwcache/pwcache.c`** -> AI Confidence: **99.31%**
4390. **`contrib/libc-vis/vis.c`** -> AI Confidence: **99.31%**
4391. **`contrib/libcbor/src/cbor/common.c`** -> AI Confidence: **99.31%**
4392. **`contrib/libcbor/src/cbor/serialization.c`** -> AI Confidence: **99.31%**
4393. **`contrib/libcxxrt/libelftc_dem_gnu3.c`** -> AI Confidence: **99.31%**
4394. **`contrib/libder/libder/libder_read.c`** -> AI Confidence: **99.31%**
4395. **`contrib/libder/tests/fuzz_stream.c`** -> AI Confidence: **99.31%**
4396. **`contrib/libder/tests/fuzz_write.c`** -> AI Confidence: **99.31%**
4397. **`contrib/libder/tests/make_corpus.c`** -> AI Confidence: **99.31%**
4398. **`contrib/libedit/chared.c`** -> AI Confidence: **99.31%**
4399. **`contrib/libedit/common.c`** -> AI Confidence: **99.31%**
4400. **`contrib/libedit/history.c`** -> AI Confidence: **99.31%**
4401. **`contrib/libedit/map.c`** -> AI Confidence: **99.31%**
4402. **`contrib/libedit/readline.c`** -> AI Confidence: **99.31%**
4403. **`contrib/libedit/tty.c`** -> AI Confidence: **99.31%**
4404. **`contrib/libedit/vi.c`** -> AI Confidence: **99.31%**
4405. **`contrib/libevent/arc4random.c`** -> AI Confidence: **99.31%**
4406. **`contrib/libevent/buffer.c`** -> AI Confidence: **99.31%**
4407. **`contrib/libevent/buffer_iocp.c`** -> AI Confidence: **99.31%**
4408. **`contrib/libevent/bufferevent_openssl.c`** -> AI Confidence: **99.31%**
4409. **`contrib/libevent/bufferevent_ratelim.c`** -> AI Confidence: **99.31%**
4410. **`contrib/libevent/epoll_sub.c`** -> AI Confidence: **99.31%**
4411. **`contrib/libevent/event_tagging.c`** -> AI Confidence: **99.31%**
4412. **`contrib/libevent/evport.c`** -> AI Confidence: **99.31%**
4413. **`contrib/libevent/evutil.c`** -> AI Confidence: **99.31%**
4414. **`contrib/libevent/include/event2/util.h`** -> AI Confidence: **99.31%**
4415. **`contrib/libevent/log.c`** -> AI Confidence: **99.31%**
4416. **`contrib/libevent/sample/dns-example.c`** -> AI Confidence: **99.31%**
4417. **`contrib/libevent/sample/event-read-fifo.c`** -> AI Confidence: **99.31%**
4418. **`contrib/libevent/sample/http-server.c`** -> AI Confidence: **99.31%**
4419. **`contrib/libevent/sample/le-proxy.c`** -> AI Confidence: **99.31%**
4420. **`contrib/libevent/select.c`** -> AI Confidence: **99.31%**
4421. **`contrib/libexecinfo/backtrace.c`** -> AI Confidence: **99.31%**
4422. **`contrib/libexecinfo/symtab.c`** -> AI Confidence: **99.31%**
4423. **`contrib/libfido2/examples/info.c`** -> AI Confidence: **99.31%**
4424. **`contrib/libfido2/fuzz/fuzz_bio.c`** -> AI Confidence: **99.31%**
4425. **`contrib/libfido2/fuzz/fuzz_credman.c`** -> AI Confidence: **99.31%**
4426. **`contrib/libfido2/fuzz/fuzz_hid.c`** -> AI Confidence: **99.31%**
4427. **`contrib/libfido2/fuzz/fuzz_largeblob.c`** -> AI Confidence: **99.31%**
4428. **`contrib/libfido2/fuzz/fuzz_mgmt.c`** -> AI Confidence: **99.31%**
4429. **`contrib/libfido2/fuzz/fuzz_netlink.c`** -> AI Confidence: **99.31%**
4430. **`contrib/libfido2/fuzz/fuzz_pcsc.c`** -> AI Confidence: **99.31%**
4431. **`contrib/libfido2/fuzz/preload-fuzz.c`** -> AI Confidence: **99.31%**
4432. **`contrib/libfido2/fuzz/preload-snoop.c`** -> AI Confidence: **99.31%**
4433. **`contrib/libfido2/openbsd-compat/bsd-getline.c`** -> AI Confidence: **99.31%**
4434. **`contrib/libfido2/openbsd-compat/posix_win.h`** -> AI Confidence: **99.31%**
4435. **`contrib/libfido2/openbsd-compat/readpassphrase.c`** -> AI Confidence: **99.31%**
4436. **`contrib/libfido2/src/hid_freebsd.c`** -> AI Confidence: **99.31%**
4437. **`contrib/libfido2/src/hid_linux.c`** -> AI Confidence: **99.31%**
4438. **`contrib/libfido2/src/hid_netbsd.c`** -> AI Confidence: **99.31%**
4439. **`contrib/libfido2/src/hid_osx.c`** -> AI Confidence: **99.31%**
4440. **`contrib/libfido2/src/hid_win.c`** -> AI Confidence: **99.31%**
4441. **`contrib/libfido2/src/netlink.c`** -> AI Confidence: **99.31%**
4442. **`contrib/libfido2/src/nfc_linux.c`** -> AI Confidence: **99.31%**
4443. **`contrib/libfido2/src/random.c`** -> AI Confidence: **99.31%**
4444. **`contrib/libfido2/tools/bio.c`** -> AI Confidence: **99.31%**
4445. **`contrib/libpcap/fad-getad.c`** -> AI Confidence: **99.31%**
4446. **`contrib/libpcap/gencode.c`** -> AI Confidence: **99.31%**
4447. **`contrib/libpcap/msdos/pktdrvr.c`** -> AI Confidence: **99.31%**
4448. **`contrib/libpcap/nametoaddr.c`** -> AI Confidence: **99.31%**
4449. **`contrib/libpcap/optimize.c`** -> AI Confidence: **99.31%**
4450. **`contrib/libpcap/pcap-bpf.c`** -> AI Confidence: **99.31%**
4451. **`contrib/libpcap/pcap-bt-linux.c`** -> AI Confidence: **99.31%**
4452. **`contrib/libpcap/pcap-bt-monitor-linux.c`** -> AI Confidence: **99.31%**
4453. **`contrib/libpcap/pcap-enet.c`** -> AI Confidence: **99.31%**
4454. **`contrib/libpcap/pcap-haiku.c`** -> AI Confidence: **99.31%**
4455. **`contrib/libpcap/pcap-libdlpi.c`** -> AI Confidence: **99.31%**
4456. **`contrib/libpcap/pcap-linux.c`** -> AI Confidence: **99.31%**
4457. **`contrib/libpcap/pcap-nit.c`** -> AI Confidence: **99.31%**
4458. **`contrib/libpcap/pcap-npf.c`** -> AI Confidence: **99.31%**
4459. **`contrib/libpcap/pcap-rpcap.c`** -> AI Confidence: **99.31%**
4460. **`contrib/libpcap/pcap-septel.c`** -> AI Confidence: **99.31%**
4461. **`contrib/libpcap/pcap-sita.c`** -> AI Confidence: **99.31%**
4462. **`contrib/libpcap/pcap-usb-linux.c`** -> AI Confidence: **99.31%**
4463. **`contrib/libpcap/pcap-util.c`** -> AI Confidence: **99.31%**
4464. **`contrib/libpcap/pcap.c`** -> AI Confidence: **99.31%**
4465. **`contrib/libpcap/rpcapd/daemon.c`** -> AI Confidence: **99.31%**
4466. **`contrib/libpcap/rpcapd/win32-svc.c`** -> AI Confidence: **99.31%**
4467. **`contrib/libpcap/savefile.c`** -> AI Confidence: **99.31%**
4468. **`contrib/libpcap/sf-pcap.c`** -> AI Confidence: **99.31%**
4469. **`contrib/libpcap/sf-pcapng.c`** -> AI Confidence: **99.31%**
4470. **`contrib/libpcap/sockutils.c`** -> AI Confidence: **99.31%**
4471. **`contrib/libsamplerate/samplerate.c`** -> AI Confidence: **99.31%**
4472. **`contrib/libsamplerate/src_linear.c`** -> AI Confidence: **99.31%**
4473. **`contrib/libsamplerate/src_zoh.c`** -> AI Confidence: **99.31%**
4474. **`contrib/libucl/src/ucl_hash.c`** -> AI Confidence: **99.31%**
4475. **`contrib/libucl/src/ucl_schema.c`** -> AI Confidence: **99.31%**
4476. **`contrib/libucl/src/ucl_util.c`** -> AI Confidence: **99.31%**
4477. **`contrib/libucl/tests/test_speed.c`** -> AI Confidence: **99.31%**
4478. **`contrib/libxo/libxo/xo_syslog.c`** -> AI Confidence: **99.31%**
4479. **`contrib/libxo/tests/core/test_05.c`** -> AI Confidence: **99.31%**
4480. **`contrib/libxo/tests/core/test_11.c`** -> AI Confidence: **99.31%**
4481. **`contrib/libxo/tests/gettext/gt_01.c`** -> AI Confidence: **99.31%**
4482. **`contrib/llvm-project/clang/include/clang/Format/Format.h`** -> AI Confidence: **99.31%**
4483. **`contrib/llvm-project/libcxx/include/__algorithm/find.h`** -> AI Confidence: **99.31%**
4484. **`contrib/llvm-project/libcxx/include/__algorithm/fold.h`** -> AI Confidence: **99.31%**
4485. **`contrib/llvm-project/libcxx/include/__algorithm/sample.h`** -> AI Confidence: **99.31%**
4486. **`contrib/llvm-project/libcxx/include/__algorithm/search.h`** -> AI Confidence: **99.31%**
4487. **`contrib/llvm-project/libcxx/include/__algorithm/sort.h`** -> AI Confidence: **99.31%**
4488. **`contrib/llvm-project/libcxx/include/__algorithm/unique.h`** -> AI Confidence: **99.31%**
4489. **`contrib/llvm-project/libcxx/include/__math/hypot.h`** -> AI Confidence: **99.31%**
4490. **`contrib/llvm-project/libcxx/include/__pstl/backends/serial.h`** -> AI Confidence: **99.31%**
4491. **`contrib/llvm-project/libcxx/include/__pstl/cpu_algos/merge.h`** -> AI Confidence: **99.31%**
4492. **`contrib/llvm-project/libcxx/include/__pstl/cpu_algos/transform.h`** -> AI Confidence: **99.31%**
4493. **`contrib/llvm-project/libcxx/include/__ranges/access.h`** -> AI Confidence: **99.31%**
4494. **`contrib/llvm-project/libcxx/include/__ranges/size.h`** -> AI Confidence: **99.31%**
4495. **`contrib/llvm-project/libcxx/include/experimental/__simd/utility.h`** -> AI Confidence: **99.31%**
4496. **`contrib/llvm-project/lldb/tools/compact-unwind/compact-unwind-dumper.c`** -> AI Confidence: **99.31%**
4497. **`contrib/lua/src/lapi.c`** -> AI Confidence: **99.31%**
4498. **`contrib/lua/src/lauxlib.c`** -> AI Confidence: **99.31%**
4499. **`contrib/lua/src/lbaselib.c`** -> AI Confidence: **99.31%**
4500. **`contrib/lua/src/ldblib.c`** -> AI Confidence: **99.31%**
4501. **`contrib/lua/src/ldump.c`** -> AI Confidence: **99.31%**
4502. **`contrib/lua/src/lfunc.c`** -> AI Confidence: **99.31%**
4503. **`contrib/lua/src/liolib.c`** -> AI Confidence: **99.31%**
4504. **`contrib/lua/src/lmathlib.c`** -> AI Confidence: **99.31%**
4505. **`contrib/lua/src/lobject.c`** -> AI Confidence: **99.31%**
4506. **`contrib/lua/src/loslib.c`** -> AI Confidence: **99.31%**
4507. **`contrib/lua/src/lparser.c`** -> AI Confidence: **99.31%**
4508. **`contrib/lua/src/lstring.c`** -> AI Confidence: **99.31%**
4509. **`contrib/lua/src/lstrlib.c`** -> AI Confidence: **99.31%**
4510. **`contrib/lua/src/ltable.c`** -> AI Confidence: **99.31%**
4511. **`contrib/lua/src/lua.c`** -> AI Confidence: **99.31%**
4512. **`contrib/lua/src/lundump.c`** -> AI Confidence: **99.31%**
4513. **`contrib/lua/src/lutf8lib.c`** -> AI Confidence: **99.31%**
4514. **`contrib/lua/src/lzio.c`** -> AI Confidence: **99.31%**
4515. **`contrib/mandoc/cgi.c`** -> AI Confidence: **99.31%**
4516. **`contrib/mandoc/compat_fts.c`** -> AI Confidence: **99.31%**
4517. **`contrib/mandoc/compat_mkstemps.c`** -> AI Confidence: **99.31%**
4518. **`contrib/mandoc/compat_ohash.c`** -> AI Confidence: **99.31%**
4519. **`contrib/mandoc/dba_read.c`** -> AI Confidence: **99.31%**
4520. **`contrib/mandoc/dba_write.c`** -> AI Confidence: **99.31%**
4521. **`contrib/mandoc/dbm.c`** -> AI Confidence: **99.31%**
4522. **`contrib/mandoc/dbm_map.c`** -> AI Confidence: **99.31%**
4523. **`contrib/mandoc/man_html.c`** -> AI Confidence: **99.31%**
4524. **`contrib/mandoc/man_macro.c`** -> AI Confidence: **99.31%**
4525. **`contrib/mandoc/man_term.c`** -> AI Confidence: **99.31%**
4526. **`contrib/mandoc/mandoc.c`** -> AI Confidence: **99.31%**
4527. **`contrib/mandoc/mandocdb.c`** -> AI Confidence: **99.31%**
4528. **`contrib/mandoc/manpath.c`** -> AI Confidence: **99.31%**
4529. **`contrib/mandoc/mansearch.c`** -> AI Confidence: **99.31%**
4530. **`contrib/mandoc/mdoc_argv.c`** -> AI Confidence: **99.31%**
4531. **`contrib/mandoc/mdoc_macro.c`** -> AI Confidence: **99.31%**
4532. **`contrib/mandoc/mdoc_markdown.c`** -> AI Confidence: **99.31%**
4533. **`contrib/mandoc/mdoc_state.c`** -> AI Confidence: **99.31%**
4534. **`contrib/mandoc/roff.c`** -> AI Confidence: **99.31%**
4535. **`contrib/mandoc/roff_term.c`** -> AI Confidence: **99.31%**
4536. **`contrib/mandoc/roff_validate.c`** -> AI Confidence: **99.31%**
4537. **`contrib/mandoc/tbl.c`** -> AI Confidence: **99.31%**
4538. **`contrib/mandoc/term_ps.c`** -> AI Confidence: **99.31%**
4539. **`contrib/mandoc/term_tab.c`** -> AI Confidence: **99.31%**
4540. **`contrib/mandoc/term_tag.c`** -> AI Confidence: **99.31%**
4541. **`contrib/mtree/getid.c`** -> AI Confidence: **99.31%**
4542. **`contrib/mtree/misc.c`** -> AI Confidence: **99.31%**
4543. **`contrib/ncurses/ncurses/tinfo/lib_setup.c`** -> AI Confidence: **99.31%**
4544. **`contrib/ncurses/progs/reset_cmd.c`** -> AI Confidence: **99.31%**
4545. **`contrib/netbsd-tests/crypto/opencrypto/h_aesctr1.c`** -> AI Confidence: **99.31%**
4546. **`contrib/netbsd-tests/crypto/opencrypto/h_aesctr2.c`** -> AI Confidence: **99.31%**
4547. **`contrib/netbsd-tests/crypto/opencrypto/h_arc4.c`** -> AI Confidence: **99.31%**
4548. **`contrib/netbsd-tests/crypto/opencrypto/h_camellia.c`** -> AI Confidence: **99.31%**
4549. **`contrib/netbsd-tests/crypto/opencrypto/h_cbcdes.c`** -> AI Confidence: **99.31%**
4550. **`contrib/netbsd-tests/crypto/opencrypto/h_comp.c`** -> AI Confidence: **99.31%**
4551. **`contrib/netbsd-tests/crypto/opencrypto/h_md5.c`** -> AI Confidence: **99.31%**
4552. **`contrib/netbsd-tests/crypto/opencrypto/h_md5hmac.c`** -> AI Confidence: **99.31%**
4553. **`contrib/netbsd-tests/crypto/opencrypto/h_null.c`** -> AI Confidence: **99.31%**
4554. **`contrib/netbsd-tests/crypto/opencrypto/h_sha1hmac.c`** -> AI Confidence: **99.31%**
4555. **`contrib/netbsd-tests/crypto/opencrypto/h_xcbcmac.c`** -> AI Confidence: **99.31%**
4556. **`contrib/netbsd-tests/dev/dm/h_dm.c`** -> AI Confidence: **99.31%**
4557. **`contrib/netbsd-tests/dev/scsipi/t_cd.c`** -> AI Confidence: **99.31%**
4558. **`contrib/netbsd-tests/dev/sysmon/t_swwdog.c`** -> AI Confidence: **99.31%**
4559. **`contrib/netbsd-tests/fs/common/fstest_nfs.c`** -> AI Confidence: **99.31%**
4560. **`contrib/netbsd-tests/fs/common/fstest_puffs.c`** -> AI Confidence: **99.31%**
4561. **`contrib/netbsd-tests/fs/ffs/t_fifos.c`** -> AI Confidence: **99.31%**
4562. **`contrib/netbsd-tests/fs/ffs/t_mount.c`** -> AI Confidence: **99.31%**
4563. **`contrib/netbsd-tests/fs/kernfs/t_basic.c`** -> AI Confidence: **99.31%**
4564. **`contrib/netbsd-tests/fs/lfs/t_pr.c`** -> AI Confidence: **99.31%**
4565. **`contrib/netbsd-tests/fs/nfs/nfsservice/getmntinfo.c`** -> AI Confidence: **99.31%**
4566. **`contrib/netbsd-tests/fs/nfs/t_mountd.c`** -> AI Confidence: **99.31%**
4567. **`contrib/netbsd-tests/fs/nullfs/t_basic.c`** -> AI Confidence: **99.31%**
4568. **`contrib/netbsd-tests/fs/ptyfs/t_ptyfs.c`** -> AI Confidence: **99.31%**
4569. **`contrib/netbsd-tests/fs/tmpfs/h_tools.c`** -> AI Confidence: **99.31%**
4570. **`contrib/netbsd-tests/fs/tmpfs/t_renamerace.c`** -> AI Confidence: **99.31%**
4571. **`contrib/netbsd-tests/fs/umapfs/t_basic.c`** -> AI Confidence: **99.31%**
4572. **`contrib/netbsd-tests/fs/union/t_pr.c`** -> AI Confidence: **99.31%**
4573. **`contrib/netbsd-tests/fs/vfs/t_mtime_otrunc.c`** -> AI Confidence: **99.31%**
4574. **`contrib/netbsd-tests/fs/vfs/t_renamerace.c`** -> AI Confidence: **99.31%**
4575. **`contrib/netbsd-tests/fs/vfs/t_rmdirrace.c`** -> AI Confidence: **99.31%**
4576. **`contrib/netbsd-tests/fs/vfs/t_vfsops.c`** -> AI Confidence: **99.31%**
4577. **`contrib/netbsd-tests/include/sys/t_socket.c`** -> AI Confidence: **99.31%**
4578. **`contrib/netbsd-tests/kernel/arch/amd64/t_ptrace_wait.c`** -> AI Confidence: **99.31%**
4579. **`contrib/netbsd-tests/kernel/h_ps_strings2.c`** -> AI Confidence: **99.31%**
4580. **`contrib/netbsd-tests/kernel/kqueue/read/t_file.c`** -> AI Confidence: **99.31%**
4581. **`contrib/netbsd-tests/kernel/kqueue/t_proc1.c`** -> AI Confidence: **99.31%**
4582. **`contrib/netbsd-tests/kernel/kqueue/t_vnode.c`** -> AI Confidence: **99.31%**
4583. **`contrib/netbsd-tests/kernel/t_extent.c`** -> AI Confidence: **99.31%**
4584. **`contrib/netbsd-tests/kernel/t_mqueue.c`** -> AI Confidence: **99.31%**
4585. **`contrib/netbsd-tests/kernel/t_pty.c`** -> AI Confidence: **99.31%**
4586. **`contrib/netbsd-tests/kernel/t_rnd.c`** -> AI Confidence: **99.31%**
4587. **`contrib/netbsd-tests/kernel/tty/t_pr.c`** -> AI Confidence: **99.31%**
4588. **`contrib/netbsd-tests/modules/k_helper3/k_helper3.c`** -> AI Confidence: **99.31%**
4589. **`contrib/netbsd-tests/net/bpf/t_bpf.c`** -> AI Confidence: **99.31%**
4590. **`contrib/netbsd-tests/net/config/netconfig.c`** -> AI Confidence: **99.31%**
4591. **`contrib/netbsd-tests/net/fdpass/fdpass.c`** -> AI Confidence: **99.31%**
4592. **`contrib/netbsd-tests/net/icmp/t_forward.c`** -> AI Confidence: **99.31%**
4593. **`contrib/netbsd-tests/net/if/ifconf.c`** -> AI Confidence: **99.31%**
4594. **`contrib/netbsd-tests/net/in_cksum/in_cksum.c`** -> AI Confidence: **99.31%**
4595. **`contrib/netbsd-tests/net/mcast/mcast.c`** -> AI Confidence: **99.31%**
4596. **`contrib/netbsd-tests/net/net/t_pktinfo.c`** -> AI Confidence: **99.31%**
4597. **`contrib/netbsd-tests/net/net/t_tcp.c`** -> AI Confidence: **99.31%**
4598. **`contrib/netbsd-tests/net/net/t_unix.c`** -> AI Confidence: **99.31%**
4599. **`contrib/netbsd-tests/rump/kernspace/alloc.c`** -> AI Confidence: **99.31%**
4600. **`contrib/netbsd-tests/rump/modautoload/t_modautoload.c`** -> AI Confidence: **99.31%**
4601. **`contrib/netbsd-tests/rump/rumpkern/h_client/h_reconcli.c`** -> AI Confidence: **99.31%**
4602. **`contrib/netbsd-tests/rump/rumpkern/h_server/h_simpleserver.c`** -> AI Confidence: **99.31%**
4603. **`contrib/netbsd-tests/rump/rumpkern/t_lwproc.c`** -> AI Confidence: **99.31%**
4604. **`contrib/netbsd-tests/rump/rumpkern/t_modcmd.c`** -> AI Confidence: **99.31%**
4605. **`contrib/netbsd-tests/rump/rumpkern/t_modlinkset.c`** -> AI Confidence: **99.31%**
4606. **`contrib/netbsd-tests/usr.bin/id/pwgr.c`** -> AI Confidence: **99.31%**
4607. **`contrib/ntp/include/isc/mem.h`** -> AI Confidence: **99.31%**
4608. **`contrib/ntp/libntp/authkeys.c`** -> AI Confidence: **99.31%**
4609. **`contrib/ntp/libntp/authreadkeys.c`** -> AI Confidence: **99.31%**
4610. **`contrib/ntp/libntp/icom.c`** -> AI Confidence: **99.31%**
4611. **`contrib/ntp/libntp/libssl_compat.c`** -> AI Confidence: **99.31%**
4612. **`contrib/ntp/libntp/ntp_calgps.c`** -> AI Confidence: **99.31%**
4613. **`contrib/ntp/libntp/ntp_crypto_rnd.c`** -> AI Confidence: **99.31%**
4614. **`contrib/ntp/libntp/ntp_random.c`** -> AI Confidence: **99.31%**
4615. **`contrib/ntp/libntp/ntp_rfc2553.c`** -> AI Confidence: **99.31%**
4616. **`contrib/ntp/libntp/prettydate.c`** -> AI Confidence: **99.31%**
4617. **`contrib/ntp/libntp/recvbuff.c`** -> AI Confidence: **99.31%**
4618. **`contrib/ntp/libntp/snprintf.c`** -> AI Confidence: **99.31%**
4619. **`contrib/ntp/libntp/socket.c`** -> AI Confidence: **99.31%**
4620. **`contrib/ntp/libntp/socktohost.c`** -> AI Confidence: **99.31%**
4621. **`contrib/ntp/libntp/ssl_init.c`** -> AI Confidence: **99.31%**
4622. **`contrib/ntp/libntp/systime.c`** -> AI Confidence: **99.31%**
4623. **`contrib/ntp/libntp/timexsup.c`** -> AI Confidence: **99.31%**
4624. **`contrib/ntp/libntp/work_fork.c`** -> AI Confidence: **99.31%**
4625. **`contrib/ntp/libntp/work_thread.c`** -> AI Confidence: **99.31%**
4626. **`contrib/ntp/libparse/clk_computime.c`** -> AI Confidence: **99.31%**
4627. **`contrib/ntp/libparse/clk_dcf7000.c`** -> AI Confidence: **99.31%**
4628. **`contrib/ntp/libparse/clk_rawdcf.c`** -> AI Confidence: **99.31%**
4629. **`contrib/ntp/libparse/clk_varitext.c`** -> AI Confidence: **99.31%**
4630. **`contrib/ntp/libparse/clk_wharton.c`** -> AI Confidence: **99.31%**
4631. **`contrib/ntp/libparse/parse.c`** -> AI Confidence: **99.31%**
4632. **`contrib/ntp/libparse/parsesolaris.c`** -> AI Confidence: **99.31%**
4633. **`contrib/ntp/libparse/parsestreams.c`** -> AI Confidence: **99.31%**
4634. **`contrib/ntp/ntpd/ntp_clockdev.c`** -> AI Confidence: **99.31%**
4635. **`contrib/ntp/ntpd/ntp_config.c`** -> AI Confidence: **99.31%**
4636. **`contrib/ntp/ntpd/ntp_io.c`** -> AI Confidence: **99.31%**
4637. **`contrib/ntp/ntpd/ntp_leapsec.c`** -> AI Confidence: **99.31%**
4638. **`contrib/ntp/ntpd/ntp_peer.c`** -> AI Confidence: **99.31%**
4639. **`contrib/ntp/ntpd/ntp_refclock.c`** -> AI Confidence: **99.31%**
4640. **`contrib/ntp/ntpd/ntp_restrict.c`** -> AI Confidence: **99.31%**
4641. **`contrib/ntp/ntpd/ntp_util.c`** -> AI Confidence: **99.31%**
4642. **`contrib/ntp/ntpd/ntpd-opts.c`** -> AI Confidence: **99.31%**
4643. **`contrib/ntp/ntpd/ntpd.c`** -> AI Confidence: **99.31%**
4644. **`contrib/ntp/ntpd/refclock_atom.c`** -> AI Confidence: **99.31%**
4645. **`contrib/ntp/ntpd/refclock_chronolog.c`** -> AI Confidence: **99.31%**
4646. **`contrib/ntp/ntpd/refclock_chu.c`** -> AI Confidence: **99.31%**
4647. **`contrib/ntp/ntpd/refclock_hopfser.c`** -> AI Confidence: **99.31%**
4648. **`contrib/ntp/ntpd/refclock_irig.c`** -> AI Confidence: **99.31%**
4649. **`contrib/ntp/ntpd/refclock_leitch.c`** -> AI Confidence: **99.31%**
4650. **`contrib/ntp/ntpd/refclock_local.c`** -> AI Confidence: **99.31%**
4651. **`contrib/ntp/ntpd/refclock_mx4200.c`** -> AI Confidence: **99.31%**
4652. **`contrib/ntp/ntpd/refclock_neoclock4x.c`** -> AI Confidence: **99.31%**
4653. **`contrib/ntp/ntpd/refclock_nmea.c`** -> AI Confidence: **99.31%**
4654. **`contrib/ntp/ntpd/refclock_oncore.c`** -> AI Confidence: **99.31%**
4655. **`contrib/ntp/ntpd/refclock_parse.c`** -> AI Confidence: **99.31%**
4656. **`contrib/ntp/ntpd/refclock_ripencc.c`** -> AI Confidence: **99.31%**
4657. **`contrib/ntp/ntpdc/ntpdc-opts.c`** -> AI Confidence: **99.31%**
4658. **`contrib/ntp/ntpdc/ntpdc.c`** -> AI Confidence: **99.31%**
4659. **`contrib/ntp/ntpdc/ntpdc_ops.c`** -> AI Confidence: **99.31%**
4660. **`contrib/ntp/ntpq/ntpq-opts.c`** -> AI Confidence: **99.31%**
4661. **`contrib/ntp/ntpq/ntpq.c`** -> AI Confidence: **99.31%**
4662. **`contrib/ntp/ntpsnmpd/ntpsnmpd-opts.c`** -> AI Confidence: **99.31%**
4663. **`contrib/ntp/parseutil/testdcf.c`** -> AI Confidence: **99.31%**
4664. **`contrib/ntp/sntp/kod_management.c`** -> AI Confidence: **99.31%**
4665. **`contrib/ntp/sntp/libevent/arc4random.c`** -> AI Confidence: **99.31%**
4666. **`contrib/ntp/sntp/libevent/buffer.c`** -> AI Confidence: **99.31%**
4667. **`contrib/ntp/sntp/libevent/buffer_iocp.c`** -> AI Confidence: **99.31%**
4668. **`contrib/ntp/sntp/libevent/bufferevent_openssl.c`** -> AI Confidence: **99.31%**
4669. **`contrib/ntp/sntp/libevent/bufferevent_ratelim.c`** -> AI Confidence: **99.31%**
4670. **`contrib/ntp/sntp/libevent/epoll_sub.c`** -> AI Confidence: **99.31%**
4671. **`contrib/ntp/sntp/libevent/event_tagging.c`** -> AI Confidence: **99.31%**
4672. **`contrib/ntp/sntp/libevent/evport.c`** -> AI Confidence: **99.31%**
4673. **`contrib/ntp/sntp/libevent/evutil.c`** -> AI Confidence: **99.31%**
4674. **`contrib/ntp/sntp/libevent/include/event2/util.h`** -> AI Confidence: **99.31%**
4675. **`contrib/ntp/sntp/libevent/log.c`** -> AI Confidence: **99.31%**
4676. **`contrib/ntp/sntp/libevent/sample/dns-example.c`** -> AI Confidence: **99.31%**
4677. **`contrib/ntp/sntp/libevent/sample/event-read-fifo.c`** -> AI Confidence: **99.31%**
4678. **`contrib/ntp/sntp/libevent/sample/http-server.c`** -> AI Confidence: **99.31%**
4679. **`contrib/ntp/sntp/libevent/sample/le-proxy.c`** -> AI Confidence: **99.31%**
4680. **`contrib/ntp/sntp/libevent/select.c`** -> AI Confidence: **99.31%**
4681. **`contrib/ntp/sntp/libopts/compat/compat.h`** -> AI Confidence: **99.31%**
4682. **`contrib/ntp/sntp/main.c`** -> AI Confidence: **99.31%**
4683. **`contrib/ntp/sntp/sntp-opts.c`** -> AI Confidence: **99.31%**
4684. **`contrib/ntp/util/lsf-times.c`** -> AI Confidence: **99.31%**
4685. **`contrib/ntp/util/pps-api.c`** -> AI Confidence: **99.31%**
4686. **`contrib/nvi/cl/cl_funcs.c`** -> AI Confidence: **99.31%**
4687. **`contrib/nvi/cl/cl_main.c`** -> AI Confidence: **99.31%**
4688. **`contrib/nvi/cl/cl_screen.c`** -> AI Confidence: **99.31%**
4689. **`contrib/nvi/cl/cl_term.c`** -> AI Confidence: **99.31%**
4690. **`contrib/nvi/common/key.c`** -> AI Confidence: **99.31%**
4691. **`contrib/nvi/common/mark.c`** -> AI Confidence: **99.31%**
4692. **`contrib/nvi/common/options_f.c`** -> AI Confidence: **99.31%**
4693. **`contrib/nvi/common/seq.c`** -> AI Confidence: **99.31%**
4694. **`contrib/nvi/ex/ex_args.c`** -> AI Confidence: **99.31%**
4695. **`contrib/nvi/ex/ex_bang.c`** -> AI Confidence: **99.31%**
4696. **`contrib/nvi/ex/ex_cscope.c`** -> AI Confidence: **99.31%**
4697. **`contrib/nvi/ex/ex_delete.c`** -> AI Confidence: **99.31%**
4698. **`contrib/nvi/ex/ex_display.c`** -> AI Confidence: **99.31%**
4699. **`contrib/nvi/ex/ex_edit.c`** -> AI Confidence: **99.31%**
4700. **`contrib/nvi/ex/ex_equal.c`** -> AI Confidence: **99.31%**
4701. **`contrib/nvi/ex/ex_file.c`** -> AI Confidence: **99.31%**
4702. **`contrib/nvi/ex/ex_preserve.c`** -> AI Confidence: **99.31%**
4703. **`contrib/nvi/ex/ex_print.c`** -> AI Confidence: **99.31%**
4704. **`contrib/nvi/ex/ex_put.c`** -> AI Confidence: **99.31%**
4705. **`contrib/nvi/ex/ex_quit.c`** -> AI Confidence: **99.31%**
4706. **`contrib/nvi/ex/ex_screen.c`** -> AI Confidence: **99.31%**
4707. **`contrib/nvi/ex/ex_script.c`** -> AI Confidence: **99.31%**
4708. **`contrib/nvi/ex/ex_shell.c`** -> AI Confidence: **99.31%**
4709. **`contrib/nvi/ex/ex_source.c`** -> AI Confidence: **99.31%**
4710. **`contrib/nvi/ex/ex_stop.c`** -> AI Confidence: **99.31%**
4711. **`contrib/nvi/ex/ex_write.c`** -> AI Confidence: **99.31%**
4712. **`contrib/nvi/ex/ex_yank.c`** -> AI Confidence: **99.31%**
4713. **`contrib/nvi/ex/ex_z.c`** -> AI Confidence: **99.31%**
4714. **`contrib/nvi/regex/regexec.c`** -> AI Confidence: **99.31%**
4715. **`contrib/nvi/vi/v_at.c`** -> AI Confidence: **99.31%**
4716. **`contrib/nvi/vi/v_ch.c`** -> AI Confidence: **99.31%**
4717. **`contrib/nvi/vi/v_delete.c`** -> AI Confidence: **99.31%**
4718. **`contrib/nvi/vi/v_ex.c`** -> AI Confidence: **99.31%**
4719. **`contrib/nvi/vi/v_init.c`** -> AI Confidence: **99.31%**
4720. **`contrib/nvi/vi/v_mark.c`** -> AI Confidence: **99.31%**
4721. **`contrib/nvi/vi/v_screen.c`** -> AI Confidence: **99.31%**
4722. **`contrib/nvi/vi/v_scroll.c`** -> AI Confidence: **99.31%**
4723. **`contrib/nvi/vi/v_z.c`** -> AI Confidence: **99.31%**
4724. **`contrib/nvi/vi/v_zexit.c`** -> AI Confidence: **99.31%**
4725. **`contrib/nvi/vi/vs_msg.c`** -> AI Confidence: **99.31%**
4726. **`contrib/nvi/vi/vs_relative.c`** -> AI Confidence: **99.31%**
4727. **`contrib/ofed/infiniband-diags/src/ibcacheedit.c`** -> AI Confidence: **99.31%**
4728. **`contrib/ofed/infiniband-diags/src/ibccconfig.c`** -> AI Confidence: **99.31%**
4729. **`contrib/ofed/infiniband-diags/src/ibccquery.c`** -> AI Confidence: **99.31%**
4730. **`contrib/ofed/infiniband-diags/src/mcm_rereg_test.c`** -> AI Confidence: **99.31%**
4731. **`contrib/ofed/infiniband-diags/src/rdma-ndd.c`** -> AI Confidence: **99.31%**
4732. **`contrib/ofed/infiniband-diags/src/saquery.c`** -> AI Confidence: **99.31%**
4733. **`contrib/ofed/infiniband-diags/src/smpdump.c`** -> AI Confidence: **99.31%**
4734. **`contrib/ofed/infiniband-diags/src/smpquery.c`** -> AI Confidence: **99.31%**
4735. **`contrib/ofed/infiniband-diags/src/vendstat.c`** -> AI Confidence: **99.31%**
4736. **`contrib/ofed/libcxgb4/dev.c`** -> AI Confidence: **99.31%**
4737. **`contrib/ofed/libcxgb4/qp.c`** -> AI Confidence: **99.31%**
4738. **`contrib/ofed/libibmad/cc.c`** -> AI Confidence: **99.31%**
4739. **`contrib/ofed/libibmad/gs.c`** -> AI Confidence: **99.31%**
4740. **`contrib/ofed/libibmad/register.c`** -> AI Confidence: **99.31%**
4741. **`contrib/ofed/libibmad/resolve.c`** -> AI Confidence: **99.31%**
4742. **`contrib/ofed/libibmad/rpc.c`** -> AI Confidence: **99.31%**
4743. **`contrib/ofed/libibnetdisc/ibnetdisc.c`** -> AI Confidence: **99.31%**
4744. **`contrib/ofed/libibnetdisc/ibnetdisc_cache.c`** -> AI Confidence: **99.31%**
4745. **`contrib/ofed/libibumad/sysfs.c`** -> AI Confidence: **99.31%**
4746. **`contrib/ofed/libibumad/umad.c`** -> AI Confidence: **99.31%**
4747. **`contrib/ofed/libibumad/umad_str.c`** -> AI Confidence: **99.31%**
4748. **`contrib/ofed/libibverbs/device.c`** -> AI Confidence: **99.31%**
4749. **`contrib/ofed/libibverbs/examples/devinfo.c`** -> AI Confidence: **99.31%**
4750. **`contrib/ofed/libibverbs/examples/rc_pingpong.c`** -> AI Confidence: **99.31%**
4751. **`contrib/ofed/libibverbs/examples/srq_pingpong.c`** -> AI Confidence: **99.31%**
4752. **`contrib/ofed/libibverbs/examples/uc_pingpong.c`** -> AI Confidence: **99.31%**
4753. **`contrib/ofed/libibverbs/examples/ud_pingpong.c`** -> AI Confidence: **99.31%**
4754. **`contrib/ofed/libibverbs/examples/xsrq_pingpong.c`** -> AI Confidence: **99.31%**
4755. **`contrib/ofed/libibverbs/init.c`** -> AI Confidence: **99.31%**
4756. **`contrib/ofed/libibverbs/memory.c`** -> AI Confidence: **99.31%**
4757. **`contrib/ofed/libibverbs/sysfs.c`** -> AI Confidence: **99.31%**
4758. **`contrib/ofed/libmlx4/cq.c`** -> AI Confidence: **99.31%**
4759. **`contrib/ofed/libmlx4/mlx4.c`** -> AI Confidence: **99.31%**
4760. **`contrib/ofed/libmlx4/qp.c`** -> AI Confidence: **99.31%**
4761. **`contrib/ofed/libmlx5/buf.c`** -> AI Confidence: **99.31%**
4762. **`contrib/ofed/libmlx5/cq.c`** -> AI Confidence: **99.31%**
4763. **`contrib/ofed/libmlx5/mlx5.c`** -> AI Confidence: **99.31%**
4764. **`contrib/ofed/libmlx5/qp.c`** -> AI Confidence: **99.31%**
4765. **`contrib/ofed/librdmacm/acm.c`** -> AI Confidence: **99.31%**
4766. **`contrib/ofed/librdmacm/addrinfo.c`** -> AI Confidence: **99.31%**
4767. **`contrib/ofed/librdmacm/cma.c`** -> AI Confidence: **99.31%**
4768. **`contrib/ofed/librdmacm/examples/cmatose.c`** -> AI Confidence: **99.31%**
4769. **`contrib/ofed/librdmacm/examples/cmtime.c`** -> AI Confidence: **99.31%**
4770. **`contrib/ofed/librdmacm/examples/common.c`** -> AI Confidence: **99.31%**
4771. **`contrib/ofed/librdmacm/examples/common.h`** -> AI Confidence: **99.31%**
4772. **`contrib/ofed/librdmacm/examples/mckey.c`** -> AI Confidence: **99.31%**
4773. **`contrib/ofed/librdmacm/examples/rcopy.c`** -> AI Confidence: **99.31%**
4774. **`contrib/ofed/librdmacm/examples/rdma_xclient.c`** -> AI Confidence: **99.31%**
4775. **`contrib/ofed/librdmacm/examples/rdma_xserver.c`** -> AI Confidence: **99.31%**
4776. **`contrib/ofed/librdmacm/examples/rping.c`** -> AI Confidence: **99.31%**
4777. **`contrib/ofed/librdmacm/examples/udaddy.c`** -> AI Confidence: **99.31%**
4778. **`contrib/ofed/librdmacm/examples/udpong.c`** -> AI Confidence: **99.31%**
4779. **`contrib/ofed/librdmacm/preload.c`** -> AI Confidence: **99.31%**
4780. **`contrib/ofed/librdmacm/rsocket.c`** -> AI Confidence: **99.31%**
4781. **`contrib/ofed/opensm/opensm/osm_console_io.c`** -> AI Confidence: **99.31%**
4782. **`contrib/ofed/opensm/opensm/osm_db_files.c`** -> AI Confidence: **99.31%**
4783. **`contrib/ofed/opensm/opensm/osm_guid_info_rcv.c`** -> AI Confidence: **99.31%**
4784. **`contrib/ofed/opensm/opensm/osm_guid_mgr.c`** -> AI Confidence: **99.31%**
4785. **`contrib/ofed/opensm/opensm/osm_mad_pool.c`** -> AI Confidence: **99.31%**
4786. **`contrib/ofed/opensm/opensm/osm_mcast_tbl.c`** -> AI Confidence: **99.31%**
4787. **`contrib/ofed/opensm/opensm/osm_multicast.c`** -> AI Confidence: **99.31%**
4788. **`contrib/ofed/opensm/opensm/osm_node_desc_rcv.c`** -> AI Confidence: **99.31%**
4789. **`contrib/ofed/opensm/opensm/osm_opensm.c`** -> AI Confidence: **99.31%**
4790. **`contrib/ofed/opensm/opensm/osm_sa.c`** -> AI Confidence: **99.31%**
4791. **`contrib/ofed/opensm/opensm/osm_sa_lft_record.c`** -> AI Confidence: **99.31%**
4792. **`contrib/ofed/opensm/opensm/osm_sa_mft_record.c`** -> AI Confidence: **99.31%**
4793. **`contrib/ofed/opensm/opensm/osm_sa_vlarb_record.c`** -> AI Confidence: **99.31%**
4794. **`contrib/ofed/opensm/opensm/osm_sm.c`** -> AI Confidence: **99.31%**
4795. **`contrib/ofed/opensm/opensm/osm_state_mgr.c`** -> AI Confidence: **99.31%**
4796. **`contrib/ofed/opensm/opensm/osm_subnet.c`** -> AI Confidence: **99.31%**
4797. **`contrib/ofed/opensm/opensm/osm_torus.c`** -> AI Confidence: **99.31%**
4798. **`contrib/ofed/opensm/opensm/osm_ucast_dnup.c`** -> AI Confidence: **99.31%**
4799. **`contrib/ofed/opensm/opensm/osm_ucast_ftree.c`** -> AI Confidence: **99.31%**
4800. **`contrib/ofed/opensm/opensm/osm_ucast_mgr.c`** -> AI Confidence: **99.31%**
4801. **`contrib/ofed/opensm/opensm/osm_ucast_updn.c`** -> AI Confidence: **99.31%**
4802. **`contrib/openbsm/bin/auditd/auditd_darwin.c`** -> AI Confidence: **99.31%**
4803. **`contrib/openbsm/bin/auditd/auditd_fbsd.c`** -> AI Confidence: **99.31%**
4804. **`contrib/openbsm/bin/auditdistd/pjdlog.c`** -> AI Confidence: **99.31%**
4805. **`contrib/openbsm/bin/auditdistd/proto_common.c`** -> AI Confidence: **99.31%**
4806. **`contrib/openbsm/bin/auditdistd/proto_socketpair.c`** -> AI Confidence: **99.31%**
4807. **`contrib/openbsm/bin/auditdistd/proto_tcp.c`** -> AI Confidence: **99.31%**
4808. **`contrib/openbsm/bin/auditdistd/proto_tls.c`** -> AI Confidence: **99.31%**
4809. **`contrib/openbsm/bin/auditdistd/receiver.c`** -> AI Confidence: **99.31%**
4810. **`contrib/openbsm/bin/auditdistd/sender.c`** -> AI Confidence: **99.31%**
4811. **`contrib/openbsm/bin/auditdistd/trail.c`** -> AI Confidence: **99.31%**
4812. **`contrib/openbsm/compat/pidfile.h`** -> AI Confidence: **99.31%**
4813. **`contrib/openbsm/libbsm/bsm_audit.c`** -> AI Confidence: **99.31%**
4814. **`contrib/openbsm/libbsm/bsm_control.c`** -> AI Confidence: **99.31%**
4815. **`contrib/openbsm/libbsm/bsm_mask.c`** -> AI Confidence: **99.31%**
4816. **`contrib/openbsm/libbsm/bsm_notify.c`** -> AI Confidence: **99.31%**
4817. **`contrib/openpam/bin/openpam_dump_policy/openpam_dump_policy.c`** -> AI Confidence: **99.31%**
4818. **`contrib/openpam/t/t_openpam_dispatch.c`** -> AI Confidence: **99.31%**
4819. **`contrib/openpam/t/t_openpam_straddch.c`** -> AI Confidence: **99.31%**
4820. **`contrib/pam-krb5/module/cache.c`** -> AI Confidence: **99.31%**
4821. **`contrib/pam-krb5/module/context.c`** -> AI Confidence: **99.31%**
4822. **`contrib/pam-krb5/module/fast.c`** -> AI Confidence: **99.31%**
4823. **`contrib/pam-krb5/module/prompting.c`** -> AI Confidence: **99.31%**
4824. **`contrib/pam-krb5/module/support.c`** -> AI Confidence: **99.31%**
4825. **`contrib/pam-krb5/pam-util/logging.c`** -> AI Confidence: **99.31%**
4826. **`contrib/pam-krb5/tests/fakepam/kuserok.c`** -> AI Confidence: **99.31%**
4827. **`contrib/pam-krb5/tests/fakepam/script.c`** -> AI Confidence: **99.31%**
4828. **`contrib/pam-krb5/tests/module/expired-t.c`** -> AI Confidence: **99.31%**
4829. **`contrib/pam-krb5/tests/pam-util/logging-t.c`** -> AI Confidence: **99.31%**
4830. **`contrib/pam-krb5/tests/tap/basic.c`** -> AI Confidence: **99.31%**
4831. **`contrib/pam-krb5/tests/tap/kadmin.c`** -> AI Confidence: **99.31%**
4832. **`contrib/pf/ftp-proxy/filter.c`** -> AI Confidence: **99.31%**
4833. **`contrib/pf/ftp-proxy/ftp-proxy.c`** -> AI Confidence: **99.31%**
4834. **`contrib/pf/libevent/buffer.c`** -> AI Confidence: **99.31%**
4835. **`contrib/pf/libevent/evbuffer.c`** -> AI Confidence: **99.31%**
4836. **`contrib/pf/libevent/log.c`** -> AI Confidence: **99.31%**
4837. **`contrib/pf/pflogd/pflogd.c`** -> AI Confidence: **99.31%**
4838. **`contrib/pf/pflogd/pidfile.c`** -> AI Confidence: **99.31%**
4839. **`contrib/pf/pflogd/privsep.c`** -> AI Confidence: **99.31%**
4840. **`contrib/pf/tftp-proxy/filter.c`** -> AI Confidence: **99.31%**
4841. **`contrib/pnglite/pnglite.c`** -> AI Confidence: **99.31%**
4842. **`contrib/processor-trace/libipt/src/pt_block_decoder.c`** -> AI Confidence: **99.31%**
4843. **`contrib/processor-trace/libipt/src/pt_ild.c`** -> AI Confidence: **99.31%**
4844. **`contrib/processor-trace/libipt/src/pt_insn_decoder.c`** -> AI Confidence: **99.31%**
4845. **`contrib/processor-trace/libipt/src/pt_query_decoder.c`** -> AI Confidence: **99.31%**
4846. **`contrib/processor-trace/libipt/src/pt_section.c`** -> AI Confidence: **99.31%**
4847. **`contrib/sendmail/libsm/assert.c`** -> AI Confidence: **99.31%**
4848. **`contrib/sendmail/libsm/b-strcmp.c`** -> AI Confidence: **99.31%**
4849. **`contrib/sendmail/libsm/clock.c`** -> AI Confidence: **99.31%**
4850. **`contrib/sendmail/libsm/debug.c`** -> AI Confidence: **99.31%**
4851. **`contrib/sendmail/libsm/errstring.c`** -> AI Confidence: **99.31%**
4852. **`contrib/sendmail/libsm/fclose.c`** -> AI Confidence: **99.31%**
4853. **`contrib/sendmail/libsm/findfp.c`** -> AI Confidence: **99.31%**
4854. **`contrib/sendmail/libsm/fpos.c`** -> AI Confidence: **99.31%**
4855. **`contrib/sendmail/libsm/heap.c`** -> AI Confidence: **99.31%**
4856. **`contrib/sendmail/libsm/mbdb.c`** -> AI Confidence: **99.31%**
4857. **`contrib/sendmail/libsm/memstat.c`** -> AI Confidence: **99.31%**
4858. **`contrib/sendmail/libsm/niprop.c`** -> AI Confidence: **99.31%**
4859. **`contrib/sendmail/libsm/notify.c`** -> AI Confidence: **99.31%**
4860. **`contrib/sendmail/libsm/rpool.c`** -> AI Confidence: **99.31%**
4861. **`contrib/sendmail/libsm/sem.c`** -> AI Confidence: **99.31%**
4862. **`contrib/sendmail/libsm/shm.c`** -> AI Confidence: **99.31%**
4863. **`contrib/sendmail/libsm/smstdio.c`** -> AI Confidence: **99.31%**
4864. **`contrib/sendmail/libsm/stdio.c`** -> AI Confidence: **99.31%**
4865. **`contrib/sendmail/libsm/strerror.c`** -> AI Confidence: **99.31%**
4866. **`contrib/sendmail/libsm/stringf.c`** -> AI Confidence: **99.31%**
4867. **`contrib/sendmail/libsm/strio.c`** -> AI Confidence: **99.31%**
4868. **`contrib/sendmail/libsm/t-ixlen.c`** -> AI Confidence: **99.31%**
4869. **`contrib/sendmail/libsm/t-sem.c`** -> AI Confidence: **99.31%**
4870. **`contrib/sendmail/libsm/t-shm.c`** -> AI Confidence: **99.31%**
4871. **`contrib/sendmail/libsmdb/smcdb.c`** -> AI Confidence: **99.31%**
4872. **`contrib/sendmail/mailstats/mailstats.c`** -> AI Confidence: **99.31%**
4873. **`contrib/sendmail/rmail/rmail.c`** -> AI Confidence: **99.31%**
4874. **`contrib/sendmail/smrsh/smrsh.c`** -> AI Confidence: **99.31%**
4875. **`contrib/sendmail/src/bf.c`** -> AI Confidence: **99.31%**
4876. **`contrib/sendmail/src/main.c`** -> AI Confidence: **99.31%**
4877. **`contrib/sendmail/src/queue.c`** -> AI Confidence: **99.31%**
4878. **`contrib/sendmail/src/sfsasl.c`** -> AI Confidence: **99.31%**
4879. **`contrib/sendmail/vacation/vacation.c`** -> AI Confidence: **99.31%**
4880. **`contrib/smbfs/smbutil/dumptree.c`** -> AI Confidence: **99.31%**
4881. **`contrib/smbfs/smbutil/lookup.c`** -> AI Confidence: **99.31%**
4882. **`contrib/smbfs/smbutil/smbutil.c`** -> AI Confidence: **99.31%**
4883. **`contrib/tcp_wrappers/fix_options.c`** -> AI Confidence: **99.31%**
4884. **`contrib/tcp_wrappers/hosts_access.c`** -> AI Confidence: **99.31%**
4885. **`contrib/tcp_wrappers/ncr.c`** -> AI Confidence: **99.31%**
4886. **`contrib/tcp_wrappers/options.c`** -> AI Confidence: **99.31%**
4887. **`contrib/tcp_wrappers/ptx.c`** -> AI Confidence: **99.31%**
4888. **`contrib/tcp_wrappers/rfc931.c`** -> AI Confidence: **99.31%**
4889. **`contrib/tcp_wrappers/shell_cmd.c`** -> AI Confidence: **99.31%**
4890. **`contrib/tcp_wrappers/tcpd.c`** -> AI Confidence: **99.31%**
4891. **`contrib/tcp_wrappers/workarounds.c`** -> AI Confidence: **99.31%**
4892. **`contrib/tcpdump/addrtoname.c`** -> AI Confidence: **99.31%**
4893. **`contrib/tcpdump/missing/getopt_long.c`** -> AI Confidence: **99.31%**
4894. **`contrib/tcpdump/parsenfsfh.c`** -> AI Confidence: **99.31%**
4895. **`contrib/tcpdump/print-atalk.c`** -> AI Confidence: **99.31%**
4896. **`contrib/tcpdump/print-atm.c`** -> AI Confidence: **99.31%**
4897. **`contrib/tcpdump/print-cnfp.c`** -> AI Confidence: **99.31%**
4898. **`contrib/tcpdump/print-dccp.c`** -> AI Confidence: **99.31%**
4899. **`contrib/tcpdump/print-esp.c`** -> AI Confidence: **99.31%**
4900. **`contrib/tcpdump/print-icmp.c`** -> AI Confidence: **99.31%**
4901. **`contrib/tcpdump/print-lisp.c`** -> AI Confidence: **99.31%**
4902. **`contrib/tcpdump/print-llc.c`** -> AI Confidence: **99.31%**
4903. **`contrib/tcpdump/print-lspping.c`** -> AI Confidence: **99.31%**
4904. **`contrib/tcpdump/print-openflow-1.0.c`** -> AI Confidence: **99.31%**
4905. **`contrib/tcpdump/print-ospf6.c`** -> AI Confidence: **99.31%**
4906. **`contrib/tcpdump/print-radius.c`** -> AI Confidence: **99.31%**
4907. **`contrib/tcpdump/print-sl.c`** -> AI Confidence: **99.31%**
4908. **`contrib/tcpdump/print-tcp.c`** -> AI Confidence: **99.31%**
4909. **`contrib/tcpdump/print-zephyr.c`** -> AI Confidence: **99.31%**
4910. **`contrib/tcpdump/print.c`** -> AI Confidence: **99.31%**
4911. **`contrib/tcpdump/smbutil.c`** -> AI Confidence: **99.31%**
4912. **`contrib/tcpdump/util-print.c`** -> AI Confidence: **99.31%**
4913. **`contrib/tcsh/tc.func.c`** -> AI Confidence: **99.31%**
4914. **`contrib/tcsh/tc.os.c`** -> AI Confidence: **99.31%**
4915. **`contrib/telnet/libtelnet/auth.c`** -> AI Confidence: **99.31%**
4916. **`contrib/telnet/libtelnet/enc_des.c`** -> AI Confidence: **99.31%**
4917. **`contrib/telnet/libtelnet/encrypt.c`** -> AI Confidence: **99.31%**
4918. **`contrib/telnet/libtelnet/krb4encpwd.c`** -> AI Confidence: **99.31%**
4919. **`contrib/telnet/libtelnet/pk.c`** -> AI Confidence: **99.31%**
4920. **`contrib/telnet/libtelnet/rsaencpwd.c`** -> AI Confidence: **99.31%**
4921. **`contrib/telnet/libtelnet/sra.c`** -> AI Confidence: **99.31%**
4922. **`contrib/telnet/telnet/authenc.c`** -> AI Confidence: **99.31%**
4923. **`contrib/telnet/telnet/commands.c`** -> AI Confidence: **99.31%**
4924. **`contrib/telnet/telnet/network.c`** -> AI Confidence: **99.31%**
4925. **`contrib/telnet/telnet/ring.c`** -> AI Confidence: **99.31%**
4926. **`contrib/tnftp/src/complete.c`** -> AI Confidence: **99.31%**
4927. **`contrib/tzcode/localtime.c`** -> AI Confidence: **99.31%**
4928. **`contrib/unbound/cachedb/cachedb.c`** -> AI Confidence: **99.31%**
4929. **`contrib/unbound/cachedb/redis.c`** -> AI Confidence: **99.31%**
4930. **`contrib/unbound/compat/arc4random.c`** -> AI Confidence: **99.31%**
4931. **`contrib/unbound/compat/getentropy_linux.c`** -> AI Confidence: **99.31%**
4932. **`contrib/unbound/compat/getentropy_osx.c`** -> AI Confidence: **99.31%**
4933. **`contrib/unbound/compat/getentropy_solaris.c`** -> AI Confidence: **99.31%**
4934. **`contrib/unbound/config.h.in`** -> AI Confidence: **99.31%**
4935. **`contrib/unbound/daemon/remote.c`** -> AI Confidence: **99.31%**
4936. **`contrib/unbound/daemon/stats.c`** -> AI Confidence: **99.31%**
4937. **`contrib/unbound/daemon/worker.c`** -> AI Confidence: **99.31%**
4938. **`contrib/unbound/dnstap/dtstream.c`** -> AI Confidence: **99.31%**
4939. **`contrib/unbound/iterator/iter_hints.c`** -> AI Confidence: **99.31%**
4940. **`contrib/unbound/iterator/iter_resptype.c`** -> AI Confidence: **99.31%**
4941. **`contrib/unbound/iterator/iter_scrub.c`** -> AI Confidence: **99.31%**
4942. **`contrib/unbound/iterator/iter_utils.c`** -> AI Confidence: **99.31%**
4943. **`contrib/unbound/iterator/iterator.c`** -> AI Confidence: **99.31%**
4944. **`contrib/unbound/libunbound/libunbound.c`** -> AI Confidence: **99.31%**
4945. **`contrib/unbound/respip/respip.c`** -> AI Confidence: **99.31%**
4946. **`contrib/unbound/services/authzone.c`** -> AI Confidence: **99.31%**
4947. **`contrib/unbound/services/listen_dnsport.c`** -> AI Confidence: **99.31%**
4948. **`contrib/unbound/services/mesh.c`** -> AI Confidence: **99.31%**
4949. **`contrib/unbound/services/modstack.c`** -> AI Confidence: **99.31%**
4950. **`contrib/unbound/services/outside_network.c`** -> AI Confidence: **99.31%**
4951. **`contrib/unbound/services/rpz.c`** -> AI Confidence: **99.31%**
4952. **`contrib/unbound/sldns/keyraw.c`** -> AI Confidence: **99.31%**
4953. **`contrib/unbound/sldns/str2wire.c`** -> AI Confidence: **99.31%**
4954. **`contrib/unbound/sldns/wire2str.c`** -> AI Confidence: **99.31%**
4955. **`contrib/unbound/smallapp/unbound-anchor.c`** -> AI Confidence: **99.31%**
4956. **`contrib/unbound/testcode/testbound.c`** -> AI Confidence: **99.31%**
4957. **`contrib/unbound/testcode/unitneg.c`** -> AI Confidence: **99.31%**
4958. **`contrib/unbound/testcode/unitverify.c`** -> AI Confidence: **99.31%**
4959. **`contrib/unbound/testcode/unitzonemd.c`** -> AI Confidence: **99.31%**
4960. **`contrib/unbound/util/data/dname.c`** -> AI Confidence: **99.31%**
4961. **`contrib/unbound/util/data/msgencode.c`** -> AI Confidence: **99.31%**
4962. **`contrib/unbound/util/data/msgparse.c`** -> AI Confidence: **99.31%**
4963. **`contrib/unbound/util/fptr_wlist.c`** -> AI Confidence: **99.31%**
4964. **`contrib/unbound/util/log.c`** -> AI Confidence: **99.31%**
4965. **`contrib/unbound/util/module.c`** -> AI Confidence: **99.31%**
4966. **`contrib/unbound/util/net_help.c`** -> AI Confidence: **99.31%**
4967. **`contrib/unbound/validator/autotrust.c`** -> AI Confidence: **99.31%**
4968. **`contrib/unbound/validator/val_anchor.c`** -> AI Confidence: **99.31%**
4969. **`contrib/unbound/validator/val_nsec.c`** -> AI Confidence: **99.31%**
4970. **`contrib/unbound/validator/val_secalgo.c`** -> AI Confidence: **99.31%**
4971. **`contrib/unbound/validator/val_sigcrypt.c`** -> AI Confidence: **99.31%**
4972. **`contrib/unbound/validator/val_utils.c`** -> AI Confidence: **99.31%**
4973. **`contrib/unbound/validator/validator.c`** -> AI Confidence: **99.31%**
4974. **`contrib/unbound/winrc/win_svc.c`** -> AI Confidence: **99.31%**
4975. **`contrib/wireguard-tools/config.c`** -> AI Confidence: **99.31%**
4976. **`contrib/wireguard-tools/genkey.c`** -> AI Confidence: **99.31%**
4977. **`contrib/wireguard-tools/ipc.c`** -> AI Confidence: **99.31%**
4978. **`contrib/wireguard-tools/terminal.c`** -> AI Confidence: **99.31%**
4979. **`contrib/wpa/hostapd/ctrl_iface.c`** -> AI Confidence: **99.31%**
4980. **`contrib/wpa/hs20/client/oma_dm_client.c`** -> AI Confidence: **99.31%**
4981. **`contrib/wpa/hs20/client/spp_client.c`** -> AI Confidence: **99.31%**
4982. **`contrib/wpa/src/ap/accounting.c`** -> AI Confidence: **99.31%**
4983. **`contrib/wpa/src/ap/airtime_policy.c`** -> AI Confidence: **99.31%**
4984. **`contrib/wpa/src/ap/ap_config.c`** -> AI Confidence: **99.31%**
4985. **`contrib/wpa/src/ap/ap_drv_ops.c`** -> AI Confidence: **99.31%**
4986. **`contrib/wpa/src/ap/ap_list.c`** -> AI Confidence: **99.31%**
4987. **`contrib/wpa/src/ap/authsrv.c`** -> AI Confidence: **99.31%**
4988. **`contrib/wpa/src/ap/beacon.c`** -> AI Confidence: **99.31%**
4989. **`contrib/wpa/src/ap/comeback_token.c`** -> AI Confidence: **99.31%**
4990. **`contrib/wpa/src/ap/ctrl_iface_ap.c`** -> AI Confidence: **99.31%**
4991. **`contrib/wpa/src/ap/dfs.c`** -> AI Confidence: **99.31%**
4992. **`contrib/wpa/src/ap/dhcp_snoop.c`** -> AI Confidence: **99.31%**
4993. **`contrib/wpa/src/ap/dpp_hostapd.c`** -> AI Confidence: **99.31%**
4994. **`contrib/wpa/src/ap/fils_hlp.c`** -> AI Confidence: **99.31%**
4995. **`contrib/wpa/src/ap/gas_serv.c`** -> AI Confidence: **99.31%**
4996. **`contrib/wpa/src/ap/hostapd.c`** -> AI Confidence: **99.31%**
4997. **`contrib/wpa/src/ap/hs20.c`** -> AI Confidence: **99.31%**
4998. **`contrib/wpa/src/ap/hw_features.c`** -> AI Confidence: **99.31%**
4999. **`contrib/wpa/src/ap/ieee802_11.c`** -> AI Confidence: **99.31%**
5000. **`contrib/wpa/src/ap/ieee802_11_auth.c`** -> AI Confidence: **99.31%**
5001. **`contrib/wpa/src/ap/ieee802_11_eht.c`** -> AI Confidence: **99.31%**
5002. **`contrib/wpa/src/ap/ieee802_11_he.c`** -> AI Confidence: **99.31%**
5003. **`contrib/wpa/src/ap/ieee802_11_ht.c`** -> AI Confidence: **99.31%**
5004. **`contrib/wpa/src/ap/ieee802_11_shared.c`** -> AI Confidence: **99.31%**
5005. **`contrib/wpa/src/ap/ieee802_11_vht.c`** -> AI Confidence: **99.31%**
5006. **`contrib/wpa/src/ap/ieee802_1x.c`** -> AI Confidence: **99.31%**
5007. **`contrib/wpa/src/ap/mbo_ap.c`** -> AI Confidence: **99.31%**
5008. **`contrib/wpa/src/ap/pmksa_cache_auth.c`** -> AI Confidence: **99.31%**
5009. **`contrib/wpa/src/ap/rrm.c`** -> AI Confidence: **99.31%**
5010. **`contrib/wpa/src/ap/sta_info.c`** -> AI Confidence: **99.31%**
5011. **`contrib/wpa/src/ap/vlan_full.c`** -> AI Confidence: **99.31%**
5012. **`contrib/wpa/src/ap/vlan_init.c`** -> AI Confidence: **99.31%**
5013. **`contrib/wpa/src/ap/wnm_ap.c`** -> AI Confidence: **99.31%**
5014. **`contrib/wpa/src/ap/wpa_auth.c`** -> AI Confidence: **99.31%**
5015. **`contrib/wpa/src/ap/wpa_auth_ft.c`** -> AI Confidence: **99.31%**
5016. **`contrib/wpa/src/ap/wpa_auth_glue.c`** -> AI Confidence: **99.31%**
5017. **`contrib/wpa/src/ap/wps_hostapd.c`** -> AI Confidence: **99.31%**
5018. **`contrib/wpa/src/common/dpp.c`** -> AI Confidence: **99.31%**
5019. **`contrib/wpa/src/common/dpp_backup.c`** -> AI Confidence: **99.31%**
5020. **`contrib/wpa/src/common/dpp_crypto.c`** -> AI Confidence: **99.31%**
5021. **`contrib/wpa/src/common/nan_de.c`** -> AI Confidence: **99.31%**
5022. **`contrib/wpa/src/common/sae.c`** -> AI Confidence: **99.31%**
5023. **`contrib/wpa/src/common/sae_pk.c`** -> AI Confidence: **99.31%**
5024. **`contrib/wpa/src/common/wpa_common.c`** -> AI Confidence: **99.31%**
5025. **`contrib/wpa/src/common/wpa_ctrl.c`** -> AI Confidence: **99.31%**
5026. **`contrib/wpa/src/crypto/crypto_gnutls.c`** -> AI Confidence: **99.31%**
5027. **`contrib/wpa/src/crypto/crypto_internal.c`** -> AI Confidence: **99.31%**
5028. **`contrib/wpa/src/crypto/crypto_openssl.c`** -> AI Confidence: **99.31%**
5029. **`contrib/wpa/src/crypto/crypto_wolfssl.c`** -> AI Confidence: **99.31%**
5030. **`contrib/wpa/src/crypto/random.c`** -> AI Confidence: **99.31%**
5031. **`contrib/wpa/src/crypto/tls_gnutls.c`** -> AI Confidence: **99.31%**
5032. **`contrib/wpa/src/crypto/tls_openssl.c`** -> AI Confidence: **99.31%**
5033. **`contrib/wpa/src/crypto/tls_openssl_ocsp.c`** -> AI Confidence: **99.31%**
5034. **`contrib/wpa/src/crypto/tls_wolfssl.c`** -> AI Confidence: **99.31%**
5035. **`contrib/wpa/src/drivers/driver_atheros.c`** -> AI Confidence: **99.31%**
5036. **`contrib/wpa/src/drivers/driver_bsd.c`** -> AI Confidence: **99.31%**
5037. **`contrib/wpa/src/drivers/driver_ndis.c`** -> AI Confidence: **99.31%**
5038. **`contrib/wpa/src/drivers/driver_nl80211.c`** -> AI Confidence: **99.31%**
5039. **`contrib/wpa/src/drivers/driver_nl80211_capa.c`** -> AI Confidence: **99.31%**
5040. **`contrib/wpa/src/drivers/driver_nl80211_event.c`** -> AI Confidence: **99.31%**
5041. **`contrib/wpa/src/drivers/driver_nl80211_monitor.c`** -> AI Confidence: **99.31%**
5042. **`contrib/wpa/src/drivers/driver_nl80211_scan.c`** -> AI Confidence: **99.31%**
5043. **`contrib/wpa/src/drivers/driver_roboswitch.c`** -> AI Confidence: **99.31%**
5044. **`contrib/wpa/src/drivers/driver_wired_common.c`** -> AI Confidence: **99.31%**
5045. **`contrib/wpa/src/drivers/linux_ioctl.c`** -> AI Confidence: **99.31%**
5046. **`contrib/wpa/src/eap_common/eap_eke_common.c`** -> AI Confidence: **99.31%**
5047. **`contrib/wpa/src/eap_common/eap_fast_common.c`** -> AI Confidence: **99.31%**
5048. **`contrib/wpa/src/eap_common/eap_pwd_common.c`** -> AI Confidence: **99.31%**
5049. **`contrib/wpa/src/eap_common/eap_sim_common.c`** -> AI Confidence: **99.31%**
5050. **`contrib/wpa/src/eap_common/eap_teap_common.c`** -> AI Confidence: **99.31%**
5051. **`contrib/wpa/src/eap_common/ikev2_common.c`** -> AI Confidence: **99.31%**
5052. **`contrib/wpa/src/eap_peer/eap.c`** -> AI Confidence: **99.31%**
5053. **`contrib/wpa/src/eap_peer/eap_aka.c`** -> AI Confidence: **99.31%**
5054. **`contrib/wpa/src/eap_peer/eap_fast.c`** -> AI Confidence: **99.31%**
5055. **`contrib/wpa/src/eap_peer/eap_mschapv2.c`** -> AI Confidence: **99.31%**
5056. **`contrib/wpa/src/eap_peer/eap_peap.c`** -> AI Confidence: **99.31%**
5057. **`contrib/wpa/src/eap_peer/eap_pwd.c`** -> AI Confidence: **99.31%**
5058. **`contrib/wpa/src/eap_peer/eap_sim.c`** -> AI Confidence: **99.31%**
5059. **`contrib/wpa/src/eap_peer/eap_teap.c`** -> AI Confidence: **99.31%**
5060. **`contrib/wpa/src/eap_peer/eap_tls_common.c`** -> AI Confidence: **99.31%**
5061. **`contrib/wpa/src/eap_peer/eap_ttls.c`** -> AI Confidence: **99.31%**
5062. **`contrib/wpa/src/eap_peer/eap_wsc.c`** -> AI Confidence: **99.31%**
5063. **`contrib/wpa/src/eap_peer/tncc.c`** -> AI Confidence: **99.31%**
5064. **`contrib/wpa/src/eap_server/eap_server_aka.c`** -> AI Confidence: **99.31%**
5065. **`contrib/wpa/src/eap_server/eap_server_fast.c`** -> AI Confidence: **99.31%**
5066. **`contrib/wpa/src/eap_server/eap_server_peap.c`** -> AI Confidence: **99.31%**
5067. **`contrib/wpa/src/eap_server/eap_server_pwd.c`** -> AI Confidence: **99.31%**
5068. **`contrib/wpa/src/eap_server/eap_server_sim.c`** -> AI Confidence: **99.31%**
5069. **`contrib/wpa/src/eap_server/eap_server_teap.c`** -> AI Confidence: **99.31%**
5070. **`contrib/wpa/src/eap_server/eap_server_ttls.c`** -> AI Confidence: **99.31%**
5071. **`contrib/wpa/src/eap_server/eap_server_wsc.c`** -> AI Confidence: **99.31%**
5072. **`contrib/wpa/src/eap_server/eap_sim_db.c`** -> AI Confidence: **99.31%**
5073. **`contrib/wpa/src/eap_server/tncs.c`** -> AI Confidence: **99.31%**
5074. **`contrib/wpa/src/eapol_auth/eapol_auth_sm.c`** -> AI Confidence: **99.31%**
5075. **`contrib/wpa/src/eapol_supp/eapol_supp_sm.c`** -> AI Confidence: **99.31%**
5076. **`contrib/wpa/src/fst/fst_ctrl_iface.c`** -> AI Confidence: **99.31%**
5077. **`contrib/wpa/src/p2p/p2p.c`** -> AI Confidence: **99.31%**
5078. **`contrib/wpa/src/pae/ieee802_1x_key.c`** -> AI Confidence: **99.31%**
5079. **`contrib/wpa/src/pasn/pasn_initiator.c`** -> AI Confidence: **99.31%**
5080. **`contrib/wpa/src/pasn/pasn_responder.c`** -> AI Confidence: **99.31%**
5081. **`contrib/wpa/src/radius/radius_client.c`** -> AI Confidence: **99.31%**
5082. **`contrib/wpa/src/radius/radius_das.c`** -> AI Confidence: **99.31%**
5083. **`contrib/wpa/src/radius/radius_server.c`** -> AI Confidence: **99.31%**
5084. **`contrib/wpa/src/rsn_supp/pmksa_cache.c`** -> AI Confidence: **99.31%**
5085. **`contrib/wpa/src/rsn_supp/preauth.c`** -> AI Confidence: **99.31%**
5086. **`contrib/wpa/src/rsn_supp/wpa.c`** -> AI Confidence: **99.31%**
5087. **`contrib/wpa/src/tls/pkcs5.c`** -> AI Confidence: **99.31%**
5088. **`contrib/wpa/src/tls/pkcs8.c`** -> AI Confidence: **99.31%**
5089. **`contrib/wpa/src/tls/tlsv1_client.c`** -> AI Confidence: **99.31%**
5090. **`contrib/wpa/src/tls/tlsv1_client_ocsp.c`** -> AI Confidence: **99.31%**
5091. **`contrib/wpa/src/tls/tlsv1_client_read.c`** -> AI Confidence: **99.31%**
5092. **`contrib/wpa/src/tls/tlsv1_client_write.c`** -> AI Confidence: **99.31%**
5093. **`contrib/wpa/src/tls/tlsv1_common.c`** -> AI Confidence: **99.31%**
5094. **`contrib/wpa/src/tls/tlsv1_cred.c`** -> AI Confidence: **99.31%**
5095. **`contrib/wpa/src/tls/tlsv1_record.c`** -> AI Confidence: **99.31%**
5096. **`contrib/wpa/src/tls/tlsv1_server.c`** -> AI Confidence: **99.31%**
5097. **`contrib/wpa/src/tls/tlsv1_server_read.c`** -> AI Confidence: **99.31%**
5098. **`contrib/wpa/src/tls/tlsv1_server_write.c`** -> AI Confidence: **99.31%**
5099. **`contrib/wpa/src/utils/eloop.c`** -> AI Confidence: **99.31%**
5100. **`contrib/wpa/src/utils/http_curl.c`** -> AI Confidence: **99.31%**
5101. **`contrib/wpa/src/utils/os_unix.c`** -> AI Confidence: **99.31%**
5102. **`contrib/wpa/src/utils/utils_module_tests.c`** -> AI Confidence: **99.31%**
5103. **`contrib/wpa/src/utils/wpa_debug.c`** -> AI Confidence: **99.31%**
5104. **`contrib/wpa/src/wps/wps_common.c`** -> AI Confidence: **99.31%**
5105. **`contrib/wpa/src/wps/wps_enrollee.c`** -> AI Confidence: **99.31%**
5106. **`contrib/wpa/src/wps/wps_er_ssdp.c`** -> AI Confidence: **99.31%**
5107. **`contrib/wpa/src/wps/wps_registrar.c`** -> AI Confidence: **99.31%**
5108. **`contrib/wpa/src/wps/wps_upnp_ap.c`** -> AI Confidence: **99.31%**
5109. **`contrib/wpa/src/wps/wps_upnp_ssdp.c`** -> AI Confidence: **99.31%**
5110. **`contrib/wpa/src/wps/wps_upnp_web.c`** -> AI Confidence: **99.31%**
5111. **`contrib/wpa/wpa_supplicant/ap.c`** -> AI Confidence: **99.31%**
5112. **`contrib/wpa/wpa_supplicant/autoscan.c`** -> AI Confidence: **99.31%**
5113. **`contrib/wpa/wpa_supplicant/bgscan_learn.c`** -> AI Confidence: **99.31%**
5114. **`contrib/wpa/wpa_supplicant/bgscan_simple.c`** -> AI Confidence: **99.31%**
5115. **`contrib/wpa/wpa_supplicant/bss.c`** -> AI Confidence: **99.31%**
5116. **`contrib/wpa/wpa_supplicant/config.c`** -> AI Confidence: **99.31%**
5117. **`contrib/wpa/wpa_supplicant/ctrl_iface_udp.c`** -> AI Confidence: **99.31%**
5118. **`contrib/wpa/wpa_supplicant/ctrl_iface_unix.c`** -> AI Confidence: **99.31%**
5119. **`contrib/wpa/wpa_supplicant/dbus/dbus_new_handlers.c`** -> AI Confidence: **99.31%**
5120. **`contrib/wpa/wpa_supplicant/dbus/dbus_new_handlers_p2p.c`** -> AI Confidence: **99.31%**
5121. **`contrib/wpa/wpa_supplicant/dpp_supplicant.c`** -> AI Confidence: **99.31%**
5122. **`contrib/wpa/wpa_supplicant/events.c`** -> AI Confidence: **99.31%**
5123. **`contrib/wpa/wpa_supplicant/hs20_supplicant.c`** -> AI Confidence: **99.31%**
5124. **`contrib/wpa/wpa_supplicant/interworking.c`** -> AI Confidence: **99.31%**
5125. **`contrib/wpa/wpa_supplicant/main.c`** -> AI Confidence: **99.31%**
5126. **`contrib/wpa/wpa_supplicant/mbo.c`** -> AI Confidence: **99.31%**
5127. **`contrib/wpa/wpa_supplicant/mesh.c`** -> AI Confidence: **99.31%**
5128. **`contrib/wpa/wpa_supplicant/mesh_mpm.c`** -> AI Confidence: **99.31%**
5129. **`contrib/wpa/wpa_supplicant/offchannel.c`** -> AI Confidence: **99.31%**
5130. **`contrib/wpa/wpa_supplicant/p2p_supplicant.c`** -> AI Confidence: **99.31%**
5131. **`contrib/wpa/wpa_supplicant/pasn_supplicant.c`** -> AI Confidence: **99.31%**
5132. **`contrib/wpa/wpa_supplicant/robust_av.c`** -> AI Confidence: **99.31%**
5133. **`contrib/wpa/wpa_supplicant/rrm.c`** -> AI Confidence: **99.31%**
5134. **`contrib/wpa/wpa_supplicant/sme.c`** -> AI Confidence: **99.31%**
5135. **`contrib/wpa/wpa_supplicant/wnm_sta.c`** -> AI Confidence: **99.31%**
5136. **`contrib/wpa/wpa_supplicant/wpa_priv.c`** -> AI Confidence: **99.31%**
5137. **`contrib/wpa/wpa_supplicant/wpa_supplicant.c`** -> AI Confidence: **99.31%**
5138. **`contrib/wpa/wpa_supplicant/wps_supplicant.c`** -> AI Confidence: **99.31%**
5139. **`contrib/xz/src/liblzma/check/crc32_fast.c`** -> AI Confidence: **99.31%**
5140. **`contrib/xz/src/lzmainfo/lzmainfo.c`** -> AI Confidence: **99.31%**
5141. **`contrib/xz/src/xz/file_io.c`** -> AI Confidence: **99.31%**
5142. **`crypto/heimdal/appl/ftp/ftpd/logwtmp.c`** -> AI Confidence: **99.31%**
5143. **`crypto/heimdal/appl/telnet/libtelnet/auth.c`** -> AI Confidence: **99.31%**
5144. **`crypto/heimdal/appl/telnet/libtelnet/enc_des.c`** -> AI Confidence: **99.31%**
5145. **`crypto/heimdal/appl/telnet/libtelnet/encrypt.c`** -> AI Confidence: **99.31%**
5146. **`crypto/heimdal/appl/telnet/libtelnet/misc.c`** -> AI Confidence: **99.31%**
5147. **`crypto/heimdal/appl/telnet/libtelnet/spx.c`** -> AI Confidence: **99.31%**
5148. **`crypto/heimdal/appl/telnet/telnetd/sys_term.c`** -> AI Confidence: **99.31%**
5149. **`crypto/heimdal/kdc/announce.c`** -> AI Confidence: **99.31%**
5150. **`crypto/krb5/src/appl/gss-sample/gss-misc.c`** -> AI Confidence: **99.31%**
5151. **`crypto/krb5/src/appl/gss-sample/gss-server.c`** -> AI Confidence: **99.31%**
5152. **`crypto/krb5/src/appl/user_user/server.c`** -> AI Confidence: **99.31%**
5153. **`crypto/krb5/src/ccapi/test/main.c`** -> AI Confidence: **99.31%**
5154. **`crypto/krb5/src/ccapi/test/simple_lock_test.c`** -> AI Confidence: **99.31%**
5155. **`crypto/krb5/src/kadmin/dbutil/kadm5_create.c`** -> AI Confidence: **99.31%**
5156. **`crypto/krb5/src/kadmin/dbutil/tabdump.c`** -> AI Confidence: **99.31%**
5157. **`crypto/krb5/src/kadmin/server/auth_acl.c`** -> AI Confidence: **99.31%**
5158. **`crypto/krb5/src/kadmin/server/kadm_rpc_svc.c`** -> AI Confidence: **99.31%**
5159. **`crypto/krb5/src/kdc/dispatch.c`** -> AI Confidence: **99.31%**
5160. **`crypto/krb5/src/kdc/kdc_authdata.c`** -> AI Confidence: **99.31%**
5161. **`crypto/krb5/src/kdc/kdc_preauth.c`** -> AI Confidence: **99.31%**
5162. **`crypto/krb5/src/lib/apputils/net-server.c`** -> AI Confidence: **99.31%**
5163. **`crypto/krb5/src/lib/gssapi/generic/oid_ops.c`** -> AI Confidence: **99.31%**
5164. **`crypto/krb5/src/lib/gssapi/mechglue/g_initialize.c`** -> AI Confidence: **99.31%**
5165. **`crypto/krb5/src/lib/kadm5/clnt/client_init.c`** -> AI Confidence: **99.31%**
5166. **`crypto/krb5/src/lib/kadm5/clnt/client_principal.c`** -> AI Confidence: **99.31%**
5167. **`crypto/krb5/src/lib/kadm5/kadm_rpc_xdr.c`** -> AI Confidence: **99.31%**
5168. **`crypto/krb5/src/lib/kadm5/srv/server_init.c`** -> AI Confidence: **99.31%**
5169. **`crypto/krb5/src/lib/kadm5/srv/server_misc.c`** -> AI Confidence: **99.31%**
5170. **`crypto/krb5/src/lib/kadm5/srv/svr_iters.c`** -> AI Confidence: **99.31%**
5171. **`crypto/krb5/src/lib/kdb/kdb_log.c`** -> AI Confidence: **99.31%**
5172. **`crypto/krb5/src/lib/krb5/ccache/cc_kcm.c`** -> AI Confidence: **99.31%**
5173. **`crypto/krb5/src/lib/krb5/ccache/cc_mslsa.c`** -> AI Confidence: **99.31%**
5174. **`crypto/krb5/src/lib/krb5/krb/preauth2.c`** -> AI Confidence: **99.31%**
5175. **`crypto/krb5/src/lib/krb5/os/localaddr.c`** -> AI Confidence: **99.31%**
5176. **`crypto/krb5/src/lib/krb5/os/prompter.c`** -> AI Confidence: **99.31%**
5177. **`crypto/krb5/src/lib/krb5/os/read_pwd.c`** -> AI Confidence: **99.31%**
5178. **`crypto/krb5/src/lib/krb5/os/sendto_kdc.c`** -> AI Confidence: **99.31%**
5179. **`crypto/krb5/src/lib/krb5/os/t_std_conf.c`** -> AI Confidence: **99.31%**
5180. **`crypto/krb5/src/lib/rpc/auth_gss.c`** -> AI Confidence: **99.31%**
5181. **`crypto/krb5/src/lib/rpc/bindresvport.c`** -> AI Confidence: **99.31%**
5182. **`crypto/krb5/src/lib/rpc/clnt_perror.c`** -> AI Confidence: **99.31%**
5183. **`crypto/krb5/src/lib/rpc/clnt_simple.c`** -> AI Confidence: **99.31%**
5184. **`crypto/krb5/src/lib/rpc/clnt_tcp.c`** -> AI Confidence: **99.31%**
5185. **`crypto/krb5/src/lib/rpc/clnt_udp.c`** -> AI Confidence: **99.31%**
5186. **`crypto/krb5/src/lib/rpc/get_myaddress.c`** -> AI Confidence: **99.31%**
5187. **`crypto/krb5/src/lib/rpc/pmap_getport.c`** -> AI Confidence: **99.31%**
5188. **`crypto/krb5/src/lib/rpc/pmap_rmt.c`** -> AI Confidence: **99.31%**
5189. **`crypto/krb5/src/lib/rpc/svc.c`** -> AI Confidence: **99.31%**
5190. **`crypto/krb5/src/plugins/kdb/db2/adb_openclose.c`** -> AI Confidence: **99.31%**
5191. **`crypto/krb5/src/plugins/kdb/db2/kdb_db2.c`** -> AI Confidence: **99.31%**
5192. **`crypto/krb5/src/plugins/kdb/db2/libdb2/btree/bt_close.c`** -> AI Confidence: **99.31%**
5193. **`crypto/krb5/src/plugins/kdb/db2/libdb2/hash/hash_bigkey.c`** -> AI Confidence: **99.31%**
5194. **`crypto/krb5/src/plugins/kdb/db2/libdb2/hash/hash_page.c`** -> AI Confidence: **99.31%**
5195. **`crypto/krb5/src/plugins/kdb/db2/libdb2/mpool/mpool.c`** -> AI Confidence: **99.31%**
5196. **`crypto/krb5/src/plugins/kdb/db2/libdb2/recno/rec_close.c`** -> AI Confidence: **99.31%**
5197. **`crypto/krb5/src/plugins/kdb/db2/libdb2/test/btree.tests/main.c`** -> AI Confidence: **99.31%**
5198. **`crypto/krb5/src/plugins/kdb/db2/pol_xdr.c`** -> AI Confidence: **99.31%**
5199. **`crypto/krb5/src/plugins/kdb/ldap/libkdb_ldap/kdb_ldap.c`** -> AI Confidence: **99.31%**
5200. **`crypto/krb5/src/plugins/kdb/ldap/libkdb_ldap/ldap_principal2.c`** -> AI Confidence: **99.31%**
5201. **`crypto/krb5/src/plugins/preauth/spake/spake_client.c`** -> AI Confidence: **99.31%**
5202. **`crypto/krb5/src/plugins/tls/k5tls/openssl.c`** -> AI Confidence: **99.31%**
5203. **`crypto/krb5/src/util/profile/prof_file.c`** -> AI Confidence: **99.31%**
5204. **`crypto/krb5/src/util/profile/prof_parse.c`** -> AI Confidence: **99.31%**
5205. **`crypto/krb5/src/util/ss/help.c`** -> AI Confidence: **99.31%**
5206. **`crypto/krb5/src/util/ss/listen.c`** -> AI Confidence: **99.31%**
5207. **`crypto/krb5/src/util/ss/pager.c`** -> AI Confidence: **99.31%**
5208. **`crypto/krb5/src/util/support/fake-addrinfo.c`** -> AI Confidence: **99.31%**
5209. **`crypto/krb5/src/util/verto/ev.c`** -> AI Confidence: **99.31%**
5210. **`crypto/krb5/src/util/verto/verto.c`** -> AI Confidence: **99.31%**
5211. **`crypto/krb5/src/windows/leashdll/timesync.c`** -> AI Confidence: **99.31%**
5212. **`crypto/libecc/include/libecc/sig/eddsa.h`** -> AI Confidence: **99.31%**
5213. **`crypto/libecc/src/curves/prj_pt.c`** -> AI Confidence: **99.31%**
5214. **`crypto/libecc/src/ecdh/x25519_448.c`** -> AI Confidence: **99.31%**
5215. **`crypto/libecc/src/nn/nn_modinv.c`** -> AI Confidence: **99.31%**
5216. **`crypto/libecc/src/sig/ecfsdsa.c`** -> AI Confidence: **99.31%**
5217. **`crypto/libecc/src/sig/ecgdsa.c`** -> AI Confidence: **99.31%**
5218. **`crypto/libecc/src/sig/eckcdsa.c`** -> AI Confidence: **99.31%**
5219. **`crypto/libecc/src/sig/ecrdsa.c`** -> AI Confidence: **99.31%**
5220. **`crypto/libecc/src/sig/ecsdsa_common.c`** -> AI Confidence: **99.31%**
5221. **`crypto/libecc/src/sig/fuzzing_ecdsa.c`** -> AI Confidence: **99.31%**
5222. **`crypto/libecc/src/sig/sm2.c`** -> AI Confidence: **99.31%**
5223. **`crypto/openssh/addr.c`** -> AI Confidence: **99.31%**
5224. **`crypto/openssh/atomicio.c`** -> AI Confidence: **99.31%**
5225. **`crypto/openssh/audit-bsm.c`** -> AI Confidence: **99.31%**
5226. **`crypto/openssh/audit.c`** -> AI Confidence: **99.31%**
5227. **`crypto/openssh/auth-bsdauth.c`** -> AI Confidence: **99.31%**
5228. **`crypto/openssh/auth-pam.c`** -> AI Confidence: **99.31%**
5229. **`crypto/openssh/auth-passwd.c`** -> AI Confidence: **99.31%**
5230. **`crypto/openssh/auth-sia.c`** -> AI Confidence: **99.31%**
5231. **`crypto/openssh/auth2-gss.c`** -> AI Confidence: **99.31%**
5232. **`crypto/openssh/auth2-kbdint.c`** -> AI Confidence: **99.31%**
5233. **`crypto/openssh/auth2-methods.c`** -> AI Confidence: **99.31%**
5234. **`crypto/openssh/authfile.c`** -> AI Confidence: **99.31%**
5235. **`crypto/openssh/blocklist.c`** -> AI Confidence: **99.31%**
5236. **`crypto/openssh/channels.c`** -> AI Confidence: **99.31%**
5237. **`crypto/openssh/cipher-aes.c`** -> AI Confidence: **99.31%**
5238. **`crypto/openssh/cipher-chachapoly-libcrypto.c`** -> AI Confidence: **99.31%**
5239. **`crypto/openssh/compat.c`** -> AI Confidence: **99.31%**
5240. **`crypto/openssh/dispatch.c`** -> AI Confidence: **99.31%**
5241. **`crypto/openssh/entropy.c`** -> AI Confidence: **99.31%**
5242. **`crypto/openssh/gss-genr.c`** -> AI Confidence: **99.31%**
5243. **`crypto/openssh/gss-serv-krb5.c`** -> AI Confidence: **99.31%**
5244. **`crypto/openssh/gss-serv.c`** -> AI Confidence: **99.31%**
5245. **`crypto/openssh/hmac.c`** -> AI Confidence: **99.31%**
5246. **`crypto/openssh/hostfile.c`** -> AI Confidence: **99.31%**
5247. **`crypto/openssh/kex-names.c`** -> AI Confidence: **99.31%**
5248. **`crypto/openssh/kexc25519.c`** -> AI Confidence: **99.31%**
5249. **`crypto/openssh/kexdh.c`** -> AI Confidence: **99.31%**
5250. **`crypto/openssh/kexecdh.c`** -> AI Confidence: **99.31%**
5251. **`crypto/openssh/kexgex.c`** -> AI Confidence: **99.31%**
5252. **`crypto/openssh/kexmlkem768x25519.c`** -> AI Confidence: **99.31%**
5253. **`crypto/openssh/kexsntrup761x25519.c`** -> AI Confidence: **99.31%**
5254. **`crypto/openssh/krl.c`** -> AI Confidence: **99.31%**
5255. **`crypto/openssh/mac.c`** -> AI Confidence: **99.31%**
5256. **`crypto/openssh/match.c`** -> AI Confidence: **99.31%**
5257. **`crypto/openssh/misc.c`** -> AI Confidence: **99.31%**
5258. **`crypto/openssh/monitor.c`** -> AI Confidence: **99.31%**
5259. **`crypto/openssh/monitor_fdpass.c`** -> AI Confidence: **99.31%**
5260. **`crypto/openssh/monitor_wrap.c`** -> AI Confidence: **99.31%**
5261. **`crypto/openssh/nchan.c`** -> AI Confidence: **99.31%**
5262. **`crypto/openssh/openbsd-compat/arc4random.c`** -> AI Confidence: **99.31%**
5263. **`crypto/openssh/openbsd-compat/bindresvport.c`** -> AI Confidence: **99.31%**
5264. **`crypto/openssh/openbsd-compat/bsd-closefrom.c`** -> AI Confidence: **99.31%**
5265. **`crypto/openssh/openbsd-compat/bsd-cygwin_util.c`** -> AI Confidence: **99.31%**
5266. **`crypto/openssh/openbsd-compat/bsd-getline.c`** -> AI Confidence: **99.31%**
5267. **`crypto/openssh/openbsd-compat/bsd-openpty.c`** -> AI Confidence: **99.31%**
5268. **`crypto/openssh/openbsd-compat/bsd-pselect.c`** -> AI Confidence: **99.31%**
5269. **`crypto/openssh/openbsd-compat/mktemp.c`** -> AI Confidence: **99.31%**
5270. **`crypto/openssh/openbsd-compat/openssl-compat.c`** -> AI Confidence: **99.31%**
5271. **`crypto/openssh/openbsd-compat/port-net.c`** -> AI Confidence: **99.31%**
5272. **`crypto/openssh/openbsd-compat/port-uw.c`** -> AI Confidence: **99.31%**
5273. **`crypto/openssh/openbsd-compat/pwcache.c`** -> AI Confidence: **99.31%**
5274. **`crypto/openssh/openbsd-compat/readpassphrase.c`** -> AI Confidence: **99.31%**
5275. **`crypto/openssh/regress/misc/fuzz-harness/mkcorpus_sntrup761.c`** -> AI Confidence: **99.31%**
5276. **`crypto/openssh/regress/mkdtemp.c`** -> AI Confidence: **99.31%**
5277. **`crypto/openssh/regress/setuid-allowed.c`** -> AI Confidence: **99.31%**
5278. **`crypto/openssh/regress/unittests/authopt/tests.c`** -> AI Confidence: **99.31%**
5279. **`crypto/openssh/regress/unittests/hostkeys/test_iterate.c`** -> AI Confidence: **99.31%**
5280. **`crypto/openssh/regress/unittests/kex/test_kex.c`** -> AI Confidence: **99.31%**
5281. **`crypto/openssh/regress/unittests/sshbuf/test_sshbuf_getput_crypto.c`** -> AI Confidence: **99.31%**
5282. **`crypto/openssh/regress/unittests/test_helper/fuzz.c`** -> AI Confidence: **99.31%**
5283. **`crypto/openssh/regress/unittests/test_helper/test_helper.c`** -> AI Confidence: **99.31%**
5284. **`crypto/openssh/sandbox-capsicum.c`** -> AI Confidence: **99.31%**
5285. **`crypto/openssh/sandbox-solaris.c`** -> AI Confidence: **99.31%**
5286. **`crypto/openssh/sftp-common.c`** -> AI Confidence: **99.31%**
5287. **`crypto/openssh/sftp-server.c`** -> AI Confidence: **99.31%**
5288. **`crypto/openssh/sftp-usergroup.c`** -> AI Confidence: **99.31%**
5289. **`crypto/openssh/srclimit.c`** -> AI Confidence: **99.31%**
5290. **`crypto/openssh/ssh-dss.c`** -> AI Confidence: **99.31%**
5291. **`crypto/openssh/ssh-ecdsa-sk.c`** -> AI Confidence: **99.31%**
5292. **`crypto/openssh/ssh-ecdsa.c`** -> AI Confidence: **99.31%**
5293. **`crypto/openssh/ssh-ed25519-sk.c`** -> AI Confidence: **99.31%**
5294. **`crypto/openssh/ssh-ed25519.c`** -> AI Confidence: **99.31%**
5295. **`crypto/openssh/ssh-rsa.c`** -> AI Confidence: **99.31%**
5296. **`crypto/openssh/ssh-sk.c`** -> AI Confidence: **99.31%**
5297. **`crypto/openssh/ssh-xmss.c`** -> AI Confidence: **99.31%**
5298. **`crypto/openssh/ssh_api.c`** -> AI Confidence: **99.31%**
5299. **`crypto/openssh/sshbuf-io.c`** -> AI Confidence: **99.31%**
5300. **`crypto/openssh/sshbuf-misc.c`** -> AI Confidence: **99.31%**
5301. **`crypto/openssh/sshbuf.c`** -> AI Confidence: **99.31%**
5302. **`crypto/openssh/sshkey-xmss.c`** -> AI Confidence: **99.31%**
5303. **`crypto/openssh/sshkey.c`** -> AI Confidence: **99.31%**
5304. **`crypto/openssh/ttymodes.c`** -> AI Confidence: **99.31%**
5305. **`crypto/openssh/umac.c`** -> AI Confidence: **99.31%**
5306. **`crypto/openssh/xmss_fast.c`** -> AI Confidence: **99.31%**
5307. **`crypto/openssh/xmss_hash.c`** -> AI Confidence: **99.31%**
5308. **`crypto/openssh/xmss_wots.c`** -> AI Confidence: **99.31%**
5309. **`crypto/openssl/apps/openssl.c`** -> AI Confidence: **99.31%**
5310. **`crypto/openssl/apps/s_server.c`** -> AI Confidence: **99.31%**
5311. **`crypto/openssl/crypto/LPdir_vms.c`** -> AI Confidence: **99.31%**
5312. **`crypto/openssl/crypto/asn1/a_d2i_fp.c`** -> AI Confidence: **99.31%**
5313. **`crypto/openssl/crypto/asn1/a_digest.c`** -> AI Confidence: **99.31%**
5314. **`crypto/openssl/crypto/asn1/a_int.c`** -> AI Confidence: **99.31%**
5315. **`crypto/openssl/crypto/asn1/a_strex.c`** -> AI Confidence: **99.31%**
5316. **`crypto/openssl/crypto/asn1/asn_moid.c`** -> AI Confidence: **99.31%**
5317. **`crypto/openssl/crypto/asn1/i2d_evp.c`** -> AI Confidence: **99.31%**
5318. **`crypto/openssl/crypto/asn1/tasn_prn.c`** -> AI Confidence: **99.31%**
5319. **`crypto/openssl/crypto/asn1/tasn_utl.c`** -> AI Confidence: **99.31%**
5320. **`crypto/openssl/crypto/asn1/x_algor.c`** -> AI Confidence: **99.31%**
5321. **`crypto/openssl/crypto/bio/bio_sock2.c`** -> AI Confidence: **99.31%**
5322. **`crypto/openssl/crypto/bio/bss_log.c`** -> AI Confidence: **99.31%**
5323. **`crypto/openssl/crypto/cmac/cmac.c`** -> AI Confidence: **99.31%**
5324. **`crypto/openssl/crypto/cmp/cmp_ctx.c`** -> AI Confidence: **99.31%**
5325. **`crypto/openssl/crypto/cmp/cmp_status.c`** -> AI Confidence: **99.31%**
5326. **`crypto/openssl/crypto/cms/cms_env.c`** -> AI Confidence: **99.31%**
5327. **`crypto/openssl/crypto/cms/cms_rsa.c`** -> AI Confidence: **99.31%**
5328. **`crypto/openssl/crypto/cms/cms_smime.c`** -> AI Confidence: **99.31%**
5329. **`crypto/openssl/crypto/comp/c_brotli.c`** -> AI Confidence: **99.31%**
5330. **`crypto/openssl/crypto/comp/c_zstd.c`** -> AI Confidence: **99.31%**
5331. **`crypto/openssl/crypto/conf/conf_api.c`** -> AI Confidence: **99.31%**
5332. **`crypto/openssl/crypto/conf/conf_mod.c`** -> AI Confidence: **99.31%**
5333. **`crypto/openssl/crypto/context.c`** -> AI Confidence: **99.31%**
5334. **`crypto/openssl/crypto/ct/ct_log.c`** -> AI Confidence: **99.31%**
5335. **`crypto/openssl/crypto/cversion.c`** -> AI Confidence: **99.31%**
5336. **`crypto/openssl/crypto/deterministic_nonce.c`** -> AI Confidence: **99.31%**
5337. **`crypto/openssl/crypto/dh/dh_ameth.c`** -> AI Confidence: **99.31%**
5338. **`crypto/openssl/crypto/dh/dh_asn1.c`** -> AI Confidence: **99.31%**
5339. **`crypto/openssl/crypto/dh/dh_kdf.c`** -> AI Confidence: **99.31%**
5340. **`crypto/openssl/crypto/dh/dh_pmeth.c`** -> AI Confidence: **99.31%**
5341. **`crypto/openssl/crypto/dsa/dsa_pmeth.c`** -> AI Confidence: **99.31%**
5342. **`crypto/openssl/crypto/ec/curve25519.c`** -> AI Confidence: **99.31%**
5343. **`crypto/openssl/crypto/ec/curve448/curve448.c`** -> AI Confidence: **99.31%**
5344. **`crypto/openssl/crypto/ec/curve448/eddsa.c`** -> AI Confidence: **99.31%**
5345. **`crypto/openssl/crypto/ec/ec_ameth.c`** -> AI Confidence: **99.31%**
5346. **`crypto/openssl/crypto/ec/ec_key.c`** -> AI Confidence: **99.31%**
5347. **`crypto/openssl/crypto/ec/ec_pmeth.c`** -> AI Confidence: **99.31%**
5348. **`crypto/openssl/crypto/ec/ecp_sm2p256.c`** -> AI Confidence: **99.31%**
5349. **`crypto/openssl/crypto/ec/ecx_meth.c`** -> AI Confidence: **99.31%**
5350. **`crypto/openssl/crypto/encode_decode/decoder_meth.c`** -> AI Confidence: **99.31%**
5351. **`crypto/openssl/crypto/encode_decode/decoder_pkey.c`** -> AI Confidence: **99.31%**
5352. **`crypto/openssl/crypto/encode_decode/encoder_meth.c`** -> AI Confidence: **99.31%**
5353. **`crypto/openssl/crypto/encode_decode/encoder_pkey.c`** -> AI Confidence: **99.31%**
5354. **`crypto/openssl/crypto/engine/eng_openssl.c`** -> AI Confidence: **99.31%**
5355. **`crypto/openssl/crypto/engine/eng_rdrand.c`** -> AI Confidence: **99.31%**
5356. **`crypto/openssl/crypto/evp/asymcipher.c`** -> AI Confidence: **99.31%**
5357. **`crypto/openssl/crypto/evp/ctrl_params_translate.c`** -> AI Confidence: **99.31%**
5358. **`crypto/openssl/crypto/evp/e_aes.c`** -> AI Confidence: **99.31%**
5359. **`crypto/openssl/crypto/evp/e_aria.c`** -> AI Confidence: **99.31%**
5360. **`crypto/openssl/crypto/evp/e_chacha20_poly1305.c`** -> AI Confidence: **99.31%**
5361. **`crypto/openssl/crypto/evp/e_idea.c`** -> AI Confidence: **99.31%**
5362. **`crypto/openssl/crypto/evp/e_rc2.c`** -> AI Confidence: **99.31%**
5363. **`crypto/openssl/crypto/evp/e_rc5.c`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `crypto/krb5/src/lib/crypto/crypto_tests/t_cksums.c` -> **100.0%** Exposure
- `crypto/krb5/src/lib/crypto/crypto_tests/t_decrypt.c` -> **100.0%** Exposure
- `crypto/krb5/src/lib/crypto/crypto_tests/t_derive.c` -> **100.0%** Exposure
- `crypto/krb5/src/lib/crypto/crypto_tests/t_prf.c` -> **100.0%** Exposure
- `crypto/krb5/src/lib/crypto/crypto_tests/t_str2key.c` -> **100.0%** Exposure
### Exploit Generation Surface
- `cddl/contrib/opensolaris/cmd/dtrace/test/cmd/scripts/dtest.pl` -> **100.0%** Exposure
- `contrib/dialog/demo.pl` -> **100.0%** Exposure
- `contrib/dialog/dialog.pl` -> **100.0%** Exposure
- `contrib/libxo/xolint/xolint.pl` -> **100.0%** Exposure
- `contrib/ncurses/misc/ncu2openbsd` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `bin/csh/Makefile` -> **100.0%** Exposure
- `bin/freebsd-version/Makefile` -> **100.0%** Exposure
- `contrib/bmake/unit-tests/depsrc-meta.mk` -> **100.0%** Exposure
- `contrib/bmake/unit-tests/deptgt-delete_on_error.mk` -> **100.0%** Exposure
- `contrib/bmake/unit-tests/meta-output.mk` -> **100.0%** Exposure
### Raw Memory Manipulation
- `bin/pax/cpio.c` -> **10.0%** Exposure
- `bin/pax/tar.c` -> **10.0%** Exposure
- `bin/ps/print.c` -> **10.0%** Exposure
- `bin/ps/ps.c` -> **10.0%** Exposure
- `cddl/contrib/opensolaris/common/ctf/ctf_create.c` -> **10.0%** Exposure
### Hardcoded Payload Artifacts
- `contrib/unbound/smallapp/unbound-anchor.c` -> **100.0%** Exposure
- `contrib/wpa/hs20/client/osu_client.c` -> **100.0%** Exposure
- `contrib/pam-krb5/ci/kdc-setup-heimdal` -> **100.0%** Exposure
- `contrib/pam-krb5/ci/kdc-setup-mit` -> **100.0%** Exposure
- `crypto/openssh/regress/brokenkeys.sh` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `contrib/arm-optimized-routines/math/Dir.mk` -> **100.0%** Exposure
- `contrib/ntp/scripts/calc_tickadj/Makefile.in` -> **100.0%** Exposure
- `contrib/ntp/scripts/ntp-wait/Makefile.in` -> **100.0%** Exposure
- `contrib/ntp/scripts/ntpsweep/Makefile.in` -> **100.0%** Exposure
- `contrib/ntp/scripts/ntptrace/Makefile.in` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1037` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `270590` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `crypto/openssh/regress/multiplex.sh` (SHELL) -> Cumulative Risk: **932.29**
- **Archetype:** `file_cluster_4` (Distance: 11.133 IQR)
- **Magnitude:** 1.97 | **LOC:** 211 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 90.0), `__global_context__` (Impact: 10.5), `Anonymous_Block` (Impact: 7.7)

### 2. `crypto/openssl/util/perl/TLSProxy/Proxy.pm` (PERL) -> Cumulative Risk: **930.51**
- **Archetype:** `file_cluster_0` (Distance: 13.438 IQR)
- **Magnitude:** 16.1 | **LOC:** 864 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `clientstart` (Impact: 379.9), `start` (Impact: 215.0), `init` (Impact: 200.9)

### 3. `sys/contrib/vchiq/interface/compat/vchi_bsd.c` (C) -> Cumulative Risk: **912.34**
- **Archetype:** `file_cluster_4` (Distance: 12.362 IQR)
- **Magnitude:** 4.24 | **LOC:** 527 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9992%)
- **Heaviest Functions:** `wait_for_completion_interruptible_timeou` (Impact: 20.9), `wait_for_completion_interruptible` (Impact: 13.1), `_completion_claim` (Impact: 12.6)

### 4. `crypto/openssl/providers/common/der/oids_to_c.pm` (PERL) -> Cumulative Risk: **912.23**
- **Archetype:** `file_cluster_17` (Distance: 18.679 IQR)
- **Magnitude:** 1.39 | **LOC:** 114 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `filter_to_H` (Impact: 48.2), `process_leaves` (Impact: 3.6)

### 5. `sys/dev/ichsmb/ichsmb.c` (C) -> Cumulative Risk: **907.58**
- **Archetype:** `file_cluster_4` (Distance: 13.25 IQR)
- **Magnitude:** 609.18 | **LOC:** 718 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `ichsmb_device_intr` (Impact: 82.5), `ichsmb_callback` (Impact: 9.9), `ichsmb_wait` (Impact: 9.3)

### 6. `sys/dev/sound/pcm/mixer.c` (C) -> Cumulative Risk: **906.37**
- **Archetype:** `file_cluster_4` (Distance: 13.482 IQR)
- **Magnitude:** 1502.06 | **LOC:** 1528 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `mixer_ioctl_cmd` (Impact: 124.1), `mixer_ioctl_channel` (Impact: 102.7), `mixer_set` (Impact: 91.7)

### 7. `usr.bin/paste/paste.c` (C) -> Cumulative Risk: **905.46**
- **Archetype:** `file_cluster_13` (Distance: 13.254 IQR)
- **Magnitude:** 391.5 | **LOC:** 277 | **CtrlFlow:** 87.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `parallel` (Impact: 83.7), `main` (Impact: 34.2), `sequential` (Impact: 27.9)

### 8. `sys/geom/geom_vfs.c` (C) -> Cumulative Risk: **901.01**
- **Archetype:** `file_cluster_13` (Distance: 13.442 IQR)
- **Magnitude:** 504.46 | **LOC:** 341 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `g_vfs_done` (Impact: 184.1), `g_vfs_orphan` (Impact: 17.6), `g_vfs_open` (Impact: 16.0)

### 9. `contrib/dialog/dialog.pl` (PERL) -> Cumulative Risk: **898.66**
- **Archetype:** `file_cluster_8` (Distance: 13.825 IQR)
- **Magnitude:** 11.7 | **LOC:** 601 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `quoted` (Impact: 587.7), `trace` (Impact: 12.4)

### 10. `sys/netgraph/ng_device.c` (C) -> Cumulative Risk: **895.62**
- **Archetype:** `file_cluster_13` (Distance: 12.627 IQR)
- **Magnitude:** 506.1 | **LOC:** 684 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `ngdread` (Impact: 80.0), `ngdioctl` (Impact: 45.2), `ng_device_rcvmsg` (Impact: 13.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `sys/netinet/tcp_stacks/rack.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.7 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.019 IQR)
- **Top Global Matches:** file_cluster_8: 15.7, file_cluster_13: 15.868, file_cluster_11: 15.921
- **Magnitude:** 20402.92 | **LOC:** 24750 | **CtrlFlow:** 76.0% | **Authorship Centralization:** 71.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 447
- **Risk Profile:** Cognitive Load (93.8114%), Tech Debt (11.9165%)
**Top Internal Functions/Classes:**
  * `rack_mark_lost` (Impact: 4365.2 | O(2^N) | DB: 447)
  * `rack_log_input_packet` (Impact: 4180.8 | O(2^N) | DB: 362)
    * *Intent:* /*
  * `rack_fo_m_copym` (Impact: 2000.4 | O(N^4) | DB: 289)
    * *Intent:* /* * We are seeing a new lower rtt very close * to the time that we would have entered probe-rtt. * ...
  * `rack_do_fastnewdata` (Impact: 271.4 | O(N^2) | DB: 59)
  * `rack_init_sysctls` (Impact: 207.2 | O(N^1) | DB: 103)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2238`, `structural_boundaries: 706`, `args: 144`, `func_start: 110`, `class_start: 152`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6118`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 4`, `orphaned_logic: 21`
* *Architecture:* `io: 39`, `api: 547`, `import: 75`
* *Defense:* `doc: 12`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` sched.h, socketvar.h, ip6.h, queue.h, mutex.h, proc.h, protosw.h, kthread.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/pms/RefTisa/sat/src/smsat.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.777 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.515 IQR)
- **Top Global Matches:** file_cluster_8: 14.777, file_cluster_7: 15.048, file_cluster_13: 15.088
- **Magnitude:** 15706.44 | **LOC:** 20820 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 633
- **Risk Profile:** Cognitive Load (65.9877%), Tech Debt (7.7022%)
**Top Internal Functions/Classes:**
  * `smsatWrite16` (Impact: 1426.2 | O(2^N) | DB: 633)
    * *Intent:* /*smEnqueueIO(smRoot, satIOContext);*/
  * `smsatTmAbortTask` (Impact: 1017.8 | O(2^N) | DB: 543)
  * `smsatModeSelect10` (Impact: 599.8 | O(2^N) | DB: 110)
  * `smsatModeSelect6` (Impact: 514.1 | O(2^N) | DB: 106)
    * *Intent:* /* * Prepare SGL and send FIS to LL layer. */ satIOContext->reqType = agRequestType; /* Save it */...
  * `smsatLogSense` (Impact: 510.9 | O(2^N) | DB: 78)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1214`, `structural_boundaries: 364`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 6028`, `dead_code: 14`, `orphaned_logic: 1`
* *Architecture:* `io: 7`, `api: 1045`, `import: 15`
* *Defense:* `doc: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` config.h, osenv.h, sm.h, ostypes.h, smapi.h, smtypes.h, cdefs.h, smproto.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/pms/RefTisa/sat/src/smsatcb.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.792 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.4 IQR)
- **Top Global Matches:** file_cluster_8: 13.792, file_cluster_7: 14.047, file_cluster_13: 14.1
- **Magnitude:** 13929.36 | **LOC:** 13769 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 171
- **Risk Profile:** Cognitive Load (56.7985%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `smsatDelayedProcessAbnormalCompletion` (Impact: 814.5 | O(2^N) | DB: 34)
  * `smsatLogSenseCB` (Impact: 803.3 | O(2^N) | DB: 171)
  * `smsatProcessAbnormalCompletion` (Impact: 793.1 | O(2^N) | DB: 34)
  * `smsatIDStartCB` (Impact: 700.1 | O(2^N) | DB: 80)
    * *Intent:* smOrgIORequest, /* == &satIntIo->satOrgSmIORequest */
  * `smsatWriteSame10CB` (Impact: 441.6 | O(2^N) | DB: 61)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1343`, `structural_boundaries: 372`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 187`, `state_mutation: 2740`, `dead_code: 33`
* *Architecture:* `io: 11`, `api: 1214`, `import: 15`
* *Defense:* `doc: 83`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` config.h, osenv.h, sm.h, ostypes.h, smapi.h, smtypes.h, cdefs.h, smproto.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/sys/netpfil/common/pft_ping.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.216 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.015 IQR)
- **Top Global Matches:** file_cluster_8: 9.216, file_cluster_13: 9.967, file_cluster_7: 9.988
- **Magnitude:** 13284.89 | **LOC:** 759 | **CtrlFlow:** 59.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (25.2063%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 150`, `args: 34`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 33`, `fragile_debt: 1`
* *Architecture:* `io: 10`, `api: 34`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` scapy.all, sys, socket, copy, logging, sniffer, math, argparse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netpfil/pf/pf.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.096 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.048 IQR)
- **Top Global Matches:** file_cluster_8: 15.096, file_cluster_13: 15.169, file_cluster_11: 15.343
- **Magnitude:** 12478.72 | **LOC:** 12125 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 70.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 396
- **Risk Profile:** Cognitive Load (96.0785%), Tech Debt (13.5663%)
**Top Internal Functions/Classes:**
  * `pf_insert_src_node` (Impact: 5527.1 | O(2^N) | DB: 396)
  * `pf_test_state_icmp` (Impact: 3506.5 | O(2^N) | DB: 383)
  * `pf_multihome_scan` (Impact: 136.2 | O(2^N) | DB: 15)
  * `pf_icmp_state_lookup` (Impact: 53.1 | O(N^1) | DB: 13)
  * `BOUND_IFACE` (Impact: 34.4 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1275`, `structural_boundaries: 749`, `args: 189`, `func_start: 56`, `class_start: 171`
* *Risk/State:* `state_mutation: 2515`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 7`, `orphaned_logic: 7`
* *Architecture:* `io: 3`, `api: 462`, `concurrency: 3`, `import: 68`
* *Defense:* `safety: 6`, `doc: 1`, `sync_locks: 6`, `immutability_locks: 26`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ip6.h, in6_pcb.h, in_fib.h, kthread.h, ah.h, opt_inet6.h, nhop.h, pfil.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/bxe/bxe.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.333 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.753 IQR)
- **Top Global Matches:** file_cluster_8: 14.333, file_cluster_7: 14.635, file_cluster_0: 14.641
- **Magnitude:** 10442.7 | **LOC:** 19454 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 426
- **Risk Profile:** Cognitive Load (92.52%), Tech Debt (35.0371%)
**Top Internal Functions/Classes:**
  * `bxe_set_pbd_csum` (Impact: 3896.7 | O(2^N) | DB: 426)
    * *Intent:* #ifndef CSUM_TCP_IPV6 #define CSUM_TCP_IPV6 0 #define CSUM_UDP_IPV6 0 #endif #define BXE_DEF_SB_ATT_...
  * `bxe_attn_int_deasserted` (Impact: 1340.4 | O(N^6) | DB: 327)
  * `bxe_hc_int_disable` (Impact: 769.9 | O(N^6) | DB: 72)
  * `bxe_check_blocks_with_parity2` (Impact: 221.8 | O(N^6) | DB: 14)
  * `bxe_check_blocks_with_parity3` (Impact: 139.5 | O(N^6) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 805`, `structural_boundaries: 447`, `args: 161`, `func_start: 122`, `class_start: 75`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 2495`, `dead_code: 8`, `fragile_debt: 24`, `orphaned_logic: 10`
* *Architecture:* `io: 3`, `api: 434`
* *Defense:* `safety: 6`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ecore_init_ops.h, 57711_int_offsets.h, bxe_dump.h, cdefs.h, 57710_int_offsets.h, bxe_ioctl.h, ecore_sp.h, 57712_int_offsets.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/pms/RefTisa/tisa/sassata/sata/host/sat.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.037 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.921 IQR)
- **Top Global Matches:** file_cluster_8: 15.037, file_cluster_7: 15.143, file_cluster_13: 15.178
- **Magnitude:** 9820.44 | **LOC:** 23309 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 141
- **Risk Profile:** Cognitive Load (33.9157%), Tech Debt (7.8721%)
**Top Internal Functions/Classes:**
  * `satIOStart` (Impact: 645.7 | O(2^N) | DB: 58)
    * *Intent:* #include <dev/pms/RefTisa/tisa/api/ostiapi.h> #include <dev/pms/RefTisa/tisa/api/tiapi.h> #include <...
  * `satWrite10` (Impact: 329.9 | O(2^N) | DB: 139)
  * `satReadBuffer` (Impact: 319.4 | O(2^N) | DB: 141)
    * *Intent:* fis->h.features = 0; /* FIS reserve */ fis->d.lbaLow = scsiCmnd->cdb[5]; /* FIS LBA (7 :0 ) */ fis->...
  * `satWrite16` (Impact: 313.9 | O(2^N) | DB: 141)
    * *Intent:* fis->d.device = 0x40; /* FIS FUA clear */ fis->d.lbaLowExp = scsiCmnd->cdb[6]; /* FIS LBA (31:24) */...
  * `satRead10` (Impact: 292.4 | O(2^N) | DB: 113)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 723`, `structural_boundaries: 241`, `func_start: 58`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 3941`, `dead_code: 21`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 796`, `import: 31`
* *Defense:* `doc: 433`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` osenv.h, dm.h, sm.h, dmapi.h, ostypes.h, tdproto.h, tdutil.h, ttdglobl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/pms/RefTisa/sallsdk/spc/sampirsp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.973 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.874 IQR)
- **Top Global Matches:** file_cluster_0: 15.973, file_cluster_11: 15.982, file_cluster_13: 16.038
- **Magnitude:** 9591.62 | **LOC:** 7873 | **CtrlFlow:** 87.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 112
- **Risk Profile:** Cognitive Load (46.1703%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mpiGeneralEventRsp` (Impact: 703.1 | O(2^N) | DB: 42)
  * `mpiSSPEvent` (Impact: 613.4 | O(2^N) | DB: 50)
  * `mpiParseOBIomb` (Impact: 593.9 | O(2^N) | DB: 112)
    * *Intent:* *WARRANTIES,INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS *FO...
  * `mpiHWevent` (Impact: 538.7 | O(2^N) | DB: 78)
  * `mpiDeviceRegRsp` (Impact: 421.6 | O(2^N) | DB: 43)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1248`, `structural_boundaries: 173`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 139`, `state_mutation: 3038`, `dead_code: 128`
* *Architecture:* `io: 3`, `api: 1003`, `import: 3`
* *Defense:* `doc: 280`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cdefs.h, config.h, saglobal.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/bxe/bxe_elink.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.252 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.254 IQR)
- **Top Global Matches:** file_cluster_8: 14.252, file_cluster_7: 14.543, file_cluster_13: 14.628
- **Magnitude:** 9506.26 | **LOC:** 15119 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 566
- **Risk Profile:** Cognitive Load (62.7772%), Tech Debt (10.7818%)
**Top Internal Functions/Classes:**
  * `elink_848x3_config_init` (Impact: 1554.7 | O(2^N) | DB: 566)
  * `elink_analyze_link_error` (Impact: 706.3 | O(2^N) | DB: 67)
  * `elink_link_update` (Impact: 302.1 | O(N^3) | DB: 77)
  * `elink_emac_enable` (Impact: 208.2 | O(2^N) | DB: 14)
  * `elink_phy_init` (Impact: 175.5 | O(N^6) | DB: 31)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1059`, `structural_boundaries: 700`, `args: 194`, `func_start: 142`, `class_start: 238`
* *Risk/State:* `state_mutation: 3181`, `dead_code: 4`, `orphaned_logic: 25`
* *Architecture:* `io: 3`, `api: 854`, `import: 7`
* *Defense:* `doc: 36`, `immutability_locks: 59`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ecore_reg.h, bxe_elink.h, ecore_mfw_req.h, ecore_fw_defs.h, cdefs.h, ecore_hsi.h, bxe.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/fs/nfsclient/nfs_clrpcops.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.093 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.984 IQR)
- **Top Global Matches:** file_cluster_8: 15.093, file_cluster_11: 15.31, file_cluster_13: 15.318
- **Magnitude:** 9215.58 | **LOC:** 10019 | **CtrlFlow:** 63.5% | **Authorship Centralization:** 90.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 688
- **Risk Profile:** Cognitive Load (96.0953%), Tech Debt (13.5957%)
**Top Internal Functions/Classes:**
  * `nfsrpc_lockt` (Impact: 2223.9 | O(N^2) | DB: 688)
  * `nfsrpc_write` (Impact: 1818.9 | O(2^N) | DB: 476)
  * `nfsm_split` (Impact: 70.2 | O(2^N) | DB: 41)
  * `nfsrpc_readrpc` (Impact: 54.3 | O(N^1) | DB: 29)
  * `nfsrpc_read` (Impact: 44.2 | O(N^1) | DB: 17)
    * *Intent:* *tl++ = txdr_unsigned((mode >> NFSLCK_SHIFT) & NFSV4OPEN_DENYBOTH);
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1158`, `structural_boundaries: 665`, `args: 77`, `func_start: 47`, `class_start: 221`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 4002`, `fragile_debt: 4`, `orphaned_logic: 11`
* *Architecture:* `io: 6`, `api: 620`, `concurrency: 18`, `import: 7`
* *Defense:* `safety: 11`, `sync_locks: 6`, `immutability_locks: 4`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` taskqueue.h, extattr.h, opt_inet6.h, sysctl.h, cdefs.h, nfsport.h, nfs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sbin/camcontrol/camcontrol.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.497 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.361 IQR)
- **Top Global Matches:** file_cluster_8: 14.497, file_cluster_13: 14.642, file_cluster_11: 14.725
- **Magnitude:** 8770.18 | **LOC:** 10824 | **CtrlFlow:** 80.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 470
- **Risk Profile:** Cognitive Load (97.0622%), Tech Debt (8.4801%)
**Top Internal Functions/Classes:**
  * `ratecontrol` (Impact: 4152.0 | O(2^N) | DB: 470)
  * `rescan_or_reset_bus` (Impact: 584.5 | O(N^3) | DB: 178)
    * *Intent:* /*retries*/ retry_count, /*cbfcnp*/ NULL, /* tag_action */ task_attr, /* inq_buf */ (uint8_t *)seria...
  * `main` (Impact: 356.5 | O(N^2) | DB: 79)
  * `cpi_print` (Impact: 218.2 | O(N^2) | DB: 36)
  * `getdevtree` (Impact: 213.8 | O(N^2) | DB: 47)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1087`, `structural_boundaries: 262`, `args: 87`, `func_start: 31`, `class_start: 60`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 2289`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 60`, `api: 508`, `import: 34`
* *Defense:* `safety: 4`, `test: 2`, `immutability_locks: 21`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ioctl.h, scsi_pass.h, libnvmf.h, smp_all.h, stdint.h, fcntl.h, mmc_all.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/pms/RefTisa/tisa/sassata/common/ossacmnapi.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.711 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.725 IQR)
- **Top Global Matches:** file_cluster_8: 13.711, file_cluster_7: 13.83, file_cluster_13: 13.937
- **Magnitude:** 8713.28 | **LOC:** 9093 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 245
- **Risk Profile:** Cognitive Load (36.0564%), Tech Debt (12.3221%)
**Top Internal Functions/Classes:**
  * `ossaHwCB` (Impact: 1634.8 | O(2^N) | DB: 245)
  * `ossaDeviceRegistrationCB` (Impact: 678.2 | O(2^N) | DB: 47)
    * *Intent:* } /* ossaFastSSPCompleted */ #endif /***************************************************************...
  * `ossaDeregisterDeviceHandleCB` (Impact: 405.4 | O(2^N) | DB: 27)
  * `ossaDiscoverSasCB` (Impact: 311.2 | O(2^N) | DB: 28)
  * `ossaFastSSPCompleted` (Impact: 289.6 | O(2^N) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 944`, `structural_boundaries: 296`, `func_start: 77`
* *Risk/State:* `safety_bypasses: 211`, `state_mutation: 1526`, `dead_code: 15`, `duplicate_logic: 6`, `orphaned_logic: 17`
* *Architecture:* `io: 1`, `api: 900`, `import: 30`
* *Defense:* `doc: 359`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` osenv.h, dm.h, sm.h, dmapi.h, ostypes.h, tdproto.h, tdutil.h, ttdglobl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/bnxt/bnxt_re/ib_verbs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.769 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.038 IQR)
- **Top Global Matches:** file_cluster_8: 14.769, file_cluster_11: 15.041, file_cluster_13: 15.073
- **Magnitude:** 8680.24 | **LOC:** 5583 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 93
- **Risk Profile:** Cognitive Load (78.0501%), Tech Debt (27.0622%)
**Top Internal Functions/Classes:**
  * `bnxt_re_modify_qp` (Impact: 286.8 | O(N^3) | DB: 93)
  * `bnxt_re_create_cq` (Impact: 251.6 | O(N^3) | DB: 68)
  * `bnxt_re_poll_cq` (Impact: 175.9 | O(N^3) | DB: 35)
  * `bnxt_re_alloc_ucontext` (Impact: 175.5 | O(N^6) | DB: 40)
  * `bnxt_re_post_send` (Impact: 128.0 | O(N^2) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1064`, `structural_boundaries: 1026`, `args: 155`, `func_start: 141`, `class_start: 374`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 3932`, `planned_debt: 7`, `fragile_debt: 1`, `orphaned_logic: 44`
* *Architecture:* `io: 14`, `api: 1014`, `import: 5`
* *Defense:* `safety: 5`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bnxt_re.h, uverbs_ioctl.h, etherdevice.h, ib_verbs.h, if_ether.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/qlnx/qlnxe/qlnx_os.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.588 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.922 IQR)
- **Top Global Matches:** file_cluster_8: 14.588, file_cluster_13: 14.802, file_cluster_7: 14.904
- **Magnitude:** 8417.18 | **LOC:** 8202 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 90.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 405
- **Risk Profile:** Cognitive Load (91.5157%), Tech Debt (7.793%)
**Top Internal Functions/Classes:**
  * `qlnx_rx_int` (Impact: 1927.6 | O(N^6) | DB: 405)
  * `qlnx_send` (Impact: 1137.7 | O(2^N) | DB: 165)
  * `qlnx_pci_attach` (Impact: 305.0 | O(N^6) | DB: 88)
  * `qlnx_tpa_start` (Impact: 112.8 | O(N^4) | DB: 105)
  * `qlnx_release` (Impact: 78.5 | O(N^6) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 869`, `structural_boundaries: 732`, `args: 87`, `func_start: 143`, `class_start: 168`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 3064`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 598`, `concurrency: 18`, `import: 35`
* *Defense:* `safety: 17`, `doc: 3`, `sync_locks: 8`, `immutability_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` mcp_public.h, ecore_spq.h, ecore_rt_defs.h, ecore_status.h, qlnx_rdma.h, ecore_l2.h, iov_schema.h, qlnx_ioctl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/sound/pci/hda/hdaa.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.613 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.95 IQR)
- **Top Global Matches:** file_cluster_8: 14.613, file_cluster_13: 14.915, file_cluster_11: 14.953
- **Magnitude:** 8323.72 | **LOC:** 7175 | **CtrlFlow:** 78.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 128
- **Risk Profile:** Cognitive Load (87.0089%), Tech Debt (10.6682%)
**Top Internal Functions/Classes:**
  * `hdaa_audio_trace_adc` (Impact: 452.3 | O(2^N) | DB: 19)
  * `hdaa_audio_trace_dac` (Impact: 446.3 | O(2^N) | DB: 12)
  * `hdaa_audio_ctl_source_volume` (Impact: 207.9 | O(N^2) | DB: 19)
  * `hdaa_audio_trace_to_out` (Impact: 195.9 | O(2^N) | DB: 12)
  * `hdaa_audio_as_parse` (Impact: 187.7 | O(N^2) | DB: 56)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1383`, `structural_boundaries: 370`, `args: 65`, `func_start: 80`, `class_start: 126`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3414`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 5`, `orphaned_logic: 2`
* *Architecture:* `api: 330`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 19`, `doc: 1`, `sync_locks: 2`, `immutability_locks: 17`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` taskqueue.h, opt_snd.h, hda_reg.h, hdac.h, ctype.h, sound.h, mixer_if.h, hdaa.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr.sbin/ctladm/ctladm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.549 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.265 IQR)
- **Top Global Matches:** file_cluster_8: 14.549, file_cluster_13: 14.707, file_cluster_11: 14.757
- **Magnitude:** 8201.04 | **LOC:** 4622 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 80
- **Risk Profile:** Cognitive Load (87.3034%), Tech Debt (9.3744%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 691.4 | O(N^6) | DB: 77)
  * `cctl_port` (Impact: 387.3 | O(N^2) | DB: 80)
  * `cctl_persistent_reserve_in` (Impact: 302.0 | O(N^6) | DB: 19)
  * `cctl_mode_sense` (Impact: 299.2 | O(N^2) | DB: 51)
  * `cctl_read_write` (Impact: 287.9 | O(N^2) | DB: 61)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1179`, `structural_boundaries: 218`, `args: 74`, `func_start: 50`, `class_start: 96`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 2707`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 33`, `api: 612`, `import: 32`
* *Defense:* `safety: 8`, `immutability_locks: 32`, `cleanup: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ioctl.h, queue.h, module.h, fcntl.h, linker.h, ctladm.h, ctype.h, callout.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/fs/nfsserver/nfs_nfsdserv.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.129 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.902 IQR)
- **Top Global Matches:** file_cluster_8: 15.129, file_cluster_11: 15.322, file_cluster_13: 15.395
- **Magnitude:** 7938.56 | **LOC:** 6703 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 109
- **Risk Profile:** Cognitive Load (85.3396%), Tech Debt (29.6966%)
**Top Internal Functions/Classes:**
  * `nfsrvd_open` (Impact: 519.1 | O(N^2) | DB: 104)
  * `nfsrvd_setattr` (Impact: 348.8 | O(N^2) | DB: 52)
  * `nfsrvd_copy_file_range` (Impact: 302.0 | O(N^2) | DB: 109)
  * `nfsrvd_lookup` (Impact: 185.9 | O(N^1) | DB: 49)
  * `nfsrvd_create` (Impact: 167.4 | O(N^2) | DB: 27)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1192`, `structural_boundaries: 332`, `args: 86`, `func_start: 43`, `class_start: 108`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 3654`, `fragile_debt: 2`, `orphaned_logic: 40`
* *Architecture:* `io: 1`, `api: 648`, `import: 6`
* *Defense:* `safety: 2`, `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` extattr.h, opt_inet6.h, filio.h, cdefs.h, nfsport.h, opt_inet.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr.sbin/ppp/command.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.483 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.426 IQR)
- **Top Global Matches:** file_cluster_8: 14.483, file_cluster_13: 14.521, file_cluster_11: 14.76
- **Magnitude:** 7758.26 | **LOC:** 3342 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 176
- **Risk Profile:** Cognitive Load (94.1988%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SetVariable` (Impact: 2563.2 | O(N^6) | DB: 176)
  * `NegotiateSet` (Impact: 395.5 | O(N^5) | DB: 43)
  * `SetServer` (Impact: 256.8 | O(N^4) | DB: 46)
  * `AddCommand` (Impact: 233.6 | O(N^4) | DB: 22)
  * `IfaceAddCommand` (Impact: 192.5 | O(2^N) | DB: 4)
    * *Intent:* #endif
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 930`, `structural_boundaries: 394`, `args: 90`, `func_start: 70`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 4`, `state_mutation: 1572`
* *Architecture:* `io: 31`, `api: 315`, `import: 62`
* *Defense:* `safety: 26`, `immutability_locks: 214`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` un.h, termios.h, async.h, auth.h, throughput.h, server.h, fcntl.h, stdarg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/e1000/e1000_ich8lan.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.213 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.871 IQR)
- **Top Global Matches:** file_cluster_8: 14.213, file_cluster_7: 14.38, file_cluster_13: 14.474
- **Magnitude:** 7461.96 | **LOC:** 6203 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 463
- **Risk Profile:** Cognitive Load (63.3564%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `e1000_init_phy_workarounds_pchlan` (Impact: 3941.6 | O(2^N) | DB: 463)
  * `e1000_update_nvm_checksum_ich8lan` (Impact: 1181.5 | O(2^N) | DB: 110)
  * `e1000_phy_is_accessible_pchlan` (Impact: 43.1 | O(N^1) | DB: 18)
  * `e1000_toggle_lanphypc_pch_lpt` (Impact: 25.8 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 664`, `structural_boundaries: 411`, `args: 123`, `func_start: 66`, `class_start: 32`
* *Risk/State:* `state_mutation: 1694`, `dead_code: 1`
* *Architecture:* `io: 6`, `api: 527`, `import: 1`
* *Defense:* `doc: 66`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` e1000_api.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/gnu/dev/bwn/phy_n/if_bwn_phy_n_core.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.589 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.243 IQR)
- **Top Global Matches:** file_cluster_8: 14.589, file_cluster_13: 14.741, file_cluster_11: 14.813
- **Magnitude:** 7354.46 | **LOC:** 6941 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 78
- **Risk Profile:** Cognitive Load (80.3404%), Tech Debt (27.5944%)
**Top Internal Functions/Classes:**
  * `bwn_nphy_cal_tx_iq_lo` (Impact: 236.2 | O(N^2) | DB: 65)
  * `bwn_nphy_rev3_rssi_cal` (Impact: 213.2 | O(N^3) | DB: 78)
  * `bwn_nphy_tx_power_fix` (Impact: 190.2 | O(N^3) | DB: 30)
  * `bwn_phy_initn` (Impact: 178.8 | O(N^2) | DB: 26)
  * `bwn_nphy_tx_power_ctl_setup` (Impact: 168.3 | O(N^2) | DB: 70)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1193`, `structural_boundaries: 487`, `args: 94`, `func_start: 93`, `class_start: 100`
* *Risk/State:* `state_mutation: 2985`, `dead_code: 3`, `planned_debt: 43`, `fragile_debt: 7`, `orphaned_logic: 14`
* *Architecture:* `io: 3`, `api: 512`, `import: 54`
* *Defense:* `doc: 9`, `immutability_locks: 31`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` if_bwn_phy_n_ppr.h, mutex.h, if_bwn_phy_n_tables.h, if_bwn_radio_2057.h, if_bwn_debug.h, module.h, systm.h, errno.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/fs/nfs/nfs_commonsubs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.751 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.631 IQR)
- **Top Global Matches:** file_cluster_8: 14.751, file_cluster_13: 14.941, file_cluster_4: 14.949
- **Magnitude:** 7258.74 | **LOC:** 5610 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 85.7%
- **Algorithmic:** O(N^2) | **DB Complexity:** 601
- **Risk Profile:** Cognitive Load (97.5665%), Tech Debt (12.2945%)
**Top Internal Functions/Classes:**
  * `nfsv4_loadattr` (Impact: 5005.8 | O(N^2) | DB: 601)
    * *Intent:* { 0, 0, 0, 0, LK_EXCLUSIVE, 1, 1 }, /* RestoreFH */ { 0, 1, 0, 0, LK_EXCLUSIVE, 1, 1 }, /* SaveFH */...
  * `nfsaddr_match` (Impact: 21.6 | O(N^1) | DB: 2)
  * `nfsm_getfh` (Impact: 15.4 | O(N^1) | DB: 8)
    * *Intent:* { 0, 0, 0, 0, LK_EXCLUSIVE, 1, 1 }, /* undef */ { 0, 0, 0, 0, LK_EXCLUSIVE, 1, 1 }, /* undef */ { 0,...
  * `nfsaddr2_match` (Impact: 11.7 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 739`, `structural_boundaries: 159`, `args: 35`, `func_start: 27`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1824`, `planned_debt: 1`, `fragile_debt: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 305`, `concurrency: 36`, `import: 8`
* *Defense:* `sync_locks: 13`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mac_framework.h, extattr.h, opt_inet6.h, cdefs.h, nfsmount.h, vm_param.h, nfsport.h, opt_inet.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/sctp_output.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.048 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.932 IQR)
- **Top Global Matches:** file_cluster_8: 14.048, file_cluster_7: 14.405, file_cluster_13: 14.405
- **Magnitude:** 7051.14 | **LOC:** 13929 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 327
- **Risk Profile:** Cognitive Load (72.0773%), Tech Debt (13.0645%)
**Top Internal Functions/Classes:**
  * `sctp_lowlevel_chunk_output` (Impact: 1552.0 | O(N^2) | DB: 327)
    * *Intent:* #endif #ifdef INET6
  * `sctp_send_asconf` (Impact: 648.0 | O(N^2) | DB: 207)
  * `sctp_sendall_completes` (Impact: 530.8 | O(N^2) | DB: 168)
  * `sctp_choose_boundspecific_stcb` (Impact: 189.6 | O(N^2) | DB: 7)
    * *Intent:* /* Ok the address may be ok */ #ifdef INET6
  * `sctp_add_addr_to_mbuf` (Impact: 183.8 | O(2^N) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1094`, `structural_boundaries: 520`, `args: 110`, `func_start: 25`, `class_start: 128`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 2692`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 9`, `orphaned_logic: 7`
* *Architecture:* `io: 2`, `api: 344`, `import: 21`
* *Defense:* `safety: 1`, `doc: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sctp_kdtrace.h, proc.h, sctp_uio.h, sctp_crc32.h, sctp_var.h, sctp_bsd_addr.h, udp_var.h, sctp_asconf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/sctp_var.h` (C | Tier 4 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.171 IQR)
- **Top Global Matches:** file_cluster_8: 13.171, file_cluster_13: 13.656, file_cluster_9: 13.671
- **Magnitude:** 7024.84 | **LOC:** 349 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (65.7517%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 37`, `args: 74`, `func_start: 16`
* *Risk/State:* `state_mutation: 130`
* *Architecture:* `io: 13`, `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sctp_uio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/bnxt/bnxt_en/if_bnxt.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.737 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.99 IQR)
- **Top Global Matches:** file_cluster_8: 14.737, file_cluster_13: 14.905, file_cluster_11: 14.987
- **Magnitude:** 6897.96 | **LOC:** 5328 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 116
- **Risk Profile:** Cognitive Load (95.3376%), Tech Debt (8.6863%)
**Top Internal Functions/Classes:**
  * `bnxt_attach_pre` (Impact: 298.7 | O(N^2) | DB: 116)
    * *Intent:* /* Device setup and teardown */
  * `bnxt_add_media_types` (Impact: 262.2 | O(N^2) | DB: 18)
  * `bnxt_report_link` (Impact: 165.9 | O(N^5) | DB: 23)
  * `bnxt_rx_queues_alloc` (Impact: 147.4 | O(N^3) | DB: 73)
  * `bnxt_handle_async_event` (Impact: 138.9 | O(N^2) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1138`, `structural_boundaries: 728`, `args: 157`, `func_start: 125`, `class_start: 146`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 3028`, `planned_debt: 4`, `orphaned_logic: 2`
* *Architecture:* `io: 8`, `api: 818`, `import: 38`
* *Defense:* `safety: 7`, `immutability_locks: 6`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` iflib.h, netdevice.h, etherdevice.h, bnxt_sysctl.h, bnxt_ulp.h, opt_inet6.h, module.h, module.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/arcmsr/arcmsr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.69 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.042 IQR)
- **Top Global Matches:** file_cluster_8: 14.69, file_cluster_13: 14.853, file_cluster_11: 14.965
- **Magnitude:** 6736.12 | **LOC:** 5422 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 71
- **Risk Profile:** Cognitive Load (73.4884%), Tech Debt (8.9062%)
**Top Internal Functions/Classes:**
  * `arcmsr_action` (Impact: 126.7 | O(N^1) | DB: 71)
  * `arcmsr_dr_handle` (Impact: 121.1 | O(2^N) | DB: 49)
    * *Intent:* /* ************************************************************************
  * `arcmsr_iop_message_xfer` (Impact: 116.3 | O(N^2) | DB: 70)
  * `arcmsr_define_adapter_type` (Impact: 98.3 | O(N^1) | DB: 26)
  * `arcmsr_iop_confirm` (Impact: 88.5 | O(N^2) | DB: 31)
    * *Intent:* *acb_device_map = bus_space_read_1(acb->btag[0], acb->bhandle[0], iop_device_map+i);
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1142`, `structural_boundaries: 690`, `args: 203`, `func_start: 134`, `class_start: 107`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 3211`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 5`
* *Architecture:* `io: 8`, `api: 676`, `import: 40`
* *Defense:* `safety: 21`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cam_xpt_periph.h, queue.h, mutex.h, proc.h, kthread.h, module.h, systm.h, conf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `krb5/usr.bin/kdestroy/Makefile` (MAKEFILE) | Magnitude: 6.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, func_start: 3, safety_bypasses: 2
- `krb5/usr.bin/klist/Makefile` (MAKEFILE) | Magnitude: 6.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, func_start: 3, safety_bypasses: 2
- `krb5/usr.bin/kswitch/Makefile` (MAKEFILE) | Magnitude: 6.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, func_start: 3, safety_bypasses: 2
- `krb5/usr.bin/kvno/Makefile` (MAKEFILE) | Magnitude: 6.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, func_start: 3, safety_bypasses: 2
- `krb5/usr.bin/sclient/Makefile` (MAKEFILE) | Magnitude: 6.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, func_start: 3, safety_bypasses: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `contrib/llvm-project/lldb/include/lldb/Breakpoint/BreakpointList.h` (CPP) | Magnitude: 0.19 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 84, indent_spaces: 41, structural_boundaries: 18, args: 12
- `tests/sys/cddl/zfs/tests/xattr/xattr_010_neg.ksh` (SHELL) | Magnitude: 5.52 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: safety_bypasses: 19, reflection_metaprogramming: 7, structural_boundaries: 5, import: 2
- `sys/contrib/openzfs/tests/zfs-tests/tests/functional/xattr/xattr_010_neg.ksh` (SHELL) | Magnitude: 0.06 | Delta: **0.16 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety_bypasses: 9, structural_boundaries: 7, events: 5, sync_locks: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `contrib/sendmail/src/domain.c` (C) | Magnitude: 16.01 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 909, indent_tabs: 741, branch: 276, pointers: 174
- `tools/tools/sysbuild/sysbuild.sh` (SHELL) | Magnitude: 0.57 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 297, state_mutation: 175, branch: 167, reflection_metaprogramming: 127
- `sys/opencrypto/cryptosoft.c` (C) | Magnitude: 2012.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 1184, state_mutation: 830, pointers: 763, branch: 394
- `contrib/libfido2/udev/check.sh` (SHELL) | Magnitude: 0.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: io: 16, indent_tabs: 11, structural_boundaries: 10, reflection_metaprogramming: 10
- `tools/test/stress2/misc/altbufferflushes.sh` (SHELL) | Magnitude: 0.04 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 14, branch: 12, structural_boundaries: 12, safety_bypasses: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `crypto/openssl/crypto/ec/ecp_oct.c` (C) | Magnitude: 5.67 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 270, state_mutation: 147, branch: 128, api: 70
- `crypto/openssh/regress/key-options.sh` (SHELL) | Magnitude: 1.21 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 72, safety_bypasses: 67, state_mutation: 56, branch: 41
- `sys/contrib/openzfs/tests/zfs-tests/tests/functional/redundancy/redundancy_draid_damaged2.ksh` (SHELL) | Magnitude: 0.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety_bypasses: 48, indent_tabs: 48, state_mutation: 22, reflection_metaprogramming: 16
- `tools/boot/lua-img.sh` (SHELL) | Magnitude: 0.01 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, reflection_metaprogramming: 8, state_mutation: 3, args: 2
- `cddl/usr.sbin/dtrace/tests/tools/genmakefiles.sh` (SHELL) | Magnitude: 0.05 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, state_mutation: 24, structural_boundaries: 21, safety_bypasses: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `contrib/bearssl/src/symcipher/aes_x86ni_cbcenc.c` (C) | Magnitude: 1.05 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 74, indent_tabs: 55, pointers: 20, structural_boundaries: 17
- `contrib/bsnmp/snmp_usm/usm_snmp.c` (C) | Magnitude: 10.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 368, pointers: 284, state_mutation: 247, branch: 190
- `contrib/ncurses/form/fld_ftchoice.c` (C) | Magnitude: 0.27 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 13, state_mutation: 12, pointers: 7, ownership: 6
- `contrib/ncurses/ncurses/trace/trace_tries.c` (C) | Magnitude: 0.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 24, indent_tabs: 12, branch: 8, pointers: 7
- `contrib/ofed/libcxgb4/qp.c` (C) | Magnitude: 8.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 444, indent_tabs: 367, pointers: 332, structural_boundaries: 81

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `contrib/libfido2/windows/release.ps1` (POWERSHELL) | Magnitude: 0.36 | Delta: **0.268 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: closures: 121, indent_tabs: 37, state_mutation: 24, structural_boundaries: 6
- `contrib/libfido2/windows/cygwin.ps1` (POWERSHELL) | Magnitude: 0.46 | Delta: **0.359 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: closures: 34, state_mutation: 24, indent_tabs: 16, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `contrib/llvm-project/llvm/include/llvm/Analysis/ModelUnderTrainingRunner.h` (C) | Magnitude: 0.19 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, immutability_locks: 18, bitwise_ops: 13, generics: 11
- `contrib/llvm-project/llvm/include/llvm/Support/Chrono.h` (CPP) | Magnitude: 1.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 79, indent_spaces: 63, doc: 43, state_mutation: 37
- `contrib/llvm-project/libcxx/include/__functional/bind.h` (CPP) | Magnitude: 2.46 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 212, structural_boundaries: 210, indent_spaces: 90, generics: 40
- `contrib/kyua/utils/optional.ipp` (CPP) | Magnitude: 1.1 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 82, state_mutation: 80, structural_boundaries: 51, indent_spaces: 47
- `contrib/llvm-project/clang/include/clang/Basic/DiagnosticError.h` (C) | Magnitude: 0.08 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, doc: 8, bitwise_ops: 7, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `contrib/bmake/mk/sys/Cygwin.mk` (MAKEFILE) | Magnitude: 0.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 7, func_start: 1, state_mutation: 1, dead_code: 1
- `lib/googletest/gmock_main/Makefile` (MAKEFILE) | Magnitude: 9.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 7, structural_boundaries: 3, func_start: 1, api: 1
- `lib/libc/tests/resolv/Makefile` (MAKEFILE) | Magnitude: 15.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 2, state_mutation: 2, dead_code: 1
- `contrib/unbound/smallapp/unbound-control-setup.sh` (SHELL) | Magnitude: 1.13 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 62, indent_spaces: 50, io: 27, branch: 19
- `contrib/unbound/smallapp/unbound-control-setup.sh.in` (SHELL) | Magnitude: 1.13 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 62, indent_spaces: 50, io: 27, branch: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `contrib/kyua/utils/signals/exceptions.cpp` (CPP) | Magnitude: 0.2 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 23, args: 10, structural_boundaries: 8, ui_framework: 8
- `contrib/ntp/html/drivers/driver38.html` (HTML) | Magnitude: 0.2 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 122, structural_boundaries: 39, ui_framework: 33, io: 19
- `crypto/krb5/src/windows/leash/htmlhelp/html/KCPYTKT.htm` (HTML) | Magnitude: 0.25 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 27, ui_framework: 17, decorators: 11, api: 9
- `crypto/krb5/src/windows/leash/htmlhelp/html/KDESTROY.htm` (HTML) | Magnitude: 0.26 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 27, ui_framework: 25, args: 11, api: 9
- `contrib/ntp/html/ntptime.html` (HTML) | Magnitude: 0.17 | Delta: **0.2 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 29, indent_spaces: 20, ui_framework: 13, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `sys/contrib/zstd/examples/streaming_compression_thread_pool.c` (C) | Magnitude: 1.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 89, indent_spaces: 86, api: 34, pointers: 29
- `bin/pwait/tests/pwait_test.sh` (SHELL) | Magnitude: 149.5 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 220, safety_bypasses: 100, concurrency: 91, panics_and_aborts: 49
- `sys/cam/ctl/ctl_backend_ramdisk.c` (C) | Magnitude: 1634.02 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 934, state_mutation: 754, pointers: 726, branch: 278
- `sys/dev/usb/usb_dev.c` (C) | Magnitude: 1727.02 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 948, state_mutation: 742, pointers: 532, branch: 296
- `sys/netgraph/ng_socket.c` (C) | Magnitude: 983.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 434, state_mutation: 363, pointers: 266, structural_boundaries: 122

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `contrib/llvm-project/llvm/include/llvm/Frontend/OpenMP/OMPIRBuilder.h` (C) | Magnitude: 2.9 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 1218, indent_spaces: 305, api: 210, pointers: 161
- `contrib/llvm-project/clang/include/clang/Format/Format.h` (C) | Magnitude: 3.13 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 2303, indent_spaces: 626, api: 256, branch: 189
- `contrib/llvm-project/llvm/include/llvm/Support/ExponentialBackoff.h` (C) | Magnitude: 0.32 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 24, indent_spaces: 13, api: 11, state_mutation: 5
- `contrib/llvm-project/llvm/include/llvm/BinaryFormat/DynamicTags.def` (MAKEFILE) | Magnitude: 2.86 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, branch: 18, dead_code: 15, func_start: 6
- `share/mk/bsd.sanitizer.mk` (MAKEFILE) | Magnitude: 41.58 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 26, branch: 10, structural_boundaries: 4, dead_code: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `contrib/xz/src/liblzma/lzma/lzma_encoder_private.h` (C) | Magnitude: 0.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 74, api: 42, indent_tabs: 40, structural_boundaries: 14
- `contrib/llvm-project/clang/include/clang/StaticAnalyzer/Core/BugReporter/Z3CrosscheckVisitor.h` (C) | Magnitude: 0.43 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, doc: 24, api: 23, pointers: 15
- `contrib/llvm-project/llvm/include/llvm/Analysis/LoopAnalysisManager.h` (C) | Magnitude: 0.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 37, api: 25, indent_spaces: 12, pointers: 10
- `contrib/llvm-project/clang/include/clang/Lex/CodeCompletionHandler.h` (C) | Magnitude: 0.31 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 33, api: 20, structural_boundaries: 10, indent_spaces: 10
- `contrib/llvm-project/llvm/include/llvm/Transforms/Utils/PromoteMemToReg.h` (C) | Magnitude: 0.23 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 13, api: 7, pointers: 3, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `contrib/arm-optimized-routines/math/sincosf.h` (C) | Magnitude: 1.53 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 96, indent_spaces: 62, pointers: 35, api: 27
- `contrib/libcbor/src/cbor/internal/builder_callbacks.c` (C) | Magnitude: 5.57 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 261, pointers: 187, state_mutation: 129, structural_boundaries: 103
- `contrib/ncurses/ncurses/tinfo/entries.c` (C) | Magnitude: 0.63 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 46, indent_spaces: 44, pointers: 21, branch: 20
- `contrib/netbsd-tests/crypto/opencrypto/h_sha1hmac.c` (C) | Magnitude: 0.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 51, state_mutation: 43, api: 13, branch: 11
- `contrib/ntp/util/timetrim.c` (C) | Magnitude: 0.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 50, state_mutation: 30, branch: 26, macros: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `contrib/bearssl/src/rsa/rsa_oaep_unpad.c` (C) | Magnitude: 0.93 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 69, indent_tabs: 47, pointers: 23, api: 13
- `contrib/ncurses/ncurses/base/define_key.c` (C) | Magnitude: 0.43 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 24, branch: 18, indent_tabs: 13, indent_spaces: 8
- `crypto/krb5/src/lib/krb5/krb/cammac_util.c` (C) | Magnitude: 0.84 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 39, indent_spaces: 32, pointers: 21, api: 15
- `crypto/krb5/src/lib/krb5/krb/random_str.c` (C) | Magnitude: 0.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 37, indent_spaces: 24, api: 7, branch: 6
- `sys/contrib/ck/include/ck_malloc.h` (C) | Magnitude: 0.16 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, pointers: 7, safety: 4, ownership: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `sys/dev/acpica/acpi.c` -> Churn: **100.0%** | Cog Load: 93.4899% | Debt: 19.3138%
- `sys/x86/cpufreq/hwpstate_amd.c` -> Churn: **96.38%** | Cog Load: 75.1634% | Debt: 30.8939%
- `sys/compat/linuxkpi/common/src/linux_80211.c` -> Churn: **92.76%** | Cog Load: 76.951% | Debt: 94.5469%
- `sys/dev/asmc/asmc.c` -> Churn: **86.74%** | Cog Load: 72.0537% | Debt: 53.5858%
- `sys/dev/vmm/vmm_dev.c` -> Churn: **80.19%** | Cog Load: 91.6118% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `sys/fs/nfsclient/nfs_clrpcops.c` -> **Rick Macklem** (90.9% isolated ownership) | Magnitude: 9215.58
- `sys/dev/bnxt/bnxt_re/ib_verbs.c` -> **Sreekanth Reddy** (100.0% isolated ownership) | Magnitude: 8680.24
- `sys/dev/qlnx/qlnxe/qlnx_os.c` -> **Zhenlei Huang** (90.9% isolated ownership) | Magnitude: 8417.18
- `sys/dev/sound/pci/hda/hdaa.c` -> **Christos Margiolis** (100.0% isolated ownership) | Magnitude: 8323.72
- `sys/fs/nfsserver/nfs_nfsdserv.c` -> **Rick Macklem** (100.0% isolated ownership) | Magnitude: 7938.56

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crypto/krb5/src/lib/krad/code.c` -> **Severity: 1346.341** (Blast Radius: 13.84 * Doc Risk: 97.279%)
- `crypto/krb5/src/include/k5-int.h` -> **Severity: 333.689** (Blast Radius: 3.337 * Doc Risk: 99.9967%)
- `contrib/ncurses/ncurses/curses.priv.h` -> **Severity: 172.54** (Blast Radius: 1.726 * Doc Risk: 99.9653%)
- `crypto/krb5/src/include/k5-thread.h` -> **Severity: 157.206** (Blast Radius: 1.851 * Doc Risk: 84.9302%)
- `sbin/ipf/common/ipf.h` -> **Severity: 135.8** (Blast Radius: 1.358 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
