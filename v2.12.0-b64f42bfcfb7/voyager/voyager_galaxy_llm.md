# ARCHITECTURAL_BRIEF: voyager
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Zaneham/voyager-fds-emulator.git` |
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
- **Scope:** 6 analyzed artifact(s), 1865 LOC.
- **Load-bearing artifact:** `include/fds.h` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/fds_asm.c` -- pulls in 5 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/fds_cpu.c` at magnitude 1065.3 (structural weight, not risk).
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
| Total Artifacts | 16 |
| Analyzed Artifacts (Scanned) | 6 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10 |
| Total LOC | 1865 |
| Volatility Index | 0.333 |
| % Scanned of codebase = | 37.5% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6667 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 4 | 1834 | 66.7% |
| MAKEFILE | 1 | 31 | 16.7% |
| MARKDOWN | 1 | 0 | 16.7% |

## 4.1 SOURCE ENCODINGS
All 6 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Compute Cores Files 33%, Data / Markup / Trivial 17%, Declarative / Non-Code 17%, Large Core Modules (3) 17%, State Mutators Files 17%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 5 | 83.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 16.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10*

**Composition by Extension & Reason:**
- `.fds`: 4x Excluded (Unsupported Extension: '.fds')
- `.pdf`: 3x Excluded (Explicitly Denied Extension: '.pdf')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.5 | 45.6 | 52.9 | 9.3 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 70.9 | 50.7 | 61.5 | 54.3 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 81.8 | 30.6 | 19.3 | 81.8 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 48.9 | 80.0 | 80.0 |
| Connectivity (formerly API Exposure) | 0.3 | 79.7 | 19.8 | 7.2 | 8.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 78.3 | 99.9 | 91.7 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 100.0 | 78.6 | 97.7 | 97.7 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 43.1 | 100.0 | 73.1 | 68.3 | 68.3 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 70.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5 | 2 | 1 | `src/fds_asm.c` |
| cleanup | 7 | 4 | 1 | `src/fds_asm.c` |
| guards | 114 | 4 | 40 | `src/fds_cpu.c` |
| danger | 25 | 3 | 9 | `src/fds_asm.c` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 87 | 5 | 25 | `include/fds.h` |
| io | 17 | 4 | 4 | `src/fds_cpu.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `Makefile` |
| events | 0 | 0 | 0 | - |
| tests | 2 | 1 | 0 | `src/main.c` |
| docs | 0 | 0 | 0 | - |
| debt | 77 | 4 | 9 | `src/main.c` |
| mutation | 487 | 5 | 103 | `src/fds_cpu.c` |
| dead_code | 23 | 4 | 3 | `src/fds_cpu.c` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 1 | 1 | 0 | `src/fds_asm.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.8**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.65**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/fds_cpu.c` (Hits: 8)
- `src/fds_asm.c` (Hits: 4)
- `src/main.c` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **fds.h** (`include/fds.h`) — 3 inbound connections
2. **fds_asm.c** (`src/fds_asm.c`) — 1 inbound connections
3. **fds_cpu.c** (`src/fds_cpu.c`) — 1 inbound connections
4. **Makefile** (`Makefile`) — 0 inbound connections
5. **README.md** (`README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **fds_asm.c** (`src/fds_asm.c`) — 5 outbound dependencies
2. **main.c** (`src/main.c`) — 4 outbound dependencies
3. **fds_cpu.c** (`src/fds_cpu.c`) — 3 outbound dependencies
4. **fds.h** (`include/fds.h`) — 2 outbound dependencies
5. **README.md** (`README.md`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `fds_cpu_step` **(Many-Argument Workhorses)** (@ `src/fds_cpu.c`) -> Impact: **224.2** | LOC: 570
  * *Intent:* /* ============================================================================ * INSTRUCTION EXECUTION * ============================================...
- `fds_disassemble` **(Many-Argument Workhorses)** (@ `src/fds_cpu.c`) -> Impact: **146.9** | LOC: 179
  * *Intent:* /* Disassemble a single instruction */
- `assemble_line` **(Many-Argument Workhorses)** (@ `src/fds_asm.c`) -> Impact: **93.5** | LOC: 207
  * *Intent:* /* ============================================================================ * ASSEMBLER CORE * ===================================================...
- `main` **(Compute Cores)** (@ `src/main.c`) -> Impact: **68.5** | LOC: 122
- `run_interactive` **(Compute Cores)** (@ `src/main.c`) -> Impact: **35.4** | LOC: 58
- `parse_number` **(Stateful Encapsulated Methods)** (@ `src/fds_asm.c`) -> Impact: **32.0** | LOC: 40
  * *Intent:* /* Parse number (hex or decimal) */
- `run_test_program` **(Many-Argument Workhorses)** (@ `src/main.c`) -> Impact: **29.4** | LOC: 68
- `fds_dma_service` **(Compute Cores)** (@ `src/fds_cpu.c`) -> Impact: **28.1** | LOC: 42
  * *Intent:* /* * Service pending DMA requests. * Called during instruction execution "access windows". * Processes channels in priority order (0 = highest). */
- `fds_assemble` **(Compute Cores)** (@ `src/fds_asm.c`) -> Impact: **23.5** | LOC: 55
  * *Intent:* /* ============================================================================ * PUBLIC API * =======================================================...
- `fds_cpu_run` **(Many-Argument Workhorses)** (@ `src/fds_cpu.c`) -> Impact: **20.0** | LOC: 40
  * *Intent:* /* Run for up to max_cycles, or until halted */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 3 | 1711.24 | 72.84% | 23.77% |
| `include` | 1 | 67.14 | 0.0% | 0.0% |
| `__monolith__` | 2 | 20.58 | 4.63% | 40.88% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Makefile` -> **81.7574%** Exposure
- `src/fds_cpu.c` -> **38.3152%** Exposure
- `src/main.c` -> **19.3321%** Exposure
- `src/fds_asm.c` -> **13.6633%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/fds_cpu.c` -> **100.0%** Exposure
- `src/fds_asm.c` -> **99.9995%** Exposure
- `src/main.c` -> **99.9423%** Exposure
- `Makefile` -> **91.6827%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/fds_cpu.c` -> **17** Orphaned Functions | **0** Duplicates
- `src/fds_asm.c` -> **3** Orphaned Functions | **0** Duplicates
- `Makefile` -> **2** Orphaned Functions | **0** Duplicates
- `src/main.c` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `12` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/fds_cpu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.179)
- **Top Global Matches:** file_cluster_4: 5.179, file_cluster_16: 8.972, file_cluster_15: 9.037
- **Magnitude:** 1065.3 | **LOC:** 1206 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 142.093; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (97.7%), Complexity Load (formerly Cognitive Load) (94.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fds_cpu_step` **(Many-Argument Workhorses)** (Impact: 224.2)
    * *Intent:* /* ============================================================================ * INSTRUCTION EXECUT...
  * `fds_disassemble` **(Many-Argument Workhorses)** (Impact: 146.9)
    * *Intent:* /* Disassemble a single instruction */
  * `fds_dma_service` **(Compute Cores)** (Impact: 28.1)
    * *Intent:* /* * Service pending DMA requests. * Called during instruction execution "access windows". * Process...
  * `fds_cpu_run` **(Many-Argument Workhorses)** (Impact: 20.0)
    * *Intent:* /* Run for up to max_cycles, or until halted */
  * `fds_load_file` **(Many-Argument Workhorses)** (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 146 instances
* *State Mutation (weighted view):* 455
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 164`, `args: 36`, `func_start: 31`
* *Risk/State:* `state_mutation: 163`, `unreferenced_by_name: 17`
* *Architecture:* `io: 8`, `api: 25`, `import: 3`
* *Defense:* `safety: 36`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 142.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.2
  * `Imports (Out-Degree: 1):` fds.h, stdio.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/fds_asm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.371)
