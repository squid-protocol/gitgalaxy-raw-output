# ARCHITECTURAL_BRIEF: illumos-gate
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/illumos/illumos-gate.git` |
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
- **Scope:** 37177 analyzed artifact(s), 9283815 LOC.
- **Load-bearing artifact:** `usr/src/uts/common/sys/types.h` -- 2522 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `usr/src/boot/efi/libefi/env.c` -- pulls in 145 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `usr/src/uts/common/io/fibre-channel/fca/qlc/ql_api.c` at magnitude 19567.26 (structural weight, not risk).
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
| Total Artifacts | 48723 |
| Analyzed Artifacts (Scanned) | 37177 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11546 |
| Total LOC | 9283815 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 76.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6897 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0139 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 12.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1798 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 23713 | 8581174 | 63.8% |
| MAKEFILE | 5914 | 138424 | 15.9% |
| SHELL | 2708 | 159903 | 7.3% |
| PLAINTEXT | 2166 | 2 | 5.8% |
| ASSEMBLY | 982 | 182027 | 2.6% |
| CPP | 417 | 92491 | 1.1% |
| XML | 246 | 0 | 0.7% |
| HTML | 229 | 2537 | 0.6% |
| MARKDOWN | 201 | 0 | 0.5% |
| JAVA | 194 | 31624 | 0.5% |
| M4 | 113 | 8647 | 0.3% |
| PERL | 106 | 27091 | 0.3% |
| YACC | 74 | 35495 | 0.2% |
| PYTHON | 53 | 5681 | 0.1% |
| JSON | 38 | 15647 | 0.1% |
| TCL | 6 | 1025 | 0.0% |
| BMS | 4 | 218 | 0.0% |
| OBJECTIVE-C | 4 | 842 | 0.0% |
| REXX | 4 | 522 | 0.0% |
| PHP | 2 | 265 | 0.0% |
| PROTO | 1 | 70 | 0.0% |
| CSV | 1 | 108 | 0.0% |
| RUST | 1 | 22 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 5 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 37169 |
| cp1252 | cp1252-fallback | 5 |
| unknown | unknown | 2 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 25%, Data / Markup / Trivial 18%, Many-Argument Workhorses Files 13%, Large Core Modules (3) 11%, Large Core Modules 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 34806 | 93.6% |
| Unknown | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2365 | 6.4% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11546*

**Composition by Extension & Reason:**
- `no_extension`: 1551x Unsupported Format (.undeterminable), 282x Excluded (Binary Format Detected), 125x Unresolved Ambiguity (No Retainable Structure)
- `.d`: 1203x Unsupported Format (.d), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.3c`: 569x Unsupported Format (.3c)
- `.9f`: 556x Unsupported Format (.9f)
- `.p5m`: 555x Unsupported Format (.p5m)
- `.conf`: 377x Unsupported Format (.conf)
- `.src`: 321x Unsupported Format (.src), 3x Excluded (Embedded Hex Payload: 644 hex tokens in 587 LOC), 2x Excluded (Embedded Hex Payload: 616 hex tokens in 530 LOC)
- `.tbl`: 250x Unsupported Format (.tbl)
- `.awk`: 199x Unsupported Format (.awk), 37x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.ok`: 135x Excluded: Neighborhood Micro-Mass Limit Exceeded, 94x Unsupported Format (.ok), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.descrip`: 227x Unsupported Format (.descrip), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.4d`: 212x Unsupported Format (.4d), 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.info`: 200x Unsupported Format (.info), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.3proc`: 152x Unsupported Format (.3proc)
- `.cfg`: 139x Unsupported Format (.cfg)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 29.5 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 42.4 | 52.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 17.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 22.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 20.9 | 4.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 45.7 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 29.7 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 65.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 223898 | 11718 | 14 | `usr/src/uts/common/io/fibre-channel/fca/qlc/ql_api.c` |
| cleanup | 35707 | 5395 | 1 | `usr/src/lib/libscf/common/scf_tmpl.c` |
| guards | 384532 | 20279 | 26 | `usr/src/test/util-tests/tests/demangle/llvm-stdcxxabi.c` |
| danger | 194771 | 12994 | 13 | `usr/src/contrib/ast/src/cmd/INIT/package.sh` |
| concurrency | 8169 | 1606 | 0 | `usr/src/cmd/svc/configd/rc_node.c` |
| connectivity | 284592 | 28114 | 18 | `usr/src/uts/common/nfs/nfs4_kprot.h` |
| io | 47793 | 5181 | 2 | `usr/src/contrib/ast/src/cmd/INIT/package.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 7522 | 1979 | 0 | `usr/src/uts/common/io/pcic.c` |
| time | 4604 | 1402 | 0 | `usr/src/cmd/cron/cron.c` |
| serialization | 175 | 101 | 0 | `usr/src/cmd/ipf/tools/Makefile` |
| regex | 4215 | 842 | 0 | `usr/src/cmd/ypcmd/yp2lscripts/ypmap2src.sh` |
| events | 14251 | 2683 | 0 | `usr/src/lib/libstmf/common/store.c` |
| tests | 2294 | 371 | 0 | `usr/src/cmd/perl/contrib/Sun/Solaris/Lgrp/t/Lgrp.t` |
| docs | 34589 | 4066 | 1 | `usr/src/boot/efi/include/Uefi/UefiPxe.h` |
| debt | 78302 | 7980 | 3 | `usr/src/cmd/cxgbetool/cudbg_view.c` |
| mutation | 2178981 | 24141 | 152 | `usr/src/uts/common/io/fibre-channel/fca/qlc/ql_api.c` |
| dead_code | 71696 | 15156 | 5 | `usr/src/uts/common/os/sunddi.c` |
| credential | 4263 | 47 | 0 | `usr/src/test/util-tests/tests/demangle/llvm-stdcxxabi.c` |
| threat | 80 | 38 | 0 | `usr/src/uts/common/gssapi/mechs/krb5/include/gssapiP_krb5.h` |
| ml_ai | 12220 | 2931 | 0 | `usr/src/uts/common/inet/ip/ip_if.c` |
| ui | 117 | 41 | 0 | `usr/src/cmd/tsol/misc/txzonemgr.sh` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `usr/src/contrib/ast/src/cmd/INIT/package.sh` (Hits: 1343)
- `usr/src/contrib/ast/src/cmd/INIT/iffe.sh` (Hits: 862)
- `usr/src/cmd/ldap/ns_ldap/idsconfig.sh` (Hits: 809)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **types.h** (`usr/src/uts/common/sys/types.h`) — 2522 inbound connections
2. **synch.c** (`usr/src/lib/libc/port/threads/synch.c`) — 2418 inbound connections
3. **Makefile.lib.64** (`usr/src/lib/Makefile.lib.64`) — 1518 inbound connections
4. **sunddi.h** (`usr/src/uts/common/sys/sunddi.h`) — 1430 inbound connections
5. **ddi.h** (`usr/src/uts/common/sys/ddi.h`) — 1238 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **env.c** (`usr/src/boot/efi/libefi/env.c`) — 145 outbound dependencies
2. **startup.c** (`usr/src/uts/i86pc/os/startup.c`) — 96 outbound dependencies
3. **machdep.c** (`usr/src/uts/i86pc/os/machdep.c`) — 91 outbound dependencies
4. **ip.c** (`usr/src/uts/common/inet/ip/ip.c`) — 89 outbound dependencies
5. **ip_input.c** (`usr/src/uts/common/inet/ip/ip_input.c`) — 85 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `soft_build_public_key_object` **(Many-Argument Workhorses)** (@ `usr/src/lib/pkcs11/pkcs11_softtoken/common/softAttributeUtil.c`) -> Impact: **1935.7** | LOC: 2706
  * *Intent:* * - Parse the object's template, and when an error is detected such as * invalid attribute type, invalid attribute value, etc., return * with appropri...
- `soft_build_private_key_object` **(Many-Argument Workhorses)** (@ `usr/src/lib/pkcs11/pkcs11_softtoken/common/softAttributeUtil.c`) -> Impact: **1861.9** | LOC: 2652
  * *Intent:* * - Parse the object's template, and when an error is detected such as * invalid attribute type, invalid attribute value, etc., return * with appropri...
- `sdioctl` **(Many-Argument Workhorses)** (@ `usr/src/uts/common/io/scsi/targets/sd.c`) -> Impact: **1783.5** | LOC: 2862
  * *Intent:* * cred_p - user credential pointer * rval_p - calling process return value (OPT) * * Return Code: EINVAL * ENOTTY * ENXIO * EIO * EFAULT * ENOTSUP * E...
- `projent_parse_attribute_values` **(Many-Argument Workhorses)** (@ `usr/src/cmd/perl/contrib/Sun/Solaris/Project/Project.pm`) -> Impact: **1764.3** | LOC: 1349
  * *Intent:* # # projent_parse_attribute_values(values) # # Values is the right hand side of a name=values attribute/values pair. # This function parses the values...
