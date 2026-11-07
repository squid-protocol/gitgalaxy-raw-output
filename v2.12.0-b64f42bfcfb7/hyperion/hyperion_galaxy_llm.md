# ARCHITECTURAL_BRIEF: hyperion
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/hercules-390/hyperion.git` |
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
- **Scope:** 697 analyzed artifact(s), 271967 LOC.
- **Load-bearing artifact:** `hercules.h` -- 194 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `hstdinc.h` -- pulls in 77 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `decNumber/decNumber.c` at magnitude 9222.0 (structural weight, not risk).
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
| Total Artifacts | 1039 |
| Analyzed Artifacts (Scanned) | 697 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 342 |
| Total LOC | 271967 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 67.1% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3527 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2436 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2106 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 23 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 329 | 223462 | 47.2% |
| PLAINTEXT | 200 | 0 | 28.7% |
| HTML | 61 | 21009 | 8.8% |
| M4 | 34 | 8076 | 4.9% |
| HLASM | 33 | 12882 | 4.7% |
| REXX | 14 | 2278 | 2.0% |
| BATCH | 9 | 2723 | 1.3% |
| SHELL | 8 | 592 | 1.1% |
| MARKDOWN | 4 | 0 | 0.6% |
| JCL | 3 | 686 | 0.4% |
| CSS | 1 | 120 | 0.1% |
| PERL | 1 | 139 | 0.1% |

## 4.1 SOURCE ENCODINGS
> 4 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 692 |
| cp1252 | cp1252-fallback | 4 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 40%, Declarative / Non-Code 20%, Large Core Modules 12%, Many-Argument Workhorses Files 10%, Large Core Modules (3) 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 493 | 70.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 204 | 29.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 342*

**Composition by Extension & Reason:**
- `.tst`: 64x Excluded (Unsupported Extension: '.tst')
- `.gif`: 44x Excluded (Explicitly Denied Extension: '.gif')
- `.core`: 33x Excluded (Unsupported Extension: '.core')
- `.list`: 32x Excluded (Unsupported Extension: '.list')
- `.msvc`: 29x Excluded (Unsupported Extension: '.msvc'), 1x Excluded (Unsupported Extension: '.MSVC')
- `.assemble`: 13x Excluded (Unsupported Extension: '.assemble')
- `.listing`: 13x Excluded (Unsupported Extension: '.listing')
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Excluded (Lexical Monotony: High structural repetition detected in 4119 LOC)
- `.am`: 8x Excluded (Unsupported Extension: '.am')
- `.subtst`: 8x Excluded (Unsupported Extension: '.subtst')
- `.png`: 6x Excluded (Explicitly Denied Extension: '.png')
- `.rc`: 5x Excluded (Unsupported Extension: '.rc')
- `.ico`: 5x Excluded (Explicitly Denied Extension: '.ico')
- `.sln`: 4x Excluded (Unsupported Extension: '.sln')
- `.vcxproj`: 3x Excluded (Unsupported Extension: '.vcxproj')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.4 | 26.4 | 2.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.5 | 37.2 | 50.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 25.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.3 | 4.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 29.0 | 1.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 48.6 | 77.4 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1717 | 131 | 5 | `hsccmd.c` |
| cleanup | 733 | 101 | 2 | `qeth.c` |
| guards | 7272 | 297 | 36 | `ltdl.c` |
| danger | 3834 | 192 | 15 | `hsccmd.c` |
| concurrency | 86 | 42 | 0 | `autoconf/mkinstalldirs` |
| connectivity | 6550 | 380 | 23 | `esame.c` |
| io | 3339 | 167 | 9 | `html/hercconf.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 148 | 30 | 0 | `ctcadpt.c` |
| time | 118 | 45 | 0 | `hsccmd.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 33 | 9 | 0 | `hao.c` |
| events | 308 | 52 | 0 | `configure.ac` |
| tests | 1 | 1 | 0 | `autogen.sh` |
| docs | 823 | 143 | 2 | `w32util.c` |
| debt | 1269 | 169 | 3 | `tests/runtest.rexx` |
| mutation | 62742 | 371 | 247 | `ctc_ptp.c` |
| dead_code | 1301 | 225 | 4 | `hsccmd.c` |
| credential | 9 | 8 | 0 | `m4/gettext.m4` |
| threat | 75 | 13 | 0 | `codepage.c` |
| ml_ai | 1912 | 123 | 6 | `hsccmd.c` |
| ui | 3048 | 45 | 0 | `html/hercmsdl.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `html/hercconf.html` (Hits: 581)
- `html/hercfaq.html` (Hits: 224)
- `html/hercmsdl.html` (Hits: 141)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **hercules.h** (`hercules.h`) — 194 inbound connections
2. **hstdinc.h** (`hstdinc.h`) — 173 inbound connections
3. **logmsg.c** (`logmsg.c`) — 102 inbound connections
4. **decNumber.c** (`decNumber/decNumber.c`) — 86 inbound connections
5. **opcode.h** (`opcode.h`) — 86 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **hstdinc.h** (`hstdinc.h`) — 77 outbound dependencies
2. **hercules.h** (`hercules.h`) — 44 outbound dependencies
3. **ltdl.c** (`ltdl.c`) — 26 outbound dependencies
4. **dyncrypt.c** (`crypto/dyncrypt.c`) — 11 outbound dependencies
5. **hsccmd.c** (`hsccmd.c`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ckddasd_execute_ccw` **(Many-Argument Workhorses)** (@ `ckddasd.c`) -> Impact: **3315.6** | LOC: 3958
  * *Intent:* } /* end function ckd_write_data */ /*-------------------------------------------------------------------*/ /* Execute a Channel Command Word */ /*---...
- `tapedev_execute_ccw` **(Many-Argument Workhorses)** (@ `tapeccws.c`) -> Impact: **1313.6** | LOC: 2855
- `decLnOp` **(Many-Argument Workhorses)** (@ `decNumber/decNumber.c`) -> Impact: **1218.7** | LOC: 2460
  * *Intent:* /* 3. Fastpaths are included for ln(10) and ln(2), up to length 40, */ /* as these are common requests. ln(10) is used by log10(x). */ /* */ /* 4. An ...
- `cckd_chkdsk` **(Many-Argument Workhorses)** (@ `cckdutil.c`) -> Impact: **963.8** | LOC: 1816
  * *Intent:* /*------------------------------------------------------------------- * Perform check function on a compressed ckd file * * check levels * -1 devhdr, ...
- `resume_cmd` **(Many-Argument Workhorses)** (@ `sr.c`) -> Impact: **709.4** | LOC: 1068
  * *Intent:* #define SR_NULL_REGS_CHECK(_regs) if ((_regs) == NULL) goto sr_null_regs_exit;
- `commadpt_execute_ccw` **(Many-Argument Workhorses)** (@ `commadpt.c`) -> Impact: **708.6** | LOC: 939
  * *Intent:* /*-------------------------------------------------------------------*/ /* Execute a Channel Command Word */ /*---------------------------------------...
- `panel_display` **(Compute Cores)** (@ `panel.c`) -> Impact: **465.8** | LOC: 1376
  * *Intent:* /*-------------------------------------------------------------------*/ /* Panel display thread */ /* */ /* This function runs on the main thread. It ...
- `printer_execute_ccw` **(Many-Argument Workhorses)** (@ `printer.c`) -> Impact: **450.9** | LOC: 497
  * *Intent:* } /* end function printer_close_device */ /*-------------------------------------------------------------------*/ /* Execute a Channel Command Word */...
- `icount_cmd` **(Many-Argument Workhorses)** (@ `hscemode.c`) -> Impact: **381.9** | LOC: 759
  * *Intent:* #endif #if defined(OPTION_INSTRUCTION_COUNTING) /*-------------------------------------------------------------------*/ /* icount command - display in...
- `decDivideOp` **(Many-Argument Workhorses)** (@ `decNumber/decNumber.c`) -> Impact: **365.1** | LOC: 582
  * *Intent:* /* exp=exp-1 */ /* end outer_loop */ /* exp=exp+1 -- set the proper exponent */ /* if have=0 then generate answer=0 */ /* Return (Result is defined by...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 308 | 174860.04 | 35.57% | 12.6% |
| `decNumber` | 32 | 17498.28 | 22.92% | 17.11% |
| `tests` | 196 | 3436.4 | 1.46% | 0.0% |
| `scripts` | 8 | 668.18 | 44.36% | 13.95% |
| `autoconf` | 5 | 441.18 | 15.98% | 33.45% |
| `m4` | 30 | 278.62 | 0.61% | 40.59% |
| `util` | 10 | 263.18 | 14.99% | 0.0% |
| `CMake` | 33 | 261.12 | 2.22% | 11.04% |
| `crypto` | 9 | 35.46 | 38.17% | 13.65% |
| `man` | 4 | 8.92 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ccfixme.h` -> **100.0%** Exposure
- `CMake/CMakeHercTestRegparm3.c` -> **99.9925%** Exposure
- `autoconf/hercules.m4` -> **99.9881%** Exposure
- `scripts/hcommand.rexx` -> **99.9295%** Exposure
- `cache.c` -> **99.5817%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `1Stop` -> **100.0%** Exposure
- `1Stop-CMake` -> **100.0%** Exposure
- `GetGitHash` -> **100.0%** Exposure
- `util/dasdlist` -> **100.0%** Exposure
- `awstape.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `hsccmd.c` -> **107** Orphaned Functions | **0** Duplicates
- `w32util.c` -> **52** Orphaned Functions | **0** Duplicates
- `decNumber/decNumber.c` -> **49** Orphaned Functions | **0** Duplicates
- `loadparm.c` -> **38** Orphaned Functions | **0** Duplicates
- `hthreads.c` -> **34** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1174` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `decNumber/decNumber.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.386)
- **Top Global Matches:** file_cluster_8: 7.386, file_cluster_6: 12.303, file_cluster_4: 20.653
- **Magnitude:** 9222.0 | **LOC:** 8142 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **86** in-repo importer(s); it depends on **6**; blast radius 19.581; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.9%), Guard Balance (formerly Safety Score) (86.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decLnOp` **(Many-Argument Workhorses)** (Impact: 1218.7)
    * *Intent:* /* 3. Fastpaths are included for ln(10) and ln(2), up to length 40, */ /* as these are common reques...
  * `decDivideOp` **(Many-Argument Workhorses)** (Impact: 365.1)
    * *Intent:* /* exp=exp-1 */ /* end outer_loop */ /* exp=exp+1 -- set the proper exponent */ /* if have=0 then ge...
  * `decAddOp` **(Many-Argument Workhorses)** (Impact: 218.2)
    * *Intent:* /* overlap the A or B coefficient */ /* then the result must be calculated into a temporary buffer. ...
  * `decCompareOp` **(Many-Argument Workhorses)** (Impact: 203.4)
    * *Intent:* /* */ /* res is C, the result. C may be A and/or B (e.g., X=X?X) */ /* lhs is A */ /* rhs is B */ /*...
  * `decNumberPower` **(Many-Argument Workhorses)** (Impact: 192.9)
    * *Intent:* /* Mathematical function restrictions apply (see above); a NaN is */ /* returned with Invalid_operat...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 49 instances
* *Amplified Cascading Flux:* 1396 instances
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 4310
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1396`, `structural_boundaries: 514`, `args: 169`, `func_start: 102`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 1518`, `dead_code: 19`, `fragile_debt: 4`, `unreferenced_by_name: 49`
* *Architecture:* `api: 67`, `import: 6`
* *Defense:* `safety: 2`, `immutability_locks: 202`, `cleanup: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.581
  * `Choke Point (Betweenness):` 0.004864 | `Ripple Effect (Closeness):` 0.15538
  * `Imports (Out-Degree: 3):` ctype.h, decNumber.h, decNumberLocal.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 86):` (Excluded from Brief to save tokens)

### `hsccmd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.082)
- **Top Global Matches:** file_cluster_8: 5.082, file_cluster_6: 14.55, file_cluster_3: 22.121
- **Magnitude:** 7490.74 | **LOC:** 8865 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **11**; blast radius 1.728; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%), Guard Balance (formerly Safety Score) (70.3%)
- **Documentation Coverage:** 77.0595% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mt_cmd` **(Many-Argument Workhorses)** (Impact: 192.5)
    * *Intent:* /*-------------------------------------------------------------------*/ /* mt command - magnetic tap...
  * `qd_cmd` **(Many-Argument Workhorses)** (Impact: 159.0)
    * *Intent:* /*-------------------------------------------------------------------*/ /* qd command - query device...
  * `automount_cmd` **(Many-Argument Workhorses)** (Impact: 144.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /* automount_cmd - show or u...
  * `qeth_cmd` **(Many-Argument Workhorses)** (Impact: 143.2)
    * *Intent:* /*-------------------------------------------------------------------*/ /* qeth command - enable/dis...
  * `fcb_cmd` **(Many-Argument Workhorses)** (Impact: 123.1)
    * *Intent:* /*-------------------------------------------------------------------*/ /* fcb - display or load */ ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 33 instances
* *Amplified Cascading Flux:* 957 instances
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 2918
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1836`, `structural_boundaries: 516`, `args: 779`, `func_start: 130`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 1004`, `dead_code: 7`, `unreferenced_by_name: 107`
* *Architecture:* `io: 44`, `api: 124`, `import: 11`
* *Defense:* `safety: 20`, `doc: 2`, `immutability_locks: 21`, `cleanup: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.728
  * `Choke Point (Betweenness):` 0.017471 | `Ripple Effect (Closeness):` 0.061843
  * `Imports (Out-Degree: 40):` ctc_ptp.h, ctcadpt.h, dasdtab.h, devtype.h, hercules.h, history.h, hstdinc.h, httpmisc.h...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `ckddasd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.842)
