# ARCHITECTURAL_BRIEF: functional
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/abitofhelp/functional.git` |
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
- **Scope:** 44 analyzed artifact(s), 5181 LOC.
- **Load-bearing artifact:** `test/unit/test_result.adb` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `test/unit/unit_runner.adb` -- pulls in 11 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `test/unit/test_result.adb` at magnitude 326.94 (structural weight, not risk).
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
| Total Artifacts | 67 |
| Analyzed Artifacts (Scanned) | 44 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 23 |
| Total LOC | 5181 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 65.7% |
| Dominant Lang | ADA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6224 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.1491 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ADA | 34 | 4731 | 77.3% |
| YAML | 4 | 122 | 9.1% |
| MARKDOWN | 4 | 0 | 9.1% |
| MAKEFILE | 1 | 316 | 2.3% |
| C | 1 | 12 | 2.3% |

## 4.1 SOURCE ENCODINGS
All 44 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 25%, Data / Markup / Trivial 20%, Interface Declarations Files 14%, Large Core Modules (2) 11%, Large Core Modules (3) 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 40 | 90.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 9.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 23*

**Composition by Extension & Reason:**
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gpr`: 4x Excluded (Unsupported Extension: '.gpr')
- `.pdf`: 3x Excluded (Explicitly Denied Extension: '.pdf')
- `.typ`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.adc`: 1x Excluded (Unsupported Extension: '.adc')
- `.jar`: 1x Excluded (Explicitly Denied Extension: '.jar')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 25.2 | 5.0 | 4.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 54.8 | 17.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.4 | 12.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 9.2 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 51.9 | 6.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 13.7 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 91.7 | 3.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 90.9 | 4.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 65.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 157 | 13 | 7 | `test/spark/spark_instantiations.ads` |
| cleanup | 19 | 4 | 0 | `Makefile` |
| guards | 428 | 32 | 44 | `test/spark/spark_instantiations.adb` |
| danger | 41 | 8 | 3 | `Makefile` |
| concurrency | 2 | 2 | 0 | `Makefile` |
| connectivity | 40 | 16 | 4 | `test/unit/test_result.adb` |
| io | 6 | 1 | 0 | `Makefile` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `Makefile` |
| time | 1 | 1 | 0 | `Makefile` |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `Makefile` |
| events | 1 | 1 | 0 | `Makefile` |
| tests | 167 | 9 | 10 | `test/unit/test_result.adb` |
| docs | 57 | 31 | 1 | `Makefile` |
| debt | 466 | 15 | 33 | `Makefile` |
| mutation | 539 | 32 | 42 | `test/unit/test_try.adb` |
| dead_code | 54 | 13 | 6 | `test/spark/spark_instantiations.ads` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 2 | 1 | 0 | `Makefile` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Makefile` (Hits: 6)
- `.clang-format` (Hits: 0)
- `.github/FUNDING.yml` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **test_result.adb** (`test/unit/test_result.adb`) — 3 inbound connections
2. **CHANGELOG.md** (`CHANGELOG.md`) — 1 inbound connections
3. **functional-option.adb** (`src/functional-option.adb`) — 1 inbound connections
4. **functional-try.adb** (`src/functional-try.adb`) — 1 inbound connections
5. **test_option.adb** (`test/unit/test_option.adb`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **unit_runner.adb** (`test/unit/unit_runner.adb`) — 11 outbound dependencies
2. **README.md** (`README.md`) — 8 outbound dependencies
3. **test_try.adb** (`test/unit/test_try.adb`) — 8 outbound dependencies
4. **functional-try.ads** (`src/functional-try.ads`) — 6 outbound dependencies
5. **test_either.adb** (`test/unit/test_either.adb`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Or_Else_With` **(Compute Cores)** (@ `src/functional-option.adb`) -> Impact: **14.2** | LOC: 30
  * *Intent:* -- Or_Else_With: lazy fallback
- `Capture` **(Compute Cores)** (@ `test/unit/test_option.adb`) -> Impact: **13.4** | LOC: 70
- `Add_Ints` **(Compute Cores)** (@ `test/spark/spark_instantiations.ads`) -> Impact: **13.3** | LOC: 24
  * *Intent:* -- ======================================================================== -- RESULT: Zip_With Instantiation -- =====================================...
- `Capture_Error` **(Compute Cores)** (@ `test/unit/test_result.adb`) -> Impact: **12.4** | LOC: 79
- `Multiply` **(Compute Cores)** (@ `test/unit/test_result.adb`) -> Impact: **12.2** | LOC: 37
- `Print_Category_Summary` **(Many-Argument Workhorses)** (@ `test/common/test_framework.adb`) -> Impact: **12.1** | LOC: 42
- `Is_Even` **(Compute Cores)** (@ `test/unit/test_option.adb`) -> Impact: **11.4** | LOC: 30
- `Is_Short` **(Compute Cores)** (@ `test/unit/test_either.adb`) -> Impact: **11.3** | LOC: 28
- `Is_Large` **(Compute Cores)** (@ `test/unit/test_either.adb`) -> Impact: **11.3** | LOC: 28
- `On_Error` **(Compute Cores)** (@ `test/unit/test_result.adb`) -> Impact: **11.2** | LOC: 26

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `test/unit` | 9 | 1101.78 | 8.76% | 0.0% |
| `src` | 19 | 571.84 | 5.12% | 21.18% |
| `__monolith__` | 4 | 134.86 | 0.93% | 2.91% |
| `test/spark` | 2 | 127.46 | 2.09% | 0.0% |
| `test/common` | 2 | 42.98 | 5.58% | 0.0% |
| `test/config` | 2 | 31.48 | 0.0% | 0.0% |
| `.github/workflows` | 2 | 21.38 | 3.01% | 0.0% |
| `.github` | 1 | 10.52 | 0.0% | 0.0% |
| `src/version` | 1 | 3.72 | 0.0% | 81.76% |
| `config` | 1 | 1.54 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/functional-try.ads` -> **99.4472%** Exposure
- `src/functional-either.adb` -> **97.3063%** Exposure
- `src/functional-result.adb` -> **93.0248%** Exposure
- `src/version/functional-version.ads` -> **81.7574%** Exposure
- `src/functional-option.adb` -> **74.8911%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/functional-scoped.adb` -> **91.6827%** Exposure
- `test/common/test_framework.adb` -> **35.3413%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/unit/test_try.adb` -> **0** Orphaned Functions | **20** Duplicates
- `test/spark/spark_instantiations.ads` -> **15** Orphaned Functions | **0** Duplicates
- `src/functional-either.adb` -> **7** Orphaned Functions | **0** Duplicates
- `src/functional-result.adb` -> **7** Orphaned Functions | **0** Duplicates
- `src/functional-option.adb` -> **6** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `94` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `test/unit/test_result.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.639)
- **Top Global Matches:** file_cluster_15: 7.639, file_cluster_0: 7.848, file_cluster_11: 7.939
- **Magnitude:** 326.94 | **LOC:** 957 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 52.455; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (36.4%), Complexity Load (formerly Cognitive Load) (17.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Capture_Error` **(Compute Cores)** (Impact: 12.4)
  * `Multiply` **(Compute Cores)** (Impact: 12.2)
  * `On_Error` **(Compute Cores)** (Impact: 11.2)
  * `Test_Contains` **(I/O & Config Routines)** (Impact: 8.1)
    * *Intent:* -- ========================================================================== -- Test: Contains and ...
  * `Error_Inner` **(Compute Cores)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 214`, `args: 33`, `func_start: 64`
* *Risk/State:* `state_mutation: 49`, `dead_code: 1`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `doc: 1`, `test: 54`, `immutability_locks: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 52.455
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.069767
  * `Imports (Out-Degree: 0):` Ada.Command_Line, Ada.Text_IO, Functional.Option, Functional.Result, Test_Framework
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `test/unit/test_option.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.002)
- **Top Global Matches:** file_cluster_0: 8.002, file_cluster_15: 8.003, file_cluster_11: 8.339
- **Magnitude:** 257.22 | **LOC:** 653 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 111.841; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (34.2%), Complexity Load (formerly Cognitive Load) (25.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Capture` **(Compute Cores)** (Impact: 13.4)
  * `Is_Even` **(Compute Cores)** (Impact: 11.4)
  * `Multiply` **(Compute Cores)** (Impact: 10.2)
    * *Intent:* -- Combine two integers by multiplication
  * `Test_Xor_Operator` **(I/O & Config Routines)** (Impact: 8.3)
    * *Intent:* -- ========================================================================== -- Test: "xor" operato...
  * `Is_Even` **(Generic / Templated Code)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 138`, `args: 19`, `func_start: 43`
* *Risk/State:* `state_mutation: 34`, `duplicate_logic: 2`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `doc: 1`, `test: 51`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 111.841
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023256
  * `Imports (Out-Degree: 1):` Ada.Command_Line, Ada.Text_IO, Functional.Option, Functional.Result, Test_Framework
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/unit/test_either.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.512)
- **Top Global Matches:** file_cluster_15: 7.512, file_cluster_0: 7.742, file_cluster_11: 7.924
- **Magnitude:** 240.3 | **LOC:** 732 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 16.785; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (27.8%), Complexity Load (formerly Cognitive Load) (10.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Is_Short` **(Compute Cores)** (Impact: 11.3)
  * `Is_Large` **(Compute Cores)** (Impact: 11.3)
  * `Is_Short` **(Generic / Templated Code)** (Impact: 9.8)
  * `Is_Large` **(Generic / Templated Code)** (Impact: 9.8)
  * `Test_To_Result` **(I/O & Config Routines)** (Impact: 9.8)
    * *Intent:* -- ========================================================================== -- Test: To_Result (co...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 149`, `args: 19`, `func_start: 39`
* *Risk/State:* `state_mutation: 27`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 1`, `doc: 1`, `test: 29`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Command_Line, Ada.Text_IO, Functional.Either, Functional.Option, Functional.Result, Test_Framework
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/functional-result.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.368)
- **Top Global Matches:** file_cluster_15: 4.368, file_cluster_11: 7.27, file_cluster_16: 7.316
- **Magnitude:** 158.42 | **LOC:** 307 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (93.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (13.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Ensure` **(Compute Cores)** (Impact: 9.1)
    * *Intent:* -- Ensure: validate Ok value with predicate
  * `Unwrap_Or` **(Compute Cores)** (Impact: 7.3)
    * *Intent:* -- Unwrap with default
  * `Map_Or` **(Compute Cores)** (Impact: 7.3)
    * *Intent:* -- Map_Or: transform Ok value or return default
  * `Fallback` **(Compute Cores)** (Impact: 7.3)
    * *Intent:* -- Fallback: eager alternative on error
  * `With_Context` **(Compute Cores)** (Impact: 7.3)
    * *Intent:* -- With_Context: enrich error with context
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 175`, `args: 32`, `func_start: 32`
* *Risk/State:* `planned_debt: 1`, `unreferenced_by_name: 7`
* *Architecture:* None
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/functional-option.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.418)
- **Top Global Matches:** file_cluster_15: 4.418, file_cluster_11: 6.554, file_cluster_16: 7.32
- **Magnitude:** 112.54 | **LOC:** 232 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 111.841; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (74.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (12.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Or_Else_With` **(Compute Cores)** (Impact: 14.2)
    * *Intent:* -- Or_Else_With: lazy fallback
  * `Filter` **(Compute Cores)** (Impact: 9.1)
    * *Intent:* -- Filter: keep value only if predicate holds
  * `Unwrap_Or` **(Compute Cores)** (Impact: 7.3)
    * *Intent:* -- Unwrap with default
  * `Map_Or` **(Compute Cores)** (Impact: 7.3)
    * *Intent:* -- Map_Or: transform Some value or return default
  * `Flatten` **(Compute Cores)** (Impact: 6.3)
    * *Intent:* -- Flatten: Option[Option[T]] -> Option[T]
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 136`, `args: 21`, `func_start: 22`
* *Risk/State:* `unreferenced_by_name: 6`
* *Architecture:* None
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 111.841
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023256
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/spark/spark_instantiations.ads` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.349)
- **Top Global Matches:** file_cluster_0: 7.349, file_cluster_15: 10.812, file_cluster_13: 11.354
- **Magnitude:** 107.8 | **LOC:** 468 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 16.785; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Dead Code Surface (formerly Dead Code) (5.7%), Complexity Load (formerly Cognitive Load) (4.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Add_Ints` **(Compute Cores)** (Impact: 13.3)
    * *Intent:* -- ======================================================================== -- RESULT: Zip_With Inst...
  * `Int_From_Right` **(Annotated & Test Methods)** (Impact: 5.5)
  * `Optional_If_Even` **(Generic / Templated Code)** (Impact: 4.9)
  * `Validate_In_Range` **(Generic / Templated Code)** (Impact: 4.5)
  * `Square` **(Compute Cores)** (Impact: 4.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 161`, `args: 29`, `func_start: 34`
* *Risk/State:* `dead_code: 1`, `unreferenced_by_name: 15`
* *Architecture:* `import: 3`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Functional.Either, Functional.Option, Functional.Result
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.518)
- **Top Global Matches:** file_cluster_12: 7.518, file_cluster_7: 8.341, file_cluster_5: 10.353
- **Magnitude:** 103.72 | **LOC:** 475 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (11.7%)
- **Documentation Coverage:** 30.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test-all` **(I/O & Config Routines)** (Impact: 10.7)
  * `test-windows` **(I/O & Config Routines)** (Impact: 9.4)
  * `clean-coverage` **(I/O & Config Routines)** (Impact: 7.5)
  * `test-unit` **(I/O & Config Routines)** (Impact: 5.7)
  * `spark-check` **(I/O & Config Routines)** (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 23`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 10`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `io: 6`, `api: 5`
* *Defense:* `safety: 1`, `doc: 22`, `test: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/test_try.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.059)
- **Top Global Matches:** file_cluster_11: 7.059, file_cluster_15: 7.235, file_cluster_0: 8.245
- **Magnitude:** 94.88 | **LOC:** 629 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 23.919; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.1%), Concurrency Surface (formerly Concurrency) (13.7%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Assert` **(Compute Cores)** (Impact: 5.7)
  * `Get_Value` **(I/O & Config Routines)** (Impact: 2.9)
  * `Test_Try` **(I/O & Config Routines)** (Impact: 1.9)
  * `To_Error` **(Parameter Forwarders)** (Impact: 1.6)
  * `To_Error` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 204`, `args: 19`, `func_start: 46`
* *Risk/State:* `state_mutation: 6`, `duplicate_logic: 20`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 16`, `doc: 1`, `test: 3`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.919
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023256
  * `Imports (Out-Degree: 0):` Ada.Command_Line, Ada.Exceptions, Ada.Text_IO, Functional.Option, Functional.Result, Functional.Try, Functional.Try.To_Result, Test_Framework
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/functional-either.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.58)
- **Top Global Matches:** file_cluster_15: 4.58, file_cluster_11: 7.245, file_cluster_2: 7.364
- **Magnitude:** 89.6 | **LOC:** 172 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.3%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (13.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Map_Left` **(Compute Cores)** (Impact: 6.1)
    * *Intent:* -- Map_Left: transform Left value
  * `Map_Right` **(Compute Cores)** (Impact: 6.1)
    * *Intent:* -- Map_Right: transform Right value
  * `Bimap` **(Compute Cores)** (Impact: 6.1)
    * *Intent:* -- Bimap: transform both Left and Right values simultaneously
  * `Map` **(Compute Cores)** (Impact: 6.1)
    * *Intent:* -- Map: transform Right value (Right-biased convenience)
  * `Swap` **(Compute Cores)** (Impact: 6.1)
    * *Intent:* -- Swap: exchange Left and Right values
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 96`, `args: 22`, `func_start: 22`
* *Risk/State:* `unreferenced_by_name: 7`
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/test_try_map_to_result_with_param.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.399)
- **Top Global Matches:** file_cluster_15: 6.399, file_cluster_11: 6.662, file_cluster_0: 8.06
- **Magnitude:** 58.16 | **LOC:** 315 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 16.785; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.8%), Connectivity (formerly Api Exposure) (13.7%), Complexity Load (formerly Cognitive Load) (4.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Assert` **(Compute Cores)** (Impact: 5.7)
  * `Test_Try_Map_To_Result_With_Param` **(I/O & Config Routines)** (Impact: 5.1)
  * `Validate_Positive` **(Parameter Forwarders)** (Impact: 3.1)
  * `Check_Range` **(Defensive Guards)** (Impact: 3.1)
  * `Divide_By` **(Parameter Forwarders)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 94`, `args: 15`, `func_start: 23`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 10`, `doc: 1`, `test: 14`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Ada.Command_Line, Ada.IO_Exceptions, Ada.Text_IO, Functional.Try.Map_To_Result_With_Param, Test_Framework
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/test_try_map_to_result.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.368)
- **Top Global Matches:** file_cluster_11: 6.368, file_cluster_15: 6.767, file_cluster_0: 8.087
- **Magnitude:** 50.44 | **LOC:** 316 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 16.785; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.3%), Connectivity (formerly Api Exposure) (13.7%), Complexity Load (formerly Cognitive Load) (4.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Assert` **(Compute Cores)** (Impact: 5.7)
  * `Test_Try_Map_To_Result` **(I/O & Config Routines)** (Impact: 5.0)
  * `Make_Error` **(Parameter Forwarders)** (Impact: 2.1)
  * `Is_Ok` **(Parameter Forwarders)** (Impact: 1.5)
  * `Is_Error` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 91`, `args: 8`, `func_start: 23`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 8`, `doc: 1`, `test: 10`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Ada.Command_Line, Ada.IO_Exceptions, Ada.Text_IO, Functional.Try.Map_To_Result, Test_Framework
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/test_scoped.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.062)
- **Top Global Matches:** file_cluster_15: 6.062, file_cluster_11: 6.908, file_cluster_0: 7.625
- **Magnitude:** 36.26 | **LOC:** 393 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 16.785; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.8%), Connectivity (formerly Api Exposure) (13.2%), Complexity Load (formerly Cognitive Load) (5.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Assert` **(Compute Cores)** (Impact: 6.1)
  * `Is_Active` **(Generic / Templated Code)** (Impact: 2.6)
  * `Raising_Release` **(Parameter Forwarders)** (Impact: 1.7)
  * `Raising_Condition` **(Parameter Forwarders)** (Impact: 1.7)
  * `Release_Resource` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 82`, `args: 6`, `func_start: 7`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 19`, `doc: 1`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Command_Line, Ada.Text_IO, Functional.Scoped, Test_Framework
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/test_try_option.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.275)
- **Top Global Matches:** file_cluster_11: 7.275, file_cluster_0: 7.327, file_cluster_15: 8.16
- **Magnitude:** 28.02 | **LOC:** 164 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 16.785; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.8%), Connectivity (formerly Api Exposure) (24.5%), Complexity Load (formerly Cognitive Load) (5.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Assert` **(Compute Cores)** (Impact: 5.7)
  * `Get_Value` **(I/O & Config Routines)** (Impact: 2.9)
  * `Test_Try_Option` **(Generic / Templated Code)** (Impact: 1.3)
  * `Raise_Error` **(Defensive Guards)** (Impact: 1.2)
  * `Test_Try_Success` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* -- ========================================================================== -- Test: Try with succ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 43`, `args: 1`, `func_start: 10`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 3`, `doc: 1`, `test: 3`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Command_Line, Ada.Text_IO, Functional.Option, Functional.Try.To_Option, Test_Framework
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/common/test_framework.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.979)
- **Top Global Matches:** file_cluster_11: 5.979, file_cluster_15: 6.456, file_cluster_2: 8.005
- **Magnitude:** 26.76 | **LOC:** 92 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 16.785; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.3%), Connectivity (formerly Api Exposure) (51.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (35.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Print_Category_Summary` **(Many-Argument Workhorses)** (Impact: 12.1)
  * `Register_Results` **(Parameter Forwarders)** (Impact: 2.0)
  * `Reset` **(Interface Declarations)** (Impact: 1.2)
  * `Grand_Total_Tests` **(Interface Declarations)** (Impact: 1.1)
  * `Grand_Total_Passed` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 20`, `args: 2`, `func_start: 5`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Text_IO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/spark/spark_instantiations.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.708)
- **Top Global Matches:** file_cluster_11: 6.708, file_cluster_2: 8.102, file_cluster_17: 8.177
- **Magnitude:** 19.66 | **LOC:** 226 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Test_Result_Operations` **(I/O & Config Routines)** (Impact: 3.5)
    * *Intent:* -- ======================================================================== -- Comprehensive Test: R...
  * `Test_Option_Operations` **(I/O & Config Routines)** (Impact: 3.5)
    * *Intent:* -- ======================================================================== -- Comprehensive Test: O...
  * `Test_Either_Operations` **(I/O & Config Routines)** (Impact: 3.3)
    * *Intent:* -- ======================================================================== -- Comprehensive Test: E...
  * `Test_Option_Some` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* -- ======================================================================== -- Basic Test Functions ...
  * `Test_Option_None` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 47`, `func_start: 9`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `immutability_locks: 72`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/functional-result.ads` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 4.837)
- **Top Global Matches:** file_cluster_0: 4.837, file_cluster_13: 7.475, file_cluster_2: 8.33
- **Magnitude:** 18.12 | **LOC:** 292 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 16.785; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 143`, `args: 64`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` function, procedure
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/functional-option.ads` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 4.852)
- **Top Global Matches:** file_cluster_0: 4.852, file_cluster_13: 7.047, file_cluster_2: 7.921
- **Magnitude:** 17.46 | **LOC:** 236 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 16.785; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (6.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 104`, `args: 39`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` function, procedure
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/functional-scoped.ads` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.547)
- **Top Global Matches:** file_cluster_0: 6.547, file_cluster_2: 8.114, file_cluster_13: 8.366
- **Magnitude:** 17.46 | **LOC:** 87 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 16.785; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Dead Code Surface (formerly Dead Code) (36.8%), Connectivity (formerly Api Exposure) (2.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Memory Alloc (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `args: 5`
* *Risk/State:* `dead_code: 2`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Finalization, function, procedure
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/functional-scoped.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.813)
- **Top Global Matches:** file_cluster_15: 6.813, file_cluster_2: 6.832, file_cluster_11: 7.51
- **Magnitude:** 17.44 | **LOC:** 72 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.6%), Complexity Load (formerly Cognitive Load) (12.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Finalize` **(Defensive Guards)** (Impact: 7.0)
  * `Finalize` **(Defensive Guards)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 17`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* None
* *Defense:* `safety: 6`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/functional-either.ads` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 4.946)
- **Top Global Matches:** file_cluster_0: 4.946, file_cluster_13: 7.215, file_cluster_2: 8.241
- **Magnitude:** 17.18 | **LOC:** 193 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 16.785; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.3%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 91`, `args: 41`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` function
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/functional-try.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.0)
- **Top Global Matches:** file_cluster_11: 6.0, file_cluster_15: 6.928, file_cluster_2: 7.073
- **Magnitude:** 16.8 | **LOC:** 105 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 31.053; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Try_To_Result_With_Param` **(Defensive Guards)** (Impact: 3.2)
    * *Intent:* -- ======================================================================== -- Try_To_Result_With_Pa...
  * `Try_To_Option_With_Param` **(Defensive Guards)** (Impact: 3.2)
    * *Intent:* -- ======================================================================== -- Try_To_Option_With_Pa...
  * `Try_To_Any_Result_With_Param` **(Defensive Guards)** (Impact: 3.1)
    * *Intent:* -- ======================================================================== -- Try_To_Any_Result_Wit...
  * `Try_To_Result` **(Defensive Guards)** (Impact: 2.3)
    * *Intent:* -- ======================================================================== -- Try_To_Result - Gener...
  * `Try_To_Functional_Option` **(Defensive Guards)** (Impact: 2.3)
    * *Intent:* -- ======================================================================== -- Try_To_Functional_Opt...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 38`, `args: 3`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023256
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/config/functional_tests_config.ads` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 5.809)
- **Top Global Matches:** file_cluster_17: 5.809, file_cluster_2: 6.089, file_cluster_15: 7.3
- **Magnitude:** 16.24 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/common/test_framework.ads` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.767)
- **Top Global Matches:** file_cluster_2: 3.767, file_cluster_17: 4.592, file_cluster_13: 5.292
- **Magnitude:** 16.22 | **LOC:** 36 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (25.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/functional-try-map_to_result_with_param.ads` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.505)
- **Top Global Matches:** file_cluster_0: 6.505, file_cluster_17: 7.1, file_cluster_2: 7.134
- **Magnitude:** 15.44 | **LOC:** 110 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 16.785; role: Isolated/Orphan
- **Top Surface Vectors:** Dead Code Surface (formerly Dead Code) (90.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 4`
* *Risk/State:* `dead_code: 6`
* *Architecture:* `import: 1`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Exceptions, function
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/functional-try-map_to_result.ads` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.706)
- **Top Global Matches:** file_cluster_0: 5.706, file_cluster_2: 6.384, file_cluster_17: 6.418
- **Magnitude:** 15.42 | **LOC:** 107 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 16.785; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Dead Code Surface (formerly Dead Code) (14.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 2`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `import: 1`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Exceptions, function
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `test/unit/test_option.adb` (ADA) | Magnitude: 257.22 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 432, structural_boundaries: 138, branch: 60, test: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `test/unit/test_try_option.adb` (ADA) | Magnitude: 28.02 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 43, debug_prints: 17, func_start: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/functional-scoped.adb` (ADA) | Magnitude: 17.44 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 17, safety: 6, branch: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test/unit/test_result.adb` -> **Michael Gardner** (100.0% isolated ownership) | Magnitude: 326.94
- `test/unit/test_option.adb` -> **Michael Gardner** (100.0% isolated ownership) | Magnitude: 257.22
- `test/unit/test_either.adb` -> **Michael Gardner** (100.0% isolated ownership) | Magnitude: 240.3
- `src/functional-result.adb` -> **Michael Gardner** (100.0% isolated ownership) | Magnitude: 158.42
- `src/functional-option.adb` -> **Michael Gardner** (100.0% isolated ownership) | Magnitude: 112.54

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `test/unit/test_result.adb` -> **Severity: 3.774** (Embedded: 0.0698 * Error Risk: 54.0949%)
- `test/unit/test_option.adb` -> **Severity: 1.27** (Embedded: 0.0233 * Error Risk: 54.6288%)
- `test/unit/test_try.adb` -> **Severity: 1.119** (Embedded: 0.0233 * Error Risk: 48.0962%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/functional-option.adb` -> **Severity: 11184.1** (Blast Radius: 111.841 * Doc Risk: 100.0%)
- `test/unit/test_option.adb` -> **Severity: 11184.1** (Blast Radius: 111.841 * Doc Risk: 100.0%)
- `test/unit/test_result.adb` -> **Severity: 5245.5** (Blast Radius: 52.455 * Doc Risk: 100.0%)
- `src/functional-try.adb` -> **Severity: 3105.3** (Blast Radius: 31.053 * Doc Risk: 100.0%)
- `test/unit/test_try.adb` -> **Severity: 2391.9** (Blast Radius: 23.919 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 742 call pairs -- scoped 9.3%, unique 5.0%, ambiguous 2.2%, external 83.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| ada | 742 | 9.3% | 5.0% | 2.2% | 83.6% |

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
