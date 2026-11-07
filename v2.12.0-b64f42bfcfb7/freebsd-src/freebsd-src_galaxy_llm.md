# ARCHITECTURAL_BRIEF: freebsd-src
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/freebsd/freebsd-src.git` |
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
- **Scope:** 85752 analyzed artifact(s), 18179820 LOC.
- **Load-bearing artifact:** `contrib/llvm-project/llvm/lib/CodeGen/AsmPrinter/DwarfDebug.cpp` -- 4766 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `contrib/llvm-project/llvm/lib/Passes/PassBuilder.cpp` -- pulls in 305 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `sys/netinet/tcp_stacks/rack.c` at magnitude 26152.76 (structural weight, not risk).
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
| Total Artifacts | 110116 |
| Analyzed Artifacts (Scanned) | 85752 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 24364 |
| Total LOC | 18179820 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 77.9% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7939 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0473 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 12.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3111 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 41850 | 12494305 | 48.8% |
| PLAINTEXT | 10941 | 8014 | 12.8% |
| CPP | 10518 | 3262865 | 12.3% |
| SHELL | 6469 | 407869 | 7.5% |
| MAKEFILE | 5349 | 286927 | 6.2% |
| YAML | 4669 | 392074 | 5.4% |
| PERL | 1860 | 386246 | 2.2% |
| M4 | 997 | 172414 | 1.2% |
| ASSEMBLY | 933 | 374796 | 1.1% |
| JSON | 540 | 103240 | 0.6% |
| MARKDOWN | 489 | 0 | 0.6% |
| PYTHON | 295 | 49818 | 0.3% |
| YACC | 172 | 61915 | 0.2% |
| TD | 122 | 87460 | 0.1% |
| HTML | 118 | 39170 | 0.1% |
| BMS | 87 | 1814 | 0.1% |
| XML | 66 | 49 | 0.1% |
| LUA | 65 | 10708 | 0.1% |
| CSHARP | 32 | 3473 | 0.0% |
| CSS | 30 | 6248 | 0.0% |
| FORTRAN | 26 | 16629 | 0.0% |
| GLSL | 18 | 18 | 0.0% |
| PHP | 17 | 216 | 0.0% |
| JAVA | 15 | 3211 | 0.0% |
| RUBY | 14 | 988 | 0.0% |
| BATCH | 13 | 768 | 0.0% |
| SQLITE | 11 | 1272 | 0.0% |
| CSV | 9 | 521 | 0.0% |
| LIVECODE | 6 | 2921 | 0.0% |
| POWERSHELL | 4 | 379 | 0.0% |
| REXX | 4 | 168 | 0.0% |
| TCL | 4 | 430 | 0.0% |
| MATLAB | 3 | 241 | 0.0% |
| DOCKERFILE | 2 | 45 | 0.0% |
| JAVASCRIPT | 2 | 215 | 0.0% |
| OBJECTIVE-C | 1 | 2313 | 0.0% |
| PROTO | 1 | 80 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 104 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 85509 |
| unknown | unknown | 136 |
| cp1252 | cp1252-fallback | 98 |
| latin-1 | latin-1-fallback | 6 |
| utf-8 | bom | 2 |
| utf-16-le | bom | 1 |

> 1 guessed file(s) read as double-byte text that decodes strictly as shift_jis / euc_jp / gbk / euc_kr: if that is the estate's code page, rescan with `--source-encoding shift_jis` (or the right one of those). E.g. `contrib/dialog/samples/msgbox4-eucjp`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 29%, Data / Markup / Trivial 27%, Large Core Modules (3) 11%, Large Core Modules 7%, Many-Argument Workhorses Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 74309 | 86.7% |
| Unknown | 136 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11287 | 13.2% |
| Static: Minified & Vendor Opaque Mass | 20 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 24364*

**Composition by Extension & Reason:**
- `no_extension`: 2621x Unsupported Format (.undeterminable), 637x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 323x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.depend`: 1573x Excluded (Unsupported Extension: '.depend'), 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 1103x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 94x Excluded: Neighborhood Micro-Mass Limit Exceeded, 24x Excluded (Machine-Generated Source Code Signature: 28 LOC)
- `.cpp`: 1186x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1761 LOC), 1x Excluded (Machine-Generated Source Code Signature: 709 LOC)
- `.d`: 1072x Excluded (Unsupported Extension: '.d'), 32x Excluded: Neighborhood Micro-Mass Limit Exceeded, 8x Unsupported Format (.d)
- `.src`: 940x Excluded (Unsupported Extension: '.src')
- `.yaml`: 36x Zero-Density Threshold (LOC: 51, Signals: 0), 34x Zero-Density Threshold (LOC: 52, Signals: 0), 30x Zero-Density Threshold (LOC: 53, Signals: 0)
- `.3`: 607x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 96 LOC), 1x Excluded (Saturation: Line 50 exceeds 500 chars)
- `.pem`: 578x Excluded (Unsupported Extension: '.pem')
- `.bc`: 532x Unsupported Format (.bc), 2x Excluded (Unsupported Extension: '.bc')
- `.td`: 517x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 2638 commas in 821 LOC), 1x Excluded (Embedded Array/Matrix Payload: 8044 commas in 2404 LOC)
- `.uu`: 506x Excluded (Unsupported Extension: '.uu'), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Unsupported Format (.uu)
- `.0`: 447x Unsupported Format (.0), 40x Excluded: Neighborhood Micro-Mass Limit Exceeded, 31x Excluded (Unsupported Extension: '.0')
- `.exp`: 513x Excluded (Unsupported Extension: '.exp'), 1x Unsupported Format (.exp)
- `.c`: 242x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded: Neighborhood Micro-Mass Limit Exceeded, 4x Excluded (Machine-Generated Source Code Signature: 57 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 22.7 | 5.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 39.2 | 52.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 15.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.8 | 0.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 40.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 48.7 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 216190 | 18217 | 5 | `contrib/llvm-project/clang/lib/Sema/SemaDecl.cpp` |
| cleanup | 54204 | 10917 | 1 | `crypto/heimdal/lib/gssapi/Makefile.in` |
| guards | 1005727 | 36981 | 29 | `contrib/llvm-project/clang/lib/Headers/altivec.h` |
| danger | 276132 | 20387 | 7 | `usr.sbin/etcupdate/etcupdate.sh` |
| concurrency | 36603 | 5438 | 0 | `sys/cam/ctl/ctl.c` |
| connectivity | 398433 | 38763 | 11 | `sys/dev/bnxt/bnxt_en/hsi_struct_def.h` |
| io | 126550 | 10527 | 1 | `contrib/lua/doc/manual.html` |
| crypto | 5 | 4 | 0 | `tests/sys/geom/class/eli/gentestvect.py` |
| ipc | 22106 | 4394 | 0 | `crypto/openssl/crypto/bn/asm/ppc64-mont.pl` |
| time | 10286 | 3197 | 0 | `contrib/tzcode/localtime.c` |
| serialization | 1619 | 291 | 0 | `contrib/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_common_interceptors.inc` |
| regex | 18530 | 3109 | 0 | `crypto/openssl/crypto/chacha/asm/chacha-loongarch64.pl` |
| events | 23990 | 4922 | 0 | `crypto/openssh/configure.ac` |
| tests | 23717 | 1270 | 0 | `contrib/googletest/googletest/test/gtest_unittest.cc` |
| docs | 410454 | 16704 | 3 | `contrib/llvm-project/clang/include/clang/ASTMatchers/ASTMatchers.h` |
| debt | 148702 | 19344 | 3 | `contrib/netbsd-tests/kernel/t_ptrace_wait.c` |
| mutation | 4195142 | 54765 | 118 | `contrib/one-true-awk/testdir/funstack.in` |
| dead_code | 176944 | 24166 | 4 | `contrib/llvm-project/lldb/source/Plugins/Instruction/ARM/EmulateInstructionARM.cpp` |
| credential | 1020 | 126 | 0 | `crypto/openssl/test/crltest.c` |
| threat | 1785 | 300 | 0 | `crypto/krb5/src/lib/crypto/crypto_tests/t_decrypt.c` |
| ml_ai | 37078 | 5756 | 0 | `contrib/llvm-project/clang/lib/Headers/avx512fintrin.h` |
| ui | 3702 | 330 | 0 | `contrib/lua/doc/manual.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `contrib/lua/doc/manual.html` (Hits: 1668)
- `usr.sbin/freebsd-update/freebsd-update.sh` (Hits: 1263)
- `contrib/lua/doc/contents.html` (Hits: 1094)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **DwarfDebug.cpp** (`contrib/llvm-project/llvm/lib/CodeGen/AsmPrinter/DwarfDebug.cpp`) — 4766 inbound connections
2. **kernel.h** (`sys/sys/kernel.h`) — 3265 inbound connections
3. **malloc.h** (`sys/sys/malloc.h`) — 2277 inbound connections
4. **socket.h** (`sys/sys/socket.h`) — 2253 inbound connections
5. **bus.h** (`sys/sys/bus.h`) — 2230 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **PassBuilder.cpp** (`contrib/llvm-project/llvm/lib/Passes/PassBuilder.cpp`) — 305 outbound dependencies
2. **sanitizer_platform_limits_netbsd.cpp** (`contrib/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.cpp`) — 202 outbound dependencies
3. **ASTReader.cpp** (`contrib/llvm-project/clang/lib/Serialization/ASTReader.cpp`) — 149 outbound dependencies
4. **PassBuilderPipelines.cpp** (`contrib/llvm-project/llvm/lib/Passes/PassBuilderPipelines.cpp`) — 125 outbound dependencies
5. **AsmPrinter.cpp** (`contrib/llvm-project/llvm/lib/CodeGen/AsmPrinter/AsmPrinter.cpp`) — 119 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ossl_aes_gcm_encrypt_avx512` **(Many-Argument Workhorses)** (@ `sys/crypto/openssl/amd64/aes-gcm-avx512.S`) -> Impact: **4990.7** | LOC: 65945
- `ossl_aes_gcm_decrypt_avx512` **(Many-Argument Workhorses)** (@ `sys/crypto/openssl/amd64/aes-gcm-avx512.S`) -> Impact: **4990.7** | LOC: 65945
- `hostapd_config_fill` **(Many-Argument Workhorses)** (@ `contrib/wpa/hostapd/config_file.c`) -> Impact: **3741.7** | LOC: 2672
  * *Intent:* #endif /* CONFIG_IEEE80211BE */
- `CodeGenFunction::EmitBuiltinExpr` **(Many-Argument Workhorses)** (@ `contrib/llvm-project/clang/lib/CodeGen/CGBuiltin.cpp`) -> Impact: **2947.5** | LOC: 3719
- `Clang::ConstructJob` **(Many-Argument Workhorses)** (@ `contrib/llvm-project/clang/lib/Driver/ToolChains/Clang.cpp`) -> Impact: **2616.3** | LOC: 3116
- `nfsv4_loadattr` **(Many-Argument Workhorses)** (@ `sys/fs/nfs/nfs_commonsubs.c`) -> Impact: **2574.7** | LOC: 1268
  * *Intent:* /* * Get the attributes for V4. * If the compare flag is true, test for any attribute changes, * otherwise return the attribute values. * These attrib...
- `sctp_setopt` **(Many-Argument Workhorses)** (@ `sys/netinet/sctp_usrreq.c`) -> Impact: **2285.8** | LOC: 3144
- `CodeGenFunction::EmitX86BuiltinExpr` **(Many-Argument Workhorses)** (@ `contrib/llvm-project/clang/lib/CodeGen/CGBuiltin.cpp`) -> Impact: **2262.4** | LOC: 2466
- `upgradeX86IntrinsicCall` **(Many-Argument Workhorses)** (@ `contrib/llvm-project/llvm/lib/IR/AutoUpgrade.cpp`) -> Impact: **2101.4** | LOC: 1689
- `CodeGenFunction::EmitAArch64BuiltinExpr` **(Many-Argument Workhorses)** (@ `contrib/llvm-project/clang/lib/CodeGen/CGBuiltin.cpp`) -> Impact: **1797.6** | LOC: 2592

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `sys/kern` | 243 | 204781.2 | 65.98% | 44.93% |
| `crypto/openssh/regress/unittests/hostkeys/testdata` | 30 | 150000.0 | 0.0% | 0.0% |
| `crypto/openssh/regress/unittests/sshkey/testdata` | 43 | 125000.18 | 0.0% | 0.0% |
| `sys/netinet` | 147 | 112026.12 | 36.0% | 16.79% |
| `crypto/openssh/regress/misc/fuzz-harness/testdata` | 18 | 80000.02 | 1.74% | 3.46% |
| `crypto/openssl/apps` | 73 | 70423.29 | 69.56% | 7.76% |
| `crypto/openssh/regress/unittests/sshsig/testdata` | 14 | 70000.0 | 0.0% | 0.0% |
| `sys/net` | 116 | 49150.9 | 32.24% | 19.62% |
| `sys/dev/qlnx/qlnxe` | 102 | 47245.5 | 18.09% | 10.26% |
| `sys/netpfil/ipfilter/netinet` | 45 | 46294.0 | 43.25% | 15.57% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `contrib/bmake/mk/sys/NetBSD.mk` -> **100.0%** Exposure
- `contrib/bmake/mk/sys/UnixWare.mk` -> **100.0%** Exposure
- `contrib/bmake/unit-tests/deptgt-suffixes.mk` -> **100.0%** Exposure
- `contrib/bmake/unit-tests/directive-for-escape.mk` -> **100.0%** Exposure
- `contrib/bmake/unit-tests/directive-include.mk` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cddl/usr.sbin/dwatch/libexec/Makefile` -> **100.0%** Exposure
- `contrib/bmake/unit-tests/Makefile` -> **100.0%** Exposure
- `contrib/bmake/unit-tests/varmod-hash.mk` -> **100.0%** Exposure
- `contrib/elftoolchain/libelf/os.Linux.mk` -> **100.0%** Exposure
- `contrib/wpa/hostapd/Android.mk` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `contrib/llvm-project/llvm/lib/IR/Core.cpp` -> **623** Orphaned Functions | **0** Duplicates
- `contrib/llvm-project/clang/lib/Headers/lasxintrin.h` -> **537** Orphaned Functions | **0** Duplicates
- `contrib/llvm-project/clang/lib/Headers/lsxintrin.h` -> **519** Orphaned Functions | **0** Duplicates
- `contrib/llvm-project/clang/include/clang/AST/OpenMPClause.h` -> **0** Orphaned Functions | **488** Duplicates
- `contrib/llvm-project/clang/lib/Serialization/ASTReader.cpp` -> **382** Orphaned Functions | **0** Duplicates

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
- **Binary Anomalies (X-Ray):** `1002` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `347692` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `sys/netinet/tcp_stacks/rack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.796)
- **Top Global Matches:** file_cluster_8: 8.796, file_cluster_6: 16.368, file_cluster_3: 23.001
- **Magnitude:** 26152.76 | **LOC:** 24750 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **74**; blast radius 0.005; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.1%), Guard Balance (formerly Safety Score) (81.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rack_output` **(Many-Argument Workhorses)** (Impact: 1229.6)
  * `rack_process_option` **(Many-Argument Workhorses)** (Impact: 694.8)
  * `rack_do_segment_nounlock` **(Many-Argument Workhorses)** (Impact: 486.0)
  * `rack_proc_sack_blk` **(Many-Argument Workhorses)** (Impact: 479.8)
  * `rack_fast_rsm_output` **(Many-Argument Workhorses)** (Impact: 424.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 4136 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 13384
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4683`, `structural_boundaries: 1978`, `args: 478`, `func_start: 218`, `class_start: 347`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 5112`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 9`
* *Architecture:* `api: 2`, `import: 75`
* *Defense:* `safety: 1`, `doc: 18`, `immutability_locks: 7`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 99):` cpu.h, in_cksum.h, route.h, nhop.h, vnet.h, cc.h, cc_newreno.h, in.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/fs/nfsclient/nfs_clrpcops.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.164)
- **Top Global Matches:** file_cluster_3: 7.164, file_cluster_8: 18.182, file_cluster_6: 31.067
- **Magnitude:** 15822.3 | **LOC:** 10019 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 0.006; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nfsrpc_readdirplus` **(Many-Argument Workhorses)** (Impact: 415.9)
    * *Intent:* /* * NFS V3 readdir plus RPC. Used in place of nfsrpc_readdir(). * (Also used for NFS V4 when mount ...
  * `nfsrpc_openrpc` **(Many-Argument Workhorses)** (Impact: 325.5)
    * *Intent:* /* * the actual open rpc */
  * `nfsrpc_readdir` **(Many-Argument Workhorses)** (Impact: 323.5)
    * *Intent:* * 3 - return them to userland in the "struct dirent", so future versions * of libc can use them and ...
  * `nfsrpc_createlayout` **(Many-Argument Workhorses)** (Impact: 287.8)
    * *Intent:* /* * Similar nfsrpc_createv4(), but also does the LayoutGet operation. * Used only for mounts with p...
  * `nfsrpc_rename` **(Many-Argument Workhorses)** (Impact: 277.6)
    * *Intent:* /* * Do an nfs rename rpc. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 25 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 2264 instances
* *Concurrency (weighted view):* 18
* *Memory Alloc (weighted view):* 26
* *State Mutation (weighted view):* 7262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2306`, `structural_boundaries: 1252`, `args: 441`, `func_start: 105`, `class_start: 407`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 2734`, `fragile_debt: 5`, `unreferenced_by_name: 44`
* *Architecture:* `api: 76`, `concurrency: 3`, `import: 7`
* *Defense:* `safety: 14`, `sync_locks: 6`, `immutability_locks: 4`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 33):` nfsport.h, nfs.h, opt_inet6.h, cdefs.h, extattr.h, sysctl.h, taskqueue.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `sys/dev/pms/RefTisa/tisa/sassata/sata/host/sat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.472)
- **Top Global Matches:** file_cluster_8: 5.472, file_cluster_6: 13.528, file_cluster_4: 22.295
- **Magnitude:** 15400.46 | **LOC:** 23309 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **31**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.3%), Complexity Load (formerly Cognitive Load) (32.9%)
- **Documentation Coverage:** 10.2767% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `satModeSense10` **(Many-Argument Workhorses)** (Impact: 281.8)
    * *Intent:* * * \param tiRoot: Pointer to TISA initiator driver/port instance. * \param tiIORequest: Pointer to ...
  * `satAddSATAIDDevCB` **(Many-Argument Workhorses)** (Impact: 212.1)
    * *Intent:* * new or old. If new, add it to the devicelist. * * \param agRoot: Handles for this instance of SAS/...
  * `satModeSelect10` **(Many-Argument Workhorses)** (Impact: 211.1)
    * *Intent:* * * \param tiRoot: Pointer to TISA initiator driver/port instance. * \param tiIORequest: Pointer to ...
  * `tdsaDiscoveryStartIDDevCB` **(Many-Argument Workhorses)** (Impact: 203.4)
    * *Intent:* * of discovery. * * \param agRoot: Handles for this instance of SAS/SATA hardware * \param agIOReque...
  * `satModeSelect6` **(Many-Argument Workhorses)** (Impact: 179.8)
    * *Intent:* * * \param tiRoot: Pointer to TISA initiator driver/port instance. * \param tiIORequest: Pointer to ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2054 instances
* *State Mutation (weighted view):* 9658
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1595`, `structural_boundaries: 765`, `args: 184`, `func_start: 125`
* *Risk/State:* `safety_bypasses: 118`, `state_mutation: 5550`, `dead_code: 38`, `unreferenced_by_name: 35`
* *Architecture:* `api: 125`, `import: 31`
* *Defense:* `doc: 847`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 40):` dm.h, dmapi.h, tddmapi.h, sa.h, saapi.h, saosapi.h, sm.h, smapi.h...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `sys/dev/pms/RefTisa/sat/src/smsat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.684)
- **Top Global Matches:** file_cluster_8: 5.684, file_cluster_6: 12.564, file_cluster_4: 21.258
- **Magnitude:** 15236.9 | **LOC:** 20820 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **15**; blast radius 0.007; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.2%), Complexity Load (formerly Cognitive Load) (63.9%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `smsatModeSense10` **(Many-Argument Workhorses)** (Impact: 281.8)
  * `smsatModeSelect10` **(Many-Argument Workhorses)** (Impact: 217.7)
  * `smsatModeSelect6` **(Many-Argument Workhorses)** (Impact: 186.4)
  * `smsatIOStart` **(Many-Argument Workhorses)** (Impact: 150.6)
  * `smsatModeSense6` **(Many-Argument Workhorses)** (Impact: 149.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2044 instances
* *State Mutation (weighted view):* 9733
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1582`, `structural_boundaries: 751`, `args: 200`, `func_start: 126`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 5645`, `dead_code: 241`, `unreferenced_by_name: 48`
* *Architecture:* `api: 126`, `import: 15`
* *Defense:* `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 26):` sa.h, saapi.h, saosapi.h, sm.h, smapi.h, tdsmapi.h, smdefs.h, smproto.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `sys/netinet/tcp_stacks/bbr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.907)
- **Top Global Matches:** file_cluster_8: 9.907, file_cluster_6: 11.234, file_cluster_4: 18.749
- **Magnitude:** 14419.34 | **LOC:** 14818 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **71**; blast radius 0.005; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bbr_output_wtime` **(Many-Argument Workhorses)** (Impact: 1021.6)
    * *Intent:* /* * Return 0 on success and a errno on failure to send. * Note that a 0 return may not mean we sent...
  * `bbr_set_sockopt` **(Many-Argument Workhorses)** (Impact: 319.1)
    * *Intent:* /* * bbr_ctloutput() must drop the inpcb lock before performing copyin on * socket option arguments....
  * `bbr_do_segment_nounlock` **(Many-Argument Workhorses)** (Impact: 290.1)
  * `bbr_process_data` **(Many-Argument Workhorses)** (Impact: 270.2)
    * *Intent:* /* * Return value of 1, the TCB is unlocked and most * likely gone, return value of 0, the TCB is st...
  * `bbr_log_ack` **(Many-Argument Workhorses)** (Impact: 188.6)
    * *Intent:* /* * Returns the number of bytes that were * acknowledged by SACK blocks. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 2182 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 6997
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2746`, `structural_boundaries: 1263`, `args: 291`, `func_start: 179`, `class_start: 180`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2633`, `planned_debt: 3`, `fragile_debt: 8`
* *Architecture:* `import: 71`
* *Defense:* `doc: 8`, `immutability_locks: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 92):` in_cksum.h, ethernet.h, if.h, if_var.h, route.h, nhop.h, vnet.h, cc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/netinet/sctp_output.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.482)
- **Top Global Matches:** file_cluster_3: 10.482, file_cluster_8: 14.395, file_cluster_6: 27.047
- **Magnitude:** 14401.46 | **LOC:** 13929 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **20**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.4%), Complexity Load (formerly Cognitive Load) (72.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sctp_med_chunk_output` **(Many-Argument Workhorses)** (Impact: 985.3)
  * `sctp_lower_sosend` **(Many-Argument Workhorses)** (Impact: 955.2)
  * `sctp_lowlevel_chunk_output` **(Many-Argument Workhorses)** (Impact: 624.5)
    * *Intent:* #endif
  * `sctp_send_initiate_ack` **(Many-Argument Workhorses)** (Impact: 573.8)
    * *Intent:* /* * Given a MBUF chain that was sent into us containing an INIT. Build a * INIT-ACK with COOKIE and...
  * `sctp_chunk_retransmission` **(Many-Argument Workhorses)** (Impact: 348.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2128 instances
* *State Mutation (weighted view):* 6754
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2283`, `structural_boundaries: 1707`, `args: 402`, `func_start: 85`, `class_start: 390`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 2498`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 18`, `unreferenced_by_name: 22`
* *Architecture:* `api: 46`, `import: 21`
* *Defense:* `safety: 2`, `doc: 12`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 50):` in_cksum.h, sctp_asconf.h, sctp_auth.h, sctp_bsd_addr.h, sctp_crc32.h, sctp_header.h, sctp_indata.h, sctp_input.h...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `sys/cam/ctl/ctl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.071)
- **Top Global Matches:** file_cluster_6: 7.071, file_cluster_4: 13.079, file_cluster_8: 13.171
- **Magnitude:** 12335.26 | **LOC:** 14553 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **42**; blast radius 0.008; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ctl_ioctl` **(Many-Argument Workhorses)** (Impact: 483.7)
  * `ctl_pro_preempt` **(Many-Argument Workhorses)** (Impact: 148.8)
    * *Intent:* /* * Returns 0 if ctl_persistent_reserve_out() should continue, non-zero if * it should return. */
  * `ctl_mode_sense` **(Compute Cores)** (Impact: 129.8)
  * `ctl_persistent_reserve_out` **(Compute Cores)** (Impact: 118.3)
  * `ctl_isc_event_handler` **(Many-Argument Workhorses)** (Impact: 105.0)
    * *Intent:* /* * ISC (Inter Shelf Communication) event handler. Events from the HA * subsystem come in here. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 115 instances
* *Amplified Race Conditions:* 106 instances
* *Amplified Cascading Flux:* 2009 instances
* *Concurrency (weighted view):* 650
* *Memory Alloc (weighted view):* 50
* *State Mutation (weighted view):* 6696
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2135`, `structural_boundaries: 2476`, `args: 409`, `func_start: 226`, `class_start: 485`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 2678`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 42`, `unreferenced_by_name: 72`
* *Architecture:* `api: 107`, `concurrency: 120`, `import: 42`
* *Defense:* `safety: 39`, `sync_locks: 322`, `immutability_locks: 66`, `cleanup: 96`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 56):` cam.h, ctl.h, ctl_backend.h, ctl_debug.h, ctl_error.h, ctl_frontend.h, ctl_ha.h, ctl_io.h...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `sys/dev/bxe/bxe.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.818)
- **Top Global Matches:** file_cluster_4: 5.818, file_cluster_6: 8.807, file_cluster_16: 12.225
- **Magnitude:** 12098.52 | **LOC:** 19454 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **11**; blast radius 0.008; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%), Complexity Load (formerly Cognitive Load) (65.3%)
- **Documentation Coverage:** 98.4405% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bxe_tx_encap` **(Many-Argument Workhorses)** (Impact: 135.8)
    * *Intent:* /* * Encapsulte an mbuf cluster into the tx bd chain and makes the memory * visible to the controlle...
  * `bxe_eioctl` **(Many-Argument Workhorses)** (Impact: 95.7)
  * `bxe_ioctl` **(Many-Argument Workhorses)** (Impact: 94.7)
    * *Intent:* /* * Handles any IOCTL calls from the operating system. * * Returns: * 0 = Success, >0 Failure */
  * `bxe_init_hw_common` **(Many-Argument Workhorses)** (Impact: 93.5)
    * *Intent:* /** * bxe_init_hw_common - initialize the HW at the COMMON phase. * * @sc: driver handle */
  * `bxe_check_blocks_with_parity1` **(Many-Argument Workhorses)** (Impact: 92.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 1872 instances
* *Concurrency (weighted view):* 18
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 6267
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2316`, `structural_boundaries: 1900`, `args: 680`, `func_start: 422`, `class_start: 276`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 2523`, `dead_code: 20`, `planned_debt: 3`, `fragile_debt: 105`, `unreferenced_by_name: 27`
* *Architecture:* `api: 51`, `concurrency: 3`, `import: 11`
* *Defense:* `safety: 39`, `doc: 67`, `sync_locks: 7`, `immutability_locks: 18`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 43):` 57710_int_offsets.h, 57711_int_offsets.h, 57712_int_offsets.h, bxe.h, bxe_dump.h, bxe_ioctl.h, ecore_init.h, ecore_init_ops.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `sys/netpfil/pf/pf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.247)
- **Top Global Matches:** file_cluster_6: 8.247, file_cluster_8: 9.596, file_cluster_4: 16.055
- **Magnitude:** 11990.76 | **LOC:** 12125 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 73.3%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **67**; blast radius 0.008; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (76.5%), Complexity Load (formerly Cognitive Load) (76.3%)
- **Documentation Coverage:** 99.3671% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pf_test` **(Many-Argument Workhorses)** (Impact: 518.0)
    * *Intent:* #if defined(INET) || defined(INET6)
  * `pf_test_state_icmp` **(Many-Argument Workhorses)** (Impact: 442.9)
  * `pf_tcp_track_full` **(Many-Argument Workhorses)** (Impact: 346.6)
  * `pf_test_rule` **(Many-Argument Workhorses)** (Impact: 245.4)
  * `pf_route` **(Many-Argument Workhorses)** (Impact: 235.7)
    * *Intent:* #ifdef INET
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 22 instances
* *Amplified Cascading Flux:* 1711 instances
* *Memory Alloc (weighted view):* 12
* *State Mutation (weighted view):* 5339
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2421`, `structural_boundaries: 2011`, `args: 496`, `func_start: 173`, `class_start: 405`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1917`, `planned_debt: 1`, `fragile_debt: 12`, `unreferenced_by_name: 24`
* *Architecture:* `api: 86`, `concurrency: 3`, `import: 68`
* *Defense:* `safety: 11`, `doc: 1`, `sync_locks: 6`, `immutability_locks: 63`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.008
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 111):` sha512.h, in_cksum.h, if.h, if_pflog.h, if_pfsync.h, if_private.h, if_types.h, if_var.h...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `sys/dev/cxgbe/t4_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.936)
- **Top Global Matches:** file_cluster_4: 6.936, file_cluster_6: 8.397, file_cluster_16: 13.622
- **Magnitude:** 11148.1 | **LOC:** 14378 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 53.3%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **51**; blast radius 0.009; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.8%), Complexity Load (formerly Cognitive Load) (79.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `port_mword` **(Compute Cores)** (Impact: 166.1)
    * *Intent:* /* * Base media word (without ETHER, pause, link active, etc.) for the port at the * given speed. */
  * `cxgbe_ioctl` **(Many-Argument Workhorses)** (Impact: 163.4)
  * `t4_ioctl` **(Many-Argument Workhorses)** (Impact: 132.8)
  * `sysctl_meminfo` **(Many-Argument Workhorses)** (Impact: 127.6)
  * `t4_attach` **(Many-Argument Workhorses)** (Impact: 116.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 64 instances
* *Amplified Race Conditions:* 66 instances
* *Amplified Cascading Flux:* 1934 instances
* *Concurrency (weighted view):* 399
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 6100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2047`, `structural_boundaries: 1683`, `args: 775`, `func_start: 262`, `class_start: 381`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 2232`, `fragile_debt: 6`, `unreferenced_by_name: 15`
* *Architecture:* `api: 47`, `concurrency: 69`, `import: 51`
* *Defense:* `safety: 25`, `test: 17`, `sync_locks: 139`, `immutability_locks: 78`, `cleanup: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.009
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 100):` common.h, t4_msg.h, t4_regs.h, t4_regs_values.h, cudbg.h, db_lex.h, ddb.h, pcireg.h...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `sys/ufs/ffs/ffs_softdep.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.733)
- **Top Global Matches:** file_cluster_4: 5.733, file_cluster_6: 8.859, file_cluster_16: 12.36
- **Magnitude:** 10512.04 | **LOC:** 15021 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **42**; blast radius 0.006; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.2%), Complexity Load (formerly Cognitive Load) (70.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `softdep_journal_freeblocks` **(Many-Argument Workhorses)** (Impact: 144.2)
    * *Intent:* * disk through step 4. * 4) Reap unsatisfied dependencies that are beyond the truncated area, * elim...
  * `handle_written_inodeblock` **(Many-Argument Workhorses)** (Impact: 137.1)
    * *Intent:* /* * Called from within softdep_disk_write_complete above to restore * in-memory inode block content...
  * `softdep_process_journal` **(Many-Argument Workhorses)** (Impact: 109.2)
    * *Intent:* /* * Flush some journal records to disk. */
  * `softdep_check_suspend` **(Many-Argument Workhorses)** (Impact: 100.2)
    * *Intent:* /* * Check if it is safe to suspend the file system now. On entry, * the vnode interlock for devvp s...
  * `initiate_write_inodeblock_ufs2` **(Many-Argument Workhorses)** (Impact: 99.8)
    * *Intent:* /* * Version of initiate_write_inodeblock that handles UFS2 dinodes. * Note that any bug fixes made ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 14 instances
* *Amplified Cascading Flux:* 1669 instances
* *Memory Alloc (weighted view):* 38
* *State Mutation (weighted view):* 5348
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1890`, `structural_boundaries: 2638`, `args: 776`, `func_start: 324`, `class_start: 919`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 2010`, `planned_debt: 1`, `fragile_debt: 10`, `unreferenced_by_name: 9`
* *Architecture:* `api: 107`, `concurrency: 1`, `import: 42`
* *Defense:* `test: 11`, `sync_locks: 2`, `immutability_locks: 4`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 68):` ddb.h, geom.h, geom_vfs.h, opt_ddb.h, opt_ffs.h, opt_quota.h, bio.h, buf.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `sys/amd64/amd64/pmap.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.252)
- **Top Global Matches:** file_cluster_4: 5.252, file_cluster_6: 10.308, file_cluster_16: 11.011
- **Magnitude:** 10144.42 | **LOC:** 12332 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **59**; blast radius 0.01; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.9%)
- **Documentation Coverage:** 99.375% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pmap_enter` **(Many-Argument Workhorses)** (Impact: 193.5)
    * *Intent:* * the specified virtual address (v) in the * target physical map with the protection requested. * * ...
  * `pmap_change_props_locked` **(Many-Argument Workhorses)** (Impact: 149.2)
  * `pmap_copy` **(Many-Argument Workhorses)** (Impact: 102.4)
    * *Intent:* /* * Copy the range specified by src_addr/len * from the source map to the range dst_addr/len * in t...
  * `pmap_enter_pde` **(Many-Argument Workhorses)** (Impact: 102.1)
    * *Intent:* * KERN_FAILURE if either (1) PMAP_ENTER_NOREPLACE was specified and a 4KB * page mapping already exi...
  * `pmap_enter_quick_locked` **(Many-Argument Workhorses)** (Impact: 88.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 1765 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 5523
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1658`, `structural_boundaries: 1313`, `args: 552`, `func_start: 311`, `class_start: 143`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 1993`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 6`
* *Architecture:* `api: 165`, `concurrency: 13`, `import: 59`
* *Defense:* `safety: 3`, `doc: 8`, `sync_locks: 21`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 77):` ddb.h, asan.h, cpu.h, cputypes.h, intr_machdep.h, md_var.h, msan.h, pcb.h...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `sbin/camcontrol/camcontrol.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.781)
- **Top Global Matches:** file_cluster_8: 7.781, file_cluster_3: 17.719, file_cluster_6: 19.309
- **Magnitude:** 10140.14 | **LOC:** 10824 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **32**; blast radius 0.006; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readdefects` **(Many-Argument Workhorses)** (Impact: 381.0)
  * `sanitize` **(Many-Argument Workhorses)** (Impact: 335.4)
  * `ratecontrol` **(Many-Argument Workhorses)** (Impact: 288.0)
  * `mmcsdcmd` **(Many-Argument Workhorses)** (Impact: 274.5)
  * `atacapprint` **(Compute Cores)** (Impact: 239.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 60 instances
* *Amplified Cascading Flux:* 1408 instances
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 4300
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2059`, `structural_boundaries: 1075`, `args: 183`, `func_start: 104`, `class_start: 190`
* *Risk/State:* `safety_bypasses: 38`, `high_risk_execution: 4`, `state_mutation: 1484`, `dead_code: 1`, `fragile_debt: 9`, `unreferenced_by_name: 3`
* *Architecture:* `io: 12`, `api: 20`, `import: 34`
* *Defense:* `safety: 9`, `test: 3`, `immutability_locks: 35`, `cleanup: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 45):` ata_all.h, cam.h, cam_ccb.h, cam_debug.h, mmc_all.h, scsi_all.h, scsi_da.h, scsi_message.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `sys/fs/nfsserver/nfs_nfsdport.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.986)
- **Top Global Matches:** file_cluster_8: 6.986, file_cluster_6: 10.843, file_cluster_4: 19.356
- **Magnitude:** 9646.92 | **LOC:** 7622 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **13**; blast radius 0.006; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nfsrvd_readdirplus` **(Many-Argument Workhorses)** (Impact: 369.1)
    * *Intent:* /* * Readdirplus for V3 and Readdir for V4. */
  * `nfsv4_sattr` **(Many-Argument Workhorses)** (Impact: 340.8)
    * *Intent:* /* * Handle the setable attributes for V4. * Returns NFSERR_BADXDR if it can't be parsed, 0 otherwis...
  * `nfsrv_dsgetsockmnt` **(Many-Argument Workhorses)** (Impact: 326.8)
    * *Intent:* /* * Get the DS mount point, fh and directory from the "pnfsd.dsfile" extended * attribute. * newnmp...
  * `nfsrv_proxyds` **(Many-Argument Workhorses)** (Impact: 208.0)
  * `nfsvno_open` **(Many-Argument Workhorses)** (Impact: 164.5)
    * *Intent:* /* * Do the vnode op stuff for Open. Similar to nfsvno_createsub(), but * must handle nfsrv_openchec...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 126 instances
* *Amplified Cascading Flux:* 1544 instances
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 4794
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1549`, `structural_boundaries: 943`, `args: 210`, `func_start: 106`, `class_start: 275`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 1706`, `planned_debt: 2`, `fragile_debt: 7`, `unreferenced_by_name: 39`
* *Architecture:* `api: 85`, `import: 13`
* *Defense:* `safety: 3`, `test: 7`, `immutability_locks: 3`, `cleanup: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 59):` nfsport.h, nlm.h, nlm_prot.h, mac_framework.h, callout.h, capsicum.h, extattr.h, filio.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `sys/fs/nfs/nfs_commonsubs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.992)
- **Top Global Matches:** file_cluster_8: 5.992, file_cluster_6: 12.961, file_cluster_4: 21.647
- **Magnitude:** 9629.58 | **LOC:** 5610 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **8**; blast radius 0.013; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.8%), Guard Balance (formerly Safety Score) (85.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nfsv4_loadattr` **(Many-Argument Workhorses)** (Impact: 2574.7)
    * *Intent:* /* * Get the attributes for V4. * If the compare flag is true, test for any attribute changes, * oth...
  * `nfsv4_fillattr` **(Many-Argument Workhorses)** (Impact: 1000.2)
    * *Intent:* /* * Fill in the attributes as marked by the bitmap (V4). */
  * `nfscl_reqstart` **(Many-Argument Workhorses)** (Impact: 163.5)
    * *Intent:* /* * Start building a request. Mostly just put the first file handle in * place. */
  * `nfscl_fillsattr` **(Many-Argument Workhorses)** (Impact: 141.6)
    * *Intent:* /* * Fill in the setable attributes. The full argument indicates whether * to fill in them all or ju...
  * `nfssvc_idname` **(Many-Argument Workhorses)** (Impact: 139.9)
    * *Intent:* /* * This function is called from the nfssvc(2) system call, to update the * kernel user/group name ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 53 instances
* *Amplified Race Conditions:* 27 instances
* *Amplified Cascading Flux:* 1359 instances
* *Concurrency (weighted view):* 162
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 4120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1388`, `structural_boundaries: 526`, `args: 211`, `func_start: 59`, `class_start: 80`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1402`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 30`
* *Architecture:* `api: 56`, `concurrency: 27`, `import: 8`
* *Defense:* `sync_locks: 59`, `immutability_locks: 3`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 25):` nfsport.h, nfsmount.h, opt_inet.h, opt_inet6.h, mac_framework.h, cdefs.h, extattr.h, vm_param.h
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `sys/dev/bxe/bxe_elink.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.273)
- **Top Global Matches:** file_cluster_4: 7.273, file_cluster_6: 7.558, file_cluster_16: 14.05
- **Magnitude:** 9480.7 | **LOC:** 15119 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.005; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.6%), Complexity Load (formerly Cognitive Load) (59.5%)
- **Documentation Coverage:** 83.9228% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `elink_set_led` **(Many-Argument Workhorses)** (Impact: 101.4)
  * `elink_link_update` **(Many-Argument Workhorses)** (Impact: 95.0)
    * *Intent:* /* The elink_link_update function should be called upon link * interrupt. * Link is considered up as...
  * `elink_populate_ext_phy` **(Many-Argument Workhorses)** (Impact: 88.4)
  * `elink_get_link_speed_duplex` **(Many-Argument Workhorses)** (Impact: 81.3)
  * `elink_848x3_config_init` **(Many-Argument Workhorses)** (Impact: 80.7)
    * *Intent:* #define PHY84833_CONSTANT_LATENCY 1193
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1357 instances
* *State Mutation (weighted view):* 4345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1823`, `structural_boundaries: 1548`, `args: 384`, `func_start: 281`, `class_start: 456`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1631`, `fragile_debt: 2`, `unreferenced_by_name: 21`
* *Architecture:* `api: 31`, `import: 7`
* *Defense:* `doc: 79`, `immutability_locks: 90`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 8):` bxe.h, bxe_elink.h, ecore_fw_defs.h, ecore_hsi.h, ecore_mfw_req.h, ecore_reg.h, cdefs.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sys/netpfil/ipfilter/netinet/fil.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.1)
- **Top Global Matches:** file_cluster_6: 7.1, file_cluster_4: 9.565, file_cluster_8: 17.156
- **Magnitude:** 9177.64 | **LOC:** 10060 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **54** in-repo importer(s); it depends on **49**; blast radius 0.035; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.6%), Guard Balance (formerly Safety Score) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ipf_checkl4sum` **(Many-Argument Workhorses)** (Impact: 926.2)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* Function: ipf_chec...
  * `frrequest` **(Many-Argument Workhorses)** (Impact: 565.6)
    * *Intent:* /* Parameters: unit(I) - device for which this is for */ /* req(I) - ioctl command (SIOC*) */ /* dat...
  * `ipf_ipf_ioctl` **(Many-Argument Workhorses)** (Impact: 220.3)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* Function: ipf_ipf_...
  * `ipf_scanlist` **(Many-Argument Workhorses)** (Impact: 122.8)
    * *Intent:* /* Returns: int - result flags of scanning filter list */ /* Parameters: fin(I) - pointer to packet ...
  * `ipf_ipftune` **(Many-Argument Workhorses)** (Impact: 102.3)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* Function: ipf_tune...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1429 instances
* *State Mutation (weighted view):* 4450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1588`, `structural_boundaries: 869`, `args: 310`, `func_start: 154`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 1592`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 7`, `unreferenced_by_name: 41`
* *Architecture:* `api: 103`, `import: 51`
* *Defense:* `safety: 16`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.035
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 52):` ipf.h, ipt.h, af.h, bpf.h, if.h, icmp6.h, in.h, in_systm.h...
  * `Imported By (In-Degree: 54):` (Excluded from Brief to save tokens)

### `sys/fs/nfsserver/nfs_nfsdstate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.694)
- **Top Global Matches:** file_cluster_8: 8.694, file_cluster_6: 9.318, file_cluster_4: 17.399
- **Magnitude:** 9125.16 | **LOC:** 9058 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 0.006; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.8%), Complexity Load (formerly Cognitive Load) (78.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nfsrv_lockctrl` **(Many-Argument Workhorses)** (Impact: 637.7)
    * *Intent:* /* * Lock control function called to update lock status. * Returns 0 upon success, -1 if there is no...
  * `nfsrv_openctrl` **(Many-Argument Workhorses)** (Impact: 390.2)
    * *Intent:* /* * Open control function to create/update open state for an open. */
  * `nfsrv_getclient` **(Many-Argument Workhorses)** (Impact: 270.5)
    * *Intent:* /* * Check to see if the client id exists and optionally confirm it. */
  * `nfsrv_opencheck` **(Many-Argument Workhorses)** (Impact: 170.9)
    * *Intent:* /* * Check for state errors for Open. * repstat is passed back out as an error if more critical erro...
  * `nfsrv_mdscopymr` **(Many-Argument Workhorses)** (Impact: 168.6)
    * *Intent:* /* * Look up the MDS file shared locked, and then get the extended attribute * to find the extant DS...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 77 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1328 instances
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 4244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1549`, `structural_boundaries: 931`, `args: 275`, `func_start: 119`, `class_start: 243`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1588`, `fragile_debt: 3`, `unreferenced_by_name: 38`
* *Architecture:* `api: 69`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 2`, `test: 11`, `sync_locks: 2`, `immutability_locks: 2`, `cleanup: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 24):` nfsport.h, opt_inet.h, opt_inet6.h, cdefs.h, extattr.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `sys/fs/nfsserver/nfs_nfsdserv.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.327)
- **Top Global Matches:** file_cluster_3: 6.327, file_cluster_8: 25.145, file_cluster_6: 38.165
- **Magnitude:** 8962.56 | **LOC:** 6703 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.005; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.0%), Complexity Load (formerly Cognitive Load) (83.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nfsrvd_open` **(Many-Argument Workhorses)** (Impact: 517.8)
    * *Intent:* /* * nfsv4 open service */
  * `nfsrvd_setattr` **(Many-Argument Workhorses)** (Impact: 231.0)
    * *Intent:* /* * nfs setattr service */
  * `nfsrvd_read` **(Many-Argument Workhorses)** (Impact: 166.8)
    * *Intent:* /* * nfs read service */
  * `nfsrvd_clone` **(Many-Argument Workhorses)** (Impact: 163.6)
    * *Intent:* /* * nfs clone service */
  * `nfsrvd_mknod` **(Many-Argument Workhorses)** (Impact: 159.9)
    * *Intent:* /* * nfs v3 mknod service (and v4 create) */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 50 instances
