# ARCHITECTURAL_BRIEF: zig-book
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pedropark99/zig-book.git` |
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
- **Scope:** 157 analyzed artifact(s), 3875 LOC.
- **Load-bearing artifact:** `ZigExamples/calling-c/user.h` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `ZigExamples/http_server/src/main.zig` -- pulls in 4 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `ZigExamples/calling-c/c.zig` at magnitude 1171.9 (structural weight, not risk).
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
| Total Artifacts | 301 |
| Analyzed Artifacts (Scanned) | 157 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 144 |
| Total LOC | 3875 |
| Volatility Index | 0.076 |
| % Scanned of codebase = | 52.2% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7654 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5431 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 119 | 3352 | 75.8% |
| JSON | 20 | 304 | 12.7% |
| HTML | 4 | 72 | 2.5% |
| PLAINTEXT | 3 | 0 | 1.9% |
| XML | 3 | 0 | 1.9% |
| MARKDOWN | 2 | 0 | 1.3% |
| PYTHON | 2 | 14 | 1.3% |
| CSS | 1 | 26 | 0.6% |
| YAML | 1 | 40 | 0.6% |
| NIX | 1 | 61 | 0.6% |
| C | 1 | 6 | 0.6% |

## 4.1 SOURCE ENCODINGS
All 157 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 42%, Data / Markup / Trivial 33%, State Mutators Files 12%, Declarative / Non-Code 4%, Large Core Modules 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 136 | 86.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 16 | 10.2% |
| Static: Literature & Documentation | 5 | 3.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 144*

**Composition by Extension & Reason:**
- `.png`: 49x Excluded (Explicitly Denied Extension: '.png')
- `.qmd`: 19x Excluded (Unsupported Extension: '.qmd')
- `.html`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.odp`: 11x Excluded (Explicitly Denied Extension: '.odp')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected)
- `.r`: 5x Excluded (Unsupported Extension: '.R'), 1x Unsupported Format (.r)
- `.css`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zig`: 2x Statistical Anomaly (Z-Score: -5.61 < -4.75), 1x Statistical Anomaly (Z-Score: -5.42 < -4.75), 1x Statistical Anomaly (Z-Score: -5.88 < -4.75)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 126390 LOC)
- `.bib`: 1x Excluded (Unsupported Extension: '.bib')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.webp`: 1x Excluded (Explicitly Denied Extension: '.webp')
- `.woff`: 1x Excluded (Explicitly Denied Extension: '.woff')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 65.5 | 3.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 74.6 | 21.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 74.5 | 26.1 | 37.8 | 37.8 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.6 | 3.5 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 84.0 | 2.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.2 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.2 | 0.1 | 0.2 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 36.9 | 63.1 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 75.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 452 | 29 | 2 | `ZigExamples/calling-c/c.zig` |
| cleanup | 41 | 29 | 1 | `ZigExamples/data-structures/generic_stack.zig` |
| guards | 337 | 86 | 6 | `ZigExamples/image_filter/src/image_filter.zig` |
| danger | 139 | 53 | 1 | `ZigExamples/calling-c/c.zig` |
| concurrency | 51 | 12 | 0 | `ZigExamples/threads/rw_lock.zig` |
| connectivity | 1094 | 113 | 2 | `ZigExamples/calling-c/c.zig` |
| io | 17 | 9 | 0 | `ZigExamples/http_server/src/config.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 3 | 1 | 0 | `ZigExamples/http_server/src/config.zig` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 3 | 3 | 0 | `Scripts/list_all_zig_example_files.py` |
| events | 1 | 1 | 0 | `ZigExamples/hello_world/src/main.zig` |
| tests | 18 | 8 | 0 | `ZigExamples/unittest/test_error.zig` |
| docs | 4 | 1 | 0 | `ZigExamples/hello_world/src/root.zig` |
| debt | 71 | 38 | 2 | `ZigExamples/calling-c/c.zig` |
| mutation | 1756 | 121 | 11 | `ZigExamples/calling-c/c.zig` |
| dead_code | 109 | 105 | 1 | `ZigExamples/image_filter/src/test.zig` |
| credential | 1 | 1 | 0 | `ZigExamples/calling-c/c.zig` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 61 | 12 | 0 | `ZigExamples/image_filter/src/test.zig` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ZigExamples/http_server/src/config.zig` (Hits: 3)
- `Assets/button.html` (Hits: 2)
- `Assets/leanpub-button.html` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **user.h** (`ZigExamples/calling-c/user.h`) — 2 inbound connections
2. **user_struct.zig** (`ZigExamples/allocators/user_struct.zig`) — 1 inbound connections
3. **c.zig** (`ZigExamples/calling-c/c.zig`) — 1 inbound connections
4. **request.zig** (`ZigExamples/http_server/src/request.zig`) — 1 inbound connections
5. **response.zig** (`ZigExamples/http_server/src/response.zig`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.zig** (`ZigExamples/http_server/src/main.zig`) — 4 outbound dependencies
2. **image_filter.zig** (`ZigExamples/image_filter/src/image_filter.zig`) — 4 outbound dependencies
3. **list_all_zig_example_files.py** (`Scripts/list_all_zig_example_files.py`) — 3 outbound dependencies
4. **test.zig** (`ZigExamples/image_filter/src/test.zig`) — 3 outbound dependencies
5. **fopen.zig** (`ZigExamples/calling-c/fopen.zig`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `decode` **(Defensive Guards)** (@ `ZigExamples/base64/base64_basic.zig`) -> Impact: **15.6** | LOC: 31
- `encode` **(Many-Argument Workhorses)** (@ `ZigExamples/base64/base64_basic.zig`) -> Impact: **14.0** | LOC: 40
- `main` **(Defensive Guards)** (@ `ZigExamples/vectors/src/main.zig`) -> Impact: **13.6** | LOC: 45
- `main` **(Defensive Guards)** (@ `ZigExamples/vectors/src/main2.zig`) -> Impact: **11.6** | LOC: 34
- `testOne` **(Defensive Guards)** (@ `ZigExamples/hello_world/src/main.zig`) -> Impact: **10.0** | LOC: 26
- `save_png` **(Defensive Guards)** (@ `ZigExamples/image_filter/src/test.zig`) -> Impact: **9.6** | LOC: 19
- `read_png` **(Defensive Guards)** (@ `ZigExamples/image_filter/src/image_filter.zig`) -> Impact: **8.3** | LOC: 27
- `_calc_decode_length` **(Defensive Guards)** (@ `ZigExamples/base64/base64_basic.zig`) -> Impact: **8.0** | LOC: 19
- `work` **(Defensive Guards)** (@ `ZigExamples/threads/cancel_thread.zig`) -> Impact: **7.8** | LOC: 14
- `_char_index` **(Compute Cores)** (@ `ZigExamples/base64/base64_basic.zig`) -> Impact: **7.7** | LOC: 15

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `ZigExamples/calling-c` | 10 | 1220.8 | 0.51% | 31.18% |
| `ZigExamples/data-structures` | 14 | 129.06 | 5.93% | 36.97% |
| `ZigExamples/base64` | 1 | 127.8 | 64.21% | 15.05% |
| `ZigExamples/threads` | 12 | 116.52 | 5.56% | 37.75% |
| `ZigExamples/zig-basics` | 22 | 110.26 | 1.96% | 34.32% |
| `ZigExamples/image_filter/src` | 2 | 93.7 | 14.17% | 43.5% |
| `Assets` | 7 | 85.06 | 0.73% | 0.0% |
| `ZigExamples/vectors/src` | 2 | 79.7 | 63.66% | 56.12% |
| `ZigExamples/http_server/src` | 5 | 56.0 | 3.43% | 15.1% |
| `ZigExamples/file-io` | 16 | 54.9 | 0.64% | 33.03% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ZigExamples/vectors/src/main.zig` -> **74.4868%** Exposure
- `ZigExamples/image_filter/src/test.zig` -> **72.8766%** Exposure
- `ZigExamples/allocators/alloc_free.zig` -> **37.7541%** Exposure
- `ZigExamples/allocators/arena_alloc.zig` -> **37.7541%** Exposure
- `ZigExamples/allocators/fixed_buffer_alloc.zig` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ZigExamples/base64/base64_basic.zig` -> **100.0%** Exposure
- `ZigExamples/vectors/src/main.zig` -> **100.0%** Exposure
- `ZigExamples/vectors/src/main2.zig` -> **99.9999%** Exposure
- `ZigExamples/data-structures/stack.zig` -> **99.2406%** Exposure
- `Scripts/list_all_zig_example_files.py` -> **99.1837%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ZigExamples/image_filter/src/test.zig` -> **3** Orphaned Functions | **0** Duplicates
- `ZigExamples/vectors/src/main.zig` -> **2** Orphaned Functions | **0** Duplicates
- `ZigExamples/allocators/alloc_free.zig` -> **1** Orphaned Functions | **0** Duplicates
- `ZigExamples/allocators/arena_alloc.zig` -> **1** Orphaned Functions | **0** Duplicates
- `ZigExamples/allocators/fixed_buffer_alloc.zig` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `136` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ZigExamples/calling-c/c.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.013)
- **Top Global Matches:** file_cluster_5: 9.013, file_cluster_12: 9.603, file_cluster_7: 9.619
- **Magnitude:** 1171.9 | **LOC:** 1171 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 11.138; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.6%), Debt Markers (formerly Tech Debt) (9.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renameat` **(State Mutators)** (Impact: 2.3)
  * `setvbuf` **(State Mutators)** (Impact: 2.3)
  * `snprintf` **(State Mutators)** (Impact: 2.3)
  * `vsnprintf` **(State Mutators)** (Impact: 2.3)
  * `__getdelim` **(State Mutators)** (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 30`, `args: 119`, `func_start: 115`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 49`, `planned_debt: 6`
* *Architecture:* `api: 947`, `import: 132`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00625
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ZigExamples/base64/base64_basic.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.05)
- **Top Global Matches:** file_cluster_12: 6.05, file_cluster_15: 7.363, file_cluster_11: 8.658
- **Magnitude:** 127.8 | **LOC:** 158 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.02; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.2%), Complexity Load (formerly Cognitive Load) (64.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decode` **(Defensive Guards)** (Impact: 15.6)
  * `encode` **(Many-Argument Workhorses)** (Impact: 14.0)
  * `_calc_decode_length` **(Defensive Guards)** (Impact: 8.0)
  * `_char_index` **(Compute Cores)** (Impact: 7.7)
  * `_calc_encode_length` **(Defensive Guards)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 30`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ZigExamples/image_filter/src/image_filter.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.753)
- **Top Global Matches:** file_cluster_7: 7.753, file_cluster_12: 8.093, file_cluster_5: 9.924
- **Magnitude:** 51.08 | **LOC:** 166 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 6.02; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.7%), Mutation Surface (formerly State Flux) (59.3%), Debt Markers (formerly Tech Debt) (14.1%), Dead Code Surface (formerly Dead Code) (11.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_png` **(Defensive Guards)** (Impact: 8.3)
  * `save_png` **(Type Conversions)** (Impact: 7.3)
  * `_read_data_to_buffer` **(Parameter Forwarders)** (Impact: 3.8)
  * `get_image_header` **(Compute Cores)** (Impact: 3.6)
  * `apply_image_filter` **(Compute Cores)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Memory Alloc (weighted view):* 2
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 25`, `args: 9`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 10`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 3`, `import: 7`
* *Defense:* `safety: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` math.h, spng.h, std, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ZigExamples/vectors/src/main.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.972)
- **Top Global Matches:** file_cluster_7: 8.972, file_cluster_12: 10.045, file_cluster_5: 11.073
- **Magnitude:** 45.42 | **LOC:** 61 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.02; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.6%), Debt Markers (formerly Tech Debt) (74.5%), Complexity Load (formerly Cognitive Load) (65.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 13.6)
  * `print_matrix` **(Defensive Guards)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 8 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 8`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 15`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ZigExamples/image_filter/src/test.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.412)
