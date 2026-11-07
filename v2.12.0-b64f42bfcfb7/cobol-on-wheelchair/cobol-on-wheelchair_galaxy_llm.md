# ARCHITECTURAL_BRIEF: cobol-on-wheelchair
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/azac/cobol-on-wheelchair` |
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
- **Scope:** 10 analyzed artifact(s), 372 LOC.
- **Load-bearing artifact:** `cowtemplate.cbl` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Dockerfile` -- pulls in 2 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `cowtemplate.cbl` at magnitude 148.2 (structural weight, not risk).
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
| Total Artifacts | 18 |
| Analyzed Artifacts (Scanned) | 10 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 372 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 55.6% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.375 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 6 | 359 | 60.0% |
| MARKDOWN | 2 | 0 | 20.0% |
| DOCKERFILE | 1 | 11 | 10.0% |
| SHELL | 1 | 2 | 10.0% |

## 4.1 SOURCE ENCODINGS
All 10 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 40%, Large Core Modules (3) 20%, Interface Declarations Files 10%, Parameter Forwarders Files 10%, State Mutators Files 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 8 | 80.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 20.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cow`: 3x Excluded (Unsupported Extension: '.cow')
- `.conf`: 1x Excluded (Unsupported Extension: '.conf')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 78.7 | 18.5 | 6.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 84.2 | 37.9 | 52.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 16.9 | 2.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.5 | 2.4 | 2.3 | 2.4 |
| Connectivity (formerly API Exposure) | 0.0 | 4.7 | 2.5 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 49.5 | 50.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.5 | 0.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 70.4 | 87.6 | 87.6 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3 | 2 | 1 | `controllers/showsum.cbl` |
| cleanup | 1 | 1 | 0 | `cowtemplate.cbl` |
| guards | 0 | 0 | 0 | - |
| danger | 10 | 5 | 3 | `cow.cbl` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 8 | 5 | 2 | `cow.cbl` |
| io | 13 | 2 | 6 | `cowtemplate.cbl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 10 | 6 | 3 | `Dockerfile` |
| time | 0 | 0 | 0 | - |
| serialization | 3 | 2 | 1 | `cow.cbl` |
| regex | 0 | 0 | 0 | - |
| events | 1 | 1 | 0 | `Dockerfile` |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 7 | 2 | 2 | `cow.cbl` |
| mutation | 67 | 5 | 19 | `cowtemplate.cbl` |
| dead_code | 3 | 2 | 1 | `cow.cbl` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cowtemplate.cbl` (Hits: 7)
- `Dockerfile` (Hits: 6)
- `README.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **cowtemplate.cbl** (`cowtemplate.cbl`) — 3 inbound connections
2. **config.cbl** (`config.cbl`) — 1 inbound connections
3. **Dockerfile** (`Dockerfile`) — 0 inbound connections
4. **README.md** (`README.md`) — 0 inbound connections
5. **index.md** (`tutorial/index.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Dockerfile** (`Dockerfile`) — 2 outbound dependencies
2. **cow.cbl** (`cow.cbl`) — 1 outbound dependencies
3. **README.md** (`README.md`) — 0 outbound dependencies
4. **index.md** (`tutorial/index.md`) — 0 outbound dependencies
5. **config.cbl** (`config.cbl`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `start-checkfilestatus` **(Compute Cores)** (@ `cowtemplate.cbl`) -> Impact: **35.2** | LOC: 44
- `CHECKQUERY` **(Many-Argument Workhorses)** (@ `cow.cbl`) -> Impact: **21.6** | LOC: 74
- `COW` **(I/O & Config Routines)** (@ `cow.cbl`) -> Impact: **6.8** | LOC: 36
- `GETQUERY` **(Compute Cores)** (@ `cow.cbl`) -> Impact: **6.6** | LOC: 19
- `start-readfile` **(I/O & Config Routines)** (@ `cowtemplate.cbl`) -> Impact: **5.8** | LOC: 37
- `SHOWVARS` **(Compute Cores)** (@ `cow.cbl`) -> Impact: **5.1** | LOC: 17
- `SHOWSUM` **(Type Conversions)** (@ `controllers/showsum.cbl`) -> Impact: **2.5** | LOC: 22
- `RUN` **(I/O & Config Routines)** (@ `Dockerfile`) -> Impact: **2.1** | LOC: 2
- `RUN` **(I/O & Config Routines)** (@ `Dockerfile`) -> Impact: **2.1** | LOC: 3
- `COWTEMPLATE` **(Parameter Forwarders)** (@ `cowtemplate.cbl`) -> Impact: **2.0** | LOC: 5

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Parameter Forwarders**: thin, many-argument glue that forwards to other code
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 6 | 266.36 | 20.06% | 2.82% |
| `controllers` | 3 | 17.88 | 9.25% | 0.0% |
| `tutorial` | 1 | 4.8 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `cowtemplate.cbl` -> **16.9256%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cowtemplate.cbl` -> **100.0%** Exposure
- `cow.cbl` -> **99.8685%** Exposure
- `controllers/showsum.cbl` -> **96.0834%** Exposure
- `config.cbl` -> **68.9974%** Exposure
- `controllers/showname.cbl` -> **31.0026%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cowtemplate.cbl` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `3` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `cowtemplate.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.685)
- **Top Global Matches:** file_cluster_8: 7.685, file_cluster_6: 17.516, file_cluster_3: 20.482
- **Magnitude:** 148.2 | **LOC:** 152 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 264.925; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.2%), Complexity Load (formerly Cognitive Load) (78.7%), Debt Markers (formerly Tech Debt) (16.9%)
- **Documentation Coverage:** 87.617% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start-checkfilestatus` **(Compute Cores)** (Impact: 35.2)
  * `start-readfile` **(I/O & Config Routines)** (Impact: 5.8)
  * `COWTEMPLATE` **(Parameter Forwarders)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 19`, `args: 6`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 35`, `unreferenced_by_name: 1`
* *Architecture:* `io: 7`, `api: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 264.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.333333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `cow.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.345)
- **Top Global Matches:** file_cluster_15: 6.345, file_cluster_11: 6.449, file_cluster_2: 7.554
- **Magnitude:** 91.22 | **LOC:** 365 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 74.627; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (60.1%), Complexity Load (formerly Cognitive Load) (36.1%), Dead Code Surface (formerly Dead Code) (7.5%)
- **Documentation Coverage:** 87.617% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CHECKQUERY` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `COW` **(I/O & Config Routines)** (Impact: 6.8)
  * `GETQUERY` **(Compute Cores)** (Impact: 6.6)
  * `SHOWVARS` **(Compute Cores)** (Impact: 5.1)
  * `web-header` **(Interface Declarations)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 40`, `args: 10`, `func_start: 2`, `class_start: 4`
* *Risk/State:* `state_mutation: 16`, `dead_code: 2`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 74.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` config
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `config.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.694)
- **Top Global Matches:** file_cluster_2: 2.694, file_cluster_17: 5.301, file_cluster_13: 6.499
- **Magnitude:** 16.08 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 138.06; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (52.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 138.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `controllers/showsum.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.136)
- **Top Global Matches:** file_cluster_2: 6.136, file_cluster_17: 6.861, file_cluster_15: 6.981
- **Magnitude:** 11.06 | **LOC:** 51 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.1%), Guard Balance (formerly Safety Score) (55.0%), Complexity Load (formerly Cognitive Load) (15.2%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SHOWSUM` **(Type Conversions)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 6`, `args: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 74.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Dockerfile` (DOCKERFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 8.2)
- **Top Global Matches:** file_cluster_2: 8.2, file_cluster_13: 9.024, file_cluster_15: 9.103
- **Magnitude:** 8.72 | **LOC:** 13 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 74.627; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (5.5%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 87.617% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RUN` **(I/O & Config Routines)** (Impact: 2.1)
  * `RUN` **(I/O & Config Routines)** (Impact: 2.1)
  * `RUN` **(I/O & Config Routines)** (Impact: 1.1)
  * `CMD` **(State Mutators)** (Impact: 1.1)
  * `ENTRYPOINT` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`, `func_start: 5`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 6`, `api: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 74.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` builder, ubuntu:trusty
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `controllers/showname.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.165)
- **Top Global Matches:** file_cluster_15: 5.165, file_cluster_2: 6.159, file_cluster_11: 6.634
- **Magnitude:** 5.28 | **LOC:** 38 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.4%), Mutation Surface (formerly State Flux) (31.0%), Complexity Load (formerly Cognitive Load) (7.4%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SHOWNAME` **(Parameter Forwarders)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 6`, `args: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 74.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tutorial/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 4.8 | **LOC:** 240 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 74.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `controllers/index.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 4.417)
- **Top Global Matches:** file_cluster_11: 4.417, file_cluster_2: 6.422, file_cluster_17: 7.002
- **Magnitude:** 1.54 | **LOC:** 26 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `INDEXWEB` **(Interface Declarations)** (Impact: 1.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 74.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `downhill.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.053)
- **Top Global Matches:** file_cluster_2: 3.053, file_cluster_17: 4.76, file_cluster_13: 5.581
- **Magnitude:** 1.14 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 74.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 27 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 74.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `cow.cbl` (COBOL) | Magnitude: 91.22 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 183, structural_boundaries: 40, branch: 24, state_mutation: 16

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cowtemplate.cbl` -> **Severity: 28.083** (Embedded: 0.3333 * Error Risk: 84.2497%)
- `config.cbl` -> **Severity: 5.873** (Embedded: 0.1111 * Error Risk: 52.854%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cowtemplate.cbl` -> **Severity: 23211.934** (Blast Radius: 264.925 * Doc Risk: 87.617%)
- `controllers/index.cbl` -> **Severity: 7462.7** (Blast Radius: 74.627 * Doc Risk: 100.0%)
- `controllers/showname.cbl` -> **Severity: 7462.7** (Blast Radius: 74.627 * Doc Risk: 100.0%)
- `controllers/showsum.cbl` -> **Severity: 7462.7** (Blast Radius: 74.627 * Doc Risk: 100.0%)
- `Dockerfile` -> **Severity: 6538.594** (Blast Radius: 74.627 * Doc Risk: 87.617%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `6` files carry mainframe facts -- `7` call sites, `2` dataset bindings, `120` record items.

### `cow.cbl` (COBOL)
- **Calls:** `CALL getquery`, `CALL checkquery`, `CALL ROUTING-DESTINY`
- **Datasets:** `KEYBOARD(declared)`
- **Record layouts (83 items):** `ENVIRONMENT-NAMES (38)`, `THE-GREAT-DISPATCH (5)`, `CHOPPERY (5)`, `THE-VALUES (4)`, `THE-VALUES (4)`, `QUERY-ANALYSIS (4)`, `QUERY-ANALYSIS-OUT (4)`, `POSTCHUNK⟵WEBINPUT (2)`, `NEWLINE (1)`, `ANALYZED-QUERY (1)`, `TESTER (1)`, `ANYFOUND (1)` … (+13 more)
- **Data moves:** 18 (ACCEPT 1, ADD 1, MOVE 12, SUBTRACT 2, UNSTRING 2); most-fed items `CHOPPED-PATH-PIECE`, `CHOPPED-PATTERN-PIECE`, `POSITIO`, `QUERY-ANALYSIS-OUT`, `QUERY-VALUE`, `QUERY-VALUE-NAME`

### `cowtemplate.cbl` (COBOL)
- **Calls:** `CALL checkfilestatus`
- **Datasets:** `READFILE-NAME(INPUT)`
- **Record layouts (16 items):** `THE-VARS (4)`, `READLINE⟵READFILE (1)`, `READFILE-NAME (1)`, `READFILE-STATUS (1)`, `TEMPLINE (1)`, `THE-VAR (1)`, `WHAT-WE-CHANGE (1)`, `COUNTER (1)`, `TEMPLATE-FILENAME (1)`, `STATUS-MESSAGE (1)`, `DISPLAY-MESSAGE (1)`, `FILE-NAME (1)` … (+1 more)
- **Data moves:** 38 (MOVE 34, STRING 4); most-fed items `DISPLAY-MESSAGE`

### `controllers/showsum.cbl` (COBOL)
- **Calls:** `CALL cowtemplate`
- **Record layouts (9 items):** `THE-VARS (4)`, `RECEIVED-VALUES (4)`, `SUM-RESULT (1)`
- **Data moves:** 8 (COMPUTE 2, MOVE 6); most-fed items `COW-VARVALUE`, `SUM-RESULT`

### `controllers/showname.cbl` (COBOL)
- **Calls:** `CALL cowtemplate`
- **Record layouts (8 items):** `THE-VARS (4)`, `THE-VALUES (4)`
- **Data moves:** 2 (MOVE 2); most-fed items `COW-VARVALUE`

### `controllers/index.cbl` (COBOL)
- **Calls:** `CALL cowtemplate`
- **Record layouts (4 items):** `THE-VARS (4)`

### `config.cbl` (COBOL)
- **Data moves:** 4 (MOVE 4)

- **Mainframe skeleton completeness:** 67% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: JCL and PROC libraries (3 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 10 call pairs -- scoped 50.0%, unique 30.0%, ambiguous 0.0%, external 20.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 9 | 55.6% | 33.3% | 0.0% | 11.1% |
| shell | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
