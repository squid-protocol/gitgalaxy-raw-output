# ARCHITECTURAL_BRIEF: bitcoin-0.1.0
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/trottier/original-bitcoin.git` |
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
- **Scope:** 33 analyzed artifact(s), 14716 LOC.
- **Load-bearing artifact:** `src/util.h` -- 11 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/headers.h` -- pulls in 50 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/ui.cpp` at magnitude 1903.14 (structural weight, not risk).
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
| Total Artifacts | 50 |
| Analyzed Artifacts (Scanned) | 33 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17 |
| Total LOC | 14716 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.0% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1628 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2933 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 51.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4895 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 26 | 14615 | 78.8% |
| PLAINTEXT | 4 | 0 | 12.1% |
| MAKEFILE | 2 | 101 | 6.1% |
| MARKDOWN | 1 | 0 | 3.0% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 32 |
| cp1252 | cp1252-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 39%, Data / Markup / Trivial 18%, Parameter Forwarders Files 15%, Interface Declarations Files 9%, Compute Cores Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 28 | 84.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 15.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17*

**Composition by Extension & Reason:**
- `.bmp`: 9x Excluded (Explicitly Denied Extension: '.bmp')
- `.dll`: 2x Excluded (Explicitly Denied Extension: '.dll')
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.exe`: 1x Excluded (Explicitly Denied Extension: '.exe')
- `.rc`: 1x Unsupported Format (.rc)
- `.fbp`: 1x Unsupported Format (.fbp)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.5 | 38.7 | 43.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 74.5 | 56.8 | 59.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 38.6 | 32.9 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 55.1 | 80.0 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 58.9 | 22.0 | 9.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 66.7 | 98.5 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 36.1 | 4.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 91.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 318 | 14 | 8 | `src/uibase.cpp` |
| cleanup | 12 | 5 | 2 | `src/db.cpp` |
| guards | 1233 | 25 | 82 | `src/uint256.h` |
| danger | 145 | 20 | 12 | `src/ui.cpp` |
| concurrency | 1 | 1 | 0 | `src/makefile.vc` |
| connectivity | 294 | 19 | 26 | `src/uibase.h` |
| io | 28 | 7 | 2 | `src/net.cpp` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 9 | 5 | 1 | `src/net.cpp` |
| tests | 1 | 1 | 0 | `src/irc.cpp` |
| docs | 147 | 15 | 14 | `src/uibase.h` |
| debt | 327 | 16 | 36 | `src/main.cpp` |
| mutation | 3649 | 26 | 278 | `src/ui.cpp` |
| dead_code | 315 | 15 | 21 | `src/ui.cpp` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 14 | 2 | 0 | `src/uibase.cpp` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.8333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/net.cpp` (Hits: 15)
- `src/irc.cpp` (Hits: 4)
- `src/serialize.h` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.h** (`src/util.h`) — 11 inbound connections
2. **util.cpp** (`src/util.cpp`) — 10 inbound connections
3. **headers.h** (`src/headers.h`) — 8 inbound connections
4. **db.h** (`src/db.h`) — 7 inbound connections
5. **sha.h** (`src/sha.h`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **headers.h** (`src/headers.h`) — 50 outbound dependencies
2. **uibase.h** (`src/uibase.h`) — 28 outbound dependencies
3. **serialize.h** (`src/serialize.h`) — 4 outbound dependencies
4. **bignum.h** (`src/bignum.h`) — 3 outbound dependencies
5. **sha.cpp** (`src/sha.cpp`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `EvalScript` **(Many-Argument Workhorses)** (@ `src/script.cpp`) -> Impact: **807.3** | LOC: 763
  * *Intent:* // // Script is a stack machine (like Forth) that evaluates a predicate // returning a bool indicating valid or not. There are no loops. // #define st...
- `GetOpName` **(Compute Cores)** (@ `src/script.h`) -> Impact: **160.8** | LOC: 134
- `ProcessMessage` **(Many-Argument Workhorses)** (@ `src/main.cpp`) -> Impact: **159.8** | LOC: 357
- `CTransaction::ConnectInputs` **(Many-Argument Workhorses)** (@ `src/main.cpp`) -> Impact: **110.0** | LOC: 99
- `CMainFrame::InsertTransaction` **(Many-Argument Workhorses)** (@ `src/ui.cpp`) -> Impact: **109.4** | LOC: 188
- `CTxDetailsDialog::CTxDetailsDialog` **(Many-Argument Workhorses)** (@ `src/ui.cpp`) -> Impact: **86.9** | LOC: 214
  * *Intent:* ////////////////////////////////////////////////////////////////////////////// // // CTxDetailsDialog //
- `HtmlEscape` **(Compute Cores)** (@ `src/ui.cpp`) -> Impact: **62.1** | LOC: 29
- `ThreadSocketHandler2` **(Compute Cores)** (@ `src/net.cpp`) -> Impact: **57.6** | LOC: 219
- `SelectCoins` **(Many-Argument Workhorses)** (@ `src/main.cpp`) -> Impact: **57.0** | LOC: 100
- `ThreadIRCSeed` **(Compute Cores)** (@ `src/irc.cpp`) -> Impact: **52.1** | LOC: 108

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 30 | 11394.66 | 36.15% | 35.99% |
| `__monolith__` | 3 | 3.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/uibase.h` -> **100.0%** Exposure
- `src/market.h` -> **99.9995%** Exposure
- `src/ui.cpp` -> **99.7303%** Exposure
- `src/db.cpp` -> **99.1845%** Exposure
- `src/util.cpp` -> **98.8972%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/script.cpp` -> **100.0%** Exposure
- `src/market.cpp` -> **99.9998%** Exposure
- `src/util.cpp` -> **99.9997%** Exposure
- `src/main.cpp` -> **99.9988%** Exposure
- `src/uint256.h` -> **99.9986%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/ui.cpp` -> **134** Orphaned Functions | **0** Duplicates
- `src/uibase.h` -> **0** Orphaned Functions | **52** Duplicates
- `src/uibase.cpp` -> **32** Orphaned Functions | **0** Duplicates
- `src/main.cpp` -> **31** Orphaned Functions | **0** Duplicates
- `src/db.cpp` -> **20** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `104` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/ui.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.708)
- **Top Global Matches:** file_cluster_15: 7.708, file_cluster_12: 7.709, file_cluster_4: 7.881
- **Magnitude:** 1903.14 | **LOC:** 3229 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 35.974; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.1%)
- **Documentation Coverage:** 92.4731% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CMainFrame::InsertTransaction` **(Many-Argument Workhorses)** (Impact: 109.4)
  * `CTxDetailsDialog::CTxDetailsDialog` **(Many-Argument Workhorses)** (Impact: 86.9)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////// // // CTxDetailsDialo...
  * `HtmlEscape` **(Compute Cores)** (Impact: 62.1)
  * `CMyApp::OnInit2` **(I/O & Config Routines)** (Impact: 44.8)
  * `CViewProductDialog::UpdateProductDisplay` **(Compute Cores)** (Impact: 31.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 209 instances
* *State Mutation (weighted view):* 752
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 403`, `structural_boundaries: 264`, `args: 89`, `func_start: 186`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 1`, `state_mutation: 334`, `dead_code: 24`, `planned_debt: 2`, `unreferenced_by_name: 134`
* *Architecture:* `io: 2`, `api: 1`, `import: 2`
* *Defense:* `safety: 15`, `doc: 26`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 35.974
  * `Choke Point (Betweenness):` 0.052151 | `Ripple Effect (Closeness):` 0.177778
  * `Imports (Out-Degree: 12):` crtdbg.h, headers.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/main.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.535)
- **Top Global Matches:** file_cluster_4: 5.535, file_cluster_15: 10.339, file_cluster_9: 10.945
- **Magnitude:** 1888.6 | **LOC:** 2661 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 28.421; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.9%), Complexity Load (formerly Cognitive Load) (60.0%)
- **Documentation Coverage:** 91.5663% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ProcessMessage` **(Many-Argument Workhorses)** (Impact: 159.8)
  * `CTransaction::ConnectInputs` **(Many-Argument Workhorses)** (Impact: 110.0)
  * `SelectCoins` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `CTransaction::AcceptTransaction` **(Many-Argument Workhorses)** (Impact: 43.6)
  * `BitcoinMiner` **(I/O & Config Routines)** (Impact: 39.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 204 instances
* *State Mutation (weighted view):* 673
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 440`, `structural_boundaries: 185`, `args: 93`, `func_start: 83`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 265`, `dead_code: 6`, `planned_debt: 1`, `unreferenced_by_name: 31`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* `safety: 7`, `doc: 25`, `immutability_locks: 56`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.421
  * `Choke Point (Betweenness):` 0.054688 | `Ripple Effect (Closeness):` 0.190476
  * `Imports (Out-Degree: 14):` headers.h, sha.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/script.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.319)
