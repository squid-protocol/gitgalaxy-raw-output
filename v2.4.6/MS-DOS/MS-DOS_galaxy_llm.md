# ARCHITECTURAL_BRIEF: MS-DOS
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/MS-DOS` |
| **Timestamp** | `2026-08-03T19:26:32.005150+00:00` |
| **Scan Duration** | `8.42s` |
| **Git Branch** | `main` |
| **Git Commit** | `2d04cacc5322951f187bb17e017c12920ac8ebe2` |
| **Git Remote** | `https://github.com/microsoft/MS-DOS.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 163 malicious artifacts.

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
| Total Artifacts | 1555 |
| Analyzed Artifacts (Scanned) | 1022 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 533 |
| Total LOC | 302435 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 65.7% |
| Dominant Lang | ASSEMBLY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8017 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.355 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.3673 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 78 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 847 | 283878 | 82.9% |
| C | 147 | 18094 | 14.4% |
| PLAINTEXT | 9 | 0 | 0.9% |
| BATCH | 7 | 129 | 0.7% |
| MAKEFILE | 7 | 304 | 0.7% |
| MARKDOWN | 3 | 0 | 0.3% |
| LIVECODE | 2 | 30 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.021`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 829 | 81.1% |
| file_cluster_13 | 103 | 10.1% |
| file_cluster_9 | 43 | 4.2% |
| file_cluster_17 | 27 | 2.6% |
| file_cluster_12 | 3 | 0.3% |
| file_cluster_4 | 1 | 0.1% |
| file_cluster_0 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 15 | 1.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 533*

**Composition by Extension & Reason:**
- `.asm`: 70x Excluded (Binary Format Detected), 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1645 LOC)
- `no_extension`: 67x Unsupported Format (.undeterminable), 4x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
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
- `.ext`: 14x Unsupported Format (.ext)
- `.txt`: 12x Excluded (Binary Format Detected)
- `.pdf`: 12x Excluded (Explicitly Denied Extension: '.pdf')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 97.7 | 19.4 | 12.1 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 17.4 | 7.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 24.6 | 2.3 | 2.3 |
| API Exposure | 0.0 | 20.0 | 6.2 | 4.6 | 0.0 |
| Concurrency Exposure | 0.0 | 91.3 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 40.0 | 26.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 10.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 95.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 46.3 | 25.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 29.3 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 0.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.3 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `v4.0/src/DEV/XMA2EMS/DIAGS.ASM` (Hits: 89)
- `v1.25/source/IO.ASM` (Hits: 69)
- `v4.0-ozzie/bin/DISK2/BIOS/IBMDSK.ASM` (Hits: 43)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **DOSSYM.INC** (`v4.0/src/INC/DOSSYM.INC`) — 93 inbound connections
2. **STRUC.INC** (`v4.0/src/INC/STRUC.INC`) — 57 inbound connections
3. **SYSMSG.INC** (`v4.0/src/INC/SYSMSG.INC`) — 44 inbound connections
4. **EXT.INC** (`v4.0/src/SELECT/EXT.INC`) — 29 inbound connections
5. **POSTEQU.INC** (`v4.0/src/INC/POSTEQU.INC`) — 24 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **MEMMINC.ASM** (`v4.0/src/MEMM/MEMM/MEMMINC.ASM`) — 17 outbound dependencies
2. **KEYBCMD.ASM** (`v4.0/src/CMD/KEYB/KEYBCMD.ASM`) — 16 outbound dependencies
3. **STDDATA.ASM** (`v4.0/src/DOS/STDDATA.ASM`) — 16 outbound dependencies
4. **MSDATA.ASM** (`v4.0/src/INC/MSDATA.ASM`) — 16 outbound dependencies
5. **MSDATA2.ASM** (`v4.0/src/INC/MSDATA2.ASM`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `START` (@ `v4.0/src/CMD/SYS/SYS1.ASM`) -> Impact: **710.3** | LOC: 3344
- `next_level_down` (@ `v4.0/src/CMD/SYS/SYS2.ASM`) -> Impact: **699.0** | LOC: 1083
- `Scan_Disk_Table_Exit` (@ `v4.0/src/CMD/FORMAT/FORMAT.ASM`) -> Impact: **399.0** | LOC: 1064
- `START` (@ `v4.0/src/CMD/TREE/TREE.ASM`) -> Impact: **310.0** | LOC: 1476
- `GENERIC_IOCTL` (@ `v4.0/src/DEV/ANSI/IOCTL.ASM`) -> Impact: **260.3** | LOC: 554
  * *Intent:* ; TO GET OR SET DEVICE CHARACTERISTICS ACCORDING TO THE BUFFER PASSED ; IN THE REQUEST PACKET. ; ; AT ENTRY: ; ; AT EXIT: ; NORMAL: CARRY CLEAR - DEVI...
- `INT_2F_VECTOR` (@ `v4.0/src/SELECT/INTVEC.ASM`) -> Impact: **234.1** | LOC: 184
- `ContJ` (@ `v4.0/src/CMD/SHARE/GSHARE2.ASM`) -> Impact: **225.9** | LOC: 997
- `dummy10` (@ `v4.0/src/CMD/MODE/MODECP.ASM`) -> Impact: **215.6** | LOC: 522
- `EXIT_INIT` (@ `v4.0/src/CMD/DISKCOPY/COPYINIT.ASM`) -> Impact: **190.4** | LOC: 754
- `Ctrl_Break_Write` (@ `v4.0/src/CMD/FORMAT/FORMAT.ASM`) -> Impact: **172.1** | LOC: 303
  * *Intent:* ;========================================================================= ; Ctrl_Break_Write : This routine takes the control break request ; an retu...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `HWCP_1` (@ `v4.0/src/DEV/PRINTER/PARSE4E.ASM`) -> **O(2^N) [Recursive]**
- `DESG_PARM1` (@ `v4.0/src/DEV/PRINTER/PARSE4E.ASM`) -> **O(2^N) [Recursive]**
- `ID_PARMS` (@ `v4.0/src/DEV/PRINTER/PARSE4E.ASM`) -> **O(2^N) [Recursive]**
- `DF1` (@ `v4.0/src/DEV/PRINTER/PARSE4E.ASM`) -> **O(2^N) [Recursive]**
- `MH1` (@ `v4.0/src/DEV/PRINTER/PARSE4E.ASM`) -> **O(2^N) [Recursive]**
- `NEXT_NUM` (@ `v4.0/src/DEV/PRINTER/PARSE4E.ASM`) -> **O(2^N) [Recursive]**
- `GET_PARMS_A` (@ `v4.0/src/DEV/PRINTER/PARSE4E.ASM`) -> **O(2^N) [Recursive]**
- `FBR1` (@ `v4.0/src/DEV/PRINTER/PARSE4E.ASM`) -> **O(2^N) [Recursive]**
- `CLR_DELIM` (@ `v4.0/src/DEV/PRINTER/PARSE4E.ASM`) -> **O(2^N) [Recursive]**
- `LL1` (@ `v4.0/src/DEV/PRINTER/PARSE4E.ASM`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `parse_init` (@ `v4.0/src/CMD/FILESYS/FILESYS.C`) -> DB Complexity: **65**
  * *Intent:* /* ;an000; */ if ((p_result1.P_Type == p_string) && (i > 2)) /* ;an000; */ { /* ;an000; */ fs_strcpy(string_ptr,p_result1.p_result_buff); /* ;an000; *...
- `Sub3_Message` (@ `v4.0/src/CMD/MEM/MEM.C`) -> DB Complexity: **60**
  * *Intent:* Parse_Ptr = (unsigned)cmd_line; /*;an003; dms; point to command */ /* ;an000; */ parse(&InRegs,&OutRegs); /* an000; dms; parse command line */ /* ;an0...
- `CONF_HMEG_OK` (@ `v4.0/src/DEV/XMA2EMS/PS2_5060.INC`) -> DB Complexity: **48**
- `Print_ext_attrib` (@ `v4.0/src/CMD/ATTRIB/ATTRIB.C`) -> DB Complexity: **44**
- `Sub4_Message` (@ `v4.0/src/CMD/MEM/MEM.C`) -> DB Complexity: **44**
  * *Intent:* /* ;an000; */ /* Display the BIO location and size */ /* ;an000; */ /* ;an000; */ Sub0_Message(NewLineMsg,STDOUT,Utility_Msg_Class); /* ;an000; */ /* ...
- `Extended_attrib` (@ `v4.0/src/CMD/ATTRIB/ATTRIB.C`) -> DB Complexity: **38**
  * *Intent:* WORD answer; /*;AN000;*/ WORD key; /*;AN000;*/ while (TRUE) { /*;AN000;*/ msg_str2.sub_value_seg = segregs.ds; /*;AN000;*/ msg_str2.sub_value = (WORD)...
- `Sub4a_Message` (@ `v4.0/src/CMD/MEM/MEM.C`) -> DB Complexity: **38**
  * *Intent:* SystemDataType = ConfigStacksMsg; /* ;an000; */ break; /* ;an000; */ case 'T': /* gga */ /* ;an000; */ SystemDataType = ConfigInstallMsg; /* gga */ /*...
- `AUXENT` (@ `v4.0/src/BIOS/MSBIO1.ASM`) -> DB Complexity: **36**
  * *Intent:* ;SB33102****************************************************************
- `END_PREPARE_FILE` (@ `v4.0/src/SELECT/ROUTINES.ASM`) -> DB Complexity: **35**
  * *Intent:* ;
- `main` (@ `v4.0/src/CMD/FILESYS/FILESYS.C`) -> DB Complexity: **34**
  * *Intent:* unsigned char max_width; /* max width of replaceable field */ /* ;an000; */ unsigned char min_width; /* min width of replaceable field */ /* ;an000; *...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `v4.0/src/INC` | 81 | 29244.96 | 37.81% | 3.8% |
| `v4.0/src/DEV/XMA2EMS` | 13 | 17802.76 | 37.2% | 3.71% |
| `v4.0/src/CMD/FDISK` | 38 | 13259.82 | 35.74% | 0.0% |
| `v4.0/src/DOS` | 83 | 10389.86 | 14.84% | 17.84% |
| `v4.0/src/CMD/CHKDSK` | 17 | 10383.78 | 30.26% | 7.36% |
| `v4.0/src/SELECT` | 66 | 10017.23 | 12.8% | 2.87% |
| `v4.0/src/BIOS` | 35 | 8513.42 | 27.52% | 17.06% |
| `v1.25/source` | 7 | 8405.06 | 22.81% | 21.59% |
| `v4.0/src/CMD/COMMAND` | 39 | 7160.12 | 13.22% | 27.69% |
| `v4.0/src/DEV/PRINTER` | 10 | 6979.26 | 28.26% | 6.99% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `v2.0/source/MSHEAD.ASM` -> **100.0%** Exposure
- `v4.0/src/DEV/DISPLAY/EGA/CPI-HEAD.ASM` -> **100.0%** Exposure
- `v4.0/src/DEV/DISPLAY/LCD/FONT-R3.ASM` -> **100.0%** Exposure
- `v4.0/src/DOS/DISPATCH.ASM` -> **100.0%** Exposure
- `v4.0/src/INC/MSHEAD.ASM` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `v4.0/src/CMD/COMMAND/COMSW.ASM` -> **100.0%** Exposure
- `v4.0/src/DOS/STDDATA.ASM` -> **100.0%** Exposure
- `v4.0/src/INC/MSDATA.ASM` -> **100.0%** Exposure
- `v4.0/src/INC/MSDATA2.ASM` -> **100.0%** Exposure
- `v4.0/src/BIOS/BIOSTRUC.INC` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `v4.0/src/CMD/FASTOPEN/FASTINIT.ASM` -> **68** Orphaned Functions | **0** Duplicates
- `v4.0/src/DEV/SMARTDRV/SMARTDRV.ASM` -> **57** Orphaned Functions | **0** Duplicates
- `v1.25/source/IO.ASM` -> **0** Orphaned Functions | **45** Duplicates
- `v4.0-ozzie/bin/DISK2/BIOS/IBMBIO.ASM` -> **30** Orphaned Functions | **10** Duplicates
- `v4.0/src/DEV/RAMDRIVE/RAMDRIVE.ASM` -> **34** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`v4.0/src/CMD/FDISK/DISPLAY.C`** -> AI Confidence: **99.48%**
2. **`v4.0/src/CMD/FDISK/D_MENUS.C`** -> AI Confidence: **99.48%**
3. **`v4.0/src/CMD/FDISK/FDISK.C`** -> AI Confidence: **99.48%**
4. **`v4.0/src/CMD/FDISK/INPUT.C`** -> AI Confidence: **99.48%**
5. **`v4.0/src/CMD/FDISK/INT13.C`** -> AI Confidence: **99.48%**
6. **`v4.0/src/CMD/FDISK/MAIN.C`** -> AI Confidence: **99.48%**
7. **`v4.0/src/CMD/FDISK/TDISPLAY.C`** -> AI Confidence: **99.48%**
8. **`v4.0/src/CMD/FDISK/VDISPLAY.C`** -> AI Confidence: **99.48%**
9. **`v4.0/src/CMD/RESTORE/RESTPARS.C`** -> AI Confidence: **99.48%**
10. **`v4.0/src/CMD/RESTORE/RTNEW.C`** -> AI Confidence: **99.48%**
11. **`v4.0/src/CMD/RESTORE/RTOLD.C`** -> AI Confidence: **99.48%**
12. **`v4.0/src/CMD/RESTORE/RTT.C`** -> AI Confidence: **99.48%**
13. **`v4.0/src/CMD/RESTORE/RTT2.C`** -> AI Confidence: **99.48%**
14. **`v4.0/src/CMD/ATTRIB/ATTRIB.C`** -> AI Confidence: **99.39%**
15. **`v4.0/src/CMD/BACKUP/BACKUP.C`** -> AI Confidence: **99.39%**
16. **`v4.0/src/CMD/RESTORE/RTDO.C`** -> AI Confidence: **99.39%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `v4.0/src/DEV/SMARTDRV/FLUSH13.C` -> **29.2835%** Exposure
### Exploit Generation Surface
- `v4.0/src/BIOS/MSINIT.ASM` -> **20.0%** Exposure
- `v4.0/src/DEV/ANSI/ANSI.ASM` -> **20.0%** Exposure
- `v4.0/src/DEV/ANSI/IOCTL.ASM` -> **20.0%** Exposure
- `v4.0/src/DEV/PRINTER/PARSE4E.ASM` -> **20.0%** Exposure
- `v4.0/src/DEV/RAMDRIVE/RAMDRIVE.ASM` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `v4.0/src/CMD/SYS/SYSHDR.INC` -> **100.0%** Exposure
- `v4.0/src/DEV/ANSI/ANSI.INC` -> **100.0%** Exposure
- `v4.0/src/DEV/DISPLAY/DEF-EQU.INC` -> **100.0%** Exposure
- `v4.0/src/INC/EA.INC` -> **99.9995%** Exposure
- `v4.0/src/INC/SF.INC` -> **99.8739%** Exposure
### Raw Memory Manipulation
- `v4.0/src/CMD/SYS/SYS2.ASM` -> **9.9987%** Exposure
- `v4.0/src/DOS/DEV.ASM` -> **9.9951%** Exposure
- `v4.0/src/CMD/FDISK/FDISKMSG.C` -> **9.9949%** Exposure
- `v4.0/src/BIOS/MSIOCTL.INC` -> **9.989%** Exposure
- `v4.0/src/BIOS/SYSINIT1.ASM` -> **9.947%** Exposure
### Algorithmic DoS Exposure
- `v2.0/source/DEBCOM2.ASM` -> **100.0%** Exposure
- `v2.0/source/EDLIN.ASM` -> **100.0%** Exposure
- `v2.0/source/FORMAT.ASM` -> **100.0%** Exposure
- `v4.0/src/CMD/KEYB/KEYBI9.ASM` -> **100.0%** Exposure
- `v4.0/src/CMD/SYS/SYS1.ASM` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `80` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2309` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `v4.0/src/INC/ERRTST.C` (C) -> Cumulative Risk: **705.32**
- **Archetype:** `file_cluster_13` (Distance: 13.211 IQR)
- **Magnitude:** 326.58 | **LOC:** 310 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.7786%)
- **Heaviest Functions:** `rootpath` (Impact: 67.0), `fPathErr` (Impact: 54.7), `strbscan` (Impact: 3.5)

