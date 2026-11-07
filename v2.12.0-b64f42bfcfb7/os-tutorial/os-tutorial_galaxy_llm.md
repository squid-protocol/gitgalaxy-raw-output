# ARCHITECTURAL_BRIEF: os-tutorial
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cfenollosa/os-tutorial.git` |
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
- **Scope:** 219 analyzed artifact(s), 6676 LOC.
- **Load-bearing artifact:** `22-malloc/cpu/type.h` -- 8 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `23-fixes/drivers/keyboard.c` -- pulls in 8 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `23-fixes/drivers/screen.c` at magnitude 165.14 (structural weight, not risk).
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
| Total Artifacts | 228 |
| Analyzed Artifacts (Scanned) | 219 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9 |
| Total LOC | 6676 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 96.1% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8513 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2975 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.1783 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 22 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 117 | 3331 | 53.4% |
| ASSEMBLY | 64 | 3040 | 29.2% |
| MARKDOWN | 26 | 0 | 11.9% |
| MAKEFILE | 12 | 305 | 5.5% |

## 4.1 SOURCE ENCODINGS
All 219 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 33%, Data / Markup / Trivial 29%, Declarative / Non-Code 19%, Large Core Modules 7%, Interface Declarations Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 193 | 88.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 26 | 11.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9*

**Composition by Extension & Reason:**
- `.asm`: 7x Statistical Anomaly (Z-Score: -8.42 < -4.75)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 61.0 | 5.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 85.1 | 17.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 31.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 7.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 25.1 | 11.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 28.2 | 1.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.3 | 75.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3 | 3 | 0 | `21-shell/drivers/keyboard.c` |
| cleanup | 22 | 11 | 0 | `14-checkpoint/Makefile` |
| guards | 40 | 24 | 1 | `21-shell/drivers/keyboard.c` |
| danger | 299 | 46 | 1 | `19-interrupts-irqs/cpu/interrupt.asm` |
| concurrency | 11 | 11 | 0 | `14-checkpoint/Makefile` |
| connectivity | 1067 | 167 | 7 | `21-shell/cpu/isr.h` |
| io | 35 | 12 | 0 | `14-checkpoint/Makefile` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 125 | 47 | 3 | `03-bootsector-memory/boot_sect_memory.asm` |
| tests | 0 | 0 | 0 | - |
| docs | 43 | 22 | 0 | `16-video-driver/drivers/screen.c` |
| debt | 6 | 3 | 0 | `17-video-scroll/kernel/util.c` |
| mutation | 649 | 55 | 7 | `21-shell/drivers/screen.c` |
| dead_code | 450 | 88 | 3 | `19-interrupts-irqs/cpu/interrupt.asm` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 7 | 4 | 0 | `21-shell/drivers/keyboard.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `14-checkpoint/Makefile` (Hits: 3)
- `15-video-ports/Makefile` (Hits: 3)
- `16-video-driver/Makefile` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **type.h** (`22-malloc/cpu/type.h`) — 8 inbound connections
2. **types.h** (`21-shell/cpu/types.h`) — 7 inbound connections
3. **util.h** (`18-interrupts/kernel/util.h`) — 5 inbound connections
4. **types.h** (`20-interrupts-timer/cpu/types.h`) — 5 inbound connections
5. **util.h** (`20-interrupts-timer/kernel/util.h`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **keyboard.c** (`23-fixes/drivers/keyboard.c`) — 8 outbound dependencies
2. **isr.c** (`21-shell/cpu/isr.c`) — 7 outbound dependencies
3. **keyboard.c** (`21-shell/drivers/keyboard.c`) — 7 outbound dependencies
4. **isr.c** (`22-malloc/cpu/isr.c`) — 7 outbound dependencies
5. **keyboard.c** (`22-malloc/drivers/keyboard.c`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `print_letter` **(Compute Cores)** (@ `20-interrupts-timer/drivers/keyboard.c`) -> Impact: **101.4** | LOC: 189
- `print_char` **(Many-Argument Workhorses)** (@ `21-shell/drivers/screen.c`) -> Impact: **33.6** | LOC: 45
  * *Intent:* /********************************************************** * Private kernel functions * **********************************************************/ /...
- `print_char` **(Many-Argument Workhorses)** (@ `22-malloc/drivers/screen.c`) -> Impact: **33.6** | LOC: 45
  * *Intent:* /********************************************************** * Private kernel functions * **********************************************************/ /...
- `print_char` **(Many-Argument Workhorses)** (@ `23-fixes/drivers/screen.c`) -> Impact: **33.6** | LOC: 45
  * *Intent:* /********************************************************** * Private kernel functions * **********************************************************/ /...
- `print_char` **(Many-Argument Workhorses)** (@ `17-video-scroll/drivers/screen.c`) -> Impact: **28.9** | LOC: 42
  * *Intent:* /********************************************************** * Private kernel functions * **********************************************************/ /...
- `print_char` **(Many-Argument Workhorses)** (@ `18-interrupts/drivers/screen.c`) -> Impact: **28.9** | LOC: 42
  * *Intent:* /********************************************************** * Private kernel functions * **********************************************************/ /...
- `print_char` **(Many-Argument Workhorses)** (@ `20-interrupts-timer/drivers/screen.c`) -> Impact: **28.9** | LOC: 42
  * *Intent:* /********************************************************** * Private kernel functions * **********************************************************/ /...
- `print_char` **(Many-Argument Workhorses)** (@ `16-video-driver/drivers/screen.c`) -> Impact: **21.4** | LOC: 26
  * *Intent:* /********************************************************** * Private kernel functions * **********************************************************/ /...
- `hex_to_ascii` **(Compute Cores)** (@ `22-malloc/libc/string.c`) -> Impact: **14.8** | LOC: 19
- `hex_to_ascii` **(Compute Cores)** (@ `23-fixes/libc/string.c`) -> Impact: **14.8** | LOC: 19

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `20-interrupts-timer/drivers` | 6 | 323.08 | 10.56% | 26.18% |
| `21-shell/cpu` | 10 | 314.64 | 0.56% | 39.94% |
| `22-malloc/cpu` | 10 | 314.64 | 0.56% | 39.94% |
| `23-fixes/cpu` | 10 | 305.28 | 0.56% | 39.94% |
| `20-interrupts-timer/cpu` | 8 | 281.18 | 0.7% | 36.08% |
| `19-interrupts-irqs/cpu` | 6 | 261.14 | 0.94% | 41.81% |
| `23-fixes/libc` | 5 | 212.76 | 24.17% | 39.14% |
| `22-malloc/libc` | 5 | 212.24 | 24.17% | 39.14% |
| `21-shell/drivers` | 4 | 211.92 | 15.95% | 25.72% |
| `22-malloc/drivers` | 4 | 211.92 | 15.95% | 25.72% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `23-fixes/cpu/interrupt.asm` -> **100.0%** Exposure
- `18-interrupts/cpu/interrupt.asm` -> **99.9998%** Exposure
- `19-interrupts-irqs/cpu/interrupt.asm` -> **99.9996%** Exposure
- `20-interrupts-timer/cpu/interrupt.asm` -> **99.9996%** Exposure
- `21-shell/cpu/interrupt.asm` -> **99.9996%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `16-video-driver/drivers/screen.c` -> **100.0%** Exposure
- `17-video-scroll/drivers/screen.c` -> **100.0%** Exposure
- `17-video-scroll/kernel/util.c` -> **100.0%** Exposure
- `18-interrupts/drivers/screen.c` -> **100.0%** Exposure
- `18-interrupts/kernel/util.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `19-interrupts-irqs/cpu/interrupt.asm` -> **48** Orphaned Functions | **0** Duplicates
- `20-interrupts-timer/cpu/interrupt.asm` -> **48** Orphaned Functions | **0** Duplicates
- `21-shell/cpu/interrupt.asm` -> **48** Orphaned Functions | **0** Duplicates
- `22-malloc/cpu/interrupt.asm` -> **48** Orphaned Functions | **0** Duplicates
- `23-fixes/cpu/interrupt.asm` -> **48** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `138` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `23-fixes/drivers/screen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.771)
- **Top Global Matches:** file_cluster_12: 5.771, file_cluster_7: 7.919, file_cluster_15: 8.81
- **Magnitude:** 165.14 | **LOC:** 151 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (64.4%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print_char` **(Many-Argument Workhorses)** (Impact: 33.6)
    * *Intent:* /********************************************************** * Private kernel functions * ***********...
  * `kprint_at` **(Many-Argument Workhorses)** (Impact: 11.0)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `clear_screen` **(I/O & Config Routines)** (Impact: 2.5)
  * `set_cursor_offset` **(Parameter Forwarders)** (Impact: 1.8)
  * `get_offset` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 12`, `args: 20`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 31`, `unreferenced_by_name: 3`
* *Architecture:* `api: 16`, `import: 4`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ports.h, mem.h, screen.h, stdint.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `21-shell/drivers/screen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.784)
- **Top Global Matches:** file_cluster_12: 5.784, file_cluster_7: 7.905, file_cluster_15: 8.846
- **Magnitude:** 165.12 | **LOC:** 150 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.2%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (65.1%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print_char` **(Many-Argument Workhorses)** (Impact: 33.6)
    * *Intent:* /********************************************************** * Private kernel functions * ***********...
  * `kprint_at` **(Many-Argument Workhorses)** (Impact: 11.0)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `clear_screen` **(I/O & Config Routines)** (Impact: 2.5)
  * `set_cursor_offset` **(Parameter Forwarders)** (Impact: 1.8)
  * `get_offset` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 12`, `args: 20`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 31`, `unreferenced_by_name: 3`
* *Architecture:* `api: 16`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ports.h, mem.h, screen.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `22-malloc/drivers/screen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.784)
- **Top Global Matches:** file_cluster_12: 5.784, file_cluster_7: 7.905, file_cluster_15: 8.846
- **Magnitude:** 165.12 | **LOC:** 150 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.2%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (65.1%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print_char` **(Many-Argument Workhorses)** (Impact: 33.6)
    * *Intent:* /********************************************************** * Private kernel functions * ***********...
  * `kprint_at` **(Many-Argument Workhorses)** (Impact: 11.0)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `clear_screen` **(I/O & Config Routines)** (Impact: 2.5)
  * `set_cursor_offset` **(Parameter Forwarders)** (Impact: 1.8)
  * `get_offset` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 12`, `args: 20`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 31`, `unreferenced_by_name: 3`
* *Architecture:* `api: 16`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ports.h, mem.h, screen.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `17-video-scroll/drivers/screen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.945)
- **Top Global Matches:** file_cluster_15: 4.945, file_cluster_11: 6.263, file_cluster_16: 7.346
- **Magnitude:** 151.94 | **LOC:** 140 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (48.8%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print_char` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* /********************************************************** * Private kernel functions * ***********...
  * `kprint_at` **(Many-Argument Workhorses)** (Impact: 11.0)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `clear_screen` **(I/O & Config Routines)** (Impact: 2.5)
  * `set_cursor_offset` **(Parameter Forwarders)** (Impact: 1.8)
  * `get_offset` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 11`, `args: 20`, `func_start: 9`
* *Risk/State:* `state_mutation: 29`, `unreferenced_by_name: 2`
* *Architecture:* `api: 15`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` util.h, ports.h, screen.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `18-interrupts/drivers/screen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.945)
- **Top Global Matches:** file_cluster_15: 4.945, file_cluster_11: 6.263, file_cluster_16: 7.346
- **Magnitude:** 151.94 | **LOC:** 140 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (48.8%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print_char` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* /********************************************************** * Private kernel functions * ***********...
  * `kprint_at` **(Many-Argument Workhorses)** (Impact: 11.0)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `clear_screen` **(I/O & Config Routines)** (Impact: 2.5)
  * `set_cursor_offset` **(Parameter Forwarders)** (Impact: 1.8)
  * `get_offset` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 11`, `args: 20`, `func_start: 9`
* *Risk/State:* `state_mutation: 29`, `unreferenced_by_name: 2`
* *Architecture:* `api: 15`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` util.h, ports.h, screen.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `20-interrupts-timer/drivers/screen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.927)
- **Top Global Matches:** file_cluster_15: 4.927, file_cluster_11: 6.231, file_cluster_16: 7.324
- **Magnitude:** 151.92 | **LOC:** 139 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (48.4%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print_char` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* /********************************************************** * Private kernel functions * ***********...
  * `kprint_at` **(Many-Argument Workhorses)** (Impact: 11.0)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `clear_screen` **(I/O & Config Routines)** (Impact: 2.5)
  * `set_cursor_offset` **(Parameter Forwarders)** (Impact: 1.8)
  * `get_offset` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 11`, `args: 20`, `func_start: 9`
* *Risk/State:* `state_mutation: 29`, `unreferenced_by_name: 2`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ports.h, screen.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `16-video-driver/drivers/screen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.875)
- **Top Global Matches:** file_cluster_15: 4.875, file_cluster_11: 6.12, file_cluster_16: 7.315
- **Magnitude:** 126.22 | **LOC:** 123 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.2%), Debt Markers (formerly Tech Debt) (53.3%), Complexity Load (formerly Cognitive Load) (44.7%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print_char` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* /********************************************************** * Private kernel functions * ***********...
  * `kprint_at` **(Many-Argument Workhorses)** (Impact: 11.0)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `clear_screen` **(I/O & Config Routines)** (Impact: 2.5)
  * `set_cursor_offset` **(Parameter Forwarders)** (Impact: 1.8)
  * `get_offset` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 11`, `args: 20`, `func_start: 9`
* *Risk/State:* `state_mutation: 23`, `unreferenced_by_name: 2`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ports.h, screen.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `19-interrupts-irqs/cpu/interrupt.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.436)
- **Top Global Matches:** file_cluster_7: 6.436, file_cluster_14: 7.873, file_cluster_12: 10.201
- **Magnitude:** 120.24 | **LOC:** 426 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (12.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `irq_common_stub` **(Parameter Forwarders)** (Impact: 5.6)
    * *Intent:* ; Common IRQ code. Identical to ISR code except for the 'call' ; and the 'pop ebx'
  * `isr_common_stub` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* ; Defined in isr.c ; Common ISR code
  * `isr0` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 0: Divide By Zero Exception
  * `isr1` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 1: Debug Exception
  * `isr2` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 2: Non Maskable Interrupt Exception
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 170`, `args: 20`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 48`, `unreferenced_by_name: 48`
* *Architecture:* `api: 48`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `20-interrupts-timer/cpu/interrupt.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.436)
- **Top Global Matches:** file_cluster_7: 6.436, file_cluster_14: 7.873, file_cluster_12: 10.201
- **Magnitude:** 120.24 | **LOC:** 426 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (12.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `irq_common_stub` **(Parameter Forwarders)** (Impact: 5.6)
    * *Intent:* ; Common IRQ code. Identical to ISR code except for the 'call' ; and the 'pop ebx'
  * `isr_common_stub` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* ; Defined in isr.c ; Common ISR code
  * `isr0` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 0: Divide By Zero Exception
  * `isr1` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 1: Debug Exception
  * `isr2` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 2: Non Maskable Interrupt Exception
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 170`, `args: 20`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 48`, `unreferenced_by_name: 48`
* *Architecture:* `api: 48`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `21-shell/cpu/interrupt.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.436)
- **Top Global Matches:** file_cluster_7: 6.436, file_cluster_14: 7.873, file_cluster_12: 10.201
- **Magnitude:** 120.24 | **LOC:** 426 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (12.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `irq_common_stub` **(Parameter Forwarders)** (Impact: 5.6)
    * *Intent:* ; Common IRQ code. Identical to ISR code except for the 'call' ; and the 'pop ebx'
  * `isr_common_stub` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* ; Defined in isr.c ; Common ISR code
  * `isr0` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 0: Divide By Zero Exception
  * `isr1` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 1: Debug Exception
  * `isr2` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 2: Non Maskable Interrupt Exception
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 170`, `args: 20`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 48`, `unreferenced_by_name: 48`
* *Architecture:* `api: 48`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `22-malloc/cpu/interrupt.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.436)
- **Top Global Matches:** file_cluster_7: 6.436, file_cluster_14: 7.873, file_cluster_12: 10.201
- **Magnitude:** 120.24 | **LOC:** 426 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (12.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `irq_common_stub` **(Parameter Forwarders)** (Impact: 5.6)
    * *Intent:* ; Common IRQ code. Identical to ISR code except for the 'call' ; and the 'pop ebx'
  * `isr_common_stub` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* ; Defined in isr.c ; Common ISR code
  * `isr0` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 0: Divide By Zero Exception
  * `isr1` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 1: Debug Exception
  * `isr2` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 2: Non Maskable Interrupt Exception
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 170`, `args: 20`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 48`, `unreferenced_by_name: 48`
* *Architecture:* `api: 48`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `23-fixes/cpu/interrupt.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 3.451)
- **Top Global Matches:** file_cluster_11: 3.451, file_cluster_15: 6.169, file_cluster_2: 6.371
- **Magnitude:** 118.96 | **LOC:** 381 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (13.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `irq_common_stub` **(Parameter Forwarders)** (Impact: 5.7)
    * *Intent:* ; Common IRQ code. Identical to ISR code except for the 'call' ; and the 'pop ebx'
  * `isr_common_stub` **(Parameter Forwarders)** (Impact: 2.7)
    * *Intent:* ; Defined in isr.c ; Common ISR code
  * `isr0` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 0: Divide By Zero Exception
  * `isr1` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 1: Debug Exception
  * `isr2` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 2: Non Maskable Interrupt Exception
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 174`, `args: 20`, `func_start: 50`
* *Risk/State:* `unreferenced_by_name: 48`
* *Architecture:* `api: 48`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `22-malloc/libc/string.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.196)
- **Top Global Matches:** file_cluster_15: 4.196, file_cluster_16: 7.186, file_cluster_11: 7.408
- **Magnitude:** 116.68 | **LOC:** 78 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.6%), Guard Balance (formerly Safety Score) (85.1%), Complexity Load (formerly Cognitive Load) (61.0%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hex_to_ascii` **(Compute Cores)** (Impact: 14.8)
  * `int_to_ascii` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* #include "string.h" #include "../cpu/type.h" /** * K&R implementation */
  * `strcmp` **(Compute Cores)** (Impact: 5.5)
    * *Intent:* /* K&R * Returns <0 if s1<s2, 0 if s1==s2, >0 if s1>s2 */
  * `reverse` **(Compute Cores)** (Impact: 3.2)
    * *Intent:* /* K&R */
  * `strlen` **(Parameter Forwarders)** (Impact: 3.1)
    * *Intent:* /* K&R */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 9`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 25`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` type.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `23-fixes/libc/string.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.183)
- **Top Global Matches:** file_cluster_15: 4.183, file_cluster_16: 7.164, file_cluster_2: 7.313
- **Magnitude:** 116.68 | **LOC:** 78 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.6%), Guard Balance (formerly Safety Score) (85.1%), Complexity Load (formerly Cognitive Load) (61.0%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hex_to_ascii` **(Compute Cores)** (Impact: 14.8)
  * `int_to_ascii` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* #include "string.h" #include <stdint.h> /** * K&R implementation */
  * `strcmp` **(Compute Cores)** (Impact: 5.5)
    * *Intent:* /* K&R * Returns <0 if s1<s2, 0 if s1==s2, >0 if s1>s2 */
  * `reverse` **(Compute Cores)** (Impact: 3.2)
    * *Intent:* /* K&R */
  * `strlen` **(Parameter Forwarders)** (Impact: 3.1)
    * *Intent:* /* K&R */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 9`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 25`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdint.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `20-interrupts-timer/drivers/keyboard.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.493)
