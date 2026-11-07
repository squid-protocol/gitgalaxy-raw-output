# ARCHITECTURAL_BRIEF: HelloSilicon
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/below/HelloSilicon.git` |
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
- **Scope:** 107 analyzed artifact(s), 2956 LOC.
- **Load-bearing artifact:** `Chapter 04/case.s` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `README.md` -- pulls in 2 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Chapter 15/upperghidra.c` at magnitude 42.04 (structural weight, not risk).
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
| Total Artifacts | 139 |
| Analyzed Artifacts (Scanned) | 107 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 32 |
| Total LOC | 2956 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 77.0% |
| Dominant Lang | ASSEMBLY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6667 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 46 | 2006 | 43.0% |
| JSON | 27 | 523 | 25.2% |
| MAKEFILE | 14 | 232 | 13.1% |
| C | 8 | 143 | 7.5% |
| XML | 7 | 0 | 6.5% |
| SWIFT | 2 | 42 | 1.9% |
| PYTHON | 1 | 10 | 0.9% |
| PLAINTEXT | 1 | 0 | 0.9% |
| MARKDOWN | 1 | 0 | 0.9% |

## 4.1 SOURCE ENCODINGS
All 107 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 39%, Parameter Forwarders Files 31%, Large Core Modules 11%, Declarative / Non-Code 7%, Compute Cores Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 105 | 98.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 32*