### 2. `v4.0/src/CMD/FC/FC.C` (C) -> Cumulative Risk: **694.01**
- **Archetype:** `file_cluster_8` (Distance: 13.041 IQR)
- **Magnitude:** 466.76 | **LOC:** 865 | **CtrlFlow:** 87.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (88.4294%)
- **Heaviest Functions:** `compare` (Impact: 57.0), `strcmpis` (Impact: 8.8), `strcmpi` (Impact: 8.2)

### 3. `v4.0/src/CMD/RESTORE/RTT3.C` (C) -> Cumulative Risk: **684.19**
- **Archetype:** `file_cluster_13` (Distance: 13.669 IQR)
- **Magnitude:** 286.44 | **LOC:** 620 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (91.075%)
- **Heaviest Functions:** `initbuf` (Impact: 19.8), `exit_routine` (Impact: 16.9), `chek_DBCS` (Impact: 13.2)

### 4. `v4.0/src/CMD/ATTRIB/ATTRIB.C` (C) -> Cumulative Risk: **644.54**
- **Archetype:** `file_cluster_13` (Distance: 15.052 IQR)
- **Magnitude:** 1414.88 | **LOC:** 2686 | **CtrlFlow:** 77.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (91.0485%)
- **Heaviest Functions:** `Extended_attrib` (Impact: 125.7), `Do_dir` (Impact: 67.8), `Print_ext_attrib` (Impact: 59.8)

