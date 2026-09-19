# ARCHITECTURAL_BRIEF: xv6-public
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/mit-pdos/xv6-public.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 87 analyzed artifact(s), 8110 LOC.
- **Load-bearing artifact:** `types.h` -- 46 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `console.c` -- pulls in 12 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `usertests.c` at magnitude 1275.1 (structural weight, not risk).
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
| Total Artifacts | 102 |
| Analyzed Artifacts (Scanned) | 87 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 15 |
| Total LOC | 8110 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 85.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.336 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2311 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 68 | 7297 | 78.2% |
| ASSEMBLY | 7 | 203 | 8.0% |
| PERL | 4 | 174 | 4.6% |
| SHELL | 4 | 226 | 4.6% |
| PLAINTEXT | 2 | 0 | 2.3% |
| MAKEFILE | 1 | 210 | 1.1% |
| MARKDOWN | 1 | 0 | 1.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `2.146`
> **Composition Archetype:** `Small Flat Repo (2)` (z +2.15; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 25%, Large Core Modules (3) 17%, Compute Cores Files 13%, Data / Markup / Trivial 9%, Interface Declarations Files 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 84 | 96.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 3.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 15*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.el`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tmpl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ld`: 1x Excluded (Unsupported Extension: '.ld')
- `.list`: 1x Excluded (Unsupported Extension: '.list')
- `.spec`: 1x Excluded (Unsupported Extension: '.spec')
- `.p`: 1x Excluded (Unsupported Extension: '.p')
- `.ftr`: 1x Excluded (Unsupported Extension: '.ftr')
- `.hdr`: 1x Excluded (Unsupported Extension: '.hdr')
- `.pl`: 1x Excluded (Machine-Generated Source Code Signature: 48 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.5 | 32.2 | 22.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 63.4 | 85.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 40.9 | 38.1 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.4 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.4 | 4.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 57.1 | 91.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 1.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 67.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1593 | 54 | 38 | `fs.c` |
| cleanup | 84 | 16 | 1 | `usertests.c` |
| guards | 165 | 30 | 6 | `x86.h` |
| danger | 794 | 50 | 10 | `usertests.c` |
| concurrency | 23 | 13 | 1 | `proc.c` |
| connectivity | 552 | 70 | 15 | `defs.h` |
| io | 295 | 24 | 4 | `usertests.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 91 | 15 | 2 | `usertests.c` |
| time | 2 | 2 | 0 | `cuth` |
| serialization | 3 | 1 | 0 | `Makefile` |
| regex | 42 | 6 | 0 | `runoff` |
| events | 1 | 1 | 0 | `trapasm.S` |
| tests | 0 | 0 | 0 | - |
| docs | 2 | 1 | 0 | `fs.c` |
| debt | 384 | 26 | 4 | `usertests.c` |
| mutation | 1715 | 51 | 42 | `usertests.c` |
| dead_code | 172 | 53 | 5 | `sysfile.c` |
| credential | 0 | 0 | 0 | - |
| threat | 69 | 18 | 2 | `exec.c` |
| ml_ai | 77 | 7 | 0 | `log.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `usertests.c` (Hits: 92)
- `runoff` (Hits: 74)
- `Makefile` (Hits: 45)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **types.h** (`types.h`) — 46 inbound connections
2. **param.h** (`param.h`) — 25 inbound connections
3. **defs.h** (`defs.h`) — 24 inbound connections
4. **stat.h** (`stat.h`) — 20 inbound connections
5. **x86.h** (`x86.h`) — 20 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **console.c** (`console.c`) — 12 outbound dependencies
2. **ide.c** (`ide.c`) — 12 outbound dependencies
3. **fs.c** (`fs.c`) — 11 outbound dependencies
4. **memide.c** (`memide.c`) — 11 outbound dependencies
5. **sysfile.c** (`sysfile.c`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__global_context__` **(Many-Argument Workhorses)** (@ `runoff`) -> Impact: **114.4** | LOC: 195
- `gettoken` **(Many-Argument Workhorses)** (@ `sh.c`) -> Impact: **49.2** | LOC: 44
- `subdir` **(I/O & Config Routines)** (@ `usertests.c`) -> Impact: **48.1** | LOC: 182
- `exec` **(Many-Argument Workhorses)** (@ `exec.c`) -> Impact: **43.4** | LOC: 105
  * *Intent:* #include "types.h" #include "param.h" #include "memlayout.h" #include "mmu.h" #include "proc.h" #include "defs.h" #include "x86.h" #include "elf.h"
- `printf` **(Many-Argument Workhorses)** (@ `printf.c`) -> Impact: **42.4** | LOC: 47
  * *Intent:* // Print to the given fd. Only understands %d, %x, %p, %s.
- `trap` **(Compute Cores)** (@ `trap.c`) -> Impact: **39.2** | LOC: 77
  * *Intent:* //PAGEBREAK: 41
- `sbrktest` **(I/O & Config Routines)** (@ `usertests.c`) -> Impact: **32.7** | LOC: 134
- `concreate` **(I/O & Config Routines)** (@ `usertests.c`) -> Impact: **32.5** | LOC: 90
  * *Intent:* // test concurrent create/link/unlink of the same file
- `cprintf` **(Compute Cores)** (@ `console.c`) -> Impact: **30.3** | LOC: 51
  * *Intent:* //PAGEBREAK: 50 // Print to the console. only understands %d, %x, %p, %s.
- `consoleintr` **(Compute Cores)** (@ `console.c`) -> Impact: **27.6** | LOC: 43
  * *Intent:* #define C(x) ((x)-'@') // Control-x

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 87 | 7277.3 | 31.07% | 39.47% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `sysproc.c` -> **99.9804%** Exposure
- `bootasm.S` -> **99.9188%** Exposure
- `ulib.c` -> **99.8932%** Exposure
- `sleeplock.c` -> **99.8499%** Exposure
- `memide.c` -> **98.9013%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bio.c` -> **100.0%** Exposure
- `bootmain.c` -> **100.0%** Exposure
- `console.c` -> **100.0%** Exposure
- `exec.c` -> **100.0%** Exposure
- `fs.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sysfile.c` -> **13** Orphaned Functions | **0** Duplicates
- `proc.c` -> **11** Orphaned Functions | **0** Duplicates
- `vm.c` -> **9** Orphaned Functions | **0** Duplicates
- `sysproc.c` -> **8** Orphaned Functions | **0** Duplicates
- `ulib.c` -> **8** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `289` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `usertests.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1275.1 | **LOC:** 1804 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `subdir` **(I/O & Config Routines)** (Impact: 48.1)
  * `sbrktest` **(I/O & Config Routines)** (Impact: 32.7)
  * `concreate` **(I/O & Config Routines)** (Impact: 32.5)
    * *Intent:* // test concurrent create/link/unlink of the same file
  * `createdelete` **(I/O & Config Routines)** (Impact: 25.6)
    * *Intent:* // four processes create and delete different files in same directory
  * `sharedfd` **(I/O & Config Routines)** (Impact: 19.5)
    * *Intent:* // More file system tests // two processes write to the same file descriptor // is the offset shared...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 252 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 761
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 318`, `structural_boundaries: 88`, `args: 35`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 206`, `state_mutation: 257`, `dead_code: 6`, `unreferenced_by_name: 4`
* *Architecture:* `io: 92`, `api: 39`, `import: 9`
* *Defense:* `cleanup: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` fcntl.h, fs.h, memlayout.h, param.h, stat.h, syscall.h, traps.h, types.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 519.36 | **LOC:** 671 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.5%)
- **Documentation Coverage:** 97.619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writei` **(Many-Argument Workhorses)** (Impact: 26.1)
    * *Intent:* // PAGEBREAK! // Write data to inode. // Caller must hold ip->lock.
  * `readi` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* //PAGEBREAK! // Read data from inode. // Caller must hold ip->lock.
  * `namex` **(C Struct Operations)** (Impact: 19.7)
    * *Intent:* // Look up and return the inode for a path name. // If parent != 0, return the inode for the parent ...
  * `iget` **(C Struct Operations)** (Impact: 15.5)
    * *Intent:* // Find the inode with number inum on device dev // and return the in-memory copy. Does not lock // ...
  * `dirlookup` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* // Look for a directory entry in a directory. // If found, set *poff to byte offset of entry.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 89 instances
* *State Mutation (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 94`, `args: 28`, `func_start: 25`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 106`, `fragile_debt: 2`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 17`, `import: 11`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` buf.h, defs.h, file.h, fs.h, mmu.h, param.h, proc.h, sleeplock.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sh.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 409.26 | **LOC:** 494 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gettoken` **(Many-Argument Workhorses)** (Impact: 49.2)
  * `runcmd` **(Compute Cores)** (Impact: 26.4)
    * *Intent:* // Execute cmd. Never returns.
  * `parseredirs` **(Compute Cores)** (Impact: 17.2)
  * `nulterminate` **(Compute Cores)** (Impact: 15.0)
    * *Intent:* // NUL-terminate all the counted strings.
  * `parseexec` **(Compute Cores)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 122`, `args: 26`, `func_start: 19`, `class_start: 50`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 7`, `state_mutation: 77`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 32`, `import: 3`
* *Defense:* `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` fcntl.h, types.h, user.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `proc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 383.26 | **LOC:** 535 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `procdump` **(Stateful Encapsulated Methods)** (Impact: 14.6)
    * *Intent:* //PAGEBREAK: 36 // Print a process listing to console. For debugging. // Runs when user types ^P on ...
  * `sleep` **(Compute Cores)** (Impact: 10.5)
    * *Intent:* // Atomically release lock and sleep on chan. // Reacquires lock when awakened.
  * `growproc` **(Compute Cores)** (Impact: 9.4)
    * *Intent:* // Grow current process's memory by n bytes. // Return 0 on success, -1 on failure.
  * `exit` **(I/O & Config Routines)** (Impact: 9.1)
    * *Intent:* // Exit the current process. Does not return. // An exited process remains in the zombie state // un...
  * `wait` **(I/O & Config Routines)** (Impact: 9.1)
    * *Intent:* // Wait for a child process to exit and return its pid. // Return -1 if this process has no children...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 80`, `args: 23`, `func_start: 19`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 94`, `dead_code: 1`, `unreferenced_by_name: 11`
* *Architecture:* `api: 20`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` defs.h, memlayout.h, mmu.h, param.h, proc.h, spinlock.h, types.h, x86.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 307.56 | **LOC:** 395 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.6%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (70.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loaduvm` **(Many-Argument Workhorses)** (Impact: 18.2)
    * *Intent:* // Load a program segment into pgdir. addr must be page-aligned // and the pages from addr to addr+s...
  * `deallocuvm` **(Many-Argument Workhorses)** (Impact: 15.2)
    * *Intent:* // Deallocate user pages to bring the process size from oldsz to // newsz. oldsz and newsz need not ...
  * `copyuvm` **(Type Conversions)** (Impact: 13.7)
    * *Intent:* // Given a parent process's page table, create a copy // of it for a child.
  * `allocuvm` **(Many-Argument Workhorses)** (Impact: 13.4)
    * *Intent:* // Allocate page tables and physical memory to grow process from oldsz to // newsz, which need not b...
  * `mappages` **(Stateful Encapsulated Methods)** (Impact: 13.3)
    * *Intent:* // Create PTEs for virtual addresses starting at va that refer to // physical addresses starting at ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 52`, `args: 30`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 56`, `dead_code: 3`, `unreferenced_by_name: 9`
* *Architecture:* `api: 15`, `import: 8`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` defs.h, elf.h, memlayout.h, mmu.h, param.h, proc.h, types.h, x86.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sysfile.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 293.64 | **LOC:** 445 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.3%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (76.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(Many-Argument Workhorses)** (Impact: 24.5)
  * `sys_open` **(I/O & Config Routines)** (Impact: 15.4)
  * `argfd` **(C Struct Operations)** (Impact: 14.8)
    * *Intent:* #include "types.h" #include "defs.h" #include "param.h" #include "stat.h" #include "mmu.h" #include ...
  * `sys_unlink` **(I/O & Config Routines)** (Impact: 13.8)
    * *Intent:* //PAGEBREAK!
  * `sys_link` **(I/O & Config Routines)** (Impact: 10.4)
    * *Intent:* // Create the path new as a link to the same inode as old.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 93`, `args: 17`, `func_start: 17`, `class_start: 20`
* *Risk/State:* `state_mutation: 45`, `dead_code: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 13`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` defs.h, fcntl.h, file.h, fs.h, mmu.h, param.h, proc.h, sleeplock.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `console.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 281.56 | **LOC:** 300 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cprintf` **(Compute Cores)** (Impact: 30.3)
    * *Intent:* //PAGEBREAK: 50 // Print to the console. only understands %d, %x, %p, %s.
  * `consoleintr` **(Compute Cores)** (Impact: 27.6)
    * *Intent:* #define C(x) ((x)-'@') // Control-x
  * `printint` **(Stateful Encapsulated Methods)** (Impact: 17.2)
  * `consoleread` **(Many-Argument Workhorses)** (Impact: 15.8)
  * `cgaputc` **(Stateful Encapsulated Methods)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 32`, `args: 21`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 51`, `unreferenced_by_name: 2`
* *Architecture:* `api: 7`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` defs.h, file.h, fs.h, memlayout.h, mmu.h, param.h, proc.h, sleeplock.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mkfs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 202.78 | **LOC:** 298 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `iappend` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* #define min(a, b) ((a) < (b) ? (a) : (b))
  * `wsect` **(Compute Cores)** (Impact: 5.8)
  * `rsect` **(Compute Cores)** (Impact: 5.8)
  * `balloc` **(Defensive Guards)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 30 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 36`, `args: 19`, `func_start: 10`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 8`, `state_mutation: 60`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 17`, `import: 10`
* *Defense:* `safety: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` assert.h, fcntl.h, fs.h, param.h, stat.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runoff` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 175.16 | **LOC:** 247 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (100.0%), Mutation Surface (formerly State Flux) (98.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__global_context__` **(Many-Argument Workhorses)** (Impact: 114.4)
  * `Anonymous_Block` **(Compute Cores)** (Impact: 5.8)
    * *Intent:* # make reference list
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 3.5)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 3.4)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 72`, `args: 32`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 97`, `state_mutation: 11`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 74`
* *Defense:* `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `string.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 174.14 | **LOC:** 106 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `memmove` **(Compute Cores)** (Impact: 12.9)
  * `strncmp` **(Compute Cores)** (Impact: 10.4)
  * `safestrcpy` **(Compute Cores)** (Impact: 8.7)
    * *Intent:* // Like strncpy but guaranteed to NUL-terminate.
  * `strncpy` **(Defensive Guards)** (Impact: 8.6)
  * `memset` **(Type Conversions)** (Impact: 8.5)
    * *Intent:* #include "types.h" #include "x86.h"
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 21`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 32`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `safety: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` types.h, x86.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runoff1` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 157.78 | **LOC:** 109 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 7.93; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Complexity Load (formerly Cognitive Load) (85.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `io: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` the
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `defs.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 144.78 | **LOC:** 191 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); blast radius 29.4; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (68.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 191`, `args: 114`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`
* *Architecture:* `api: 127`
* *Defense:* `safety: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.27907
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `mp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 136.8 | **LOC:** 140 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Complexity Load (formerly Cognitive Load) (72.0%), Debt Markers (formerly Tech Debt) (24.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mpinit` **(Compute Cores)** (Impact: 15.4)
  * `mpconfig` **(C Struct Operations)** (Impact: 10.8)
    * *Intent:* // Search for an MP configuration table. For now, // don't accept the default configurations (physad...
  * `mpsearch1` **(Stateful Encapsulated Methods)** (Impact: 7.5)
    * *Intent:* // Look for an MP structure in the len bytes at addr.
  * `mpsearch` **(C Struct Operations)** (Impact: 5.9)
    * *Intent:* // Search for the MP Floating Pointer Structure, which according to the // spec is in one of the fol...
  * `sum` **(Stateful Encapsulated Methods)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 38`, `args: 5`, `func_start: 5`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 30`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` defs.h, memlayout.h, mmu.h, mp.h, param.h, proc.h, types.h, x86.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exec.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 136.28 | **LOC:** 115 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Complexity Load (formerly Cognitive Load) (97.5%), Debt Markers (formerly Tech Debt) (28.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exec` **(Many-Argument Workhorses)** (Impact: 43.4)
    * *Intent:* #include "types.h" #include "param.h" #include "memlayout.h" #include "mmu.h" #include "proc.h" #inc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 8`, `args: 1`, `func_start: 1`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 30`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` defs.h, elf.h, memlayout.h, mmu.h, param.h, proc.h, types.h, x86.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `printf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 135.12 | **LOC:** 86 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printf` **(Many-Argument Workhorses)** (Impact: 42.4)
    * *Intent:* // Print to the given fd. Only understands %d, %x, %p, %s.
  * `printint` **(Stateful Encapsulated Methods)** (Impact: 19.2)
  * `putc` **(Encapsulated Accessors)** (Impact: 2.0)
    * *Intent:* #include "types.h" #include "stat.h" #include "user.h"
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 4`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 23`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` stat.h, types.h, user.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `log.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 124.48 | **LOC:** 235 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.5%), Complexity Load (formerly Cognitive Load) (62.5%), Debt Markers (formerly Tech Debt) (56.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `log_write` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* // Caller has modified b->data and is done with the buffer. // Record the block number and pin in th...
  * `begin_op` **(Compute Cores)** (Impact: 6.8)
    * *Intent:* // called at the start of each FS system call.
  * `end_op` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* // called at the end of each FS system call. // commits if this was the last outstanding operation.
  * `initlog` **(Compute Cores)** (Impact: 3.5)
  * `install_trans` **(C Struct Operations)** (Impact: 2.7)
    * *Intent:* // Copy committed blocks from log to their home location
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 40`, `args: 10`, `func_start: 10`, `class_start: 14`
* *Risk/State:* `state_mutation: 27`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` buf.h, defs.h, fs.h, param.h, sleeplock.h, spinlock.h, types.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `umalloc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 120.44 | **LOC:** 91 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Complexity Load (formerly Cognitive Load) (71.8%), Debt Markers (formerly Tech Debt) (36.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `free` **(Compute Cores)** (Impact: 15.2)
  * `malloc` **(Compute Cores)** (Impact: 12.7)
  * `morecore` **(Stateful Encapsulated Methods)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 27 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 16`, `args: 4`, `func_start: 3`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` param.h, stat.h, types.h, user.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ulib.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 120.42 | **LOC:** 107 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Guard Balance (formerly Safety Score) (98.6%), Complexity Load (formerly Cognitive Load) (64.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gets` **(Compute Cores)** (Impact: 9.5)
  * `strchr` **(Type Conversions)** (Impact: 5.6)
  * `strcmp` **(Compute Cores)** (Impact: 5.5)
  * `atoi` **(Compute Cores)** (Impact: 4.7)
  * `memmove` **(Parameter Forwarders)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 19`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 22`, `unreferenced_by_name: 8`
* *Architecture:* `io: 3`, `api: 9`, `import: 5`
* *Defense:* `immutability_locks: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` fcntl.h, stat.h, types.h, user.h, x86.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `grep.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 118.56 | **LOC:** 108 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `matchhere` **(Compute Cores)** (Impact: 14.5)
    * *Intent:* // matchhere: search for re at beginning of text
  * `matchstar` **(Compute Cores)** (Impact: 12.4)
    * *Intent:* // matchstar: search for c*re at beginning of text
  * `grep` **(Compute Cores)** (Impact: 11.7)
  * `main` **(Compute Cores)** (Impact: 10.0)
  * `match` **(Compute Cores)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 11`, `args: 8`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 17`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 8`, `import: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` stat.h, types.h, user.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pipe.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 110.48 | **LOC:** 122 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.2%), Debt Markers (formerly Tech Debt) (83.6%), Complexity Load (formerly Cognitive Load) (75.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pipealloc` **(Compute Cores)** (Impact: 13.9)
  * `piperead` **(Compute Cores)** (Impact: 13.1)
  * `pipeclose` **(Type Conversions)** (Impact: 11.2)
  * `pipewrite` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* //PAGEBREAK: 40
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 17`, `args: 4`, `func_start: 4`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `unreferenced_by_name: 4`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` defs.h, file.h, fs.h, mmu.h, param.h, proc.h, sleeplock.h, spinlock.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 109.08 | **LOC:** 145 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Debt Markers (formerly Tech Debt) (92.8%), Complexity Load (formerly Cognitive Load) (62.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bget` **(C Struct Operations)** (Impact: 13.8)
    * *Intent:* // Look through buffer cache for block on device dev. // If not found, allocate a buffer. // In eith...
  * `brelse` **(Compute Cores)** (Impact: 5.3)
    * *Intent:* // Release a locked buffer. // Move to the head of the MRU list.
  * `bread` **(Compute Cores)** (Impact: 4.0)
    * *Intent:* // Return a locked buf with the contents of the indicated block.
  * `bwrite` **(Parameter Forwarders)** (Impact: 3.2)
    * *Intent:* // Write b's contents to disk. Must be locked.
  * `binit` **(I/O & Config Routines)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 18`, `args: 5`, `func_start: 5`, `class_start: 8`
* *Risk/State:* `state_mutation: 26`, `unreferenced_by_name: 4`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` buf.h, defs.h, fs.h, param.h, sleeplock.h, spinlock.h, types.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `file.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 106.38 | **LOC:** 158 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.2%), Guard Balance (formerly Safety Score) (87.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filewrite` **(Many-Argument Workhorses)** (Impact: 22.0)
    * *Intent:* //PAGEBREAK! // Write to file f.
  * `fileread` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* // Read from file f.
  * `fileclose` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* // Close file f. (Decrement ref count, close when reaches 0.)
  * `filestat` **(Parameter Forwarders)** (Impact: 4.0)
    * *Intent:* // Get metadata about file f.
  * `filealloc` **(Interface Declarations)** (Impact: 3.8)
    * *Intent:* // Allocate a file structure.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 31`, `args: 7`, `func_start: 7`, `class_start: 8`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 7`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` defs.h, file.h, fs.h, param.h, sleeplock.h, spinlock.h, types.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `syscall.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 92.1 | **LOC:** 146 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (85.5%), Debt Markers (formerly Tech Debt) (41.9%), Complexity Load (formerly Cognitive Load) (34.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `argptr` **(Type Conversions)** (Impact: 10.7)
    * *Intent:* // Fetch the nth word-sized system call argument as a pointer // to a block of memory of size bytes....
  * `fetchstr` **(Type Conversions)** (Impact: 7.7)
    * *Intent:* // Fetch the nul-terminated string at addr from the current process. // Doesn't actually copy the st...
  * `syscall` **(Compute Cores)** (Impact: 5.8)
  * `fetchint` **(Compute Cores)** (Impact: 5.7)
    * *Intent:* #include "param.h" #include "memlayout.h" #include "mmu.h" #include "proc.h" #include "x86.h" #inclu...
  * `argstr` **(Parameter Forwarders)** (Impact: 3.9)
    * *Intent:* // Fetch the nth word-sized system call argument as a string pointer. // Check that the pointer is v...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 39`, `args: 27`, `func_start: 6`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`, `unreferenced_by_name: 2`
* *Architecture:* `api: 27`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` defs.h, memlayout.h, mmu.h, param.h, proc.h, syscall.h, types.h, x86.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 85.06 | **LOC:** 169 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.1%), Debt Markers (formerly Tech Debt) (61.4%), Complexity Load (formerly Cognitive Load) (56.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iderw` **(Compute Cores)** (Impact: 14.3)
    * *Intent:* //PAGEBREAK! // Sync buf with disk. // If B_DIRTY is set, write buf to disk, clear B_DIRTY, set B_VA...
  * `idestart` **(Stateful Encapsulated Methods)** (Impact: 12.7)
    * *Intent:* // Start the request for b. Caller must hold idelock.
  * `ideintr` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* // Interrupt handler.
  * `idewait` **(Stateful Encapsulated Methods)** (Impact: 6.2)
    * *Intent:* // Wait for IDE disk to become ready.
  * `ideinit` **(I/O & Config Routines)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 18`, `args: 7`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` buf.h, defs.h, fs.h, memlayout.h, mmu.h, param.h, proc.h, sleeplock.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spinlock.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 84.44 | **LOC:** 127 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 7.93; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.2%), Debt Markers (formerly Tech Debt) (85.4%), Complexity Load (formerly Cognitive Load) (66.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getcallerpcs` **(Compute Cores)** (Impact: 11.2)
    * *Intent:* // Record the current call stack in pcs[] by following the %ebp chain.
  * `popcli` **(Compute Cores)** (Impact: 5.5)
  * `acquire` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* // Acquire the lock. // Loops (spins) until the lock is acquired. // Holding a lock for a long time ...
  * `release` **(Compute Cores)** (Impact: 4.0)
    * *Intent:* // Release the lock.
  * `holding` **(Parameter Forwarders)** (Impact: 3.3)
    * *Intent:* // Check whether this cpu is holding the lock.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 15`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 16`, `unreferenced_by_name: 3`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` defs.h, memlayout.h, mmu.h, param.h, proc.h, spinlock.h, types.h, x86.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `defs.h` -> **Severity: 19.21** (Embedded: 0.2791 * Error Risk: 68.8358%)
- `user.h` -> **Severity: 18.895** (Embedded: 0.2093 * Error Risk: 90.2786%)
- `x86.h` -> **Severity: 13.719** (Embedded: 0.2326 * Error Risk: 58.992%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `x86.h` -> **Severity: 2981.7** (Blast Radius: 29.817 * Doc Risk: 100.0%)
- `Makefile` -> **Severity: 793.0** (Blast Radius: 7.93 * Doc Risk: 100.0%)
- `bio.c` -> **Severity: 793.0** (Blast Radius: 7.93 * Doc Risk: 100.0%)
- `bootmain.c` -> **Severity: 793.0** (Blast Radius: 7.93 * Doc Risk: 100.0%)
- `cat.c` -> **Severity: 793.0** (Blast Radius: 7.93 * Doc Risk: 100.0%)

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