**Composition by Extension & Reason:**
- `no_extension`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable), 2x Excluded (Unsupported Extension: '.xcworkspacedata')
- `.xcscheme`: 5x Excluded (Unsupported Extension: '.xcscheme')
- `.pbxproj`: 2x Excluded (Unsupported Extension: '.pbxproj')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 57.9 | 2.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 72.0 | 3.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 23.5 | 28.6 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.6 | 2.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 20.1 | 2.4 | 3.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 1.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.6 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 53.5 | 0.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 59.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1 | 1 | 0 | `Chapter 10/ToUpper/Shared/ContentView.swift` |
| cleanup | 4 | 4 | 0 | `Chapter 05/makefile` |
| guards | 19 | 11 | 0 | `Chapter 07/fileio.S` |
| danger | 40 | 24 | 2 | `Chapter 07/fileio.S` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 75 | 61 | 2 | `Chapter 16/upper.c` |
| io | 43 | 24 | 2 | `Chapter 07/fileio.S` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2 | 1 | 0 | `Chapter 03/makefile` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 41 | 23 | 2 | `Chapter 07/fileio.S` |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 21 | 12 | 1 | `Chapter 09/uppertst.c` |
| mutation | 156 | 29 | 6 | `Chapter 15/upperghidra.c` |
| dead_code | 114 | 54 | 1 | `Chapter 05/codesnippets.s` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 29 | 7 | 0 | `Chapter 12/codesnippets.s` |
| ui | 8 | 2 | 0 | `Chapter 10/ToUpper/Shared/ContentView.swift` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Chapter 07/fileio.S` (Hits: 7)
- `Chapter 06/mainmacro.s` (Hits: 3)
- `Chapter 01/HelloWorld.s` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **case.s** (`Chapter 04/case.s`) — 1 inbound connections
2. **uppermacro.s** (`Chapter 06/uppermacro.s`) — 1 inbound connections
3. **upper.h** (`Chapter 10/ToUpper/Shared/upper.h`) — 1 inbound connections
4. **HelloWorld.s** (`Chapter 01/HelloWorld.s`) — 0 inbound connections
5. **addexamp1.s** (`Chapter 02/addexamp1.s`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`README.md`) — 2 outbound dependencies
2. **mainmacro.s** (`Chapter 06/mainmacro.s`) — 1 outbound dependencies
3. **addexamp2.s** (`Chapter 09/addexamp2.s`) — 1 outbound dependencies
4. **divexamp.s** (`Chapter 11/divexamp.s`) — 1 outbound dependencies
5. **mulexamp.s** (`Chapter 11/mulexamp.s`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `dotloop` **(Many-Argument Workhorses)** (@ `Chapter 11/matrixmult.s`) -> Impact: **15.2** | LOC: 22
- `loop` **(Many-Argument Workhorses)** (@ `Chapter 14/upper4.s`) -> Impact: **11.9** | LOC: 11
  * *Intent:* // The loop is until byte pointed to by R1 is non-zero
- `loop` **(Many-Argument Workhorses)** (@ `Chapter 13/main.s`) -> Impact: **11.8** | LOC: 24
- `loop` **(Parameter Forwarders)** (@ `Chapter 14/upper2.s`) -> Impact: **10.5** | LOC: 15
  * *Intent:* // The loop is until byte pointed to by R1 is non-zero
- `mytoupper` **(Compute Cores)** (@ `Chapter 16/upper.c`) -> Impact: **9.6** | LOC: 18
- `mytoupper` **(Compute Cores)** (@ `Chapter 15/upper.c`) -> Impact: **9.5** | LOC: 17
  * *Intent:* #include <stdio.h>
- `loop` **(Compute Cores)** (@ `Chapter 14/upper3.s`) -> Impact: **9.3** | LOC: 7
  * *Intent:* // The loop is until byte pointed to by R1 is non-zero
- `cont` **(Many-Argument Workhorses)** (@ `Chapter 04/printdword.s`) -> Impact: **9.2** | LOC: 26
- `loop` **(Compute Cores)** (@ `Chapter 12/main.s`) -> Impact: **9.2** | LOC: 24
- `cont` **(Many-Argument Workhorses)** (@ `Chapter 05/upper.s`) -> Impact: **8.5** | LOC: 23

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Parameter Forwarders**: thin, many-argument glue that forwards to other code

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Chapter 09` | 8 | 87.18 | 1.29% | 28.32% |
| `Chapter 04` | 4 | 85.84 | 6.34% | 53.5% |
| `Chapter 12` | 7 | 83.26 | 2.42% | 34.56% |
| `Chapter 06` | 6 | 82.94 | 2.71% | 41.82% |
| `Chapter 14` | 6 | 82.06 | 5.51% | 37.75% |
| `Chapter 16` | 6 | 78.04 | 7.02% | 51.23% |
| `Chapter 15` | 3 | 72.1 | 29.93% | 25.17% |
| `Chapter 11` | 5 | 69.14 | 2.14% | 23.39% |
| `Chapter 10/ToUpper/Shared` | 5 | 60.4 | 2.42% | 7.55% |
| `Chapter 07` | 4 | 57.12 | 4.08% | 16.6% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Chapter 05/codesnippets.s` -> **99.9999%** Exposure
- `Chapter 04/codesnippets.s` -> **99.9998%** Exposure
- `Chapter 02/codesnippets.s` -> **99.9997%** Exposure
- `Chapter 12/codesnippets.s` -> **99.9968%** Exposure
- `Chapter 06/codesnippets.s` -> **99.875%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Chapter 15/upperghidra.c` -> **100.0%** Exposure
- `Chapter 15/upper.c` -> **99.9254%** Exposure
- `Chapter 16/upper.c` -> **99.9254%** Exposure
- `Chapter 09/uppertst5.py` -> **91.6827%** Exposure
- `Chapter 14/upper4.s` -> **40.1312%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Chapter 05/codesnippets.s` -> **13** Orphaned Functions | **0** Duplicates
- `Chapter 02/codesnippets.s` -> **9** Orphaned Functions | **0** Duplicates
- `Chapter 04/codesnippets.s` -> **9** Orphaned Functions | **0** Duplicates
- `Chapter 06/codesnippets.s` -> **9** Orphaned Functions | **0** Duplicates
- `Chapter 12/codesnippets.s` -> **9** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `16` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Chapter 15/upperghidra.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.271)
- **Top Global Matches:** file_cluster_2: 6.271, file_cluster_17: 6.605, file_cluster_15: 6.908
- **Magnitude:** 42.04 | **LOC:** 41 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.128; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.0%), Complexity Load (formerly Cognitive Load) (57.9%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 6.4)
    * *Intent:* #define true 1
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 04/codesnippets.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.526)
- **Top Global Matches:** file_cluster_15: 5.526, file_cluster_11: 7.496, file_cluster_2: 7.742
- **Magnitude:** 33.74 | **LOC:** 79 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Dead Code Surface (formerly Dead Code) (13.5%), Complexity Load (formerly Cognitive Load) (9.0%), Connectivity (formerly Api Exposure) (3.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loop` **(Compute Cores)** (Impact: 7.4)
  * `loop2` **(Parameter Forwarders)** (Impact: 3.1)
  * `loop3` **(Parameter Forwarders)** (Impact: 3.0)
  * `l9` **(Parameter Forwarders)** (Impact: 2.2)
  * `_start` **(I/O & Config Routines)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 16`, `args: 22`, `func_start: 14`
* *Risk/State:* `dead_code: 1`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 11/matrixmult.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.066)
- **Top Global Matches:** file_cluster_15: 5.066, file_cluster_17: 7.16, file_cluster_16: 7.264
- **Magnitude:** 30.6 | **LOC:** 99 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (46.3%), Complexity Load (formerly Cognitive Load) (6.8%), Connectivity (formerly Api Exposure) (3.0%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dotloop` **(Many-Argument Workhorses)** (Impact: 15.2)
  * `printloop` **(Parameter Forwarders)** (Impact: 5.8)
  * `colloop` **(Parameter Forwarders)** (Impact: 2.8)
  * `main` **(Parameter Forwarders)** (Impact: 2.2)
  * `rowloop` **(Parameter Forwarders)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 42`, `args: 44`, `func_start: 5`
* *Risk/State:* `unreferenced_by_name: 2`
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 06/codesnippets.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.186)
- **Top Global Matches:** file_cluster_11: 5.186, file_cluster_15: 5.907, file_cluster_17: 6.994
- **Magnitude:** 30.16 | **LOC:** 125 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Dead Code Surface (formerly Dead Code) (17.4%), Connectivity (formerly Api Exposure) (2.9%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SUMFN` **(Parameter Forwarders)** (Impact: 3.4)
  * `l8` **(Parameter Forwarders)** (Impact: 2.2)
  * `l5` **(Parameter Forwarders)** (Impact: 2.1)
  * `l9` **(Parameter Forwarders)** (Impact: 2.1)
  * `l2` **(Parameter Forwarders)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 50`, `args: 28`, `func_start: 16`
* *Risk/State:* `dead_code: 2`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 1`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 05/codesnippets.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.81)
- **Top Global Matches:** file_cluster_15: 5.81, file_cluster_11: 7.176, file_cluster_2: 7.279
- **Magnitude:** 28.3 | **LOC:** 105 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (4.7%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `l16` **(Parameter Forwarders)** (Impact: 3.1)
  * `l11` **(Parameter Forwarders)** (Impact: 2.2)
  * `l13` **(Parameter Forwarders)** (Impact: 2.2)
  * `l10` **(Parameter Forwarders)** (Impact: 2.1)
  * `l12` **(Parameter Forwarders)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 24`, `args: 57`, `func_start: 13`
* *Risk/State:* `unreferenced_by_name: 13`
* *Architecture:* `io: 1`, `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 16/upper.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.888)
- **Top Global Matches:** file_cluster_11: 5.888, file_cluster_15: 6.324, file_cluster_2: 7.006
- **Magnitude:** 27.92 | **LOC:** 39 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.128; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (58.5%), Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (31.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mytoupper` **(Compute Cores)** (Impact: 9.6)
  * `main` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* #define BUFFERSIZE 10
  * `dummy` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* #include <stdio.h>
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 3`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 15/upper.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.989)
- **Top Global Matches:** file_cluster_11: 5.989, file_cluster_15: 6.458, file_cluster_2: 7.33
- **Magnitude:** 25.42 | **LOC:** 33 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.128; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (58.5%), Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (31.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mytoupper` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* #include <stdio.h>
  * `main` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 2`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 14/upper4.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.566)