* *Amplified Cascading Flux:* 1459 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 4700
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1508`, `structural_boundaries: 538`, `args: 276`, `func_start: 64`, `class_start: 151`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1782`, `fragile_debt: 2`, `unreferenced_by_name: 62`
* *Architecture:* `api: 77`, `import: 6`
* *Defense:* `safety: 4`, `cleanup: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 19):` nfsport.h, opt_inet.h, opt_inet6.h, cdefs.h, extattr.h, filio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/dev/ocs_fc/ocs_hw.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.126)
- **Top Global Matches:** file_cluster_4: 6.126, file_cluster_6: 8.893, file_cluster_16: 13.193
- **Magnitude:** 8473.26 | **LOC:** 12703 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **4**; blast radius 0.011; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.0%), Complexity Load (formerly Cognitive Load) (54.9%)
- **Documentation Coverage:** 27.2171% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ocs_hw_get` **(Many-Argument Workhorses)** (Impact: 212.3)
  * `ocs_hw_io_send` **(Many-Argument Workhorses)** (Impact: 176.2)
    * *Intent:* * @param type Type of IO (target read, target response, and so on). * @param io Previously-allocated...
  * `ocs_hw_init` **(Many-Argument Workhorses)** (Impact: 156.6)
    * *Intent:* * @ingroup devInitShutdown * @brief Allocate memory structures to prepare for the device operation. ...
  * `ocs_hw_set` **(Many-Argument Workhorses)** (Impact: 155.1)
  * `ocs_hw_srrs_send` **(Many-Argument Workhorses)** (Impact: 148.4)
    * *Intent:* * * @param hw Hardware context. * @param type Type of sequence (ELS request/response, FC-CT). * @par...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1227 instances
* *State Mutation (weighted view):* 3840
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1704`, `structural_boundaries: 1188`, `args: 323`, `func_start: 225`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 1386`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 19`, `unreferenced_by_name: 64`
* *Architecture:* `api: 114`, `import: 4`
* *Defense:* `safety: 2`, `doc: 179`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 16):` ocs.h, ocs_hw.h, ocs_hw_queues.h, ocs_os.h
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `sys/arm64/arm64/pmap.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.885)
- **Top Global Matches:** file_cluster_4: 6.885, file_cluster_6: 7.06, file_cluster_16: 14.532
- **Magnitude:** 8391.84 | **LOC:** 10232 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **49**; blast radius 0.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.4%), Complexity Load (formerly Cognitive Load) (74.6%)
- **Documentation Coverage:** 98.5251% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pmap_enter` **(Many-Argument Workhorses)** (Impact: 250.2)
    * *Intent:* /* * Insert the given physical page (p) at * the specified virtual address (v) in the * target physi...
  * `pmap_change_props_locked` **(Many-Argument Workhorses)** (Impact: 131.9)
  * `pmap_enter_quick_locked` **(Many-Argument Workhorses)** (Impact: 116.5)
  * `pmap_enter_l3c` **(Many-Argument Workhorses)** (Impact: 111.4)
  * `pmap_enter_l2` **(Many-Argument Workhorses)** (Impact: 110.1)
    * *Intent:* /* * Tries to create the specified L2 page mapping. Returns KERN_SUCCESS if * the mapping was create...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 1374 instances
* *Concurrency (weighted view):* 61
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 4270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1410`, `structural_boundaries: 1072`, `args: 487`, `func_start: 212`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 1522`, `planned_debt: 5`, `fragile_debt: 3`
* *Architecture:* `api: 135`, `concurrency: 11`, `import: 49`
* *Defense:* `safety: 3`, `doc: 7`, `sync_locks: 17`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.007
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 66):` asan.h, cpu_feat.h, elf.h, ifunc.h, machdep.h, md_var.h, pcb.h, opt_vm.h...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `sys/netpfil/ipfilter/netinet/ip_nat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.002)
- **Top Global Matches:** file_cluster_8: 10.002, file_cluster_3: 14.63, file_cluster_6: 22.275
- **Magnitude:** 8302.24 | **LOC:** 8417 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **49**; blast radius 0.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ipf_nat_ioctl` **(Many-Argument Workhorses)** (Impact: 332.6)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* Function: ipf_nat_...
  * `ipf_nat_inlookup` **(Many-Argument Workhorses)** (Impact: 202.1)
    * *Intent:* /* mapdst(I) - destination IP address */ /* */ /* Lookup a nat entry based on the mapped destination...
  * `ipf_nat_outlookup` **(Many-Argument Workhorses)** (Impact: 191.8)
    * *Intent:* /* rw(I) - 1 == write lock on held, 0 == read lock. */ /* */ /* Lookup a nat entry based on the sour...
  * `ipf_nat_matcharray` **(Many-Argument Workhorses)** (Impact: 151.1)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* Function: ipf_nat_...
  * `ipf_nat_newmap` **(Many-Argument Workhorses)** (Impact: 148.5)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* Function: ipf_nat_...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1438 instances
* *State Mutation (weighted view):* 4447
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1541`, `structural_boundaries: 570`, `args: 181`, `func_start: 80`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 68`, `state_mutation: 1571`, `planned_debt: 1`, `fragile_debt: 3`, `unreferenced_by_name: 15`
* *Architecture:* `api: 46`, `import: 51`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 44):` md5.h, af.h, if.h, if_var.h, in.h, in_systm.h, ip.h, ip_compat.h...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `sys/dev/pms/RefTisa/sat/src/smsatcb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 15.545)
- **Top Global Matches:** file_cluster_3: 15.545, file_cluster_1: 34.265, file_cluster_8: 36.557
- **Magnitude:** 8123.0 | **LOC:** 13769 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 0.005; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.6%), Complexity Load (formerly Cognitive Load) (43.6%)
- **Documentation Coverage:** 84.7458% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `smsatLogSenseCB` **(Many-Argument Workhorses)** (Impact: 277.1)
  * `smsatDelayedProcessAbnormalCompletion` **(Many-Argument Workhorses)** (Impact: 272.7)
  * `smsatProcessAbnormalCompletion` **(Many-Argument Workhorses)** (Impact: 266.9)
  * `smsatStartStopUnitCB` **(Many-Argument Workhorses)** (Impact: 184.2)
  * `smsatRequestSenseCB` **(Many-Argument Workhorses)** (Impact: 178.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 769 instances
* *State Mutation (weighted view):* 2880
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1486`, `structural_boundaries: 649`, `args: 80`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 240`, `state_mutation: 1342`, `dead_code: 15`, `unreferenced_by_name: 47`
* *Architecture:* `api: 60`, `import: 15`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.005
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 24):` sa.h, saapi.h, saosapi.h, sm.h, smapi.h, tdsmapi.h, smdefs.h, smproto.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sys/dev/sound/pci/hda/hdaa.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.572)
- **Top Global Matches:** file_cluster_8: 10.572, file_cluster_3: 14.548, file_cluster_6: 22.72
- **Magnitude:** 8074.28 | **LOC:** 7175 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.006; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.2%)
- **Documentation Coverage:** 99.2806% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hdaa_audio_trace_dac` **(Many-Argument Workhorses)** (Impact: 131.3)
    * *Intent:* /* * Trace path from DAC to pin. */
  * `hdaa_audio_trace_adc` **(Many-Argument Workhorses)** (Impact: 130.6)
    * *Intent:* /* * Trace path from widget to ADC. */
  * `hdaa_audio_ctl_source_amp` **(Many-Argument Workhorses)** (Impact: 110.0)
    * *Intent:* /* * Find controls to control amplification for source and calculate possible * amplification range....
  * `hdaa_pcmchannel_setup` **(Compute Cores)** (Impact: 107.7)
  * `hdaa_audio_ctl_dest_amp` **(Many-Argument Workhorses)** (Impact: 97.8)
    * *Intent:* /* * Find controls to control amplification for destination and calculate * possible amplification r...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 1394 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 4269
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1800`, `structural_boundaries: 857`, `args: 177`, `func_start: 128`, `class_start: 177`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1481`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 5`
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 29`, `doc: 2`, `sync_locks: 2`, `immutability_locks: 30`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.006
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 17):` hda_reg.h, hdaa.h, hdac.h, sound.h, mixer_if.h, opt_snd.h, ctype.h, taskqueue.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sys/dev/cxgbe/common/t4_hw.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.207)
- **Top Global Matches:** file_cluster_4: 5.207, file_cluster_16: 8.264, file_cluster_15: 8.832
- **Magnitude:** 7971.48 | **LOC:** 13642 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **8**; blast radius 0.017; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (71.2%), Guard Balance (formerly Safety Score) (70.4%)
- **Documentation Coverage:** 28.7846% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `t4_wr_mbox_meat_timeout` **(Many-Argument Workhorses)** (Impact: 105.2)
    * *Intent:* * store the FW's reply to the command. The command and its optional * reply are of the same length. ...
  * `t4_link_l1cfg` **(Many-Argument Workhorses)** (Impact: 73.6)
    * *Intent:* /** * t4_link_l1cfg - apply link configuration to MAC/PHY * @phy: the PHY to setup * @mac: the MAC t...
  * `t4_fw_hello` **(Many-Argument Workhorses)** (Impact: 62.1)
    * *Intent:* /** * t4_fw_hello - establish communication with FW * @adap: the adapter * @mbox: mailbox to use for...
  * `t4_filter_field_shift` **(Compute Cores)** (Impact: 58.4)
    * *Intent:* /** * t4_filter_field_shift - calculate filter field shift * @adap: the adapter * @filter_sel: the d...
  * `mem_intr_handler` **(Many-Argument Workhorses)** (Impact: 57.6)
    * *Intent:* /* * EDC/MC interrupt handler. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1312 instances
* *State Mutation (weighted view):* 4355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1037`, `structural_boundaries: 1209`, `args: 663`, `func_start: 256`, `class_start: 113`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1731`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 129`
* *Architecture:* `api: 191`, `import: 8`
* *Defense:* `safety: 21`, `doc: 164`, `test: 1`, `immutability_locks: 253`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` common.h, t4fw_interface.h, opt_inet.h, cdefs.h, eventhandler.h, param.h, t4_regs.h, t4_regs_values.h
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `contrib/llvm-project/llvm/include/llvm/IR/ValueSymbolTable.h` (CPP) | Magnitude: 0.2 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 55, doc: 53, indent_spaces: 33, class_start: 12
- `contrib/llvm-project/llvm/include/llvm/Support/ArrayRecycler.h` (CPP) | Magnitude: 0.57 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 59, doc: 31, args: 27, structural_boundaries: 24
- `contrib/llvm-project/lld/ELF/InputSection.h` (CPP) | Magnitude: 1.08 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 234, structural_boundaries: 132, pointers: 83, args: 58
- `contrib/llvm-project/llvm/include/llvm/CodeGen/NonRelocatableStringpool.h` (CPP) | Magnitude: 0.12 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 21, structural_boundaries: 16, indent_spaces: 15, args: 7
- `contrib/llvm-project/libcxx/include/__bit/has_single_bit.h` (CPP) | Magnitude: 0.03 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: macros: 6, import: 3, structural_boundaries: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `contrib/llvm-project/lldb/source/Host/common/LockFileBase.cpp` (CPP) | Magnitude: 0.45 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 23, immutability_locks: 23, func_start: 11
- `contrib/llvm-project/llvm/lib/LTO/SummaryBasedOptimizations.cpp` (CPP) | Magnitude: 0.17 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 29, pointers: 19, args: 15
- `contrib/ntp/sntp/unity/auto/generate_module.rb` (RUBY) | Magnitude: 1.67 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 107, branch: 46, state_mutation: 29, io: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `contrib/llvm-project/clang/lib/Driver/DriverOptions.cpp` (CPP) | Magnitude: 0.04 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 9, import: 9, macros: 8, immutability_locks: 8
- `contrib/llvm-project/llvm/include/llvm/MC/MCSchedule.h` (CPP) | Magnitude: 0.49 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 127, doc: 110, immutability_locks: 56, structural_boundaries: 36
- `contrib/llvm-project/clang/include/clang/AST/StmtOpenACC.h` (CPP) | Magnitude: 0.74 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 139, structural_boundaries: 60, immutability_locks: 41, pointers: 39
- `contrib/llvm-project/lldb/source/API/SBModuleSpec.cpp` (CPP) | Magnitude: 0.68 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 93, pointers: 74, func_start: 36, structural_boundaries: 35
- `lib/libc/rpc/svc_run.c` (C) | Magnitude: 24.84 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 27, import: 12, pointers: 10, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `contrib/llvm-project/compiler-rt/lib/profile/InstrProfilingPort.h` (C) | Magnitude: 0.05 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: macros: 81, args: 25, reflection_metaprogramming: 24, indent_spaces: 19
- `contrib/llvm-project/libunwind/src/UnwindCursor.hpp` (CPP) | Magnitude: 19.45 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1843, structural_boundaries: 624, branch: 414, pointers: 348
- `sys/contrib/dev/iwlwifi/mld/session-protect.c` (C) | Magnitude: 1.38 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 124, pointers: 84, structural_boundaries: 66, class_start: 28
- `contrib/llvm-project/llvm/lib/MC/MCDisassembler/Disassembler.cpp` (CPP) | Magnitude: 1.53 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 187, pointers: 117, args: 71, branch: 34
- `contrib/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_unwind_fuchsia.cpp` (CPP) | Magnitude: 0.16 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 21, pointers: 16, structural_boundaries: 9, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `contrib/libarchive/libarchive/test/test_write_format_zip_zip64.c` (C) | Magnitude: 0.08 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 17, pointers: 4, structural_boundaries: 3, safety: 3
- `contrib/llvm-project/libcxx/include/__utility/unreachable.h` (CPP) | Magnitude: 0.03 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: macros: 6, structural_boundaries: 4, func_start: 2, import: 2
- `crypto/openssl/test/recipes/15-test_gendsa.t` (PERL) | Magnitude: 0.19 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 109, branch: 33, test: 20, structural_boundaries: 12
- `contrib/llvm-project/compiler-rt/lib/nsan/tests/NSanUnitTest.cpp` (CPP) | Magnitude: 0.12 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, args: 30, test: 27, explicit_casts: 25
- `contrib/libarchive/libarchive/test/test_compat_tar_directory.c` (C) | Magnitude: 0.06 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 22, args: 5, pointers: 5, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `libexec/rc/rc.d/nfsd` (SHELL) | Magnitude: 40.82 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 30, structural_boundaries: 24, branch: 14, io: 13
- `contrib/ntp/libntp/Makefile.in` (MAKEFILE) | Magnitude: 2.05 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 776, core_var_decl: 412, structural_boundaries: 396, design_upper_case: 256
- `libexec/rc/rc.d/noshutdown` (SHELL) | Magnitude: 21.66 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 5, core_var_decl: 5, design_snake_case: 5, structural_boundaries: 3
- `sys/contrib/openzfs/contrib/dracut/02zfsexpandknowledge/module-setup.sh.in` (SHELL) | Magnitude: 1.01 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 85, branch: 27, io: 27
- `cddl/contrib/opensolaris/cmd/dtrace/test/tst/common/printa/tst.largeusersym.ksh` (SHELL) | Magnitude: 0.2 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 19, structural_boundaries: 16, io: 9, safety_bypasses: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `contrib/libarchive/libarchive/test/test_compat_bzip2.c` (C) | Magnitude: 0.18 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 28, pointers: 6, structural_boundaries: 4, state_mutation: 3
- `contrib/netbsd-tests/fs/vfs/t_full.c` (C) | Magnitude: 0.52 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 34, branch: 12, import: 11, state_mutation: 8
- `sys/dev/drm2/ttm/ttm_lock.c` (C) | Magnitude: 369.06 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 193, pointers: 123, structural_boundaries: 84, state_mutation: 64
- `contrib/libarchive/libarchive/test/test_read_pax_xattr_rht_security_selinux.c` (C) | Magnitude: 0.06 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 22, pointers: 11, immutability_locks: 4, structural_boundaries: 3
- `contrib/llvm-project/llvm/lib/Transforms/Scalar/StructurizeCFG.cpp` (CPP) | Magnitude: 6.48 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 677, pointers: 356, args: 249, branch: 172

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `contrib/tzcode/difftime.c` (C) | Magnitude: 0.26 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 8, branch: 6, structural_boundaries: 6, time_date_logic: 5
- `contrib/arm-optimized-routines/math/aarch64/sve/sv_log1pf_inline.h` (C) | Magnitude: 0.12 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 31, core_var_decl: 18, design_snake_case: 18, pointers: 12
- `contrib/libarchive/libarchive/test/test_read_format_zip.c` (C) | Magnitude: 3.13 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 802, pointers: 194, structural_boundaries: 103, class_start: 60
- `lib/libcasper/services/cap_net/cap_net.h` (C) | Magnitude: 34.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: pointers: 64, args: 31, structural_boundaries: 28, macros: 22
- `sys/compat/linuxkpi/common/include/linux/crc32.h` (C) | Magnitude: 3.48 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 2, macros: 2, pointers: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `contrib/llvm-project/llvm/include/llvm/IR/AssemblyAnnotationWriter.h` (CPP) | Magnitude: 0.16 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 12, doc: 11, class_start: 6
- `contrib/libarchive/libarchive/test/test_read_format_zip_with_invalid_traditional_eocd.c` (C) | Magnitude: 0.05 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 20, pointers: 9, structural_boundaries: 2, class_start: 2
- `contrib/libarchive/libarchive/test/test_read_format_7zip_encryption_partially.c` (C) | Magnitude: 0.07 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 35, pointers: 6, args: 3, structural_boundaries: 2
- `sys/dev/pccbb/pccbbvar.h` (C) | Magnitude: 35.88 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 40, pointers: 37, indent_tabs: 34, macros: 26
- `contrib/llvm-project/libcxx/include/__math/fma.h` (CPP) | Magnitude: 0.16 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 17, indent_spaces: 11, import: 5, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `contrib/openpam/lib/libpam/pam_open_session.c` (C) | Magnitude: 0.08 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 7, import: 4, args: 2, branch: 1
- `crypto/krb5/src/util/profile/argv_parse.h` (C) | Magnitude: 0.13 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: args: 2, api: 2, pointers: 2, structural_boundaries: 1
- `sys/crypto/openssl/aarch64/ghashv8-armx.S` (ASSEMBLY) | Magnitude: 0.56 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: args: 694, indent_tabs: 490, pointers: 100, structural_boundaries: 18
- `contrib/llvm-project/clang/include/clang/Frontend/SerializedDiagnostics.h` (CPP) | Magnitude: 0.18 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 17, doc: 9, structural_boundaries: 6, core_var_decl: 6
- `contrib/netbsd-tests/lib/libc/sys/t_wait_noproc.c` (C) | Magnitude: 1.4 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 107, func_start: 25, args: 19, state_mutation: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_3
- `crypto/heimdal/lib/roken/getarg.c` (C) | Magnitude: 7.38 | Delta: **0.151** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 161, indent_tabs: 154, branch: 138, pointers: 127
- `contrib/tcsh/ed.inputl.c` (C) | Magnitude: 9.46 | Delta: **0.196** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 256, branch: 219, state_mutation: 215, core_var_decl: 171

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `contrib/libarchive/libarchive/archive_string.c` (C) | Magnitude: 42.43 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 2365, pointers: 1186, state_mutation: 777, branch: 757
- `crypto/heimdal/appl/afsutil/afslog.c` (C) | Magnitude: 2.46 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 84, pointers: 57, branch: 56, indent_tabs: 56
- `lib/geom/mirror/geom_mirror.c` (C) | Magnitude: 347.52 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 318, state_mutation: 77, branch: 61, pointers: 61
- `contrib/llvm-project/clang/lib/StaticAnalyzer/Checkers/IteratorModeling.cpp` (CPP) | Magnitude: 4.89 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 512, pointers: 263, args: 193, structural_boundaries: 177
- `sys/contrib/openzfs/module/zfs/zfs_sa.c` (C) | Magnitude: 2.3 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 239, pointers: 181, branch: 48, state_mutation: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `contrib/googletest/googletest/include/gtest/gtest-printers.h` (CPP) | Magnitude: 4.02 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 406, structural_boundaries: 346, args: 137, immutability_locks: 118
- `contrib/llvm-project/compiler-rt/lib/fuzzer/FuzzerExtFunctionsDlsym.cpp` (CPP) | Magnitude: 0.11 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 7, args: 5, import: 5
- `contrib/llvm-project/llvm/include/llvm/CodeGen/MachineSSAUpdater.h` (CPP) | Magnitude: 0.17 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: doc: 44, structural_boundaries: 22, indent_spaces: 20, pointers: 13
- `contrib/llvm-project/compiler-rt/lib/asan/asan_allocator.h` (CPP) | Magnitude: 0.45 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 87, immutability_locks: 54, pointers: 44
- `contrib/llvm-project/clang/include/clang/StaticAnalyzer/Core/PathSensitive/ProgramStateTrait.h` (CPP) | Magnitude: 0.56 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 153, structural_boundaries: 120, doc: 61, args: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `sys/dev/cxgbe/common/t4vf_hw.c` (C) | Magnitude: 319.16 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 221, state_mutation: 98, pointers: 98, structural_boundaries: 42
- `sys/contrib/openzfs/contrib/pyzfs/libzfs_core/_nvlist.py` (PYTHON) | Magnitude: 2.99 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 165, state_mutation: 66, core_var_decl: 60, design_snake_case: 59
- `lib/libkvm/kvm_i386.c` (C) | Magnitude: 292.4 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 244, pointers: 101, state_mutation: 58, branch: 48
- `contrib/openbsm/bin/auditfilterd/auditfilterd.c` (C) | Magnitude: 1.95 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 164, branch: 48, pointers: 36, structural_boundaries: 29
- `stand/libsa/smbios.c` (C) | Magnitude: 490.66 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 328, branch: 117, state_mutation: 81, structural_boundaries: 75

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tools/test/stress2/testcases/rename/rename.c` (C) | Magnitude: 0.1 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 65, state_mutation: 21, branch: 19, import: 9
- `share/mk/bsd.clang-analyze.mk` (MAKEFILE) | Magnitude: 17.22 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 9, state_mutation: 7, structural_boundaries: 6, func_start: 5
- `contrib/ncurses/ncurses/base/lib_clreol.c` (C) | Magnitude: 0.37 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: pointers: 18, indent_tabs: 16, core_var_decl: 8, design_snake_case: 8
- `tools/test/stress2/misc/mmap26.sh` (SHELL) | Magnitude: 0.03 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 31, structural_boundaries: 15, branch: 11, io: 9
- `contrib/llvm-project/llvm/include/llvm/Support/PrettyStackTrace.h` (CPP) | Magnitude: 0.11 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 40, doc: 38, structural_boundaries: 21, immutability_locks: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `contrib/ntp/ntpd/ntp_proto.c` (C) | Magnitude: 38.82 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_3`
  * Top Architectural Signatures: indent_tabs: 2524, pointers: 1317, branch: 827, state_mutation: 794
- `contrib/tcpdump/print-isoclns.c` (C) | Magnitude: 26.35 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_3`
  * Top Architectural Signatures: indent_spaces: 1972, branch: 536, state_mutation: 461, structural_boundaries: 382
- `usr.sbin/pkg/pkg.c` (C) | Magnitude: 1005.74 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 809, pointers: 236, branch: 212, state_mutation: 178
- `sys/fs/msdosfs/msdosfs_vnops.c` (C) | Magnitude: 1519.48 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 1123, pointers: 714, branch: 323, state_mutation: 313
- `contrib/dialog/dlg_keys.c` (C) | Magnitude: 9.19 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 275, indent_tabs: 225, branch: 198, pointers: 188

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `sys/tools/syscalls/config.lua` (LUA) | Magnitude: 0.11 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 136, core_var_decl: 71, design_snake_case: 71, structural_boundaries: 52
- `lib/libc/gen/ttyname.c` (C) | Magnitude: 34.5 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 32, import: 16, branch: 13, structural_boundaries: 12
- `contrib/sendmail/test/t_seteuid.c` (C) | Magnitude: 0.61 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 77, debug_prints: 16, auth_middleware: 14, branch: 13
- `bin/realpath/realpath.c` (C) | Magnitude: 61.68 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 29, state_mutation: 12, branch: 11, structural_boundaries: 7
- `contrib/netbsd-tests/kernel/kqueue/t_proc1.c` (C) | Magnitude: 0.71 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 59, state_mutation: 14, structural_boundaries: 13, branch: 12

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `sys/dev/acpica/acpi.c` -> Churn: **100.0%** | Cog Load: 72.4908% | Debt: 43.6404%
- `sys/x86/cpufreq/hwpstate_amd.c` -> Churn: **97.45%** | Cog Load: 72.3377% | Debt: 8.8737%
- `sys/compat/linuxkpi/common/src/linux_80211.c` -> Churn: **92.37%** | Cog Load: 71.8409% | Debt: 53.5932%
- `sys/dev/asmc/asmc.c` -> Churn: **87.7%** | Cog Load: 60.0957% | Debt: 0.0%
- `sys/dev/cxgbe/t4_main.c` -> Churn: **79.8%** | Cog Load: 79.3474% | Debt: 10.022%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `sys/fs/nfsclient/nfs_clrpcops.c` -> **Rick Macklem** (100.0% isolated ownership) | Magnitude: 15822.3
- `sys/netinet/sctp_output.c` -> **Gleb Smirnoff** (100.0% isolated ownership) | Magnitude: 14401.46
- `sys/amd64/amd64/pmap.c` -> **Konstantin Belousov** (100.0% isolated ownership) | Magnitude: 10144.42
- `sys/fs/nfsserver/nfs_nfsdport.c` -> **Rick Macklem** (100.0% isolated ownership) | Magnitude: 9646.92
- `sys/fs/nfs/nfs_commonsubs.c` -> **Rick Macklem** (100.0% isolated ownership) | Magnitude: 9629.58

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `contrib/llvm-project/llvm/lib/CodeGen/AsmPrinter/DwarfDebug.cpp` -> **Severity: 845.625** (Blast Radius: 9.84 * Doc Risk: 85.9375%)
- `tools/test/stress2/misc/rename12.sh` -> **Severity: 638.5** (Blast Radius: 6.385 * Doc Risk: 100.0%)
- `contrib/bearssl/src/inner.h` -> **Severity: 199.0** (Blast Radius: 1.99 * Doc Risk: 100.0%)
- `sys/sys/endian.h` -> **Severity: 195.7** (Blast Radius: 1.957 * Doc Risk: 100.0%)
- `contrib/llvm-project/llvm/include/llvm/ADT/iterator_range.h` -> **Severity: 182.4** (Blast Radius: 2.28 * Doc Risk: 80.0%)

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 100306 literal sites + 5115 sites through wrappers = 105421
- **`memory_alloc`:** 58116 literal sites + 80073 sites through wrappers = 138189
- **`panics_and_aborts`:** 53572 literal sites + 1854 sites through wrappers = 55426

- `free` (macro, memory_alloc, primitive): 29878 call sites in 5673 files -- `contrib/llvm-project/openmp/runtime/src/kmp_wrapper_malloc.h`
- `malloc` (macro, memory_alloc, primitive): 10793 call sites in 4194 files -- `contrib/llvm-project/openmp/runtime/src/kmp_wrapper_malloc.h`
- `ATF_TP_ADD_TC` (macro, memory_alloc, via atf_utils_free_charpp): 4302 call sites in 725 files -- `contrib/atf/atf-c/macros.h`
- `kfree` (macro, memory_alloc, primitive): 2258 call sites in 362 files -- `contrib/libucl/klib/khash.h`
- `ATF_ADD_TEST_CASE` (macro, memory_alloc, primitive): 1719 call sites in 148 files -- `contrib/atf/atf-c++/macros.hpp`
- `gettext` (function, debug_prints, primitive): 1227 call sites in 24 files -- `contrib/libcbor/doc/Makefile`
- `realloc` (macro, memory_alloc, via unbound_stat_realloc_log): 1150 call sites in 700 files -- `contrib/llvm-project/openmp/runtime/src/kmp_wrapper_malloc.h`
- `kzalloc` (macro, memory_alloc, via kmalloc): 732 call sites in 256 files -- `sys/compat/linuxkpi/common/include/linux/slab.h`
- `BN_new` (macro, memory_alloc, primitive): 625 call sites in 105 files -- `usr.bin/factor/factor.c`
- `archive_entry_free` (function, memory_alloc, primitive): 607 call sites in 141 files -- `contrib/libarchive/libarchive/archive_entry.c`
- `mm_free` (macro, memory_alloc, primitive): 518 call sites in 60 files -- `contrib/libevent/mm-internal.h`
- `archive_entry_new` (function, memory_alloc, via archive_entry_new2): 466 call sites in 123 files -- `contrib/libarchive/libarchive/archive_entry.c`
*(+5091 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2629220 call pairs -- scoped 23.7%, unique 18.6%, ambiguous 31.3%, external 26.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 1562323 | 18.4% | 27.6% | 24.9% | 29.1% |
| cpp | 923097 | 34.6% | 5.6% | 46.3% | 13.5% |
| shell | 93237 | 7.3% | 4.8% | 1.5% | 86.3% |
| m4 | 14588 | 15.1% | 2.8% | 1.2% | 80.9% |
| python | 13920 | 30.5% | 0.0% | 12.3% | 57.2% |
| perl | 10333 | 19.0% | 0.0% | 3.5% | 77.5% |
| yacc | 6702 | 0.3% | 27.2% | 43.4% | 29.1% |
| lua | 2242 | 26.4% | 3.8% | 1.8% | 67.9% |
| java | 757 | 16.6% | 0.1% | 2.8% | 80.4% |
| livecode | 689 | 0.0% | 0.9% | 0.0% | 99.1% |

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
