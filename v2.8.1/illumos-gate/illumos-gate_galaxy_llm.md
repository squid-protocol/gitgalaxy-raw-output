# ARCHITECTURAL_BRIEF: illumos-gate
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/illumos/illumos-gate.git` |
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
| Total Artifacts | 48723 |
| Analyzed Artifacts (Scanned) | 37146 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11577 |
| Total LOC | 8688182 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 76.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7317 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0268 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3715 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1711 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 23844 | 8043754 | 64.2% |
| MAKEFILE | 6001 | 148740 | 16.2% |
| SHELL | 2705 | 160066 | 7.3% |
| PLAINTEXT | 2158 | 2 | 5.8% |
| ASSEMBLY | 897 | 162512 | 2.4% |
| CPP | 265 | 42685 | 0.7% |
| XML | 245 | 0 | 0.7% |
| HTML | 229 | 2537 | 0.6% |
| MARKDOWN | 205 | 0 | 0.6% |
| JAVA | 193 | 31158 | 0.5% |
| M4 | 114 | 10455 | 0.3% |
| PERL | 106 | 27091 | 0.3% |
| YACC | 74 | 35495 | 0.2% |
| PYTHON | 54 | 6382 | 0.1% |
| JSON | 38 | 15647 | 0.1% |
| BINARY_THREAT | 8 | 8 | 0.0% |
| OBJECTIVE-C | 4 | 842 | 0.0% |
| TCL | 3 | 608 | 0.0% |
| PROTO | 1 | 70 | 0.0% |
| CSV | 1 | 108 | 0.0% |
| RUST | 1 | 22 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +0.06; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 25%, Data / Markup / Trivial 18%, Large Core Modules 15%, I/O & Config Routines Files 13%, Many-Argument Workhorses Files 11%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 34771 | 93.6% |
| Unknown | 10 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2361 | 6.4% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11577*

**Composition by Extension & Reason:**
- `no_extension`: 1570x Unsupported Format (.undeterminable), 282x Excluded (Binary Format Detected), 106x Unresolved Ambiguity (No Retainable Structure)
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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 31.3 | 9.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 53.2 | 68.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 20.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 22.2 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.1 | 4.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 46.0 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 81.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 30.4 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 65.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 73.1 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2813121 | 21086 | 186 | `usr/src/contrib/mDNSResponder/mDNSCore/mDNS.c` |
| cleanup | 35458 | 5384 | 1 | `usr/src/lib/libscf/common/scf_tmpl.c` |
| guards | 359041 | 20252 | 26 | `usr/src/test/util-tests/tests/demangle/gcc-libstdc++.c` |
| danger | 194047 | 12899 | 13 | `usr/src/contrib/ast/src/cmd/INIT/package.sh` |
| concurrency | 8138 | 1601 | 0 | `usr/src/cmd/svc/configd/rc_node.c` |
| connectivity | 286290 | 28189 | 18 | `usr/src/uts/common/nfs/nfs4_kprot.h` |
| io | 48998 | 5166 | 2 | `usr/src/contrib/ast/src/cmd/INIT/package.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 7489 | 1975 | 0 | `usr/src/uts/common/io/pcic.c` |
| time | 4579 | 1404 | 0 | `usr/src/cmd/cron/cron.c` |
| serialization | 183 | 103 | 0 | `usr/src/cmd/ipf/tools/Makefile` |
| regex | 4243 | 846 | 0 | `usr/src/cmd/ypcmd/yp2lscripts/ypmap2src.sh` |
| events | 14215 | 2679 | 0 | `usr/src/lib/libstmf/common/store.c` |
| tests | 2293 | 370 | 0 | `usr/src/cmd/perl/contrib/Sun/Solaris/Lgrp/t/Lgrp.t` |
| docs | 34243 | 4059 | 1 | `usr/src/boot/efi/include/Uefi/UefiPxe.h` |
| debt | 78394 | 7964 | 3 | `usr/src/cmd/cxgbetool/cudbg_view.c` |
| mutation | 2169682 | 24112 | 152 | `usr/src/uts/common/io/fibre-channel/fca/qlc/ql_api.c` |
| dead_code | 79915 | 16165 | 6 | `usr/src/uts/common/io/sfxge/common/efx_regs_mcdi.h` |
| credential | 103 | 44 | 0 | `usr/src/cmd/ldap/ns_ldap/idsconfig.sh` |
| threat | 109111 | 10891 | 7 | `usr/src/uts/common/io/cxgbe/firmware/t4fw_interface.h` |
| ml_ai | 12081 | 2927 | 0 | `usr/src/uts/common/inet/ip/ip_if.c` |
| ui | 116 | 40 | 0 | `usr/src/cmd/tsol/misc/txzonemgr.sh` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `usr/src/contrib/ast/src/cmd/INIT/package.sh` (Hits: 1343)
- `usr/src/tools/scripts/webrev.sh` (Hits: 1089)
- `usr/src/contrib/ast/src/cmd/INIT/iffe.sh` (Hits: 862)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Makefile.lib.64** (`usr/src/lib/Makefile.lib.64`) — 1519 inbound connections
2. **ddi.h** (`usr/src/uts/common/sys/ddi.h`) — 1234 inbound connections
3. **debug.h** (`usr/src/uts/common/sys/debug.h`) — 1132 inbound connections
4. **kmem.h** (`usr/src/uts/common/sys/kmem.h`) — 1113 inbound connections
5. **modctl.h** (`usr/src/uts/common/sys/modctl.h`) — 1095 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **env.c** (`usr/src/boot/efi/libefi/env.c`) — 145 outbound dependencies
2. **startup.c** (`usr/src/uts/i86pc/os/startup.c`) — 96 outbound dependencies
3. **machdep.c** (`usr/src/uts/i86pc/os/machdep.c`) — 91 outbound dependencies
4. **ip.c** (`usr/src/uts/common/inet/ip/ip.c`) — 89 outbound dependencies
5. **ip_input.c** (`usr/src/uts/common/inet/ip/ip_input.c`) — 85 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `soft_build_public_key_object` **(Many-Argument Workhorses)** (@ `usr/src/lib/pkcs11/pkcs11_softtoken/common/softAttributeUtil.c`) -> Impact: **1943.0** | LOC: 2706
  * *Intent:* * - Parse the object's template, and when an error is detected such as * invalid attribute type, invalid attribute value, etc., return * with appropri...
- `soft_build_private_key_object` **(Many-Argument Workhorses)** (@ `usr/src/lib/pkcs11/pkcs11_softtoken/common/softAttributeUtil.c`) -> Impact: **1866.8** | LOC: 2652
  * *Intent:* * - Parse the object's template, and when an error is detected such as * invalid attribute type, invalid attribute value, etc., return * with appropri...
- `projent_parse_attribute_values` **(Many-Argument Workhorses)** (@ `usr/src/cmd/perl/contrib/Sun/Solaris/Project/Project.pm`) -> Impact: **1764.3** | LOC: 1349
  * *Intent:* # # projent_parse_attribute_values(values) # # Values is the right hand side of a name=values attribute/values pair. # This function parses the values...
- `strioctl` **(Many-Argument Workhorses)** (@ `usr/src/uts/common/os/streamio.c`) -> Impact: **1656.9** | LOC: 2534
  * *Intent:* /* * ioctl for streams */
- `setoption` **(Many-Argument Workhorses)** (@ `usr/src/cmd/sendmail/src/readcf.c`) -> Impact: **1470.8** | LOC: 1638
  * *Intent:* #define OPTNAME o->o_name == NULL ? "<unknown>" : o->o_name
