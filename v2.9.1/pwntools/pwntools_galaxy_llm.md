# ARCHITECTURAL_BRIEF: pwntools
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Gallopsled/pwntools.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 710 analyzed artifact(s), 111059 LOC.
- **Load-bearing artifact:** `pwnlib/constants/constant.py` -- 32 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pwn/toplevel.py` -- pulls in 67 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pwnlib/constants/linux/amd64.py` at magnitude 1902.02 (structural weight, not risk).
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
| Total Artifacts | 1443 |
| Analyzed Artifacts (Scanned) | 710 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 733 |
| Total LOC | 111059 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 49.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6266 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2393 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5794 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 36 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 326 | 9950 | 45.9% |
| PYTHON | 216 | 46083 | 30.4% |
| C | 126 | 54398 | 17.7% |
| MARKDOWN | 12 | 0 | 1.7% |
| SHELL | 11 | 319 | 1.5% |
| PLAINTEXT | 7 | 0 | 1.0% |
| MAKEFILE | 6 | 111 | 0.8% |
| DOCKERFILE | 6 | 198 | 0.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `3.519`
> **Composition Archetype:** `Hub-Coupled App` (z +3.52; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 32%, Data / Markup / Trivial 16%, Large Core Modules 15%, Parameter Forwarders Files 14%, State Mutators Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 691 | 97.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 19 | 2.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 733*

**Composition by Extension & Reason:**
- `.asm`: 217x Excluded (Machine-Generated Source Code Signature: 102 LOC), 95x Excluded (Machine-Generated Source Code Signature: 103 LOC), 85x Excluded (Machine-Generated Source Code Signature: 104 LOC)
- `no_extension`: 55x Excluded (Binary Format Detected), 35x Unsupported Format (.undeterminable), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 80x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 11x Statistical Anomaly (Z-Score: -5.94 < -4.60), 2x Excluded (Lexical Monotony: High structural repetition detected in 3375 LOC), 1x Excluded (Machine-Generated Source Code Signature: 452 LOC)
- `.py`: 2x Excluded (Lexical Monotony: High structural repetition detected in 3376 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2011 LOC)
- `.yml`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 22374 LOC)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.native`: 2x Excluded (Unsupported Extension: '.native')
- `.native32`: 2x Excluded (Unsupported Extension: '.native32')
- `.cfg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.aarch64`: 1x Excluded (Unsupported Extension: '.aarch64')
- `.arm`: 1x Excluded (Binary Format Detected)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.9 | 11.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 33.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 33.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.1 | 0.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.5 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 66.3 | 3.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 49.7 | 48.5 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1647 | 222 | 7 | `pwnlib/data/includes/generator/linux/diet/unistd.h` |
| cleanup | 77 | 30 | 0 | `pwnlib/tubes/process.py` |
| guards | 7246 | 161 | 7 | `pwnlib/constants/linux/alpha.py` |
| danger | 1000 | 177 | 4 | `pwnlib/tubes/process.py` |
| concurrency | 123 | 51 | 0 | `pwnlib/util/iters.py` |
| connectivity | 2319 | 187 | 6 | `pwnlib/data/includes/generator/linux/diet/unistd.h` |
| io | 1472 | 229 | 6 | `pwnlib/tubes/process.py` |
| crypto | 4 | 4 | 0 | `pwnlib/commandline/libcdb.py` |
| ipc | 206 | 56 | 0 | `pwnlib/data/includes/generator/freebsd/sys/socket.h` |
| time | 106 | 19 | 0 | `pwnlib/data/includes/generator/linux/diet/sys/stat.h` |
| serialization | 1 | 1 | 0 | `pwnlib/util/iters.py` |
| regex | 66 | 28 | 0 | `pwnlib/rop/rop.py` |
| events | 157 | 42 | 0 | `pwnlib/protocols/adb/__init__.py` |
| tests | 11 | 7 | 0 | `pwnlib/commandline/elfpatch.py` |
| docs | 966 | 107 | 2 | `pwnlib/elf/elf.py` |
| debt | 236 | 98 | 1 | `pwnlib/tubes/ssh.py` |
| mutation | 59382 | 516 | 46 | `pwnlib/constants/linux/amd64.py` |
| dead_code | 608 | 301 | 2 | `pwnlib/data/includes/generator/linux/diet/fcntl.h` |
| credential | 0 | 0 | 0 | - |
| threat | 541 | 111 | 2 | `pwnlib/data/includes/generator/linux/diet/sys/cdefs.h` |
| ml_ai | 2 | 1 | 0 | `pwnlib/util/misc.py` |
| ui | 4 | 4 | 0 | `pwnlib/commandline/template.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pwnlib/tubes/process.py` (Hits: 62)
- `pwnlib/tubes/ssh.py` (Hits: 57)
- `pwnlib/util/misc.py` (Hits: 39)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **constant.py** (`pwnlib/constants/constant.py`) — 32 inbound connections
2. **packing.py** (`pwnlib/util/packing.py`) — 19 inbound connections
3. **string.h** (`pwnlib/data/includes/generator/linux/diet/string.h`) — 18 inbound connections
4. **args.py** (`pwnlib/args.py`) — 17 inbound connections
5. **fiddling.py** (`pwnlib/util/fiddling.py`) — 16 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **toplevel.py** (`pwn/toplevel.py`) — 67 outbound dependencies
2. **elf.py** (`pwnlib/elf/elf.py`) — 35 outbound dependencies
3. **process.py** (`pwnlib/tubes/process.py`) — 32 outbound dependencies
4. **ssh.py** (`pwnlib/tubes/ssh.py`) — 30 outbound dependencies
5. **__init__.py** (`pwnlib/context/__init__.py`) — 27 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Many-Argument Workhorses)** (@ `pwnlib/tubes/process.py`) -> Impact: **234.9** | LOC: 190
- `attach` **(Many-Argument Workhorses)** (@ `pwnlib/gdb.py`) -> Impact: **224.9** | LOC: 426
- `debug` **(Many-Argument Workhorses)** (@ `pwnlib/gdb.py`) -> Impact: **173.1** | LOC: 320
- `run_in_new_terminal` **(Many-Argument Workhorses)** (@ `pwnlib/util/misc.py`) -> Impact: **161.8** | LOC: 198
  * *Intent:* """run_in_new_terminal(command, terminal=None, args=None, kill_at_exit=True, preexec_fn=None) -> int Run a command in a new terminal. When ``terminal`...