- **Top Global Matches:** file_cluster_7: 7.412, file_cluster_12: 7.647, file_cluster_5: 9.652
- **Magnitude:** 42.62 | **LOC:** 100 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.02; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.8%), Debt Markers (formerly Tech Debt) (72.9%), Guard Balance (formerly Safety Score) (59.1%), Complexity Load (formerly Cognitive Load) (18.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save_png` **(Defensive Guards)** (Impact: 9.6)
  * `main` **(Defensive Guards)** (Impact: 5.1)
  * `apply_image_filter` **(Defensive Guards)** (Impact: 4.0)
  * `read_data_to_buffer` **(Parameter Forwarders)** (Impact: 3.8)
  * `get_image_header` **(Parameter Forwarders)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 20`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 7`, `unreferenced_by_name: 3`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` spng.h, std, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ZigExamples/data-structures/generic_stack.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.55)
- **Top Global Matches:** file_cluster_12: 7.55, file_cluster_15: 9.277, file_cluster_5: 9.39
- **Magnitude:** 35.68 | **LOC:** 70 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.02; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Guard Balance (formerly Safety Score) (46.8%), Debt Markers (formerly Tech Debt) (30.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Stack` **(Defensive Guards)** (Impact: 6.4)
  * `push` **(Defensive Guards)** (Impact: 4.1)
  * `pop` **(Compute Cores)** (Impact: 3.1)
  * `init` **(Defensive Guards)** (Impact: 2.2)
  * `main` **(Defensive Guards)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 2 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ZigExamples/vectors/src/main2.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 13.076)
- **Top Global Matches:** file_cluster_7: 13.076, file_cluster_9: 13.089, file_cluster_12: 13.561
- **Magnitude:** 34.28 | **LOC:** 38 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.02; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (61.8%), Guard Balance (formerly Safety Score) (60.0%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 7 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ZigExamples/data-structures/stack.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.301)
- **Top Global Matches:** file_cluster_12: 7.301, file_cluster_15: 8.962, file_cluster_7: 9.648
- **Magnitude:** 29.1 | **LOC:** 66 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.02; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Guard Balance (formerly Safety Score) (46.7%), Debt Markers (formerly Tech Debt) (33.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `push` **(Defensive Guards)** (Impact: 4.1)
  * `pop` **(Compute Cores)** (Impact: 3.1)
  * `init` **(Defensive Guards)** (Impact: 2.2)
  * `main` **(Defensive Guards)** (Impact: 2.0)
  * `deinit` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 2 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 7`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ZigExamples/build.zig` (ZIG | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.255)
- **Top Global Matches:** file_cluster_15: 6.255, file_cluster_12: 6.682, file_cluster_2: 7.215
- **Magnitude:** 27.84 | **LOC:** 134 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.02; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (47.2%), Mutation Surface (formerly State Flux) (19.5%), Debt Markers (formerly Tech Debt) (15.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(I/O & Config Routines)** (Impact: 6.8)
  * `delete_compiled_artifacts` **(Defensive Guards)** (Impact: 6.3)
  * `get_file_name` **(Defensive Guards)** (Impact: 4.7)
  * `get_base_name` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 14`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ZigExamples/http_server/src/request.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.342)
