# ARCHITECTURAL_BRIEF: MS-DOS
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/microsoft/MS-DOS.git` |
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
- **Scope:** 1003 analyzed artifact(s), 302687 LOC.
- **Load-bearing artifact:** `v4.0/src/INC/DOSSYM.INC` -- 94 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `v4.0/src/INC/DOSSYM.INC` -- pulls in 22 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `v4.0/src/SELECT/GET_STAT.C` at magnitude 9778.12 (structural weight, not risk).
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
| Total Artifacts | 1555 |
| Analyzed Artifacts (Scanned) | 1003 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 552 |
| Total LOC | 302687 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 64.5% |
| Dominant Lang | ASSEMBLY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7973 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2851 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0083 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 98 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 828 | 274405 | 82.6% |
| C | 148 | 27817 | 14.8% |
| PLAINTEXT | 8 | 0 | 0.8% |
| BATCH | 7 | 128 | 0.7% |
| MAKEFILE | 7 | 307 | 0.7% |
| MARKDOWN | 3 | 0 | 0.3% |
| LIVECODE | 2 | 30 | 0.2% |

## 4.1 SOURCE ENCODINGS
> 102 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 901 |
| cp1252 | cp1252-fallback | 80 |
| latin-1 | latin-1-fallback | 22 |

> 50 guessed file(s) read as double-byte text that decodes strictly as shift_jis: if that is the estate's code page, rescan with `--source-encoding shift_jis` (or the right one of those). E.g. `v4.0/src/CMD/FASTOPEN/FASTOPEN.TXT`, `v4.0/src/CMD/CHKDSK/CHKINIT.ASM`, `v4.0/src/CMD/FASTOPEN/FASTINIT.ASM`, `v4.0/src/CMD/FORMAT/FOREXEC.ASM`, `v4.0/src/CMD/FORMAT/FORINIT.ASM` and 45 more.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 47%, Parameter Forwarders Files 17%, Large Core Modules (3) 16%, Large Core Modules 6%, Data / Markup / Trivial 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 992 | 98.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 552*

**Composition by Extension & Reason:**
- `.asm`: 62x Excluded (Binary Format Detected), 15x Zero-Density Threshold (LOC: 256, Signals: 0), 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 68x Unsupported Format (.undeterminable), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unresolved Ambiguity (No Retainable Structure)
- `.lnk`: 50x Unsupported Format (.lnk), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skl`: 48x Unsupported Format (.skl), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.exe`: 45x Excluded (Explicitly Denied Extension: '.EXE')
- `.com`: 29x Excluded (Binary Format Detected)
- `.md`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inc`: 2x Zero-Density Threshold (LOC: 64, Signals: 0), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 5603 commas in 802 LOC)
- `.lib`: 19x Excluded (Explicitly Denied Extension: '.LIB')
- `.obj`: 18x Excluded (Explicitly Denied Extension: '.OBJ')
- `.equ`: 17x Unsupported Format (.equ)
- `.doc`: 15x Excluded (Explicitly Denied Extension: '.DOC')
- `.bas`: 13x Excluded (Binary Format Detected), 1x Excluded (Unsupported Extension: '.BAS')
- `.ext`: 14x Unsupported Format (.ext)
- `.pdf`: 12x Excluded (Explicitly Denied Extension: '.pdf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 81.5 | 6.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 88.6 | 22.5 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 21.7 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 10.0 | 3.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 45.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7049 | 373 | 18 | `v2.0/source/DEBASM.ASM` |
| cleanup | 8 | 6 | 0 | `v4.0/src/TOOLS/BLD/INC/IO.H` |
| guards | 8966 | 499 | 25 | `v2.0/source/DOSSYM_v211.ASM` |
| danger | 994 | 160 | 1 | `v4.0/src/CMD/BACKUP/BACKUP.C` |
| concurrency | 730 | 161 | 2 | `v1.25/source/ASM.ASM` |
| connectivity | 6741 | 613 | 15 | `v4.0/src/CMD/FDISK/DOSCALL.H` |
| io | 667 | 71 | 0 | `v4.0/src/DEV/XMA2EMS/DIAGS.ASM` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 20 | 6 | 0 | `v4.0/src/TOOLS/BLD/INC/TIME.H` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 314 | 92 | 0 | `v1.25/source/COMMAND.ASM` |
| tests | 43 | 10 | 0 | `v4.0/src/CMD/RESTORE/RTOLD1.C` |
| docs | 1269 | 91 | 0 | `v4.0/src/CMD/FDISK/DOSCALL.H` |
| debt | 528 | 134 | 1 | `v4.0/src/CMD/BACKUP/BACKUP.C` |
| mutation | 14234 | 476 | 29 | `v4.0/src/CMD/BACKUP/BACKUP.C` |
| dead_code | 5162 | 392 | 14 | `v4.0/src/DOS/EXTATTR.ASM` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 30 | 8 | 0 | `v4.0/src/CMD/FDISK/FDISKMSG.C` |
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
4. **DOSSYM.ASM** (`v2.0/source/DOSSYM.ASM`) — 18 inbound connections
5. **CASTRUC.INC** (`v4.0/src/SELECT/CASTRUC.INC`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **DOSSYM.INC** (`v4.0/src/INC/DOSSYM.INC`) — 22 outbound dependencies
2. **SMDOSSYM.INC** (`v4.0/src/INC/SMDOSSYM.INC`) — 17 outbound dependencies
3. **MEMMINC.ASM** (`v4.0/src/MEMM/MEMM/MEMMINC.ASM`) — 17 outbound dependencies
4. **KEYBCMD.ASM** (`v4.0/src/CMD/KEYB/KEYBCMD.ASM`) — 16 outbound dependencies
5. **STDDATA.ASM** (`v4.0/src/DOS/STDDATA.ASM`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `START` **(Many-Argument Workhorses)** (@ `v4.0/src/CMD/SYS/SYS1.ASM`) -> Impact: **312.7** | LOC: 3343
- `main` **(Many-Argument Workhorses)** (@ `v4.0/src/CMD/REPLACE/REPLACE.C`) -> Impact: **240.3** | LOC: 476
  * *Intent:* /* dexit load_msg */ /* dfree parser_prep */ /* display_exit putbyte */ /* display_msg putdword */ /* doadd putword */ /* docopy restore */ /* dodir s...
- `restore_a_file` **(Many-Argument Workhorses)** (@ `v4.0/src/CMD/RESTORE/RTFILE.C`) -> Impact: **209.1** | LOC: 542
  * *Intent:* /* file under the proper path. If the path is not found, build */ /* the path. */ /* It then enter a loop to do reading the source disk and */ /* writ...
- `START` **(Many-Argument Workhorses)** (@ `v4.0/src/CMD/TREE/TREE.ASM`) -> Impact: **184.9** | LOC: 1476
- `valid_input_date` **(Many-Argument Workhorses)** (@ `v4.0/src/CMD/RESTORE/RTT2.C`) -> Impact: **161.6** | LOC: 236
  * *Intent:* /* */ /* EFFECTS: */ /* */ /* INTERNAL REFERENCES: */ /* ROUTINES: */ /* usererror */ /* unexperror */ /* putmsg */ /* set_reset_test_flag */ /* */ /*...
- `check_target_filespec` **(Many-Argument Workhorses)** (@ `v4.0/src/CMD/RESTORE/RESTPARS.C`) -> Impact: **135.4** | LOC: 353
  * *Intent:* /* for user to "Insert diskette for drive %1" */ qregs.x.ax = SETLOGICALDRIVE; /*;AN000;8*/ qregs.h.bl = srcddir[0] - 'A' + 1; /*;AN000;8*/ intdos(&qr...
- `next_level_down` **(Many-Argument Workhorses)** (@ `v4.0/src/CMD/SYS/SYS2.ASM`) -> Impact: **133.5** | LOC: 1083
- `search_src_disk_old` **(Many-Argument Workhorses)** (@ `v4.0/src/CMD/RESTORE/RTOLD.C`) -> Impact: **131.0** | LOC: 219
  * *Intent:* /* cammand line. */ /* */ /* Whenever there is a file found, subroutine filespecmatch */ /* is called to match the file path, and file extension. */ /...
- `findfile_new` **(Many-Argument Workhorses)** (@ `v4.0/src/CMD/RESTORE/RTNEW1.C`) -> Impact: **123.9** | LOC: 201
  * *Intent:* /* /* SUBROUTINE NAME : findfile_new /* /* DESCRIPTIVE NAME : Find a file with matching file name from /* the file CONTROL.xxx. /* /* FUNCTION: For ne...
- `dorestore` **(Many-Argument Workhorses)** (@ `v4.0/src/CMD/RESTORE/RTDO.C`) -> Impact: **120.3** | LOC: 313
  * *Intent:* /* 5. Check whether the diskette contains old or new data /* format. /* 6. ouput "file were backup xx-xx-xx" /* /* For each diskette, do the following...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `v4.0/src/CMD/FDISK` | 38 | 38859.17 | 28.57% | 0.0% |
| `v4.0/src/SELECT` | 61 | 12774.88 | 3.55% | 8.04% |
| `v4.0/src/DOS` | 83 | 7948.24 | 6.84% | 15.57% |
| `v2.0/source` | 39 | 6435.04 | 6.71% | 11.01% |
| `v1.25/source` | 7 | 5660.06 | 13.55% | 17.83% |
| `v4.0/src/CMD/COMMAND` | 39 | 5585.86 | 7.21% | 37.21% |
| `v4.0/src/BIOS` | 34 | 4848.54 | 5.56% | 15.93% |
| `v4.0/src/DEV/PRINTER` | 10 | 4777.06 | 13.09% | 21.08% |
| `v4.0/src/INC` | 76 | 4486.32 | 5.44% | 4.32% |
| `v4.0/src/CMD/RESTORE` | 23 | 3967.96 | 18.0% | 32.2% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `v4.0/src/DEV/XMAEM/XMAEM.MAK` -> **100.0%** Exposure
- `v4.0/src/DEV/XMAEM/INDEEMU.ASM` -> **99.9932%** Exposure
- `v2.0/source/MSHEAD.ASM` -> **99.9925%** Exposure
- `v4.0/src/INC/MSHEAD.ASM` -> **99.9925%** Exposure
- `v4.0/src/DEV/XMAEM/INDEI15.ASM` -> **99.972%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `v4.0/src/CMD/ATTRIB/ATTRIB.C` -> **100.0%** Exposure
- `v4.0/src/CMD/BACKUP/BACKUP.C` -> **100.0%** Exposure
- `v4.0/src/CMD/FC/FC.C` -> **100.0%** Exposure
- `v4.0/src/CMD/FC/FGETL.C` -> **100.0%** Exposure
- `v4.0/src/CMD/FC/NTOI.C` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `v4.0/src/DEV/PRINTER/CPSPM10.ASM` -> **136** Orphaned Functions | **0** Duplicates
- `v4.0/src/CMD/FASTOPEN/FASTINIT.ASM` -> **70** Orphaned Functions | **0** Duplicates
- `v4.0/src/DEV/SMARTDRV/SMARTDRV.ASM` -> **55** Orphaned Functions | **2** Duplicates
- `v4.0/src/DEV/RAMDRIVE/RAMDRIVE.ASM` -> **45** Orphaned Functions | **2** Duplicates
- `v4.0/src/INC/SHELLRD.INC` -> **43** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `46` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2385` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `v4.0/src/SELECT/GET_STAT.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.806)
- **Top Global Matches:** file_cluster_2: 3.806, file_cluster_17: 4.814, file_cluster_15: 5.646
- **Magnitude:** 9778.12 | **LOC:** 1217 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.4%), Connectivity (formerly Api Exposure) (66.3%), Complexity Load (formerly Cognitive Load) (49.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 168 instances
* *State Mutation (weighted view):* 616
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 62`, `args: 55`, `func_start: 16`, `class_start: 4`
* *Risk/State:* `state_mutation: 280`, `dead_code: 5`
* *Architecture:* `api: 39`, `import: 6`
* *Defense:* `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dos.h, extern.h, get_stat.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/D_MENUS.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.251)
- **Top Global Matches:** file_cluster_12: 5.251, file_cluster_7: 6.403, file_cluster_2: 6.506
- **Magnitude:** 5845.18 | **LOC:** 942 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.5%), Complexity Load (formerly Cognitive Load) (55.3%), Connectivity (formerly Api Exposure) (5.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 60 instances
* *State Mutation (weighted view):* 240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 25`, `args: 42`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 120`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, dos.h, extern.h, fdisk.h, fdiskmsg.h, stdio.h, string.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/FDISK.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.524)
- **Top Global Matches:** file_cluster_12: 5.524, file_cluster_2: 5.851, file_cluster_17: 6.769
- **Magnitude:** 5802.42 | **LOC:** 1122 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.1%), Connectivity (formerly Api Exposure) (56.6%), Complexity Load (formerly Cognitive Load) (53.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 282
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 24`, `args: 33`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 144`
* *Architecture:* `api: 11`, `import: 11`
* *Defense:* `safety: 1`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, dos.h, doscall.h, extern.h, fdisk.h, fdiskmsg.h, msgret.h, process.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/C_MENUS.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.372)
- **Top Global Matches:** file_cluster_12: 5.372, file_cluster_7: 5.489, file_cluster_2: 7.627
- **Magnitude:** 5634.04 | **LOC:** 1068 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.8%), Complexity Load (formerly Cognitive Load) (52.3%), Connectivity (formerly Api Exposure) (5.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 18`, `args: 38`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 76`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dos.h, extern.h, fdisk.h, fdiskmsg.h, stdio.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/INPUT.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.684)
- **Top Global Matches:** file_cluster_2: 3.684, file_cluster_17: 4.918, file_cluster_15: 5.767
- **Magnitude:** 5558.71 | **LOC:** 674 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.3%), Complexity Load (formerly Cognitive Load) (69.8%), Connectivity (formerly Api Exposure) (6.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 251
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 31`, `args: 23`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 109`
* *Architecture:* `api: 8`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, dos.h, doscall.h, extern.h, fdisk.h, fdiskmsg.h, stdio.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/BACKUP/BACKUP.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.159)
- **Top Global Matches:** file_cluster_4: 9.159, file_cluster_12: 9.194, file_cluster_7: 10.651
- **Magnitude:** 2333.78 | **LOC:** 4385 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 2.075; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%), Connectivity (formerly Api Exposure) (61.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `display_msg` **(Compute Cores)** (Impact: 56.7)
    * *Intent:* /************************************************************/
  * `check_path_validity` **(Compute Cores)** (Impact: 45.6)
    * *Intent:* sublist.one = 0; /*;AN000;p2592*/ sublist.max_width1 = (BYTE)strlen(t); /*;AN000;p2592*/ sublist.min...
  * `check_date` **(Compute Cores)** (Impact: 33.6)
    * *Intent:* else /*;AN000;4*/ display_it (ax,STDERR,1,NOWAIT,(BYTE)PARSEERROR); /*;AN000;6*/ return_code = RETCO...
  * `parser` **(Many-Argument Workhorses)** (Impact: 28.3)
    * *Intent:* dta_addr = (struct FileFindBuf *)&dta; /* Get address of FindFile buffer */ return; /*;AN000;6*/ } /...
  * `see_if_it_should_be_backed_up` **(I/O & Config Routines)** (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 377 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 1335
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 453`, `structural_boundaries: 254`, `args: 143`, `func_start: 92`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 109`, `high_risk_execution: 1`, `state_mutation: 581`, `dead_code: 35`, `fragile_debt: 17`
* *Architecture:* `api: 93`, `import: 10`
* *Defense:* `doc: 203`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00289
  * `Imports (Out-Degree: 0):` backpars.h, backup.h, direct.h, dos.h, doscalls.h, malloc.h, process.h, stdlib.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `v4.0/src/CMD/FDISK/DISPLAY.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.526)
- **Top Global Matches:** file_cluster_2: 4.526, file_cluster_17: 5.553, file_cluster_15: 6.167
- **Magnitude:** 2250.84 | **LOC:** 407 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.5%), Complexity Load (formerly Cognitive Load) (64.8%), Dead Code Surface (formerly Dead Code) (8.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 25`, `args: 12`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 82`, `dead_code: 1`
* *Architecture:* `api: 6`, `import: 8`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, dos.h, doscall.h, extern.h, fdisk.h, fdiskmsg.h, stdio.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/MAIN.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.355)
- **Top Global Matches:** file_cluster_2: 4.355, file_cluster_17: 5.779, file_cluster_15: 6.375
- **Magnitude:** 2205.17 | **LOC:** 333 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.9%), Complexity Load (formerly Cognitive Load) (45.4%), Connectivity (formerly Api Exposure) (3.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 1`, `args: 17`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 18`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, dos.h, doscall.h, extern.h, fdisk.h, fdiskmsg.h, msgret.h, process.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v1.25/source/ASM.ASM` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.811)
- **Top Global Matches:** file_cluster_15: 5.811, file_cluster_11: 7.266, file_cluster_16: 8.155
- **Magnitude:** 1825.8 | **LOC:** 4006 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); blast radius 8.616; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.5%), Complexity Load (formerly Cognitive Load) (20.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NWAIT` **(Many-Argument Workhorses)** (Impact: 29.0)
  * `FACTOR` **(Compute Cores)** (Impact: 25.5)
  * `REGCHK` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `GRP3` **(Compute Cores)** (Impact: 21.5)
  * `MROPS` **(Many-Argument Workhorses)** (Impact: 19.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 401
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 319`, `structural_boundaries: 1755`, `args: 1914`, `func_start: 477`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 151`, `fragile_debt: 1`, `unreferenced_by_name: 23`
* *Architecture:* None
* *Defense:* `sync_locks: 47`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015742
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `v1.25/source/MSDOS.ASM` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.332)
- **Top Global Matches:** file_cluster_15: 6.332, file_cluster_11: 7.444, file_cluster_16: 8.496
- **Magnitude:** 1710.58 | **LOC:** 4031 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); blast radius 3.142; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (76.8%), Guard Balance (formerly Safety Score) (55.2%), Connectivity (formerly Api Exposure) (47.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SETDATE` **(Many-Argument Workhorses)** (Impact: 16.9)
  * `SMALREC` **(Type Conversions)** (Impact: 12.8)
  * `LOAD` **(Type Conversions)** (Impact: 12.5)
  * `INCHK` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `GETCH` **(Compute Cores)** (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 1820`, `args: 1835`, `func_start: 404`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 141`, `dead_code: 1`, `fragile_debt: 3`
* *Architecture:* `api: 31`
* *Defense:* `sync_locks: 22`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00822
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `v4.0/src/DEV/SMARTDRV/SMARTDRV.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.218)
- **Top Global Matches:** file_cluster_15: 7.218, file_cluster_12: 7.951, file_cluster_11: 8.332
- **Magnitude:** 1694.0 | **LOC:** 7587 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.664; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (57.2%), Guard Balance (formerly Safety Score) (54.3%), Mutation Surface (formerly State Flux) (48.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pbw$4` **(Many-Argument Workhorses)** (Impact: 23.3)
    * *Intent:* ; ; error exit ;
  * `FIRST_ARG` **(Compute Cores)** (Impact: 20.2)
  * `do_it` **(Many-Argument Workhorses)** (Impact: 18.3)
  * `CHECK_SYS` **(Compute Cores)** (Impact: 15.1)
  * `GET_AVAIL` **(Compute Cores)** (Impact: 13.5)
    * *Intent:* ; ; Allocate drive memory ;
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 247
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 2077`, `args: 1977`, `func_start: 393`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 1`, `state_mutation: 97`, `dead_code: 35`, `fragile_debt: 8`, `duplicate_logic: 2`, `unreferenced_by_name: 55`
* *Architecture:* `io: 21`, `api: 18`, `import: 7`
* *Defense:* `sync_locks: 14`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ab_macro.asm, above.asm, devsym.asm, emm.asm, loadall.asm, mi.asm, syscall.asm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/PROFILE.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.4)
- **Top Global Matches:** file_cluster_2: 2.4, file_cluster_17: 4.588, file_cluster_15: 5.627
- **Magnitude:** 1565.09 | **LOC:** 802 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.2%), Complexity Load (formerly Cognitive Load) (56.8%), Connectivity (formerly Api Exposure) (30.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 378
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 23`, `args: 2`, `func_start: 5`
* *Risk/State:* `state_mutation: 166`, `dead_code: 3`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, doscall.h, fdiskc.msg, profile.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/REPLACE/REPLACE.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.526)
- **Top Global Matches:** file_cluster_4: 9.526, file_cluster_6: 11.574, file_cluster_12: 12.838
- **Magnitude:** 1533.18 | **LOC:** 2048 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.6%), Complexity Load (formerly Cognitive Load) (73.3%)
- **Documentation Coverage:** 65.7895% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 240.3)
    * *Intent:* /* dexit load_msg */ /* dfree parser_prep */ /* display_exit putbyte */ /* display_msg putdword */ /...
  * `display_msg` **(Many-Argument Workhorses)** (Impact: 97.5)
    * *Intent:* /* outline (string for replacement parm) */ /* */ /* OUTPUT: none */ /* */ /* NORMAL EXIT: The corre...
  * `docopy` **(Many-Argument Workhorses)** (Impact: 89.6)
    * *Intent:* /*ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ*/
  * `dodir` **(Many-Argument Workhorses)** (Impact: 38.3)
    * *Intent:* /*ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ*/
  * `doadd` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* /*ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 194 instances
* *State Mutation (weighted view):* 820
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 140`, `args: 37`, `func_start: 38`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 73`, `high_risk_execution: 1`, `state_mutation: 432`, `unreferenced_by_name: 1`
* *Architecture:* `api: 42`, `import: 3`
* *Defense:* `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` comsub.h, dos.h, replacep.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/ATTRIB/ATTRIB.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.46)
- **Top Global Matches:** file_cluster_6: 8.46, file_cluster_4: 12.933, file_cluster_8: 15.627
- **Magnitude:** 1486.9 | **LOC:** 2686 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Parse_it` **(Many-Argument Workhorses)** (Impact: 86.2)
    * *Intent:* /* Output: various control variables are set */ /* */ /* Normal exit: status = NOERROR */ /* */ /* E...
  * `Extended_attrib` **(Many-Argument Workhorses)** (Impact: 56.9)
    * *Intent:* /* Output: none */ /* */ /* Normal exit: */ /* */ /* Error exit: None */ /* */ /* Internal Reference...
  * `Print_ext_attrib` **(Many-Argument Workhorses)** (Impact: 52.3)
    * *Intent:* /* Output: none */ /* */ /* Normal exit: target = source */ /* */ /* Error exit: None */ /* */ /* In...
  * `Do_dir` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* /* Output: none */ /* */ /* Normal exit: */ /* */ /* Error exit: None */ /* */ /* Internal Reference...
  * `Special_attrib` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* /* Output: none */ /* */ /* Normal exit: */ /* */ /* Error exit: None */ /* */ /* Internal Reference...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 271 instances
* *State Mutation (weighted view):* 1015
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 98`, `args: 19`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 61`, `high_risk_execution: 3`, `state_mutation: 473`, `dead_code: 13`
* *Architecture:* `api: 24`, `import: 7`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` attrib.h, dos.h, io.h, msgret.h, parse.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/DEV/PRINTER/CPSPM10.ASM` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.489)
- **Top Global Matches:** file_cluster_15: 5.489, file_cluster_11: 6.907, file_cluster_16: 8.052
- **Magnitude:** 1470.4 | **LOC:** 3852 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.805; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Debt Markers (formerly Tech Debt) (94.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DST_SLTLP` **(Many-Argument Workhorses)** (Impact: 13.0)
  * `DST_BUFNXT` **(Many-Argument Workhorses)** (Impact: 10.2)
    * *Intent:* ;; ;; ;; **** NEXT IN LOOP ****
  * `DST_BUFLP` **(Many-Argument Workhorses)** (Impact: 9.6)
    * *Intent:* ;;
  * `SET_DID` **(Many-Argument Workhorses)** (Impact: 9.4)
    * *Intent:* ;;
  * `COMMON_INTR` **(Type Conversions)** (Impact: 9.1)
    * *Intent:* ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; ; ; Common interrupt entry : ; at entry, BUFn (CS:BX) of ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 136 instances
* *State Mutation (weighted view):* 440
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 1365`, `args: 1445`, `func_start: 348`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 168`, `dead_code: 4`, `unreferenced_by_name: 136`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.805
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000963
  * `Imports (Out-Degree: 1):` CPSPEQU.INC
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `v4.0/src/CMD/FDISK/SPACE.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.365)
- **Top Global Matches:** file_cluster_2: 3.365, file_cluster_17: 5.194, file_cluster_15: 5.993
- **Magnitude:** 1436.43 | **LOC:** 440 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.5%), Complexity Load (formerly Cognitive Load) (64.1%), Dead Code Surface (formerly Dead Code) (17.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 8`, `args: 5`, `func_start: 4`
* *Risk/State:* `state_mutation: 130`, `dead_code: 5`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dos.h, extern.h, fdisk.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/DEV/RAMDRIVE/RAMDRIVE.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.19)
- **Top Global Matches:** file_cluster_15: 7.19, file_cluster_12: 8.331, file_cluster_11: 8.38
- **Magnitude:** 1219.02 | **LOC:** 6218 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.882; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (75.5%), Guard Balance (formerly Safety Score) (52.9%), Mutation Surface (formerly State Flux) (28.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FIRST_ARG` **(Compute Cores)** (Impact: 23.8)
  * `CHECK_DOS_VOL` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* ; EXIT: ; CARRY SET - error, message already printed ; CARRY CLEAR ; INIT_DRIVE set ; SECTOR_BUFFER ...
  * `GET_AVAIL` **(Compute Cores)** (Impact: 16.8)
    * *Intent:* ; ; Allocate drive memory ;
  * `CHECK_SYS` **(Compute Cores)** (Impact: 15.1)
  * `FATSUB` **(Compute Cores)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 1434`, `args: 1378`, `func_start: 308`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 50`, `dead_code: 76`, `planned_debt: 1`, `fragile_debt: 11`, `duplicate_logic: 2`, `unreferenced_by_name: 45`
* *Architecture:* `io: 17`, `import: 8`
* *Defense:* `safety: 3`, `sync_locks: 5`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.882
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00536
  * `Imports (Out-Degree: 0):` ab_macro.inc, above.inc, devsym.inc, dirent.inc, emm.inc, loadall.inc, mi.inc, syscall.inc
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `v4.0/src/CMD/FDISK/DISKOUT.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.132)
- **Top Global Matches:** file_cluster_2: 3.132, file_cluster_17: 4.902, file_cluster_15: 5.772
- **Magnitude:** 1186.8 | **LOC:** 355 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.4%), Complexity Load (formerly Cognitive Load) (62.1%), Connectivity (formerly Api Exposure) (5.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 184
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 8`, `args: 9`, `func_start: 3`
* *Risk/State:* `state_mutation: 102`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dos.h, extern.h, fdisk.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/VDISPLAY.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.726)
- **Top Global Matches:** file_cluster_2: 4.726, file_cluster_17: 5.909, file_cluster_15: 6.672
- **Magnitude:** 1154.21 | **LOC:** 180 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.6%), Complexity Load (formerly Cognitive Load) (70.0%), Connectivity (formerly Api Exposure) (4.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 1`, `args: 13`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dos.h, extern.h, fdisk.h, fdiskmsg.h, memory.h, stdio.h, string.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/PARTINFO.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.264)
- **Top Global Matches:** file_cluster_2: 3.264, file_cluster_17: 4.627, file_cluster_15: 5.365
- **Magnitude:** 1140.66 | **LOC:** 262 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.7%), Complexity Load (formerly Cognitive Load) (65.9%), Connectivity (formerly Api Exposure) (8.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 25`, `args: 12`, `func_start: 10`
* *Risk/State:* `state_mutation: 28`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dos.h, extern.h, fdisk.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FDISK/CONVERT.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.512)
- **Top Global Matches:** file_cluster_2: 4.512, file_cluster_17: 4.847, file_cluster_15: 6.138
- **Magnitude:** 1130.65 | **LOC:** 479 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.664; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.9%), Complexity Load (formerly Cognitive Load) (31.9%), Connectivity (formerly Api Exposure) (7.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 10`, `args: 10`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 62`
* *Architecture:* `api: 10`, `import: 6`
* *Defense:* `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, dos.h, extern.h, fdisk.h, string.h, subtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/INC/PCINPUT.INC` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.133)
- **Top Global Matches:** file_cluster_15: 5.133, file_cluster_11: 6.726, file_cluster_16: 7.867
- **Magnitude:** 1087.04 | **LOC:** 3795 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (76.8%), Guard Balance (formerly Safety Score) (54.4%), Debt Markers (formerly Tech Debt) (18.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LF160` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* ; buffer ; ; Completed updating LVB, adjust pointers
  * `LS160` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* ; buffer ;=W ; ;=W ; Completed updating LVB, adjust pointers ;=W
  * `LF130` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* ; ; Byte is a single byte character
  * `LS130` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* ; ;=W ; Byte is a single byte character ;=W
  * `LF80` **(Compute Cores)** (Impact: 11.0)
    * *Intent:* ; ; Double byte character fits on current row
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 1327`, `args: 1529`, `func_start: 217`
* *Risk/State:* `state_mutation: 79`, `dead_code: 3`, `fragile_debt: 1`, `unreferenced_by_name: 11`
* *Architecture:* `io: 5`
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/INC/SHELLRD.INC` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.27)
- **Top Global Matches:** file_cluster_15: 5.27, file_cluster_11: 6.773, file_cluster_16: 7.994
- **Magnitude:** 1062.52 | **LOC:** 5112 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (32.3%), Debt Markers (formerly Tech Debt) (29.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BEXIT` **(Many-Argument Workhorses)** (Impact: 38.0)
    * *Intent:* ;
  * `GIEXIT` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* ;if in text mode deactivate box ; option ;
  * `PH10` **(Compute Cores)** (Impact: 13.5)
    * *Intent:* ; ; display mouse pointer ;
  * `CR_EXIT` **(Many-Argument Workhorses)** (Impact: 10.2)
    * *Intent:* ;
  * `EP370` **(Compute Cores)** (Impact: 9.8)
    * *Intent:* ;
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 1869`, `args: 1331`, `func_start: 254`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`, `dead_code: 1`, `unreferenced_by_name: 43`
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `v4.0/src/CMD/FORMAT/FORMAT.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.248)
- **Top Global Matches:** file_cluster_15: 7.248, file_cluster_11: 8.314, file_cluster_16: 9.176
- **Magnitude:** 928.14 | **LOC:** 4509 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **15**; blast radius 5.298; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.3%), Debt Markers (formerly Tech Debt) (25.6%), Mutation Surface (formerly State Flux) (18.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Scan_Disk_Table_Exit` **(Many-Argument Workhorses)** (Impact: 108.8)
  * `Ctrl_Break_Write` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* ;========================================================================= ; Ctrl_Break_Write : This...
  * `Write_Exit` **(Many-Argument Workhorses)** (Impact: 27.4)
  * `Keep_Going` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `BAD100` **(Many-Argument Workhorses)** (Impact: 16.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 1560`, `args: 1217`, `func_start: 136`
* *Risk/State:* `state_mutation: 34`, `dead_code: 6`, `fragile_debt: 5`, `unreferenced_by_name: 19`
* *Architecture:* `io: 1`, `api: 174`, `import: 15`
* *Defense:* `sync_locks: 2`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.298
  * `Choke Point (Betweenness):` 0.000381 | `Ripple Effect (Closeness):` 0.009424
  * `Imports (Out-Degree: 15):` BPB.INC, CPMFCB.INC, CURDIR.INC, DIRENT.INC, DOSMAC.INC, DPB.INC, ERROR.INC, FOREQU.INC...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `v4.0/src/CMD/APPEND/APPEND.ASM` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.429)
- **Top Global Matches:** file_cluster_15: 6.429, file_cluster_11: 7.532, file_cluster_16: 8.662
- **Magnitude:** 887.8 | **LOC:** 3462 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.735; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (60.5%), Guard Balance (formerly Safety Score) (52.6%), Dead Code Surface (formerly Dead Code) (38.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `no_dbcs2` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* ; we go back through ;AN006;
  * `found_it_remote` **(Many-Argument Workhorses)** (Impact: 11.9)
  * `abort_exit` **(Type Conversions)** (Impact: 11.1)
  * `got_the_end` **(Type Conversions)** (Impact: 10.6)
  * `ccn_20` **(State Mutators)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 1089`, `args: 811`, `func_start: 238`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 38`, `dead_code: 83`, `fragile_debt: 2`, `unreferenced_by_name: 36`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000963
  * `Imports (Out-Degree: 0):` appendp.inc, msgdcl.inc, parse.asm, pdb.inc, sysmac.lib, sysmsg.inc, versiona.inc
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `v4.0/src/MEMM/MEMM/RRTRAP.ASM` (ASSEMBLY) | Magnitude: 19.78 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 119, structural_boundaries: 85, args: 41, pointers: 33
- `v4.0/src/SELECT/ROUTINE2.ASM` (ASSEMBLY) | Magnitude: 121.06 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 382, indent_spaces: 329, args: 280, pointers: 34
- `v4.0/src/BIOS/MSSTACK.INC` (ASSEMBLY) | Magnitude: 35.02 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 122, structural_boundaries: 59, args: 35, branch: 11
- `v4.0/src/SELECT/PRN_DEF.ASM` (ASSEMBLY) | Magnitude: 139.72 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 463, indent_spaces: 425, args: 325, globals: 46
- `v4.0/src/MEMM/MEMM/ROM_SRCH.ASM` (ASSEMBLY) | Magnitude: 46.04 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 107, structural_boundaries: 74, args: 64, bitwise_ops: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `v4.0/src/CMD/GRAPHICS/GRPARMS.ASM` (ASSEMBLY) | Magnitude: 36.52 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 192, structural_boundaries: 129, args: 114, indent_spaces: 39
- `v4.0/src/MEMM/MEMM/SHIPHI.ASM` (ASSEMBLY) | Magnitude: 28.1 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 72, structural_boundaries: 53, args: 53, func_start: 7
- `v4.0/src/MAPPER/KBDSSTAT.ASM` (ASSEMBLY) | Magnitude: 29.38 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 26, args: 23, bitwise_ops: 12
- `v4.0/src/MEMM/MEMM/VMTRAP.ASM` (ASSEMBLY) | Magnitude: 99.5 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 252, structural_boundaries: 154, args: 41, api: 36
- `v4.0/src/CMD/GRAPHICS/GRLOAD2.ASM` (ASSEMBLY) | Magnitude: 38.16 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 231, args: 216, indent_spaces: 194, bitwise_ops: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `v4.0/src/DEV/PRINTER/PARSER.ASM` (ASSEMBLY) | Magnitude: 35.22 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 162, args: 117, indent_tabs: 46, state_mutation: 13
- `v4.0/src/INC/DIRENT.INC` (ASSEMBLY) | Magnitude: 15.48 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: globals: 11, immutability_locks: 10, class_start: 1
- `v4.0/src/SELECT/SEL_FILE.INC` (ASSEMBLY) | Magnitude: 108.54 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: globals: 170, indent_tabs: 156, immutability_locks: 94, api: 85
- `v2.0/source/COMSW.ASM` (ASSEMBLY) | Magnitude: 14.68 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: immutability_locks: 8, bitwise_ops: 1
- `v4.0/src/DEV/COUNTRY/MKCNTRY.INC` (ASSEMBLY) | Magnitude: 17.28 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: immutability_locks: 64, indent_spaces: 34, globals: 6, class_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `v4.0/src/INC/CURDIR.INC` (ASSEMBLY) | Magnitude: 15.44 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: globals: 9, immutability_locks: 9, class_start: 1, explicit_casts: 1
- `v4.0/src/INC/VECTOR.INC` (ASSEMBLY) | Magnitude: 15.88 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: immutability_locks: 37, indent_tabs: 5, bitwise_ops: 1
- `v4.0/src/INC/SMIFSSYM.INC` (ASSEMBLY) | Magnitude: 15.66 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: immutability_locks: 14, globals: 10, indent_spaces: 7, class_start: 2
- `v4.0/src/SELECT/ASM2C.ASM` (ASSEMBLY) | Magnitude: 20.9 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 49, structural_boundaries: 37, globals: 23, args: 20
- `v4.0/src/CMD/EXE2BIN/E2BPARSE.INC` (ASSEMBLY) | Magnitude: 16.94 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: immutability_locks: 43, globals: 20, indent_spaces: 20, class_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `v4.0/src/CMD/BACKUP/BACKUP.C` (C) | Magnitude: 2333.78 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 968, state_mutation: 581, branch: 453, core_var_decl: 340

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `v4.0/src/CMD/EDLIN/EDLCMD2.ASM` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 84.8122%)
- `v4.0/src/BIOS/SYSINIT2.ASM` -> **Severity: 0.01** (Bridge: 0.0002 * Flux: 54.0207%)
- `v4.0/src/BIOS/SYSINIT1.ASM` -> **Severity: 0.007** (Bridge: 0.0002 * Flux: 41.9358%)
- `v4.0/src/CMD/FORMAT/FORMAT.ASM` -> **Severity: 0.007** (Bridge: 0.0004 * Flux: 18.596%)
- `v2.0/source/RECOVER.ASM` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 88.1507%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `v4.0/src/INC/STRUC.INC` -> **Severity: 2.402** (Embedded: 0.0479 * Error Risk: 50.1484%)
- `v4.0/src/INC/MSGSERV.ASM` -> **Severity: 1.256** (Embedded: 0.0229 * Error Risk: 54.9086%)
- `v1.25/source/ASM.ASM` -> **Severity: 0.873** (Embedded: 0.0157 * Error Risk: 55.4672%)
- `v4.0/src/CMD/RESTORE/RTT3.C` -> **Severity: 0.859** (Embedded: 0.0116 * Error Risk: 74.3204%)
- `v4.0/src/DEV/SMARTDRV/FLUSH13.C` -> **Severity: 0.511** (Embedded: 0.0069 * Error Risk: 74.5618%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `v1.25/source/ASM.ASM` -> **Severity: 861.6** (Blast Radius: 8.616 * Doc Risk: 100.0%)
- `v4.0/src/CMD/FORMAT/FORMAT.ASM` -> **Severity: 529.8** (Blast Radius: 5.298 * Doc Risk: 100.0%)
- `v4.0/src/CMD/EDLIN/EDLCMD2.ASM` -> **Severity: 355.2** (Blast Radius: 3.552 * Doc Risk: 100.0%)
- `v4.0/src/SELECT/MACROS8.INC` -> **Severity: 341.7** (Blast Radius: 3.417 * Doc Risk: 100.0%)
- `v4.0/src/INC/IOCTL.INC` -> **Severity: 334.0** (Blast Radius: 3.34 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6677 call pairs -- scoped 32.2%, unique 5.9%, ambiguous 3.1%, external 58.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| assembly | 5595 | 31.8% | 5.5% | 3.1% | 59.6% |
| c | 1055 | 35.4% | 8.5% | 3.2% | 52.9% |
| livecode | 27 | 0.0% | 0.0% | 0.0% | 100.0% |

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
