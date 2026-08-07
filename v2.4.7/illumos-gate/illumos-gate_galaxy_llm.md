# ARCHITECTURAL_BRIEF: illumos-gate
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/OS/illumos-gate` |
| **Timestamp** | `2026-08-07T03:34:06.940277+00:00` |
| **Scan Duration** | `140.47s` |
| **Git Branch** | `master` |
| **Git Commit** | `bb22c2af5c5ffa416f82a7b13a92d58240c65a83` |
| **Git Remote** | `https://github.com/illumos/illumos-gate.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 33307 malicious artifacts.

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
| Total Artifacts | 48723 |
| Analyzed Artifacts (Scanned) | 37186 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11537 |
| Total LOC | 6313943 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 76.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1243 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1446 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 23856 | 5645821 | 64.2% |
| MAKEFILE | 6003 | 148268 | 16.1% |
| SHELL | 2705 | 154890 | 7.3% |
| PLAINTEXT | 2158 | 2 | 5.8% |
| ASSEMBLY | 897 | 206914 | 2.4% |
| CPP | 265 | 32445 | 0.7% |
| XML | 245 | 0 | 0.7% |
| HTML | 229 | 2537 | 0.6% |
| MARKDOWN | 205 | 0 | 0.6% |
| JAVA | 193 | 25237 | 0.5% |
| M4 | 139 | 15649 | 0.4% |
| PERL | 106 | 26988 | 0.3% |
| YACC | 74 | 31241 | 0.2% |
| PYTHON | 54 | 6366 | 0.1% |
| JSON | 38 | 15647 | 0.1% |
| BINARY_THREAT | 8 | 8 | 0.0% |
| OBJECTIVE-C | 4 | 842 | 0.0% |
| TCL | 3 | 608 | 0.0% |
| PROTO | 1 | 70 | 0.0% |
| CSV | 1 | 108 | 0.0% |
| RUST | 1 | 22 | 0.0% |
| SCHEME | 1 | 280 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.313`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 17390 | 46.8% |
| file_cluster_13 | 15883 | 42.7% |
| file_cluster_9 | 909 | 2.4% |
| file_cluster_4 | 270 | 0.7% |
| file_cluster_12 | 129 | 0.3% |
| file_cluster_11 | 79 | 0.2% |
| file_cluster_0 | 54 | 0.1% |
| file_cluster_17 | 44 | 0.1% |
| file_cluster_7 | 27 | 0.1% |
| file_cluster_16 | 15 | 0.0% |
| Unknown | 10 | 0.0% |
| file_cluster_6 | 7 | 0.0% |
| file_cluster_2 | 2 | 0.0% |
| file_cluster_1 | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2361 | 6.3% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11537*

**Composition by Extension & Reason:**
- `no_extension`: 1540x Unsupported Format (.undeterminable), 282x Excluded (Binary Format Detected), 136x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.d`: 1201x Unsupported Format (.d), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.3c`: 569x Unsupported Format (.3c)
- `.9f`: 556x Unsupported Format (.9f)
- `.p5m`: 555x Unsupported Format (.p5m)
- `.conf`: 377x Unsupported Format (.conf)
- `.src`: 314x Unsupported Format (.src), 3x Excluded (Embedded Hex Payload: 644 hex tokens in 587 LOC), 2x Excluded (Monolithic Amalgamation: 82155 LOC exceeds safe regex boundaries)
- `.tbl`: 250x Unsupported Format (.tbl)
- `.awk`: 198x Unsupported Format (.awk), 37x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Binary Format Detected)
- `.ok`: 135x Excluded: Neighborhood Micro-Mass Limit Exceeded, 94x Unsupported Format (.ok), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.descrip`: 228x Unsupported Format (.descrip)
- `.4d`: 212x Unsupported Format (.4d), 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.info`: 200x Unsupported Format (.info), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.3proc`: 152x Unsupported Format (.3proc)
- `.cfg`: 139x Unsupported Format (.cfg)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 39.9 | 23.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 58.2 | 77.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.5 | 2.3 | 2.3 |
| API Exposure | 0.0 | 19.8 | 7.3 | 7.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 54.1 | 91.2 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 5.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 89.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 38.3 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 53.8 | 56.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `usr/src/contrib/ast/src/cmd/INIT/package.sh` (Hits: 1308)
- `usr/src/tools/scripts/webrev.sh` (Hits: 954)
- `usr/src/cmd/ldap/ns_ldap/idsconfig.sh` (Hits: 804)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **locale.h** (`usr/src/head/locale.h`) — 942 inbound connections
2. **lint.h** (`usr/src/lib/libc/inc/lint.h`) — 629 inbound connections
3. **pwd.h** (`usr/src/head/pwd.h`) — 399 inbound connections
4. **curses_inc.h** (`usr/src/lib/libcurses/screen/curses_inc.h`) — 398 inbound connections
5. **k5-int.h** (`usr/src/uts/common/gssapi/mechs/krb5/include/k5-int.h`) — 351 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **env.c** (`usr/src/boot/efi/libefi/env.c`) — 145 outbound dependencies
2. **startup.c** (`usr/src/uts/i86pc/os/startup.c`) — 96 outbound dependencies
3. **machdep.c** (`usr/src/uts/i86pc/os/machdep.c`) — 91 outbound dependencies
4. **ip.c** (`usr/src/uts/common/inet/ip/ip.c`) — 89 outbound dependencies
5. **ip_input.c** (`usr/src/uts/common/inet/ip/ip_input.c`) — 85 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Anonymous_Block_[Truncated]` (@ `usr/src/contrib/ast/src/cmd/INIT/package.sh`) -> Impact: **5155.3** | LOC: 7251
- `Anonymous_Block_[Truncated]` (@ `usr/src/cmd/ldap/ns_ldap/idsconfig.sh`) -> Impact: **2934.3** | LOC: 5342
- `Anonymous_Block_[Truncated]` (@ `usr/src/contrib/ast/src/cmd/INIT/iffe.sh`) -> Impact: **2773.5** | LOC: 4615
- `data_copy_with_holes` (@ `usr/src/cmd/cpio/cpio.c`) -> Impact: **2285.5** | LOC: 2321
- `rdwr_bytes` (@ `usr/src/cmd/cpio/cpio.c`) -> Impact: **2268.7** | LOC: 2325
  * *Intent:* /*
- `segvn_faultpage` (@ `usr/src/uts/common/vm/seg_vn.c`) -> Impact: **2205.0** | LOC: 2245
- `read_compress_holes` (@ `usr/src/cmd/cpio/cpio.c`) -> Impact: **2008.9** | LOC: 2308
- `segvn_full_szcpages` (@ `usr/src/uts/common/vm/seg_vn.c`) -> Impact: **1988.5** | LOC: 2209
- `Anonymous_Block_[Truncated]` (@ `usr/src/cmd/ypcmd/yp2lscripts/inityp2l.sh`) -> Impact: **1950.7** | LOC: 5779
- `read_holesdata` (@ `usr/src/cmd/cpio/cpio.c`) -> Impact: **1864.4** | LOC: 2316

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `usr/src/uts/common/os` | 177 | 109039.12 | 73.57% | 52.92% |
| `usr/src/uts/common/io` | 120 | 66583.16 | 70.2% | 39.38% |
| `usr/src/uts/common/fs/zfs` | 119 | 63381.68 | 73.01% | 47.35% |
| `usr/src/uts/common/fs/nfs` | 58 | 60108.8 | 76.45% | 47.74% |
| `usr/src/uts/common/io/fibre-channel/fca/emlxs` | 23 | 59232.7 | 81.01% | 21.05% |
| `usr/src/uts/common/inet/ip` | 60 | 55877.76 | 64.67% | 42.28% |
| `usr/src/lib/libdwarf/common` | 167 | 45679.74 | 32.44% | 27.96% |
| `usr/src/cmd/sendmail/src` | 50 | 42278.4 | 65.68% | 23.64% |
| `usr/src/uts/sun4v/io` | 45 | 42114.78 | 75.87% | 20.51% |
| `usr/src/uts/common/sys` | 677 | 41239.02 | 13.55% | 3.35% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `usr/src/boot/efi/loader/arch/arm64/Makefile.inc` -> **100.0%** Exposure
- `usr/src/cmd/mdb/intel/amd64/mdb_ks/Makefile` -> **100.0%** Exposure
- `usr/src/cmd/sgs/lddstub/Makefile.com` -> **100.0%** Exposure
- `usr/src/contrib/ast/src/cmd/INIT/MSGFUN.mk` -> **100.0%** Exposure
- `usr/src/contrib/ast/src/cmd/INIT/MSGKEY.mk` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `usr/src/Makefile.smatch` -> **100.0%** Exposure
- `usr/src/boot/efi/Makefile.inc` -> **100.0%** Exposure
- `usr/src/boot/forth/Makefile` -> **100.0%** Exposure
- `usr/src/boot/libsa/Makefile.inc` -> **100.0%** Exposure
- `usr/src/boot/libsa/amd64/Makefile` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `usr/src/uts/sun4v/cpu/niagara_copy.S` -> **436** Orphaned Functions | **12** Duplicates
- `usr/src/uts/sun4u/cpu/spitfire_copy.S` -> **165** Orphaned Functions | **0** Duplicates
- `usr/src/uts/sun4u/cpu/opl_olympus_copy.S` -> **155** Orphaned Functions | **4** Duplicates
- `usr/src/uts/sun4u/cpu/cheetah_copy.S` -> **154** Orphaned Functions | **4** Duplicates
- `usr/src/lib/libmvec/common/vis/__vatan2f.S` -> **155** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`usr/src/boot/common/ls.c`** -> AI Confidence: **99.48%**
2. **`usr/src/boot/i386/libi386/bootinfo.c`** -> AI Confidence: **99.48%**
3. **`usr/src/cmd/abi/spectrans/parser/extends.c`** -> AI Confidence: **99.48%**
4. **`usr/src/cmd/acct/acctcom.c`** -> AI Confidence: **99.48%**
5. **`usr/src/cmd/acct/fwtmp.c`** -> AI Confidence: **99.48%**
6. **`usr/src/cmd/acct/utmp2wtmp.c`** -> AI Confidence: **99.48%**
7. **`usr/src/cmd/acpi/iasl/cvparser.c`** -> AI Confidence: **99.48%**
8. **`usr/src/cmd/allocate/allocate.c`** -> AI Confidence: **99.48%**
9. **`usr/src/cmd/amdzen/udf.c`** -> AI Confidence: **99.48%**
10. **`usr/src/cmd/ast/libast/amd64/conftab.c`** -> AI Confidence: **99.48%**
11. **`usr/src/cmd/ast/libast/i386/conftab.c`** -> AI Confidence: **99.48%**
12. **`usr/src/cmd/ast/libast/sparc/conftab.c`** -> AI Confidence: **99.48%**
13. **`usr/src/cmd/ast/libast/sparcv9/conftab.c`** -> AI Confidence: **99.48%**
14. **`usr/src/cmd/audio/audiorecord/audiorecord.c`** -> AI Confidence: **99.48%**
15. **`usr/src/cmd/awk/main.c`** -> AI Confidence: **99.48%**
16. **`usr/src/cmd/backup/dump/dumpusg.h`** -> AI Confidence: **99.48%**
17. **`usr/src/cmd/bhyve/amd64/vga.c`** -> AI Confidence: **99.48%**
18. **`usr/src/cmd/bhyve/amd64/xmsr.c`** -> AI Confidence: **99.48%**
19. **`usr/src/cmd/bhyve/common/pci_e82545.c`** -> AI Confidence: **99.48%**
20. **`usr/src/cmd/bhyve/common/pci_irq.c`** -> AI Confidence: **99.48%**
21. **`usr/src/cmd/bhyvectl/bhyvectl.c`** -> AI Confidence: **99.48%**
22. **`usr/src/cmd/bnu/stoa.c`** -> AI Confidence: **99.48%**
23. **`usr/src/cmd/boot/bootadm/bootadm_digest.c`** -> AI Confidence: **99.48%**
24. **`usr/src/cmd/cdrw/main.c`** -> AI Confidence: **99.48%**
25. **`usr/src/cmd/chmod/common.c`** -> AI Confidence: **99.48%**
26. **`usr/src/cmd/cmd-crypto/kmfcfg/create.c`** -> AI Confidence: **99.48%**
27. **`usr/src/cmd/cmd-crypto/kmfcfg/delete.c`** -> AI Confidence: **99.48%**
28. **`usr/src/cmd/cmd-crypto/kmfcfg/export.c`** -> AI Confidence: **99.48%**
29. **`usr/src/cmd/cmd-crypto/kmfcfg/import.c`** -> AI Confidence: **99.48%**
30. **`usr/src/cmd/cmd-crypto/kmfcfg/modify.c`** -> AI Confidence: **99.48%**
31. **`usr/src/cmd/cmd-crypto/pktool/download.c`** -> AI Confidence: **99.48%**
32. **`usr/src/cmd/cmd-inet/lib/nwamd/enm.c`** -> AI Confidence: **99.48%**
33. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/states.c`** -> AI Confidence: **99.48%**
34. **`usr/src/cmd/cmd-inet/usr.bin/chat/chat.c`** -> AI Confidence: **99.48%**
35. **`usr/src/cmd/cmd-inet/usr.bin/pppdump/pppdump.c`** -> AI Confidence: **99.48%**
36. **`usr/src/cmd/cmd-inet/usr.bin/whois.c`** -> AI Confidence: **99.48%**
37. **`usr/src/cmd/cmd-inet/usr.sbin/ifconfig/defs.h`** -> AI Confidence: **99.48%**
38. **`usr/src/cmd/cmd-inet/usr.sbin/ilbadm/ilbadm_stats.c`** -> AI Confidence: **99.48%**
39. **`usr/src/cmd/cmd-inet/usr.sbin/ilbadm/ilbadm_subr.c`** -> AI Confidence: **99.48%**
40. **`usr/src/cmd/cmd-inet/usr.sbin/inetadm/inetadm.c`** -> AI Confidence: **99.48%**
41. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_isis.c`** -> AI Confidence: **99.48%**
42. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_ldap.c`** -> AI Confidence: **99.48%**
43. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_pf.c`** -> AI Confidence: **99.48%**
44. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_rpcprint.c`** -> AI Confidence: **99.48%**
45. **`usr/src/cmd/cpio/cpio.c`** -> AI Confidence: **99.48%**
46. **`usr/src/cmd/cron/crontab.c`** -> AI Confidence: **99.48%**
47. **`usr/src/cmd/cron/parse.c`** -> AI Confidence: **99.48%**
48. **`usr/src/cmd/ctfmerge/ctfmerge.c`** -> AI Confidence: **99.48%**
49. **`usr/src/cmd/dd/dd.c`** -> AI Confidence: **99.48%**
50. **`usr/src/cmd/deroff/deroff.c`** -> AI Confidence: **99.48%**
51. **`usr/src/cmd/devfsadm/sgen_link.c`** -> AI Confidence: **99.48%**
52. **`usr/src/cmd/devmgmt/cmds/getdgrp.c`** -> AI Confidence: **99.48%**
53. **`usr/src/cmd/devmgmt/cmds/getvol.c`** -> AI Confidence: **99.48%**
54. **`usr/src/cmd/devmgmt/cmds/listdgrp.c`** -> AI Confidence: **99.48%**
55. **`usr/src/cmd/dfs.cmds/dfshares/dfshares.c`** -> AI Confidence: **99.48%**
56. **`usr/src/cmd/dispadmin/fssdispadmin.c`** -> AI Confidence: **99.48%**
57. **`usr/src/cmd/dispadmin/fxdispadmin.c`** -> AI Confidence: **99.48%**
58. **`usr/src/cmd/dispadmin/iadispadmin.c`** -> AI Confidence: **99.48%**
59. **`usr/src/cmd/dispadmin/rtdispadmin.c`** -> AI Confidence: **99.48%**
60. **`usr/src/cmd/dispadmin/sdcdispadmin.c`** -> AI Confidence: **99.48%**
61. **`usr/src/cmd/dispadmin/tsdispadmin.c`** -> AI Confidence: **99.48%**
62. **`usr/src/cmd/fcinfo/fcadm-list.c`** -> AI Confidence: **99.48%**
63. **`usr/src/cmd/fcinfo/fcoeadm.c`** -> AI Confidence: **99.48%**
64. **`usr/src/cmd/file/magicutils.c`** -> AI Confidence: **99.48%**
65. **`usr/src/cmd/filesync/action.c`** -> AI Confidence: **99.48%**
66. **`usr/src/cmd/filesync/anal.c`** -> AI Confidence: **99.48%**
67. **`usr/src/cmd/filesync/base.c`** -> AI Confidence: **99.48%**
68. **`usr/src/cmd/filesync/files.c`** -> AI Confidence: **99.48%**
69. **`usr/src/cmd/fm/eversholt/eftinfo/common/eftinfo.c`** -> AI Confidence: **99.48%**
70. **`usr/src/cmd/fm/eversholt/esc/common/escmain.c`** -> AI Confidence: **99.48%**
71. **`usr/src/cmd/format/analyze.c`** -> AI Confidence: **99.48%**
72. **`usr/src/cmd/fs.d/ff.c`** -> AI Confidence: **99.48%**
73. **`usr/src/cmd/fs.d/fsck.c`** -> AI Confidence: **99.48%**
74. **`usr/src/cmd/fs.d/nfs/lib/replica.c`** -> AI Confidence: **99.48%**
75. **`usr/src/cmd/fs.d/nfs/lib/smfcfg.c`** -> AI Confidence: **99.48%**
76. **`usr/src/cmd/fs.d/nfs/mount/mount.c`** -> AI Confidence: **99.48%**
77. **`usr/src/cmd/fs.d/smbclnt/chacl/chacl.c`** -> AI Confidence: **99.48%**
78. **`usr/src/cmd/fs.d/smbclnt/mount/mount.c`** -> AI Confidence: **99.48%**
79. **`usr/src/cmd/fs.d/smbclnt/smbutil/discon.c`** -> AI Confidence: **99.48%**
80. **`usr/src/cmd/fs.d/smbclnt/smbutil/info.c`** -> AI Confidence: **99.48%**
81. **`usr/src/cmd/fs.d/smbclnt/smbutil/print.c`** -> AI Confidence: **99.48%**
82. **`usr/src/cmd/fs.d/ufs/fsdb/fsdb.c`** -> AI Confidence: **99.48%**
83. **`usr/src/cmd/geniconvtbl/disassemble.c`** -> AI Confidence: **99.48%**
84. **`usr/src/cmd/gss/gsscred/gsscred.c`** -> AI Confidence: **99.48%**
85. **`usr/src/cmd/hal/addons/cpufreq/addon-cpufreq.c`** -> AI Confidence: **99.48%**
86. **`usr/src/cmd/hal/hald/device_info.c`** -> AI Confidence: **99.48%**
87. **`usr/src/cmd/hal/hald/solaris/devinfo_cpu.c`** -> AI Confidence: **99.48%**
88. **`usr/src/cmd/hal/hald/solaris/devinfo_pci.c`** -> AI Confidence: **99.48%**
89. **`usr/src/cmd/hal/hald/solaris/devinfo_usb.c`** -> AI Confidence: **99.48%**
90. **`usr/src/cmd/hal/probing/acpi/probe-acpi.c`** -> AI Confidence: **99.48%**
91. **`usr/src/cmd/hal/probing/network-printer/probe-network-printer.c`** -> AI Confidence: **99.48%**
92. **`usr/src/cmd/hal/probing/printer/probe-printer.c`** -> AI Confidence: **99.48%**
93. **`usr/src/cmd/hal/probing/volume/probe-volume.c`** -> AI Confidence: **99.48%**
94. **`usr/src/cmd/hal/tools/hal-storage-eject.c`** -> AI Confidence: **99.48%**
95. **`usr/src/cmd/hal/tools/hal-storage-mount.c`** -> AI Confidence: **99.48%**
96. **`usr/src/cmd/hal/tools/hal-storage-unmount.c`** -> AI Confidence: **99.48%**
97. **`usr/src/cmd/hal/utils/printer.c`** -> AI Confidence: **99.48%**
98. **`usr/src/cmd/i2cadm/i2cadm_io.c`** -> AI Confidence: **99.48%**
99. **`usr/src/cmd/idmap/idmapd/dbutils.c`** -> AI Confidence: **99.48%**
100. **`usr/src/cmd/idmap/idmapd/server.c`** -> AI Confidence: **99.48%**
101. **`usr/src/cmd/ipf/tools/ipfs.c`** -> AI Confidence: **99.48%**
102. **`usr/src/cmd/ipf/tools/ipnat.c`** -> AI Confidence: **99.48%**
103. **`usr/src/cmd/ipf/tools/ippool.c`** -> AI Confidence: **99.48%**
104. **`usr/src/cmd/ipf/tools/lexer.c`** -> AI Confidence: **99.48%**
105. **`usr/src/cmd/isns/isnsd/config.c`** -> AI Confidence: **99.48%**
106. **`usr/src/cmd/isns/isnsd/door.c`** -> AI Confidence: **99.48%**
107. **`usr/src/cmd/isns/isnsd/dseng.c`** -> AI Confidence: **99.48%**
108. **`usr/src/cmd/isns/isnsd/dump.c`** -> AI Confidence: **99.48%**
109. **`usr/src/cmd/isns/isnsd/func.c`** -> AI Confidence: **99.48%**
110. **`usr/src/cmd/isns/isnsd/htable.c`** -> AI Confidence: **99.48%**
111. **`usr/src/cmd/isns/isnsd/xml/data.c`** -> AI Confidence: **99.48%**
112. **`usr/src/cmd/keyserv/chkey.c`** -> AI Confidence: **99.48%**
113. **`usr/src/cmd/krb5/kadmin/cli/kadmin.c`** -> AI Confidence: **99.48%**
114. **`usr/src/cmd/krb5/kadmin/dbutil/dump.c`** -> AI Confidence: **99.48%**
115. **`usr/src/cmd/krb5/kadmin/dbutil/ovload.c`** -> AI Confidence: **99.48%**
116. **`usr/src/cmd/krb5/kadmin/kdcmgr/klookup.c`** -> AI Confidence: **99.48%**
117. **`usr/src/cmd/krb5/kadmin/ktutil/ktutil_funcs.c`** -> AI Confidence: **99.48%**
118. **`usr/src/cmd/krb5/kadmin/server/kadm_rpc_svc.c`** -> AI Confidence: **99.48%**
119. **`usr/src/cmd/krb5/kdestroy/kdestroy.c`** -> AI Confidence: **99.48%**
120. **`usr/src/cmd/krb5/kinit/kinit.c`** -> AI Confidence: **99.48%**
121. **`usr/src/cmd/krb5/klist/klist.c`** -> AI Confidence: **99.48%**
122. **`usr/src/cmd/krb5/krb5kdc/dispatch.c`** -> AI Confidence: **99.48%**
123. **`usr/src/cmd/krb5/krb5kdc/do_as_req.c`** -> AI Confidence: **99.48%**
124. **`usr/src/cmd/krb5/krb5kdc/do_tgs_req.c`** -> AI Confidence: **99.48%**
125. **`usr/src/cmd/krb5/krb5kdc/kdc_util.c`** -> AI Confidence: **99.48%**
126. **`usr/src/cmd/krb5/krb5kdc/main.c`** -> AI Confidence: **99.48%**
127. **`usr/src/cmd/krb5/ldap_util/kdb5_ldap_policy.c`** -> AI Confidence: **99.48%**
128. **`usr/src/cmd/krb5/ldap_util/kdb5_ldap_realm.c`** -> AI Confidence: **99.48%**
129. **`usr/src/cmd/krb5/ldap_util/kdb5_ldap_util.c`** -> AI Confidence: **99.48%**
130. **`usr/src/cmd/krb5/slave/kpropd.c`** -> AI Confidence: **99.48%**
131. **`usr/src/cmd/ldap/common/etest.c`** -> AI Confidence: **99.48%**
132. **`usr/src/cmd/ldap/common/ldapmodrdn.c`** -> AI Confidence: **99.48%**
133. **`usr/src/cmd/ldap/common/ldaptest.c`** -> AI Confidence: **99.48%**
134. **`usr/src/cmd/ldap/common/tmpltest.c`** -> AI Confidence: **99.48%**
135. **`usr/src/cmd/ldmad/ldma_device.c`** -> AI Confidence: **99.48%**
136. **`usr/src/cmd/listen/lsdbf.c`** -> AI Confidence: **99.48%**
137. **`usr/src/cmd/localedef/ctype.c`** -> AI Confidence: **99.48%**
138. **`usr/src/cmd/localedef/monetary.c`** -> AI Confidence: **99.48%**
139. **`usr/src/cmd/localedef/time.c`** -> AI Confidence: **99.48%**
140. **`usr/src/cmd/logadm/kw.c`** -> AI Confidence: **99.48%**
141. **`usr/src/cmd/lp/cmd/lpadmin/chkopts.c`** -> AI Confidence: **99.48%**
142. **`usr/src/cmd/lp/cmd/lpadmin/do_align.c`** -> AI Confidence: **99.48%**
143. **`usr/src/cmd/lp/cmd/lpadmin/do_mount.c`** -> AI Confidence: **99.48%**
144. **`usr/src/cmd/lp/cmd/lpadmin/do_printer.c`** -> AI Confidence: **99.48%**
145. **`usr/src/cmd/lp/cmd/lpadmin/do_pwheel.c`** -> AI Confidence: **99.48%**
146. **`usr/src/cmd/lp/cmd/lpadmin/lpadmin.c`** -> AI Confidence: **99.48%**
147. **`usr/src/cmd/lp/cmd/lpadmin/options.c`** -> AI Confidence: **99.48%**
148. **`usr/src/cmd/lp/cmd/lpadmin/output.c`** -> AI Confidence: **99.48%**
149. **`usr/src/cmd/lp/cmd/lpadmin/rmdest.c`** -> AI Confidence: **99.48%**
150. **`usr/src/cmd/lp/cmd/lpforms.c`** -> AI Confidence: **99.48%**
151. **`usr/src/cmd/lp/cmd/lpsched/validate.c`** -> AI Confidence: **99.48%**
152. **`usr/src/cmd/lp/cmd/lpusers.c`** -> AI Confidence: **99.48%**
153. **`usr/src/cmd/lp/filter/postscript/postcomm/postcomm.c`** -> AI Confidence: **99.48%**
154. **`usr/src/cmd/lp/filter/postscript/postio/ifdef.c`** -> AI Confidence: **99.48%**
155. **`usr/src/cmd/lp/lib/lp/tidbit.c`** -> AI Confidence: **99.48%**
156. **`usr/src/cmd/lp/lib/papi/lpsched-jobs.c`** -> AI Confidence: **99.48%**
157. **`usr/src/cmd/lp/lib/requests/getrequest.c`** -> AI Confidence: **99.48%**
158. **`usr/src/cmd/luxadm/adm.c`** -> AI Confidence: **99.48%**
159. **`usr/src/cmd/mandoc/eqn_html.c`** -> AI Confidence: **99.48%**
160. **`usr/src/cmd/mandoc/eqn_term.c`** -> AI Confidence: **99.48%**
161. **`usr/src/cmd/mandoc/main.c`** -> AI Confidence: **99.48%**
162. **`usr/src/cmd/mandoc/mandoc.c`** -> AI Confidence: **99.48%**
163. **`usr/src/cmd/mandoc/preconv.c`** -> AI Confidence: **99.48%**
164. **`usr/src/cmd/mandoc/tbl_opts.c`** -> AI Confidence: **99.48%**
165. **`usr/src/cmd/mandoc/term.c`** -> AI Confidence: **99.48%**
166. **`usr/src/cmd/mandoc/tree.c`** -> AI Confidence: **99.48%**
167. **`usr/src/cmd/mdb/common/kmdb/kmdb_fault.c`** -> AI Confidence: **99.48%**
168. **`usr/src/cmd/mdb/common/mdb/mdb_fmt.c`** -> AI Confidence: **99.48%**
169. **`usr/src/cmd/mdb/common/mdb/mdb_stack.c`** -> AI Confidence: **99.48%**
170. **`usr/src/cmd/mdb/common/mdb/mdb_string.c`** -> AI Confidence: **99.48%**
171. **`usr/src/cmd/mdb/common/modules/usba/prtusb.c`** -> AI Confidence: **99.48%**
172. **`usr/src/cmd/mdb/intel/mdb/proc_x86util.c`** -> AI Confidence: **99.48%**
173. **`usr/src/cmd/mkdir/mkdir.c`** -> AI Confidence: **99.48%**
174. **`usr/src/cmd/more/more.c`** -> AI Confidence: **99.48%**
175. **`usr/src/cmd/nlsadmin/nlsadmin.c`** -> AI Confidence: **99.48%**
176. **`usr/src/cmd/nvmeadm/nvmeadm_print.c`** -> AI Confidence: **99.48%**
177. **`usr/src/cmd/nvmeadm/nvmeadm_vuc.c`** -> AI Confidence: **99.48%**
178. **`usr/src/cmd/oamuser/group/groupadd.c`** -> AI Confidence: **99.48%**
179. **`usr/src/cmd/oamuser/group/groupmod.c`** -> AI Confidence: **99.48%**
180. **`usr/src/cmd/oamuser/user/useradd.c`** -> AI Confidence: **99.48%**
181. **`usr/src/cmd/oamuser/user/userdel.c`** -> AI Confidence: **99.48%**
182. **`usr/src/cmd/oamuser/user/usermod.c`** -> AI Confidence: **99.48%**
183. **`usr/src/cmd/oamuser/user/val_lgrp.c`** -> AI Confidence: **99.48%**
184. **`usr/src/cmd/oamuser/user/val_lprj.c`** -> AI Confidence: **99.48%**
185. **`usr/src/cmd/passmgmt/passmgmt.c`** -> AI Confidence: **99.48%**
186. **`usr/src/cmd/pbind/pbind.c`** -> AI Confidence: **99.48%**
187. **`usr/src/cmd/pcidr/plugins/default/pcidr_plugin.c`** -> AI Confidence: **99.48%**
188. **`usr/src/cmd/pools/pooladm/pooladm.c`** -> AI Confidence: **99.48%**
189. **`usr/src/cmd/powertop/common/powertop.c`** -> AI Confidence: **99.48%**
190. **`usr/src/cmd/print/bsd-sysv-commands/accept.c`** -> AI Confidence: **99.48%**
191. **`usr/src/cmd/print/bsd-sysv-commands/cancel.c`** -> AI Confidence: **99.48%**
192. **`usr/src/cmd/print/bsd-sysv-commands/disable.c`** -> AI Confidence: **99.48%**
193. **`usr/src/cmd/print/bsd-sysv-commands/enable.c`** -> AI Confidence: **99.48%**
194. **`usr/src/cmd/print/bsd-sysv-commands/in.lpd.c`** -> AI Confidence: **99.48%**
195. **`usr/src/cmd/print/bsd-sysv-commands/lp.c`** -> AI Confidence: **99.48%**
196. **`usr/src/cmd/print/bsd-sysv-commands/lpmove.c`** -> AI Confidence: **99.48%**
197. **`usr/src/cmd/print/bsd-sysv-commands/lpq.c`** -> AI Confidence: **99.48%**
198. **`usr/src/cmd/print/bsd-sysv-commands/lpr.c`** -> AI Confidence: **99.48%**
199. **`usr/src/cmd/print/bsd-sysv-commands/reject.c`** -> AI Confidence: **99.48%**
200. **`usr/src/cmd/priocntl/fxpriocntl.c`** -> AI Confidence: **99.48%**
201. **`usr/src/cmd/priocntl/priocntl.c`** -> AI Confidence: **99.48%**
202. **`usr/src/cmd/prstat/prstat.c`** -> AI Confidence: **99.48%**
203. **`usr/src/cmd/ptools/pcred/pcred.c`** -> AI Confidence: **99.48%**
204. **`usr/src/cmd/rcap/common/rcapd_conf.c`** -> AI Confidence: **99.48%**
205. **`usr/src/cmd/regcmp/regcmp.c`** -> AI Confidence: **99.48%**
206. **`usr/src/cmd/rmdir/rmdir.c`** -> AI Confidence: **99.48%**
207. **`usr/src/cmd/rpcbind/rpcb_check.c`** -> AI Confidence: **99.48%**
208. **`usr/src/cmd/scadm/sparc/mpxu/common/configlog.c`** -> AI Confidence: **99.48%**
209. **`usr/src/cmd/scadm/sparc/mpxu/common/consolelog.c`** -> AI Confidence: **99.48%**
210. **`usr/src/cmd/sed/compile.c`** -> AI Confidence: **99.48%**
211. **`usr/src/cmd/sendmail/db/btree/bt_cursor.c`** -> AI Confidence: **99.48%**
212. **`usr/src/cmd/sendmail/db/btree/bt_put.c`** -> AI Confidence: **99.48%**
213. **`usr/src/cmd/sendmail/db/btree/bt_rec.c`** -> AI Confidence: **99.48%**
214. **`usr/src/cmd/sendmail/db/btree/bt_recno.c`** -> AI Confidence: **99.48%**
215. **`usr/src/cmd/sendmail/db/db/db.c`** -> AI Confidence: **99.48%**
216. **`usr/src/cmd/sendmail/db/db/db_appinit.c`** -> AI Confidence: **99.48%**
217. **`usr/src/cmd/sendmail/db/db/db_apprec.c`** -> AI Confidence: **99.48%**
218. **`usr/src/cmd/sendmail/db/db/db_conv.c`** -> AI Confidence: **99.48%**
219. **`usr/src/cmd/sendmail/db/db/db_rec.c`** -> AI Confidence: **99.48%**
220. **`usr/src/cmd/sendmail/db/db/db_region.c`** -> AI Confidence: **99.48%**
221. **`usr/src/cmd/sendmail/db/hash/hash.c`** -> AI Confidence: **99.48%**
222. **`usr/src/cmd/sendmail/db/hash/hash_rec.c`** -> AI Confidence: **99.48%**
223. **`usr/src/cmd/sendmail/db/lock/lock_deadlock.c`** -> AI Confidence: **99.48%**
224. **`usr/src/cmd/sendmail/db/mp/mp_bh.c`** -> AI Confidence: **99.48%**
225. **`usr/src/cmd/sendmail/include/sm/conf.h`** -> AI Confidence: **99.48%**
226. **`usr/src/cmd/sendmail/libsm/fseek.c`** -> AI Confidence: **99.48%**
227. **`usr/src/cmd/sendmail/libsm/fvwrite.c`** -> AI Confidence: **99.48%**
228. **`usr/src/cmd/sendmail/libsm/setvbuf.c`** -> AI Confidence: **99.48%**
229. **`usr/src/cmd/sendmail/libsm/strto.c`** -> AI Confidence: **99.48%**
230. **`usr/src/cmd/sendmail/libsm/t-memstat.c`** -> AI Confidence: **99.48%**
231. **`usr/src/cmd/sendmail/libsm/vfscanf.c`** -> AI Confidence: **99.48%**
232. **`usr/src/cmd/sendmail/src/conf.h`** -> AI Confidence: **99.48%**
233. **`usr/src/cmd/sendmail/util/mail.local.c`** -> AI Confidence: **99.48%**
234. **`usr/src/cmd/sendmail/util/praliases.c`** -> AI Confidence: **99.48%**
235. **`usr/src/cmd/sgs/elfedit/common/elfedit_machelf.c`** -> AI Confidence: **99.48%**
236. **`usr/src/cmd/sgs/libconv/common/sections.c`** -> AI Confidence: **99.48%**
237. **`usr/src/cmd/sgs/libld/common/args.c`** -> AI Confidence: **99.48%**
238. **`usr/src/cmd/sgs/libld/common/map_core.c`** -> AI Confidence: **99.48%**
239. **`usr/src/cmd/sgs/libld/common/outfile.c`** -> AI Confidence: **99.48%**
240. **`usr/src/cmd/sgs/librtld/common/relocate.c`** -> AI Confidence: **99.48%**
241. **`usr/src/cmd/sgs/rtld/amd64/_setup.c`** -> AI Confidence: **99.48%**
242. **`usr/src/cmd/sgs/rtld/amd64/amd64_elf.c`** -> AI Confidence: **99.48%**
243. **`usr/src/cmd/sgs/rtld/common/config_elf.c`** -> AI Confidence: **99.48%**
244. **`usr/src/cmd/sgs/rtld/common/elf.c`** -> AI Confidence: **99.48%**
245. **`usr/src/cmd/sgs/rtld/common/globals.c`** -> AI Confidence: **99.48%**
246. **`usr/src/cmd/sgs/rtld/common/move.c`** -> AI Confidence: **99.48%**
247. **`usr/src/cmd/sgs/rtld/common/remove.c`** -> AI Confidence: **99.48%**
248. **`usr/src/cmd/sgs/rtld/common/util.c`** -> AI Confidence: **99.48%**
249. **`usr/src/cmd/sgs/rtld/i386/_setup.c`** -> AI Confidence: **99.48%**
250. **`usr/src/cmd/sgs/rtld/i386/i386_elf.c`** -> AI Confidence: **99.48%**
251. **`usr/src/cmd/sgs/rtld/sparc/_setup.c`** -> AI Confidence: **99.48%**
252. **`usr/src/cmd/sgs/rtld/sparcv9/_setup.c`** -> AI Confidence: **99.48%**
253. **`usr/src/cmd/sgs/rtld/sparcv9/sparc_elf.c`** -> AI Confidence: **99.48%**
254. **`usr/src/cmd/spd/spd.c`** -> AI Confidence: **99.48%**
255. **`usr/src/cmd/sqlite/shell.c`** -> AI Confidence: **99.48%**
256. **`usr/src/cmd/sunpc/other/dos2unix.c`** -> AI Confidence: **99.48%**
257. **`usr/src/cmd/sunpc/other/unix2dos.c`** -> AI Confidence: **99.48%**
258. **`usr/src/cmd/svc/lsvcrun/lsvcrun.c`** -> AI Confidence: **99.48%**
259. **`usr/src/cmd/svc/startd/libscf.c`** -> AI Confidence: **99.48%**
260. **`usr/src/cmd/svc/startd/method.c`** -> AI Confidence: **99.48%**
261. **`usr/src/cmd/svc/svcadm/svcadm.c`** -> AI Confidence: **99.48%**
262. **`usr/src/cmd/svc/svcadm/synch.c`** -> AI Confidence: **99.48%**
263. **`usr/src/cmd/svc/svccfg/svccfg_libscf.c`** -> AI Confidence: **99.48%**
264. **`usr/src/cmd/svc/svcprop/svcprop.c`** -> AI Confidence: **99.48%**
265. **`usr/src/cmd/svr4pkg/libinst/open_package_datastream.c`** -> AI Confidence: **99.48%**
266. **`usr/src/cmd/svr4pkg/pkgchk/main.c`** -> AI Confidence: **99.48%**
267. **`usr/src/cmd/svr4pkg/pkginstall/instvol.c`** -> AI Confidence: **99.48%**
268. **`usr/src/cmd/svr4pkg/pkgremove/main.c`** -> AI Confidence: **99.48%**
269. **`usr/src/cmd/tail/read.c`** -> AI Confidence: **99.48%**
270. **`usr/src/cmd/tail/tail.c`** -> AI Confidence: **99.48%**
271. **`usr/src/cmd/tcpd/tcpdchk.c`** -> AI Confidence: **99.48%**
272. **`usr/src/cmd/touch/touch.c`** -> AI Confidence: **99.48%**
273. **`usr/src/cmd/troff/n1.c`** -> AI Confidence: **99.48%**
274. **`usr/src/cmd/troff/n7.c`** -> AI Confidence: **99.48%**
275. **`usr/src/cmd/troff/n9.c`** -> AI Confidence: **99.48%**
276. **`usr/src/cmd/troff/nroff.d/n10.c`** -> AI Confidence: **99.48%**
277. **`usr/src/cmd/truss/actions.c`** -> AI Confidence: **99.48%**
278. **`usr/src/cmd/truss/listopts.c`** -> AI Confidence: **99.48%**
279. **`usr/src/cmd/truss/print.c`** -> AI Confidence: **99.48%**
280. **`usr/src/cmd/uadmin/uadmin.c`** -> AI Confidence: **99.48%**
281. **`usr/src/cmd/vgrind/vfontedpr.c`** -> AI Confidence: **99.48%**
282. **`usr/src/cmd/vi/port/ex.c`** -> AI Confidence: **99.48%**
283. **`usr/src/cmd/xargs/xargs.c`** -> AI Confidence: **99.48%**
284. **`usr/src/cmd/ypcmd/makedbm.c`** -> AI Confidence: **99.48%**
285. **`usr/src/cmd/ypcmd/stdhosts.c`** -> AI Confidence: **99.48%**
286. **`usr/src/cmd/ypcmd/yppasswd/changepasswd.c`** -> AI Confidence: **99.48%**
287. **`usr/src/cmd/ypcmd/yppasswd/yppasswdd.c`** -> AI Confidence: **99.48%**
288. **`usr/src/cmd/zfs/zfs_iter.c`** -> AI Confidence: **99.48%**
289. **`usr/src/common/acl/acl_common.c`** -> AI Confidence: **99.48%**
290. **`usr/src/common/acpica/disassembler/dmopcode.c`** -> AI Confidence: **99.48%**
291. **`usr/src/common/acpica/dispatcher/dsfield.c`** -> AI Confidence: **99.48%**
292. **`usr/src/common/acpica/dispatcher/dsmethod.c`** -> AI Confidence: **99.48%**
293. **`usr/src/common/acpica/dispatcher/dsobject.c`** -> AI Confidence: **99.48%**
294. **`usr/src/common/acpica/dispatcher/dsopcode.c`** -> AI Confidence: **99.48%**
295. **`usr/src/common/acpica/dispatcher/dspkginit.c`** -> AI Confidence: **99.48%**
296. **`usr/src/common/acpica/dispatcher/dsutils.c`** -> AI Confidence: **99.48%**
297. **`usr/src/common/acpica/dispatcher/dswexec.c`** -> AI Confidence: **99.48%**
298. **`usr/src/common/acpica/dispatcher/dswload.c`** -> AI Confidence: **99.48%**
299. **`usr/src/common/acpica/dispatcher/dswload2.c`** -> AI Confidence: **99.48%**
300. **`usr/src/common/acpica/executer/exconfig.c`** -> AI Confidence: **99.48%**
301. **`usr/src/common/acpica/executer/exoparg1.c`** -> AI Confidence: **99.48%**
302. **`usr/src/common/acpica/namespace/nsparse.c`** -> AI Confidence: **99.48%**
303. **`usr/src/common/acpica/parser/psargs.c`** -> AI Confidence: **99.48%**
304. **`usr/src/common/acpica/parser/psloop.c`** -> AI Confidence: **99.48%**
305. **`usr/src/common/acpica/parser/psparse.c`** -> AI Confidence: **99.48%**
306. **`usr/src/common/acpica/parser/psxface.c`** -> AI Confidence: **99.48%**
307. **`usr/src/common/crypto/dh/dh_impl.c`** -> AI Confidence: **99.48%**
308. **`usr/src/common/crypto/dsa/dsa_impl.c`** -> AI Confidence: **99.48%**
309. **`usr/src/common/crypto/ecc/ec.c`** -> AI Confidence: **99.48%**
310. **`usr/src/common/crypto/ecc/ec2_test.c`** -> AI Confidence: **99.48%**
311. **`usr/src/common/crypto/ecc/ecdecode.c`** -> AI Confidence: **99.48%**
312. **`usr/src/common/crypto/ecc/ecl.c`** -> AI Confidence: **99.48%**
313. **`usr/src/common/crypto/ecc/ecp_test.c`** -> AI Confidence: **99.48%**
314. **`usr/src/common/crypto/ecc/oid.c`** -> AI Confidence: **99.48%**
315. **`usr/src/common/crypto/ecc/secitem.c`** -> AI Confidence: **99.48%**
316. **`usr/src/common/crypto/modes/modes.c`** -> AI Confidence: **99.48%**
317. **`usr/src/common/devid/devid.c`** -> AI Confidence: **99.48%**
318. **`usr/src/common/devid/devid_smp.c`** -> AI Confidence: **99.48%**
319. **`usr/src/common/exacct/exacct_core.c`** -> AI Confidence: **99.48%**
320. **`usr/src/common/inet/inet_hash.c`** -> AI Confidence: **99.48%**
321. **`usr/src/common/unicode/u8_textprep.c`** -> AI Confidence: **99.48%**
322. **`usr/src/common/util/string.c`** -> AI Confidence: **99.48%**
323. **`usr/src/common/util/strtol.c`** -> AI Confidence: **99.48%**
324. **`usr/src/common/util/strtoll.c`** -> AI Confidence: **99.48%**
325. **`usr/src/common/util/strtoul.c`** -> AI Confidence: **99.48%**
326. **`usr/src/common/util/strtoull.c`** -> AI Confidence: **99.48%**
327. **`usr/src/common/zfs/zfeature_common.c`** -> AI Confidence: **99.48%**
328. **`usr/src/contrib/ast/src/cmd/INIT/release.c`** -> AI Confidence: **99.48%**
329. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/cd_pwd.c`** -> AI Confidence: **99.48%**
330. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/hist.c`** -> AI Confidence: **99.48%**
331. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/misc.c`** -> AI Confidence: **99.48%**
332. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/poll_solaris.c`** -> AI Confidence: **99.48%**
333. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/print.c`** -> AI Confidence: **99.48%**
334. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/read.c`** -> AI Confidence: **99.48%**
335. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/sleep.c`** -> AI Confidence: **99.48%**
336. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/typeset.c`** -> AI Confidence: **99.48%**
337. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/ulimit.c`** -> AI Confidence: **99.48%**
338. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/umask.c`** -> AI Confidence: **99.48%**
339. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/whence.c`** -> AI Confidence: **99.48%**
340. **`usr/src/contrib/ast/src/cmd/ksh93/data/builtins.c`** -> AI Confidence: **99.48%**
341. **`usr/src/contrib/ast/src/cmd/ksh93/data/msg.c`** -> AI Confidence: **99.48%**
342. **`usr/src/contrib/ast/src/cmd/ksh93/edit/completion.c`** -> AI Confidence: **99.48%**
343. **`usr/src/contrib/ast/src/cmd/ksh93/edit/edit.c`** -> AI Confidence: **99.48%**
344. **`usr/src/contrib/ast/src/cmd/ksh93/edit/emacs.c`** -> AI Confidence: **99.48%**
345. **`usr/src/contrib/ast/src/cmd/ksh93/edit/vi.c`** -> AI Confidence: **99.48%**
346. **`usr/src/contrib/ast/src/cmd/ksh93/sh/args.c`** -> AI Confidence: **99.48%**
347. **`usr/src/contrib/ast/src/cmd/ksh93/sh/expand.c`** -> AI Confidence: **99.48%**
348. **`usr/src/contrib/ast/src/cmd/ksh93/sh/fault.c`** -> AI Confidence: **99.48%**
349. **`usr/src/contrib/ast/src/cmd/ksh93/sh/lex.c`** -> AI Confidence: **99.48%**
350. **`usr/src/contrib/ast/src/cmd/ksh93/sh/macro.c`** -> AI Confidence: **99.48%**
351. **`usr/src/contrib/ast/src/cmd/ksh93/sh/main.c`** -> AI Confidence: **99.48%**
352. **`usr/src/contrib/ast/src/cmd/ksh93/sh/name.c`** -> AI Confidence: **99.48%**
353. **`usr/src/contrib/ast/src/cmd/ksh93/sh/parse.c`** -> AI Confidence: **99.48%**
354. **`usr/src/contrib/ast/src/cmd/ksh93/sh/string.c`** -> AI Confidence: **99.48%**
355. **`usr/src/contrib/ast/src/cmd/ksh93/sh/suid_exec.c`** -> AI Confidence: **99.48%**
356. **`usr/src/contrib/ast/src/cmd/ksh93/sh/xec.c`** -> AI Confidence: **99.48%**
357. **`usr/src/contrib/ast/src/lib/libast/comp/iconv.c`** -> AI Confidence: **99.48%**
358. **`usr/src/contrib/ast/src/lib/libast/comp/omitted.c`** -> AI Confidence: **99.48%**
359. **`usr/src/contrib/ast/src/lib/libast/comp/spawnveg.c`** -> AI Confidence: **99.48%**
360. **`usr/src/contrib/ast/src/lib/libast/features/fcntl.c`** -> AI Confidence: **99.48%**
361. **`usr/src/contrib/ast/src/lib/libast/features/limits.c`** -> AI Confidence: **99.48%**
362. **`usr/src/contrib/ast/src/lib/libast/misc/error.c`** -> AI Confidence: **99.48%**
363. **`usr/src/contrib/ast/src/lib/libast/misc/glob.c`** -> AI Confidence: **99.48%**
364. **`usr/src/contrib/ast/src/lib/libast/misc/magic.c`** -> AI Confidence: **99.48%**
365. **`usr/src/contrib/ast/src/lib/libast/port/astconf.c`** -> AI Confidence: **99.48%**
366. **`usr/src/contrib/ast/src/lib/libast/port/astwinsize.c`** -> AI Confidence: **99.48%**
367. **`usr/src/contrib/ast/src/lib/libast/port/mc.c`** -> AI Confidence: **99.48%**
368. **`usr/src/contrib/ast/src/lib/libast/tm/tmlocale.c`** -> AI Confidence: **99.48%**
369. **`usr/src/contrib/ast/src/lib/libast/tm/tvtouch.c`** -> AI Confidence: **99.48%**
370. **`usr/src/contrib/ast/src/lib/libcmd/cp.c`** -> AI Confidence: **99.48%**
371. **`usr/src/contrib/ast/src/lib/libdll/dllscan.c`** -> AI Confidence: **99.48%**
372. **`usr/src/contrib/bhyve/lib/libutil/expand_number.c`** -> AI Confidence: **99.48%**
373. **`usr/src/contrib/bhyve/lib/libutil/humanize_number.c`** -> AI Confidence: **99.48%**
374. **`usr/src/contrib/mDNSResponder/mDNSCore/mDNS.c`** -> AI Confidence: **99.48%**
375. **`usr/src/contrib/mDNSResponder/mDNSShared/ClientRequests.c`** -> AI Confidence: **99.48%**
376. **`usr/src/contrib/mDNSResponder/mDNSShared/uds_daemon.c`** -> AI Confidence: **99.48%**
377. **`usr/src/contrib/zlib/zconf.h`** -> AI Confidence: **99.48%**
378. **`usr/src/grub/grub-0.97/grub/main.c`** -> AI Confidence: **99.48%**
379. **`usr/src/grub/grub-0.97/lib/getopt.c`** -> AI Confidence: **99.48%**
380. **`usr/src/lib/cfgadm_plugins/sbd/common/ap.c`** -> AI Confidence: **99.48%**
381. **`usr/src/lib/cfgadm_plugins/sbd/common/ap_seq.c`** -> AI Confidence: **99.48%**
382. **`usr/src/lib/fm/topo/modules/common/disk/disk_common.c`** -> AI Confidence: **99.48%**
383. **`usr/src/lib/fm/topo/modules/common/pcibus/pcibus_labels.c`** -> AI Confidence: **99.48%**
384. **`usr/src/lib/fm/topo/modules/i86pc/x86pi/x86pi.c`** -> AI Confidence: **99.48%**
385. **`usr/src/lib/gss_mechs/mech_krb5/krb5/asn.1/ldap_key_seq.c`** -> AI Confidence: **99.48%**
386. **`usr/src/lib/gss_mechs/mech_krb5/krb5/keytab/kt_solaris.c`** -> AI Confidence: **99.48%**
387. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/get_in_tkt.c`** -> AI Confidence: **99.48%**
388. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/mk_safe.c`** -> AI Confidence: **99.48%**
389. **`usr/src/lib/gss_mechs/mech_krb5/mech/accept_sec_context.c`** -> AI Confidence: **99.48%**
390. **`usr/src/lib/hal/libhal-storage/common/libhal-storage.c`** -> AI Confidence: **99.48%**
391. **`usr/src/lib/hbaapi/common/HBAAPILIB.c`** -> AI Confidence: **99.48%**
392. **`usr/src/lib/iconv_modules/hi_IN/UTF-8%iscii91.c`** -> AI Confidence: **99.48%**
393. **`usr/src/lib/iconv_modules/ja/common/ISO-2022-JP_TO_UTF-8.c`** -> AI Confidence: **99.48%**
394. **`usr/src/lib/iconv_modules/ko/common/ucs_to_unihan.c`** -> AI Confidence: **99.48%**
395. **`usr/src/lib/iconv_modules/utf-8/common/binarytables/test/sb_to_utf8_test.c`** -> AI Confidence: **99.48%**
396. **`usr/src/lib/iconv_modules/utf-8/common/binarytables/test/utf8_to_ebcdic_test.c`** -> AI Confidence: **99.48%**
397. **`usr/src/lib/iconv_modules/utf-8/common/sb_to_ucs.h`** -> AI Confidence: **99.48%**
398. **`usr/src/lib/iconv_modules/utf-8/common/sb_to_utf8.h`** -> AI Confidence: **99.48%**
399. **`usr/src/lib/iconv_modules/utf-8/common/ucs_to_sb.h`** -> AI Confidence: **99.48%**
400. **`usr/src/lib/iconv_modules/utf-8/common/utf8_to_sb.h`** -> AI Confidence: **99.48%**
401. **`usr/src/lib/iconv_modules/zh/common/UTF-8%zh_CN.euc.c`** -> AI Confidence: **99.48%**
402. **`usr/src/lib/iconv_modules/zh/common/UTF-8%zh_CN.gbk.c`** -> AI Confidence: **99.48%**
403. **`usr/src/lib/iconv_modules/zh/common/zh_CN.iso2022-CN%zh_CN.euc.c`** -> AI Confidence: **99.48%**
404. **`usr/src/lib/krb5/kadm5/alt_prof.c`** -> AI Confidence: **99.48%**
405. **`usr/src/lib/krb5/kadm5/srv/server_acl.c`** -> AI Confidence: **99.48%**
406. **`usr/src/lib/krb5/kadm5/srv/svr_principal.c`** -> AI Confidence: **99.48%**
407. **`usr/src/lib/krb5/kdb/kdb_convert.c`** -> AI Confidence: **99.48%**
408. **`usr/src/lib/krb5/plugins/kdb/db2/libdb2/btree/bt_open.c`** -> AI Confidence: **99.48%**
409. **`usr/src/lib/krb5/plugins/kdb/db2/libdb2/btree/bt_put.c`** -> AI Confidence: **99.48%**
410. **`usr/src/lib/krb5/plugins/kdb/db2/libdb2/btree/bt_split.c`** -> AI Confidence: **99.48%**
411. **`usr/src/lib/krb5/plugins/kdb/db2/libdb2/recno/rec_open.c`** -> AI Confidence: **99.48%**
412. **`usr/src/lib/krb5/plugins/kdb/db2/libdb2/recno/rec_put.c`** -> AI Confidence: **99.48%**
413. **`usr/src/lib/krb5/plugins/kdb/db2/libdb2/recno/rec_seq.c`** -> AI Confidence: **99.48%**
414. **`usr/src/lib/krb5/plugins/kdb/ldap/ldap_exp.c`** -> AI Confidence: **99.48%**
415. **`usr/src/lib/krb5/plugins/kdb/ldap/libkdb_ldap/ldap_misc.c`** -> AI Confidence: **99.48%**
416. **`usr/src/lib/krb5/plugins/kdb/ldap/libkdb_ldap/ldap_principal2.c`** -> AI Confidence: **99.48%**
417. **`usr/src/lib/krb5/plugins/preauth/pkinit/pkinit_clnt.c`** -> AI Confidence: **99.48%**
418. **`usr/src/lib/krb5/plugins/preauth/pkinit/pkinit_identity.c`** -> AI Confidence: **99.48%**
419. **`usr/src/lib/krb5/ss/mk_cmds.c`** -> AI Confidence: **99.48%**
420. **`usr/src/lib/lib9p/common/pack.c`** -> AI Confidence: **99.48%**
421. **`usr/src/lib/libadm/common/devtab.c`** -> AI Confidence: **99.48%**
422. **`usr/src/lib/libadm/common/puttext.c`** -> AI Confidence: **99.48%**
423. **`usr/src/lib/libc/i386/crt/_rtld.c`** -> AI Confidence: **99.48%**
424. **`usr/src/lib/libc/port/fp/__x_power.c`** -> AI Confidence: **99.48%**
425. **`usr/src/lib/libc/port/fp/file_decim.c`** -> AI Confidence: **99.48%**
426. **`usr/src/lib/libc/port/gen/fmtmsg.c`** -> AI Confidence: **99.48%**
427. **`usr/src/lib/libc/port/gen/hsearch.c`** -> AI Confidence: **99.48%**
428. **`usr/src/lib/libc/port/gen/mktemp.c`** -> AI Confidence: **99.48%**
429. **`usr/src/lib/libc/port/gen/nlspath_checks.c`** -> AI Confidence: **99.48%**
430. **`usr/src/lib/libc/port/gen/pfmt_print.c`** -> AI Confidence: **99.48%**
431. **`usr/src/lib/libc/port/gen/priv_str_xlate.c`** -> AI Confidence: **99.48%**
432. **`usr/src/lib/libc/port/gen/psecflags.c`** -> AI Confidence: **99.48%**
433. **`usr/src/lib/libc/port/gen/select.c`** -> AI Confidence: **99.48%**
434. **`usr/src/lib/libc/port/i18n/wstod.c`** -> AI Confidence: **99.48%**
435. **`usr/src/lib/libc/port/locale/collate.c`** -> AI Confidence: **99.48%**
436. **`usr/src/lib/libc/port/locale/fnmatch.c`** -> AI Confidence: **99.48%**
437. **`usr/src/lib/libc/port/locale/fwide.c`** -> AI Confidence: **99.48%**
438. **`usr/src/lib/libc/port/locale/gb18030.c`** -> AI Confidence: **99.48%**
439. **`usr/src/lib/libc/port/locale/nl_langinfo.c`** -> AI Confidence: **99.48%**
440. **`usr/src/lib/libc/port/locale/setlocale.c`** -> AI Confidence: **99.48%**
441. **`usr/src/lib/libc/port/locale/strcoll.c`** -> AI Confidence: **99.48%**
442. **`usr/src/lib/libc/port/locale/strfmon.c`** -> AI Confidence: **99.48%**
443. **`usr/src/lib/libc/port/locale/strftime.c`** -> AI Confidence: **99.48%**
444. **`usr/src/lib/libc/port/locale/wcscoll.c`** -> AI Confidence: **99.48%**
445. **`usr/src/lib/libc/port/print/doprnt.c`** -> AI Confidence: **99.48%**
446. **`usr/src/lib/libc/port/regex/regcmp.c`** -> AI Confidence: **99.48%**
447. **`usr/src/lib/libc/port/stdio/_findbuf.c`** -> AI Confidence: **99.48%**
448. **`usr/src/lib/libc/port/stdio/data.c`** -> AI Confidence: **99.48%**
449. **`usr/src/lib/libc/port/stdio/doscan.c`** -> AI Confidence: **99.48%**
450. **`usr/src/lib/libc/port/stdio/fgets.c`** -> AI Confidence: **99.48%**
451. **`usr/src/lib/libc/port/stdio/fseek.c`** -> AI Confidence: **99.48%**
452. **`usr/src/lib/libc/port/stdio/gets.c`** -> AI Confidence: **99.48%**
453. **`usr/src/lib/libc/port/stdio/setbuf.c`** -> AI Confidence: **99.48%**
454. **`usr/src/lib/libc/port/stdio/setvbuf.c`** -> AI Confidence: **99.48%**
455. **`usr/src/lib/libc/sparc/crt/_rtld.c`** -> AI Confidence: **99.48%**
456. **`usr/src/lib/libcommputil/common/sdp_parse.c`** -> AI Confidence: **99.48%**
457. **`usr/src/lib/libcrypt/common/des_soft.c`** -> AI Confidence: **99.48%**
458. **`usr/src/lib/libcryptoutil/common/pkcs11_uri.c`** -> AI Confidence: **99.48%**
459. **`usr/src/lib/libctf/common/ctf_elfwrite.c`** -> AI Confidence: **99.48%**
460. **`usr/src/lib/libcurses/screen/tparm.c`** -> AI Confidence: **99.48%**
461. **`usr/src/lib/libdiskmgt/common/entry.c`** -> AI Confidence: **99.48%**
462. **`usr/src/lib/libdladm/common/libdlether.c`** -> AI Confidence: **99.48%**
463. **`usr/src/lib/libdtrace/common/dt_as.c`** -> AI Confidence: **99.48%**
464. **`usr/src/lib/libdtrace/common/dt_cc.c`** -> AI Confidence: **99.48%**
465. **`usr/src/lib/libdtrace/common/dt_cg.c`** -> AI Confidence: **99.48%**
466. **`usr/src/lib/libdtrace/common/dt_link.c`** -> AI Confidence: **99.48%**
467. **`usr/src/lib/libdtrace/common/dt_pragma.c`** -> AI Confidence: **99.48%**
468. **`usr/src/lib/libdtrace/sparc/dt_isadep.c`** -> AI Confidence: **99.48%**
469. **`usr/src/lib/libdwarf/common/dwarf_locationop_read.c`** -> AI Confidence: **99.48%**
470. **`usr/src/lib/libdwarf/common/gennames.c`** -> AI Confidence: **99.48%**
471. **`usr/src/lib/libdwarf/common/pro_log_extra_flag_strings.c`** -> AI Confidence: **99.48%**
472. **`usr/src/lib/libfakekernel/common/sys/t_lock.h`** -> AI Confidence: **99.48%**
473. **`usr/src/lib/libfcoe/common/libfcoe.c`** -> AI Confidence: **99.48%**
474. **`usr/src/lib/libgen/common/bgets.c`** -> AI Confidence: **99.48%**
475. **`usr/src/lib/libgen/common/reg_compile.c`** -> AI Confidence: **99.48%**
476. **`usr/src/lib/libgss/g_dsp_status.c`** -> AI Confidence: **99.48%**
477. **`usr/src/lib/libima/common/ima-lib.c`** -> AI Confidence: **99.48%**
478. **`usr/src/lib/libipmp/common/ipmp_mpathd.c`** -> AI Confidence: **99.48%**
479. **`usr/src/lib/libkmf/libkmf/common/certop.c`** -> AI Confidence: **99.48%**
480. **`usr/src/lib/libldap5/sources/ldap/common/getdxbyname.c`** -> AI Confidence: **99.48%**
481. **`usr/src/lib/libldap5/sources/ldap/util/line64.c`** -> AI Confidence: **99.48%**
482. **`usr/src/lib/libm/common/C/_SVID_error.c`** -> AI Confidence: **99.48%**
483. **`usr/src/lib/libm/common/m9x/__fex_hdlr.c`** -> AI Confidence: **99.48%**
484. **`usr/src/lib/libm/common/m9x/__fex_sparc.c`** -> AI Confidence: **99.48%**
485. **`usr/src/lib/libm/common/m9x/__fex_sym.c`** -> AI Confidence: **99.48%**
486. **`usr/src/lib/libnisdb/ldap_ldap.c`** -> AI Confidence: **99.48%**
487. **`usr/src/lib/libnisdb/ldap_map.c`** -> AI Confidence: **99.48%**
488. **`usr/src/lib/libnisdb/ldap_nisdbquery.c`** -> AI Confidence: **99.48%**
489. **`usr/src/lib/libnisdb/ldap_val.c`** -> AI Confidence: **99.48%**
490. **`usr/src/lib/libnisdb/nis_parse_ldap_attr.c`** -> AI Confidence: **99.48%**
491. **`usr/src/lib/libnisdb/nis_parse_ldap_conf.c`** -> AI Confidence: **99.48%**
492. **`usr/src/lib/libnisdb/nis_parse_ldap_map.c`** -> AI Confidence: **99.48%**
493. **`usr/src/lib/libnisdb/nis_parse_ldap_util.c`** -> AI Confidence: **99.48%**
494. **`usr/src/lib/libnisdb/yptol/dit_access_utils.c`** -> AI Confidence: **99.48%**
495. **`usr/src/lib/libnsl/nsl/t_rcv.c`** -> AI Confidence: **99.48%**
496. **`usr/src/lib/libnsl/nsl/t_rcvv.c`** -> AI Confidence: **99.48%**
497. **`usr/src/lib/libnsl/nss/inet_matchaddr.c`** -> AI Confidence: **99.48%**
498. **`usr/src/lib/libproc/common/Psymtab_machelf32.c`** -> AI Confidence: **99.48%**
499. **`usr/src/lib/libproc/common/Psyscall.c`** -> AI Confidence: **99.48%**
500. **`usr/src/lib/libprtdiag/common/libdevinfo_sun4u.c`** -> AI Confidence: **99.48%**
501. **`usr/src/lib/libprtdiag_psr/sparc/desktop/common/desktop.c`** -> AI Confidence: **99.48%**
502. **`usr/src/lib/libresolv/res_query.c`** -> AI Confidence: **99.48%**
503. **`usr/src/lib/libresolv2/common/bsd/strtoul.c`** -> AI Confidence: **99.48%**
504. **`usr/src/lib/libresolv2/common/inet/inet_cidr_pton.c`** -> AI Confidence: **99.48%**
505. **`usr/src/lib/libresolv2/common/inet/inet_net_pton.c`** -> AI Confidence: **99.48%**
506. **`usr/src/lib/libresolv2/common/inet/inet_neta.c`** -> AI Confidence: **99.48%**
507. **`usr/src/lib/libresolv2/common/inet/nsap_addr.c`** -> AI Confidence: **99.48%**
508. **`usr/src/lib/libresolv2/common/irs/irpmarshall.c`** -> AI Confidence: **99.48%**
509. **`usr/src/lib/libresolv2/common/isc/ev_files.c`** -> AI Confidence: **99.48%**
510. **`usr/src/lib/libresolv2/common/nameser/ns_print.c`** -> AI Confidence: **99.48%**
511. **`usr/src/lib/libresolv2/common/nameser/ns_rdata.c`** -> AI Confidence: **99.48%**
512. **`usr/src/lib/libresolv2/common/nameser/ns_ttl.c`** -> AI Confidence: **99.48%**
513. **`usr/src/lib/libresolv2/common/resolv/res_query.c`** -> AI Confidence: **99.48%**
514. **`usr/src/lib/libresolv2/common/resolv/res_sendsigned.c`** -> AI Confidence: **99.48%**
515. **`usr/src/lib/librestart/common/librestart.c`** -> AI Confidence: **99.48%**
516. **`usr/src/lib/libsasl/lib/client.c`** -> AI Confidence: **99.48%**
517. **`usr/src/lib/libsasl/lib/server.c`** -> AI Confidence: **99.48%**
518. **`usr/src/lib/libsasl/lib/seterror.c`** -> AI Confidence: **99.48%**
519. **`usr/src/lib/libscf/common/midlevel.c`** -> AI Confidence: **99.48%**
520. **`usr/src/lib/libscf/common/scf_tmpl.c`** -> AI Confidence: **99.48%**
521. **`usr/src/lib/libsec/common/acltext.c`** -> AI Confidence: **99.48%**
522. **`usr/src/lib/libshare/nfs/libshare_nfs.c`** -> AI Confidence: **99.48%**
523. **`usr/src/lib/libshare/smbfs/smbfs_scfutil.c`** -> AI Confidence: **99.48%**
524. **`usr/src/lib/libsldap/common/ns_writes.c`** -> AI Confidence: **99.48%**
525. **`usr/src/lib/libslp/clib/slp_auth.c`** -> AI Confidence: **99.48%**
526. **`usr/src/lib/libsmbfs/smb/charsets.c`** -> AI Confidence: **99.48%**
527. **`usr/src/lib/libsmbfs/smb/iod_wk.c`** -> AI Confidence: **99.48%**
528. **`usr/src/lib/libsmbfs/smb/rc_scf.c`** -> AI Confidence: **99.48%**
529. **`usr/src/lib/libsmbfs/smb/spnego.c`** -> AI Confidence: **99.48%**
530. **`usr/src/lib/libsmbfs/smb/ssp.c`** -> AI Confidence: **99.48%**
531. **`usr/src/lib/libsqlite/tool/diffdb.c`** -> AI Confidence: **99.48%**
532. **`usr/src/lib/libsqlite/tool/showdb.c`** -> AI Confidence: **99.48%**
533. **`usr/src/lib/libstmf/common/store.c`** -> AI Confidence: **99.48%**
534. **`usr/src/lib/libtsnet/common/misc.c`** -> AI Confidence: **99.48%**
535. **`usr/src/lib/libtsnet/common/tsol_sgetzcent.c`** -> AI Confidence: **99.48%**
536. **`usr/src/lib/libtsol/common/stob.c`** -> AI Confidence: **99.48%**
537. **`usr/src/lib/libzfsbootenv/common/lzbe_pair.c`** -> AI Confidence: **99.48%**
538. **`usr/src/lib/libzonestat/common/libzonestat.c`** -> AI Confidence: **99.48%**
539. **`usr/src/lib/madv/common/madv.c`** -> AI Confidence: **99.48%**
540. **`usr/src/lib/mpss/common/mpss.c`** -> AI Confidence: **99.48%**
541. **`usr/src/lib/nsswitch/files/common/files_common.c`** -> AI Confidence: **99.48%**
542. **`usr/src/lib/pam_modules/krb5/krb5_setcred.c`** -> AI Confidence: **99.48%**
543. **`usr/src/lib/pam_modules/krb5_migrate/krb5_migrate_authenticate.c`** -> AI Confidence: **99.48%**
544. **`usr/src/lib/pam_modules/list/list.c`** -> AI Confidence: **99.48%**
545. **`usr/src/lib/passwdutil/nss_attr.c`** -> AI Confidence: **99.48%**
546. **`usr/src/lib/pkcs11/pkcs11_kernel/common/kernelAttributeUtil.c`** -> AI Confidence: **99.48%**
547. **`usr/src/lib/pkcs11/pkcs11_kernel/common/kernelKeys.c`** -> AI Confidence: **99.48%**
548. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softAESCrypt.c`** -> AI Confidence: **99.48%**
549. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softASN1.c`** -> AI Confidence: **99.48%**
550. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softAttributeUtil.c`** -> AI Confidence: **99.48%**
551. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softDH.c`** -> AI Confidence: **99.48%**
552. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softKeysUtil.c`** -> AI Confidence: **99.48%**
553. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softRSA.c`** -> AI Confidence: **99.48%**
554. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softSignUtil.c`** -> AI Confidence: **99.48%**
555. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softVerifyUtil.c`** -> AI Confidence: **99.48%**
556. **`usr/src/lib/print/libipp-core/common/ipp_types.c`** -> AI Confidence: **99.48%**
557. **`usr/src/lib/print/libpapi-common/common/uri.c`** -> AI Confidence: **99.48%**
558. **`usr/src/lib/print/libpapi-lpd/common/lpd-misc.c`** -> AI Confidence: **99.48%**
559. **`usr/src/lib/print/libprint/common/nss_ldap.c`** -> AI Confidence: **99.48%**
560. **`usr/src/lib/sasl_plugins/cram/crammd5_init.c`** -> AI Confidence: **99.48%**
561. **`usr/src/lib/sasl_plugins/digestmd5/digestmd5_init.c`** -> AI Confidence: **99.48%**
562. **`usr/src/lib/sasl_plugins/gssapi/gssapiv2_init.c`** -> AI Confidence: **99.48%**
563. **`usr/src/lib/sasl_plugins/login/login_init.c`** -> AI Confidence: **99.48%**
564. **`usr/src/lib/sasl_plugins/plain/plain_init.c`** -> AI Confidence: **99.48%**
565. **`usr/src/lib/smbclnt/libfksmbfs/common/fake_rename.c`** -> AI Confidence: **99.48%**
566. **`usr/src/lib/smbsrv/libfksmbsrv/common/fake_lookup.c`** -> AI Confidence: **99.48%**
567. **`usr/src/psm/stand/boot/common/readfile.c`** -> AI Confidence: **99.48%**
568. **`usr/src/psm/stand/boot/sparc/common/bootflags.c`** -> AI Confidence: **99.48%**
569. **`usr/src/stand/lib/fs/nfs/bootparams.c`** -> AI Confidence: **99.48%**
570. **`usr/src/stand/lib/fs/nfs/rpc.c`** -> AI Confidence: **99.48%**
571. **`usr/src/stand/lib/tcp/tcp.c`** -> AI Confidence: **99.48%**
572. **`usr/src/test/crypto-tests/tests/common/cryptotest_kcf.c`** -> AI Confidence: **99.48%**
573. **`usr/src/test/i2c-tests/i2csimd/i2csimd.c`** -> AI Confidence: **99.48%**
574. **`usr/src/test/libc-tests/tests/posix_spawn/posix_spawn.c`** -> AI Confidence: **99.48%**
575. **`usr/src/test/libc-tests/tests/random/inz_split_vpp.c`** -> AI Confidence: **99.48%**
576. **`usr/src/test/libc-tests/tests/regex/testregex.c`** -> AI Confidence: **99.48%**
577. **`usr/src/test/libc-tests/tests/stdio/orientation_test.c`** -> AI Confidence: **99.48%**
578. **`usr/src/test/libc-tests/tests/strcoll-strxfrm-6907.c`** -> AI Confidence: **99.48%**
579. **`usr/src/test/libc-tests/tests/threads/thread_name.c`** -> AI Confidence: **99.48%**
580. **`usr/src/test/libc-tests/tests/wctype/wctype_test.c`** -> AI Confidence: **99.48%**
581. **`usr/src/test/libsec-tests/cmd/acl_to_text.c`** -> AI Confidence: **99.48%**
582. **`usr/src/test/os-tests/tests/cores/secmapper/secmapper.c`** -> AI Confidence: **99.48%**
583. **`usr/src/test/os-tests/tests/mac/mac_cksum.c`** -> AI Confidence: **99.48%**
584. **`usr/src/test/os-tests/tests/mac/mac_lso.c`** -> AI Confidence: **99.48%**
585. **`usr/src/test/os-tests/tests/uccid/excl-badread.c`** -> AI Confidence: **99.48%**
586. **`usr/src/test/os-tests/tests/uccid/excl-basic.c`** -> AI Confidence: **99.48%**
587. **`usr/src/test/os-tests/tests/uccid/excl-close.c`** -> AI Confidence: **99.48%**
588. **`usr/src/test/os-tests/tests/uccid/excl-loop.c`** -> AI Confidence: **99.48%**
589. **`usr/src/test/os-tests/tests/uccid/excl-reset.c`** -> AI Confidence: **99.48%**
590. **`usr/src/test/os-tests/tests/uccid/modify.c`** -> AI Confidence: **99.48%**
591. **`usr/src/test/os-tests/tests/uccid/txn-pollerr.c`** -> AI Confidence: **99.48%**
592. **`usr/src/test/os-tests/tests/uccid/yk-readonly.c`** -> AI Confidence: **99.48%**
593. **`usr/src/test/os-tests/tests/xsave/xsave_baducontext.c`** -> AI Confidence: **99.48%**
594. **`usr/src/test/smbclient-tests/cmd/cp_mmap/cp_mmap.c`** -> AI Confidence: **99.48%**
595. **`usr/src/test/smbclient-tests/cmd/mkfile_mmap/mkfile_mmap.c`** -> AI Confidence: **99.48%**
596. **`usr/src/test/smbclient-tests/cmd/prot_mmap/prot_mmap.c`** -> AI Confidence: **99.48%**
597. **`usr/src/tools/protocmp/proto_list.c`** -> AI Confidence: **99.48%**
598. **`usr/src/tools/smatch/src/char.c`** -> AI Confidence: **99.48%**
599. **`usr/src/ucbcmd/stty/sttyparse.c`** -> AI Confidence: **99.48%**
600. **`usr/src/ucblib/librpcsoc/get_myaddress.c`** -> AI Confidence: **99.48%**
601. **`usr/src/ucblib/libucb/port/stdio/doprnt.c`** -> AI Confidence: **99.48%**
602. **`usr/src/ucblib/libucb/port/sys/wait4.c`** -> AI Confidence: **99.48%**
603. **`usr/src/uts/common/c2/audit_path.c`** -> AI Confidence: **99.48%**
604. **`usr/src/uts/common/crypto/api/kcf_dual.c`** -> AI Confidence: **99.48%**
605. **`usr/src/uts/common/crypto/api/kcf_mac.c`** -> AI Confidence: **99.48%**
606. **`usr/src/uts/common/crypto/core/kcf_callprov.c`** -> AI Confidence: **99.48%**
607. **`usr/src/uts/common/crypto/core/kcf_mech_tabs.c`** -> AI Confidence: **99.48%**
608. **`usr/src/uts/common/crypto/io/sha2_mod.c`** -> AI Confidence: **99.48%**
609. **`usr/src/uts/common/crypto/spi/kcf_spi.c`** -> AI Confidence: **99.48%**
610. **`usr/src/uts/common/disp/cmt_policy.c`** -> AI Confidence: **99.48%**
611. **`usr/src/uts/common/exec/elf/elf.c`** -> AI Confidence: **99.48%**
612. **`usr/src/uts/common/exec/elf/elf_notes.c`** -> AI Confidence: **99.48%**
613. **`usr/src/uts/common/fs/mntfs/mntvnops.c`** -> AI Confidence: **99.48%**
614. **`usr/src/uts/common/fs/nfs/nfs4_acl.c`** -> AI Confidence: **99.48%**
615. **`usr/src/uts/common/fs/nfs/nfs4_attr.c`** -> AI Confidence: **99.48%**
616. **`usr/src/uts/common/fs/nfs/nfs4_client_debug.c`** -> AI Confidence: **99.48%**
617. **`usr/src/uts/common/fs/nfs/nfs4_recovery.c`** -> AI Confidence: **99.48%**
618. **`usr/src/uts/common/fs/portfs/port.c`** -> AI Confidence: **99.48%**
619. **`usr/src/uts/common/fs/proc/prcontrol.c`** -> AI Confidence: **99.48%**
620. **`usr/src/uts/common/fs/proc/prioctl.c`** -> AI Confidence: **99.48%**
621. **`usr/src/uts/common/fs/proc/prsubr.c`** -> AI Confidence: **99.48%**
622. **`usr/src/uts/common/fs/proc/prusrio.c`** -> AI Confidence: **99.48%**
623. **`usr/src/uts/common/fs/smbsrv/smb2_durable.c`** -> AI Confidence: **99.48%**
624. **`usr/src/uts/common/fs/smbsrv/smb_common_open.c`** -> AI Confidence: **99.48%**
625. **`usr/src/uts/common/fs/smbsrv/smb_mangle_name.c`** -> AI Confidence: **99.48%**
626. **`usr/src/uts/common/fs/smbsrv/smb_quota.c`** -> AI Confidence: **99.48%**
627. **`usr/src/uts/common/fs/smbsrv/smb_session_setup_andx.c`** -> AI Confidence: **99.48%**
628. **`usr/src/uts/common/fs/ufs/lufs_map.c`** -> AI Confidence: **99.48%**
629. **`usr/src/uts/common/fs/ufs/lufs_thread.c`** -> AI Confidence: **99.48%**
630. **`usr/src/uts/common/fs/zfs/lua/lvm.c`** -> AI Confidence: **99.48%**
631. **`usr/src/uts/common/fs/zfs/sys/zfs_context.h`** -> AI Confidence: **99.48%**
632. **`usr/src/uts/common/fs/zfs/vdev_label.c`** -> AI Confidence: **99.48%**
633. **`usr/src/uts/common/fs/zfs/vdev_raidz.c`** -> AI Confidence: **99.48%**
634. **`usr/src/uts/common/fs/zfs/vdev_trim.c`** -> AI Confidence: **99.48%**
635. **`usr/src/uts/common/fs/zfs/zfs_vnops.c`** -> AI Confidence: **99.48%**
636. **`usr/src/uts/common/fs/zfs/zio_checksum.c`** -> AI Confidence: **99.48%**
637. **`usr/src/uts/common/inet/ip/igmp.c`** -> AI Confidence: **99.48%**
638. **`usr/src/uts/common/inet/ip/ip6_output.c`** -> AI Confidence: **99.48%**
639. **`usr/src/uts/common/inet/ip/ip6_rts.c`** -> AI Confidence: **99.48%**
640. **`usr/src/uts/common/inet/ip/ip_ftable.c`** -> AI Confidence: **99.48%**
641. **`usr/src/uts/common/inet/ip/ip_rts.c`** -> AI Confidence: **99.48%**
642. **`usr/src/uts/common/inet/ip/ip_sadb.c`** -> AI Confidence: **99.48%**
643. **`usr/src/uts/common/inet/ip/ip_tunables.c`** -> AI Confidence: **99.48%**
644. **`usr/src/uts/common/inet/ipf/ip_auth.c`** -> AI Confidence: **99.48%**
645. **`usr/src/uts/common/inet/ipf/ip_log.c`** -> AI Confidence: **99.48%**
646. **`usr/src/uts/common/inet/ipf/ip_nat.c`** -> AI Confidence: **99.48%**
647. **`usr/src/uts/common/inet/ipf/ip_nat6.c`** -> AI Confidence: **99.48%**
648. **`usr/src/uts/common/inet/ipf/ip_proxy.c`** -> AI Confidence: **99.48%**
649. **`usr/src/uts/common/inet/ipf/ip_state.c`** -> AI Confidence: **99.48%**
650. **`usr/src/uts/common/inet/sctp/sctp_bind.c`** -> AI Confidence: **99.48%**
651. **`usr/src/uts/common/inet/sctp/sctp_cookie.c`** -> AI Confidence: **99.48%**
652. **`usr/src/uts/common/inet/sctp/sctp_input.c`** -> AI Confidence: **99.48%**
653. **`usr/src/uts/common/inet/sctp/sctp_output.c`** -> AI Confidence: **99.48%**
654. **`usr/src/uts/common/inet/squeue.c`** -> AI Confidence: **99.48%**
655. **`usr/src/uts/common/inet/tcp/tcp_bind.c`** -> AI Confidence: **99.48%**
656. **`usr/src/uts/common/inet/tcp/tcp_time_wait.c`** -> AI Confidence: **99.48%**
657. **`usr/src/uts/common/io/1394/adapters/hci1394_vendor.c`** -> AI Confidence: **99.48%**
658. **`usr/src/uts/common/io/1394/s1394_addr.c`** -> AI Confidence: **99.48%**
659. **`usr/src/uts/common/io/1394/s1394_asynch.c`** -> AI Confidence: **99.48%**
660. **`usr/src/uts/common/io/1394/s1394_hotplug.c`** -> AI Confidence: **99.48%**
661. **`usr/src/uts/common/io/audio/impl/audio_oss.c`** -> AI Confidence: **99.48%**
662. **`usr/src/uts/common/io/audio/impl/audio_sun.c`** -> AI Confidence: **99.48%**
663. **`usr/src/uts/common/io/bnx/570x/driver/common/lmdev/bnx_hw_cpu.c`** -> AI Confidence: **99.48%**
664. **`usr/src/uts/common/io/bnx/bnxgldv3.c`** -> AI Confidence: **99.48%**
665. **`usr/src/uts/common/io/bnxe/577xx/drivers/common/lm/device/bnxe_hw_debug.c`** -> AI Confidence: **99.48%**
666. **`usr/src/uts/common/io/bpf/bpf_filter.c`** -> AI Confidence: **99.48%**
667. **`usr/src/uts/common/io/comstar/port/fct/discovery.c`** -> AI Confidence: **99.48%**
668. **`usr/src/uts/common/io/fibre-channel/fca/qlc/ql_init.c`** -> AI Confidence: **99.48%**
669. **`usr/src/uts/common/io/fibre-channel/fca/qlc/ql_iocb.c`** -> AI Confidence: **99.48%**
670. **`usr/src/uts/common/io/fibre-channel/fca/qlc/ql_isr.c`** -> AI Confidence: **99.48%**
671. **`usr/src/uts/common/io/fibre-channel/impl/fp.c`** -> AI Confidence: **99.48%**
672. **`usr/src/uts/common/io/ib/adapters/hermon/hermon_cq.c`** -> AI Confidence: **99.48%**
673. **`usr/src/uts/common/io/ib/adapters/hermon/hermon_mr.c`** -> AI Confidence: **99.48%**
674. **`usr/src/uts/common/io/ib/adapters/hermon/hermon_qp.c`** -> AI Confidence: **99.48%**
675. **`usr/src/uts/common/io/ib/adapters/hermon/hermon_srq.c`** -> AI Confidence: **99.48%**
676. **`usr/src/uts/common/io/ib/adapters/hermon/hermon_wr.c`** -> AI Confidence: **99.48%**
677. **`usr/src/uts/common/io/ib/adapters/tavor/tavor_cfg.c`** -> AI Confidence: **99.48%**
678. **`usr/src/uts/common/io/ib/adapters/tavor/tavor_cq.c`** -> AI Confidence: **99.48%**
679. **`usr/src/uts/common/io/ib/adapters/tavor/tavor_mr.c`** -> AI Confidence: **99.48%**
680. **`usr/src/uts/common/io/ib/adapters/tavor/tavor_qp.c`** -> AI Confidence: **99.48%**
681. **`usr/src/uts/common/io/ib/adapters/tavor/tavor_srq.c`** -> AI Confidence: **99.48%**
682. **`usr/src/uts/common/io/ib/clients/eoib/enx_misc.c`** -> AI Confidence: **99.48%**
683. **`usr/src/uts/common/io/ib/ibnex/ibnex_ioctl.c`** -> AI Confidence: **99.48%**
684. **`usr/src/uts/common/io/kb8042/at_keyprocess.c`** -> AI Confidence: **99.48%**
685. **`usr/src/uts/common/io/mac/mac_ndd.c`** -> AI Confidence: **99.48%**
686. **`usr/src/uts/common/io/mac/mac_sched.c`** -> AI Confidence: **99.48%**
687. **`usr/src/uts/common/io/mlxcx/mlxcx_gld.c`** -> AI Confidence: **99.48%**
688. **`usr/src/uts/common/io/mxfe/mxfe.c`** -> AI Confidence: **99.48%**
689. **`usr/src/uts/common/io/ntxn/unm_nic_isr.c`** -> AI Confidence: **99.48%**
690. **`usr/src/uts/common/io/ppp/sppp/sppp.c`** -> AI Confidence: **99.48%**
691. **`usr/src/uts/common/io/ppp/spppasyn/spppasyn.c`** -> AI Confidence: **99.48%**
692. **`usr/src/uts/common/io/ppp/spppcomp/vjcompress.c`** -> AI Confidence: **99.48%**
693. **`usr/src/uts/common/io/ppp/sppptun/sppptun.c`** -> AI Confidence: **99.48%**
694. **`usr/src/uts/common/io/scsi/adapters/mpt_sas/mptsas_raid.c`** -> AI Confidence: **99.48%**
695. **`usr/src/uts/common/io/sfxge/sfxge_gld_v3.c`** -> AI Confidence: **99.48%**
696. **`usr/src/uts/common/io/stream.c`** -> AI Confidence: **99.48%**
697. **`usr/src/uts/common/io/vuidmice/vuidps2.c`** -> AI Confidence: **99.48%**
698. **`usr/src/uts/common/ipp/dlcosmk/dlcosmk.c`** -> AI Confidence: **99.48%**
699. **`usr/src/uts/common/ipp/ipgpc/ipgpc.h`** -> AI Confidence: **99.48%**
700. **`usr/src/uts/common/ipp/meters/tokenmt.c`** -> AI Confidence: **99.48%**
701. **`usr/src/uts/common/ipp/meters/tswtcl.c`** -> AI Confidence: **99.48%**
702. **`usr/src/uts/common/krtld/kobj_bootflags.c`** -> AI Confidence: **99.48%**
703. **`usr/src/uts/common/ktli/t_krcvudat.c`** -> AI Confidence: **99.48%**
704. **`usr/src/uts/common/os/cyclic.c`** -> AI Confidence: **99.48%**
705. **`usr/src/uts/common/os/exit.c`** -> AI Confidence: **99.48%**
706. **`usr/src/uts/common/os/ip_cksum.c`** -> AI Confidence: **99.48%**
707. **`usr/src/uts/common/os/labelsys.c`** -> AI Confidence: **99.48%**
708. **`usr/src/uts/common/os/pool.c`** -> AI Confidence: **99.48%**
709. **`usr/src/uts/common/os/procset.c`** -> AI Confidence: **99.48%**
710. **`usr/src/uts/common/os/turnstile.c`** -> AI Confidence: **99.48%**
711. **`usr/src/uts/common/syscall/corectl.c`** -> AI Confidence: **99.48%**
712. **`usr/src/uts/common/syscall/fcntl.c`** -> AI Confidence: **99.48%**
713. **`usr/src/uts/common/syscall/fdsync.c`** -> AI Confidence: **99.48%**
714. **`usr/src/uts/common/syscall/getcwd.c`** -> AI Confidence: **99.48%**
715. **`usr/src/uts/common/syscall/gid.c`** -> AI Confidence: **99.48%**
716. **`usr/src/uts/common/syscall/lseek.c`** -> AI Confidence: **99.48%**
717. **`usr/src/uts/common/syscall/lwpsys.c`** -> AI Confidence: **99.48%**
718. **`usr/src/uts/common/syscall/p_online.c`** -> AI Confidence: **99.48%**
719. **`usr/src/uts/common/syscall/pgrpsys.c`** -> AI Confidence: **99.48%**
720. **`usr/src/uts/common/syscall/poll.c`** -> AI Confidence: **99.48%**
721. **`usr/src/uts/common/syscall/processor_bind.c`** -> AI Confidence: **99.48%**
722. **`usr/src/uts/common/syscall/rctlsys.c`** -> AI Confidence: **99.48%**
723. **`usr/src/uts/common/syscall/uid.c`** -> AI Confidence: **99.48%**
724. **`usr/src/uts/common/vm/vm_pagelist.c`** -> AI Confidence: **99.48%**
725. **`usr/src/uts/common/vm/vm_usage.c`** -> AI Confidence: **99.48%**
726. **`usr/src/uts/i86pc/cpu/genuineintel/gintel_main.c`** -> AI Confidence: **99.48%**
727. **`usr/src/uts/i86pc/dboot/dboot_printf.c`** -> AI Confidence: **99.48%**
728. **`usr/src/uts/i86pc/dboot/dboot_startkern.c`** -> AI Confidence: **99.48%**
729. **`usr/src/uts/i86pc/io/acpi/acpidev/acpidev_memory.c`** -> AI Confidence: **99.48%**
730. **`usr/src/uts/i86pc/io/acpi/acpidev/acpidev_pci.c`** -> AI Confidence: **99.48%**
731. **`usr/src/uts/i86pc/io/acpi/acpidev/acpidev_resource.c`** -> AI Confidence: **99.48%**
732. **`usr/src/uts/i86pc/io/dr/dr_cpu.c`** -> AI Confidence: **99.48%**
733. **`usr/src/uts/i86pc/io/dr/dr_quiesce.c`** -> AI Confidence: **99.48%**
734. **`usr/src/uts/i86pc/io/pci/pci_tools.c`** -> AI Confidence: **99.48%**
735. **`usr/src/uts/i86pc/os/mlsetup.c`** -> AI Confidence: **99.48%**
736. **`usr/src/uts/i86pc/os/pci_cfgacc_x86.c`** -> AI Confidence: **99.48%**
737. **`usr/src/uts/i86pc/os/trap.c`** -> AI Confidence: **99.48%**
738. **`usr/src/uts/i86pc/vm/htable.c`** -> AI Confidence: **99.48%**
739. **`usr/src/uts/i86pc/vm/i86_mmu.c`** -> AI Confidence: **99.48%**
740. **`usr/src/uts/i86xpv/io/privcmd_hcall.c`** -> AI Confidence: **99.48%**
741. **`usr/src/uts/intel/amd64/krtld/doreloc.c`** -> AI Confidence: **99.48%**
742. **`usr/src/uts/intel/ia32/krtld/doreloc.c`** -> AI Confidence: **99.48%**
743. **`usr/src/uts/intel/io/imc/imc.c`** -> AI Confidence: **99.48%**
744. **`usr/src/uts/intel/io/intel_nb5000/nb_pci_cfg.c`** -> AI Confidence: **99.48%**
745. **`usr/src/uts/intel/io/intel_nhm/mem_addr.c`** -> AI Confidence: **99.48%**
746. **`usr/src/uts/intel/io/vmm/amd/vmcb.c`** -> AI Confidence: **99.48%**
747. **`usr/src/uts/intel/os/cpuid_subr.c`** -> AI Confidence: **99.48%**
748. **`usr/src/uts/intel/sys/acpi/platform/acenv.h`** -> AI Confidence: **99.48%**
749. **`usr/src/uts/intel/sys/acpi/platform/acfreebsd.h`** -> AI Confidence: **99.48%**
750. **`usr/src/uts/intel/sys/acpi/platform/acnetbsd.h`** -> AI Confidence: **99.48%**
751. **`usr/src/uts/intel/syscall/lwp_private.c`** -> AI Confidence: **99.48%**
752. **`usr/src/uts/sparc/dtrace/fasttrap_isa.c`** -> AI Confidence: **99.48%**
753. **`usr/src/uts/sparc/krtld/doreloc.c`** -> AI Confidence: **99.48%**
754. **`usr/src/uts/sparc/krtld/kobj_reloc.c`** -> AI Confidence: **99.48%**
755. **`usr/src/uts/sparc/v9/os/simulator.c`** -> AI Confidence: **99.48%**
756. **`usr/src/uts/sun4/io/px/px_intr.c`** -> AI Confidence: **99.48%**
757. **`usr/src/uts/sun4/os/trap.c`** -> AI Confidence: **99.48%**
758. **`usr/src/uts/sun4u/io/i2c/clients/max1617.c`** -> AI Confidence: **99.48%**
759. **`usr/src/uts/sun4u/io/iocache.c`** -> AI Confidence: **99.48%**
760. **`usr/src/uts/sun4u/io/isadma.c`** -> AI Confidence: **99.48%**
761. **`usr/src/uts/sun4u/io/pciex/pci_cfgacc_4u.c`** -> AI Confidence: **99.48%**
762. **`usr/src/uts/sun4u/io/px/px_tools_4u.c`** -> AI Confidence: **99.48%**
763. **`usr/src/uts/sun4u/io/sbd_cpu.c`** -> AI Confidence: **99.48%**
764. **`usr/src/uts/sun4u/ngdr/io/dr_cpu.c`** -> AI Confidence: **99.48%**
765. **`usr/src/uts/sun4u/ngdr/io/dr_mem.c`** -> AI Confidence: **99.48%**
766. **`usr/src/uts/sun4u/ngdr/io/dr_quiesce.c`** -> AI Confidence: **99.48%**
767. **`usr/src/uts/sun4u/opl/io/oplmsu/oplmsu_ioctl_lrp.c`** -> AI Confidence: **99.48%**
768. **`usr/src/uts/sun4u/opl/io/pcicmu/pcmu_util.c`** -> AI Confidence: **99.48%**
769. **`usr/src/uts/sun4u/os/plat_ecc_unum.c`** -> AI Confidence: **99.48%**
770. **`usr/src/uts/sun4u/os/ppage.c`** -> AI Confidence: **99.48%**
771. **`usr/src/uts/sun4u/sunfire/io/ac_stat.c`** -> AI Confidence: **99.48%**
772. **`usr/src/uts/sun4v/io/n2rng/n2rng_entp_setup.c`** -> AI Confidence: **99.48%**
773. **`usr/src/uts/sun4v/io/px/px_err.c`** -> AI Confidence: **99.48%**
774. **`usr/src/uts/sun4v/io/px/px_tools_4v.c`** -> AI Confidence: **99.48%**
775. **`usr/src/uts/sun4v/os/mpo.c`** -> AI Confidence: **99.48%**
776. **`usr/src/contrib/ast/src/cmd/INIT/iffe.sh`** -> AI Confidence: **99.48%**
777. **`usr/src/tools/scripts/webrev.sh`** -> AI Confidence: **99.48%**
778. **`usr/src/cmd/audio/audioconvert/parse.cc`** -> AI Confidence: **99.48%**
779. **`usr/src/cmd/audio/utilities/AudioGain.cc`** -> AI Confidence: **99.48%**
780. **`usr/src/cmd/make/bin/doname.cc`** -> AI Confidence: **99.48%**
781. **`usr/src/cmd/make/bin/main.cc`** -> AI Confidence: **99.48%**
782. **`usr/src/cmd/make/bin/read.cc`** -> AI Confidence: **99.48%**
783. **`usr/src/lib/sun_fc/common/FCHBA.cc`** -> AI Confidence: **99.48%**
784. **`usr/src/lib/sun_fc/common/FCHBANPIVPort.cc`** -> AI Confidence: **99.48%**
785. **`usr/src/lib/sun_fc/common/FCHBAPort.cc`** -> AI Confidence: **99.48%**
786. **`usr/src/lib/sun_fc/common/TgtFCHBA.cc`** -> AI Confidence: **99.48%**
787. **`usr/src/lib/sun_fc/common/TgtFCHBAPort.cc`** -> AI Confidence: **99.48%**
788. **`usr/src/lib/sun_fc/common/Trace.cc`** -> AI Confidence: **99.48%**
789. **`usr/src/uts/common/rpc/rpc.h`** -> AI Confidence: **99.44%**
790. **`usr/src/contrib/ast/src/lib/libast/dir/dirlib.h`** -> AI Confidence: **99.43%**
791. **`usr/src/contrib/mDNSResponder/mDNSCore/mDNSEmbeddedAPI.h`** -> AI Confidence: **99.43%**
792. **`usr/src/contrib/zlib/zutil.h`** -> AI Confidence: **99.43%**
793. **`usr/src/lib/iconv_modules/hi_IN/include/iscii.h`** -> AI Confidence: **99.43%**
794. **`usr/src/lib/libnsl/dial/stoa.c`** -> AI Confidence: **99.43%**
795. **`usr/src/test/libc-tests/tests/fnmatch.c`** -> AI Confidence: **99.43%**
796. **`usr/src/contrib/ast/src/lib/libast/include/ast_std.h`** -> AI Confidence: **99.42%**
797. **`usr/src/lib/libdwarf/common/dwarf_incl.h`** -> AI Confidence: **99.42%**
798. **`usr/src/lib/libldap5/include/ldap/portable.h`** -> AI Confidence: **99.42%**
799. **`usr/src/lib/libm/common/C/libm.h`** -> AI Confidence: **99.42%**
800. **`usr/src/lib/libresolv2/include/port_after.h`** -> AI Confidence: **99.42%**
801. **`usr/src/lib/udapl/udapl_tavor/include/dapl.h`** -> AI Confidence: **99.42%**
802. **`usr/src/boot/common/multiboot2.c`** -> AI Confidence: **99.39%**
803. **`usr/src/boot/efi/libefi/acpi.c`** -> AI Confidence: **99.39%**
804. **`usr/src/boot/efi/libefi/env.c`** -> AI Confidence: **99.39%**
805. **`usr/src/boot/i386/common/cons.c`** -> AI Confidence: **99.39%**
806. **`usr/src/boot/i386/isoboot/isoboot.c`** -> AI Confidence: **99.39%**
807. **`usr/src/boot/i386/libi386/biosacpi.c`** -> AI Confidence: **99.39%**
808. **`usr/src/cmd/abi/spectrans/parser/frontend.c`** -> AI Confidence: **99.39%**
809. **`usr/src/cmd/abi/spectrans/parser/main.c`** -> AI Confidence: **99.39%**
810. **`usr/src/cmd/abi/spectrans/spec2map/xlator.c`** -> AI Confidence: **99.39%**
811. **`usr/src/cmd/acct/lib/devtolin.c`** -> AI Confidence: **99.39%**
812. **`usr/src/cmd/acpi/common/adwalk.c`** -> AI Confidence: **99.39%**
813. **`usr/src/cmd/acpi/common/dmextern.c`** -> AI Confidence: **99.39%**
814. **`usr/src/cmd/acpi/common/dmswitch.c`** -> AI Confidence: **99.39%**
815. **`usr/src/cmd/acpihpd/notify.c`** -> AI Confidence: **99.39%**
816. **`usr/src/cmd/allocate/add_allocatable.c`** -> AI Confidence: **99.39%**
817. **`usr/src/cmd/allocate/allocate3.c`** -> AI Confidence: **99.39%**
818. **`usr/src/cmd/allocate/dminfo.c`** -> AI Confidence: **99.39%**
819. **`usr/src/cmd/audio/audioctl/audioctl.c`** -> AI Confidence: **99.39%**
820. **`usr/src/cmd/audio/utilities/device_ctl.c`** -> AI Confidence: **99.39%**
821. **`usr/src/cmd/awk/run.c`** -> AI Confidence: **99.39%**
822. **`usr/src/cmd/awk/tran.c`** -> AI Confidence: **99.39%**
823. **`usr/src/cmd/backup/dump/dumpmain.c`** -> AI Confidence: **99.39%**
824. **`usr/src/cmd/backup/restore/interactive.c`** -> AI Confidence: **99.39%**
825. **`usr/src/cmd/backup/restore/main.c`** -> AI Confidence: **99.39%**
826. **`usr/src/cmd/bhyve/common/pci_hostbridge.c`** -> AI Confidence: **99.39%**
827. **`usr/src/cmd/bhyve/common/usb_mouse.c`** -> AI Confidence: **99.39%**
828. **`usr/src/cmd/bnu/dial.c`** -> AI Confidence: **99.39%**
829. **`usr/src/cmd/bnu/uudecode.c`** -> AI Confidence: **99.39%**
830. **`usr/src/cmd/bnu/uuencode.c`** -> AI Confidence: **99.39%**
831. **`usr/src/cmd/boot/bootadm/bootadm_hyper.c`** -> AI Confidence: **99.39%**
832. **`usr/src/cmd/boot/bootadm/bootadm_upgrade.c`** -> AI Confidence: **99.39%**
833. **`usr/src/cmd/boot/symdef/symdef.c`** -> AI Confidence: **99.39%**
834. **`usr/src/cmd/captoinfo/otermcap.c`** -> AI Confidence: **99.39%**
835. **`usr/src/cmd/cat/cat.c`** -> AI Confidence: **99.39%**
836. **`usr/src/cmd/cdrw/copycd.c`** -> AI Confidence: **99.39%**
837. **`usr/src/cmd/cdrw/write_image.c`** -> AI Confidence: **99.39%**
838. **`usr/src/cmd/chgrp/chgrp.c`** -> AI Confidence: **99.39%**
839. **`usr/src/cmd/chown/chown.c`** -> AI Confidence: **99.39%**
840. **`usr/src/cmd/cmd-crypto/elfsign/elfsign.c`** -> AI Confidence: **99.39%**
841. **`usr/src/cmd/cmd-crypto/kmfcfg/uninstall.c`** -> AI Confidence: **99.39%**
842. **`usr/src/cmd/cmd-crypto/kmfcfg/util.c`** -> AI Confidence: **99.39%**
843. **`usr/src/cmd/cmd-crypto/pktool/export.c`** -> AI Confidence: **99.39%**
844. **`usr/src/cmd/cmd-crypto/pktool/gencert.c`** -> AI Confidence: **99.39%**
845. **`usr/src/cmd/cmd-crypto/pktool/gencsr.c`** -> AI Confidence: **99.39%**
846. **`usr/src/cmd/cmd-crypto/pktool/genkey.c`** -> AI Confidence: **99.39%**
847. **`usr/src/cmd/cmd-crypto/pktool/genkeypair.c`** -> AI Confidence: **99.39%**
848. **`usr/src/cmd/cmd-crypto/pktool/list.c`** -> AI Confidence: **99.39%**
849. **`usr/src/cmd/cmd-crypto/pktool/setpin.c`** -> AI Confidence: **99.39%**
850. **`usr/src/cmd/cmd-crypto/pktool/signcsr.c`** -> AI Confidence: **99.39%**
851. **`usr/src/cmd/cmd-inet/lib/ipmgmtd/ipmgmt_persist.c`** -> AI Confidence: **99.39%**
852. **`usr/src/cmd/cmd-inet/lib/nwamd/llp.c`** -> AI Confidence: **99.39%**
853. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/adopt.c`** -> AI Confidence: **99.39%**
854. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/agent.c`** -> AI Confidence: **99.39%**
855. **`usr/src/cmd/cmd-inet/usr.bin/ftp/domacro.c`** -> AI Confidence: **99.39%**
856. **`usr/src/cmd/cmd-inet/usr.bin/pppd/cbcp.c`** -> AI Confidence: **99.39%**
857. **`usr/src/cmd/cmd-inet/usr.bin/pppd/ipcp.c`** -> AI Confidence: **99.39%**
858. **`usr/src/cmd/cmd-inet/usr.bin/pppd/utils.c`** -> AI Confidence: **99.39%**
859. **`usr/src/cmd/cmd-inet/usr.lib/bridged/dlpi.c`** -> AI Confidence: **99.39%**
860. **`usr/src/cmd/cmd-inet/usr.lib/ilbd/ilbd_hc.c`** -> AI Confidence: **99.39%**
861. **`usr/src/cmd/cmd-inet/usr.lib/ilbd/ilbd_sg.c`** -> AI Confidence: **99.39%**
862. **`usr/src/cmd/cmd-inet/usr.lib/inetd/config.c`** -> AI Confidence: **99.39%**
863. **`usr/src/cmd/cmd-inet/usr.lib/inetd/repval.c`** -> AI Confidence: **99.39%**
864. **`usr/src/cmd/cmd-inet/usr.lib/pppoe/logging.c`** -> AI Confidence: **99.39%**
865. **`usr/src/cmd/cmd-inet/usr.sbin/ilbadm/ilbadm_import.c`** -> AI Confidence: **99.39%**
866. **`usr/src/cmd/cmd-inet/usr.sbin/in.rlogind.c`** -> AI Confidence: **99.39%**
867. **`usr/src/cmd/cmd-inet/usr.sbin/in.routed/main.c`** -> AI Confidence: **99.39%**
868. **`usr/src/cmd/cmd-inet/usr.sbin/inetconv/inetconv.c`** -> AI Confidence: **99.39%**
869. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_dhcp.c`** -> AI Confidence: **99.39%**
870. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_filter.c`** -> AI Confidence: **99.39%**
871. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_icmp.c`** -> AI Confidence: **99.39%**
872. **`usr/src/cmd/cmd-inet/usr.sbin/soconfig.c`** -> AI Confidence: **99.39%**
873. **`usr/src/cmd/compress/compress.c`** -> AI Confidence: **99.39%**
874. **`usr/src/cmd/csh/sh.tchar.c`** -> AI Confidence: **99.39%**
875. **`usr/src/cmd/ctfconvert/ctfconvert.c`** -> AI Confidence: **99.39%**
876. **`usr/src/cmd/ctfdump/ctfdump.c`** -> AI Confidence: **99.39%**
877. **`usr/src/cmd/ctrun/ctrun.c`** -> AI Confidence: **99.39%**
878. **`usr/src/cmd/devfsadm/devalloc.c`** -> AI Confidence: **99.39%**
879. **`usr/src/cmd/devmgmt/cmds/devreserv.c`** -> AI Confidence: **99.39%**
880. **`usr/src/cmd/devmgmt/cmds/putdev.c`** -> AI Confidence: **99.39%**
881. **`usr/src/cmd/dfs.cmds/sharemgr/commands.c`** -> AI Confidence: **99.39%**
882. **`usr/src/cmd/dis/dis_main.c`** -> AI Confidence: **99.39%**
883. **`usr/src/cmd/diskinfo/diskinfo.c`** -> AI Confidence: **99.39%**
884. **`usr/src/cmd/dladm/dladm.c`** -> AI Confidence: **99.39%**
885. **`usr/src/cmd/dlmgmtd/dlmgmt_db.c`** -> AI Confidence: **99.39%**
886. **`usr/src/cmd/dlmgmtd/dlmgmt_door.c`** -> AI Confidence: **99.39%**
887. **`usr/src/cmd/dtrace/dtrace.c`** -> AI Confidence: **99.39%**
888. **`usr/src/cmd/dtrace/test/tst/common/ip/msnc.c`** -> AI Confidence: **99.39%**
889. **`usr/src/cmd/du/du.c`** -> AI Confidence: **99.39%**
890. **`usr/src/cmd/dumpadm/main.c`** -> AI Confidence: **99.39%**
891. **`usr/src/cmd/expr/compile.c`** -> AI Confidence: **99.39%**
892. **`usr/src/cmd/expr/expr.c`** -> AI Confidence: **99.39%**
893. **`usr/src/cmd/fm/fmadm/common/faulty.c`** -> AI Confidence: **99.39%**
894. **`usr/src/cmd/fm/fmd/common/fmd_protocol.c`** -> AI Confidence: **99.39%**
895. **`usr/src/cmd/fm/fminject/common/inj_defn.c`** -> AI Confidence: **99.39%**
896. **`usr/src/cmd/fm/modules/common/cpumem-retire/cma_cpu.c`** -> AI Confidence: **99.39%**
897. **`usr/src/cmd/fm/modules/common/cpumem-retire/cma_page.c`** -> AI Confidence: **99.39%**
898. **`usr/src/cmd/fm/notify/smtp-notify/common/smtp-notify.c`** -> AI Confidence: **99.39%**
899. **`usr/src/cmd/fmt/fmt.c`** -> AI Confidence: **99.39%**
900. **`usr/src/cmd/format/io.c`** -> AI Confidence: **99.39%**
901. **`usr/src/cmd/fs.d/autofs/autod_autofs.c`** -> AI Confidence: **99.39%**
902. **`usr/src/cmd/fs.d/autofs/autod_lookup.c`** -> AI Confidence: **99.39%**
903. **`usr/src/cmd/fs.d/autofs/autod_nfs.c`** -> AI Confidence: **99.39%**
904. **`usr/src/cmd/fs.d/autofs/ns_files.c`** -> AI Confidence: **99.39%**
905. **`usr/src/cmd/fs.d/autofs/ns_fnutils.c`** -> AI Confidence: **99.39%**
906. **`usr/src/cmd/fs.d/bootfs/mount.c`** -> AI Confidence: **99.39%**
907. **`usr/src/cmd/fs.d/hsfs/labelit/labelit.c`** -> AI Confidence: **99.39%**
908. **`usr/src/cmd/fs.d/mount.c`** -> AI Confidence: **99.39%**
909. **`usr/src/cmd/fs.d/nfs/lib/nfslog_config.c`** -> AI Confidence: **99.39%**
910. **`usr/src/cmd/fs.d/nfs/mountd/mountd.c`** -> AI Confidence: **99.39%**
911. **`usr/src/cmd/fs.d/nfs/nfsref/nfsref.c`** -> AI Confidence: **99.39%**
912. **`usr/src/cmd/fs.d/nfs/nfsstat/nfsstat.c`** -> AI Confidence: **99.39%**
913. **`usr/src/cmd/fs.d/nfs/rp_basic/libnfs_basic.c`** -> AI Confidence: **99.39%**
914. **`usr/src/cmd/fs.d/pcfs/mount/mount.c`** -> AI Confidence: **99.39%**
915. **`usr/src/cmd/fs.d/smbclnt/smbiod/smbiod.c`** -> AI Confidence: **99.39%**
916. **`usr/src/cmd/fs.d/smbclnt/smbutil/login.c`** -> AI Confidence: **99.39%**
917. **`usr/src/cmd/fs.d/switchout.c`** -> AI Confidence: **99.39%**
918. **`usr/src/cmd/fs.d/ufs/fsck/pass1.c`** -> AI Confidence: **99.39%**
919. **`usr/src/cmd/fs.d/ufs/fsck/pass3b.c`** -> AI Confidence: **99.39%**
920. **`usr/src/cmd/fs.d/ufs/fssnap/fssnap.c`** -> AI Confidence: **99.39%**
921. **`usr/src/cmd/fs.d/ufs/quotaon/quotaon.c`** -> AI Confidence: **99.39%**
922. **`usr/src/cmd/fs.d/ufs/tunefs/tunefs.c`** -> AI Confidence: **99.39%**
923. **`usr/src/cmd/fstyp/fstyp.c`** -> AI Confidence: **99.39%**
924. **`usr/src/cmd/gcore/gcore.c`** -> AI Confidence: **99.39%**
925. **`usr/src/cmd/gencat/gencat.c`** -> AI Confidence: **99.39%**
926. **`usr/src/cmd/geniconvtbl/assemble.c`** -> AI Confidence: **99.39%**
927. **`usr/src/cmd/geniconvtbl/geniconvtbl.c`** -> AI Confidence: **99.39%**
928. **`usr/src/cmd/geniconvtbl/itm_util.c`** -> AI Confidence: **99.39%**
929. **`usr/src/cmd/genmsg/main.c`** -> AI Confidence: **99.39%**
930. **`usr/src/cmd/grep/grep.c`** -> AI Confidence: **99.39%**
931. **`usr/src/cmd/grpck/grpck.c`** -> AI Confidence: **99.39%**
932. **`usr/src/cmd/gss/gssd/gssdtest.c`** -> AI Confidence: **99.39%**
933. **`usr/src/cmd/hal/addons/storage/addon-storage.c`** -> AI Confidence: **99.39%**
934. **`usr/src/cmd/hal/hald/hald_dbus.c`** -> AI Confidence: **99.39%**
935. **`usr/src/cmd/hal/hald/ids.c`** -> AI Confidence: **99.39%**
936. **`usr/src/cmd/hal/hald/util.c`** -> AI Confidence: **99.39%**
937. **`usr/src/cmd/hal/probing/xkb/probe-xkb.c`** -> AI Confidence: **99.39%**
938. **`usr/src/cmd/hal/tools/hal-device.c`** -> AI Confidence: **99.39%**
939. **`usr/src/cmd/hal/tools/hal-is-caller-privileged.c`** -> AI Confidence: **99.39%**
940. **`usr/src/cmd/hal/tools/hal-storage-cleanup-all-mountpoints.c`** -> AI Confidence: **99.39%**
941. **`usr/src/cmd/hal/tools/hal-storage-cleanup-mountpoint.c`** -> AI Confidence: **99.39%**
942. **`usr/src/cmd/hal/tools/hal-storage-closetray.c`** -> AI Confidence: **99.39%**
943. **`usr/src/cmd/hal/tools/hal-storage-zpool.c`** -> AI Confidence: **99.39%**
944. **`usr/src/cmd/hal/tools/hal_set_property.c`** -> AI Confidence: **99.39%**
945. **`usr/src/cmd/hal/tools/lshal.c`** -> AI Confidence: **99.39%**
946. **`usr/src/cmd/hal/utils/acpi.c`** -> AI Confidence: **99.39%**
947. **`usr/src/cmd/head/head.c`** -> AI Confidence: **99.39%**
948. **`usr/src/cmd/iconv/iconv_main.c`** -> AI Confidence: **99.39%**
949. **`usr/src/cmd/idmap/idmap/namemaps.c`** -> AI Confidence: **99.39%**
950. **`usr/src/cmd/idmap/idmapd/idmap_config.c`** -> AI Confidence: **99.39%**
951. **`usr/src/cmd/intrstat/intrstat.c`** -> AI Confidence: **99.39%**
952. **`usr/src/cmd/ipf/lib/kmem.c`** -> AI Confidence: **99.39%**
953. **`usr/src/cmd/ipf/svc/ipfd.c`** -> AI Confidence: **99.39%**
954. **`usr/src/cmd/ipf/tools/ip_fil.c`** -> AI Confidence: **99.39%**
955. **`usr/src/cmd/ipf/tools/ipmon.c`** -> AI Confidence: **99.39%**
956. **`usr/src/cmd/isns/isnsd/qry.c`** -> AI Confidence: **99.39%**
957. **`usr/src/cmd/isns/isnsd/sched.c`** -> AI Confidence: **99.39%**
958. **`usr/src/cmd/keyserv/keylogin.c`** -> AI Confidence: **99.39%**
959. **`usr/src/cmd/krb5/kadmin/cli/keytab.c`** -> AI Confidence: **99.39%**
960. **`usr/src/cmd/krb5/kadmin/dbutil/kdb5_create.c`** -> AI Confidence: **99.39%**
961. **`usr/src/cmd/krb5/kadmin/kclient/ksmb.c`** -> AI Confidence: **99.39%**
962. **`usr/src/cmd/krb5/kadmin/ktutil/ktutil.c`** -> AI Confidence: **99.39%**
963. **`usr/src/cmd/krb5/kadmin/server/server_stubs.c`** -> AI Confidence: **99.39%**
964. **`usr/src/cmd/krb5/kwarn/kwarnd_proc.c`** -> AI Confidence: **99.39%**
965. **`usr/src/cmd/krb5/slave/kprop.c`** -> AI Confidence: **99.39%**
966. **`usr/src/cmd/ldap/common/dtest.c`** -> AI Confidence: **99.39%**
967. **`usr/src/cmd/ldap/common/ldaptool-sasl.c`** -> AI Confidence: **99.39%**
968. **`usr/src/cmd/ldap/ns_ldap/ldaplist.c`** -> AI Confidence: **99.39%**
969. **`usr/src/cmd/lofiadm/main.c`** -> AI Confidence: **99.39%**
970. **`usr/src/cmd/lp/cmd/lpadmin/fromclass.c`** -> AI Confidence: **99.39%**
971. **`usr/src/cmd/lp/cmd/lpfilter.c`** -> AI Confidence: **99.39%**
972. **`usr/src/cmd/lp/cmd/lpsched/exec.c`** -> AI Confidence: **99.39%**
973. **`usr/src/cmd/lp/cmd/lpsched/fncs.c`** -> AI Confidence: **99.39%**
974. **`usr/src/cmd/lp/lib/filters/insfilter.c`** -> AI Confidence: **99.39%**
975. **`usr/src/cmd/lp/lib/forms/getform.c`** -> AI Confidence: **99.39%**
976. **`usr/src/cmd/lp/lib/forms/wrform.c`** -> AI Confidence: **99.39%**
977. **`usr/src/cmd/lp/lib/lp/Syscalls.c`** -> AI Confidence: **99.39%**
978. **`usr/src/cmd/lp/lib/lp/getname.c`** -> AI Confidence: **99.39%**
979. **`usr/src/cmd/lp/lib/lp/isterminfo.c`** -> AI Confidence: **99.39%**
980. **`usr/src/cmd/lp/lib/msgs/mgetputm.c`** -> AI Confidence: **99.39%**
981. **`usr/src/cmd/lp/lib/papi/lpsched-msgs.c`** -> AI Confidence: **99.39%**
982. **`usr/src/cmd/lp/lib/papi/lpsched-printers.c`** -> AI Confidence: **99.39%**
983. **`usr/src/cmd/lp/lib/printers/getpentry.c`** -> AI Confidence: **99.39%**
984. **`usr/src/cmd/lp/lib/printers/getprinter.c`** -> AI Confidence: **99.39%**
985. **`usr/src/cmd/lp/lib/printers/putprinter.c`** -> AI Confidence: **99.39%**
986. **`usr/src/cmd/lp/lib/requests/putrequest.c`** -> AI Confidence: **99.39%**
987. **`usr/src/cmd/lp/model/lp.cat.c`** -> AI Confidence: **99.39%**
988. **`usr/src/cmd/ls/ls.c`** -> AI Confidence: **99.39%**
989. **`usr/src/cmd/luxadm/fchba.c`** -> AI Confidence: **99.39%**
990. **`usr/src/cmd/mandoc/eqn.c`** -> AI Confidence: **99.39%**
991. **`usr/src/cmd/mandoc/html.c`** -> AI Confidence: **99.39%**
992. **`usr/src/cmd/mandoc/man.c`** -> AI Confidence: **99.39%**
993. **`usr/src/cmd/mandoc/man_validate.c`** -> AI Confidence: **99.39%**
994. **`usr/src/cmd/mandoc/mdoc_html.c`** -> AI Confidence: **99.39%**
995. **`usr/src/cmd/mandoc/mdoc_man.c`** -> AI Confidence: **99.39%**
996. **`usr/src/cmd/mandoc/mdoc_validate.c`** -> AI Confidence: **99.39%**
997. **`usr/src/cmd/mandoc/tag.c`** -> AI Confidence: **99.39%**
998. **`usr/src/cmd/mandoc/tbl_data.c`** -> AI Confidence: **99.39%**
999. **`usr/src/cmd/mandoc/tbl_layout.c`** -> AI Confidence: **99.39%**
1000. **`usr/src/cmd/mdb/common/kmdb/kmdb_main.c`** -> AI Confidence: **99.39%**
1001. **`usr/src/cmd/mdb/common/mdb/mdb_err.c`** -> AI Confidence: **99.39%**
1002. **`usr/src/cmd/mdb/common/mdb/mdb_io.c`** -> AI Confidence: **99.39%**
1003. **`usr/src/cmd/mdb/common/mdb/mdb_main.c`** -> AI Confidence: **99.39%**
1004. **`usr/src/cmd/mdb/common/modules/arp/arp.c`** -> AI Confidence: **99.39%**
1005. **`usr/src/cmd/mdb/common/modules/crypto/common.c`** -> AI Confidence: **99.39%**
1006. **`usr/src/cmd/mdb/common/modules/crypto/impl.c`** -> AI Confidence: **99.39%**
1007. **`usr/src/cmd/mdb/common/modules/disk_label/disk_label.c`** -> AI Confidence: **99.39%**
1008. **`usr/src/cmd/mdb/common/modules/genunix/findstack.c`** -> AI Confidence: **99.39%**
1009. **`usr/src/cmd/mdb/common/modules/mpt_sas/mpt_sas.c`** -> AI Confidence: **99.39%**
1010. **`usr/src/cmd/mdb/intel/mdb/mdb_amd64util.c`** -> AI Confidence: **99.39%**
1011. **`usr/src/cmd/mdb/intel/mdb/mdb_ia32util.c`** -> AI Confidence: **99.39%**
1012. **`usr/src/cmd/mdb/intel/mdb/proc_amd64dep.c`** -> AI Confidence: **99.39%**
1013. **`usr/src/cmd/mdb/tools/setdynflag/common/setdynflag.c`** -> AI Confidence: **99.39%**
1014. **`usr/src/cmd/mkfile/mkfile.c`** -> AI Confidence: **99.39%**
1015. **`usr/src/cmd/modload/modunload.c`** -> AI Confidence: **99.39%**
1016. **`usr/src/cmd/modload/update_drv.c`** -> AI Confidence: **99.39%**
1017. **`usr/src/cmd/nvmeadm/nvmeadm_field.c`** -> AI Confidence: **99.39%**
1018. **`usr/src/cmd/oamuser/lib/vlogin.c`** -> AI Confidence: **99.39%**
1019. **`usr/src/cmd/oawk/lib.c`** -> AI Confidence: **99.39%**
1020. **`usr/src/cmd/oawk/main.c`** -> AI Confidence: **99.39%**
1021. **`usr/src/cmd/oplhpd/scf_notify.c`** -> AI Confidence: **99.39%**
1022. **`usr/src/cmd/pcidr/pcidr_common.c`** -> AI Confidence: **99.39%**
1023. **`usr/src/cmd/pcieadm/pcieadm_devs.c`** -> AI Confidence: **99.39%**
1024. **`usr/src/cmd/pcitool/pcitool_ui.c`** -> AI Confidence: **99.39%**
1025. **`usr/src/cmd/plimit/plimit.c`** -> AI Confidence: **99.39%**
1026. **`usr/src/cmd/pools/poolbind/poolbind.c`** -> AI Confidence: **99.39%**
1027. **`usr/src/cmd/pools/poolstat/poolstat.c`** -> AI Confidence: **99.39%**
1028. **`usr/src/cmd/pools/poolstat/sa_kstat.c`** -> AI Confidence: **99.39%**
1029. **`usr/src/cmd/ppgsz/ppgsz.c`** -> AI Confidence: **99.39%**
1030. **`usr/src/cmd/praudit/main.c`** -> AI Confidence: **99.39%**
1031. **`usr/src/cmd/prctl/prctl.c`** -> AI Confidence: **99.39%**
1032. **`usr/src/cmd/print/bsd-sysv-commands/lprm.c`** -> AI Confidence: **99.39%**
1033. **`usr/src/cmd/print/bsd-sysv-commands/lpstat.c`** -> AI Confidence: **99.39%**
1034. **`usr/src/cmd/printf/printf.c`** -> AI Confidence: **99.39%**
1035. **`usr/src/cmd/priocntl/fsspriocntl.c`** -> AI Confidence: **99.39%**
1036. **`usr/src/cmd/priocntl/iapriocntl.c`** -> AI Confidence: **99.39%**
1037. **`usr/src/cmd/priocntl/rtpriocntl.c`** -> AI Confidence: **99.39%**
1038. **`usr/src/cmd/priocntl/subr.c`** -> AI Confidence: **99.39%**
1039. **`usr/src/cmd/priocntl/tspriocntl.c`** -> AI Confidence: **99.39%**
1040. **`usr/src/cmd/psrinfo/psrinfo.c`** -> AI Confidence: **99.39%**
1041. **`usr/src/cmd/ptools/ppriv/ppriv.c`** -> AI Confidence: **99.39%**
1042. **`usr/src/cmd/ptools/psecflags/psecflags.c`** -> AI Confidence: **99.39%**
1043. **`usr/src/cmd/pwd/pwd.c`** -> AI Confidence: **99.39%**
1044. **`usr/src/cmd/raidz_test/raidz_test.c`** -> AI Confidence: **99.39%**
1045. **`usr/src/cmd/rcap/rcapadm/rcapadm.c`** -> AI Confidence: **99.39%**
1046. **`usr/src/cmd/rcap/rcapd/rcapd_rfd.c`** -> AI Confidence: **99.39%**
1047. **`usr/src/cmd/rdmsr/rdmsr.c`** -> AI Confidence: **99.39%**
1048. **`usr/src/cmd/rmmount/rmmount.c`** -> AI Confidence: **99.39%**
1049. **`usr/src/cmd/rmvolmgr/rmm_common.c`** -> AI Confidence: **99.39%**
1050. **`usr/src/cmd/rpcbind/check_bound.c`** -> AI Confidence: **99.39%**
1051. **`usr/src/cmd/rpcgen/rpc_scan.c`** -> AI Confidence: **99.39%**
1052. **`usr/src/cmd/sa/timex.c`** -> AI Confidence: **99.39%**
1053. **`usr/src/cmd/saf/misc.c`** -> AI Confidence: **99.39%**
1054. **`usr/src/cmd/saf/sacadm.c`** -> AI Confidence: **99.39%**
1055. **`usr/src/cmd/sed/process.c`** -> AI Confidence: **99.39%**
1056. **`usr/src/cmd/sendmail/db/btree/bt_search.c`** -> AI Confidence: **99.39%**
1057. **`usr/src/cmd/sendmail/db/btree/bt_split.c`** -> AI Confidence: **99.39%**
1058. **`usr/src/cmd/sendmail/db/btree/bt_stat.c`** -> AI Confidence: **99.39%**
1059. **`usr/src/cmd/sendmail/db/db/db_iface.c`** -> AI Confidence: **99.39%**
1060. **`usr/src/cmd/sendmail/db/db/db_ret.c`** -> AI Confidence: **99.39%**
1061. **`usr/src/cmd/sendmail/db/hash/hash_dup.c`** -> AI Confidence: **99.39%**
1062. **`usr/src/cmd/sendmail/db/hash/hash_page.c`** -> AI Confidence: **99.39%**
1063. **`usr/src/cmd/sendmail/db/lock/lock.c`** -> AI Confidence: **99.39%**
1064. **`usr/src/cmd/sendmail/db/mp/mp_fget.c`** -> AI Confidence: **99.39%**
1065. **`usr/src/cmd/sendmail/db/mp/mp_fput.c`** -> AI Confidence: **99.39%**
1066. **`usr/src/cmd/sendmail/db/mp/mp_region.c`** -> AI Confidence: **99.39%**
1067. **`usr/src/cmd/sendmail/db/os/os_map.c`** -> AI Confidence: **99.39%**
1068. **`usr/src/cmd/sendmail/db/os/os_open.c`** -> AI Confidence: **99.39%**
1069. **`usr/src/cmd/sendmail/db/os/os_tmpdir.c`** -> AI Confidence: **99.39%**
1070. **`usr/src/cmd/sendmail/libsm/cf.c`** -> AI Confidence: **99.39%**
1071. **`usr/src/cmd/sendmail/libsm/exc.c`** -> AI Confidence: **99.39%**
1072. **`usr/src/cmd/sendmail/libsm/fflush.c`** -> AI Confidence: **99.39%**
1073. **`usr/src/cmd/sendmail/libsm/ldap.c`** -> AI Confidence: **99.39%**
1074. **`usr/src/cmd/sendmail/libsm/makebuf.c`** -> AI Confidence: **99.39%**
1075. **`usr/src/cmd/sendmail/libsm/refill.c`** -> AI Confidence: **99.39%**
1076. **`usr/src/cmd/sendmail/libsm/t-qic.c`** -> AI Confidence: **99.39%**
1077. **`usr/src/cmd/sendmail/libsm/vfprintf.c`** -> AI Confidence: **99.39%**
1078. **`usr/src/cmd/sendmail/src/conf.c`** -> AI Confidence: **99.39%**
1079. **`usr/src/cmd/sendmail/src/map.c`** -> AI Confidence: **99.39%**
1080. **`usr/src/cmd/sendmail/src/milter.c`** -> AI Confidence: **99.39%**
1081. **`usr/src/cmd/sendmail/src/srvrsmtp.c`** -> AI Confidence: **99.39%**
1082. **`usr/src/cmd/sendmail/src/tls.c`** -> AI Confidence: **99.39%**
1083. **`usr/src/cmd/sendmail/util/editmap.c`** -> AI Confidence: **99.39%**
1084. **`usr/src/cmd/sendmail/util/makemap.c`** -> AI Confidence: **99.39%**
1085. **`usr/src/cmd/setfacl/setfacl.c`** -> AI Confidence: **99.39%**
1086. **`usr/src/cmd/sgs/crle/common/crle.c`** -> AI Confidence: **99.39%**
1087. **`usr/src/cmd/sgs/crle/common/util.c`** -> AI Confidence: **99.39%**
1088. **`usr/src/cmd/sgs/elfdump/common/elfdump.c`** -> AI Confidence: **99.39%**
1089. **`usr/src/cmd/sgs/elfdump/common/fake_shdr.c`** -> AI Confidence: **99.39%**
1090. **`usr/src/cmd/sgs/elfedit/common/util_machelf.c`** -> AI Confidence: **99.39%**
1091. **`usr/src/cmd/sgs/elfedit/modules/common/dyn.c`** -> AI Confidence: **99.39%**
1092. **`usr/src/cmd/sgs/elfedit/modules/common/shdr.c`** -> AI Confidence: **99.39%**
1093. **`usr/src/cmd/sgs/elfedit/modules/common/str.c`** -> AI Confidence: **99.39%**
1094. **`usr/src/cmd/sgs/elfedit/modules/common/sym.c`** -> AI Confidence: **99.39%**
1095. **`usr/src/cmd/sgs/elfedit/modules/common/syminfo.c`** -> AI Confidence: **99.39%**
1096. **`usr/src/cmd/sgs/error/common/errormain.c`** -> AI Confidence: **99.39%**
1097. **`usr/src/cmd/sgs/ldprof/common/profile.c`** -> AI Confidence: **99.39%**
1098. **`usr/src/cmd/sgs/libelf/common/clscook.c`** -> AI Confidence: **99.39%**
1099. **`usr/src/cmd/sgs/libld/common/files.c`** -> AI Confidence: **99.39%**
1100. **`usr/src/cmd/sgs/libld/common/libs.c`** -> AI Confidence: **99.39%**
1101. **`usr/src/cmd/sgs/libld/common/machrel.amd.c`** -> AI Confidence: **99.39%**
1102. **`usr/src/cmd/sgs/libld/common/machrel.intel.c`** -> AI Confidence: **99.39%**
1103. **`usr/src/cmd/sgs/libld/common/machrel.sparc.c`** -> AI Confidence: **99.39%**
1104. **`usr/src/cmd/sgs/libld/common/sections.c`** -> AI Confidence: **99.39%**
1105. **`usr/src/cmd/sgs/libld/common/unwind.c`** -> AI Confidence: **99.39%**
1106. **`usr/src/cmd/sgs/liblddbg/common/debug.c`** -> AI Confidence: **99.39%**
1107. **`usr/src/cmd/sgs/pvs/common/pvs.c`** -> AI Confidence: **99.39%**
1108. **`usr/src/cmd/sgs/rtld/common/analyze.c`** -> AI Confidence: **99.39%**
1109. **`usr/src/cmd/sgs/rtld/common/audit.c`** -> AI Confidence: **99.39%**
1110. **`usr/src/cmd/sgs/rtld/common/cap.c`** -> AI Confidence: **99.39%**
1111. **`usr/src/cmd/sgs/rtld/common/dlfcns.c`** -> AI Confidence: **99.39%**
1112. **`usr/src/cmd/sgs/rtld/common/object.c`** -> AI Confidence: **99.39%**
1113. **`usr/src/cmd/sgs/rtld/common/paths.c`** -> AI Confidence: **99.39%**
1114. **`usr/src/cmd/sgs/rtld/common/tsort.c`** -> AI Confidence: **99.39%**
1115. **`usr/src/cmd/sgs/rtld/sparc/sparc_elf.c`** -> AI Confidence: **99.39%**
1116. **`usr/src/cmd/sh/jobs.c`** -> AI Confidence: **99.39%**
1117. **`usr/src/cmd/sleep/sleep.c`** -> AI Confidence: **99.39%**
1118. **`usr/src/cmd/smbios/smbios.c`** -> AI Confidence: **99.39%**
1119. **`usr/src/cmd/smbsrv/test-msgbuf/test_main.c`** -> AI Confidence: **99.39%**
1120. **`usr/src/cmd/spell/spellprog.c`** -> AI Confidence: **99.39%**
1121. **`usr/src/cmd/stat/common/dsr.c`** -> AI Confidence: **99.39%**
1122. **`usr/src/cmd/svc/mfstscan/mfstscan.c`** -> AI Confidence: **99.39%**
1123. **`usr/src/cmd/svc/startd/expand.c`** -> AI Confidence: **99.39%**
1124. **`usr/src/cmd/svc/startd/file.c`** -> AI Confidence: **99.39%**
1125. **`usr/src/cmd/svc/startd/fork.c`** -> AI Confidence: **99.39%**
1126. **`usr/src/cmd/svc/startd/graph.c`** -> AI Confidence: **99.39%**
1127. **`usr/src/cmd/svc/startd/restarter.c`** -> AI Confidence: **99.39%**
1128. **`usr/src/cmd/svc/startd/specials.c`** -> AI Confidence: **99.39%**
1129. **`usr/src/cmd/svc/svccfg/svccfg_engine.c`** -> AI Confidence: **99.39%**
1130. **`usr/src/cmd/svc/svccfg/svccfg_xml.c`** -> AI Confidence: **99.39%**
1131. **`usr/src/cmd/svc/svcs/svcs.c`** -> AI Confidence: **99.39%**
1132. **`usr/src/cmd/svr4pkg/installf/main.c`** -> AI Confidence: **99.39%**
1133. **`usr/src/cmd/svr4pkg/libinst/depchk.c`** -> AI Confidence: **99.39%**
1134. **`usr/src/cmd/svr4pkg/libinst/pkgdbmerg.c`** -> AI Confidence: **99.39%**
1135. **`usr/src/cmd/svr4pkg/libinst/putparam.c`** -> AI Confidence: **99.39%**
1136. **`usr/src/cmd/svr4pkg/libinst/sml.c`** -> AI Confidence: **99.39%**
1137. **`usr/src/cmd/svr4pkg/pkgadd/main.c`** -> AI Confidence: **99.39%**
1138. **`usr/src/cmd/svr4pkg/pkgadm/lock.c`** -> AI Confidence: **99.39%**
1139. **`usr/src/cmd/svr4pkg/pkgchk/checkmap.c`** -> AI Confidence: **99.39%**
1140. **`usr/src/cmd/svr4pkg/pkgchk/ckentry.c`** -> AI Confidence: **99.39%**
1141. **`usr/src/cmd/svr4pkg/pkginstall/dockspace.c`** -> AI Confidence: **99.39%**
1142. **`usr/src/cmd/svr4pkg/pkginstall/merginfo.c`** -> AI Confidence: **99.39%**
1143. **`usr/src/cmd/svr4pkg/pkgrm/check.c`** -> AI Confidence: **99.39%**
1144. **`usr/src/cmd/svr4pkg/pkgrm/main.c`** -> AI Confidence: **99.39%**
1145. **`usr/src/cmd/sysdef/sysdef.c`** -> AI Confidence: **99.39%**
1146. **`usr/src/cmd/syseventd/modules/sysevent_conf_mod/sysevent_conf_mod.c`** -> AI Confidence: **99.39%**
1147. **`usr/src/cmd/tail/forward.c`** -> AI Confidence: **99.39%**
1148. **`usr/src/cmd/tail/reverse.c`** -> AI Confidence: **99.39%**
1149. **`usr/src/cmd/tcpd/inetcf.c`** -> AI Confidence: **99.39%**
1150. **`usr/src/cmd/tcpd/tcpdmatch.c`** -> AI Confidence: **99.39%**
1151. **`usr/src/cmd/th_tools/th_define.c`** -> AI Confidence: **99.39%**
1152. **`usr/src/cmd/tic/tic_parse.c`** -> AI Confidence: **99.39%**
1153. **`usr/src/cmd/tic/tic_read.c`** -> AI Confidence: **99.39%**
1154. **`usr/src/cmd/tip/remcap.c`** -> AI Confidence: **99.39%**
1155. **`usr/src/cmd/tr/tr.c`** -> AI Confidence: **99.39%**
1156. **`usr/src/cmd/troff/n2.c`** -> AI Confidence: **99.39%**
1157. **`usr/src/cmd/truss/expound.c`** -> AI Confidence: **99.39%**
1158. **`usr/src/cmd/truss/procset.c`** -> AI Confidence: **99.39%**
1159. **`usr/src/cmd/tsol/updatehome/updatehome.c`** -> AI Confidence: **99.39%**
1160. **`usr/src/cmd/ttymon/sttyparse.c`** -> AI Confidence: **99.39%**
1161. **`usr/src/cmd/ttymon/tmpmtab.c`** -> AI Confidence: **99.39%**
1162. **`usr/src/cmd/ttymon/tmsac.c`** -> AI Confidence: **99.39%**
1163. **`usr/src/cmd/ttymon/tmttydefs.c`** -> AI Confidence: **99.39%**
1164. **`usr/src/cmd/ul/ul.c`** -> AI Confidence: **99.39%**
1165. **`usr/src/cmd/valtools/ckdate.c`** -> AI Confidence: **99.39%**
1166. **`usr/src/cmd/valtools/ckgid.c`** -> AI Confidence: **99.39%**
1167. **`usr/src/cmd/valtools/ckint.c`** -> AI Confidence: **99.39%**
1168. **`usr/src/cmd/valtools/ckitem.c`** -> AI Confidence: **99.39%**
1169. **`usr/src/cmd/valtools/ckkeywd.c`** -> AI Confidence: **99.39%**
1170. **`usr/src/cmd/valtools/ckpath.c`** -> AI Confidence: **99.39%**
1171. **`usr/src/cmd/valtools/ckrange.c`** -> AI Confidence: **99.39%**
1172. **`usr/src/cmd/valtools/ckstr.c`** -> AI Confidence: **99.39%**
1173. **`usr/src/cmd/valtools/cktime.c`** -> AI Confidence: **99.39%**
1174. **`usr/src/cmd/valtools/ckuid.c`** -> AI Confidence: **99.39%**
1175. **`usr/src/cmd/valtools/ckyorn.c`** -> AI Confidence: **99.39%**
1176. **`usr/src/cmd/varpd/varpd.c`** -> AI Confidence: **99.39%**
1177. **`usr/src/cmd/vi/misc/ctags.c`** -> AI Confidence: **99.39%**
1178. **`usr/src/cmd/vi/port/ex_io.c`** -> AI Confidence: **99.39%**
1179. **`usr/src/cmd/volcheck/volcheck.c`** -> AI Confidence: **99.39%**
1180. **`usr/src/cmd/vrrpadm/vrrpadm.c`** -> AI Confidence: **99.39%**
1181. **`usr/src/cmd/wracct/wracct.c`** -> AI Confidence: **99.39%**
1182. **`usr/src/cmd/ypcmd/mkalias.c`** -> AI Confidence: **99.39%**
1183. **`usr/src/cmd/zic/private.h`** -> AI Confidence: **99.39%**
1184. **`usr/src/cmd/zoneadmd/zcons.c`** -> AI Confidence: **99.39%**
1185. **`usr/src/common/bignum/bignumimpl.c`** -> AI Confidence: **99.39%**
1186. **`usr/src/common/bootbanner/bootbanner.c`** -> AI Confidence: **99.39%**
1187. **`usr/src/common/crypto/modes/ecb.c`** -> AI Confidence: **99.39%**
1188. **`usr/src/common/crypto/rsa/rsa_impl.c`** -> AI Confidence: **99.39%**
1189. **`usr/src/common/ficl/main.c`** -> AI Confidence: **99.39%**
1190. **`usr/src/common/lz4/lz4.c`** -> AI Confidence: **99.39%**
1191. **`usr/src/common/smbclnt/smbfs_ntacl.c`** -> AI Confidence: **99.39%**
1192. **`usr/src/common/smbsrv/smb_match.c`** -> AI Confidence: **99.39%**
1193. **`usr/src/common/smbsrv/smb_msgbuf.c`** -> AI Confidence: **99.39%**
1194. **`usr/src/common/smbsrv/smb_utf8.c`** -> AI Confidence: **99.39%**
1195. **`usr/src/common/tsol/stol.c`** -> AI Confidence: **99.39%**
1196. **`usr/src/common/unicode/uconv.c`** -> AI Confidence: **99.39%**
1197. **`usr/src/common/zfs/zfs_namecheck.c`** -> AI Confidence: **99.39%**
1198. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/shiocmd_solaris.c`** -> AI Confidence: **99.39%**
1199. **`usr/src/contrib/ast/src/cmd/ksh93/data/variables.c`** -> AI Confidence: **99.39%**
1200. **`usr/src/contrib/ast/src/cmd/ksh93/edit/history.c`** -> AI Confidence: **99.39%**
1201. **`usr/src/contrib/ast/src/cmd/ksh93/sh/init.c`** -> AI Confidence: **99.39%**
1202. **`usr/src/contrib/ast/src/cmd/ksh93/sh/io.c`** -> AI Confidence: **99.39%**
1203. **`usr/src/contrib/ast/src/cmd/ksh93/sh/path.c`** -> AI Confidence: **99.39%**
1204. **`usr/src/contrib/ast/src/cmd/ksh93/sh/subshell.c`** -> AI Confidence: **99.39%**
1205. **`usr/src/contrib/ast/src/lib/libast/comp/syslog.c`** -> AI Confidence: **99.39%**
1206. **`usr/src/contrib/ast/src/lib/libast/uwin/rcmd.c`** -> AI Confidence: **99.39%**
1207. **`usr/src/contrib/ast/src/lib/libast/vmalloc/vmmopen.c`** -> AI Confidence: **99.39%**
1208. **`usr/src/contrib/zlib/gzguts.h`** -> AI Confidence: **99.39%**
1209. **`usr/src/grub/grub-0.97/lib/device.c`** -> AI Confidence: **99.39%**
1210. **`usr/src/grub/grub-0.97/stage2/builtins.c`** -> AI Confidence: **99.39%**
1211. **`usr/src/head/iso/wchar_iso.h`** -> AI Confidence: **99.39%**
1212. **`usr/src/head/signal.h`** -> AI Confidence: **99.39%**
1213. **`usr/src/lib/auditd_plugins/remote/audit_remote.c`** -> AI Confidence: **99.39%**
1214. **`usr/src/lib/brand/solaris10/s10_brand/common/s10_brand.c`** -> AI Confidence: **99.39%**
1215. **`usr/src/lib/cfgadm_plugins/ac/common/mema_prom.c`** -> AI Confidence: **99.39%**
1216. **`usr/src/lib/cfgadm_plugins/sbd/common/ap_msg.c`** -> AI Confidence: **99.39%**
1217. **`usr/src/lib/cfgadm_plugins/sbd/common/ap_rcm.c`** -> AI Confidence: **99.39%**
1218. **`usr/src/lib/cfgadm_plugins/sbd/common/ap_sbd.c`** -> AI Confidence: **99.39%**
1219. **`usr/src/lib/fm/libdiskstatus/common/libdiskstatus.c`** -> AI Confidence: **99.39%**
1220. **`usr/src/lib/fm/libfmd_log/common/fmd_log.c`** -> AI Confidence: **99.39%**
1221. **`usr/src/lib/fm/topo/libtopo/common/sw.c`** -> AI Confidence: **99.39%**
1222. **`usr/src/lib/fm/topo/libtopo/common/topo_digraph_xml.c`** -> AI Confidence: **99.39%**
1223. **`usr/src/lib/fm/topo/libtopo/common/topo_method.c`** -> AI Confidence: **99.39%**
1224. **`usr/src/lib/fm/topo/libtopo/common/topo_subr.c`** -> AI Confidence: **99.39%**
1225. **`usr/src/lib/fm/topo/libtopo/common/topo_xml.c`** -> AI Confidence: **99.39%**
1226. **`usr/src/lib/fm/topo/modules/common/disk/disk_nvme.c`** -> AI Confidence: **99.39%**
1227. **`usr/src/lib/fm/topo/modules/common/fac_prov_ahci/fac_prov_ahci.c`** -> AI Confidence: **99.39%**
1228. **`usr/src/lib/fm/topo/modules/common/shared/topo_sensor.c`** -> AI Confidence: **99.39%**
1229. **`usr/src/lib/fm/topo/modules/common/usb/topo_usb_metadata.c`** -> AI Confidence: **99.39%**
1230. **`usr/src/lib/fm/topo/modules/i86pc/x86pi/x86pi_bboard.c`** -> AI Confidence: **99.39%**
1231. **`usr/src/lib/fm/topo/modules/i86pc/x86pi/x86pi_subr.c`** -> AI Confidence: **99.39%**
1232. **`usr/src/lib/gss_mechs/mech_krb5/et/com_err.c`** -> AI Confidence: **99.39%**
1233. **`usr/src/lib/gss_mechs/mech_krb5/krb5/os/sendto_kdc.c`** -> AI Confidence: **99.39%**
1234. **`usr/src/lib/gss_mechs/mech_krb5/krb5/rcache/rc_io.c`** -> AI Confidence: **99.39%**
1235. **`usr/src/lib/gss_mechs/mech_krb5/mech/init_sec_context.c`** -> AI Confidence: **99.39%**
1236. **`usr/src/lib/gss_mechs/mech_krb5/mech/oid_ops.c`** -> AI Confidence: **99.39%**
1237. **`usr/src/lib/gss_mechs/mech_spnego/mech/spnego_mech.c`** -> AI Confidence: **99.39%**
1238. **`usr/src/lib/hbaapi/common/HBAAPILIB-sun.c`** -> AI Confidence: **99.39%**
1239. **`usr/src/lib/iconv_modules/ja/common/Unicode_TO_PCK.c`** -> AI Confidence: **99.39%**
1240. **`usr/src/lib/iconv_modules/ko/common/comp_to_pack.c`** -> AI Confidence: **99.39%**
1241. **`usr/src/lib/iconv_modules/ko/common/nbyte_to_euc.c`** -> AI Confidence: **99.39%**
1242. **`usr/src/lib/iconv_modules/ko/common/utf_to_iso_main.c`** -> AI Confidence: **99.39%**
1243. **`usr/src/lib/iconv_modules/vi/common/tcvn%UCS-2.c`** -> AI Confidence: **99.39%**
1244. **`usr/src/lib/iconv_modules/vi/common/tcvn%UTF-8.c`** -> AI Confidence: **99.39%**
1245. **`usr/src/lib/iconv_modules/zh/common/UTF-8%zh_CN.iso2022-CN.c`** -> AI Confidence: **99.39%**
1246. **`usr/src/lib/iconv_modules/zh/common/zh_CN.gbk%UTF-8.c`** -> AI Confidence: **99.39%**
1247. **`usr/src/lib/iconv_modules/zh/common/zh_CN.gbk%zh_CN.iso2022-CN.c`** -> AI Confidence: **99.39%**
1248. **`usr/src/lib/iconv_modules/zh/common/zh_CN.iso2022-7%UTF-8.c`** -> AI Confidence: **99.39%**
1249. **`usr/src/lib/iconv_modules/zh/common/zh_CN.iso2022-CN%UTF-8.c`** -> AI Confidence: **99.39%**
1250. **`usr/src/lib/iconv_modules/zh/common/zh_CN.iso2022-CN%zh_CN.gbk.c`** -> AI Confidence: **99.39%**
1251. **`usr/src/lib/krb5/kdb/kdb5.c`** -> AI Confidence: **99.39%**
1252. **`usr/src/lib/krb5/plugins/kdb/db2/kdb_db2.c`** -> AI Confidence: **99.39%**
1253. **`usr/src/lib/krb5/plugins/kdb/db2/libdb2/btree/bt_seq.c`** -> AI Confidence: **99.39%**
1254. **`usr/src/lib/krb5/plugins/kdb/db2/libdb2/recno/rec_get.c`** -> AI Confidence: **99.39%**
1255. **`usr/src/lib/krb5/plugins/preauth/pkinit/pkinit_crypto_openssl.c`** -> AI Confidence: **99.39%**
1256. **`usr/src/lib/krb5/plugins/preauth/pkinit/pkinit_matching.c`** -> AI Confidence: **99.39%**
1257. **`usr/src/lib/libadm/common/ckdate.c`** -> AI Confidence: **99.39%**
1258. **`usr/src/lib/libadm/common/cktime.c`** -> AI Confidence: **99.39%**
1259. **`usr/src/lib/libadm/common/devattr.c`** -> AI Confidence: **99.39%**
1260. **`usr/src/lib/libadm/common/pkgparam.c`** -> AI Confidence: **99.39%**
1261. **`usr/src/lib/libadm/common/putdev.c`** -> AI Confidence: **99.39%**
1262. **`usr/src/lib/libadutils/common/srv_query.c`** -> AI Confidence: **99.39%**
1263. **`usr/src/lib/libbe/common/be_activate.c`** -> AI Confidence: **99.39%**
1264. **`usr/src/lib/libbe/common/be_rename.c`** -> AI Confidence: **99.39%**
1265. **`usr/src/lib/libbsm/common/audit_crontab.c`** -> AI Confidence: **99.39%**
1266. **`usr/src/lib/libc/amd64/gen/makectxt.c`** -> AI Confidence: **99.39%**
1267. **`usr/src/lib/libc/port/aio/aio.c`** -> AI Confidence: **99.39%**
1268. **`usr/src/lib/libc/port/aio/posix_aio.c`** -> AI Confidence: **99.39%**
1269. **`usr/src/lib/libc/port/gen/catopen.c`** -> AI Confidence: **99.39%**
1270. **`usr/src/lib/libc/port/gen/flock.c`** -> AI Confidence: **99.39%**
1271. **`usr/src/lib/libc/port/gen/ftw.c`** -> AI Confidence: **99.39%**
1272. **`usr/src/lib/libc/port/gen/getopt_long.c`** -> AI Confidence: **99.39%**
1273. **`usr/src/lib/libc/port/gen/getpw.c`** -> AI Confidence: **99.39%**
1274. **`usr/src/lib/libc/port/gen/getvfsent.c`** -> AI Confidence: **99.39%**
1275. **`usr/src/lib/libc/port/gen/l64a.c`** -> AI Confidence: **99.39%**
1276. **`usr/src/lib/libc/port/gen/ndbm.c`** -> AI Confidence: **99.39%**
1277. **`usr/src/lib/libc/port/gen/nftw.c`** -> AI Confidence: **99.39%**
1278. **`usr/src/lib/libc/port/i18n/wsprintf.c`** -> AI Confidence: **99.39%**
1279. **`usr/src/lib/libc/port/inet/inet_ntop.c`** -> AI Confidence: **99.39%**
1280. **`usr/src/lib/libc/port/locale/euc.c`** -> AI Confidence: **99.39%**
1281. **`usr/src/lib/libc/port/locale/fgetws.c`** -> AI Confidence: **99.39%**
1282. **`usr/src/lib/libc/port/locale/strcasestr.c`** -> AI Confidence: **99.39%**
1283. **`usr/src/lib/libc/port/locale/strptime.c`** -> AI Confidence: **99.39%**
1284. **`usr/src/lib/libc/port/locale/strxfrm.c`** -> AI Confidence: **99.39%**
1285. **`usr/src/lib/libc/port/regex/glob.c`** -> AI Confidence: **99.39%**
1286. **`usr/src/lib/libc/port/regex/regex.c`** -> AI Confidence: **99.39%**
1287. **`usr/src/lib/libc/port/regex/wordexp.c`** -> AI Confidence: **99.39%**
1288. **`usr/src/lib/libc/port/stdio/_flsbuf.c`** -> AI Confidence: **99.39%**
1289. **`usr/src/lib/libc/port/stdio/fdopen.c`** -> AI Confidence: **99.39%**
1290. **`usr/src/lib/libc/port/stdio/fread.c`** -> AI Confidence: **99.39%**
1291. **`usr/src/lib/libc/port/stdio/fseeko.c`** -> AI Confidence: **99.39%**
1292. **`usr/src/lib/libc/port/stdio/ftell.c`** -> AI Confidence: **99.39%**
1293. **`usr/src/lib/libc/port/stdio/fwrite.c`** -> AI Confidence: **99.39%**
1294. **`usr/src/lib/libc/port/stdio/getline.c`** -> AI Confidence: **99.39%**
1295. **`usr/src/lib/libc/port/stdio/getw.c`** -> AI Confidence: **99.39%**
1296. **`usr/src/lib/libc/port/stdio/mse.c`** -> AI Confidence: **99.39%**
1297. **`usr/src/lib/libcommputil/common/sdp.c`** -> AI Confidence: **99.39%**
1298. **`usr/src/lib/libcommputil/common/sdp_parse_helper.c`** -> AI Confidence: **99.39%**
1299. **`usr/src/lib/libcpc/common/subr.c`** -> AI Confidence: **99.39%**
1300. **`usr/src/lib/libcurses/screen/setupterm.c`** -> AI Confidence: **99.39%**
1301. **`usr/src/lib/libdemangle/common/rust-v0puny.c`** -> AI Confidence: **99.39%**
1302. **`usr/src/lib/libdhcputil/common/dhcp_symbol.c`** -> AI Confidence: **99.39%**
1303. **`usr/src/lib/libdisasm/common/dis_sparc_fmt.c`** -> AI Confidence: **99.39%**
1304. **`usr/src/lib/libdladm/common/libdlbridge.c`** -> AI Confidence: **99.39%**
1305. **`usr/src/lib/libdladm/common/libdlvnic.c`** -> AI Confidence: **99.39%**
1306. **`usr/src/lib/libdladm/common/libdlwlan.c`** -> AI Confidence: **99.39%**
1307. **`usr/src/lib/libdladm/common/propfuncs.c`** -> AI Confidence: **99.39%**
1308. **`usr/src/lib/libdtrace/common/dt_aggregate.c`** -> AI Confidence: **99.39%**
1309. **`usr/src/lib/libdtrace/common/dt_parser.c`** -> AI Confidence: **99.39%**
1310. **`usr/src/lib/libdtrace/common/dt_sugar.c`** -> AI Confidence: **99.39%**
1311. **`usr/src/lib/libgen/common/mkdirp.c`** -> AI Confidence: **99.39%**
1312. **`usr/src/lib/libgen/common/reg_step.c`** -> AI Confidence: **99.39%**
1313. **`usr/src/lib/libgss/g_acquire_cred.c`** -> AI Confidence: **99.39%**
1314. **`usr/src/lib/libi2c/common/libi2c.c`** -> AI Confidence: **99.39%**
1315. **`usr/src/lib/libidmap/common/directory_helper.c`** -> AI Confidence: **99.39%**
1316. **`usr/src/lib/libinetsvc/common/inetsvc.c`** -> AI Confidence: **99.39%**
1317. **`usr/src/lib/libinstzones/common/zones_lofs.c`** -> AI Confidence: **99.39%**
1318. **`usr/src/lib/libinstzones/common/zones_paths.c`** -> AI Confidence: **99.39%**
1319. **`usr/src/lib/libipadm/common/ipadm_persist.c`** -> AI Confidence: **99.39%**
1320. **`usr/src/lib/libjedec/common/libjedec_spd.c`** -> AI Confidence: **99.39%**
1321. **`usr/src/lib/libkmf/ber_der/common/clasn1.c`** -> AI Confidence: **99.39%**
1322. **`usr/src/lib/libkmf/libkmf/common/client.c`** -> AI Confidence: **99.39%**
1323. **`usr/src/lib/libkmf/plugins/kmf_nss/common/nss_spi.c`** -> AI Confidence: **99.39%**
1324. **`usr/src/lib/libkmf/plugins/kmf_openssl/common/openssl_spi.c`** -> AI Confidence: **99.39%**
1325. **`usr/src/lib/libm/common/m9x/__fex_i386.c`** -> AI Confidence: **99.39%**
1326. **`usr/src/lib/libnisdb/db_index_entry_c.c`** -> AI Confidence: **99.39%**
1327. **`usr/src/lib/libnisdb/ldap_attr.c`** -> AI Confidence: **99.39%**
1328. **`usr/src/lib/libnisdb/ldap_cto.c`** -> AI Confidence: **99.39%**
1329. **`usr/src/lib/libnisdb/ldap_op.c`** -> AI Confidence: **99.39%**
1330. **`usr/src/lib/libnisdb/ldap_parse.c`** -> AI Confidence: **99.39%**
1331. **`usr/src/lib/libnisdb/nis_parse_ldap_yp_util.c`** -> AI Confidence: **99.39%**
1332. **`usr/src/lib/libnisdb/yptol/dit_access.c`** -> AI Confidence: **99.39%**
1333. **`usr/src/lib/libnls/common/nlsrequest.c`** -> AI Confidence: **99.39%**
1334. **`usr/src/lib/libnsl/des/des_soft.c`** -> AI Confidence: **99.39%**
1335. **`usr/src/lib/libnsl/nsl/t_alloc.c`** -> AI Confidence: **99.39%**
1336. **`usr/src/lib/libnsl/nsl/t_listen.c`** -> AI Confidence: **99.39%**
1337. **`usr/src/lib/libnsl/nsl/t_rcvdis.c`** -> AI Confidence: **99.39%**
1338. **`usr/src/lib/libnsl/nsl/t_rcvudata.c`** -> AI Confidence: **99.39%**
1339. **`usr/src/lib/libnsl/nsl/t_rcvvudata.c`** -> AI Confidence: **99.39%**
1340. **`usr/src/lib/libnsl/rpc/auth_time.c`** -> AI Confidence: **99.39%**
1341. **`usr/src/lib/libnsl/rpc/clnt_bcast.c`** -> AI Confidence: **99.39%**
1342. **`usr/src/lib/libnsl/rpc/clnt_generic.c`** -> AI Confidence: **99.39%**
1343. **`usr/src/lib/libnsl/rpc/rtime_tli.c`** -> AI Confidence: **99.39%**
1344. **`usr/src/lib/libpctx/common/libpctx.c`** -> AI Confidence: **99.39%**
1345. **`usr/src/lib/libpkg/common/pkgexecl.c`** -> AI Confidence: **99.39%**
1346. **`usr/src/lib/libpkg/common/srchcfile.c`** -> AI Confidence: **99.39%**
1347. **`usr/src/lib/libpool/common/pool_commit.c`** -> AI Confidence: **99.39%**
1348. **`usr/src/lib/libproc/common/Pgcore.c`** -> AI Confidence: **99.39%**
1349. **`usr/src/lib/libproc/common/Pscantext.c`** -> AI Confidence: **99.39%**
1350. **`usr/src/lib/libproc/common/pr_meminfo.c`** -> AI Confidence: **99.39%**
1351. **`usr/src/lib/libprtdiag/common/cpu.c`** -> AI Confidence: **99.39%**
1352. **`usr/src/lib/libprtdiag/common/memory.c`** -> AI Confidence: **99.39%**
1353. **`usr/src/lib/libprtdiag/common/pdevinfo_sun4u.c`** -> AI Confidence: **99.39%**
1354. **`usr/src/lib/libprtdiag_psr/sparc/javelin/common/javelin.c`** -> AI Confidence: **99.39%**
1355. **`usr/src/lib/libprtdiag_psr/sparc/littleneck/common/littleneck.c`** -> AI Confidence: **99.39%**
1356. **`usr/src/lib/libprtdiag_psr/sparc/serengeti/common/serengeti.c`** -> AI Confidence: **99.39%**
1357. **`usr/src/lib/libresolv/res_init.c`** -> AI Confidence: **99.39%**
1358. **`usr/src/lib/libresolv/res_send.c`** -> AI Confidence: **99.39%**
1359. **`usr/src/lib/libresolv2/common/bsd/mktemp.c`** -> AI Confidence: **99.39%**
1360. **`usr/src/lib/libresolv2/common/inet/inet_cidr_ntop.c`** -> AI Confidence: **99.39%**
1361. **`usr/src/lib/libresolv2/common/inet/inet_net_ntop.c`** -> AI Confidence: **99.39%**
1362. **`usr/src/lib/libresolv2/common/irs/getaddrinfo.c`** -> AI Confidence: **99.39%**
1363. **`usr/src/lib/libresolv2/common/irs/util.c`** -> AI Confidence: **99.39%**
1364. **`usr/src/lib/libresolv2/common/isc/assertions.c`** -> AI Confidence: **99.39%**
1365. **`usr/src/lib/libresolv2/common/isc/base64.c`** -> AI Confidence: **99.39%**
1366. **`usr/src/lib/libresolv2/common/nameser/ns_date.c`** -> AI Confidence: **99.39%**
1367. **`usr/src/lib/libresolv2/common/nameser/ns_parse.c`** -> AI Confidence: **99.39%**
1368. **`usr/src/lib/libresolv2/common/resolv/res_debug.c`** -> AI Confidence: **99.39%**
1369. **`usr/src/lib/libresolv2/common/resolv/res_send.c`** -> AI Confidence: **99.39%**
1370. **`usr/src/lib/librsm/common/rsmgen.c`** -> AI Confidence: **99.39%**
1371. **`usr/src/lib/librstp/common/port.c`** -> AI Confidence: **99.39%**
1372. **`usr/src/lib/libsasl/lib/checkpw.c`** -> AI Confidence: **99.39%**
1373. **`usr/src/lib/libsasl/lib/saslutil.c`** -> AI Confidence: **99.39%**
1374. **`usr/src/lib/libshare/common/scfutil.c`** -> AI Confidence: **99.39%**
1375. **`usr/src/lib/libsip/common/sip_logging.c`** -> AI Confidence: **99.39%**
1376. **`usr/src/lib/libsldap/common/ns_reads.c`** -> AI Confidence: **99.39%**
1377. **`usr/src/lib/libsmbfs/smb/keychain.c`** -> AI Confidence: **99.39%**
1378. **`usr/src/lib/libsmbfs/smb/krb5ssp.c`** -> AI Confidence: **99.39%**
1379. **`usr/src/lib/libsqlite/src/func.c`** -> AI Confidence: **99.39%**
1380. **`usr/src/lib/libsqlite/tool/showjournal.c`** -> AI Confidence: **99.39%**
1381. **`usr/src/lib/libstmf/common/stmf.c`** -> AI Confidence: **99.39%**
1382. **`usr/src/lib/libtecla/common/homedir.c`** -> AI Confidence: **99.39%**
1383. **`usr/src/lib/libtsol/common/setflabel.c`** -> AI Confidence: **99.39%**
1384. **`usr/src/lib/libumem/common/envvar.c`** -> AI Confidence: **99.39%**
1385. **`usr/src/lib/libwrap/fix_options.c`** -> AI Confidence: **99.39%**
1386. **`usr/src/lib/libxcurses/src/libc/xcurses/setup.c`** -> AI Confidence: **99.39%**
1387. **`usr/src/lib/libxcurses/src/tabs/tabs.c`** -> AI Confidence: **99.39%**
1388. **`usr/src/lib/libzfs/common/libzfs_changelist.c`** -> AI Confidence: **99.39%**
1389. **`usr/src/lib/libzfs/common/libzfs_crypto.c`** -> AI Confidence: **99.39%**
1390. **`usr/src/lib/libzfs/common/libzfs_sendrecv.c`** -> AI Confidence: **99.39%**
1391. **`usr/src/lib/nsswitch/files/common/getservent.c`** -> AI Confidence: **99.39%**
1392. **`usr/src/lib/pam_modules/krb5/krb5_authenticate.c`** -> AI Confidence: **99.39%**
1393. **`usr/src/lib/pam_modules/sample/sample_authenticate.c`** -> AI Confidence: **99.39%**
1394. **`usr/src/lib/pam_modules/unix_auth/unix_auth.c`** -> AI Confidence: **99.39%**
1395. **`usr/src/lib/passwdutil/__get_authtoken_attr.c`** -> AI Confidence: **99.39%**
1396. **`usr/src/lib/passwdutil/__set_authtoken_attr.c`** -> AI Confidence: **99.39%**
1397. **`usr/src/lib/passwdutil/files_attr.c`** -> AI Confidence: **99.39%**
1398. **`usr/src/lib/passwdutil/ldap_attr.c`** -> AI Confidence: **99.39%**
1399. **`usr/src/lib/pkcs11/libpkcs11/common/metaObjectManager.c`** -> AI Confidence: **99.39%**
1400. **`usr/src/lib/pkcs11/libpkcs11/common/pkcs11Conf.c`** -> AI Confidence: **99.39%**
1401. **`usr/src/lib/pkcs11/pkcs11_kernel/common/kernelDecrypt.c`** -> AI Confidence: **99.39%**
1402. **`usr/src/lib/pkcs11/pkcs11_kernel/common/kernelEmulate.c`** -> AI Confidence: **99.39%**
1403. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softDESCrypt.c`** -> AI Confidence: **99.39%**
1404. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softDSA.c`** -> AI Confidence: **99.39%**
1405. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softDecryptUtil.c`** -> AI Confidence: **99.39%**
1406. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softDigestUtil.c`** -> AI Confidence: **99.39%**
1407. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softEncryptUtil.c`** -> AI Confidence: **99.39%**
1408. **`usr/src/lib/policykit/libpolkit/common/libpolkit-rbac.c`** -> AI Confidence: **99.39%**
1409. **`usr/src/lib/print/libhttp-core/common/http.c`** -> AI Confidence: **99.39%**
1410. **`usr/src/lib/print/libpapi-dynamic/common/nss.c`** -> AI Confidence: **99.39%**
1411. **`usr/src/lib/print/libpapi-lpd/common/lpd-job.c`** -> AI Confidence: **99.39%**
1412. **`usr/src/lib/print/libpapi-lpd/common/lpd-query.c`** -> AI Confidence: **99.39%**
1413. **`usr/src/lib/sasl_plugins/cram/cram.c`** -> AI Confidence: **99.39%**
1414. **`usr/src/lib/sasl_plugins/digestmd5/digestmd5.c`** -> AI Confidence: **99.39%**
1415. **`usr/src/lib/sasl_plugins/plain/plain.c`** -> AI Confidence: **99.39%**
1416. **`usr/src/lib/scsi/plugins/ses/SUN/common/sun_enclosure.c`** -> AI Confidence: **99.39%**
1417. **`usr/src/lib/smbclnt/libfknsmb/common/fake_ktli.c`** -> AI Confidence: **99.39%**
1418. **`usr/src/lib/smbclnt/libfksmbfs/common/fake_lookup.c`** -> AI Confidence: **99.39%**
1419. **`usr/src/lib/smbclnt/libfksmbfs/common/fake_open.c`** -> AI Confidence: **99.39%**
1420. **`usr/src/lib/smbsrv/libfksmbsrv/common/fksmb_init.c`** -> AI Confidence: **99.39%**
1421. **`usr/src/lib/smbsrv/libmlsvc/common/mlsvc_client.c`** -> AI Confidence: **99.39%**
1422. **`usr/src/lib/smbsrv/libsmb/common/smb_scfutil.c`** -> AI Confidence: **99.39%**
1423. **`usr/src/lib/smbsrv/libsmb/common/smb_syslog.c`** -> AI Confidence: **99.39%**
1424. **`usr/src/lib/smbsrv/libsmbns/common/smbns_krb.c`** -> AI Confidence: **99.39%**
1425. **`usr/src/lib/storage/libg_fc/common/cmd.c`** -> AI Confidence: **99.39%**
1426. **`usr/src/lib/udapl/udapl_tavor/common/dapl_cr_callback.c`** -> AI Confidence: **99.39%**
1427. **`usr/src/stand/lib/fs/nfs/lookup.c`** -> AI Confidence: **99.39%**
1428. **`usr/src/stand/lib/fs/nfs/mount.c`** -> AI Confidence: **99.39%**
1429. **`usr/src/stand/lib/fs/nfs/nfs4ops.c`** -> AI Confidence: **99.39%**
1430. **`usr/src/stand/lib/fs/ufs/lufsboot.c`** -> AI Confidence: **99.39%**
1431. **`usr/src/stand/lib/tcp/tcp_sack.c`** -> AI Confidence: **99.39%**
1432. **`usr/src/test/bhyve-tests/tests/inst_emul/rdmsr.c`** -> AI Confidence: **99.39%**
1433. **`usr/src/test/bhyve-tests/tests/inst_emul/wrmsr.c`** -> AI Confidence: **99.39%**
1434. **`usr/src/test/bhyve-tests/tests/kdev/vlapic_msr_access.c`** -> AI Confidence: **99.39%**
1435. **`usr/src/test/bhyve-tests/tests/viona/create_delete.c`** -> AI Confidence: **99.39%**
1436. **`usr/src/test/bhyve-tests/tests/vmm/cpuid_ioctl.c`** -> AI Confidence: **99.39%**
1437. **`usr/src/test/bhyve-tests/tests/vmm/mem_devmem.c`** -> AI Confidence: **99.39%**
1438. **`usr/src/test/bhyve-tests/tests/vmm/mem_partial.c`** -> AI Confidence: **99.39%**
1439. **`usr/src/test/bhyve-tests/tests/vmm/mem_seg_map.c`** -> AI Confidence: **99.39%**
1440. **`usr/src/test/i2c-tests/tests/ioctl/i2c_ioctl_util.c`** -> AI Confidence: **99.39%**
1441. **`usr/src/test/libc-tests/tests/random/inz_child.c`** -> AI Confidence: **99.39%**
1442. **`usr/src/test/libc-tests/tests/random/inz_split.c`** -> AI Confidence: **99.39%**
1443. **`usr/src/test/libc-tests/tests/random/inz_vpp.c`** -> AI Confidence: **99.39%**
1444. **`usr/src/test/libc-tests/tests/select/select_test.c`** -> AI Confidence: **99.39%**
1445. **`usr/src/test/libc-tests/tests/stdio/fdclose.c`** -> AI Confidence: **99.39%**
1446. **`usr/src/test/libc-tests/tests/stdio/test_mbrtowc.c`** -> AI Confidence: **99.39%**
1447. **`usr/src/test/os-tests/tests/eventfd.c`** -> AI Confidence: **99.39%**
1448. **`usr/src/test/os-tests/tests/file-locking/acquire-lock.c`** -> AI Confidence: **99.39%**
1449. **`usr/src/test/os-tests/tests/gpio/gpio_lookup.c`** -> AI Confidence: **99.39%**
1450. **`usr/src/test/os-tests/tests/libtopo/digraph-test.c`** -> AI Confidence: **99.39%**
1451. **`usr/src/test/os-tests/tests/oclo/oclo.c`** -> AI Confidence: **99.39%**
1452. **`usr/src/test/os-tests/tests/sockfs/rights.c`** -> AI Confidence: **99.39%**
1453. **`usr/src/test/os-tests/tests/xsave/proc_xregs_set.c`** -> AI Confidence: **99.39%**
1454. **`usr/src/test/smbclient-tests/cmd/rw_mmap/rw_mmap.c`** -> AI Confidence: **99.39%**
1455. **`usr/src/tools/btxld/btxld.c`** -> AI Confidence: **99.39%**
1456. **`usr/src/tools/cpcgen/cpcgen.c`** -> AI Confidence: **99.39%**
1457. **`usr/src/tools/ctf/stabs/common/ctfstabs.c`** -> AI Confidence: **99.39%**
1458. **`usr/src/tools/smatch/src/graph.c`** -> AI Confidence: **99.39%**
1459. **`usr/src/ucbcmd/chown/chown.c`** -> AI Confidence: **99.39%**
1460. **`usr/src/ucbcmd/install.d/install.c`** -> AI Confidence: **99.39%**
1461. **`usr/src/ucbcmd/sed/sed1.c`** -> AI Confidence: **99.39%**
1462. **`usr/src/ucblib/libucb/port/stdio/fopen.c`** -> AI Confidence: **99.39%**
1463. **`usr/src/uts/common/conf/param.c`** -> AI Confidence: **99.39%**
1464. **`usr/src/uts/common/contract/process.c`** -> AI Confidence: **99.39%**
1465. **`usr/src/uts/common/crypto/api/kcf_cipher.c`** -> AI Confidence: **99.39%**
1466. **`usr/src/uts/common/crypto/api/kcf_digest.c`** -> AI Confidence: **99.39%**
1467. **`usr/src/uts/common/crypto/api/kcf_keys.c`** -> AI Confidence: **99.39%**
1468. **`usr/src/uts/common/crypto/api/kcf_miscapi.c`** -> AI Confidence: **99.39%**
1469. **`usr/src/uts/common/crypto/api/kcf_sign.c`** -> AI Confidence: **99.39%**
1470. **`usr/src/uts/common/crypto/api/kcf_verify.c`** -> AI Confidence: **99.39%**
1471. **`usr/src/uts/common/crypto/core/kcf_prov_tabs.c`** -> AI Confidence: **99.39%**
1472. **`usr/src/uts/common/crypto/io/aes.c`** -> AI Confidence: **99.39%**
1473. **`usr/src/uts/common/crypto/io/crypto.c`** -> AI Confidence: **99.39%**
1474. **`usr/src/uts/common/crypto/io/dprov.c`** -> AI Confidence: **99.39%**
1475. **`usr/src/uts/common/crypto/io/sha1_mod.c`** -> AI Confidence: **99.39%**
1476. **`usr/src/uts/common/disp/fss.c`** -> AI Confidence: **99.39%**
1477. **`usr/src/uts/common/disp/priocntl.c`** -> AI Confidence: **99.39%**
1478. **`usr/src/uts/common/dtrace/dtrace.c`** -> AI Confidence: **99.39%**
1479. **`usr/src/uts/common/exec/elf/old_notes.c`** -> AI Confidence: **99.39%**
1480. **`usr/src/uts/common/fs/autofs/auto_vnops.c`** -> AI Confidence: **99.39%**
1481. **`usr/src/uts/common/fs/dnlc.c`** -> AI Confidence: **99.39%**
1482. **`usr/src/uts/common/fs/fdbuffer.c`** -> AI Confidence: **99.39%**
1483. **`usr/src/uts/common/fs/fifofs/fifovnops.c`** -> AI Confidence: **99.39%**
1484. **`usr/src/uts/common/fs/fs_subr.c`** -> AI Confidence: **99.39%**
1485. **`usr/src/uts/common/fs/fsflush.c`** -> AI Confidence: **99.39%**
1486. **`usr/src/uts/common/fs/gfs.c`** -> AI Confidence: **99.39%**
1487. **`usr/src/uts/common/fs/nfs/nfs3_vfsops.c`** -> AI Confidence: **99.39%**
1488. **`usr/src/uts/common/fs/nfs/nfs3_vnops.c`** -> AI Confidence: **99.39%**
1489. **`usr/src/uts/common/fs/nfs/nfs4_srv_attr.c`** -> AI Confidence: **99.39%**
1490. **`usr/src/uts/common/fs/nfs/nfs4_srv_readdir.c`** -> AI Confidence: **99.39%**
1491. **`usr/src/uts/common/fs/nfs/nfs4_subr.c`** -> AI Confidence: **99.39%**
1492. **`usr/src/uts/common/fs/nfs/nfs4_vnops.c`** -> AI Confidence: **99.39%**
1493. **`usr/src/uts/common/fs/nfs/nfs_acl_vnops.c`** -> AI Confidence: **99.39%**
1494. **`usr/src/uts/common/fs/nfs/nfs_subr.c`** -> AI Confidence: **99.39%**
1495. **`usr/src/uts/common/fs/nfs/nfs_vnops.c`** -> AI Confidence: **99.39%**
1496. **`usr/src/uts/common/fs/pcfs/pc_alloc.c`** -> AI Confidence: **99.39%**
1497. **`usr/src/uts/common/fs/proc/prvnops.c`** -> AI Confidence: **99.39%**
1498. **`usr/src/uts/common/fs/smbclnt/netsmb/smb_iod.c`** -> AI Confidence: **99.39%**
1499. **`usr/src/uts/common/fs/smbclnt/netsmb/smb_usr.c`** -> AI Confidence: **99.39%**
1500. **`usr/src/uts/common/fs/smbclnt/smbfs/smbfs_rwlock.c`** -> AI Confidence: **99.39%**
1501. **`usr/src/uts/common/fs/smbsrv/smb_acl.c`** -> AI Confidence: **99.39%**
1502. **`usr/src/uts/common/fs/smbsrv/smb_fsops.c`** -> AI Confidence: **99.39%**
1503. **`usr/src/uts/common/fs/smbsrv/smb_idmap.c`** -> AI Confidence: **99.39%**
1504. **`usr/src/uts/common/fs/smbsrv/smb_init.c`** -> AI Confidence: **99.39%**
1505. **`usr/src/uts/common/fs/sockfs/sockcommon_sops.c`** -> AI Confidence: **99.39%**
1506. **`usr/src/uts/common/fs/sockfs/sodirect.c`** -> AI Confidence: **99.39%**
1507. **`usr/src/uts/common/fs/ufs/quota_ufs.c`** -> AI Confidence: **99.39%**
1508. **`usr/src/uts/common/fs/ufs/ufs_bmap.c`** -> AI Confidence: **99.39%**
1509. **`usr/src/uts/common/fs/ufs/ufs_dir.c`** -> AI Confidence: **99.39%**
1510. **`usr/src/uts/common/fs/ufs/ufs_extvnops.c`** -> AI Confidence: **99.39%**
1511. **`usr/src/uts/common/fs/ufs/ufs_inode.c`** -> AI Confidence: **99.39%**
1512. **`usr/src/uts/common/fs/ufs/ufs_lockfs.c`** -> AI Confidence: **99.39%**
1513. **`usr/src/uts/common/fs/xattr.c`** -> AI Confidence: **99.39%**
1514. **`usr/src/uts/common/fs/zfs/arc.c`** -> AI Confidence: **99.39%**
1515. **`usr/src/uts/common/fs/zfs/dbuf.c`** -> AI Confidence: **99.39%**
1516. **`usr/src/uts/common/fs/zfs/dmu_zfetch.c`** -> AI Confidence: **99.39%**
1517. **`usr/src/uts/common/fs/zfs/dnode.c`** -> AI Confidence: **99.39%**
1518. **`usr/src/uts/common/fs/zfs/dnode_sync.c`** -> AI Confidence: **99.39%**
1519. **`usr/src/uts/common/fs/zfs/lua/lcode.c`** -> AI Confidence: **99.39%**
1520. **`usr/src/uts/common/fs/zfs/lua/ldebug.c`** -> AI Confidence: **99.39%**
1521. **`usr/src/uts/common/fs/zfs/lua/ldo.c`** -> AI Confidence: **99.39%**
1522. **`usr/src/uts/common/fs/zfs/lua/lgc.c`** -> AI Confidence: **99.39%**
1523. **`usr/src/uts/common/fs/zfs/lua/llex.c`** -> AI Confidence: **99.39%**
1524. **`usr/src/uts/common/fs/zfs/lua/ltable.c`** -> AI Confidence: **99.39%**
1525. **`usr/src/uts/common/fs/zfs/lua/ltm.c`** -> AI Confidence: **99.39%**
1526. **`usr/src/uts/common/fs/zfs/spa_config.c`** -> AI Confidence: **99.39%**
1527. **`usr/src/uts/common/fs/zfs/vdev.c`** -> AI Confidence: **99.39%**
1528. **`usr/src/uts/common/fs/zfs/vdev_disk.c`** -> AI Confidence: **99.39%**
1529. **`usr/src/uts/common/fs/zfs/vdev_raidz_math.c`** -> AI Confidence: **99.39%**
1530. **`usr/src/uts/common/fs/zfs/zcp.c`** -> AI Confidence: **99.39%**
1531. **`usr/src/uts/common/fs/zfs/zcp_get.c`** -> AI Confidence: **99.39%**
1532. **`usr/src/uts/common/fs/zfs/zfs_acl.c`** -> AI Confidence: **99.39%**
1533. **`usr/src/uts/common/fs/zfs/zfs_dir.c`** -> AI Confidence: **99.39%**
1534. **`usr/src/uts/common/fs/zfs/zfs_log.c`** -> AI Confidence: **99.39%**
1535. **`usr/src/uts/common/fs/zfs/zfs_sa.c`** -> AI Confidence: **99.39%**
1536. **`usr/src/uts/common/fs/zfs/zio.c`** -> AI Confidence: **99.39%**
1537. **`usr/src/uts/common/fs/zfs/zio_crypt.c`** -> AI Confidence: **99.39%**
1538. **`usr/src/uts/common/fs/zfs/zio_inject.c`** -> AI Confidence: **99.39%**
1539. **`usr/src/uts/common/gssapi/mechs/krb5/mech/k5sealv3.c`** -> AI Confidence: **99.39%**
1540. **`usr/src/uts/common/idmap/idmap_cache.c`** -> AI Confidence: **99.39%**
1541. **`usr/src/uts/common/idmap/idmap_kapi.c`** -> AI Confidence: **99.39%**
1542. **`usr/src/uts/common/inet/ilb/ilb_nat.c`** -> AI Confidence: **99.39%**
1543. **`usr/src/uts/common/inet/ip/conn_opt.c`** -> AI Confidence: **99.39%**
1544. **`usr/src/uts/common/inet/ip/inet_ntop.c`** -> AI Confidence: **99.39%**
1545. **`usr/src/uts/common/inet/ip/ip.c`** -> AI Confidence: **99.39%**
1546. **`usr/src/uts/common/inet/ip/ip6.c`** -> AI Confidence: **99.39%**
1547. **`usr/src/uts/common/inet/ip/ip6_if.c`** -> AI Confidence: **99.39%**
1548. **`usr/src/uts/common/inet/ip/ip6_input.c`** -> AI Confidence: **99.39%**
1549. **`usr/src/uts/common/inet/ip/ip6_ire.c`** -> AI Confidence: **99.39%**
1550. **`usr/src/uts/common/inet/ip/ip_attr.c`** -> AI Confidence: **99.39%**
1551. **`usr/src/uts/common/inet/ip/ip_input.c`** -> AI Confidence: **99.39%**
1552. **`usr/src/uts/common/inet/ip/ip_ndp.c`** -> AI Confidence: **99.39%**
1553. **`usr/src/uts/common/inet/ip/ip_output.c`** -> AI Confidence: **99.39%**
1554. **`usr/src/uts/common/inet/ip/keysock.c`** -> AI Confidence: **99.39%**
1555. **`usr/src/uts/common/inet/ip/sadb.c`** -> AI Confidence: **99.39%**
1556. **`usr/src/uts/common/inet/ip/spdsock.c`** -> AI Confidence: **99.39%**
1557. **`usr/src/uts/common/inet/ip/tnet.c`** -> AI Confidence: **99.39%**
1558. **`usr/src/uts/common/inet/ipf/fil.c`** -> AI Confidence: **99.39%**
1559. **`usr/src/uts/common/inet/ipf/ip_frag.c`** -> AI Confidence: **99.39%**
1560. **`usr/src/uts/common/inet/ipf/ip_htable.c`** -> AI Confidence: **99.39%**
1561. **`usr/src/uts/common/inet/ipf/ip_lookup.c`** -> AI Confidence: **99.39%**
1562. **`usr/src/uts/common/inet/ipf/ip_pool.c`** -> AI Confidence: **99.39%**
1563. **`usr/src/uts/common/inet/iptun/iptun.c`** -> AI Confidence: **99.39%**
1564. **`usr/src/uts/common/inet/nd.c`** -> AI Confidence: **99.39%**
1565. **`usr/src/uts/common/inet/sctp/sctp_addr.c`** -> AI Confidence: **99.39%**
1566. **`usr/src/uts/common/inet/sctp/sctp_common.c`** -> AI Confidence: **99.39%**
1567. **`usr/src/uts/common/inet/sctp/sctp_hash.c`** -> AI Confidence: **99.39%**
1568. **`usr/src/uts/common/inet/sctp/sctp_init.c`** -> AI Confidence: **99.39%**
1569. **`usr/src/uts/common/inet/sctp/sctp_opt_data.c`** -> AI Confidence: **99.39%**
1570. **`usr/src/uts/common/inet/tcp/tcp_fusion.c`** -> AI Confidence: **99.39%**
1571. **`usr/src/uts/common/inet/tcp/tcp_input.c`** -> AI Confidence: **99.39%**
1572. **`usr/src/uts/common/inet/tcp/tcp_misc.c`** -> AI Confidence: **99.39%**
1573. **`usr/src/uts/common/inet/tcp/tcp_opt_data.c`** -> AI Confidence: **99.39%**
1574. **`usr/src/uts/common/inet/tcp/tcp_output.c`** -> AI Confidence: **99.39%**
1575. **`usr/src/uts/common/inet/tcp/tcp_sack.c`** -> AI Confidence: **99.39%**
1576. **`usr/src/uts/common/io/1394/t1394.c`** -> AI Confidence: **99.39%**
1577. **`usr/src/uts/common/io/aggr/aggr_grp.c`** -> AI Confidence: **99.39%**
1578. **`usr/src/uts/common/io/aggr/aggr_recv.c`** -> AI Confidence: **99.39%**
1579. **`usr/src/uts/common/io/asy.c`** -> AI Confidence: **99.39%**
1580. **`usr/src/uts/common/io/atge/atge_main.c`** -> AI Confidence: **99.39%**
1581. **`usr/src/uts/common/io/ath/ath_rate.c`** -> AI Confidence: **99.39%**
1582. **`usr/src/uts/common/io/audio/ac97/ac97_ad.c`** -> AI Confidence: **99.39%**
1583. **`usr/src/uts/common/io/audio/drv/audiocmihd/audiocmihd.c`** -> AI Confidence: **99.39%**
1584. **`usr/src/uts/common/io/audio/impl/audio_ctrl.c`** -> AI Confidence: **99.39%**
1585. **`usr/src/uts/common/io/bnxe/577xx/drivers/common/include/debug.h`** -> AI Confidence: **99.39%**
1586. **`usr/src/uts/common/io/bnxe/577xx/drivers/common/lm/l4/lm_l4rx.c`** -> AI Confidence: **99.39%**
1587. **`usr/src/uts/common/io/bnxe/577xx/drivers/common/lm/l4/lm_l4sp.c`** -> AI Confidence: **99.39%**
1588. **`usr/src/uts/common/io/bridge.c`** -> AI Confidence: **99.39%**
1589. **`usr/src/uts/common/io/busra.c`** -> AI Confidence: **99.39%**
1590. **`usr/src/uts/common/io/cardbus/cardbus_hp.c`** -> AI Confidence: **99.39%**
1591. **`usr/src/uts/common/io/chxge/ch.c`** -> AI Confidence: **99.39%**
1592. **`usr/src/uts/common/io/comstar/lu/stmf_sbd/ats_copy_mgr.c`** -> AI Confidence: **99.39%**
1593. **`usr/src/uts/common/io/comstar/lu/stmf_sbd/sbd.c`** -> AI Confidence: **99.39%**
1594. **`usr/src/uts/common/io/comstar/lu/stmf_sbd/sbd_pgr.c`** -> AI Confidence: **99.39%**
1595. **`usr/src/uts/common/io/comstar/lu/stmf_sbd/sbd_scsi.c`** -> AI Confidence: **99.39%**
1596. **`usr/src/uts/common/io/comstar/port/fct/fct.c`** -> AI Confidence: **99.39%**
1597. **`usr/src/uts/common/io/comstar/port/iscsit/iscsit_login.c`** -> AI Confidence: **99.39%**
1598. **`usr/src/uts/common/io/comstar/port/qlt/qlt.c`** -> AI Confidence: **99.39%**
1599. **`usr/src/uts/common/io/comstar/stmf/stmf.c`** -> AI Confidence: **99.39%**
1600. **`usr/src/uts/common/io/conskbd.c`** -> AI Confidence: **99.39%**
1601. **`usr/src/uts/common/io/consms.c`** -> AI Confidence: **99.39%**
1602. **`usr/src/uts/common/io/cryptmod.c`** -> AI Confidence: **99.39%**
1603. **`usr/src/uts/common/io/devpoll.c`** -> AI Confidence: **99.39%**
1604. **`usr/src/uts/common/io/fcoe/fcoe_eth.c`** -> AI Confidence: **99.39%**
1605. **`usr/src/uts/common/io/fibre-channel/fca/fcoei/fcoei_eth.c`** -> AI Confidence: **99.39%**
1606. **`usr/src/uts/common/io/fibre-channel/fca/qlc/ql_mbx.c`** -> AI Confidence: **99.39%**
1607. **`usr/src/uts/common/io/fibre-channel/fca/qlc/ql_xioctl.c`** -> AI Confidence: **99.39%**
1608. **`usr/src/uts/common/io/fibre-channel/fca/qlge/qlge_gld.c`** -> AI Confidence: **99.39%**
1609. **`usr/src/uts/common/io/fibre-channel/impl/fctl.c`** -> AI Confidence: **99.39%**
1610. **`usr/src/uts/common/io/ib/adapters/hermon/hermon_qpmod.c`** -> AI Confidence: **99.39%**
1611. **`usr/src/uts/common/io/ib/adapters/tavor/tavor_qpmod.c`** -> AI Confidence: **99.39%**
1612. **`usr/src/uts/common/io/ib/adapters/tavor/tavor_wr.c`** -> AI Confidence: **99.39%**
1613. **`usr/src/uts/common/io/ib/clients/eoib/eib_data.c`** -> AI Confidence: **99.39%**
1614. **`usr/src/uts/common/io/ib/clients/eoib/eib_ibt.c`** -> AI Confidence: **99.39%**
1615. **`usr/src/uts/common/io/ib/clients/eoib/enx_q.c`** -> AI Confidence: **99.39%**
1616. **`usr/src/uts/common/io/ib/clients/ibd/ibd.c`** -> AI Confidence: **99.39%**
1617. **`usr/src/uts/common/io/ib/clients/iser/iser_cm.c`** -> AI Confidence: **99.39%**
1618. **`usr/src/uts/common/io/ib/clients/iser/iser_cq.c`** -> AI Confidence: **99.39%**
1619. **`usr/src/uts/common/io/ib/clients/of/sol_umad/sol_umad.c`** -> AI Confidence: **99.39%**
1620. **`usr/src/uts/common/io/ib/clients/of/sol_uverbs/sol_uverbs.c`** -> AI Confidence: **99.39%**
1621. **`usr/src/uts/common/io/ib/clients/of/sol_uverbs/sol_uverbs_event.c`** -> AI Confidence: **99.39%**
1622. **`usr/src/uts/common/io/ib/clients/rdsv3/rdsv3_impl.c`** -> AI Confidence: **99.39%**
1623. **`usr/src/uts/common/io/ib/clients/rdsv3/send.c`** -> AI Confidence: **99.39%**
1624. **`usr/src/uts/common/io/ib/mgt/ibcm/ibcm_arp_link.c`** -> AI Confidence: **99.39%**
1625. **`usr/src/uts/common/io/ib/mgt/ibdm/ibdm.c`** -> AI Confidence: **99.39%**
1626. **`usr/src/uts/common/io/idm/idm_conn_sm.c`** -> AI Confidence: **99.39%**
1627. **`usr/src/uts/common/io/mac/mac.c`** -> AI Confidence: **99.39%**
1628. **`usr/src/uts/common/io/mac/mac_bcast.c`** -> AI Confidence: **99.39%**
1629. **`usr/src/uts/common/io/mac/mac_datapath_setup.c`** -> AI Confidence: **99.39%**
1630. **`usr/src/uts/common/io/mii/mii.c`** -> AI Confidence: **99.39%**
1631. **`usr/src/uts/common/io/mii/mii_intel.c`** -> AI Confidence: **99.39%**
1632. **`usr/src/uts/common/io/mlxcx/mlxcx_intr.c`** -> AI Confidence: **99.39%**
1633. **`usr/src/uts/common/io/ntxn/unm_gem.c`** -> AI Confidence: **99.39%**
1634. **`usr/src/uts/common/io/nxge/nxge_fflp.c`** -> AI Confidence: **99.39%**
1635. **`usr/src/uts/common/io/nxge/nxge_send.c`** -> AI Confidence: **99.39%**
1636. **`usr/src/uts/common/io/pci_cap.c`** -> AI Confidence: **99.39%**
1637. **`usr/src/uts/common/io/pciex/hotplug/pcishpc.c`** -> AI Confidence: **99.39%**
1638. **`usr/src/uts/common/io/pciex/pcie.c`** -> AI Confidence: **99.39%**
1639. **`usr/src/uts/common/io/pciex/pcie_fault.c`** -> AI Confidence: **99.39%**
1640. **`usr/src/uts/common/io/pm.c`** -> AI Confidence: **99.39%**
1641. **`usr/src/uts/common/io/ppm/ppm.c`** -> AI Confidence: **99.39%**
1642. **`usr/src/uts/common/io/ppp/spppcomp/spppcomp.c`** -> AI Confidence: **99.39%**
1643. **`usr/src/uts/common/io/ppp/spppcomp/zlib.c`** -> AI Confidence: **99.39%**
1644. **`usr/src/uts/common/io/scsi/adapters/iscsi/iscsi_io.c`** -> AI Confidence: **99.39%**
1645. **`usr/src/uts/common/io/scsi/adapters/iscsi/iscsi_ioctl.c`** -> AI Confidence: **99.39%**
1646. **`usr/src/uts/common/io/scsi/adapters/mpt_sas/mptsas.c`** -> AI Confidence: **99.39%**
1647. **`usr/src/uts/common/io/scsi/adapters/mpt_sas/mptsas_impl.c`** -> AI Confidence: **99.39%**
1648. **`usr/src/uts/common/io/sfxge/sfxge.c`** -> AI Confidence: **99.39%**
1649. **`usr/src/uts/common/io/sfxge/sfxge_intr.c`** -> AI Confidence: **99.39%**
1650. **`usr/src/uts/common/io/softmac/softmac_main.c`** -> AI Confidence: **99.39%**
1651. **`usr/src/uts/common/io/telmod.c`** -> AI Confidence: **99.39%**
1652. **`usr/src/uts/common/io/ttcompat.c`** -> AI Confidence: **99.39%**
1653. **`usr/src/uts/common/io/tty_pts.c`** -> AI Confidence: **99.39%**
1654. **`usr/src/uts/common/io/usb/clients/audio/usb_as/usb_as.c`** -> AI Confidence: **99.39%**
1655. **`usr/src/uts/common/io/usb/clients/usbser/usbftdi/uftdi_dsd.c`** -> AI Confidence: **99.39%**
1656. **`usr/src/uts/common/io/usb/clients/usbser/usbsacm/usbsacm.c`** -> AI Confidence: **99.39%**
1657. **`usr/src/uts/common/io/usb/clients/usbser/usbser_keyspan/keyspan_dsd.c`** -> AI Confidence: **99.39%**
1658. **`usr/src/uts/common/io/usb/clients/usbser/usbser_keyspan/keyspan_pipe.c`** -> AI Confidence: **99.39%**
1659. **`usr/src/uts/common/io/usb/scsa2usb/usb_ms_bulkonly.c`** -> AI Confidence: **99.39%**
1660. **`usr/src/uts/common/io/usb/usba/hubdi.c`** -> AI Confidence: **99.39%**
1661. **`usr/src/uts/common/io/usbgem/usbgem.c`** -> AI Confidence: **99.39%**
1662. **`usr/src/uts/common/io/vr/vr.c`** -> AI Confidence: **99.39%**
1663. **`usr/src/uts/common/ipp/dscpmk/dscpmk.c`** -> AI Confidence: **99.39%**
1664. **`usr/src/uts/common/ipp/flowacct/flowacct.c`** -> AI Confidence: **99.39%**
1665. **`usr/src/uts/common/kiconv/kiconv_ja/kiconv_ja.c`** -> AI Confidence: **99.39%**
1666. **`usr/src/uts/common/ktli/t_kgtstate.c`** -> AI Confidence: **99.39%**
1667. **`usr/src/uts/common/ktli/t_ksndudat.c`** -> AI Confidence: **99.39%**
1668. **`usr/src/uts/common/ktli/t_kspoll.c`** -> AI Confidence: **99.39%**
1669. **`usr/src/uts/common/os/clock.c`** -> AI Confidence: **99.39%**
1670. **`usr/src/uts/common/os/clock_tick.c`** -> AI Confidence: **99.39%**
1671. **`usr/src/uts/common/os/console.c`** -> AI Confidence: **99.39%**
1672. **`usr/src/uts/common/os/contract.c`** -> AI Confidence: **99.39%**
1673. **`usr/src/uts/common/os/core.c`** -> AI Confidence: **99.39%**
1674. **`usr/src/uts/common/os/dacf_clnt.c`** -> AI Confidence: **99.39%**
1675. **`usr/src/uts/common/os/devid_cache.c`** -> AI Confidence: **99.39%**
1676. **`usr/src/uts/common/os/dkioc_free_util.c`** -> AI Confidence: **99.39%**
1677. **`usr/src/uts/common/os/dumpsubr.c`** -> AI Confidence: **99.39%**
1678. **`usr/src/uts/common/os/fork.c`** -> AI Confidence: **99.39%**
1679. **`usr/src/uts/common/os/klpd.c`** -> AI Confidence: **99.39%**
1680. **`usr/src/uts/common/os/lgrp.c`** -> AI Confidence: **99.39%**
1681. **`usr/src/uts/common/os/lwp.c`** -> AI Confidence: **99.39%**
1682. **`usr/src/uts/common/os/mem_cage.c`** -> AI Confidence: **99.39%**
1683. **`usr/src/uts/common/os/modsysfile.c`** -> AI Confidence: **99.39%**
1684. **`usr/src/uts/common/os/msacct.c`** -> AI Confidence: **99.39%**
1685. **`usr/src/uts/common/os/mutex.c`** -> AI Confidence: **99.39%**
1686. **`usr/src/uts/common/os/pgrp.c`** -> AI Confidence: **99.39%**
1687. **`usr/src/uts/common/os/putnext.c`** -> AI Confidence: **99.39%**
1688. **`usr/src/uts/common/os/sched.c`** -> AI Confidence: **99.39%**
1689. **`usr/src/uts/common/os/sig.c`** -> AI Confidence: **99.39%**
1690. **`usr/src/uts/common/os/streamio.c`** -> AI Confidence: **99.39%**
1691. **`usr/src/uts/common/os/swapgeneric.c`** -> AI Confidence: **99.39%**
1692. **`usr/src/uts/common/os/taskq.c`** -> AI Confidence: **99.39%**
1693. **`usr/src/uts/common/pcmcia/cs/cs.c`** -> AI Confidence: **99.39%**
1694. **`usr/src/uts/common/rpc/sec_gss/rpcsec_gss_misc.c`** -> AI Confidence: **99.39%**
1695. **`usr/src/uts/common/syscall/access.c`** -> AI Confidence: **99.39%**
1696. **`usr/src/uts/common/syscall/getrandom.c`** -> AI Confidence: **99.39%**
1697. **`usr/src/uts/common/syscall/lgrpsys.c`** -> AI Confidence: **99.39%**
1698. **`usr/src/uts/common/syscall/lwp_sobj.c`** -> AI Confidence: **99.39%**
1699. **`usr/src/uts/common/syscall/lwp_timer.c`** -> AI Confidence: **99.39%**
1700. **`usr/src/uts/common/syscall/mmapobjsys.c`** -> AI Confidence: **99.39%**
1701. **`usr/src/uts/common/syscall/nice.c`** -> AI Confidence: **99.39%**
1702. **`usr/src/uts/common/syscall/psecflags.c`** -> AI Confidence: **99.39%**
1703. **`usr/src/uts/common/syscall/rw.c`** -> AI Confidence: **99.39%**
1704. **`usr/src/uts/common/syscall/sigprocmask.c`** -> AI Confidence: **99.39%**
1705. **`usr/src/uts/common/syscall/sigqueue.c`** -> AI Confidence: **99.39%**
1706. **`usr/src/uts/common/syscall/symlink.c`** -> AI Confidence: **99.39%**
1707. **`usr/src/uts/common/syscall/systeminfo.c`** -> AI Confidence: **99.39%**
1708. **`usr/src/uts/common/syscall/uadmin.c`** -> AI Confidence: **99.39%**
1709. **`usr/src/uts/common/syscall/utime.c`** -> AI Confidence: **99.39%**
1710. **`usr/src/uts/common/syscall/utssys.c`** -> AI Confidence: **99.39%**
1711. **`usr/src/uts/common/vm/seg_vn.c`** -> AI Confidence: **99.39%**
1712. **`usr/src/uts/common/vm/vm_page.c`** -> AI Confidence: **99.39%**
1713. **`usr/src/uts/common/vm/vm_swap.c`** -> AI Confidence: **99.39%**
1714. **`usr/src/uts/i86pc/boot/boot_console.c`** -> AI Confidence: **99.39%**
1715. **`usr/src/uts/i86pc/boot/boot_fb.c`** -> AI Confidence: **99.39%**
1716. **`usr/src/uts/i86pc/cpu/generic_cpu/gcpu_mca.c`** -> AI Confidence: **99.39%**
1717. **`usr/src/uts/i86pc/dboot/dboot_elfload.c`** -> AI Confidence: **99.39%**
1718. **`usr/src/uts/i86pc/io/acpi/acpidev/acpidev_scope.c`** -> AI Confidence: **99.39%**
1719. **`usr/src/uts/i86pc/io/acpi/acpinex/acpinex_event.c`** -> AI Confidence: **99.39%**
1720. **`usr/src/uts/i86pc/io/apix/apix_utils.c`** -> AI Confidence: **99.39%**
1721. **`usr/src/uts/i86pc/io/dr/dr_mem_acpi.c`** -> AI Confidence: **99.39%**
1722. **`usr/src/uts/i86pc/io/fipe/fipe_drv.c`** -> AI Confidence: **99.39%**
1723. **`usr/src/uts/i86pc/io/hrtimers.c`** -> AI Confidence: **99.39%**
1724. **`usr/src/uts/i86pc/io/mp_platform_common.c`** -> AI Confidence: **99.39%**
1725. **`usr/src/uts/i86pc/io/mp_platform_misc.c`** -> AI Confidence: **99.39%**
1726. **`usr/src/uts/i86pc/io/pci/pci_common.c`** -> AI Confidence: **99.39%**
1727. **`usr/src/uts/i86pc/io/pcplusmp/apic_introp.c`** -> AI Confidence: **99.39%**
1728. **`usr/src/uts/i86pc/io/ppm/acpisleep.c`** -> AI Confidence: **99.39%**
1729. **`usr/src/uts/i86pc/io/psm/psm_common.c`** -> AI Confidence: **99.39%**
1730. **`usr/src/uts/i86pc/os/biosdisk.c`** -> AI Confidence: **99.39%**
1731. **`usr/src/uts/i86pc/os/fakebop.c`** -> AI Confidence: **99.39%**
1732. **`usr/src/uts/i86pc/os/memnode.c`** -> AI Confidence: **99.39%**
1733. **`usr/src/uts/i86pc/os/mp_startup.c`** -> AI Confidence: **99.39%**
1734. **`usr/src/uts/i86pc/vm/hment.c`** -> AI Confidence: **99.39%**
1735. **`usr/src/uts/i86pc/vm/vm_machdep.c`** -> AI Confidence: **99.39%**
1736. **`usr/src/uts/i86xpv/io/psm/mp_platform_xpv.c`** -> AI Confidence: **99.39%**
1737. **`usr/src/uts/i86xpv/io/psm/xpv_intr.c`** -> AI Confidence: **99.39%**
1738. **`usr/src/uts/i86xpv/os/xen_mmu.c`** -> AI Confidence: **99.39%**
1739. **`usr/src/uts/intel/amd64/krtld/kobj_reloc.c`** -> AI Confidence: **99.39%**
1740. **`usr/src/uts/intel/io/amdzen/zen_umc.c`** -> AI Confidence: **99.39%**
1741. **`usr/src/uts/intel/io/dktp/hba/ghd/ghd_timer.c`** -> AI Confidence: **99.39%**
1742. **`usr/src/uts/intel/io/intel_nb5000/intel_nb5000.c`** -> AI Confidence: **99.39%**
1743. **`usr/src/uts/intel/io/intel_nb5000/nb5000_init.c`** -> AI Confidence: **99.39%**
1744. **`usr/src/uts/intel/io/vmm/vmm_cpuid.c`** -> AI Confidence: **99.39%**
1745. **`usr/src/uts/intel/os/cpuid.c`** -> AI Confidence: **99.39%**
1746. **`usr/src/uts/intel/os/ddi_i86.c`** -> AI Confidence: **99.39%**
1747. **`usr/src/uts/intel/os/fmsmb.c`** -> AI Confidence: **99.39%**
1748. **`usr/src/uts/intel/os/fpu_subr.c`** -> AI Confidence: **99.39%**
1749. **`usr/src/uts/sfmmu/vm/hat_sfmmu.c`** -> AI Confidence: **99.39%**
1750. **`usr/src/uts/sparc/fpu/fpu_simulator.c`** -> AI Confidence: **99.39%**
1751. **`usr/src/uts/sparc/v9/fpu/fpu.c`** -> AI Confidence: **99.39%**
1752. **`usr/src/uts/sparc/v9/fpu/v9instr.c`** -> AI Confidence: **99.39%**
1753. **`usr/src/uts/sparc/v9/syscall/install_utrap.c`** -> AI Confidence: **99.39%**
1754. **`usr/src/uts/sun4/io/px/px_msi.c`** -> AI Confidence: **99.39%**
1755. **`usr/src/uts/sun4/io/px/px_tools.c`** -> AI Confidence: **99.39%**
1756. **`usr/src/uts/sun4/os/memnode.c`** -> AI Confidence: **99.39%**
1757. **`usr/src/uts/sun4/vm/vm_dep.c`** -> AI Confidence: **99.39%**
1758. **`usr/src/uts/sun4u/cpu/us3_cheetah.c`** -> AI Confidence: **99.39%**
1759. **`usr/src/uts/sun4u/cpu/us3_cheetahplus.c`** -> AI Confidence: **99.39%**
1760. **`usr/src/uts/sun4u/cpu/us3_jalapeno.c`** -> AI Confidence: **99.39%**
1761. **`usr/src/uts/sun4u/excalibur/io/xcalppm.c`** -> AI Confidence: **99.39%**
1762. **`usr/src/uts/sun4u/io/pci/db21554.c`** -> AI Confidence: **99.39%**
1763. **`usr/src/uts/sun4u/io/pci/pci_devctl.c`** -> AI Confidence: **99.39%**
1764. **`usr/src/uts/sun4u/io/pci/pci_dma.c`** -> AI Confidence: **99.39%**
1765. **`usr/src/uts/sun4u/io/pci/pci_pwr.c`** -> AI Confidence: **99.39%**
1766. **`usr/src/uts/sun4u/io/pci/pci_tools.c`** -> AI Confidence: **99.39%**
1767. **`usr/src/uts/sun4u/io/pci/pci_util.c`** -> AI Confidence: **99.39%**
1768. **`usr/src/uts/sun4u/io/pci/pcix.c`** -> AI Confidence: **99.39%**
1769. **`usr/src/uts/sun4u/io/px/px_hlib.c`** -> AI Confidence: **99.39%**
1770. **`usr/src/uts/sun4u/io/sbbc.c`** -> AI Confidence: **99.39%**
1771. **`usr/src/uts/sun4u/io/sbd.c`** -> AI Confidence: **99.39%**
1772. **`usr/src/uts/sun4u/io/sbd_mem.c`** -> AI Confidence: **99.39%**
1773. **`usr/src/uts/sun4u/opl/io/dr_mem.c`** -> AI Confidence: **99.39%**
1774. **`usr/src/uts/sun4u/opl/io/oplmsu/oplmsu_cmn_func.c`** -> AI Confidence: **99.39%**
1775. **`usr/src/uts/sun4u/os/fillsysinfo.c`** -> AI Confidence: **99.39%**
1776. **`usr/src/uts/sun4u/os/mach_trap.c`** -> AI Confidence: **99.39%**
1777. **`usr/src/uts/sun4u/serengeti/io/sbdp_error.c`** -> AI Confidence: **99.39%**
1778. **`usr/src/uts/sun4u/serengeti/io/sbdp_mbox.c`** -> AI Confidence: **99.39%**
1779. **`usr/src/uts/sun4u/serengeti/io/sghsc.c`** -> AI Confidence: **99.39%**
1780. **`usr/src/uts/sun4u/serengeti/os/sg_unum.c`** -> AI Confidence: **99.39%**
1781. **`usr/src/uts/sun4u/vm/mach_kpm.c`** -> AI Confidence: **99.39%**
1782. **`usr/src/uts/sun4v/cpu/niagara2.c`** -> AI Confidence: **99.39%**
1783. **`usr/src/uts/sun4v/cpu/niagara_perfctr.c`** -> AI Confidence: **99.39%**
1784. **`usr/src/uts/sun4v/io/dr_mem.c`** -> AI Confidence: **99.39%**
1785. **`usr/src/uts/sun4v/io/glvc/glvc.c`** -> AI Confidence: **99.39%**
1786. **`usr/src/uts/sun4v/io/n2rng/n2rng.c`** -> AI Confidence: **99.39%**
1787. **`usr/src/uts/sun4v/io/vdsk_common.c`** -> AI Confidence: **99.39%**
1788. **`usr/src/uts/sun4v/io/vio_util.c`** -> AI Confidence: **99.39%**
1789. **`usr/src/uts/sun4v/os/fillsysinfo.c`** -> AI Confidence: **99.39%**
1790. **`usr/src/uts/sun4v/os/mach_trap.c`** -> AI Confidence: **99.39%**
1791. **`usr/src/uts/sun4v/os/ppage.c`** -> AI Confidence: **99.39%**
1792. **`usr/src/contrib/ast/src/cmd/INIT/package.sh`** -> AI Confidence: **99.39%**
1793. **`usr/src/cmd/krb5/kadmin/cli/getdate.y`** -> AI Confidence: **99.39%**
1794. **`usr/src/cmd/audio/audioconvert/convert.cc`** -> AI Confidence: **99.39%**
1795. **`usr/src/cmd/make/bin/parallel.cc`** -> AI Confidence: **99.39%**
1796. **`usr/src/cmd/make/lib/mksh/dosys.cc`** -> AI Confidence: **99.39%**
1797. **`usr/src/lib/libnisdb/db.cc`** -> AI Confidence: **99.39%**
1798. **`usr/src/lib/libnisdb/db_entry.cc`** -> AI Confidence: **99.39%**
1799. **`usr/src/lib/libnisdb/db_index.cc`** -> AI Confidence: **99.39%**
1800. **`usr/src/lib/libnisdb/db_mindex2.cc`** -> AI Confidence: **99.39%**
1801. **`usr/src/lib/libnisdb/db_mindex3.cc`** -> AI Confidence: **99.39%**
1802. **`usr/src/lib/libnisdb/db_table.cc`** -> AI Confidence: **99.39%**
1803. **`usr/src/lib/sun_fc/common/HBA.cc`** -> AI Confidence: **99.39%**
1804. **`usr/src/lib/sun_fc/common/HBAList.cc`** -> AI Confidence: **99.39%**
1805. **`usr/src/lib/pyzfs/common/allow.py`** -> AI Confidence: **99.39%**
1806. **`usr/src/boot/efi/loader/main.c`** -> AI Confidence: **99.35%**
1807. **`usr/src/cmd/bhyve/common/bhyverun.c`** -> AI Confidence: **99.35%**
1808. **`usr/src/cmd/cmd-crypto/kmfcfg/install.c`** -> AI Confidence: **99.35%**
1809. **`usr/src/cmd/cmd-inet/usr.sbin/ipadm/ipadm.c`** -> AI Confidence: **99.35%**
1810. **`usr/src/cmd/cmd-inet/usr.sbin/ipsecutils/ipsecalgs.c`** -> AI Confidence: **99.35%**
1811. **`usr/src/cmd/cmd-inet/usr.sbin/nwamadm/nwamadm.c`** -> AI Confidence: **99.35%**
1812. **`usr/src/cmd/date/date.c`** -> AI Confidence: **99.35%**
1813. **`usr/src/cmd/fs.d/autofs/autod_mount.c`** -> AI Confidence: **99.35%**
1814. **`usr/src/cmd/fs.d/autofs/mount.c`** -> AI Confidence: **99.35%**
1815. **`usr/src/cmd/fs.d/lofs/mount/mount.c`** -> AI Confidence: **99.35%**
1816. **`usr/src/cmd/fs.d/nfs/lib/nfslogtab.c`** -> AI Confidence: **99.35%**
1817. **`usr/src/cmd/fs.d/nfs/statd/sm_svc.c`** -> AI Confidence: **99.35%**
1818. **`usr/src/cmd/fs.d/smbclnt/lsacl/lsacl.c`** -> AI Confidence: **99.35%**
1819. **`usr/src/cmd/fs.d/smbclnt/smbutil/status.c`** -> AI Confidence: **99.35%**
1820. **`usr/src/cmd/fs.d/tmpfs/mount.c`** -> AI Confidence: **99.35%**
1821. **`usr/src/cmd/geniconvtbl/itmcomp.c`** -> AI Confidence: **99.35%**
1822. **`usr/src/cmd/hal/hald/solaris/devinfo_storage.c`** -> AI Confidence: **99.35%**
1823. **`usr/src/cmd/hal/hald/solaris/sysevent.c`** -> AI Confidence: **99.35%**
1824. **`usr/src/cmd/hal/probing/storage/probe-storage.c`** -> AI Confidence: **99.35%**
1825. **`usr/src/cmd/ipcs/ipcs.c`** -> AI Confidence: **99.35%**
1826. **`usr/src/cmd/isns/isnsd/dd.c`** -> AI Confidence: **99.35%**
1827. **`usr/src/cmd/kbd/kbd.c`** -> AI Confidence: **99.35%**
1828. **`usr/src/cmd/krb5/kadmin/server/ipropd_svc.c`** -> AI Confidence: **99.35%**
1829. **`usr/src/cmd/ktest/ktest.c`** -> AI Confidence: **99.35%**
1830. **`usr/src/cmd/mandoc/mdoc.c`** -> AI Confidence: **99.35%**
1831. **`usr/src/cmd/mandoc/mdoc_term.c`** -> AI Confidence: **99.35%**
1832. **`usr/src/cmd/mdb/common/mdb/mdb.c`** -> AI Confidence: **99.35%**
1833. **`usr/src/cmd/mdb/common/mdb/mdb_print.c`** -> AI Confidence: **99.35%**
1834. **`usr/src/cmd/mdb/common/modules/sctp/sctp.c`** -> AI Confidence: **99.35%**
1835. **`usr/src/cmd/picl/plugins/sun4u/lw8/frutree/piclfrutree.c`** -> AI Confidence: **99.35%**
1836. **`usr/src/cmd/plockstat/plockstat.c`** -> AI Confidence: **99.35%**
1837. **`usr/src/cmd/prtfru/prtfru.c`** -> AI Confidence: **99.35%**
1838. **`usr/src/cmd/psrset/psrset.c`** -> AI Confidence: **99.35%**
1839. **`usr/src/cmd/renice/renice.c`** -> AI Confidence: **99.35%**
1840. **`usr/src/cmd/sgs/libld/common/map.c`** -> AI Confidence: **99.35%**
1841. **`usr/src/cmd/sgs/link_audit/common/truss.c`** -> AI Confidence: **99.35%**
1842. **`usr/src/cmd/sgs/rtld/common/setup.c`** -> AI Confidence: **99.35%**
1843. **`usr/src/cmd/svr4pkg/installf/dofinal.c`** -> AI Confidence: **99.35%**
1844. **`usr/src/cmd/svr4pkg/libinst/setadmin.c`** -> AI Confidence: **99.35%**
1845. **`usr/src/cmd/svr4pkg/pkginstall/main.c`** -> AI Confidence: **99.35%**
1846. **`usr/src/cmd/svr4pkg/pkgmk/mkpkgmap.c`** -> AI Confidence: **99.35%**
1847. **`usr/src/cmd/svr4pkg/pkgserv/pkgserv.c`** -> AI Confidence: **99.35%**
1848. **`usr/src/cmd/tabs/tabs.c`** -> AI Confidence: **99.35%**
1849. **`usr/src/cmd/tr/str.c`** -> AI Confidence: **99.35%**
1850. **`usr/src/cmd/vntsd/common.c`** -> AI Confidence: **99.35%**
1851. **`usr/src/cmd/vtfontcvt/vtfontcvt.c`** -> AI Confidence: **99.35%**
1852. **`usr/src/cmd/ypcmd/yp_b_svc.c`** -> AI Confidence: **99.35%**
1853. **`usr/src/lib/fm/topo/modules/common/fac_prov_mptsas/fac_prov_mptsas.c`** -> AI Confidence: **99.35%**
1854. **`usr/src/lib/fm/topo/modules/i86pc/chip/chip_smbios.c`** -> AI Confidence: **99.35%**
1855. **`usr/src/lib/gss_mechs/mech_krb5/support/plugins.c`** -> AI Confidence: **99.35%**
1856. **`usr/src/lib/krb5/kadm5/clnt/logger.c`** -> AI Confidence: **99.35%**
1857. **`usr/src/lib/lib9p/common/genacl.c`** -> AI Confidence: **99.35%**
1858. **`usr/src/lib/libbe/common/be_create.c`** -> AI Confidence: **99.35%**
1859. **`usr/src/lib/libc/port/fp/sigfpe.c`** -> AI Confidence: **99.35%**
1860. **`usr/src/lib/libc/port/regex/regfree.c`** -> AI Confidence: **99.35%**
1861. **`usr/src/lib/libc/port/stdio/fopen.c`** -> AI Confidence: **99.35%**
1862. **`usr/src/lib/libdevinfo/devfsmap.c`** -> AI Confidence: **99.35%**
1863. **`usr/src/lib/libkmf/libkmf/common/certgetsetop.c`** -> AI Confidence: **99.35%**
1864. **`usr/src/lib/libldap5/sources/ldap/common/digest_md5.c`** -> AI Confidence: **99.35%**
1865. **`usr/src/lib/libnsl/nsl/t_rcvrel.c`** -> AI Confidence: **99.35%**
1866. **`usr/src/lib/libpkg/common/pkgmount.c`** -> AI Confidence: **99.35%**
1867. **`usr/src/lib/libresolv2/common/isc/eventlib.c`** -> AI Confidence: **99.35%**
1868. **`usr/src/lib/libsasl/include/config.h`** -> AI Confidence: **99.35%**
1869. **`usr/src/lib/libsasl/lib/dlopen.c`** -> AI Confidence: **99.35%**
1870. **`usr/src/lib/libsmbfs/smb/connect.c`** -> AI Confidence: **99.35%**
1871. **`usr/src/lib/libzfs/common/libzfs_import.c`** -> AI Confidence: **99.35%**
1872. **`usr/src/lib/pam_modules/krb5/krb5_acct_mgmt.c`** -> AI Confidence: **99.35%**
1873. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softMAC.c`** -> AI Confidence: **99.35%**
1874. **`usr/src/lib/smbclnt/libfksmbfs/common/fake_unlink.c`** -> AI Confidence: **99.35%**
1875. **`usr/src/lib/smbsrv/libfksmbsrv/common/fake_ksocket.c`** -> AI Confidence: **99.35%**
1876. **`usr/src/stand/lib/fs/nfs/nfs2ops.c`** -> AI Confidence: **99.35%**
1877. **`usr/src/stand/lib/sock/socket.c`** -> AI Confidence: **99.35%**
1878. **`usr/src/test/bhyve-tests/tests/inst_emul/exit_paging.c`** -> AI Confidence: **99.35%**
1879. **`usr/src/uts/common/crypto/io/md5_mod.c`** -> AI Confidence: **99.35%**
1880. **`usr/src/uts/common/disp/ts.c`** -> AI Confidence: **99.35%**
1881. **`usr/src/uts/common/fs/lookup.c`** -> AI Confidence: **99.35%**
1882. **`usr/src/uts/common/fs/nfs/nfs4x_dispatch.c`** -> AI Confidence: **99.35%**
1883. **`usr/src/uts/common/fs/pcfs/pc_vfsops.c`** -> AI Confidence: **99.35%**
1884. **`usr/src/uts/common/fs/sharefs/sharetab.c`** -> AI Confidence: **99.35%**
1885. **`usr/src/uts/common/fs/zfs/dsl_prop.c`** -> AI Confidence: **99.35%**
1886. **`usr/src/uts/common/fs/zfs/vdev_removal.c`** -> AI Confidence: **99.35%**
1887. **`usr/src/uts/common/fs/zfs/zfs_znode.c`** -> AI Confidence: **99.35%**
1888. **`usr/src/uts/common/inet/ilb/ilb_conn.c`** -> AI Confidence: **99.35%**
1889. **`usr/src/uts/common/inet/ip/ip_ire.c`** -> AI Confidence: **99.35%**
1890. **`usr/src/uts/common/inet/sctp/sctp.c`** -> AI Confidence: **99.35%**
1891. **`usr/src/uts/common/inet/tcp/tcp.c`** -> AI Confidence: **99.35%**
1892. **`usr/src/uts/common/inet/tunables.c`** -> AI Confidence: **99.35%**
1893. **`usr/src/uts/common/io/1394/s1394_dev_disc.c`** -> AI Confidence: **99.35%**
1894. **`usr/src/uts/common/io/atge/atge_l1.c`** -> AI Confidence: **99.35%**
1895. **`usr/src/uts/common/io/comstar/port/srpt/srpt_cm.c`** -> AI Confidence: **99.35%**
1896. **`usr/src/uts/common/io/ib/clients/of/sol_uverbs/sol_uverbs_qp.c`** -> AI Confidence: **99.35%**
1897. **`usr/src/uts/common/io/ib/mgt/ibcm/ibcm_arp.c`** -> AI Confidence: **99.35%**
1898. **`usr/src/uts/common/io/kbtrans/kbtrans.c`** -> AI Confidence: **99.35%**
1899. **`usr/src/uts/common/io/mac/mac_client.c`** -> AI Confidence: **99.35%**
1900. **`usr/src/uts/common/io/ntxn/unm_nic_hw.c`** -> AI Confidence: **99.35%**
1901. **`usr/src/uts/common/io/ppm/ppm_subr.c`** -> AI Confidence: **99.35%**
1902. **`usr/src/uts/common/io/sata/adapters/ahci/ahci.c`** -> AI Confidence: **99.35%**
1903. **`usr/src/uts/common/io/sata/impl/sata.c`** -> AI Confidence: **99.35%**
1904. **`usr/src/uts/common/io/sfxge/sfxge_rx.c`** -> AI Confidence: **99.35%**
1905. **`usr/src/uts/common/io/sfxge/sfxge_tx.c`** -> AI Confidence: **99.35%**
1906. **`usr/src/uts/common/io/wpi/wpi.c`** -> AI Confidence: **99.35%**
1907. **`usr/src/uts/common/os/kmem.c`** -> AI Confidence: **99.35%**
1908. **`usr/src/uts/common/os/move.c`** -> AI Confidence: **99.35%**
1909. **`usr/src/uts/common/os/pcifm.c`** -> AI Confidence: **99.35%**
1910. **`usr/src/uts/common/os/rwlock.c`** -> AI Confidence: **99.35%**
1911. **`usr/src/uts/common/os/timers.c`** -> AI Confidence: **99.35%**
1912. **`usr/src/uts/common/os/vmem.c`** -> AI Confidence: **99.35%**
1913. **`usr/src/uts/common/pcmcia/cis/cis.c`** -> AI Confidence: **99.35%**
1914. **`usr/src/uts/common/pcmcia/nexus/pcmcia.c`** -> AI Confidence: **99.35%**
1915. **`usr/src/uts/common/syscall/chdir.c`** -> AI Confidence: **99.35%**
1916. **`usr/src/uts/common/syscall/ppriv.c`** -> AI Confidence: **99.35%**
1917. **`usr/src/uts/common/syscall/pset.c`** -> AI Confidence: **99.35%**
1918. **`usr/src/uts/common/syscall/rename.c`** -> AI Confidence: **99.35%**
1919. **`usr/src/uts/common/syscall/sigaction.c`** -> AI Confidence: **99.35%**
1920. **`usr/src/uts/i86pc/cpu/authenticamd/authamd_main.c`** -> AI Confidence: **99.35%**
1921. **`usr/src/uts/i86pc/os/lgrpplat.c`** -> AI Confidence: **99.35%**
1922. **`usr/src/uts/i86xpv/os/mp_xen.c`** -> AI Confidence: **99.35%**
1923. **`usr/src/uts/intel/io/fdc.c`** -> AI Confidence: **99.35%**
1924. **`usr/src/uts/intel/os/sysi86.c`** -> AI Confidence: **99.35%**
1925. **`usr/src/uts/sun4/io/px/px_devctl.c`** -> AI Confidence: **99.35%**
1926. **`usr/src/uts/sun4u/io/i2c/clients/adm1031.c`** -> AI Confidence: **99.35%**
1927. **`usr/src/uts/sun4u/sunfire/io/sysctrl_dr.c`** -> AI Confidence: **99.35%**
1928. **`usr/src/uts/sun4v/io/pciex/pci_cfgacc_4v.c`** -> AI Confidence: **99.35%**
1929. **`usr/src/lib/libnisdb/db_mindex.cc`** -> AI Confidence: **99.35%**
1930. **`usr/src/lib/libnisdb/nis_db.cc`** -> AI Confidence: **99.35%**
1931. **`usr/src/boot/common/interp_forth.c`** -> AI Confidence: **99.34%**
1932. **`usr/src/boot/efi/libefi/efichar.c`** -> AI Confidence: **99.34%**
1933. **`usr/src/boot/efi/loader/reloc.c`** -> AI Confidence: **99.34%**
1934. **`usr/src/boot/i386/libi386/cpuid.c`** -> AI Confidence: **99.34%**
1935. **`usr/src/cmd/acct/accton.c`** -> AI Confidence: **99.34%**
1936. **`usr/src/cmd/acpi/common/dmtable.c`** -> AI Confidence: **99.34%**
1937. **`usr/src/cmd/acpi/iasl/asllisting.c`** -> AI Confidence: **99.34%**
1938. **`usr/src/cmd/acpi/iasl/aslload.c`** -> AI Confidence: **99.34%**
1939. **`usr/src/cmd/acpi/iasl/aslopt.c`** -> AI Confidence: **99.34%**
1940. **`usr/src/cmd/acpi/iasl/aslxref.c`** -> AI Confidence: **99.34%**
1941. **`usr/src/cmd/acpi/iasl/cvcompiler.c`** -> AI Confidence: **99.34%**
1942. **`usr/src/cmd/awk/lex.c`** -> AI Confidence: **99.34%**
1943. **`usr/src/cmd/awk/maketab.c`** -> AI Confidence: **99.34%**
1944. **`usr/src/cmd/awk_xpg4/awk1.c`** -> AI Confidence: **99.34%**
1945. **`usr/src/cmd/cmd-crypto/cryptoadm/adm_util.c`** -> AI Confidence: **99.34%**
1946. **`usr/src/cmd/cmd-crypto/pktool/delete.c`** -> AI Confidence: **99.34%**
1947. **`usr/src/cmd/cmd-crypto/pktool/import.c`** -> AI Confidence: **99.34%**
1948. **`usr/src/cmd/cmd-inet/sbin/dhcpinfo/dhcpinfo.c`** -> AI Confidence: **99.34%**
1949. **`usr/src/cmd/cmd-inet/usr.bin/pppd/ccp.c`** -> AI Confidence: **99.34%**
1950. **`usr/src/cmd/cmd-inet/usr.bin/pppd/fsm.c`** -> AI Confidence: **99.34%**
1951. **`usr/src/cmd/cmd-inet/usr.bin/talk/get_names.c`** -> AI Confidence: **99.34%**
1952. **`usr/src/cmd/cmd-inet/usr.bin/telnet/main.c`** -> AI Confidence: **99.34%**
1953. **`usr/src/cmd/cmd-inet/usr.bin/telnet/network.c`** -> AI Confidence: **99.34%**
1954. **`usr/src/cmd/cmd-inet/usr.sbin/in.fingerd.c`** -> AI Confidence: **99.34%**
1955. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_slp.c`** -> AI Confidence: **99.34%**
1956. **`usr/src/cmd/col/col.c`** -> AI Confidence: **99.34%**
1957. **`usr/src/cmd/ctfdiff/ctfdiff.c`** -> AI Confidence: **99.34%**
1958. **`usr/src/cmd/devfsadm/devfsadm.c`** -> AI Confidence: **99.34%**
1959. **`usr/src/cmd/drd/drd_rcm.c`** -> AI Confidence: **99.34%**
1960. **`usr/src/cmd/dtrace/test/cmd/badioctl/badioctl.c`** -> AI Confidence: **99.34%**
1961. **`usr/src/cmd/emul64ioctl/emul64ioctl.c`** -> AI Confidence: **99.34%**
1962. **`usr/src/cmd/filesync/recon.c`** -> AI Confidence: **99.34%**
1963. **`usr/src/cmd/fs.d/fssnapsup.c`** -> AI Confidence: **99.34%**
1964. **`usr/src/cmd/fs.d/smbclnt/smbutil/view.c`** -> AI Confidence: **99.34%**
1965. **`usr/src/cmd/fs.d/volcopy.c`** -> AI Confidence: **99.34%**
1966. **`usr/src/cmd/getent/dogetnetgr.c`** -> AI Confidence: **99.34%**
1967. **`usr/src/cmd/gettext/gettext.c`** -> AI Confidence: **99.34%**
1968. **`usr/src/cmd/idmap/idmap/idmap_engine.c`** -> AI Confidence: **99.34%**
1969. **`usr/src/cmd/idmap/idmapd/idmap_lsa.c`** -> AI Confidence: **99.34%**
1970. **`usr/src/cmd/idmap/idmapd/init.c`** -> AI Confidence: **99.34%**
1971. **`usr/src/cmd/ipf/lib/load_hash.c`** -> AI Confidence: **99.34%**
1972. **`usr/src/cmd/keyserv/keylogout.c`** -> AI Confidence: **99.34%**
1973. **`usr/src/cmd/krb5/kadmin/dbutil/kdb5_destroy.c`** -> AI Confidence: **99.34%**
1974. **`usr/src/cmd/krb5/kadmin/kclient/kconf.c`** -> AI Confidence: **99.34%**
1975. **`usr/src/cmd/krb5/ldap_util/kdb5_ldap_services.c`** -> AI Confidence: **99.34%**
1976. **`usr/src/cmd/localedef/messages.c`** -> AI Confidence: **99.34%**
1977. **`usr/src/cmd/lp/lib/access/dumpaccess.c`** -> AI Confidence: **99.34%**
1978. **`usr/src/cmd/lp/lib/filters/conv.c`** -> AI Confidence: **99.34%**
1979. **`usr/src/cmd/lp/lib/filters/getfilter.c`** -> AI Confidence: **99.34%**
1980. **`usr/src/cmd/lp/lib/lp/makepath.c`** -> AI Confidence: **99.34%**
1981. **`usr/src/cmd/lp/lib/lp/makestr.c`** -> AI Confidence: **99.34%**
1982. **`usr/src/cmd/lp/lib/lp/set_charset.c`** -> AI Confidence: **99.34%**
1983. **`usr/src/cmd/lp/lib/lp/tx.c`** -> AI Confidence: **99.34%**
1984. **`usr/src/cmd/lp/lib/printers/freeprinter.c`** -> AI Confidence: **99.34%**
1985. **`usr/src/cmd/lp/lib/printers/okprinter.c`** -> AI Confidence: **99.34%**
1986. **`usr/src/cmd/lp/model/lp.tell.c`** -> AI Confidence: **99.34%**
1987. **`usr/src/cmd/mailwrapper/mailwrapper.c`** -> AI Confidence: **99.34%**
1988. **`usr/src/cmd/mdb/common/kmdb/kaif_start.c`** -> AI Confidence: **99.34%**
1989. **`usr/src/cmd/mdb/common/mdb/mdb_argvec.c`** -> AI Confidence: **99.34%**
1990. **`usr/src/cmd/mdb/common/mdb/mdb_dump.c`** -> AI Confidence: **99.34%**
1991. **`usr/src/cmd/mdb/common/mdb/mdb_evset.c`** -> AI Confidence: **99.34%**
1992. **`usr/src/cmd/mdb/common/modules/crypto/sched_impl.c`** -> AI Confidence: **99.34%**
1993. **`usr/src/cmd/mkpwdict/mkpwdict.c`** -> AI Confidence: **99.34%**
1994. **`usr/src/cmd/nscd/nscd_cfgfile.c`** -> AI Confidence: **99.34%**
1995. **`usr/src/cmd/nscd/nscd_nswparse.c`** -> AI Confidence: **99.34%**
1996. **`usr/src/cmd/policykit/polkit-is-privileged.c`** -> AI Confidence: **99.34%**
1997. **`usr/src/cmd/pptadm/pptadm.c`** -> AI Confidence: **99.34%**
1998. **`usr/src/cmd/rpcbind/pmap_svc.c`** -> AI Confidence: **99.34%**
1999. **`usr/src/cmd/rpcgen/rpc_clntout.c`** -> AI Confidence: **99.34%**
2000. **`usr/src/cmd/saf/pmadm.c`** -> AI Confidence: **99.34%**
2001. **`usr/src/cmd/scadm/sparc/mpxu/common/process_command.c`** -> AI Confidence: **99.34%**
2002. **`usr/src/cmd/sendmail/db/btree/bt_curadj.c`** -> AI Confidence: **99.34%**
2003. **`usr/src/cmd/sendmail/db/os/os_dir.c`** -> AI Confidence: **99.34%**
2004. **`usr/src/cmd/sendmail/db/os/os_oflags.c`** -> AI Confidence: **99.34%**
2005. **`usr/src/cmd/sendmail/db/os/os_seek.c`** -> AI Confidence: **99.34%**
2006. **`usr/src/cmd/sendmail/libsm/config.c`** -> AI Confidence: **99.34%**
2007. **`usr/src/cmd/sendmail/libsm/flags.c`** -> AI Confidence: **99.34%**
2008. **`usr/src/cmd/sendmail/libsm/snprintf.c`** -> AI Confidence: **99.34%**
2009. **`usr/src/cmd/sendmail/libsm/util.c`** -> AI Confidence: **99.34%**
2010. **`usr/src/cmd/sendmail/libsm/wsetup.c`** -> AI Confidence: **99.34%**
2011. **`usr/src/cmd/sgs/libconv/common/config.c`** -> AI Confidence: **99.34%**
2012. **`usr/src/cmd/sgs/libconv/common/dwarf_ehe.c`** -> AI Confidence: **99.34%**
2013. **`usr/src/cmd/sgs/libld/common/ldmain.c`** -> AI Confidence: **99.34%**
2014. **`usr/src/cmd/sgs/libld/common/syms.c`** -> AI Confidence: **99.34%**
2015. **`usr/src/cmd/sgs/libld/common/update.c`** -> AI Confidence: **99.34%**
2016. **`usr/src/cmd/sgs/librtld/common/dynamic.c`** -> AI Confidence: **99.34%**
2017. **`usr/src/cmd/sgs/librtld_db/sparc/plt32_resolution.c`** -> AI Confidence: **99.34%**
2018. **`usr/src/cmd/sgs/librtld_db/sparcv9/plt64_resolution.c`** -> AI Confidence: **99.34%**
2019. **`usr/src/cmd/sh/bltin.c`** -> AI Confidence: **99.34%**
2020. **`usr/src/cmd/sh/pwd.c`** -> AI Confidence: **99.34%**
2021. **`usr/src/cmd/sh/xec.c`** -> AI Confidence: **99.34%**
2022. **`usr/src/cmd/tsol/atohexlabel/atohexlabel.c`** -> AI Confidence: **99.34%**
2023. **`usr/src/cmd/tsol/hextoalabel/hextoalabel.c`** -> AI Confidence: **99.34%**
2024. **`usr/src/cmd/vi/port/ex_cmds.c`** -> AI Confidence: **99.34%**
2025. **`usr/src/cmd/vi/port/ex_cmdsub.c`** -> AI Confidence: **99.34%**
2026. **`usr/src/cmd/vi/port/ex_voper.c`** -> AI Confidence: **99.34%**
2027. **`usr/src/common/acpica/disassembler/dmcstyle.c`** -> AI Confidence: **99.34%**
2028. **`usr/src/common/acpica/disassembler/dmdeferred.c`** -> AI Confidence: **99.34%**
2029. **`usr/src/common/acpica/disassembler/dmnames.c`** -> AI Confidence: **99.34%**
2030. **`usr/src/common/acpica/disassembler/dmutils.c`** -> AI Confidence: **99.34%**
2031. **`usr/src/common/acpica/disassembler/dmwalk.c`** -> AI Confidence: **99.34%**
2032. **`usr/src/common/acpica/dispatcher/dsargs.c`** -> AI Confidence: **99.34%**
2033. **`usr/src/common/acpica/dispatcher/dscontrol.c`** -> AI Confidence: **99.34%**
2034. **`usr/src/common/acpica/dispatcher/dsinit.c`** -> AI Confidence: **99.34%**
2035. **`usr/src/common/acpica/dispatcher/dsmthdat.c`** -> AI Confidence: **99.34%**
2036. **`usr/src/common/acpica/events/evregion.c`** -> AI Confidence: **99.34%**
2037. **`usr/src/common/acpica/events/evxface.c`** -> AI Confidence: **99.34%**
2038. **`usr/src/common/acpica/executer/excreate.c`** -> AI Confidence: **99.34%**
2039. **`usr/src/common/acpica/executer/exdump.c`** -> AI Confidence: **99.34%**
2040. **`usr/src/common/acpica/executer/exfield.c`** -> AI Confidence: **99.34%**
2041. **`usr/src/common/acpica/executer/exfldio.c`** -> AI Confidence: **99.34%**
2042. **`usr/src/common/acpica/executer/exoparg2.c`** -> AI Confidence: **99.34%**
2043. **`usr/src/common/acpica/executer/exoparg3.c`** -> AI Confidence: **99.34%**
2044. **`usr/src/common/acpica/executer/exoparg6.c`** -> AI Confidence: **99.34%**
2045. **`usr/src/common/acpica/executer/exprep.c`** -> AI Confidence: **99.34%**
2046. **`usr/src/common/acpica/executer/exresnte.c`** -> AI Confidence: **99.34%**
2047. **`usr/src/common/acpica/executer/exresolv.c`** -> AI Confidence: **99.34%**
2048. **`usr/src/common/acpica/executer/exresop.c`** -> AI Confidence: **99.34%**
2049. **`usr/src/common/acpica/executer/exstore.c`** -> AI Confidence: **99.34%**
2050. **`usr/src/common/acpica/namespace/nsaccess.c`** -> AI Confidence: **99.34%**
2051. **`usr/src/common/acpica/namespace/nseval.c`** -> AI Confidence: **99.34%**
2052. **`usr/src/common/acpica/namespace/nsload.c`** -> AI Confidence: **99.34%**
2053. **`usr/src/common/acpica/parser/psobject.c`** -> AI Confidence: **99.34%**
2054. **`usr/src/common/acpica/parser/psopinfo.c`** -> AI Confidence: **99.34%**
2055. **`usr/src/common/acpica/parser/pstree.c`** -> AI Confidence: **99.34%**
2056. **`usr/src/common/acpica/utilities/utdelete.c`** -> AI Confidence: **99.34%**
2057. **`usr/src/common/acpica/utilities/utxfinit.c`** -> AI Confidence: **99.34%**
2058. **`usr/src/common/crypto/ecc/ecl_curve.c`** -> AI Confidence: **99.34%**
2059. **`usr/src/common/crypto/ecc/ecl_gf.c`** -> AI Confidence: **99.34%**
2060. **`usr/src/common/crypto/ecc/ecl_mult.c`** -> AI Confidence: **99.34%**
2061. **`usr/src/common/crypto/ecc/ecp_192.c`** -> AI Confidence: **99.34%**
2062. **`usr/src/common/crypto/ecc/ecp_224.c`** -> AI Confidence: **99.34%**
2063. **`usr/src/common/crypto/ecc/ecp_256.c`** -> AI Confidence: **99.34%**
2064. **`usr/src/common/crypto/ecc/ecp_384.c`** -> AI Confidence: **99.34%**
2065. **`usr/src/common/crypto/edonr/edonr.c`** -> AI Confidence: **99.34%**
2066. **`usr/src/common/crypto/md5/md5.c`** -> AI Confidence: **99.34%**
2067. **`usr/src/common/iscsi/base64.c`** -> AI Confidence: **99.34%**
2068. **`usr/src/common/mpi/mpmontg.c`** -> AI Confidence: **99.34%**
2069. **`usr/src/common/util/sscanf.c`** -> AI Confidence: **99.34%**
2070. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/cflow.c`** -> AI Confidence: **99.34%**
2071. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/getopts.c`** -> AI Confidence: **99.34%**
2072. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/mkservice.c`** -> AI Confidence: **99.34%**
2073. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/regress.c`** -> AI Confidence: **99.34%**
2074. **`usr/src/contrib/ast/src/cmd/ksh93/sh/arith.c`** -> AI Confidence: **99.34%**
2075. **`usr/src/contrib/ast/src/cmd/ksh93/sh/bash.c`** -> AI Confidence: **99.34%**
2076. **`usr/src/contrib/ast/src/cmd/ksh93/sh/streval.c`** -> AI Confidence: **99.34%**
2077. **`usr/src/contrib/ast/src/cmd/ksh93/sh/timers.c`** -> AI Confidence: **99.34%**
2078. **`usr/src/contrib/ast/src/cmd/msgcc/msggen.c`** -> AI Confidence: **99.34%**
2079. **`usr/src/contrib/ast/src/lib/libast/comp/fcntl.c`** -> AI Confidence: **99.34%**
2080. **`usr/src/contrib/ast/src/lib/libast/comp/getoptl.c`** -> AI Confidence: **99.34%**
2081. **`usr/src/contrib/ast/src/lib/libast/comp/strtold.c`** -> AI Confidence: **99.34%**
2082. **`usr/src/contrib/ast/src/lib/libast/disc/sfkeyprintf.c`** -> AI Confidence: **99.34%**
2083. **`usr/src/contrib/ast/src/lib/libast/features/map.c`** -> AI Confidence: **99.34%**
2084. **`usr/src/contrib/ast/src/lib/libast/misc/cmdarg.c`** -> AI Confidence: **99.34%**
2085. **`usr/src/contrib/ast/src/lib/libast/misc/fts.c`** -> AI Confidence: **99.34%**
2086. **`usr/src/contrib/ast/src/lib/libast/misc/optget.c`** -> AI Confidence: **99.34%**
2087. **`usr/src/contrib/ast/src/lib/libast/misc/procopen.c`** -> AI Confidence: **99.34%**
2088. **`usr/src/contrib/ast/src/lib/libast/misc/translate.c`** -> AI Confidence: **99.34%**
2089. **`usr/src/contrib/ast/src/lib/libast/path/pathcanon.c`** -> AI Confidence: **99.34%**
2090. **`usr/src/contrib/ast/src/lib/libast/path/pathcheck.c`** -> AI Confidence: **99.34%**
2091. **`usr/src/contrib/ast/src/lib/libast/path/pathkey.c`** -> AI Confidence: **99.34%**
2092. **`usr/src/contrib/ast/src/lib/libast/path/pathprobe.c`** -> AI Confidence: **99.34%**
2093. **`usr/src/contrib/ast/src/lib/libast/path/pathprog.c`** -> AI Confidence: **99.34%**
2094. **`usr/src/contrib/ast/src/lib/libast/vmalloc/vmbest.c`** -> AI Confidence: **99.34%**
2095. **`usr/src/contrib/ast/src/lib/libcmd/chgrp.c`** -> AI Confidence: **99.34%**
2096. **`usr/src/contrib/ast/src/lib/libcmd/cksum.c`** -> AI Confidence: **99.34%**
2097. **`usr/src/contrib/ast/src/lib/libcmd/cmd.h`** -> AI Confidence: **99.34%**
2098. **`usr/src/contrib/ast/src/lib/libcmd/date.c`** -> AI Confidence: **99.34%**
2099. **`usr/src/contrib/ast/src/lib/libcmd/fds.c`** -> AI Confidence: **99.34%**
2100. **`usr/src/contrib/ast/src/lib/libcmd/id.c`** -> AI Confidence: **99.34%**
2101. **`usr/src/contrib/ast/src/lib/libcmd/join.c`** -> AI Confidence: **99.34%**
2102. **`usr/src/contrib/ast/src/lib/libcmd/stty.c`** -> AI Confidence: **99.34%**
2103. **`usr/src/contrib/ast/src/lib/libcmd/tail.c`** -> AI Confidence: **99.34%**
2104. **`usr/src/contrib/ast/src/lib/libcmd/uname.c`** -> AI Confidence: **99.34%**
2105. **`usr/src/contrib/ast/src/lib/libcmd/wclib.c`** -> AI Confidence: **99.34%**
2106. **`usr/src/contrib/zlib/infback.c`** -> AI Confidence: **99.34%**
2107. **`usr/src/grub/grub-0.97/lib/getopt1.c`** -> AI Confidence: **99.34%**
2108. **`usr/src/grub/grub-0.97/stage2/disk_io.c`** -> AI Confidence: **99.34%**
2109. **`usr/src/lib/fm/libfmevent/common/fmev_publish.c`** -> AI Confidence: **99.34%**
2110. **`usr/src/lib/fm/topo/modules/i86pc/chip/chip_subr.c`** -> AI Confidence: **99.34%**
2111. **`usr/src/lib/gss_mechs/mech_krb5/krb5/asn.1/krb5_decode.c`** -> AI Confidence: **99.34%**
2112. **`usr/src/lib/gss_mechs/mech_krb5/krb5/asn.1/krb5_encode.c`** -> AI Confidence: **99.34%**
2113. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/deltat.c`** -> AI Confidence: **99.34%**
2114. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/gic_pwd.c`** -> AI Confidence: **99.34%**
2115. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/mk_cred.c`** -> AI Confidence: **99.34%**
2116. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/rd_cred.c`** -> AI Confidence: **99.34%**
2117. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/recvauth.c`** -> AI Confidence: **99.34%**
2118. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/sendauth.c`** -> AI Confidence: **99.34%**
2119. **`usr/src/lib/gss_mechs/mech_krb5/krb5/os/an_to_ln.c`** -> AI Confidence: **99.34%**
2120. **`usr/src/lib/gss_mechs/mech_krb5/mech/import_name.c`** -> AI Confidence: **99.34%**
2121. **`usr/src/lib/gss_mechs/mech_krb5/mech/store_cred.c`** -> AI Confidence: **99.34%**
2122. **`usr/src/lib/iconv_modules/common/cnv_utf8ibm.c`** -> AI Confidence: **99.34%**
2123. **`usr/src/lib/iconv_modules/common/tab_lookup.c`** -> AI Confidence: **99.34%**
2124. **`usr/src/lib/iconv_modules/euro/utils/8859%646fr.c`** -> AI Confidence: **99.34%**
2125. **`usr/src/lib/iconv_modules/euro/utils/8859%646it.c`** -> AI Confidence: **99.34%**
2126. **`usr/src/lib/iconv_modules/euro/utils/8859%646sv.c`** -> AI Confidence: **99.34%**
2127. **`usr/src/lib/iconv_modules/euro/utils/gentbl/rewritetbl.c`** -> AI Confidence: **99.34%**
2128. **`usr/src/lib/iconv_modules/hi_IN/iscii91%UTF-8.c`** -> AI Confidence: **99.34%**
2129. **`usr/src/lib/iconv_modules/ja/common/ISO-2022-JP-2004_TO_Unicode.c`** -> AI Confidence: **99.34%**
2130. **`usr/src/lib/iconv_modules/ja/common/ISO-2022-JP_TO_PCK.c`** -> AI Confidence: **99.34%**
2131. **`usr/src/lib/iconv_modules/ja/common/ISO-2022-JP_TO_eucJP.c`** -> AI Confidence: **99.34%**
2132. **`usr/src/lib/iconv_modules/ja/common/PCK_TO_ISO-2022-JP.c`** -> AI Confidence: **99.34%**
2133. **`usr/src/lib/iconv_modules/ja/common/PCK_TO_Unicode.c`** -> AI Confidence: **99.34%**
2134. **`usr/src/lib/iconv_modules/ja/common/PCK_TO_eucJP.c`** -> AI Confidence: **99.34%**
2135. **`usr/src/lib/iconv_modules/ja/common/PCK_TO_jis.c`** -> AI Confidence: **99.34%**
2136. **`usr/src/lib/iconv_modules/ja/common/eucJP_TO_ISO-2022-JP.c`** -> AI Confidence: **99.34%**
2137. **`usr/src/lib/iconv_modules/ja/common/eucJP_TO_KUTEN.c`** -> AI Confidence: **99.34%**
2138. **`usr/src/lib/iconv_modules/ja/common/eucJP_TO_PCK.c`** -> AI Confidence: **99.34%**
2139. **`usr/src/lib/iconv_modules/ja/common/eucJP_TO_jis.c`** -> AI Confidence: **99.34%**
2140. **`usr/src/lib/iconv_modules/ja/common/jis_TO_PCK.c`** -> AI Confidence: **99.34%**
2141. **`usr/src/lib/iconv_modules/ja/common/jis_TO_eucJP.c`** -> AI Confidence: **99.34%**
2142. **`usr/src/lib/iconv_modules/ko/common/euc_to_nbyte.c`** -> AI Confidence: **99.34%**
2143. **`usr/src/lib/iconv_modules/ko/common/utf_to_euc_main.c`** -> AI Confidence: **99.34%**
2144. **`usr/src/lib/iconv_modules/ko/common/utf_to_johap92.c`** -> AI Confidence: **99.34%**
2145. **`usr/src/lib/iconv_modules/ko/common/utf_to_njh_main.c`** -> AI Confidence: **99.34%**
2146. **`usr/src/lib/iconv_modules/ko/common/utf_to_ojh_main.c`** -> AI Confidence: **99.34%**
2147. **`usr/src/lib/iconv_modules/ko/common/utf_to_uhang_main.c`** -> AI Confidence: **99.34%**
2148. **`usr/src/lib/iconv_modules/th_TH/common/utf_to_euc_main.c`** -> AI Confidence: **99.34%**
2149. **`usr/src/lib/iconv_modules/utf-8/common/sb_to_ucs.c`** -> AI Confidence: **99.34%**
2150. **`usr/src/lib/iconv_modules/utf-8/common/ucs_to_sb.c`** -> AI Confidence: **99.34%**
2151. **`usr/src/lib/iconv_modules/utf-8/common/ucs_to_utf7.c`** -> AI Confidence: **99.34%**
2152. **`usr/src/lib/iconv_modules/utf-8/common/ucs_to_utf8.c`** -> AI Confidence: **99.34%**
2153. **`usr/src/lib/iconv_modules/utf-8/common/utf7_to_ucs.c`** -> AI Confidence: **99.34%**
2154. **`usr/src/lib/iconv_modules/utf-8/common/utf8.c`** -> AI Confidence: **99.34%**
2155. **`usr/src/lib/iconv_modules/utf-8/common/utf8_to_ucs.c`** -> AI Confidence: **99.34%**
2156. **`usr/src/lib/iconv_modules/utf-8/common/utf8_to_utf_ebcdic.c`** -> AI Confidence: **99.34%**
2157. **`usr/src/lib/iconv_modules/utf-8/common/utf_ebcdic_to_utf8.c`** -> AI Confidence: **99.34%**
2158. **`usr/src/lib/iconv_modules/utf-8/utils/cp720_to_ucs4_generator.c`** -> AI Confidence: **99.34%**
2159. **`usr/src/lib/iconv_modules/utf-8/utils/cp720_to_utf8_generator.c`** -> AI Confidence: **99.34%**
2160. **`usr/src/lib/iconv_modules/utf-8/utils/sb_to_ucs4_generator.c`** -> AI Confidence: **99.34%**
2161. **`usr/src/lib/iconv_modules/utf-8/utils/sb_to_utf8_generator.c`** -> AI Confidence: **99.34%**
2162. **`usr/src/lib/iconv_modules/utf-8/utils/ucs4_to_cp720_generator.c`** -> AI Confidence: **99.34%**
2163. **`usr/src/lib/iconv_modules/utf-8/utils/ucs4_to_sb_generator.c`** -> AI Confidence: **99.34%**
2164. **`usr/src/lib/iconv_modules/utf-8/utils/utf8_to_cp720_generator.c`** -> AI Confidence: **99.34%**
2165. **`usr/src/lib/iconv_modules/utf-8/utils/utf8_to_sb_generator.c`** -> AI Confidence: **99.34%**
2166. **`usr/src/lib/iconv_modules/vi/common/UTF-8%viscii.c`** -> AI Confidence: **99.34%**
2167. **`usr/src/lib/iconv_modules/zh/common/UTF-8%HZ-GB-2312.c`** -> AI Confidence: **99.34%**
2168. **`usr/src/lib/iconv_modules/zh/common/UTF-8%zh_TW-iso2022-7.c`** -> AI Confidence: **99.34%**
2169. **`usr/src/lib/iconv_modules/zh/common/zh_CN.gbk%zh_TW-big5.c`** -> AI Confidence: **99.34%**
2170. **`usr/src/lib/iconv_modules/zh/common/zh_CN.gbk%zh_TW-big5p.c`** -> AI Confidence: **99.34%**
2171. **`usr/src/lib/iconv_modules/zh/common/zh_TW-euc%UTF-8.c`** -> AI Confidence: **99.34%**
2172. **`usr/src/lib/krb5/plugins/kdb/db2/adb_policy.c`** -> AI Confidence: **99.34%**
2173. **`usr/src/lib/krb5/plugins/kdb/db2/libdb2/recno/rec_search.c`** -> AI Confidence: **99.34%**
2174. **`usr/src/lib/krb5/plugins/kdb/ldap/libkdb_ldap/kdb_ldap_conn.c`** -> AI Confidence: **99.34%**
2175. **`usr/src/lib/krb5/plugins/kdb/ldap/libkdb_ldap/ldap_principal.c`** -> AI Confidence: **99.34%**
2176. **`usr/src/lib/krb5/plugins/kdb/ldap/libkdb_ldap/ldap_realm.c`** -> AI Confidence: **99.34%**
2177. **`usr/src/lib/krb5/plugins/kdb/ldap/libkdb_ldap/ldap_service_stash.c`** -> AI Confidence: **99.34%**
2178. **`usr/src/lib/krb5/plugins/kdb/ldap/libkdb_ldap/ldap_services.c`** -> AI Confidence: **99.34%**
2179. **`usr/src/lib/krb5/plugins/kdb/ldap/libkdb_ldap/ldap_tkt_policy.c`** -> AI Confidence: **99.34%**
2180. **`usr/src/lib/libadm/common/listdev.c`** -> AI Confidence: **99.34%**
2181. **`usr/src/lib/libc/port/fp/econvert.c`** -> AI Confidence: **99.34%**
2182. **`usr/src/lib/libc/port/fp/func_decim.c`** -> AI Confidence: **99.34%**
2183. **`usr/src/lib/libc/port/fp/gconvert.c`** -> AI Confidence: **99.34%**
2184. **`usr/src/lib/libc/port/gen/ecvt.c`** -> AI Confidence: **99.34%**
2185. **`usr/src/lib/libc/port/gen/strtod.c`** -> AI Confidence: **99.34%**
2186. **`usr/src/lib/libc/port/gen/tcsetattr.c`** -> AI Confidence: **99.34%**
2187. **`usr/src/lib/libc/port/gen/ttyslot.c`** -> AI Confidence: **99.34%**
2188. **`usr/src/lib/libc/port/rt/sched.c`** -> AI Confidence: **99.34%**
2189. **`usr/src/lib/libc/port/stdio/_filbuf.c`** -> AI Confidence: **99.34%**
2190. **`usr/src/lib/libc/port/stdio/_stdio_flags.c`** -> AI Confidence: **99.34%**
2191. **`usr/src/lib/libc/port/sys/lockf.c`** -> AI Confidence: **99.34%**
2192. **`usr/src/lib/libcryptoutil/common/keyfile.c`** -> AI Confidence: **99.34%**
2193. **`usr/src/lib/libcurses/screen/newscreen.c`** -> AI Confidence: **99.34%**
2194. **`usr/src/lib/libdladm/common/usage.c`** -> AI Confidence: **99.34%**
2195. **`usr/src/lib/libdtrace/common/dt_consume.c`** -> AI Confidence: **99.34%**
2196. **`usr/src/lib/libdtrace/common/dt_string.c`** -> AI Confidence: **99.34%**
2197. **`usr/src/lib/libgen/common/gmatch.c`** -> AI Confidence: **99.34%**
2198. **`usr/src/lib/libgen/common/strecpy.c`** -> AI Confidence: **99.34%**
2199. **`usr/src/lib/libkmf/libkmf/common/pem_encode.c`** -> AI Confidence: **99.34%**
2200. **`usr/src/lib/libm/common/C/sincospi.c`** -> AI Confidence: **99.34%**
2201. **`usr/src/lib/libm/common/m9x/__fex_sse.c`** -> AI Confidence: **99.34%**
2202. **`usr/src/lib/libnisdb/ldap_ruleval.c`** -> AI Confidence: **99.34%**
2203. **`usr/src/lib/libnvpair/nvpair_json.c`** -> AI Confidence: **99.34%**
2204. **`usr/src/lib/libpkg/common/mappath.c`** -> AI Confidence: **99.34%**
2205. **`usr/src/lib/libproc/common/pr_fcntl.c`** -> AI Confidence: **99.34%**
2206. **`usr/src/lib/libprtdiag_psr/sparc/daktari/common/workfile.c`** -> AI Confidence: **99.34%**
2207. **`usr/src/lib/libresolv/res_debug.c`** -> AI Confidence: **99.34%**
2208. **`usr/src/lib/libresolv2/common/bsd/strsep.c`** -> AI Confidence: **99.34%**
2209. **`usr/src/lib/libresolv2/common/inet/inet_network.c`** -> AI Confidence: **99.34%**
2210. **`usr/src/lib/libresolv2/common/irs/gai_strerror.c`** -> AI Confidence: **99.34%**
2211. **`usr/src/lib/libresolv2/common/irs/getnetgrent_r.c`** -> AI Confidence: **99.34%**
2212. **`usr/src/lib/libresolv2/common/isc/hex.c`** -> AI Confidence: **99.34%**
2213. **`usr/src/lib/libresolv2/common/isc/tree.c`** -> AI Confidence: **99.34%**
2214. **`usr/src/lib/libsaveargs/amd64/saveargs.c`** -> AI Confidence: **99.34%**
2215. **`usr/src/lib/libslp/clib/slp_utf8.c`** -> AI Confidence: **99.34%**
2216. **`usr/src/lib/libsmbfs/smb/spnegoparse.c`** -> AI Confidence: **99.34%**
2217. **`usr/src/lib/libsocket/inet/link_addr.c`** -> AI Confidence: **99.34%**
2218. **`usr/src/lib/libsocket/socket/_soutil.c`** -> AI Confidence: **99.34%**
2219. **`usr/src/lib/libsqlite/src/date.c`** -> AI Confidence: **99.34%**
2220. **`usr/src/lib/libsqlite/src/tclsqlite.c`** -> AI Confidence: **99.34%**
2221. **`usr/src/lib/libsqlite/test/crashtest1.c`** -> AI Confidence: **99.34%**
2222. **`usr/src/lib/libtecla/common/keytab.c`** -> AI Confidence: **99.34%**
2223. **`usr/src/lib/libtecla/common/pathutil.c`** -> AI Confidence: **99.34%**
2224. **`usr/src/lib/libtsalarm/common/tsalarm.c`** -> AI Confidence: **99.34%**
2225. **`usr/src/lib/libwrap/percent_x.c`** -> AI Confidence: **99.34%**
2226. **`usr/src/lib/libxcurses/h/m_wchar.h`** -> AI Confidence: **99.34%**
2227. **`usr/src/lib/libxcurses/src/libc/xcurses/tparm.c`** -> AI Confidence: **99.34%**
2228. **`usr/src/lib/libzfs/common/libzfs_config.c`** -> AI Confidence: **99.34%**
2229. **`usr/src/lib/libzfsbootenv/common/lzbe_device.c`** -> AI Confidence: **99.34%**
2230. **`usr/src/lib/pam_modules/krb5/utils.c`** -> AI Confidence: **99.34%**
2231. **`usr/src/lib/pkcs11/libpkcs11/common/metaAttrManager.c`** -> AI Confidence: **99.34%**
2232. **`usr/src/lib/pkcs11/libpkcs11/common/metaUtil.c`** -> AI Confidence: **99.34%**
2233. **`usr/src/lib/pkcs11/pkcs11_kernel/common/kernelEncrypt.c`** -> AI Confidence: **99.34%**
2234. **`usr/src/lib/pkcs11/pkcs11_softtoken/common/softKeys.c`** -> AI Confidence: **99.34%**
2235. **`usr/src/lib/print/libpapi-dynamic/common/service.c`** -> AI Confidence: **99.34%**
2236. **`usr/src/lib/smbclnt/libfksmbfs/common/fksmbfs_rwlock.c`** -> AI Confidence: **99.34%**
2237. **`usr/src/lib/smbsrv/libfksmbsrv/common/fake_xattr.c`** -> AI Confidence: **99.34%**
2238. **`usr/src/lib/smbsrv/libsmb/common/smb_acl.c`** -> AI Confidence: **99.34%**
2239. **`usr/src/lib/udapl/udapl_tavor/common/dapl_ep_disconnect.c`** -> AI Confidence: **99.34%**
2240. **`usr/src/lib/udapl/udapl_tavor/common/dapl_ep_free.c`** -> AI Confidence: **99.34%**
2241. **`usr/src/lib/udapl/udapl_tavor/common/dapl_ep_reset.c`** -> AI Confidence: **99.34%**
2242. **`usr/src/lib/udapl/udapl_tavor/common/dapl_ia_open.c`** -> AI Confidence: **99.34%**
2243. **`usr/src/lib/udapl/udapl_tavor/common/dapl_rmr_bind.c`** -> AI Confidence: **99.34%**
2244. **`usr/src/lib/udapl/udapl_tavor/common/dapl_rsp_create.c`** -> AI Confidence: **99.34%**
2245. **`usr/src/test/libc-tests/tests/err/err.c`** -> AI Confidence: **99.34%**
2246. **`usr/src/test/libc-tests/tests/stdio/open_memstreamtest.c`** -> AI Confidence: **99.34%**
2247. **`usr/src/test/os-tests/tests/ksid/ksid.c`** -> AI Confidence: **99.34%**
2248. **`usr/src/test/os-tests/tests/pf_key/eacq-enabler.c`** -> AI Confidence: **99.34%**
2249. **`usr/src/test/os-tests/tests/secflags/secflags_syscall.c`** -> AI Confidence: **99.34%**
2250. **`usr/src/test/smbsrv-tests/tests/smb_sid/large_sids.c`** -> AI Confidence: **99.34%**
2251. **`usr/src/test/zfs-tests/cmd/devname2devid/devname2devid.c`** -> AI Confidence: **99.34%**
2252. **`usr/src/tools/cscope-fast/invlib.c`** -> AI Confidence: **99.34%**
2253. **`usr/src/tools/cscope-fast/vpinit.c`** -> AI Confidence: **99.34%**
2254. **`usr/src/tools/smatch/src/sort.c`** -> AI Confidence: **99.34%**
2255. **`usr/src/ucbhead/sys/param.h`** -> AI Confidence: **99.34%**
2256. **`usr/src/uts/common/crypto/core/kcf_policy.c`** -> AI Confidence: **99.34%**
2257. **`usr/src/uts/common/crypto/io/dca_dsa.c`** -> AI Confidence: **99.34%**
2258. **`usr/src/uts/common/crypto/io/dca_rsa.c`** -> AI Confidence: **99.34%**
2259. **`usr/src/uts/common/des/des_soft.c`** -> AI Confidence: **99.34%**
2260. **`usr/src/uts/common/disp/shuttle.c`** -> AI Confidence: **99.34%**
2261. **`usr/src/uts/common/fs/nfs/nfs_strerror.c`** -> AI Confidence: **99.34%**
2262. **`usr/src/uts/common/fs/zfs/dsl_crypt.c`** -> AI Confidence: **99.34%**
2263. **`usr/src/uts/common/fs/zfs/lua/lobject.c`** -> AI Confidence: **99.34%**
2264. **`usr/src/uts/common/fs/zfs/lua/lstrlib.c`** -> AI Confidence: **99.34%**
2265. **`usr/src/uts/common/fs/zfs/vdev_mirror.c`** -> AI Confidence: **99.34%**
2266. **`usr/src/uts/common/fs/zfs/vdev_raidz_math_avx2.c`** -> AI Confidence: **99.34%**
2267. **`usr/src/uts/common/fs/zfs/vdev_raidz_math_sse2.c`** -> AI Confidence: **99.34%**
2268. **`usr/src/uts/common/inet/cc/cc_newreno.c`** -> AI Confidence: **99.34%**
2269. **`usr/src/uts/common/inet/ip/ipcsum.c`** -> AI Confidence: **99.34%**
2270. **`usr/src/uts/common/io/1394/adapters/hci1394_ixl_isr.c`** -> AI Confidence: **99.34%**
2271. **`usr/src/uts/common/io/1394/adapters/hci1394_tlist.c`** -> AI Confidence: **99.34%**
2272. **`usr/src/uts/common/io/audio/ac97/ac97.c`** -> AI Confidence: **99.34%**
2273. **`usr/src/uts/common/io/bnxe/577xx/drivers/common/lm/device/lm_phy.c`** -> AI Confidence: **99.34%**
2274. **`usr/src/uts/common/io/bnxe/577xx/drivers/common/lm/device/lm_recv.c`** -> AI Confidence: **99.34%**
2275. **`usr/src/uts/common/io/bnxe/577xx/drivers/common/lm/l4/lm_l4tx.c`** -> AI Confidence: **99.34%**
2276. **`usr/src/uts/common/io/fibre-channel/fca/qlc/ql_hba_fru.c`** -> AI Confidence: **99.34%**
2277. **`usr/src/uts/common/io/hxge/hxge_fm.c`** -> AI Confidence: **99.34%**
2278. **`usr/src/uts/common/io/ib/clients/rds/rdsib_ib.c`** -> AI Confidence: **99.34%**
2279. **`usr/src/uts/common/io/ib/mgt/ibmf/ibmf_utils.c`** -> AI Confidence: **99.34%**
2280. **`usr/src/uts/common/io/mii/mii_cicada.c`** -> AI Confidence: **99.34%**
2281. **`usr/src/uts/common/io/mii/mii_marvell.c`** -> AI Confidence: **99.34%**
2282. **`usr/src/uts/common/io/mii/mii_realtek.c`** -> AI Confidence: **99.34%**
2283. **`usr/src/uts/common/io/nxge/nxge_fm.c`** -> AI Confidence: **99.34%**
2284. **`usr/src/uts/common/io/scsi/targets/ses_sen.c`** -> AI Confidence: **99.34%**
2285. **`usr/src/uts/common/io/sfxge/sfxge_nvram.c`** -> AI Confidence: **99.34%**
2286. **`usr/src/uts/common/io/sfxge/sfxge_pci.c`** -> AI Confidence: **99.34%**
2287. **`usr/src/uts/common/io/softmac/softmac_fp.c`** -> AI Confidence: **99.34%**
2288. **`usr/src/uts/common/io/softmac/softmac_stat.c`** -> AI Confidence: **99.34%**
2289. **`usr/src/uts/common/io/vuidmice/vuidm3p.c`** -> AI Confidence: **99.34%**
2290. **`usr/src/uts/common/io/vuidmice/vuidm4p.c`** -> AI Confidence: **99.34%**
2291. **`usr/src/uts/common/io/vuidmice/vuidm5p.c`** -> AI Confidence: **99.34%**
2292. **`usr/src/uts/common/os/vm_meter.c`** -> AI Confidence: **99.34%**
2293. **`usr/src/uts/common/syscall/sigpending.c`** -> AI Confidence: **99.34%**
2294. **`usr/src/uts/i86pc/io/acpi/acpidev/acpidev_device.c`** -> AI Confidence: **99.34%**
2295. **`usr/src/uts/i86pc/os/smb_dev.c`** -> AI Confidence: **99.34%**
2296. **`usr/src/uts/i86pc/promif/prom_panic.c`** -> AI Confidence: **99.34%**
2297. **`usr/src/uts/intel/sys/acpi/platform/acenvex.h`** -> AI Confidence: **99.34%**
2298. **`usr/src/uts/sparc/fpu/iu_simulator.c`** -> AI Confidence: **99.34%**
2299. **`usr/src/uts/sun4/io/px/px_dma.c`** -> AI Confidence: **99.34%**
2300. **`usr/src/uts/sun4/io/px/px_space.c`** -> AI Confidence: **99.34%**
2301. **`usr/src/uts/sun4u/io/pci/pci_debug.c`** -> AI Confidence: **99.34%**
2302. **`usr/src/uts/sun4u/sys/machthread.h`** -> AI Confidence: **99.34%**
2303. **`usr/src/uts/sun4u/vm/mach_sfmmu.h`** -> AI Confidence: **99.34%**
2304. **`usr/src/uts/sun4v/io/fault_iso.c`** -> AI Confidence: **99.34%**
2305. **`usr/src/uts/sun4v/io/n2piupc/n2piupc_biterr.c`** -> AI Confidence: **99.34%**
2306. **`usr/src/cmd/print/scripts/ppdmgr`** -> AI Confidence: **99.34%**
2307. **`usr/src/contrib/ast/src/cmd/INIT/ditto.sh`** -> AI Confidence: **99.34%**
2308. **`usr/src/contrib/ast/src/cmd/ksh93/tests/bracket.sh`** -> AI Confidence: **99.34%**
2309. **`usr/src/tools/scripts/ws.sh`** -> AI Confidence: **99.34%**
2310. **`usr/src/cmd/make/bin/read2.cc`** -> AI Confidence: **99.34%**
2311. **`usr/src/cmd/make/lib/mksh/macro.cc`** -> AI Confidence: **99.34%**
2312. **`usr/src/cmd/make/lib/mksh/read.cc`** -> AI Confidence: **99.34%**
2313. **`usr/src/lib/sun_fc/common/Lockable.cc`** -> AI Confidence: **99.34%**
2314. **`usr/src/contrib/ast/src/cmd/ksh93/include/terminal.h`** -> AI Confidence: **99.33%**
2315. **`usr/src/ucbcmd/from/from.c`** -> AI Confidence: **99.33%**
2316. **`usr/src/cmd/make/bin/files.cc`** -> AI Confidence: **99.33%**
2317. **`usr/src/boot/efi/libefi/errno.c`** -> AI Confidence: **99.32%**
2318. **`usr/src/boot/include/limits.h`** -> AI Confidence: **99.32%**
2319. **`usr/src/boot/include/math.h`** -> AI Confidence: **99.32%**
2320. **`usr/src/boot/libsa/string/strlcpy.c`** -> AI Confidence: **99.32%**
2321. **`usr/src/boot/libsa/string/strrchr.c`** -> AI Confidence: **99.32%**
2322. **`usr/src/boot/libsa/string/strsep.c`** -> AI Confidence: **99.32%**
2323. **`usr/src/cmd/acpi/common/getopt.c`** -> AI Confidence: **99.32%**
2324. **`usr/src/cmd/acpi/iasl/aslnamesp.c`** -> AI Confidence: **99.32%**
2325. **`usr/src/cmd/acpi/iasl/asloperands.c`** -> AI Confidence: **99.32%**
2326. **`usr/src/cmd/acpi/iasl/asloptions.c`** -> AI Confidence: **99.32%**
2327. **`usr/src/cmd/acpi/iasl/aslpld.c`** -> AI Confidence: **99.32%**
2328. **`usr/src/cmd/acpi/iasl/aslprepkg.c`** -> AI Confidence: **99.32%**
2329. **`usr/src/cmd/acpi/iasl/aslresource.c`** -> AI Confidence: **99.32%**
2330. **`usr/src/cmd/acpi/iasl/aslrestype2.c`** -> AI Confidence: **99.32%**
2331. **`usr/src/cmd/acpi/iasl/aslrestype2s.c`** -> AI Confidence: **99.32%**
2332. **`usr/src/cmd/acpi/iasl/asltree.c`** -> AI Confidence: **99.32%**
2333. **`usr/src/cmd/adbgen/common/adbgen3.c`** -> AI Confidence: **99.32%**
2334. **`usr/src/cmd/adbgen/common/adbsub.c`** -> AI Confidence: **99.32%**
2335. **`usr/src/cmd/bnu/pk0.c`** -> AI Confidence: **99.32%**
2336. **`usr/src/cmd/bnu/uucheck.c`** -> AI Confidence: **99.32%**
2337. **`usr/src/cmd/cmd-inet/usr.bin/talk/ctl_transact.c`** -> AI Confidence: **99.32%**
2338. **`usr/src/cmd/csh/printf.c`** -> AI Confidence: **99.32%**
2339. **`usr/src/cmd/csh/sh.dol.c`** -> AI Confidence: **99.32%**
2340. **`usr/src/cmd/eqn/funny.c`** -> AI Confidence: **99.32%**
2341. **`usr/src/cmd/eqn/text.c`** -> AI Confidence: **99.32%**
2342. **`usr/src/cmd/fm/fmd/common/fmd_string.c`** -> AI Confidence: **99.32%**
2343. **`usr/src/cmd/fm/modules/common/fabric-xlate/fx_fire.c`** -> AI Confidence: **99.32%**
2344. **`usr/src/cmd/fs.d/deffs.c`** -> AI Confidence: **99.32%**
2345. **`usr/src/cmd/ipf/lib/ipft_hx.c`** -> AI Confidence: **99.32%**
2346. **`usr/src/cmd/krb5/kadmin/dbutil/strtok.c`** -> AI Confidence: **99.32%**
2347. **`usr/src/cmd/ldap/common/idtest.c`** -> AI Confidence: **99.32%**
2348. **`usr/src/cmd/look/look.c`** -> AI Confidence: **99.32%**
2349. **`usr/src/cmd/lp/cmd/lpsched/log.c`** -> AI Confidence: **99.32%**
2350. **`usr/src/cmd/lp/filter/postscript/postio/slowsend.c`** -> AI Confidence: **99.32%**
2351. **`usr/src/cmd/lp/lib/filters/search.c`** -> AI Confidence: **99.32%**
2352. **`usr/src/cmd/lp/lib/lp/dellist.c`** -> AI Confidence: **99.32%**
2353. **`usr/src/cmd/lp/lib/lp/dirs.c`** -> AI Confidence: **99.32%**
2354. **`usr/src/cmd/lp/lib/msgs/msend.c`** -> AI Confidence: **99.32%**
2355. **`usr/src/cmd/lp/lib/oam/agettxt.c`** -> AI Confidence: **99.32%**
2356. **`usr/src/cmd/lp/model/lp.set.c`** -> AI Confidence: **99.32%**
2357. **`usr/src/cmd/mail/Dout.c`** -> AI Confidence: **99.32%**
2358. **`usr/src/cmd/mail/Tout.c`** -> AI Confidence: **99.32%**
2359. **`usr/src/cmd/mailx/fio.c`** -> AI Confidence: **99.32%**
2360. **`usr/src/cmd/mdb/common/modules/genunix/kgrep.c`** -> AI Confidence: **99.32%**
2361. **`usr/src/cmd/msgfmt/gnu_lex.c`** -> AI Confidence: **99.32%**
2362. **`usr/src/cmd/newform/newform.c`** -> AI Confidence: **99.32%**
2363. **`usr/src/cmd/refer/hunt1.c`** -> AI Confidence: **99.32%**
2364. **`usr/src/cmd/refer/hunt6.c`** -> AI Confidence: **99.32%**
2365. **`usr/src/cmd/refer/inv1.c`** -> AI Confidence: **99.32%**
2366. **`usr/src/cmd/sendmail/db/os/os_rpath.c`** -> AI Confidence: **99.32%**
2367. **`usr/src/cmd/sendmail/include/sm/config.h`** -> AI Confidence: **99.32%**
2368. **`usr/src/cmd/sendmail/include/sm/limits.h`** -> AI Confidence: **99.32%**
2369. **`usr/src/cmd/sendmail/libsmutil/safefile.c`** -> AI Confidence: **99.32%**
2370. **`usr/src/cmd/sendmail/src/domain.c`** -> AI Confidence: **99.32%**
2371. **`usr/src/cmd/sendmail/src/readcf.c`** -> AI Confidence: **99.32%**
2372. **`usr/src/cmd/sendmail/src/trace.c`** -> AI Confidence: **99.32%**
2373. **`usr/src/cmd/sgs/elfedit/common/sys.c`** -> AI Confidence: **99.32%**
2374. **`usr/src/cmd/sgs/libld/common/globals.c`** -> AI Confidence: **99.32%**
2375. **`usr/src/cmd/sgs/mcs/common/utils.c`** -> AI Confidence: **99.32%**
2376. **`usr/src/cmd/sgs/tsort/common/erraction.c`** -> AI Confidence: **99.32%**
2377. **`usr/src/cmd/sh/macro.c`** -> AI Confidence: **99.32%**
2378. **`usr/src/cmd/sh/ulimit.c`** -> AI Confidence: **99.32%**
2379. **`usr/src/cmd/svr4pkg/libinst/nblk.c`** -> AI Confidence: **99.32%**
2380. **`usr/src/cmd/tic/tic_scan.c`** -> AI Confidence: **99.32%**
2381. **`usr/src/cmd/vi/port/ex_re.c`** -> AI Confidence: **99.32%**
2382. **`usr/src/cmd/vi/port/ex_set.c`** -> AI Confidence: **99.32%**
2383. **`usr/src/cmd/vi/port/ex_vops3.c`** -> AI Confidence: **99.32%**
2384. **`usr/src/cmd/vi/port/printf.c`** -> AI Confidence: **99.32%**
2385. **`usr/src/common/acpica/dispatcher/dswscope.c`** -> AI Confidence: **99.32%**
2386. **`usr/src/common/acpica/events/evgpeutil.c`** -> AI Confidence: **99.32%**
2387. **`usr/src/common/acpica/events/evxfevnt.c`** -> AI Confidence: **99.32%**
2388. **`usr/src/common/acpica/executer/exdebug.c`** -> AI Confidence: **99.32%**
2389. **`usr/src/common/acpica/executer/exstorob.c`** -> AI Confidence: **99.32%**
2390. **`usr/src/common/acpica/hardware/hwregs.c`** -> AI Confidence: **99.32%**
2391. **`usr/src/common/acpica/hardware/hwxface.c`** -> AI Confidence: **99.32%**
2392. **`usr/src/common/acpica/namespace/nsobject.c`** -> AI Confidence: **99.32%**
2393. **`usr/src/common/acpica/namespace/nswalk.c`** -> AI Confidence: **99.32%**
2394. **`usr/src/common/acpica/resources/rsinfo.c`** -> AI Confidence: **99.32%**
2395. **`usr/src/common/acpica/resources/rslist.c`** -> AI Confidence: **99.32%**
2396. **`usr/src/common/acpica/resources/rsmisc.c`** -> AI Confidence: **99.32%**
2397. **`usr/src/common/acpica/tables/tbfind.c`** -> AI Confidence: **99.32%**
2398. **`usr/src/common/acpica/utilities/utaddress.c`** -> AI Confidence: **99.32%**
2399. **`usr/src/common/acpica/utilities/utcopy.c`** -> AI Confidence: **99.32%**
2400. **`usr/src/common/acpica/utilities/uteval.c`** -> AI Confidence: **99.32%**
2401. **`usr/src/common/acpica/utilities/utids.c`** -> AI Confidence: **99.32%**
2402. **`usr/src/common/acpica/utilities/utobject.c`** -> AI Confidence: **99.32%**
2403. **`usr/src/common/acpica/utilities/utownerid.c`** -> AI Confidence: **99.32%**
2404. **`usr/src/common/acpica/utilities/utresdecode.c`** -> AI Confidence: **99.32%**
2405. **`usr/src/common/acpica/utilities/utstring.c`** -> AI Confidence: **99.32%**
2406. **`usr/src/common/crypto/aes/amd64/aesopt.h`** -> AI Confidence: **99.32%**
2407. **`usr/src/common/crypto/ecc/ecp_aff.c`** -> AI Confidence: **99.32%**
2408. **`usr/src/common/smbsrv/smb_cfg_util.c`** -> AI Confidence: **99.32%**
2409. **`usr/src/contrib/ast/src/cmd/ksh93/bltins/trap.c`** -> AI Confidence: **99.32%**
2410. **`usr/src/contrib/ast/src/cmd/ksh93/data/keywords.c`** -> AI Confidence: **99.32%**
2411. **`usr/src/contrib/ast/src/cmd/ksh93/data/lexstates.c`** -> AI Confidence: **99.32%**
2412. **`usr/src/contrib/ast/src/cmd/ksh93/data/options.c`** -> AI Confidence: **99.32%**
2413. **`usr/src/contrib/ast/src/cmd/ksh93/data/testops.c`** -> AI Confidence: **99.32%**
2414. **`usr/src/contrib/ast/src/cmd/ksh93/mamstate.c`** -> AI Confidence: **99.32%**
2415. **`usr/src/contrib/ast/src/cmd/ksh93/sh/deparse.c`** -> AI Confidence: **99.32%**
2416. **`usr/src/contrib/ast/src/cmd/ksh93/sh/nvtype.c`** -> AI Confidence: **99.32%**
2417. **`usr/src/contrib/ast/src/cmd/msgcc/msgcvt.c`** -> AI Confidence: **99.32%**
2418. **`usr/src/contrib/ast/src/cmd/msgcc/msgget.c`** -> AI Confidence: **99.32%**
2419. **`usr/src/contrib/ast/src/lib/libast/astsa/strmatch.c`** -> AI Confidence: **99.32%**
2420. **`usr/src/contrib/ast/src/lib/libast/comp/execvpe.c`** -> AI Confidence: **99.32%**
2421. **`usr/src/contrib/ast/src/lib/libast/comp/getopt.c`** -> AI Confidence: **99.32%**
2422. **`usr/src/contrib/ast/src/lib/libast/comp/setsid.c`** -> AI Confidence: **99.32%**
2423. **`usr/src/contrib/ast/src/lib/libast/comp/strftime.c`** -> AI Confidence: **99.32%**
2424. **`usr/src/contrib/ast/src/lib/libast/comp/strtoll.c`** -> AI Confidence: **99.32%**
2425. **`usr/src/contrib/ast/src/lib/libast/comp/strtoull.c`** -> AI Confidence: **99.32%**
2426. **`usr/src/contrib/ast/src/lib/libast/comp/symlink.c`** -> AI Confidence: **99.32%**
2427. **`usr/src/contrib/ast/src/lib/libast/comp/tempnam.c`** -> AI Confidence: **99.32%**
2428. **`usr/src/contrib/ast/src/lib/libast/disc/sfdcmore.c`** -> AI Confidence: **99.32%**
2429. **`usr/src/contrib/ast/src/lib/libast/features/botch.c`** -> AI Confidence: **99.32%**
2430. **`usr/src/contrib/ast/src/lib/libast/features/mode.c`** -> AI Confidence: **99.32%**
2431. **`usr/src/contrib/ast/src/lib/libast/features/signal.c`** -> AI Confidence: **99.32%**
2432. **`usr/src/contrib/ast/src/lib/libast/include/wait.h`** -> AI Confidence: **99.32%**
2433. **`usr/src/contrib/ast/src/lib/libast/misc/signal.c`** -> AI Confidence: **99.32%**
2434. **`usr/src/contrib/ast/src/lib/libast/obsolete/spawn.c`** -> AI Confidence: **99.32%**
2435. **`usr/src/contrib/ast/src/lib/libast/port/iblocks.c`** -> AI Confidence: **99.32%**
2436. **`usr/src/contrib/ast/src/lib/libast/port/touch.c`** -> AI Confidence: **99.32%**
2437. **`usr/src/contrib/ast/src/lib/libast/preroot/setpreroot.c`** -> AI Confidence: **99.32%**
2438. **`usr/src/contrib/ast/src/lib/libast/sfio/sftable.c`** -> AI Confidence: **99.32%**
2439. **`usr/src/contrib/ast/src/lib/libast/string/ccmapid.c`** -> AI Confidence: **99.32%**
2440. **`usr/src/contrib/ast/src/lib/libast/string/fmtls.c`** -> AI Confidence: **99.32%**
2441. **`usr/src/contrib/ast/src/lib/libast/string/strperm.c`** -> AI Confidence: **99.32%**
2442. **`usr/src/contrib/ast/src/lib/libast/string/strpsearch.c`** -> AI Confidence: **99.32%**
2443. **`usr/src/contrib/ast/src/lib/libast/string/tokline.c`** -> AI Confidence: **99.32%**
2444. **`usr/src/contrib/ast/src/lib/libast/tm/tmgoff.c`** -> AI Confidence: **99.32%**
2445. **`usr/src/contrib/ast/src/lib/libast/tm/tmlex.c`** -> AI Confidence: **99.32%**
2446. **`usr/src/contrib/ast/src/lib/libast/tm/tmword.c`** -> AI Confidence: **99.32%**
2447. **`usr/src/contrib/ast/src/lib/libast/tm/tmxdate.c`** -> AI Confidence: **99.32%**
2448. **`usr/src/contrib/ast/src/lib/libcmd/getconf.c`** -> AI Confidence: **99.32%**
2449. **`usr/src/contrib/ast/src/lib/libcmd/pids.c`** -> AI Confidence: **99.32%**
2450. **`usr/src/contrib/ast/src/lib/libcmd/tee.c`** -> AI Confidence: **99.32%**
2451. **`usr/src/contrib/ast/src/lib/libcmd/vmstate.c`** -> AI Confidence: **99.32%**
2452. **`usr/src/contrib/ast/src/lib/libcmd/wc.c`** -> AI Confidence: **99.32%**
2453. **`usr/src/contrib/ast/src/lib/libpp/ppsearch.c`** -> AI Confidence: **99.32%**
2454. **`usr/src/contrib/mDNSResponder/Clients/ClientCommon.c`** -> AI Confidence: **99.32%**
2455. **`usr/src/contrib/mDNSResponder/mDNSShared/dnssd_clientlib.c`** -> AI Confidence: **99.32%**
2456. **`usr/src/grub/grub-0.97/netboot/tulip.c`** -> AI Confidence: **99.32%**
2457. **`usr/src/grub/grub-0.97/stage2/common.c`** -> AI Confidence: **99.32%**
2458. **`usr/src/grub/grub-0.97/stage2/fsys_fat.c`** -> AI Confidence: **99.32%**
2459. **`usr/src/grub/grub-0.97/stage2/stage2.c`** -> AI Confidence: **99.32%**
2460. **`usr/src/head/inttypes.h`** -> AI Confidence: **99.32%**
2461. **`usr/src/head/stdio.h`** -> AI Confidence: **99.32%**
2462. **`usr/src/lib/gss_mechs/mech_dh/backend/mech/support.c`** -> AI Confidence: **99.32%**
2463. **`usr/src/lib/gss_mechs/mech_krb5/crypto/des/afsstring2key.c`** -> AI Confidence: **99.32%**
2464. **`usr/src/lib/gss_mechs/mech_krb5/crypto/keyed_checksum_types.c`** -> AI Confidence: **99.32%**
2465. **`usr/src/lib/gss_mechs/mech_krb5/krb5/ccache/ccdefops.c`** -> AI Confidence: **99.32%**
2466. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/conv_princ.c`** -> AI Confidence: **99.32%**
2467. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/fwd_tgt.c`** -> AI Confidence: **99.32%**
2468. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/mk_priv.c`** -> AI Confidence: **99.32%**
2469. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/rd_priv.c`** -> AI Confidence: **99.32%**
2470. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/rd_safe.c`** -> AI Confidence: **99.32%**
2471. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/srv_rcache.c`** -> AI Confidence: **99.32%**
2472. **`usr/src/lib/gss_mechs/mech_krb5/krb5/krb/walk_rtree.c`** -> AI Confidence: **99.32%**
2473. **`usr/src/lib/gss_mechs/mech_krb5/krb5/os/realm_dom.c`** -> AI Confidence: **99.32%**
2474. **`usr/src/lib/gss_mechs/mech_krb5/mech/set_ccache.c`** -> AI Confidence: **99.32%**
2475. **`usr/src/lib/iconv_modules/ko/common/c2p.c`** -> AI Confidence: **99.32%**
2476. **`usr/src/lib/iconv_modules/ko/common/johap92_to_utf.c`** -> AI Confidence: **99.32%**
2477. **`usr/src/lib/iconv_modules/ko/common/utf_to_ojh_sub.c`** -> AI Confidence: **99.32%**
2478. **`usr/src/lib/iconv_modules/ko/common/wansung_to_utf.c`** -> AI Confidence: **99.32%**
2479. **`usr/src/lib/iconv_modules/utf-8/common/binarytables/test/mkmnmcstbl.c`** -> AI Confidence: **99.32%**
2480. **`usr/src/lib/krb5/kadm5/str_conv.c`** -> AI Confidence: **99.32%**
2481. **`usr/src/lib/krb5/plugins/kdb/ldap/libkdb_ldap/ldap_service_rights.c`** -> AI Confidence: **99.32%**
2482. **`usr/src/lib/krb5/ss/parse.c`** -> AI Confidence: **99.32%**
2483. **`usr/src/lib/libc/i386/inc/SYS.h`** -> AI Confidence: **99.32%**
2484. **`usr/src/lib/libc/port/fp/decimal_bin.c`** -> AI Confidence: **99.32%**
2485. **`usr/src/lib/libc/port/fp/double_decim.c`** -> AI Confidence: **99.32%**
2486. **`usr/src/lib/libc/port/gen/a64l.c`** -> AI Confidence: **99.32%**
2487. **`usr/src/lib/libc/port/gen/getisax.c`** -> AI Confidence: **99.32%**
2488. **`usr/src/lib/libc/port/gen/malloc.c`** -> AI Confidence: **99.32%**
2489. **`usr/src/lib/libc/port/gen/siglist.c`** -> AI Confidence: **99.32%**
2490. **`usr/src/lib/libc/port/gen/strcspn.c`** -> AI Confidence: **99.32%**
2491. **`usr/src/lib/libc/port/gen/strncat.c`** -> AI Confidence: **99.32%**
2492. **`usr/src/lib/libc/port/gen/strncpy.c`** -> AI Confidence: **99.32%**
2493. **`usr/src/lib/libc/port/gen/strsep.c`** -> AI Confidence: **99.32%**
2494. **`usr/src/lib/libc/port/gen/strspn.c`** -> AI Confidence: **99.32%**
2495. **`usr/src/lib/libc/port/gen/strtonum.c`** -> AI Confidence: **99.32%**
2496. **`usr/src/lib/libc/port/i18n/wcsnlen.c`** -> AI Confidence: **99.32%**
2497. **`usr/src/lib/libc/port/threads/rwlock.c`** -> AI Confidence: **99.32%**
2498. **`usr/src/lib/libc/sparc/fp/_Q_set_except.c`** -> AI Confidence: **99.32%**
2499. **`usr/src/lib/libcurses/screen/copywin.c`** -> AI Confidence: **99.32%**
2500. **`usr/src/lib/libcurses/screen/delkeymap.c`** -> AI Confidence: **99.32%**
2501. **`usr/src/lib/libcurses/screen/init_acs.c`** -> AI Confidence: **99.32%**
2502. **`usr/src/lib/libcurses/screen/mbtranslate.c`** -> AI Confidence: **99.32%**
2503. **`usr/src/lib/libcurses/screen/newwin.c`** -> AI Confidence: **99.32%**
2504. **`usr/src/lib/libcurses/screen/slk_start.c`** -> AI Confidence: **99.32%**
2505. **`usr/src/lib/libcurses/screen/wborder.c`** -> AI Confidence: **99.32%**
2506. **`usr/src/lib/libcurses/screen/wclrtoeol.c`** -> AI Confidence: **99.32%**
2507. **`usr/src/lib/libcurses/screen/winsch.c`** -> AI Confidence: **99.32%**
2508. **`usr/src/lib/libcurses/screen/winsdelln.c`** -> AI Confidence: **99.32%**
2509. **`usr/src/lib/libcurses/screen/wnoutref.c`** -> AI Confidence: **99.32%**
2510. **`usr/src/lib/libeti/form/common/regcmp.c`** -> AI Confidence: **99.32%**
2511. **`usr/src/lib/libldap5/sources/ldap/common/getfilter.c`** -> AI Confidence: **99.32%**
2512. **`usr/src/lib/libm/common/LD/jnl.c`** -> AI Confidence: **99.32%**
2513. **`usr/src/lib/libm/common/LD/sincosl.c`** -> AI Confidence: **99.32%**
2514. **`usr/src/lib/libm/common/LD/sincospil.c`** -> AI Confidence: **99.32%**
2515. **`usr/src/lib/libm/common/LD/sinpil.c`** -> AI Confidence: **99.32%**
2516. **`usr/src/lib/libm/common/Q/jnl.c`** -> AI Confidence: **99.32%**
2517. **`usr/src/lib/libm/common/complex/cacoshl.c`** -> AI Confidence: **99.32%**
2518. **`usr/src/lib/libm/common/complex/cacosl.c`** -> AI Confidence: **99.32%**
2519. **`usr/src/lib/libm/common/complex/casinl.c`** -> AI Confidence: **99.32%**
2520. **`usr/src/lib/libm/common/complex/catanl.c`** -> AI Confidence: **99.32%**
2521. **`usr/src/lib/libm/common/complex/clog.c`** -> AI Confidence: **99.32%**
2522. **`usr/src/lib/libm/common/complex/clogl.c`** -> AI Confidence: **99.32%**
2523. **`usr/src/lib/libm/common/complex/cpowl.c`** -> AI Confidence: **99.32%**
2524. **`usr/src/lib/libm/common/complex/cprojl.c`** -> AI Confidence: **99.32%**
2525. **`usr/src/lib/libm/common/complex/csqrtl.c`** -> AI Confidence: **99.32%**
2526. **`usr/src/lib/libm/common/complex/ctanhl.c`** -> AI Confidence: **99.32%**
2527. **`usr/src/lib/libm/common/complex/k_clog_rl.c`** -> AI Confidence: **99.32%**
2528. **`usr/src/lib/libm/common/m9x/fma.c`** -> AI Confidence: **99.32%**
2529. **`usr/src/lib/libm/common/m9x/fmaf.c`** -> AI Confidence: **99.32%**
2530. **`usr/src/lib/libm/common/m9x/fmal.c`** -> AI Confidence: **99.32%**
2531. **`usr/src/lib/libm/common/m9x/nearbyintl.c`** -> AI Confidence: **99.32%**
2532. **`usr/src/lib/libm/common/m9x/remquof.c`** -> AI Confidence: **99.32%**
2533. **`usr/src/lib/libmail/common/setup_exec.c`** -> AI Confidence: **99.32%**
2534. **`usr/src/lib/libmp/common/msqrt.c`** -> AI Confidence: **99.32%**
2535. **`usr/src/lib/libmtmalloc/tests/align.c`** -> AI Confidence: **99.32%**
2536. **`usr/src/lib/librstp/common/roletrns.c`** -> AI Confidence: **99.32%**
2537. **`usr/src/lib/libscf/common/notify_params.c`** -> AI Confidence: **99.32%**
2538. **`usr/src/lib/libsqlite/src/encode.c`** -> AI Confidence: **99.32%**
2539. **`usr/src/lib/libuutil/common/uu_strtoint.c`** -> AI Confidence: **99.32%**
2540. **`usr/src/lib/libxcurses/src/libc/mks/m_errorx.c`** -> AI Confidence: **99.32%**
2541. **`usr/src/lib/libxcurses/src/libc/xcurses/wadd_wch.c`** -> AI Confidence: **99.32%**
2542. **`usr/src/lib/nsswitch/ldap/common/getspent.c`** -> AI Confidence: **99.32%**
2543. **`usr/src/lib/udapl/udapl_tavor/common/dapl_cno_wait.c`** -> AI Confidence: **99.32%**
2544. **`usr/src/lib/udapl/udapl_tavor/common/dapl_ep_dup_connect.c`** -> AI Confidence: **99.32%**
2545. **`usr/src/lib/udapl/udapl_tavor/common/dapl_ep_post_recv.c`** -> AI Confidence: **99.32%**
2546. **`usr/src/lib/udapl/udapl_tavor/common/dapl_evd_dequeue.c`** -> AI Confidence: **99.32%**
2547. **`usr/src/lib/udapl/udapl_tavor/common/dapl_evd_free.c`** -> AI Confidence: **99.32%**
2548. **`usr/src/lib/udapl/udapl_tavor/common/dapl_evd_post_se.c`** -> AI Confidence: **99.32%**
2549. **`usr/src/lib/udapl/udapl_tavor/common/dapl_ia_query.c`** -> AI Confidence: **99.32%**
2550. **`usr/src/lib/udapl/udapl_tavor/common/dapl_lmr_free.c`** -> AI Confidence: **99.32%**
2551. **`usr/src/lib/udapl/udapl_tavor/common/dapl_rmr_free.c`** -> AI Confidence: **99.32%**
2552. **`usr/src/psm/promif/ieee1275/common/prom_printf.c`** -> AI Confidence: **99.32%**
2553. **`usr/src/test/bhyve-tests/tests/kdev/payload_vlapic_msr_access.c`** -> AI Confidence: **99.32%**
2554. **`usr/src/test/os-tests/tests/saveargs/testmatch/testmatch.c`** -> AI Confidence: **99.32%**
2555. **`usr/src/test/util-tests/tests/ctf/check-float.c`** -> AI Confidence: **99.32%**
2556. **`usr/src/test/util-tests/tests/ctf/check-int.c`** -> AI Confidence: **99.32%**
2557. **`usr/src/tools/protocmp/arch.c`** -> AI Confidence: **99.32%**
2558. **`usr/src/ucblib/libtermcap/tgoto.c`** -> AI Confidence: **99.32%**
2559. **`usr/src/uts/common/fs/smbsrv/smb2_fsctl_fs.c`** -> AI Confidence: **99.32%**
2560. **`usr/src/uts/common/fs/smbsrv/smb2_query_info.c`** -> AI Confidence: **99.32%**
2561. **`usr/src/uts/common/fs/smbsrv/smb2_set_info.c`** -> AI Confidence: **99.32%**
2562. **`usr/src/uts/common/fs/smbsrv/smb_nt_create_andx.c`** -> AI Confidence: **99.32%**
2563. **`usr/src/uts/common/io/bnxe/577xx/drivers/common/lm/device/hw_debug.h`** -> AI Confidence: **99.32%**
2564. **`usr/src/uts/common/io/cxgbe/t4nex/fastlz.c`** -> AI Confidence: **99.32%**
2565. **`usr/src/uts/common/io/hxge/hxge_kstats.c`** -> AI Confidence: **99.32%**
2566. **`usr/src/uts/common/io/nxge/nxge_mac.c`** -> AI Confidence: **99.32%**
2567. **`usr/src/uts/common/io/nxge/nxge_zcp.c`** -> AI Confidence: **99.32%**
2568. **`usr/src/uts/common/io/sfxge/common/efx_ev.c`** -> AI Confidence: **99.32%**
2569. **`usr/src/uts/common/io/sfxge/common/hunt_nic.c`** -> AI Confidence: **99.32%**
2570. **`usr/src/uts/common/io/sfxge/common/siena_nic.c`** -> AI Confidence: **99.32%**
2571. **`usr/src/uts/common/io/sfxge/efsys.h`** -> AI Confidence: **99.32%**
2572. **`usr/src/uts/common/io/sfxge/sfxge_dma.c`** -> AI Confidence: **99.32%**
2573. **`usr/src/uts/common/io/sfxge/sfxge_vpd.c`** -> AI Confidence: **99.32%**
2574. **`usr/src/uts/common/sys/asynch.h`** -> AI Confidence: **99.32%**
2575. **`usr/src/uts/common/sys/auxv.h`** -> AI Confidence: **99.32%**
2576. **`usr/src/uts/common/sys/bitmap.h`** -> AI Confidence: **99.32%**
2577. **`usr/src/uts/common/sys/byteorder.h`** -> AI Confidence: **99.32%**
2578. **`usr/src/uts/common/sys/ipc.h`** -> AI Confidence: **99.32%**
2579. **`usr/src/uts/common/sys/rds.h`** -> AI Confidence: **99.32%**
2580. **`usr/src/uts/common/syscall/cladm.c`** -> AI Confidence: **99.32%**
2581. **`usr/src/uts/i86xpv/sys/xpv_impl.h`** -> AI Confidence: **99.32%**
2582. **`usr/src/uts/i86xpv/sys/xpv_user.h`** -> AI Confidence: **99.32%**
2583. **`usr/src/uts/intel/promif/prom_putchar.c`** -> AI Confidence: **99.32%**
2584. **`usr/src/uts/intel/sys/privmregs.h`** -> AI Confidence: **99.32%**
2585. **`usr/src/uts/sun4/sys/xc_impl.h`** -> AI Confidence: **99.32%**
2586. **`usr/src/uts/sun4u/serengeti/sys/ssm.h`** -> AI Confidence: **99.32%**
2587. **`usr/src/cmd/dumpadm/svc-dumpadm`** -> AI Confidence: **99.32%**
2588. **`usr/src/cmd/sendmail/lib/smtp-sendmail`** -> AI Confidence: **99.32%**
2589. **`usr/src/cmd/svc/milestone/fs-usr`** -> AI Confidence: **99.32%**
2590. **`usr/src/cmd/svc/milestone/net-nwam`** -> AI Confidence: **99.32%**
2591. **`usr/src/cmd/svc/milestone/net-physical`** -> AI Confidence: **99.32%**
2592. **`usr/src/contrib/ast/src/cmd/ksh93/tests/basic.sh`** -> AI Confidence: **99.32%**
2593. **`usr/src/contrib/ast/src/cmd/ksh93/tests/functions.sh`** -> AI Confidence: **99.32%**
2594. **`usr/src/lib/brand/solaris10/cmd/s10_net_physical.sh`** -> AI Confidence: **99.32%**
2595. **`usr/src/test/zfs-tests/tests/functional/cachefile/cachefile_003_pos.ksh`** -> AI Confidence: **99.32%**
2596. **`usr/src/test/zfs-tests/tests/functional/mmp/mmp_active_import.ksh`** -> AI Confidence: **99.32%**
2597. **`usr/src/tools/scripts/build_cscope.sh`** -> AI Confidence: **99.32%**
2598. **`usr/src/boot/common/bcache.c`** -> AI Confidence: **99.31%**
2599. **`usr/src/boot/common/dev_net.c`** -> AI Confidence: **99.31%**
2600. **`usr/src/boot/common/disk.c`** -> AI Confidence: **99.31%**
2601. **`usr/src/boot/common/gfx_fb.c`** -> AI Confidence: **99.31%**
2602. **`usr/src/boot/common/gpt.c`** -> AI Confidence: **99.31%**
2603. **`usr/src/boot/common/module.c`** -> AI Confidence: **99.31%**
2604. **`usr/src/boot/common/part.c`** -> AI Confidence: **99.31%**
2605. **`usr/src/boot/common/tem.c`** -> AI Confidence: **99.31%**
2606. **`usr/src/boot/common/vdisk.c`** -> AI Confidence: **99.31%**
2607. **`usr/src/boot/efi/libefi/devicename.c`** -> AI Confidence: **99.31%**
2608. **`usr/src/boot/efi/libefi/efi_console.c`** -> AI Confidence: **99.31%**
2609. **`usr/src/boot/efi/libefi/efiisaio.c`** -> AI Confidence: **99.31%**
2610. **`usr/src/boot/efi/libefi/efipart.c`** -> AI Confidence: **99.31%**
2611. **`usr/src/boot/efi/libefi/efiserialio.c`** -> AI Confidence: **99.31%**
2612. **`usr/src/boot/efi/loader/arch/i386/bootinfo.c`** -> AI Confidence: **99.31%**
2613. **`usr/src/boot/efi/loader/bootinfo.c`** -> AI Confidence: **99.31%**
2614. **`usr/src/boot/efi/loader/copy.c`** -> AI Confidence: **99.31%**
2615. **`usr/src/boot/efi/loader/framebuffer.c`** -> AI Confidence: **99.31%**
2616. **`usr/src/boot/efi/loader/memmap.c`** -> AI Confidence: **99.31%**
2617. **`usr/src/boot/i386/gptzfsboot/zfsboot.c`** -> AI Confidence: **99.31%**
2618. **`usr/src/boot/i386/libi386/biosdisk.c`** -> AI Confidence: **99.31%**
2619. **`usr/src/boot/i386/libi386/biosmem.c`** -> AI Confidence: **99.31%**
2620. **`usr/src/boot/i386/libi386/biossmap.c`** -> AI Confidence: **99.31%**
2621. **`usr/src/boot/i386/libi386/bootinfo32.c`** -> AI Confidence: **99.31%**
2622. **`usr/src/boot/i386/libi386/bootinfo64.c`** -> AI Confidence: **99.31%**
2623. **`usr/src/boot/i386/libi386/devicename.c`** -> AI Confidence: **99.31%**
2624. **`usr/src/boot/i386/libi386/i386_copy.c`** -> AI Confidence: **99.31%**
2625. **`usr/src/boot/i386/libi386/linux.c`** -> AI Confidence: **99.31%**
2626. **`usr/src/boot/i386/libi386/multiboot.c`** -> AI Confidence: **99.31%**
2627. **`usr/src/boot/i386/libi386/vbe.c`** -> AI Confidence: **99.31%**
2628. **`usr/src/boot/libsa/arp.c`** -> AI Confidence: **99.31%**
2629. **`usr/src/boot/libsa/bootp.c`** -> AI Confidence: **99.31%**
2630. **`usr/src/boot/libsa/cd9660.c`** -> AI Confidence: **99.31%**
2631. **`usr/src/boot/libsa/dosfs.c`** -> AI Confidence: **99.31%**
2632. **`usr/src/boot/libsa/net.c`** -> AI Confidence: **99.31%**
2633. **`usr/src/boot/libsa/zfs/nvlist.c`** -> AI Confidence: **99.31%**
2634. **`usr/src/boot/libsa/zfs/zfs.c`** -> AI Confidence: **99.31%**
2635. **`usr/src/boot/libsa/zfs/zfsimpl.c`** -> AI Confidence: **99.31%**
2636. **`usr/src/cmd/abi/apptracecmd/apptrace.c`** -> AI Confidence: **99.31%**
2637. **`usr/src/cmd/abi/spectrans/spec2map/util.c`** -> AI Confidence: **99.31%**
2638. **`usr/src/cmd/abi/spectrans/spec2map/versions.c`** -> AI Confidence: **99.31%**
2639. **`usr/src/cmd/abi/spectrans/spec2trace/bindings.c`** -> AI Confidence: **99.31%**
2640. **`usr/src/cmd/abi/spectrans/spec2trace/printfuncs.c`** -> AI Confidence: **99.31%**
2641. **`usr/src/cmd/abi/spectrans/spec2trace/symtab.c`** -> AI Confidence: **99.31%**
2642. **`usr/src/cmd/abi/spectrans/spec2trace/util.c`** -> AI Confidence: **99.31%**
2643. **`usr/src/cmd/acct/acctcms.c`** -> AI Confidence: **99.31%**
2644. **`usr/src/cmd/acct/acctcon1.c`** -> AI Confidence: **99.31%**
2645. **`usr/src/cmd/acct/acctdusg.c`** -> AI Confidence: **99.31%**
2646. **`usr/src/cmd/acct/acctprc1.c`** -> AI Confidence: **99.31%**
2647. **`usr/src/cmd/acct/wtmpfix.c`** -> AI Confidence: **99.31%**
2648. **`usr/src/cmd/acctadm/aconf.c`** -> AI Confidence: **99.31%**
2649. **`usr/src/cmd/acctadm/main.c`** -> AI Confidence: **99.31%**
2650. **`usr/src/cmd/acctadm/res.c`** -> AI Confidence: **99.31%**
2651. **`usr/src/cmd/acctadm/utils.c`** -> AI Confidence: **99.31%**
2652. **`usr/src/cmd/acpi/common/adisasm.c`** -> AI Confidence: **99.31%**
2653. **`usr/src/cmd/acpi/common/dmtables.c`** -> AI Confidence: **99.31%**
2654. **`usr/src/cmd/acpi/common/osunixxf.c`** -> AI Confidence: **99.31%**
2655. **`usr/src/cmd/acpi/iasl/aslmapoutput.c`** -> AI Confidence: **99.31%**
2656. **`usr/src/cmd/acpi/iasl/aslmaputils.c`** -> AI Confidence: **99.31%**
2657. **`usr/src/cmd/acpi/iasl/aslutils.c`** -> AI Confidence: **99.31%**
2658. **`usr/src/cmd/acpihpd/acpihpd.c`** -> AI Confidence: **99.31%**
2659. **`usr/src/cmd/addbadsec/ix_altsctr.c`** -> AI Confidence: **99.31%**
2660. **`usr/src/cmd/ahciem/ahciem.c`** -> AI Confidence: **99.31%**
2661. **`usr/src/cmd/allocate/mkdevalloc.c`** -> AI Confidence: **99.31%**
2662. **`usr/src/cmd/amdzen/usmn.c`** -> AI Confidence: **99.31%**
2663. **`usr/src/cmd/amt/amt.c`** -> AI Confidence: **99.31%**
2664. **`usr/src/cmd/asa/asa.c`** -> AI Confidence: **99.31%**
2665. **`usr/src/cmd/audio/audioplay/audioplay.c`** -> AI Confidence: **99.31%**
2666. **`usr/src/cmd/audio/audiotest/audiotest.c`** -> AI Confidence: **99.31%**
2667. **`usr/src/cmd/audio/utilities/filehdr.c`** -> AI Confidence: **99.31%**
2668. **`usr/src/cmd/audit/audit.c`** -> AI Confidence: **99.31%**
2669. **`usr/src/cmd/auditconfig/auditconfig.c`** -> AI Confidence: **99.31%**
2670. **`usr/src/cmd/auditd/auditd.c`** -> AI Confidence: **99.31%**
2671. **`usr/src/cmd/auditd/doorway.c`** -> AI Confidence: **99.31%**
2672. **`usr/src/cmd/auditstat/auditstat.c`** -> AI Confidence: **99.31%**
2673. **`usr/src/cmd/auths/auths.c`** -> AI Confidence: **99.31%**
2674. **`usr/src/cmd/autopush/autopush.c`** -> AI Confidence: **99.31%**
2675. **`usr/src/cmd/awk/lib.c`** -> AI Confidence: **99.31%**
2676. **`usr/src/cmd/backup/dump/dumptape.c`** -> AI Confidence: **99.31%**
2677. **`usr/src/cmd/backup/dump/lftw.c`** -> AI Confidence: **99.31%**
2678. **`usr/src/cmd/backup/lib/byteorder.c`** -> AI Confidence: **99.31%**
2679. **`usr/src/cmd/backup/lib/rmtlib.c`** -> AI Confidence: **99.31%**
2680. **`usr/src/cmd/backup/restore/tape.c`** -> AI Confidence: **99.31%**
2681. **`usr/src/cmd/backup/restore/utilities.c`** -> AI Confidence: **99.31%**
2682. **`usr/src/cmd/bart/create.c`** -> AI Confidence: **99.31%**
2683. **`usr/src/cmd/bdiff/bdiff.c`** -> AI Confidence: **99.31%**
2684. **`usr/src/cmd/beadm/beadm.c`** -> AI Confidence: **99.31%**
2685. **`usr/src/cmd/bhyve/amd64/atkbdc.c`** -> AI Confidence: **99.31%**
2686. **`usr/src/cmd/bhyve/amd64/bhyverun_machdep.c`** -> AI Confidence: **99.31%**
2687. **`usr/src/cmd/bhyve/amd64/e820.c`** -> AI Confidence: **99.31%**
2688. **`usr/src/cmd/bhyve/amd64/mptbl.c`** -> AI Confidence: **99.31%**
2689. **`usr/src/cmd/bhyve/amd64/pci_lpc.c`** -> AI Confidence: **99.31%**
2690. **`usr/src/cmd/bhyve/amd64/ps2kbd.c`** -> AI Confidence: **99.31%**
2691. **`usr/src/cmd/bhyve/amd64/ps2mouse.c`** -> AI Confidence: **99.31%**
2692. **`usr/src/cmd/bhyve/amd64/task_switch.c`** -> AI Confidence: **99.31%**
2693. **`usr/src/cmd/bhyve/common/audio.c`** -> AI Confidence: **99.31%**
2694. **`usr/src/cmd/bhyve/common/block_if.c`** -> AI Confidence: **99.31%**
2695. **`usr/src/cmd/bhyve/common/gdb.c`** -> AI Confidence: **99.31%**
2696. **`usr/src/cmd/bhyve/common/net_backend_dlpi.c`** -> AI Confidence: **99.31%**
2697. **`usr/src/cmd/bhyve/common/net_utils.c`** -> AI Confidence: **99.31%**
2698. **`usr/src/cmd/bhyve/common/pci_ahci.c`** -> AI Confidence: **99.31%**
2699. **`usr/src/cmd/bhyve/common/pci_emul.c`** -> AI Confidence: **99.31%**
2700. **`usr/src/cmd/bhyve/common/pci_fbuf.c`** -> AI Confidence: **99.31%**
2701. **`usr/src/cmd/bhyve/common/pci_nvme.c`** -> AI Confidence: **99.31%**
2702. **`usr/src/cmd/bhyve/common/pci_passthru.c`** -> AI Confidence: **99.31%**
2703. **`usr/src/cmd/bhyve/common/pci_virtio_block.c`** -> AI Confidence: **99.31%**
2704. **`usr/src/cmd/bhyve/common/pci_xhci.c`** -> AI Confidence: **99.31%**
2705. **`usr/src/cmd/bhyve/common/privileges.c`** -> AI Confidence: **99.31%**
2706. **`usr/src/cmd/bhyve/common/rfb.c`** -> AI Confidence: **99.31%**
2707. **`usr/src/cmd/bhyve/common/tpm_device.c`** -> AI Confidence: **99.31%**
2708. **`usr/src/cmd/bhyve/common/tpm_emul_swtpm.c`** -> AI Confidence: **99.31%**
2709. **`usr/src/cmd/bhyve/common/uart_emul.c`** -> AI Confidence: **99.31%**
2710. **`usr/src/cmd/bhyve/common/virtio.c`** -> AI Confidence: **99.31%**
2711. **`usr/src/cmd/bhyve/test/tests/mevent/read_pause.c`** -> AI Confidence: **99.31%**
2712. **`usr/src/cmd/bhyve/test/tests/mevent/read_requeue.c`** -> AI Confidence: **99.31%**
2713. **`usr/src/cmd/bhyve/test/tests/mevent/vnode_file.c`** -> AI Confidence: **99.31%**
2714. **`usr/src/cmd/bhyve/test/tests/mevent/vnode_zvol.c`** -> AI Confidence: **99.31%**
2715. **`usr/src/cmd/biosdev/biosdev.c`** -> AI Confidence: **99.31%**
2716. **`usr/src/cmd/bnu/callers.c`** -> AI Confidence: **99.31%**
2717. **`usr/src/cmd/bnu/dkdial.c`** -> AI Confidence: **99.31%**
2718. **`usr/src/cmd/bnu/in.uucpd.c`** -> AI Confidence: **99.31%**
2719. **`usr/src/cmd/bnu/uucp.h`** -> AI Confidence: **99.31%**
2720. **`usr/src/cmd/boot/bootadm/bootadm.c`** -> AI Confidence: **99.31%**
2721. **`usr/src/cmd/boot/bootadm/bootadm_loader.c`** -> AI Confidence: **99.31%**
2722. **`usr/src/cmd/boot/common/bblk_einfo.c`** -> AI Confidence: **99.31%**
2723. **`usr/src/cmd/boot/common/boot_utils.c`** -> AI Confidence: **99.31%**
2724. **`usr/src/cmd/boot/common/mboot_extra.c`** -> AI Confidence: **99.31%**
2725. **`usr/src/cmd/boot/fiocompress/fiocompress.c`** -> AI Confidence: **99.31%**
2726. **`usr/src/cmd/boot/installboot/i386/installboot.c`** -> AI Confidence: **99.31%**
2727. **`usr/src/cmd/boot/installboot/sparc/installboot.c`** -> AI Confidence: **99.31%**
2728. **`usr/src/cmd/boot/installgrub/installgrub.c`** -> AI Confidence: **99.31%**
2729. **`usr/src/cmd/busstat/busstat.c`** -> AI Confidence: **99.31%**
2730. **`usr/src/cmd/captoinfo/captoinfo.c`** -> AI Confidence: **99.31%**
2731. **`usr/src/cmd/cdrw/blank.c`** -> AI Confidence: **99.31%**
2732. **`usr/src/cmd/cdrw/bstream.c`** -> AI Confidence: **99.31%**
2733. **`usr/src/cmd/cdrw/dae.c`** -> AI Confidence: **99.31%**
2734. **`usr/src/cmd/cdrw/device.c`** -> AI Confidence: **99.31%**
2735. **`usr/src/cmd/cdrw/misc_scsi.c`** -> AI Confidence: **99.31%**
2736. **`usr/src/cmd/cdrw/mmc.c`** -> AI Confidence: **99.31%**
2737. **`usr/src/cmd/cdrw/toshiba.c`** -> AI Confidence: **99.31%**
2738. **`usr/src/cmd/cdrw/transport.c`** -> AI Confidence: **99.31%**
2739. **`usr/src/cmd/cdrw/util.c`** -> AI Confidence: **99.31%**
2740. **`usr/src/cmd/cdrw/write_audio.c`** -> AI Confidence: **99.31%**
2741. **`usr/src/cmd/cfgadm/cfgadm.c`** -> AI Confidence: **99.31%**
2742. **`usr/src/cmd/chmod/chmod.c`** -> AI Confidence: **99.31%**
2743. **`usr/src/cmd/cmd-crypto/cryptoadm/adm_kef.c`** -> AI Confidence: **99.31%**
2744. **`usr/src/cmd/cmd-crypto/cryptoadm/adm_kef_ioctl.c`** -> AI Confidence: **99.31%**
2745. **`usr/src/cmd/cmd-crypto/cryptoadm/adm_kef_util.c`** -> AI Confidence: **99.31%**
2746. **`usr/src/cmd/cmd-crypto/cryptoadm/adm_metaslot.c`** -> AI Confidence: **99.31%**
2747. **`usr/src/cmd/cmd-crypto/cryptoadm/adm_uef.c`** -> AI Confidence: **99.31%**
2748. **`usr/src/cmd/cmd-crypto/digest/digest.c`** -> AI Confidence: **99.31%**
2749. **`usr/src/cmd/cmd-crypto/kmfcfg/list.c`** -> AI Confidence: **99.31%**
2750. **`usr/src/cmd/cmd-crypto/pktool/inittoken.c`** -> AI Confidence: **99.31%**
2751. **`usr/src/cmd/cmd-crypto/pktool/pktool.c`** -> AI Confidence: **99.31%**
2752. **`usr/src/cmd/cmd-inet/common/kcmd.c`** -> AI Confidence: **99.31%**
2753. **`usr/src/cmd/cmd-inet/lib/ipmgmtd/ipmgmt_door.c`** -> AI Confidence: **99.31%**
2754. **`usr/src/cmd/cmd-inet/lib/ipmgmtd/ipmgmt_main.c`** -> AI Confidence: **99.31%**
2755. **`usr/src/cmd/cmd-inet/lib/ipmgmtd/ipmgmt_util.c`** -> AI Confidence: **99.31%**
2756. **`usr/src/cmd/cmd-inet/lib/nwamd/conditions.c`** -> AI Confidence: **99.31%**
2757. **`usr/src/cmd/cmd-inet/lib/nwamd/dlpi_events.c`** -> AI Confidence: **99.31%**
2758. **`usr/src/cmd/cmd-inet/lib/nwamd/door_if.c`** -> AI Confidence: **99.31%**
2759. **`usr/src/cmd/cmd-inet/lib/nwamd/events.c`** -> AI Confidence: **99.31%**
2760. **`usr/src/cmd/cmd-inet/lib/nwamd/known_wlans.c`** -> AI Confidence: **99.31%**
2761. **`usr/src/cmd/cmd-inet/lib/nwamd/loc.c`** -> AI Confidence: **99.31%**
2762. **`usr/src/cmd/cmd-inet/lib/nwamd/main.c`** -> AI Confidence: **99.31%**
2763. **`usr/src/cmd/cmd-inet/lib/nwamd/ncp.c`** -> AI Confidence: **99.31%**
2764. **`usr/src/cmd/cmd-inet/lib/nwamd/ncu.c`** -> AI Confidence: **99.31%**
2765. **`usr/src/cmd/cmd-inet/lib/nwamd/ncu_ip.c`** -> AI Confidence: **99.31%**
2766. **`usr/src/cmd/cmd-inet/lib/nwamd/ncu_phys.c`** -> AI Confidence: **99.31%**
2767. **`usr/src/cmd/cmd-inet/lib/nwamd/routing_events.c`** -> AI Confidence: **99.31%**
2768. **`usr/src/cmd/cmd-inet/lib/nwamd/sysevent_events.c`** -> AI Confidence: **99.31%**
2769. **`usr/src/cmd/cmd-inet/lib/nwamd/util.c`** -> AI Confidence: **99.31%**
2770. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/async.c`** -> AI Confidence: **99.31%**
2771. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/bound.c`** -> AI Confidence: **99.31%**
2772. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/class_id.c`** -> AI Confidence: **99.31%**
2773. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/defaults.c`** -> AI Confidence: **99.31%**
2774. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/init_reboot.c`** -> AI Confidence: **99.31%**
2775. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/interface.c`** -> AI Confidence: **99.31%**
2776. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/ipc_action.c`** -> AI Confidence: **99.31%**
2777. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/packet.c`** -> AI Confidence: **99.31%**
2778. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/release.c`** -> AI Confidence: **99.31%**
2779. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/renew.c`** -> AI Confidence: **99.31%**
2780. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/request.c`** -> AI Confidence: **99.31%**
2781. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/script_handler.c`** -> AI Confidence: **99.31%**
2782. **`usr/src/cmd/cmd-inet/sbin/dhcpagent/select.c`** -> AI Confidence: **99.31%**
2783. **`usr/src/cmd/cmd-inet/sbin/netstrategy/netstrategy.c`** -> AI Confidence: **99.31%**
2784. **`usr/src/cmd/cmd-inet/usr.bin/finger.c`** -> AI Confidence: **99.31%**
2785. **`usr/src/cmd/cmd-inet/usr.bin/ftp/secure.c`** -> AI Confidence: **99.31%**
2786. **`usr/src/cmd/cmd-inet/usr.bin/nc/netcat.c`** -> AI Confidence: **99.31%**
2787. **`usr/src/cmd/cmd-inet/usr.bin/nc/socks.c`** -> AI Confidence: **99.31%**
2788. **`usr/src/cmd/cmd-inet/usr.bin/pppd/auth.c`** -> AI Confidence: **99.31%**
2789. **`usr/src/cmd/cmd-inet/usr.bin/pppd/chap.c`** -> AI Confidence: **99.31%**
2790. **`usr/src/cmd/cmd-inet/usr.bin/pppd/chap_ms.c`** -> AI Confidence: **99.31%**
2791. **`usr/src/cmd/cmd-inet/usr.bin/pppd/demand.c`** -> AI Confidence: **99.31%**
2792. **`usr/src/cmd/cmd-inet/usr.bin/pppd/ipv6cp.c`** -> AI Confidence: **99.31%**
2793. **`usr/src/cmd/cmd-inet/usr.bin/pppd/main.c`** -> AI Confidence: **99.31%**
2794. **`usr/src/cmd/cmd-inet/usr.bin/pppd/multilink.c`** -> AI Confidence: **99.31%**
2795. **`usr/src/cmd/cmd-inet/usr.bin/pppd/options.c`** -> AI Confidence: **99.31%**
2796. **`usr/src/cmd/cmd-inet/usr.bin/pppd/plugins/pppoe.c`** -> AI Confidence: **99.31%**
2797. **`usr/src/cmd/cmd-inet/usr.bin/pppd/sys-solaris.c`** -> AI Confidence: **99.31%**
2798. **`usr/src/cmd/cmd-inet/usr.bin/pppstats/pppstats.c`** -> AI Confidence: **99.31%**
2799. **`usr/src/cmd/cmd-inet/usr.bin/rcp.c`** -> AI Confidence: **99.31%**
2800. **`usr/src/cmd/cmd-inet/usr.bin/rdist/docmd.c`** -> AI Confidence: **99.31%**
2801. **`usr/src/cmd/cmd-inet/usr.bin/rdist/server.c`** -> AI Confidence: **99.31%**
2802. **`usr/src/cmd/cmd-inet/usr.bin/rlogin.c`** -> AI Confidence: **99.31%**
2803. **`usr/src/cmd/cmd-inet/usr.bin/rsh.c`** -> AI Confidence: **99.31%**
2804. **`usr/src/cmd/cmd-inet/usr.bin/ruptime.c`** -> AI Confidence: **99.31%**
2805. **`usr/src/cmd/cmd-inet/usr.bin/rwho.c`** -> AI Confidence: **99.31%**
2806. **`usr/src/cmd/cmd-inet/usr.bin/telnet/auth.c`** -> AI Confidence: **99.31%**
2807. **`usr/src/cmd/cmd-inet/usr.bin/telnet/authenc.c`** -> AI Confidence: **99.31%**
2808. **`usr/src/cmd/cmd-inet/usr.bin/telnet/commands.c`** -> AI Confidence: **99.31%**
2809. **`usr/src/cmd/cmd-inet/usr.bin/telnet/kerberos5.c`** -> AI Confidence: **99.31%**
2810. **`usr/src/cmd/cmd-inet/usr.bin/telnet/ring.c`** -> AI Confidence: **99.31%**
2811. **`usr/src/cmd/cmd-inet/usr.bin/telnet/sys_bsd.c`** -> AI Confidence: **99.31%**
2812. **`usr/src/cmd/cmd-inet/usr.bin/telnet/telnet.c`** -> AI Confidence: **99.31%**
2813. **`usr/src/cmd/cmd-inet/usr.bin/telnet/utilities.c`** -> AI Confidence: **99.31%**
2814. **`usr/src/cmd/cmd-inet/usr.bin/tftp/main.c`** -> AI Confidence: **99.31%**
2815. **`usr/src/cmd/cmd-inet/usr.bin/tftp/tftp.c`** -> AI Confidence: **99.31%**
2816. **`usr/src/cmd/cmd-inet/usr.bin/tftp/tftpsubs.c`** -> AI Confidence: **99.31%**
2817. **`usr/src/cmd/cmd-inet/usr.lib/bridged/door.c`** -> AI Confidence: **99.31%**
2818. **`usr/src/cmd/cmd-inet/usr.lib/bridged/events.c`** -> AI Confidence: **99.31%**
2819. **`usr/src/cmd/cmd-inet/usr.lib/bridged/rstp.c`** -> AI Confidence: **99.31%**
2820. **`usr/src/cmd/cmd-inet/usr.lib/ilbd/ilb/ilb_probe.c`** -> AI Confidence: **99.31%**
2821. **`usr/src/cmd/cmd-inet/usr.lib/ilbd/ilbd_main.c`** -> AI Confidence: **99.31%**
2822. **`usr/src/cmd/cmd-inet/usr.lib/ilbd/ilbd_nat.c`** -> AI Confidence: **99.31%**
2823. **`usr/src/cmd/cmd-inet/usr.lib/ilbd/ilbd_rules.c`** -> AI Confidence: **99.31%**
2824. **`usr/src/cmd/cmd-inet/usr.lib/ilbd/ilbd_scf.c`** -> AI Confidence: **99.31%**
2825. **`usr/src/cmd/cmd-inet/usr.lib/in.chargend/in.chargend.c`** -> AI Confidence: **99.31%**
2826. **`usr/src/cmd/cmd-inet/usr.lib/in.discardd/in.discardd.c`** -> AI Confidence: **99.31%**
2827. **`usr/src/cmd/cmd-inet/usr.lib/inetd/inetd.c`** -> AI Confidence: **99.31%**
2828. **`usr/src/cmd/cmd-inet/usr.lib/inetd/wait.c`** -> AI Confidence: **99.31%**
2829. **`usr/src/cmd/cmd-inet/usr.lib/pppoe/options.c`** -> AI Confidence: **99.31%**
2830. **`usr/src/cmd/cmd-inet/usr.lib/pppoe/pppoec.c`** -> AI Confidence: **99.31%**
2831. **`usr/src/cmd/cmd-inet/usr.lib/vrrpd/vrrpd.c`** -> AI Confidence: **99.31%**
2832. **`usr/src/cmd/cmd-inet/usr.lib/wpad/wpa.c`** -> AI Confidence: **99.31%**
2833. **`usr/src/cmd/cmd-inet/usr.lib/wpad/wpa_supplicant.c`** -> AI Confidence: **99.31%**
2834. **`usr/src/cmd/cmd-inet/usr.sbin/arp.c`** -> AI Confidence: **99.31%**
2835. **`usr/src/cmd/cmd-inet/usr.sbin/if_mpadm.c`** -> AI Confidence: **99.31%**
2836. **`usr/src/cmd/cmd-inet/usr.sbin/ifconfig/ifconfig.c`** -> AI Confidence: **99.31%**
2837. **`usr/src/cmd/cmd-inet/usr.sbin/ifconfig/revarp.c`** -> AI Confidence: **99.31%**
2838. **`usr/src/cmd/cmd-inet/usr.sbin/ilbadm/ilbadm.c`** -> AI Confidence: **99.31%**
2839. **`usr/src/cmd/cmd-inet/usr.sbin/ilbadm/ilbadm_hc.c`** -> AI Confidence: **99.31%**
2840. **`usr/src/cmd/cmd-inet/usr.sbin/ilbadm/ilbadm_nat.c`** -> AI Confidence: **99.31%**
2841. **`usr/src/cmd/cmd-inet/usr.sbin/ilbadm/ilbadm_rules.c`** -> AI Confidence: **99.31%**
2842. **`usr/src/cmd/cmd-inet/usr.sbin/ilbadm/ilbadm_sg.c`** -> AI Confidence: **99.31%**
2843. **`usr/src/cmd/cmd-inet/usr.sbin/in.comsat.c`** -> AI Confidence: **99.31%**
2844. **`usr/src/cmd/cmd-inet/usr.sbin/in.rexecd.c`** -> AI Confidence: **99.31%**
2845. **`usr/src/cmd/cmd-inet/usr.sbin/in.routed/if.c`** -> AI Confidence: **99.31%**
2846. **`usr/src/cmd/cmd-inet/usr.sbin/in.routed/rtquery.c`** -> AI Confidence: **99.31%**
2847. **`usr/src/cmd/cmd-inet/usr.sbin/in.routed/trace.c`** -> AI Confidence: **99.31%**
2848. **`usr/src/cmd/cmd-inet/usr.sbin/in.rshd.c`** -> AI Confidence: **99.31%**
2849. **`usr/src/cmd/cmd-inet/usr.sbin/in.rwhod.c`** -> AI Confidence: **99.31%**
2850. **`usr/src/cmd/cmd-inet/usr.sbin/in.talkd/announce.c`** -> AI Confidence: **99.31%**
2851. **`usr/src/cmd/cmd-inet/usr.sbin/in.talkd/in.talkd.c`** -> AI Confidence: **99.31%**
2852. **`usr/src/cmd/cmd-inet/usr.sbin/in.talkd/process.c`** -> AI Confidence: **99.31%**
2853. **`usr/src/cmd/cmd-inet/usr.sbin/in.telnetd.c`** -> AI Confidence: **99.31%**
2854. **`usr/src/cmd/cmd-inet/usr.sbin/in.tftpd.c`** -> AI Confidence: **99.31%**
2855. **`usr/src/cmd/cmd-inet/usr.sbin/ipaddrsel.c`** -> AI Confidence: **99.31%**
2856. **`usr/src/cmd/cmd-inet/usr.sbin/ipqosconf/ipqosconf.c`** -> AI Confidence: **99.31%**
2857. **`usr/src/cmd/cmd-inet/usr.sbin/ipsecutils/ikeadm.c`** -> AI Confidence: **99.31%**
2858. **`usr/src/cmd/cmd-inet/usr.sbin/ipsecutils/ipsecconf.c`** -> AI Confidence: **99.31%**
2859. **`usr/src/cmd/cmd-inet/usr.sbin/ipsecutils/ipseckey.c`** -> AI Confidence: **99.31%**
2860. **`usr/src/cmd/cmd-inet/usr.sbin/ndd.c`** -> AI Confidence: **99.31%**
2861. **`usr/src/cmd/cmd-inet/usr.sbin/nwamcfg/nwamcfg.c`** -> AI Confidence: **99.31%**
2862. **`usr/src/cmd/cmd-inet/usr.sbin/ping/ping.c`** -> AI Confidence: **99.31%**
2863. **`usr/src/cmd/cmd-inet/usr.sbin/ping/ping_aux.c`** -> AI Confidence: **99.31%**
2864. **`usr/src/cmd/cmd-inet/usr.sbin/ping/ping_aux6.c`** -> AI Confidence: **99.31%**
2865. **`usr/src/cmd/cmd-inet/usr.sbin/route.c`** -> AI Confidence: **99.31%**
2866. **`usr/src/cmd/cmd-inet/usr.sbin/routeadm/routeadm.c`** -> AI Confidence: **99.31%**
2867. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop.c`** -> AI Confidence: **99.31%**
2868. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_arp.c`** -> AI Confidence: **99.31%**
2869. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_bparam.c`** -> AI Confidence: **99.31%**
2870. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_capture.c`** -> AI Confidence: **99.31%**
2871. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_dhcpv6.c`** -> AI Confidence: **99.31%**
2872. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_display.c`** -> AI Confidence: **99.31%**
2873. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_dns.c`** -> AI Confidence: **99.31%**
2874. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_ether.c`** -> AI Confidence: **99.31%**
2875. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_igmp.c`** -> AI Confidence: **99.31%**
2876. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_ip.c`** -> AI Confidence: **99.31%**
2877. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_ipsec.c`** -> AI Confidence: **99.31%**
2878. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_mount.c`** -> AI Confidence: **99.31%**
2879. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_nfs.c`** -> AI Confidence: **99.31%**
2880. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_nfs3.c`** -> AI Confidence: **99.31%**
2881. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_nfs4.c`** -> AI Confidence: **99.31%**
2882. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_nfs_acl.c`** -> AI Confidence: **99.31%**
2883. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_nis.c`** -> AI Confidence: **99.31%**
2884. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_nlm.c`** -> AI Confidence: **99.31%**
2885. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_ospf.c`** -> AI Confidence: **99.31%**
2886. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_ospf6.c`** -> AI Confidence: **99.31%**
2887. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_pmap.c`** -> AI Confidence: **99.31%**
2888. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_ppp.c`** -> AI Confidence: **99.31%**
2889. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_pppoe.c`** -> AI Confidence: **99.31%**
2890. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_rip.c`** -> AI Confidence: **99.31%**
2891. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_rip6.c`** -> AI Confidence: **99.31%**
2892. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_rpc.c`** -> AI Confidence: **99.31%**
2893. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_rpcsec.c`** -> AI Confidence: **99.31%**
2894. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_rport.c`** -> AI Confidence: **99.31%**
2895. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_solarnet.c`** -> AI Confidence: **99.31%**
2896. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_tcp.c`** -> AI Confidence: **99.31%**
2897. **`usr/src/cmd/cmd-inet/usr.sbin/snoop/snoop_udp.c`** -> AI Confidence: **99.31%**
2898. **`usr/src/cmd/cmd-inet/usr.sbin/sppptun/sppptun.c`** -> AI Confidence: **99.31%**
2899. **`usr/src/cmd/cmd-inet/usr.sbin/syncinit.c`** -> AI Confidence: **99.31%**
2900. **`usr/src/cmd/cmd-inet/usr.sbin/syncloop.c`** -> AI Confidence: **99.31%**
2901. **`usr/src/cmd/cmd-inet/usr.sbin/syncstat.c`** -> AI Confidence: **99.31%**
2902. **`usr/src/cmd/cmd-inet/usr.sbin/traceroute/traceroute.c`** -> AI Confidence: **99.31%**
2903. **`usr/src/cmd/cmd-inet/usr.sbin/traceroute/traceroute_aux.c`** -> AI Confidence: **99.31%**
2904. **`usr/src/cmd/cmd-inet/usr.sbin/traceroute/traceroute_aux6.c`** -> AI Confidence: **99.31%**
2905. **`usr/src/cmd/cmd-inet/usr.sbin/wificonfig/wificonfig.c`** -> AI Confidence: **99.31%**
2906. **`usr/src/cmd/connstat/connstat_main.c`** -> AI Confidence: **99.31%**
2907. **`usr/src/cmd/connstat/connstat_mib.c`** -> AI Confidence: **99.31%**
2908. **`usr/src/cmd/consadm/consadm.c`** -> AI Confidence: **99.31%**
2909. **`usr/src/cmd/coreadm/coreadm.c`** -> AI Confidence: **99.31%**
2910. **`usr/src/cmd/cpc/common/cpustat.c`** -> AI Confidence: **99.31%**
2911. **`usr/src/cmd/cpc/common/cputrack.c`** -> AI Confidence: **99.31%**
2912. **`usr/src/cmd/cpio/utils.c`** -> AI Confidence: **99.31%**
2913. **`usr/src/cmd/cron/at.c`** -> AI Confidence: **99.31%**
2914. **`usr/src/cmd/cron/atrm.c`** -> AI Confidence: **99.31%**
2915. **`usr/src/cmd/cron/cron.c`** -> AI Confidence: **99.31%**
2916. **`usr/src/cmd/cron/funcs.c`** -> AI Confidence: **99.31%**
2917. **`usr/src/cmd/cron/permit.c`** -> AI Confidence: **99.31%**
2918. **`usr/src/cmd/csh/sh.c`** -> AI Confidence: **99.31%**
2919. **`usr/src/cmd/csh/wait3.c`** -> AI Confidence: **99.31%**
2920. **`usr/src/cmd/ctstat/ctstat.c`** -> AI Confidence: **99.31%**
2921. **`usr/src/cmd/ctwatch/ctwatch.c`** -> AI Confidence: **99.31%**
2922. **`usr/src/cmd/cxgbetool/cudbg_view.c`** -> AI Confidence: **99.31%**
2923. **`usr/src/cmd/cxgbetool/cxgbetool.c`** -> AI Confidence: **99.31%**
2924. **`usr/src/cmd/datadm/datadm.c`** -> AI Confidence: **99.31%**
2925. **`usr/src/cmd/dc/dc.c`** -> AI Confidence: **99.31%**
2926. **`usr/src/cmd/dcs/sparc/sun4u/dcs.c`** -> AI Confidence: **99.31%**
2927. **`usr/src/cmd/dcs/sparc/sun4u/dcs_msg.c`** -> AI Confidence: **99.31%**
2928. **`usr/src/cmd/dcs/sparc/sun4u/rdr_messages.c`** -> AI Confidence: **99.31%**
2929. **`usr/src/cmd/dcs/sparc/sun4u/ri_init.c`** -> AI Confidence: **99.31%**
2930. **`usr/src/cmd/demangle/demangle.c`** -> AI Confidence: **99.31%**
2931. **`usr/src/cmd/devctl/devctl.c`** -> AI Confidence: **99.31%**
2932. **`usr/src/cmd/devfsadm/cfg_link.c`** -> AI Confidence: **99.31%**
2933. **`usr/src/cmd/devfsadm/devpolicy.c`** -> AI Confidence: **99.31%**
2934. **`usr/src/cmd/devfsadm/disk_link.c`** -> AI Confidence: **99.31%**
2935. **`usr/src/cmd/devfsadm/lofi_link.c`** -> AI Confidence: **99.31%**
2936. **`usr/src/cmd/devfsadm/port_link.c`** -> AI Confidence: **99.31%**
2937. **`usr/src/cmd/devfsadm/usb_link.c`** -> AI Confidence: **99.31%**
2938. **`usr/src/cmd/devmgmt/cmds/devattr.c`** -> AI Confidence: **99.31%**
2939. **`usr/src/cmd/devmgmt/cmds/devfree.c`** -> AI Confidence: **99.31%**
2940. **`usr/src/cmd/devmgmt/cmds/getdev.c`** -> AI Confidence: **99.31%**
2941. **`usr/src/cmd/devmgmt/cmds/putdgrp.c`** -> AI Confidence: **99.31%**
2942. **`usr/src/cmd/dfs.cmds/sharectl/sharectl.c`** -> AI Confidence: **99.31%**
2943. **`usr/src/cmd/dfs.cmds/sharemgr/sharemgr_main.c`** -> AI Confidence: **99.31%**
2944. **`usr/src/cmd/diff/diff.c`** -> AI Confidence: **99.31%**
2945. **`usr/src/cmd/diff/diffh.c`** -> AI Confidence: **99.31%**
2946. **`usr/src/cmd/dis/dis_target.c`** -> AI Confidence: **99.31%**
2947. **`usr/src/cmd/diskscan/diskscan.c`** -> AI Confidence: **99.31%**
2948. **`usr/src/cmd/dispadmin/dispadmin.c`** -> AI Confidence: **99.31%**
2949. **`usr/src/cmd/dispadmin/subr.c`** -> AI Confidence: **99.31%**
2950. **`usr/src/cmd/dlmgmtd/dlmgmt_main.c`** -> AI Confidence: **99.31%**
2951. **`usr/src/cmd/dlmgmtd/dlmgmt_util.c`** -> AI Confidence: **99.31%**
2952. **`usr/src/cmd/dlstat/dlstat.c`** -> AI Confidence: **99.31%**
2953. **`usr/src/cmd/dlutil/dlled.c`** -> AI Confidence: **99.31%**
2954. **`usr/src/cmd/dlutil/dlrecv.c`** -> AI Confidence: **99.31%**
2955. **`usr/src/cmd/dlutil/dlsend.c`** -> AI Confidence: **99.31%**
2956. **`usr/src/cmd/dlutil/dltraninfo.c`** -> AI Confidence: **99.31%**
2957. **`usr/src/cmd/drd/drd.c`** -> AI Confidence: **99.31%**
2958. **`usr/src/cmd/dtrace/test/cmd/baddof/baddof.c`** -> AI Confidence: **99.31%**
2959. **`usr/src/cmd/dumpadm/dconf.c`** -> AI Confidence: **99.31%**
2960. **`usr/src/cmd/dumpadm/minfree.c`** -> AI Confidence: **99.31%**
2961. **`usr/src/cmd/dumpadm/utils.c`** -> AI Confidence: **99.31%**
2962. **`usr/src/cmd/dumpcs/dumpcs.c`** -> AI Confidence: **99.31%**
2963. **`usr/src/cmd/ed/ed.c`** -> AI Confidence: **99.31%**
2964. **`usr/src/cmd/eeprom/i386/benv.c`** -> AI Confidence: **99.31%**
2965. **`usr/src/cmd/eeprom/sparc/openprom.c`** -> AI Confidence: **99.31%**
2966. **`usr/src/cmd/eject/eject.c`** -> AI Confidence: **99.31%**
2967. **`usr/src/cmd/enhance/enhance.c`** -> AI Confidence: **99.31%**
2968. **`usr/src/cmd/etdump/etdump.c`** -> AI Confidence: **99.31%**
2969. **`usr/src/cmd/exstr/exstr.c`** -> AI Confidence: **99.31%**
2970. **`usr/src/cmd/fcinfo/printAttrs.c`** -> AI Confidence: **99.31%**
2971. **`usr/src/cmd/fdformat/fdformat.c`** -> AI Confidence: **99.31%**
2972. **`usr/src/cmd/fdisk/fdisk.c`** -> AI Confidence: **99.31%**
2973. **`usr/src/cmd/file/elf_read.c`** -> AI Confidence: **99.31%**
2974. **`usr/src/cmd/filesync/debug.c`** -> AI Confidence: **99.31%**
2975. **`usr/src/cmd/filesync/eval.c`** -> AI Confidence: **99.31%**
2976. **`usr/src/cmd/filesync/main.c`** -> AI Confidence: **99.31%**
2977. **`usr/src/cmd/filesync/rules.c`** -> AI Confidence: **99.31%**
2978. **`usr/src/cmd/find/find.c`** -> AI Confidence: **99.31%**
2979. **`usr/src/cmd/flowadm/flowadm.c`** -> AI Confidence: **99.31%**
2980. **`usr/src/cmd/flowstat/flowstat.c`** -> AI Confidence: **99.31%**
2981. **`usr/src/cmd/fm/eversholt/common/check.c`** -> AI Confidence: **99.31%**
2982. **`usr/src/cmd/fm/eversholt/common/eftread.c`** -> AI Confidence: **99.31%**
2983. **`usr/src/cmd/fm/eversholt/common/lut.c`** -> AI Confidence: **99.31%**
2984. **`usr/src/cmd/fm/eversholt/common/ptree.c`** -> AI Confidence: **99.31%**
2985. **`usr/src/cmd/fm/eversholt/common/tree.c`** -> AI Confidence: **99.31%**
2986. **`usr/src/cmd/fm/fmadm/common/fmadm.c`** -> AI Confidence: **99.31%**
2987. **`usr/src/cmd/fm/fmd/common/fmd.c`** -> AI Confidence: **99.31%**
2988. **`usr/src/cmd/fm/fmd/common/fmd_api.c`** -> AI Confidence: **99.31%**
2989. **`usr/src/cmd/fm/fmd/common/fmd_builtin.c`** -> AI Confidence: **99.31%**
2990. **`usr/src/cmd/fm/fmd/common/fmd_case.c`** -> AI Confidence: **99.31%**
2991. **`usr/src/cmd/fm/fmd/common/fmd_ckpt.c`** -> AI Confidence: **99.31%**
2992. **`usr/src/cmd/fm/fmd/common/fmd_conf.c`** -> AI Confidence: **99.31%**
2993. **`usr/src/cmd/fm/fmd/common/fmd_dispq.c`** -> AI Confidence: **99.31%**
2994. **`usr/src/cmd/fm/fmd/common/fmd_dr.c`** -> AI Confidence: **99.31%**
2995. **`usr/src/cmd/fm/fmd/common/fmd_event.c`** -> AI Confidence: **99.31%**
2996. **`usr/src/cmd/fm/fmd/common/fmd_mdb.c`** -> AI Confidence: **99.31%**
2997. **`usr/src/cmd/fm/fmd/common/fmd_rpc_adm.c`** -> AI Confidence: **99.31%**
2998. **`usr/src/cmd/fm/fmd/common/fmd_subr.c`** -> AI Confidence: **99.31%**
2999. **`usr/src/cmd/fm/fmd/common/fmd_sysevent.c`** -> AI Confidence: **99.31%**
3000. **`usr/src/cmd/fm/fmdump/common/fmdump.c`** -> AI Confidence: **99.31%**
3001. **`usr/src/cmd/fm/fminject/common/inj_main.c`** -> AI Confidence: **99.31%**
3002. **`usr/src/cmd/fm/fmstat/common/fmstat.c`** -> AI Confidence: **99.31%**
3003. **`usr/src/cmd/fm/fmtopo/common/fmtopo.c`** -> AI Confidence: **99.31%**
3004. **`usr/src/cmd/fm/mcdecode/mcdecode.c`** -> AI Confidence: **99.31%**
3005. **`usr/src/cmd/fm/modules/common/cpumem-retire/cma_cpu_arch.c`** -> AI Confidence: **99.31%**
3006. **`usr/src/cmd/fm/modules/common/cpumem-retire/cma_main.c`** -> AI Confidence: **99.31%**
3007. **`usr/src/cmd/fm/modules/common/disk-monitor/diskmon_conf.c`** -> AI Confidence: **99.31%**
3008. **`usr/src/cmd/fm/modules/common/disk-monitor/dm_platform.c`** -> AI Confidence: **99.31%**
3009. **`usr/src/cmd/fm/modules/common/disk-monitor/hotplug_mgr.c`** -> AI Confidence: **99.31%**
3010. **`usr/src/cmd/fm/modules/common/disk-monitor/schg_mgr.c`** -> AI Confidence: **99.31%**
3011. **`usr/src/cmd/fm/modules/common/disk-monitor/topo_gather.c`** -> AI Confidence: **99.31%**
3012. **`usr/src/cmd/fm/modules/common/disk-transport/disk_transport.c`** -> AI Confidence: **99.31%**
3013. **`usr/src/cmd/fm/modules/common/event-transport/etm.c`** -> AI Confidence: **99.31%**
3014. **`usr/src/cmd/fm/modules/common/eversholt/eft_mdb.c`** -> AI Confidence: **99.31%**
3015. **`usr/src/cmd/fm/modules/common/eversholt/eval.c`** -> AI Confidence: **99.31%**
3016. **`usr/src/cmd/fm/modules/common/eversholt/fme.c`** -> AI Confidence: **99.31%**
3017. **`usr/src/cmd/fm/modules/common/eversholt/iexpr.c`** -> AI Confidence: **99.31%**
3018. **`usr/src/cmd/fm/modules/common/eversholt/itree.c`** -> AI Confidence: **99.31%**
3019. **`usr/src/cmd/fm/modules/common/eversholt/platform.c`** -> AI Confidence: **99.31%**
3020. **`usr/src/cmd/fm/modules/common/ext-event-transport/fmevt_inbound.c`** -> AI Confidence: **99.31%**
3021. **`usr/src/cmd/fm/modules/common/ext-event-transport/fmevt_outbound.c`** -> AI Confidence: **99.31%**
3022. **`usr/src/cmd/fm/modules/common/fabric-xlate/fabric-xlate.c`** -> AI Confidence: **99.31%**
3023. **`usr/src/cmd/fm/modules/common/fabric-xlate/fx_subr.c`** -> AI Confidence: **99.31%**
3024. **`usr/src/cmd/fm/modules/common/ip-transport/ip.c`** -> AI Confidence: **99.31%**
3025. **`usr/src/cmd/fm/modules/common/sensor-transport/sensor_transport.c`** -> AI Confidence: **99.31%**
3026. **`usr/src/cmd/fm/modules/common/ses-log-transport/ses_log_transport.c`** -> AI Confidence: **99.31%**
3027. **`usr/src/cmd/fm/modules/common/syslog-msgs/syslog.c`** -> AI Confidence: **99.31%**
3028. **`usr/src/cmd/fm/modules/common/zfs-diagnosis/zfs_de.c`** -> AI Confidence: **99.31%**
3029. **`usr/src/cmd/fm/modules/common/zfs-retire/zfs_retire.c`** -> AI Confidence: **99.31%**
3030. **`usr/src/cmd/fm/schemes/cpu/cpu.c`** -> AI Confidence: **99.31%**
3031. **`usr/src/cmd/fm/schemes/mem/mem.c`** -> AI Confidence: **99.31%**
3032. **`usr/src/cmd/fm/schemes/mem/mem_read.c`** -> AI Confidence: **99.31%**
3033. **`usr/src/cmd/fmthard/fmthard.c`** -> AI Confidence: **99.31%**
3034. **`usr/src/cmd/fold/fold.c`** -> AI Confidence: **99.31%**
3035. **`usr/src/cmd/format/add_definition.c`** -> AI Confidence: **99.31%**
3036. **`usr/src/cmd/format/auto_sense.c`** -> AI Confidence: **99.31%**
3037. **`usr/src/cmd/format/checkdev.c`** -> AI Confidence: **99.31%**
3038. **`usr/src/cmd/format/ctlr_ata.c`** -> AI Confidence: **99.31%**
3039. **`usr/src/cmd/format/ctlr_scsi.c`** -> AI Confidence: **99.31%**
3040. **`usr/src/cmd/format/disk_generic.c`** -> AI Confidence: **99.31%**
3041. **`usr/src/cmd/format/ix_altsctr.c`** -> AI Confidence: **99.31%**
3042. **`usr/src/cmd/format/label.c`** -> AI Confidence: **99.31%**
3043. **`usr/src/cmd/format/main.c`** -> AI Confidence: **99.31%**
3044. **`usr/src/cmd/format/menu_cache.c`** -> AI Confidence: **99.31%**
3045. **`usr/src/cmd/format/menu_command.c`** -> AI Confidence: **99.31%**
3046. **`usr/src/cmd/format/menu_defect.c`** -> AI Confidence: **99.31%**
3047. **`usr/src/cmd/format/menu_fdisk.c`** -> AI Confidence: **99.31%**
3048. **`usr/src/cmd/format/menu_partition.c`** -> AI Confidence: **99.31%**
3049. **`usr/src/cmd/format/menu_scsi.c`** -> AI Confidence: **99.31%**
3050. **`usr/src/cmd/format/misc.c`** -> AI Confidence: **99.31%**
3051. **`usr/src/cmd/format/modify_partition.c`** -> AI Confidence: **99.31%**
3052. **`usr/src/cmd/format/partition.c`** -> AI Confidence: **99.31%**
3053. **`usr/src/cmd/format/startup.c`** -> AI Confidence: **99.31%**
3054. **`usr/src/cmd/fruadm/fruadm.c`** -> AI Confidence: **99.31%**
3055. **`usr/src/cmd/fs.d/autofs/auto_subr.c`** -> AI Confidence: **99.31%**
3056. **`usr/src/cmd/fs.d/autofs/autod_main.c`** -> AI Confidence: **99.31%**
3057. **`usr/src/cmd/fs.d/autofs/autod_parse.c`** -> AI Confidence: **99.31%**
3058. **`usr/src/cmd/fs.d/autofs/autod_readdir.c`** -> AI Confidence: **99.31%**
3059. **`usr/src/cmd/fs.d/autofs/autod_xdr.c`** -> AI Confidence: **99.31%**
3060. **`usr/src/cmd/fs.d/autofs/automount.c`** -> AI Confidence: **99.31%**
3061. **`usr/src/cmd/fs.d/autofs/ns_fnmount.c`** -> AI Confidence: **99.31%**
3062. **`usr/src/cmd/fs.d/autofs/ns_fnreaddir.c`** -> AI Confidence: **99.31%**
3063. **`usr/src/cmd/fs.d/autofs/ns_ldap.c`** -> AI Confidence: **99.31%**
3064. **`usr/src/cmd/fs.d/autofs/ns_nis.c`** -> AI Confidence: **99.31%**
3065. **`usr/src/cmd/fs.d/ctfs/mount.c`** -> AI Confidence: **99.31%**
3066. **`usr/src/cmd/fs.d/dev/mount.c`** -> AI Confidence: **99.31%**
3067. **`usr/src/cmd/fs.d/df.c`** -> AI Confidence: **99.31%**
3068. **`usr/src/cmd/fs.d/fd/mount.c`** -> AI Confidence: **99.31%**
3069. **`usr/src/cmd/fs.d/fslib.c`** -> AI Confidence: **99.31%**
3070. **`usr/src/cmd/fs.d/hsfs/fstyp/fstyp.c`** -> AI Confidence: **99.31%**
3071. **`usr/src/cmd/fs.d/hsfs/mount/mount.c`** -> AI Confidence: **99.31%**
3072. **`usr/src/cmd/fs.d/mntfs/mount.c`** -> AI Confidence: **99.31%**
3073. **`usr/src/cmd/fs.d/nfs/clear_locks/clear_locks.c`** -> AI Confidence: **99.31%**
3074. **`usr/src/cmd/fs.d/nfs/lib/nfs_resolve.c`** -> AI Confidence: **99.31%**
3075. **`usr/src/cmd/fs.d/nfs/lib/nfs_sec.c`** -> AI Confidence: **99.31%**
3076. **`usr/src/cmd/fs.d/nfs/lib/nfs_subr.c`** -> AI Confidence: **99.31%**
3077. **`usr/src/cmd/fs.d/nfs/lib/ref_subr.c`** -> AI Confidence: **99.31%**
3078. **`usr/src/cmd/fs.d/nfs/lockd/lockd.c`** -> AI Confidence: **99.31%**
3079. **`usr/src/cmd/fs.d/nfs/mountd/nfs_cmd.c`** -> AI Confidence: **99.31%**
3080. **`usr/src/cmd/fs.d/nfs/mountd/nfsauth.c`** -> AI Confidence: **99.31%**
3081. **`usr/src/cmd/fs.d/nfs/nfsd/nfsd.c`** -> AI Confidence: **99.31%**
3082. **`usr/src/cmd/fs.d/nfs/nfslog/dbtab.c`** -> AI Confidence: **99.31%**
3083. **`usr/src/cmd/fs.d/nfs/nfslog/nfslog_trans.c`** -> AI Confidence: **99.31%**
3084. **`usr/src/cmd/fs.d/nfs/nfslog/nfslogd.c`** -> AI Confidence: **99.31%**
3085. **`usr/src/cmd/fs.d/nfs/nfslog/process_buffer.c`** -> AI Confidence: **99.31%**
3086. **`usr/src/cmd/fs.d/nfs/nfslog/readbuf.c`** -> AI Confidence: **99.31%**
3087. **`usr/src/cmd/fs.d/nfs/nfsmapid/nfsmapid_server.c`** -> AI Confidence: **99.31%**
3088. **`usr/src/cmd/fs.d/nfs/nfsmapid/nfsmapid_test.c`** -> AI Confidence: **99.31%**
3089. **`usr/src/cmd/fs.d/nfs/showmount/showmount.c`** -> AI Confidence: **99.31%**
3090. **`usr/src/cmd/fs.d/nfs/statd/sm_proc.c`** -> AI Confidence: **99.31%**
3091. **`usr/src/cmd/fs.d/nfs/statd/sm_statd.c`** -> AI Confidence: **99.31%**
3092. **`usr/src/cmd/fs.d/nfs/tests/rpcsec_gss_conn/rpcsec_gss_conn.c`** -> AI Confidence: **99.31%**
3093. **`usr/src/cmd/fs.d/nfs/tests/test_svc_tp_create/test_svc_tp_create.c`** -> AI Confidence: **99.31%**
3094. **`usr/src/cmd/fs.d/nfs/umount/umount.c`** -> AI Confidence: **99.31%**
3095. **`usr/src/cmd/fs.d/objfs/mount.c`** -> AI Confidence: **99.31%**
3096. **`usr/src/cmd/fs.d/pcfs/fsck/bpb.c`** -> AI Confidence: **99.31%**
3097. **`usr/src/cmd/fs.d/pcfs/fsck/clusters.c`** -> AI Confidence: **99.31%**
3098. **`usr/src/cmd/fs.d/pcfs/fsck/dir.c`** -> AI Confidence: **99.31%**
3099. **`usr/src/cmd/fs.d/pcfs/fsck/fat.c`** -> AI Confidence: **99.31%**
3100. **`usr/src/cmd/fs.d/pcfs/fsck/fsck_main.c`** -> AI Confidence: **99.31%**
3101. **`usr/src/cmd/fs.d/pcfs/mkfs/mkfs_main.c`** -> AI Confidence: **99.31%**
3102. **`usr/src/cmd/fs.d/proc/mount.c`** -> AI Confidence: **99.31%**
3103. **`usr/src/cmd/fs.d/reparsed/reparsed.c`** -> AI Confidence: **99.31%**
3104. **`usr/src/cmd/fs.d/sharefs/mount.c`** -> AI Confidence: **99.31%**
3105. **`usr/src/cmd/fs.d/smbclnt/fksmbcl/fkiod_cl.c`** -> AI Confidence: **99.31%**
3106. **`usr/src/cmd/fs.d/smbclnt/fksmbcl/fknewvc.c`** -> AI Confidence: **99.31%**
3107. **`usr/src/cmd/fs.d/smbclnt/fksmbcl/fksmbcl_main.c`** -> AI Confidence: **99.31%**
3108. **`usr/src/cmd/fs.d/smbclnt/fksmbcl/shares.c`** -> AI Confidence: **99.31%**
3109. **`usr/src/cmd/fs.d/smbclnt/smbiod-svc/smbiod-svc.c`** -> AI Confidence: **99.31%**
3110. **`usr/src/cmd/fs.d/smbclnt/smbutil/lookup.c`** -> AI Confidence: **99.31%**
3111. **`usr/src/cmd/fs.d/smbclnt/smbutil/shares_rpc.c`** -> AI Confidence: **99.31%**
3112. **`usr/src/cmd/fs.d/smbclnt/smbutil/smbutil.c`** -> AI Confidence: **99.31%**
3113. **`usr/src/cmd/fs.d/udfs/common/ud_lib.c`** -> AI Confidence: **99.31%**
3114. **`usr/src/cmd/fs.d/udfs/fsck/inode.c`** -> AI Confidence: **99.31%**
3115. **`usr/src/cmd/fs.d/udfs/fsck/main.c`** -> AI Confidence: **99.31%**
3116. **`usr/src/cmd/fs.d/udfs/fsck/pass1.c`** -> AI Confidence: **99.31%**
3117. **`usr/src/cmd/fs.d/udfs/fsck/utilities.c`** -> AI Confidence: **99.31%**
3118. **`usr/src/cmd/fs.d/udfs/fsdb/fsdb.c`** -> AI Confidence: **99.31%**
3119. **`usr/src/cmd/fs.d/udfs/fstyp/fstyp.c`** -> AI Confidence: **99.31%**
3120. **`usr/src/cmd/fs.d/udfs/labelit/labelit.c`** -> AI Confidence: **99.31%**
3121. **`usr/src/cmd/fs.d/udfs/mkfs/mkfs.c`** -> AI Confidence: **99.31%**
3122. **`usr/src/cmd/fs.d/udfs/mkfs/udfslib.c`** -> AI Confidence: **99.31%**
3123. **`usr/src/cmd/fs.d/udfs/mount/mount.c`** -> AI Confidence: **99.31%**
3124. **`usr/src/cmd/fs.d/ufs/clri/clri.c`** -> AI Confidence: **99.31%**
3125. **`usr/src/cmd/fs.d/ufs/df/df.c`** -> AI Confidence: **99.31%**
3126. **`usr/src/cmd/fs.d/ufs/edquota/edquota.c`** -> AI Confidence: **99.31%**
3127. **`usr/src/cmd/fs.d/ufs/ff/ff.c`** -> AI Confidence: **99.31%**
3128. **`usr/src/cmd/fs.d/ufs/fsck/dir.c`** -> AI Confidence: **99.31%**
3129. **`usr/src/cmd/fs.d/ufs/fsck/inode.c`** -> AI Confidence: **99.31%**
3130. **`usr/src/cmd/fs.d/ufs/fsck/main.c`** -> AI Confidence: **99.31%**
3131. **`usr/src/cmd/fs.d/ufs/fsck/pass2.c`** -> AI Confidence: **99.31%**
3132. **`usr/src/cmd/fs.d/ufs/fsck/pass3.c`** -> AI Confidence: **99.31%**
3133. **`usr/src/cmd/fs.d/ufs/fsck/pass4.c`** -> AI Confidence: **99.31%**
3134. **`usr/src/cmd/fs.d/ufs/fsck/pass5.c`** -> AI Confidence: **99.31%**
3135. **`usr/src/cmd/fs.d/ufs/fsck/setup.c`** -> AI Confidence: **99.31%**
3136. **`usr/src/cmd/fs.d/ufs/fsck/utilities.c`** -> AI Confidence: **99.31%**
3137. **`usr/src/cmd/fs.d/ufs/fsirand/fsirand.c`** -> AI Confidence: **99.31%**
3138. **`usr/src/cmd/fs.d/ufs/labelit/labelit.c`** -> AI Confidence: **99.31%**
3139. **`usr/src/cmd/fs.d/ufs/mkfs/mkfs.c`** -> AI Confidence: **99.31%**
3140. **`usr/src/cmd/fs.d/ufs/mount/mount.c`** -> AI Confidence: **99.31%**
3141. **`usr/src/cmd/fs.d/ufs/quot/quot.c`** -> AI Confidence: **99.31%**
3142. **`usr/src/cmd/fs.d/ufs/quota/quota.c`** -> AI Confidence: **99.31%**
3143. **`usr/src/cmd/fs.d/ufs/quotacheck/quotacheck.c`** -> AI Confidence: **99.31%**
3144. **`usr/src/cmd/fs.d/ufs/repquota/repquota.c`** -> AI Confidence: **99.31%**
3145. **`usr/src/cmd/fs.d/ufs/roll_log/roll_log.c`** -> AI Confidence: **99.31%**
3146. **`usr/src/cmd/fs.d/umount.c`** -> AI Confidence: **99.31%**
3147. **`usr/src/cmd/fuser/fuser.c`** -> AI Confidence: **99.31%**
3148. **`usr/src/cmd/fwflash/common/fwflash.c`** -> AI Confidence: **99.31%**
3149. **`usr/src/cmd/fwflash/plugins/transport/common/hermon.c`** -> AI Confidence: **99.31%**
3150. **`usr/src/cmd/fwflash/plugins/transport/common/sd.c`** -> AI Confidence: **99.31%**
3151. **`usr/src/cmd/fwflash/plugins/transport/common/tavor.c`** -> AI Confidence: **99.31%**
3152. **`usr/src/cmd/fwflash/plugins/transport/common/ufm.c`** -> AI Confidence: **99.31%**
3153. **`usr/src/cmd/genmsg/util.c`** -> AI Confidence: **99.31%**
3154. **`usr/src/cmd/getconf/getconf.c`** -> AI Confidence: **99.31%**
3155. **`usr/src/cmd/getent/dogetethers.c`** -> AI Confidence: **99.31%**
3156. **`usr/src/cmd/getent/dogethost.c`** -> AI Confidence: **99.31%**
3157. **`usr/src/cmd/getent/dogetipnodes.c`** -> AI Confidence: **99.31%**
3158. **`usr/src/cmd/getent/dogetnet.c`** -> AI Confidence: **99.31%**
3159. **`usr/src/cmd/getent/dogetnetmask.c`** -> AI Confidence: **99.31%**
3160. **`usr/src/cmd/getent/dogetproto.c`** -> AI Confidence: **99.31%**
3161. **`usr/src/cmd/getent/dogetserv.c`** -> AI Confidence: **99.31%**
3162. **`usr/src/cmd/getfacl/getfacl.c`** -> AI Confidence: **99.31%**
3163. **`usr/src/cmd/gpioadm/gpioadm.c`** -> AI Confidence: **99.31%**
3164. **`usr/src/cmd/gpioadm/gpioadm_controller.c`** -> AI Confidence: **99.31%**
3165. **`usr/src/cmd/gpioadm/gpioadm_dpio.c`** -> AI Confidence: **99.31%**
3166. **`usr/src/cmd/gpioadm/gpioadm_gpio.c`** -> AI Confidence: **99.31%**
3167. **`usr/src/cmd/gss/gssd/gssd.c`** -> AI Confidence: **99.31%**
3168. **`usr/src/cmd/gss/gssd/gssd_clnt_stubs.c`** -> AI Confidence: **99.31%**
3169. **`usr/src/cmd/gss/gssd/gssd_generic.c`** -> AI Confidence: **99.31%**
3170. **`usr/src/cmd/gss/gssd/gssd_getuid.c`** -> AI Confidence: **99.31%**
3171. **`usr/src/cmd/gss/gssd/gssd_handle.c`** -> AI Confidence: **99.31%**
3172. **`usr/src/cmd/gss/gssd/gssd_proc.c`** -> AI Confidence: **99.31%**
3173. **`usr/src/cmd/hal/addons/acpi/addon-acpi.c`** -> AI Confidence: **99.31%**
3174. **`usr/src/cmd/hal/addons/network-devices/cache.c`** -> AI Confidence: **99.31%**
3175. **`usr/src/cmd/hal/addons/network-devices/common.c`** -> AI Confidence: **99.31%**
3176. **`usr/src/cmd/hal/addons/network-devices/snmp.c`** -> AI Confidence: **99.31%**
3177. **`usr/src/cmd/hal/hald-runner/runner.c`** -> AI Confidence: **99.31%**
3178. **`usr/src/cmd/hal/hald/device.c`** -> AI Confidence: **99.31%**
3179. **`usr/src/cmd/hal/hald/hald.c`** -> AI Confidence: **99.31%**
3180. **`usr/src/cmd/hal/hald/hald_runner.c`** -> AI Confidence: **99.31%**
3181. **`usr/src/cmd/hal/hald/logger.c`** -> AI Confidence: **99.31%**
3182. **`usr/src/cmd/hal/hald/solaris/devinfo.c`** -> AI Confidence: **99.31%**
3183. **`usr/src/cmd/hal/hald/solaris/devinfo_acpi.c`** -> AI Confidence: **99.31%**
3184. **`usr/src/cmd/hal/hald/solaris/devinfo_ieee1394.c`** -> AI Confidence: **99.31%**
3185. **`usr/src/cmd/hal/hald/solaris/devinfo_misc.c`** -> AI Confidence: **99.31%**
3186. **`usr/src/cmd/hal/hald/solaris/hotplug.c`** -> AI Confidence: **99.31%**
3187. **`usr/src/cmd/hal/hald/util_helper.c`** -> AI Confidence: **99.31%**
3188. **`usr/src/cmd/hal/hald/util_pm.c`** -> AI Confidence: **99.31%**
3189. **`usr/src/cmd/hal/probing/network-printer/probe-snmp.c`** -> AI Confidence: **99.31%**
3190. **`usr/src/cmd/hal/tools/hal-storage-shared.c`** -> AI Confidence: **99.31%**
3191. **`usr/src/cmd/hal/tools/sunos/hal-system-lcd-set-brightness-sunos.c`** -> AI Confidence: **99.31%**
3192. **`usr/src/cmd/hal/utils/adt_data.c`** -> AI Confidence: **99.31%**
3193. **`usr/src/cmd/hal/utils/cdutils.c`** -> AI Confidence: **99.31%**
3194. **`usr/src/cmd/hal/utils/fsutils.c`** -> AI Confidence: **99.31%**
3195. **`usr/src/cmd/halt/halt.c`** -> AI Confidence: **99.31%**
3196. **`usr/src/cmd/hostname/hostname.c`** -> AI Confidence: **99.31%**
3197. **`usr/src/cmd/hotplug/hotplug.c`** -> AI Confidence: **99.31%**
3198. **`usr/src/cmd/hotplugd/hotplugd_door.c`** -> AI Confidence: **99.31%**
3199. **`usr/src/cmd/hotplugd/hotplugd_impl.c`** -> AI Confidence: **99.31%**
3200. **`usr/src/cmd/hotplugd/hotplugd_info.c`** -> AI Confidence: **99.31%**
3201. **`usr/src/cmd/i2cadm/i2cadm_controller.c`** -> AI Confidence: **99.31%**
3202. **`usr/src/cmd/i2cadm/i2cadm_device.c`** -> AI Confidence: **99.31%**
3203. **`usr/src/cmd/i2cadm/i2cadm_port.c`** -> AI Confidence: **99.31%**
3204. **`usr/src/cmd/i2cadm/i2cadm_scan.c`** -> AI Confidence: **99.31%**
3205. **`usr/src/cmd/iconv/charmap.c`** -> AI Confidence: **99.31%**
3206. **`usr/src/cmd/iconv/scanner.c`** -> AI Confidence: **99.31%**
3207. **`usr/src/cmd/id/id.c`** -> AI Confidence: **99.31%**
3208. **`usr/src/cmd/idmap/idmap/idmap.c`** -> AI Confidence: **99.31%**
3209. **`usr/src/cmd/idmap/idmapd/adspriv_impl.c`** -> AI Confidence: **99.31%**
3210. **`usr/src/cmd/idmap/idmapd/adutils.c`** -> AI Confidence: **99.31%**
3211. **`usr/src/cmd/idmap/idmapd/directory_provider_ad.c`** -> AI Confidence: **99.31%**
3212. **`usr/src/cmd/idmap/idmapd/directory_provider_builtin.c`** -> AI Confidence: **99.31%**
3213. **`usr/src/cmd/idmap/idmapd/directory_server.c`** -> AI Confidence: **99.31%**
3214. **`usr/src/cmd/idmap/idmapd/krb5_lookup.c`** -> AI Confidence: **99.31%**
3215. **`usr/src/cmd/init/init.c`** -> AI Confidence: **99.31%**
3216. **`usr/src/cmd/ipcrm/ipcrm.c`** -> AI Confidence: **99.31%**
3217. **`usr/src/cmd/ipf/lib/facpri.c`** -> AI Confidence: **99.31%**
3218. **`usr/src/cmd/ipf/tools/ipfstat.c`** -> AI Confidence: **99.31%**
3219. **`usr/src/cmd/ipf/tools/ipfzone.c`** -> AI Confidence: **99.31%**
3220. **`usr/src/cmd/isainfo/isainfo.c`** -> AI Confidence: **99.31%**
3221. **`usr/src/cmd/iscsiadm/cmdparse.c`** -> AI Confidence: **99.31%**
3222. **`usr/src/cmd/iscsiadm/iscsiadm_main.c`** -> AI Confidence: **99.31%**
3223. **`usr/src/cmd/isns/isnsadm/cmdparse.c`** -> AI Confidence: **99.31%**
3224. **`usr/src/cmd/isns/isnsadm/isnsadm.c`** -> AI Confidence: **99.31%**
3225. **`usr/src/cmd/isns/isnsd/admintf.c`** -> AI Confidence: **99.31%**
3226. **`usr/src/cmd/isns/isnsd/cache.c`** -> AI Confidence: **99.31%**
3227. **`usr/src/cmd/isns/isnsd/dsapi.c`** -> AI Confidence: **99.31%**
3228. **`usr/src/cmd/isns/isnsd/esi.c`** -> AI Confidence: **99.31%**
3229. **`usr/src/cmd/isns/isnsd/main.c`** -> AI Confidence: **99.31%**
3230. **`usr/src/cmd/isns/isnsd/obj.c`** -> AI Confidence: **99.31%**
3231. **`usr/src/cmd/isns/isnsd/pdu.c`** -> AI Confidence: **99.31%**
3232. **`usr/src/cmd/isns/isnsd/scn.c`** -> AI Confidence: **99.31%**
3233. **`usr/src/cmd/isns/isnsd/server.c`** -> AI Confidence: **99.31%**
3234. **`usr/src/cmd/itadm/itadm.c`** -> AI Confidence: **99.31%**
3235. **`usr/src/cmd/keyserv/chkey_common.c`** -> AI Confidence: **99.31%**
3236. **`usr/src/cmd/keyserv/key_generic.c`** -> AI Confidence: **99.31%**
3237. **`usr/src/cmd/keyserv/keyserv.c`** -> AI Confidence: **99.31%**
3238. **`usr/src/cmd/keyserv/keyserv_cache.c`** -> AI Confidence: **99.31%**
3239. **`usr/src/cmd/keyserv/newkey.c`** -> AI Confidence: **99.31%**
3240. **`usr/src/cmd/keyserv/update.c`** -> AI Confidence: **99.31%**
3241. **`usr/src/cmd/krb5/kadmin/cli/ss_wrapper.c`** -> AI Confidence: **99.31%**
3242. **`usr/src/cmd/krb5/kadmin/dbutil/kdb5_util.c`** -> AI Confidence: **99.31%**
3243. **`usr/src/cmd/krb5/kproplog/kproplog.c`** -> AI Confidence: **99.31%**
3244. **`usr/src/cmd/krb5/krb5kdc/kdc_preauth.c`** -> AI Confidence: **99.31%**
3245. **`usr/src/cmd/krb5/krb5kdc/network.c`** -> AI Confidence: **99.31%**
3246. **`usr/src/cmd/krb5/kwarn/kwarnd.c`** -> AI Confidence: **99.31%**
3247. **`usr/src/cmd/krb5/kwarn/kwarnd_clnt_stubs.c`** -> AI Confidence: **99.31%**
3248. **`usr/src/cmd/krb5/kwarn/kwarnd_generic.c`** -> AI Confidence: **99.31%**
3249. **`usr/src/cmd/krb5/kwarn/kwarnd_handle.c`** -> AI Confidence: **99.31%**
3250. **`usr/src/cmd/last/last.c`** -> AI Confidence: **99.31%**
3251. **`usr/src/cmd/latencytop/display.c`** -> AI Confidence: **99.31%**
3252. **`usr/src/cmd/latencytop/dwrapper.c`** -> AI Confidence: **99.31%**
3253. **`usr/src/cmd/latencytop/latencytop.c`** -> AI Confidence: **99.31%**
3254. **`usr/src/cmd/latencytop/stat.c`** -> AI Confidence: **99.31%**
3255. **`usr/src/cmd/ldap/common/common.c`** -> AI Confidence: **99.31%**
3256. **`usr/src/cmd/ldap/common/convutf8.c`** -> AI Confidence: **99.31%**
3257. **`usr/src/cmd/ldap/ns_ldap/ldapaddent.c`** -> AI Confidence: **99.31%**
3258. **`usr/src/cmd/ldap/ns_ldap/ldapaddrbac.c`** -> AI Confidence: **99.31%**
3259. **`usr/src/cmd/ldap/ns_ldap/ldapaddtsol.c`** -> AI Confidence: **99.31%**
3260. **`usr/src/cmd/ldap/ns_ldap/ldapclient.c`** -> AI Confidence: **99.31%**
3261. **`usr/src/cmd/ldapcachemgr/cachemgr.c`** -> AI Confidence: **99.31%**
3262. **`usr/src/cmd/ldapcachemgr/cachemgr_change.c`** -> AI Confidence: **99.31%**
3263. **`usr/src/cmd/ldapcachemgr/cachemgr_discovery.c`** -> AI Confidence: **99.31%**
3264. **`usr/src/cmd/ldapcachemgr/cachemgr_getldap.c`** -> AI Confidence: **99.31%**
3265. **`usr/src/cmd/ldapcachemgr/cachemgr_parse.c`** -> AI Confidence: **99.31%**
3266. **`usr/src/cmd/ldmad/ldma_dio.c`** -> AI Confidence: **99.31%**
3267. **`usr/src/cmd/ldmad/ldmad.c`** -> AI Confidence: **99.31%**
3268. **`usr/src/cmd/ldmad/mdesc_lib.c`** -> AI Confidence: **99.31%**
3269. **`usr/src/cmd/listen/listen.c`** -> AI Confidence: **99.31%**
3270. **`usr/src/cmd/listen/nlps_serv.c`** -> AI Confidence: **99.31%**
3271. **`usr/src/cmd/loadkeys/dumpkeys.c`** -> AI Confidence: **99.31%**
3272. **`usr/src/cmd/locale/locale.c`** -> AI Confidence: **99.31%**
3273. **`usr/src/cmd/localedef/charmap.c`** -> AI Confidence: **99.31%**
3274. **`usr/src/cmd/localedef/collate.c`** -> AI Confidence: **99.31%**
3275. **`usr/src/cmd/localedef/localedef.c`** -> AI Confidence: **99.31%**
3276. **`usr/src/cmd/localedef/numeric.c`** -> AI Confidence: **99.31%**
3277. **`usr/src/cmd/localedef/scanner.c`** -> AI Confidence: **99.31%**
3278. **`usr/src/cmd/locator/locator.c`** -> AI Confidence: **99.31%**
3279. **`usr/src/cmd/lockstat/lockstat.c`** -> AI Confidence: **99.31%**
3280. **`usr/src/cmd/lockstat/sym.c`** -> AI Confidence: **99.31%**
3281. **`usr/src/cmd/logadm/conf.c`** -> AI Confidence: **99.31%**
3282. **`usr/src/cmd/logadm/err.c`** -> AI Confidence: **99.31%**
3283. **`usr/src/cmd/logadm/glob.c`** -> AI Confidence: **99.31%**
3284. **`usr/src/cmd/logadm/main.c`** -> AI Confidence: **99.31%**
3285. **`usr/src/cmd/logger/logger.c`** -> AI Confidence: **99.31%**
3286. **`usr/src/cmd/login/login.c`** -> AI Confidence: **99.31%**
3287. **`usr/src/cmd/login/login_audit.c`** -> AI Confidence: **99.31%**
3288. **`usr/src/cmd/logins/logins.c`** -> AI Confidence: **99.31%**
3289. **`usr/src/cmd/lp/cmd/lpadmin/default.c`** -> AI Confidence: **99.31%**
3290. **`usr/src/cmd/lp/cmd/lpadmin/pick_opts.c`** -> AI Confidence: **99.31%**
3291. **`usr/src/cmd/lp/cmd/lpsched/lpsched.c`** -> AI Confidence: **99.31%**
3292. **`usr/src/cmd/lp/cmd/lpshut.c`** -> AI Confidence: **99.31%**
3293. **`usr/src/cmd/lp/filter/postscript/download/download.c`** -> AI Confidence: **99.31%**
3294. **`usr/src/cmd/lp/filter/postscript/postio/parallel.c`** -> AI Confidence: **99.31%**
3295. **`usr/src/cmd/lp/filter/postscript/postio/postio.c`** -> AI Confidence: **99.31%**
3296. **`usr/src/cmd/lp/filter/postscript/postreverse/postreverse.c`** -> AI Confidence: **99.31%**
3297. **`usr/src/cmd/lp/lib/access/allowed.c`** -> AI Confidence: **99.31%**
3298. **`usr/src/cmd/lp/lib/class/getclass.c`** -> AI Confidence: **99.31%**
3299. **`usr/src/cmd/lp/lib/filters/loadfilters.c`** -> AI Confidence: **99.31%**
3300. **`usr/src/cmd/lp/lib/forms/putform.c`** -> AI Confidence: **99.31%**
3301. **`usr/src/cmd/lp/lib/forms/rdform.c`** -> AI Confidence: **99.31%**
3302. **`usr/src/cmd/lp/lib/lp/Sys_malloc.c`** -> AI Confidence: **99.31%**
3303. **`usr/src/cmd/lp/lib/lp/files.c`** -> AI Confidence: **99.31%**
3304. **`usr/src/cmd/lp/lib/msgs/mconnect.c`** -> AI Confidence: **99.31%**
3305. **`usr/src/cmd/lp/lib/msgs/mcreate.c`** -> AI Confidence: **99.31%**
3306. **`usr/src/cmd/lp/lib/msgs/mdestroy.c`** -> AI Confidence: **99.31%**
3307. **`usr/src/cmd/lp/lib/msgs/mlisten.c`** -> AI Confidence: **99.31%**
3308. **`usr/src/cmd/lp/lib/oam/fmtmsg.c`** -> AI Confidence: **99.31%**
3309. **`usr/src/cmd/lp/lib/papi/job.c`** -> AI Confidence: **99.31%**
3310. **`usr/src/cmd/lp/model/netpr/misc.c`** -> AI Confidence: **99.31%**
3311. **`usr/src/cmd/lp/model/netpr/net.c`** -> AI Confidence: **99.31%**
3312. **`usr/src/cmd/lp/model/netpr/netpr.c`** -> AI Confidence: **99.31%**
3313. **`usr/src/cmd/lp/model/netpr/tcp_misc.c`** -> AI Confidence: **99.31%**
3314. **`usr/src/cmd/luxadm/diag.c`** -> AI Confidence: **99.31%**
3315. **`usr/src/cmd/luxadm/errormsgs.c`** -> AI Confidence: **99.31%**
3316. **`usr/src/cmd/luxadm/fabric_conf.c`** -> AI Confidence: **99.31%**
3317. **`usr/src/cmd/luxadm/g_adm.c`** -> AI Confidence: **99.31%**
3318. **`usr/src/cmd/luxadm/hotplug.c`** -> AI Confidence: **99.31%**
3319. **`usr/src/cmd/luxadm/lux_util.c`** -> AI Confidence: **99.31%**
3320. **`usr/src/cmd/luxadm/qlgcupdate.c`** -> AI Confidence: **99.31%**
3321. **`usr/src/cmd/luxadm/setboot.c`** -> AI Confidence: **99.31%**
3322. **`usr/src/cmd/luxadm/x86_adm.c`** -> AI Confidence: **99.31%**
3323. **`usr/src/cmd/man/makewhatis.c`** -> AI Confidence: **99.31%**
3324. **`usr/src/cmd/man/man.c`** -> AI Confidence: **99.31%**
3325. **`usr/src/cmd/mandoc/compat_ohash.c`** -> AI Confidence: **99.31%**
3326. **`usr/src/cmd/mandoc/dba_read.c`** -> AI Confidence: **99.31%**
3327. **`usr/src/cmd/mandoc/dba_write.c`** -> AI Confidence: **99.31%**
3328. **`usr/src/cmd/mandoc/dbm.c`** -> AI Confidence: **99.31%**
3329. **`usr/src/cmd/mandoc/dbm_map.c`** -> AI Confidence: **99.31%**
3330. **`usr/src/cmd/mandoc/man_html.c`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `usr/src/cmd/cmd-crypto/pktool/genkey.c` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `361` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `161232` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `usr/src/cmd/fm/fmd/common/fmd_fmri.c` (C) -> Cumulative Risk: **783.35**
- **Archetype:** `file_cluster_4` (Distance: 13.331 IQR)
- **Magnitude:** 431.2 | **LOC:** 449 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9657%)
- **Heaviest Functions:** `fmd_fmri_uriescape` (Impact: 37.9), `fmd_fmri_auth2str` (Impact: 9.8), `fmd_fmri_nvl2str` (Impact: 6.2)

### 2. `usr/src/cmd/fm/fmd/common/fmd_idspace.c` (C) -> Cumulative Risk: **775.78**
- **Archetype:** `file_cluster_4` (Distance: 12.805 IQR)
- **Magnitude:** 302.14 | **LOC:** 343 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9999%)
- **Heaviest Functions:** `fmd_idspace_create` (Impact: 7.6), `fmd_idspace_free` (Impact: 7.5), `fmd_idspace_xalloc_locked` (Impact: 6.3)

### 3. `usr/src/lib/libsip/common/sip_dialog_ui.c` (C) -> Cumulative Risk: **773.84**
- **Archetype:** `file_cluster_4` (Distance: 12.963 IQR)
- **Magnitude:** 591.5 | **LOC:** 613 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9897%)
- **Heaviest Functions:** `sip_create_dialog_req` (Impact: 32.5), `sip_get_dialog_remote_tag` (Impact: 8.5), `sip_get_dialog_local_tag` (Impact: 8.4)

### 4. `usr/src/cmd/fm/fmd/common/fmd_event.c` (C) -> Cumulative Risk: **768.67**
- **Archetype:** `file_cluster_4` (Distance: 12.849 IQR)
- **Magnitude:** 259.14 | **LOC:** 365 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (98.3489%), Concurrency (98.1836%)
- **Heaviest Functions:** `fmd_event_destroy` (Impact: 18.2), `fmd_event_create` (Impact: 9.1), `fmd_event_nvunwrap` (Impact: 8.0)

### 5. `usr/src/lib/pkcs11/pkcs11_softtoken/common/softVerify.c` (C) -> Cumulative Risk: **758.66**
- **Archetype:** `file_cluster_4` (Distance: 12.415 IQR)
- **Magnitude:** 282.24 | **LOC:** 383 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `C_VerifyInit` (Impact: 14.2), `C_VerifyRecoverInit` (Impact: 14.2), `C_VerifyRecover` (Impact: 12.4)

### 6. `usr/src/lib/pkcs11/pkcs11_softtoken/common/softSign.c` (C) -> Cumulative Risk: **752.75**
- **Archetype:** `file_cluster_4` (Distance: 12.467 IQR)
- **Magnitude:** 305.56 | **LOC:** 415 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `C_Sign` (Impact: 14.8), `C_SignInit` (Impact: 14.2), `C_SignRecoverInit` (Impact: 14.2)

### 7. `usr/src/lib/libsip/common/sip_ui.c` (C) -> Cumulative Risk: **743.8**
- **Archetype:** `file_cluster_4` (Distance: 13.763 IQR)
- **Magnitude:** 1587.4 | **LOC:** 1350 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.5592%), Documentation (99.0337%)
- **Heaviest Functions:** `sip_get_resp_desc` (Impact: 100.9), `sip_register_sent_by` (Impact: 31.1), `sip_get_header_value` (Impact: 30.2)

### 8. `usr/src/lib/pkcs11/pkcs11_kernel/common/kernelSession.c` (C) -> Cumulative Risk: **742.76**
- **Archetype:** `file_cluster_4` (Distance: 12.468 IQR)
- **Magnitude:** 315.74 | **LOC:** 594 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.8073%), Cognitive Load (99.5709%)
- **Heaviest Functions:** `C_Login` (Impact: 27.5), `C_Logout` (Impact: 15.8), `kernel_set_operationstate` (Impact: 9.3)

### 9. `usr/src/lib/scsi/libsmp/common/smp_engine.c` (C) -> Cumulative Risk: **742.11**
- **Archetype:** `file_cluster_13` (Distance: 13.531 IQR)
- **Magnitude:** 575.52 | **LOC:** 736 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.352%), Tech Debt (96.7334%)
- **Heaviest Functions:** `smp_engine_hold` (Impact: 35.0), `smp_action_xalloc` (Impact: 24.9), `smp_engine_loadone` (Impact: 11.6)

### 10. `usr/src/lib/libuutil/common/uu_avl.c` (C) -> Cumulative Risk: **741.04**
- **Archetype:** `file_cluster_4` (Distance: 13.023 IQR)
- **Magnitude:** 481.66 | **LOC:** 569 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.9146%), Documentation (95.3696%)
- **Heaviest Functions:** `uu_avl_pool_create` (Impact: 21.9), `uu_avl_node_fini` (Impact: 13.1), `uu_avl_node_init` (Impact: 9.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `usr/src/head/unistd.h` (C | Tier 0 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.387 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.691 IQR)
- **Top Global Matches:** file_cluster_8: 10.387, file_cluster_7: 11.123, file_cluster_9: 11.206
- **Magnitude:** 25366.77 | **LOC:** 723 | **CtrlFlow:** 79.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (16.6944%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 56`, `args: 136`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 3`
* *Architecture:* `io: 5`, `api: 156`, `import: 4`
* *Defense:* `safety: 19`, `immutability_locks: 71`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types.h, null.h, unistd.h, feature_tests.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/cmd/vi/misc/ctags.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.996 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.443 IQR)
- **Top Global Matches:** file_cluster_8: 13.996, file_cluster_0: 14.127, file_cluster_11: 14.18
- **Magnitude:** 20350.08 | **LOC:** 1448 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.3855%), Tech Debt (9.511%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 122`, `args: 39`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 2`, `state_mutation: 715`, `dead_code: 5`, `fragile_debt: 1`
* *Architecture:* `io: 15`, `api: 51`
* *Defense:* `safety: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unistd.h, ctype.h, types.h, stdlib.h, strings.h, string.h, stdio.h, stat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/cmd/cpio/cpio.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.626 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.85 IQR)
- **Top Global Matches:** file_cluster_8: 14.626, file_cluster_13: 14.719, file_cluster_11: 14.828
- **Magnitude:** 16089.54 | **LOC:** 9761 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.3067%), Tech Debt (11.2964%)
**Top Internal Functions/Classes:**
  * `data_copy_with_holes` (Impact: 2285.5)
  * `rdwr_bytes` (Impact: 2268.7)
    * *Intent:* /*
  * `read_compress_holes` (Impact: 2008.9)
  * `read_holesdata` (Impact: 1864.4)
  * `creat_spec` (Impact: 1386.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1332`, `structural_boundaries: 370`, `args: 122`, `func_start: 55`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 2635`, `dead_code: 4`, `fragile_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `io: 89`, `api: 271`, `import: 36`
* *Defense:* `safety: 28`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` param.h, grp.h, memory.h, ctype.h, fcntl.h, statvfs.h, mkdev.h, stdarg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/sata/impl/sata.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.945 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.915 IQR)
- **Top Global Matches:** file_cluster_8: 14.945, file_cluster_13: 15.192, file_cluster_11: 15.221
- **Magnitude:** 13571.56 | **LOC:** 21963 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.2954%), Tech Debt (9.2995%)
**Top Internal Functions/Classes:**
  * `sata_scsi_tgt_init` (Impact: 1006.6)
    * *Intent:* /* * The sata cfgadm pluging will invoke this operation only if
  * `sata_scsi_start` (Impact: 881.9)
    * *Intent:* } /* End of DEVCTL_AP_CONTROL cmd switch */
  * `sata_alloc_pmult` (Impact: 712.5)
  * `sata_identify_device` (Impact: 651.3)
  * `sata_get_atapi_inquiry_data` (Impact: 633.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1945`, `structural_boundaries: 826`, `args: 34`, `func_start: 126`, `class_start: 106`
* *Risk/State:* `safety_bypasses: 97`, `state_mutation: 6153`, `dead_code: 7`, `planned_debt: 3`, `orphaned_logic: 11`
* *Architecture:* `io: 18`, `api: 968`, `import: 27`
* *Defense:* `safety: 17`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.h, sata.h, ddifm.h, sata_satl.h, taskq.h, protocol.h, sysevent.h, sdt.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/vm/seg_vn.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.743 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.807 IQR)
- **Top Global Matches:** file_cluster_8: 14.743, file_cluster_13: 14.865, file_cluster_11: 14.958
- **Magnitude:** 11533.14 | **LOC:** 10343 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (19.9362%)
**Top Internal Functions/Classes:**
  * `segvn_faultpage` (Impact: 2205.0)
  * `segvn_full_szcpages` (Impact: 1988.5)
  * `segvn_softunlock` (Impact: 1479.6)
    * *Intent:* /* * We don't need any segment level locks for "segvn" data * since the address space is "write" loc...
  * `segvn_free` (Impact: 1313.5)
  * `segvn_advise` (Impact: 396.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1058`, `structural_boundaries: 396`, `args: 63`, `func_start: 27`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 2347`, `planned_debt: 1`, `fragile_debt: 15`, `orphaned_logic: 3`
* *Architecture:* `api: 442`, `import: 33`
* *Defense:* `safety: 65`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` param.h, vmsystm.h, dumphdr.h, systm.h, sysmacros.h, vm.h, proc.h, mman.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/cmd/dladm/dladm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.479 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.478 IQR)
- **Top Global Matches:** file_cluster_8: 14.479, file_cluster_13: 14.695, file_cluster_0: 14.759
- **Magnitude:** 10440.8 | **LOC:** 10617 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (75.72%), Tech Debt (7.7396%)
**Top Internal Functions/Classes:**
  * `create_modify_add_bridge` (Impact: 212.4)
  * `do_show_bridge` (Impact: 201.3)
  * `do_create_vnic` (Impact: 171.3)
  * `do_show_aggr` (Impact: 152.6)
  * `do_create_aggr` (Impact: 127.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2364`, `structural_boundaries: 955`, `args: 137`, `func_start: 194`, `class_start: 63`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 2`, `state_mutation: 3966`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `io: 57`, `api: 1434`, `import: 54`
* *Defense:* `safety: 175`, `immutability_locks: 210`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` ctype.h, libdlpi.h, libdllink.h, processor.h, fcntl.h, stdarg.h, priv.h, strings.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/fibre-channel/fca/qlc/ql_api.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.923 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.821 IQR)
- **Top Global Matches:** file_cluster_8: 14.923, file_cluster_13: 15.21, file_cluster_11: 15.222
- **Magnitude:** 10348.86 | **LOC:** 22988 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.5028%), Tech Debt (9.1541%)
**Top Internal Functions/Classes:**
  * `ql_erase_flash` (Impact: 569.7)
    * *Intent:* /* * issue an echo command with a user supplied
  * `ql_setup_msix` (Impact: 533.5)
  * `ql_83xx_ascii_fw_dump` (Impact: 307.9)
  * `ql_attach` (Impact: 261.6)
    * *Intent:* /* * _fini * Prepares a module for unloading. It is called when the system * wants to unload a modul...
  * `ql_getmap` (Impact: 90.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1523`, `structural_boundaries: 780`, `args: 13`, `func_start: 115`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 104`, `high_risk_execution: 1`, `state_mutation: 6468`, `dead_code: 4`, `fragile_debt: 2`, `orphaned_logic: 8`
* *Architecture:* `io: 20`, `api: 518`, `import: 11`
* *Defense:* `safety: 172`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` ql_init.h, ql_xioctl.h, ql_ioctl.h, ql_debug.h, ql_isr.h, ql_iocb.h, ql_mbx.h, ql_nx.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/cmd/krb5/kinit/kinit.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.21 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.913 IQR)
- **Top Global Matches:** file_cluster_8: 13.21, file_cluster_13: 13.439, file_cluster_11: 13.642
- **Magnitude:** 10298.12 | **LOC:** 1397 | **CtrlFlow:** 80.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.4789%), Tech Debt (8.9482%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 79`, `args: 7`, `func_start: 18`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 561`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 165`, `import: 16`
* *Defense:* `safety: 2`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` unistd.h, com_err.h, libintl.h, netdb.h, k5-int.h, prof_int.h, errno.h, pwd.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/lib/libzonecfg/common/libzonecfg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.498 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.218 IQR)
- **Top Global Matches:** file_cluster_8: 14.498, file_cluster_13: 14.514, file_cluster_11: 14.596
- **Magnitude:** 10210.6 | **LOC:** 8396 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (74.8911%)
**Top Internal Functions/Classes:**
  * `zonecfg_ifname_exists` (Impact: 1163.8)
  * `zonecfg_lookup_dev` (Impact: 1143.8)
  * `zonecfg_destroy_tmp_pool` (Impact: 1048.7)
  * `zonecfg_delete_rctl_core` (Impact: 977.1)
  * `zonecfg_warn_poold` (Impact: 287.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1061`, `structural_boundaries: 937`, `args: 73`, `func_start: 176`, `class_start: 53`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 5`, `state_mutation: 2300`, `dead_code: 5`, `planned_debt: 1`, `orphaned_logic: 99`
* *Architecture:* `io: 35`, `api: 699`, `concurrency: 6`, `import: 45`
* *Defense:* `safety: 70`, `test: 20`, `sync_locks: 1`, `immutability_locks: 122`, `cleanup: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` ctype.h, acl.h, prof_attr.h, uuid.h, strings.h, sockio.h, libbrand.h, pthread.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/stand/lib/tcp/tcp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.692 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.664 IQR)
- **Top Global Matches:** file_cluster_8: 14.692, file_cluster_13: 14.803, file_cluster_11: 14.899
- **Magnitude:** 10116.76 | **LOC:** 7097 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (20.6657%)
**Top Internal Functions/Classes:**
  * `tcp_send` (Impact: 1314.8)
    * *Intent:* /* * The format argument to pass to tcp_display(). * DISP_PORT_ONLY means that the returned string h...
  * `tcp_state_wait` (Impact: 1165.4)
  * `tcp_parse_options` (Impact: 1120.7)
  * `tcp_eager_unlink` (Impact: 1046.8)
  * `tcp_bind` (Impact: 976.1)
    * *Intent:* /* * The receive entry point for upper layer to call to get data. Note * that this follows the curre...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 656`, `structural_boundaries: 164`, `args: 12`, `func_start: 32`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 1933`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 5`, `orphaned_logic: 10`
* *Architecture:* `io: 3`, `api: 227`, `import: 22`
* *Defense:* `safety: 50`, `test: 48`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ipv4.h, bootdebug.h, promif.h, mib2.h, if_types.h, sysmacros.h, socket_inet.h, tcp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/scsi/impl/scsi_hba.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.165 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.179 IQR)
- **Top Global Matches:** file_cluster_8: 14.165, file_cluster_11: 14.351, file_cluster_0: 14.361
- **Magnitude:** 9999.88 | **LOC:** 10528 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (59.534%)
**Top Internal Functions/Classes:**
  * `scsi_busctl_initchild` (Impact: 1318.2)
    * *Intent:* /* * If an HBA is *not* doing its own fma support by calling * ddi_fm_init() prior to scsi_hba_attac...
  * `iport_preattach_tran_smp_device` (Impact: 1306.8)
    * *Intent:* /* * The 'scsi-binding-set' property can be defined in driver.conf * files of legacy drivers on an a...
  * `scsi_hba_bus_ctl` (Impact: 1235.5)
  * `scsi_initialize_hba_interface` (Impact: 1178.9)
    * *Intent:* nodev, /* strategy */ nodev, /* print */ nodev, /* dump */ nodev, /* read */ nodev, /* write */ scsi...
  * `scsi_hba_ident_nodename_compatible_get` (Impact: 315.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1049`, `structural_boundaries: 490`, `args: 56`, `func_start: 127`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 76`, `high_risk_execution: 2`, `state_mutation: 2000`, `dead_code: 10`, `planned_debt: 5`, `fragile_debt: 3`, `orphaned_logic: 68`
* *Architecture:* `io: 3`, `api: 676`
* *Defense:* `safety: 35`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` time.h, mdi_impldefs.h, file.h, protocol.h, sunndi.h, sas.h, damap.h, ddi.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/scsi/adapters/mpt_sas/mptsas.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.475 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.798 IQR)
- **Top Global Matches:** file_cluster_8: 14.475, file_cluster_7: 14.791, file_cluster_11: 14.856
- **Magnitude:** 9841.54 | **LOC:** 17103 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.1877%), Tech Debt (9.2083%)
**Top Internal Functions/Classes:**
  * `mptsas_handle_event` (Impact: 359.4)
    * *Intent:* /*
  * `mptsas_handle_dr` (Impact: 353.3)
  * `mptsas_attach` (Impact: 159.0)
    * *Intent:* #else
  * `mptsas_handle_topo_change` (Impact: 143.6)
  * `mptsas_create_phys_lun` (Impact: 113.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2130`, `structural_boundaries: 769`, `args: 35`, `func_start: 192`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 167`, `high_risk_execution: 3`, `state_mutation: 5019`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 2`, `orphaned_logic: 9`
* *Architecture:* `io: 37`, `api: 1129`
* *Defense:* `safety: 14`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mpi2_raid.h, mptsas_var.h, util.h, sas.h, ddifm.h, scsi_reset_notify.h, mpi2_cnfg.h, raidioctl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/fibre-channel/fca/emlxs/emlxs_solaris.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.549 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.306 IQR)
- **Top Global Matches:** file_cluster_8: 14.549, file_cluster_13: 14.862, file_cluster_7: 14.863
- **Magnitude:** 9220.86 | **LOC:** 12434 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (98.1374%), Tech Debt (14.0332%)
**Top Internal Functions/Classes:**
  * `emlxs_pkt_complete` (Impact: 928.8)
  * `emlxs_fca_port_manage` (Impact: 891.4)
  * `emlxs_send_els` (Impact: 891.0)
  * `emlxs_fca_pkt_abort` (Impact: 871.8)
  * `emlxs_fca_bind_port` (Impact: 203.5)
    * *Intent:* emlxs_open, /* cb_open */ emlxs_close, /* cb_close */ nodev, /* cb_strategy */ nodev, /* cb_print */...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1092`, `structural_boundaries: 407`, `args: 10`, `func_start: 83`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 3593`, `dead_code: 1`, `orphaned_logic: 33`
* *Architecture:* `api: 600`, `import: 2`
* *Defense:* `safety: 44`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` modctl.h, emlxs.h, emlxs_version.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/dtrace/dtrace.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.572 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.247 IQR)
- **Top Global Matches:** file_cluster_8: 14.572, file_cluster_13: 14.687, file_cluster_11: 14.763
- **Magnitude:** 8907.72 | **LOC:** 17435 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (8.021%)
**Top Internal Functions/Classes:**
  * `dtrace_match_priv` (Impact: 1261.7)
  * `dtrace_difo_chunksize` (Impact: 1046.7)
  * `dtrace_enabling_match` (Impact: 930.1)
  * `dtrace_enabling_provide` (Impact: 926.0)
  * `dtrace_match_glob` (Impact: 260.5)
    * *Intent:* hrtime_t dtrace_chill_max = MSEC2NSEC(500); /* 500 ms */ hrtime_t dtrace_chill_interval = NANOSEC; /...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 977`, `structural_boundaries: 326`, `args: 9`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 2389`, `planned_debt: 3`
* *Architecture:* `io: 19`, `api: 556`, `import: 29`
* *Defense:* `safety: 20`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mkdev.h, taskq.h, kdi.h, mutex_impl.h, systm.h, cpuvar.h, sysmacros.h, strsubr.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/scsi/targets/st.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.454 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.928 IQR)
- **Top Global Matches:** file_cluster_8: 14.454, file_cluster_7: 14.766, file_cluster_13: 14.769
- **Magnitude:** 8820.94 | **LOC:** 18596 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.1865%), Tech Debt (14.9127%)
**Top Internal Functions/Classes:**
  * `st_get_conf_from_st_dot_conf` (Impact: 1028.9)
  * `st_check_error` (Impact: 706.0)
  * `st_print_cdb` (Impact: 445.9)
  * `st_decode_sense` (Impact: 311.8)
  * `st_backward_space_files` (Impact: 151.7)
    * *Intent:* /* * Limit the maximum length of the result to * sizeof (struct mtdrivetype). */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1326`, `structural_boundaries: 663`, `args: 180`, `func_start: 85`, `class_start: 93`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 3702`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 16`, `orphaned_logic: 3`
* *Architecture:* `io: 25`, `api: 483`, `import: 10`
* *Defense:* `safety: 13`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mtio.h, file.h, kstat.h, ddi.h, scsi.h, sunddi.h, modctl.h, ddidmareq.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/cmd/devfsadm/devfsadm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.323 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.716 IQR)
- **Top Global Matches:** file_cluster_8: 14.323, file_cluster_11: 14.485, file_cluster_13: 14.487
- **Magnitude:** 8785.94 | **LOC:** 8788 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.2895%), Tech Debt (12.2893%)
**Top Internal Functions/Classes:**
  * `devfsadm_read_link` (Impact: 1457.3)
  * `rm_link_from_cache` (Impact: 1059.9)
    * *Intent:* /* * look for relevant link create rules in the modules, and * invoke the link create callback funct...
  * `process_devlink_compat` (Impact: 999.3)
    * *Intent:* /* * This function and all the functions it calls below were added to
  * `translate_major` (Impact: 219.7)
    * *Intent:* /* * If there is redirection, new phys path * and old phys path will not match and the
  * `alloc_cmp_str` (Impact: 202.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 983`, `structural_boundaries: 422`, `args: 77`, `func_start: 96`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 40`, `high_risk_execution: 1`, `state_mutation: 2512`, `dead_code: 4`, `orphaned_logic: 19`
* *Architecture:* `io: 66`, `api: 410`, `import: 10`
* *Defense:* `safety: 49`, `test: 24`, `immutability_locks: 17`, `cleanup: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` param.h, deflt.h, libbsm.h, label.h, devfsadm_impl.h, devalloc.h, zone.h, devices.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/fibre-channel/fca/emlxs/emlxs_dfc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.656 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.372 IQR)
- **Top Global Matches:** file_cluster_8: 14.656, file_cluster_11: 14.942, file_cluster_7: 14.957
- **Magnitude:** 8760.02 | **LOC:** 11112 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (85.3344%), Tech Debt (8.3795%)
**Top Internal Functions/Classes:**
  * `emlxs_dfc_destroy_vport` (Impact: 441.1)
  * `emlxs_dfc_loopback_mode` (Impact: 130.7)
  * `emlxs_fcio_get_port_attrs` (Impact: 119.7)
  * `emlxs_fcio_get_disc_port_attrs` (Impact: 115.0)
  * `emlxs_fcio_get_adapter_port_attrs` (Impact: 96.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1548`, `structural_boundaries: 449`, `args: 1`, `func_start: 98`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 239`, `state_mutation: 5201`, `planned_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `io: 7`, `api: 906`, `import: 1`
* *Defense:* `safety: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` emlxs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/fibre-channel/ulp/fcp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.482 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.932 IQR)
- **Top Global Matches:** file_cluster_8: 14.482, file_cluster_13: 14.75, file_cluster_7: 14.799
- **Magnitude:** 8582.36 | **LOC:** 16357 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.3635%), Tech Debt (18.5151%)
**Top Internal Functions/Classes:**
  * `fcp_trigger_lun` (Impact: 1260.4)
  * `fcp_alloc_tgt` (Impact: 881.9)
    * *Intent:* /* * Function: fcp_port_attach * * Description: Called by the transport framework to resume, suspend...
  * `fcp_check_reportlun` (Impact: 806.7)
  * `fcp_setup_device_data_ioctl` (Impact: 170.7)
    * *Intent:* * STEP 5: The watchdog timer expires. The watch dog timer does much more that * what is described he...
  * `fcp_offline_child` (Impact: 137.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1117`, `structural_boundaries: 603`, `args: 66`, `func_start: 77`, `class_start: 139`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 2901`, `fragile_debt: 4`, `orphaned_logic: 26`
* *Architecture:* `io: 4`, `api: 519`, `import: 22`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` devctl.h, utsname.h, scsi_reset_notify.h, ndi_impldefs.h, proc.h, open.h, scsi.h, time.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/sfmmu/vm/hat_sfmmu.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.642 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.608 IQR)
- **Top Global Matches:** file_cluster_8: 14.642, file_cluster_13: 14.771, file_cluster_11: 14.919
- **Magnitude:** 8481.38 | **LOC:** 15642 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (22.3822%)
**Top Internal Functions/Classes:**
  * `hat_page_clrwrt` (Impact: 926.5)
    * *Intent:* * tte_valid = 1 * tte_size2 = size & TTE_SZ2_BITS (Panther and Olympus-C only) * tte_size = size * t...
  * `ism_tsb_entries` (Impact: 914.1)
    * *Intent:* /* * Select the optimum TSB size given the number of mappings * that need to be cached.
  * `hat_swapout` (Impact: 723.0)
  * `hat_lock_init` (Impact: 566.1)
    * *Intent:* #endif /* * Semi-private sfmmu data structures. Some of them are initialize in * startup or in hat_i...
  * `sfmmu_chgattr` (Impact: 294.5)
    * *Intent:* /* * hat_kern_setup() will call sfmmu_init_ktsbinfo()
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 903`, `structural_boundaries: 346`, `args: 55`, `func_start: 80`, `class_start: 66`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 2716`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`, `orphaned_logic: 30`
* *Architecture:* `io: 1`, `api: 500`, `import: 47`
* *Defense:* `safety: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vmsystm.h, rm.h, systm.h, vm_dep.h, mmu.h, machparam.h, cpuvar.h, sysmacros.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/cmd/awk_xpg4/awk3.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.555 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.973 IQR)
- **Top Global Matches:** file_cluster_8: 13.555, file_cluster_13: 13.91, file_cluster_11: 13.944
- **Magnitude:** 8083.29 | **LOC:** 2224 | **CtrlFlow:** 77.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.66%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 279`, `structural_boundaries: 83`, `args: 5`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 685`
* *Architecture:* `api: 144`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` y.tab.h, awk.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/bnxe/577xx/common/bnxe_clc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.427 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.344 IQR)
- **Top Global Matches:** file_cluster_8: 14.427, file_cluster_7: 14.684, file_cluster_13: 14.699
- **Magnitude:** 8023.38 | **LOC:** 15674 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.0257%), Tech Debt (29.9413%)
**Top Internal Functions/Classes:**
  * `elink_8073_xaui_wa` (Impact: 548.2)
  * `elink_set_sfp_media` (Impact: 543.4)
  * `elink_get_link_speed_duplex` (Impact: 97.2)
  * `elink_set_led` (Impact: 83.2)
  * `elink_sync_link` (Impact: 78.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1150`, `structural_boundaries: 774`, `args: 200`, `func_start: 171`, `class_start: 269`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2969`, `dead_code: 4`, `fragile_debt: 1`, `orphaned_logic: 68`
* *Architecture:* `io: 8`, `api: 982`, `import: 28`
* *Defense:* `doc: 51`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` if.h, aeu_inputs.h, stdio.h, 57712_reg.h, kernel.h, dev_info.h, malloc.h, shmem.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/fs/ufs/ufs_vnops.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.733 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.583 IQR)
- **Top Global Matches:** file_cluster_13: 14.733, file_cluster_8: 14.808, file_cluster_11: 14.926
- **Magnitude:** 7933.86 | **LOC:** 6525 | **CtrlFlow:** 62.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (16.8375%)
**Top Internal Functions/Classes:**
  * `ufs_write` (Impact: 1636.3)
  * `wrip` (Impact: 1459.3)
  * `ufs_getpage_miss` (Impact: 821.8)
    * *Intent:* /* * inlined lockfs checks
  * `ufs_putpage` (Impact: 657.5)
  * `ufs_create` (Impact: 226.9)
    * *Intent:* /* * If the size of the file changed, then update the * size field in the inode now. This can't be d...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 666`, `structural_boundaries: 405`, `args: 72`, `func_start: 34`, `class_start: 112`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1500`, `planned_debt: 1`, `fragile_debt: 7`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 363`, `import: 61`
* *Defense:* `safety: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` param.h, fcntl.h, vmsystm.h, ufs_fs.h, signal.h, user.h, filio.h, dnlc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/sun/io/scsi/adapters/fas.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.309 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.856 IQR)
- **Top Global Matches:** file_cluster_8: 14.309, file_cluster_7: 14.62, file_cluster_13: 14.665
- **Magnitude:** 7405.06 | **LOC:** 9444 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (17.5714%)
**Top Internal Functions/Classes:**
  * `fas_next_window` (Impact: 1067.7)
  * `fas_runpoll` (Impact: 1059.5)
  * `fas_finish` (Impact: 347.4)
  * `fas_commoncap` (Impact: 270.9)
  * `fas_ncmds_checkdrain` (Impact: 156.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 923`, `structural_boundaries: 474`, `args: 89`, `func_start: 91`, `class_start: 80`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 2635`, `dead_code: 1`, `fragile_debt: 8`, `orphaned_logic: 13`
* *Architecture:* `io: 29`, `api: 332`
* *Defense:* `safety: 6`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fasdma.h, file.h, fascmd.h, vtrace.h, scsi.h, fasvar.h, scsi_reset_notify.h, note.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/cmd/boot/bootadm/bootadm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.602 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.437 IQR)
- **Top Global Matches:** file_cluster_8: 14.602, file_cluster_13: 14.655, file_cluster_11: 14.741
- **Magnitude:** 7079.94 | **LOC:** 10263 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (9.3216%)
**Top Internal Functions/Classes:**
  * `bam_menu` (Impact: 1212.1)
  * `parse_args_internal` (Impact: 1047.6)
    * *Intent:* /* * svc:/system/filesystem/usr:default service checks for this file and * does a boot archive updat...
  * `cmpstat` (Impact: 120.8)
  * `extend_iso_archive` (Impact: 111.8)
  * `install_bootloader` (Impact: 104.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1011`, `structural_boundaries: 516`, `args: 101`, `func_start: 91`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 2395`, `orphaned_logic: 9`
* *Architecture:* `io: 162`, `api: 460`, `import: 44`
* *Defense:* `safety: 124`, `test: 48`, `immutability_locks: 48`, `cleanup: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` param.h, grp.h, ctype.h, fdisk.h, filio.h, deflt.h, zlib.h, statvfs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/sun4v/io/vdc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.078 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.918 IQR)
- **Top Global Matches:** file_cluster_8: 14.078, file_cluster_13: 14.272, file_cluster_11: 14.355
- **Magnitude:** 6919.66 | **LOC:** 8713 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (9.8611%)
**Top Internal Functions/Classes:**
  * `vdc_recv` (Impact: 777.1)
    * *Intent:* /* * Function: * vdc_is_opened *
  * `vdc_populate_descriptor` (Impact: 768.4)
  * `vdc_do_sync_op` (Impact: 727.6)
  * `vdc_process_msg_thread` (Impact: 135.8)
  * `vd_process_ioctl` (Impact: 119.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1071`, `structural_boundaries: 568`, `args: 19`, `func_start: 101`, `class_start: 51`
* *Risk/State:* `safety_bypasses: 45`, `high_risk_execution: 3`, `state_mutation: 2628`, `dead_code: 8`, `planned_debt: 10`, `orphaned_logic: 5`
* *Architecture:* `io: 42`, `api: 499`, `import: 41`
* *Defense:* `safety: 38`, `test: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vio_common.h, fcntl.h, archsystm.h, fdisk.h, vdsk_mailbox.h, mdeg.h, mach_descrip.h, promif.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `usr/src/lib/iconv_modules/ja/common/jfp_iconv_unicode.h` (C) | Magnitude: 609.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 456, state_mutation: 427, pointers: 153, branch: 126
- `usr/src/cmd/perl/contrib/Sun/Solaris/Intrs/Intrs.pm` (PERL) | Magnitude: 0.23 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, api: 5, import: 5, decorators: 4
- `usr/src/cmd/mdb/Makefile.subdirs` (MAKEFILE) | Magnitude: 19.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 10, api: 3, indent_tabs: 3, func_start: 2
- `usr/src/cmd/bnu/uuxqt.c` (C) | Magnitude: 450.06 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 342, state_mutation: 152, branch: 149, structural_boundaries: 109
- `usr/src/lib/libldap5/sources/ldap/common/url.c` (C) | Magnitude: 592.6 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 382, pointers: 155, indent_spaces: 154, branch: 111

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `usr/src/test/zfs-tests/tests/functional/xattr/xattr_010_neg.ksh` (SHELL) | Magnitude: 5.6 | Delta: **0.163 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety_bypasses: 9, structural_boundaries: 7, events: 5, sync_locks: 3
- `usr/src/lib/libdtrace_jni/java/src/org/opensolaris/os/dtrace/ConsumerEvent.java` (JAVA) | Magnitude: 7.54 | Delta: **0.238 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, doc: 8, structural_boundaries: 5, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `usr/src/tools/smatch/src/smatch_scripts/gen_implicit_dependencies.sh` (SHELL) | Magnitude: 0.03 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 15, io: 14, safety_bypasses: 9, branch: 8
- `usr/src/cmd/ast/libshell/common/tests/sun_solaris_cr_6904878_join_-t_no_longer_works_with_multibyte_char_separator.sh` (SHELL) | Magnitude: 105.94 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 67, branch: 49, structural_boundaries: 36, sec_reflection_metaprogramming: 33
- `usr/src/cmd/msgfmt/msgfmt.c` (C) | Magnitude: 1189.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 728, indent_tabs: 628, branch: 186, pointers: 180
- `usr/src/cmd/ast/libshell/common/tests/sun_solaris_cr_6904575_cut_-d_with_multibyte_character_no_longer_works.sh` (SHELL) | Magnitude: 109.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 68, branch: 50, structural_boundaries: 40, io: 36
- `usr/src/cmd/spell/spell.sh` (SHELL) | Magnitude: 118.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: branch: 51, indent_tabs: 39, state_mutation: 38, safety_bypasses: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `usr/src/ucbhead/curses.h` (C) | Magnitude: 130.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 102, macros: 82, api: 71, reflection_metaprogramming: 55
- `usr/src/cmd/ast/libshell/common/tests/sun_solaris_cr_6713682_compound_var_bleeds_through_subshell.sh` (SHELL) | Magnitude: 86.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 54, reflection_metaprogramming: 34, branch: 25, safety: 17
- `usr/src/cmd/ast/libshell/common/tests/sun_solaris_cr_6763594_command_failure_execs_twice.sh` (SHELL) | Magnitude: 24.24 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: io: 14, state_mutation: 12, reflection_metaprogramming: 12, structural_boundaries: 9
- `usr/src/test/zfs-tests/tests/functional/acl/nontrivial/zfs_acl_chmod_inherit_002_pos.ksh` (SHELL) | Magnitude: 266.18 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 141, state_mutation: 111, safety_bypasses: 106, branch: 96
- `usr/src/tools/smatch/src/ptrlist.h` (C) | Magnitude: 0.15 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 110, indent_tabs: 77, structural_boundaries: 53, pointers: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `usr/src/cmd/connstat/connstat_tcp.c` (C) | Magnitude: 224.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 212, pointers: 119, state_mutation: 99, structural_boundaries: 52
- `usr/src/cmd/ldapcachemgr/cachemgr.h` (C) | Magnitude: 70.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 48, pointers: 32, structural_boundaries: 29, indent_tabs: 21
- `usr/src/cmd/localedef/collate.c` (C) | Magnitude: 1097.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 644, indent_tabs: 543, pointers: 209, branch: 156
- `usr/src/cmd/sendmail/libsm/match.c` (C) | Magnitude: 161.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 105, indent_tabs: 83, branch: 34, structural_boundaries: 22
- `usr/src/cmd/vtfontcvt/vtfontcvt.c` (C) | Magnitude: 1245.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 668, state_mutation: 650, branch: 277, pointers: 153

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `usr/src/cmd/svc/svccfg/svccfg.l` (YACC) | Magnitude: 77.3 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 59, indent_tabs: 53, structural_boundaries: 52, generics: 40
- `usr/src/cmd/fm/fminject/common/inj_lex.l` (YACC) | Magnitude: 32.92 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: generics: 34, structural_boundaries: 31, indent_tabs: 30, state_mutation: 16
- `usr/src/lib/libdtrace_jni/java/src/org/opensolaris/os/dtrace/AggregateSpec.java` (JAVA) | Magnitude: 72.86 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 49, indent_tabs: 42, structural_boundaries: 24, generics: 14
- `usr/src/cmd/acpi/iasl/dtparser.y` (YACC) | Magnitude: 82.56 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 77, args: 68, indent_spaces: 55, branch: 27
- `usr/src/cmd/acpi/iasl/prparser.y` (YACC) | Magnitude: 79.68 | Delta: **0.145 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 74, args: 69, indent_spaces: 60, branch: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `usr/src/lib/rpcsec_gss/Makefile.com` (MAKEFILE) | Magnitude: 20.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, state_mutation: 5, dead_code: 3, indent_tabs: 3
- `usr/src/cmd/hal/addons/network-devices/svc-network-discovery` (SHELL) | Magnitude: 50.58 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 42, reflection_metaprogramming: 29, state_mutation: 27, structural_boundaries: 11
- `usr/src/lib/libprtdiag_psr/sparc/opl/Makefile` (MAKEFILE) | Magnitude: 19.56 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 10, structural_boundaries: 6, state_mutation: 3, dead_code: 3
- `usr/src/uts/i86pc/Makefile.workarounds` (MAKEFILE) | Magnitude: 33.36 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 18, dead_code: 1, sec_high_risk_execution: 1, sec_dead_code: 1
- `usr/src/cmd/fs.d/ufs/Makefile.roll` (MAKEFILE) | Magnitude: 15.64 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 3, state_mutation: 2, dead_code: 1, indent_tabs: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `usr/src/cmd/print/scripts/desktop-print-management` (SHELL) | Magnitude: 2.08 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, ui_framework: 1, ownership: 1, debug_prints: 1
- `usr/src/cmd/print/scripts/desktop-print-management-prefs` (SHELL) | Magnitude: 3.58 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 1, structural_boundaries: 1, ui_framework: 1, ownership: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `usr/src/test/libc-tests/tests/common/test_common.c` (C) | Magnitude: 310.7 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 266, state_mutation: 156, pointers: 83, structural_boundaries: 82
- `usr/src/contrib/ast/src/cmd/ksh93/tests/io.sh` (SHELL) | Magnitude: 6.55 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 353, io: 348, safety_bypasses: 226, indent_tabs: 186
- `usr/src/lib/mpapi/libmpapi/common/mpapi.c` (C) | Magnitude: 537.06 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 252, indent_tabs: 169, indent_spaces: 157, branch: 108
- `usr/src/lib/pkcs11/pkcs11_softtoken/common/softGeneral.c` (C) | Magnitude: 169.44 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 160, pointers: 65, structural_boundaries: 61, state_mutation: 42
- `usr/src/cmd/isns/isnsd/config.c` (C) | Magnitude: 201.94 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 147, branch: 70, state_mutation: 62, api: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `usr/src/uts/intel/sfxge/Makefile` (MAKEFILE) | Magnitude: 24.42 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, state_mutation: 6, func_start: 5, api: 3
- `usr/src/cmd/sgs/lddstub/Makefile.com` (MAKEFILE) | Magnitude: 15.68 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, import: 2, state_mutation: 1, dead_code: 1
- `usr/src/uts/intel/ktest/Makefile` (MAKEFILE) | Magnitude: 18.3 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, func_start: 5, api: 3, import: 2
- `usr/src/contrib/mDNSResponder/mDNSCore/mDNSEmbeddedAPI.h` (C) | Magnitude: 0.7 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: api: 53, branch: 47, indent_spaces: 44, macros: 16
- `usr/src/cmd/tcpd/Makefile` (MAKEFILE) | Magnitude: 28.06 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 25, indent_tabs: 13, state_mutation: 9, dead_code: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `usr/src/uts/common/io/qede/579xx/drivers/ecore/documentation/snippets/ecore_int_endis.h` (C) | Magnitude: 16.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 6, api: 4, pointers: 4
- `usr/src/uts/common/io/qede/579xx/drivers/ecore/documentation/snippets/ptt.h` (C) | Magnitude: 28.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, structural_boundaries: 14, api: 13, pointers: 10
- `usr/src/boot/efi/include/Protocol/Mtftp6.h` (C) | Magnitude: 144.06 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 298, api: 125, indent_spaces: 113, pointers: 47
- `usr/src/boot/efi/include/Protocol/Usb2HostController.h` (C) | Magnitude: 122.46 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 138, indent_spaces: 104, api: 94, pointers: 36
- `usr/src/uts/common/io/qede/579xx/drivers/ecore/ecore_init_fw_funcs.h` (C) | Magnitude: 59.94 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 79, api: 44, structural_boundaries: 26, pointers: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `usr/src/cmd/sendmail/util/praliases.c` (C) | Magnitude: 457.8 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 249, state_mutation: 210, branch: 99, pointers: 72
- `usr/src/cmd/svc/configd/object.c` (C) | Magnitude: 676.16 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 381, indent_tabs: 348, pointers: 213, api: 103
- `usr/src/cmd/ypcmd/ypcat.c` (C) | Magnitude: 8.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 10, ownership: 4, branch: 3, structural_boundaries: 3
- `usr/src/common/crypto/ecc/ecl_curve.c` (C) | Magnitude: 1.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: pointers: 91, indent_tabs: 78, state_mutation: 66, branch: 38
- `usr/src/common/nvpair/nvpair.c` (C) | Magnitude: 5500.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 1073, state_mutation: 871, pointers: 584, branch: 530

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `usr/src/cmd/abi/spectrans/parser/Makefile` (MAKEFILE) | Magnitude: 11.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 1, dead_code: 1, import: 1, sec_dead_code: 1
- `usr/src/cmd/abi/spectrans/parser/i386/Makefile` (MAKEFILE) | Magnitude: 11.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 1, dead_code: 1, import: 1, sec_dead_code: 1
- `usr/src/cmd/abi/spectrans/parser/sparc/Makefile` (MAKEFILE) | Magnitude: 11.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 1, dead_code: 1, import: 1, sec_dead_code: 1
- `usr/src/cmd/abi/spectrans/spec2map/Makefile` (MAKEFILE) | Magnitude: 11.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 1, dead_code: 1, import: 1, sec_dead_code: 1
- `usr/src/cmd/abi/spectrans/spec2map/i386/Makefile` (MAKEFILE) | Magnitude: 11.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 1, dead_code: 1, import: 1, sec_dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `usr/src/cmd/nvmeadm/nvmeadm_field.c` -> Churn: **74.2%** | Cog Load: 77.1216% | Debt: 19.9024%
- `usr/src/cmd/nvmeadm/nvmeadm.c` -> Churn: **71.01%** | Cog Load: 83.6245% | Debt: 10.625%
- `usr/src/uts/common/io/mac/mac_datapath_setup.c` -> Churn: **65.03%** | Cog Load: 80.9665% | Debt: 32.7651%
- `usr/src/uts/intel/io/viona/viona_rx.c` -> Churn: **63.74%** | Cog Load: 81.3028% | Debt: 17.4837%
- `usr/src/cmd/bhyve/common/pci_virtio_scsi.c` -> Churn: **59.96%** | Cog Load: 100.0% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `usr/src/cmd/dladm/dladm.c` -> **Toomas Soome** (100.0% isolated ownership) | Magnitude: 10440.8
- `usr/src/uts/common/io/fibre-channel/fca/emlxs/emlxs_solaris.c` -> **Toomas Soome** (100.0% isolated ownership) | Magnitude: 9220.86
- `usr/src/uts/common/dtrace/dtrace.c` -> **Patrick Mooney** (100.0% isolated ownership) | Magnitude: 8907.72
- `usr/src/uts/common/io/fibre-channel/fca/emlxs/emlxs_dfc.c` -> **Toomas Soome** (100.0% isolated ownership) | Magnitude: 8760.02
- `usr/src/lib/libstmf/common/stmf.c` -> **Toomas Soome** (100.0% isolated ownership) | Magnitude: 6777.44

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `usr/src/uts/common/gssapi/mechs/krb5/include/gssapiP_generic.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `usr/src/lib/libnvpair/libnvpair.h` -> **Severity: 843.988** (Blast Radius: 8.571 * Doc Risk: 98.4702%)
- `usr/src/head/locale.h` -> **Severity: 742.808** (Blast Radius: 7.682 * Doc Risk: 96.6946%)
- `usr/src/uts/common/gssapi/mechs/krb5/include/k5-int.h` -> **Severity: 423.8** (Blast Radius: 4.238 * Doc Risk: 100.0%)
- `usr/src/head/libelf.h` -> **Severity: 336.8** (Blast Radius: 3.368 * Doc Risk: 100.0%)
- `usr/src/lib/libc/inc/file64.h` -> **Severity: 325.399** (Blast Radius: 3.254 * Doc Risk: 99.9998%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