- **Top Global Matches:** file_cluster_6: 6.319, file_cluster_4: 8.793, file_cluster_9: 15.842
- **Magnitude:** 1429.86 | **LOC:** 1128 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 18.003; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `EvalScript` **(Many-Argument Workhorses)** (Impact: 807.3)
    * *Intent:* // // Script is a stack machine (like Forth) that evaluates a predicate // returning a bool indicati...
  * `Solver` **(Compute Cores)** (Impact: 34.2)
  * `SignatureHash` **(Many-Argument Workhorses)** (Impact: 32.1)
    * *Intent:* #undef top
  * `Solver` **(Many-Argument Workhorses)** (Impact: 29.4)
  * `CheckSig` **(Many-Argument Workhorses)** (Impact: 19.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 135 instances
* *State Mutation (weighted view):* 407
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 81`, `args: 25`, `func_start: 14`
* *Risk/State:* `state_mutation: 137`, `dead_code: 4`, `unreferenced_by_name: 5`
* *Architecture:* `import: 1`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.003
  * `Choke Point (Betweenness):` 0.003427 | `Ripple Effect (Closeness):` 0.148148
  * `Imports (Out-Degree: 6):` headers.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/serialize.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.101)
- **Top Global Matches:** file_cluster_0: 7.101, file_cluster_15: 8.889, file_cluster_11: 9.41
- **Magnitude:** 722.8 | **LOC:** 1152 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 28.724; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Debt Markers (formerly Tech Debt) (96.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WriteCompactSize` **(Compute Cores)** (Impact: 13.6)
  * `ReadCompactSize` **(Compute Cores)** (Impact: 11.3)
  * `Unserialize_impl` **(Many-Argument Workhorses)** (Impact: 10.9)
  * `GetSizeOfCompactSize` **(Compute Cores)** (Impact: 10.2)
    * *Intent:* // // Compact size // size < 253 -- 1 byte // size <= USHRT_MAX -- 3 bytes (253 + 2 bytes) // size <...
  * `main` **(State Mutators)** (Impact: 9.8)
    * *Intent:* // n=1024000 8 seconds // n=2048000 16 seconds // n=4096000 32 seconds // stringstream: // n=1000 1 ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 588`, `args: 157`, `func_start: 171`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 143`, `dead_code: 5`, `duplicate_logic: 20`
* *Architecture:* `io: 3`, `api: 22`, `import: 4`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 106`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.237664
  * `Imports (Out-Degree: 0):` is_fundamental.hpp, iostream, map, vector
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/uint256.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.032)
- **Top Global Matches:** file_cluster_15: 7.032, file_cluster_11: 8.727, file_cluster_16: 9.087
- **Magnitude:** 712.56 | **LOC:** 751 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 17.782; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%), Complexity Load (formerly Cognitive Load) (72.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SetHex` **(Compute Cores)** (Impact: 17.2)
  * `Testuint256AdHoc` **(I/O & Config Routines)** (Impact: 13.0)
  * `operator<<=` **(Compute Cores)** (Impact: 9.3)
  * `operator>>=` **(Compute Cores)** (Impact: 9.3)
  * `operator<` **(Compute Cores)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 329
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 276`, `args: 15`, `func_start: 140`, `class_start: 3`
* *Risk/State:* `state_mutation: 141`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `doc: 2`, `immutability_locks: 255`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.782
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.210029
  * `Imports (Out-Degree: 0):` limits.h, string
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/net.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.177)
- **Top Global Matches:** file_cluster_4: 6.177, file_cluster_6: 10.405, file_cluster_12: 11.157
- **Magnitude:** 627.78 | **LOC:** 1068 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 26.671; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.8%), Complexity Load (formerly Cognitive Load) (50.3%)
- **Documentation Coverage:** 97.0588% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ThreadSocketHandler2` **(Compute Cores)** (Impact: 57.6)
  * `ThreadOpenConnections2` **(Compute Cores)** (Impact: 38.6)
  * `StartNode` **(Compute Cores)** (Impact: 28.4)
  * `GetMyExternalIP2` **(Many-Argument Workhorses)** (Impact: 24.5)
  * `ConnectSocket` **(Compute Cores)** (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 70 instances
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 86`, `args: 55`, `func_start: 34`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 93`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `io: 15`, `import: 2`
* *Defense:* `safety: 4`, `doc: 5`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.671
  * `Choke Point (Betweenness):` 0.025706 | `Ripple Effect (Closeness):` 0.163265
  * `Imports (Out-Degree: 7):` headers.h, winsock2.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/main.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.237)
- **Top Global Matches:** file_cluster_15: 6.237, file_cluster_11: 6.548, file_cluster_16: 8.152
- **Magnitude:** 601.96 | **LOC:** 1318 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 27.12; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.9%), Complexity Load (formerly Cognitive Load) (52.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IsNewerThan` **(Compute Cores)** (Impact: 12.7)
  * `ReadFromDisk` **(Compute Cores)** (Impact: 11.4)
  * `ReadFromDisk` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `CheckTransaction` **(Compute Cores)** (Impact: 10.2)
  * `operator==` **(Compute Cores)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 159`, `args: 73`, `func_start: 109`, `class_start: 24`
* *Risk/State:* `state_mutation: 148`, `duplicate_logic: 9`
* *Architecture:* `api: 25`
* *Defense:* `doc: 1`, `immutability_locks: 111`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.12
  * `Choke Point (Betweenness):` 0.031065 | `Ripple Effect (Closeness):` 0.222222
  * `Imports (Out-Degree: 6):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/bignum.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.096)
- **Top Global Matches:** file_cluster_15: 6.096, file_cluster_11: 7.479, file_cluster_16: 8.411
- **Magnitude:** 399.58 | **LOC:** 499 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 35.674; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%), Guard Balance (formerly Safety Score) (67.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setint64` **(Compute Cores)** (Impact: 15.8)
  * `SetHex` **(Compute Cores)** (Impact: 12.8)
  * `setuint64` **(Compute Cores)** (Impact: 9.8)
  * `setuint256` **(Compute Cores)** (Impact: 9.8)
  * `SetCompact` **(Compute Cores)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 82`, `args: 54`, `func_start: 67`, `class_start: 3`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 35.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.244088
  * `Imports (Out-Degree: 0):` bn.h, stdexcept, vector
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/uibase.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 8.005)
- **Top Global Matches:** file_cluster_2: 8.005, file_cluster_15: 8.148, file_cluster_17: 8.522
- **Magnitude:** 390.42 | **LOC:** 1807 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 16.278; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.7%), Debt Markers (formerly Tech Debt) (50.0%)
- **Documentation Coverage:** 96.875% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CMainFrameBase::CMainFrameBase` **(Many-Argument Workhorses)** (Impact: 6.1)
    * *Intent:* // Distributed under the MIT/X11 software license, see the accompanying // file license.txt or http:...
  * `CSendDialogBase::CSendDialogBase` **(Many-Argument Workhorses)** (Impact: 6.1)
  * `CEditProductDialogBase::CEditProductDialogBase` **(Many-Argument Workhorses)** (Impact: 6.1)
  * `CViewProductDialogBase::CViewProductDialogBase` **(Many-Argument Workhorses)** (Impact: 6.1)
  * `CPokerDialogBase::CPokerDialogBase` **(Many-Argument Workhorses)** (Impact: 6.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 400`, `func_start: 32`
* *Risk/State:* `state_mutation: 256`, `unreferenced_by_name: 32`
* *Architecture:* `import: 1`
* *Defense:* `doc: 3`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.278
  * `Choke Point (Betweenness):` 0.001008 | `Ripple Effect (Closeness):` 0.145665
  * `Imports (Out-Degree: 1):` uibase.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/script.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.187)
- **Top Global Matches:** file_cluster_15: 6.187, file_cluster_11: 7.93, file_cluster_16: 8.505
- **Magnitude:** 376.72 | **LOC:** 598 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 22.058; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.7%), Complexity Load (formerly Cognitive Load) (47.8%)
- **Documentation Coverage:** 96.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetOpName` **(Compute Cores)** (Impact: 160.8)
  * `GetOp` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `operator<<` **(Compute Cores)** (Impact: 8.1)
  * `FindAndDelete` **(Compute Cores)** (Impact: 7.9)
  * `push_int64` **(Compute Cores)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 164`, `args: 31`, `func_start: 47`, `class_start: 2`
* *Risk/State:* `state_mutation: 22`, `dead_code: 2`
* *Architecture:* `api: 6`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.058
  * `Choke Point (Betweenness):` 0.000588 | `Ripple Effect (Closeness):` 0.216216
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/net.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.556)
- **Top Global Matches:** file_cluster_12: 6.556, file_cluster_5: 8.349, file_cluster_7: 9.437
- **Magnitude:** 361.16 | **LOC:** 857 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 25.294; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.1%), Connectivity (formerly Api Exposure) (51.6%)
- **Documentation Coverage:** 97.3684% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `operator<` **(Compute Cores)** (Impact: 12.8)
  * `AdvertStartPublish` **(Many-Argument Workhorses)** (Impact: 11.9)
    * *Intent:* // // Templates for the publish and subscription system. // The object being published as T& obj nee...
  * `IsValid` **(I/O & Config Routines)** (Impact: 11.4)
  * `AdvertStopPublish` **(Generic / Templated Code)** (Impact: 9.5)
  * `CInv` **(Compute Cores)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 143`, `args: 58`, `func_start: 57`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 77`, `dead_code: 3`
* *Architecture:* `api: 26`
* *Defense:* `safety: 10`, `doc: 1`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.294
  * `Choke Point (Betweenness):` 0.016633 | `Ripple Effect (Closeness):` 0.228571
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/db.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.486)
- **Top Global Matches:** file_cluster_4: 5.486, file_cluster_15: 8.288, file_cluster_16: 9.923
- **Magnitude:** 357.84 | **LOC:** 609 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 47.647; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Debt Markers (formerly Tech Debt) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.6%)
- **Documentation Coverage:** 96.875% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CWalletDB::LoadWallet` **(Compute Cores)** (Impact: 31.1)
    * *Intent:* // // CWalletDB //
  * `CRITICAL_BLOCK` **(Compute Cores)** (Impact: 30.5)
    * *Intent:* //// todo: shouldn't we catch exceptions and try to recover and continue?
  * `CDB::CDB` **(Many-Argument Workhorses)** (Impact: 29.7)
  * `CTxDB::ReadOwnerTxes` **(Many-Argument Workhorses)** (Impact: 26.2)
  * `CTxDB::LoadBlockIndex` **(I/O & Config Routines)** (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 28 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 46`, `args: 13`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 44`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 20`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* `safety: 9`, `doc: 6`, `immutability_locks: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 47.647
  * `Choke Point (Betweenness):` 0.035232 | `Ripple Effect (Closeness):` 0.181818
  * `Imports (Out-Degree: 8):` headers.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/uibase.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.966)
- **Top Global Matches:** file_cluster_11: 5.966, file_cluster_17: 6.852, file_cluster_2: 8.066
- **Magnitude:** 266.9 | **LOC:** 721 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **28**; blast radius 31.618; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (58.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OnClose` **(Interface Declarations)** (Impact: 1.5)
    * *Intent:* // Virtual event handlers, overide them in your derived class
  * `OnIdle` **(Interface Declarations)** (Impact: 1.5)
  * `OnMouseEvents` **(Interface Declarations)** (Impact: 1.5)
  * `OnPaint` **(Interface Declarations)** (Impact: 1.5)
  * `OnMenuFileExit` **(Interface Declarations)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 250`, `func_start: 117`, `class_start: 16`
* *Risk/State:* `duplicate_logic: 52`
* *Architecture:* `api: 81`, `import: 28`
* *Defense:* `doc: 51`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.618
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.230114
  * `Imports (Out-Degree: 0):` bitmap.h, button.h, checkbox.h, choice.h, colour.h, combobox.h, dialog.h, font.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/util.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.696)
- **Top Global Matches:** file_cluster_4: 5.696, file_cluster_15: 8.12, file_cluster_16: 9.385
- **Magnitude:** 265.06 | **LOC:** 380 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **1**; blast radius 85.507; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ParseMoney` **(Compute Cores)** (Impact: 43.6)
  * `FormatMoney` **(Compute Cores)** (Impact: 16.2)
  * `strprintf` **(Compute Cores)** (Impact: 15.4)
  * `AddTimeData` **(Compute Cores)** (Impact: 13.7)
  * `my_snprintf` **(Many-Argument Workhorses)** (Impact: 9.7)
    * *Intent:* // Safer snprintf // - prints up to limit-1 characters // - output string is always null terminated ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 28`, `args: 20`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `state_mutation: 36`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 85.507
  * `Choke Point (Betweenness):` 0.102201 | `Ripple Effect (Closeness):` 0.363636
  * `Imports (Out-Degree: 2):` headers.h
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/util.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.781)
- **Top Global Matches:** file_cluster_15: 7.781, file_cluster_11: 8.418, file_cluster_0: 8.584
- **Magnitude:** 177.7 | **LOC:** 400 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); blast radius 80.705; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.4%), Guard Balance (formerly Safety Score) (60.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OutputDebugStringF` **(Many-Argument Workhorses)** (Impact: 18.7)
  * `HexStr` **(Generic / Templated Code)** (Impact: 8.5)
  * `HexNumStr` **(Generic / Templated Code)** (Impact: 6.5)
  * `Hash` **(Many-Argument Workhorses)** (Impact: 3.4)
  * `roundint` **(Parameter Forwarders)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 71`, `args: 29`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 34`
* *Architecture:* `io: 1`, `api: 20`
* *Defense:* `safety: 4`, `immutability_locks: 41`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 80.705
  * `Choke Point (Betweenness):` 0.050554 | `Ripple Effect (Closeness):` 0.380952
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/irc.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.241)
- **Top Global Matches:** file_cluster_4: 6.241, file_cluster_6: 8.269, file_cluster_15: 12.528
- **Magnitude:** 174.64 | **LOC:** 289 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 16.968; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.6%), Complexity Load (formerly Cognitive Load) (39.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ThreadIRCSeed` **(Compute Cores)** (Impact: 52.1)
  * `RecvLine` **(Compute Cores)** (Impact: 22.5)
  * `RecvUntil` **(Compute Cores)** (Impact: 18.7)
  * `RecvLineIRC` **(Compute Cores)** (Impact: 9.8)
  * `Send` **(Compute Cores)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 32`, `args: 12`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.968
  * `Choke Point (Betweenness):` 0.000336 | `Ripple Effect (Closeness):` 0.125
  * `Imports (Out-Degree: 4):` headers.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/db.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.598)
- **Top Global Matches:** file_cluster_15: 6.598, file_cluster_11: 7.8, file_cluster_0: 8.21
- **Magnitude:** 170.26 | **LOC:** 421 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **1**; blast radius 36.905; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (54.2%), Guard Balance (formerly Safety Score) (54.0%), Complexity Load (formerly Cognitive Load) (11.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ReadAtCursor` **(Many-Argument Workhorses)** (Impact: 26.5)
  * `Write` **(Many-Argument Workhorses)** (Impact: 7.3)
  * `Read` **(Type Conversions)** (Impact: 6.6)
  * `Erase` **(Generic / Templated Code)** (Impact: 5.2)
  * `TxnBegin` **(Interface Declarations)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 82`, `args: 48`, `func_start: 33`, `class_start: 15`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 11`
* *Architecture:* `api: 34`, `import: 1`
* *Defense:* `immutability_locks: 46`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.905
  * `Choke Point (Betweenness):` 0.022295 | `Ripple Effect (Closeness):` 0.258065
  * `Imports (Out-Degree: 1):` db_cxx.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/market.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.083)