- `regsort` **(Many-Argument Workhorses)** (@ `pwnlib/regsort.py`) -> Impact: **156.6** | LOC: 327
  * *Intent:* """ Sorts register dependencies. Given a dictionary of registers to desired register contents, return the optimal order in which to set the registers ...
- `process` **(Many-Argument Workhorses)** (@ `pwnlib/tubes/ssh.py`) -> Impact: **138.9** | LOC: 250
- `dd` **(Many-Argument Workhorses)** (@ `pwnlib/util/packing.py`) -> Impact: **138.8** | LOC: 184
- `ret2csu` **(Many-Argument Workhorses)** (@ `pwnlib/rop/ret2csu.py`) -> Impact: **127.3** | LOC: 94
  * *Intent:* """Build a ret2csu ROPchain Arguments: edi, rsi, rdx: Three primary registers to populate rbx, rbp, r12, r13, r14, r15: Optional registers to populate...
- `__init__` **(Many-Argument Workhorses)** (@ `pwnlib/tubes/ssh.py`) -> Impact: **121.7** | LOC: 168
- `hexdump_iter` **(Many-Argument Workhorses)** (@ `pwnlib/util/fiddling.py`) -> Impact: **120.9** | LOC: 163

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pwnlib/constants/linux` | 15 | 22476.18 | 0.0% | 0.0% |
| `pwnlib` | 29 | 6314.82 | 33.87% | 20.75% |
| `pwnlib/tubes` | 10 | 4675.62 | 48.7% | 11.81% |
| `pwnlib/util` | 14 | 4530.8 | 44.31% | 10.7% |
| `pwnlib/elf` | 7 | 3316.96 | 38.85% | 8.85% |
| `pwnlib/term` | 12 | 2791.62 | 62.34% | 38.09% |
| `pwnlib/rop` | 7 | 1973.44 | 50.04% | 21.33% |
| `pwnlib/commandline` | 23 | 1483.38 | 54.18% | 0.0% |
| `pwnlib/constants` | 4 | 1199.6 | 9.93% | 24.9% |
| `pwnlib/adb` | 5 | 1105.64 | 25.15% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pwnlib/shellcraft/templates/amd64/push.asm` -> **100.0%** Exposure
- `pwnlib/shellcraft/templates/thumb/push.asm` -> **99.9999%** Exposure
- `pwnlib/gdb_api_bridge.py` -> **99.9988%** Exposure
- `pwnlib/shellcraft/templates/loongarch64/mov.asm` -> **99.9962%** Exposure
- `pwnlib/timeout.py` -> **99.9896%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pwnlib/abi.py` -> **100.0%** Exposure
- `pwnlib/adb/adb.py` -> **100.0%** Exposure
- `pwnlib/adb/bootloader.py` -> **100.0%** Exposure
- `pwnlib/args.py` -> **100.0%** Exposure
- `pwnlib/asm.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `examples/fmtstr/Makefile` -> **11** Orphaned Functions | **0** Duplicates
- `pwnlib/encoders/arm/alphanumeric/ARM_Instructions.py` -> **9** Orphaned Functions | **0** Duplicates
- `pwnlib/gdb_api_bridge.py` -> **6** Orphaned Functions | **2** Duplicates
- `pwnlib/rop/ret2dlresolve.py` -> **0** Orphaned Functions | **8** Duplicates
- `pwnlib/shellcraft/registers.py` -> **8** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `68` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1216` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pwnlib/constants/linux/amd64.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1902.02 | **LOC:** 1852 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1850`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/constants/linux/alpha.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1775.54 | **LOC:** 1728 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1726`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/constants/linux/s390.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1775.54 | **LOC:** 1728 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1726`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/constants/linux/sparc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1770.44 | **LOC:** 1723 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1721`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/constants/linux/i386.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1769.42 | **LOC:** 1722 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1720`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/tubes/ssh.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1763.4 | **LOC:** 2242 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **30**; blast radius 1.283; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.1%)
- **Documentation Coverage:** 47.3373% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process` **(Many-Argument Workhorses)** (Impact: 138.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 121.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 95.8)
  * `interactive` **(Defensive Guards)** (Impact: 31.7)
    * *Intent:* """interactive(prompt = pwnlib.term.text.bold_red('$') + ' ') If not in TTY-mode, this does exactly ...
  * `libs` **(Many-Argument Workhorses)** (Impact: 29.8)
    * *Intent:* """Downloads the libraries referred to by a file. This is done by running ldd on the remote server, ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 214 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 753
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 310`, `args: 88`, `func_start: 87`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 2`, `state_mutation: 325`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 3`
* *Architecture:* `io: 57`, `api: 75`, `concurrency: 2`, `import: 34`
* *Defense:* `safety: 61`, `doc: 52`, `sync_locks: 1`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.283
  * `Choke Point (Betweenness):` 8e-05 | `Ripple Effect (Closeness):` 0.009078
  * `Imports (Out-Degree: 8):` ctypes, io, logging, os, paramiko, paramiko.ssh_exception, platform, pwn...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pwnlib/elf/elf.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1713.62 | **LOC:** 2601 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 71.4%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **35**; blast radius 4.366; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.3%)