- **Top Global Matches:** file_cluster_15: 5.566, file_cluster_17: 7.428, file_cluster_16: 7.491
- **Magnitude:** 21.34 | **LOC:** 47 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (40.1%), Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (10.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loop` **(Many-Argument Workhorses)** (Impact: 11.9)
    * *Intent:* // The loop is until byte pointed to by R1 is non-zero
  * `toupper` **(Parameter Forwarders)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `args: 37`, `func_start: 2`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 09/uppertst5.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 4.936)
- **Top Global Matches:** file_cluster_7: 4.936, file_cluster_14: 8.343, file_cluster_12: 9.08
- **Magnitude:** 21.2 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.128; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (56.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctypes
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 04/printdword.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.412)
- **Top Global Matches:** file_cluster_15: 5.412, file_cluster_11: 7.415, file_cluster_2: 7.444
- **Magnitude:** 21.18 | **LOC:** 64 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (34.3%), Complexity Load (formerly Cognitive Load) (6.7%), Connectivity (formerly Api Exposure) (3.3%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cont` **(Many-Argument Workhorses)** (Impact: 9.2)
  * `_start` **(Parameter Forwarders)** (Impact: 4.6)
  * `loop` **(Parameter Forwarders)** (Impact: 3.8)
  * `letter` **(Parameter Forwarders)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 19`, `args: 41`, `func_start: 4`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 04/case.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.228)
- **Top Global Matches:** file_cluster_11: 5.228, file_cluster_15: 5.426, file_cluster_2: 7.442
- **Magnitude:** 20.94 | **LOC:** 132 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 16.887; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (41.9%), Complexity Load (formerly Cognitive Load) (5.0%), Connectivity (formerly Api Exposure) (2.8%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_start` **(Compute Cores)** (Impact: 4.7)
  * `endit` **(I/O & Config Routines)** (Impact: 2.6)
    * *Intent:* // Setup the parameters to exit the program // and then call the kernel to do it.
  * `cend` **(Parameter Forwarders)** (Impact: 2.5)
  * `break` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* // b break not necessary here as it will // fall thru when done executing the // select3: case
  * `cloop` **(Parameter Forwarders)** (Impact: 1.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 33`, `args: 16`, `func_start: 9`
* *Risk/State:* `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.887
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009434
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Chapter 02/codesnippets.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.06)
- **Top Global Matches:** file_cluster_15: 6.06, file_cluster_11: 7.218, file_cluster_2: 7.319
- **Magnitude:** 20.28 | **LOC:** 71 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Dead Code Surface (formerly Dead Code) (15.0%), Connectivity (formerly Api Exposure) (3.2%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `l9` **(Parameter Forwarders)** (Impact: 3.2)
  * `l6` **(Parameter Forwarders)** (Impact: 2.9)
    * *Intent:* // Uncomment the next line if you want to see the // Assembler error for a constant that can't be //...
  * `l1` **(Parameter Forwarders)** (Impact: 2.2)
  * `l3` **(State Mutators)** (Impact: 1.9)
  * `l4` **(State Mutators)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 15`, `args: 70`, `func_start: 9`
* *Risk/State:* `dead_code: 1`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 12/maincomp.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.237)
- **Top Global Matches:** file_cluster_15: 4.237, file_cluster_17: 6.94, file_cluster_11: 6.949
- **Magnitude:** 19.86 | **LOC:** 79 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (28.6%), Complexity Load (formerly Cognitive Load) (6.7%), Connectivity (formerly Api Exposure) (3.2%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loop` **(Compute Cores)** (Impact: 7.6)
  * `next` **(Parameter Forwarders)** (Impact: 2.5)
  * `main` **(Parameter Forwarders)** (Impact: 2.1)
  * `equal` **(Parameter Forwarders)** (Impact: 1.9)
  * `equal2` **(Parameter Forwarders)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 29`, `args: 27`, `func_start: 6`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 07/main.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.694)
- **Top Global Matches:** file_cluster_15: 5.694, file_cluster_17: 7.198, file_cluster_11: 7.385
- **Magnitude:** 19.46 | **LOC:** 78 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (28.6%), Complexity Load (formerly Cognitive Load) (6.0%), Connectivity (formerly Api Exposure) (3.2%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loop` **(Parameter Forwarders)** (Impact: 7.1)
    * *Intent:* // loop through file until done.
  * `nxtfil` **(Parameter Forwarders)** (Impact: 6.5)
  * `_start` **(Parameter Forwarders)** (Impact: 2.5)
  * `exit` **(State Mutators)** (Impact: 1.1)
    * *Intent:* // Setup the parameters to exit the program // and then call the kernel to do it.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 26`, `args: 33`, `func_start: 4`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 05/upper.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.801)
- **Top Global Matches:** file_cluster_15: 5.801, file_cluster_11: 7.739, file_cluster_2: 7.745
- **Magnitude:** 18.52 | **LOC:** 53 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (6.4%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cont` **(Many-Argument Workhorses)** (Impact: 8.5)
  * `_start` **(Parameter Forwarders)** (Impact: 4.2)
  * `loop` **(Parameter Forwarders)** (Impact: 3.9)
    * *Intent:* // The loop is until byte pointed to by X1 is non-zero
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 16`, `args: 31`, `func_start: 3`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 10/ToUpper/Shared/Assets.xcassets/AppIcon.appiconset/Contents.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.094)
- **Top Global Matches:** file_cluster_2: 2.094, file_cluster_17: 4.919, file_cluster_13: 6.275
- **Magnitude:** 17.96 | **LOC:** 149 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 13/matrixmultneon.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.766)
- **Top Global Matches:** file_cluster_15: 5.766, file_cluster_17: 7.379, file_cluster_2: 7.565
- **Magnitude:** 17.0 | **LOC:** 93 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (50.0%), Complexity Load (formerly Cognitive Load) (5.2%), Connectivity (formerly Api Exposure) (3.1%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 8.4)
  * `printloop` **(Parameter Forwarders)** (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 39`, `args: 34`, `func_start: 2`
* *Risk/State:* `unreferenced_by_name: 2`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 12/codesnippets.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.547)
- **Top Global Matches:** file_cluster_11: 6.547, file_cluster_15: 6.806, file_cluster_2: 7.651
- **Magnitude:** 16.8 | **LOC:** 83 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (3.1%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `l8` **(Parameter Forwarders)** (Impact: 2.4)
  * `l3` **(State Mutators)** (Impact: 2.0)
  * `l7` **(State Mutators)** (Impact: 1.8)
  * `l2` **(Parameter Forwarders)** (Impact: 1.7)
  * `l4` **(I/O & Config Routines)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `args: 24`, `func_start: 9`
* *Risk/State:* `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 14/upper.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.459)
- **Top Global Matches:** file_cluster_15: 4.459, file_cluster_11: 6.51, file_cluster_2: 6.589
- **Magnitude:** 16.68 | **LOC:** 32 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (6.4%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cont` **(Parameter Forwarders)** (Impact: 7.0)
  * `loop` **(Parameter Forwarders)** (Impact: 4.5)
    * *Intent:* // The loop is until byte pointed to by X1 is non-zero
  * `toupper` **(Parameter Forwarders)** (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 10`, `args: 23`, `func_start: 3`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 16/upper.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.459)
- **Top Global Matches:** file_cluster_15: 4.459, file_cluster_11: 6.51, file_cluster_2: 6.589
- **Magnitude:** 16.68 | **LOC:** 32 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (6.4%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cont` **(Parameter Forwarders)** (Impact: 7.0)
  * `loop` **(Parameter Forwarders)** (Impact: 4.5)
    * *Intent:* // The loop is until byte pointed to by X1 is non-zero
  * `toupper` **(Parameter Forwarders)** (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 10`, `args: 23`, `func_start: 3`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 10/ToUpper/ToUpper WatchKit App/Assets.xcassets/AppIcon.appiconset/Contents.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.019)
- **Top Global Matches:** file_cluster_2: 2.019, file_cluster_17: 4.889, file_cluster_13: 6.247
- **Magnitude:** 16.62 | **LOC:** 82 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 09/debug.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.272)
- **Top Global Matches:** file_cluster_17: 4.272, file_cluster_2: 5.215, file_cluster_11: 6.217
- **Magnitude:** 16.34 | **LOC:** 72 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 60`, `args: 44`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 11/debug.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.272)
- **Top Global Matches:** file_cluster_17: 4.272, file_cluster_2: 5.215, file_cluster_11: 6.217
- **Magnitude:** 16.34 | **LOC:** 72 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 60`, `args: 44`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 14/upper2.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.566)
- **Top Global Matches:** file_cluster_15: 4.566, file_cluster_11: 6.676, file_cluster_2: 6.74
- **Magnitude:** 16.32 | **LOC:** 34 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (6.4%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loop` **(Parameter Forwarders)** (Impact: 10.5)
    * *Intent:* // The loop is until byte pointed to by R1 is non-zero
  * `toupper` **(Parameter Forwarders)** (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 9`, `args: 30`, `func_start: 2`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Chapter 07/upper.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.425)
