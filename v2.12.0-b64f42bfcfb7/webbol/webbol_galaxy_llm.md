# ARCHITECTURAL_BRIEF: webbol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/jmsdnns/webbol` |
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
- **Scope:** 13 analyzed artifact(s), 621 LOC.
- **Load-bearing artifact:** `http-structs.cpy` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `webserver.cbl` -- pulls in 3 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `url-decode.cbl` at magnitude 169.24 (structural weight, not risk).
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
| Total Artifacts | 13 |
| Analyzed Artifacts (Scanned) | 13 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 0 |
| Total LOC | 621 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 100.0% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.28 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1021 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 10 | 596 | 76.9% |
| MAKEFILE | 1 | 24 | 7.7% |
| MARKDOWN | 1 | 0 | 7.7% |
| HTML | 1 | 1 | 7.7% |

## 4.1 SOURCE ENCODINGS
All 13 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 54%, Data / Markup / Trivial 23%, Declarative / Non-Code 23%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 12 | 92.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 7.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 0*


## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 88.1 | 30.7 | 11.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 86.4 | 35.6 | 29.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 8.8 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 8.2 | 1.9 | 1.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 49.9 | 49.3 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 50.0 | 29.2 | 50.0 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 3 | 3 | 1 | `Makefile` |
| guards | 1 | 1 | 0 | `webserver.cbl` |
| danger | 24 | 6 | 5 | `webserver.cbl` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 9 | 6 | 1 | `Makefile` |
| io | 2 | 1 | 0 | `file-ops.cbl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 13 | 2 | 4 | `webserver.cbl` |
| time | 0 | 0 | 0 | - |
| serialization | 4 | 1 | 0 | `http-handler.cbl` |
| regex | 16 | 4 | 2 | `http-handler.cbl` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 12 | 1 | 0 | `webserver.cbl` |
| mutation | 131 | 7 | 28 | `url-decode.cbl` |
| dead_code | 0 | 0 | 0 | - |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 1 | 1 | 0 | `webserver.cbl` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `file-ops.cbl` (Hits: 2)
- `Makefile` (Hits: 0)
- `README.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **http-structs.cpy** (`http-structs.cpy`) — 2 inbound connections
2. **config.cpy** (`config.cpy`) — 1 inbound connections
3. **file-ops.cbl** (`file-ops.cbl`) — 1 inbound connections
4. **file-structs.cpy** (`file-structs.cpy`) — 1 inbound connections
5. **http-handler.cbl** (`http-handler.cbl`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **webserver.cbl** (`webserver.cbl`) — 3 outbound dependencies
2. **http-handler.cbl** (`http-handler.cbl`) — 2 outbound dependencies
3. **Makefile** (`Makefile`) — 0 outbound dependencies
4. **README.md** (`README.md`) — 0 outbound dependencies
5. **config.cpy** (`config.cpy`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `DECODE-HEX-CHAR` **(I/O & Config Routines)** (@ `url-decode.cbl`) -> Impact: **48.8** | LOC: 76
  * *Intent:* *> Convert two-character hex code to actual character *> Handles common URL-encoded special characters used in web requests
- `MAIN-LOGIC` **(I/O & Config Routines)** (@ `file-ops.cbl`) -> Impact: **23.7** | LOC: 94
- `MAIN-LOGIC` **(I/O & Config Routines)** (@ `mime-types.cbl`) -> Impact: **22.9** | LOC: 58
  * *Intent:* *> Main MIME type detection logic
- `MAIN-LOGIC` **(I/O & Config Routines)** (@ `path-utils.cbl`) -> Impact: **14.6** | LOC: 72
  * *Intent:* *> Main path validation and sanitization logic
- `MAIN-LOGIC` **(I/O & Config Routines)** (@ `http-handler.cbl`) -> Impact: **13.9** | LOC: 99
  * *Intent:* *> Main HTTP request processing logic
- `HANDLE-REQUEST` **(I/O & Config Routines)** (@ `webserver.cbl`) -> Impact: **11.0** | LOC: 60
  * *Intent:* *> Read HTTP request from client and generate response
- `MAIN-LOGIC` **(I/O & Config Routines)** (@ `url-decode.cbl`) -> Impact: **9.5** | LOC: 50
  * *Intent:* *> Main URL decoding logic
- `INIT-SOCKET` **(I/O & Config Routines)** (@ `webserver.cbl`) -> Impact: **8.0** | LOC: 59
  * *Intent:* *> Create and configure a TCP socket for the web server
- `MAIN-LOGIC` **(I/O & Config Routines)** (@ `webserver.cbl`) -> Impact: **4.0** | LOC: 19
  * *Intent:* *> Main program entry point
- `ACCEPT-LOOP` **(I/O & Config Routines)** (@ `webserver.cbl`) -> Impact: **3.4** | LOC: 28
  * *Intent:* *> Main server loop - accept and handle client connections

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 13 | 504.77 | 28.37% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `file-ops.cbl` -> **100.0%** Exposure
- `mime-types.cbl` -> **100.0%** Exposure
- `path-utils.cbl` -> **100.0%** Exposure
- `url-decode.cbl` -> **100.0%** Exposure
- `http-handler.cbl` -> **99.7728%** Exposure

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
- **Unknown Dependencies:** `5` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `url-decode.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.759)
- **Top Global Matches:** file_cluster_3: 7.759, file_cluster_8: 21.403, file_cluster_6: 34.162
- **Magnitude:** 169.24 | **LOC:** 161 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 78.745; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.1%), Guard Balance (formerly Safety Score) (86.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DECODE-HEX-CHAR` **(I/O & Config Routines)** (Impact: 48.8)
    * *Intent:* *> Convert two-character hex code to actual character *> Handles common URL-encoded special characte...
  * `MAIN-LOGIC` **(I/O & Config Routines)** (Impact: 9.5)
    * *Intent:* *> Main URL decoding logic
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 78.745
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `file-ops.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.014)
- **Top Global Matches:** file_cluster_1: 6.014, file_cluster_3: 48.282, file_cluster_8: 70.091
- **Magnitude:** 82.58 | **LOC:** 130 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 78.745; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.8%), Complexity Load (formerly Cognitive Load) (68.3%), Connectivity (formerly Api Exposure) (2.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-LOGIC` **(I/O & Config Routines)** (Impact: 23.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 17`, `args: 2`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 78.745
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mime-types.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.221)
- **Top Global Matches:** file_cluster_1: 6.221, file_cluster_3: 48.31, file_cluster_8: 70.113
- **Magnitude:** 74.04 | **LOC:** 82 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 78.745; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (79.1%), Guard Balance (formerly Safety Score) (78.1%), Connectivity (formerly Api Exposure) (3.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-LOGIC` **(I/O & Config Routines)** (Impact: 22.9)
    * *Intent:* *> Main MIME type detection logic
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 10`, `args: 2`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 78.745
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `http-handler.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.606)
- **Top Global Matches:** file_cluster_2: 6.606, file_cluster_15: 6.954, file_cluster_16: 7.598
- **Magnitude:** 53.04 | **LOC:** 239 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 81.482; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (59.1%), Complexity Load (formerly Cognitive Load) (42.9%), Connectivity (formerly Api Exposure) (2.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-LOGIC` **(I/O & Config Routines)** (Impact: 13.9)
    * *Intent:* *> Main HTTP request processing logic
  * `BUILD-200-RESPONSE` **(I/O & Config Routines)** (Impact: 3.0)
    * *Intent:* *> Build HTTP 200 OK response with file content
  * `BUILD-404-RESPONSE` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *> Build HTTP 404 Not Found response
  * `BUILD-403-RESPONSE` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *> Build HTTP 403 Forbidden response (for security violations)
  * `BUILD-413-RESPONSE` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *> Build HTTP 413 Payload Too Large response (for oversized files)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 16`, `args: 10`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 81.482
  * `Choke Point (Betweenness):` 0.037879 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 6):` file-structs, http-structs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `webserver.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.189)
- **Top Global Matches:** file_cluster_2: 7.189, file_cluster_15: 7.291, file_cluster_16: 7.867
- **Magnitude:** 49.9 | **LOC:** 200 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 67.202; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Guard Balance (formerly Safety Score) (61.8%), Complexity Load (formerly Cognitive Load) (23.0%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HANDLE-REQUEST` **(I/O & Config Routines)** (Impact: 11.0)
    * *Intent:* *> Read HTTP request from client and generate response
  * `INIT-SOCKET` **(I/O & Config Routines)** (Impact: 8.0)
    * *Intent:* *> Create and configure a TCP socket for the web server
  * `MAIN-LOGIC` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* *> Main program entry point
  * `ACCEPT-LOOP` **(I/O & Config Routines)** (Impact: 3.4)
    * *Intent:* *> Main server loop - accept and handle client connections
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 31`, `args: 18`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 11`
* *Architecture:* `import: 3`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 67.202
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` config, http-structs, socket-defs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `path-utils.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.466)
- **Top Global Matches:** file_cluster_9: 6.466, file_cluster_16: 12.265, file_cluster_15: 12.337
- **Magnitude:** 45.7 | **LOC:** 104 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 78.745; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.4%), Complexity Load (formerly Cognitive Load) (67.4%), Connectivity (formerly Api Exposure) (3.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-LOGIC` **(I/O & Config Routines)** (Impact: 14.6)
    * *Intent:* *> Main path validation and sanitization logic
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 13`, `args: 2`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 78.745
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.695)
- **Top Global Matches:** file_cluster_2: 5.695, file_cluster_13: 7.07, file_cluster_11: 7.243
- **Magnitude:** 13.58 | **LOC:** 49 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (8.2%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `url-decode.o` **(I/O & Config Routines)** (Impact: 1.3)
  * `run` **(I/O & Config Routines)** (Impact: 1.2)
    * *Intent:* # Run the server
  * `all` **(State Mutators)** (Impact: 1.1)
    * *Intent:* # Default target
  * `path-utils.o` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* # Compile modules to object files
  * `mime-types.o` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `func_start: 8`
* *Risk/State:* None
* *Architecture:* `api: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.202
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.514)
- **Top Global Matches:** file_cluster_2: 4.514, file_cluster_17: 5.545, file_cluster_13: 6.03
- **Magnitude:** 10.52 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.202
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 3.32 | **LOC:** 166 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.202
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `http-structs.cpy` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.131)
- **Top Global Matches:** file_cluster_2: 2.131, file_cluster_17: 4.943, file_cluster_13: 6.272
- **Magnitude:** 0.76 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 93.025; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 93.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `socket-defs.cpy` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.089)
- **Top Global Matches:** file_cluster_2: 2.089, file_cluster_17: 4.924, file_cluster_13: 6.259
- **Magnitude:** 0.76 | **LOC:** 30 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 81.482; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 81.482
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `file-structs.cpy` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.149)
- **Top Global Matches:** file_cluster_2: 2.149, file_cluster_17: 4.951, file_cluster_13: 6.278
- **Magnitude:** 0.73 | **LOC:** 19 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 78.745; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 78.745
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `config.cpy` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.314)
- **Top Global Matches:** file_cluster_2: 2.314, file_cluster_17: 5.027, file_cluster_13: 6.332
- **Magnitude:** 0.6 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 81.482; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 81.482
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `webserver.cbl` (COBOL) | Magnitude: 49.9 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 31, args: 18, branch: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `http-handler.cbl` -> **Severity: 3.779** (Bridge: 0.0379 * Flux: 99.7728%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `url-decode.cbl` -> **Severity: 9.596** (Embedded: 0.1111 * Error Risk: 86.3675%)
- `mime-types.cbl` -> **Severity: 8.68** (Embedded: 0.1111 * Error Risk: 78.1209%)
- `file-ops.cbl` -> **Severity: 8.084** (Embedded: 0.1111 * Error Risk: 72.7595%)
- `path-utils.cbl` -> **Severity: 7.603** (Embedded: 0.1111 * Error Risk: 68.4242%)
- `http-handler.cbl` -> **Severity: 4.926** (Embedded: 0.0833 * Error Risk: 59.1077%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `http-handler.cbl` -> **Severity: 4074.1** (Blast Radius: 81.482 * Doc Risk: 50.0%)
- `file-ops.cbl` -> **Severity: 3937.25** (Blast Radius: 78.745 * Doc Risk: 50.0%)
- `mime-types.cbl` -> **Severity: 3937.25** (Blast Radius: 78.745 * Doc Risk: 50.0%)
- `path-utils.cbl` -> **Severity: 3937.25** (Blast Radius: 78.745 * Doc Risk: 50.0%)
- `url-decode.cbl` -> **Severity: 3937.25** (Blast Radius: 78.745 * Doc Risk: 50.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `10` files carry mainframe facts -- `13` call sites, `1` dataset bindings, `87` record items.

### `http-handler.cbl` (COBOL)
- **Calls:** `CALL URL-DECODE`, `CALL PATH-UTILS`, `CALL FILE-OPS`, `CALL MIME-TYPES`
- **Record layouts (10 items):** `WS-INDEX (1)`, `WS-SPACE-POS (1)`, `WS-PATH-LEN (1)`, `WS-RETURN-CODE (1)`, `WS-SIZE-STR (1)`, `WS-CRLF (1)`, `WS-DECODED-PATH (1)`, `LS-REQUEST-BUF (1)`, `LS-RESPONSE-BUF (1)`, `LS-RESPONSE-LEN (1)`
- **Data moves:** 48 (ADD 1, COMPUTE 3, MOVE 11, STRING 33); most-fed items `LS-RESPONSE-BUF`, `WS-PATH-LEN`, `LS-RESPONSE-LEN`, `REQUEST-METHOD`, `REQUEST-PATH`, `WS-INDEX`

### `url-decode.cbl` (COBOL)
- **Record layouts (9 items):** `WS-IN-INDEX (1)`, `WS-OUT-INDEX (1)`, `WS-LENGTH (1)`, `WS-CHAR (1)`, `WS-HEX-CODE (1)`, `WS-HEX-VALUE (1)`, `WS-DECODED-CHAR (1)`, `LS-INPUT-PATH (1)`, `LS-OUTPUT-PATH (1)`
- **Data moves:** 38 (ADD 6, MOVE 32); most-fed items `LS-OUTPUT-PATH`, `WS-CHAR`, `WS-HEX-CODE`

### `file-ops.cbl` (COBOL)
- **Datasets:** `WS-FILE-NAME(INPUT)`
- **Record layouts (14 items):** `LS-RETURN-CODE (4)`, `FILE-RECORD⟵DISK-FILE (1)`, `WS-FILE-NAME (1)`, `WS-FILE-STATUS (1)`, `WS-BUFFER-POS (1)`, `WS-LINE-LEN (1)`, `WS-EOF-FLAG (1)`, `WS-OVERFLOW-FLAG (1)`, `LS-FILE-PATH (1)`, `LS-FILE-BUFFER (1)`, `LS-FILE-SIZE (1)`
- **Data moves:** 22 (ADD 2, COMPUTE 1, MOVE 19); most-fed items `WS-FILE-NAME`, `LS-FILE-BUFFER`, `LS-FILE-SIZE`, `WS-BUFFER-POS`

### `webserver.cbl` (COBOL)
- **Calls:** `CALL socket`, `CALL setsockopt`, `CALL bind`, `CALL listen`, `CALL accept`, `CALL close`, `CALL recv`, `CALL HTTP-HANDLER`, `CALL send`
- **Record layouts (4 items):** `WS-REQUEST-COUNT (1)`, `WS-PORT-STR (1)`, `WS-PORT-NETWORK (1)`, `WS-HEADER-END (1)`
- **Data moves:** 11 (ADD 2, COMPUTE 2, MOVE 6, SUBTRACT 1); most-fed items `WS-PORT-NETWORK`, `SA-PORT`

### `mime-types.cbl` (COBOL)
- **Record layouts (5 items):** `WS-INDEX (1)`, `WS-LENGTH (1)`, `WS-EXT-START (1)`, `LS-FILE-PATH (1)`, `LS-MIME-TYPE (1)`
- **Data moves:** 17 (COMPUTE 1, MOVE 16); most-fed items `WS-EXT-START`

### `path-utils.cbl` (COBOL)
- **Record layouts (9 items):** `LS-RETURN-CODE (3)`, `WS-INDEX (1)`, `WS-LENGTH (1)`, `WS-CHAR (1)`, `WS-PREV-CHAR (1)`, `LS-INPUT-PATH (1)`, `LS-OUTPUT-PATH (1)`
- **Data moves:** 11 (MOVE 11); most-fed items `LS-OUTPUT-PATH`, `WS-CHAR`, `WS-PREV-CHAR`

### `socket-defs.cpy` (COBOL)
- **Record layouts (13 items):** `SERVER-ADDRESS (5)`, `SOCKET-HANDLE (1)`, `CLIENT-SOCKET (1)`, `SOCKET-RESULT (1)`, `BYTES-READ (1)`, `BYTES-SENT (1)`, `ADDR-LEN (1)`, `BACKLOG (1)`, `SOCKET-OPT (1)`

### `http-structs.cpy` (COBOL)
- **Record layouts (10 items):** `HTTP-REQUEST (4)`, `HTTP-RESPONSE (3)`, `STATUS-LINE (1)`, `CONTENT-TYPE-HDR (1)`, `CONTENT-LENGTH-HDR (1)`

### `file-structs.cpy` (COBOL)
- **Record layouts (9 items):** `FILE-EXISTS-FLAG (3)`, `FILE-BUFFER (1)`, `FILE-SIZE (1)`, `FILE-PATH (1)`, `SANITIZED-PATH (1)`, `MIME-TYPE (1)`, `FILE-EXTENSION (1)`

### `config.cpy` (COBOL)
- **Record layouts (4 items):** `SERVER-PORT (1)`, `MAX-CONNECTIONS (1)`, `BUFFER-SIZE (1)`, `MAX-PATH-LEN (1)`

- **Mainframe skeleton completeness:** 46% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: application programs (source or load-module list) (8 gaps); JCL and PROC libraries (1 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 21 call pairs -- scoped 38.1%, unique 23.8%, ambiguous 0.0%, external 38.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 21 | 38.1% | 23.8% | 0.0% | 38.1% |

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