- `tmxdate` **(Many-Argument Workhorses)** (@ `usr/src/contrib/ast/src/lib/libast/tm/tmxdate.c`) -> Impact: **1433.5** | LOC: 1590
  * *Intent:* #define K1(c1) (c1) #define K2(c1,c2) (((c1)<<8)|(c2)) #define K3(c1,c2,c3) (((c1)<<16)|((c2)<<8)|(c3)) #define K4(c1,c2,c3,c4) (((c1)<<24)|((c2)<<16)...
- `sadb_common_add` **(Many-Argument Workhorses)** (@ `usr/src/uts/common/inet/ip/sadb.c`) -> Impact: **1426.3** | LOC: 2278
  * *Intent:* * SAs can be "inbound", "outbound", or "both". The "primary" and "secondary" * hash bucket parameters are set in order of what the SA will be most of ...
- `opthelp` **(Many-Argument Workhorses)** (@ `usr/src/contrib/ast/src/lib/libast/misc/optget.c`) -> Impact: **1396.5** | LOC: 1741
  * *Intent:* * what: * 0 ?short by default, ?long if any long options used * * otherwise see help_text[] (--???) * external formatter: * \a...\a italic * \b...\b b...
- `dtrace_disx86` **(Many-Argument Workhorses)** (@ `usr/src/common/dis/i386/dis_tables.c`) -> Impact: **1354.0** | LOC: 2658
  * *Intent:* /* * Dissassemble a single x86 or amd64 instruction. * * Mode determines the default operating mode (SIZE16, SIZE32 or SIZE64) * for interpreting inst...
- `sfvprintf` **(Many-Argument Workhorses)** (@ `usr/src/contrib/ast/src/lib/libast/sfio/sfvprintf.c`) -> Impact: **1319.8** | LOC: 1355
  * *Intent:* /* On some platform(s), large functions are not compilable. ** In such a case, the below macro should be defined non-zero so that ** some in-lined mac...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `usr/src/uts/common/os` | 177 | 164204.26 | 68.05% | 50.37% |
| `usr/src/uts/common/fs/nfs` | 58 | 107553.82 | 71.88% | 41.53% |
| `usr/src/uts/common/io` | 120 | 106553.04 | 64.03% | 35.69% |
| `usr/src/uts/common/inet/ip` | 60 | 101974.48 | 59.8% | 38.96% |
| `usr/src/uts/common/fs/zfs` | 119 | 97019.52 | 61.41% | 40.07% |
| `usr/src/cmd/sendmail/src` | 50 | 74129.78 | 64.64% | 26.35% |
| `usr/src/uts/common/io/fibre-channel/fca/emlxs` | 23 | 73605.06 | 75.51% | 21.35% |
| `usr/src/uts/common/io/fibre-channel/fca/qlc` | 12 | 48907.02 | 63.77% | 18.28% |
| `usr/src/lib/libdwarf/common` | 167 | 47680.28 | 27.53% | 25.42% |
| `usr/src/uts/sun4v/io` | 45 | 46143.72 | 70.19% | 20.8% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `usr/src/contrib/ast/src/lib/libpp/pp.def` -> **100.0%** Exposure
- `usr/src/cmd/ipf/lib/genmask.c` -> **100.0%** Exposure
- `usr/src/cmd/mdb/common/libstandctf/ctf_subr.c` -> **100.0%** Exposure
- `usr/src/cmd/mdb/intel/kmdb/kmdb_kdi_isadep.c` -> **100.0%** Exposure
- `usr/src/common/atomic/atomic.c` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `usr/src/boot/forth/Makefile` -> **100.0%** Exposure
- `usr/src/boot/libsa/Makefile.inc` -> **100.0%** Exposure
- `usr/src/cmd/fm/modules/common/eversholt/Makefile` -> **100.0%** Exposure
- `usr/src/cmd/fm/modules/common/fabric-xlate/Makefile` -> **100.0%** Exposure
- `usr/src/cmd/fm/modules/common/sw-diag-response/software-diagnosis/Makefile` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `usr/src/uts/common/os/sunddi.c` -> **209** Orphaned Functions | **0** Duplicates
- `usr/src/contrib/ast/src/lib/libpp/pp.def` -> **186** Orphaned Functions | **0** Duplicates
- `usr/src/lib/libzonecfg/common/libzonecfg.c` -> **138** Orphaned Functions | **0** Duplicates
- `usr/src/uts/common/io/i40e/core/i40e_common.c` -> **136** Orphaned Functions | **0** Duplicates
- `usr/src/uts/common/io/cxgbe/common/t4_hw.c` -> **133** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `usr/src/cmd/cmd-crypto/pktool/genkey.c` -> **73.1059%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `354` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `161321` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `usr/src/cmd/fm/fmd/common/fmd_fmri.c` (C) -> Cumulative Risk: **781.71**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.23)
- **Magnitude:** 372.4 | **LOC:** 449 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `fmd_fmri_uriescape` (Many-Argument Workhorses, Impact: 37.9), `fmd_fmri_nvl2str` (Many-Argument Workhorses, Impact: 11.2), `fmd_fmri_auth2str` (Compute Cores, Impact: 10.3)

### 2. `usr/src/cmd/fm/fmd/common/fmd_idspace.c` (C) -> Cumulative Risk: **780.41**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.62)
- **Magnitude:** 305.04 | **LOC:** 343 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `fmd_idspace_xalloc_locked` (Many-Argument Workhorses, Impact: 11.3), `fmd_idspace_free` (Compute Cores, Impact: 10.2), `fmd_idspace_alloc_locked` (Compute Cores, Impact: 9.6)

### 3. `usr/src/lib/libsip/common/sip_dialog_ui.c` (C) -> Cumulative Risk: **774.4**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.53)
- **Magnitude:** 625.1 | **LOC:** 613 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `sip_create_dialog_req` (Many-Argument Workhorses, Impact: 60.9), `sip_get_dialog_local_tag` (Type Conversions, Impact: 13.6), `sip_get_dialog_remote_tag` (Type Conversions, Impact: 13.6)

### 4. `usr/src/cmd/fm/fmd/common/fmd_eventq.c` (C) -> Cumulative Risk: **773.43**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.89)
- **Magnitude:** 311.7 | **LOC:** 381 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `fmd_eventq_insert_at_time` (Compute Cores, Impact: 20.1), `fmd_eventq_delete` (Compute Cores, Impact: 13.3), `fmd_eventq_drop_topo` (Compute Cores, Impact: 13.0)

### 5. `usr/src/cmd/fm/fmd/common/fmd_time.c` (C) -> Cumulative Risk: **773.27**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.48)
- **Magnitude:** 234.84 | **LOC:** 399 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `fmd_time_sync` (C Struct Operations, Impact: 11.6), `fmd_time_ena2hrt` (Compute Cores, Impact: 11.5), `fmd_simulator_wait` (Compute Cores, Impact: 9.8)

### 6. `usr/src/cmd/scadm/sparc/mpxu/common/xsem.c` (C) -> Cumulative Risk: **772.73**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.49)
- **Magnitude:** 130.08 | **LOC:** 183 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `xsem_xwait` (Many-Argument Workhorses, Impact: 26.5), `xsem_wait` (Compute Cores, Impact: 11.3), `xsem_trywait` (Compute Cores, Impact: 6.7)

### 7. `usr/src/lib/pkcs11/pkcs11_kernel/common/kernelSession.c` (C) -> Cumulative Risk: **763.63**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.36)
- **Magnitude:** 437.52 | **LOC:** 594 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.1776%)
- **Heaviest Functions:** `C_Login` (Many-Argument Workhorses, Impact: 40.3), `kernel_get_operationstate` (Many-Argument Workhorses, Impact: 33.4), `kernel_set_operationstate` (Many-Argument Workhorses, Impact: 24.1)

### 8. `usr/src/lib/libsip/common/sip_hash.c` (C) -> Cumulative Risk: **760.95**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.62)
- **Magnitude:** 190.04 | **LOC:** 193 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9589%)
- **Heaviest Functions:** `sip_hash_delete` (Many-Argument Workhorses, Impact: 27.4), `sip_hash_add` (Defensive Guards, Impact: 9.4), `sip_hash_find` (Many-Argument Workhorses, Impact: 7.8)

### 9. `usr/src/lib/libuutil/common/uu_avl.c` (C) -> Cumulative Risk: **757.01**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.04)
- **Magnitude:** 425.76 | **LOC:** 569 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.4703%)
- **Heaviest Functions:** `uu_avl_pool_create` (Many-Argument Workhorses, Impact: 21.9), `uu_avl_insert` (Type Conversions, Impact: 15.7), `uu_avl_remove` (Compute Cores, Impact: 13.9)

### 10. `usr/src/lib/pkcs11/pkcs11_softtoken/common/softVerify.c` (C) -> Cumulative Risk: **755.32**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -1.14)
- **Magnitude:** 272.34 | **LOC:** 383 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `C_VerifyRecover` (Many-Argument Workhorses, Impact: 24.7), `C_VerifyInit` (Many-Argument Workhorses, Impact: 19.4), `C_VerifyRecoverInit` (Many-Argument Workhorses, Impact: 19.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `usr/src/uts/common/io/fibre-channel/fca/qlc/ql_api.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 19597.26 | **LOC:** 22988 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.4606%), Tech Debt (8.9072%)
**Top Internal Functions/Classes:**
  * `ql_83xx_ascii_fw_dump` **(Many-Argument Workhorses)** (Impact: 492.8)
    * *Intent:* /* * ql_83xx_ascii_fw_dump * Converts ISP83xx firmware binary dump to ascii. * * Input: * ha = adapt...
  * `ql_attach` **(Many-Argument Workhorses)** (Impact: 331.2)
    * *Intent:* * ql_attach * Configure and attach an instance of the driver * for a port. * * Input: * dip = pointe...
  * `ql_port_manage` **(Many-Argument Workhorses)** (Impact: 292.1)
    * *Intent:* * Perform port management or diagnostics. * * Input: * fca_handle = handle setup by ql_bind_port(). ...
  * `ql_25xx_ascii_fw_dump` **(Many-Argument Workhorses)** (Impact: 181.4)
    * *Intent:* /* * ql_25xx_ascii_fw_dump * Converts ISP25xx firmware binary dump to ascii. * * Input: * ha = adapt...
  * `ql_81xx_ascii_fw_dump` **(Many-Argument Workhorses)** (Impact: 181.4)
    * *Intent:* /* * ql_81xx_ascii_fw_dump * Converts ISP81xx firmware binary dump to ascii. * * Input: * ha = adapt...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3806 instances
* *State Mutation (weighted view):* 12359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3085`, `structural_boundaries: 1957`, `args: 510`, `func_start: 215`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 612`, `state_mutation: 4747`, `dead_code: 5`, `fragile_debt: 3`, `unreferenced_by_name: 14`
* *Architecture:* `api: 81`, `import: 11`
* *Defense:* `safety: 187`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` ql_api.h, ql_apps.h, ql_debug.h, ql_fm.h, ql_init.h, ql_iocb.h, ql_ioctl.h, ql_isr.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/dtrace/dtrace.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 15485.72 | **LOC:** 17435 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (98.8181%), Tech Debt (9.19%)
**Top Internal Functions/Classes:**
  * `dtrace_dif_subr` **(Many-Argument Workhorses)** (Impact: 1002.8)
    * *Intent:* /* * Emulate the execution of DTrace ID subroutines invoked by the call opcode. * Notice that we don...
  * `dtrace_difo_validate` **(Many-Argument Workhorses)** (Impact: 512.3)
    * *Intent:* /* * Validate a DTrace DIF object by checking the IR instructions. The following * rules are current...
  * `dtrace_dif_emulate` **(Many-Argument Workhorses)** (Impact: 418.7)
    * *Intent:* /* * Emulate the execution of DTrace IR instructions specified by the given * DIF object. This funct...
  * `dtrace_ioctl` **(Many-Argument Workhorses)** (Impact: 339.5)
    * *Intent:* /*ARGSUSED*/
  * `dtrace_probe` **(Many-Argument Workhorses)** (Impact: 331.9)
    * *Intent:* /* * If you're looking for the epicenter of DTrace, you just found it. This * is the function called...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2527 instances
* *State Mutation (weighted view):* 7883
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2905`, `structural_boundaries: 1541`, `args: 503`, `func_start: 227`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 122`, `state_mutation: 2829`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 25`, `import: 29`
* *Defense:* `safety: 117`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` in.h, strtolctype.h, atomic.h, cmn_err.h, conf.h, cpuvar.h, cred_impl.h, ctf_api.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/cmd/svc/svccfg/svccfg_libscf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 14868.24 | **LOC:** 17650 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (95.6411%), Tech Debt (11.9543%)
**Top Internal Functions/Classes:**
  * `upgrade_dependent` **(Many-Argument Workhorses)** (Impact: 928.6)
    * *Intent:* * - dependency pg in target is corrupt (error printed) * - running snapshot in dependent is missing ...
  * `lscf_service_import` **(Many-Argument Workhorses)** (Impact: 475.6)
    * *Intent:* * - instance added unexpectedly (error printed) * - instance deleted unexpectedly (error printed) * ...
  * `process_old_pg` **(Many-Argument Workhorses)** (Impact: 419.5)
    * *Intent:* * - couldn't upgrade dependents (backend access denied) * - couldn't import pg (backend access denie...
  * `upgrade_dependents` **(Many-Argument Workhorses)** (Impact: 397.7)
    * *Intent:* * - couldn't create dependent (repository read-only) * EACCES - could not modify dependents pg (back...
  * `lscf_instance_import` **(Many-Argument Workhorses)** (Impact: 325.5)
    * *Intent:* * EINVAL - invalid instance name (error printed) * - invalid pgroup_t's (error printed) * - invalid ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 156 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 1717 instances
* *High Risk Execution (weighted view):* 7
* *Memory Alloc (weighted view):* 16
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 5248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4381`, `structural_boundaries: 1293`, `args: 312`, `func_start: 182`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 55`, `high_risk_execution: 9`, `state_mutation: 1814`, `dead_code: 4`, `planned_debt: 25`, `fragile_debt: 2`, `unreferenced_by_name: 27`
* *Architecture:* `io: 7`, `api: 50`, `import: 31`
* *Defense:* `safety: 93`, `immutability_locks: 263`, `cleanup: 156`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` alloca.h, assert.h, ctype.h, door.h, errno.h, fcntl.h, fnmatch.h, inttypes.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/scsi/targets/st.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 14566.46 | **LOC:** 18596 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.0768%), Tech Debt (12.2463%)
**Top Internal Functions/Classes:**
  * `st_decode_sense` **(Many-Argument Workhorses)** (Impact: 443.2)
  * `st_ioctl` **(Many-Argument Workhorses)** (Impact: 349.2)
    * *Intent:* /* * This routine implements the ioctl calls. It is called * from the device switch at normal priori...
  * `st_set_state` **(Many-Argument Workhorses)** (Impact: 238.5)
  * `st_interpret_read_pos` **(Many-Argument Workhorses)** (Impact: 230.5)
    * *Intent:* #define FIX_ENDIAN32(x) st_swap32(x) #define FIX_ENDIAN64(x) st_swap64(x) #endif /* * st_interpret_r...
  * `st_do_mtioctop` **(Many-Argument Workhorses)** (Impact: 228.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2479 instances
* *State Mutation (weighted view):* 7837
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2877`, `structural_boundaries: 1606`, `args: 1417`, `func_start: 191`, `class_start: 169`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 2879`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 27`, `unreferenced_by_name: 3`
* *Architecture:* `api: 15`, `import: 10`
* *Defense:* `safety: 30`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` byteorder.h, ddi.h, ddidmareq.h, file.h, kstat.h, modctl.h, mtio.h, scsi.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/sata/impl/sata.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 14478.8 | **LOC:** 21963 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.7309%), Tech Debt (8.696%)
**Top Internal Functions/Classes:**
  * `sata_hba_ioctl` **(Many-Argument Workhorses)** (Impact: 157.1)
    * *Intent:* * DEVCTL_BUS_GETSTATE * * All other cmds are passed to HBA if it provide ioctl handler, or failed * ...
  * `sata_hba_event_notify` **(Many-Argument Workhorses)** (Impact: 150.4)
    * *Intent:* * Events for different addresses/addr types cannot be combined. * A warning message is generated for...
  * `sata_build_lsense_page_10` **(Many-Argument Workhorses)** (Impact: 123.8)
    * *Intent:* * * Note: Self test and SMART data is accessible in device log pages. * The log pages can be accesse...
  * `sata_dma_buf_setup` **(Many-Argument Workhorses)** (Impact: 122.7)
    * *Intent:* /* * Allocate DMA resources for the buffer * This function handles initial DMA resource allocation a...
  * `sata_txlt_start_stop_unit` **(Compute Cores)** (Impact: 120.4)
    * *Intent:* * SPC-4/SBC-3 SATL ATA power condition SATL SPC/SBC * ----------------------------------------------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2459 instances
* *State Mutation (weighted view):* 8130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2667`, `structural_boundaries: 1498`, `args: 765`, `func_start: 208`, `class_start: 138`
* *Risk/State:* `safety_bypasses: 151`, `state_mutation: 3212`, `dead_code: 9`, `planned_debt: 3`, `unreferenced_by_name: 12`
* *Architecture:* `api: 28`, `import: 27`
* *Defense:* `safety: 23`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` cmn_err.h, conf.h, ddi.h, ddifm.h, disp.h, errno.h, file.h, ddi.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/inet/ip/ip_if.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 14000.1 | **LOC:** 19148 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (76.2476%), Tech Debt (28.4269%)
**Top Internal Functions/Classes:**
  * `ip_rt_add` **(Many-Argument Workhorses)** (Impact: 322.5)
    * *Intent:* /* * ip_rt_add is called to add an IPv4 route to the forwarding table. * ill is passed in to associa...
  * `ip_sioctl_flags` **(Many-Argument Workhorses)** (Impact: 208.0)
    * *Intent:* /* * Set interface flags. Many flags require special handling (e.g., * bringing the interface down);...
  * `ip_sioctl_ilb_cmd` **(Many-Argument Workhorses)** (Impact: 165.9)
    * *Intent:* /* * ILB ioctl uses cv_wait (such as deleting a rule or adding a server) and * this assumes the cont...
  * `ipif_select_source_v4` **(Many-Argument Workhorses)** (Impact: 145.0)
    * *Intent:* /* * Pick the optimal ipif on `ill' for sending to destination `dst' from zone * `zoneid'. We rate u...
  * `ip_sioctl_arp` **(Many-Argument Workhorses)** (Impact: 144.0)
    * *Intent:* /* ARP IOCTLs. */ /* ARGSUSED */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2124 instances
