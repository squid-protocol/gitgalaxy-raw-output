# ARCHITECTURAL_BRIEF: zopeneditor-sample
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/IBM/zopeneditor-sample.git` |
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
- **Scope:** 47 analyzed artifact(s), 2261 LOC.
- **Load-bearing artifact:** `COBOL/SAM1.cbl` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `JCL/RUN.jcl` -- pulls in 14 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `COBOL/SAM1.cbl` at magnitude 254.24 (structural weight, not risk).
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
| Total Artifacts | 58 |
| Analyzed Artifacts (Scanned) | 47 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11 |
| Total LOC | 2261 |
| Volatility Index | 0.191 |
| % Scanned of codebase = | 81.0% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6895 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.3203 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5517 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 10 | 680 | 21.3% |
| JCL | 10 | 464 | 21.3% |
| PLAINTEXT | 7 | 0 | 14.9% |
| REXX | 4 | 100 | 8.5% |
| SHELL | 4 | 95 | 8.5% |
| PLI | 3 | 454 | 6.4% |
| YAML | 3 | 131 | 6.4% |
| HLASM | 2 | 131 | 4.3% |
| MARKDOWN | 2 | 0 | 4.3% |
| JSON | 2 | 206 | 4.3% |

## 4.1 SOURCE ENCODINGS
All 47 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 40%, Declarative / Non-Code 23%, Large Core Modules 21%, Interface Declarations Files 6%, Compute Cores Files 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 38 | 80.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 19.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.code-workspace')
- `.inc`: 4x Unresolved Ambiguity (No Retainable Structure)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.asm`: 1x Excluded (Lexical Monotony: High structural repetition detected in 6433 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 75.8 | 12.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.3 | 34.2 | 50.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 37.8 | 2.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 4.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 3.5 | 0.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 38.7 | 22.3 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 4.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 21.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 47.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 9 | 3 | 0 | `COPYBOOK/TRANREC.cpy` |
| cleanup | 41 | 12 | 3 | `JCL/ALLOCATE.jcl` |
| guards | 34 | 12 | 1 | `ASMCOPY/REGISTRS.asm` |
| danger | 59 | 9 | 2 | `zowe/zowecli-cobol-upload-run-tutorial.sh` |
| concurrency | 35 | 10 | 3 | `JCL/ALLOCATE.jcl` |
| connectivity | 5 | 5 | 0 | `ASM/ASAM1.asm` |
| io | 235 | 14 | 20 | `JCL/RUN.jcl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 2 | 0 | `zowe/zowecli-create-profiles.sh` |
| time | 11 | 6 | 1 | `COBOL/SAM1.cbl` |
| serialization | 0 | 0 | 0 | - |
| regex | 4 | 2 | 0 | `COBOL/SAM1.cbl` |
| events | 16 | 8 | 2 | `JCL/ALLOCATE.jcl` |
| tests | 0 | 0 | 0 | - |
| docs | 9 | 5 | 0 | `multiroot/sam/zapp.yaml` |
| debt | 70 | 12 | 3 | `REXX/RSAM1.rexx` |
| mutation | 825 | 22 | 61 | `JCL/RUN.jcl` |
| dead_code | 8 | 5 | 0 | `zowe/zowecli-cobol-clean.sh` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `JCL/RUN.jcl` (Hits: 33)
- `JCL/RUNPSAM1.jcl` (Hits: 27)
- `COBOL/SAM1.cbl` (Hits: 23)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **SAM1.cbl** (`COBOL/SAM1.cbl`) — 2 inbound connections
2. **CUSTCOPY.cpy** (`COPYBOOK/CUSTCOPY.cpy`) — 2 inbound connections
3. **TRANREC.cpy** (`COPYBOOK/TRANREC.cpy`) — 2 inbound connections
4. **PSAM2.pli** (`PLI/PSAM2.pli`) — 2 inbound connections
5. **ASAM1.asm** (`ASM/ASAM1.asm`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **RUN.jcl** (`JCL/RUN.jcl`) — 14 outbound dependencies
2. **RUNPSAM1.jcl** (`JCL/RUNPSAM1.jcl`) — 13 outbound dependencies
3. **RUNASAM1.jcl** (`JCL/RUNASAM1.jcl`) — 11 outbound dependencies
4. **ALLOCATE.jcl** (`JCL/ALLOCATE.jcl`) — 7 outbound dependencies
5. **PLIALLOC.jcl** (`JCL/PLIALLOC.jcl`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `PSAM1` **(I/O & Config Routines)** (@ `PLI/PSAM1.pli`) -> Impact: **25.0** | LOC: 260
- `PSAM1` **(I/O & Config Routines)** (@ `PLI/PSAM1LIB.pli`) -> Impact: **24.5** | LOC: 250
- `100-VALIDATE-TRAN` **(I/O & Config Routines)** (@ `COBOL/SAM2.cbl`) -> Impact: **19.0** | LOC: 40
- `200-PROCESS-TRAN` **(I/O & Config Routines)** (@ `COBOL/SAM2.cbl`) -> Impact: **13.4** | LOC: 29
- `ASAM1` **(I/O & Config Routines)** (@ `ASM/ASAM1.asm`) -> Impact: **13.3** | LOC: 186
- `PSAM2` **(Many-Argument Workhorses)** (@ `PLI/PSAM2.pli`) -> Impact: **12.9** | LOC: 84
- `100-PROCESS-TRANSACTIONS` **(I/O & Config Routines)** (@ `COBOL/SAM1.cbl`) -> Impact: **12.6** | LOC: 31
- `file2` **(I/O & Config Routines)** (@ `REXX/RSAM1.rexx`) -> Impact: **9.6** | LOC: 51
- `710-READ-TRAN-FILE` **(I/O & Config Routines)** (@ `COBOL/SAM1.cbl`) -> Impact: **9.0** | LOC: 20
- `730-READ-CUSTOMER-FILE` **(I/O & Config Routines)** (@ `COBOL/SAM1.cbl`) -> Impact: **7.8** | LOC: 16

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `COBOL` | 2 | 408.52 | 68.79% | 4.24% |
| `PLI` | 3 | 278.08 | 56.87% | 12.58% |
| `JCL` | 8 | 80.24 | 0.0% | 0.0% |
| `__monolith__` | 5 | 72.66 | 0.7% | 0.0% |
| `zowe` | 4 | 61.5 | 20.22% | 0.0% |
| `REXX` | 2 | 50.2 | 28.86% | 0.0% |
| `ASM` | 1 | 18.6 | 5.97% | 0.0% |
| `ASMCOPY` | 1 | 15.32 | 0.0% | 0.0% |
| `multiroot/sam` | 1 | 15.28 | 2.56% | 0.0% |
| `JCLLIB` | 1 | 14.56 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `PLI/PSAM2.pli` -> **37.7541%** Exposure
- `REXXINC/FIBFORM.rexx` -> **37.7541%** Exposure
- `COBOL/SAM1.cbl` -> **8.4703%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `COBOL/SAM2.cbl` -> **100.0%** Exposure
- `PLI/PSAM2.pli` -> **100.0%** Exposure
- `COBOL/SAM1.cbl` -> **99.9999%** Exposure
- `zowe/zowecli-cobol-upload-run-tutorial.sh` -> **99.9999%** Exposure
- `PLI/PSAM1LIB.pli` -> **99.9995%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `PLI/PSAM2.pli` -> **1** Orphaned Functions | **0** Duplicates
- `REXXINC/FIBFORM.rexx` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `80` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `COBOL/SAM1.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.7)
- **Top Global Matches:** file_cluster_2: 6.7, file_cluster_11: 6.962, file_cluster_15: 7.028
- **Magnitude:** 254.24 | **LOC:** 505 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 40.314; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.4%), Complexity Load (formerly Cognitive Load) (61.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `100-PROCESS-TRANSACTIONS` **(I/O & Config Routines)** (Impact: 12.6)
  * `710-READ-TRAN-FILE` **(I/O & Config Routines)** (Impact: 9.0)
  * `730-READ-CUSTOMER-FILE` **(I/O & Config Routines)** (Impact: 7.8)
  * `740-WRITE-CUSTOUT-FILE` **(I/O & Config Routines)** (Impact: 6.8)
  * `700-OPEN-FILES` **(I/O & Config Routines)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 57`, `args: 4`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 73`, `planned_debt: 1`
* *Architecture:* `io: 23`, `import: 4`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 40.314
  * `Choke Point (Betweenness):` 0.003673 | `Ripple Effect (Closeness):` 0.045
  * `Imports (Out-Degree: 3):` CUSTCOPY, TRANREC
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `COBOL/SAM2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.651)
- **Top Global Matches:** file_cluster_6: 7.651, file_cluster_8: 12.566, file_cluster_4: 13.895
- **Magnitude:** 154.28 | **LOC:** 159 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 26.715; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.3%), Complexity Load (formerly Cognitive Load) (75.8%), Connectivity (formerly Api Exposure) (2.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `100-VALIDATE-TRAN` **(I/O & Config Routines)** (Impact: 19.0)
  * `200-PROCESS-TRAN` **(I/O & Config Routines)** (Impact: 13.4)
  * `000-MAIN` **(I/O & Config Routines)** (Impact: 4.7)
  * `310-CRUNCH-LOOP` **(I/O & Config Routines)** (Impact: 4.6)
  * `300-PROCESS-CPU-CRUNCH` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 15`, `args: 4`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 37`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.715
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.04
  * `Imports (Out-Degree: 2):` CUSTCOPY, TRANREC
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `PLI/PSAM1.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.075)
- **Top Global Matches:** file_cluster_11: 7.075, file_cluster_2: 7.774, file_cluster_15: 7.876
- **Magnitude:** 109.64 | **LOC:** 315 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 28.29; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.4%), Complexity Load (formerly Cognitive Load) (52.9%), Connectivity (formerly Api Exposure) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PSAM1` **(I/O & Config Routines)** (Impact: 25.0)
  * `TRANTOT` **(I/O & Config Routines)** (Impact: 5.1)
  * `PRTHDG1` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 63`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`
* *Architecture:* `io: 20`, `api: 1`, `import: 2`
* *Defense:* `safety: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.29
  * `Choke Point (Betweenness):` 0.000408 | `Ripple Effect (Closeness):` 0.02
  * `Imports (Out-Degree: 1):` BALSTATS, CUSTPLI
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `PLI/PSAM1LIB.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.14)
- **Top Global Matches:** file_cluster_11: 7.14, file_cluster_2: 7.831, file_cluster_15: 7.926
- **Magnitude:** 108.78 | **LOC:** 305 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 15.292; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.5%), Complexity Load (formerly Cognitive Load) (59.8%), Connectivity (formerly Api Exposure) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PSAM1` **(I/O & Config Routines)** (Impact: 24.5)
  * `TRANTOT` **(I/O & Config Routines)** (Impact: 5.1)
  * `PRTHDG1` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 52`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`