- **Top Global Matches:** file_cluster_12: 6.342, file_cluster_15: 7.42, file_cluster_2: 8.59
- **Magnitude:** 27.74 | **LOC:** 78 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 7.726; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (50.7%), Guard Balance (formerly Safety Score) (40.9%), Mutation Surface (formerly State Flux) (35.2%), Complexity Load (formerly Cognitive Load) (7.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_request` **(Defensive Guards)** (Impact: 4.5)
  * `parse_request` **(Defensive Guards)** (Impact: 3.3)
  * `is_supported` **(Defensive Guards)** (Impact: 3.2)
  * `read_next_line` **(Defensive Guards)** (Impact: 2.4)
  * `init` **(Parameter Forwarders)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 11`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 10`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.726
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00625
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Assets/paypal-button.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.389)
- **Top Global Matches:** file_cluster_2: 4.389, file_cluster_13: 5.386, file_cluster_17: 5.982
- **Magnitude:** 26.68 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 2`, `func_start: 1`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Scripts/list_all_zig_example_files.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.015)
- **Top Global Matches:** file_cluster_2: 6.015, file_cluster_17: 7.174, file_cluster_13: 7.481
- **Magnitude:** 24.2 | **LOC:** 15 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.02; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (56.4%), Complexity Load (formerly Cognitive Load) (19.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 5`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, pathlib, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ZigExamples/threads/rw_lock.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.937)
- **Top Global Matches:** file_cluster_2: 7.937, file_cluster_15: 7.95, file_cluster_17: 8.554
- **Magnitude:** 19.8 | **LOC:** 40 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.02; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (50.0%), Guard Balance (formerly Safety Score) (43.6%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reader` **(Defensive Guards)** (Impact: 6.5)
  * `writer` **(Defensive Guards)** (Impact: 5.6)
  * `main` **(Defensive Guards)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 2`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 6`, `sync_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ZigExamples/threads/cancel_thread.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.378)
- **Top Global Matches:** file_cluster_15: 7.378, file_cluster_2: 7.426, file_cluster_11: 8.084
- **Magnitude:** 17.54 | **LOC:** 31 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.02; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Mutation Surface (formerly State Flux) (50.0%), Guard Balance (formerly Safety Score) (46.4%), Concurrency Surface (formerly Concurrency) (45.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `work` **(Defensive Guards)** (Impact: 7.8)
  * `do_more_work` **(Defensive Guards)** (Impact: 1.6)
  * `main` **(Defensive Guards)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 2`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ZigExamples/hello_world/src/main.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.911)