### 5. `v4.0/src/CMD/RESTORE/RTNEW1.C` (C) -> Cumulative Risk: **636.15**
- **Archetype:** `file_cluster_13` (Distance: 14.396 IQR)
- **Magnitude:** 356.94 | **LOC:** 628 | **CtrlFlow:** 77.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `findnext_new` (Impact: 45.2), `get_fileheader_length` (Impact: 6.5), `read_in_next_dirblock` (Impact: 3.8)

### 6. `v4.0/src/INC/SF.INC` (ASSEMBLY) -> Cumulative Risk: **619.92**
- **Archetype:** `file_cluster_8` (Distance: 13.963 IQR)
- **Magnitude:** 366.04 | **LOC:** 169 | **CtrlFlow:** 88.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9999%), Safety Score (99.9812%)

### 7. `v4.0/src/CMD/SYS/SYSHDR.INC` (ASSEMBLY) -> Cumulative Risk: **616.18**
- **Archetype:** `file_cluster_8` (Distance: 12.858 IQR)
- **Magnitude:** 468.74 | **LOC:** 428 | **CtrlFlow:** 87.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Documentation (99.8088%)

### 8. `v4.0/src/CMD/FILESYS/FILESYS.C` (C) -> Cumulative Risk: **609.93**
- **Archetype:** `file_cluster_8` (Distance: 12.318 IQR)
- **Magnitude:** 363.22 | **LOC:** 923 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (97.3437%)
- **Heaviest Functions:** `main` (Impact: 104.0), `fs_status` (Impact: 14.0), `device_attach` (Impact: 7.5)