- **Documentation Coverage:** 23.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checksec` **(Many-Argument Workhorses)** (Impact: 69.4)
    * *Intent:* """checksec(banner=True, color=True) Prints out information in the binary, similar to ``checksec.sh`...
  * `search` **(Many-Argument Workhorses)** (Impact: 68.4)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 43.9)
    * *Intent:* # elftools uses the backing file for all reads and writes # in order to permit writing without being...
  * `libc_start_main_return` **(Compute Cores)** (Impact: 34.7)
    * *Intent:* """:class:`int`: Address of the return address into __libc_start_main from main. >>> bash = ELF(whic...
  * `nx` **(I/O & Config Routines)** (Impact: 29.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 258 instances
* *State Mutation (weighted view):* 819
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 359`, `args: 110`, `func_start: 108`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 303`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 12`, `api: 95`, `import: 42`
* *Defense:* `safety: 27`, `doc: 92`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.366
  * `Choke Point (Betweenness):` 0.000515 | `Ripple Effect (Closeness):` 0.018493
  * `Imports (Out-Degree: 12):` collections, elftools.elf.constants, elftools.elf.descriptions, elftools.elf.dynamic, elftools.elf.elffile, elftools.elf.enums, elftools.elf.gnuversions, elftools.elf.relocation...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `pwnlib/constants/linux/mips.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1687.82 | **LOC:** 1642 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1640`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/constants/linux/powerpc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1605.2 | **LOC:** 1561 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1559`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/constants/linux/powerpc64.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1552.16 | **LOC:** 1509 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1507`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/constants/linux/ia64.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1529.72 | **LOC:** 1487 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1485`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/constants/linux/sparc64.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1475.66 | **LOC:** 1434 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1432`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/constants/linux/aarch64.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1458.32 | **LOC:** 1417 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1415`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/constants/linux/s390x.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1454.24 | **LOC:** 1413 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1411`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/constants/linux/loongarch64.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1363.46 | **LOC:** 1324 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1322`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/constants/linux/riscv64.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1346.12 | **LOC:** 1307 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1305`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/tubes/process.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1109.36 | **LOC:** 1600 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 16.7%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **32**; blast radius 4.43; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.1%)
- **Documentation Coverage:** 43.2099% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 234.9)
  * `_validate` **(Many-Argument Workhorses)** (Impact: 59.9)
    * *Intent:* """ Perform extended validation on the executable path, argv, and envp. Mostly to make Python happy,...
  * `libc_mapping` **(Compute Cores)** (Impact: 20.0)
  * `corefile` **(Stateful Encapsulated Methods)** (Impact: 19.3)
    * *Intent:* """corefile() -> pwnlib.elf.elf.Core Returns a corefile for the process. If the process is alive, at...
  * `can_recv_raw` **(Defensive Guards)** (Impact: 18.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 140 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 437
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 188`, `args: 42`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 1`, `state_mutation: 157`, `dead_code: 3`, `fragile_debt: 5`
* *Architecture:* `io: 62`, `api: 38`, `concurrency: 2`, `import: 35`
* *Defense:* `safety: 30`, `doc: 32`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.43
  * `Choke Point (Betweenness):` 0.000449 | `Ripple Effect (Closeness):` 0.016644
  * `Imports (Out-Degree: 10):` collections, ctypes, errno, fcntl, getpass, logging, os, pty...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `pwnlib/constants/freebsd.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1105.4 | **LOC:** 1071 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1069`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pwnlib.constants.constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/rop/rop.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1104.68 | **LOC:** 1667 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **25**; blast radius 2.413; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.4%)
- **Documentation Coverage:** 39.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(Many-Argument Workhorses)** (Impact: 107.7)
    * *Intent:* """ Construct the ROP chain into a list of elements which can be passed to :func:`.flat`. Arguments:...
  * `setRegisters` **(Many-Argument Workhorses)** (Impact: 45.0)
    * *Intent:* """ Returns an list of addresses/values which will set the specified register context. Arguments: re...
  * `__load` **(Compute Cores)** (Impact: 41.2)
    * *Intent:* """Load all ROP gadgets for the selected ELF files"""
  * `ret2csu` **(Many-Argument Workhorses)** (Impact: 38.3)
  * `__getattr__` **(Compute Cores)** (Impact: 33.3)
    * *Intent:* """Helper to make finding ROP gadgets easier. Also provides a shorthand for ``.call()``: ``rop.funct...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 168 instances