* *State Mutation (weighted view):* 6649
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2548`, `structural_boundaries: 1528`, `args: 620`, `func_start: 340`, `class_start: 98`
* *Risk/State:* `safety_bypasses: 197`, `state_mutation: 2401`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 9`, `unreferenced_by_name: 109`
* *Architecture:* `api: 204`, `import: 72`
* *Defense:* `safety: 21`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 53):` arp.h, common.h, ilb_ip.h, ip.h, ip6.h, ip6_asp.h, ip_arp.h, ip_ftable.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/fs/nfs/nfs4_vnops.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 13483.66 | **LOC:** 16007 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.2583%), Tech Debt (21.0149%)
**Top Internal Functions/Classes:**
  * `nfs4open_otw` **(Many-Argument Workhorses)** (Impact: 468.6)
    * *Intent:* /* * The OPEN operation creates and/or opens a regular file * * ARGSUSED */
  * `nfs4close_one` **(Many-Argument Workhorses)** (Impact: 343.8)
    * *Intent:* * * CLOSE_RESEND and CLOSE_AFTER_RESEND will not attempt to retry after client * recovery. Instead, ...
  * `nfs4_reopen` **(Many-Argument Workhorses)** (Impact: 259.9)
    * *Intent:* * filehandles) may be handled silently by this routine. * - if it is EINTR, ETIMEDOUT, or NFS4_FRC_U...
  * `nfs4frlock` **(Many-Argument Workhorses)** (Impact: 233.1)
    * *Intent:* * * NFS4_LCK_CTYPE_RESEND: same as NFS4_LCK_CTYPE_RECLAIM, with the addition * that we will use the ...
  * `nfs4setattr` **(Many-Argument Workhorses)** (Impact: 205.9)
    * *Intent:* * To replace the "guarded" version 3 setattr, we use two types of compound * setattr requests: * 1. ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1911 instances
* *State Mutation (weighted view):* 6064
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2270`, `structural_boundaries: 802`, `args: 376`, `func_start: 147`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 2242`, `dead_code: 4`, `planned_debt: 13`, `fragile_debt: 43`, `unreferenced_by_name: 7`
* *Architecture:* `api: 42`, `import: 58`
* *Defense:* `safety: 42`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 39):` fs_subr.h, lm.h, nfs.h, nfs4.h, nfs4_clnt.h, nfs4_kprot.h, nfs_acl.h, nfs_clnt.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/scsi/adapters/mpt_sas/mptsas.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 11537.54 | **LOC:** 17103 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.7238%), Tech Debt (8.896%)
**Top Internal Functions/Classes:**
  * `mptsas_do_passthru` **(Many-Argument Workhorses)** (Impact: 241.5)
  * `mptsas_handle_event` **(Compute Cores)** (Impact: 208.8)
    * *Intent:* /* * handle events from ioc */
  * `mptsas_create_virt_lun` **(Many-Argument Workhorses)** (Impact: 207.4)
  * `mptsas_scsi_init_pkt` **(Many-Argument Workhorses)** (Impact: 189.2)
    * *Intent:* /* * tran_init_pkt(9E) - allocate scsi_pkt(9S) for command * * One of three possibilities: * - alloc...
  * `mptsas_handle_event_sync` **(Compute Cores)** (Impact: 187.3)
    * *Intent:* #define SMP_RESET_IN_PROGRESS MPI2_EVENT_SAS_TOPO_LR_SMP_RESET_IN_PROGRESS /* * handle sync events f...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1816 instances
* *State Mutation (weighted view):* 5816
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2154`, `structural_boundaries: 1442`, `args: 627`, `func_start: 253`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 225`, `state_mutation: 2184`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 3`, `unreferenced_by_name: 7`
* *Architecture:* `api: 30`, `import: 32`
* *Defense:* `safety: 30`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` ddifm.h, file.h, ddi.h, protocol.h, util.h, dv_node.h, model.h, note.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/fibre-channel/impl/fp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 11413.22 | **LOC:** 15410 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.6687%), Tech Debt (8.0753%)
**Top Internal Functions/Classes:**
  * `fp_fciocmd` **(Many-Argument Workhorses)** (Impact: 980.1)
    * *Intent:* /* * One heck of a function to serve userland. */
  * `fp_job_handler` **(Compute Cores)** (Impact: 164.9)
    * *Intent:* /* * Dedicated thread to perform various activities. One thread for * each fc_local_port_t (driver s...
  * `fp_ns_reg` **(Many-Argument Workhorses)** (Impact: 160.3)
    * *Intent:* /* * NS Registration function. * * It should be seriously noted that FC-GS-2 currently doesn't suppo...
  * `fp_validate_area_domain` **(Many-Argument Workhorses)** (Impact: 148.5)
    * *Intent:* /* * Handle Domain, Area changes in the Fabric. */
  * `fp_validate_rscn_page` **(Many-Argument Workhorses)** (Impact: 148.2)
    * *Intent:* /* * Work hard to make sense out of an RSCN page. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1969 instances
* *State Mutation (weighted view):* 6492
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1941`, `structural_boundaries: 909`, `args: 390`, `func_start: 134`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 216`, `state_mutation: 2554`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 9`, `import: 28`
* *Defense:* `safety: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` buf.h, byteorder.h, cmn_err.h, conf.h, ddi.h, errno.h, fc.h, fc_fcaif.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/sfmmu/vm/hat_sfmmu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 11371.14 | **LOC:** 15642 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.9379%), Tech Debt (19.3203%)
**Top Internal Functions/Classes:**
  * `sfmmu_tteload_addentry` **(Many-Argument Workhorses)** (Impact: 262.5)
    * *Intent:* /* * Function adds a tte entry into the hmeblk. It returns 0 if successful and 1 * otherwise. */
  * `sfmmu_hblk_alloc` **(Many-Argument Workhorses)** (Impact: 177.1)
    * *Intent:* * (b) if the reserve pool is empty, acquire hblk_reserve_lock * and return hblk_reserve. * * (3) cal...
  * `hat_join_region` **(Many-Argument Workhorses)** (Impact: 175.1)
    * *Intent:* /* * This routine implements the shared context functionality required when * attaching a segment to...
  * `hat_unload_callback` **(Many-Argument Workhorses)** (Impact: 163.7)
  * `sfmmu_hblk_unload` **(Many-Argument Workhorses)** (Impact: 127.3)
    * *Intent:* /* * This function unloads a range of addresses for an hmeblk. * It returns the next address to be u...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1898 instances
* *State Mutation (weighted view):* 5972
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1913`, `structural_boundaries: 1201`, `args: 561`, `func_start: 231`, `class_start: 186`
* *Risk/State:* `safety_bypasses: 60`, `state_mutation: 2176`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 9`, `unreferenced_by_name: 56`
* *Architecture:* `api: 132`, `import: 47`
* *Defense:* `safety: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` archsystm.h, atomic.h, bitmap.h, callb.h, cmn_err.h, cpu.h, cpu_module.h, cpuvar.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/inet/ip/ip.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 10773.44 | **LOC:** 15375 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (74.9039%), Tech Debt (23.5839%)
**Top Internal Functions/Classes:**
  * `ip_rput_dlpi_writer` **(Many-Argument Workhorses)** (Impact: 375.9)
    * *Intent:* /* * Handling of DLPI messages that require exclusive access to the ipsq. * * Need to do ipsq_pendin...
  * `ip_reassemble` **(Many-Argument Workhorses)** (Impact: 188.6)
    * *Intent:* /* * Handles both IPv4 and IPv6 reassembly - doing the out-of-order cases, * When an ipf is passed h...
  * `ip_xmit` **(Many-Argument Workhorses)** (Impact: 172.5)
    * *Intent:* * * We return an error on failure. In particular we return EWOULDBLOCK * when the driver flow contro...
  * `ip_set_destination_v4` **(Many-Argument Workhorses)** (Impact: 157.2)
    * *Intent:* * Note that we allow connect to broadcast and multicast addresses when * IPDF_ALLOW_MCBC is set. * f...
  * `ip_input_fragment` **(Many-Argument Workhorses)** (Impact: 144.4)
    * *Intent:* /* * Fragmentation reassembly. Each ILL has a hash table for * queuing packets undergoing reassembly...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1706 instances
* *State Mutation (weighted view):* 5508
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1902`, `structural_boundaries: 1116`, `args: 315`, `func_start: 185`, `class_start: 44`
* *Risk/State:* `safety_bypasses: 154`, `state_mutation: 2096`, `dead_code: 2`, `planned_debt: 7`, `fragile_debt: 14`, `unreferenced_by_name: 63`
* *Architecture:* `api: 135`, `import: 89`
* *Defense:* `safety: 16`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 73):` arp.h, cc.h, common.h, ilb_ip.h, ip.h, ip6.h, ip6_asp.h, ip_arp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/fibre-channel/ulp/fcp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 10304.1 | **LOC:** 16357 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.5564%), Tech Debt (9.2896%)
**Top Internal Functions/Classes:**
  * `fcp_port_ioctl` **(Many-Argument Workhorses)** (Impact: 334.9)
    * *Intent:* /* * called for ioctls on the transport's devctl interface, and the transport * has passed it to us ...
  * `fcp_handle_devices` **(Many-Argument Workhorses)** (Impact: 141.6)
    * *Intent:* * * Argument: *pptr Fcp port structure. * *devlist Pointer to the first entry of a table * containin...
  * `fcp_complete_pkt` **(Compute Cores)** (Impact: 140.5)
  * `fcp_send_scsi_ioctl` **(Compute Cores)** (Impact: 140.3)
    * *Intent:* * * Returns: * 0 = OK * EAGAIN = See errno.h * EBUSY = See errno.h * EINTR = See errno.h * EINVAL = ...
  * `fcp_setup_device_data_ioctl` **(Many-Argument Workhorses)** (Impact: 140.2)
    * *Intent:* * data = ioctl data * mode = See ioctl(9E) * * Output: * data = ioctl data * rval = return value - s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1584 instances
* *State Mutation (weighted view):* 5143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1943`, `structural_boundaries: 1770`, `args: 589`, `func_start: 175`, `class_start: 341`
* *Risk/State:* `safety_bypasses: 93`, `state_mutation: 1975`, `dead_code: 6`, `fragile_debt: 8`, `unreferenced_by_name: 3`
* *Architecture:* `api: 16`, `import: 22`
* *Defense:* `safety: 9`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` byteorder.h, console.h, ctype.h, devctl.h, fc.h, fc_ulpif.h, fcpvar.h, file.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/bnxe/577xx/common/bnxe_clc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 10074.3 | **LOC:** 15674 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.4568%), Tech Debt (11.1629%)
**Top Internal Functions/Classes:**
  * `elink_set_led` **(Many-Argument Workhorses)** (Impact: 101.5)
    * *Intent:* #endif /* EXCLUDE_XGXS */
  * `elink_link_update` **(Many-Argument Workhorses)** (Impact: 92.4)
    * *Intent:* /* The elink_link_update function should be called upon link * interrupt. * Link is considered up as...
  * `elink_populate_ext_phy` **(Many-Argument Workhorses)** (Impact: 89.1)
    * *Intent:* #ifndef ELINK_EMUL_ONLY
  * `elink_848x3_config_init` **(Many-Argument Workhorses)** (Impact: 83.2)
    * *Intent:* #endif /* #ifndef EXCLUDE_WARPCORE */ #if !defined(EXCLUDE_BCM8481) || !defined(EXCLUDE_BCM84833) #d...
  * `elink_get_link_speed_duplex` **(Many-Argument Workhorses)** (Impact: 81.3)
    * *Intent:* #endif /* EXCLUDE_XGXS */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1446 instances
