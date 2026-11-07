# ARCHITECTURAL_BRIEF: pwntools
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Gallopsled/pwntools.git` |
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
- **Scope:** 563 analyzed artifact(s), 34405 LOC.
- **Load-bearing artifact:** `pwnlib/context/__init__.py` -- 50 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pwn/toplevel.py` -- pulls in 66 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pwnlib/tubes/ssh.py` at magnitude 1795.9 (structural weight, not risk).
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
| Total Artifacts | 1445 |
| Analyzed Artifacts (Scanned) | 563 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 882 |
| Total LOC | 34405 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 39.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3584 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3146 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9876 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 15 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 326 | 9950 | 57.9% |
| PYTHON | 182 | 23165 | 32.3% |
| MARKDOWN | 17 | 0 | 3.0% |
| SHELL | 11 | 372 | 2.0% |
| YAML | 7 | 534 | 1.2% |
| MAKEFILE | 6 | 111 | 1.1% |
| DOCKERFILE | 6 | 198 | 1.1% |
| PLAINTEXT | 4 | 0 | 0.7% |
| C | 4 | 75 | 0.7% |

## 4.1 SOURCE ENCODINGS
All 563 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 20%, Data / Markup / Trivial 18%, Parameter Forwarders Files 17%, Declarative / Non-Code 16%, State Mutators Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 542 | 96.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 21 | 3.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 882*

**Composition by Extension & Reason:**
- `.asm`: 217x Excluded (Machine-Generated Source Code Signature: 102 LOC), 95x Excluded (Machine-Generated Source Code Signature: 103 LOC), 85x Excluded (Machine-Generated Source Code Signature: 104 LOC)
- `.h`: 141x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 55x Excluded (Binary Format Detected), 36x Unsupported Format (.undeterminable), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 80x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 293 LOC), 1x Excluded (Saturation: Line 79 exceeds 500 chars)
- `.txt`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.native`: 2x Excluded (Unsupported Extension: '.native')
- `.native32`: 2x Excluded (Unsupported Extension: '.native32')
- `.cfg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.aarch64`: 1x Excluded (Unsupported Extension: '.aarch64')
- `.arm`: 1x Excluded (Binary Format Detected)
- `.mips`: 1x Excluded (Unsupported Extension: '.mips')
- `.mips64`: 1x Excluded (Unsupported Extension: '.mips64')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.9 | 13.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.5 | 28.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 27.8 | 16.2 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 96.9 | 7.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 27.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 15.4 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.0 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 71.9 | 5.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 63.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 507 | 103 | 2 | `pwnlib/util/crc/__init__.py` |
| cleanup | 71 | 24 | 0 | `pwnlib/tubes/process.py` |
| guards | 1177 | 113 | 4 | `pwnlib/tubes/ssh.py` |
| danger | 990 | 176 | 5 | `pwnlib/tubes/process.py` |
| concurrency | 132 | 56 | 0 | `pwnlib/util/iters.py` |
| connectivity | 1685 | 158 | 6 | `pwnlib/elf/elf.py` |
| io | 1469 | 225 | 6 | `pwnlib/tubes/process.py` |
| crypto | 4 | 4 | 0 | `pwnlib/commandline/libcdb.py` |
| ipc | 168 | 49 | 0 | `pwnlib/util/misc.py` |
| time | 33 | 17 | 0 | `pwnlib/tubes/process.py` |
| serialization | 1 | 1 | 0 | `pwnlib/util/iters.py` |
| regex | 56 | 27 | 0 | `pwnlib/rop/rop.py` |
| events | 155 | 37 | 0 | `pwnlib/protocols/adb/__init__.py` |
| tests | 14 | 9 | 0 | `pwnlib/commandline/elfpatch.py` |
| docs | 1014 | 112 | 3 | `pwnlib/elf/elf.py` |
| debt | 240 | 91 | 2 | `pwnlib/tubes/ssh.py` |
| mutation | 13222 | 480 | 52 | `pwnlib/tubes/ssh.py` |
| dead_code | 462 | 272 | 2 | `pwnlib/shellcraft/registers.py` |
| credential | 0 | 0 | 0 | - |
| threat | 73 | 12 | 0 | `pwnlib/encoders/mips/xor.py` |
| ml_ai | 0 | 0 | 0 | - |
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

1. **__init__.py** (`pwnlib/context/__init__.py`) — 50 inbound connections
2. **__init__.py** (`pwn/__init__.py`) — 44 inbound connections
3. **log.py** (`pwnlib/log.py`) — 44 inbound connections
4. **tube.py** (`pwnlib/tubes/tube.py`) — 29 inbound connections
5. **packing.py** (`pwnlib/util/packing.py`) — 29 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **toplevel.py** (`pwn/toplevel.py`) — 66 outbound dependencies
2. **elf.py** (`pwnlib/elf/elf.py`) — 34 outbound dependencies
3. **process.py** (`pwnlib/tubes/process.py`) — 30 outbound dependencies
4. **ssh.py** (`pwnlib/tubes/ssh.py`) — 29 outbound dependencies
5. **__init__.py** (`pwnlib/context/__init__.py`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Many-Argument Workhorses)** (@ `pwnlib/tubes/process.py`) -> Impact: **234.9** | LOC: 190
- `attach` **(Many-Argument Workhorses)** (@ `pwnlib/gdb.py`) -> Impact: **224.9** | LOC: 426
- `debug` **(Many-Argument Workhorses)** (@ `pwnlib/gdb.py`) -> Impact: **173.1** | LOC: 320
- `run_in_new_terminal` **(Many-Argument Workhorses)** (@ `pwnlib/util/misc.py`) -> Impact: **161.8** | LOC: 198
  * *Intent:* """run_in_new_terminal(command, terminal=None, args=None, kill_at_exit=True, preexec_fn=None) -> int Run a command in a new terminal. When ``terminal`...
- `regsort` **(Many-Argument Workhorses)** (@ `pwnlib/regsort.py`) -> Impact: **156.6** | LOC: 327
  * *Intent:* """ Sorts register dependencies. Given a dictionary of registers to desired register contents, return the optimal order in which to set the registers ...