- **Top Global Matches:** file_cluster_12: 6.911, file_cluster_7: 7.45, file_cluster_5: 9.361
- **Magnitude:** 16.22 | **LOC:** 72 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 6.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Guard Balance (formerly Safety Score) (38.3%), Debt Markers (formerly Tech Debt) (36.8%), Complexity Load (formerly Cognitive Load) (6.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testOne` **(Defensive Guards)** (Impact: 10.0)
  * `main` **(Defensive Guards)** (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 8`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 10`, `test: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` hello_world, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `flake.nix` (NIX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.015)
- **Top Global Matches:** file_cluster_2: 2.015, file_cluster_17: 4.957, file_cluster_13: 6.226
- **Magnitude:** 16.22 | **LOC:** 90 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_quarto.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.994)
- **Top Global Matches:** file_cluster_2: 1.994, file_cluster_17: 4.881, file_cluster_13: 6.234
- **Magnitude:** 15.8 | **LOC:** 49 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Assets/button.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.156)
- **Top Global Matches:** file_cluster_2: 4.156, file_cluster_13: 5.59, file_cluster_17: 6.131
- **Magnitude:** 15.36 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 1`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Assets/leanpub-button.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.156)
- **Top Global Matches:** file_cluster_2: 4.156, file_cluster_13: 5.59, file_cluster_17: 6.131
- **Magnitude:** 15.36 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 1`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Assets/revolut-button.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.156)
- **Top Global Matches:** file_cluster_2: 4.156, file_cluster_13: 5.59, file_cluster_17: 6.131
- **Magnitude:** 15.36 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 1`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_freeze/Chapters/references/execute-results/html.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.052)
- **Top Global Matches:** file_cluster_2: 2.052, file_cluster_17: 4.908, file_cluster_13: 6.249
- **Magnitude:** 15.34 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_freeze/Chapters/15-vectors/execute-results/html.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.068)
- **Top Global Matches:** file_cluster_2: 2.068, file_cluster_17: 4.915, file_cluster_13: 6.253
- **Magnitude:** 15.3 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_freeze/index/execute-results/html.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.068)
- **Top Global Matches:** file_cluster_2: 2.068, file_cluster_17: 4.915, file_cluster_13: 6.253
- **Magnitude:** 15.3 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `_freeze/references/execute-results/html.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.068)
- **Top Global Matches:** file_cluster_2: 2.068, file_cluster_17: 4.915, file_cluster_13: 6.253
- **Magnitude:** 15.3 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ZigExamples/hello_world/build.zig.zon` (ZIG | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.089)
- **Top Global Matches:** file_cluster_2: 2.089, file_cluster_17: 4.924, file_cluster_13: 6.259
- **Magnitude:** 15.26 | **LOC:** 82 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `ZigExamples/threads/cancel_thread.zig` (ZIG) | Magnitude: 17.54 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, globals: 6, core_var_decl: 6, design_snake_case: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `ZigExamples/threads/rw_lock.zig` (ZIG) | Magnitude: 19.8 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 23, sync_locks: 17, core_var_decl: 12, design_snake_case: 7
- `ZigExamples/threads/mutex.zig` (ZIG) | Magnitude: 12.24 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, core_var_decl: 8, sync_locks: 7, globals: 5
- `ZigExamples/data-structures/string_hash.zig` (ZIG) | Magnitude: 4.1 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 12, core_var_decl: 5, design_snake_case: 5, structural_boundaries: 4
- `ZigExamples/data-structures/hash_table_it_key.zig` (ZIG) | Magnitude: 4.1 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 11, core_var_decl: 6, design_snake_case: 5, structural_boundaries: 4
- `ZigExamples/data-structures/hash_tables_it.zig` (ZIG) | Magnitude: 4.22 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 12, core_var_decl: 6, design_snake_case: 5, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `ZigExamples/vectors/src/main2.zig` (ZIG) | Magnitude: 34.28 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 30, safety: 9, state_mutation: 7, core_var_decl: 7
- `ZigExamples/threads/sleep.zig` (ZIG) | Magnitude: 6.78 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 18, core_var_decl: 11, safety: 9, design_snake_case: 8
- `ZigExamples/pointer/p2.zig` (ZIG) | Magnitude: 9.32 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 16, core_var_decl: 6, design_snake_case: 5, structural_boundaries: 3

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `ZigExamples/base64/base64_basic.zig` -> Churn: **63.09%** | Cog Load: 64.2129% | Debt: 15.0489%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `ZigExamples/base64/base64_basic.zig` -> **pedropark99** (100.0% isolated ownership) | Magnitude: 127.8

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `ZigExamples/calling-c/c.zig` -> **Severity: 0.353** (Embedded: 0.0063 * Error Risk: 56.554%)
- `ZigExamples/allocators/user_struct.zig` -> **Severity: 0.308** (Embedded: 0.0063 * Error Risk: 49.2858%)
- `ZigExamples/zig-basics/hello_world.zig` -> **Severity: 0.308** (Embedded: 0.0063 * Error Risk: 49.2858%)
- `ZigExamples/http_server/src/request.zig` -> **Severity: 0.256** (Embedded: 0.0063 * Error Risk: 40.9069%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ZigExamples/calling-c/c.zig` -> **Severity: 1113.8** (Blast Radius: 11.138 * Doc Risk: 100.0%)
- `ZigExamples/zig-basics/hello_world.zig` -> **Severity: 1113.8** (Blast Radius: 11.138 * Doc Risk: 100.0%)
- `ZigExamples/allocators/user_struct.zig` -> **Severity: 857.9** (Blast Radius: 8.579 * Doc Risk: 100.0%)
- `ZigExamples/zig-basics/pub-keyword.zig` -> **Severity: 857.9** (Blast Radius: 8.579 * Doc Risk: 100.0%)
- `ZigExamples/http_server/src/request.zig` -> **Severity: 772.6** (Blast Radius: 7.726 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 788 call pairs -- scoped 7.5%, unique 0.0%, ambiguous 3.3%, external 89.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 778 | 7.6% | 0.0% | 3.3% | 89.1% |
| python | 10 | 0.0% | 0.0% | 0.0% | 100.0% |

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