* *State Mutation (weighted view):* 4615
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2010`, `structural_boundaries: 1635`, `args: 436`, `func_start: 300`, `class_start: 451`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1723`, `dead_code: 4`, `fragile_debt: 3`, `unreferenced_by_name: 30`
* *Architecture:* `api: 41`, `import: 28`
* *Defense:* `doc: 82`, `immutability_locks: 90`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` 57712_reg.h, aeu_inputs.h, inet.h, byteorder.h, bcmtype.h, bigmac_addresses.h, clc.h, clc_reg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/comstar/port/qlt/qlt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 10000.68 | **LOC:** 10798 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.6551%), Tech Debt (11.9658%)
**Top Internal Functions/Classes:**
  * `qlt_attach` **(Many-Argument Workhorses)** (Impact: 294.8)
  * `qlt_firmware_dump` **(Many-Argument Workhorses)** (Impact: 225.2)
    * *Intent:* /* * All QLT_FIRMWARE_* will mainly be handled in this function * It can not be called in interrupt ...
  * `qlt_ioctl` **(Many-Argument Workhorses)** (Impact: 191.2)
    * *Intent:* /* * All of these ioctls are unstable interfaces which are meant to be used * in a controlled lab en...
  * `qlt_isr` **(Many-Argument Workhorses)** (Impact: 160.3)
    * *Intent:* /* * **SHOULD ONLY BE CALLED FROM INTERRUPT CONTEXT. DO NOT CALL ELSEWHERE** */ /* ARGSUSED */
  * `qlt_msix_default_handler` **(Many-Argument Workhorses)** (Impact: 150.7)
    * *Intent:* /* * **SHOULD ONLY BE CALLED FROM INTERRUPT CONTEXT. DO NOT CALL ELSEWHERE** */ /* ARGSUSED */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1729 instances
* *State Mutation (weighted view):* 6175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1579`, `structural_boundaries: 772`, `args: 425`, `func_start: 137`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 200`, `state_mutation: 2717`, `dead_code: 2`, `fragile_debt: 16`, `unreferenced_by_name: 5`
* *Architecture:* `api: 68`, `import: 21`
* *Defense:* `safety: 146`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` qlt.h, qlt_dma.h, qlt_ioctl.h, qlt_open.h, atomic.h, byteorder.h, conf.h, cred.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/fibre-channel/fca/qlc/ql_xioctl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 9916.7 | **LOC:** 10723 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.3935%), Tech Debt (8.4786%)
**Top Internal Functions/Classes:**
  * `ql_scsi_passthru` **(Many-Argument Workhorses)** (Impact: 308.0)
    * *Intent:* * ql_scsi_passthru * IOCTL SCSI passthrough. * * Input: * ha: adapter state pointer. * cmd: User spa...
  * `ql_setup_flash` **(Compute Cores)** (Impact: 177.4)
    * *Intent:* /* * ql_setup_flash * Gets the manufacturer and id number of the flash chip, and * sets up the size ...
  * `ql_sdm_ioctl` **(Many-Argument Workhorses)** (Impact: 145.5)
    * *Intent:* * arg: Pointer to EXT_IOCTL cmd data in application land. * mode: flags * * Returns: * 0: success * ...
  * `ql_process_flt` **(Many-Argument Workhorses)** (Impact: 122.4)
    * *Intent:* /* * ql_process_flt * Obtains flash addresses from flash layout table * * Input: * ha: adapter state...
  * `ql_xioctl` **(Many-Argument Workhorses)** (Impact: 119.7)
    * *Intent:* * arg: data type varies with request * mode: flags * cred_p: credentials pointer * rval_p: pointer t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1900 instances
* *State Mutation (weighted view):* 6079
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1567`, `structural_boundaries: 906`, `args: 286`, `func_start: 106`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 85`, `state_mutation: 2279`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 14`, `import: 9`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` ql_api.h, ql_apps.h, ql_debug.h, ql_init.h, ql_iocb.h, ql_ioctl.h, ql_mbx.h, ql_nx.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/lib/pkcs11/pkcs11_softtoken/common/softAttributeUtil.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 9398.88 | **LOC:** 7094 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (10.4814%)
**Top Internal Functions/Classes:**
  * `soft_build_public_key_object` **(Many-Argument Workhorses)** (Impact: 1943.0)
    * *Intent:* * - Parse the object's template, and when an error is detected such as * invalid attribute type, inv...
  * `soft_build_private_key_object` **(Many-Argument Workhorses)** (Impact: 1866.8)
    * *Intent:* * - Parse the object's template, and when an error is detected such as * invalid attribute type, inv...
  * `soft_find_match_attrs` **(Many-Argument Workhorses)** (Impact: 583.8)
  * `soft_build_secret_key_object` **(Many-Argument Workhorses)** (Impact: 510.9)
    * *Intent:* * invalid attribute type, invalid attribute value, etc., return * with appropriate return value. * -...
  * `soft_get_private_value` **(Many-Argument Workhorses)** (Impact: 165.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 31 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 771 instances
* *Concurrency (weighted view):* 12
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 2325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1650`, `structural_boundaries: 858`, `args: 275`, `func_start: 60`
* *Risk/State:* `safety_bypasses: 142`, `state_mutation: 783`, `dead_code: 1`, `unreferenced_by_name: 18`
* *Architecture:* `api: 51`, `concurrency: 2`, `import: 16`
* *Defense:* `safety: 12`, `sync_locks: 2`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` aes_impl.h, arcfour.h, bignum.h, blowfish_impl.h, des_impl.h, rsa_impl.h, cryptoki.h, softCrypt.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/vm/seg_vn.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 9164.16 | **LOC:** 10343 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.6026%), Tech Debt (19.8685%)
**Top Internal Functions/Classes:**
  * `segvn_fault_vnodepages` **(Many-Argument Workhorses)** (Impact: 609.5)
    * *Intent:* #else /* VM_STATS */ #define SEGVN_VMSTAT_FLTVNPAGES(idx) #endif
  * `segvn_fault` **(Many-Argument Workhorses)** (Impact: 412.7)
    * *Intent:* * Call segvn_softunlock * Return * endif * Checking and set up work * If we will need some non-anony...
  * `segvn_faultpage` **(Many-Argument Workhorses)** (Impact: 330.1)
    * *Intent:* * Return * endif * If this is an anon page * Use anon_getpage to get the page * else * Find page in ...
  * `segvn_pagelock` **(Many-Argument Workhorses)** (Impact: 327.1)
    * *Intent:* * segment case reference count in pcache entry counts active locks from many * different segments so...
  * `segvn_lockop` **(Many-Argument Workhorses)** (Impact: 286.6)
    * *Intent:* * increment p_lckcnt by calling page_subclaim() which takes care of * availrmem accounting and p_lck...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1298 instances