- **Top Global Matches:** file_cluster_15: 6.083, file_cluster_11: 7.745, file_cluster_16: 8.024
- **Magnitude:** 122.42 | **LOC:** 265 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 19.105; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (87.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AddAtomsAndPropagate` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `CUser::AddAtom` **(Compute Cores)** (Impact: 15.5)
  * `CReview::AcceptReview` **(I/O & Config Routines)** (Impact: 7.8)
  * `AdvertInsert` **(Compute Cores)** (Impact: 5.6)
  * `CProduct::CheckProduct` **(I/O & Config Routines)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 19`, `args: 7`, `func_start: 9`
* *Risk/State:* `state_mutation: 20`, `dead_code: 6`, `unreferenced_by_name: 6`
* *Architecture:* `import: 1`
* *Defense:* `doc: 8`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.105
  * `Choke Point (Betweenness):` 0.013542 | `Ripple Effect (Closeness):` 0.163265
  * `Imports (Out-Degree: 6):` headers.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/base58.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.836)
- **Top Global Matches:** file_cluster_15: 4.836, file_cluster_16: 7.409, file_cluster_11: 7.894
- **Magnitude:** 118.42 | **LOC:** 202 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 28.998; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%), Guard Balance (formerly Safety Score) (65.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DecodeBase58` **(Compute Cores)** (Impact: 23.0)
  * `EncodeBase58` **(Compute Cores)** (Impact: 10.5)
  * `DecodeBase58Check` **(Compute Cores)** (Impact: 7.8)
  * `AddressToHash160` **(Compute Cores)** (Impact: 7.6)
  * `DecodeBase58` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 33`, `args: 6`, `func_start: 13`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.998
  * `Choke Point (Betweenness):` 0.002184 | `Ripple Effect (Closeness):` 0.235294
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/sha.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.693)
- **Top Global Matches:** file_cluster_15: 5.693, file_cluster_17: 7.002, file_cluster_2: 7.695
- **Magnitude:** 81.24 | **LOC:** 555 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 15.455; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.9%), Complexity Load (formerly Cognitive Load) (69.5%), Guard Balance (formerly Safety Score) (55.1%), Debt Markers (formerly Tech Debt) (37.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SHA512::Transform` **(Many-Argument Workhorses)** (Impact: 7.2)
    * *Intent:* #endif // #if CRYPTOPP_BOOL_SSE2_ASM_AVAILABLE
  * `SHA256::Transform` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* // for SHA256 #define S0(x) (rotrFixed(x,2)^rotrFixed(x,13)^rotrFixed(x,22)) #define S1(x) (rotrFixe...
  * `SHA512_SSE2_Transform` **(Many-Argument Workhorses)** (Impact: 3.7)
    * *Intent:* #if CRYPTOPP_BOOL_SSE2_ASM_AVAILABLE && CRYPTOPP_BOOL_X86 // put assembly version in separate functi...
  * `SHA1::Transform` **(Many-Argument Workhorses)** (Impact: 3.6)
    * *Intent:* #define f1(x,y,z) (z^(x&(y^z))) #define f2(x,y,z) (x^y^z) #define f3(x,y,z) ((x&y)|(z&(x|y))) #defin...
  * `SHA384::InitState` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* */ #undef S0 #undef S1 #undef s0 #undef s1 #undef R // *********************************************...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 11`, `args: 11`, `func_start: 9`
* *Risk/State:* `state_mutation: 41`, `unreferenced_by_name: 8`
* *Architecture:* `import: 3`
* *Defense:* `safety: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.153072
  * `Imports (Out-Degree: 1):` assert.h, memory.h, sha.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/key.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.824)
- **Top Global Matches:** file_cluster_15: 5.824, file_cluster_11: 7.107, file_cluster_16: 8.216
- **Magnitude:** 64.32 | **LOC:** 157 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 23.039; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.7%), Connectivity (formerly Api Exposure) (40.9%), Mutation Surface (formerly State Flux) (33.1%), Complexity Load (formerly Cognitive Load) (14.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sign` **(Parameter Forwarders)** (Impact: 4.3)
  * `Verify` **(Parameter Forwarders)** (Impact: 4.3)
  * `Sign` **(Compute Cores)** (Impact: 4.0)
  * `Verify` **(Compute Cores)** (Impact: 3.8)
  * `GetPrivKey` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 20`, `args: 8`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 7`
* *Defense:* `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.225781
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/ui.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.259)
- **Top Global Matches:** file_cluster_12: 6.259, file_cluster_11: 7.284, file_cluster_15: 8.224
- **Magnitude:** 52.2 | **LOC:** 419 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 20.33; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (86.8%), Guard Balance (formerly Safety Score) (52.3%), Connectivity (formerly Api Exposure) (30.9%), Complexity Load (formerly Cognitive Load) (2.4%)
- **Documentation Coverage:** 93.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CGetTextFromUserDialog` **(Many-Argument Workhorses)** (Impact: 6.2)
    * *Intent:* /** Constructor */
  * `OnKeyDown` **(Compute Cores)** (Impact: 6.0)
  * `OnKeyDown` **(Interface Declarations)** (Impact: 1.5)
  * `OnKeyDown` **(Interface Declarations)** (Impact: 1.5)
    * *Intent:* // Event handlers
  * `OnKeyDown` **(Interface Declarations)** (Impact: 1.5)
    * *Intent:* // Event handlers
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 149`, `args: 16`, `func_start: 13`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 2`, `duplicate_logic: 5`
* *Architecture:* `api: 17`
* *Defense:* `doc: 14`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.33
  * `Choke Point (Betweenness):` 0.024933 | `Ripple Effect (Closeness):` 0.205128
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/market.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.18)
- **Top Global Matches:** file_cluster_11: 5.18, file_cluster_2: 7.019, file_cluster_17: 7.175
- **Magnitude:** 38.48 | **LOC:** 183 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 20.488; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (78.5%), Guard Balance (formerly Safety Score) (56.1%), Connectivity (formerly Api Exposure) (39.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SetNull` **(Interface Declarations)** (Impact: 1.4)
  * `CReview` **(I/O & Config Routines)** (Impact: 1.4)
  * `CProduct` **(I/O & Config Routines)** (Impact: 1.3)
  * `GetAtomCount` **(Interface Declarations)** (Impact: 1.2)
  * `CUser` **(I/O & Config Routines)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 17`, `args: 5`, `func_start: 12`, `class_start: 6`
* *Risk/State:* `state_mutation: 13`, `duplicate_logic: 7`
* *Architecture:* `api: 5`
* *Defense:* `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.488
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.216216
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/sha.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.647)
- **Top Global Matches:** file_cluster_11: 6.647, file_cluster_17: 7.109, file_cluster_15: 7.266
- **Magnitude:** 32.0 | **LOC:** 178 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **1**; blast radius 105.837; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.7%), Connectivity (formerly Api Exposure) (42.1%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ByteReverse` **(Parameter Forwarders)** (Impact: 2.4)
  * `ByteReverse` **(Parameter Forwarders)** (Impact: 2.3)
    * *Intent:* #ifdef WORD64_AVAILABLE
  * `rotlFixed` **(Generic / Templated Code)** (Impact: 2.0)
    * *Intent:* #endif
  * `rotrFixed` **(Generic / Templated Code)** (Impact: 2.0)
  * `ByteReverse` **(Parameter Forwarders)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 59`, `args: 10`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 2`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 105.837
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.316406
  * `Imports (Out-Degree: 0):` stdlib.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.873)