- **Top Global Matches:** file_cluster_8: 7.493, file_cluster_6: 17.415, file_cluster_3: 20.406
- **Magnitude:** 110.56 | **LOC:** 212 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (14.9%), Debt Markers (formerly Tech Debt) (11.8%), Connectivity (formerly Api Exposure) (2.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print_letter` **(Compute Cores)** (Impact: 101.4)
  * `keyboard_callback` **(Encapsulated Accessors)** (Impact: 2.0)
    * *Intent:* #include "keyboard.h" #include "ports.h" #include "../cpu/isr.h" #include "screen.h"
  * `init_keyboard` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 62`, `args: 3`, `func_start: 3`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` isr.h, keyboard.h, ports.h, screen.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `20-interrupts-timer/kernel/util.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.976)
- **Top Global Matches:** file_cluster_12: 5.976, file_cluster_7: 7.674, file_cluster_15: 8.009
- **Magnitude:** 86.8 | **LOC:** 48 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.1%), Guard Balance (formerly Safety Score) (84.7%), Complexity Load (formerly Cognitive Load) (52.4%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `int_to_ascii` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* /** * K&R implementation */
  * `memory_copy` **(Parameter Forwarders)** (Impact: 4.3)
    * *Intent:* #include "util.h"
  * `memory_set` **(Parameter Forwarders)** (Impact: 4.2)
  * `reverse` **(Compute Cores)** (Impact: 3.2)
    * *Intent:* /* K&R */
  * `strlen` **(Parameter Forwarders)** (Impact: 3.1)
    * *Intent:* /* K&R */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 5`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `unreferenced_by_name: 3`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `21-shell/libc/string.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.073)
