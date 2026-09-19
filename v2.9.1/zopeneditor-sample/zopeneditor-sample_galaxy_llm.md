# ARCHITECTURAL_BRIEF: zopeneditor-sample
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/IBM/zopeneditor-sample.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 48 analyzed artifact(s), 2269 LOC.
- **Load-bearing artifact:** `INCLUDES/BALSTATS.inc` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `JCL/RUN.jcl` -- pulls in 14 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `COBOL/SAM1.cbl` at magnitude 257.24 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 48 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10 |
| Total LOC | 2269 |
| Volatility Index | 0.021 |
| % Scanned of codebase = | 82.8% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6667 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.7071 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.1429 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 10 | 680 | 20.8% |
| JCL | 10 | 464 | 20.8% |
| PLAINTEXT | 7 | 0 | 14.6% |
| REXX | 4 | 100 | 8.3% |
| SHELL | 4 | 95 | 8.3% |
| PLI | 3 | 454 | 6.2% |
| YAML | 3 | 131 | 6.2% |
| HLASM | 2 | 131 | 4.2% |
| MARKDOWN | 2 | 0 | 4.2% |
| JSON | 2 | 206 | 4.2% |
| ASSEMBLY | 1 | 8 | 2.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo`
> **Architectural Drift Z-Score:** `3.219`
> **Composition Archetype:** `Small Flat Repo` (z +3.22; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 40%, Declarative / Non-Code 25%, Large Core Modules 21%, Interface Declarations Files 6%, Compute Cores Files 2%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 39 | 81.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 18.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.code-workspace')
- `.inc`: 3x Unresolved Ambiguity (No Retainable Structure)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.asm`: 1x Excluded (Lexical Monotony: High structural repetition detected in 6433 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 75.8 | 11.8 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 41.9 | 60.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 73.1 | 2.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 4.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 3.5 | 0.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 37.7 | 21.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 4.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.6 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 16.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 46.2 | 0.0 | 0.0 |
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
| io | 259 | 15 | 20 | `COBOL/SAM1.cbl` |
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
| dead_code | 9 | 6 | 1 | `zowe/zowecli-cobol-clean.sh` |
| credential | 0 | 0 | 0 | - |
| threat | 12 | 4 | 0 | `COPYBOOK/TRANREC.cpy` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `COBOL/SAM1.cbl` (Hits: 45)
- `JCL/RUN.jcl` (Hits: 33)
- `JCL/RUNPSAM1.jcl` (Hits: 27)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **BALSTATS.inc** (`INCLUDES/BALSTATS.inc`) — 3 inbound connections
2. **REGISTRS.asm** (`ASMCOPY/REGISTRS.asm`) — 1 inbound connections
3. **SAM1.cbl** (`COBOL/SAM1.cbl`) — 1 inbound connections
4. **SAM2PAR5.cpy** (`multiroot/copybooks/trans/SAM2PAR5.cpy`) — 1 inbound connections
5. **COMPSET.jcl** (`JCLLIB/COMPSET.jcl`) — 1 inbound connections

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
- `PSAM2` **(Many-Argument Workhorses)** (@ `PLI/PSAM2.pli`) -> Impact: **12.7** | LOC: 81
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
| `COBOL` | 2 | 412.62 | 68.79% | 18.44% |
| `PLI` | 3 | 278.28 | 56.87% | 0.0% |
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
- `REXXINC/FIBFORM.rexx` -> **73.1059%** Exposure
- `COBOL/SAM2.cbl` -> **22.4524%** Exposure
- `COBOL/SAM1.cbl` -> **14.4232%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `COBOL/SAM2.cbl` -> **100.0%** Exposure
- `PLI/PSAM2.pli` -> **100.0%** Exposure
- `COBOL/SAM1.cbl` -> **99.9999%** Exposure
- `zowe/zowecli-cobol-upload-run-tutorial.sh` -> **99.9999%** Exposure
- `PLI/PSAM1LIB.pli` -> **99.9995%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `COBOL/SAM1.cbl` -> **1** Orphaned Functions | **0** Duplicates
- `COBOL/SAM2.cbl` -> **1** Orphaned Functions | **0** Duplicates
- `REXXINC/FIBFORM.rexx` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `80` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `COBOL/SAM1.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 257.24 | **LOC:** 505 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 30.522; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `100-PROCESS-TRANSACTIONS` **(I/O & Config Routines)** (Impact: 12.6)
  * `710-READ-TRAN-FILE` **(I/O & Config Routines)** (Impact: 9.0)
  * `730-READ-CUSTOMER-FILE` **(I/O & Config Routines)** (Impact: 7.8)
  * `740-WRITE-CUSTOUT-FILE` **(I/O & Config Routines)** (Impact: 6.8)
  * `REPORT-FILE` **(I/O & Config Routines)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 58`, `args: 4`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 73`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 45`, `import: 4`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.522
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.026667
  * `Imports (Out-Degree: 0):` CUSTCOPY, TRANREC
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL/SAM2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 155.38 | **LOC:** 159 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 17.087; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Complexity Load (formerly Cognitive Load) (75.8%), Debt Markers (formerly Tech Debt) (22.5%)
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
* *Structure:* `branch: 34`, `structural_boundaries: 16`, `args: 4`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 37`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CUSTCOPY, TRANREC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `PLI/PSAM1.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 109.84 | **LOC:** 315 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 17.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.3%), Complexity Load (formerly Cognitive Load) (52.9%), Connectivity (formerly Api Exposure) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PSAM1` **(I/O & Config Routines)** (Impact: 25.0)
  * `TRANTOT` **(I/O & Config Routines)** (Impact: 5.1)
  * `PRTHDG1` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 63`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`
* *Architecture:* `io: 20`, `api: 1`, `import: 2`
* *Defense:* `safety: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` BALSTATS, CUSTPLI
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `PLI/PSAM1LIB.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 108.98 | **LOC:** 305 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 17.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.9%), Complexity Load (formerly Cognitive Load) (59.8%), Connectivity (formerly Api Exposure) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PSAM1` **(I/O & Config Routines)** (Impact: 24.5)
  * `TRANTOT` **(I/O & Config Routines)** (Impact: 5.1)
  * `PRTHDG1` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 52`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`
* *Architecture:* `io: 20`, `api: 1`, `import: 4`
* *Defense:* `safety: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` BALSTATS, CUSTPLI, DATETIME, REPTTOTL
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `PLI/PSAM2.pli` (PLI | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 59.46 | **LOC:** 86 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 17.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.9%), Complexity Load (formerly Cognitive Load) (57.9%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PSAM2` **(Many-Argument Workhorses)** (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 7`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` BALSTATS, CUSTPLI
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `REXX/RSAM1.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 31.4 | **LOC:** 133 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Guard Balance (formerly Safety Score) (68.6%), Complexity Load (formerly Cognitive Load) (27.9%), Test Surface (formerly Verification) (2.4%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zowe/zowecli-cobol-upload-run-tutorial.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 28.36 | **LOC:** 55 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Dead Code Surface (formerly Dead Code) (56.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__global_context__` **(Unclassified)** (Impact: 3.0)
  * `Anonymous_Block` **(Unclassified)** (Impact: 2.3)
  * `Anonymous_Block` **(Unclassified)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 11`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 10`, `dead_code: 2`
* *Architecture:* None
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `REXX/FIB.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 18.8 | **LOC:** 40 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.2%), Complexity Load (formerly Cognitive Load) (29.8%), Test Surface (formerly Verification) (2.4%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zapp-example.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 18.74 | **LOC:** 187 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ASM/ASAM1.asm` (HLASM | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 18.6 | **LOC:** 188 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 17.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.9%), Mutation Surface (formerly State Flux) (15.4%), Complexity Load (formerly Cognitive Load) (6.0%), Connectivity (formerly Api Exposure) (2.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ASAM1` **(I/O & Config Routines)** (Impact: 13.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 93`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 4`, `api: 1`, `import: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` REGISTRS
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/RUN.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 18.52 | **LOC:** 168 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 17.087; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Mutation Surface (formerly State Flux) (42.1%), Test Surface (formerly Verification) (2.4%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &CMPLLIB, &HLQ..SAMPLE.COBOL(SAM1), &HLQ..SAMPLE.COBOL(SAM2), &HLQ..SAMPLE.COPY, &HLQ..SAMPLE.COPYLIB, &HLQ..SAMPLE.CUSTFILE, &HLQ..SAMPLE.CUSTOUT, &HLQ..SAMPLE.CUSTRPT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zapp.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 17.12 | **LOC:** 123 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Complexity Load (formerly Cognitive Load) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zcodeformat-example.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ASMCOPY/REGISTRS.asm` (HLASM | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 15.32 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 31.612; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.612
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zowe/zowecli-cobol-clean.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 15.3 | **LOC:** 26 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (97.9%), Dead Code Surface (formerly Dead Code) (64.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__global_context__` **(Unclassified)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 4`, `dead_code: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `multiroot/sam/zapp.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 15.28 | **LOC:** 25 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 30.522; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (2.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.522
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.026667
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zcodeformat.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCLLIB/COMPSET.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 14.56 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 31.612; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.4%), Mutation Surface (formerly State Flux) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.612
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `INCLUDES/BALSTATS.inc` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 14.16 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 38.874; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.06
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `JCL/RUNASAM1.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 13.42 | **LOC:** 76 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 17.087; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (70.2%), Test Surface (formerly Verification) (2.4%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.ASM(ASAM1), &HLQ..SAMPLE.ASM.FILEIN, &HLQ..SAMPLE.ASM.FILEOUT, &HLQ..SAMPLE.ASMCOPY, &HLQ..SAMPLE.ASMLOAD, &HLQ..SAMPLE.ASMOBJ, &HLQ..SAMPLE.ASMOBJ(ASAM1), &LINKLIB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/RUNPSAM1.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 13.2 | **LOC:** 86 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 17.087; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (66.5%), Test Surface (formerly Verification) (2.4%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &CMPLLIB, &HLQ..SAMPLE.PLI(PSAM1), &HLQ..SAMPLE.PLI(PSAM2), &HLQ..SAMPLE.PLI.CUSTFILE, &HLQ..SAMPLE.PLI.CUSTRPT, &HLQ..SAMPLE.PLI.INCLLIB, &HLQ..SAMPLE.PLI.TRANFILE, &HLQ..SAMPLE.PLILOAD...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zowe/zowecli-create-profiles.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 11.0 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (78.3%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__global_context__` **(Unclassified)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `REXXLIB/HELLO.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/PLIALLOC.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 8.82 | **LOC:** 91 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 17.087; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.4%), Mutation Surface (formerly State Flux) (21.9%), Test Surface (formerly Verification) (2.3%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.PLI, &HLQ..SAMPLE.PLI.CUSTFILE, &HLQ..SAMPLE.PLI.INCLLIB, &HLQ..SAMPLE.PLI.TRANFILE, &HLQ..SAMPLE.PLILOAD, &HLQ..SAMPLE.PLINC, &HLQ..SAMPLE.PLIOBJ
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/ALLOCATE.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 8.56 | **LOC:** 90 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 17.087; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (60.1%), Mutation Surface (formerly State Flux) (22.7%), Test Surface (formerly Verification) (2.3%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.COBOL, &HLQ..SAMPLE.COPY, &HLQ..SAMPLE.COPYLIB, &HLQ..SAMPLE.CUSTFILE, &HLQ..SAMPLE.LOAD, &HLQ..SAMPLE.OBJ, &HLQ..SAMPLE.TRANFILE
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `zowe/zowecli-cobol-upload-run-tutorial.sh` -> Churn: **63.09%** | Cog Load: 53.9915% | Debt: 0.0%

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `COBOL/SAM1.cbl` -> **Severity: 2.44** (Embedded: 0.0267 * Error Risk: 91.4923%)
- `JCLLIB/COMPSET.jcl` -> **Severity: 1.368** (Embedded: 0.02 * Error Risk: 68.383%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `COBOL/SAM1.cbl` -> **Severity: 3052.2** (Blast Radius: 30.522 * Doc Risk: 100.0%)
- `ASM/ASAM1.asm` -> **Severity: 1708.7** (Blast Radius: 17.087 * Doc Risk: 100.0%)
- `COBOL/SAM2.cbl` -> **Severity: 1708.7** (Blast Radius: 17.087 * Doc Risk: 100.0%)
- `JCL/ALLOCATE.jcl` -> **Severity: 1708.7** (Blast Radius: 17.087 * Doc Risk: 100.0%)
- `JCL/ASMALLOC.jcl` -> **Severity: 1708.7** (Blast Radius: 17.087 * Doc Risk: 100.0%)

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
