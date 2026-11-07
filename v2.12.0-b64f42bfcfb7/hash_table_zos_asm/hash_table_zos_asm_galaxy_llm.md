# ARCHITECTURAL_BRIEF: hash_table_zos_asm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/tobiaslinke/hash_table_zos_asm.git` |
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
- **Scope:** 26 analyzed artifact(s), 4266 LOC.
- **Load-bearing artifact:** `HASH.MACLIB/THTCBLKS` -- 15 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `HASH.PROCLIB/ASMLINK` -- pulls in 9 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `HASH.ASM/THTSCOM` at magnitude 66.92 (structural weight, not risk).
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
| Total Artifacts | 36 |
| Analyzed Artifacts (Scanned) | 26 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10 |
| Total LOC | 4266 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 72.2% |
| Dominant Lang | HLASM |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.106 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4374 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0851 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| HLASM | 25 | 4245 | 96.2% |
| JCL | 1 | 21 | 3.8% |

## 4.1 SOURCE ENCODINGS
All 26 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 92%, Interface Declarations Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 26 | 100.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10*

**Composition by Extension & Reason:**
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 11.8 | 4.6 | 5.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 68.9 | 16.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 37.8 | 3.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.4 | 2.4 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 4.1 | 2.4 | 2.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 80.8 | 3.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 10.5 | 0.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.4 | 0.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 24 | 9 | 2 | `HASH.ASM/THTBATCH` |
| cleanup | 12 | 4 | 1 | `HASH.ASM/THTBATCH` |
| guards | 352 | 24 | 17 | `HASH.ASM/THTBATCH` |
| danger | 8 | 2 | 0 | `HASH.ASM/THTSERV0` |
| concurrency | 2 | 1 | 0 | `HASH.ASM/THTSERV0` |
| connectivity | 24 | 23 | 1 | `HASH.ASM/THTSERV0` |
| io | 19 | 2 | 0 | `HASH.PROCLIB/ASMLINK` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 17 | 17 | 1 | `HASH.ASM/THTBATCH` |
| debt | 0 | 0 | 0 | - |
| mutation | 440 | 23 | 25 | `HASH.ASM/THTBATCH` |
| dead_code | 6 | 5 | 1 | `HASH.ASM/THTHASH2` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **17.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `HASH.PROCLIB/ASMLINK` (Hits: 11)
- `HASH.ASM/THTBATCH` (Hits: 8)
- `HASH.ASM/THTCREAT` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **THTCBLKS** (`HASH.MACLIB/THTCBLKS`) — 15 inbound connections
2. **THTCOMM** (`HASH.MACLIB/THTCOMM`) — 15 inbound connections
3. **THTHASH2** (`HASH.ASM/THTHASH2`) — 6 inbound connections
4. **THTHASH3** (`HASH.ASM/THTHASH3`) — 5 inbound connections
5. **THTDELET** (`HASH.ASM/THTDELET`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ASMLINK** (`HASH.PROCLIB/ASMLINK`) — 9 outbound dependencies
2. **THTBATCH** (`HASH.ASM/THTBATCH`) — 0 outbound dependencies
3. **THTCREAT** (`HASH.ASM/THTCREAT`) — 0 outbound dependencies
4. **THTDELET** (`HASH.ASM/THTDELET`) — 0 outbound dependencies
5. **THTDROP0** (`HASH.ASM/THTDROP0`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `THTPARSR` **(I/O & Config Routines)** (@ `HASH.ASM/THTPARSR`) -> Impact: **48.5** | LOC: 629
- `THTSCOM` **(I/O & Config Routines)** (@ `HASH.ASM/THTSCOM`) -> Impact: **47.1** | LOC: 462
- `THTBATCH` **(I/O & Config Routines)** (@ `HASH.ASM/THTBATCH`) -> Impact: **35.0** | LOC: 280
- `THTDELET` **(I/O & Config Routines)** (@ `HASH.ASM/THTDELET`) -> Impact: **35.0** | LOC: 400
- `THTPUT00` **(I/O & Config Routines)** (@ `HASH.ASM/THTPUT00`) -> Impact: **27.7** | LOC: 333
- `THTINSRT` **(I/O & Config Routines)** (@ `HASH.ASM/THTINSRT`) -> Impact: **27.1** | LOC: 322
- `THTSELEC` **(I/O & Config Routines)** (@ `HASH.ASM/THTSELEC`) -> Impact: **26.8** | LOC: 295
- `THTMERG0` **(I/O & Config Routines)** (@ `HASH.ASM/THTMERG0`) -> Impact: **23.0** | LOC: 259
- `THTUPDAT` **(I/O & Config Routines)** (@ `HASH.ASM/THTUPDAT`) -> Impact: **22.3** | LOC: 266
- `THTSELES` **(I/O & Config Routines)** (@ `HASH.ASM/THTSELES`) -> Impact: **16.3** | LOC: 206

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `HASH.ASM` | 22 | 560.38 | 5.45% | 0.0% |
| `HASH.MACLIB` | 3 | 14.82 | 0.0% | 33.19% |
| `HASH.PROCLIB` | 1 | 4.42 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `HASH.MACLIB/THTCOMM` -> **37.7541%** Exposure
- `HASH.MACLIB/THTPARM` -> **37.7541%** Exposure
- `HASH.MACLIB/THTCBLKS` -> **24.0736%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `HASH.ASM/THTSCOM` -> **10.487%** Exposure
- `HASH.ASM/THTBATCH` -> **9.6745%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `HASH.MACLIB/THTCBLKS` -> **1** Orphaned Functions | **0** Duplicates
- `HASH.MACLIB/THTCOMM` -> **1** Orphaned Functions | **0** Duplicates
- `HASH.MACLIB/THTPARM` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `9` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `HASH.ASM/THTSCOM` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.861)
- **Top Global Matches:** file_cluster_1: 6.861, file_cluster_3: 48.373, file_cluster_8: 70.143
- **Magnitude:** 66.92 | **LOC:** 529 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (10.5%), Complexity Load (formerly Cognitive Load) (7.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTSCOM` **(I/O & Config Routines)** (Impact: 47.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Memory Alloc (weighted view):* 1
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 215`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTBATCH` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.787)
- **Top Global Matches:** file_cluster_1: 6.787, file_cluster_3: 48.364, file_cluster_8: 70.138
- **Magnitude:** 65.86 | **LOC:** 1053 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (9.7%), Complexity Load (formerly Cognitive Load) (6.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTBATCH` **(I/O & Config Routines)** (Impact: 35.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 3 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 391`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`
* *Architecture:* `io: 8`, `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 19`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTPARSR` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.936)
- **Top Global Matches:** file_cluster_1: 6.936, file_cluster_3: 48.386, file_cluster_8: 70.153
- **Magnitude:** 57.82 | **LOC:** 646 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.4%), Test Surface (formerly Verification) (2.4%), Connectivity (formerly Api Exposure) (2.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTPARSR` **(I/O & Config Routines)** (Impact: 48.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 268`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTDELET` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.875)
- **Top Global Matches:** file_cluster_9: 6.875, file_cluster_16: 12.255, file_cluster_15: 12.377
- **Magnitude:** 42.0 | **LOC:** 413 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 37.766; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (7.3%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTDELET` **(I/O & Config Routines)** (Impact: 35.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 153`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.766
  * `Choke Point (Betweenness):` 0.006667 | `Ripple Effect (Closeness):` 0.08
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `HASH.ASM/THTPUT00` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.984)
- **Top Global Matches:** file_cluster_9: 6.984, file_cluster_16: 12.256, file_cluster_15: 12.384
- **Magnitude:** 32.96 | **LOC:** 346 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (7.0%), Test Surface (formerly Verification) (2.4%), Connectivity (formerly Api Exposure) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTPUT00` **(I/O & Config Routines)** (Impact: 27.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 133`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTINSRT` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.994)
- **Top Global Matches:** file_cluster_9: 6.994, file_cluster_16: 12.272, file_cluster_15: 12.39
- **Magnitude:** 32.14 | **LOC:** 337 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (7.2%), Connectivity (formerly Api Exposure) (2.4%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTINSRT` **(I/O & Config Routines)** (Impact: 27.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 123`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTSELEC` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.987)
- **Top Global Matches:** file_cluster_9: 6.987, file_cluster_16: 12.285, file_cluster_15: 12.403
- **Magnitude:** 31.72 | **LOC:** 313 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (7.4%), Dead Code Surface (formerly Dead Code) (6.2%), Connectivity (formerly Api Exposure) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTSELEC` **(I/O & Config Routines)** (Impact: 26.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 114`, `func_start: 1`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTSERV0` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.727)
- **Top Global Matches:** file_cluster_2: 6.727, file_cluster_17: 7.297, file_cluster_15: 7.431
- **Magnitude:** 28.46 | **LOC:** 201 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (80.8%), Guard Balance (formerly Safety Score) (68.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (11.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTSERV0` **(I/O & Config Routines)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 7
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 59`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 3`
* *Architecture:* `api: 2`, `concurrency: 2`
* *Defense:* `doc: 1`, `immutability_locks: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTMERG0` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.069)
- **Top Global Matches:** file_cluster_9: 7.069, file_cluster_16: 12.299, file_cluster_15: 12.425
- **Magnitude:** 27.98 | **LOC:** 336 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (7.1%), Connectivity (formerly Api Exposure) (2.4%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTMERG0` **(I/O & Config Routines)** (Impact: 23.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 120`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTUPDAT` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.086)
- **Top Global Matches:** file_cluster_9: 7.086, file_cluster_16: 12.295, file_cluster_15: 12.41
- **Magnitude:** 26.6 | **LOC:** 280 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (7.5%), Connectivity (formerly Api Exposure) (2.5%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTUPDAT` **(I/O & Config Routines)** (Impact: 22.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 91`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTSELES` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.17)
- **Top Global Matches:** file_cluster_9: 7.17, file_cluster_16: 12.341, file_cluster_15: 12.405
- **Magnitude:** 21.2 | **LOC:** 221 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (6.0%), Connectivity (formerly Api Exposure) (2.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTSELES` **(I/O & Config Routines)** (Impact: 16.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 82`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTGET00` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.833)
- **Top Global Matches:** file_cluster_2: 6.833, file_cluster_17: 7.052, file_cluster_13: 7.257
- **Magnitude:** 15.0 | **LOC:** 175 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.7%), Connectivity (formerly Api Exposure) (2.7%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTGET00` **(I/O & Config Routines)** (Impact: 11.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 65`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTHASH1` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.272)
- **Top Global Matches:** file_cluster_2: 5.272, file_cluster_13: 6.394, file_cluster_15: 6.776
- **Magnitude:** 14.3 | **LOC:** 152 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.5%), Connectivity (formerly Api Exposure) (2.8%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTHASH1` **(I/O & Config Routines)** (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 45`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTDROP0` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.968)
- **Top Global Matches:** file_cluster_2: 6.968, file_cluster_17: 7.093, file_cluster_13: 7.269
- **Magnitude:** 13.46 | **LOC:** 147 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (6.2%), Connectivity (formerly Api Exposure) (2.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTDROP0` **(I/O & Config Routines)** (Impact: 9.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 44`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTINIT0` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.97)
- **Top Global Matches:** file_cluster_2: 6.97, file_cluster_13: 7.228, file_cluster_17: 7.265
- **Magnitude:** 12.62 | **LOC:** 141 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (2.8%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTINIT0` **(I/O & Config Routines)** (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 36`, `func_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTSHTAB` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.713)
- **Top Global Matches:** file_cluster_2: 6.713, file_cluster_17: 7.215, file_cluster_13: 7.269
- **Magnitude:** 12.38 | **LOC:** 155 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.0%), Connectivity (formerly Api Exposure) (2.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTSHTAB` **(I/O & Config Routines)** (Impact: 8.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 55`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTCREAT` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.849)
- **Top Global Matches:** file_cluster_2: 6.849, file_cluster_17: 6.961, file_cluster_13: 7.221
- **Magnitude:** 12.36 | **LOC:** 159 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (6.5%), Connectivity (formerly Api Exposure) (2.7%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTCREAT` **(I/O & Config Routines)** (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 52`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTSHMAP` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.034)
- **Top Global Matches:** file_cluster_2: 7.034, file_cluster_17: 7.352, file_cluster_13: 7.38
- **Magnitude:** 11.98 | **LOC:** 144 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.2%), Connectivity (formerly Api Exposure) (2.8%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTSHMAP` **(I/O & Config Routines)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Memory Alloc (weighted view):* 2
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 42`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTHASH2` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.242)
- **Top Global Matches:** file_cluster_2: 5.242, file_cluster_13: 6.243, file_cluster_17: 6.566
- **Magnitude:** 11.0 | **LOC:** 148 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); blast radius 59.451; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Dead Code Surface (formerly Dead Code) (14.4%), Connectivity (formerly Api Exposure) (2.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTHASH2` **(I/O & Config Routines)** (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 51`, `func_start: 1`
* *Risk/State:* `dead_code: 2`
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 59.451
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.256
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `HASH.ASM/THTPURG0` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.871)
- **Top Global Matches:** file_cluster_2: 6.871, file_cluster_17: 7.14, file_cluster_13: 7.329
- **Magnitude:** 10.22 | **LOC:** 145 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.7%), Connectivity (formerly Api Exposure) (2.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTPURG0` **(I/O & Config Routines)** (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 44`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.ASM/THTSHSTA` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.141)
- **Top Global Matches:** file_cluster_2: 7.141, file_cluster_13: 7.311, file_cluster_17: 7.344
- **Magnitude:** 8.44 | **LOC:** 116 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (2.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTSHSTA` **(I/O & Config Routines)** (Impact: 6.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 39`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.MACLIB/THTCBLKS` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 6.681)
- **Top Global Matches:** file_cluster_17: 6.681, file_cluster_2: 6.948, file_cluster_15: 7.665
- **Magnitude:** 7.88 | **LOC:** 109 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); blast radius 171.968; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (24.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTCBLKS` **(I/O & Config Routines)** (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 48`, `func_start: 1`, `class_start: 8`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 171.968
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.6
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `HASH.ASM/THTHASH3` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.943)
- **Top Global Matches:** file_cluster_13: 5.943, file_cluster_2: 6.006, file_cluster_17: 6.855
- **Magnitude:** 4.96 | **LOC:** 60 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); blast radius 52.621; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (3.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTHASH3` **(I/O & Config Routines)** (Impact: 3.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 17`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 52.621
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.217778
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `HASH.PROCLIB/ASMLINK` (JCL | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.433)
- **Top Global Matches:** file_cluster_11: 5.433, file_cluster_2: 6.911, file_cluster_13: 7.861
- **Magnitude:** 4.42 | **LOC:** 29 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 24.106; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ASM` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* //ASMLINK PROC //*-------------------------------------------------------------- //* ASSEMBLE //*---...
  * `LINK` **(Interface Declarations)** (Impact: 1.4)
    * *Intent:* //ASM EXEC PGM=ASMA90,PARM= //SYSLIB DD DISP=SHR,DSN=SYS1.MACLIB // DD DISP=SHR,DSN=SYS1.MODGEN // D...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 19`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 11`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ASM.SOURCE.LIB.NAME(PROGNAME), GKI0794.HASH.MACLIB, GKI0794.TAF.MACLIB, LOADLIB.NAME, OBJECT.CODE.LIB.NAME, OBJECT.CODE.LIB.NAME(PROGNAME), SYS1.CSSLIB, SYS1.MACLIB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HASH.MACLIB/THTPARM` (HLASM | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 6.764)
- **Top Global Matches:** file_cluster_17: 6.764, file_cluster_2: 8.014, file_cluster_15: 8.445
- **Magnitude:** 3.98 | **LOC:** 48 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (37.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THTPARM` **(I/O & Config Routines)** (Impact: 3.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `HASH.ASM/THTHASH3` (HLASM) | Magnitude: 4.96 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 17, decorators: 2, bitwise_ops: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `HASH.ASM/THTCREAT` (HLASM) | Magnitude: 12.36 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 52, immutability_locks: 17, decorators: 2
- `HASH.ASM/THTDROP0` (HLASM) | Magnitude: 13.46 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 44, immutability_locks: 17, branch: 2

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `HASH.ASM/THTDELET` -> **Severity: 4.012** (Embedded: 0.08 * Error Risk: 50.1481%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `HASH.MACLIB/THTCBLKS` -> **Severity: 17196.8** (Blast Radius: 171.968 * Doc Risk: 100.0%)
- `HASH.MACLIB/THTCOMM` -> **Severity: 17196.8** (Blast Radius: 171.968 * Doc Risk: 100.0%)
- `HASH.ASM/THTHASH2` -> **Severity: 5945.1** (Blast Radius: 59.451 * Doc Risk: 100.0%)
- `HASH.ASM/THTHASH3` -> **Severity: 5262.1** (Blast Radius: 52.621 * Doc Risk: 100.0%)
- `HASH.ASM/THTDELET` -> **Severity: 3776.6** (Blast Radius: 37.766 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `1` files carry mainframe facts -- `2` call sites, `9` dataset bindings, `0` record items.

### `HASH.PROCLIB/ASMLINK` (JCL)
- **Calls:** `EXEC PGM ASMA90`, `EXEC PGM IEWL`
- **Datasets:** `SYSLIB→SYS1.MACLIB`, `SYSLIB→SYS1.MODGEN`, `SYSLIB→GKI0794.TAF.MACLIB`, `SYSLIB→GKI0794.HASH.MACLIB`, `SYSLIN→OBJECT.CODE.LIB.NAME(PROGNAME)`, `SYSIN→ASM.SOURCE.LIB.NAME(PROGNAME)`, `SYSLIB→SYS1.CSSLIB`, `SYSLMOD→LOADLIB.NAME`, `SYSLIN→OBJECT.CODE.LIB.NAME`

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 221 call pairs -- scoped 0.0%, unique 19.5%, ambiguous 0.0%, external 80.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| hlasm | 219 | 0.0% | 19.6% | 0.0% | 80.4% |
| jcl | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
