# ARCHITECTURAL_BRIEF: MS-DOS
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/microsoft/MS-DOS.git` |
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
| Total Artifacts | 1555 |
| Analyzed Artifacts (Scanned) | 995 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 560 |
| Total LOC | 295339 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 64.0% |
| Dominant Lang | ASSEMBLY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7988 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3449 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.1187 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 78 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 820 | 267058 | 82.4% |
| C | 147 | 27816 | 14.8% |
| PLAINTEXT | 9 | 0 | 0.9% |
| BATCH | 7 | 128 | 0.7% |
| MAKEFILE | 7 | 307 | 0.7% |
| MARKDOWN | 3 | 0 | 0.3% |
| LIVECODE | 2 | 30 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 980 | 98.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 15 | 1.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 560*

**Composition by Extension & Reason:**
- `.asm`: 70x Excluded (Binary Format Detected), 15x Zero-Density Threshold (LOC: 256, Signals: 0), 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 68x Unsupported Format (.undeterminable), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unresolved Ambiguity (No Retainable Structure)
- `.lnk`: 50x Unsupported Format (.lnk), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skl`: 48x Unsupported Format (.skl), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.exe`: 45x Excluded (Explicitly Denied Extension: '.EXE')
- `.com`: 29x Excluded (Binary Format Detected)
- `.md`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lib`: 19x Excluded (Explicitly Denied Extension: '.LIB')
- `.obj`: 18x Excluded (Explicitly Denied Extension: '.OBJ')
- `.equ`: 17x Unsupported Format (.equ)
- `.doc`: 15x Excluded (Explicitly Denied Extension: '.DOC')
- `.bas`: 13x Excluded (Binary Format Detected), 1x Excluded (Unsupported Extension: '.BAS')
- `.inc`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 5603 commas in 802 LOC), 1x Zero-Density Threshold (LOC: 254, Signals: 0)
- `.ext`: 14x Unsupported Format (.ext)
- `.txt`: 12x Excluded (Binary Format Detected)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 81.5 | 7.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 27.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 21.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.6 | 3.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 11.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 64.6 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 44.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 28567 | 538 | 84 | `v4.0/src/DEV/SMARTDRV/SMARTDRV.ASM` |
| cleanup | 8 | 6 | 0 | `v4.0/src/TOOLS/BLD/INC/IO.H` |
| guards | 8424 | 476 | 24 | `v2.0/source/DOSSYM_v211.ASM` |
| danger | 999 | 161 | 1 | `v4.0/src/CMD/BACKUP/BACKUP.C` |
| concurrency | 715 | 157 | 2 | `v1.25/source/ASM.ASM` |
| connectivity | 6701 | 593 | 15 | `v4.0/src/CMD/FDISK/DOSCALL.H` |
| io | 667 | 70 | 0 | `v4.0/src/DEV/XMA2EMS/DIAGS.ASM` |
| crypto | 0 | 0 | 0 | - |
| ipc | 15 | 5 | 0 | `v4.0/src/INC/PDB.INC` |
| time | 20 | 6 | 0 | `v4.0/src/TOOLS/BLD/INC/TIME.H` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 308 | 91 | 0 | `v1.25/source/COMMAND.ASM` |
| tests | 43 | 10 | 0 | `v4.0/src/CMD/RESTORE/RTOLD1.C` |
| docs | 1410 | 93 | 0 | `v4.0/src/CMD/FDISK/DOSCALL.H` |
| debt | 543 | 137 | 1 | `v4.0/src/CMD/BACKUP/BACKUP.C` |
| mutation | 16312 | 482 | 29 | `v4.0/src/CMD/MODE/MODEDEFS.INC` |
| dead_code | 7468 | 507 | 19 | `v4.0/src/DOS/EXTATTR.ASM` |
| credential | 0 | 0 | 0 | - |
| threat | 110 | 24 | 0 | `v4.0/src/CMD/FC/TOOLS.H` |
| ml_ai | 43 | 11 | 0 | `v4.0/src/CMD/FDISK/FDISKMSG.C` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `v4.0/src/DEV/XMA2EMS/DIAGS.ASM` (Hits: 89)
- `v4.0/src/DEV/XMA2EMS/XMA1DIAG.INC` (Hits: 89)
- `v1.25/source/IO.ASM` (Hits: 68)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **DOSSYM.INC** (`v4.0/src/INC/DOSSYM.INC`) — 94 inbound connections
2. **STRUC.INC** (`v4.0/src/INC/STRUC.INC`) — 57 inbound connections
3. **SYSMSG.INC** (`v4.0/src/INC/SYSMSG.INC`) — 45 inbound connections
4. **EXT.INC** (`v4.0/src/SELECT/EXT.INC`) — 29 inbound connections
5. **CASTRUC.INC** (`v4.0/src/SELECT/CASTRUC.INC`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **MEMMINC.ASM** (`v4.0/src/MEMM/MEMM/MEMMINC.ASM`) — 17 outbound dependencies
2. **KEYBCMD.ASM** (`v4.0/src/CMD/KEYB/KEYBCMD.ASM`) — 16 outbound dependencies
3. **STDDATA.ASM** (`v4.0/src/DOS/STDDATA.ASM`) — 16 outbound dependencies
4. **MSDATA.ASM** (`v4.0/src/INC/MSDATA.ASM`) — 16 outbound dependencies
5. **MSDATA2.ASM** (`v4.0/src/INC/MSDATA2.ASM`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `START` (@ `v4.0/src/CMD/SYS/SYS1.ASM`) -> Impact: **312.7** | LOC: 3343
- `main` (@ `v4.0/src/CMD/REPLACE/REPLACE.C`) -> Impact: **240.3** | LOC: 476
  * *Intent:* /* dexit load_msg */ /* dfree parser_prep */ /* display_exit putbyte */ /* display_msg putdword */ /* doadd putword */ /* docopy restore */ /* dodir s...
- `restore_a_file` (@ `v4.0/src/CMD/RESTORE/RTFILE.C`) -> Impact: **209.1** | LOC: 542
  * *Intent:* /* file under the proper path. If the path is not found, build */ /* the path. */ /* It then enter a loop to do reading the source disk and */ /* writ...
- `START` (@ `v4.0/src/CMD/TREE/TREE.ASM`) -> Impact: **184.9** | LOC: 1476
- `valid_input_date` (@ `v4.0/src/CMD/RESTORE/RTT2.C`) -> Impact: **161.6** | LOC: 236
  * *Intent:* /* */ /* EFFECTS: */ /* */ /* INTERNAL REFERENCES: */ /* ROUTINES: */ /* usererror */ /* unexperror */ /* putmsg */ /* set_reset_test_flag */ /* */ /*...
- `check_target_filespec` (@ `v4.0/src/CMD/RESTORE/RESTPARS.C`) -> Impact: **137.2** | LOC: 353
  * *Intent:* /* for user to "Insert diskette for drive %1" */ qregs.x.ax = SETLOGICALDRIVE; /*;AN000;8*/ qregs.h.bl = srcddir[0] - 'A' + 1; /*;AN000;8*/ intdos(&qr...
- `next_level_down` (@ `v4.0/src/CMD/SYS/SYS2.ASM`) -> Impact: **133.5** | LOC: 1083
- `search_src_disk_old` (@ `v4.0/src/CMD/RESTORE/RTOLD.C`) -> Impact: **131.0** | LOC: 219
  * *Intent:* /* cammand line. */ /* */ /* Whenever there is a file found, subroutine filespecmatch */ /* is called to match the file path, and file extension. */ /...
- `dorestore` (@ `v4.0/src/CMD/RESTORE/RTDO.C`) -> Impact: **128.8** | LOC: 313
  * *Intent:* /* 5. Check whether the diskette contains old or new data /* format. /* 6. ouput "file were backup xx-xx-xx" /* /* For each diskette, do the following...
- `findfile_new` (@ `v4.0/src/CMD/RESTORE/RTNEW1.C`) -> Impact: **123.9** | LOC: 201
  * *Intent:* /* /* SUBROUTINE NAME : findfile_new /* /* DESCRIPTIVE NAME : Find a file with matching file name from /* the file CONTROL.xxx. /* /* FUNCTION: For ne...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `v4.0/src/CMD/FDISK` | 38 | 38939.2 | 29.18% | 0.0% |
| `v4.0/src/SELECT` | 63 | 12818.04 | 3.78% | 11.44% |
| `v4.0/src/DOS` | 83 | 7935.54 | 6.84% | 19.29% |
| `v1.25/source` | 7 | 5660.06 | 13.55% | 20.2% |
| `v4.0/src/CMD/COMMAND` | 39 | 5597.36 | 7.21% | 40.69% |
| `v4.0/src/BIOS` | 35 | 4921.8 | 7.86% | 17.68% |
| `v4.0/src/DEV/PRINTER` | 10 | 4777.06 | 13.09% | 22.45% |
| `v4.0/src/INC` | 78 | 4710.9 | 9.63% | 5.85% |
| `v4.0/src/CMD/RESTORE` | 23 | 4001.46 | 18.2% | 36.21% |
| `v4.0/src/MEMM/MEMM` | 57 | 3522.72 | 6.2% | 18.37% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `v4.0/src/DEV/XMAEM/XMAEM.MAK` -> **100.0%** Exposure
- `v2.0/source/MSHEAD.ASM` -> **99.999%** Exposure
- `v4.0/src/INC/MSHEAD.ASM` -> **99.999%** Exposure
- `v4.0/src/DEV/XMAEM/INDEEMU.ASM` -> **99.9953%** Exposure
- `v4.0/src/DEV/XMAEM/INDEI15.ASM` -> **99.9824%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `v4.0/src/BIOS/MSEQU.INC` -> **100.0%** Exposure
- `v4.0/src/CMD/CHKDSK/CHKMSG.INC` -> **100.0%** Exposure
- `v4.0/src/CMD/EXE2BIN/E2BTABLE.INC` -> **100.0%** Exposure
- `v4.0/src/CMD/FORMAT/FORMSG.INC` -> **100.0%** Exposure
- `v4.0/src/CMD/MODE/MODEDEFS.INC` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `v4.0/src/DEV/PRINTER/CPSPM10.ASM` -> **136** Orphaned Functions | **0** Duplicates
- `v4.0/src/CMD/FASTOPEN/FASTINIT.ASM` -> **70** Orphaned Functions | **0** Duplicates
- `v4.0/src/DEV/SMARTDRV/SMARTDRV.ASM` -> **56** Orphaned Functions | **0** Duplicates
- `v4.0/src/DEV/RAMDRIVE/RAMDRIVE.ASM` -> **45** Orphaned Functions | **0** Duplicates
- `v4.0/src/INC/SHELLRD.INC` -> **43** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `80` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2348` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `v4.0/src/DEV/DISPLAY/F-PARSER.INC` (ASSEMBLY) -> Cumulative Risk: **596.22**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 679.74 | **LOC:** 2041 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Dead Code (97.8738%), State Flux (91.6241%)
- **Heaviest Functions:** `NO_CARRY5` (Impact: 14.5), `MATCH_SEARCH` (Impact: 8.8), `FOUND_DO` (Impact: 7.1)

### 2. `v4.0/src/DEV/PRINTER/CPSPM10.ASM` (ASSEMBLY) -> Cumulative Risk: **596.17**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1470.4 | **LOC:** 3852 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.993%), Tech Debt (95.0648%)
- **Heaviest Functions:** `DST_SLTLP` (Impact: 13.0), `DST_BUFNXT` (Impact: 10.2), `DST_BUFLP` (Impact: 9.6)

### 3. `v4.0/src/DOS/IFS.ASM` (ASSEMBLY) -> Cumulative Risk: **593.86**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 76.28 | **LOC:** 524 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Dead Code (99.1647%), Tech Debt (93.3404%)
- **Heaviest Functions:** `chk_al5` (Impact: 5.8), `not_stack` (Impact: 5.1), `chk_al6` (Impact: 4.9)

### 4. `v4.0/src/CMD/FC/FC.C` (C) -> Cumulative Risk: **586.41**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 393.82 | **LOC:** 865 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.8021%)
- **Heaviest Functions:** `compare` (Impact: 28.9), `strcmpis` (Impact: 14.7), `strcmpi` (Impact: 9.4)

### 5. `v4.0/src/BIOS/MSCON.ASM` (ASSEMBLY) -> Cumulative Risk: **583.84**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 88.72 | **LOC:** 329 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (96.9536%), Dead Code (95.8353%)
- **Heaviest Functions:** `ALT_Ext_Chk` (Impact: 6.8), `NOCHR` (Impact: 6.3), `RD_Ext_Chk` (Impact: 6.1)

### 6. `v4.0/src/MEMM/MEMM/MAPDMA.C` (C) -> Cumulative Risk: **582.69**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 289.42 | **LOC:** 425 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.9458%)
- **Heaviest Functions:** `SwapDMAPages` (Impact: 74.8), `GetPteFromIndex` (Impact: 8.0)

### 7. `v4.0/src/CMD/CHKDSK/CHKDSK1.ASM` (ASSEMBLY) -> Cumulative Risk: **565.49**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 178.92 | **LOC:** 682 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Dead Code (94.2776%), State Flux (84.3371%)
- **Heaviest Functions:** `FRAGCHK` (Impact: 9.7), `GotPath` (Impact: 7.5), `RDOK` (Impact: 7.2)

### 8. `v4.0/src/MAPPER/DBCS.ASM` (ASSEMBLY) -> Cumulative Risk: **559.39**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 15.2 | **LOC:** 72 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (97.0688%), State Flux (91.6827%)
- **Heaviest Functions:** `loopx` (Impact: 4.4), `Copy_Vector` (Impact: 1.9), `Exit` (Impact: 1.2)

### 9. `v4.0/src/INC/ERRTST.C` (C) -> Cumulative Risk: **557.15**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 215.78 | **LOC:** 310 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.2394%), Verification (80.0%)
- **Heaviest Functions:** `rootpath` (Impact: 35.1), `fPathErr` (Impact: 23.4), `strbscan` (Impact: 3.9)

### 10. `v4.0/src/CMD/EDLIN/EDLCMD1.ASM` (ASSEMBLY) -> Cumulative Risk: **554.27**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 289.88 | **LOC:** 664 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (92.8096%), State Flux (92.6393%)
- **Heaviest Functions:** `SRCH` (Impact: 10.7), `len_ok` (Impact: 9.9), `EWriteOK` (Impact: 9.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `v4.0/src/SELECT/GET_STAT.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9778.12 | **LOC:** 1217 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.5515%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 168 instances
* *State Mutation (weighted view):* 616
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 62`, `args: 55`, `func_start: 16`, `class_start: 4`
* *Risk/State:* `state_mutation: 280`, `dead_code: 5`
* *Architecture:* `api: 39`, `import: 6`
* *Defense:* `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dos.h, extern.h, get_stat.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/D_MENUS.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5845.18 | **LOC:** 942 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.3454%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 60 instances
* *State Mutation (weighted view):* 240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 25`, `args: 42`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 120`, `dead_code: 1`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, dos.h, extern.h, fdisk.h, fdiskmsg.h, stdio.h, string.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/FDISK.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5802.42 | **LOC:** 1122 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.6723%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 282
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 24`, `args: 33`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 144`
* *Architecture:* `api: 11`, `import: 11`
* *Defense:* `safety: 1`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, dos.h, doscall.h, extern.h, fdisk.h, fdiskmsg.h, msgret.h, process.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/C_MENUS.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5634.04 | **LOC:** 1068 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.3448%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 18`, `args: 38`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 76`, `dead_code: 3`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dos.h, extern.h, fdisk.h, fdiskmsg.h, stdio.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/INPUT.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5558.71 | **LOC:** 674 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.7636%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 251
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 31`, `args: 23`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 109`
* *Architecture:* `api: 8`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, dos.h, doscall.h, extern.h, fdisk.h, fdiskmsg.h, stdio.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/BACKUP/BACKUP.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2476.48 | **LOC:** 4385 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.1302%), Tech Debt (17.887%)
**Top Internal Functions/Classes:**
  * `display_msg` (Impact: 56.7)
    * *Intent:* /************************************************************/
  * `check_path_validity` (Impact: 47.0)
    * *Intent:* sublist.one = 0; /*;AN000;p2592*/ sublist.max_width1 = (BYTE)strlen(t); /*;AN000;p2592*/ sublist.min...
  * `check_date` (Impact: 33.6)
    * *Intent:* else /*;AN000;4*/ display_it (ax,STDERR,1,NOWAIT,(BYTE)PARSEERROR); /*;AN000;6*/ return_code = RETCO...
  * `parser` (Impact: 28.3)
    * *Intent:* dta_addr = (struct FileFindBuf *)&dta; /* Get address of FindFile buffer */ return; /*;AN000;6*/ } /...
  * `see_if_it_should_be_backed_up` (Impact: 27.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 406 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 1393
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 510`, `structural_boundaries: 254`, `args: 143`, `func_start: 92`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 109`, `high_risk_execution: 1`, `state_mutation: 581`, `dead_code: 18`, `fragile_debt: 17`
* *Architecture:* `api: 93`, `import: 10`
* *Defense:* `doc: 203`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` backpars.h, backup.h, direct.h, dos.h, doscalls.h, malloc.h, process.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/DISPLAY.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2250.84 | **LOC:** 407 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.7652%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 25`, `args: 12`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 82`
* *Architecture:* `api: 6`, `import: 8`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, dos.h, doscall.h, extern.h, fdisk.h, fdiskmsg.h, stdio.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/MAIN.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2205.17 | **LOC:** 333 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.3563%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 1`, `args: 17`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 18`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, dos.h, doscall.h, extern.h, fdisk.h, fdiskmsg.h, msgret.h, process.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v1.25/source/ASM.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1825.8 | **LOC:** 4006 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.7765%), Tech Debt (18.9246%)
**Top Internal Functions/Classes:**
  * `NWAIT` (Impact: 29.0)
  * `FACTOR` (Impact: 25.5)
  * `REGCHK` (Impact: 21.9)
  * `GRP3` (Impact: 21.5)
  * `MROPS` (Impact: 19.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 401
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 319`, `structural_boundaries: 1755`, `args: 1914`, `func_start: 477`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 151`, `dead_code: 5`, `fragile_debt: 1`, `unreferenced_by_name: 23`
* *Architecture:* None
* *Defense:* `sync_locks: 47`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.771
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011719
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `v1.25/source/MSDOS.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1710.58 | **LOC:** 4031 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.5999%), Tech Debt (8.8424%)
**Top Internal Functions/Classes:**
  * `SETDATE` (Impact: 16.9)
  * `SMALREC` (Impact: 12.8)
  * `LOAD` (Impact: 12.5)
  * `INCHK` (Impact: 12.4)
  * `GETCH` (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 1820`, `args: 1835`, `func_start: 404`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 141`, `dead_code: 12`, `fragile_debt: 3`
* *Architecture:* `api: 31`
* *Defense:* `sync_locks: 22`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/DEV/SMARTDRV/SMARTDRV.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1684.9 | **LOC:** 7587 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.1528%), Tech Debt (54.3494%)
**Top Internal Functions/Classes:**
  * `pbw$4` (Impact: 23.3)
    * *Intent:* ; ; error exit ;
  * `FIRST_ARG` (Impact: 20.2)
  * `do_it` (Impact: 18.3)
  * `CHECK_SYS` (Impact: 15.1)
  * `GET_AVAIL` (Impact: 13.5)
    * *Intent:* ; ; Allocate drive memory ;
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 75 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 247
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 2077`, `args: 1977`, `func_start: 386`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 1`, `state_mutation: 97`, `dead_code: 61`, `fragile_debt: 8`, `unreferenced_by_name: 56`
* *Architecture:* `io: 21`, `api: 18`, `import: 7`
* *Defense:* `sync_locks: 14`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ab_macro.asm, above.asm, devsym.asm, emm.asm, loadall.asm, mi.asm, syscall.asm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/PROFILE.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1565.09 | **LOC:** 802 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.777%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 378
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 23`, `args: 2`, `func_start: 5`
* *Risk/State:* `state_mutation: 166`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, doscall.h, fdiskc.msg, profile.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/REPLACE/REPLACE.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1533.18 | **LOC:** 2048 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.2423%), Tech Debt (8.3127%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 240.3)
    * *Intent:* /* dexit load_msg */ /* dfree parser_prep */ /* display_exit putbyte */ /* display_msg putdword */ /...
  * `display_msg` (Impact: 97.5)
    * *Intent:* /* outline (string for replacement parm) */ /* */ /* OUTPUT: none */ /* */ /* NORMAL EXIT: The corre...
  * `docopy` (Impact: 89.6)
    * *Intent:* /**/
  * `dodir` (Impact: 38.3)
    * *Intent:* /**/
  * `doadd` (Impact: 23.8)
    * *Intent:* /**/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 194 instances
* *State Mutation (weighted view):* 820
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 140`, `args: 37`, `func_start: 38`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 73`, `high_risk_execution: 1`, `state_mutation: 432`, `dead_code: 4`, `unreferenced_by_name: 1`
* *Architecture:* `api: 42`, `import: 3`
* *Defense:* `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` comsub.h, dos.h, replacep.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/ATTRIB/ATTRIB.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1486.9 | **LOC:** 2686 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.7854%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Parse_it` (Impact: 86.2)
    * *Intent:* /* Output: various control variables are set */ /* */ /* Normal exit: status = NOERROR */ /* */ /* E...
  * `Extended_attrib` (Impact: 56.9)
    * *Intent:* /* Output: none */ /* */ /* Normal exit: */ /* */ /* Error exit: None */ /* */ /* Internal Reference...
  * `Print_ext_attrib` (Impact: 52.3)
    * *Intent:* /* Output: none */ /* */ /* Normal exit: target = source */ /* */ /* Error exit: None */ /* */ /* In...
  * `Do_dir` (Impact: 31.5)
    * *Intent:* /* Output: none */ /* */ /* Normal exit: */ /* */ /* Error exit: None */ /* */ /* Internal Reference...
  * `Special_attrib` (Impact: 22.9)
    * *Intent:* /* Output: none */ /* */ /* Normal exit: */ /* */ /* Error exit: None */ /* */ /* Internal Reference...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 271 instances
* *State Mutation (weighted view):* 1015
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 98`, `args: 19`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 61`, `high_risk_execution: 3`, `state_mutation: 473`, `dead_code: 18`
* *Architecture:* `api: 24`, `import: 7`
* *Defense:* `doc: 80`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` attrib.h, dos.h, io.h, msgret.h, parse.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/DEV/PRINTER/CPSPM10.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1470.4 | **LOC:** 3852 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.8027%), Tech Debt (95.0648%)
**Top Internal Functions/Classes:**
  * `DST_SLTLP` (Impact: 13.0)
  * `DST_BUFNXT` (Impact: 10.2)
    * *Intent:* ;; ;; ;; **** NEXT IN LOOP ****
  * `DST_BUFLP` (Impact: 9.6)
    * *Intent:* ;;
  * `SET_DID` (Impact: 9.4)
    * *Intent:* ;;
  * `COMMON_INTR` (Impact: 9.1)
    * *Intent:* ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; ; ; Common interrupt entry : ; at entry, BUFn (CS:BX) of ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 136 instances
* *State Mutation (weighted view):* 440
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 1365`, `args: 1445`, `func_start: 348`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 168`, `dead_code: 10`, `unreferenced_by_name: 136`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CPSPEQU.INC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/SPACE.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1436.43 | **LOC:** 440 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.1426%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 8`, `args: 5`, `func_start: 4`
* *Risk/State:* `state_mutation: 130`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dos.h, extern.h, fdisk.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/DEV/RAMDRIVE/RAMDRIVE.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1204.82 | **LOC:** 6218 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.9084%), Tech Debt (71.3066%)
**Top Internal Functions/Classes:**
  * `FIRST_ARG` (Impact: 23.8)
  * `CHECK_DOS_VOL` (Impact: 18.0)
    * *Intent:* ; EXIT: ; CARRY SET - error, message already printed ; CARRY CLEAR ; INIT_DRIVE set ; SECTOR_BUFFER ...
  * `GET_AVAIL` (Impact: 16.8)
    * *Intent:* ; ; Allocate drive memory ;
  * `CHECK_SYS` (Impact: 15.1)
  * `FATSUB` (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 33 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 1434`, `args: 1378`, `func_start: 300`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 50`, `dead_code: 111`, `planned_debt: 1`, `fragile_debt: 11`, `unreferenced_by_name: 45`
* *Architecture:* `io: 17`, `import: 8`
* *Defense:* `safety: 3`, `sync_locks: 5`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ab_macro.inc, above.inc, devsym.inc, dirent.inc, emm.inc, loadall.inc, mi.inc, syscall.inc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/CONVERT.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1198.98 | **LOC:** 479 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.4201%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 10`, `args: 10`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 62`
* *Architecture:* `api: 10`, `import: 6`
* *Defense:* `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, dos.h, extern.h, fdisk.h, string.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/DISKOUT.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1186.8 | **LOC:** 355 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.1381%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 184
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 8`, `args: 9`, `func_start: 3`
* *Risk/State:* `state_mutation: 102`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dos.h, extern.h, fdisk.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/VDISPLAY.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1154.21 | **LOC:** 180 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.9628%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 1`, `args: 13`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dos.h, extern.h, fdisk.h, fdiskmsg.h, memory.h, stdio.h, string.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/PARTINFO.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1140.66 | **LOC:** 262 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.8862%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 25`, `args: 12`, `func_start: 10`
* *Risk/State:* `state_mutation: 28`, `dead_code: 6`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dos.h, extern.h, fdisk.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/INC/PCINPUT.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1087.04 | **LOC:** 3795 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.9821%), Tech Debt (20.0616%)
**Top Internal Functions/Classes:**
  * `LF160` (Impact: 12.2)
    * *Intent:* ; buffer ; ; Completed updating LVB, adjust pointers
  * `LS160` (Impact: 12.2)
    * *Intent:* ; buffer ;=W ; ;=W ; Completed updating LVB, adjust pointers ;=W
  * `LF130` (Impact: 11.1)
    * *Intent:* ; ; Byte is a single byte character
  * `LS130` (Impact: 11.1)
    * *Intent:* ; ;=W ; Byte is a single byte character ;=W
  * `LF80` (Impact: 11.0)
    * *Intent:* ; ; Double byte character fits on current row
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 1327`, `args: 1529`, `func_start: 217`
* *Risk/State:* `state_mutation: 79`, `dead_code: 46`, `fragile_debt: 1`, `unreferenced_by_name: 11`
* *Architecture:* `io: 5`
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/INC/SHELLRD.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1062.52 | **LOC:** 5112 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.9728%), Tech Debt (30.7552%)
**Top Internal Functions/Classes:**
  * `BEXIT` (Impact: 38.0)
    * *Intent:* ;
  * `GIEXIT` (Impact: 15.6)
    * *Intent:* ;if in text mode deactivate box ; option ;
  * `PH10` (Impact: 13.5)
    * *Intent:* ; ; display mouse pointer ;
  * `CR_EXIT` (Impact: 10.2)
    * *Intent:* ;
  * `EP370` (Impact: 9.8)
    * *Intent:* ;
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 1869`, `args: 1331`, `func_start: 254`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`, `dead_code: 47`, `unreferenced_by_name: 43`
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FORMAT/FORMAT.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 928.14 | **LOC:** 4509 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.8788%), Tech Debt (26.6607%)
**Top Internal Functions/Classes:**
  * `Scan_Disk_Table_Exit` (Impact: 108.8)
  * `Ctrl_Break_Write` (Impact: 36.3)
    * *Intent:* ;========================================================================= ; Ctrl_Break_Write : This...
  * `Write_Exit` (Impact: 27.4)
  * `Keep_Going` (Impact: 19.2)
  * `BAD100` (Impact: 16.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 1560`, `args: 1217`, `func_start: 136`
* *Risk/State:* `state_mutation: 34`, `dead_code: 32`, `fragile_debt: 5`, `unreferenced_by_name: 19`
* *Architecture:* `io: 1`, `api: 174`, `import: 15`
* *Defense:* `sync_locks: 2`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` BPB.INC, CPMFCB.INC, CURDIR.INC, DIRENT.INC, DOSMAC.INC, DPB.INC, ERROR.INC, FOREQU.INC...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/APPEND/APPEND.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 887.8 | **LOC:** 3462 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.2122%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `no_dbcs2` (Impact: 12.2)
    * *Intent:* ; we go back through ;AN006;
  * `found_it_remote` (Impact: 11.9)
  * `abort_exit` (Impact: 11.1)
  * `got_the_end` (Impact: 10.6)
  * `ccn_20` (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 1089`, `args: 811`, `func_start: 238`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 38`, `dead_code: 163`, `fragile_debt: 2`, `unreferenced_by_name: 36`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` appendp.inc, msgdcl.inc, parse.asm, pdb.inc, sysmac.lib, sysmsg.inc, versiona.inc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `v4.0/src/INC/MSGSERV.ASM` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 81.7095%)
- `v4.0/src/SELECT/MACROS4.INC` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 14.259%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `v4.0/src/INC/STRUC.INC` -> **Severity: 4.574** (Embedded: 0.0557 * Error Risk: 82.1722%)
- `v4.0/src/INC/MSGSERV.ASM` -> **Severity: 1.474** (Embedded: 0.0227 * Error Risk: 64.9296%)
- `v1.25/source/ASM.ASM` -> **Severity: 0.776** (Embedded: 0.0117 * Error Risk: 66.1892%)
- `v4.0/src/BIOS/MSEQU.INC` -> **Severity: 0.477** (Embedded: 0.0049 * Error Risk: 97.6645%)
- `v4.0/src/BIOS/MSGROUP.INC` -> **Severity: 0.473** (Embedded: 0.0078 * Error Risk: 60.5532%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `v1.25/source/ASM.ASM` -> **Severity: 577.1** (Blast Radius: 5.771 * Doc Risk: 100.0%)
- `v4.0/src/SELECT/MACROS8.INC` -> **Severity: 382.6** (Blast Radius: 3.826 * Doc Risk: 100.0%)
- `v4.0/src/DEV/XMAEM/INDEINI.ASM` -> **Severity: 243.7** (Blast Radius: 2.437 * Doc Risk: 100.0%)
- `v4.0/src/SELECT/MACROS4.INC` -> **Severity: 213.1** (Blast Radius: 2.131 * Doc Risk: 100.0%)
- `v4.0-ozzie/bin/DISK2/BIOS/DEFDBUG.INC` -> **Severity: 199.7** (Blast Radius: 1.997 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
