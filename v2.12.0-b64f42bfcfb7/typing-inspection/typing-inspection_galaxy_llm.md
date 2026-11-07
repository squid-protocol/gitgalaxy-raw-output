# ARCHITECTURAL_BRIEF: typing-inspection
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
- **Scope:** 18 analyzed artifact(s), 1264 LOC.
- **Load-bearing artifact:** `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `typing_inspection-0.4.2/tests/conftest.py` -- pulls in 12 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `typing_inspection-0.4.2/src/typing_inspection/introspection.py` at magnitude 281.8 (structural weight, not risk).
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
| Total Artifacts | 26 |
| Analyzed Artifacts (Scanned) | 18 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 1264 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3194 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.1581 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 11 | 951 | 61.1% |
| YAML | 3 | 276 | 16.7% |
| MARKDOWN | 2 | 0 | 11.1% |
| MAKEFILE | 1 | 30 | 5.6% |
| SHELL | 1 | 7 | 5.6% |

## 4.1 SOURCE ENCODINGS
All 18 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 50%, Generic / Templated Code Files 28%, Large Core Modules 6%, Large Core Modules (2) 6%, Many-Argument Workhorses Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 16 | 88.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 11.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.yml`: 1x Zero-Density Threshold (LOC: 97, Signals: 0)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 38.9 | 9.9 | 4.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.5 | 45.6 | 50.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 92.2 | 7.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.6 | 1.3 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 65.9 | 11.1 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.9 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 52.9 | 56.6 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 21 | 5 | 2 | `typing_inspection-0.4.2/tests/introspection/test_literal_values.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 99 | 9 | 16 | `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` |
| danger | 115 | 10 | 21 | `typing_inspection-0.4.2/src/typing_inspection/introspection.py` |
| concurrency | 14 | 2 | 0 | `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` |
| connectivity | 134 | 11 | 14 | `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` |
| io | 24 | 10 | 3 | `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `typing_inspection-0.4.2/build-docs.sh` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `typing_inspection-0.4.2/tests/conftest.py` |
| events | 0 | 0 | 0 | - |
| tests | 71 | 8 | 14 | `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` |
| docs | 114 | 10 | 25 | `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` |
| debt | 7 | 3 | 1 | `typing_inspection-0.4.2/.github/workflows/ci.yml` |
| mutation | 376 | 11 | 55 | `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` |
| dead_code | 30 | 6 | 6 | `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0285**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` (Hits: 6)
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` (Hits: 4)
- `typing_inspection-0.4.2/.github/workflows/ci.yml` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **introspection.py** (`typing_inspection-0.4.2/src/typing_inspection/introspection.py`) — 3 inbound connections
2. **__init__.py** (`typing_inspection-0.4.2/src/typing_inspection/__init__.py`) — 2 inbound connections
3. **typing_objects.py** (`typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) — 1 inbound connections
4. **ci.yml** (`typing_inspection-0.4.2/.github/workflows/ci.yml`) — 0 inbound connections
5. **coverage.yml** (`typing_inspection-0.4.2/.github/workflows/coverage.yml`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **conftest.py** (`typing_inspection-0.4.2/tests/conftest.py`) — 12 outbound dependencies
2. **ci.yml** (`typing_inspection-0.4.2/.github/workflows/ci.yml`) — 10 outbound dependencies
3. **introspection.py** (`typing_inspection-0.4.2/src/typing_inspection/introspection.py`) — 9 outbound dependencies
4. **typing_objects.py** (`typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) — 9 outbound dependencies
5. **test_member_checks.py** (`typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `inspect_annotation` **(Many-Argument Workhorses)** (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> Impact: **54.1** | LOC: 122
- `get_literal_values` **(Many-Argument Workhorses)** (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> Impact: **49.5** | LOC: 110
- `_unpack_annotated_inner` **(Many-Argument Workhorses)** (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> Impact: **25.2** | LOC: 64
- `_compile_identity_check_function` **(Stateful Encapsulated Methods)** (@ `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) -> Impact: **21.2** | LOC: 43
  * *Intent:* """Create a function checking that the function argument is the (unparameterized) typing `member`. The function will make sure to check against both t...
- `_compile_isinstance_check_function` **(Stateful Encapsulated Methods)** (@ `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) -> Impact: **18.8** | LOC: 30
  * *Intent:* """Create a function checking that the function is an instance of the typing `member`. The function will make sure to check against both the `typing` ...
- `run` **(Many-Argument Workhorses)** (@ `typing_inspection-0.4.2/tests/conftest.py`) -> Impact: **13.7** | LOC: 33
- `create_module` **(Generic / Templated Code)** (@ `typing_inspection-0.4.2/tests/conftest.py`) -> Impact: **12.3** | LOC: 38
- `allowed_qualifiers` **(Generic / Templated Code)** (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> Impact: **12.2** | LOC: 17
  * *Intent:* """The allowed [type qualifiers][type qualifier] for this annotation source."""
- `_extract_source_code_from_function` **(Stateful Encapsulated Methods)** (@ `typing_inspection-0.4.2/tests/conftest.py`) -> Impact: **7.8** | LOC: 14
- `_unpack_annotated` **(Stateful Encapsulated Methods)** (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> Impact: **7.4** | LOC: 10
  * *Intent:* # This could eventually be made public:

*Function archetypes referenced above:*
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `typing_inspection-0.4.2/src/typing_inspection` | 4 | 594.1 | 20.04% | 6.82% |
| `typing_inspection-0.4.2/tests/introspection` | 4 | 95.82 | 2.83% | 0.0% |
| `typing_inspection-0.4.2/tests/typing_objects` | 2 | 81.92 | 9.32% | 0.0% |
| `typing_inspection-0.4.2/tests` | 1 | 73.44 | 30.0% | 0.0% |
| `typing_inspection-0.4.2/.github/workflows` | 3 | 43.42 | 5.15% | 30.74% |
| `typing_inspection-0.4.2` | 4 | 28.04 | 0.56% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `typing_inspection-0.4.2/.github/workflows/ci.yml` -> **92.2334%** Exposure
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` -> **14.0027%** Exposure
- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **13.2964%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` -> **100.0%** Exposure
- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **99.9999%** Exposure
- `typing_inspection-0.4.2/.github/workflows/docs_publish.yml` -> **50.0%** Exposure
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` -> **31.948%** Exposure
- `typing_inspection-0.4.2/.github/workflows/coverage.yml` -> **16.7982%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` -> **12** Orphaned Functions | **0** Duplicates
- `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` -> **9** Orphaned Functions | **0** Duplicates
- `typing_inspection-0.4.2/tests/introspection/test_literal_values.py` -> **6** Orphaned Functions | **0** Duplicates
- `typing_inspection-0.4.2/.github/workflows/ci.yml` -> **0** Orphaned Functions | **2** Duplicates
- `typing_inspection-0.4.2/tests/conftest.py` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `78` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `typing_inspection-0.4.2/src/typing_inspection/introspection.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.986)
- **Top Global Matches:** file_cluster_6: 12.986, file_cluster_4: 16.679, file_cluster_8: 18.01
- **Magnitude:** 281.8 | **LOC:** 588 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 124.719; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (38.9%)
- **Documentation Coverage:** 63.1579% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inspect_annotation` **(Many-Argument Workhorses)** (Impact: 54.1)
  * `get_literal_values` **(Many-Argument Workhorses)** (Impact: 49.5)
  * `_unpack_annotated_inner` **(Many-Argument Workhorses)** (Impact: 25.2)
  * `allowed_qualifiers` **(Generic / Templated Code)** (Impact: 12.2)
    * *Intent:* """The allowed [type qualifiers][type qualifier] for this annotation source."""
  * `_unpack_annotated` **(Stateful Encapsulated Methods)** (Impact: 7.4)
    * *Intent:* # This could eventually be made public:
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 63`, `args: 11`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 40`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 2`, `api: 12`, `import: 9`
* *Defense:* `safety: 12`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 124.719
  * `Choke Point (Betweenness):` 0.009804 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 1):` .typing_objects, __future__, collections.abc, dataclasses, enum, sys, types, typing...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.639)
- **Top Global Matches:** file_cluster_5: 7.639, file_cluster_7: 9.396, file_cluster_12: 10.026
- **Magnitude:** 217.82 | **LOC:** 608 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 145.92; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (37.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_compile_identity_check_function` **(Stateful Encapsulated Methods)** (Impact: 21.2)
    * *Intent:* """Create a function checking that the function argument is the (unparameterized) typing `member`. T...
  * `_compile_isinstance_check_function` **(Stateful Encapsulated Methods)** (Impact: 18.8)
    * *Intent:* """Create a function checking that the function is an instance of the typing `member`. The function ...
  * `is_namedtuple` **(Defensive Guards)** (Impact: 5.2)
    * *Intent:* """Return whether the argument is a named tuple type. This includes [`NamedTuple`][typing.NamedTuple...
  * `is_typealiastype` **(Generic / Templated Code)** (Impact: 2.9)
    * *Intent:* # Parameterized PEP 695 type aliases are instances of `types.GenericAlias` in typing_extensions>=4.1...
  * `is_newtype` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 37 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 36`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 2`, `state_mutation: 81`
* *Architecture:* `io: 4`, `api: 6`, `import: 12`
* *Defense:* `safety: 14`, `doc: 37`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 145.92
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.126984
  * `Imports (Out-Degree: 0):` collections.abc, contextlib, re, sys, textwrap, types, typing, typing_extensions...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 10.905)
- **Top Global Matches:** file_cluster_14: 10.905, file_cluster_5: 13.183, file_cluster_7: 14.551
- **Magnitude:** 83.96 | **LOC:** 418 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 39.91; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (89.5%), Connectivity (formerly Api Exposure) (65.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (31.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_annotated` **(Generic / Templated Code)** (Impact: 1.5)
    * *Intent:* """ Return whether the argument is the [`Annotated`][typing.Annotated] [special form][]. ```pycon >>...
  * `is_any` **(Generic / Templated Code)** (Impact: 1.5)
    * *Intent:* """ Return whether the argument is the [`Any`][typing.Any] [special form][]. ```pycon >>> is_any(Any...
  * `is_classvar` **(Generic / Templated Code)** (Impact: 1.5)
    * *Intent:* """ Return whether the argument is the [`ClassVar`][typing.ClassVar] [type qualifier][]. ```pycon >>...
  * `is_concatenate` **(Generic / Templated Code)** (Impact: 1.5)
    * *Intent:* """ Return whether the argument is the [`Concatenate`][typing.Concatenate] [special form][]. ```pyco...
  * `is_final` **(Generic / Templated Code)** (Impact: 1.5)
    * *Intent:* """ Return whether the argument is the [`Final`][typing.Final] [type qualifier][]. ```pycon >>> is_f...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 40`, `args: 31`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 2`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 32`, `import: 4`
* *Defense:* `doc: 33`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, types, typing, typing_extensions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.658)
- **Top Global Matches:** file_cluster_0: 8.658, file_cluster_9: 9.274, file_cluster_16: 10.113
- **Magnitude:** 73.44 | **LOC:** 83 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 39.91; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (30.0%), Connectivity (formerly Api Exposure) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 13.7)
  * `create_module` **(Generic / Templated Code)** (Impact: 12.3)
  * `_extract_source_code_from_function` **(Stateful Encapsulated Methods)** (Impact: 7.8)
  * `_create_module_file` **(Stateful Encapsulated Methods)** (Impact: 2.5)
    * *Intent:* # Max path length in Windows is 260. Leaving some buffer here max_name_len = 240 - len(str(tmp_path)...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 27`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 2`, `import: 12`
* *Defense:* `safety: 1`, `doc: 1`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, _pytest.assertion.rewrite, collections.abc, importlib.util, inspect, pathlib, pytest, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.404)
- **Top Global Matches:** file_cluster_5: 6.404, file_cluster_7: 9.416, file_cluster_12: 9.942
- **Magnitude:** 71.4 | **LOC:** 210 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 39.91; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (18.6%), Connectivity (formerly Api Exposure) (10.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_identity_member_check` **(Generic / Templated Code)** (Impact: 2.1)
  * `test_is_typealiastype` **(Defensive Guards)** (Impact: 1.7)
  * `test_is_namedtuple` **(Generic / Templated Code)** (Impact: 1.5)
  * `test_is_newtype` **(Generic / Templated Code)** (Impact: 1.5)
  * `test_is_paramspec` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 45`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 18`, `unreferenced_by_name: 12`
* *Architecture:* `io: 6`, `api: 14`, `import: 11`
* *Defense:* `safety: 15`, `test: 25`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` collections, collections.abc, pytest, sys, types, typing, typing_extensions, typing_inspection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.092)
- **Top Global Matches:** file_cluster_5: 7.092, file_cluster_12: 8.642, file_cluster_7: 10.008
- **Magnitude:** 51.9 | **LOC:** 207 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 39.91; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.6%), Connectivity (formerly Api Exposure) (8.6%), Complexity Load (formerly Cognitive Load) (7.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_annotation_source_invalid_qualifiers` **(Generic / Templated Code)** (Impact: 3.7)
  * `test_annotation_source_valid_qualifiers` **(Generic / Templated Code)** (Impact: 3.6)
  * `test_unpack_type_aliases_undefined_lenient` **(Defensive Guards)** (Impact: 3.1)
  * `test_unpack_type_aliases_undefined_eager_fails` **(Defensive Guards)** (Impact: 2.9)
  * `test_bare_qualifier` **(Defensive Guards)** (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 61`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`, `unreferenced_by_name: 9`
* *Architecture:* `io: 2`, `api: 9`, `import: 8`
* *Defense:* `safety: 22`, `doc: 2`, `test: 21`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dataclasses, pytest, sys, textwrap, typing, typing_extensions, typing_inspection.introspection
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/.github/workflows/ci.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.018)
- **Top Global Matches:** file_cluster_11: 6.018, file_cluster_2: 6.194, file_cluster_15: 6.847
- **Magnitude:** 27.82 | **LOC:** 236 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 39.91; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (92.2%), Guard Balance (formerly Safety Score) (50.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (14.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Install dependencies and typing-extensions main` **(I/O & Config Routines)** (Impact: 2.2)
  * `run` **(I/O & Config Routines)** (Impact: 2.2)
  * `Install lowest dependencies` **(I/O & Config Routines)** (Impact: 2.1)
  * `Install dependencies` **(I/O & Config Routines)** (Impact: 1.2)
  * `Run tests` **(Interface Declarations)** (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 27`, `args: 26`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 1`, `import: 24`
* *Defense:* `doc: 9`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@v4, download-artifact@v4, setup-python@v5, upload-artifact@v4, setup-uv@v5, action@v3.0.1, python-coverage-comment-action@v3, v1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/introspection/test_literal_values.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.146)
- **Top Global Matches:** file_cluster_5: 8.146, file_cluster_7: 9.949, file_cluster_12: 10.346
- **Magnitude:** 27.52 | **LOC:** 80 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 39.91; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.6%), Connectivity (formerly Api Exposure) (8.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_literal_values_unpack_type_aliases_undefined` **(Type Conversions)** (Impact: 2.4)
  * `test_literal_values_skip_aliases_no_type_check` **(Type Conversions)** (Impact: 1.9)
  * `test_literal_values_type_check` **(Type Conversions)** (Impact: 1.6)
  * `test_literal_values_unpack_type_aliases` **(Type Conversions)** (Impact: 1.4)
  * `test_literal_values_skip_aliases_type_check` **(Type Conversions)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 32`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 11`, `unreferenced_by_name: 6`
* *Architecture:* `io: 1`, `api: 6`, `import: 8`
* *Defense:* `safety: 6`, `doc: 1`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pytest, sys, textwrap, typing, typing_extensions, typing_inspection, typing_inspection.introspection
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.574)
- **Top Global Matches:** file_cluster_2: 5.574, file_cluster_15: 7.115, file_cluster_13: 7.201
- **Magnitude:** 24.3 | **LOC:** 40 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (13.0%), Test Surface (formerly Verification) (2.4%), Complexity Load (formerly Cognitive Load) (2.2%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `.uv` **(I/O & Config Routines)** (Impact: 2.2)
  * `install` **(I/O & Config Routines)** (Impact: 1.2)
  * `test` **(I/O & Config Routines)** (Impact: 1.2)
  * `format` **(I/O & Config Routines)** (Impact: 1.2)
  * `format-diff` **(I/O & Config Routines)** (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`, `func_start: 9`
* *Risk/State:* None
* *Architecture:* `api: 12`
* *Defense:* `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/.github/workflows/docs_publish.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.538)
- **Top Global Matches:** file_cluster_11: 5.538, file_cluster_2: 6.476, file_cluster_15: 6.952
- **Magnitude:** 12.32 | **LOC:** 47 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 39.91; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.0%), Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (8.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Interface Declarations)** (Impact: 3.2)
  * `run` **(I/O & Config Routines)** (Impact: 2.1)
  * `Set git credentials` **(I/O & Config Routines)** (Impact: 1.2)
  * `run` **(State Mutators)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 3`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@v4, setup-uv@v5, check-python-version@v4.1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/src/typing_inspection/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 90.796; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 90.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `typing_inspection-0.4.2/tests/introspection/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/typing_objects/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/introspection/test_is_union_origin.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.58)
- **Top Global Matches:** file_cluster_5: 8.58, file_cluster_7: 9.634, file_cluster_14: 9.663
- **Magnitude:** 5.88 | **LOC:** 26 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 39.91; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (4.0%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_is_union_origin` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 11`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 7`
* *Defense:* `safety: 1`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pytest, sys, types, typing, typing_extensions, typing_inspection.introspection
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/.github/workflows/coverage.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.493)
- **Top Global Matches:** file_cluster_2: 5.493, file_cluster_17: 6.707, file_cluster_15: 6.994
- **Magnitude:** 3.28 | **LOC:** 61 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 39.91; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (16.8%), Complexity Load (formerly Cognitive Load) (3.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(I/O & Config Routines)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 5`, `args: 9`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `import: 3`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` setup-uv@v5, action-download-artifact@v8, python-coverage-comment-action@v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/build-docs.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.936)
- **Top Global Matches:** file_cluster_7: 6.936, file_cluster_14: 7.895, file_cluster_5: 10.942
- **Magnitude:** 1.74 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 2`
* *Defense:* `safety: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/HISTORY.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **Severity: 0.98** (Bridge: 0.0098 * Flux: 99.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **Severity: 13.333** (Embedded: 0.1667 * Error Risk: 80.0%)
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` -> **Severity: 10.562** (Embedded: 0.127 * Error Risk: 83.1776%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **Severity: 7876.99** (Blast Radius: 124.719 * Doc Risk: 63.1579%)
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` -> **Severity: 7296.0** (Blast Radius: 145.92 * Doc Risk: 50.0%)
- `typing_inspection-0.4.2/tests/conftest.py` -> **Severity: 3991.0** (Blast Radius: 39.91 * Doc Risk: 100.0%)
- `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` -> **Severity: 3991.0** (Blast Radius: 39.91 * Doc Risk: 100.0%)
- `typing_inspection-0.4.2/tests/introspection/test_is_union_origin.py` -> **Severity: 3991.0** (Blast Radius: 39.91 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 151 call pairs -- scoped 17.2%, unique 0.0%, ambiguous 2.0%, external 80.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 148 | 17.6% | 0.0% | 2.0% | 80.4% |
| shell | 3 | 0.0% | 0.0% | 0.0% | 100.0% |

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