- **Top Global Matches:** file_cluster_15: 4.425, file_cluster_11: 6.479, file_cluster_2: 6.541
- **Magnitude:** 16.08 | **LOC:** 32 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (6.4%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cont` **(Parameter Forwarders)** (Impact: 7.0)
  * `loop` **(Parameter Forwarders)** (Impact: 3.9)
    * *Intent:* // The loop is until byte pointed to by X1 is non-zero
  * `toupper` **(Parameter Forwarders)** (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 10`, `args: 21`, `func_start: 3`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Chapter 04/case.s` -> **Severity: 1688.7** (Blast Radius: 16.887 * Doc Risk: 100.0%)
- `Chapter 01/HelloWorld.s` -> **Severity: 912.8** (Blast Radius: 9.128 * Doc Risk: 100.0%)
- `Chapter 02/addexamp1.s` -> **Severity: 912.8** (Blast Radius: 9.128 * Doc Risk: 100.0%)
- `Chapter 02/addexamp2.s` -> **Severity: 912.8** (Blast Radius: 9.128 * Doc Risk: 100.0%)
- `Chapter 02/addexamps.s` -> **Severity: 912.8** (Blast Radius: 9.128 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 20 call pairs -- scoped 15.0%, unique 0.0%, ambiguous 5.0%, external 80.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 11 | 27.3% | 0.0% | 9.1% | 63.6% |
| python | 4 | 0.0% | 0.0% | 0.0% | 100.0% |
| swift | 3 | 0.0% | 0.0% | 0.0% | 100.0% |
| assembly | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