- **Top Global Matches:** file_cluster_8: 7.842, file_cluster_6: 9.641, file_cluster_4: 17.981
- **Magnitude:** 6872.72 | **LOC:** 6157 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 0.826; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.9%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ckddasd_execute_ccw` **(Many-Argument Workhorses)** (Impact: 3315.6)
    * *Intent:* } /* end function ckd_write_data */ /*--------------------------------------------------------------...
  * `ckddasd_init_handler` **(Many-Argument Workhorses)** (Impact: 238.2)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Initialize the device han...
  * `ckd_read_count` **(Many-Argument Workhorses)** (Impact: 105.3)
    * *Intent:* } /* end function mt_advance */ /*------------------------------------------------------------------...
  * `ckddasd_hresume` **(Many-Argument Workhorses)** (Impact: 87.3)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Hercules resume */ /*----...
  * `ckd_build_sense` **(Many-Argument Workhorses)** (Impact: 83.8)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Build sense data */ /*---...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 844 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 2628
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1230`, `structural_boundaries: 449`, `args: 159`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 940`, `dead_code: 1`, `fragile_debt: 5`
* *Architecture:* `io: 14`, `api: 15`, `import: 5`
* *Defense:* `safety: 4`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.826
  * `Choke Point (Betweenness):` 0.000975 | `Ripple Effect (Closeness):` 0.045422
  * `Imports (Out-Degree: 18):` dasdblks.h, devtype.h, hercules.h, hstdinc.h, sr.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ctc_ptp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.351)
- **Top Global Matches:** file_cluster_6: 9.351, file_cluster_8: 9.877, file_cluster_4: 17.073
- **Magnitude:** 6564.04 | **LOC:** 9608 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.732; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.6%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_rrh_C108` **(Many-Argument Workhorses)** (Impact: 306.5)
    * *Intent:* } /* End function write_rrh_C17E() */ /* -----------------------------------------------------------...
  * `parse_conf_stmt` **(Many-Argument Workhorses)** (Impact: 258.6)
    * *Intent:* /* ------------------------------------------------------------------ */ /* parse_conf_stmt() */ /* ...
  * `gen_csv_sid` **(Many-Argument Workhorses)** (Impact: 152.5)
    * *Intent:* // values the output token value will always be the same. // For example:- // if Clock1 is always C5...
  * `write_rrh_417E` **(Many-Argument Workhorses)** (Impact: 151.6)
    * *Intent:* } /* End function point_CSVcv() */ /* --------------------------------------------------------------...
  * `get_preconfigured_value` **(Many-Argument Workhorses)** (Impact: 111.9)
    * *Intent:* } /* End function parse_conf_stmt() */ /* ----------------------------------------------------------...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 27 instances
* *Amplified Cascading Flux:* 1058 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 4265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 759`, `structural_boundaries: 335`, `args: 349`, `func_start: 55`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 167`, `state_mutation: 2149`, `dead_code: 39`, `fragile_debt: 5`
* *Architecture:* `io: 2`, `api: 55`, `import: 10`
* *Defense:* `safety: 15`, `immutability_locks: 3`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.732
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` ctc_ptp.h, ctcadpt.h, herc_getopt.h, hercules.h, hstdinc.h, ifaddrs.h, mpc.h, opcode.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cckddasd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.057)
- **Top Global Matches:** file_cluster_8: 8.057, file_cluster_6: 9.479, file_cluster_4: 17.756
- **Magnitude:** 5644.52 | **LOC:** 6188 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 0.849; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.6%), Complexity Load (formerly Cognitive Load) (74.7%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cckd_command` **(Many-Argument Workhorses)** (Impact: 226.5)
    * *Intent:* /*-------------------------------------------------------------------*/ /* cckd command processor */...
  * `cckd_sf_remove` **(Compute Cores)** (Impact: 107.2)
    * *Intent:* } /* end function cckd_sf_add */ /*-----------------------------------------------------------------...
  * `cckd_gc_percolate` **(Many-Argument Workhorses)** (Impact: 103.1)
    * *Intent:* } /* end thread cckd_gcol */ /*-------------------------------------------------------------------*/...
  * `cckd_read_trk` **(Many-Argument Workhorses)** (Impact: 96.3)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Read a track image */ /* ...
  * `cckd_gcol` **(Compute Cores)** (Impact: 74.6)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Garbage Collection thread...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 987 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 3125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1049`, `structural_boundaries: 378`, `args: 398`, `func_start: 89`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1151`, `dead_code: 4`, `fragile_debt: 3`
* *Architecture:* `io: 9`, `api: 177`, `import: 4`
* *Defense:* `safety: 14`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.849
  * `Choke Point (Betweenness):` 0.002801 | `Ripple Effect (Closeness):` 0.052634
  * `Imports (Out-Degree: 16):` devtype.h, hercules.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `float.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.425)
- **Top Global Matches:** file_cluster_4: 6.425, file_cluster_6: 9.972, file_cluster_16: 11.925
- **Magnitude:** 5302.02 | **LOC:** 7873 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.732; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.8%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_ef` **(Many-Argument Workhorses)** (Impact: 147.0)
    * *Intent:* } /* end function add_lf */ /*-------------------------------------------------------------------*/ ...
  * `add_sf` **(Many-Argument Workhorses)** (Impact: 107.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /*--------------------------...
  * `add_lf` **(Many-Argument Workhorses)** (Impact: 107.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Add long float */ /* */ /...
  * `compare_float_ext_reg` **(Compute Cores)** (Impact: 99.0)
    * *Intent:* /*-------------------------------------------------------------------*/ /* B369 CXR - Compare Floati...
  * `convert_float_ext_to_fixed_reg` **(Compute Cores)** (Impact: 84.3)
    * *Intent:* /*-------------------------------------------------------------------*/ /* B3BA CFXR - Convert from ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 915 instances
* *State Mutation (weighted view):* 2943
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 983`, `structural_boundaries: 142`, `args: 60`, `func_start: 155`, `class_start: 3`
* *Risk/State:* `state_mutation: 1113`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 117`, `import: 6`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.732
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` float.c, hercules.h, hstdinc.h, inline.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `general1.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.87)
- **Top Global Matches:** file_cluster_6: 7.87, file_cluster_4: 9.081, file_cluster_16: 16.228
- **Magnitude:** 4290.38 | **LOC:** 6029 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.732; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.4%), Complexity Load (formerly Cognitive Load) (69.6%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convert_utf8_to_utf16` **(Compute Cores)** (Impact: 114.7)
    * *Intent:* } /* end convert_utf16_to_utf8 */ /*----------------------------------------------------------------...
  * `compare_and_swap_and_store` **(Compute Cores)** (Impact: 67.4)
    * *Intent:* #define MAX_CSST_SC 4 #endif /*#ifndef MAX_CSST_SC*/ #else #ifndef MAX_CSST_FC #define MAX_CSST_FC 1...
  * `exclusive_or_character` **(Compute Cores)** (Impact: 65.0)
    * *Intent:* /*-------------------------------------------------------------------*/ /* D7 XC - Exclusive Or Char...
  * `move_long` **(Compute Cores)** (Impact: 62.2)
    * *Intent:* /*-------------------------------------------------------------------*/ /* 0E MVCL - Move Long [RR] ...
  * `and_character` **(Compute Cores)** (Impact: 60.2)
    * *Intent:* /*-------------------------------------------------------------------*/ /* D4 NC - And Character [SS...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 842 instances
* *State Mutation (weighted view):* 2651
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 765`, `structural_boundaries: 84`, `args: 144`, `func_start: 114`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 4`, `state_mutation: 967`, `dead_code: 6`, `fragile_debt: 1`
* *Architecture:* `api: 112`, `import: 7`
* *Defense:* `safety: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.732
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` clock.h, general1.c, hercules.h, hstdinc.h, inline.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esame.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 9.363)
- **Top Global Matches:** file_cluster_15: 9.363, file_cluster_12: 9.472, file_cluster_16: 9.509
- **Magnitude:** 4252.26 | **LOC:** 8494 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.732; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.5%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resume_program` **(Many-Argument Workhorses)** (Impact: 83.7)
    * *Intent:* } /* end DEF_INST(trap4) */ #endif /*defined(FEATURE_LINKAGE_STACK)*/ #if defined(FEATURE_RESUME_PRO...
  * `perform_frame_management_function` **(Compute Cores)** (Impact: 76.5)
    * *Intent:* #if defined(FEATURE_ENHANCED_DAT_FACILITY) /*-------------------------------------------------------...
  * `reset_reference_bits_multiple` **(I/O & Config Routines)** (Impact: 42.4)
    * *Intent:* #endif /*defined(FEATURE_CONFIGURATION_TOPOLOGY_FACILITY)*/ #if defined(FEATURE_RESET_REFERENCE_BITS...
  * `store_multiple_long` **(Compute Cores)** (Impact: 29.9)
    * *Intent:* } /* end DEF_INST(load_control_long) */ #endif /*defined(FEATURE_ESAME)*/ #if defined(FEATURE_ESAME)...
  * `load_multiple_long` **(Compute Cores)** (Impact: 28.6)
    * *Intent:* } /* end DEF_INST(load_multiple_high) */ #endif /*defined(FEATURE_ESAME)*/ #if defined(FEATURE_ESAME...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 688 instances