- `strioctl` **(Many-Argument Workhorses)** (@ `usr/src/uts/common/os/streamio.c`) -> Impact: **1654.1** | LOC: 2534
  * *Intent:* /* * ioctl for streams */
- `iscsi_ioctl` **(Many-Argument Workhorses)** (@ `usr/src/uts/common/io/scsi/adapters/iscsi/iscsi.c`) -> Impact: **1473.8** | LOC: 3124
  * *Intent:* /* * iscsi_ioctl - */ /* ARGSUSED */
- `dtrace_disx86` **(Many-Argument Workhorses)** (@ `usr/src/common/dis/i386/dis_tables.c`) -> Impact: **1472.6** | LOC: 3056
  * *Intent:* /* * Dissassemble a single x86 or amd64 instruction. * * Mode determines the default operating mode (SIZE16, SIZE32 or SIZE64) * for interpreting inst...
- `tmxdate` **(Many-Argument Workhorses)** (@ `usr/src/contrib/ast/src/lib/libast/tm/tmxdate.c`) -> Impact: **1433.5** | LOC: 1590
  * *Intent:* #define K1(c1) (c1) #define K2(c1,c2) (((c1)<<8)|(c2)) #define K3(c1,c2,c3) (((c1)<<16)|((c2)<<8)|(c3)) #define K4(c1,c2,c3,c4) (((c1)<<24)|((c2)<<16)...
- `sqliteVdbeExec` **(Many-Argument Workhorses)** (@ `usr/src/lib/libsqlite/src/vdbe.c`) -> Impact: **1425.1** | LOC: 4433
  * *Intent:* ** The error code is stored in p->rc and this routine returns SQLITE_ERROR. ** ** If the callback ever returns non-zero, then the program exits ** imm...
- `sadb_common_add` **(Many-Argument Workhorses)** (@ `usr/src/uts/common/inet/ip/sadb.c`) -> Impact: **1422.7** | LOC: 2278
  * *Intent:* * SAs can be "inbound", "outbound", or "both". The "primary" and "secondary" * hash bucket parameters are set in order of what the SA will be most of ...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `usr/src/uts/common/os` | 177 | 163121.66 | 67.32% | 47.46% |
| `usr/src/uts/common/fs/nfs` | 58 | 107034.22 | 71.73% | 39.9% |
| `usr/src/uts/common/io` | 121 | 105649.92 | 63.36% | 33.72% |
| `usr/src/uts/common/inet/ip` | 60 | 101369.88 | 59.53% | 37.46% |
| `usr/src/uts/common/fs/zfs` | 120 | 96870.36 | 60.56% | 37.54% |
| `usr/src/uts/common/io/fibre-channel/fca/emlxs` | 23 | 73134.96 | 75.21% | 20.62% |
| `usr/src/cmd/sendmail/src` | 50 | 70202.38 | 62.96% | 24.31% |
| `usr/src/lib/libdwarf/common` | 168 | 52300.28 | 26.47% | 22.97% |
| `usr/src/uts/common/io/fibre-channel/fca/qlc` | 20 | 51000.28 | 38.1% | 13.4% |
| `usr/src/uts/sun4v/io` | 45 | 45673.92 | 69.96% | 19.37% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `usr/src/contrib/ast/src/lib/libpp/pp.def` -> **100.0%** Exposure
- `usr/src/cmd/ipf/lib/genmask.c` -> **100.0%** Exposure
- `usr/src/cmd/mdb/common/libstandctf/ctf_subr.c` -> **100.0%** Exposure
- `usr/src/common/atomic/atomic.c` -> **100.0%** Exposure
- `usr/src/common/tsol/blabel.c` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `usr/src/boot/forth/Makefile` -> **100.0%** Exposure
- `usr/src/cmd/fm/modules/common/eversholt/Makefile` -> **100.0%** Exposure
- `usr/src/cmd/fm/modules/common/fabric-xlate/Makefile` -> **100.0%** Exposure
- `usr/src/cmd/fm/modules/common/sw-diag-response/software-diagnosis/Makefile` -> **100.0%** Exposure
- `usr/src/cmd/fs.d/smbclnt/fksmbcl/Makefile` -> **100.0%** Exposure
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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `399` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `161322` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `usr/src/uts/common/io/fibre-channel/fca/qlc/ql_api.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.671)
- **Top Global Matches:** file_cluster_8: 9.671, file_cluster_6: 13.118, file_cluster_4: 21.023
- **Magnitude:** 19567.26 | **LOC:** 22988 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **11**; blast radius 0.017; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ql_83xx_ascii_fw_dump` **(Many-Argument Workhorses)** (Impact: 492.8)
    * *Intent:* /* * ql_83xx_ascii_fw_dump * Converts ISP83xx firmware binary dump to ascii. * * Input: * ha = adapt...
  * `ql_attach` **(Many-Argument Workhorses)** (Impact: 329.5)
    * *Intent:* * ql_attach * Configure and attach an instance of the driver * for a port. * * Input: * dip = pointe...
  * `ql_port_manage` **(Many-Argument Workhorses)** (Impact: 292.1)
    * *Intent:* * Perform port management or diagnostics. * * Input: * fca_handle = handle setup by ql_bind_port(). ...
  * `ql_25xx_ascii_fw_dump` **(Many-Argument Workhorses)** (Impact: 181.4)
    * *Intent:* /* * ql_25xx_ascii_fw_dump * Converts ISP25xx firmware binary dump to ascii. * * Input: * ha = adapt...
  * `ql_81xx_ascii_fw_dump` **(Many-Argument Workhorses)** (Impact: 181.4)
    * *Intent:* /* * ql_81xx_ascii_fw_dump * Converts ISP81xx firmware binary dump to ascii. * * Input: * ha = adapt...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3805 instances
* *State Mutation (weighted view):* 12357
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3068`, `structural_boundaries: 1957`, `args: 510`, `func_start: 215`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 612`, `state_mutation: 4747`, `fragile_debt: 3`, `unreferenced_by_name: 14`
* *Architecture:* `api: 81`, `import: 11`
* *Defense:* `safety: 187`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 31):` ql_api.h, ql_apps.h, ql_debug.h, ql_fm.h, ql_init.h, ql_iocb.h, ql_ioctl.h, ql_isr.h...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/io/scsi/targets/sd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.04)
- **Top Global Matches:** file_cluster_8: 10.04, file_cluster_6: 12.033, file_cluster_4: 19.609
- **Magnitude:** 17904.8 | **LOC:** 31270 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.01; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.8%), Guard Balance (formerly Safety Score) (71.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sdioctl` **(Many-Argument Workhorses)** (Impact: 1783.5)
    * *Intent:* * cred_p - user credential pointer * rval_p - calling process return value (OPT) * * Return Code: EI...
  * `sd_start_cmds` **(Many-Argument Workhorses)** (Impact: 682.7)
    * *Intent:* * Description: Remove and transport cmds from the driver queues. * * Arguments: un - pointer to the ...
  * `sd_unit_attach` **(Many-Argument Workhorses)** (Impact: 276.1)
    * *Intent:* * * Description: Performs DDI_ATTACH processing for sdattach(). Allocates * the soft state structure...
  * `sddump` **(Many-Argument Workhorses)** (Impact: 168.0)
    * *Intent:* #define SD_NDUMP_RETRIES 12 /* * System Crash Dump routine */
  * `sd_retry_command` **(Many-Argument Workhorses)** (Impact: 152.6)
    * *Intent:* * failure_code - errno return code to set in the bp if the * command is going to be failed. * * retr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2386 instances
