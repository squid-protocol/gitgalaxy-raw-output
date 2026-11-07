# ARCHITECTURAL_BRIEF: zECS
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/walmartlabs/zECS` |
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
- **Scope:** 37 analyzed artifact(s), 3957 LOC.
- **Load-bearing artifact:** `Source/ZECSZFC.cpy` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `JCL/CONFIG.jcl` -- pulls in 26 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Source/ZECS001.cbl` at magnitude 776.3 (structural weight, not risk).
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
| Total Artifacts | 38 |
| Analyzed Artifacts (Scanned) | 37 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 3957 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 97.4% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4028 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2399 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.25 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JCL | 13 | 671 | 35.1% |
| COBOL | 7 | 2670 | 18.9% |
| CSD | 6 | 147 | 16.2% |
| MARKDOWN | 4 | 0 | 10.8% |
| PLAINTEXT | 3 | 0 | 8.1% |
| HLASM | 2 | 442 | 5.4% |
| REXX | 1 | 26 | 2.7% |
| YAML | 1 | 1 | 2.7% |

## 4.1 SOURCE ENCODINGS
All 37 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 41%, Interface Declarations Files 27%, Declarative / Non-Code 19%, Large Core Modules 8%, State Mutators Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 30 | 81.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7 | 18.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.7 | 15.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 72.1 | 23.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 16.7 | 1.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 12.7 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 10.6 | 0.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 87.7 | 6.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 6.3 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 63.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 8.9 | 0.3 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8 | 2 | 0 | `Source/ZECS001.cbl` |
| cleanup | 45 | 6 | 3 | `JCL/CONFIG.jcl` |
| guards | 112 | 7 | 7 | `Source/ZECS001.cbl` |
| danger | 171 | 10 | 12 | `Source/ZECS001.cbl` |
| concurrency | 39 | 6 | 1 | `JCL/CONFIG.jcl` |
| connectivity | 61 | 7 | 4 | `Source/ZECS001.cbl` |
| io | 273 | 18 | 11 | `JCL/CONFIG.jcl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 16 | 7 | 2 | `Source/ZECS001.cbl` |
| time | 14 | 5 | 1 | `Source/ZECS000.cbl` |
| serialization | 10 | 4 | 0 | `Source/ZECS001.cbl` |
| regex | 10 | 3 | 0 | `Source/ZECS000.cbl` |
| events | 11 | 7 | 1 | `Source/ZECSNC.asm` |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 0 | 0 | 0 | - |
| mutation | 841 | 24 | 41 | `JCL/CONFIG.jcl` |
| dead_code | 9 | 3 | 0 | `Source/ZECS000.cbl` |
| credential | 1 | 1 | 0 | `Source/ZECS001.cbl` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 4 | 2 | 0 | `Source/ZECSNC.asm` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `JCL/CONFIG.jcl` (Hits: 150)
- `Source/ZECS001.cbl` (Hits: 29)
- `JCL/DEFZC##.jcl` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ZECSZFC.cpy** (`Source/ZECSZFC.cpy`) — 3 inbound connections
2. **ZECSZKC.cpy** (`Source/ZECSZKC.cpy`) — 3 inbound connections
3. **Installation.md** (`Installation.md`) — 2 inbound connections
4. **ZECS000.cbl** (`Source/ZECS000.cbl`) — 2 inbound connections
5. **ZECS003.cbl** (`Source/ZECS003.cbl`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CONFIG.jcl** (`JCL/CONFIG.jcl`) — 26 outbound dependencies
2. **CSDZECS.rdo** (`Source/CSDZECS.rdo`) — 6 outbound dependencies
3. **DEFZC##.jcl** (`JCL/DEFZC##.jcl`) — 5 outbound dependencies
4. **DEFEXPR.jcl** (`JCL/DEFEXPR.jcl`) — 4 outbound dependencies
5. **README.md** (`README.md`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ZECS002` **(I/O & Config Routines)** (@ `Source/ZECS002.asm`) -> Impact: **36.7** | LOC: 334
  * *Intent:* * *********************************************************************** * Control Section * ********************************************************...
- `ZECSNC` **(I/O & Config Routines)** (@ `Source/ZECSNC.asm`) -> Impact: **22.5** | LOC: 210
  * *Intent:* * *********************************************************************** * Control Section * ********************************************************...
- `1610-SCAN-ZCXXSD` **(I/O & Config Routines)** (@ `Source/ZECS001.cbl`) -> Impact: **14.1** | LOC: 22
  * *Intent:* ***************************************************************** * Scan Security Model (ZCxxSD) until UserID and Access match. * ********************...
- `1000-ACCESS-PARMS` **(I/O & Config Routines)** (@ `Source/ZECS001.cbl`) -> Impact: **13.9** | LOC: 98
  * *Intent:* ***************************************************************** * Access parms. * *****************************************************************...
- `3300-READ-FILE` **(I/O & Config Routines)** (@ `Source/ZECS001.cbl`) -> Impact: **13.5** | LOC: 70
  * *Intent:* ***************************************************************** * HTTP GET. * * Read FILE structure. * * Only update access timestamp when LAT is pr...
- `A2000-SETUP-ECS-REQUEST` **(I/O & Config Routines)** (@ `Source/ECS001.cbl`) -> Impact: **13.2** | LOC: 45
  * *Intent:* ****************************************************************** * * ******************************************************************...
- `8200-WEB-CONVERSE` **(I/O & Config Routines)** (@ `Source/ZECS001.cbl`) -> Impact: **11.6** | LOC: 71
  * *Intent:* ***************************************************************** * Converse with the other Data Center zECS. * * The first element of the path, which...
- `3000-DEPLICATE` **(Defensive Guards)** (@ `Source/ZECS000.cbl`) -> Impact: **11.3** | LOC: 26
  * *Intent:* ***************************************************************** * Deplicate request to the other Data Center. * * Delete *FILE and *KEY records only...
- `1310-TTL` **(I/O & Config Routines)** (@ `Source/ZECS001.cbl`) -> Impact: **9.2** | LOC: 25
  * *Intent:* ***************************************************************** * Process TTL query string for POST/PUT. * *****************************************...
- `2000-REPLICATE` **(Defensive Guards)** (@ `Source/ZECS003.cbl`) -> Impact: **9.1** | LOC: 21
  * *Intent:* ***************************************************************** * Replicate request to the other Data Center. * * If this is a replicate request, se...

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Source` | 22 | 1549.48 | 21.26% | 1.81% |
| `JCL` | 10 | 119.02 | 0.0% | 0.0% |
| `__monolith__` | 5 | 19.62 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Source/ZECS000.cbl` -> **16.7208%** Exposure
- `Source/ZECSNC.asm` -> **12.2901%** Exposure
- `Source/ZECS002.asm` -> **10.8337%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Source/REXXREPL.exec` -> **100.0%** Exposure
- `Source/ECS001.cbl` -> **99.9999%** Exposure
- `Source/ZECS001.cbl` -> **99.994%** Exposure
- `Source/ZECS000.cbl` -> **98.2708%** Exposure
- `Source/ZECS003.cbl` -> **93.6053%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Source/ZECS000.cbl` -> **5** Orphaned Functions | **0** Duplicates
- `Source/ZECS002.asm` -> **1** Orphaned Functions | **0** Duplicates
- `Source/ZECSNC.asm` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `Source/ZECS001.cbl` -> **8.8944%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `67` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Source/ZECS001.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.925)
- **Top Global Matches:** file_cluster_12: 6.925, file_cluster_7: 7.574, file_cluster_5: 9.735
- **Magnitude:** 776.3 | **LOC:** 2165 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 31.965; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1610-SCAN-ZCXXSD` **(I/O & Config Routines)** (Impact: 14.1)
    * *Intent:* ***************************************************************** * Scan Security Model (ZCxxSD) unt...
  * `1000-ACCESS-PARMS` **(I/O & Config Routines)** (Impact: 13.9)
    * *Intent:* ***************************************************************** * Access parms. * ****************...
  * `3300-READ-FILE` **(I/O & Config Routines)** (Impact: 13.5)
    * *Intent:* ***************************************************************** * HTTP GET. * * Read FILE structur...
  * `8200-WEB-CONVERSE` **(I/O & Config Routines)** (Impact: 11.6)
    * *Intent:* ***************************************************************** * Converse with the other Data Cen...
  * `1310-TTL` **(I/O & Config Routines)** (Impact: 9.2)
    * *Intent:* ***************************************************************** * Process TTL query string for POS...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 110 instances
* *State Mutation (weighted view):* 435
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 191`, `args: 1`, `func_start: 120`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 57`, `state_mutation: 215`
* *Architecture:* `io: 29`, `api: 1`, `import: 2`
* *Defense:* `safety: 41`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.965
  * `Choke Point (Betweenness):` 0.002381 | `Ripple Effect (Closeness):` 0.027778
  * `Imports (Out-Degree: 4):` ZECSZFC, ZECSZKC
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Source/ZECS000.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.167)
- **Top Global Matches:** file_cluster_7: 7.167, file_cluster_12: 7.672, file_cluster_5: 9.749
- **Magnitude:** 224.78 | **LOC:** 839 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 35.778; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.3%), Complexity Load (formerly Cognitive Load) (83.8%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (77.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `3000-DEPLICATE` **(Defensive Guards)** (Impact: 11.3)
    * *Intent:* ***************************************************************** * Deplicate request to the other D...
  * `3200-DELETE` **(I/O & Config Routines)** (Impact: 6.0)
    * *Intent:* ***************************************************************** * Delete the local cache record. *...
  * `7000-GET-URL` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* ***************************************************************** * Get URL for deplication process....
  * `2000-READ-FILE` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* ***************************************************************** * Read zECS file/data record. * * ...
  * `1100-CONTROL` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* ***************************************************************** * Read zcEXPIRE control file when ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 62`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 56`, `unreferenced_by_name: 5`
* *Architecture:* `io: 14`, `api: 1`, `concurrency: 5`, `import: 2`
* *Defense:* `safety: 18`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 35.778
  * `Choke Point (Betweenness):` 0.001587 | `Ripple Effect (Closeness):` 0.055556
  * `Imports (Out-Degree: 2):` ZECSZFC, ZECSZKC
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Source/ECS001.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.734)
- **Top Global Matches:** file_cluster_7: 6.734, file_cluster_12: 6.934, file_cluster_5: 9.45
- **Magnitude:** 163.52 | **LOC:** 422 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A2000-SETUP-ECS-REQUEST` **(I/O & Config Routines)** (Impact: 13.2)
    * *Intent:* ****************************************************************** * * *****************************...
  * `A4000-EXECUTE-SERVICE` **(I/O & Config Routines)** (Impact: 8.5)
    * *Intent:* ****************************************************************** * Execute the zECS service with t...
  * `A4100-GET-EXISTING-PATH` **(I/O & Config Routines)** (Impact: 6.7)
    * *Intent:* ****************************************************************** * * *****************************...
  * `A3000-OPEN-CONNECTION` **(I/O & Config Routines)** (Impact: 3.5)
    * *Intent:* ****************************************************************** * Open the HTTP connection with t...
  * `A1000-GET-INPUT-REQUEST` **(I/O & Config Routines)** (Impact: 3.2)
    * *Intent:* ****************************************************************** * Use a URIMAP defintion to execu...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 34`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 57`
* *Architecture:* `io: 2`
* *Defense:* `safety: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/ZECS003.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.768)
- **Top Global Matches:** file_cluster_12: 6.768, file_cluster_7: 7.247, file_cluster_5: 9.577
- **Magnitude:** 94.88 | **LOC:** 464 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 33.037; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.6%), Guard Balance (formerly Safety Score) (59.3%), Complexity Load (formerly Cognitive Load) (49.8%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2000-REPLICATE` **(Defensive Guards)** (Impact: 9.1)
    * *Intent:* ***************************************************************** * Replicate request to the other D...
  * `7000-GET-URL` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* ***************************************************************** * Get URL for replication process....
  * `3000-READ-ZF` **(I/O & Config Routines)** (Impact: 4.9)
    * *Intent:* ***************************************************************** * Read zECS cache record. * * Sinc...
  * `7100-WEB-OPEN` **(I/O & Config Routines)** (Impact: 3.7)
    * *Intent:* ***************************************************************** * Open WEB connection with the oth...
  * `ZECS003` **(I/O & Config Routines)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 29`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 20`
* *Architecture:* `io: 7`, `api: 1`, `import: 2`
* *Defense:* `safety: 7`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 33.037
  * `Choke Point (Betweenness):` 0.000794 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 2):` ZECSZFC, ZECSZKC
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `JCL/CONFIG.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.261)
- **Top Global Matches:** file_cluster_11: 6.261, file_cluster_2: 7.479, file_cluster_15: 8.385
- **Magnitude:** 78.24 | **LOC:** 567 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 22.432; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `STEP01` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* //* Steps for this job to complete successfully //* ------------------------------------------------...
  * `STEP03` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /* //********************************************************************** //* Replace ASMZECS JCL ...
  * `STEP05` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /* //********************************************************************** //* Replace CSDZECS JCL ...
  * `STEP07` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /* //********************************************************************** //* Replace CSDZECSN JCL...
  * `STEP09` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /* //********************************************************************** //* Replace CSDZECSR JCL...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 250`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 25`
* *Architecture:* `io: 150`
* *Defense:* `sync_locks: 25`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` @jcl_lib@(ASMZECS), @jcl_lib@(CSDZECS), @jcl_lib@(CSDZECSN), @jcl_lib@(CSDZECSR), @jcl_lib@(CSDZECSS), @jcl_lib@(DEFEXPR), @jcl_lib@(DEFZC##), @jcl_lib@(ZC##DC)...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/ZECS002.asm` (HLASM | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 8.391)
- **Top Global Matches:** file_cluster_1: 8.391, file_cluster_3: 48.604, file_cluster_8: 70.293
- **Magnitude:** 47.8 | **LOC:** 401 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 33.037; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.8%), Debt Markers (formerly Tech Debt) (10.8%), Complexity Load (formerly Cognitive Load) (7.5%), Dead Code Surface (formerly Dead Code) (5.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ZECS002` **(I/O & Config Routines)** (Impact: 36.7)
    * *Intent:* * *********************************************************************** * Control Section * ******...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 186`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 2`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`
* *Defense:* `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Source/REXXREPL.exec` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.529)
- **Top Global Matches:** file_cluster_2: 4.529, file_cluster_17: 6.207, file_cluster_15: 6.743
- **Magnitude:** 43.52 | **LOC:** 43 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.0%), Complexity Load (formerly Cognitive Load) (61.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 4`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 4`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/ZECSPLT.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.644)
- **Top Global Matches:** file_cluster_7: 6.644, file_cluster_12: 7.786, file_cluster_5: 9.65
- **Magnitude:** 35.92 | **LOC:** 170 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 26.245; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (87.7%), Complexity Load (formerly Cognitive Load) (76.0%), Mutation Surface (formerly State Flux) (62.6%), Guard Balance (formerly Safety Score) (61.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2000-INQUIRE-NEXT` **(Defensive Guards)** (Impact: 3.6)
    * *Intent:* ***************************************************************** * Inquire URIMAP NEXT. * *********...
  * `ZECSPLT` **(I/O & Config Routines)** (Impact: 2.5)
  * `2100-CHECK-URIMAP` **(Interface Declarations)** (Impact: 2.2)
    * *Intent:* ***************************************************************** * Check URIMAP for ZC* entries * *...
  * `2200-START` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* ***************************************************************** * Issue START command for zECS exi...
  * `1000-INQUIRE-START` **(I/O & Config Routines)** (Impact: 1.2)
    * *Intent:* ***************************************************************** * Inquire URIMAP START. * ********...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 18`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 5`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.245
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027778
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Source/ZECSNC.asm` (HLASM | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 12.15)
- **Top Global Matches:** file_cluster_9: 12.15, file_cluster_7: 12.876, file_cluster_12: 13.104
- **Magnitude:** 30.24 | **LOC:** 300 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 26.245; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.8%), Concurrency Surface (formerly Concurrency) (16.5%), Debt Markers (formerly Tech Debt) (12.3%), Complexity Load (formerly Cognitive Load) (7.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ZECSNC` **(I/O & Config Routines)** (Impact: 22.5)
    * *Intent:* * *********************************************************************** * Control Section * ******...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 121`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 1`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `concurrency: 1`
* *Defense:* `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.245
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027778
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Source/ZCEXPIRE.idcams` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.971)
- **Top Global Matches:** file_cluster_2: 1.971, file_cluster_17: 4.914, file_cluster_13: 6.213
- **Magnitude:** 15.4 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/ZECSFILE.idcams` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.971)
- **Top Global Matches:** file_cluster_2: 1.971, file_cluster_17: 4.914, file_cluster_13: 6.213
- **Magnitude:** 15.4 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/ZECSKEY.idcams` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.971)
- **Top Global Matches:** file_cluster_2: 1.971, file_cluster_17: 4.914, file_cluster_13: 6.213
- **Magnitude:** 15.4 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/CSDZECSX.rdo` (CSD | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.465)
- **Top Global Matches:** file_cluster_2: 2.465, file_cluster_17: 4.739, file_cluster_13: 6.079
- **Magnitude:** 15.22 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/CSDZC##.rdo` (CSD | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.827)
- **Top Global Matches:** file_cluster_15: 5.827, file_cluster_2: 5.873, file_cluster_17: 6.893
- **Magnitude:** 14.6 | **LOC:** 75 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 22.432; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (7.4%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ZX@id@` **(Parameter Forwarders)** (Impact: 2.8)
  * `ZC@id@` **(State Mutators)** (Impact: 2.1)
  * `ZD@id@` **(State Mutators)** (Impact: 2.1)
  * `ZR@id@` **(State Mutators)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 6`, `func_start: 4`
* *Risk/State:* None
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ZECS000, ZECS001
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/CSDZECSS.rdo` (CSD | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.197)
- **Top Global Matches:** file_cluster_2: 2.197, file_cluster_17: 4.973, file_cluster_13: 6.293
- **Magnitude:** 13.64 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/CSDZECSN.rdo` (CSD | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.228)
- **Top Global Matches:** file_cluster_2: 2.228, file_cluster_17: 4.987, file_cluster_13: 6.303
- **Magnitude:** 13.12 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/CSDZECSR.rdo` (CSD | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.228)
- **Top Global Matches:** file_cluster_2: 2.228, file_cluster_17: 4.987, file_cluster_13: 6.303
- **Magnitude:** 13.12 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/CSDZECS.rdo` (CSD | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.697)
- **Top Global Matches:** file_cluster_15: 6.697, file_cluster_2: 7.573, file_cluster_13: 7.8
- **Magnitude:** 12.14 | **LOC:** 42 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 22.432; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (10.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ZPLT` **(Parameter Forwarders)** (Impact: 2.2)
  * `ZNCD` **(State Mutators)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 7`, `func_start: 2`, `class_start: 5`
* *Risk/State:* None
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ZECS000, ZECS0001, ZECS002, ZECS003, ZECSNC, ZECSPLT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/DEFZC##.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.692)
- **Top Global Matches:** file_cluster_11: 5.692, file_cluster_2: 6.889, file_cluster_15: 7.949
- **Magnitude:** 11.46 | **LOC:** 87 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 22.432; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.1%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CONFIG` **(I/O & Config Routines)** (Impact: 1.9)
    * *Intent:* //DEFZC## JOB @job_parms@ //********************************************************************** /...
  * `CUSTOMIZ` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /* //SYSUT2 DD DISP=(NEW,PASS),DSN=&&STRINGS, // UNIT=VIO,SPACE=(80,(1000,1000)), // DCB=(LRECL=80,R...
  * `ECSFILEC` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /* //********************************************************************** //* Define the CSD defin...
  * `ECSKEYC` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /* //********************************************************************** //* Define the ECSFILE f...
  * `DEFINE` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* /* //********************************************************************** //* Define the CSD defin...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 30`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`
* *Architecture:* `io: 15`
* *Defense:* `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` @cics_csd@, @cics_hlq@.SDFHLOAD, @source_lib@(CSDZC##), @source_lib@(ZECSFILE), @source_lib@(ZECSKEY)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_config.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/ASMZECS.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.266)
- **Top Global Matches:** file_cluster_2: 5.266, file_cluster_17: 7.402, file_cluster_15: 7.797
- **Magnitude:** 9.16 | **LOC:** 65 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ZECS000` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* //ASMZECS JOB @job_parms@ //********************************************************************** /...
  * `ZECS001` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* /* //********************************************************************** //* Compile and link ZEC...
  * `ZECS002` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* /* //********************************************************************** //* Assemble and link ZE...
  * `ZECS003` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* /* //********************************************************************** //* Compile and link ZEC...
  * `ZECSNC` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* /* //********************************************************************** //* Assemble and link ZE...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 6`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/DEFEXPR.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.451)
- **Top Global Matches:** file_cluster_11: 5.451, file_cluster_2: 6.831, file_cluster_17: 7.854
- **Magnitude:** 7.82 | **LOC:** 59 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 22.432; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.2%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CUSTOMIZ` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* //* Create config file for following steps //*******************************************************...
  * `ECSFILEC` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /* //********************************************************************** //* Define the CSD defin...
  * `CONFIG` **(Interface Declarations)** (Impact: 1.4)
    * *Intent:* //DEFEXPR JOB @job_parms@ //********************************************************************** /...
  * `DEFINE` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* /* //********************************************************************** //* Define the CSD defin...
  * `ECSFILED` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* /* //********************************************************************** //* Define the ZCEXPIRE ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`
* *Architecture:* `io: 11`
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` @cics_csd@, @cics_hlq@.SDFHLOAD, @source_lib@(CSDZECSX), @source_lib@(ZCEXPIRE)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Installation.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 4.6 | **LOC:** 230 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 59.135; role: Pure Producer (Foundation)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.135
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055556
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `JCL/ZC##SD.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 4.814)
- **Top Global Matches:** file_cluster_11: 4.814, file_cluster_2: 6.267, file_cluster_17: 7.365
- **Magnitude:** 3.3 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 22.432; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DEFDOCT` **(Interface Declarations)** (Impact: 1.5)
    * *Intent:* /* //SYSUT2 DD DISP=SHR,DSN=@doct_lib@(ZC##SD) //SYSIN DD DUMMY //**********************************...
  * `CREATE` **(Interface Declarations)** (Impact: 1.4)
    * *Intent:* //ZC##SD JOB @job_parms@ //********************************************************************** //...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `func_start: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` @cics_csd@, @cics_hlq@.SDFHLOAD, @doct_lib@(ZC##SD)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/ZC##DC.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 4.836)
- **Top Global Matches:** file_cluster_11: 4.836, file_cluster_2: 6.301, file_cluster_17: 7.383
- **Magnitude:** 3.28 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 22.432; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DEFDOCT` **(Interface Declarations)** (Impact: 1.5)
    * *Intent:* /* //SYSUT2 DD DISP=SHR,DSN=@doct_lib@(ZC##DC) //SYSIN DD DUMMY //**********************************...
  * `CREATE` **(Interface Declarations)** (Impact: 1.4)
    * *Intent:* //ZC##DC JOB @job_parms@ //********************************************************************** //...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `func_start: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` @cics_csd@, @cics_hlq@.SDFHLOAD, @doct_lib@(ZC##DC)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `Source/CSDZC##.rdo` (CSD) | Magnitude: 14.6 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 61, import: 7, system_config_mutation: 7, args: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Source/ZECS001.cbl` -> **Severity: 0.238** (Bridge: 0.0024 * Flux: 99.994%)
- `Source/ZECS000.cbl` -> **Severity: 0.156** (Bridge: 0.0016 * Flux: 98.2708%)
- `Source/ZECS003.cbl` -> **Severity: 0.074** (Bridge: 0.0008 * Flux: 93.6053%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Source/ZECS003.cbl` -> **Severity: 3.706** (Embedded: 0.0625 * Error Risk: 59.295%)
- `Source/ZECS002.asm` -> **Severity: 3.487** (Embedded: 0.0625 * Error Risk: 55.7921%)
- `Source/ZECS000.cbl` -> **Severity: 3.482** (Embedded: 0.0556 * Error Risk: 62.6711%)
- `Source/ZECS001.cbl` -> **Severity: 1.869** (Embedded: 0.0278 * Error Risk: 67.2668%)
- `Source/ZECSNC.asm` -> **Severity: 1.799** (Embedded: 0.0278 * Error Risk: 64.7594%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Source/ZECS000.cbl` -> **Severity: 3577.8** (Blast Radius: 35.778 * Doc Risk: 100.0%)
- `Source/ZECS003.cbl` -> **Severity: 3303.7** (Blast Radius: 33.037 * Doc Risk: 100.0%)
- `Source/ZECS002.asm` -> **Severity: 3303.7** (Blast Radius: 33.037 * Doc Risk: 100.0%)
- `Source/ZECS001.cbl` -> **Severity: 3196.5** (Blast Radius: 31.965 * Doc Risk: 100.0%)
- `Source/ZECSPLT.cbl` -> **Severity: 2624.5** (Blast Radius: 26.245 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `28` files carry mainframe facts -- `77` call sites, `102` dataset bindings, `656` record items.

- **CICS resources:** `26` CSD `DEFINE` records (FILE→DSNAME, TDQUEUE, DB2TRAN→DB2ENTRY→PLAN, MAPSET, LIBRARY, ...), full attributes in `csd_resource_data`.

- **CICS operations:** `61` EXEC CICS operations naming a resource (`26` FILE, `5` QUEUE, `30` WEB); verb, direction, VALUE-resolved name and INTO/FROM record in `cics_resource_data`.

- **CICS task control:** `7` commands (`1` DELAY, `1` ENQ, `1` RETRIEVE, `4` START); child transid (or its STRING-built pattern), channel, CHILD/REQID token and timing in `cics_task_data`.

### `Source/ZECS001.cbl` (COBOL)
- **Calls:** `XCTL ZECS003`, `LINK ZECS002`, `CALL ZUIDSTCK`
- **COMMAREA passed:** `XCTL ZECS003 ← ZECS003-COMM-AREA`, `LINK ZECS002 ← ZECS002-COMM-AREA`
- **Record layouts (321 items):** `FILE-ERROR (15)`, `KEY-ERROR (12)`, `ZECS002-COMM-AREA (8)`, `TD-RECORD (8)`, `50702-MESSAGE (8)`, `WEB-ERROR (8)`, `SD-DSECT (7)`, `FILLER (6)`, `DC-CONTROL (6)`, `DELETE-RECORD (6)`, `LINKAGE-ADDRESSES (5)`, `FILLER (5)` … (+188 more)
- **CICS operations:** `WEB ? (close/read/write)`, `WEB Authorization (read)`, `FILE ZK-FCT? (delete/read/update/write)`, `FILE ZF-FCT? (delete/read/update/write)`, `WEB URL-HOST-NAME? (open)`, `WEB WEB-PATH? (converse)`, `WEB HEADER-ACAO? (write)`, `QUEUE @tdq@ (write)`
- **Data moves:** 221 (ADD 11, DIVIDE 4, MOVE 178, MULTIPLY 2, SUBTRACT 13, UNSTRING 13); most-fed items `HTTP-507-LENGTH`, `HTTP-507-TEXT`, `FE-FN`, `ZF-LENGTH`, `ZF-SEGMENT`, `HTTP-KEY-ERROR`
- **Unit of work:** `1` commit / `1` rollback points; handlers none; `19/55` RESP results tested

### `JCL/CONFIG.jcl` (JCL)
- **Calls:** `EXEC PGM IKJEFT1B`, `EXEC PGM IEBGENER`
- **Datasets:** `INPUT→@JCL_LIB@(ASMZECS)`, `STRINGS→@SOURCE_LIB@(CONFIG)`, `SYSUT2→@JCL_LIB@(ASMZECS)`, `INPUT→@JCL_LIB@(CSDZECS)`, `STRINGS→@SOURCE_LIB@(CONFIG)`, `SYSUT2→@JCL_LIB@(CSDZECS)`, `INPUT→@JCL_LIB@(CSDZECSN)`, `STRINGS→@SOURCE_LIB@(CONFIG)`, `SYSUT2→@JCL_LIB@(CSDZECSN)`, `INPUT→@JCL_LIB@(CSDZECSR)`, `STRINGS→@SOURCE_LIB@(CONFIG)`, `SYSUT2→@JCL_LIB@(CSDZECSR)` … (+63)
- **Job flow:** `STEP01=IKJEFT1B` -> `STEP02=IEBGENER` -> `STEP03=IKJEFT1B` -> `STEP04=IEBGENER` -> `STEP05=IKJEFT1B` -> `STEP06=IEBGENER` -> `STEP07=IKJEFT1B` -> `STEP08=IEBGENER` -> `STEP09=IKJEFT1B` -> `STEP10=IEBGENER`; creates `&&OUTPUT`

### `Source/ZECS000.cbl` (COBOL)
- **Calls:** `START TRANSID EIBTRNID`
- **Record layouts (153 items):** `ZX-RECORD (14)`, `FILE-ERROR (12)`, `KEY-ERROR (12)`, `TD-RECORD (8)`, `FILLER (6)`, `DC-CONTROL (6)`, `ZECS-DC (4)`, `ZC-EXPIRE-ENQ (4)`, `ZC-PARM (3)`, `ZK-FCT (3)`, `ZF-FCT (3)`, `CURRENT-ABS (1)` … (+77 more)
- **CICS operations:** `FILE ZCEXPIRE (read/update/write)`, `FILE ZF-FCT? (delete/read/update)`, `FILE ZK-FCT? (delete)`, `WEB URL-HOST-NAME? (open)`, `WEB WEB-PATH? (converse)`, `WEB ? (close)`, `QUEUE @tdq@ (write)`
- **CICS task control:** `RETRIEVE`, `ENQ ZC-EXPIRE-ENQ`, `DELAY`, `START EIBTRNID`
- **Data moves:** 63 (ADD 4, MOVE 47, STRING 3, SUBTRACT 9); most-fed items `RELATIVE-TIME`, `WEB-PATH`, `THE-OTHER-DC-LENGTH`, `WEB-PATH-LENGTH`, `ZX-KEY`, `TTL-MILLISECONDS`
- **Unit of work:** `2` commit / `0` rollback points; handlers `ABEND->9100-ABEND`; `9/31` RESP results tested

### `Source/ZECS003.cbl` (COBOL)
- **Record layouts (100 items):** `FILE-ERROR (11)`, `KEY-ERROR (11)`, `TD-RECORD (8)`, `DC-CONTROL (6)`, `ZECS-DC (4)`, `ZK-FCT (3)`, `ZF-FCT (3)`, `DFHCOMMAREA (3)`, `CURRENT-ABS (1)`, `TWELVE (1)`, `TEN (1)`, `SEVEN (1)` … (+47 more)
- **CICS operations:** `FILE ZF-FCT? (delete/read)`, `FILE ZK-FCT? (delete)`, `WEB URL-HOST-NAME? (open)`, `WEB WEB-PATH? (converse)`, `WEB ? (close/write)`
- **Data moves:** 26 (ADD 1, MOVE 17, STRING 4, SUBTRACT 4); most-fed items `WEB-PATH`, `WEB-PATH-LENGTH`, `THE-OTHER-DC-LENGTH`, `DC-TRANID`, `DC-TYPE`, `URI-MAP`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `4/12` RESP results tested

### `Source/ECS001.cbl` (COBOL)
- **Record layouts (34 items):** `CICS-MSG (6)`, `CICS-MSG2 (6)`, `INPUT-PARMS (3)`, `TERM-DATA (2)`, `URIMAP-NAME (1)`, `SESSION-TOKEN (1)`, `ECS-KEY (1)`, `ECS-KEY-LEN (1)`, `TERM-DATA-LEN (1)`, `BODY-DATA (1)`, `BODY-DATA-LEN (1)`, `ECS-DATA (1)` … (+9 more)
- **CICS operations:** `WEB ECS001 (open)`, `WEB PATH-NAME? (converse)`, `WEB ? (close)`
- **Data moves:** 61 (ADD 3, MOVE 51, STRING 2, SUBTRACT 1, UNSTRING 4); most-fed items `TERM-LINES`, `CICS-MSG-RESP`, `CICS-MSG-RESP2`, `BODY-DATA`, `CICS-MSG-CODE`, `CICS-MSG-STATUS`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `5/7` RESP results tested

### `JCL/DEFZC##.jcl` (JCL)
- **Calls:** `EXEC PGM IEBGENER`, `EXEC PGM IKJEFT1B`, `EXEC PGM DFHCSDUP`, `EXEC PGM IDCAMS`
- **Datasets:** `INPUT→@SOURCE_LIB@(CSDZC##)`, `STEPLIB→@CICS_HLQ@.SDFHLOAD`, `DFHCSD→@CICS_CSD@`, `INPUT→@SOURCE_LIB@(ZECSFILE)`, `INPUT→@SOURCE_LIB@(ZECSKEY)`
- **Job flow:** `CONFIG=IEBGENER` -> `CUSTOMIZ=IKJEFT1B` -> `DEFINE=DFHCSDUP` -> `ECSFILEC=IKJEFT1B` -> `ECSFILED=IDCAMS` -> `ECSKEYC=IKJEFT1B` -> `ECSKEYD=IDCAMS`; creates `&&CSDCMDS`, `&&STRINGS`, `&&ZECSFILE`, `&&ZECSKEY`

### `Source/ZECSPLT.cbl` (COBOL)
- **Calls:** `START TRANSID ZX-TRANID`
- **Record layouts (23 items):** `TD-RECORD (8)`, `URI-MAP (3)`, `ZX-TRANID (3)`, `ST-CODE (1)`, `EOF (1)`, `ZC (1)`, `URI-TRAN (1)`, `ZC-LENGTH (1)`, `CSSL (1)`, `TD-LENGTH (1)`, `URI-PATH (1)`, `DFHCOMMAREA (1)`
- **CICS operations:** `QUEUE @tdq@ (write)`
- **CICS task control:** `START ZX-TRANID`
- **Data moves:** 6 (MOVE 6); most-fed items `TD-PATH`, `TD-SUFFIX`, `TD-TRAN`, `ZX-SUFFIX`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `1/6` RESP results tested

### `JCL/DEFEXPR.jcl` (JCL)
- **Calls:** `EXEC PGM IEBGENER`, `EXEC PGM IKJEFT1B`, `EXEC PGM DFHCSDUP`, `EXEC PGM IDCAMS`
- **Datasets:** `INPUT→@SOURCE_LIB@(CSDZECSX)`, `STEPLIB→@CICS_HLQ@.SDFHLOAD`, `DFHCSD→@CICS_CSD@`, `INPUT→@SOURCE_LIB@(ZCEXPIRE)`
- **Job flow:** `CONFIG=IEBGENER` -> `CUSTOMIZ=IKJEFT1B` -> `DEFINE=DFHCSDUP` -> `ECSFILEC=IKJEFT1B` -> `ECSFILED=IDCAMS`; creates `&&CSDCMDS`, `&&STRINGS`, `&&ZCEXPIRE`

### `JCL/ASMZECS.jcl` (JCL)
- **Job flow:** `ZECS000=PROC DFHYITVL` -> `ZECS001=PROC DFHYITVL` -> `ZECS002=PROC DFHEITAL` -> `ZECS003=PROC DFHYITVL` -> `ZECSNC=PROC DFHEITAL` -> `ZECSPLT=PROC DFHYITVL`

### `Source/ZECSZFC.cpy` (COBOL)
- **Record layouts (17 items):** `ZF-RECORD (16)`, `ZF-PREFIX (1)`

### `JCL/ZC##DC.jcl` (JCL)
- **Calls:** `EXEC PGM IEBGENER`, `EXEC PGM DFHCSDUP`
- **Datasets:** `SYSUT2→@DOCT_LIB@(ZC##DC)`, `STEPLIB→@CICS_HLQ@.SDFHLOAD`, `DFHCSD→@CICS_CSD@`
- **CSD resources:** `DOCTEMPLATE x1`
- **Job flow:** `CREATE=IEBGENER` -> `DEFDOCT=DFHCSDUP`

### `JCL/ZC##SD.jcl` (JCL)
- **Calls:** `EXEC PGM IEBGENER`, `EXEC PGM DFHCSDUP`
- **Datasets:** `SYSUT2→@DOCT_LIB@(ZC##SD)`, `STEPLIB→@CICS_HLQ@.SDFHLOAD`, `DFHCSD→@CICS_CSD@`
- **CSD resources:** `DOCTEMPLATE x1`
- **Job flow:** `CREATE=IEBGENER` -> `DEFDOCT=DFHCSDUP`

### `Source/ZECSNC.asm` (HLASM)
- **Calls:** `START TRANSID Z_EXP`
- **CICS operations:** `QUEUE @tdq@ (write)`
- **CICS task control:** `START Z_EXP`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `1/11` RESP results tested

### `Source/CSDZC##.rdo` (CSD)
- **CSD resources:** `FILE x2`, `TRANCLASS x4`, `TRANSACTION x4`, `URIMAP x3`
- **CICS bindings:** `FILE ZC@ID@FILE→@ECS_HLQ@.ZC@ID@FILE.@ENVIRONMENT@`, `FILE ZC@ID@KEY→@ECS_HLQ@.ZC@ID@KEY.@ENVIRONMENT@`

### `JCL/CSDZECS.jcl` (JCL)
- **Calls:** `EXEC PGM DFHCSDUP`
- **Datasets:** `STEPLIB→@CICS_HLQ@.SDFHLOAD`, `DFHCSD→@CICS_CSD@`, `SYSIN→@SOURCE_LIB@(CSDZECS)`
- **Job flow:** `ZECSGRP=DFHCSDUP`

### `JCL/CSDZECSN.jcl` (JCL)
- **Calls:** `EXEC PGM DFHCSDUP`
- **Datasets:** `STEPLIB→@CICS_HLQ@.SDFHLOAD`, `DFHCSD→@CICS_CSD@`, `SYSIN→@SOURCE_LIB@(CSDZECSN)`
- **Job flow:** `STEP01=DFHCSDUP`

### `JCL/CSDZECSR.jcl` (JCL)
- **Calls:** `EXEC PGM DFHCSDUP`
- **Datasets:** `STEPLIB→@CICS_HLQ@.SDFHLOAD`, `DFHCSD→@CICS_CSD@`, `SYSIN→@SOURCE_LIB@(CSDZECSR)`
- **Job flow:** `STEP01=DFHCSDUP`

### `JCL/CSDZECSS.jcl` (JCL)
- **Calls:** `EXEC PGM DFHCSDUP`
- **Datasets:** `STEPLIB→@CICS_HLQ@.SDFHLOAD`, `DFHCSD→@CICS_CSD@`, `SYSIN→@SOURCE_LIB@(CSDZECSS)`
- **Job flow:** `STEP01=DFHCSDUP`

### `Source/ZECSZKC.cpy` (COBOL)
- **Record layouts (8 items):** `ZK-RECORD (8)`

### `Source/CSDZECS.rdo` (CSD)
- **CSD resources:** `PROGRAM x5`, `TRANSACTION x2`

*(+8 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 88% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: scheduler export (CA-7 / Control-M / TWS) (10 gaps); CSD extract (DFHCSDUP LIST / CICSPlex SM), or the web / API layer that LINKs it (2 gaps); application programs (source or load-module list) (1 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 260 call pairs -- scoped 69.2%, unique 0.0%, ambiguous 0.0%, external 30.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 181 | 99.4% | 0.0% | 0.0% | 0.6% |
| jcl | 76 | 0.0% | 0.0% | 0.0% | 100.0% |
| hlasm | 3 | 0.0% | 0.0% | 0.0% | 100.0% |

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