* *State Mutation (weighted view):* 2231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 688`, `structural_boundaries: 59`, `args: 347`, `func_start: 256`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 26`, `state_mutation: 855`, `dead_code: 9`, `fragile_debt: 1`
* *Architecture:* `api: 254`, `import: 7`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.732
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` clock.h, esame.c, hercules.h, hstdinc.h, inline.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `qeth.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.343)
- **Top Global Matches:** file_cluster_4: 9.343, file_cluster_6: 10.745, file_cluster_12: 13.85
- **Magnitude:** 4214.96 | **LOC:** 6666 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.776; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.7%), Complexity Load (formerly Cognitive Load) (68.1%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `osa_adapter_cmd` **(Many-Argument Workhorses)** (Impact: 351.8)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Adapter Command Routine *...
  * `qeth_execute_ccw` **(Many-Argument Workhorses)** (Impact: 350.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Execute a Channel Command...
  * `qeth_init_handler` **(Many-Argument Workhorses)** (Impact: 186.4)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Initialize the device han...
  * `write_buffered_packets` **(Many-Argument Workhorses)** (Impact: 106.8)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Write all packets/frames ...
  * `read_L2_packets` **(Many-Argument Workhorses)** (Impact: 59.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Read one L2 frame from TA...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 55 instances
* *Amplified Cascading Flux:* 598 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 2062
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 746`, `structural_boundaries: 313`, `args: 274`, `func_start: 83`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 188`, `state_mutation: 866`, `dead_code: 38`, `fragile_debt: 24`
* *Architecture:* `io: 1`, `api: 2`, `import: 11`
* *Defense:* `safety: 14`, `immutability_locks: 12`, `cleanup: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.776
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.001435
  * `Imports (Out-Degree: 24):` chsc.h, ctcadpt.h, dbgtrace.h, devtype.h, hercifc.h, hercules.h, hstdinc.h, mpc.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `control.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.38)
- **Top Global Matches:** file_cluster_8: 7.38, file_cluster_6: 11.58, file_cluster_4: 19.909
- **Magnitude:** 4036.14 | **LOC:** 7573 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.732; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.6%), Complexity Load (formerly Cognitive Load) (69.8%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `signal_processor` **(Many-Argument Workhorses)** (Impact: 229.4)
    * *Intent:* } /* end DEF_INST(set_system_mask) */ /*------------------------------------------------------------...
  * `program_call` **(Many-Argument Workhorses)** (Impact: 190.3)
    * *Intent:* #if defined(FEATURE_DUAL_ADDRESS_SPACE) /*----------------------------------------------------------...
  * `store_system_information` **(Many-Argument Workhorses)** (Impact: 147.5)
    * *Intent:* } /* end function stsi_capability */ #endif /*!defined(_STSI_CAPABILITY)*/ #ifdef FEATURE_STORE_SYST...
  * `branch_in_subspace_group` **(Many-Argument Workhorses)** (Impact: 73.1)
    * *Intent:* } /* end DEF_INST(branch_and_set_authority) */ #endif /*defined(FEATURE_BRANCH_AND_SET_AUTHORITY)*/ ...
  * `set_storage_key_extended` **(Compute Cores)** (Impact: 68.7)
    * *Intent:* } /* end function conditional_sske_procedure */ #endif /*defined(FEATURE_CONDITIONAL_SSKE)*/ #endif ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 684 instances
