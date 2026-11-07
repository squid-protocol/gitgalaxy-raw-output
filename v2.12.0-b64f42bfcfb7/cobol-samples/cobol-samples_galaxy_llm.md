# ARCHITECTURAL_BRIEF: cobol-samples
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/neopragma/cobol-samples.git` |
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
- **Scope:** 34 analyzed artifact(s), 1521 LOC.
- **Load-bearing artifact:** `DATE1-notes.md` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `README.md` -- pulls in 15 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/main/cobol/IFEVAL.CBL` at magnitude 142.2 (structural weight, not risk).
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
| Total Artifacts | 53 |
| Analyzed Artifacts (Scanned) | 34 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 19 |
| Total LOC | 1521 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 64.2% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3435 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.661 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 16 | 0 | 47.1% |
| COBOL | 15 | 1458 | 44.1% |
| SHELL | 3 | 63 | 8.8% |

## 4.1 SOURCE ENCODINGS
All 34 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 50%, Large Core Modules 35%, Interface Declarations Files 9%, Compute Cores Files 3%, Declarative / Non-Code 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 18 | 52.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 16 | 47.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 19*

**Composition by Extension & Reason:**
- `no_extension`: 14x Excluded (Binary Format Detected), 3x Unsupported Format (.undeterminable), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bin`: 1x Excluded (Unsupported Extension: '.bin')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 82.9 | 31.4 | 20.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 86.7 | 60.8 | 58.8 | 79.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.6 | 2.4 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 3.5 | 0.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 81.8 | 98.2 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 16.3 | 1.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 86.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8 | 4 | 1 | `src/main/cobol/DATE1.CBL` |
| cleanup | 4 | 2 | 0 | `src/main/cobol/CPSEQFR.CBL` |
| guards | 0 | 0 | 0 | - |
| danger | 41 | 17 | 3 | `compile` |
| concurrency | 1 | 1 | 0 | `compile` |
| connectivity | 2 | 2 | 0 | `compile` |
| io | 23 | 4 | 3 | `compile` |
| crypto | 0 | 0 | 0 | - |
| ipc | 10 | 2 | 0 | `src/main/cobol/MOVEME.CBL` |
| time | 20 | 3 | 0 | `src/main/cobol/DATE1.CBL` |
| serialization | 10 | 5 | 1 | `src/main/cobol/STRINGIT.CBL` |
| regex | 18 | 4 | 1 | `src/main/cobol/STRINGIT.CBL` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 166 | 13 | 17 | `src/main/cobol/MOVEME.CBL` |
| mutation | 308 | 17 | 30 | `src/main/cobol/MOVEME.CBL` |
| dead_code | 3 | 2 | 0 | `src/main/cobol/NOTBOOL.CBL` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 4 | 1 | 0 | `src/main/cobol/ATTRACT.CBL` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `compile` (Hits: 7)
- `src/main/cobol/CPSEQFR.CBL` (Hits: 7)
- `src/main/cobol/CPSEQVR.CBL` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **DATE1-notes.md** (`DATE1-notes.md`) — 3 inbound connections
2. **DATE2-notes.md** (`DATE2-notes.md`) — 3 inbound connections
3. **COND88-notes.md** (`COND88-notes.md`) — 2 inbound connections
4. **HEX2TEXT.CBL** (`src/main/cobol/HEX2TEXT.CBL`) — 2 inbound connections
5. **ATTRACT-notes.md** (`ATTRACT-notes.md`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`README.md`) — 15 outbound dependencies
2. **HOURGLASS-notes.md** (`HOURGLASS-notes.md`) — 2 outbound dependencies
3. **DATE1-notes.md** (`DATE1-notes.md`) — 1 outbound dependencies
4. **DATE2-notes.md** (`DATE2-notes.md`) — 1 outbound dependencies
5. **IFEVAL-notes.md** (`IFEVAL-notes.md`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `COND88` **(I/O & Config Routines)** (@ `src/main/cobol/IFEVAL.CBL`) -> Impact: **32.3** | LOC: 126
- `NOTBOOL` **(I/O & Config Routines)** (@ `src/main/cobol/NOTBOOL.CBL`) -> Impact: **30.0** | LOC: 140
- `COND88` **(I/O & Config Routines)** (@ `src/main/cobol/COND88.CBL`) -> Impact: **22.3** | LOC: 66
- `REFORMER` **(I/O & Config Routines)** (@ `src/main/cobol/REFORMER.CBL`) -> Impact: **16.9** | LOC: 119
- `MOVEME` **(I/O & Config Routines)** (@ `src/main/cobol/MOVEME.CBL`) -> Impact: **11.6** | LOC: 171
- `INVCALC` **(I/O & Config Routines)** (@ `src/main/cobol/INVCALC.CBL`) -> Impact: **9.8** | LOC: 77
- `CPSEQFR` **(I/O & Config Routines)** (@ `src/main/cobol/CPSEQFR.CBL`) -> Impact: **8.3** | LOC: 26
- `PRINT-INVOICE-DETAILS` **(I/O & Config Routines)** (@ `src/main/cobol/INVCALC.CBL`) -> Impact: **8.2** | LOC: 44
- `ATTRACT` **(I/O & Config Routines)** (@ `src/main/cobol/ATTRACT.CBL`) -> Impact: **7.4** | LOC: 28
- `CPSEQVR` **(I/O & Config Routines)** (@ `src/main/cobol/CPSEQVR.CBL`) -> Impact: **6.2** | LOC: 25

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/main/cobol` | 15 | 718.96 | 31.68% | 0.0% |
| `__monolith__` | 19 | 82.4 | 4.77% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `compile` -> **100.0%** Exposure
- `src/main/cobol/COND88.CBL` -> **100.0%** Exposure
- `src/main/cobol/IFEVAL.CBL` -> **100.0%** Exposure
- `src/main/cobol/NOTBOOL.CBL` -> **100.0%** Exposure
- `src/main/cobol/INVCALC.CBL` -> **99.9994%** Exposure

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `14` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `21` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/main/cobol/IFEVAL.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.104)
- **Top Global Matches:** file_cluster_1: 6.104, file_cluster_3: 48.299, file_cluster_8: 70.107
- **Magnitude:** 142.2 | **LOC:** 153 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.7%), Complexity Load (formerly Cognitive Load) (81.4%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `COND88` **(I/O & Config Routines)** (Impact: 32.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/NOTBOOL.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.178)
- **Top Global Matches:** file_cluster_1: 6.178, file_cluster_3: 48.31, file_cluster_8: 70.113
- **Magnitude:** 118.68 | **LOC:** 185 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.2%), Complexity Load (formerly Cognitive Load) (78.3%), Dead Code Surface (formerly Dead Code) (16.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NOTBOOL` **(I/O & Config Routines)** (Impact: 30.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 29`, `dead_code: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/COND88.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.131)
- **Top Global Matches:** file_cluster_1: 6.131, file_cluster_3: 48.3, file_cluster_8: 70.108
- **Magnitude:** 89.72 | **LOC:** 100 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.9%), Guard Balance (formerly Safety Score) (81.0%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `COND88` **(I/O & Config Routines)** (Impact: 22.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/INVCALC.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.198)
- **Top Global Matches:** file_cluster_9: 7.198, file_cluster_11: 9.298, file_cluster_2: 9.683
- **Magnitude:** 75.04 | **LOC:** 175 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.4%), Complexity Load (formerly Cognitive Load) (54.6%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `INVCALC` **(I/O & Config Routines)** (Impact: 9.8)
  * `PRINT-INVOICE-DETAILS` **(I/O & Config Routines)** (Impact: 8.2)
  * `INVALID-INVOICE-DATA` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 26`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 39`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/REFORMER.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.72)
- **Top Global Matches:** file_cluster_9: 6.72, file_cluster_16: 12.33, file_cluster_15: 12.395
- **Magnitude:** 68.04 | **LOC:** 211 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (63.2%), Complexity Load (formerly Cognitive Load) (46.3%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `REFORMER` **(I/O & Config Routines)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 26`, `args: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 30`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/MOVEME.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.465)
- **Top Global Matches:** file_cluster_2: 6.465, file_cluster_15: 7.58, file_cluster_17: 7.739
- **Magnitude:** 66.08 | **LOC:** 230 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.8%), Complexity Load (formerly Cognitive Load) (35.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MOVEME` **(I/O & Config Routines)** (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 66`, `args: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compile` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.493)
- **Top Global Matches:** file_cluster_7: 7.493, file_cluster_14: 9.426, file_cluster_12: 9.86
- **Magnitude:** 51.02 | **LOC:** 70 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 18.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (76.4%), Connectivity (formerly Api Exposure) (3.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `show_help` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 46`, `args: 8`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 8`
* *Architecture:* `io: 7`, `api: 1`, `import: 1`
* *Defense:* `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` envvars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/ATTRACT.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_11: 6.671, file_cluster_2: 7.168, file_cluster_15: 7.602
- **Magnitude:** 40.1 | **LOC:** 184 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Guard Balance (formerly Safety Score) (57.6%), Complexity Load (formerly Cognitive Load) (19.8%), Dead Code Surface (formerly Dead Code) (10.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ATTRACT` **(I/O & Config Routines)** (Impact: 7.4)
  * `ComputeAttraction` **(I/O & Config Routines)** (Impact: 3.5)
  * `SolicitAttributesOfBody` **(I/O & Config Routines)** (Impact: 2.2)
  * `VerifyAttributesOfBody` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 38`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`, `dead_code: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CPSEQFR.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.286)
- **Top Global Matches:** file_cluster_12: 8.286, file_cluster_7: 9.496, file_cluster_9: 10.18
- **Magnitude:** 19.86 | **LOC:** 86 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.8%), Guard Balance (formerly Safety Score) (58.4%), Complexity Load (formerly Cognitive Load) (17.0%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CPSEQFR` **(I/O & Config Routines)** (Impact: 8.3)
  * `END-OF-PROGRAM` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 13`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`
* *Architecture:* `io: 7`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CPSEQVR.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.948)
- **Top Global Matches:** file_cluster_12: 6.948, file_cluster_7: 7.703, file_cluster_11: 9.252
- **Magnitude:** 18.74 | **LOC:** 83 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.3%), Guard Balance (formerly Safety Score) (59.1%), Complexity Load (formerly Cognitive Load) (21.9%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CPSEQVR` **(I/O & Config Routines)** (Impact: 6.2)
  * `END-OF-PROGRAM` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 12`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `io: 6`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/HEX2TEXT.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.787)
- **Top Global Matches:** file_cluster_15: 5.787, file_cluster_2: 5.953, file_cluster_17: 6.759
- **Magnitude:** 18.5 | **LOC:** 43 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 48.731; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (58.5%), Complexity Load (formerly Cognitive Load) (37.3%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HEX2TEXT` **(Compute Cores)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `args: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.731
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.060606
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/main/cobol/DATE1.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.123)
- **Top Global Matches:** file_cluster_7: 7.123, file_cluster_12: 7.542, file_cluster_2: 9.74
- **Magnitude:** 18.24 | **LOC:** 176 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.2%), Guard Balance (formerly Safety Score) (58.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DATE1` **(I/O & Config Routines)** (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 11`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/STRINGIT.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.292)
- **Top Global Matches:** file_cluster_2: 6.292, file_cluster_17: 7.637, file_cluster_15: 7.757
- **Magnitude:** 17.9 | **LOC:** 113 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.3%), Guard Balance (formerly Safety Score) (54.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `STRINGIT` **(I/O & Config Routines)** (Impact: 5.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 19`, `args: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/DATE2.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.373)
- **Top Global Matches:** file_cluster_2: 5.373, file_cluster_17: 6.983, file_cluster_15: 7.327
- **Magnitude:** 15.8 | **LOC:** 180 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.4%), Mutation Surface (formerly State Flux) (45.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DATE2` **(I/O & Config Routines)** (Impact: 4.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compile-all` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 4.639)
- **Top Global Matches:** file_cluster_14: 4.639, file_cluster_7: 10.901, file_cluster_5: 14.683
- **Magnitude:** 11.86 | **LOC:** 14 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (70.0%), Complexity Load (formerly Cognitive Load) (14.2%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2`
* *Architecture:* `io: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/BRAKES.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.069)
- **Top Global Matches:** file_cluster_2: 5.069, file_cluster_17: 6.832, file_cluster_11: 7.039
- **Magnitude:** 6.5 | **LOC:** 60 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (52.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BRAKES` **(I/O & Config Routines)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/HELLO.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.808)
- **Top Global Matches:** file_cluster_2: 5.808, file_cluster_17: 7.348, file_cluster_11: 7.576
- **Magnitude:** 3.56 | **LOC:** 44 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Mutation Surface (formerly State Flux) (16.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HELLO` **(I/O & Config Routines)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.058)
- **Top Global Matches:** file_cluster_2: 3.058, file_cluster_17: 4.931, file_cluster_13: 6.21
- **Magnitude:** 1.88 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MOVEME-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.7 | **LOC:** 85 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 19.071; role: Pure Producer (Foundation)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030303
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `HOURGLASS-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.56 | **LOC:** 78 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 19.071; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030303
  * `Imports (Out-Degree: 2):` DATE1-notes.md, DATE2-notes.md
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.26 | **LOC:** 63 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 18.048; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` ATTRACT-notes.md, BRAKES-notes.md, COND88-notes.md, CPSEQFR-notes.md, CPSEQVR-notes.md, DATE1-notes.md, DATE2-notes.md, HELLO-notes.md...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `DATE2-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.08 | **LOC:** 54 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 181.136; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 181.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.090909
  * `Imports (Out-Degree: 1):` DATE1-notes.md
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ATTRACT-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.04 | **LOC:** 52 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 19.071; role: Pure Producer (Foundation)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030303
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `BRAKES-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 19.071; role: Pure Producer (Foundation)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030303
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COND88-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 35.281; role: Pure Producer (Foundation)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 35.281
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.060606
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/main/cobol/HEX2TEXT.CBL` -> **Severity: 3.545** (Embedded: 0.0606 * Error Risk: 58.4884%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/main/cobol/HEX2TEXT.CBL` -> **Severity: 4873.1** (Blast Radius: 48.731 * Doc Risk: 100.0%)
- `src/main/cobol/ATTRACT.CBL` -> **Severity: 1804.8** (Blast Radius: 18.048 * Doc Risk: 100.0%)
- `src/main/cobol/BRAKES.CBL` -> **Severity: 1804.8** (Blast Radius: 18.048 * Doc Risk: 100.0%)
- `src/main/cobol/COND88.CBL` -> **Severity: 1804.8** (Blast Radius: 18.048 * Doc Risk: 100.0%)
- `src/main/cobol/CPSEQFR.CBL` -> **Severity: 1804.8** (Blast Radius: 18.048 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `15` files carry mainframe facts -- `10` call sites, `4` dataset bindings, `457` record items.

### `src/main/cobol/DATE2.CBL` (COBOL)
- **Record layouts (79 items):** `DATE-DATA (21)`, `MONTH-ABBR-DATA (13)`, `DAY-ORDINALS-DATA (11)`, `DAY-NAMES-DATA (8)`, `SHORTHAND-DATE-US-STYLE (6)`, `SHORTHAND-DATE-EURO-STYLE (6)`, `FILLER (6)`, `DAY-CALCULATION-FIELDS (3)`, `FILER (2)`, `FILLER (2)`, `FULL-DATE (1)`
- **Data moves:** 25 (ACCEPT 6, DIVIDE 4, MOVE 6, STRING 9); most-fed items `FULL-DATE`, `DAY-DIV-BY-10`, `DAY-LAST-DIGIT`, `DAY-OF-MONTH OF SHORTHAND-DATE-EURO-STYLE`, `DAY-OF-MONTH OF SHORTHAND-DATE-US-STYLE`, `MONTH OF SHORTHAND-DATE-EURO-STYLE`

### `src/main/cobol/DATE1.CBL` (COBOL)
- **Record layouts (83 items):** `NCSA-TIMESTAMP (18)`, `CURRENT-DATE-DATA (17)`, `MONTH-ABBR-DATA (13)`, `DAY-ORDINALS-DATA (11)`, `SHORTHAND-DATE-US-STYLE (6)`, `SHORTHAND-DATE-EURO-STYLE (6)`, `FILLER (6)`, `DAY-CALCULATION-FIELDS (3)`, `FILER (2)`, `FULL-DATE (1)`
- **Data moves:** 19 (DIVIDE 4, MOVE 9, STRING 6); most-fed items `FULL-DATE`, `NCSA-TIMESTAMP`, `DAY-DIV-BY-10`, `DAY-LAST-DIGIT`, `MONTH-ABBR OF NCSA-TIMESTAMP`, `SHORTHAND-DATE-EURO-STYLE`

### `src/main/cobol/REFORMER.CBL` (COBOL)
- **Calls:** `CALL HEX2TEXT`
- **Record layouts (62 items):** `FILLER (53)`, `HEX-OUTPUT-RECORD (5)`, `WS-HEX2TEXT-CONVERSION (4)`
- **Data moves:** 27 (ADD 1, MOVE 21, STRING 2, UNSTRING 3); most-fed items `OUT-SKU`, `WS-SKU-PREFIX`, `HEX-OUTPUT-RECORD-HIGH-ORDER`, `HEX-OUTPUT-RECORD-LOW-ORDER`, `OUT-INV-DATE-YYYY-MM-DD`, `OUT-INVOICE-NO`

### `src/main/cobol/ATTRACT.CBL` (COBOL)
- **Record layouts (49 items):** `GENERALWORKAREAS (34)`, `COMPUTATIONALWORKAREAS (15)`
- **Data moves:** 34 (ACCEPT 6, COMPUTE 18, MOVE 10); most-fed items `F`, `D`, `DX`, `DY`, `FX`, `FY`

### `src/main/cobol/INVCALC.CBL` (COBOL)
- **Record layouts (33 items):** `INVOICE (16)`, `INVOICE-FORMATTED (9)`, `FILLER (8)`
- **Data moves:** 42 (ADD 4, INITIALIZE 1, MOVE 33, MULTIPLY 4); most-fed items `INV-DATE-FORMATTED`, `LINE-WORKING-TOTAL`, `LINE-WORKING-TAX`, `CUMULATIVE-PRICE-BEFORE-TAX`, `CUMULATIVE-PRICE-WITH-TAX`, `CUMULATIVE-SALES-TAX`

### `src/main/cobol/MOVEME.CBL` (COBOL)
- **Calls:** `CALL HEX2TEXT`
- **Record layouts (34 items):** `WS-DATA-ITEMS (21)`, `WS-GROUP-ITEM (9)`, `WS-HEX2TEXT-CONVERSION (4)`
- **Data moves:** 30 (INITIALIZE 1, MOVE 29); most-fed items `WS-ORIGINAL-VALUE`

### `src/main/cobol/IFEVAL.CBL` (COBOL)
- **Record layouts (7 items):** `FILLER (7)`
- **Data moves:** 38 (ADD 1, DIVIDE 2, MOVE 33, SUBTRACT 2); most-fed items `NUMERIC-2`

### `src/main/cobol/NOTBOOL.CBL` (COBOL)
- **Record layouts (16 items):** `FILLER (16)`
- **Data moves:** 24 (COMPUTE 2, MOVE 22); most-fed items `EX4-FLAG`, `EX7-FLAG`, `EX2-FLAG`, `EX3-FLAG`

### `src/main/cobol/COND88.CBL` (COBOL)
- **Record layouts (17 items):** `FILLER (17)`
- **Data moves:** 18 (MOVE 18)

### `src/main/cobol/STRINGIT.CBL` (COBOL)
- **Record layouts (15 items):** `FILLER (15)`
- **Data moves:** 19 (ADD 4, INITIALIZE 2, MOVE 3, STRING 10); most-fed items `WS-OUTPUT-AREA`, `WS-OUTPUT-LENGTH`, `WS-FAMILY-NAME-OUT`, `WS-GIVEN-NAME-OUT`, `WS-MIDDLE-NAME-OUT`

### `src/main/cobol/HEX2TEXT.CBL` (COBOL)
- **Record layouts (17 items):** `LS-HEX2TEXT-CONVERSION (4)`, `FILLER (3)`, `HEXVAL (1)`, `HEXSTR (1)`, `DEC (1)`, `I (1)`, `J (1)`, `Q (1)`, `R (1)`, `J1 (1)`, `Q1 (1)`, `R1 (1)`
- **Data moves:** 11 (COMPUTE 4, DIVIDE 4, MOVE 3); most-fed items `LS-RESULT`, `DECBYTE`, `J`, `J1`, `Q`, `Q1`

### `src/main/cobol/CPSEQVR.CBL` (COBOL)
- **Datasets:** `VARFILE1(INPUT/OUTPUT)`, `VARFILE2(OUTPUT)`
- **Record layouts (14 items):** `WORKAREAS (10)`, `RECORD-AREA (2)`, `INPUT-RECORD⟵INFILE (1)`, `OUTPUT-RECORD⟵OUTFILE (1)`
- **Data moves:** 7 (ADD 2, COMPUTE 2, MOVE 2, WRITE 1); most-fed items `FIELD-COUNT`, `OUT-RECLEN`, `OUTPUT-RECORD`, `RECORD-AREA`

### `src/main/cobol/CPSEQFR.CBL` (COBOL)
- **Datasets:** `INFILE1(INPUT/OUTPUT)`, `OUTFILE1(OUTPUT)`
- **Record layouts (13 items):** `WORKAREAS (7)`, `INPUT-RECORD⟵INFILE (3)`, `OUTPUT-RECORD⟵OUTFILE (3)`
- **Data moves:** 3 (ADD 1, MOVE 2); most-fed items `OUTPUT-FIRST-30`, `OUTPUT-LAST-10`

### `src/main/cobol/BRAKES.CBL` (COBOL)
- **Record layouts (11 items):** `GIVEN-VALUES (6)`, `CALCULATED-VALUES (5)`
- **Data moves:** 8 (COMPUTE 7, MOVE 1); most-fed items `MGH`, `DELTAT-CELSIUS`, `MC`, `DELTAT-CELSIUS-FORMATTED`

### `src/main/cobol/HELLO.CBL` (COBOL)
- **Record layouts (7 items):** `WS-MESSAGES (7)`
- **Data moves:** 4 (ACCEPT 1, STRING 3); most-fed items `WS-MESSAGE`

- **Mainframe skeleton completeness:** 66% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: JCL and PROC libraries (14 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 16 call pairs -- scoped 43.8%, unique 12.5%, ambiguous 0.0%, external 43.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| shell | 9 | 22.2% | 0.0% | 0.0% | 77.8% |
| cobol | 7 | 71.4% | 28.6% | 0.0% | 0.0% |

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