### 9. `v4.0/src/CMD/REPLACE/REPLACE.C` (C) -> Cumulative Risk: **608.91**
- **Archetype:** `file_cluster_8` (Distance: 13.331 IQR)
- **Magnitude:** 670.8 | **LOC:** 2048 | **CtrlFlow:** 82.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (87.4967%)
- **Heaviest Functions:** `dodir` (Impact: 66.5), `docopy` (Impact: 13.3), `dwrite` (Impact: 11.8)

### 10. `v4.0/src/CMD/MEM/MEM.C` (C) -> Cumulative Risk: **591.71**
- **Archetype:** `file_cluster_8` (Distance: 13.229 IQR)
- **Magnitude:** 664.98 | **LOC:** 1675 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (84.1199%)
- **Heaviest Functions:** `GetFromArgvZero` (Impact: 51.8), `TypeOf` (Impact: 41.1), `Sub3_Message` (Impact: 25.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `v4.0/src/INC/SHELLRD.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.585 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.76 IQR)
- **Top Global Matches:** file_cluster_8: 14.585, file_cluster_7: 14.979, file_cluster_13: 15.032
- **Magnitude:** 7963.42 | **LOC:** 5112 | **CtrlFlow:** 95.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (58.1499%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 390`, `structural_boundaries: 18`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 5864`
* *Architecture:* `io: 42`, `api: 1983`
* *Defense:* `test: 56`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/INC/PCINPUT.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.793 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.077 IQR)
- **Top Global Matches:** file_cluster_8: 14.793, file_cluster_7: 15.187, file_cluster_13: 15.228
- **Magnitude:** 6704.42 | **LOC:** 3795 | **CtrlFlow:** 97.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (59.7897%), Tech Debt (7.9661%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 372`, `structural_boundaries: 9`, `args: 1`
* *Risk/State:* `state_mutation: 5360`, `fragile_debt: 1`
* *Architecture:* `io: 38`, `api: 1254`
* *Defense:* `test: 102`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/DEV/XMA2EMS/LIM40.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.865 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.896 IQR)
- **Top Global Matches:** file_cluster_8: 15.865, file_cluster_0: 16.131, file_cluster_13: 16.134
- **Magnitude:** 5644.08 | **LOC:** 1793 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (60.7597%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 76`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 5053`
* *Architecture:* `io: 7`, `api: 549`
* *Defense:* `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/CHKDSK/CHKDISK.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.779 IQR)
- **Top Global Matches:** file_cluster_8: 8.779, file_cluster_13: 9.463, file_cluster_7: 9.696
- **Magnitude:** 5343.78 | **LOC:** 328 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (20.8609%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 56`, `args: 114`, `func_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 1`, `api: 2`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` CHKMACRO.INC, CHKCHNG.INC, pathmac.inc, DOSSYM.INC, chkseg.inc, CHKEQU.INC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/DEV/XMA2EMS/XMA1DIAG.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.954 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.336 IQR)
- **Top Global Matches:** file_cluster_8: 14.954, file_cluster_7: 15.328, file_cluster_0: 15.342
- **Magnitude:** 4105.18 | **LOC:** 1871 | **CtrlFlow:** 94.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (55.9971%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3266`
* *Architecture:* `io: 21`, `api: 789`
* *Defense:* `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000976
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `v4.0/src/SELECT/GET_STAT.C` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.067 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.915 IQR)
- **Top Global Matches:** file_cluster_13: 14.067, file_cluster_8: 14.267, file_cluster_0: 14.279
- **Magnitude:** 2789.91 | **LOC:** 1217 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (39.5564%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 46`, `args: 19`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `state_mutation: 235`, `dead_code: 4`
* *Architecture:* `api: 115`, `import: 6`
* *Defense:* `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdlib.h, string.h, dos.h, stdio.h, extern.h, get_stat.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/INC/DSEG.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 17.575 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.008 IQR)
- **Top Global Matches:** file_cluster_8: 17.575, file_cluster_11: 17.748, file_cluster_13: 17.772
- **Magnitude:** 2499.12 | **LOC:** 209 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (78.9246%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`
* *Risk/State:* `state_mutation: 2383`
* *Architecture:* `api: 97`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001951
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `v1.25/source/MSDOS.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.011 IQR)
- **Top Global Matches:** file_cluster_8: 12.011, file_cluster_7: 12.591, file_cluster_17: 12.594
- **Magnitude:** 2349.68 | **LOC:** 4031 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (24.6647%), Tech Debt (8.9038%)
**Top Internal Functions/Classes:**
  * `GETCH` (Impact: 39.0 | O(2^N) | DB: 3)
  * `DWRITE` (Impact: 31.1 | O(2^N))
  * `OPTCLUS` (Impact: 30.5 | O(2^N) | DB: 2)
  * `SMALREC` (Impact: 29.8 | O(N^2) | DB: 1)
  * `SKPCLP` (Impact: 25.9 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 825`, `structural_boundaries: 1243`, `args: 1835`, `func_start: 404`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 358`, `dead_code: 12`, `fragile_debt: 3`
* *Architecture:* `io: 28`, `api: 6`
* *Defense:* `safety: 1`, `sync_locks: 22`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v1.25/source/ASM.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.887 IQR)
- **Top Global Matches:** file_cluster_8: 11.887, file_cluster_7: 12.472, file_cluster_1: 12.614
- **Magnitude:** 2249.5 | **LOC:** 4006 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (29.0062%), Tech Debt (9.0683%)
**Top Internal Functions/Classes:**
  * `CHKRET` (Impact: 35.0 | O(2^N) | DB: 4)
  * `DEC` (Impact: 32.1 | O(2^N) | DB: 5)
  * `NWAIT` (Impact: 31.9 | O(N^1) | DB: 2)
  * `ASMLIN` (Impact: 30.1 | O(N^1) | DB: 3)
  * `REGCHK` (Impact: 28.6 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1051`, `structural_boundaries: 1023`, `args: 1914`, `func_start: 477`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 435`, `dead_code: 5`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 7`
* *Defense:* `safety: 2`, `sync_locks: 47`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011707
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `v4.0/src/CMD/FDISK/INPUT.C` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.499 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.549 IQR)
- **Top Global Matches:** file_cluster_8: 12.499, file_cluster_13: 12.751, file_cluster_7: 12.957
- **Magnitude:** 1948.76 | **LOC:** 674 | **CtrlFlow:** 94.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (73.904%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 8`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 277`
* *Architecture:* `api: 158`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, string.h, fdisk.h, fdiskmsg.h, dos.h, subtype.h, stdio.h, extern.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/CHKDSK/CHKMSG.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.206 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.543 IQR)
- **Top Global Matches:** file_cluster_8: 14.206, file_cluster_7: 14.608, file_cluster_13: 14.696
- **Magnitude:** 1880.94 | **LOC:** 1048 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (52.1%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`
* *Risk/State:* `state_mutation: 1545`
* *Architecture:* `io: 1`, `api: 300`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000976
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `v4.0/src/CMD/MODE/MODEDEFS.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.866 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.454 IQR)
- **Top Global Matches:** file_cluster_8: 14.866, file_cluster_7: 15.257, file_cluster_13: 15.308
- **Magnitude:** 1879.52 | **LOC:** 750 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (52.4773%), Tech Debt (8.6096%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1754`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 96`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000976
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `v4.0/src/CMD/FORMAT/FORMAT.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.131 IQR)
- **Top Global Matches:** file_cluster_8: 12.131, file_cluster_13: 12.531, file_cluster_0: 12.566
- **Magnitude:** 1766.54 | **LOC:** 4509 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (14.9097%), Tech Debt (13.4217%)
**Top Internal Functions/Classes:**
  * `Scan_Disk_Table_Exit` (Impact: 399.0 | O(N^2) | DB: 14)
  * `Ctrl_Break_Write` (Impact: 172.1 | O(2^N) | DB: 2)
    * *Intent:* ;========================================================================= ; Ctrl_Break_Write : This...
  * `Write_Exit` (Impact: 67.9 | O(N^1) | DB: 2)
  * `BAD100` (Impact: 41.7 | O(N^2))
  * `TrackLayoutSet` (Impact: 32.5 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 649`, `structural_boundaries: 1039`, `args: 1217`, `func_start: 136`
* *Risk/State:* `state_mutation: 109`, `dead_code: 32`, `fragile_debt: 5`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 174`, `import: 15`
* *Defense:* `sync_locks: 2`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` DPB.INC, SYSVAR.INC, PDB.INC, IOCTL.INC, SYSCALL.INC, VERSIONA.INC, DIRENT.INC, FORMACRO.INC...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/DEV/SMARTDRV/SMARTDRV.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.285 IQR)
- **Top Global Matches:** file_cluster_8: 13.285, file_cluster_17: 13.588, file_cluster_0: 13.621
- **Magnitude:** 1718.54 | **LOC:** 7587 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (18.7066%), Tech Debt (55.688%)
**Top Internal Functions/Classes:**
  * `pbw$4` (Impact: 35.9 | O(N^1) | DB: 1)
    * *Intent:* ; ; error exit ;
  * `SETLOOP` (Impact: 26.1 | O(2^N))
  * `do_it` (Impact: 23.6 | O(N^1) | DB: 3)
  * `NEXTC` (Impact: 23.3 | O(2^N) | DB: 2)
  * `FIRST_ARG` (Impact: 18.1 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 914`, `structural_boundaries: 1462`, `args: 1977`, `func_start: 386`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 1`, `state_mutation: 277`, `dead_code: 61`, `fragile_debt: 8`, `orphaned_logic: 57`
* *Architecture:* `io: 28`, `api: 18`, `import: 7`
* *Defense:* `sync_locks: 14`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` above.asm, ab_macro.asm, devsym.asm, emm.asm, syscall.asm, mi.asm, loadall.asm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FORMAT/FORMSG.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.461 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.531 IQR)
- **Top Global Matches:** file_cluster_8: 14.461, file_cluster_7: 14.85, file_cluster_13: 14.937
- **Magnitude:** 1694.26 | **LOC:** 862 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (50.8609%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`
* *Risk/State:* `state_mutation: 1455`
* *Architecture:* `api: 208`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000976
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `v1.25/source/COMMAND.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.092 IQR)
- **Top Global Matches:** file_cluster_8: 11.092, file_cluster_1: 11.633, file_cluster_7: 11.719
- **Magnitude:** 1669.78 | **LOC:** 2166 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (18.3965%), Tech Debt (13.4304%)
**Top Internal Functions/Classes:**
  * `CONVLP` (Impact: 39.1 | O(2^N) | DB: 7)
  * `MILLENIUM` (Impact: 30.6 | O(N^2))
  * `MULTAPP` (Impact: 30.2 | O(2^N))
  * `COMTAIL` (Impact: 27.0 | O(2^N))
  * `COMTIM` (Impact: 26.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 710`, `args: 972`, `func_start: 202`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 151`, `dead_code: 2`, `fragile_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 22`
* *Defense:* `safety: 2`, `sync_locks: 19`, `immutability_locks: 58`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/DEV/PRINTER/CPSPM10.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.18 IQR)
- **Top Global Matches:** file_cluster_8: 12.18, file_cluster_7: 12.744, file_cluster_17: 12.78
- **Magnitude:** 1656.6 | **LOC:** 3852 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (30.2408%), Tech Debt (15.5352%)
**Top Internal Functions/Classes:**
  * `CTLres2_R` (Impact: 57.2 | O(N^2))
  * `SET_DID` (Impact: 27.0 | O(2^N) | DB: 1)
    * *Intent:* ;;
  * `CTL_COMMON` (Impact: 15.8 | O(N^1) | DB: 2)
  * `RET0_NO_STACK` (Impact: 15.7 | O(N^1))
    * *Intent:* ;; ;;
  * `IVK_RET` (Impact: 14.7 | O(N^1))
    * *Intent:* ;;
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 431`, `structural_boundaries: 1114`, `args: 1445`, `func_start: 348`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 461`, `dead_code: 10`, `orphaned_logic: 19`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CPSPEQU.INC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/DEV/XMA2EMS/ROMSCAN.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.97 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.935 IQR)
- **Top Global Matches:** file_cluster_8: 15.97, file_cluster_13: 16.253, file_cluster_0: 16.278
- **Magnitude:** 1647.12 | **LOC:** 420 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (57.7794%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`
* *Risk/State:* `state_mutation: 1505`
* *Architecture:* `io: 1`, `api: 121`
* *Defense:* `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/FDISK.C` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.5 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.529 IQR)
- **Top Global Matches:** file_cluster_8: 12.5, file_cluster_7: 12.866, file_cluster_0: 12.964
- **Magnitude:** 1591.84 | **LOC:** 1122 | **CtrlFlow:** 84.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (65.0095%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 17`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 260`
* *Architecture:* `api: 139`
* *Defense:* `safety: 1`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, string.h, fdisk.h, fdiskmsg.h, dos.h, subtype.h, stdio.h, process.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v2.0/source/EDLIN.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.594 IQR)
- **Top Global Matches:** file_cluster_8: 11.594, file_cluster_17: 12.178, file_cluster_7: 12.204
- **Magnitude:** 1561.12 | **LOC:** 1846 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (29.1232%), Tech Debt (21.8263%)
**Top Internal Functions/Classes:**
  * `SRCH` (Impact: 34.8 | O(2^N) | DB: 1)
  * `NUMLP` (Impact: 30.6 | O(2^N))
  * `REPLP` (Impact: 27.5 | O(N^2) | DB: 5)
  * `PAGE` (Impact: 26.1 | O(N^2) | DB: 1)
  * `BLKMOVE` (Impact: 26.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 425`, `structural_boundaries: 590`, `args: 790`, `func_start: 177`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 181`, `dead_code: 4`, `fragile_debt: 4`, `orphaned_logic: 5`
* *Architecture:* `io: 7`, `api: 5`, `import: 1`
* *Defense:* `sync_locks: 4`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DOSSYM.ASM
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/DEV/XMA2EMS/EMSINIT.INC` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.937 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.139 IQR)
- **Top Global Matches:** file_cluster_8: 13.937, file_cluster_0: 14.308, file_cluster_7: 14.326
- **Magnitude:** 1504.28 | **LOC:** 887 | **CtrlFlow:** 95.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (61.4429%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 3`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 1023`
* *Architecture:* `io: 20`, `api: 451`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000976
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `v4.0/src/DEV/RAMDRIVE/RAMDRIVE.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.28 IQR)
- **Top Global Matches:** file_cluster_17: 15.28, file_cluster_8: 15.387, file_cluster_9: 15.418
- **Magnitude:** 1502.72 | **LOC:** 6218 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (15.9775%), Tech Debt (58.3861%)
**Top Internal Functions/Classes:**
  * `GET_AVAIL` (Impact: 37.9 | O(2^N))
    * *Intent:* ; ; Allocate drive memory ;
  * `FATSUB` (Impact: 32.0 | O(2^N))
  * `FIRST_ARG` (Impact: 21.1 | O(N^1) | DB: 1)
  * `skip_adj_dev_size` (Impact: 19.3 | O(N^1) | DB: 1)
  * `GETNUM1` (Impact: 17.6 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 625`, `structural_boundaries: 1038`, `args: 1378`, `func_start: 300`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 145`, `dead_code: 111`, `planned_debt: 1`, `fragile_debt: 11`, `orphaned_logic: 34`
* *Architecture:* `io: 25`, `import: 8`
* *Defense:* `safety: 3`, `sync_locks: 5`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mi.inc, syscall.inc, loadall.inc, above.inc, emm.inc, devsym.inc, ab_macro.inc, dirent.inc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/ATTRIB/ATTRIB.C` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.052 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.687 IQR)
- **Top Global Matches:** file_cluster_13: 15.052, file_cluster_0: 15.128, file_cluster_11: 15.137
- **Magnitude:** 1414.88 | **LOC:** 2686 | **CtrlFlow:** 77.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (34.3786%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Extended_attrib` (Impact: 125.7 | O(N^6) | DB: 38)
    * *Intent:* WORD answer; /*;AN000;*/ WORD key; /*;AN000;*/ while (TRUE) { /*;AN000;*/ msg_str2.sub_value_seg = s...
  * `Do_dir` (Impact: 67.8 | O(2^N) | DB: 14)
    * *Intent:* /* */ /* y = 0-119 (1980-2099) */ /* m = 1-12 */ /* d = 1-31 */ /* */ /* Message retriever requires:...
  * `Print_ext_attrib` (Impact: 59.8 | O(N^3) | DB: 44)
  * `Attrib` (Impact: 26.6 | O(N^3) | DB: 12)
    * *Intent:* else if (length == 2) { /*;AN000;*/ msg_num.sub_flags = sf_unsbin2d | sf_word | sf_right; /*;AN000;*...
  * `Check_DBCS` (Impact: 21.9 | O(N^3) | DB: 10)
    * *Intent:* /* determine which info to get by using ID */ if (id == A_FILESIZE) { /* get filesize */ /*;AN000;*/...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 57`, `func_start: 20`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 779`, `dead_code: 16`
* *Architecture:* `io: 1`, `api: 199`, `import: 7`
* *Defense:* `doc: 68`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` attrib.h, string.h, dos.h, io.h, stdio.h, parse.h, msgret.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/APPEND/APPEND.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 17.783 IQR)
- **Top Global Matches:** file_cluster_9: 17.783, file_cluster_17: 17.83, file_cluster_0: 17.831
- **Magnitude:** 1389.8 | **LOC:** 3462 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (18.0347%), Tech Debt (30.3381%)
**Top Internal Functions/Classes:**
  * `do_closes` (Impact: 23.8 | O(2^N) | DB: 1)
  * `got_the_end` (Impact: 20.4 | O(2^N) | DB: 1)
  * `version_loc` (Impact: 19.5 | O(N^1))
    * *Intent:* ;----------------------------------------------------------------------------- ; Resident data area ...
  * `abort_exit` (Impact: 19.1 | O(N^1) | DB: 3)
  * `copy_true_name_loop2` (Impact: 18.3 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 512`, `structural_boundaries: 737`, `args: 810`, `func_start: 239`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 113`, `dead_code: 163`, `fragile_debt: 2`, `orphaned_logic: 18`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sysmsg.inc, versiona.inc, appendp.inc, parse.asm, msgdcl.inc, sysmac.lib, pdb.inc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/DEV/XMA2EMS/DIAGS.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.043 IQR)
- **Top Global Matches:** file_cluster_8: 12.043, file_cluster_17: 12.387, file_cluster_0: 12.42
- **Magnitude:** 1340.1 | **LOC:** 1910 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (20.727%), Tech Debt (13.1217%)
**Top Internal Functions/Classes:**
  * `STG2` (Impact: 144.2 | O(2^N) | DB: 3)
  * `MA1` (Impact: 65.0 | O(2^N))
    * *Intent:* ;BEGIN TEST
  * `RMW2` (Impact: 57.4 | O(2^N))
  * `R2` (Impact: 36.4 | O(N^4) | DB: 7)
  * `PT1` (Impact: 36.3 | O(2^N) | DB: 1)
    * *Intent:* ;EACH TASK ID IS ASSIGNED 64K ;FROM 640K TO 1024K
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 408`, `args: 837`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 79`, `dead_code: 15`, `orphaned_logic: 5`
* *Architecture:* `io: 89`, `concurrency: 4`, `import: 1`
* *Defense:* `sync_locks: 24`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EMS_US.MSG
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `v4.0/src/BIOS/MS96TPI.INC` (ASSEMBLY) | Magnitude: 263.74 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 234, args: 105, branch: 91, structural_boundaries: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `v4.0/src/CMD/FC/TOOLS.H` (C) | Magnitude: 36.18 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 42, api: 14, reflection_metaprogramming: 13, indent_spaces: 9
- `v4.0/src/TOOLS/BLD/INC/VARARGS.H` (C) | Magnitude: 0.02 | Delta: **0.136 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 6, state_mutation: 3, reflection_metaprogramming: 3, structural_boundaries: 1
- `v4.0/src/TOOLS/BLD/INC/STDARG.H` (C) | Magnitude: 0.02 | Delta: **0.206 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 5, state_mutation: 3, reflection_metaprogramming: 3, structural_boundaries: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `v4.0/src/CMD/MODE/MODELENG.ASM` (ASSEMBLY) | Magnitude: 35.7 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 62, args: 49, structural_boundaries: 47, branch: 19
- `v4.0/src/MAPPER/WCHSTRA.ASM` (ASSEMBLY) | Magnitude: 32.6 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 48, args: 33, structural_boundaries: 24, state_mutation: 13
- `v4.0/src/MAPPER/CLOSE.ASM` (ASSEMBLY) | Magnitude: 9.84 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 8, args: 7, branch: 3
- `v4.0/src/INC/STRING.C` (C) | Magnitude: 76.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 42, indent_tabs: 25, pointers: 21, api: 17
- `v4.0/src/MAPPER/SEL_DISK.ASM` (ASSEMBLY) | Magnitude: 18.52 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, args: 5, state_mutation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `v4.0/src/BIOS/MSVOLID.INC` (ASSEMBLY) | Magnitude: 99.14 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 147, args: 102, structural_boundaries: 99, branch: 32
- `v4.0/src/BIOS/SYSCONF.ASM` (ASSEMBLY) | Magnitude: 1006.96 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 1390, args: 705, structural_boundaries: 618, branch: 374
- `v4.0/src/CMD/GRAPHICS/GRCOLPRT.ASM` (ASSEMBLY) | Magnitude: 333.46 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 234, args: 210, structural_boundaries: 194, branch: 109
- `v4.0/src/CMD/SYS/SYS2.ASM` (ASSEMBLY) | Magnitude: 897.86 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: args: 579, indent_spaces: 522, structural_boundaries: 420, pointers: 310
- `v4.0/src/DOS/DELETE.ASM` (ASSEMBLY) | Magnitude: 169.48 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 312, args: 149, structural_boundaries: 124, branch: 74

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `v4.0/src/DOS/LOCK.ASM` (ASSEMBLY) | Magnitude: 82.14 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 91, dead_code: 72, structural_boundaries: 33, args: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `v4.0/src/MAPPER/BEEP.ASM` (ASSEMBLY) | Magnitude: 30.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, args: 30, structural_boundaries: 19, branch: 12
- `v4.0/src/MEMM/EMM/EMMDISP.ASM` (ASSEMBLY) | Magnitude: 22.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 63, args: 11, structural_boundaries: 10, state_mutation: 9
- `v4.0/src/CMD/RECOVER/RECOVER.ASM` (ASSEMBLY) | Magnitude: 569.0 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: args: 517, indent_tabs: 493, structural_boundaries: 394, branch: 245
- `v4.0/src/DOS/SEARCH.ASM` (ASSEMBLY) | Magnitude: 129.14 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 187, args: 84, structural_boundaries: 66, pointers: 58
- `v4.0/src/MAPPER/READ.ASM` (ASSEMBLY) | Magnitude: 6.76 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, args: 9, pointers: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `v4.0/src/CMD/GRAFTABL/GRTABSM.ASM` (ASSEMBLY) | Magnitude: 24.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 7, sec_high_risk_execution: 6, structural_boundaries: 5, state_mutation: 5
- `v4.0/src/MAPPER/GMACHMOD.ASM` (ASSEMBLY) | Magnitude: 17.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_tabs: 5, args: 2, dead_code: 2
- `v4.0/src/DOS/FILE.ASM` (ASSEMBLY) | Magnitude: 255.8 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 432, args: 195, structural_boundaries: 137, branch: 82
- `v4.0/src/SELECT/ASM2C.ASM` (ASSEMBLY) | Magnitude: 20.9 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 49, structural_boundaries: 33, args: 20, dead_code: 7
- `v4.0/src/DOS/HANDLE.ASM` (ASSEMBLY) | Magnitude: 223.58 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 338, args: 169, structural_boundaries: 110, dead_code: 83

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `v4.0/src/SELECT/MACROS4.INC` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 50.5303%)
- `v4.0/src/SELECT/MACROS5.INC` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 45.7034%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `v4.0/src/INC/DOSSYM.INC` -> **Severity: 8.415** (Embedded: 0.0907 * Error Risk: 92.7433%)
- `v4.0/src/INC/SYSMSG.INC` -> **Severity: 4.013** (Embedded: 0.0429 * Error Risk: 93.4745%)
- `v4.0/src/INC/POSTEQU.INC` -> **Severity: 2.341** (Embedded: 0.0234 * Error Risk: 100.0%)
- `v4.0/src/SELECT/SELECT.INC` -> **Severity: 1.149** (Embedded: 0.0117 * Error Risk: 98.177%)
- `v4.0/src/INC/STRUC.INC` -> **Severity: 1.144** (Embedded: 0.0556 * Error Risk: 20.5694%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `v4.0/src/INC/STRUC.INC` -> **Severity: 1749.561** (Blast Radius: 17.933 * Doc Risk: 97.561%)
- `v4.0/src/INC/SYSMSG.INC` -> **Severity: 1655.201** (Blast Radius: 16.553 * Doc Risk: 99.994%)
- `v4.0/src/INC/POSTEQU.INC` -> **Severity: 1520.0** (Blast Radius: 15.2 * Doc Risk: 100.0%)
- `v4.0/src/INC/DOSSYM.INC` -> **Severity: 1019.822** (Blast Radius: 49.728 * Doc Risk: 20.508%)
- `v4.0/src/SELECT/EXT.INC` -> **Severity: 806.6** (Blast Radius: 8.066 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
