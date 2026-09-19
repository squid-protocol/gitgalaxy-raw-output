# ARCHITECTURAL_BRIEF: hyperion
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/hercules-390/hyperion.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 672 analyzed artifact(s), 265986 LOC.
- **Load-bearing artifact:** `hercules.h` -- 193 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `hstdinc.h` -- pulls in 77 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `decNumber/decNumber.c` at magnitude 9998.4 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 672 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 367 |
| Total LOC | 265986 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 64.7% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4343 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2595 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1859 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 27 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 328 | 222324 | 48.8% |
| PLAINTEXT | 177 | 0 | 26.3% |
| HTML | 60 | 20566 | 8.9% |
| M4 | 33 | 3675 | 4.9% |
| HLASM | 33 | 12882 | 4.9% |
| REXX | 14 | 2278 | 2.1% |
| BATCH | 9 | 2723 | 1.3% |
| SHELL | 8 | 592 | 1.2% |
| MARKDOWN | 4 | 0 | 0.6% |
| JCL | 3 | 686 | 0.4% |
| CSS | 1 | 120 | 0.1% |
| PERL | 1 | 139 | 0.1% |
| BINARY_THREAT | 1 | 1 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `3.755`
> **Composition Archetype:** `Hub-Coupled App` (z +3.75; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 38%, Declarative / Non-Code 22%, Many-Argument Workhorses Files 11%, Large Core Modules 10%, Large Core Modules (3) 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 490 | 72.9% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 181 | 26.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 367*

**Composition by Extension & Reason:**
- `.tst`: 64x Excluded (Unsupported Extension: '.tst')
- `.gif`: 44x Excluded (Explicitly Denied Extension: '.gif')
- `.core`: 33x Excluded (Unsupported Extension: '.core')
- `.list`: 32x Excluded (Unsupported Extension: '.list')
- `.msvc`: 29x Excluded (Unsupported Extension: '.msvc'), 1x Excluded (Unsupported Extension: '.MSVC')
- `.cmake`: 22x Excluded (Unsupported Extension: '.cmake')
- `.assemble`: 13x Excluded (Unsupported Extension: '.assemble')
- `.listing`: 13x Excluded (Unsupported Extension: '.listing')
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Excluded (Lexical Monotony: High structural repetition detected in 4119 LOC)
- `.am`: 8x Excluded (Unsupported Extension: '.am')
- `.subtst`: 8x Excluded (Unsupported Extension: '.subtst')
- `.png`: 6x Excluded (Explicitly Denied Extension: '.png')
- `.rc`: 5x Excluded (Unsupported Extension: '.rc')
- `.ico`: 5x Excluded (Explicitly Denied Extension: '.ico')
- `.sln`: 4x Excluded (Unsupported Extension: '.sln')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.4 | 29.8 | 7.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 46.4 | 53.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 23.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.0 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 47.6 | 2.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 46.1 | 77.4 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 62021 | 297 | 235 | `ctc_ptp.c` |
| cleanup | 732 | 101 | 2 | `qeth.c` |
| guards | 7204 | 293 | 38 | `ltdl.c` |
| danger | 3792 | 188 | 15 | `hsccmd.c` |
| concurrency | 92 | 43 | 0 | `autoconf/mkinstalldirs` |
| connectivity | 5517 | 367 | 21 | `hexterns.h` |
| io | 3322 | 165 | 9 | `html/hercconf.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 148 | 30 | 0 | `ctcadpt.c` |
| time | 116 | 44 | 0 | `hsccmd.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 33 | 9 | 0 | `hao.c` |
| events | 249 | 50 | 0 | `configure.ac` |
| tests | 1 | 1 | 0 | `autogen.sh` |
| docs | 819 | 141 | 2 | `w32util.c` |
| debt | 1219 | 167 | 3 | `tests/runtest.rexx` |
| mutation | 61407 | 368 | 247 | `ctc_ptp.c` |
| dead_code | 1471 | 239 | 4 | `decNumber/decNumber.c` |
| credential | 8 | 7 | 0 | `m4/gettext.m4` |
| threat | 2050 | 150 | 5 | `opcode.h` |
| ml_ai | 1892 | 121 | 7 | `hsccmd.c` |
| ui | 3038 | 44 | 0 | `html/hercmsdl.html` |

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

1. **hercules.h** (`hercules.h`) — 193 inbound connections
2. **hstdinc.h** (`hstdinc.h`) — 172 inbound connections
3. **opcode.h** (`opcode.h`) — 85 inbound connections
4. **hercules.css** (`html/hercules.css`) — 55 inbound connections
5. **inline.h** (`inline.h`) — 45 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **hstdinc.h** (`hstdinc.h`) — 77 outbound dependencies
2. **hercules.h** (`hercules.h`) — 44 outbound dependencies
3. **ltdl.c** (`ltdl.c`) — 26 outbound dependencies
4. **dyncrypt.c** (`crypto/dyncrypt.c`) — 11 outbound dependencies
5. **hsccmd.c** (`hsccmd.c`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ckddasd_execute_ccw` **(Many-Argument Workhorses)** (@ `ckddasd.c`) -> Impact: **1832.9** | LOC: 2086
  * *Intent:* } /* end function ckd_write_data */ /*-------------------------------------------------------------------*/ /* Execute a Channel Command Word */ /*---...
- `decLnOp` **(Many-Argument Workhorses)** (@ `decNumber/decNumber.c`) -> Impact: **1422.2** | LOC: 2460
  * *Intent:* /* 3. Fastpaths are included for ln(10) and ln(2), up to length 40, */ /* as these are common requests. ln(10) is used by log10(x). */ /* */ /* 4. An ...
- `tapedev_execute_ccw` **(Many-Argument Workhorses)** (@ `tapeccws.c`) -> Impact: **1341.3** | LOC: 2855
- `cckd_chkdsk` **(Many-Argument Workhorses)** (@ `cckdutil.c`) -> Impact: **882.8** | LOC: 1618
  * *Intent:* /*------------------------------------------------------------------- * Perform check function on a compressed ckd file * * check levels * -1 devhdr, ...
- `resume_cmd` **(Many-Argument Workhorses)** (@ `sr.c`) -> Impact: **731.4** | LOC: 1068
  * *Intent:* #define SR_NULL_REGS_CHECK(_regs) if ((_regs) == NULL) goto sr_null_regs_exit;
- `commadpt_execute_ccw` **(Many-Argument Workhorses)** (@ `commadpt.c`) -> Impact: **715.5** | LOC: 939
  * *Intent:* /*-------------------------------------------------------------------*/ /* Execute a Channel Command Word */ /*---------------------------------------...
- `panel_display` **(Compute Cores)** (@ `panel.c`) -> Impact: **491.8** | LOC: 1376
  * *Intent:* /*-------------------------------------------------------------------*/ /* Panel display thread */ /* */ /* This function runs on the main thread. It ...
- `printer_execute_ccw` **(Many-Argument Workhorses)** (@ `printer.c`) -> Impact: **450.9** | LOC: 497
  * *Intent:* } /* end function printer_close_device */ /*-------------------------------------------------------------------*/ /* Execute a Channel Command Word */...
- `decDivideOp` **(Many-Argument Workhorses)** (@ `decNumber/decNumber.c`) -> Impact: **404.8** | LOC: 582
  * *Intent:* /* exp=exp-1 */ /* end outer_loop */ /* exp=exp+1 -- set the proper exponent */ /* if have=0 then generate answer=0 */ /* Return (Result is defined by...
- `w32_init_hostinfo` **(Compute Cores)** (@ `w32util.c`) -> Impact: **402.6** | LOC: 726

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 308 | 165646.34 | 40.53% | 14.17% |
| `decNumber` | 32 | 18867.98 | 26.57% | 23.83% |
| `tests` | 196 | 3379.0 | 1.46% | 0.0% |
| `util` | 11 | 764.98 | 13.62% | 0.0% |
| `scripts` | 8 | 668.18 | 44.36% | 14.21% |
| `m4` | 30 | 278.62 | 0.61% | 67.23% |
| `CMake` | 11 | 115.18 | 8.51% | 48.7% |
| `autoconf` | 3 | 87.82 | 24.98% | 33.33% |
| `crypto` | 8 | 27.46 | 38.0% | 15.88% |
| `man` | 4 | 8.92 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ccfixme.h` -> **100.0%** Exposure
- `CMake/CMakeHercTestRegparm3.c` -> **99.9983%** Exposure
- `autoconf/hercules.m4` -> **99.9931%** Exposure
- `scripts/hcommand.rexx` -> **99.9617%** Exposure
- `m4/printf-posix.m4` -> **99.929%** Exposure
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
- **Unknown Dependencies:** `1176` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `decNumber/decNumber.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 9998.4 | **LOC:** 8142 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Complexity Load (formerly Cognitive Load) (95.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decLnOp` **(Many-Argument Workhorses)** (Impact: 1422.2)
    * *Intent:* /* 3. Fastpaths are included for ln(10) and ln(2), up to length 40, */ /* as these are common reques...
  * `decDivideOp` **(Many-Argument Workhorses)** (Impact: 404.8)
    * *Intent:* /* exp=exp-1 */ /* end outer_loop */ /* exp=exp+1 -- set the proper exponent */ /* if have=0 then ge...
  * `decAddOp` **(Many-Argument Workhorses)** (Impact: 252.6)
    * *Intent:* /* overlap the A or B coefficient */ /* then the result must be calculated into a temporary buffer. ...
  * `decNumberPower` **(Many-Argument Workhorses)** (Impact: 224.3)
    * *Intent:* /* Mathematical function restrictions apply (see above); a NaN is */ /* returned with Invalid_operat...
  * `decCompareOp` **(Many-Argument Workhorses)** (Impact: 216.6)
    * *Intent:* /* */ /* res is C, the result. C may be A and/or B (e.g., X=X?X) */ /* lhs is A */ /* rhs is B */ /*...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 49 instances
* *Amplified Cascading Flux:* 1431 instances
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 4380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1652`, `structural_boundaries: 514`, `args: 169`, `func_start: 102`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 1518`, `dead_code: 79`, `fragile_debt: 4`, `unreferenced_by_name: 49`
* *Architecture:* `api: 67`, `import: 6`
* *Defense:* `safety: 2`, `immutability_locks: 202`, `cleanup: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ctype.h, decNumber.h, decNumberLocal.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hsccmd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 7647.14 | **LOC:** 8865 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.4%)
- **Documentation Coverage:** 77.0595% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mt_cmd` **(Many-Argument Workhorses)** (Impact: 194.5)
    * *Intent:* /*-------------------------------------------------------------------*/ /* mt command - magnetic tap...
  * `qd_cmd` **(Many-Argument Workhorses)** (Impact: 159.0)
    * *Intent:* /*-------------------------------------------------------------------*/ /* qd command - query device...
  * `automount_cmd` **(Many-Argument Workhorses)** (Impact: 156.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /* automount_cmd - show or u...
  * `qeth_cmd` **(Many-Argument Workhorses)** (Impact: 145.2)
    * *Intent:* /*-------------------------------------------------------------------*/ /* qeth command - enable/dis...
  * `fcb_cmd` **(Many-Argument Workhorses)** (Impact: 125.1)
    * *Intent:* /*-------------------------------------------------------------------*/ /* fcb - display or load */ ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 33 instances
* *Amplified Cascading Flux:* 964 instances
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 2932
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1929`, `structural_boundaries: 516`, `args: 779`, `func_start: 130`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 1004`, `dead_code: 7`, `unreferenced_by_name: 107`
* *Architecture:* `io: 44`, `api: 124`, `import: 11`
* *Defense:* `safety: 20`, `doc: 2`, `immutability_locks: 21`, `cleanup: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` ctc_ptp.h, ctcadpt.h, dasdtab.h, devtype.h, hercules.h, history.h, hstdinc.h, httpmisc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ctc_ptp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6771.64 | **LOC:** 9608 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.1%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_conf_stmt` **(Many-Argument Workhorses)** (Impact: 339.1)
    * *Intent:* /* ------------------------------------------------------------------ */ /* parse_conf_stmt() */ /* ...
  * `write_rrh_C108` **(Many-Argument Workhorses)** (Impact: 332.5)
    * *Intent:* } /* End function write_rrh_C17E() */ /* -----------------------------------------------------------...
  * `write_rrh_417E` **(Many-Argument Workhorses)** (Impact: 155.6)
    * *Intent:* } /* End function point_CSVcv() */ /* --------------------------------------------------------------...
  * `gen_csv_sid` **(Many-Argument Workhorses)** (Impact: 152.5)
    * *Intent:* // values the output token value will always be the same. // For example:- // if Clock1 is always C5...
  * `get_preconfigured_value` **(Many-Argument Workhorses)** (Impact: 125.8)
    * *Intent:* } /* End function parse_conf_stmt() */ /* ----------------------------------------------------------...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 27 instances
* *Amplified Cascading Flux:* 1071 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 4291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 861`, `structural_boundaries: 335`, `args: 349`, `func_start: 55`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 167`, `state_mutation: 2149`, `dead_code: 36`, `fragile_debt: 5`
* *Architecture:* `io: 2`, `api: 55`, `import: 10`
* *Defense:* `safety: 15`, `immutability_locks: 3`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` ctc_ptp.h, ctcadpt.h, herc_getopt.h, hercules.h, hstdinc.h, ifaddrs.h, mpc.h, opcode.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cckddasd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 5685.22 | **LOC:** 6188 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.0%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cckd_command` **(Many-Argument Workhorses)** (Impact: 226.5)
    * *Intent:* /*-------------------------------------------------------------------*/ /* cckd command processor */...
  * `cckd_sf_remove` **(Compute Cores)** (Impact: 107.2)
    * *Intent:* } /* end function cckd_sf_add */ /*-----------------------------------------------------------------...
  * `cckd_gc_percolate` **(Many-Argument Workhorses)** (Impact: 103.1)
    * *Intent:* } /* end thread cckd_gcol */ /*-------------------------------------------------------------------*/...
  * `cckd_read_trk` **(Many-Argument Workhorses)** (Impact: 98.6)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Read a track image */ /* ...
  * `cckd_gcol` **(Compute Cores)** (Impact: 74.6)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Garbage Collection thread...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 991 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 3130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1067`, `structural_boundaries: 376`, `args: 398`, `func_start: 89`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1148`, `dead_code: 12`, `fragile_debt: 3`
* *Architecture:* `io: 9`, `api: 177`, `import: 4`
* *Defense:* `safety: 14`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` devtype.h, hercules.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ckddasd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 5398.02 | **LOC:** 6157 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Complexity Load (formerly Cognitive Load) (95.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ckddasd_execute_ccw` **(Many-Argument Workhorses)** (Impact: 1832.9)
    * *Intent:* } /* end function ckd_write_data */ /*--------------------------------------------------------------...
  * `ckddasd_init_handler` **(Many-Argument Workhorses)** (Impact: 244.2)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Initialize the device han...
  * `ckd_read_count` **(Many-Argument Workhorses)** (Impact: 105.3)
    * *Intent:* } /* end function mt_advance */ /*------------------------------------------------------------------...
  * `ckddasd_hresume` **(Many-Argument Workhorses)** (Impact: 87.3)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Hercules resume */ /*----...
  * `ckd_build_sense` **(Many-Argument Workhorses)** (Impact: 83.8)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Build sense data */ /*---...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 845 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 2630
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1244`, `structural_boundaries: 449`, `args: 159`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 940`, `fragile_debt: 5`
* *Architecture:* `io: 14`, `api: 15`, `import: 5`
* *Defense:* `safety: 4`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` dasdblks.h, devtype.h, hercules.h, hstdinc.h, sr.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `qeth.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4366.76 | **LOC:** 6666 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.1%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `osa_adapter_cmd` **(Many-Argument Workhorses)** (Impact: 385.8)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Adapter Command Routine *...
  * `qeth_execute_ccw` **(Many-Argument Workhorses)** (Impact: 378.6)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Execute a Channel Command...
  * `qeth_init_handler` **(Many-Argument Workhorses)** (Impact: 198.4)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Initialize the device han...
  * `write_buffered_packets` **(Many-Argument Workhorses)** (Impact: 109.0)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Write all packets/frames ...
  * `read_L2_packets` **(Many-Argument Workhorses)** (Impact: 59.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Read one L2 frame from TA...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 55 instances
* *Amplified Cascading Flux:* 610 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 2086
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 848`, `structural_boundaries: 313`, `args: 274`, `func_start: 83`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 188`, `state_mutation: 866`, `dead_code: 12`, `fragile_debt: 24`
* *Architecture:* `io: 1`, `api: 2`, `import: 11`
* *Defense:* `safety: 14`, `immutability_locks: 12`, `cleanup: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` chsc.h, ctcadpt.h, dbgtrace.h, devtype.h, hercifc.h, hercules.h, hstdinc.h, mpc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `float.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4023.92 | **LOC:** 7873 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.3%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_ef` **(Many-Argument Workhorses)** (Impact: 147.0)
    * *Intent:* } /* end function add_lf */ /*-------------------------------------------------------------------*/ ...
  * `add_sf` **(Many-Argument Workhorses)** (Impact: 107.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /*--------------------------...
  * `add_lf` **(Many-Argument Workhorses)** (Impact: 107.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Add long float */ /* */ /...
  * `cmp_sf` **(Many-Argument Workhorses)** (Impact: 79.0)
    * *Intent:* } /* end function add_ef */ /*-------------------------------------------------------------------*/ ...
  * `cmp_lf` **(Many-Argument Workhorses)** (Impact: 79.0)
    * *Intent:* } /* end function cmp_sf */ /*-------------------------------------------------------------------*/ ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 928 instances
* *State Mutation (weighted view):* 2969
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1013`, `structural_boundaries: 142`, `args: 60`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `state_mutation: 1113`, `planned_debt: 1`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` float.c, hercules.h, hstdinc.h, inline.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `decNumber/decBasic.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3901.02 | **LOC:** 3912 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 1.101; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Complexity Load (formerly Cognitive Load) (80.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decDivide` **(Many-Argument Workhorses)** (Impact: 345.7)
    * *Intent:* /* */ /* result gets the result of dividing dfl by dfr: */ /* dfl is the first decFloat (lhs) */ /* ...
  * `decFloatFMA` **(Many-Argument Workhorses)** (Impact: 192.2)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decFloatFMA -- multiply ...
  * `decFloatAdd` **(Many-Argument Workhorses)** (Impact: 177.6)
    * *Intent:* #endif
  * `decFloatQuantize` **(Many-Argument Workhorses)** (Impact: 152.4)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decFloatQuantize -- quan...
  * `decFiniteMultiply` **(Many-Argument Workhorses)** (Impact: 140.3)
    * *Intent:* #define MULTBASE ((uInt)BILLION) // the base used for multiply #define MULOPLEN DECPMAX9 // operand ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 610 instances
* *State Mutation (weighted view):* 1905
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 738`, `structural_boundaries: 325`, `args: 89`, `func_start: 72`, `class_start: 13`
* *Risk/State:* `state_mutation: 685`, `dead_code: 47`
* *Architecture:* `api: 64`
* *Defense:* `immutability_locks: 119`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.101
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002976
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `dasdload.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3656.54 | **LOC:** 4470 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.3%)
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
* *Structure:* `branch: 534`, `structural_boundaries: 275`, `args: 220`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 3`, `state_mutation: 744`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 21`, `api: 4`, `import: 3`
* *Defense:* `safety: 2`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` dasdblks.h, hercules.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `commadpt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3398.4 | **LOC:** 3783 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.8%), Complexity Load (formerly Cognitive Load) (92.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `commadpt_execute_ccw` **(Many-Argument Workhorses)** (Impact: 715.5)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Execute a Channel Command...
  * `commadpt_init_handler` **(Many-Argument Workhorses)** (Impact: 308.1)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Device Initialisation */ ...
  * `commadpt_thread` **(Compute Cores)** (Impact: 247.8)
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
* *Structure:* `branch: 641`, `structural_boundaries: 263`, `args: 123`, `func_start: 31`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 635`, `dead_code: 11`, `fragile_debt: 4`
* *Architecture:* `io: 12`, `api: 1`, `import: 5`
* *Defense:* `safety: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` commadpt.h, devtype.h, hercules.h, hstdinc.h, parser.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cckdutil.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3303.52 | **LOC:** 2932 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Complexity Load (formerly Cognitive Load) (99.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cckd_chkdsk` **(Many-Argument Workhorses)** (Impact: 882.8)
    * *Intent:* /*------------------------------------------------------------------- * Perform check function on a ...
  * `cckd_comp` **(Many-Argument Workhorses)** (Impact: 216.8)
    * *Intent:* /*------------------------------------------------------------------- * Remove all free space from a...
  * `cckd_swapend` **(Compute Cores)** (Impact: 94.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /* EXTERNALGUI support */ /*...
  * `cdsk_valid_trk` **(Many-Argument Workhorses)** (Impact: 78.7)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Validate a track image */...
  * `comp_spctab_sort` **(Stateful Encapsulated Methods)** (Impact: 19.6)
    * *Intent:* } /* cckd_comp() */ /*------------------------------------------------------------------- * cckd_com...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 25 instances
* *Amplified Cascading Flux:* 606 instances
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 1908
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 763`, `structural_boundaries: 119`, `args: 123`, `func_start: 14`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 696`, `dead_code: 39`, `unreferenced_by_name: 2`
* *Architecture:* `io: 56`, `api: 11`, `import: 3`
* *Defense:* `safety: 8`, `immutability_locks: 10`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` hercules.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `console.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3092.62 | **LOC:** 4518 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.9%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loc3270_execute_ccw` **(Many-Argument Workhorses)** (Impact: 271.5)
    * *Intent:* } /* end function console_connection_handler */ /*--------------------------------------------------...
  * `telnet_ev_handler` **(Many-Argument Workhorses)** (Impact: 185.3)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Telnet event handler */ /...
  * `build_logo` **(Many-Argument Workhorses)** (Impact: 156.8)
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
* *Structure:* `branch: 664`, `structural_boundaries: 212`, `args: 158`, `func_start: 38`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 511`, `dead_code: 2`, `fragile_debt: 5`
* *Architecture:* `io: 8`, `import: 8`
* *Defense:* `safety: 43`, `doc: 1`, `immutability_locks: 17`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` cnsllogo.h, devtype.h, hercules.h, hexdumpe.h, hexterns.h, hstdinc.h, opcode.h, sr.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `channel.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3063.84 | **LOC:** 6323 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.9%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `halt_subchan` **(Many-Argument Workhorses)** (Impact: 70.4)
    * *Intent:* /*-------------------------------------------------------------------*/ /* HALT SUBCHANNEL */ /*----...
  * `schedule_ioq` **(Many-Argument Workhorses)** (Impact: 38.4)
    * *Intent:* /* */ /* */ /* Locks Used: */ /* */ /* None */ /* */ /* */ /* Returns: */ /* */ /* 0 - Success */ /*...
  * `cancel_subchan` **(Many-Argument Workhorses)** (Impact: 35.6)
    * *Intent:* /*-------------------------------------------------------------------*/ /* CANCEL SUBCHANNEL */ /*--...
  * `haltio` **(Many-Argument Workhorses)** (Impact: 35.1)
    * *Intent:* } /* end function testio */ /*-------------------------------------------------------------------*/ ...
  * `clear_subchan` **(Many-Argument Workhorses)** (Impact: 34.7)
    * *Intent:* /*-------------------------------------------------------------------*/ /* CLEAR SUBCHANNEL */ /*---...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 641 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 2043
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1059`, `structural_boundaries: 232`, `args: 227`, `func_start: 69`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 7`, `state_mutation: 761`, `dead_code: 6`, `fragile_debt: 4`
* *Architecture:* `api: 50`, `import: 7`
* *Defense:* `safety: 2`, `doc: 6`, `immutability_locks: 37`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` channel.c, chsc.h, devtype.h, hercules.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tapeccws.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 3007.48 | **LOC:** 4393 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.9%), Complexity Load (formerly Cognitive Load) (81.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 67.7022% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tapedev_execute_ccw` **(Many-Argument Workhorses)** (Impact: 1341.3)
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
* *Amplified Cascading Flux:* 344 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1056
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 562`, `structural_boundaries: 238`, `args: 160`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 368`, `dead_code: 7`, `fragile_debt: 14`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 25`, `import: 3`
* *Defense:* `safety: 1`, `doc: 25`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` hercules.h, hstdinc.h, tapedev.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `w32util.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2999.54 | **LOC:** 4756 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.0%)
- **Documentation Coverage:** 38.4406% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `w32_init_hostinfo` **(Compute Cores)** (Impact: 402.6)
  * `w32_select` **(Many-Argument Workhorses)** (Impact: 77.0)
  * `clock_gettime` **(Stateful Encapsulated Methods)** (Impact: 54.6)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////////////// // (PUBLI...
  * `w32_poor_mans_fork` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `w32_nanosleep` **(Stateful Encapsulated Methods)** (Impact: 47.8)
    * *Intent:* #endif // !defined( HAVE_GETTIMEOFDAY ) ////////////////////////////////////////////////////////////...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 30 instances
* *Amplified Cascading Flux:* 447 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 1423
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 697`, `structural_boundaries: 372`, `args: 268`, `func_start: 84`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 529`, `dead_code: 12`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 52`
* *Architecture:* `io: 5`, `api: 88`, `import: 3`
* *Defense:* `safety: 22`, `doc: 89`, `immutability_locks: 54`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` dbgtrace.h, hercules.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `general1.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2778.78 | **LOC:** 6029 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.4%), Complexity Load (formerly Cognitive Load) (71.6%), Debt Markers (formerly Tech Debt) (7.9%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DEF_INST` **(I/O & Config Routines)** (Impact: 5.3)
    * *Intent:* #define _GENERAL1_C_ #endif #include "hercules.h" #include "opcode.h" #include "inline.h" #include "...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 863 instances
* *State Mutation (weighted view):* 2693
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 860`, `structural_boundaries: 84`, `args: 144`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 4`, `state_mutation: 967`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` clock.h, general1.c, hercules.h, hstdinc.h, inline.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `panel.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2771.2 | **LOC:** 3347 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Complexity Load (formerly Cognitive Load) (93.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 74.0815% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `panel_display` **(Compute Cores)** (Impact: 491.8)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Panel display thread */ /...
  * `NP_update` **(Many-Argument Workhorses)** (Impact: 292.6)
    * *Intent:* /*=NP================================================================*/ /* This refreshes the screen...
  * `NP_screen_redraw` **(Many-Argument Workhorses)** (Impact: 72.8)
    * *Intent:* /*=NP================================================================*/ /* This draws the initial sc...
  * `set_console_title` **(Compute Cores)** (Impact: 40.8)
  * `copy_regs` **(Compute Cores)** (Impact: 13.3)
    * *Intent:* #endif // OPTION_MIPS_COUNTING /////////////////////////////////////////////////////////////////////...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 522 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 1642
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 837`, `structural_boundaries: 182`, `args: 264`, `func_start: 41`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 598`, `dead_code: 1`, `fragile_debt: 5`, `unreferenced_by_name: 2`
* *Architecture:* `io: 5`, `api: 6`, `import: 7`
* *Defense:* `safety: 27`, `doc: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` devtype.h, fillfnam.h, hconsole.h, hercules.h, history.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ltdl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2569.86 | **LOC:** 4526 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.4%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_dlopen` **(Many-Argument Workhorses)** (Impact: 138.3)
  * `load_deplibs` **(Many-Argument Workhorses)** (Impact: 65.3)
  * `lt_dlloader_add` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* /* --- USER MODULE LOADER API --- */
  * `foreach_dirinpath` **(Many-Argument Workhorses)** (Impact: 32.9)
    * *Intent:* it is appended to each SEARCH_PATH element before FUNC is called. */
  * `canonicalize_path` **(Many-Argument Workhorses)** (Impact: 29.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 392 instances
* *State Mutation (weighted view):* 1191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 591`, `structural_boundaries: 267`, `args: 97`, `func_start: 101`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 407`, `dead_code: 2`, `planned_debt: 2`, `unreferenced_by_name: 22`
* *Architecture:* `io: 2`, `api: 44`, `import: 27`
* *Defense:* `safety: 127`, `immutability_locks: 168`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` argz.h, assert.h, config.h, ctype.h, dirent.h, dl.h, dld.h, dlfcn.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ecpsvm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2519.4 | **LOC:** 5113 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.8%)
- **Documentation Coverage:** 71.3449% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ecpsvm_do_disp2` **(Many-Argument Workhorses)** (Impact: 127.8)
    * *Intent:* /* DISP2 Core */
  * `ecpsvm_dolctl` **(Many-Argument Workhorses)** (Impact: 117.4)
    * *Intent:* /* B7 - LCTL Instruction Assist */
  * `ecpsvm_dolra` **(Many-Argument Workhorses)** (Impact: 84.4)
    * *Intent:* */
  * `ecpsvm_dosio` **(Many-Argument Workhorses)** (Impact: 53.0)
    * *Intent:* /* operation exception and a trip */ /* through the DMKPRG & DMKPRV code */ /* path. In addition, th...
  * `ecpsvm_check_pswtrans` **(Many-Argument Workhorses)** (Impact: 35.0)
    * *Intent:* /* only if re-enabling bits (and no Int pending) */ /* */ /* For the time being, we do THIS : */ /* ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 478 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1579
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 441`, `structural_boundaries: 289`, `args: 703`, `func_start: 43`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 623`, `dead_code: 11`, `fragile_debt: 2`
* *Architecture:* `api: 36`, `import: 7`
* *Defense:* `safety: 7`, `doc: 20`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ecpsvm.c, ecpsvm.h, hercules.h, hstdinc.h, inline.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dasdutil.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2462.76 | **LOC:** 2289 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.9%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_ckd_file` **(Many-Argument Workhorses)** (Impact: 320.0)
    * *Intent:* /* volcyls Total number of cylinders on volume */ /* volser Volume serial number */ /* comp Compress...
  * `create_ckd` **(Many-Argument Workhorses)** (Impact: 127.9)
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
* *Structure:* `branch: 314`, `structural_boundaries: 115`, `args: 104`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 508`, `dead_code: 3`, `fragile_debt: 2`, `unreferenced_by_name: 14`
* *Architecture:* `io: 40`, `api: 21`, `import: 5`
* *Defense:* `safety: 8`, `immutability_locks: 1`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` dasdblks.h, devtype.h, hercules.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esame.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2424.06 | **LOC:** 8494 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.0%), Complexity Load (formerly Cognitive Load) (69.8%), Debt Markers (formerly Tech Debt) (7.9%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DEF_INST` **(I/O & Config Routines)** (Impact: 3.8)
    * *Intent:* #endif #if !defined(_ESAME_C_) #define _ESAME_C_ #endif #include "hercules.h" #include "opcode.h" #i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 733 instances
* *State Mutation (weighted view):* 2321
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1040`, `structural_boundaries: 59`, `args: 347`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 26`, `state_mutation: 855`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` clock.h, esame.c, hercules.h, hstdinc.h, inline.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shared.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2372.44 | **LOC:** 3082 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.6%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serverRequest` **(Many-Argument Workhorses)** (Impact: 194.2)
    * *Intent:* } /* recvData */ /*------------------------------------------------------------------- * Process a r...
  * `shared_ckd_init` **(Many-Argument Workhorses)** (Impact: 132.2)
    * *Intent:* } /* shared_update_notify */ /*------------------------------------------------------------------- *...
  * `shared_fba_init` **(Many-Argument Workhorses)** (Impact: 100.5)
    * *Intent:* } /* shared_ckd_close */ /*------------------------------------------------------------------- * FBA...
  * `recvData` **(Many-Argument Workhorses)** (Impact: 89.6)
    * *Intent:* } /* clientRecv */ /*------------------------------------------------------------------- * Receive d...
  * `serverConnect` **(Compute Cores)** (Impact: 66.7)
    * *Intent:* } /* findDevice */ /*------------------------------------------------------------------- * Connect a...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 367 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 1161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 483`, `structural_boundaries: 196`, `args: 162`, `func_start: 40`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 427`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 18`, `api: 10`, `import: 4`
* *Defense:* `safety: 6`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` devtype.h, hercules.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `control.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 2356.14 | **LOC:** 7573 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.5%), Complexity Load (formerly Cognitive Load) (75.5%), Connectivity (formerly Api Exposure) (8.8%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stsi_capability` **(Stateful Encapsulated Methods)** (Impact: 16.9)
  * `MIPSreal` **(Compute Cores)** (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 713 instances
* *State Mutation (weighted view):* 2226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1329`, `structural_boundaries: 107`, `args: 326`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 46`, `state_mutation: 800`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` control.c, hercules.h, hstdinc.h, inline.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ctcadpt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2352.82 | **LOC:** 3610 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.7%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CTCE_ExecuteCCW` **(Many-Argument Workhorses)** (Impact: 199.7)
    * *Intent:* // Hercules PC Host A with IP address 192.168.1.100 : // // 0E40 CTCE 30880 192.168.1.200 30880 // 0...
  * `CTCE_Trace` **(Many-Argument Workhorses)** (Impact: 181.0)
    * *Intent:* // --------------------------------------------------------------------- // CTCE_Trace // ----------...
  * `CTCX_ExecuteCCW` **(Many-Argument Workhorses)** (Impact: 170.9)
    * *Intent:* // ------------------------------------------------------------------- // Execute a Channel Command ...
  * `CTCE_Send` **(Many-Argument Workhorses)** (Impact: 125.9)
    * *Intent:* // // CTCE_Send //
  * `CTCE_RecvThread` **(Many-Argument Workhorses)** (Impact: 96.8)
    * *Intent:* // // CTCE_RecvThread //
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 322 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 1090
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 437`, `structural_boundaries: 158`, `args: 129`, `func_start: 25`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 4`, `state_mutation: 446`, `dead_code: 12`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 18`, `api: 14`, `import: 6`
* *Defense:* `safety: 15`, `doc: 7`, `immutability_locks: 25`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ctcadpt.h, devtype.h, hercules.h, hstdinc.h, opcode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hscemode.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2339.12 | **LOC:** 2357 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.1%), Complexity Load (formerly Cognitive Load) (93.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 77.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `icount_cmd` **(Many-Argument Workhorses)** (Impact: 381.9)
    * *Intent:* #endif #if defined(OPTION_INSTRUCTION_COUNTING) /*--------------------------------------------------...
  * `ipending_cmd` **(Many-Argument Workhorses)** (Impact: 209.8)
    * *Intent:* /*-------------------------------------------------------------------*/ /* ipending command - displa...
  * `psw_cmd` **(Many-Argument Workhorses)** (Impact: 209.3)
    * *Intent:* /*-------------------------------------------------------------------*/ /* psw command - display or ...
  * `trace_cmd` **(Many-Argument Workhorses)** (Impact: 84.7)
    * *Intent:* /*-------------------------------------------------------------------*/ /* tracing commands: t, t+, ...
  * `aea_cmd` **(Many-Argument Workhorses)** (Impact: 64.0)
    * *Intent:* /*-------------------------------------------------------------------*/ /* aea - display aea values ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 345 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1059
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 545`, `structural_boundaries: 149`, `args: 245`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 369`, `fragile_debt: 2`
* *Architecture:* `io: 12`, `api: 21`, `import: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` hercules.h, hscemode.c, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `feature.h` -> **Severity: 0.087** (Bridge: 0.0022 * Flux: 39.5395%)
- `opcode.h` -> **Severity: 0.043** (Bridge: 0.0008 * Flux: 51.3182%)
- `inline.h` -> **Severity: 0.02** (Bridge: 0.0002 * Flux: 99.9999%)
- `tapedev.h` -> **Severity: 0.008** (Bridge: 0.0003 * Flux: 22.9785%)
- `hstructs.h` -> **Severity: 0.007** (Bridge: 0.0009 * Flux: 8.7409%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `chain.h` -> **Severity: 14.377** (Embedded: 0.1458 * Error Risk: 98.5783%)
- `hinlines.h` -> **Severity: 13.967** (Embedded: 0.1458 * Error Risk: 95.7634%)
- `extstring.h` -> **Severity: 13.902** (Embedded: 0.1458 * Error Risk: 95.321%)
- `clock.h` -> **Severity: 13.565** (Embedded: 0.1473 * Error Risk: 92.0764%)
- `cpuint.h` -> **Severity: 12.769** (Embedded: 0.1458 * Error Risk: 87.5477%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `machdep.h` -> **Severity: 742.094** (Blast Radius: 9.591 * Doc Risk: 77.374%)
- `inline.h` -> **Severity: 578.68** (Blast Radius: 7.479 * Doc Risk: 77.374%)
- `dbgtrace.h` -> **Severity: 515.775** (Blast Radius: 6.666 * Doc Risk: 77.374%)
- `vstore.h` -> **Severity: 309.496** (Blast Radius: 4.0 * Doc Risk: 77.374%)
- `clock.h` -> **Severity: 247.752** (Blast Radius: 3.202 * Doc Risk: 77.374%)

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