* *State Mutation (weighted view):* 2168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 990`, `structural_boundaries: 107`, `args: 326`, `func_start: 67`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 46`, `state_mutation: 800`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 70`, `import: 6`
* *Defense:* `safety: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.732
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` control.c, hercules.h, hstdinc.h, inline.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `decNumber/decBasic.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.08)
- **Top Global Matches:** file_cluster_6: 6.08, file_cluster_4: 8.908, file_cluster_8: 16.43
- **Magnitude:** 3628.32 | **LOC:** 3912 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.981; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decDivide` **(Many-Argument Workhorses)** (Impact: 301.6)
    * *Intent:* /* */ /* result gets the result of dividing dfl by dfr: */ /* dfl is the first decFloat (lhs) */ /* ...
  * `decFloatFMA` **(Many-Argument Workhorses)** (Impact: 187.3)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decFloatFMA -- multiply ...
  * `decFloatAdd` **(Many-Argument Workhorses)** (Impact: 139.6)
    * *Intent:* #endif
  * `decFloatQuantize` **(Many-Argument Workhorses)** (Impact: 134.5)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decFloatQuantize -- quan...
  * `decNumCompare` **(Many-Argument Workhorses)** (Impact: 129.6)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decNumCompare -- numeric...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 564 instances
* *State Mutation (weighted view):* 1813
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 646`, `structural_boundaries: 325`, `args: 89`, `func_start: 72`, `class_start: 13`
* *Risk/State:* `state_mutation: 685`, `dead_code: 20`
* *Architecture:* `api: 64`
* *Defense:* `immutability_locks: 119`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002869
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `dasdload.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.04)
- **Top Global Matches:** file_cluster_8: 8.04, file_cluster_6: 10.838, file_cluster_4: 19.172
- **Magnitude:** 3614.74 | **LOC:** 4470 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.732; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.1%), Complexity Load (formerly Cognitive Load) (67.5%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_ctrl_stmt` **(Many-Argument Workhorses)** (Impact: 261.1)
    * *Intent:* /* The dcb attributes can be: */ /* dsorg recfm lrecl blksize keylen */ /* For the XMIT method the d...
  * `process_iebcopy_file` **(Many-Argument Workhorses)** (Impact: 222.7)
    * *Intent:* /* method METHOD_XMIT or METHOD_VS */ /* Output: */ /* odsorg Dataset organization */ /* orecfm Reco...
  * `process_control_file` **(Many-Argument Workhorses)** (Impact: 170.2)
    * *Intent:* /* cfname Control file name */ /* ofname DASD image file name */ /* cif -> CKD image file descriptor...
  * `seq_initialize` **(Many-Argument Workhorses)** (Impact: 114.0)
    * *Intent:* /* outhead Output starting head number */ /* extsize Extent size in tracks */ /* dsorg Dataset organ...
  * `write_vtoc` **(Many-Argument Workhorses)** (Impact: 104.9)
    * *Intent:* /* vtocext Number of tracks in VTOC, or zero */ /* Input/output: */ /* nxtcyl Starting cylinder numb...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 476 instances
* *High Risk Execution (weighted view):* 2
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 1696
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 508`, `structural_boundaries: 275`, `args: 220`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 3`, `state_mutation: 744`, `unreferenced_by_name: 1`
* *Architecture:* `io: 21`, `api: 4`, `import: 3`
* *Defense:* `safety: 2`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.732
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` dasdblks.h, hercules.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cckdutil.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.346)
- **Top Global Matches:** file_cluster_8: 6.346, file_cluster_6: 12.81, file_cluster_4: 21.396
- **Magnitude:** 3370.02 | **LOC:** 2932 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **3**; blast radius 1.324; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.4%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cckd_chkdsk` **(Many-Argument Workhorses)** (Impact: 963.8)
    * *Intent:* /*------------------------------------------------------------------- * Perform check function on a ...
  * `cckd_comp` **(Many-Argument Workhorses)** (Impact: 216.8)
    * *Intent:* /*------------------------------------------------------------------- * Remove all free space from a...
  * `cckd_swapend` **(Compute Cores)** (Impact: 94.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /* EXTERNALGUI support */ /*...
  * `cdsk_valid_trk` **(Many-Argument Workhorses)** (Impact: 74.2)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Validate a track image */...
  * `comp_spctab_sort` **(Stateful Encapsulated Methods)** (Impact: 19.6)
    * *Intent:* } /* cckd_comp() */ /*------------------------------------------------------------------- * cckd_com...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 26 instances
* *Amplified Cascading Flux:* 601 instances
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 1898
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 752`, `structural_boundaries: 119`, `args: 123`, `func_start: 14`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 696`, `dead_code: 7`, `unreferenced_by_name: 2`
* *Architecture:* `io: 56`, `api: 11`, `import: 3`
* *Defense:* `safety: 8`, `immutability_locks: 10`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.324
  * `Choke Point (Betweenness):` 0.002252 | `Ripple Effect (Closeness):` 0.047026
  * `Imports (Out-Degree: 8):` hercules.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `commadpt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.822)
- **Top Global Matches:** file_cluster_6: 5.822, file_cluster_4: 9.735, file_cluster_8: 15.619
- **Magnitude:** 3369.1 | **LOC:** 3783 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.732; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.7%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `commadpt_execute_ccw` **(Many-Argument Workhorses)** (Impact: 708.6)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Execute a Channel Command...
  * `commadpt_init_handler` **(Many-Argument Workhorses)** (Impact: 308.1)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Device Initialisation */ ...
  * `commadpt_thread` **(Many-Argument Workhorses)** (Impact: 236.5)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Communication Thread main...
  * `commadpt_read_tty` **(Many-Argument Workhorses)** (Impact: 127.7)
  * `commadpt_initiate_userdial` **(Compute Cores)** (Impact: 39.4)
    * *Intent:* /*-------------------------------------------------------------------*/ /* commadpt_initiate_userdia...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 536 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 1707
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 613`, `structural_boundaries: 263`, `args: 123`, `func_start: 31`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 635`, `dead_code: 4`, `fragile_debt: 4`
* *Architecture:* `io: 12`, `api: 1`, `import: 5`
* *Defense:* `safety: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.732
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` commadpt.h, devtype.h, hercules.h, hstdinc.h, parser.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `console.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.118)
- **Top Global Matches:** file_cluster_8: 5.118, file_cluster_6: 15.193, file_cluster_3: 21.395
- **Magnitude:** 3080.32 | **LOC:** 4518 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.732; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.2%), Guard Balance (formerly Safety Score) (74.2%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loc3270_execute_ccw` **(Many-Argument Workhorses)** (Impact: 271.5)
    * *Intent:* } /* end function console_connection_handler */ /*--------------------------------------------------...
  * `telnet_ev_handler` **(Many-Argument Workhorses)** (Impact: 185.3)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Telnet event handler */ /...
  * `build_logo` **(Many-Argument Workhorses)** (Impact: 154.5)
    * *Intent:* /* size of the returned buffer if successful. */ /* */ /* 'errmsg' is the address of a char pointer ...
  * `console_connection_handler` **(Many-Argument Workhorses)** (Impact: 144.9)
    * *Intent:* } /* end function connect_client */ /*--------------------------------------------------------------...
  * `constty_execute_ccw` **(Many-Argument Workhorses)** (Impact: 135.9)
    * *Intent:* *unitstat = CSW_CE | CSW_DE | CSW_UC; } /* end switch(code) */ } /* end function loc3270_execute_ccw...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 28 instances
* *Amplified Cascading Flux:* 470 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 1451
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 639`, `structural_boundaries: 212`, `args: 158`, `func_start: 38`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 511`, `fragile_debt: 5`
* *Architecture:* `io: 8`, `import: 8`
* *Defense:* `safety: 43`, `doc: 1`, `immutability_locks: 17`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.732
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` cnsllogo.h, devtype.h, hercules.h, hexdumpe.h, hexterns.h, hstdinc.h, opcode.h, sr.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tapeccws.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 5.997)
- **Top Global Matches:** file_cluster_3: 5.997, file_cluster_8: 20.431, file_cluster_6: 33.389
- **Magnitude:** 2975.78 | **LOC:** 4393 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **3**; blast radius 1.153; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%)
- **Documentation Coverage:** 67.7022% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tapedev_execute_ccw` **(Many-Argument Workhorses)** (Impact: 1313.6)
  * `build_sense_3590` **(Many-Argument Workhorses)** (Impact: 121.5)
    * *Intent:* /*-------------------------------------------------------------------*/ /* build_sense_3590 */ /*---...
  * `build_sense_3480_etal` **(Many-Argument Workhorses)** (Impact: 112.3)
    * *Intent:* } /* end function build_sense_3420 */ /*------------------------------------------------------------...
  * `load_display` **(Many-Argument Workhorses)** (Impact: 88.7)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Load Display channel comm...
  * `build_sense_3410_3420` **(Many-Argument Workhorses)** (Impact: 72.6)
    * *Intent:* } /* end function build_senseX */ /*----------------------------------------------------------------...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 342 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1052
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 553`, `structural_boundaries: 238`, `args: 160`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 368`, `dead_code: 3`, `fragile_debt: 14`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 25`, `import: 3`
* *Defense:* `safety: 1`, `doc: 25`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.153
  * `Choke Point (Betweenness):` 0.000533 | `Ripple Effect (Closeness):` 0.008608
  * `Imports (Out-Degree: 14):` hercules.h, hstdinc.h, tapedev.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `channel.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.081)
- **Top Global Matches:** file_cluster_4: 5.081, file_cluster_16: 9.72, file_cluster_15: 10.914
- **Magnitude:** 2955.04 | **LOC:** 6323 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **6**; blast radius 1.69; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.0%), Guard Balance (formerly Safety Score) (73.8%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `halt_subchan` **(Many-Argument Workhorses)** (Impact: 66.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /* HALT SUBCHANNEL */ /*----...
  * `haltio` **(Many-Argument Workhorses)** (Impact: 35.1)
    * *Intent:* } /* end function testio */ /*-------------------------------------------------------------------*/ ...
  * `schedule_ioq` **(Many-Argument Workhorses)** (Impact: 34.9)
    * *Intent:* /* */ /* */ /* Locks Used: */ /* */ /* None */ /* */ /* */ /* Returns: */ /* */ /* 0 - Success */ /*...
  * `cancel_subchan` **(Many-Argument Workhorses)** (Impact: 33.8)
    * *Intent:* /*-------------------------------------------------------------------*/ /* CANCEL SUBCHANNEL */ /*--...
  * `resume_subchan` **(Many-Argument Workhorses)** (Impact: 32.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /* RESUME SUBCHANNEL */ /*--...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 613 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 1987
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 951`, `structural_boundaries: 232`, `args: 227`, `func_start: 69`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 7`, `state_mutation: 761`, `dead_code: 9`, `fragile_debt: 4`
* *Architecture:* `api: 50`, `import: 7`
* *Defense:* `safety: 2`, `doc: 6`, `immutability_locks: 37`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.018528 | `Ripple Effect (Closeness):` 0.081869
  * `Imports (Out-Degree: 14):` channel.c, chsc.h, devtype.h, hercules.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `w32util.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.259)
- **Top Global Matches:** file_cluster_4: 5.259, file_cluster_6: 10.703, file_cluster_16: 11.258
- **Magnitude:** 2880.14 | **LOC:** 4756 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **60** in-repo importer(s); it depends on **3**; blast radius 12.253; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.0%), Complexity Load (formerly Cognitive Load) (62.6%)
- **Documentation Coverage:** 38.4406% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `w32_init_hostinfo` **(Compute Cores)** (Impact: 303.6)
  * `w32_select` **(Many-Argument Workhorses)** (Impact: 77.0)
  * `clock_gettime` **(Stateful Encapsulated Methods)** (Impact: 54.6)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////////////// // (PUBLI...
  * `w32_poor_mans_fork` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `w32_nanosleep` **(Stateful Encapsulated Methods)** (Impact: 47.8)
    * *Intent:* #endif // !defined( HAVE_GETTIMEOFDAY ) ////////////////////////////////////////////////////////////...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 30 instances
* *Amplified Cascading Flux:* 444 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 1417
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 582`, `structural_boundaries: 372`, `args: 268`, `func_start: 84`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 529`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 52`
* *Architecture:* `io: 5`, `api: 88`, `import: 3`
* *Defense:* `safety: 22`, `doc: 89`, `immutability_locks: 54`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.253
  * `Choke Point (Betweenness):` 0.001956 | `Ripple Effect (Closeness):` 0.135605
  * `Imports (Out-Degree: 10):` dbgtrace.h, hercules.h, hstdinc.h
  * `Imported By (In-Degree: 60):` (Excluded from Brief to save tokens)

### `ecpsvm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.175)
- **Top Global Matches:** file_cluster_4: 5.175, file_cluster_6: 8.247, file_cluster_15: 12.482
- **Magnitude:** 2753.3 | **LOC:** 5113 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 1.001; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.3%), Complexity Load (formerly Cognitive Load) (60.9%)
- **Documentation Coverage:** 71.0834% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ecpsvm_do_disp2` **(Many-Argument Workhorses)** (Impact: 125.8)
    * *Intent:* /* DISP2 Core */
  * `ecpsvm_dolctl` **(Many-Argument Workhorses)** (Impact: 117.4)
    * *Intent:* /* B7 - LCTL Instruction Assist */
  * `ecpsvm_dolra` **(Many-Argument Workhorses)** (Impact: 84.4)
    * *Intent:* */
  * `ecpsvm_dosio` **(Many-Argument Workhorses)** (Impact: 53.0)
    * *Intent:* /* operation exception and a trip */ /* through the DMKPRG & DMKPRV code */ /* path. In addition, th...
  * `ecpsvm_dispatch_main` **(Compute Cores)** (Impact: 50.8)
    * *Intent:* /* E60D DISP0 Instruction */ /* DISP0 : Operand 1 : DISP0 Data list, Operand 2 : DISP0 Exit list */ ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 460 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1543
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 289`, `args: 703`, `func_start: 66`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 623`, `dead_code: 6`, `fragile_debt: 2`
* *Architecture:* `api: 59`, `import: 7`
* *Defense:* `safety: 7`, `doc: 20`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.001
  * `Choke Point (Betweenness):` 0.000915 | `Ripple Effect (Closeness):` 0.052412
  * `Imports (Out-Degree: 12):` ecpsvm.c, ecpsvm.h, hercules.h, hstdinc.h, inline.h, opcode.h
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `panel.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.019)
- **Top Global Matches:** file_cluster_4: 6.019, file_cluster_6: 9.904, file_cluster_16: 11.374
- **Magnitude:** 2669.1 | **LOC:** 3347 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 0.852; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.4%)
- **Documentation Coverage:** 74.0815% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `panel_display` **(Compute Cores)** (Impact: 465.8)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Panel display thread */ /...
  * `NP_update` **(Many-Argument Workhorses)** (Impact: 279.9)
    * *Intent:* /*=NP================================================================*/ /* This refreshes the screen...
  * `NP_screen_redraw` **(Many-Argument Workhorses)** (Impact: 60.1)
    * *Intent:* /*=NP================================================================*/ /* This draws the initial sc...
  * `set_console_title` **(Compute Cores)** (Impact: 38.0)
  * `do_panel_command` **(Stateful Encapsulated Methods)** (Impact: 13.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 502 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 1602
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 765`, `structural_boundaries: 182`, `args: 264`, `func_start: 41`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 598`, `fragile_debt: 5`, `unreferenced_by_name: 2`
* *Architecture:* `io: 5`, `api: 6`, `import: 7`
* *Defense:* `safety: 27`, `doc: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.852
  * `Choke Point (Betweenness):` 0.001725 | `Ripple Effect (Closeness):` 0.052449
  * `Imports (Out-Degree: 23):` devtype.h, fillfnam.h, hconsole.h, hercules.h, history.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ltdl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.52)