- **Top Global Matches:** file_cluster_7: 5.873, file_cluster_12: 7.534, file_cluster_5: 9.359
- **Magnitude:** 19.84 | **LOC:** 84 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.5%), Debt Markers (formerly Tech Debt) (36.0%), Dead Code Surface (formerly Dead Code) (17.7%), Connectivity (formerly Api Exposure) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `obj/ui_res.o` **(Interface Declarations)** (Impact: 1.4)
  * `all` **(State Mutators)** (Impact: 1.1)
  * `headers.h.gch` **(I/O & Config Routines)** (Impact: 1.1)
  * `obj/util.o` **(I/O & Config Routines)** (Impact: 1.1)
  * `obj/script.o` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 13.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/ui.cpp` (CPP) | Magnitude: 1903.14 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1904, branch: 403, state_mutation: 334, pointers: 330

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/uibase.cpp` (CPP) | Magnitude: 390.42 | Delta: **0.143** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1184, pointers: 872, args: 400, core_var_decl: 259

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/util.cpp` -> **Severity: 10.22** (Bridge: 0.1022 * Flux: 99.9997%)
- `src/main.cpp` -> **Severity: 5.469** (Bridge: 0.0547 * Flux: 99.9988%)
- `src/ui.cpp` -> **Severity: 5.215** (Bridge: 0.0522 * Flux: 99.9928%)
- `src/util.h` -> **Severity: 4.977** (Bridge: 0.0506 * Flux: 98.4507%)
- `src/db.cpp` -> **Severity: 3.515** (Bridge: 0.0352 * Flux: 99.7545%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/util.cpp` -> **Severity: 24.565** (Embedded: 0.3636 * Error Risk: 67.5536%)
- `src/util.h` -> **Severity: 22.866** (Embedded: 0.381 * Error Risk: 60.0237%)
- `src/bignum.h` -> **Severity: 16.397** (Embedded: 0.2441 * Error Risk: 67.1773%)
- `src/sha.h` -> **Severity: 15.718** (Embedded: 0.3164 * Error Risk: 49.6774%)
- `src/uint256.h` -> **Severity: 15.647** (Embedded: 0.21 * Error Risk: 74.4997%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/sha.h` -> **Severity: 10583.7** (Blast Radius: 105.837 * Doc Risk: 100.0%)
- `src/util.cpp` -> **Severity: 8550.7** (Blast Radius: 85.507 * Doc Risk: 100.0%)
- `src/util.h` -> **Severity: 8070.5** (Blast Radius: 80.705 * Doc Risk: 100.0%)
- `src/db.cpp` -> **Severity: 4615.803** (Blast Radius: 47.647 * Doc Risk: 96.875%)
- `src/db.h` -> **Severity: 3690.5** (Blast Radius: 36.905 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`memory_alloc`:** 299 literal sites + 1 sites through wrappers = 300

- `AddOrphanTx` (function, memory_alloc, primitive): 1 call sites in 1 files -- `src/main.cpp`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3736 call pairs -- scoped 13.6%, unique 8.6%, ambiguous 25.6%, external 52.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 3736 | 13.6% | 8.6% | 25.6% | 52.2% |

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