* *Architecture:* `io: 20`, `api: 1`, `import: 4`
* *Defense:* `safety: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BALSTATS, CUSTPLI, DATETIME, REPTTOTL
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `PLI/PSAM2.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.984)
- **Top Global Matches:** file_cluster_2: 5.984, file_cluster_15: 6.355, file_cluster_13: 6.423
- **Magnitude:** 59.66 | **LOC:** 86 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 52.338; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.8%), Complexity Load (formerly Cognitive Load) (57.9%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PSAM2` **(Many-Argument Workhorses)** (Impact: 12.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 7`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 20`, `unreferenced_by_name: 1`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 52.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.045
  * `Imports (Out-Degree: 0):` BALSTATS, CUSTPLI
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `REXX/RSAM1.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.131)
- **Top Global Matches:** file_cluster_9: 8.131, file_cluster_2: 9.007, file_cluster_15: 9.296
- **Magnitude:** 31.4 | **LOC:** 133 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Guard Balance (formerly Safety Score) (53.5%), Complexity Load (formerly Cognitive Load) (27.9%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `file2` **(I/O & Config Routines)** (Impact: 9.6)
  * `file1` **(I/O & Config Routines)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 19`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 5`
* *Architecture:* `io: 9`
* *Defense:* `safety: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zowe/zowecli-cobol-upload-run-tutorial.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 6.426)
- **Top Global Matches:** file_cluster_14: 6.426, file_cluster_7: 13.271, file_cluster_5: 16.753
- **Magnitude:** 28.36 | **LOC:** 55 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.3%), Dead Code Surface (formerly Dead Code) (56.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 11`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 10`, `dead_code: 2`
* *Architecture:* None
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `REXX/FIB.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.78)
- **Top Global Matches:** file_cluster_2: 6.78, file_cluster_15: 6.921, file_cluster_17: 7.894
- **Magnitude:** 18.8 | **LOC:** 40 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.7%), Complexity Load (formerly Cognitive Load) (29.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fibonacci` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* /******************************************************************************* * Prints the fibona...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 5`
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zapp-example.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.135)
- **Top Global Matches:** file_cluster_2: 2.135, file_cluster_17: 4.936, file_cluster_13: 6.29
- **Magnitude:** 18.74 | **LOC:** 187 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ASM/ASAM1.asm` (HLASM | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.317)
- **Top Global Matches:** file_cluster_2: 6.317, file_cluster_13: 7.311, file_cluster_15: 7.409
- **Magnitude:** 18.6 | **LOC:** 188 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 28.29; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Mutation Surface (formerly State Flux) (15.4%), Complexity Load (formerly Cognitive Load) (6.0%), Connectivity (formerly Api Exposure) (2.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ASAM1` **(I/O & Config Routines)** (Impact: 13.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 93`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 4`, `api: 1`, `import: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.29
  * `Choke Point (Betweenness):` 0.000408 | `Ripple Effect (Closeness):` 0.02
  * `Imports (Out-Degree: 1):` REGISTRS
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `JCL/RUN.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.322)
- **Top Global Matches:** file_cluster_11: 6.322, file_cluster_15: 7.307, file_cluster_2: 7.911
- **Magnitude:** 18.52 | **LOC:** 168 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 15.292; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (52.2%), Mutation Surface (formerly State Flux) (42.1%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CMPLSAM1` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* //SYSUT10 DD UNIT=&SPACE1 //SYSUT11 DD UNIT=&SPACE1 //SYSUT12 DD UNIT=&SPACE1 //SYSUT13 DD UNIT=&SPA...
  * `CMPLSAM2` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* //* //***************************************************************** // SET HLQ='IBMUSER' *TSO US...
  * `SAM1` **(I/O & Config Routines)** (Impact: 2.0)
    * *Intent:* //* CLEAN UP //************************* //DELETE EXEC PGM=IEFBR14 //SYSPRINT DD SYSOUT=* //SYSOUT D...
  * `LINKSAM1` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /* //* //*************************** //* * //* LINK SAM1 * //* * //*************************** //*...
  * `LINKSAM2` **(Interface Declarations)** (Impact: 1.5)
    * *Intent:* //SYSUT9 DD UNIT=&SPACE1 //SYSUT10 DD UNIT=&SPACE1 //SYSUT11 DD UNIT=&SPACE1 //SYSUT12 DD UNIT=&SPAC...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 74`, `args: 2`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `io: 33`
* *Defense:* `sync_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` &CMPLLIB, &HLQ..SAMPLE.COBOL(SAM1), &HLQ..SAMPLE.COBOL(SAM2), &HLQ..SAMPLE.COPY, &HLQ..SAMPLE.COPYLIB, &HLQ..SAMPLE.CUSTFILE, &HLQ..SAMPLE.CUSTOUT, &HLQ..SAMPLE.CUSTRPT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zapp.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.022)
- **Top Global Matches:** file_cluster_2: 2.022, file_cluster_17: 4.89, file_cluster_13: 6.249
- **Magnitude:** 17.12 | **LOC:** 123 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Complexity Load (formerly Cognitive Load) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zcodeformat-example.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.04)
- **Top Global Matches:** file_cluster_2: 2.04, file_cluster_17: 4.902, file_cluster_13: 6.245
- **Magnitude:** 15.38 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ASMCOPY/REGISTRS.asm` (HLASM | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 6.97)
- **Top Global Matches:** file_cluster_17: 6.97, file_cluster_2: 7.018, file_cluster_15: 8.487
- **Magnitude:** 15.32 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 39.34; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.026667
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zowe/zowecli-cobol-clean.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 5.922)
- **Top Global Matches:** file_cluster_14: 5.922, file_cluster_7: 11.667, file_cluster_5: 15.401
- **Magnitude:** 15.3 | **LOC:** 26 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (80.0%), Dead Code Surface (formerly Dead Code) (64.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 4`, `dead_code: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `multiroot/sam/zapp.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.121)
- **Top Global Matches:** file_cluster_2: 2.121, file_cluster_17: 4.94, file_cluster_13: 6.269
- **Magnitude:** 15.28 | **LOC:** 25 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 27.316; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (2.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 27.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.026667
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zcodeformat.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.115)
- **Top Global Matches:** file_cluster_2: 2.115, file_cluster_17: 4.936, file_cluster_13: 6.267
- **Magnitude:** 15.22 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCLLIB/COMPSET.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.922)
- **Top Global Matches:** file_cluster_2: 5.922, file_cluster_17: 6.84, file_cluster_13: 7.338
- **Magnitude:** 14.56 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 28.29; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `JCL/RUNASAM1.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.278)
- **Top Global Matches:** file_cluster_11: 6.278, file_cluster_15: 7.529, file_cluster_2: 8.141
- **Magnitude:** 13.42 | **LOC:** 76 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 15.292; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (52.9%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ASM1` **(Parameter Forwarders)** (Impact: 2.0)
    * *Intent:* // SET SPACE1='SYSALLDA,SPACE=(CYL,(1,1))' *SPACE ALLOCATION //************************* //* CLEAN U...
  * `EXECUTE` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /* //************************* //* RUN ASAM1 //*************************
  * `LKED` **(Interface Declarations)** (Impact: 1.5)
    * *Intent:* //SYSLIB DD DISP=SHR,DSN=&MACLIB // DD DISP=SHR,DSN=&MODGEN // DD DISP=SHR,DSN=&SCEEMAC // DD DISP=S...
  * `DELETE` **(Interface Declarations)** (Impact: 1.4)
    * *Intent:* //* //* THE FOLLOWING SYMBOLICS NEED TO BE UPDATED WITH THE ASSEMBLER //* LIBRARIES AND YOUR TSO USE...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 33`, `args: 1`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 21`
* *Defense:* `safety: 1`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` &HLQ..SAMPLE.ASM(ASAM1), &HLQ..SAMPLE.ASM.FILEIN, &HLQ..SAMPLE.ASM.FILEOUT, &HLQ..SAMPLE.ASMCOPY, &HLQ..SAMPLE.ASMLOAD, &HLQ..SAMPLE.ASMOBJ, &HLQ..SAMPLE.ASMOBJ(ASAM1), &LINKLIB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/RUNPSAM1.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.497)
- **Top Global Matches:** file_cluster_11: 6.497, file_cluster_15: 7.506, file_cluster_2: 8.315
- **Magnitude:** 13.2 | **LOC:** 86 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 15.292; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (51.4%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CMPPSAM1` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* //************************* //* COMPILE PSAM2 //************************* //CMPPSAM2 EXEC PGM=IBMZPL...
  * `CMPPSAM2` **(Parameter Forwarders)** (Impact: 1.8)
    * *Intent:* //* //************************* //* CLEAN UP //************************* //DELETE EXEC PGM=IEFBR14 /...
  * `LNKPSAM1` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* //************************* //CMPPSAM1 EXEC PGM=IBMZPLI,PARM='LIST,MAP,RULES(LAXIF)' //STEPLIB DD DI...
  * `RUNPSAM1` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* //* //************************* //* RUN PSAM1 //*************************
  * `DELETE` **(Interface Declarations)** (Impact: 1.3)
    * *Intent:* //***************************************************************** //* //* THE FOLLOWING SYMBOLICS ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 36`, `args: 2`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 27`
* *Defense:* `safety: 1`, `sync_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` &CMPLLIB, &HLQ..SAMPLE.PLI(PSAM1), &HLQ..SAMPLE.PLI(PSAM2), &HLQ..SAMPLE.PLI.CUSTFILE, &HLQ..SAMPLE.PLI.CUSTRPT, &HLQ..SAMPLE.PLI.INCLLIB, &HLQ..SAMPLE.PLI.TRANFILE, &HLQ..SAMPLE.PLILOAD...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zowe/zowecli-create-profiles.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.824)
- **Top Global Matches:** file_cluster_2: 4.824, file_cluster_17: 6.794, file_cluster_13: 7.617
- **Magnitude:** 11.0 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (56.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `REXXLIB/HELLO.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.187)
- **Top Global Matches:** file_cluster_2: 5.187, file_cluster_17: 6.914, file_cluster_13: 7.871
- **Magnitude:** 10.52 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/PLIALLOC.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.858)
- **Top Global Matches:** file_cluster_2: 6.858, file_cluster_17: 8.262, file_cluster_15: 8.309
- **Magnitude:** 8.82 | **LOC:** 91 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 15.292; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Mutation Surface (formerly State Flux) (21.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ALLOCAT` **(I/O & Config Routines)** (Impact: 3.1)
    * *Intent:* // UNIT=SYSDA,SPACE=(CYL,(0)) //DD5 DD DSN=&HLQ..SAMPLE.PLI.TRANFILE, // DISP=(MOD,DELETE,DELETE), /...
  * `DELETE` **(I/O & Config Routines)** (Impact: 2.3)
    * *Intent:* //* //* US GOVERNMENT USERS RESTRICTED RIGHTS - USE, DUPLICATION, //* OR DISCLOSURE RESTRICTED BY GS...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 20`
* *Defense:* `safety: 1`, `sync_locks: 7`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.PLI, &HLQ..SAMPLE.PLI.CUSTFILE, &HLQ..SAMPLE.PLI.INCLLIB, &HLQ..SAMPLE.PLI.TRANFILE, &HLQ..SAMPLE.PLILOAD, &HLQ..SAMPLE.PLINC, &HLQ..SAMPLE.PLIOBJ
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/ALLOCATE.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.93)
- **Top Global Matches:** file_cluster_2: 6.93, file_cluster_17: 8.317, file_cluster_15: 8.36
- **Magnitude:** 8.56 | **LOC:** 90 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 15.292; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (50.0%), Mutation Surface (formerly State Flux) (22.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ALLOCAT` **(I/O & Config Routines)** (Impact: 3.0)
    * *Intent:* // UNIT=SYSDA,SPACE=(CYL,(0)) //DD5 DD DSN=&HLQ..SAMPLE.TRANFILE, // DISP=(MOD,DELETE,DELETE), // UN...
  * `DELETE` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* //* //* US GOVERNMENT USERS RESTRICTED RIGHTS - USE, DUPLICATION, //* OR DISCLOSURE RESTRICTED BY GS...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 20`
* *Defense:* `safety: 1`, `sync_locks: 7`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.COBOL, &HLQ..SAMPLE.COPY, &HLQ..SAMPLE.COPYLIB, &HLQ..SAMPLE.CUSTFILE, &HLQ..SAMPLE.LOAD, &HLQ..SAMPLE.OBJ, &HLQ..SAMPLE.TRANFILE
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/ASMALLOC.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.99)
- **Top Global Matches:** file_cluster_2: 6.99, file_cluster_17: 8.35, file_cluster_15: 8.391
- **Magnitude:** 7.56 | **LOC:** 74 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 15.292; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Mutation Surface (formerly State Flux) (29.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ALLOCAT` **(I/O & Config Routines)** (Impact: 2.5)
    * *Intent:* // UNIT=SYSDA,SPACE=(CYL,(0)) //DD3 DD DSN=&HLQ..SAMPLE.ASM, // DISP=(MOD,DELETE,DELETE), // UNIT=SY...
  * `DELETE` **(I/O & Config Routines)** (Impact: 2.0)
    * *Intent:* //* //* US GOVERNMENT USERS RESTRICTED RIGHTS - USE, DUPLICATION, //* OR DISCLOSURE RESTRICTED BY GS...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 18`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 16`
* *Defense:* `safety: 1`, `sync_locks: 5`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.ASM, &HLQ..SAMPLE.ASM.FILEIN, &HLQ..SAMPLE.ASMCOPY, &HLQ..SAMPLE.ASMLOAD, &HLQ..SAMPLE.ASMOBJ
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `ASMCOPY/REGISTRS.asm` (HLASM) | Magnitude: 15.32 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: immutability_locks: 16

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `zowe/zowecli-cobol-upload-run-tutorial.sh` -> Churn: **100.0%** | Cog Load: 53.9915% | Debt: 0.0%

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `COBOL/SAM1.cbl` -> **Severity: 0.367** (Bridge: 0.0037 * Flux: 99.9999%)
- `PLI/PSAM1.pli` -> **Severity: 0.041** (Bridge: 0.0004 * Flux: 99.9984%)
- `ASM/ASAM1.asm` -> **Severity: 0.006** (Bridge: 0.0004 * Flux: 15.3898%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `PLI/PSAM2.pli` -> **Severity: 3.547** (Embedded: 0.045 * Error Risk: 78.8229%)
- `COBOL/SAM2.cbl` -> **Severity: 3.294** (Embedded: 0.04 * Error Risk: 82.3402%)
- `COBOL/SAM1.cbl` -> **Severity: 3.079** (Embedded: 0.045 * Error Risk: 68.4268%)
- `PLI/PSAM1.pli` -> **Severity: 1.287** (Embedded: 0.02 * Error Risk: 64.353%)
- `JCLLIB/COMPSET.jcl` -> **Severity: 1.043** (Embedded: 0.02 * Error Risk: 52.1415%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `PLI/PSAM2.pli` -> **Severity: 5233.8** (Blast Radius: 52.338 * Doc Risk: 100.0%)
- `COBOL/SAM1.cbl` -> **Severity: 4031.4** (Blast Radius: 40.314 * Doc Risk: 100.0%)
- `ASM/ASAM1.asm` -> **Severity: 2829.0** (Blast Radius: 28.29 * Doc Risk: 100.0%)
- `PLI/PSAM1.pli` -> **Severity: 2829.0** (Blast Radius: 28.29 * Doc Risk: 100.0%)
- `COBOL/SAM2.cbl` -> **Severity: 2671.5** (Blast Radius: 26.715 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `23` files carry mainframe facts -- `27` call sites, `109` dataset bindings, `361` record items.

### `COBOL/SAM1.cbl` (COBOL)
- **Calls:** `CALL SAM2`
- **Datasets:** `CUSTFILE(INPUT)`, `CUSTOUT(OUTPUT)`, `TRANFILE(INPUT)`, `CUSTRPT(OUTPUT)`
- **Record layouts (104 items):** `REPORT-TOTALS (15)`, `WS-FIELDS (15)`, `RPT-HEADER1 (14)`, `SYSTEM-DATE-AND-TIME (10)`, `RPT-STATS-DETAIL (9)`, `MSG-TRAN-SCALE-1 (5)`, `MSG-TRAN-SCALE-2 (5)`, `ERR-MSG-BAD-TRAN (4)`, `ERR-MSG-BAD-TRAN-2 (4)`, `RPT-TRAN-DETAIL1 (4)`, `RPT-STATS-HDR2 (4)`, `RPT-STATS-HDR3 (4)` … (+4 more)
- **Data moves:** 93 (ACCEPT 4, ADD 7, COMPUTE 7, MOVE 60, WRITE 15); most-fed items `REPORT-RECORD`, `ERR-MSG-DATA2`, `RPT-NUM-TRAN-ERR`, `RPT-NUM-TRAN-PROC`, `RPT-NUM-TRANS`, `CSTOUT-CONTACT-REC`

### `JCL/RUN.jcl` (JCL)
- **Calls:** `EXEC PGM IGYCRCTL`, `EXEC PGM IEWL`, `EXEC PGM IEFBR14`, `EXEC PGM SAM1`
- **Datasets:** `STEPLIB→IGY.V6R5M0.SIGYCOMP`, `SYSIN→IBMUSER.SAMPLE.COBOL(SAM2)`, `SYSLIB→IBMUSER.SAMPLE.COPY`, `SYSLIN→IBMUSER.SAMPLE.OBJ(SAM2)`, `STEPLIB→IGY.V6R5M0.SIGYCOMP`, `SYSIN→IBMUSER.SAMPLE.COBOL(SAM1)`, `SYSLIB→IBMUSER.SAMPLE.COPY`, `MYFILE→IBMUSER.SAMPLE.COPYLIB`, `MYLIB→IBMUSER.SAMPLE.COPYLIB`, `SYSLIN→IBMUSER.SAMPLE.OBJ(SAM1)`, `SYSLMOD→IBMUSER.SAMPLE.LOAD`, `SYSLIB→CEE.SCEELKED` … (+12)
- **Job flow:** `CMPLSAM2=IGYCRCTL` -> `CMPLSAM1=IGYCRCTL` -> `LINKSAM2=IEWL` -> `LINKSAM1=IEWL` -> `DELETE=IEFBR14` -> `SAM1=SAM1`; creates `&HLQ..SAMPLE.CUSTOUT`, `&HLQ..SAMPLE.CUSTRPT`

### `PLI/PSAM1.pli` (PLI)
- **Calls:** `CALL PSAM2`
- **Record layouts (61 items):** `SYSTEM_DATE_AND_TIME (10)`, `TRAN_RECORD (8)`, `HDR2 (3)`, `HDR3 (3)`, `DUMP_FINDER (1)`, `TRAN_COMMENT (1)`, `TRAN_RECORD_ALL (1)`, `TRANFILE_EOF (1)`, `CUSTFILE_EOF (1)`, `TRAN_OK_FLAG (1)`, `NUM_TRANFILE_RECS (1)`, `NUM_TRAN_ERRORS (1)` … (+29 more)
- **Data moves:** 35 (ASSIGN 35); most-fed items `NUMB_11`, `NUM_TRANSACTIONS`, `NUMA_11`, `NUM_PRINT_COMPLETED`, `NUMA_7V2`, `NUMB_7V2`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/0` RESP results tested

### `PLI/PSAM1LIB.pli` (PLI)
- **Calls:** `CALL PSAM2`
- **Record layouts (41 items):** `TRAN_RECORD (8)`, `HDR2 (3)`, `HDR3 (3)`, `DUMP_FINDER (1)`, `TRAN_COMMENT (1)`, `TRAN_RECORD_ALL (1)`, `TRANFILE_EOF (1)`, `CUSTFILE_EOF (1)`, `TRAN_OK_FLAG (1)`, `PROGRAM_STATUS (1)`, `MSG_BAD_TRAN (1)`, `MSG_OPEN_ERROR (1)` … (+18 more)
- **Data moves:** 35 (ASSIGN 35); most-fed items `NUMB_11`, `NUM_TRANSACTIONS`, `NUMA_11`, `NUM_PRINT_COMPLETED`, `NUMA_7V2`, `NUMB_7V2`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/0` RESP results tested

### `JCL/RUNPSAM1.jcl` (JCL)
- **Calls:** `EXEC PGM IEFBR14`, `EXEC PGM IBMZPLI`, `EXEC PGM IEWL`, `EXEC PGM PSAM1`
- **Datasets:** `DD1→IBMUSER.SAMPLE.PLI.CUSTRPT`, `STEPLIB→IBMZ.V5R3M0.SIBMZCMP`, `SYSLIB→IBMUSER.SAMPLE.PLINC`, `SYSLIN→IBMUSER.SAMPLE.PLIOBJ(PSAM2)`, `SYSIN→IBMUSER.SAMPLE.PLI(PSAM2)`, `STEPLIB→IBMZ.V5R3M0.SIBMZCMP`, `SYSLIB→IBMUSER.SAMPLE.PLINC`, `MYFILE→IBMUSER.SAMPLE.PLI.INCLLIB`, `MYLIB→IBMUSER.SAMPLE.PLI.INCLLIB`, `SYSLIN→IBMUSER.SAMPLE.PLIOBJ(PSAM1)`, `SYSIN→IBMUSER.SAMPLE.PLI(PSAM1)`, `SYSLIB→CEE.SCEELKED` … (+6)
- **Job flow:** `DELETE=IEFBR14` -> `CMPPSAM2=IBMZPLI` -> `CMPPSAM1=IBMZPLI` -> `LNKPSAM1=IEWL` -> `RUNPSAM1=PSAM1`; creates `&HLQ..SAMPLE.PLI.CUSTRPT`

### `JCL/RUNASAM1.jcl` (JCL)
- **Calls:** `EXEC PGM IEFBR14`, `EXEC PGM ASMA90`, `EXEC PGM IEWL`, `EXEC PGM ASAM1`
- **Datasets:** `DD1→TSOUSER.SAMPLE.ASM.FILEOUT`, `SYSLIB→SYS1.MACLIB`, `SYSLIB→SYS1.MODGEN`, `SYSLIB→CEE.SCEEMAC`, `SYSLIB→TSOUSER.SAMPLE.ASMCOPY`, `SYSPUNCH→TSOUSER.SAMPLE.ASMOBJ(ASAM1)`, `SYSIN→TSOUSER.SAMPLE.ASM(ASAM1)`, `SYSLMOD→TSOUSER.SAMPLE.ASMLOAD`, `SYSLIB→CEE.SCEELKED`, `OBJ→TSOUSER.SAMPLE.ASMOBJ`, `STEPLIB→TSOUSER.SAMPLE.ASMLOAD`, `FILEIN→TSOUSER.SAMPLE.ASM.FILEIN` … (+1)
- **Job flow:** `DELETE=IEFBR14` -> `ASM1=ASMA90` -> `LKED=IEWL` -> `EXECUTE=ASAM1`; creates `&HLQ..SAMPLE.ASM.FILEOUT`

### `COBOL/SAM2.cbl` (COBOL)
- **Record layouts (10 items):** `WS-FIELDS (8)`, `TRAN-OK (1)`, `TRAN-MSG (1)`
- **Data moves:** 37 (COMPUTE 14, MOVE 23); most-fed items `TRAN-COUNT`, `CUST-ACCT-BALANCE`, `CUST-ORDERS-YTD`, `WORK-SUM`, `WS-UPDATE-NUM`, `CUST-NAME`

### `JCL/ALLOCATE.jcl` (JCL)
- **Calls:** `EXEC PGM IEFBR14`
- **Datasets:** `DD1→IBMUSER.SAMPLE.OBJ`, `DD2→IBMUSER.SAMPLE.LOAD`, `DD3→IBMUSER.SAMPLE.COBOL`, `DD4→IBMUSER.SAMPLE.COPY`, `DD5→IBMUSER.SAMPLE.TRANFILE`, `DD6→IBMUSER.SAMPLE.CUSTFILE`, `DD7→IBMUSER.SAMPLE.COPYLIB`, `DD1→IBMUSER.SAMPLE.OBJ`, `DD2→IBMUSER.SAMPLE.LOAD`, `DD3→IBMUSER.SAMPLE.COBOL`, `DD4→IBMUSER.SAMPLE.COPY`, `DD5→IBMUSER.SAMPLE.TRANFILE` … (+2)
- **Job flow:** `DELETE=IEFBR14` -> `ALLOCAT=IEFBR14 (cond)`; creates `&HLQ..SAMPLE.COBOL`, `&HLQ..SAMPLE.COPY`, `&HLQ..SAMPLE.COPYLIB`, `&HLQ..SAMPLE.CUSTFILE`, `&HLQ..SAMPLE.LOAD`, `&HLQ..SAMPLE.OBJ`

### `JCL/PLIALLOC.jcl` (JCL)
- **Calls:** `EXEC PGM IEFBR14`
- **Datasets:** `DD1→IBMUSER.SAMPLE.PLIOBJ`, `DD2→IBMUSER.SAMPLE.PLILOAD`, `DD3→IBMUSER.SAMPLE.PLI`, `DD4→IBMUSER.SAMPLE.PLINC`, `DD5→IBMUSER.SAMPLE.PLI.TRANFILE`, `DD6→IBMUSER.SAMPLE.PLI.CUSTFILE`, `DD7→IBMUSER.SAMPLE.PLI.INCLLIB`, `DD1→IBMUSER.SAMPLE.PLIOBJ`, `DD2→IBMUSER.SAMPLE.PLILOAD`, `DD3→IBMUSER.SAMPLE.PLI`, `DD4→IBMUSER.SAMPLE.PLINC`, `DD5→IBMUSER.SAMPLE.PLI.TRANFILE` … (+2)
- **Job flow:** `DELETE=IEFBR14` -> `ALLOCAT=IEFBR14 (cond)`; creates `&HLQ..SAMPLE.PLI`, `&HLQ..SAMPLE.PLI.CUSTFILE`, `&HLQ..SAMPLE.PLI.INCLLIB`, `&HLQ..SAMPLE.PLI.TRANFILE`, `&HLQ..SAMPLE.PLILOAD`, `&HLQ..SAMPLE.PLINC`

### `JCL/ASMALLOC.jcl` (JCL)
- **Calls:** `EXEC PGM IEFBR14`
- **Datasets:** `DD1→IBMUSER.SAMPLE.ASMOBJ`, `DD2→IBMUSER.SAMPLE.ASMLOAD`, `DD3→IBMUSER.SAMPLE.ASM`, `DD4→IBMUSER.SAMPLE.ASMCOPY`, `DD5→IBMUSER.SAMPLE.ASM.FILEIN`, `DD1→IBMUSER.SAMPLE.ASMOBJ`, `DD2→IBMUSER.SAMPLE.ASMLOAD`, `DD3→IBMUSER.SAMPLE.ASM`, `DD4→IBMUSER.SAMPLE.ASMCOPY`, `DD5→IBMUSER.SAMPLE.ASM.FILEIN`
- **Job flow:** `DELETE=IEFBR14` -> `ALLOCAT=IEFBR14 (cond)`; creates `&HLQ..SAMPLE.ASM`, `&HLQ..SAMPLE.ASM.FILEIN`, `&HLQ..SAMPLE.ASMCOPY`, `&HLQ..SAMPLE.ASMLOAD`, `&HLQ..SAMPLE.ASMOBJ`

### `COPYBOOK/TRANREC.cpy` (COBOL)
- **Record layouts (30 items):** `TRANSACTION-RECORD (30)`

### `multiroot/copybooks/trans/TRANREC.cpy` (COBOL)
- **Record layouts (30 items):** `TRANSACTION-RECORD (30)`

### `JCL/REXALLOC.jcl` (JCL)
- **Calls:** `EXEC PGM IEFBR14`
- **Datasets:** `DD1→TSOUSER.SAMPLE.REXX`, `DD2→TSOUSER.SAMPLE.REXX.FILEIN1`, `DD3→TSOUSER.SAMPLE.REXX.FILEIN2`, `DD4→TSOUSER.SAMPLE.REXX.FILEOUT`, `DD1→TSOUSER.SAMPLE.REXX`, `DD2→TSOUSER.SAMPLE.REXX.FILEIN1`, `DD3→TSOUSER.SAMPLE.REXX.FILEIN2`, `DD4→TSOUSER.SAMPLE.REXX.FILEOUT`
- **Job flow:** `DELETE=IEFBR14` -> `ALLOCAT=IEFBR14 (cond)`; creates `&HLQ..SAMPLE.REXX`, `&HLQ..SAMPLE.REXX.FILEIN1`, `&HLQ..SAMPLE.REXX.FILEIN2`, `&HLQ..SAMPLE.REXX.FILEOUT`

### `COPYBOOK/CUSTCOPY.cpy` (COBOL)
- **Record layouts (27 items):** `:TAG:-REC (16)`, `:TAG:-CONTACT-REC (11)`

### `multiroot/copybooks/cust/CUSTCOPY.cpy` (COBOL)
- **Record layouts (27 items):** `:TAG:-REC (16)`, `:TAG:-CONTACT-REC (11)`

### `JCLPROC/COMPROC.jcl` (JCL)
- **Calls:** `EXEC PGM IGYCRCTL`
- **Datasets:** `STEPLIB→&CMPLLIB`, `SYSIN→&HLQ..SAMPLE.COBOL(SAM2)`, `SYSLIB→&HLQ..SAMPLE.COPY`, `SYSLIN→&HLQ..SAMPLE.OBJ(SAM2)`

### `PLI/PSAM2.pli` (PLI)
- **Record layouts (2 items):** `DUMP_FINDER (1)`, `PROGRAM_STATUS (1)`
- **Data moves:** 25 (ASSIGN 25); most-fed items `BALANCE_AVG`, `BALANCE_MAX`, `BALANCE_MIN`, `BALANCE_RANGE`, `BALANCE_TOTAL`, `BALANCE_COUNT`

### `COPYLIB-MVS/REPTTOTL.cpy` (COBOL)
- **Record layouts (15 items):** `REPORT-TOTALS (15)`

### `COPYLIB/DATETIME.cpy` (COBOL)
- **Record layouts (10 items):** `SYSTEM-DATE-AND-TIME (10)`

### `JCL/INCLUDE.jcl` (JCL)
- **Job flow:** `STEP1=PROC COMPROC`

*(+3 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 92% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: scheduler export (CA-7 / Control-M / TWS) (8 gaps); JCL and PROC libraries (1 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 90 call pairs -- scoped 38.9%, unique 3.3%, ambiguous 0.0%, external 57.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 32 | 96.9% | 3.1% | 0.0% | 0.0% |
| jcl | 24 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 23 | 0.0% | 0.0% | 0.0% | 100.0% |
| pli | 6 | 66.7% | 33.3% | 0.0% | 0.0% |
| hlasm | 5 | 0.0% | 0.0% | 0.0% | 100.0% |

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
