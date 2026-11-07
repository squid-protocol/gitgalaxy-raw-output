# ARCHITECTURAL_BRIEF: cpm65
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/davidgiven/cpm65.git` |
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
- **Scope:** 214 analyzed artifact(s), 42442 LOC.
- **Load-bearing artifact:** `config.py` -- 12 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tools/cpmemu/biosbdos.c` -- pulls in 12 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `apps/asm.c` at magnitude 1239.08 (structural weight, not risk).
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
| Total Artifacts | 427 |
| Analyzed Artifacts (Scanned) | 214 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 213 |
| Total LOC | 42442 |
| Volatility Index | 0.014 |
| % Scanned of codebase = | 50.1% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7331 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6082 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4696 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 9 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 113 | 29527 | 52.8% |
| C | 35 | 8191 | 16.4% |
| PYTHON | 34 | 2493 | 15.9% |
| CPP | 9 | 1678 | 4.2% |
| LUA | 6 | 228 | 2.8% |
| PLAINTEXT | 5 | 0 | 2.3% |
| MARKDOWN | 4 | 0 | 1.9% |
| SHELL | 4 | 74 | 1.9% |
| YAML | 3 | 236 | 1.4% |
| MAKEFILE | 1 | 15 | 0.5% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 213 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 36%, Declarative / Non-Code 30%, Data / Markup / Trivial 10%, Large Core Modules (3) 7%, Interface Declarations Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 205 | 95.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 4.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 213*