- **Top Global Matches:** file_cluster_4: 7.52, file_cluster_16: 8.216, file_cluster_12: 9.063
- **Magnitude:** 2531.16 | **LOC:** 4526 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **66** in-repo importer(s); it depends on **26**; blast radius 12.753; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.7%), Guard Balance (formerly Safety Score) (64.5%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_dlopen` **(Many-Argument Workhorses)** (Impact: 138.3)
  * `load_deplibs` **(Many-Argument Workhorses)** (Impact: 61.8)
  * `lt_dlloader_add` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* /* --- USER MODULE LOADER API --- */
  * `foreach_dirinpath` **(Many-Argument Workhorses)** (Impact: 32.9)
    * *Intent:* it is appended to each SEARCH_PATH element before FUNC is called. */
  * `canonicalize_path` **(Many-Argument Workhorses)** (Impact: 29.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 386 instances
* *State Mutation (weighted view):* 1179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 506`, `structural_boundaries: 267`, `args: 97`, `func_start: 101`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 407`, `planned_debt: 2`, `unreferenced_by_name: 22`
* *Architecture:* `io: 2`, `api: 44`, `import: 27`
* *Defense:* `safety: 127`, `immutability_locks: 168`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.753
  * `Choke Point (Betweenness):` 0.006735 | `Ripple Effect (Closeness):` 0.134383
  * `Imports (Out-Degree: 2):` argz.h, assert.h, config.h, ctype.h, dirent.h, dl.h, dld.h, dlfcn.h...
  * `Imported By (In-Degree: 66):` (Excluded from Brief to save tokens)

### `dasdutil.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.717)
- **Top Global Matches:** file_cluster_8: 9.717, file_cluster_3: 15.455, file_cluster_6: 21.737
- **Magnitude:** 2448.36 | **LOC:** 2289 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **5**; blast radius 1.571; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.6%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_ckd_file` **(Many-Argument Workhorses)** (Impact: 320.0)
    * *Intent:* /* volcyls Total number of cylinders on volume */ /* volser Volume serial number */ /* comp Compress...
  * `create_ckd` **(Many-Argument Workhorses)** (Impact: 116.7)
    * *Intent:* /* nullfmt xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx */ /* rawflag create raw image (skip speci...
  * `capacity_calc` **(Many-Argument Workhorses)** (Impact: 112.5)
    * *Intent:* /* numrecs Number of records of specified length per track */ /* numhead Number of tracks per cylind...
  * `create_compressed_fba` **(Many-Argument Workhorses)** (Impact: 108.2)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Subroutine to create a co...
  * `open_ckd_image` **(Many-Argument Workhorses)** (Impact: 85.8)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Subroutine to open a CKD ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 12 instances
* *Amplified Cascading Flux:* 397 instances
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 1302
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 115`, `args: 104`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 508`, `fragile_debt: 2`, `unreferenced_by_name: 14`
* *Architecture:* `io: 40`, `api: 21`, `import: 5`
* *Defense:* `safety: 8`, `immutability_locks: 1`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.571
  * `Choke Point (Betweenness):` 0.001126 | `Ripple Effect (Closeness):` 0.041389
  * `Imports (Out-Degree: 12):` dasdblks.h, devtype.h, hercules.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `general2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.755)