* *State Mutation (weighted view):* 7821
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3329`, `structural_boundaries: 2836`, `args: 2054`, `func_start: 272`, `class_start: 503`
* *Risk/State:* `safety_bypasses: 127`, `high_risk_execution: 1`, `state_mutation: 3049`, `dead_code: 2`, `planned_debt: 20`, `fragile_debt: 11`
* *Architecture:* `api: 22`, `import: 29`
* *Defense:* `safety: 88`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 58):` sd_xbuf.h, aio_req.h, byteorder.h, cdio.h, cmlb.h, dkbad.h, dkio.h, dkioc_free_util.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/dtrace/dtrace.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.247)
- **Top Global Matches:** file_cluster_6: 6.247, file_cluster_4: 11.736, file_cluster_8: 14.123
- **Magnitude:** 15433.52 | **LOC:** 17435 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **29**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.7%), Guard Balance (formerly Safety Score) (80.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dtrace_dif_subr` **(Many-Argument Workhorses)** (Impact: 985.8)
    * *Intent:* /* * Emulate the execution of DTrace ID subroutines invoked by the call opcode. * Notice that we don...
  * `dtrace_difo_validate` **(Many-Argument Workhorses)** (Impact: 512.3)
    * *Intent:* /* * Validate a DTrace DIF object by checking the IR instructions. The following * rules are current...
  * `dtrace_dif_emulate` **(Many-Argument Workhorses)** (Impact: 418.7)
    * *Intent:* /* * Emulate the execution of DTrace IR instructions specified by the given * DIF object. This funct...
  * `dtrace_ioctl` **(Many-Argument Workhorses)** (Impact: 339.5)
    * *Intent:* /*ARGSUSED*/
  * `dtrace_probe` **(Many-Argument Workhorses)** (Impact: 329.3)
    * *Intent:* /* * If you're looking for the epicenter of DTrace, you just found it. This * is the function called...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2516 instances
* *State Mutation (weighted view):* 7861
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2868`, `structural_boundaries: 1541`, `args: 503`, `func_start: 227`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 122`, `state_mutation: 2829`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 25`, `import: 29`
* *Defense:* `safety: 117`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 41):` in.h, strtolctype.h, atomic.h, cmn_err.h, conf.h, cpuvar.h, cred_impl.h, ctf_api.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `usr/src/cmd/svc/svccfg/svccfg_libscf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.856)
- **Top Global Matches:** file_cluster_8: 11.856, file_cluster_3: 13.902, file_cluster_6: 23.923
- **Magnitude:** 14843.54 | **LOC:** 17650 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **31**; blast radius 0.014; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `upgrade_dependent` **(Many-Argument Workhorses)** (Impact: 928.6)
    * *Intent:* * - dependency pg in target is corrupt (error printed) * - running snapshot in dependent is missing ...
  * `lscf_service_import` **(Many-Argument Workhorses)** (Impact: 463.4)
    * *Intent:* * - instance added unexpectedly (error printed) * - instance deleted unexpectedly (error printed) * ...
  * `process_old_pg` **(Many-Argument Workhorses)** (Impact: 419.5)
    * *Intent:* * - couldn't upgrade dependents (backend access denied) * - couldn't import pg (backend access denie...
  * `upgrade_dependents` **(Many-Argument Workhorses)** (Impact: 397.7)
    * *Intent:* * - couldn't create dependent (repository read-only) * EACCES - could not modify dependents pg (back...
  * `lscf_instance_import` **(Many-Argument Workhorses)** (Impact: 320.3)
    * *Intent:* * EINVAL - invalid instance name (error printed) * - invalid pgroup_t's (error printed) * - invalid ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 156 instances
* *Amplified Cascading Flux:* 1717 instances
* *High Risk Execution (weighted view):* 7
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 5248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4336`, `structural_boundaries: 1293`, `args: 312`, `func_start: 184`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 55`, `high_risk_execution: 9`, `state_mutation: 1814`, `dead_code: 1`, `planned_debt: 25`, `fragile_debt: 2`, `unreferenced_by_name: 29`
* *Architecture:* `io: 7`, `api: 50`, `import: 31`
* *Defense:* `safety: 93`, `immutability_locks: 263`, `cleanup: 156`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 38):` alloca.h, assert.h, ctype.h, door.h, errno.h, fcntl.h, fnmatch.h, inttypes.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/io/scsi/targets/st.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.105)
- **Top Global Matches:** file_cluster_8: 6.105, file_cluster_6: 13.371, file_cluster_4: 22.083
- **Magnitude:** 14449.96 | **LOC:** 18596 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.014; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.6%), Guard Balance (formerly Safety Score) (78.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `st_decode_sense` **(Many-Argument Workhorses)** (Impact: 440.7)
  * `st_ioctl` **(Many-Argument Workhorses)** (Impact: 343.9)
    * *Intent:* /* * This routine implements the ioctl calls. It is called * from the device switch at normal priori...
  * `st_set_state` **(Many-Argument Workhorses)** (Impact: 238.5)
  * `st_interpret_read_pos` **(Many-Argument Workhorses)** (Impact: 230.5)
    * *Intent:* #define FIX_ENDIAN32(x) st_swap32(x) #define FIX_ENDIAN64(x) st_swap64(x) #endif /* * st_interpret_r...
  * `st_do_mtioctop` **(Many-Argument Workhorses)** (Impact: 228.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2464 instances
* *State Mutation (weighted view):* 7807
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2796`, `structural_boundaries: 1606`, `args: 1417`, `func_start: 191`, `class_start: 169`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 2879`, `planned_debt: 1`, `fragile_debt: 27`, `unreferenced_by_name: 3`
* *Architecture:* `api: 15`, `import: 10`
* *Defense:* `safety: 30`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 29):` byteorder.h, ddi.h, ddidmareq.h, file.h, kstat.h, modctl.h, mtio.h, scsi.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/io/sata/impl/sata.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.944)
- **Top Global Matches:** file_cluster_8: 5.944, file_cluster_6: 12.905, file_cluster_4: 21.676
- **Magnitude:** 14320.3 | **LOC:** 21963 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **27**; blast radius 0.012; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.9%), Complexity Load (formerly Cognitive Load) (75.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sata_hba_ioctl` **(Many-Argument Workhorses)** (Impact: 157.1)
    * *Intent:* * DEVCTL_BUS_GETSTATE * * All other cmds are passed to HBA if it provide ioctl handler, or failed * ...
  * `sata_hba_event_notify` **(Many-Argument Workhorses)** (Impact: 148.4)
    * *Intent:* * Events for different addresses/addr types cannot be combined. * A warning message is generated for...
  * `sata_build_lsense_page_10` **(Many-Argument Workhorses)** (Impact: 123.8)
    * *Intent:* * * Note: Self test and SMART data is accessible in device log pages. * The log pages can be accesse...
  * `sata_dma_buf_setup` **(Many-Argument Workhorses)** (Impact: 122.7)
    * *Intent:* /* * Allocate DMA resources for the buffer * This function handles initial DMA resource allocation a...
  * `sata_txlt_start_stop_unit` **(Compute Cores)** (Impact: 120.4)
    * *Intent:* * SPC-4/SBC-3 SATL ATA power condition SATL SPC/SBC * ----------------------------------------------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2435 instances
* *State Mutation (weighted view):* 8082
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2602`, `structural_boundaries: 1498`, `args: 765`, `func_start: 208`, `class_start: 138`
* *Risk/State:* `safety_bypasses: 151`, `state_mutation: 3212`, `dead_code: 3`, `planned_debt: 3`, `unreferenced_by_name: 12`
* *Architecture:* `api: 28`, `import: 27`
* *Defense:* `safety: 23`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.012
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 45):` cmn_err.h, conf.h, ddi.h, ddifm.h, disp.h, errno.h, file.h, ddi.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/inet/ip/ip_if.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.311)
- **Top Global Matches:** file_cluster_6: 6.311, file_cluster_4: 8.835, file_cluster_12: 16.77
- **Magnitude:** 13903.7 | **LOC:** 19148 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **72**; blast radius 0.019; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.0%), Complexity Load (formerly Cognitive Load) (76.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ip_rt_add` **(Many-Argument Workhorses)** (Impact: 319.0)
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
* *Amplified Cascading Flux:* 2112 instances
* *State Mutation (weighted view):* 6625
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2509`, `structural_boundaries: 1528`, `args: 620`, `func_start: 340`, `class_start: 98`
* *Risk/State:* `safety_bypasses: 197`, `state_mutation: 2401`, `planned_debt: 3`, `fragile_debt: 9`, `unreferenced_by_name: 109`
* *Architecture:* `api: 204`, `import: 72`
* *Defense:* `safety: 21`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 124):` arp.h, common.h, ilb_ip.h, ip.h, ip6.h, ip6_asp.h, ip_arp.h, ip_ftable.h...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/fs/nfs/nfs4_vnops.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.618)
- **Top Global Matches:** file_cluster_8: 5.618, file_cluster_6: 15.714, file_cluster_3: 21.095
- **Magnitude:** 13417.56 | **LOC:** 16007 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **58**; blast radius 0.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nfs4open_otw` **(Many-Argument Workhorses)** (Impact: 462.3)
    * *Intent:* /* * The OPEN operation creates and/or opens a regular file * * ARGSUSED */
  * `nfs4close_one` **(Many-Argument Workhorses)** (Impact: 340.5)
    * *Intent:* * * CLOSE_RESEND and CLOSE_AFTER_RESEND will not attempt to retry after client * recovery. Instead, ...
  * `nfs4_reopen` **(Many-Argument Workhorses)** (Impact: 241.4)
    * *Intent:* * filehandles) may be handled silently by this routine. * - if it is EINTR, ETIMEDOUT, or NFS4_FRC_U...
  * `nfs4frlock` **(Many-Argument Workhorses)** (Impact: 233.1)
    * *Intent:* * * NFS4_LCK_CTYPE_RESEND: same as NFS4_LCK_CTYPE_RECLAIM, with the addition * that we will use the ...
  * `nfs4setattr` **(Many-Argument Workhorses)** (Impact: 205.9)
    * *Intent:* * To replace the "guarded" version 3 setattr, we use two types of compound * setattr requests: * 1. ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1901 instances
* *State Mutation (weighted view):* 6044
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2250`, `structural_boundaries: 802`, `args: 376`, `func_start: 147`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 2242`, `planned_debt: 13`, `fragile_debt: 43`, `unreferenced_by_name: 7`
* *Architecture:* `api: 42`, `import: 58`
* *Defense:* `safety: 42`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 100):` fs_subr.h, lm.h, nfs.h, nfs4.h, nfs4_clnt.h, nfs4_kprot.h, nfs_acl.h, nfs_clnt.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/io/fibre-channel/impl/fp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.816)
- **Top Global Matches:** file_cluster_8: 9.816, file_cluster_6: 10.551, file_cluster_4: 18.279
- **Magnitude:** 11466.02 | **LOC:** 15410 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.01; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.2%), Complexity Load (formerly Cognitive Load) (71.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fp_fciocmd` **(Many-Argument Workhorses)** (Impact: 1109.1)
    * *Intent:* /* * One heck of a function to serve userland. */
  * `fp_job_handler` **(Many-Argument Workhorses)** (Impact: 163.5)
    * *Intent:* /* * Dedicated thread to perform various activities. One thread for * each fc_local_port_t (driver s...
  * `fp_ns_reg` **(Many-Argument Workhorses)** (Impact: 155.0)
    * *Intent:* /* * NS Registration function. * * It should be seriously noted that FC-GS-2 currently doesn't suppo...
  * `fp_validate_area_domain` **(Many-Argument Workhorses)** (Impact: 143.6)
    * *Intent:* /* * Handle Domain, Area changes in the Fabric. */
  * `fp_validate_rscn_page` **(Many-Argument Workhorses)** (Impact: 134.0)
    * *Intent:* /* * Work hard to make sense out of an RSCN page. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1951 instances
* *State Mutation (weighted view):* 6456
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1922`, `structural_boundaries: 909`, `args: 390`, `func_start: 134`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 216`, `state_mutation: 2554`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 9`, `import: 28`
* *Defense:* `safety: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 43):` buf.h, byteorder.h, cmn_err.h, conf.h, ddi.h, errno.h, fc.h, fc_fcaif.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/scsi/adapters/mpt_sas/mptsas.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.257)
- **Top Global Matches:** file_cluster_6: 7.257, file_cluster_4: 8.605, file_cluster_12: 16.045
- **Magnitude:** 11270.54 | **LOC:** 17103 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **32**; blast radius 0.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.9%), Guard Balance (formerly Safety Score) (74.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mptsas_do_passthru` **(Many-Argument Workhorses)** (Impact: 241.5)
  * `mptsas_handle_event` **(Many-Argument Workhorses)** (Impact: 197.5)
    * *Intent:* /* * handle events from ioc */
  * `mptsas_scsi_init_pkt` **(Many-Argument Workhorses)** (Impact: 186.0)
    * *Intent:* /* * tran_init_pkt(9E) - allocate scsi_pkt(9S) for command * * One of three possibilities: * - alloc...
  * `mptsas_handle_event_sync` **(Many-Argument Workhorses)** (Impact: 183.0)
    * *Intent:* #define SMP_RESET_IN_PROGRESS MPI2_EVENT_SAS_TOPO_LR_SMP_RESET_IN_PROGRESS /* * handle sync events f...
  * `mptsas_attach` **(Many-Argument Workhorses)** (Impact: 169.0)
    * *Intent:* /* * Notes: * Set up all device state and allocate data structures, * mutexes, condition variables, ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1791 instances
* *State Mutation (weighted view):* 5766
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2044`, `structural_boundaries: 1442`, `args: 627`, `func_start: 253`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 225`, `state_mutation: 2184`, `planned_debt: 4`, `fragile_debt: 3`, `unreferenced_by_name: 7`
* *Architecture:* `api: 30`, `import: 32`
* *Defense:* `safety: 30`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 69):` ddifm.h, file.h, ddi.h, protocol.h, util.h, dv_node.h, model.h, note.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `usr/src/uts/sfmmu/vm/hat_sfmmu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.63)
- **Top Global Matches:** file_cluster_6: 5.63, file_cluster_4: 8.264, file_cluster_16: 16.468
- **Magnitude:** 11260.14 | **LOC:** 15642 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **47**; blast radius 0.018; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.3%), Guard Balance (formerly Safety Score) (77.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sfmmu_tteload_addentry` **(Many-Argument Workhorses)** (Impact: 259.6)
    * *Intent:* /* * Function adds a tte entry into the hmeblk. It returns 0 if successful and 1 * otherwise. */
  * `sfmmu_hblk_alloc` **(Many-Argument Workhorses)** (Impact: 177.1)
    * *Intent:* * (b) if the reserve pool is empty, acquire hblk_reserve_lock * and return hblk_reserve. * * (3) cal...
  * `hat_join_region` **(Many-Argument Workhorses)** (Impact: 175.1)
    * *Intent:* /* * This routine implements the shared context functionality required when * attaching a segment to...
  * `hat_unload_callback` **(Many-Argument Workhorses)** (Impact: 163.7)
  * `sfmmu_hblk_unload` **(Many-Argument Workhorses)** (Impact: 127.3)
    * *Intent:* /* * This function unloads a range of addresses for an hmeblk. * It returns the next address to be u...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1874 instances
* *State Mutation (weighted view):* 5924
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1844`, `structural_boundaries: 1201`, `args: 561`, `func_start: 231`, `class_start: 186`
* *Risk/State:* `safety_bypasses: 60`, `state_mutation: 2176`, `planned_debt: 1`, `fragile_debt: 9`, `unreferenced_by_name: 56`
* *Architecture:* `api: 132`, `import: 47`
* *Defense:* `safety: 48`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 54):` archsystm.h, atomic.h, bitmap.h, callb.h, cmn_err.h, cpu.h, cpu_module.h, cpuvar.h...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/inet/ip/ip.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.795)
- **Top Global Matches:** file_cluster_6: 6.795, file_cluster_8: 12.355, file_cluster_4: 13.566
- **Magnitude:** 10730.24 | **LOC:** 15375 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **40** in-repo importer(s); it depends on **89**; blast radius 0.021; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.7%), Complexity Load (formerly Cognitive Load) (74.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ip_rput_dlpi_writer` **(Many-Argument Workhorses)** (Impact: 367.0)
    * *Intent:* /* * Handling of DLPI messages that require exclusive access to the ipsq. * * Need to do ipsq_pendin...
  * `ip_reassemble` **(Many-Argument Workhorses)** (Impact: 188.6)
    * *Intent:* /* * Handles both IPv4 and IPv6 reassembly - doing the out-of-order cases, * When an ipf is passed h...
  * `ip_xmit` **(Many-Argument Workhorses)** (Impact: 166.5)
    * *Intent:* * * We return an error on failure. In particular we return EWOULDBLOCK * when the driver flow contro...
  * `ip_set_destination_v4` **(Many-Argument Workhorses)** (Impact: 157.2)
    * *Intent:* * Note that we allow connect to broadcast and multicast addresses when * IPDF_ALLOW_MCBC is set. * f...
  * `ip_input_fragment` **(Many-Argument Workhorses)** (Impact: 144.4)
    * *Intent:* /* * Fragmentation reassembly. Each ILL has a hash table for * queuing packets undergoing reassembly...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1705 instances
* *State Mutation (weighted view):* 5506
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1880`, `structural_boundaries: 1116`, `args: 315`, `func_start: 185`, `class_start: 44`
* *Risk/State:* `safety_bypasses: 154`, `state_mutation: 2096`, `planned_debt: 7`, `fragile_debt: 14`, `unreferenced_by_name: 63`
* *Architecture:* `api: 135`, `import: 89`
* *Defense:* `safety: 16`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.021
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 161):` arp.h, cc.h, common.h, ilb_ip.h, ip.h, ip6.h, ip6_asp.h, ip_arp.h...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/io/fibre-channel/ulp/fcp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.198)
- **Top Global Matches:** file_cluster_6: 7.198, file_cluster_8: 10.589, file_cluster_4: 14.851
- **Magnitude:** 10103.7 | **LOC:** 16357 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.01; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.5%), Complexity Load (formerly Cognitive Load) (72.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fcp_port_ioctl` **(Many-Argument Workhorses)** (Impact: 331.7)
    * *Intent:* /* * called for ioctls on the transport's devctl interface, and the transport * has passed it to us ...
  * `fcp_complete_pkt` **(Many-Argument Workhorses)** (Impact: 139.1)
  * `fcp_send_scsi_ioctl` **(Many-Argument Workhorses)** (Impact: 138.9)
    * *Intent:* * * Returns: * 0 = OK * EAGAIN = See errno.h * EBUSY = See errno.h * EINTR = See errno.h * EINVAL = ...
  * `fcp_handle_devices` **(Many-Argument Workhorses)** (Impact: 138.9)
    * *Intent:* * * Argument: *pptr Fcp port structure. * *devlist Pointer to the first entry of a table * containin...
  * `fcp_setup_device_data_ioctl` **(Many-Argument Workhorses)** (Impact: 131.3)
    * *Intent:* * data = ioctl data * mode = See ioctl(9E) * * Output: * data = ioctl data * rval = return value - s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1570 instances
* *State Mutation (weighted view):* 5115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1839`, `structural_boundaries: 1770`, `args: 589`, `func_start: 175`, `class_start: 341`
* *Risk/State:* `safety_bypasses: 93`, `state_mutation: 1975`, `fragile_debt: 8`, `unreferenced_by_name: 3`
* *Architecture:* `api: 16`, `import: 22`
* *Defense:* `safety: 9`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 40):` byteorder.h, console.h, ctype.h, devctl.h, fc.h, fc_ulpif.h, fcpvar.h, file.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/bnxe/577xx/common/bnxe_clc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.986)
- **Top Global Matches:** file_cluster_4: 6.986, file_cluster_6: 7.443, file_cluster_16: 13.943
- **Magnitude:** 9995.8 | **LOC:** 15674 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **27**; blast radius 0.023; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.8%), Complexity Load (formerly Cognitive Load) (64.8%)
- **Documentation Coverage:** 85.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `elink_set_led` **(Many-Argument Workhorses)** (Impact: 101.5)
    * *Intent:* #endif /* EXCLUDE_XGXS */
  * `elink_link_update` **(Many-Argument Workhorses)** (Impact: 90.6)
    * *Intent:* /* The elink_link_update function should be called upon link * interrupt. * Link is considered up as...
  * `elink_populate_ext_phy` **(Many-Argument Workhorses)** (Impact: 89.1)
    * *Intent:* #ifndef ELINK_EMUL_ONLY
  * `elink_848x3_config_init` **(Many-Argument Workhorses)** (Impact: 83.2)
    * *Intent:* #endif /* #ifndef EXCLUDE_WARPCORE */ #if !defined(EXCLUDE_BCM8481) || !defined(EXCLUDE_BCM84833) #d...
  * `elink_get_link_speed_duplex` **(Many-Argument Workhorses)** (Impact: 81.3)
    * *Intent:* #endif /* EXCLUDE_XGXS */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1445 instances
* *State Mutation (weighted view):* 4613
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1917`, `structural_boundaries: 1635`, `args: 436`, `func_start: 300`, `class_start: 451`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1723`, `fragile_debt: 3`, `unreferenced_by_name: 30`
* *Architecture:* `api: 41`, `import: 28`
* *Defense:* `doc: 82`, `immutability_locks: 90`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 17):` 57712_reg.h, aeu_inputs.h, inet.h, byteorder.h, bcmtype.h, bigmac_addresses.h, clc.h, clc_reg.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/io/comstar/port/qlt/qlt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.909)
- **Top Global Matches:** file_cluster_6: 6.909, file_cluster_8: 12.743, file_cluster_4: 13.478
- **Magnitude:** 9930.68 | **LOC:** 10798 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.01; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `qlt_attach` **(Many-Argument Workhorses)** (Impact: 281.0)
  * `qlt_firmware_dump` **(Many-Argument Workhorses)** (Impact: 225.2)
    * *Intent:* /* * All QLT_FIRMWARE_* will mainly be handled in this function * It can not be called in interrupt ...
  * `qlt_ioctl` **(Many-Argument Workhorses)** (Impact: 191.2)
    * *Intent:* /* * All of these ioctls are unstable interfaces which are meant to be used * in a controlled lab en...
  * `qlt_isr` **(Many-Argument Workhorses)** (Impact: 158.6)
    * *Intent:* /* * **SHOULD ONLY BE CALLED FROM INTERRUPT CONTEXT. DO NOT CALL ELSEWHERE** */ /* ARGSUSED */
  * `qlt_msix_default_handler` **(Many-Argument Workhorses)** (Impact: 149.0)
    * *Intent:* /* * **SHOULD ONLY BE CALLED FROM INTERRUPT CONTEXT. DO NOT CALL ELSEWHERE** */ /* ARGSUSED */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1721 instances
* *State Mutation (weighted view):* 6159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1548`, `structural_boundaries: 772`, `args: 425`, `func_start: 137`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 200`, `state_mutation: 2717`, `dead_code: 6`, `fragile_debt: 16`, `unreferenced_by_name: 5`
* *Architecture:* `api: 68`, `import: 21`
* *Defense:* `safety: 146`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 33):` qlt.h, qlt_dma.h, qlt_ioctl.h, qlt_open.h, atomic.h, byteorder.h, conf.h, cred.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/io/fibre-channel/fca/qlc/ql_xioctl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.252)
- **Top Global Matches:** file_cluster_8: 6.252, file_cluster_6: 12.651, file_cluster_4: 21.387
- **Magnitude:** 9859.4 | **LOC:** 10723 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **9**; blast radius 0.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ql_scsi_passthru` **(Many-Argument Workhorses)** (Impact: 308.0)
    * *Intent:* * ql_scsi_passthru * IOCTL SCSI passthrough. * * Input: * ha: adapter state pointer. * cmd: User spa...
  * `ql_setup_flash` **(Compute Cores)** (Impact: 176.0)
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
* *Structure:* `branch: 1538`, `structural_boundaries: 906`, `args: 286`, `func_start: 106`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 85`, `state_mutation: 2279`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 14`, `import: 9`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 17):` ql_api.h, ql_apps.h, ql_debug.h, ql_init.h, ql_iocb.h, ql_ioctl.h, ql_mbx.h, ql_nx.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `usr/src/lib/pkcs11/pkcs11_softtoken/common/softAttributeUtil.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 12.936)
- **Top Global Matches:** file_cluster_3: 12.936, file_cluster_8: 13.486, file_cluster_6: 25.589
- **Magnitude:** 9333.08 | **LOC:** 7094 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **16**; blast radius 0.016; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `soft_build_public_key_object` **(Many-Argument Workhorses)** (Impact: 1935.7)
    * *Intent:* * - Parse the object's template, and when an error is detected such as * invalid attribute type, inv...
  * `soft_build_private_key_object` **(Many-Argument Workhorses)** (Impact: 1861.9)
    * *Intent:* * - Parse the object's template, and when an error is detected such as * invalid attribute type, inv...
  * `soft_find_match_attrs` **(Many-Argument Workhorses)** (Impact: 583.8)
  * `soft_build_secret_key_object` **(Many-Argument Workhorses)** (Impact: 510.9)
    * *Intent:* * invalid attribute type, invalid attribute value, etc., return * with appropriate return value. * -...
  * `soft_get_private_key_attribute` **(Many-Argument Workhorses)** (Impact: 144.6)
    * *Intent:* /* * Get the value of a requested attribute of a Private Key Object. * * Rule: All the attributes in...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 31 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 771 instances
* *Concurrency (weighted view):* 12
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 2325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1623`, `structural_boundaries: 858`, `args: 275`, `func_start: 60`
* *Risk/State:* `safety_bypasses: 142`, `state_mutation: 783`, `unreferenced_by_name: 18`
* *Architecture:* `api: 51`, `concurrency: 2`, `import: 16`
* *Defense:* `safety: 12`, `sync_locks: 2`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 18):` aes_impl.h, arcfour.h, bignum.h, blowfish_impl.h, des_impl.h, rsa_impl.h, cryptoki.h, softCrypt.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/vm/seg_vn.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.497)
- **Top Global Matches:** file_cluster_3: 6.497, file_cluster_8: 19.616, file_cluster_6: 32.501
- **Magnitude:** 9149.16 | **LOC:** 10343 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.01; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Amplified Cascading Flux:* 1291 instances
* *State Mutation (weighted view):* 3963
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1885`, `structural_boundaries: 827`, `args: 216`, `func_start: 61`, `class_start: 216`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 1381`, `planned_debt: 2`, `fragile_debt: 32`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 33`
* *Defense:* `safety: 130`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 52):` bitmap.h, callb.h, cmn_err.h, cred.h, debug.h, dumphdr.h, errno.h, kmem.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/uts/common/fs/nfs/nfs4_srv.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.303)
- **Top Global Matches:** file_cluster_6: 7.303, file_cluster_8: 9.484, file_cluster_4: 15.371
- **Magnitude:** 8787.92 | **LOC:** 10505 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **46**; blast radius 0.016; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Structure:* `branch: 1449`, `structural_boundaries: 920`, `args: 201`, `func_start: 124`, `class_start: 184`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 1641`, `dead_code: 2`, `fragile_debt: 15`, `unreferenced_by_name: 11`
* *Architecture:* `api: 66`, `import: 46`
* *Defense:* `safety: 9`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 81):` fs_reparse.h, common.h, ip.h, ip6.h, export.h, lm.h, nfs.h, nfs4.h...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/io/fibre-channel/fca/emlxs/emlxs_dfc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.759)
- **Top Global Matches:** file_cluster_8: 9.759, file_cluster_6: 10.978, file_cluster_4: 18.825
- **Magnitude:** 8750.68 | **LOC:** 11112 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 0.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emlxs_dfc_send_mbox` **(Many-Argument Workhorses)** (Impact: 241.3)
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
* *Amplified Cascading Flux:* 1428 instances
* *State Mutation (weighted view):* 4880
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1476`, `structural_boundaries: 732`, `args: 631`, `func_start: 109`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 271`, `state_mutation: 2024`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 13`, `import: 1`
* *Defense:* `safety: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 18):` emlxs.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/io/fibre-channel/fca/emlxs/emlxs_solaris.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.218)
- **Top Global Matches:** file_cluster_6: 7.218, file_cluster_8: 13.176, file_cluster_4: 13.431
- **Magnitude:** 8543.32 | **LOC:** 12434 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **3**; blast radius 0.038; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.0%), Complexity Load (formerly Cognitive Load) (72.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emlxs_fca_port_manage` **(Many-Argument Workhorses)** (Impact: 427.5)
    * *Intent:* } /* emlxs_fca_reset() */
  * `emlxs_fca_bind_port` **(Many-Argument Workhorses)** (Impact: 182.6)
    * *Intent:* /* * emlxs_fca_bind_port * * Arguments: * * dip: the dev_info pointer for the ddiinst * port_info: p...
  * `emlxs_fca_pkt_abort` **(Many-Argument Workhorses)** (Impact: 150.5)
    * *Intent:* } /* emlxs_ub_destroy() */ /*ARGSUSED*/
  * `emlxs_check_parm` **(Many-Argument Workhorses)** (Impact: 146.4)
    * *Intent:* } /* emlxs_get_props() */
  * `emlxs_send_els_rsp` **(Many-Argument Workhorses)** (Impact: 140.8)
    * *Intent:* } /* emlxs_send_els() */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1546 instances