**Composition by Extension & Reason:**
- `.ld`: 29x Unsupported Format (.ld)
- `.txt`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.s`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 59, Signals: 0), 1x Zero-Density Threshold (LOC: 75, Signals: 0)
- `.bas`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 15x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.fnt`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inc`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 53, Signals: 0), 1x Zero-Density Threshold (LOC: 115, Signals: 0)
- `.c`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pas`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.pas')
- `.html`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.6 | 15.8 | 5.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.5 | 35.1 | 50.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 12.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 27.9 | 10.4 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.6 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.8 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 63.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 53 | 19 | 0 | `tools/libbdf.c` |
| cleanup | 33 | 14 | 0 | `tools/libbdf.c` |
| guards | 568 | 43 | 7 | `apps/asm.c` |
| danger | 259 | 52 | 4 | `apps/asm.c` |
| concurrency | 35 | 8 | 0 | `scripts/get-roms.sh` |
| connectivity | 369 | 88 | 4 | `apps/qe.c` |
| io | 101 | 28 | 1 | `tools/multilink.cc` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2 | 2 | 0 | `tools/mkdfs.c` |
| time | 2 | 1 | 0 | `tools/mkimd.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `src/arch/neo6502/build.py` |
| events | 7 | 4 | 0 | `apps/asm.c` |
| tests | 0 | 0 | 0 | - |
| docs | 4 | 2 | 0 | `.github/workflows/ccpp.yml` |
| debt | 143 | 35 | 2 | `tools/cpmemu/emulator.c` |
| mutation | 5283 | 171 | 66 | `apps/asm.c` |
| dead_code | 234 | 89 | 3 | `apps/objdump.c` |
| credential | 1 | 1 | 0 | `scripts/get-roms.sh` |
| threat | 5 | 1 | 0 | `src/arch/atari800/build.py` |
| ml_ai | 8 | 5 | 0 | `tools/cpmemu/biosbdos.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tools/multilink.cc` (Hits: 12)
- `tools/mkimd.c` (Hits: 9)
- `src/arch/nano6502/buildimage.py` (Hits: 9)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **config.py** (`config.py`) — 12 inbound connections
2. **drivers.inc** (`apps/drivers.inc`) — 10 inbound connections
3. **atari800.S** (`src/arch/atari800/atari800.S`) — 9 inbound connections
4. **printi.h** (`lib/printi.h`) — 5 inbound connections
5. **neo6502.h** (`src/arch/neo6502/utils/neo6502.h`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **biosbdos.c** (`tools/cpmemu/biosbdos.c`) — 12 outbound dependencies
2. **fileio.c** (`tools/cpmemu/fileio.c`) — 11 outbound dependencies
3. **xextobin.cc** (`tools/xextobin.cc`) — 10 outbound dependencies
4. **qe.c** (`apps/qe.c`) — 9 outbound dependencies
5. **mkdfs.c** (`tools/mkdfs.c`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ansi_parse` **(Compute Cores)** (@ `apps/ansiterm.c`) -> Impact: **195.3** | LOC: 313
- `bdos_entry` **(Compute Cores)** (@ `tools/cpmemu/biosbdos.c`) -> Impact: **99.7** | LOC: 89
- `consumeToken` **(I/O & Config Routines)** (@ `apps/asm.c`) -> Impact: **84.0** | LOC: 201
- `vt52_parse` **(Compute Cores)** (@ `apps/ansiterm.c`) -> Impact: **79.1** | LOC: 168
- `main` **(I/O & Config Routines)** (@ `apps/ansiterm.c`) -> Impact: **57.6** | LOC: 153
- `consumeExpressionNode` **(Compute Cores)** (@ `apps/asm.c`) -> Impact: **49.0** | LOC: 132
- `colon` **(Compute Cores)** (@ `apps/qe.c`) -> Impact: **49.0** | LOC: 104
- `main` **(Many-Argument Workhorses)** (@ `tools/img2osi.c`) -> Impact: **47.6** | LOC: 120
- `placeCode` **(Compute Cores)** (@ `apps/asm.c`) -> Impact: **46.7** | LOC: 114
- `parseArgs` **(Compute Cores)** (@ `tools/mkoricdsk.cc`) -> Impact: **42.4** | LOC: 52

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `apps` | 33 | 5443.4 | 33.23% | 13.8% |
| `src/arch/snes` | 7 | 425.74 | 11.17% | 17.68% |
| `src/arch/neo6502/utils` | 7 | 358.9 | 47.64% | 27.93% |
| `src/arch/nano6502` | 4 | 316.32 | 33.44% | 3.17% |
| `src/bdos` | 11 | 244.36 | 2.19% | 7.3% |
| `src/arch/kim-1` | 12 | 202.8 | 3.74% | 4.85% |
| `src/arch/atari800` | 4 | 181.42 | 4.58% | 6.35% |
| `src/arch/kim-1/boot` | 5 | 175.18 | 5.82% | 72.58% |
| `lib` | 9 | 162.64 | 0.77% | 8.14% |
| `src/arch/commodore/diskaccess` | 12 | 157.56 | 1.25% | 10.69% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/arch/kim-1/boot/bootsd.S` -> **99.9776%** Exposure
- `src/arch/snes/loader.S` -> **99.9349%** Exposure
- `src/arch/neo6502/utils/neo6502.c` -> **97.0688%** Exposure
- `apps/objdump.c` -> **93.8571%** Exposure
- `src/arch/kim-1/boot/bootsdshield.S` -> **91.3168%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `apps/cpm65.inc` -> **100.0%** Exposure
- `apps/drivers.inc` -> **100.0%** Exposure
- `apps/ansiterm.c` -> **100.0%** Exposure
- `apps/attr.c` -> **100.0%** Exposure
- `apps/copy.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/arch/snes/main.asm` -> **13** Orphaned Functions | **2** Duplicates
- `apps/objdump.c` -> **15** Orphaned Functions | **0** Duplicates
- `src/arch/kim-1/boot/bootsd.S` -> **10** Orphaned Functions | **2** Duplicates
- `tools/cpmemu/fileio.c` -> **11** Orphaned Functions | **0** Duplicates
- `src/arch/oric/oric.S` -> **7** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `357` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `apps/asm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.261)
- **Top Global Matches:** file_cluster_4: 6.261, file_cluster_16: 9.644, file_cluster_12: 10.87
- **Magnitude:** 1239.08 | **LOC:** 2139 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 3.756; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `consumeToken` **(I/O & Config Routines)** (Impact: 84.0)
  * `consumeExpressionNode` **(Compute Cores)** (Impact: 49.0)
  * `placeCode` **(Compute Cores)** (Impact: 46.7)
  * `parse` **(I/O & Config Routines)** (Impact: 36.5)
  * `consumeArgument` **(I/O & Config Routines)** (Impact: 31.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 195 instances
* *State Mutation (weighted view):* 617
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 212`, `args: 50`, `func_start: 78`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 227`, `unreferenced_by_name: 2`
* *Architecture:* `api: 11`, `import: 8`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cpm.h, ctype.h, printi.h, stdbool.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/qe.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.152)
- **Top Global Matches:** file_cluster_4: 7.152, file_cluster_12: 7.305, file_cluster_15: 7.783
- **Magnitude:** 983.2 | **LOC:** 1241 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.756; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.4%), Complexity Load (formerly Cognitive Load) (72.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `colon` **(Compute Cores)** (Impact: 49.0)
  * `main` **(Many-Argument Workhorses)** (Impact: 28.7)
    * *Intent:* /* ======================================================================= */ /* EDITOR OPERATIONS *...
  * `insert_mode` **(Compute Cores)** (Impact: 24.8)
  * `draw_line` **(Compute Cores)** (Impact: 22.9)
  * `compute_length` **(Many-Argument Workhorses)** (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 157 instances
* *State Mutation (weighted view):* 488
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 156`, `args: 63`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 174`, `unreferenced_by_name: 2`
* *Architecture:* `api: 63`, `import: 9`
* *Defense:* `safety: 2`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cpm.h, ctype.h, screen.h, limits.h, stdbool.h, stdint.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ansiterm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.748)
- **Top Global Matches:** file_cluster_8: 6.748, file_cluster_6: 17.186, file_cluster_3: 20.027
- **Magnitude:** 881.6 | **LOC:** 952 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.756; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.7%), Guard Balance (formerly Safety Score) (78.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ansi_parse` **(Compute Cores)** (Impact: 195.3)
  * `vt52_parse` **(Compute Cores)** (Impact: 79.1)
  * `main` **(I/O & Config Routines)** (Impact: 57.6)
  * `xmodem_receive` **(I/O & Config Routines)** (Impact: 17.6)
  * `xmodem_send` **(I/O & Config Routines)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 161 instances
* *State Mutation (weighted view):* 488
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 98`, `args: 18`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 166`, `dead_code: 1`, `planned_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` cpm.h, printi.h, screen.h, serial.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/stat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.687)
- **Top Global Matches:** file_cluster_4: 6.687, file_cluster_15: 7.705, file_cluster_12: 8.205
- **Magnitude:** 396.98 | **LOC:** 655 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 3.756; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.1%), Complexity Load (formerly Cognitive Load) (67.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `file_manipulation` **(I/O & Config Routines)** (Impact: 41.3)
  * `scan` **(I/O & Config Routines)** (Impact: 15.7)
    * *Intent:* /* Reads the next input token into the 4-byte accumulator. */
  * `device_manipulation` **(I/O & Config Routines)** (Impact: 14.6)
    * *Intent:* /* Handle device assignment, querying, and miscellaneous other things */
  * `compare_accumulator` **(Compute Cores)** (Impact: 9.8)
    * *Intent:* /* Compares the accumulator with an array of uint8_t[4] words. Returns the * matching index plus one...
  * `set_drive_status` **(I/O & Config Routines)** (Impact: 8.3)
    * *Intent:* /* Handles the A:=R/O and A: DSK: cases. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 82`, `args: 24`, `func_start: 23`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 76`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 24`, `import: 7`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cpm.h, printi.h, stdbool.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/objdump.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.818)
- **Top Global Matches:** file_cluster_16: 5.818, file_cluster_4: 8.184, file_cluster_15: 8.546
- **Magnitude:** 227.34 | **LOC:** 343 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 3.756; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (93.9%), Complexity Load (formerly Cognitive Load) (88.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 38.7)
  * `getrelo` **(Stateful Encapsulated Methods)** (Impact: 6.4)
  * `print` **(Stateful Encapsulated Methods)** (Impact: 4.7)
  * `os` **(Stateful Encapsulated Methods)** (Impact: 4.7)
  * `oh1` **(Stateful Encapsulated Methods)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 37`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 47`, `unreferenced_by_name: 15`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 6502data.h, cpm.h, stdbool.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/snes/main.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.503)
- **Top Global Matches:** file_cluster_2: 6.503, file_cluster_15: 7.547, file_cluster_11: 7.82
- **Magnitude:** 217.84 | **LOC:** 1764 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 8.279; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.7%), Debt Markers (formerly Tech Debt) (23.8%), Mutation Surface (formerly State Flux) (13.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_current_key` **(I/O & Config Routines)** (Impact: 9.3)
  * `tty_conout` **(I/O & Config Routines)** (Impact: 6.0)
  * `load_font_data` **(I/O & Config Routines)** (Impact: 4.5)
  * `fd_wait_until_drive_ready` **(I/O & Config Routines)** (Impact: 3.8)
  * `loop` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 19`, `func_start: 94`
* *Risk/State:* `state_mutation: 7`, `duplicate_logic: 2`, `unreferenced_by_name: 13`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.279
  * `Choke Point (Betweenness):` 8.5e-05 | `Ripple Effect (Closeness):` 0.018433
  * `Imports (Out-Degree: 1):` snes.inc
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `apps/sys.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.501)
- **Top Global Matches:** file_cluster_4: 5.501, file_cluster_16: 9.745, file_cluster_15: 10.631
- **Magnitude:** 195.22 | **LOC:** 315 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.756; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copy_file` **(I/O & Config Routines)** (Impact: 20.1)
  * `copy_reserved_sectors` **(I/O & Config Routines)** (Impact: 13.1)
  * `main` **(I/O & Config Routines)** (Impact: 12.4)
  * `print_filename` **(Stateful Encapsulated Methods)** (Impact: 6.5)
  * `copy_system_files` **(I/O & Config Routines)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 22`, `args: 11`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 40`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cpm.h, stdbool.h, stdint.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/copy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.67)
- **Top Global Matches:** file_cluster_6: 8.67, file_cluster_4: 8.988, file_cluster_16: 14.925
- **Magnitude:** 180.82 | **LOC:** 251 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.756; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.8%), Complexity Load (formerly Cognitive Load) (70.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 20.4)
  * `copy_file` **(I/O & Config Routines)** (Impact: 12.7)
  * `print_fcb` **(Stateful Encapsulated Methods)** (Impact: 11.3)
  * `parse_cmdline` **(I/O & Config Routines)** (Impact: 10.4)
  * `getword` **(Stateful Encapsulated Methods)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 22`, `args: 5`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 35`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cpm.h, stdbool.h, stdint.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/life.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.719)
- **Top Global Matches:** file_cluster_8: 8.719, file_cluster_6: 10.427, file_cluster_4: 18.336
- **Magnitude:** 170.5 | **LOC:** 168 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.756; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 34.1)
  * `life` **(I/O & Config Routines)** (Impact: 14.6)
  * `fatal` **(Encapsulated Accessors)** (Impact: 1.8)
  * `cr` **(Encapsulated Accessors)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 14`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 40`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cpm.h, printi.h, screen.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/submit.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.999)
- **Top Global Matches:** file_cluster_4: 6.999, file_cluster_6: 7.506, file_cluster_16: 13.142
- **Magnitude:** 165.22 | **LOC:** 220 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.756; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.3%), Guard Balance (formerly Safety Score) (69.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_byte` **(Stateful Encapsulated Methods)** (Impact: 28.8)
  * `main` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `printi` **(Stateful Encapsulated Methods)** (Impact: 7.9)
  * `printn` **(Compute Cores)** (Impact: 5.7)
  * `fatal` **(Stateful Encapsulated Methods)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 23`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 27`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cpm.h, ctype.h, stdbool.h, stdint.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/atari800/atari800.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.959)
- **Top Global Matches:** file_cluster_2: 5.959, file_cluster_15: 6.714, file_cluster_11: 6.843
- **Magnitude:** 131.48 | **LOC:** 1337 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); blast radius 20.789; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.9%), Mutation Surface (formerly State Flux) (27.5%), Debt Markers (formerly Tech Debt) (25.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `screen_jmptable_hi` **(I/O & Config Routines)** (Impact: 16.1)
  * `key_down` **(Compute Cores)** (Impact: 6.5)
  * `clok_done` **(I/O & Config Routines)** (Impact: 4.3)
  * `KIR` **(I/O & Config Routines)** (Impact: 3.4)
  * `IVNM` **(Interface Declarations)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 22`, `args: 8`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 20`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 20.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.043693
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `apps/cpm65.inc` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.604)
- **Top Global Matches:** file_cluster_2: 2.604, file_cluster_17: 5.341, file_cluster_15: 6.406
- **Magnitude:** 117.92 | **LOC:** 105 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.1%), Complexity Load (formerly Cognitive Load) (51.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* `state_mutation: 91`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/nano6502/buildimage.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.896)
- **Top Global Matches:** file_cluster_2: 3.896, file_cluster_17: 5.888, file_cluster_15: 6.623
- **Magnitude:** 111.44 | **LOC:** 118 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.756; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.7%), Complexity Load (formerly Cognitive Load) (64.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 35`
* *Architecture:* `io: 9`, `import: 2`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bdos/filesystem.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.127)
- **Top Global Matches:** file_cluster_2: 6.127, file_cluster_11: 6.584, file_cluster_15: 7.243
- **Magnitude:** 105.58 | **LOC:** 1868 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.6%), Mutation Surface (formerly State Flux) (12.5%), Debt Markers (formerly Tech Debt) (9.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_first` **(I/O & Config Routines)** (Impact: 8.6)
  * `merge_error` **(I/O & Config Routines)** (Impact: 7.0)
  * `error$` **(I/O & Config Routines)** (Impact: 6.0)
  * `no_more_files` **(I/O & Config Routines)** (Impact: 5.0)
  * `eof` **(I/O & Config Routines)** (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 31`, `func_start: 26`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/mkfs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.865)
- **Top Global Matches:** file_cluster_16: 5.865, file_cluster_15: 6.347, file_cluster_12: 7.087
- **Magnitude:** 104.16 | **LOC:** 171 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.756; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.0%), Guard Balance (formerly Safety Score) (65.9%), Debt Markers (formerly Tech Debt) (25.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printip` **(Compute Cores)** (Impact: 15.0)
    * *Intent:* /* * Prints a 32-bit decimal number with optional left padding and configurable * precision. *. */
  * `main` **(I/O & Config Routines)** (Impact: 11.4)
  * `print` **(Stateful Encapsulated Methods)** (Impact: 4.7)
  * `printhex4` **(Compute Cores)** (Impact: 4.7)
  * `printx` **(Encapsulated Accessors)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 18`, `args: 11`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `unreferenced_by_name: 2`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cpm.h, stdbool.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/snes/checksum.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.139)
- **Top Global Matches:** file_cluster_9: 8.139, file_cluster_11: 9.288, file_cluster_15: 9.323
- **Magnitude:** 104.06 | **LOC:** 84 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 3.756; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.3%), Complexity Load (formerly Cognitive Load) (71.9%), Connectivity (formerly Api Exposure) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checksum` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* # applies the SNES checksum to a ROM # usage: # checksum.py LOROM filein [fileout] # checksum.py HIR...
  * `usage` **(Interface Declarations)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 5`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 26`
* *Architecture:* `io: 5`, `api: 2`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/neo6502/utils/nattr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.618)
- **Top Global Matches:** file_cluster_8: 6.618, file_cluster_6: 17.107, file_cluster_3: 20.119
- **Magnitude:** 102.58 | **LOC:** 121 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.756; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.8%), Guard Balance (formerly Safety Score) (68.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 39.6)
  * `setattrs` **(Stateful Encapsulated Methods)** (Impact: 8.1)
  * `getattrs` **(Stateful Encapsulated Methods)** (Impact: 6.9)
    * *Intent:* #include <stdio.h> #include <stdlib.h> #include <string.h> #include <cpm.h> #include "neo6502.h"
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 6`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cpm.h, neo6502.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/neo6502/neo6502.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.829)
- **Top Global Matches:** file_cluster_2: 5.829, file_cluster_15: 7.137, file_cluster_13: 7.603
- **Magnitude:** 102.32 | **LOC:** 1708 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.7%), Mutation Surface (formerly State Flux) (14.3%), Debt Markers (formerly Tech Debt) (10.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `delete_exit` **(I/O & Config Routines)** (Impact: 13.5)
  * `bdos_WRITERANDOMFILLED` **(I/O & Config Routines)** (Impact: 8.8)
  * `internal_READSEQUENTIAL` **(I/O & Config Routines)** (Impact: 4.9)
  * `screen_jmptable_hi` **(I/O & Config Routines)** (Impact: 3.5)
  * `_start` **(I/O & Config Routines)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 35`, `args: 1`, `func_start: 17`
