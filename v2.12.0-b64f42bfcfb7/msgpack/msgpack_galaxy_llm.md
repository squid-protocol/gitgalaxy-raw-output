# ARCHITECTURAL_BRIEF: msgpack
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 35 analyzed artifact(s), 4026 LOC.
- **Load-bearing artifact:** `msgpack-1.1.2/msgpack/__init__.py` -- 17 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `msgpack-1.1.2/msgpack/fallback.py` -- pulls in 8 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `msgpack-1.1.2/msgpack/fallback.py` at magnitude 967.66 (structural weight, not risk).
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
| Total Artifacts | 39 |
| Analyzed Artifacts (Scanned) | 35 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4 |
| Total LOC | 4026 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 89.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2502 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.1937 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 14.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3654 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 25 | 2595 | 71.4% |
| CPP | 7 | 1431 | 20.0% |
| PLAINTEXT | 2 | 0 | 5.7% |
| MARKDOWN | 1 | 0 | 2.9% |

## 4.1 SOURCE ENCODINGS
All 35 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 23%, Parameter Forwarders Files 17%, Interface Declarations Files 14%, Large Core Modules (3) 14%, Data / Markup / Trivial 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 32 | 91.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 8.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4*

**Composition by Extension & Reason:**
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 25514 LOC)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 83.2 | 27.6 | 27.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 73.2 | 46.5 | 54.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.2 | 9.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 20.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 73.9 | 15.3 | 9.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 37.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 20.2 | 1.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 78.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 57 | 17 | 5 | `msgpack-1.1.2/msgpack/fallback.py` |
| cleanup | 1 | 1 | 0 | `msgpack-1.1.2/test/test_seq.py` |
| guards | 384 | 29 | 35 | `msgpack-1.1.2/msgpack/fallback.py` |
| danger | 135 | 19 | 7 | `msgpack-1.1.2/msgpack/fallback.py` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 234 | 26 | 15 | `msgpack-1.1.2/msgpack/fallback.py` |
| io | 6 | 3 | 0 | `msgpack-1.1.2/test/test_unpack.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 15 | 3 | 0 | `msgpack-1.1.2/test/test_timestamp.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 129 | 16 | 13 | `msgpack-1.1.2/test/test_limits.py` |
| docs | 44 | 7 | 5 | `msgpack-1.1.2/msgpack/ext.py` |
| debt | 12 | 6 | 1 | `msgpack-1.1.2/msgpack/fallback.py` |
| mutation | 1348 | 32 | 84 | `msgpack-1.1.2/msgpack/fallback.py` |
| dead_code | 176 | 21 | 13 | `msgpack-1.1.2/msgpack/unpack.h` |
| credential | 0 | 0 | 0 | - |
| threat | 51 | 6 | 5 | `msgpack-1.1.2/test/test_format.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `msgpack-1.1.2/test/test_unpack.py` (Hits: 4)
- `msgpack-1.1.2/msgpack/fallback.py` (Hits: 1)
- `msgpack-1.1.2/setup.py` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`msgpack-1.1.2/msgpack/__init__.py`) — 17 inbound connections
2. **fallback.py** (`msgpack-1.1.2/msgpack/fallback.py`) — 17 inbound connections
3. **ext.py** (`msgpack-1.1.2/msgpack/ext.py`) — 10 inbound connections
4. **_unpacker.pyx** (`msgpack-1.1.2/msgpack/_unpacker.pyx`) — 6 inbound connections
5. **_packer.pyx** (`msgpack-1.1.2/msgpack/_packer.pyx`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **fallback.py** (`msgpack-1.1.2/msgpack/fallback.py`) — 8 outbound dependencies
2. **pack.h** (`msgpack-1.1.2/msgpack/pack.h`) — 7 outbound dependencies
3. **__init__.py** (`msgpack-1.1.2/msgpack/__init__.py`) — 5 outbound dependencies
4. **test_pack.py** (`msgpack-1.1.2/test/test_pack.py`) — 5 outbound dependencies
5. **sysdep.h** (`msgpack-1.1.2/msgpack/sysdep.h`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `unpack_execute` **(Many-Argument Workhorses)** (@ `msgpack-1.1.2/msgpack/unpack_template.h`) -> Impact: **216.3** | LOC: 309
- `_pack` **(Many-Argument Workhorses)** (@ `msgpack-1.1.2/msgpack/fallback.py`) -> Impact: **128.6** | LOC: 123
- `_pack_inner` **(Many-Argument Workhorses)** (@ `msgpack-1.1.2/msgpack/_packer.pyx`) -> Impact: **123.8** | LOC: 105
  * *Intent:* # returns -2 when default should(o) be called
- `__init__` **(Stateful Encapsulated Methods)** (@ `msgpack-1.1.2/msgpack/fallback.py`) -> Impact: **109.2** | LOC: 91
- `_unpack` **(Many-Argument Workhorses)** (@ `msgpack-1.1.2/msgpack/fallback.py`) -> Impact: **66.0** | LOC: 73
- `__init__` **(Many-Argument Workhorses)** (@ `msgpack-1.1.2/msgpack/_unpacker.pyx`) -> Impact: **64.0** | LOC: 59
- `init_ctx` **(Many-Argument Workhorses)** (@ `msgpack-1.1.2/msgpack/_unpacker.pyx`) -> Impact: **62.8** | LOC: 55
- `unpack_container_header` **(Many-Argument Workhorses)** (@ `msgpack-1.1.2/msgpack/unpack_container_header.h`) -> Impact: **58.4** | LOC: 50
- `unpack_callback_ext` **(Many-Argument Workhorses)** (@ `msgpack-1.1.2/msgpack/unpack.h`) -> Impact: **55.9** | LOC: 90
  * *Intent:* #include "datetime.h"
- `unpackb` **(Many-Argument Workhorses)** (@ `msgpack-1.1.2/msgpack/_unpacker.pyx`) -> Impact: **51.4** | LOC: 68

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `msgpack-1.1.2/msgpack` | 14 | 2968.56 | 40.7% | 20.83% |
| `msgpack-1.1.2/test` | 17 | 863.14 | 16.19% | 0.0% |
| `msgpack-1.1.2` | 4 | 43.38 | 9.79% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `msgpack-1.1.2/msgpack/_packer.pyx` -> **99.2031%** Exposure
- `msgpack-1.1.2/msgpack/unpack.h` -> **97.6135%** Exposure
- `msgpack-1.1.2/msgpack/_unpacker.pyx` -> **67.3884%** Exposure
- `msgpack-1.1.2/msgpack/unpack_template.h` -> **16.8487%** Exposure
- `msgpack-1.1.2/msgpack/fallback.py` -> **10.6355%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `msgpack-1.1.2/msgpack/_packer.pyx` -> **100.0%** Exposure
- `msgpack-1.1.2/msgpack/_unpacker.pyx` -> **100.0%** Exposure
- `msgpack-1.1.2/msgpack/ext.py` -> **100.0%** Exposure
- `msgpack-1.1.2/msgpack/fallback.py` -> **100.0%** Exposure
- `msgpack-1.1.2/setup.py` -> **99.9999%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `msgpack-1.1.2/msgpack/unpack.h` -> **20** Orphaned Functions | **0** Duplicates
- `msgpack-1.1.2/test/test_pack.py` -> **15** Orphaned Functions | **0** Duplicates
- `msgpack-1.1.2/test/test_case.py` -> **13** Orphaned Functions | **0** Duplicates
- `msgpack-1.1.2/test/test_memoryview.py` -> **13** Orphaned Functions | **0** Duplicates
- `msgpack-1.1.2/msgpack/_packer.pyx` -> **12** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `76` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `msgpack-1.1.2/msgpack/fallback.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.881)
- **Top Global Matches:** file_cluster_4: 5.881, file_cluster_6: 9.325, file_cluster_16: 11.947
- **Magnitude:** 967.66 | **LOC:** 930 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **8**; blast radius 95.21; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.2%)
- **Documentation Coverage:** 84.7458% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_pack` **(Many-Argument Workhorses)** (Impact: 128.6)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 109.2)
  * `_unpack` **(Many-Argument Workhorses)** (Impact: 66.0)
  * `_read_header` **(Compute Cores)** (Impact: 50.0)
  * `pack_ext_type` **(Defensive Guards)** (Impact: 27.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 120 instances
* *State Mutation (weighted view):* 392
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 150`, `args: 39`, `func_start: 39`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 152`, `planned_debt: 5`
* *Architecture:* `io: 1`, `api: 23`, `import: 8`
* *Defense:* `safety: 24`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 95.21
  * `Choke Point (Betweenness):` 0.009433 | `Ripple Effect (Closeness):` 0.501548
  * `Imports (Out-Degree: 2):` .exceptions, .ext, __pypy__, __pypy__.builders, datetime, io, struct, sys
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `msgpack-1.1.2/msgpack/_unpacker.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.307)
- **Top Global Matches:** file_cluster_15: 5.307, file_cluster_16: 7.754, file_cluster_2: 8.335
- **Magnitude:** 458.22 | **LOC:** 548 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **2**; blast radius 29.899; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.2%), Debt Markers (formerly Tech Debt) (67.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 64.0)
  * `init_ctx` **(Many-Argument Workhorses)** (Impact: 62.8)
  * `unpackb` **(Many-Argument Workhorses)** (Impact: 51.4)
  * `_unpack` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `append_buffer` **(Many-Argument Workhorses)** (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 182
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 43`, `args: 20`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 76`, `dead_code: 5`, `unreferenced_by_name: 11`
* *Architecture:* `api: 9`, `import: 2`
* *Defense:* `safety: 4`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 29.899
  * `Choke Point (Betweenness):` 0.0026 | `Ripple Effect (Closeness):` 0.176471
  * `Imports (Out-Degree: 2):` .exceptions, .ext
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `msgpack-1.1.2/msgpack/_packer.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.307)
- **Top Global Matches:** file_cluster_4: 6.307, file_cluster_15: 8.045, file_cluster_12: 9.428
- **Magnitude:** 349.32 | **LOC:** 359 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **1**; blast radius 27.223; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.9%)
- **Documentation Coverage:** 69.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_pack_inner` **(Many-Argument Workhorses)** (Impact: 123.8)
    * *Intent:* # returns -2 when default should(o) be called
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 16.8)
  * `_pack` **(Compute Cores)** (Impact: 10.6)
  * `pack_map_pairs` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* """ Pack *pairs* as msgpack map type. *pairs* should be a sequence of pairs. (`len(pairs)` and `for ...
  * `pack` **(Defensive Guards)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 37`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 48`, `planned_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 7`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 27.223
  * `Choke Point (Betweenness):` 0.000817 | `Ripple Effect (Closeness):` 0.147059
  * `Imports (Out-Degree: 1):` .ext
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `msgpack-1.1.2/msgpack/unpack_template.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.734)
- **Top Global Matches:** file_cluster_6: 6.734, file_cluster_4: 10.579, file_cluster_8: 15.532
- **Magnitude:** 329.94 | **LOC:** 424 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 33.783; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unpack_execute` **(Many-Argument Workhorses)** (Impact: 216.3)
  * `unpack_construct` **(Parameter Forwarders)** (Impact: 2.4)
    * *Intent:* #undef NEXT_CS #undef SWITCH_RANGE_BEGIN #undef SWITCH_RANGE #undef SWITCH_RANGE_DEFAULT #undef SWIT...
  * `unpack_skip` **(Parameter Forwarders)** (Impact: 2.4)
  * `unpack_init` **(Parameter Forwarders)** (Impact: 2.0)
  * `unpack_data` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 48`, `args: 34`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 44`, `dead_code: 4`, `fragile_debt: 2`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 33.783
  * `Choke Point (Betweenness):` 0.000891 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 2):` unpack_container_header.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `msgpack-1.1.2/msgpack/unpack.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.535)
- **Top Global Matches:** file_cluster_15: 6.535, file_cluster_4: 6.892, file_cluster_16: 8.488
- **Magnitude:** 313.94 | **LOC:** 392 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 49.859; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unpack_callback_ext` **(Many-Argument Workhorses)** (Impact: 55.9)
    * *Intent:* #include "datetime.h"
  * `unpack_callback_map_item` **(Many-Argument Workhorses)** (Impact: 23.3)
  * `unpack_callback_raw` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `unpack_timestamp` **(Compute Cores)** (Impact: 13.2)
    * *Intent:* /* * Unpack ext buffer to a timestamp. Pulled from msgpack-c timestamp.h. */
  * `unpack_callback_map` **(Compute Cores)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 89`, `args: 15`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `state_mutation: 37`, `unreferenced_by_name: 20`
* *Architecture:* `import: 3`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 49.859
  * `Choke Point (Betweenness):` 0.004456 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 2):` datetime.h, unpack_define.h, unpack_template.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `msgpack-1.1.2/msgpack/pack_template.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.415)
- **Top Global Matches:** file_cluster_15: 5.415, file_cluster_16: 7.439, file_cluster_17: 7.616
- **Magnitude:** 246.34 | **LOC:** 597 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 28.096; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `msgpack_pack_ext` **(Many-Argument Workhorses)** (Impact: 32.6)
    * *Intent:* /* * Ext */
  * `msgpack_pack_raw` **(Compute Cores)** (Impact: 14.8)
    * *Intent:* /* * Raw */
  * `msgpack_pack_timestamp` **(Many-Argument Workhorses)** (Impact: 11.5)
    * *Intent:* /* * Pack Timestamp extension type. Follows msgpack-c pack_template.h. */
  * `msgpack_pack_bin` **(Compute Cores)** (Impact: 11.3)
    * *Intent:* /* * bin */
  * `msgpack_pack_short` **(Compute Cores)** (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 21`, `args: 11`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 43`
* *Architecture:* `api: 14`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.096
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.029412
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `msgpack-1.1.2/test/test_pack.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.335)
- **Top Global Matches:** file_cluster_11: 6.335, file_cluster_15: 7.085, file_cluster_2: 8.034
- **Magnitude:** 125.98 | **LOC:** 182 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (41.7%), Connectivity (formerly Api Exposure) (11.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testMapSize` **(Defensive Guards)** (Impact: 7.7)
  * `test_manualreset` **(Type Conversions)** (Impact: 6.4)
  * `testArraySize` **(Defensive Guards)** (Impact: 6.3)
  * `testPack` **(I/O & Config Routines)** (Impact: 3.5)
  * `testPackUnicode` **(Defensive Guards)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 43`, `args: 17`, `func_start: 17`
* *Risk/State:* `state_mutation: 32`, `unreferenced_by_name: 15`
* *Architecture:* `api: 17`, `import: 5`
* *Defense:* `safety: 16`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` collections, io, msgpack, pytest, struct
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/msgpack/ext.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.236)
- **Top Global Matches:** file_cluster_15: 6.236, file_cluster_13: 8.331, file_cluster_11: 8.488
- **Magnitude:** 116.18 | **LOC:** 171 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **3**; blast radius 130.49; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.2%), Guard Balance (formerly Safety Score) (65.7%)
- **Documentation Coverage:** 20.6897% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_bytes` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* """Unpack bytes into a `Timestamp` object. Used for pure-Python msgpack unpacking. :param b: Payload...
  * `__init__` **(Defensive Guards)** (Impact: 9.1)
    * *Intent:* """Initialize a Timestamp object. :param int seconds: Number of seconds since the UNIX epoch (00:00:...
  * `__new__` **(Defensive Guards)** (Impact: 8.4)
  * `to_bytes` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* """Pack this Timestamp object into bytes. Used for pure-Python msgpack packing. :returns data: Paylo...
  * `__eq__` **(Compute Cores)** (Impact: 5.4)
    * *Intent:* """Check for equality with another Timestamp object"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 37`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 15`, `import: 3`
* *Defense:* `safety: 4`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 130.49
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.405331
  * `Imports (Out-Degree: 0):` collections, datetime, struct
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `msgpack-1.1.2/test/test_timestamp.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.829)
- **Top Global Matches:** file_cluster_12: 7.829, file_cluster_10: 8.256, file_cluster_15: 8.625
- **Magnitude:** 107.66 | **LOC:** 172 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.0%), Complexity Load (formerly Cognitive Load) (41.0%), Connectivity (formerly Api Exposure) (9.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_timestamp` **(Defensive Guards)** (Impact: 6.8)
    * *Intent:* # timestamp32 ts = Timestamp(2**32 - 1) assert ts.to_bytes() == b"\xff\xff\xff\xff" packed = msgpack...
  * `test_pack_datetime_without_tzinfo` **(Callbacks & Closures)** (Impact: 2.7)
  * `test_unpack_timestamp` **(Annotated & Test Methods)** (Impact: 2.2)
    * *Intent:* # timestamp 32 assert msgpack.unpackb(b"\xd6\xff\x00\x00\x00\x00") == Timestamp(0) # timestamp 64 as...
  * `test_pack_datetime` **(Defensive Guards)** (Impact: 2.1)
  * `test_timestamp_datetime` **(Defensive Guards)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 63`, `args: 11`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 49`, `unreferenced_by_name: 10`
* *Architecture:* `api: 10`, `import: 4`
* *Defense:* `safety: 40`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` datetime, msgpack, msgpack.ext, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/msgpack/unpack_container_header.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.253)
- **Top Global Matches:** file_cluster_1: 5.253, file_cluster_3: 48.179, file_cluster_8: 70.024
- **Magnitude:** 75.36 | **LOC:** 52 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 26.951; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.1%), Guard Balance (formerly Safety Score) (59.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unpack_container_header` **(Many-Argument Workhorses)** (Impact: 58.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 4`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 1`
* *Defense:* `safety: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.951
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `msgpack-1.1.2/test/test_unpack.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.107)
- **Top Global Matches:** file_cluster_12: 7.107, file_cluster_15: 8.575, file_cluster_16: 9.032
- **Magnitude:** 63.06 | **LOC:** 90 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.5%), Complexity Load (formerly Cognitive Load) (27.9%), Connectivity (formerly Api Exposure) (8.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_hook` **(Encapsulated Accessors)** (Impact: 6.2)
  * `test_unpacker_ext_hook` **(C Struct Operations)** (Impact: 3.9)
  * `test_unpacker_tell_read_bytes` **(Defensive Guards)** (Impact: 2.5)
  * `test_unpacker_tell` **(Defensive Guards)** (Impact: 2.4)
  * `test_unpacker_hook_refcnt` **(Defensive Guards)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 41`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `unreferenced_by_name: 6`
* *Architecture:* `io: 4`, `api: 7`, `import: 4`
* *Defense:* `safety: 19`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` io, msgpack, pytest, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/test/test_sequnpack.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.407)
- **Top Global Matches:** file_cluster_12: 7.407, file_cluster_11: 7.712, file_cluster_15: 8.218
- **Magnitude:** 62.96 | **LOC:** 149 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (34.8%), Complexity Load (formerly Cognitive Load) (27.3%), Connectivity (formerly Api Exposure) (8.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_unpack_tell` **(Type Conversions)** (Impact: 8.1)
  * `test_foobar` **(Defensive Guards)** (Impact: 3.0)
  * `test_readbytes` **(Defensive Guards)** (Impact: 2.2)
  * `test_partialdata` **(Interface Declarations)** (Impact: 2.0)
  * `test_foobar_skip` **(Defensive Guards)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 61`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `unreferenced_by_name: 8`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `safety: 35`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` io, msgpack, msgpack.exceptions, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/test/test_stricttype.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.991)
- **Top Global Matches:** file_cluster_15: 7.991, file_cluster_11: 8.625, file_cluster_13: 8.854
- **Magnitude:** 60.08 | **LOC:** 60 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (29.9%), Connectivity (formerly Api Exposure) (10.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_tuple_ext` **(Defensive Guards)** (Impact: 4.1)
  * `test_tuple` **(Type Conversions)** (Impact: 3.9)
  * `convert` **(Type Conversions)** (Impact: 3.7)
  * `default` **(Defensive Guards)** (Impact: 3.1)
  * `default` **(Type Conversions)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 25`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 3`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 6`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` collections, msgpack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/test/test_extension.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.011)
- **Top Global Matches:** file_cluster_11: 7.011, file_cluster_15: 7.444, file_cluster_13: 8.411
- **Magnitude:** 56.86 | **LOC:** 79 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.5%), Complexity Load (formerly Cognitive Load) (27.4%), Connectivity (formerly Api Exposure) (10.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `default` **(Defensive Guards)** (Impact: 4.5)
  * `test_overriding_hooks` **(Defensive Guards)** (Impact: 3.7)
  * `default` **(Defensive Guards)** (Impact: 3.3)
  * `test_extension_type` **(Defensive Guards)** (Impact: 3.2)
  * `ext_hook` **(Defensive Guards)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 32`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 4`
* *Architecture:* `api: 8`, `import: 3`
* *Defense:* `safety: 18`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` array, msgpack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/test/test_case.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.559)
- **Top Global Matches:** file_cluster_11: 5.559, file_cluster_15: 6.419, file_cluster_2: 8.053
- **Magnitude:** 56.52 | **LOC:** 137 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (41.4%), Connectivity (formerly Api Exposure) (11.7%), Complexity Load (formerly Cognitive Load) (4.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_match` **(I/O & Config Routines)** (Impact: 6.8)
  * `match` **(Defensive Guards)** (Impact: 3.6)
  * `test_1` **(I/O & Config Routines)** (Impact: 2.7)
  * `test_9` **(I/O & Config Routines)** (Impact: 2.6)
  * `check` **(Defensive Guards)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 24`, `args: 17`, `func_start: 17`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 13`
* *Architecture:* `api: 17`, `import: 1`
* *Defense:* `safety: 5`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` msgpack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/test/test_limits.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.247)
- **Top Global Matches:** file_cluster_11: 5.247, file_cluster_15: 7.484, file_cluster_2: 7.64
- **Magnitude:** 54.74 | **LOC:** 166 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.7%), Dead Code Surface (formerly Dead Code) (20.2%), Connectivity (formerly Api Exposure) (9.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_max_str_len` **(Interface Declarations)** (Impact: 1.6)
  * `test_max_bin_len` **(Interface Declarations)** (Impact: 1.6)
  * `test_max_array_len` **(Interface Declarations)** (Impact: 1.6)
  * `test_max_map_len` **(Interface Declarations)** (Impact: 1.6)
  * `test_max_ext_len` **(Interface Declarations)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 33`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 28`, `dead_code: 3`, `unreferenced_by_name: 10`
* *Architecture:* `api: 10`, `import: 2`
* *Defense:* `safety: 7`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` msgpack, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/test/test_obj.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.309)
- **Top Global Matches:** file_cluster_12: 7.309, file_cluster_10: 8.856, file_cluster_11: 9.571
- **Magnitude:** 48.28 | **LOC:** 83 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (20.9%), Connectivity (formerly Api Exposure) (8.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_decode_complex` **(Encapsulated Accessors)** (Impact: 3.0)
  * `_encode_complex` **(Encapsulated Accessors)** (Impact: 3.0)
  * `_arr_to_str` **(Encapsulated Accessors)** (Impact: 2.9)
  * `test_decode_pairs_hook` **(Callbacks & Closures)** (Impact: 2.5)
  * `bad_complex_decoder` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 31`, `args: 16`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`, `unreferenced_by_name: 8`
* *Architecture:* `api: 10`, `import: 2`
* *Defense:* `safety: 5`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` msgpack, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/test/test_memoryview.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.721)
- **Top Global Matches:** file_cluster_12: 6.721, file_cluster_11: 7.511, file_cluster_15: 8.821
- **Magnitude:** 45.04 | **LOC:** 100 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.3%), Connectivity (formerly Api Exposure) (11.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_runtest` **(Stateful Encapsulated Methods)** (Impact: 3.5)
    * *Intent:* # create a new array original_array = array(format) original_array.fromlist([255] * (nbytes // origi...
  * `make_array` **(Parameter Forwarders)** (Impact: 1.9)
  * `test_multidim_memoryview` **(Type Conversions)** (Impact: 1.3)
    * *Intent:* # See https://github.com/msgpack/msgpack-python/issues/526 view = memoryview(b"\00" * 6) data = view...
  * `test_fixstr_from_byte` **(Interface Declarations)** (Impact: 1.1)
  * `test_fixstr_from_float` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 26`, `args: 15`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`, `unreferenced_by_name: 13`
* *Architecture:* `api: 14`, `import: 2`
* *Defense:* `safety: 6`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` array, msgpack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 4.305)
- **Top Global Matches:** file_cluster_7: 4.305, file_cluster_14: 7.311, file_cluster_12: 8.977
- **Magnitude:** 36.52 | **LOC:** 33 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 12.594; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (39.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7`
* *Architecture:* `io: 1`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, setuptools, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/test/test_newspec.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.496)
- **Top Global Matches:** file_cluster_11: 6.496, file_cluster_15: 7.508, file_cluster_2: 7.839
- **Magnitude:** 36.2 | **LOC:** 91 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (22.0%), Connectivity (formerly Api Exposure) (8.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_str8` **(Defensive Guards)** (Impact: 1.9)
  * `test_bin16` **(Defensive Guards)** (Impact: 1.9)
  * `test_ext` **(Interface Declarations)** (Impact: 1.9)
  * `check` **(Defensive Guards)** (Impact: 1.9)
  * `test_bin8` **(Defensive Guards)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 43`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 18`, `unreferenced_by_name: 5`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 35`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` msgpack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/test/test_buffer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.884)
- **Top Global Matches:** file_cluster_11: 6.884, file_cluster_15: 7.814, file_cluster_13: 8.513
- **Magnitude:** 34.72 | **LOC:** 50 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.1%), Complexity Load (formerly Cognitive Load) (28.0%), Connectivity (formerly Api Exposure) (8.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_packer_getbuffer` **(Defensive Guards)** (Impact: 2.9)
  * `test_unpack_memoryview` **(Defensive Guards)** (Impact: 2.4)
  * `test_unpack_bytearray` **(Defensive Guards)** (Impact: 2.3)
  * `test_unpack_buffer` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 22`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 4`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 10`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` array, msgpack, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/test/test_seq.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.412)
- **Top Global Matches:** file_cluster_15: 6.412, file_cluster_11: 7.905, file_cluster_2: 8.205
- **Magnitude:** 33.34 | **LOC:** 42 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (27.0%), Connectivity (formerly Api Exposure) (5.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_exceeding_unpacker_read_size` **(Defensive Guards)** (Impact: 4.4)
  * `gen_binary_data` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 9`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 4`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io, msgpack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/test/test_format.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 4.05)
- **Top Global Matches:** file_cluster_11: 4.05, file_cluster_2: 6.507, file_cluster_15: 6.58
- **Magnitude:** 27.8 | **LOC:** 89 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (11.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check` **(Defensive Guards)** (Impact: 2.3)
  * `testMap` **(I/O & Config Routines)** (Impact: 1.9)
  * `testRaw` **(Interface Declarations)** (Impact: 1.6)
  * `testUnsignedInt` **(Interface Declarations)** (Impact: 1.4)
  * `testSignedInt` **(Interface Declarations)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 15`, `args: 11`, `func_start: 11`
* *Risk/State:* `unreferenced_by_name: 10`
* *Architecture:* `api: 11`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` msgpack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msgpack-1.1.2/msgpack/pack.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 6.077)
- **Top Global Matches:** file_cluster_17: 6.077, file_cluster_15: 6.75, file_cluster_2: 7.01
- **Magnitude:** 23.94 | **LOC:** 70 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 36.475; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (61.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (45.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `msgpack_pack_write` **(Many-Argument Workhorses)** (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `func_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.475
  * `Choke Point (Betweenness):` 0.000891 | `Ripple Effect (Closeness):` 0.029412
  * `Imports (Out-Degree: 2):` limits.h, pack_template.h, stdbool.h, stddef.h, stdlib.h, string.h, sysdep.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `msgpack-1.1.2/test/test_read_size.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.894)
- **Top Global Matches:** file_cluster_15: 7.894, file_cluster_2: 8.019, file_cluster_11: 8.093
- **Magnitude:** 22.94 | **LOC:** 73 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 12.594; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (16.9%), Connectivity (formerly Api Exposure) (9.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_read_array_header` **(Defensive Guards)** (Impact: 1.6)
  * `test_read_map_header` **(Defensive Guards)** (Impact: 1.6)
  * `test_incorrect_type_array` **(Defensive Guards)** (Impact: 1.4)
  * `test_incorrect_type_map` **(Defensive Guards)** (Impact: 1.4)
  * `test_correct_type_nested_array` **(Defensive Guards)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 27`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 6`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 31`, `doc: 1`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` msgpack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `msgpack-1.1.2/test/test_read_size.py` (PYTHON) | Magnitude: 22.94 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 49, safety: 31, structural_boundaries: 27, state_mutation: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `msgpack-1.1.2/msgpack/__init__.py` -> **Severity: 1.21** (Bridge: 0.0121 * Flux: 99.9254%)
- `msgpack-1.1.2/msgpack/fallback.py` -> **Severity: 0.943** (Bridge: 0.0094 * Flux: 100.0%)
- `msgpack-1.1.2/msgpack/unpack.h` -> **Severity: 0.446** (Bridge: 0.0045 * Flux: 99.9958%)
- `msgpack-1.1.2/msgpack/_unpacker.pyx` -> **Severity: 0.26** (Bridge: 0.0026 * Flux: 100.0%)
- `msgpack-1.1.2/msgpack/pack.h` -> **Severity: 0.089** (Bridge: 0.0009 * Flux: 99.9932%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `msgpack-1.1.2/msgpack/fallback.py` -> **Severity: 36.72** (Embedded: 0.5015 * Error Risk: 73.2135%)
- `msgpack-1.1.2/msgpack/__init__.py` -> **Severity: 28.687** (Embedded: 0.5 * Error Risk: 57.3744%)
- `msgpack-1.1.2/msgpack/ext.py` -> **Severity: 26.635** (Embedded: 0.4053 * Error Risk: 65.7124%)
- `msgpack-1.1.2/msgpack/exceptions.py` -> **Severity: 18.932** (Embedded: 0.3268 * Error Risk: 57.9324%)
- `msgpack-1.1.2/msgpack/_unpacker.pyx` -> **Severity: 12.74** (Embedded: 0.1765 * Error Risk: 72.1922%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `msgpack-1.1.2/msgpack/exceptions.py` -> **Severity: 9182.8** (Blast Radius: 91.828 * Doc Risk: 100.0%)
- `msgpack-1.1.2/msgpack/fallback.py` -> **Severity: 8068.648** (Blast Radius: 95.21 * Doc Risk: 84.7458%)
- `msgpack-1.1.2/msgpack/unpack.h` -> **Severity: 4985.9** (Blast Radius: 49.859 * Doc Risk: 100.0%)
- `msgpack-1.1.2/msgpack/pack.h` -> **Severity: 3647.5** (Blast Radius: 36.475 * Doc Risk: 100.0%)
- `msgpack-1.1.2/msgpack/unpack_template.h` -> **Severity: 3378.3** (Blast Radius: 33.783 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 967 call pairs -- scoped 43.4%, unique 2.0%, ambiguous 1.0%, external 53.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 811 | 50.6% | 0.0% | 1.2% | 48.2% |
| cpp | 156 | 6.4% | 12.2% | 0.0% | 81.4% |

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
