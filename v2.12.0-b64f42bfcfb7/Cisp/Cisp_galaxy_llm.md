# ARCHITECTURAL_BRIEF: Cisp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/lauryndbrown/Cisp` |
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
- **Scope:** 8 analyzed artifact(s), 816 LOC.
- **Load-bearing artifact:** `logger.cbl` -- 5 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Heaviest artifact:** `tokenizer.cbl` at magnitude 252.64 (structural weight, not risk).
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
| Total Artifacts | 51 |
| Analyzed Artifacts (Scanned) | 8 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 43 |
| Total LOC | 816 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 15.7% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5319 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.1667 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 6 | 801 | 75.0% |
| MARKDOWN | 1 | 0 | 12.5% |
| BATCH | 1 | 15 | 12.5% |

## 4.1 SOURCE ENCODINGS
All 8 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 38%, State Mutators Files 25%, Data / Markup / Trivial 12%, Declarative / Non-Code 12%, Interface Declarations Files 12%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 7 | 87.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 12.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 43*

**Composition by Extension & Reason:**
- `.dll`: 29x Excluded (Explicitly Denied Extension: '.dll')
- `.lisp`: 8x Excluded (Unsupported Extension: '.lisp')
- `.exe`: 3x Excluded (Explicitly Denied Extension: '.exe')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.data`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 90.6 | 48.9 | 53.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 77.7 | 55.5 | 61.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 23.0 | 7.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 13.5 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 3.3 | 2.0 | 2.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 85.5 | 99.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 50.0 | 42.9 | 50.0 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5 | 2 | 2 | `recursion.cbl` |
| cleanup | 12 | 6 | 2 | `recursion.cbl` |
| guards | 0 | 0 | 0 | - |
| danger | 7 | 6 | 1 | `cisp-error.cbl` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 5 | 5 | 1 | `cisp-error.cbl` |
| io | 20 | 4 | 6 | `recursion.cbl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 31 | 5 | 8 | `lisp.cbl` |
| time | 0 | 0 | 0 | - |
| serialization | 16 | 4 | 4 | `tokenizer.cbl` |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 23 | 5 | 6 | `tokenizer.cbl` |
| mutation | 202 | 7 | 54 | `tokenizer.cbl` |
| dead_code | 6 | 3 | 2 | `tokenizer.cbl` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **1.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `recursion.cbl` (Hits: 8)
- `logger.cbl` (Hits: 6)
- `tokenizer.cbl` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **logger.cbl** (`logger.cbl`) — 5 inbound connections
2. **recursion.cbl** (`recursion.cbl`) — 2 inbound connections
3. **cisp-error.cbl** (`cisp-error.cbl`) — 1 inbound connections
4. **lisp.cbl** (`lisp.cbl`) — 1 inbound connections
5. **tokenizer.cbl** (`tokenizer.cbl`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
No file in this repository declares an import that GitGalaxy resolved, so there is no coupling ranking to report. See the note above -- the same caveat applies.


## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `MAIN-PROCEDURE` **(Compute Cores)** (@ `recursion.cbl`) -> Impact: **11.2** | LOC: 25
- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `lisp.cbl`) -> Impact: **10.2** | LOC: 25
- `FORMAT-LISP-PROCEDURE` **(I/O & Config Routines)** (@ `tokenizer.cbl`) -> Impact: **9.0** | LOC: 40
- `FILE-HANDLING-PROCEDURE` **(I/O & Config Routines)** (@ `tokenizer.cbl`) -> Impact: **8.3** | LOC: 27
- `CALC-LISP-LENGTH` **(I/O & Config Routines)** (@ `tokenizer.cbl`) -> Impact: **8.0** | LOC: 19
- `MAIN-PROCEDURE` **(Compute Cores)** (@ `logger.cbl`) -> Impact: **6.5** | LOC: 11
- `FORMAT-PAREN-SPACE-PROCEDURE` **(Compute Cores)** (@ `tokenizer.cbl`) -> Impact: **6.5** | LOC: 9
- `TOKENIZE-LISP-PROCEDURE` **(I/O & Config Routines)** (@ `tokenizer.cbl`) -> Impact: **6.2** | LOC: 24
- `EVALUATE-CURRENT-VALUES` **(I/O & Config Routines)** (@ `lisp.cbl`) -> Impact: **6.0** | LOC: 21
- `EVALUATE-CURRENT-COMMAND` **(I/O & Config Routines)** (@ `lisp.cbl`) -> Impact: **5.5** | LOC: 10

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 7 | 551.28 | 48.87% | 7.84% |
| `bin` | 1 | 15.3 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lisp.cbl` -> **22.9758%** Exposure
- `tokenizer.cbl` -> **20.1587%** Exposure
- `recursion.cbl` -> **11.7199%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `tokenizer.cbl` -> **100.0%** Exposure
- `lisp.cbl` -> **99.9999%** Exposure
- `recursion.cbl` -> **99.9984%** Exposure
- `cisp.cbl` -> **99.931%** Exposure
- `logger.cbl` -> **99.9137%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tokenizer.cbl` -> **3** Orphaned Functions | **0** Duplicates
- `lisp.cbl` -> **2** Orphaned Functions | **0** Duplicates
- `recursion.cbl` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `32` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `0` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tokenizer.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.447)
- **Top Global Matches:** file_cluster_11: 6.447, file_cluster_15: 6.795, file_cluster_2: 7.19
- **Magnitude:** 252.64 | **LOC:** 306 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 92.71; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%), Complexity Load (formerly Cognitive Load) (65.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FORMAT-LISP-PROCEDURE` **(I/O & Config Routines)** (Impact: 9.0)
  * `FILE-HANDLING-PROCEDURE` **(I/O & Config Routines)** (Impact: 8.3)
  * `CALC-LISP-LENGTH` **(I/O & Config Routines)** (Impact: 8.0)
  * `FORMAT-PAREN-SPACE-PROCEDURE` **(Compute Cores)** (Impact: 6.5)
  * `TOKENIZE-LISP-PROCEDURE` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 39`, `args: 9`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 81`, `unreferenced_by_name: 3`
* *Architecture:* `io: 5`, `api: 1`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 92.71
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.142857
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `recursion.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.899)
- **Top Global Matches:** file_cluster_15: 6.899, file_cluster_2: 7.048, file_cluster_11: 7.86
- **Magnitude:** 114.76 | **LOC:** 229 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 140.376; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.9%), Guard Balance (formerly Safety Score) (64.9%), Debt Markers (formerly Tech Debt) (11.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Compute Cores)** (Impact: 11.2)
  * `PRINT-CALL-STACK-PROCEDURE` **(I/O & Config Routines)** (Impact: 4.8)
  * `IS-STACK-EMPTY-PROCEDURE` **(I/O & Config Routines)** (Impact: 3.3)
  * `POP-CALL-STACK-PROCEDURE` **(I/O & Config Routines)** (Impact: 2.7)
  * `CALL-STACK-ADD-PROCEDURE` **(I/O & Config Routines)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 29`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 54`, `unreferenced_by_name: 1`