* *State Mutation (weighted view):* 3977
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1900`, `structural_boundaries: 827`, `args: 216`, `func_start: 61`, `class_start: 216`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 1381`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 32`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 33`
* *Defense:* `safety: 130`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` bitmap.h, callb.h, cmn_err.h, cred.h, debug.h, dumphdr.h, errno.h, kmem.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/fs/nfs/nfs4_srv.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 8792.32 | **LOC:** 10505 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.3662%), Tech Debt (14.687%)
**Top Internal Functions/Classes:**
  * `rfs4_op_rename` **(Many-Argument Workhorses)** (Impact: 222.9)
    * *Intent:* /* * rename: args: SAVED_FH: from directory, CURRENT_FH: target directory, * oldname and newname. * ...
  * `rfs4_createfile` **(Many-Argument Workhorses)** (Impact: 205.2)
  * `rfs4_op_lock` **(Many-Argument Workhorses)** (Impact: 177.5)
    * *Intent:* /*ARGSUSED*/
  * `rfs4_op_create` **(Many-Argument Workhorses)** (Impact: 173.2)
    * *Intent:* /* * nfsv4 create is used to create non-regular files. For regular files, * use nfsv4 open. */ /* AR...
  * `rfs4_op_open` **(Many-Argument Workhorses)** (Impact: 161.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1514 instances
* *State Mutation (weighted view):* 4669
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1455`, `structural_boundaries: 920`, `args: 201`, `func_start: 124`, `class_start: 184`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 1641`, `dead_code: 3`, `fragile_debt: 15`, `unreferenced_by_name: 11`
* *Architecture:* `api: 66`, `import: 46`
* *Defense:* `safety: 9`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` fs_reparse.h, common.h, ip.h, ip6.h, export.h, lm.h, nfs.h, nfs4.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/fibre-channel/fca/emlxs/emlxs_dfc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 8769.18 | **LOC:** 11112 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (82.2589%), Tech Debt (8.2384%)
**Top Internal Functions/Classes:**
  * `emlxs_dfc_send_mbox` **(Many-Argument Workhorses)** (Impact: 243.3)
    * *Intent:* } /* emlxs_dfc_set_diag() */ /*ARGSUSED*/
  * `emlxs_fcio_get_port_attrs` **(Many-Argument Workhorses)** (Impact: 147.7)
    * *Intent:* } /* emlxs_fcio_get_disc_port_attrs() */ /*ARGSUSED*/
  * `emlxs_fcio_get_disc_port_attrs` **(Many-Argument Workhorses)** (Impact: 143.0)
    * *Intent:* } /* emlxs_fcio_get_other_adapter_ports() */ /*ARGSUSED*/
  * `emlxs_fcio_get_adapter_port_attrs` **(Many-Argument Workhorses)** (Impact: 140.3)
    * *Intent:* } /* emlxs_fcio_get_adapter_attrs() */ #ifndef _MULTI_DATAMODEL /* ARGSUSED */ #endif
  * `emlxs_send_menlo_cmd` **(Many-Argument Workhorses)** (Impact: 132.9)
    * *Intent:* } /* emlxs_dfc_send_menlo() */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1433 instances