* *Risk/State:* `state_mutation: 17`, `unreferenced_by_name: 5`
* *Architecture:* `api: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/attr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.486)
- **Top Global Matches:** file_cluster_8: 8.486, file_cluster_6: 18.018, file_cluster_3: 20.576
- **Magnitude:** 101.44 | **LOC:** 144 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 3.756; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.2%), Complexity Load (formerly Cognitive Load) (70.9%), Debt Markers (formerly Tech Debt) (16.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 23.2)
  * `print_filename` **(Stateful Encapsulated Methods)** (Impact: 7.7)
  * `getword` **(Stateful Encapsulated Methods)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 11`, `args: 1`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 20`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cpm.h, ctype.h, printi.h, stdbool.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/nano6502/nano6502.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.68)
- **Top Global Matches:** file_cluster_2: 5.68, file_cluster_11: 6.128, file_cluster_15: 7.007
- **Magnitude:** 98.08 | **LOC:** 1143 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.6%), Mutation Surface (formerly State Flux) (13.0%), Debt Markers (formerly Tech Debt) (12.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `banner_wait` **(I/O & Config Routines)** (Impact: 6.5)
  * `screen_getchar_data` **(I/O & Config Routines)** (Impact: 4.8)
  * `screen_getchar_wait` **(I/O & Config Routines)** (Impact: 4.7)
  * `jmptable_hi` **(I/O & Config Routines)** (Impact: 4.0)
  * `wait_serial_in` **(I/O & Config Routines)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 18`, `func_start: 29`