- **Top Global Matches:** file_cluster_4: 5.371, file_cluster_16: 9.372, file_cluster_15: 10.823
- **Magnitude:** 421.74 | **LOC:** 701 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 142.093; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (97.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assemble_line` **(Many-Argument Workhorses)** (Impact: 93.5)
    * *Intent:* /* ============================================================================ * ASSEMBLER CORE * =...
  * `parse_number` **(Stateful Encapsulated Methods)** (Impact: 32.0)
    * *Intent:* /* Parse number (hex or decimal) */
  * `fds_assemble` **(Compute Cores)** (Impact: 23.5)
    * *Intent:* /* ============================================================================ * PUBLIC API * =====...
  * `fds_asm_error_str` **(Compute Cores)** (Impact: 16.3)
  * `add_label` **(Stateful Encapsulated Methods)** (Impact: 12.7)
    * *Intent:* /* Add or update label */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 57 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 90`, `args: 18`, `func_start: 13`, `class_start: 6`
* *Risk/State:* `state_mutation: 65`, `unreferenced_by_name: 3`
* *Architecture:* `io: 4`, `api: 10`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 23`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 142.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.2
  * `Imports (Out-Degree: 1):` fds.h, ctype.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.285)
- **Top Global Matches:** file_cluster_8: 6.285, file_cluster_6: 17.063, file_cluster_3: 19.89
- **Magnitude:** 224.2 | **LOC:** 354 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 110.722; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (97.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 68.5)
  * `run_interactive` **(Compute Cores)** (Impact: 35.4)
  * `run_test_program` **(Many-Argument Workhorses)** (Impact: 29.4)
  * `write_binary` **(Stateful Encapsulated Methods)** (Impact: 6.1)
    * *Intent:* /* Write assembled program to binary file */
  * `print_listing` **(Stateful Encapsulated Methods)** (Impact: 3.7)
    * *Intent:* /* Print assembled listing */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 37`, `args: 7`, `func_start: 6`
* *Risk/State:* `state_mutation: 28`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 4`
* *Defense:* `test: 2`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 110.722
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` fds.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `include/fds.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 2.593)
- **Top Global Matches:** file_cluster_17: 2.593, file_cluster_2: 5.342, file_cluster_15: 6.268
- **Magnitude:** 67.14 | **LOC:** 494 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 383.65; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Connectivity (formerly Api Exposure) (79.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 66`, `args: 30`, `class_start: 15`
* *Risk/State:* None
* *Architecture:* `api: 47`, `import: 2`
* *Defense:* `safety: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 383.65
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.6
  * `Imports (Out-Degree: 0):` stdbool.h, stdint.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.646)
- **Top Global Matches:** file_cluster_2: 6.646, file_cluster_13: 7.632, file_cluster_15: 7.732
- **Magnitude:** 16.52 | **LOC:** 56 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (100.0%), Mutation Surface (formerly State Flux) (91.7%), Debt Markers (formerly Tech Debt) (81.8%), Guard Balance (formerly Safety Score) (54.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `all` **(I/O & Config Routines)** (Impact: 1.5)
  * `test` **(State Mutators)** (Impact: 1.1)
  * `clean` **(State Mutators)** (Impact: 1.1)
  * `step` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* # Run with step mode
  * `disasm` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* # Disassemble a binary file
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 11`, `func_start: 5`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 110.722
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 4.06 | **LOC:** 203 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 110.722; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 110.722
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LICENSE
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/fds_cpu.c` -> Churn: **86.14%** | Cog Load: 94.5342% | Debt: 38.3152%
- `src/fds_asm.c` -> Churn: **68.26%** | Cog Load: 71.1264% | Debt: 13.6633%
- `src/main.c` -> Churn: **68.26%** | Cog Load: 52.854% | Debt: 19.3321%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/fds_cpu.c` -> **ZaneHam** (100.0% isolated ownership) | Magnitude: 1065.3
- `src/fds_asm.c` -> **ZaneHam** (100.0% isolated ownership) | Magnitude: 421.74
- `src/main.c` -> **ZaneHam** (100.0% isolated ownership) | Magnitude: 224.2

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/fds_cpu.c` -> **Severity: 14.181** (Embedded: 0.2 * Error Risk: 70.9034%)
- `src/fds_asm.c` -> **Severity: 13.327** (Embedded: 0.2 * Error Risk: 66.6373%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/fds_asm.c` -> **Severity: 14209.3** (Blast Radius: 142.093 * Doc Risk: 100.0%)
- `src/fds_cpu.c` -> **Severity: 14209.3** (Blast Radius: 142.093 * Doc Risk: 100.0%)
- `src/main.c` -> **Severity: 11072.2** (Blast Radius: 110.722 * Doc Risk: 100.0%)
- `Makefile` -> **Severity: 5536.1** (Blast Radius: 110.722 * Doc Risk: 50.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`memory_alloc`:** 4 literal sites + 2 sites through wrappers = 6

- `fds_program_free` (function, memory_alloc, primitive): 2 call sites in 1 files -- `src/fds_asm.c`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 110 call pairs -- scoped 34.5%, unique 18.2%, ambiguous 0.0%, external 47.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 110 | 34.5% | 18.2% | 0.0% | 47.3% |

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