- **Top Global Matches:** file_cluster_6: 6.755, file_cluster_4: 9.768, file_cluster_8: 16.519
- **Magnitude:** 2402.96 | **LOC:** 2941 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.732; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.5%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convert_utf8_to_utf32` **(Compute Cores)** (Impact: 109.5)
    * *Intent:* #if defined(FEATURE_EXTENDED_TRANSLATION_FACILITY_3) /*---------------------------------------------...
  * `perform_locked_operation` **(Compute Cores)** (Impact: 91.0)
    * *Intent:* #if defined(FEATURE_PERFORM_LOCKED_OPERATION) /*----------------------------------------------------...
  * `or_character` **(Compute Cores)** (Impact: 60.3)
    * *Intent:* /*-------------------------------------------------------------------*/ /* D6 OC - Or Characters [SS...
  * `translate_and_test_extended` **(Compute Cores)** (Impact: 41.3)
    * *Intent:* #endif /*defined(FEATURE_EXTENDED_TRANSLATION_FACILITY_3)*/ #ifdef FEATURE_PARSING_ENHANCEMENT_FACIL...
  * `translate_and_test_reverse_extended` **(Compute Cores)** (Impact: 41.3)
    * *Intent:* /*-------------------------------------------------------------------*/ /* B9BD TRTRE - Translate an...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 479 instances
* *State Mutation (weighted view):* 1522
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 428`, `structural_boundaries: 81`, `args: 49`, `func_start: 46`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 5`, `state_mutation: 564`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `api: 45`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.732
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` clock.h, general2.c, hercules.h, hstdinc.h, inline.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shared.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.368)
- **Top Global Matches:** file_cluster_6: 7.368, file_cluster_8: 9.6, file_cluster_4: 15.412
- **Magnitude:** 2343.44 | **LOC:** 3082 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 0.857; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.8%), Complexity Load (formerly Cognitive Load) (72.0%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serverRequest` **(Many-Argument Workhorses)** (Impact: 191.9)
    * *Intent:* } /* recvData */ /*------------------------------------------------------------------- * Process a r...
  * `shared_ckd_init` **(Many-Argument Workhorses)** (Impact: 130.2)
    * *Intent:* } /* shared_update_notify */ /*------------------------------------------------------------------- *...
  * `shared_fba_init` **(Many-Argument Workhorses)** (Impact: 100.5)
    * *Intent:* } /* shared_ckd_close */ /*------------------------------------------------------------------- * FBA...
  * `recvData` **(Many-Argument Workhorses)** (Impact: 84.7)
    * *Intent:* } /* clientRecv */ /*------------------------------------------------------------------- * Receive d...
  * `serverConnect` **(Compute Cores)** (Impact: 66.7)
    * *Intent:* } /* findDevice */ /*------------------------------------------------------------------- * Connect a...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 365 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 1157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 466`, `structural_boundaries: 196`, `args: 162`, `func_start: 40`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 427`, `fragile_debt: 1`
* *Architecture:* `io: 18`, `api: 10`, `import: 4`
* *Defense:* `safety: 6`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.857
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.045477
  * `Imports (Out-Degree: 15):` devtype.h, hercules.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ctcadpt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.518)
- **Top Global Matches:** file_cluster_8: 8.518, file_cluster_3: 15.608, file_cluster_6: 20.854
- **Magnitude:** 2334.62 | **LOC:** 3610 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.732; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.7%), Guard Balance (formerly Safety Score) (72.7%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CTCE_ExecuteCCW` **(Many-Argument Workhorses)** (Impact: 196.2)
    * *Intent:* // Hercules PC Host A with IP address 192.168.1.100 : // // 0E40 CTCE 30880 192.168.1.200 30880 // 0...
  * `CTCE_Trace` **(Many-Argument Workhorses)** (Impact: 173.1)
    * *Intent:* // --------------------------------------------------------------------- // CTCE_Trace // ----------...
  * `CTCX_ExecuteCCW` **(Many-Argument Workhorses)** (Impact: 170.9)
    * *Intent:* // ------------------------------------------------------------------- // Execute a Channel Command ...
  * `CTCE_Send` **(Many-Argument Workhorses)** (Impact: 125.9)
    * *Intent:* // // CTCE_Send //
  * `CTCE_RecvThread` **(Many-Argument Workhorses)** (Impact: 96.8)
    * *Intent:* // // CTCE_RecvThread //
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 320 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 1086
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 158`, `args: 129`, `func_start: 25`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 4`, `state_mutation: 446`, `dead_code: 14`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 18`, `api: 14`, `import: 6`
* *Defense:* `safety: 15`, `doc: 7`, `immutability_locks: 25`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.732
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` ctcadpt.h, devtype.h, hercules.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `memrchr.c` (C) | Magnitude: 18.28 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 7, pointers: 5, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `decNumber/example3.c` (C) | Magnitude: 16.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 42, pointers: 37, structural_boundaries: 4, debug_prints: 4
- `autoconf/libtool.m4` (M4) | Magnitude: 309.22 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 2331, core_var_decl: 907, args: 874, design_snake_case: 746
- `esame.c` (C) | Magnitude: 4252.26 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 2635, pointers: 1246, globals: 857, state_mutation: 855

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `cache.c` (C) | Magnitude: 560.86 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 314, branch: 112, structural_boundaries: 83, state_mutation: 82

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `external.c` (C) | Magnitude: 152.16 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 256, pointers: 85, macros: 80, branch: 67
- `ctcadpt.h` (C) | Magnitude: 80.9 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 235, structural_boundaries: 91, macros: 72, class_start: 56
- `vm.c` (C) | Magnitude: 609.52 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 815, pointers: 282, branch: 221, state_mutation: 208

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `m4/lib-link.m4` (M4) | Magnitude: 37.4 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 401, core_var_decl: 103, design_snake_case: 96, args: 27
- `hercules.cnf.rexx` (REXX) | Magnitude: 82.7 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 30, structural_boundaries: 28, core_var_decl: 27, state_mutation: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `decNumber/example5.c` (C) | Magnitude: 13.86 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 20, pointers: 8, branch: 2, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `bootstrap.c` (C) | Magnitude: 245.04 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 341, args: 54, state_mutation: 49, branch: 46

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `channel.c` -> **Severity: 1.853** (Bridge: 0.0185 * Flux: 100.0%)
- `sockdev.c` -> **Severity: 1.829** (Bridge: 0.0183 * Flux: 99.9999%)
- `hsccmd.c` -> **Severity: 1.747** (Bridge: 0.0175 * Flux: 100.0%)
- `service.c` -> **Severity: 0.95** (Bridge: 0.0095 * Flux: 100.0%)
- `hscutl.c` -> **Severity: 0.916** (Bridge: 0.0092 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `decNumber/decNumber.c` -> **Severity: 13.413** (Embedded: 0.1554 * Error Risk: 86.3235%)
- `hthreads.c` -> **Severity: 10.637** (Embedded: 0.1376 * Error Risk: 77.2978%)
- `chain.h` -> **Severity: 10.579** (Embedded: 0.1322 * Error Risk: 80.0%)
- `extstring.h` -> **Severity: 10.175** (Embedded: 0.1414 * Error Risk: 71.9449%)
- `hscutl.c` -> **Severity: 9.902** (Embedded: 0.1332 * Error Risk: 74.3483%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `decNumber/decNumber.c` -> **Severity: 1958.1** (Blast Radius: 19.581 * Doc Risk: 100.0%)
- `hscutl.c` -> **Severity: 1195.751** (Blast Radius: 16.798 * Doc Risk: 71.1841%)
- `logmsg.c` -> **Severity: 1021.801** (Blast Radius: 13.206 * Doc Risk: 77.374%)
- `hthreads.c` -> **Severity: 994.952** (Blast Radius: 12.859 * Doc Risk: 77.374%)
- `ltdl.c` -> **Severity: 986.751** (Blast Radius: 12.753 * Doc Risk: 77.374%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `3` files carry mainframe facts -- `7` call sites, `13` dataset bindings, `0` record items.

### `util/rawstape.jcl` (JCL)
- **Calls:** `EXEC PGM ASMA90`, `EXEC PGM IEWL`, `EXEC PGM IEBGENER`
- **Datasets:** `SYSLIB→SYS1.MACLIB`, `SYSLIB→SYS1.MODGEN`, `SYSLMOD→IBMUSER.LOAD(RAWSTAPE)`, `SYSUT1→IBMUSER.SADUMP.AWS`, `SYSUT2→IBMUSER.SADUMP`, `SYSUT2→IBMUSER.SADUMP`
- **Job flow:** `ASMA90=ASMA90` -> `IEWL=IEWL` -> `CONVERT=*.IEWL.SYSLMOD` -> `SETDCB=IEBGENER`; creates `&&PUNCH`, `IBMUSER.SADUMP`

### `util/awswrite.jcl` (JCL)
- **Calls:** `EXEC PGM ASMA90`, `EXEC PGM IEWL`
- **Datasets:** `SYSLIB→SYS1.MACLIB`, `SYSLIB→SYS1.MODGEN`, `AWSIN→&SYSUID..XXXXXX.AWSTAPE`
- **Job flow:** `ASMCLG=PROC ASMCLG`; creates `&&GOSET(GO)`, `&&OBJSET`

### `util/tapeconv.jcl` (JCL)
- **Calls:** `EXEC PGM ASMA90`, `EXEC PGM IEWL`
- **Datasets:** `SYSLIB→SYS1.MACLIB`, `SYSLIB→SYS1.MODGEN`, `SYSUT1→TAPE.DATASET`, `SYSUT2→IBMUSER.AWSTAPE.DATASET`
- **Job flow:** `ASMCLG=PROC ASMCLG`; creates `&&GOSET(GO)`, `&&OBJSET`, `IBMUSER.AWSTAPE.DATASET`

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: scheduler export (CA-7 / Control-M / TWS) (3 gaps).

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 891 literal sites + 3 sites through wrappers = 894
- **`memory_alloc`:** 903 literal sites + 70 sites through wrappers = 973
- **`panics_and_aborts`:** 1783 literal sites + 49 sites through wrappers = 1832

- `free_aligned` (macro, memory_alloc, primitive): 31 call sites in 6 files -- `hmalloc.h`
- `devnotfound_msg` (function, panics_and_aborts, primitive): 14 call sites in 1 files -- `hsccmd.c`
- `syntax` (function, panics_and_aborts, primitive): 13 call sites in 1 files -- `cckddiag.c`
- `cckd_free` (function, memory_alloc, primitive): 11 call sites in 1 files -- `cckddasd.c`
- `clean` (function, memory_alloc, primitive): 8 call sites in 1 files -- `cckddiag.c`
- `copy_to_historyCmdLine` (function, memory_alloc, primitive): 6 call sites in 1 files -- `history.c`
- `fork` (function, panics_and_aborts, primitive): 5 call sites in 4 files -- `w32util.c`
- `syntax` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `cckdcdsk.c`
- `syntax` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `cckdcomp.c`
- `syntax` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `cckdswap.c`
- `initrecs` (function, memory_alloc, primitive): 3 call sites in 1 files -- `vmfplc2.c`
- `test_abort` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `script.c`
*(+12 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 25716 call pairs -- scoped 14.0%, unique 19.1%, ambiguous 0.4%, external 66.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 24472 | 13.8% | 20.1% | 0.4% | 65.7% |
| m4 | 637 | 11.8% | 1.3% | 0.0% | 87.0% |
| hlasm | 419 | 6.0% | 0.0% | 0.0% | 94.0% |
| shell | 63 | 22.2% | 0.0% | 0.0% | 77.8% |
| batch | 59 | 98.3% | 0.0% | 0.0% | 1.7% |
| rexx | 50 | 78.0% | 0.0% | 0.0% | 22.0% |
| perl | 12 | 25.0% | 0.0% | 0.0% | 75.0% |
| jcl | 3 | 66.7% | 0.0% | 0.0% | 33.3% |
| html | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