* *Architecture:* `io: 8`, `api: 1`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 140.376
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.321429
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lisp.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.324)
- **Top Global Matches:** file_cluster_11: 6.324, file_cluster_15: 7.197, file_cluster_2: 7.414
- **Magnitude:** 109.6 | **LOC:** 193 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 92.71; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.6%), Guard Balance (formerly Safety Score) (67.3%), Debt Markers (formerly Tech Debt) (23.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 10.2)
  * `EVALUATE-CURRENT-VALUES` **(I/O & Config Routines)** (Impact: 6.0)
  * `EVALUATE-CURRENT-COMMAND` **(I/O & Config Routines)** (Impact: 5.5)
  * `INIT-RECURSION-OBJECT-PROCEDURE` **(I/O & Config Routines)** (Impact: 3.9)
  * `RETURN-PROCEDURE` **(I/O & Config Routines)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 28`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 92.71
  * `Choke Point (Betweenness):` 0.047619 | `Ripple Effect (Closeness):` 0.142857
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `logger.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.66)
- **Top Global Matches:** file_cluster_11: 6.66, file_cluster_15: 6.944, file_cluster_2: 7.415
- **Magnitude:** 26.7 | **LOC:** 62 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); blast radius 358.969; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (58.6%), Complexity Load (formerly Cognitive Load) (53.9%), Connectivity (formerly Api Exposure) (3.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Compute Cores)** (Impact: 6.5)
  * `LOG-INIT-PROCEDURE` **(I/O & Config Routines)** (Impact: 1.4)
  * `LOG-CLOSE-PROCEDURE` **(I/O & Config Routines)** (Impact: 1.4)
  * `LOG-WRITE-TO-PROCEDURE` **(I/O & Config Routines)** (Impact: 1.2)
  * `LOG-FLAG-ERROR-PROCEDURE` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 14`, `args: 2`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 6`, `api: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 358.969
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.714286
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `cisp.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.649)
- **Top Global Matches:** file_cluster_11: 5.649, file_cluster_2: 7.082, file_cluster_15: 7.365
- **Magnitude:** 24.14 | **LOC:** 79 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (59.0%), Complexity Load (formerly Cognitive Load) (28.2%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-CMD-LINE-PROCEDURE` **(Interface Declarations)** (Impact: 1.5)
  * `MAIN-PROCEDURE` **(Interface Declarations)** (Impact: 1.4)
  * `TOKENIZE-LISP-PROCEDURE` **(State Mutators)** (Impact: 1.4)
  * `EVALUTE-LISP-PROCEDURE` **(State Mutators)** (Impact: 1.4)
  * `INIT-LOGGER-PROCEDURE` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 15`, `args: 14`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `io: 1`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 72.242
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cisp-error.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.12)
- **Top Global Matches:** file_cluster_11: 5.12, file_cluster_2: 7.099, file_cluster_15: 7.233
- **Magnitude:** 21.78 | **LOC:** 68 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 98.51; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Guard Balance (formerly Safety Score) (61.3%), Complexity Load (formerly Cognitive Load) (20.3%), Connectivity (formerly Api Exposure) (3.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Interface Declarations)** (Impact: 3.2)
  * `CLOSE-OPEN-FILES-PROCEDURE` **(Interface Declarations)** (Impact: 2.5)
  * `THROW-ERROR-PROCEDURE` **(Interface Declarations)** (Impact: 2.3)
  * `LOG-ERROR-PROCEDURE` **(I/O & Config Routines)** (Impact: 1.5)
  * `END-CISP-PROCEDURE` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `args: 8`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`
* *Architecture:* `api: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 98.51
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.190476
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bin/cisp.bat` (BATCH | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.013)
- **Top Global Matches:** file_cluster_2: 2.013, file_cluster_17: 4.937, file_cluster_13: 6.224
- **Magnitude:** 15.3 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 72.242
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.66 | **LOC:** 83 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 72.242
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

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lisp.cbl` -> **Severity: 4.762** (Bridge: 0.0476 * Flux: 99.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `logger.cbl` -> **Severity: 41.844** (Embedded: 0.7143 * Error Risk: 58.5809%)
- `recursion.cbl` -> **Severity: 20.856** (Embedded: 0.3214 * Error Risk: 64.8861%)
- `cisp-error.cbl` -> **Severity: 11.674** (Embedded: 0.1905 * Error Risk: 61.2886%)
- `tokenizer.cbl` -> **Severity: 11.098** (Embedded: 0.1429 * Error Risk: 77.6847%)
- `lisp.cbl` -> **Severity: 9.609** (Embedded: 0.1429 * Error Risk: 67.2607%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `logger.cbl` -> **Severity: 17948.45** (Blast Radius: 358.969 * Doc Risk: 50.0%)
- `recursion.cbl` -> **Severity: 7018.8** (Blast Radius: 140.376 * Doc Risk: 50.0%)
- `cisp-error.cbl` -> **Severity: 4925.5** (Blast Radius: 98.51 * Doc Risk: 50.0%)
- `lisp.cbl` -> **Severity: 4635.5** (Blast Radius: 92.71 * Doc Risk: 50.0%)
- `tokenizer.cbl` -> **Severity: 4635.5** (Blast Radius: 92.71 * Doc Risk: 50.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `6` files carry mainframe facts -- `30` call sites, `4` dataset bindings, `150` record items.

### `tokenizer.cbl` (COBOL)
- **Calls:** `CALL LOGGER`
- **Datasets:** `DYNAMIC(INPUT)`
- **Record layouts (47 items):** `WS-FORMAT-LISP (9)`, `WS-PARSE-STR (8)`, `WS-SYMBOL-FLAGS (5)`, `LS-LISP-SYMBOLS (4)`, `WS-LOG-RECORD (3)`, `WS-LISP-EOF (2)`, `WS-IS-COMMENT (2)`, `WS-FLAG (2)`, `IN-LISP-RECORD⟵LISP-FILE (1)`, `WS-LISP-NAME (1)`, `WS-IN-LISP-RECORD (1)`, `WS-LISP-LENGTH (1)` … (+8 more)
- **Data moves:** 75 (ADD 18, MOVE 36, STRING 15, SUBTRACT 5, UNSTRING 1); most-fed items `WS-IN-LISP-RECORD`, `WS-CALC-LENGTH-STR`, `WS-PAREN-TEMP-NUM`, `WS-PAREN-TEMP-STR`, `WS-TEMP-NUM`, `LS-SYMBOL`

### `recursion.cbl` (COBOL)
- **Calls:** `CALL LOGGER`
- **Datasets:** `STACK.DAT(I-O/OUTPUT)`
- **Record layouts (42 items):** `WS-CALL-STACK (9)`, `CALL-STACK-FILE⟵CALL-STACK (8)`, `LS-RECURSION-OBJECT (6)`, `WS-STACK-STATUS (5)`, `WS-RETURN (3)`, `WS-LOG-RECORD (3)`, `WS-CALL-STACK-FILE-STATUS (2)`, `WS-IS-LAST-EXPRESSION (2)`, `WS-CALL-STACK-EOF (1)`, `WS-CALL-STACK-NEXT-ID (1)`, `WS-LOG-OPERATION-FLAG (1)`, `LS-RECURSION-FLAG (1)`
- **Keyed files:** `CALL-STACK INDEXED/RANDOM key COMMAND-ID`
- **Data moves:** 51 (ADD 1, MOVE 37, READ 1, STRING 12); most-fed items `WS-LOG-RECORD-MESSAGE`, `COMMAND-ID`, `LS-COMMAND-NAME`, `LS-COMMAND-RESULT`, `WS-LAST-ID`, `COMMAND-NAME`

### `lisp.cbl` (COBOL)
- **Calls:** `CALL RECURSION`, `CALL LOGGER`, `CALL CISP-ERROR`
- **Record layouts (27 items):** `WS-RECURSION-OBJECT (6)`, `WS-ERROR (5)`, `LS-LISP-SYMBOLS (4)`, `WS-LOG-RECORD (3)`, `WS-INIT-COMMAND (2)`, `WS-SYMBOL-TABLE-INDEX (1)`, `WS-CURR-COMMAND (1)`, `WS-CURRENT-VALUE (1)`, `WS-CURRENT-VALUE-NUMERIC (1)`, `WS-CISP-ERROR-FLAG (1)`, `WS-LOG-OPERATION-FLAG (1)`, `WS-RECURSION-FLAG (1)`
- **Data moves:** 32 (ADD 1, MOVE 23, STRING 8); most-fed items `WS-CURR-COMMAND`, `WS-COMMAND-NAME`, `WS-CURRENT-VALUE`, `WS-LOG-RECORD-MESSAGE`, `WS-COMMAND-RESULT`, `WS-COMMAND-RESULT-NUMERIC`

### `cisp.cbl` (COBOL)
- **Calls:** `CALL LOGGER`, `CALL TOKENIZER`, `CALL LISP`
- **Datasets:** `..\TEST\TESTS-LISTS.TXT(declared)`
- **Record layouts (14 items):** `WS-LISP-SYMBOLS (4)`, `WS-CMD-LINE (3)`, `WS-LOG-RECORD (3)`, `WS-LISP-FILE-NAME (2)`, `LISP-TEST-FILE-NAME⟵TESTS-FILE (1)`, `WS-LOG-OPERATION-FLAG (1)`
- **Data moves:** 14 (ACCEPT 2, MOVE 12); most-fed items `WS-LISP-FILE-NAME`

### `cisp-error.cbl` (COBOL)
- **Calls:** `CALL LOGGER`, `CALL RECURSION`
- **Record layouts (11 items):** `LS-ERROR (5)`, `WS-LOG-RECORD (3)`, `WS-LOG-OPERATION-FLAG (1)`, `WS-RECURSION-FLAG (1)`, `LS-CISP-ERROR-FLAG (1)`
- **Data moves:** 10 (MOVE 5, STRING 5); most-fed items `WS-LOG-RECORD-MESSAGE`

### `logger.cbl` (COBOL)
- **Datasets:** `DYNAMIC(OUTPUT)`
- **Record layouts (9 items):** `LOG-RECORD⟵LOG-FILE (4)`, `LS-LOG-RECORD (3)`, `WS-LOG-FILE-NAME (1)`, `LS-LOG-OPERATION-FLAG (1)`
- **Data moves:** 10 (ADD 2, MOVE 8); most-fed items `LOG-RECORD-FUNCTION-NAME`, `LOG-RECORD-MESSAGE`

- **Mainframe skeleton completeness:** 67% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: JCL and PROC libraries (1 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 84 call pairs -- scoped 65.5%, unique 34.5%, ambiguous 0.0%, external 0.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 84 | 65.5% | 34.5% | 0.0% | 0.0% |

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