* *State Mutation (weighted view):* 4946
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1484`, `structural_boundaries: 954`, `args: 570`, `func_start: 123`
* *Risk/State:* `safety_bypasses: 207`, `state_mutation: 1854`, `dead_code: 3`, `fragile_debt: 1`, `unreferenced_by_name: 22`
* *Architecture:* `api: 73`, `import: 3`
* *Defense:* `safety: 80`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.038
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 34):` emlxs.h, emlxs_version.h, modctl.h
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/os/streamio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.162)
- **Top Global Matches:** file_cluster_3: 7.162, file_cluster_8: 19.354, file_cluster_6: 32.14
- **Magnitude:** 8430.88 | **LOC:** 8752 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **53**; blast radius 0.02; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `strioctl` **(Many-Argument Workhorses)** (Impact: 1654.1)
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
* *Structure:* `branch: 1645`, `structural_boundaries: 690`, `args: 222`, `func_start: 43`, `class_start: 89`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 1301`, `planned_debt: 1`, `fragile_debt: 9`, `unreferenced_by_name: 15`
* *Architecture:* `api: 29`, `import: 53`
* *Defense:* `safety: 11`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 76):` audit.h, autoconf.h, cmn_err.h, cred.h, debug.h, dld.h, errno.h, file.h...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `usr/src/uts/common/inet/ip/sadb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.779)
- **Top Global Matches:** file_cluster_6: 7.779, file_cluster_4: 11.906, file_cluster_8: 15.824
- **Magnitude:** 8430.56 | **LOC:** 8129 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **42**; blast radius 0.012; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.8%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sadb_common_add` **(Many-Argument Workhorses)** (Impact: 1422.7)
    * *Intent:* * SAs can be "inbound", "outbound", or "both". The "primary" and "secondary" * hash bucket parameter...
  * `sadb_update_sa` **(Many-Argument Workhorses)** (Impact: 153.4)
    * *Intent:* /* * Common code to update an SA. */
  * `sadb_acquire` **(Many-Argument Workhorses)** (Impact: 136.2)
    * *Intent:* /* * For this mblk, insert a new acquire record. Assume bucket contains addrs * of all of the same l...
  * `sadb_sa2msg` **(Many-Argument Workhorses)** (Impact: 135.5)
    * *Intent:* /* * Given an original message header with sufficient space following it, and an * SA, construct a f...
  * `sadb_form_query` **(Many-Argument Workhorses)** (Impact: 130.9)
    * *Intent:* /* * Common function which extracts several PF_KEY extensions for ease of * SADB matching. * * XXX T...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1248 instances
* *State Mutation (weighted view):* 4003
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1155`, `structural_boundaries: 475`, `args: 173`, `func_start: 118`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 152`, `state_mutation: 1507`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 31`, `unreferenced_by_name: 30`
* *Architecture:* `api: 65`, `import: 44`
* *Defense:* `safety: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.012
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 69):` common.h, ip.h, ip6.h, ip_if.h, ip_ire.h, ipclassifier.h, ipdrop.h, ipsec_impl.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `usr/src/cmd/cpio/cpio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.35)
- **Top Global Matches:** file_cluster_8: 6.35, file_cluster_6: 15.492, file_cluster_3: 21.834
- **Magnitude:** 8105.48 | **LOC:** 9761 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.01; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Complexity Load (formerly Cognitive Load) (76.5%)
- **Documentation Coverage:** 99.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup` **(Many-Argument Workhorses)** (Impact: 186.2)
    * *Intent:* /* * setup: Perform setup and initialization functions. Parse the options * using getopt(3C), call c...
  * `gethdr` **(Compute Cores)** (Impact: 183.9)
    * *Intent:* #endif /* * gethdr: Get a header from the archive, validate it and check for the trailer. * Any user...
  * `openout` **(Compute Cores)** (Impact: 162.4)
    * *Intent:* /* * openout: Open files for output and set all necessary information. * If the u option is set (unc...
  * `rstfiles` **(Many-Argument Workhorses)** (Impact: 159.6)
    * *Intent:* /* * rstfiles: Perform final changes to the file. If the -u option is set, * and overwrite == U_OVER...
  * `verbose` **(Compute Cores)** (Impact: 138.1)
    * *Intent:* /* * verbose: For each file, print either the filename (-v) or a dot (-V). * If the -t option (table...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 46 instances
* *Amplified Cascading Flux:* 1440 instances
* *High Risk Execution (weighted view):* 10
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 4375
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2035`, `structural_boundaries: 1002`, `args: 944`, `func_start: 111`, `class_start: 60`
* *Risk/State:* `safety_bypasses: 72`, `high_risk_execution: 12`, `state_mutation: 1495`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 81`, `api: 30`, `import: 37`
* *Defense:* `safety: 51`, `doc: 2`, `immutability_locks: 6`, `cleanup: 85`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.01
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 34):` aclutils.h, attr.h, cpio.h, ctype.h, dirent.h, errno.h, fcntl.h, fnmatch.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/src/cmd/boot/bootadm/bootadm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.212)
- **Top Global Matches:** file_cluster_6: 9.212, file_cluster_8: 10.778, file_cluster_4: 16.45
- **Magnitude:** 8094.86 | **LOC:** 10263 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **44**; blast radius 0.016; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_partition` **(Many-Argument Workhorses)** (Impact: 561.9)
    * *Intent:* #define SECTOR_SIZE 512
  * `get_set_kernel` **(Many-Argument Workhorses)** (Impact: 159.9)
    * *Intent:* /* * Title for an entry to set properties that once went in bootenv.rc. */ #define BOOTENV_RC_TITLE ...
  * `line_parser` **(Many-Argument Workhorses)** (Impact: 140.8)
    * *Intent:* /* * A line in menu.lst looks like * [ ]*<cmd>[ \t=]*<arg>* */
  * `bam_menu` **(Many-Argument Workhorses)** (Impact: 124.6)
  * `find_boot_entry` **(Many-Argument Workhorses)** (Impact: 124.3)
    * *Intent:* /* * look for matching bootadm entry with specified parameters * Here are the rules (based on existi...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 138 instances
* *Amplified Cascading Flux:* 1204 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 3678
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1599`, `structural_boundaries: 1124`, `args: 373`, `func_start: 166`, `class_start: 75`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 2`, `state_mutation: 1270`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 101`, `api: 44`, `import: 44`
* *Defense:* `safety: 251`, `test: 1`, `immutability_locks: 98`, `cleanup: 205`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 49):` alloca.h, bootadm.h, ctype.h, deflt.h, device_info.h, dirent.h, errno.h, fcntl.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `usr/src/lib/libm/i386/src/expl.S` (ASSEMBLY) | Magnitude: 24.74 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 76, pointers: 22, args: 21, structural_boundaries: 12
- `usr/src/lib/scsi/plugins/ses/libses/common/libses.c` (C) | Magnitude: 22.54 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 23, pointers: 10, structural_boundaries: 7, branch: 4
- `usr/src/uts/sparc/v9/ml/lock_prim.S` (ASSEMBLY) | Magnitude: 75.84 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 346, structural_boundaries: 61, pointers: 45, concurrency: 25
- `usr/src/tools/smatch/src/smatch_start_states.c` (C) | Magnitude: 0.02 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 14, pointers: 14, indent_tabs: 12, encapsulation: 7
- `usr/src/lib/libnsl/nss/gethostent6.c` (C) | Magnitude: 23.42 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 20, indent_tabs: 17, structural_boundaries: 10, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `usr/src/cmd/sgs/libconv/common/lddstub.c` (C) | Magnitude: 53.08 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 33, branch: 15, structural_boundaries: 9, args: 9
- `usr/src/lib/gss_mechs/mech_krb5/krb5/ccache/cc_memory.c` (C) | Magnitude: 461.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 259, pointers: 225, indent_tabs: 103, state_mutation: 89
- `usr/src/cmd/sqlite/Makefile` (MAKEFILE) | Magnitude: 9.96 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 6, indent_tabs: 6, core_var_decl: 6, design_upper_case: 6
- `usr/src/lib/libsldap/common/ns_cache_door.c` (C) | Magnitude: 109.58 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 79, pointers: 30, structural_boundaries: 24, state_mutation: 24
- `usr/src/lib/libwrap/percent_m.c` (C) | Magnitude: 26.98 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: pointers: 8, state_mutation: 5, branch: 4, globals: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `usr/src/cmd/perl/contrib/Sun/Solaris/Task/pod/Task.pod` (PERL) | Magnitude: 0.16 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 15, decorators: 7, bitwise_ops: 7, io: 4
- `usr/src/lib/libslp/javalib/com/sun/slp/ServiceLocationAttributeDescriptor.java` (JAVA) | Magnitude: 22.28 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 11, doc: 11, args: 10, func_start: 10
- `usr/src/lib/libdtrace_jni/java/src/org/opensolaris/os/dtrace/AggregationValue.java` (JAVA) | Magnitude: 3.18 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, api: 2, doc: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `usr/src/lib/libpkg/common/pkgstr.c` (C) | Magnitude: 399.8 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 356, pointers: 118, explicit_casts: 87, safety_bypasses: 79
- `usr/src/cmd/sgs/link_audit/common/mach.h` (C) | Magnitude: 16.82 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: macros: 34, pointers: 26, reflection_metaprogramming: 24, safety_bypasses: 8
- `usr/src/cmd/dtrace/test/tst/common/printa/tst.largeusersym.ksh` (SHELL) | Magnitude: 19.94 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 19, structural_boundaries: 16, io: 9, safety_bypasses: 7
- `usr/src/tools/scripts/protocmp.terse.sh` (SHELL) | Magnitude: 4.1 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 47, structural_boundaries: 19, branch: 10, safety_bypasses: 10
- `usr/src/head/iso/stdlib_iso.h` (CPP) | Magnitude: 8.44 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 45, macros: 39, pointers: 35, args: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `usr/src/lib/gss_mechs/mech_krb5/krb5/keytab/ktbase.c` (C) | Magnitude: 174.24 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 87, pointers: 71, state_mutation: 32, structural_boundaries: 31
- `usr/src/lib/libsmbfs/smb/acl_print.c` (C) | Magnitude: 28.88 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 33, pointers: 22, import: 21, debug_prints: 13
- `usr/src/uts/sun4v/io/hardclk.c` (C) | Magnitude: 104.04 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 66, structural_boundaries: 25, import: 24, args: 20
- `usr/src/lib/libxcurses2/src/libc/xcurses/whln_st.c` (C) | Magnitude: 57.74 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 22, pointers: 14, state_mutation: 11, branch: 8
- `usr/src/uts/common/exec/shbin/shbin.c` (C) | Magnitude: 117.5 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 101, pointers: 44, structural_boundaries: 35, state_mutation: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `usr/src/cmd/devfsadm/ramdisk_link.c` (C) | Magnitude: 17.86 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 10, import: 9, branch: 5
- `usr/src/cmd/picl/plugins/sun4u/cherrystone/psvcplugin/psvcplugin.c` (C) | Magnitude: 73.9 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 113, structural_boundaries: 23, import: 18, pointers: 16
- `usr/src/cmd/dis/dis_util.c` (C) | Magnitude: 23.7 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 22, structural_boundaries: 12, import: 6, pointers: 6
- `usr/src/contrib/ast/src/lib/libast/comp/nftw.c` (C) | Magnitude: 0.46 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 19, pointers: 14, state_mutation: 10, structural_boundaries: 8
- `usr/src/uts/common/fs/ctfs/ctfs_latest.c` (C) | Magnitude: 55.38 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 62, pointers: 34, import: 17, state_mutation: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `usr/src/lib/libc/port/sys/chmod.c` (C) | Magnitude: 10.54 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: args: 9, macros: 8, import: 7, structural_boundaries: 5
- `usr/src/uts/common/sys/scsi/adapters/mfi/mfi_bbu.h` (C) | Magnitude: 23.98 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 67, structural_boundaries: 8, class_start: 8, api: 7
- `usr/src/cmd/sendmail/libsm/t-scanf.c` (C) | Magnitude: 27.04 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 24, state_mutation: 6, import: 6, core_var_decl: 6
- `usr/src/lib/libc/port/sys/mkdir.c` (C) | Magnitude: 6.78 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: args: 6, import: 4, macros: 4, structural_boundaries: 3
- `usr/src/lib/libc/port/sys/rename.c` (C) | Magnitude: 7.1 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: args: 6, import: 5, macros: 4, pointers: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `usr/src/contrib/ast/src/lib/libast/comp/closelog.c` (C) | Magnitude: 0.19 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 9, scientific: 7, state_mutation: 5, macros: 4
- `usr/src/lib/iconv_modules/ko/common/nbyte_euc.h` (C) | Magnitude: 35.58 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 40, state_mutation: 18, pointers: 15, structural_boundaries: 4
- `usr/src/lib/libxcurses/src/libc/mks/m_malloc.c` (C) | Magnitude: 18.5 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 11, macros: 7, branch: 3, structural_boundaries: 3
- `usr/src/uts/common/syscall/umask.c` (C) | Magnitude: 4.22 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: import: 8, indent_tabs: 4, pointers: 2, structural_boundaries: 1
- `usr/src/cmd/sort/Makefile` (MAKEFILE) | Magnitude: 25.56 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 36, structural_boundaries: 21, core_var_decl: 15, design_upper_case: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_3
- `usr/src/contrib/ast/src/lib/libast/misc/optget.c` (C) | Magnitude: 99.44 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 4914, branch: 2194, state_mutation: 1585, pointers: 888

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `usr/src/cmd/fs.d/fsck.c` (C) | Magnitude: 833.38 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 603, branch: 193, state_mutation: 145, pointers: 140
- `usr/src/lib/libxcurses2/src/libc/xcurses/slk.c` (C) | Magnitude: 350.56 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 220, pointers: 74, branch: 64, state_mutation: 64
- `usr/src/uts/common/io/scsi/adapters/smartpqi/smartpqi_hw.c` (C) | Magnitude: 762.86 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 524, pointers: 489, state_mutation: 193, structural_boundaries: 113
- `usr/src/uts/common/io/pciex/hotplug/pcie_hp.c` (C) | Magnitude: 803.08 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 575, pointers: 236, branch: 166, structural_boundaries: 130
- `usr/src/uts/common/inet/ip/spdsock.c` (C) | Magnitude: 2793.14 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 2115, pointers: 1375, state_mutation: 548, branch: 477

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `usr/src/lib/libdtrace_jni/java/src/org/opensolaris/os/dtrace/LogLinearDistribution.java` (JAVA) | Magnitude: 130.52 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 134, core_var_decl: 38, state_mutation: 29, design_snake_case: 26
- `usr/src/lib/libdtrace_jni/java/src/org/opensolaris/os/dtrace/LocalConsumer.java` (JAVA) | Magnitude: 758.84 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 373, indent_spaces: 373, structural_boundaries: 273, branch: 140

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `usr/src/cmd/cmd-inet/lib/nwamd/ncu.c` (C) | Magnitude: 1255.08 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1099, pointers: 463, branch: 310, state_mutation: 196
- `usr/src/tools/smatch/src/smatch_ranges.c` (C) | Magnitude: 2.46 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1478, pointers: 667, structural_boundaries: 595, branch: 503
- `usr/src/cmd/audio/utilities/filehdr.c` (C) | Magnitude: 1023.96 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 715, pointers: 275, branch: 198, state_mutation: 179
- `usr/src/uts/i86pc/io/pci/pci_common.c` (C) | Magnitude: 1651.6 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 965, pointers: 440, branch: 317, state_mutation: 287
- `usr/src/lib/libxcurses2/src/libc/xcurses/wgetn_ws.c` (C) | Magnitude: 185.54 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 140, structural_boundaries: 51, state_mutation: 40, pointers: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `usr/src/uts/common/crypto/io/dca_debug.c` (C) | Magnitude: 0.22 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 24, pointers: 11, structural_boundaries: 7, import: 6
- `usr/src/uts/common/inet/rawip_impl.h` (CPP) | Magnitude: 16.14 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 16, structural_boundaries: 12, pointers: 12, import: 9
- `usr/src/lib/fm/topo/maps/SMCI,SSG-2028R-ACR24L/SSG-2028R-ACR24L-disk-hc-topology.xmlgenksh` (SHELL) | Magnitude: 40.04 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: io: 94, indent_spaces: 57, core_var_decl: 42, design_snake_case: 42
- `usr/src/cmd/sendmail/db/xa/xa_db.c` (C) | Magnitude: 140.8 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 142, pointers: 129, state_mutation: 47, structural_boundaries: 26
- `usr/src/lib/libc/port/i18n/gettext.c` (C) | Magnitude: 60.68 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 90, core_var_decl: 34, design_snake_case: 34, pointers: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `usr/src/cmd/cmd-inet/lib/ipmgmtd/ipmgmt_persist.c` (C) | Magnitude: 1933.44 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 1060, pointers: 567, branch: 406, state_mutation: 277
- `usr/src/cmd/awk_xpg4/awk1.c` (C) | Magnitude: 1839.8 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 1071, branch: 395, state_mutation: 387, pointers: 250
- `usr/src/lib/libkmf/libkmf/common/certop.c` (C) | Magnitude: 2935.64 | Delta: **0.146** (centroid distance) | Secondary Pull: `file_cluster_3`
  * Top Architectural Signatures: indent_tabs: 1792, pointers: 637, branch: 605, state_mutation: 457
- `usr/src/cmd/krb5/krb5kdc/kdc_preauth.c` (C) | Magnitude: 2420.98 | Delta: **0.151** (centroid distance) | Secondary Pull: `file_cluster_3`
  * Top Architectural Signatures: pointers: 652, indent_spaces: 609, indent_tabs: 557, state_mutation: 433
- `usr/src/uts/common/io/fibre-channel/fca/emlxs/emlxs_dhchap.c` (C) | Magnitude: 7210.08 | Delta: **0.165** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 4808, pointers: 3243, state_mutation: 1345, branch: 1217

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `usr/src/uts/common/inet/sctp/sctp_misc.c` (C) | Magnitude: 189.84 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 131, pointers: 84, state_mutation: 36, structural_boundaries: 33
- `usr/src/uts/common/fs/tmpfs/tmp_tnode.c` (C) | Magnitude: 210.62 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 158, pointers: 138, state_mutation: 51, import: 27
- `usr/src/cmd/hostname/hostname.c` (C) | Magnitude: 45.42 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 41, branch: 11, structural_boundaries: 11, import: 8
- `usr/src/lib/krb5/kadm5/srv/server_kdb.c` (C) | Magnitude: 224.92 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: pointers: 93, indent_spaces: 91, indent_tabs: 57, state_mutation: 41
- `usr/src/uts/common/io/net80211/net80211_amrr.c` (C) | Magnitude: 82.02 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 51, indent_tabs: 48, state_mutation: 19, branch: 13

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `usr/src/cmd/nvmeadm/nvmeadm_field.c` -> Churn: **74.2%** | Cog Load: 69.0675% | Debt: 8.818%
- `usr/src/uts/common/io/mac/mac_datapath_setup.c` -> Churn: **65.03%** | Cog Load: 76.6708% | Debt: 17.5704%
- `usr/src/cmd/bhyve/common/pci_virtio_scsi.c` -> Churn: **59.96%** | Cog Load: 80.4078% | Debt: 7.9619%
- `usr/src/cmd/nvmeadm/nvmeadm.c` -> Churn: **58.83%** | Cog Load: 55.4286% | Debt: 8.1329%
- `usr/src/cmd/mv/mv.c` -> Churn: **57.94%** | Cog Load: 82.5404% | Debt: 7.996%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `usr/src/cmd/svc/svccfg/svccfg_libscf.c` -> **Toomas Soome** (100.0% isolated ownership) | Magnitude: 14843.54
- `usr/src/uts/common/fs/nfs/nfs4_vnops.c` -> **Toomas Soome** (100.0% isolated ownership) | Magnitude: 13417.56
- `usr/src/uts/common/inet/ip/ip.c` -> **Toomas Soome** (100.0% isolated ownership) | Magnitude: 10730.24
- `usr/src/uts/common/io/fibre-channel/fca/emlxs/emlxs_dfc.c` -> **Toomas Soome** (100.0% isolated ownership) | Magnitude: 8750.68
- `usr/src/uts/common/io/fibre-channel/fca/emlxs/emlxs_solaris.c` -> **Toomas Soome** (100.0% isolated ownership) | Magnitude: 8543.32

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `usr/src/contrib/ast/src/cmd/ksh93/tests/grep.sh` -> **Severity: 512.2** (Blast Radius: 5.122 * Doc Risk: 100.0%)
- `usr/src/contrib/ast/src/cmd/ksh93/tests/functions.sh` -> **Severity: 408.2** (Blast Radius: 4.082 * Doc Risk: 100.0%)
- `usr/src/uts/Makefile.uts` -> **Severity: 384.6** (Blast Radius: 3.846 * Doc Risk: 100.0%)
- `usr/src/lib/libc/port/threads/synch.c` -> **Severity: 299.5** (Blast Radius: 2.995 * Doc Risk: 100.0%)
- `usr/src/cmd/initpkg/umountall.sh` -> **Severity: 297.4** (Blast Radius: 2.974 * Doc Risk: 100.0%)

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 67845 literal sites + 2339 sites through wrappers = 70184
- **`memory_alloc`:** 35720 literal sites + 47310 sites through wrappers = 83030
- **`panics_and_aborts`:** 19894 literal sites + 1601 sites through wrappers = 21495

- `free` (macro, memory_alloc, primitive): 22569 call sites in 3312 files -- `usr/src/boot/libsa/stand.h`
- `malloc` (macro, memory_alloc, primitive): 6838 call sites in 2424 files -- `usr/src/boot/libsa/stand.h`
- `realloc` (macro, memory_alloc, primitive): 947 call sites in 598 files -- `usr/src/boot/libsa/stand.h`
- `krb5_xfree` (macro, memory_alloc, primitive): 383 call sites in 77 files -- `usr/src/uts/common/gssapi/mechs/krb5/include/krb5.h`
- `FREE` (macro, memory_alloc, primitive): 382 call sites in 73 files -- `usr/src/cmd/audio/include/libaudio_impl.h`
- `S_FREE` (macro, memory_alloc, primitive): 326 call sites in 21 files -- `usr/src/cmd/cfgadm/cfgadm.c`
- `di_devfs_path_free` (function, memory_alloc, primitive): 313 call sites in 84 files -- `usr/src/lib/libdevinfo/devinfo.c`
- `MALLOC` (macro, memory_alloc, primitive): 295 call sites in 67 files -- `usr/src/cmd/audio/include/libaudio_impl.h`
- `newof` (macro, memory_alloc, primitive): 263 call sites in 115 files -- `usr/src/contrib/ast/src/cmd/INIT/mamake.c`
- `NSLDAPI_FREE` (macro, memory_alloc, via ldap_x_free): 256 call sites in 32 files -- `usr/src/lib/libldap5/sources/ldap/common/ldap-int.h`
- `scf_pg_destroy` (function, memory_alloc, via uu_free): 237 call sites in 51 files -- `usr/src/lib/libscf/common/lowlevel.c`
- `sqliteFree` (function, memory_alloc, primitive): 212 call sites in 27 files -- `usr/src/lib/libsqlite/src/util.c`
*(+2544 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1133209 call pairs -- scoped 16.7%, unique 26.9%, ambiguous 29.2%, external 27.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 1083493 | 16.6% | 27.6% | 30.0% | 25.8% |
| shell | 27608 | 15.9% | 6.4% | 3.3% | 74.4% |
| java | 6937 | 39.4% | 4.6% | 23.8% | 32.3% |
| cpp | 6846 | 17.9% | 17.1% | 37.4% | 27.6% |
| yacc | 3029 | 0.4% | 48.4% | 29.1% | 22.1% |
| perl | 2839 | 22.6% | 0.0% | 0.7% | 76.6% |
| python | 1433 | 24.4% | 0.0% | 5.9% | 69.7% |
| m4 | 480 | 46.9% | 0.6% | 0.0% | 52.5% |
| assembly | 394 | 16.0% | 18.3% | 33.0% | 32.7% |
| tcl | 150 | 6.7% | 0.0% | 0.0% | 93.3% |

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