* *Risk/State:* `state_mutation: 9`, `unreferenced_by_name: 5`
* *Architecture:* `api: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/drivers.inc` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.405)
- **Top Global Matches:** file_cluster_2: 3.405, file_cluster_17: 5.801, file_cluster_15: 6.68
- **Magnitude:** 90.72 | **LOC:** 44 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); blast radius 35.682; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.5%), Complexity Load (formerly Cognitive Load) (56.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 35.682
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.046083
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/arch/oric/oric.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.465)
- **Top Global Matches:** file_cluster_2: 5.465, file_cluster_15: 6.995, file_cluster_17: 7.316
- **Magnitude:** 90.48 | **LOC:** 1521 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.6%), Debt Markers (formerly Tech Debt) (20.3%), Mutation Surface (formerly State Flux) (13.0%), Complexity Load (formerly Cognitive Load) (5.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jmptable_hi` **(I/O & Config Routines)** (Impact: 7.5)
  * `screen_jmptable_hi` **(I/O & Config Routines)** (Impact: 7.0)
  * `sector2_start` **(I/O & Config Routines)** (Impact: 6.3)
  * `jasmin_start` **(I/O & Config Routines)** (Impact: 4.4)
    * *Intent:* ; Jasmin boot code starts here.
  * `banner_end` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 28`, `args: 4`, `func_start: 18`
* *Risk/State:* `state_mutation: 10`, `fragile_debt: 1`, `unreferenced_by_name: 7`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ls.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.404)
- **Top Global Matches:** file_cluster_2: 5.404, file_cluster_11: 6.38, file_cluster_15: 6.678
- **Magnitude:** 90.38 | **LOC:** 608 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 3.756; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (34.0%), Debt Markers (formerly Tech Debt) (15.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `no_fill_wildcards` **(I/O & Config Routines)** (Impact: 5.5)
  * `no_archived` **(I/O & Config Routines)** (Impact: 5.0)
  * `mul128` **(I/O & Config Routines)** (Impact: 4.7)
  * `test_nfiles` **(I/O & Config Routines)** (Impact: 3.5)
  * `jloop` **(I/O & Config Routines)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 24`, `func_start: 28`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 4`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cpm65.inc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/nano6502/buildsysimage.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.843)