* *State Mutation (weighted view):* 525
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 169`, `args: 46`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 189`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `io: 7`, `api: 34`, `import: 35`
* *Defense:* `safety: 46`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.413
  * `Choke Point (Betweenness):` 0.000157 | `Ripple Effect (Closeness):` 0.004426
  * `Imports (Out-Degree: 7):` , .ret2csu, collections, copy, enum, hashlib, itertools, os...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pwnlib/gdb.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1090.06 | **LOC:** 1605 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **20**; blast radius 2.961; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (52.8%)
- **Documentation Coverage:** 46.9697% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `attach` **(Many-Argument Workhorses)** (Impact: 224.9)
  * `debug` **(Many-Argument Workhorses)** (Impact: 173.1)
  * `_gdbserver_args` **(Many-Argument Workhorses)** (Impact: 63.8)
    * *Intent:* """_gdbserver_args(pid=None, path=None, args=None, which=None, env=None) -> list Sets up a listening...
  * `_gdbserver_port` **(Stateful Encapsulated Methods)** (Impact: 16.3)
  * `find_module_addresses` **(Many-Argument Workhorses)** (Impact: 16.2)
    * *Intent:* """ Cheat to find modules by using GDB. We can't use ``/proc/$pid/map`` since some servers forbid it...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 138 instances
