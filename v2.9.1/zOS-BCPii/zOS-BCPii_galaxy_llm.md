# ARCHITECTURAL_BRIEF: zOS-BCPii
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/IBM/zOS-BCPii.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 22 analyzed artifact(s), 10838 LOC.
- **Load-bearing artifact:** `Example-LPARActivate-C/h/hwijprs.h` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Example-LPARActivate-C/cpp/hwirstc1.cpp` -- pulls in 12 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Example-Audit-REXX/RXAUDIT1.rexx` at magnitude 1224.72 (structural weight, not risk).
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
| Total Artifacts | 30 |
| Analyzed Artifacts (Scanned) | 22 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 10838 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 73.3% |
| Dominant Lang | REXX |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1667 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 9 | 0 | 40.9% |
| REXX | 7 | 9590 | 31.8% |
| CPP | 4 | 1202 | 18.2% |
| JCL | 2 | 46 | 9.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 41%, Large Core Modules 36%, Declarative / Non-Code 9%, Large Core Modules (3) 9%, Parameter Forwarders Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 13 | 59.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 40.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8*

**Composition by Extension & Reason:**
- `.png`: 5x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 50.6 | 29.8 | 40.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.1 | 73.8 | 94.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 58.5 | 9.0 | 8.6 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 56.1 | 80.0 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 69.7 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.1 | 4.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 54.1 | 44.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 369 | 5 | 35 | `Example-LPARActivate-C/cpp/hwirstc1.cpp` |
| cleanup | 105 | 8 | 13 | `Example-LPARActivate-C/cpp/hwirstc1.cpp` |
| guards | 39 | 10 | 4 | `Example-LPARActivate-C/h/hwirstc1.h` |
| danger | 183 | 9 | 26 | `Example-CustomUsrGrp-REXX/RXUSRGP1.rexx` |
| concurrency | 1 | 1 | 0 | `Example-LPARActivate-C/cpp/hwirstc1.cpp` |
| connectivity | 0 | 0 | 0 | - |
| io | 28 | 8 | 4 | `Example-LPARActivate-C/jcl/hwirstcx.jcl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 148 | 7 | 25 | `Example-Audit-REXX/RXAUDIT1.rexx` |
| time | 13 | 7 | 1 | `Example-LPARLoad-SYSREXX/HWIXMRS3.rexx` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 5 | 3 | 1 | `Example-LPARActivate-C/jcl/hwirstc1.jcl` |
| tests | 0 | 0 | 0 | - |
| docs | 288 | 9 | 40 | `Example-CustomUsrGrp-REXX/RXUSRGP1.rexx` |
| debt | 914 | 9 | 163 | `Example-QueryInfo-REXX/RXQUERY1.rexx` |
| mutation | 4257 | 12 | 585 | `Example-Audit-REXX/RXAUDIT1.rexx` |
| dead_code | 131 | 9 | 24 | `Example-Crypto-REXX/RXCRYPT1.rexx` |
| credential | 0 | 0 | 0 | - |
| threat | 1 | 1 | 0 | `Example-LPARActivate-C/cpp/hwijprs.cpp` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Example-LPARActivate-C/jcl/hwirstcx.jcl` (Hits: 6)
- `Example-Audit-REXX/RXAUDIT1.rexx` (Hits: 4)
- `Example-Crypto-REXX/RXCRYPT1.rexx` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **hwijprs.h** (`Example-LPARActivate-C/h/hwijprs.h`) — 2 inbound connections
2. **hwirstc1.h** (`Example-LPARActivate-C/h/hwirstc1.h`) — 1 inbound connections
3. **README.md** (`Example-Audit-REXX/README.md`) — 0 inbound connections
4. **README.md** (`Example-Crypto-REXX/README.md`) — 0 inbound connections
5. **README.md** (`Example-CustomUsrGrp-REXX/README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **hwirstc1.cpp** (`Example-LPARActivate-C/cpp/hwirstc1.cpp`) — 12 outbound dependencies
2. **hwijprs.cpp** (`Example-LPARActivate-C/cpp/hwijprs.cpp`) — 7 outbound dependencies
3. **hwirstc1.h** (`Example-LPARActivate-C/h/hwirstc1.h`) — 4 outbound dependencies
4. **README.md** (`Example-Audit-REXX/README.md`) — 1 outbound dependencies
5. **README.md** (`Example-Crypto-REXX/README.md`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `asyncPost` **(Many-Argument Workhorses)** (@ `Example-LPARActivate-C/cpp/hwirstc1.cpp`) -> Impact: **46.0** | LOC: 116
  * *Intent:* /* * Method: asyncPost * * Issue an asynchronous POST operation that on success * returns a job-uri which should be used to POLL for * the result of t...
- `JSON_findValue` **(I/O & Config Routines)** (@ `Example-Audit-REXX/RXAUDIT1.rexx`) -> Impact: **36.4** | LOC: 147
  * *Intent:* return serializedDataOut /* end function */ /**********************************************************/ /* Function: JSON_findValue */ /* */ /* Retur...
- `JSON_findValue` **(I/O & Config Routines)** (@ `Example-Crypto-REXX/RXCRYPT1.rexx`) -> Impact: **36.4** | LOC: 147
  * *Intent:* return serializedDataOut /* end function */ /**********************************************************/ /* Function: JSON_findValue */ /* */ /* Retur...
- `JSON_findValue` **(I/O & Config Routines)** (@ `Example-Energy-REXX/RXENRGY1.rexx`) -> Impact: **35.4** | LOC: 147
  * *Intent:* return serializedDataOut /* end function */ /**********************************************************/ /* Function: JSON_findValue */ /* */ /* Retur...
- `do_get_value` **(Many-Argument Workhorses)** (@ `Example-LPARActivate-C/cpp/hwijprs.cpp`) -> Impact: **33.2** | LOC: 109
  * *Intent:* /* * Method: do_get_value * * Retrieves the specified value by calling the appropriate service using the * value of the specified HWTJ_JTYPE_TYPE. * *...
- `GetArgs` **(I/O & Config Routines)** (@ `Example-CustomUsrGrp-REXX/RXUSRGP1.rexx`) -> Impact: **32.9** | LOC: 97
  * *Intent:* * Input: ARG_STR - The string representation of the arguments passed * to the REXX script by the user * * Output: An Integer indicating if function wa...
- `getLPARInfo` **(Compute Cores)** (@ `Example-LPARActivate-C/cpp/hwirstc1.cpp`) -> Impact: **31.3** | LOC: 117
  * *Intent:* /* * Method: getLPARInfo * * Issue List Logical Partitions of CPC operation to retrieve the URI * and target name assocaited with the LPAR. All subseq...
- `JSON_findValue` **(I/O & Config Routines)** (@ `Example-QueryInfo-REXX/RXQUERY1.rexx`) -> Impact: **27.6** | LOC: 132
  * *Intent:* return serializedDataOut /* end function */ /**********************************************************/ /* Function: JSON_findValue */ /* */ /* Retur...
- `FindJSONValue` **(I/O & Config Routines)** (@ `Example-CustomUsrGrp-REXX/RXUSRGP1.rexx`) -> Impact: **26.9** | LOC: 159
  * *Intent:* * API's { HWTJSRCH, HWTJGVAL, HWTJGBOV }, as appropriate. * * Input: objectToSearch - The object to search for the value of * interest * searchName - ...
- `getCPCInfo` **(Compute Cores)** (@ `Example-LPARActivate-C/cpp/hwirstc1.cpp`) -> Impact: **25.6** | LOC: 117
  * *Intent:* /* * Method: getCPCInfo * * Issue List CPC Objects operation to retrieve the URI * and target name assocaited with the CPC. All subsequent * request w...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Example-Audit-REXX` | 2 | 1227.22 | 25.19% | 4.61% |
| `Example-Crypto-REXX` | 2 | 1180.8 | 25.28% | 5.12% |
| `Example-CustomUsrGrp-REXX` | 2 | 1157.98 | 16.88% | 4.32% |
| `Example-Energy-REXX` | 2 | 1070.26 | 24.58% | 4.75% |
| `Example-QueryInfo-REXX` | 2 | 871.72 | 23.92% | 6.17% |
| `Example-LPARLoad-REXX` | 2 | 835.0 | 24.2% | 0.0% |
| `Example-LPARLoad-SYSREXX` | 2 | 716.66 | 24.49% | 0.0% |
| `Example-LPARActivate-C/cpp` | 2 | 678.74 | 29.06% | 33.77% |
| `Example-LPARActivate-C/h` | 2 | 31.4 | 0.0% | 0.0% |
| `Example-LPARActivate-C/jcl` | 2 | 7.62 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Example-LPARActivate-C/cpp/hwijprs.cpp` -> **58.5237%** Exposure
- `Example-QueryInfo-REXX/RXQUERY1.rexx` -> **12.3327%** Exposure
- `Example-Crypto-REXX/RXCRYPT1.rexx` -> **10.238%** Exposure
- `Example-Energy-REXX/RXENRGY1.rexx` -> **9.5066%** Exposure
- `Example-Audit-REXX/RXAUDIT1.rexx` -> **9.2201%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Example-Audit-REXX/RXAUDIT1.rexx` -> **100.0%** Exposure
- `Example-Crypto-REXX/RXCRYPT1.rexx` -> **100.0%** Exposure
- `Example-CustomUsrGrp-REXX/RXUSRGP1.rexx` -> **100.0%** Exposure
- `Example-Energy-REXX/RXENRGY1.rexx` -> **100.0%** Exposure
- `Example-LPARLoad-REXX/RXLOAD1.rexx` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Example-LPARActivate-C/cpp/hwijprs.cpp` -> **9** Orphaned Functions | **0** Duplicates
- `Example-QueryInfo-REXX/RXQUERY1.rexx` -> **6** Orphaned Functions | **0** Duplicates
- `Example-Crypto-REXX/RXCRYPT1.rexx` -> **5** Orphaned Functions | **0** Duplicates
- `Example-Audit-REXX/RXAUDIT1.rexx` -> **3** Orphaned Functions | **0** Duplicates
- `Example-Energy-REXX/RXENRGY1.rexx` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `28` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Example-Audit-REXX/RXAUDIT1.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1224.72 | **LOC:** 2482 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (50.4%)
- **Documentation Coverage:** 41.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `JSON_findValue` **(I/O & Config Routines)** (Impact: 36.4)
    * *Intent:* return serializedDataOut /* end function */ /*******************************************************...
  * `JSON_findValue2` **(I/O & Config Routines)** (Impact: 21.4)
    * *Intent:* /**********************************************************/ /* Function: JSON_findValue2 */ /* */ /...
  * `QueryLPAR` **(I/O & Config Routines)** (Impact: 18.9)
    * *Intent:* /*******************************************************/ /* Function: QueryLPAR */ /* */ /* Retriev...
  * `GetArgs` **(I/O & Config Routines)** (Impact: 16.6)
    * *Intent:* return /* end procedure */ /***********************************************/ /* Function: GetArgs */...
  * `getStorageCentralAllocationEntries` **(I/O & Config Routines)** (Impact: 16.5)
    * *Intent:* /*******************************************************/ /* Function: getStorageCentralAllocationEn...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 225 instances
* *High Risk Execution (weighted view):* 13
* *State Mutation (weighted view):* 823
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 372`, `args: 6`, `func_start: 45`
* *Risk/State:* `high_risk_execution: 15`, `state_mutation: 373`, `dead_code: 21`, `unreferenced_by_name: 3`
* *Architecture:* `io: 4`
* *Defense:* `safety: 4`, `doc: 40`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-Crypto-REXX/RXCRYPT1.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1178.56 | **LOC:** 2457 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (50.6%)
- **Documentation Coverage:** 41.3043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `JSON_findValue` **(I/O & Config Routines)** (Impact: 36.4)
    * *Intent:* return serializedDataOut /* end function */ /*******************************************************...
  * `JSON_findValue2` **(I/O & Config Routines)** (Impact: 21.4)
    * *Intent:* /**********************************************************/ /* Function: JSON_findValue2 */ /* */ /...
  * `GetArgs` **(I/O & Config Routines)** (Impact: 20.1)
    * *Intent:* /* or return fatal error code via usage() invocation. */ /* Required input parameters: */ /* -D <dat...
  * `GetLocalCPCInfo` **(I/O & Config Routines)** (Impact: 19.5)
    * *Intent:* /*******************************************************/ /* Function: GetLocalCPCInfo */ /* */ /* R...
  * `QueryCrypto` **(I/O & Config Routines)** (Impact: 17.6)
    * *Intent:* /*******************************************************/ /* Function: QueryCrypto */ /* */ /* Retri...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 229 instances
* *High Risk Execution (weighted view):* 12
* *State Mutation (weighted view):* 768
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 291`, `structural_boundaries: 384`, `args: 6`, `func_start: 46`
* *Risk/State:* `high_risk_execution: 14`, `state_mutation: 310`, `dead_code: 22`, `unreferenced_by_name: 5`
* *Architecture:* `io: 4`
* *Defense:* `safety: 4`, `doc: 41`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-CustomUsrGrp-REXX/RXUSRGP1.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1149.9 | **LOC:** 2839 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (33.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetArgs` **(I/O & Config Routines)** (Impact: 32.9)
    * *Intent:* * Input: ARG_STR - The string representation of the arguments passed * to the REXX script by the use...
  * `FindJSONValue` **(I/O & Config Routines)** (Impact: 26.9)
    * *Intent:* * API's { HWTJSRCH, HWTJGVAL, HWTJGBOV }, as appropriate. * * Input: objectToSearch - The object to ...
  * `GetRequest` **(I/O & Config Routines)** (Impact: 17.6)
    * *Intent:* * Optional Input: * uri - The URI to target with a GET request * targetName - The target name of the...
  * `GetLocalLPARInfo` **(I/O & Config Routines)** (Impact: 16.9)
    * *Intent:* * * Input: TARGET_CPC_URI - The CPC URI to target * TARGET_CPC_NAME - The name of the CPC to target ...
  * `GetLocalCPCInfo` **(I/O & Config Routines)** (Impact: 16.8)
    * *Intent:* * * Purpose: Retrieve the uri and target name associated with the local * CPC, prime CPCuri, and CPC...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 238 instances
* *High Risk Execution (weighted view):* 28
* *State Mutation (weighted view):* 791
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 273`, `args: 3`, `func_start: 41`
* *Risk/State:* `high_risk_execution: 30`, `state_mutation: 315`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`
* *Defense:* `safety: 2`, `doc: 83`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-Energy-REXX/RXENRGY1.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1067.8 | **LOC:** 2169 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.2%)
- **Documentation Coverage:** 40.2439% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `JSON_findValue` **(I/O & Config Routines)** (Impact: 35.4)
    * *Intent:* return serializedDataOut /* end function */ /*******************************************************...
  * `JSON_findValue2` **(I/O & Config Routines)** (Impact: 21.4)
    * *Intent:* /**********************************************************/ /* Function: JSON_findValue2 */ /* */ /...
  * `GetArgs` **(I/O & Config Routines)** (Impact: 16.6)
    * *Intent:* return /* end procedure */ /***********************************************/ /* Function: GetArgs */...
  * `GetLocalCPCInfo` **(I/O & Config Routines)** (Impact: 15.7)
    * *Intent:* /*******************************************************/ /* Function: GetLocalCPCInfo */ /* */ /* R...
  * `surfaceResponse` **(I/O & Config Routines)** (Impact: 15.1)
    * *Intent:* /********************************************************/ /* Procedure: surfaceResponse() */ /* par...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 192 instances
* *High Risk Execution (weighted view):* 11
* *State Mutation (weighted view):* 723
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 317`, `args: 6`, `func_start: 41`
* *Risk/State:* `high_risk_execution: 13`, `state_mutation: 339`, `dead_code: 20`, `unreferenced_by_name: 3`
* *Architecture:* `io: 4`
* *Defense:* `safety: 4`, `doc: 37`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-QueryInfo-REXX/RXQUERY1.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 866.46 | **LOC:** 1963 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.8%)
- **Documentation Coverage:** 44.5946% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `JSON_findValue` **(I/O & Config Routines)** (Impact: 27.6)
    * *Intent:* return serializedDataOut /* end function */ /*******************************************************...
  * `GetLocalCPCInfo` **(I/O & Config Routines)** (Impact: 17.1)
    * *Intent:* /*******************************************************/ /* Function: GetLocalCPCInfo */ /* */ /* R...
  * `GetLocalLPARInfo` **(I/O & Config Routines)** (Impact: 16.9)
    * *Intent:* /*******************************************************/ /* Function: GetLocalLPARInfo */ /* */ /* ...
  * `surfaceResponse` **(I/O & Config Routines)** (Impact: 15.2)
    * *Intent:* /********************************************************/ /* Procedure: surfaceResponse() */ /* par...
  * `GetArgs` **(I/O & Config Routines)** (Impact: 14.7)
    * *Intent:* return /* end procedure */ /***********************************************/ /* Function: GetArgs */...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 164 instances
* *High Risk Execution (weighted view):* 11
* *State Mutation (weighted view):* 572
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 270`, `args: 3`, `func_start: 37`
* *Risk/State:* `high_risk_execution: 13`, `state_mutation: 244`, `dead_code: 20`, `unreferenced_by_name: 6`
* *Architecture:* `io: 2`
* *Defense:* `safety: 2`, `doc: 33`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-LPARLoad-REXX/RXLOAD1.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 831.22 | **LOC:** 1836 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (48.4%)
- **Documentation Coverage:** 42.1875% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetJobStatus` **(I/O & Config Routines)** (Impact: 22.6)
    * *Intent:* /* <job-status-code>, and potentially about <job-reason-code> */ /* */ /* Returns: 0 if the value of...
  * `GetArgs` **(I/O & Config Routines)** (Impact: 22.2)
    * *Intent:* return result /* end function */ /***********************************************/ /* Function: GetA...
  * `GetLparUri` **(I/O & Config Routines)** (Impact: 19.6)
    * *Intent:* /*******************************************************************/ /* Function: GetLparUri */ /* ...
  * `JSON_findValue` **(I/O & Config Routines)** (Impact: 15.8)
    * *Intent:* return NO_ERROR /* end function */ /**********************************************************/ /* F...
  * `GetCpcUri` **(I/O & Config Routines)** (Impact: 14.6)
    * *Intent:* return NO_ERROR /* end function */ /****************************************************************...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 141 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 566
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 291`, `args: 3`, `func_start: 32`
* *Risk/State:* `high_risk_execution: 9`, `state_mutation: 284`, `dead_code: 10`
* *Architecture:* `io: 2`
* *Defense:* `safety: 1`, `doc: 28`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-LPARLoad-SYSREXX/HWIXMRS3.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 712.64 | **LOC:** 1629 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.0%)
- **Documentation Coverage:** 44.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetJobStatus` **(I/O & Config Routines)** (Impact: 22.5)
    * *Intent:* /* <job-status-code>, and potentially about <job-reason-code>. */ /* */ /* Returns: 0 if the value o...
  * `GetLparUri` **(I/O & Config Routines)** (Impact: 19.4)
    * *Intent:* return NO_ERROR /* end function */ /****************************************************************...
  * `JSON_findValue` **(I/O & Config Routines)** (Impact: 15.8)
    * *Intent:* return NO_ERROR /* end function */ /**********************************************************/ /* F...
  * `surfaceResponse` **(I/O & Config Routines)** (Impact: 14.9)
    * *Intent:* /********************************************************/ /* Procedure: surfaceResponse() */ /* par...
  * `GetCpcUri` **(I/O & Config Routines)** (Impact: 14.6)
    * *Intent:* return NO_ERROR /* end function */ /****************************************************************...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 115 instances
* *State Mutation (weighted view):* 486
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 281`, `func_start: 26`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 256`, `dead_code: 10`
* *Architecture:* None
* *Defense:* `doc: 23`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-LPARActivate-C/cpp/hwirstc1.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 510.56 | **LOC:** 1172 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 42.194; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (40.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `asyncPost` **(Many-Argument Workhorses)** (Impact: 46.0)
    * *Intent:* /* * Method: asyncPost * * Issue an asynchronous POST operation that on success * returns a job-uri ...
  * `getLPARInfo` **(Compute Cores)** (Impact: 31.3)
    * *Intent:* /* * Method: getLPARInfo * * Issue List Logical Partitions of CPC operation to retrieve the URI * an...
  * `getCPCInfo` **(Compute Cores)** (Impact: 25.6)
    * *Intent:* /* * Method: getCPCInfo * * Issue List CPC Objects operation to retrieve the URI * and target name a...
  * `isJobRunning` **(Many-Argument Workhorses)** (Impact: 23.9)
    * *Intent:* /* * Method: isJobRunning * * Retrieve the status of the job associated with the passed in * job uri...
  * `traceRequest` **(Many-Argument Workhorses)** (Impact: 23.6)
    * *Intent:* /* * Method: traceRequest * * Print out the various request parameters */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 51 instances
* *Memory Alloc (weighted view):* 12
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 34`, `args: 31`, `func_start: 20`
* *Risk/State:* `state_mutation: 99`, `unreferenced_by_name: 1`
* *Architecture:* `import: 12`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 2`, `cleanup: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` hwicic.h, hwijprs.h, hwirstc1.h, hwtjic.h, iconv.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-LPARActivate-C/cpp/hwijprs.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 168.18 | **LOC:** 730 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 42.194; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (75.6%), Guard Balance (formerly Safety Score) (68.6%), Debt Markers (formerly Tech Debt) (58.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_get_value` **(Many-Argument Workhorses)** (Impact: 33.2)
    * *Intent:* /* * Method: do_get_value * * Retrieves the specified value by calling the appropriate service using...
  * `find_value` **(Many-Argument Workhorses)** (Impact: 23.6)
    * *Intent:* * * Input: - A handle of type object or array. * - A string used as a search parameter. * - A JSON t...
  * `find_boolvalue` **(Many-Argument Workhorses)** (Impact: 20.7)
    * *Intent:* * - A JSON type as defined in the IBM-provided C interface definition * file. * * Output: * -1 if va...
  * `do_cleanup` **(I/O & Config Routines)** (Impact: 12.8)
    * *Intent:* * behavior of terminate if the parser is determined to be stuck * in an "in-use" state. IBM recommen...
  * `do_get_boolvalue` **(Compute Cores)** (Impact: 12.1)
    * *Intent:* /* * Method: do_get_boolvalue * * -1 if value not obtained, * 0 if bool is FALSE, * 1 if bool is TRU...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 20`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 10`, `unreferenced_by_name: 9`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` hwijprs.h, hwtjic.h, stdio.h, stdlib.h, string.h, strings.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-LPARActivate-C/h/hwirstc1.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 16.04 | **LOC:** 106 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 60.127; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 15`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `import: 4`
* *Defense:* `doc: 2`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 60.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.047619
  * `Imports (Out-Degree: 0):` hwicic.h, stdlib.h, time.h, time.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Example-LPARActivate-C/h/hwijprs.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 15.36 | **LOC:** 46 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 95.992; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 11`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 95.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.095238
  * `Imports (Out-Degree: 0):` hwtjic.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Example-CustomUsrGrp-REXX/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 8.08 | **LOC:** 404 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-LPARActivate-C/jcl/hwirstcx.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 5.76 | **LOC:** 68 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 42.194; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.5%), Mutation Surface (formerly State Flux) (31.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `STEP1` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* //* either express or implied. See the License for the specific //* language governing permissions a...
  * `STEP2` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* /* //*--------------------------------------------- //* COMPILE and BIND HWIRSTC1 //*---------------...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CBC.SCCNPRC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-QueryInfo-REXX/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 5.26 | **LOC:** 263 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-LPARLoad-SYSREXX/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 4.02 | **LOC:** 201 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-LPARLoad-REXX/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 3.78 | **LOC:** 189 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-Audit-REXX/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.5 | **LOC:** 125 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 42.194; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sampleAuditResult.png
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-Energy-REXX/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.46 | **LOC:** 123 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-LPARActivate-C/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.4 | **LOC:** 120 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-Crypto-REXX/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.24 | **LOC:** 112 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 42.194; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SampleCryptoResult.png
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example-LPARActivate-C/jcl/hwirstc1.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1.86 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 42.194; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HWIRSTC1` **(Parameter Forwarders)** (Impact: 1.7)
    * *Intent:* //* you may not use this file except in compliance with the License. //* You may obtain a copy of th...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hlq.HWIREST.PDSE.LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.8 | **LOC:** 90 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Example-LPARActivate-C/h/hwijprs.h` -> **Severity: 6.686** (Embedded: 0.0952 * Error Risk: 70.2063%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Example-LPARActivate-C/cpp/hwijprs.cpp` -> **Severity: 4219.4** (Blast Radius: 42.194 * Doc Risk: 100.0%)
- `Example-LPARActivate-C/cpp/hwirstc1.cpp` -> **Severity: 4219.4** (Blast Radius: 42.194 * Doc Risk: 100.0%)
- `Example-LPARActivate-C/jcl/hwirstc1.jcl` -> **Severity: 4219.4** (Blast Radius: 42.194 * Doc Risk: 100.0%)
- `Example-LPARActivate-C/jcl/hwirstcx.jcl` -> **Severity: 4219.4** (Blast Radius: 42.194 * Doc Risk: 100.0%)
- `Example-CustomUsrGrp-REXX/RXUSRGP1.rexx` -> **Severity: 2109.7** (Blast Radius: 42.194 * Doc Risk: 50.0%)

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