- **Top Global Matches:** file_cluster_2: 3.843, file_cluster_17: 5.821, file_cluster_15: 6.571
- **Magnitude:** 90.18 | **LOC:** 98 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.756; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.7%), Complexity Load (formerly Cognitive Load) (63.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 28`
* *Architecture:* `io: 7`, `import: 2`
* *Defense:* `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/kim-1/boot/bootsd.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.894)
- **Top Global Matches:** file_cluster_2: 5.894, file_cluster_11: 6.248, file_cluster_15: 6.874
- **Magnitude:** 88.84 | **LOC:** 409 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (83.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sd_readsector` **(I/O & Config Routines)** (Impact: 5.2)
  * `ram_start` **(I/O & Config Routines)** (Impact: 4.3)
  * `_delayloop` **(I/O & Config Routines)** (Impact: 4.3)
  * `e1` **(I/O & Config Routines)** (Impact: 3.9)
  * `_cmd41` **(I/O & Config Routines)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 10`, `func_start: 26`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 9`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.756
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/bdos/exit.S` (ASSEMBLY) | Magnitude: 5.92 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 108, structural_boundaries: 3, func_start: 2, state_mutation: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tools/cpmemu/fileio.c` (C) | Magnitude: 0.31 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 308, pointers: 105, structural_boundaries: 72, branch: 66
- `src/arch/kim-1/boot/build.py` (PYTHON) | Magnitude: 4.62 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, core_var_decl: 30, design_snake_case: 29, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `apps/vt52drv.asm` (ASSEMBLY) | Magnitude: 36.96 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 351, structural_boundaries: 39, state_mutation: 13, bitwise_ops: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/arch/commodore/pet.S` -> **nick-less** (100.0% isolated ownership) | Magnitude: 79.42

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/arch/neo6502/utils/ntrunc.c` -> **Severity: 0.04** (Bridge: 0.0004 * Flux: 100.0%)
- `tools/cpmemu/biosbdos.c` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 99.986%)
- `tools/cpmemu/emulator.c` -> **Severity: 0.019** (Bridge: 0.0002 * Flux: 99.9994%)
- `tools/cpmemu/fileio.c` -> **Severity: 0.014** (Bridge: 0.0001 * Flux: 99.9993%)
- `src/arch/neo6502/utils/ndir.c` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `apps/drivers.inc` -> **Severity: 4.124** (Embedded: 0.0461 * Error Risk: 89.4999%)
- `config.py` -> **Severity: 3.236** (Embedded: 0.0553 * Error Risk: 58.5183%)
- `src/arch/atari800/atari800.S` -> **Severity: 2.268** (Embedded: 0.0437 * Error Risk: 51.9083%)
- `src/arch/neo6502/utils/neo6502.c` -> **Severity: 1.373** (Embedded: 0.0219 * Error Risk: 62.5811%)
- `src/arch/neo6502/utils/ntrunc.c` -> **Severity: 1.302** (Embedded: 0.0205 * Error Risk: 63.4136%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/arch/atari800/atari800.S` -> **Severity: 2078.9** (Blast Radius: 20.789 * Doc Risk: 100.0%)
- `src/arch/neo6502/utils/ntrunc.c` -> **Severity: 1334.1** (Blast Radius: 13.341 * Doc Risk: 100.0%)
- `src/arch/neo6502/utils/neo6502.c` -> **Severity: 1014.7** (Blast Radius: 10.147 * Doc Risk: 100.0%)
- `tools/cpmemu/emulator.c` -> **Severity: 868.2** (Blast Radius: 8.682 * Doc Risk: 100.0%)
- `src/arch/snes/main.asm` -> **Severity: 827.9** (Blast Radius: 8.279 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 78 literal sites + 4 sites through wrappers = 82

- `syntaxError` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `tools/mkcombifs.cc`
- `syntaxError` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `tools/multilink.cc`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1612 call pairs -- scoped 35.3%, unique 8.6%, ambiguous 5.8%, external 50.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 1230 | 43.0% | 11.2% | 4.3% | 41.5% |
| cpp | 161 | 17.4% | 0.6% | 9.9% | 72.0% |
| python | 138 | 3.6% | 0.0% | 18.1% | 78.3% |
| lua | 72 | 8.3% | 0.0% | 0.0% | 91.7% |
| shell | 11 | 9.1% | 0.0% | 0.0% | 90.9% |

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