- **Top Global Matches:** file_cluster_15: 4.073, file_cluster_2: 7.029, file_cluster_11: 7.042
- **Magnitude:** 85.52 | **LOC:** 57 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.6%), Guard Balance (formerly Safety Score) (82.3%), Complexity Load (formerly Cognitive Load) (52.4%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `int_to_ascii` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* #include "string.h" /** * K&R implementation */
  * `strcmp` **(Compute Cores)** (Impact: 5.5)
    * *Intent:* /* K&R * Returns <0 if s1<s2, 0 if s1==s2, >0 if s1>s2 */
  * `reverse` **(Compute Cores)** (Impact: 3.2)
    * *Intent:* /* K&R */
  * `strlen` **(Parameter Forwarders)** (Impact: 3.1)
    * *Intent:* /* K&R */
  * `append` **(Parameter Forwarders)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 7`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 20`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `18-interrupts/cpu/interrupt.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.478)
- **Top Global Matches:** file_cluster_7: 6.478, file_cluster_14: 7.69, file_cluster_5: 10.352
- **Magnitude:** 79.22 | **LOC:** 290 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (12.3%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isr_common_stub` **(Parameter Forwarders)** (Impact: 4.7)
    * *Intent:* ; Defined in isr.c ; Common ISR code
  * `isr0` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 0: Divide By Zero Exception
  * `isr1` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 1: Debug Exception
  * `isr2` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 2: Non Maskable Interrupt Exception
  * `isr3` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* ; 3: Int 3 Exception
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 104`, `args: 10`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 32`, `unreferenced_by_name: 32`
* *Architecture:* `api: 32`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `21-shell/cpu/isr.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 3.185)
- **Top Global Matches:** file_cluster_17: 3.185, file_cluster_2: 4.674, file_cluster_13: 6.034
- **Magnitude:** 70.58 | **LOC:** 90 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 5.232; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 56`, `args: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 54`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.232
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.017778
  * `Imports (Out-Degree: 1):` types.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `22-malloc/cpu/isr.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 3.185)
- **Top Global Matches:** file_cluster_17: 3.185, file_cluster_2: 4.674, file_cluster_13: 6.034
- **Magnitude:** 70.58 | **LOC:** 90 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 5.099; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 56`, `args: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 54`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.099
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.017778
  * `Imports (Out-Degree: 1):` type.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `23-fixes/cpu/isr.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 3.294)
- **Top Global Matches:** file_cluster_17: 3.294, file_cluster_2: 4.701, file_cluster_13: 6.133
- **Magnitude:** 70.58 | **LOC:** 96 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 5.552; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 56`, `args: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 54`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018519
  * `Imports (Out-Degree: 0):` stdint.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `19-interrupts-irqs/cpu/isr.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 3.18)
- **Top Global Matches:** file_cluster_17: 3.18, file_cluster_2: 4.682, file_cluster_13: 6.038
- **Magnitude:** 69.56 | **LOC:** 89 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 4.915; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 55`, `args: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 53`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.915
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.008889
  * `Imports (Out-Degree: 1):` types.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `20-interrupts-timer/cpu/isr.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 3.18)
- **Top Global Matches:** file_cluster_17: 3.18, file_cluster_2: 4.682, file_cluster_13: 6.038
- **Magnitude:** 69.56 | **LOC:** 89 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 5.892; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 55`, `args: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 53`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.892
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.017778
  * `Imports (Out-Degree: 1):` types.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `18-interrupts/kernel/util.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.193)
- **Top Global Matches:** file_cluster_12: 7.193, file_cluster_7: 7.348, file_cluster_5: 9.549
- **Magnitude:** 54.22 | **LOC:** 31 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (73.6%), Complexity Load (formerly Cognitive Load) (49.4%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `int_to_ascii` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* /** * K&R implementation */
  * `memory_copy` **(Parameter Forwarders)** (Impact: 4.3)
    * *Intent:* #include "util.h"
  * `memory_set` **(Parameter Forwarders)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 3`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`, `planned_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `19-interrupts-irqs/kernel/util.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.193)
- **Top Global Matches:** file_cluster_12: 7.193, file_cluster_7: 7.348, file_cluster_5: 9.549
- **Magnitude:** 54.22 | **LOC:** 31 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 3.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (73.6%), Complexity Load (formerly Cognitive Load) (49.4%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `int_to_ascii` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* /** * K&R implementation */
  * `memory_copy` **(Parameter Forwarders)** (Impact: 4.3)
    * *Intent:* #include "util.h"
  * `memory_set` **(Parameter Forwarders)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 3`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`, `planned_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `18-interrupts/cpu/isr.c` (C) | Magnitude: 7.54 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 72, import: 4, structural_boundaries: 2, func_start: 2
- `23-fixes/cpu/timer.c` (C) | Magnitude: 6.06 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 9, import: 4, core_var_decl: 4, design_snake_case: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `17-video-scroll/kernel/util.h` (C) | Magnitude: 13.04 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, args: 2, api: 2, pointers: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `07-bootsector-disk/boot_sect_main.asm` (ASSEMBLY) | Magnitude: 15.38 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 11, args: 4, import: 3

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `10-32bit-enter/32bit-switch.asm` -> **Severity: 0.463** (Embedded: 0.0089 * Error Risk: 52.1415%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `23-fixes/kernel/kernel.c` -> **Severity: 580.4** (Blast Radius: 5.804 * Doc Risk: 100.0%)
- `10-32bit-enter/32bit-switch.asm` -> **Severity: 362.354** (Blast Radius: 4.248 * Doc Risk: 85.3%)
- `08-32bit-print/32bit-print.asm` -> **Severity: 332.831** (Blast Radius: 4.248 * Doc Risk: 78.35%)
- `05-bootsector-functions-strings/boot_sect_print.asm` -> **Severity: 323.5** (Blast Radius: 6.47 * Doc Risk: 50.0%)
- `14-checkpoint/boot/32bit_print.asm` -> **Severity: 313.7** (Blast Radius: 3.137 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 418 call pairs -- scoped 30.1%, unique 0.2%, ambiguous 51.0%, external 18.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 328 | 36.9% | 0.0% | 41.5% | 21.6% |
| assembly | 90 | 5.6% | 1.1% | 85.6% | 7.8% |

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