- `__init__` **(Many-Argument Workhorses)** (@ `pwnlib/tubes/ssh.py`) -> Impact: **154.2** | LOC: 207
- `process` **(Many-Argument Workhorses)** (@ `pwnlib/tubes/ssh.py`) -> Impact: **138.9** | LOC: 250
- `dd` **(Many-Argument Workhorses)** (@ `pwnlib/util/packing.py`) -> Impact: **138.8** | LOC: 184
- `ret2csu` **(Many-Argument Workhorses)** (@ `pwnlib/rop/ret2csu.py`) -> Impact: **127.3** | LOC: 94
  * *Intent:* """Build a ret2csu ROPchain Arguments: edi, rsi, rdx: Three primary registers to populate rbx, rbp, r12, r13, r14, r15: Optional registers to populate...
- `hexdump_iter` **(Many-Argument Workhorses)** (@ `pwnlib/util/fiddling.py`) -> Impact: **120.9** | LOC: 163

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pwnlib` | 30 | 6763.88 | 34.34% | 18.99% |
| `pwnlib/util` | 15 | 4840.2 | 44.16% | 9.48% |
| `pwnlib/tubes` | 10 | 4708.12 | 48.7% | 8.95% |
| `pwnlib/elf` | 7 | 3316.96 | 38.85% | 7.28% |
| `pwnlib/term` | 12 | 2791.62 | 62.34% | 31.78% |
| `pwnlib/rop` | 7 | 1973.44 | 50.04% | 20.27% |
| `pwnlib/commandline` | 23 | 1483.38 | 54.18% | 0.0% |
| `pwnlib/adb` | 5 | 1105.64 | 25.15% | 0.0% |
| `pwnlib/context` | 1 | 757.82 | 55.56% | 11.0% |
| `pwnlib/encoders/arm/alphanumeric` | 6 | 666.58 | 49.73% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pwnlib/shellcraft/templates/amd64/push.asm` -> **99.9993%** Exposure
- `pwnlib/shellcraft/templates/thumb/push.asm` -> **99.9989%** Exposure
- `pwnlib/gdb_api_bridge.py` -> **99.9979%** Exposure
- `pwnlib/timeout.py` -> **99.9818%** Exposure
- `pwnlib/rop/ret2dlresolve.py` -> **99.9691%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pwnlib/abi.py` -> **100.0%** Exposure
- `pwnlib/adb/adb.py` -> **100.0%** Exposure
- `pwnlib/adb/bootloader.py` -> **100.0%** Exposure
- `pwnlib/args.py` -> **100.0%** Exposure
- `pwnlib/asm.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `examples/fmtstr/Makefile` -> **11** Orphaned Functions | **0** Duplicates
- `pwnlib/gdb_api_bridge.py` -> **6** Orphaned Functions | **2** Duplicates
- `pwnlib/rop/ret2dlresolve.py` -> **0** Orphaned Functions | **8** Duplicates
- `pwnlib/shellcraft/registers.py` -> **8** Orphaned Functions | **0** Duplicates
- `pwnlib/term/term.py` -> **7** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `1036` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pwnlib/tubes/ssh.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.571)
- **Top Global Matches:** file_cluster_12: 7.571, file_cluster_4: 7.738, file_cluster_16: 10.107
- **Magnitude:** 1795.9 | **LOC:** 2242 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **29**; blast radius 12.502; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.3%)
- **Documentation Coverage:** 47.3373% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 154.2)
  * `process` **(Many-Argument Workhorses)** (Impact: 138.9)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.502
  * `Choke Point (Betweenness):` 0.001618 | `Ripple Effect (Closeness):` 0.097896
  * `Imports (Out-Degree: 15):` ctypes, io, logging, os, paramiko, paramiko.ssh_exception, platform, pwnlib...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `pwnlib/elf/elf.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.189)
- **Top Global Matches:** file_cluster_12: 7.189, file_cluster_4: 7.809, file_cluster_15: 9.028
- **Magnitude:** 1713.62 | **LOC:** 2601 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **34**; blast radius 18.125; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (60.9%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.125
  * `Choke Point (Betweenness):` 0.004675 | `Ripple Effect (Closeness):` 0.099651
  * `Imports (Out-Degree: 18):` collections, elftools.elf.constants, elftools.elf.descriptions, elftools.elf.dynamic, elftools.elf.elffile, elftools.elf.enums, elftools.elf.gnuversions, elftools.elf.relocation...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `pwnlib/tubes/process.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.919)
- **Top Global Matches:** file_cluster_12: 8.919, file_cluster_4: 9.535, file_cluster_7: 10.718
- **Magnitude:** 1109.36 | **LOC:** 1600 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **30**; blast radius 5.855; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.0%)
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
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 1`, `state_mutation: 157`, `dead_code: 2`, `fragile_debt: 5`
* *Architecture:* `io: 62`, `api: 38`, `concurrency: 2`, `import: 35`
* *Defense:* `safety: 30`, `doc: 32`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.855
  * `Choke Point (Betweenness):` 0.000902 | `Ripple Effect (Closeness):` 0.081057
  * `Imports (Out-Degree: 14):` collections, ctypes, errno, fcntl, logging, os, pty, pwnlib...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `pwnlib/rop/rop.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.19)
- **Top Global Matches:** file_cluster_4: 7.19, file_cluster_6: 10.107, file_cluster_12: 11.781
- **Magnitude:** 1104.68 | **LOC:** 1667 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **25**; blast radius 2.857; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.4%)
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
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 189`, `fragile_debt: 1`
* *Architecture:* `io: 7`, `api: 34`, `import: 35`
* *Defense:* `safety: 46`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.857
  * `Choke Point (Betweenness):` 0.000502 | `Ripple Effect (Closeness):` 0.022402
  * `Imports (Out-Degree: 14):` .ret2csu, .ret2dlresolve, collections, copy, enum, hashlib, itertools, os...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pwnlib/gdb.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.545)
- **Top Global Matches:** file_cluster_4: 5.545, file_cluster_12: 10.511, file_cluster_6: 10.86
- **Magnitude:** 1099.96 | **LOC:** 1605 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **18**; blast radius 3.048; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Complexity Load (formerly Cognitive Load) (52.8%)
- **Documentation Coverage:** 46.9697% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `attach` **(Many-Argument Workhorses)** (Impact: 224.9)
  * `debug` **(Many-Argument Workhorses)** (Impact: 173.1)
  * `_gdbserver_args` **(Many-Argument Workhorses)** (Impact: 63.8)
    * *Intent:* """_gdbserver_args(pid=None, path=None, args=None, which=None, env=None) -> list Sets up a listening...
  * `find_module_addresses` **(Many-Argument Workhorses)** (Impact: 30.1)
    * *Intent:* """ Cheat to find modules by using GDB. We can't use ``/proc/$pid/map`` since some servers forbid it...
  * `_gdbserver_port` **(Stateful Encapsulated Methods)** (Impact: 16.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 136 instances
* *Api Near Db Sink:* 2 instances
* *State Mutation (weighted view):* 433
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 144`, `args: 39`, `func_start: 36`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 161`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 25`, `api: 24`, `concurrency: 1`, `import: 27`
* *Defense:* `safety: 25`, `doc: 27`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.048
  * `Choke Point (Betweenness):` 0.001489 | `Ripple Effect (Closeness):` 0.077661
  * `Imports (Out-Degree: 13):` gdb, os, platform, psutil, pwnlib, pwnlib.asm, pwnlib.context, pwnlib.log...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pwnlib/util/packing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.918)
- **Top Global Matches:** file_cluster_4: 5.918, file_cluster_6: 8.714, file_cluster_12: 12.62
- **Magnitude:** 1025.3 | **LOC:** 1455 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **7**; blast radius 22.04; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.5%), Connectivity (formerly Api Exposure) (65.1%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.04
  * `Choke Point (Betweenness):` 0.000815 | `Ripple Effect (Closeness):` 0.107346
  * `Imports (Out-Degree: 4):` collections, pwnlib.context, pwnlib.log, pwnlib.util, struct, sys, warnings
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `pwnlib/tubes/tube.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.305)
- **Top Global Matches:** file_cluster_12: 6.305, file_cluster_15: 8.846, file_cluster_4: 9.238
- **Magnitude:** 964.04 | **LOC:** 1721 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **19**; blast radius 12.591; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.9%), Guard Balance (formerly Safety Score) (72.1%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.591
  * `Choke Point (Betweenness):` 0.001112 | `Ripple Effect (Closeness):` 0.093297
  * `Imports (Out-Degree: 8):` abc, gzip, io, logging, lzma, os, pwnlib, pwnlib.args...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `pwnlib/adb/adb.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.175)
- **Top Global Matches:** file_cluster_12: 6.175, file_cluster_15: 8.059, file_cluster_16: 8.839
- **Magnitude:** 958.16 | **LOC:** 1604 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 1.311; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%), Connectivity (formerly Api Exposure) (55.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.311
  * `Choke Point (Betweenness):` 0.000114 | `Ripple Effect (Closeness):` 0.001779
  * `Imports (Out-Degree: 14):` dateutil.parser, functools, glob, logging, os, pwnlib, pwnlib.context, pwnlib.device...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pwnlib/dynelf.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.787)
- **Top Global Matches:** file_cluster_16: 6.787, file_cluster_4: 7.005, file_cluster_15: 7.799
- **Magnitude:** 944.86 | **LOC:** 1068 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 1.681; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (39.5%)
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
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 209`
* *Architecture:* `api: 22`, `import: 11`
* *Defense:* `safety: 4`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.681
  * `Choke Point (Betweenness):` 3.6e-05 | `Ripple Effect (Closeness):` 0.028309
  * `Imports (Out-Degree: 8):` ctypes, elftools.elf.enums, pwnlib, pwnlib.context, pwnlib.elf, pwnlib.log, pwnlib.memleak, pwnlib.util.fiddling...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pwnlib/elf/corefile.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.608)
- **Top Global Matches:** file_cluster_4: 8.608, file_cluster_12: 8.646, file_cluster_7: 10.559
- **Magnitude:** 942.7 | **LOC:** 1648 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **25**; blast radius 4.784; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Connectivity (formerly Api Exposure) (55.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.000276 | `Ripple Effect (Closeness):` 0.078761
  * `Imports (Out-Degree: 12):` collections, ctypes, elftools, elftools.common.utils, elftools.construct, glob, gzip, io...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pwnlib/util/fiddling.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.954)
- **Top Global Matches:** file_cluster_4: 5.954, file_cluster_6: 9.95, file_cluster_12: 11.214
- **Magnitude:** 879.02 | **LOC:** 1145 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **12**; blast radius 10.526; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.0%)
- **Documentation Coverage:** 47.6923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hexdump_iter` **(Many-Argument Workhorses)** (Impact: 120.9)
  * `bits` **(Many-Argument Workhorses)** (Impact: 49.8)
    * *Intent:* """bits(s, endian = 'big', zero = 0, one = 1) -> list Converts the argument into a list of bits. Arg...
  * `xor` **(Compute Cores)** (Impact: 32.3)
    * *Intent:* # misc binary functions """xor(*args, cut = 'max') -> str Flattens its arguments using :func:`pwnlib...
  * `xor_key` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `unbits` **(Compute Cores)** (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 127 instances
* *State Mutation (weighted view):* 386
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 105`, `args: 35`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 132`
* *Architecture:* `api: 32`, `import: 17`
* *Defense:* `safety: 18`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.526
  * `Choke Point (Betweenness):` 0.000594 | `Ripple Effect (Closeness):` 0.093611
  * `Imports (Out-Degree: 6):` base64, binascii, io, os, pwnlib.context, pwnlib.log, pwnlib.term, pwnlib.util...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `pwnlib/fmtstr.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.06)
- **Top Global Matches:** file_cluster_12: 7.06, file_cluster_4: 8.803, file_cluster_15: 9.874
- **Magnitude:** 861.1 | **LOC:** 1057 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 1.681; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.2%)
- **Documentation Coverage:** 58.7302% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `merge_atoms_overlapping` **(Many-Argument Workhorses)** (Impact: 48.9)
    * *Intent:* # # what we don't do: # - create new atoms that cannot be created by merging existing atoms # - opti...
  * `find_min_hamming_in_range_step` **(Many-Argument Workhorses)** (Impact: 31.9)
    * *Intent:* """ Compute a single step of the algorithm for find_min_hamming_in_range Arguments: prev(dict): resu...
  * `make_payload_dollar` **(Many-Argument Workhorses)** (Impact: 31.5)
  * `sort_atoms` **(Many-Argument Workhorses)** (Impact: 27.4)
    * *Intent:* """ This function sorts atoms such that the amount by which the format string counter has to been in...
  * `find_min_hamming_in_range` **(Many-Argument Workhorses)** (Impact: 27.0)
    * *Intent:* """ Find the value which differs in the least amount of bytes from the target and is in the given ra...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 131 instances
* *State Mutation (weighted view):* 411
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 111`, `args: 38`, `func_start: 35`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 149`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `api: 31`, `import: 10`
* *Defense:* `safety: 11`, `doc: 21`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.681
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.028309
  * `Imports (Out-Degree: 6):` logging, operator, pwnlib.log, pwnlib.memleak, pwnlib.util.cyclic, pwnlib.util.fiddling, pwnlib.util.misc, pwnlib.util.packing...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pwnlib/util/misc.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.93)
- **Top Global Matches:** file_cluster_6: 7.93, file_cluster_4: 13.378, file_cluster_8: 14.169
- **Magnitude:** 848.56 | **LOC:** 984 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 14.3%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **21**; blast radius 6.405; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.4%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.9%)
- **Documentation Coverage:** 39.3939% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_in_new_terminal` **(Many-Argument Workhorses)** (Impact: 161.8)
    * *Intent:* """run_in_new_terminal(command, terminal=None, args=None, kill_at_exit=True, preexec_fn=None) -> int...
  * `_create_execve_script` **(Many-Argument Workhorses)** (Impact: 100.2)
  * `normalize_argv_env` **(Many-Argument Workhorses)** (Impact: 47.6)
    * *Intent:* # # Validate argv # # - Must be a list/tuple of strings # - Each string must not contain '\x00' # ar...
  * `which` **(Many-Argument Workhorses)** (Impact: 33.0)
    * *Intent:* """which(name, flags = os.X_OK, all = False) -> str or str set Works as the system command ``which``...
  * `register_sizes` **(Many-Argument Workhorses)** (Impact: 21.3)
    * *Intent:* """Create dictionaries over register sizes and relations Given a list of lists of overlapping regist...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 128 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 395
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 99`, `args: 18`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 9`, `state_mutation: 139`, `planned_debt: 2`
* *Architecture:* `io: 39`, `api: 16`, `import: 23`
* *Defense:* `safety: 26`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.405
  * `Choke Point (Betweenness):` 0.000637 | `Ripple Effect (Closeness):` 0.083241
  * `Imports (Out-Degree: 9):` base64, errno, inspect, json, os, pwnlib, pwnlib.context, pwnlib.log...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `pwnlib/context/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.425)
- **Top Global Matches:** file_cluster_12: 6.425, file_cluster_15: 8.31, file_cluster_16: 9.347
- **Magnitude:** 757.82 | **LOC:** 1785 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **50** in-repo importer(s); it depends on **25**; blast radius 38.867; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (96.9%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.6%)
- **Documentation Coverage:** 48.5149% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `log_file` **(Many-Argument Workhorses)** (Impact: 18.7)
  * `setter` **(Defensive Guards)** (Impact: 16.4)
  * `device` **(Defensive Guards)** (Impact: 16.3)
    * *Intent:* """Sets the device being operated on. """
  * `LocalContext` **(Defensive Guards)** (Impact: 14.4)
    * *Intent:* """ Wraps the specified function on a context.local() block, using kwargs. Example: >>> context.clea...
  * `arch` **(Many-Argument Workhorses)** (Impact: 13.5)
    * *Intent:* """ Target binary architecture. Allowed values are listed in :attr:`pwnlib.context.ContextType.archi...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 65 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 255`, `args: 101`, `func_start: 100`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 113`, `planned_debt: 5`
* *Architecture:* `io: 30`, `api: 93`, `concurrency: 3`, `import: 27`
* *Defense:* `safety: 37`, `doc: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.867
  * `Choke Point (Betweenness):` 0.003655 | `Ripple Effect (Closeness):` 0.125236
  * `Imports (Out-Degree: 9):` atexit, collections, collections.abc, errno, functools, logging, os, os.path...
  * `Imported By (In-Degree: 50):` (Excluded from Brief to save tokens)

### `pwnlib/term/key.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.774)
- **Top Global Matches:** file_cluster_4: 6.774, file_cluster_12: 9.967, file_cluster_16: 10.78
- **Magnitude:** 635.98 | **LOC:** 487 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.081; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.4%)
- **Documentation Coverage:** 94.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_peek_simple` **(I/O & Config Routines)** (Impact: 31.1)
  * `_parse_csi` **(Stateful Encapsulated Methods)** (Impact: 26.0)
    * *Intent:* # csi
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 22.4)
  * `__str__` **(Stateful Encapsulated Methods)** (Impact: 19.7)
  * `_peekkey_ss3` **(Stateful Encapsulated Methods)** (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 123 instances
* *State Mutation (weighted view):* 379
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 121`, `args: 28`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 133`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 6`, `api: 7`, `import: 8`
* *Defense:* `safety: 9`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.081
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` errno, os, pwnlib.term, select, string, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/libcdb.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.07)
- **Top Global Matches:** file_cluster_4: 7.07, file_cluster_12: 10.787, file_cluster_6: 11.296
- **Magnitude:** 625.58 | **LOC:** 958 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 1.081; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.0%), Complexity Load (formerly Cognitive Load) (50.5%)
- **Documentation Coverage:** 41.4634% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `search_by_symbol_offsets` **(Many-Argument Workhorses)** (Impact: 61.8)
    * *Intent:* """ Lookup possible matching libc versions based on leaked function addresses. The leaked function a...
  * `search_by_hash` **(Many-Argument Workhorses)** (Impact: 34.1)
    * *Intent:* """search_by_hash(str, str, bool, bool) -> str Arguments: search_target(str): Use for searching the ...
  * `unstrip_libc` **(Compute Cores)** (Impact: 30.1)
    * *Intent:* """ Given a path to a libc binary, attempt to download matching debug info and add them back to the ...
  * `_extract_tarfile` **(Stateful Encapsulated Methods)** (Impact: 30.1)
  * `download_libraries` **(Many-Argument Workhorses)** (Impact: 25.2)
    * *Intent:* """download_libraries(str, bool) -> str Download the matching libraries for the given libc binary an...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 169`, `args: 27`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 98`
* *Architecture:* `io: 38`, `api: 17`, `import: 29`
* *Defense:* `safety: 14`, `doc: 15`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.081
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` io, os, pwnlib.context, pwnlib.elf, pwnlib.filesystem.path, pwnlib.log, pwnlib.term, pwnlib.tubes.process...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/term/readline.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.249)
- **Top Global Matches:** file_cluster_12: 6.249, file_cluster_15: 7.706, file_cluster_4: 8.235
- **Magnitude:** 623.58 | **LOC:** 496 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 1.829; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.1%)
- **Documentation Coverage:** 97.4684% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readline` **(Many-Argument Workhorses)** (Impact: 34.1)
    * *Intent:* # The argument _size is unused, but is there for compatibility # with the existing readline global b...
  * `redisplay` **(I/O & Config Routines)** (Impact: 17.6)
  * `update_search_results` **(Compute Cores)** (Impact: 11.0)
  * `fmt_suggestions` **(Compute Cores)** (Impact: 9.3)
  * `auto_complete` **(Compute Cores)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 115 instances
* *State Mutation (weighted view):* 371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 110`, `args: 37`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 141`, `fragile_debt: 1`
* *Architecture:* `io: 7`, `api: 38`, `import: 12`
* *Defense:* `safety: 11`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.829
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.029708
  * `Imports (Out-Degree: 2):` builtins, io, os, pwnlib.term, pwnlib.util, sys
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pwnlib/asm.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.292)
- **Top Global Matches:** file_cluster_4: 6.292, file_cluster_6: 9.918, file_cluster_12: 11.419
- **Magnitude:** 587.12 | **LOC:** 1032 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **16**; blast radius 3.517; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.9%), Complexity Load (formerly Cognitive Load) (54.9%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `asm` **(Many-Argument Workhorses)** (Impact: 54.7)
  * `disasm` **(Many-Argument Workhorses)** (Impact: 50.4)
    * *Intent:* """disasm(data, ...) -> str Disassembles a bytestring into human readable assembler. To see which ar...
  * `make_elf` **(Many-Argument Workhorses)** (Impact: 36.3)
  * `make_elf_from_assembly` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `which_binutils` **(Many-Argument Workhorses)** (Impact: 29.3)
    * *Intent:* """ Finds a binutils in the PATH somewhere. Expects that the utility is prefixed with the architectu...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 75 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 113`, `args: 24`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 135`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 20`, `api: 12`, `import: 20`
* *Defense:* `safety: 10`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.517
  * `Choke Point (Betweenness):` 0.000315 | `Ripple Effect (Closeness):` 0.078097
  * `Imports (Out-Degree: 9):` collections, errno, glob, os, platform, pwnlib, pwnlib.context, pwnlib.log...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pwnlib/util/iters.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.597)
- **Top Global Matches:** file_cluster_4: 6.597, file_cluster_12: 8.221, file_cluster_15: 8.731
- **Magnitude:** 540.12 | **LOC:** 983 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.081; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (92.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%)
- **Documentation Coverage:** 24.6377% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bruteforce` **(Many-Argument Workhorses)** (Impact: 68.3)
    * *Intent:* """bruteforce(func, alphabet, length, method = 'upto', start = None) Bruteforce `func` to return :co...
  * `mbruteforce` **(Many-Argument Workhorses)** (Impact: 62.8)
    * *Intent:* """mbruteforce(func, alphabet, length, method = 'upto', start = None, threads = None) Same functiona...
  * `unique_window` **(Many-Argument Workhorses)** (Impact: 15.9)
    * *Intent:* """unique_everseen(iterable, window, key = None) -> iterator Get unique elements, preserving order. ...
  * `unique_everseen` **(Compute Cores)** (Impact: 12.1)
    * *Intent:* """unique_everseen(iterable, key = None) -> iterator Get unique elements, preserving order. Remember...
  * `repeat_func` **(Many-Argument Workhorses)** (Impact: 8.2)
    * *Intent:* """repeat_func(func, *args, **kwargs) -> iterator Repeatedly calls `func` with positional arguments ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 62 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 82`, `args: 37`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 76`, `planned_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 31`, `concurrency: 4`, `import: 11`
* *Defense:* `safety: 7`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.081
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` collections, copy, itertools, marshal, multiprocessing, operator, pwnlib.context, pwnlib.log...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/term/term.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.219)
- **Top Global Matches:** file_cluster_12: 6.219, file_cluster_15: 7.401, file_cluster_4: 8.129
- **Magnitude:** 514.8 | **LOC:** 423 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.081; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_locked` **(Compute Cores)** (Impact: 35.5)
  * `output` **(Many-Argument Workhorses)** (Impact: 28.0)
  * `put` **(Compute Cores)** (Impact: 23.2)
  * `goto` **(Compute Cores)** (Impact: 13.8)
  * `update` **(Defensive Guards)** (Impact: 12.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 70 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 108`, `args: 38`, `func_start: 38`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 98`, `unreferenced_by_name: 7`
* *Architecture:* `io: 13`, `api: 34`, `concurrency: 4`, `import: 16`
* *Defense:* `safety: 5`, `sync_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.081
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ..context, ..py2compat, .termcap, atexit, errno, fcntl, os, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwnlib/protocols/adb/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.911)
- **Top Global Matches:** file_cluster_12: 6.911, file_cluster_15: 7.806, file_cluster_16: 7.854
- **Magnitude:** 485.08 | **LOC:** 635 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 3.363; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%), Connectivity (formerly Api Exposure) (51.2%)
- **Documentation Coverage:** 65.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wait_for_device` **(Compute Cores)** (Impact: 23.4)
  * `read` **(Many-Argument Workhorses)** (Impact: 23.1)
    * *Intent:* """Execute the ``READ`` command of the ``SYNC`` API. Arguments: path(str): Path to the file to read ...
  * `transport` **(Many-Argument Workhorses)** (Impact: 21.6)
    * *Intent:* """Sets the Transport on the remote device. Examples: .. doctest:: :skipif: skip_android >>> pwnlib....
  * `_write` **(Stateful Encapsulated Methods)** (Impact: 17.2)
  * `_list` **(Stateful Encapsulated Methods)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 59 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 128`, `args: 49`, `func_start: 49`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 72`
* *Architecture:* `api: 43`, `import: 15`
* *Defense:* `safety: 12`, `doc: 23`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.363
  * `Choke Point (Betweenness):` 0.00072 | `Ripple Effect (Closeness):` 0.046964
  * `Imports (Out-Degree: 13):` functools, logging, pwnlib.context, pwnlib.log, pwnlib.tubes.listen, pwnlib.tubes.process, pwnlib.tubes.remote, pwnlib.util.lists...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pwnlib/log.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.173)
- **Top Global Matches:** file_cluster_15: 6.173, file_cluster_16: 6.483, file_cluster_12: 6.639
- **Magnitude:** 437.76 | **LOC:** 705 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **44** in-repo importer(s); it depends on **15**; blast radius 36.743; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (88.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (79.1%)
- **Documentation Coverage:** 38.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emit` **(Many-Argument Workhorses)** (Impact: 22.5)
    * *Intent:* """ Emit a log record or create/update an animated progress logger depending on whether :data:`term....
  * `maybe_hexdump` **(Compute Cores)** (Impact: 18.6)
    * *Intent:* """maybe_hexdump(self, message, *args, **kwargs) Logs a message using indented. Repeated single byte...
  * `format` **(Compute Cores)** (Impact: 11.8)
    * *Intent:* # use the default formatter to actually format the record msg = super(Formatter, self).format(record...
  * `_log` **(Stateful Encapsulated Methods)** (Impact: 10.4)
    * *Intent:* # Logs are strings, not bytes. Handle Python3 bytes() objects. status = _need_text(status) # this pr...
  * `read_log_config` **(Compute Cores)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 50 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 103`, `args: 47`, `func_start: 47`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 83`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 46`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 2`, `doc: 32`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.743
  * `Choke Point (Betweenness):` 0.001848 | `Ripple Effect (Closeness):` 0.114886
  * `Imports (Out-Degree: 8):` logging, os, pwnlib, pwnlib.config, pwnlib.context, pwnlib.exception, pwnlib.term, pwnlib.util.fiddling...
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `pwnlib/regsort.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.661)
- **Top Global Matches:** file_cluster_6: 9.661, file_cluster_4: 13.244, file_cluster_8: 16.918
- **Magnitude:** 396.92 | **LOC:** 445 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 1.497; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (56.7%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `regsort` **(Many-Argument Workhorses)** (Impact: 156.6)
    * *Intent:* """ Sorts register dependencies. Given a dictionary of registers to desired register contents, retur...
  * `check_cycle_` **(Many-Argument Workhorses)** (Impact: 21.4)
  * `extract_dependencies` **(Many-Argument Workhorses)** (Impact: 8.9)
    * *Intent:* """Return a list of all registers which directly depend on the specified register. Example: >>> extr...
  * `depends_on_cycle` **(Compute Cores)** (Impact: 6.3)
  * `check_cycle` **(Many-Argument Workhorses)** (Impact: 5.2)
    * *Intent:* """Walk down the assignment list of a register, return the path walked if it is encountered again. R...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 33`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 63`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 1`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02789
  * `Imports (Out-Degree: 2):` collections, pwnlib.context, pwnlib.log, random
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pwnlib/encoders/arm/alphanumeric/builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.134)
- **Top Global Matches:** file_cluster_9: 6.134, file_cluster_15: 7.241, file_cluster_16: 8.73
- **Magnitude:** 377.16 | **LOC:** 454 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.387; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `algo1` **(Many-Argument Workhorses)** (Impact: 26.9)
  * `DecoderBuilder` **(Many-Argument Workhorses)** (Impact: 26.8)
  * `buildInit` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `DecoderLoopBuilder` **(Many-Argument Workhorses)** (Impact: 17.7)
  * `algo2` **(Compute Cores)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 36`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 105`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.387
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.001779
  * `Imports (Out-Degree: 3):` .ARM_Instructions, .alphanum_byte, .random_funcs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pwnlib/filesystem/ssh.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.842)
- **Top Global Matches:** file_cluster_15: 6.842, file_cluster_12: 7.278, file_cluster_16: 8.448
- **Magnitude:** 349.38 | **LOC:** 781 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 1.717; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.9%), Guard Balance (formerly Safety Score) (56.4%)
- **Documentation Coverage:** 55.3957% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mkdir` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* # self.ssh.sftp.truncate(self.path, 0)
  * `unlink` **(Many-Argument Workhorses)** (Impact: 8.7)
    * *Intent:* """Remove an existing file. TODO: This test fails catastrophically if the file name is unlink_me (no...
  * `__init__` **(Compute Cores)** (Impact: 8.3)
  * `__eq__` **(Type Conversions)** (Impact: 7.5)
  * `is_dir` **(Compute Cores)** (Impact: 5.4)
    * *Intent:* """Returns True if the path exists and is a directory Example: >>> f = SSHPath('is_dir', ssh=ssh_con...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 146`, `args: 71`, `func_start: 71`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 28`, `planned_debt: 2`
* *Architecture:* `io: 9`, `api: 70`, `import: 8`
* *Defense:* `safety: 13`, `doc: 37`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.717
  * `Choke Point (Betweenness):` 0.000127 | `Ripple Effect (Closeness):` 0.021597
  * `Imports (Out-Degree: 4):` os, pathlib, pwnlib.context, pwnlib.util.misc, pwnlib.util.packing, sys, tempfile, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `pwnlib/shellcraft/templates/i386/cgc/syscall.asm` (ASSEMBLY) | Magnitude: 6.56 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 27, core_var_decl: 11, design_snake_case: 11, io: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `pwnlib/tubes/serialtube.py` (PYTHON) | Magnitude: 96.46 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 28, core_var_decl: 22, design_snake_case: 20
- `pwnlib/util/net.py` (PYTHON) | Magnitude: 263.8 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 141, state_mutation: 60, core_var_decl: 46, design_snake_case: 45
- `pwnlib/term/completer.py` (PYTHON) | Magnitude: 265.18 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 127, state_mutation: 47, branch: 45, structural_boundaries: 41
- `pwnlib/term/unix_termcap.py` (PYTHON) | Magnitude: 87.78 | Delta: **0.152** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 42, state_mutation: 17, branch: 15, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `pwnlib/shellcraft/templates/amd64/linux/findpeer.asm` (ASSEMBLY) | Magnitude: 13.36 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, args: 8, structural_boundaries: 6, branch: 3
- `pwnlib/shellcraft/templates/i386/linux/loader.asm` (ASSEMBLY) | Magnitude: 19.62 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 55, args: 25, core_var_decl: 15
- `pwnlib/shellcraft/templates/amd64/linux/loader.asm` (ASSEMBLY) | Magnitude: 19.56 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 54, args: 27, core_var_decl: 15
- `pwnlib/shellcraft/templates/i386/linux/stager.asm` (ASSEMBLY) | Magnitude: 8.0 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 13, core_var_decl: 9, design_snake_case: 9
- `pwnlib/shellcraft/templates/i386/function.asm` (ASSEMBLY) | Magnitude: 5.64 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 38, core_var_decl: 9, design_snake_case: 9, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pwnlib/data/elf/fmtstr/vuln.c` (C) | Magnitude: 11.9 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 15, pointers: 5, structural_boundaries: 4, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `pwnlib/shellcraft/templates/i386/linux/findpeer.asm` (ASSEMBLY) | Magnitude: 14.56 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 12, args: 7, branch: 3
- `pwnlib/shellcraft/templates/thumb/linux/listen.asm` (ASSEMBLY) | Magnitude: 7.9 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: args: 45, indent_spaces: 39, structural_boundaries: 24, io: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pwnlib/elf/corefile.py` (PYTHON) | Magnitude: 942.7 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 665, structural_boundaries: 227, state_mutation: 184, branch: 172

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `pwnlib/commandline/common.py` (PYTHON) | Magnitude: 34.04 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 17, core_var_decl: 9, design_snake_case: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pwnlib/commandline/hex.py` (PYTHON) | Magnitude: 37.0 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, core_var_decl: 18, design_snake_case: 18, structural_boundaries: 13

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pwnlib/tubes/ssh.py` -> Churn: **67.32%** | Cog Load: 51.5069% | Debt: 30.1386%
- `pwnlib/util/packing.py` -> Churn: **55.68%** | Cog Load: 55.6788% | Debt: 10.5303%
- `.github/workflows/ci.yml` -> Churn: **52.99%** | Cog Load: 7.0721% | Debt: 97.3978%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pwnlib/dynelf.py` -> **RocketDev** (100.0% isolated ownership) | Magnitude: 944.86
- `pwnlib/elf/corefile.py` -> **RocketDev** (100.0% isolated ownership) | Magnitude: 942.7
- `pwnlib/fmtstr.py` -> **RocketDev** (100.0% isolated ownership) | Magnitude: 861.1
- `pwnlib/context/__init__.py` -> **RocketDev** (100.0% isolated ownership) | Magnitude: 757.82
- `pwnlib/term/key.py` -> **RocketDev** (100.0% isolated ownership) | Magnitude: 635.98

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pwn/toplevel.py` -> **Severity: 0.814** (Bridge: 0.0082 * Flux: 98.8087%)
- `pwnlib/elf/elf.py` -> **Severity: 0.468** (Bridge: 0.0047 * Flux: 100.0%)
- `pwn/__init__.py` -> **Severity: 0.408** (Bridge: 0.0082 * Flux: 50.0%)
- `pwnlib/context/__init__.py` -> **Severity: 0.311** (Bridge: 0.0037 * Flux: 84.9999%)
- `pwnlib/log.py` -> **Severity: 0.185** (Bridge: 0.0018 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pwnlib/log.py` -> **Severity: 8.786** (Embedded: 0.1149 * Error Risk: 76.4746%)
- `pwnlib/util/packing.py` -> **Severity: 8.316** (Embedded: 0.1073 * Error Risk: 77.4655%)
- `pwnlib/elf/elf.py` -> **Severity: 8.102** (Embedded: 0.0997 * Error Risk: 81.3068%)
- `pwnlib/context/__init__.py` -> **Severity: 8.092** (Embedded: 0.1252 * Error Risk: 64.6164%)
- `pwnlib/util/fiddling.py` -> **Severity: 7.815** (Embedded: 0.0936 * Error Risk: 83.485%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pwnlib/context/__init__.py` -> **Severity: 1885.629** (Blast Radius: 38.867 * Doc Risk: 48.5149%)
- `pwnlib/log.py` -> **Severity: 1428.895** (Blast Radius: 36.743 * Doc Risk: 38.8889%)
- `pwnlib/util/packing.py` -> **Severity: 1288.053** (Blast Radius: 22.04 * Doc Risk: 58.4416%)
- `pwnlib/timeout.py` -> **Severity: 677.216** (Blast Radius: 9.782 * Doc Risk: 69.2308%)
- `pwnlib/tubes/tube.py` -> **Severity: 648.176** (Blast Radius: 12.591 * Doc Risk: 51.4793%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6624 call pairs -- scoped 34.9%, unique 0.0%, ambiguous 15.2%, external 49.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 6492 | 35.4% | 0.0% | 15.5% | 49.1% |
| shell | 108 | 12.0% | 0.0% | 0.0% | 88.0% |
| c | 15 | 6.7% | 0.0% | 0.0% | 93.3% |
| assembly | 9 | 0.0% | 0.0% | 0.0% | 100.0% |

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