* *Api Near Db Sink:* 2 instances
* *State Mutation (weighted view):* 437
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 144`, `args: 39`, `func_start: 36`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 161`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 25`, `api: 24`, `concurrency: 1`, `import: 27`
* *Defense:* `safety: 25`, `doc: 27`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.961
  * `Choke Point (Betweenness):` 9.5e-05 | `Ripple Effect (Closeness):` 0.016736
  * `Imports (Out-Degree: 3):` gdb, os, platform, psutil, pwnlib, pwnlib.asm, pwnlib.context, pwnlib.log...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pwnlib/util/packing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1025.3 | **LOC:** 1455 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **8**; blast radius 10.358; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.7%)
- **Documentation Coverage:** 58.4416% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dd` **(Many-Argument Workhorses)** (Impact: 138.8)
  * `pack` **(Many-Argument Workhorses)** (Impact: 74.3)
  * `_fit` **(Many-Argument Workhorses)** (Impact: 52.7)
    * *Intent:* # Pulls bytes from `filler` and adds them to `pad` until it ends in `key`. # Returns the index of `k...
  * `_flat` **(Many-Argument Workhorses)** (Impact: 36.0)
  * `overlap` **(Compute Cores)** (Impact: 32.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 141 instances
* *State Mutation (weighted view):* 437
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 138`, `args: 41`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 155`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 34`, `import: 9`
* *Defense:* `safety: 46`, `doc: 25`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.358
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033948
  * `Imports (Out-Degree: 0):` collections, of, pwnlib.context, pwnlib.log, pwnlib.util, struct, sys, warnings
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `pwnlib/tubes/tube.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 964.04 | **LOC:** 1721 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **19**; blast radius 2.893; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.9%)
- **Documentation Coverage:** 51.4793% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `upload_manually` **(Many-Argument Workhorses)** (Impact: 69.2)
  * `interactive` **(Many-Argument Workhorses)** (Impact: 47.6)
    * *Intent:* """interactive(prompt = pwnlib.term.text.bold_red('$') + ' ') Does simultaneous reading and writing ...
  * `recvuntil` **(Many-Argument Workhorses)** (Impact: 26.8)
    * *Intent:* """recvuntil(delims, drop=False, timeout=default) -> bytes Receive data until one of `delims` is enc...
  * `recvregex` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `recvlines` **(Many-Argument Workhorses)** (Impact: 17.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 101 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 329
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 239`, `args: 86`, `func_start: 84`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 127`, `planned_debt: 1`
* *Architecture:* `io: 6`, `api: 82`, `concurrency: 2`, `import: 24`
* *Defense:* `safety: 35`, `doc: 56`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.893
  * `Choke Point (Betweenness):` 0.000123 | `Ripple Effect (Closeness):` 0.016263
  * `Imports (Out-Degree: 4):` abc, gzip, io, logging, lzma, os, pwnlib, pwnlib.args...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pwnlib/adb/adb.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 958.16 | **LOC:** 1604 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 2.454; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (55.1%)
- **Documentation Coverage:** 41.2791% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compile` **(I/O & Config Routines)** (Impact: 18.1)
  * `unlink` **(Compute Cores)** (Impact: 16.2)
    * *Intent:* """Unlinks a file or directory on the target device. Examples: .. doctest:: :skipif: skip_android >>...
  * `__getattr__` **(Compute Cores)** (Impact: 15.1)
  * `walk` **(Compute Cores)** (Impact: 14.9)
  * `which` **(Many-Argument Workhorses)** (Impact: 14.1)
    * *Intent:* """Retrieves the full path to a binary in ``$PATH`` on the device Arguments: name(str): Binary name ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 136 instances
* *State Mutation (weighted view):* 441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 304`, `args: 89`, `func_start: 87`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 169`
* *Architecture:* `io: 30`, `api: 79`, `import: 20`
* *Defense:* `safety: 8`, `doc: 60`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.454
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.003112
  * `Imports (Out-Degree: 3):` dateutil.parser, functools, glob, logging, os, pwnlib, pwnlib.context, pwnlib.device...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pwnlib/dynelf.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 944.86 | **LOC:** 1068 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 1.029; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (39.5%)
- **Documentation Coverage:** 30.3571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lookup` **(Many-Argument Workhorses)** (Impact: 45.8)
    * *Intent:* """lookup(symb = None, lib = None) -> int Find the address of ``symbol``, which is found in ``lib``....
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 36.9)
    * *Intent:* ''' Instantiates an object which can resolve symbols in a running binary given a :class:`pwnlib.meml...
  * `_rel_lookup` **(Many-Argument Workhorses)** (Impact: 27.1)
    * *Intent:* """Performs slower symbol lookup using DT_JMPREL(.rela.plt)"""
  * `_resolve_symbol_gnu` **(Many-Argument Workhorses)** (Impact: 19.9)
    * *Intent:* """ Internal Documentation: The GNU hash structure is a bit more complex than the normal hash struct...
  * `_lookup` **(Many-Argument Workhorses)** (Impact: 18.8)
    * *Intent:* """Performs the actual symbol lookup within one ELF file."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 166 instances
* *State Mutation (weighted view):* 541
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 129`, `args: 36`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 209`, `dead_code: 3`
* *Architecture:* `api: 22`, `import: 11`
* *Defense:* `safety: 4`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001844
  * `Imports (Out-Degree: 4):` ctypes, elftools.elf.enums, pwnlib, pwnlib.context, pwnlib.elf, pwnlib.log, pwnlib.memleak, pwnlib.util.fiddling...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pwnlib/elf/corefile.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 942.7 | **LOC:** 1648 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **26**; blast radius 1.702; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (55.0%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 48.8)
    * *Intent:* #: The NT_PRSTATUS object. self.prstatus = None #: The NT_PRPSINFO object self.prpsinfo = None #: Th...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 31.5)
  * `_parse_nt_file` **(Stateful Encapsulated Methods)** (Impact: 31.2)
  * `_parse_stack` **(Compute Cores)** (Impact: 22.6)
    * *Intent:* # Get a copy of the stack mapping stack = self.stack if not stack: return # If the stack does not en...
  * `apport_crash_extract_corefile` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* """Extract a corefile from an apport crash file contents. Arguments: crashfile_data(str): Crash file...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 139 instances
* *State Mutation (weighted view):* 462
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 227`, `args: 55`, `func_start: 52`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 184`, `fragile_debt: 1`
* *Architecture:* `io: 22`, `api: 47`, `import: 31`
* *Defense:* `safety: 32`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.000141 | `Ripple Effect (Closeness):` 0.012178
  * `Imports (Out-Degree: 9):` collections, ctypes, elftools, elftools.common.utils, elftools.construct, glob, gzip, io...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pwnlib/tubes/ssh.py` -> Churn: **62.06%** | Cog Load: 51.4727% | Debt: 31.5542%
- `pwnlib/util/packing.py` -> Churn: **51.33%** | Cog Load: 55.6788% | Debt: 11.4098%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pwnlib/dynelf.py` -> **RocketDev** (100.0% isolated ownership) | Magnitude: 944.86
- `pwnlib/fmtstr.py` -> **RocketDev** (100.0% isolated ownership) | Magnitude: 861.1
- `pwnlib/term/key.py` -> **RocketDev** (100.0% isolated ownership) | Magnitude: 635.98
- `pwnlib/protocols/adb/__init__.py` -> **RocketDev** (100.0% isolated ownership) | Magnitude: 485.08
- `pwnlib/regsort.py` -> **RocketDev** (100.0% isolated ownership) | Magnitude: 396.92

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pwnlib/elf/elf.py` -> **Severity: 0.052** (Bridge: 0.0005 * Flux: 100.0%)
- `pwnlib/tubes/process.py` -> **Severity: 0.045** (Bridge: 0.0004 * Flux: 100.0%)
- `pwnlib/util/fiddling.py` -> **Severity: 0.031** (Bridge: 0.0003 * Flux: 100.0%)
- `pwnlib/util/misc.py` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 100.0%)
- `pwnlib/args.py` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pwnlib/util/packing.py` -> **Severity: 3.316** (Embedded: 0.0339 * Error Risk: 97.6935%)
- `pwnlib/args.py` -> **Severity: 3.296** (Embedded: 0.0341 * Error Risk: 96.5338%)
- `pwnlib/term/term.py` -> **Severity: 2.994** (Embedded: 0.0305 * Error Risk: 98.2109%)
- `pwnlib/util/fiddling.py` -> **Severity: 2.806** (Embedded: 0.0283 * Error Risk: 99.2713%)
- `pwnlib/constants/constant.py` -> **Severity: 2.77** (Embedded: 0.0443 * Error Risk: 62.5811%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pwnlib/constants/constant.py` -> **Severity: 2786.2** (Blast Radius: 27.862 * Doc Risk: 100.0%)
- `pwnlib/shellcraft/templates/i386/cgc/random.asm` -> **Severity: 993.7** (Blast Radius: 9.937 * Doc Risk: 100.0%)
- `pwnlib/term/term.py` -> **Severity: 931.8** (Blast Radius: 9.318 * Doc Risk: 100.0%)
- `pwnlib/util/packing.py` -> **Severity: 605.338** (Blast Radius: 10.358 * Doc Risk: 58.4416%)
- `pwnlib/timeout.py` -> **Severity: 546.162** (Blast Radius: 7.889 * Doc Risk: 69.2308%)

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