* *State Mutation (weighted view):* 4890
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1480`, `structural_boundaries: 732`, `args: 631`, `func_start: 109`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 271`, `state_mutation: 2024`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 13`, `import: 1`
* *Defense:* `safety: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` emlxs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/fibre-channel/fca/emlxs/emlxs_solaris.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 8704.82 | **LOC:** 12434 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (73.0349%), Tech Debt (10.9332%)
**Top Internal Functions/Classes:**
  * `emlxs_fca_port_manage` **(Many-Argument Workhorses)** (Impact: 432.7)
    * *Intent:* } /* emlxs_fca_reset() */
  * `emlxs_fca_bind_port` **(Many-Argument Workhorses)** (Impact: 212.6)
    * *Intent:* /* * emlxs_fca_bind_port * * Arguments: * * dip: the dev_info pointer for the ddiinst * port_info: p...
  * `emlxs_fca_pkt_abort` **(Many-Argument Workhorses)** (Impact: 152.5)
    * *Intent:* } /* emlxs_ub_destroy() */ /*ARGSUSED*/
  * `emlxs_check_parm` **(Many-Argument Workhorses)** (Impact: 146.4)
    * *Intent:* } /* emlxs_get_props() */
  * `emlxs_send_els_rsp` **(Many-Argument Workhorses)** (Impact: 142.6)
    * *Intent:* } /* emlxs_send_els() */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1567 instances
* *State Mutation (weighted view):* 4988
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1568`, `structural_boundaries: 954`, `args: 570`, `func_start: 123`
* *Risk/State:* `safety_bypasses: 207`, `state_mutation: 1854`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 22`
* *Architecture:* `api: 73`, `import: 3`
* *Defense:* `safety: 80`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` emlxs.h, emlxs_version.h, modctl.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/inet/ip/sadb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 8439.96 | **LOC:** 8129 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.8425%), Tech Debt (41.8031%)
**Top Internal Functions/Classes:**
  * `sadb_common_add` **(Many-Argument Workhorses)** (Impact: 1426.3)
    * *Intent:* * SAs can be "inbound", "outbound", or "both". The "primary" and "secondary" * hash bucket parameter...
  * `sadb_update_sa` **(Many-Argument Workhorses)** (Impact: 153.4)
    * *Intent:* /* * Common code to update an SA. */
  * `sadb_acquire` **(Many-Argument Workhorses)** (Impact: 138.5)
    * *Intent:* /* * For this mblk, insert a new acquire record. Assume bucket contains addrs * of all of the same l...
  * `sadb_sa2msg` **(Many-Argument Workhorses)** (Impact: 135.5)
    * *Intent:* /* * Given an original message header with sufficient space following it, and an * SA, construct a f...
  * `sadb_form_query` **(Many-Argument Workhorses)** (Impact: 130.9)
    * *Intent:* /* * Common function which extracts several PF_KEY extensions for ease of * SADB matching. * * XXX T...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1248 instances
* *State Mutation (weighted view):* 4003
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1164`, `structural_boundaries: 475`, `args: 173`, `func_start: 118`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 152`, `state_mutation: 1507`, `dead_code: 6`, `planned_debt: 4`, `fragile_debt: 31`, `unreferenced_by_name: 30`
* *Architecture:* `api: 65`, `import: 44`
* *Defense:* `safety: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` common.h, ip.h, ip6.h, ip_if.h, ip_ire.h, ipclassifier.h, ipdrop.h, ipsec_impl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/os/streamio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 8433.68 | **LOC:** 8752 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.8637%), Tech Debt (15.159%)
**Top Internal Functions/Classes:**
  * `strioctl` **(Many-Argument Workhorses)** (Impact: 1656.9)
    * *Intent:* /* * ioctl for streams */
  * `kstrgetmsg` **(Many-Argument Workhorses)** (Impact: 437.0)
    * *Intent:* * Note that a NULL uiop implies that FNDELAY and FNONBLOCK are assumed * not enabled. * The timeout ...
  * `strgetmsg` **(Many-Argument Workhorses)** (Impact: 335.4)
    * *Intent:* /* * Get the next message from the read queue. If the message is * priority, STRPRI will have been s...
  * `strrput_nondata` **(Many-Argument Workhorses)** (Impact: 252.9)
  * `strdoioctl` **(Many-Argument Workhorses)** (Impact: 209.0)
    * *Intent:* * Send an ioctl message downstream and wait for acknowledgement. * flags may be set to either U_TO_K...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1224 instances
* *State Mutation (weighted view):* 3749
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1649`, `structural_boundaries: 690`, `args: 222`, `func_start: 43`, `class_start: 89`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 1301`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 9`, `unreferenced_by_name: 15`
* *Architecture:* `api: 29`, `import: 53`
* *Defense:* `safety: 11`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 36):` audit.h, autoconf.h, cmn_err.h, cred.h, debug.h, dld.h, errno.h, file.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/cmd/boot/bootadm/bootadm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 8408.56 | **LOC:** 10263 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.3573%), Tech Debt (7.9084%)
**Top Internal Functions/Classes:**
  * `get_partition` **(Compute Cores)** (Impact: 615.7)
    * *Intent:* #define SECTOR_SIZE 512
  * `get_set_kernel` **(Many-Argument Workhorses)** (Impact: 179.5)
    * *Intent:* /* * Title for an entry to set properties that once went in bootenv.rc. */ #define BOOTENV_RC_TITLE ...
  * `line_parser` **(Many-Argument Workhorses)** (Impact: 140.8)
    * *Intent:* /* * A line in menu.lst looks like * [ ]*<cmd>[ \t=]*<arg>* */
  * `bam_menu` **(Many-Argument Workhorses)** (Impact: 133.5)
  * `cmpstat` **(Many-Argument Workhorses)** (Impact: 128.9)
    * *Intent:* /*ARGSUSED*/
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 138 instances
* *Amplified Cascading Flux:* 1216 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 3702
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1736`, `structural_boundaries: 1124`, `args: 373`, `func_start: 166`, `class_start: 75`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 2`, `state_mutation: 1270`, `dead_code: 2`, `unreferenced_by_name: 3`
* *Architecture:* `io: 101`, `api: 44`, `import: 44`
* *Defense:* `safety: 251`, `test: 1`, `immutability_locks: 98`, `cleanup: 205`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` alloca.h, bootadm.h, ctype.h, deflt.h, device_info.h, dirent.h, errno.h, fcntl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/cmd/cpio/cpio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 8190.98 | **LOC:** 9761 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.3517%), Tech Debt (8.4526%)
**Top Internal Functions/Classes:**
  * `setup` **(Many-Argument Workhorses)** (Impact: 203.5)
    * *Intent:* /* * setup: Perform setup and initialization functions. Parse the options * using getopt(3C), call c...
  * `gethdr` **(Compute Cores)** (Impact: 185.9)
    * *Intent:* #endif /* * gethdr: Get a header from the archive, validate it and check for the trailer. * Any user...
  * `openout` **(Compute Cores)** (Impact: 168.0)
    * *Intent:* /* * openout: Open files for output and set all necessary information. * If the u option is set (unc...
  * `rstfiles` **(Compute Cores)** (Impact: 161.3)
    * *Intent:* /* * rstfiles: Perform final changes to the file. If the -u option is set, * and overwrite == U_OVER...
  * `verbose` **(Compute Cores)** (Impact: 138.1)
    * *Intent:* /* * verbose: For each file, print either the filename (-v) or a dot (-V). * If the -t option (table...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 46 instances
* *Amplified Rce:* 4 instances
* *Amplified Cascading Flux:* 1440 instances
* *High Risk Execution (weighted view):* 10
* *Memory Alloc (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 4
* *State Mutation (weighted view):* 4375
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2116`, `structural_boundaries: 1002`, `args: 944`, `func_start: 111`, `class_start: 60`
* *Risk/State:* `safety_bypasses: 72`, `high_risk_execution: 12`, `state_mutation: 1495`, `dead_code: 4`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 81`, `api: 30`, `import: 37`
* *Defense:* `safety: 51`, `doc: 2`, `immutability_locks: 6`, `cleanup: 85`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` aclutils.h, attr.h, cpio.h, ctype.h, dirent.h, errno.h, fcntl.h, fnmatch.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/cmd/dladm/dladm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 8051.08 | **LOC:** 10617 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (71.2679%), Tech Debt (7.7083%)
**Top Internal Functions/Classes:**
  * `create_modify_add_bridge` **(Many-Argument Workhorses)** (Impact: 178.9)
  * `do_show_bridge` **(Many-Argument Workhorses)** (Impact: 165.3)
  * `do_create_vnic` **(Many-Argument Workhorses)** (Impact: 145.3)
  * `do_show_aggr` **(Many-Argument Workhorses)** (Impact: 136.6)
  * `print_link_topology` **(Many-Argument Workhorses)** (Impact: 114.7)
    * *Intent:* /* * Print the active topology information. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 18 instances
* *Amplified Cascading Flux:* 1033 instances
* *High Risk Execution (weighted view):* 10
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 3160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1881`, `structural_boundaries: 1309`, `args: 389`, `func_start: 194`, `class_start: 63`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 14`, `state_mutation: 1094`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 60`, `import: 54`
* *Defense:* `safety: 175`, `immutability_locks: 210`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` inet.h, auth_attr.h, auth_list.h, adt.h, adt_event.h, ctype.h, dlfcn.h, errno.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `usr/src/cmd/nvmeadm/nvmeadm_field.c` -> Churn: **74.2%** | Cog Load: 69.4862% | Debt: 9.4997%
- `usr/src/cmd/nvmeadm/nvmeadm.c` -> Churn: **65.29%** | Cog Load: 57.7388% | Debt: 8.3232%
- `usr/src/uts/common/io/mac/mac_datapath_setup.c` -> Churn: **65.03%** | Cog Load: 76.9005% | Debt: 18.0065%
- `usr/src/uts/intel/io/viona/viona_rx.c` -> Churn: **63.74%** | Cog Load: 78.1264% | Debt: 17.4837%
- `usr/src/cmd/bhyve/common/pci_virtio_scsi.c` -> Churn: **59.96%** | Cog Load: 80.7225% | Debt: 8.355%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `usr/src/uts/common/dtrace/dtrace.c` -> **Patrick Mooney** (100.0% isolated ownership) | Magnitude: 15485.72
- `usr/src/cmd/svc/svccfg/svccfg_libscf.c` -> **Toomas Soome** (100.0% isolated ownership) | Magnitude: 14868.24
- `usr/src/uts/common/fs/nfs/nfs4_vnops.c` -> **Toomas Soome** (100.0% isolated ownership) | Magnitude: 13483.66
- `usr/src/uts/common/inet/ip/ip.c` -> **Toomas Soome** (100.0% isolated ownership) | Magnitude: 10773.44
- `usr/src/uts/common/io/fibre-channel/fca/emlxs/emlxs_dfc.c` -> **Toomas Soome** (100.0% isolated ownership) | Magnitude: 8769.18

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `usr/src/uts/common/sys/devops.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 16.5631%)
- `usr/src/uts/common/sys/scsi/impl/uscsi.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `usr/src/uts/common/sys/strsubr.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `usr/src/uts/common/sys/model.h` -> **Severity: 2.349** (Embedded: 0.0399 * Error Risk: 58.7964%)
- `usr/src/uts/common/sys/ddi_hp_impl.h` -> **Severity: 2.15** (Embedded: 0.0236 * Error Risk: 91.1339%)
- `usr/src/uts/common/sys/rwstlock.h` -> **Severity: 1.874** (Embedded: 0.0299 * Error Risk: 62.5811%)
- `usr/src/uts/common/sys/vnode.h` -> **Severity: 1.726** (Embedded: 0.0378 * Error Risk: 45.672%)
- `usr/src/uts/common/sys/dditypes.h` -> **Severity: 1.716** (Embedded: 0.035 * Error Risk: 49.0742%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `usr/src/uts/Makefile.uts` -> **Severity: 493.9** (Blast Radius: 4.939 * Doc Risk: 100.0%)
- `usr/src/uts/common/gssapi/mechs/krb5/include/k5-int.h` -> **Severity: 283.6** (Blast Radius: 2.836 * Doc Risk: 100.0%)
- `usr/src/head/pwd.h` -> **Severity: 158.1** (Blast Radius: 1.581 * Doc Risk: 100.0%)
- `usr/src/tools/smatch/src/check_debug.h` -> **Severity: 129.5** (Blast Radius: 1.295 * Doc Risk: 100.0%)
- `usr/src/tools/smatch/src/smatch.h` -> **Severity: 124.3** (Blast Radius: 1.243 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
