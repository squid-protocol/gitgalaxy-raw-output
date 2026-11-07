# ARCHITECTURAL_BRIEF: contourpy
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
- **Scope:** 108 analyzed artifact(s), 14876 LOC.
- **Load-bearing artifact:** `contourpy-1.3.3/lib/contourpy/__init__.py` -- 41 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `contourpy-1.3.3/lib/contourpy/util/bokeh_renderer.py` -- pulls in 19 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `contourpy-1.3.3/src/base_impl.h` at magnitude 3437.54 (structural weight, not risk).
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
| Total Artifacts | 172 |
| Analyzed Artifacts (Scanned) | 108 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 64 |
| Total LOC | 14876 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 62.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4677 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1321 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8741 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 9 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 64 | 7966 | 59.3% |
| CPP | 32 | 6241 | 29.6% |
| MARKDOWN | 5 | 0 | 4.6% |
| YAML | 5 | 645 | 4.6% |
| JSON | 1 | 24 | 0.9% |
| PLAINTEXT | 1 | 0 | 0.9% |

## 4.1 SOURCE ENCODINGS
All 108 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 29%, Data / Markup / Trivial 16%, Large Core Modules (2) 14%, Declarative / Non-Code 13%, Many-Argument Workhorses Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 102 | 94.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 5.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 64*

**Composition by Extension & Reason:**
- `.png`: 52x Excluded (Explicitly Denied Extension: '.png')
- `.build`: 4x Excluded (Unsupported Extension: '.build')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.4 | 23.5 | 10.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 88.5 | 43.5 | 50.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 23.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 14.1 | 7.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 1.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 30.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 9.5 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 74.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 194 | 28 | 8 | `contourpy-1.3.3/tests/test_typecheck.py` |
| cleanup | 8 | 3 | 0 | `contourpy-1.3.3/tests/test_config.py` |
| guards | 1369 | 63 | 38 | `contourpy-1.3.3/src/mpl2014.cpp` |
| danger | 389 | 38 | 12 | `contourpy-1.3.3/lib/contourpy/typecheck.py` |
| concurrency | 54 | 10 | 0 | `contourpy-1.3.3/src/threaded.cpp` |
| connectivity | 532 | 73 | 13 | `contourpy-1.3.3/src/base_impl.h` |
| io | 48 | 8 | 0 | `contourpy-1.3.3/.github/workflows/test.yml` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `contourpy-1.3.3/tests/test_codebase.py` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 7 | 4 | 0 | `contourpy-1.3.3/tests/test_renderer.py` |
| events | 7 | 4 | 0 | `contourpy-1.3.3/.github/workflows/build_wheels.yml` |
| tests | 817 | 22 | 21 | `contourpy-1.3.3/tests/test_filled.py` |
| docs | 103 | 14 | 2 | `contourpy-1.3.3/.github/workflows/test.yml` |
| debt | 122 | 14 | 1 | `contourpy-1.3.3/lib/contourpy/_contourpy.pyi` |
| mutation | 5897 | 84 | 163 | `contourpy-1.3.3/src/base_impl.h` |
| dead_code | 330 | 53 | 6 | `contourpy-1.3.3/src/mpl2014.cpp` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 59 | 29 | 2 | `contourpy-1.3.3/lib/contourpy/util/mpl_renderer.py` |
| ui | 15 | 1 | 0 | `contourpy-1.3.3/benchmarks/plot_benchmarks.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.6905**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `contourpy-1.3.3/.github/workflows/test.yml` (Hits: 19)
- `contourpy-1.3.3/tests/image_comparison.py` (Hits: 12)
- `contourpy-1.3.3/tests/conftest.py` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`contourpy-1.3.3/lib/contourpy/__init__.py`) — 41 inbound connections
2. **_contourpy.pyi** (`contourpy-1.3.3/lib/contourpy/_contourpy.pyi`) — 37 inbound connections
3. **bench_base.py** (`contourpy-1.3.3/benchmarks/benchmarks/bench_base.py`) — 16 inbound connections
4. **util_bench.py** (`contourpy-1.3.3/benchmarks/benchmarks/util_bench.py`) — 16 inbound connections
5. **renderer.py** (`contourpy-1.3.3/lib/contourpy/util/renderer.py`) — 12 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **bokeh_renderer.py** (`contourpy-1.3.3/lib/contourpy/util/bokeh_renderer.py`) — 19 outbound dependencies
2. **mpl_renderer.py** (`contourpy-1.3.3/lib/contourpy/util/mpl_renderer.py`) — 18 outbound dependencies
3. **test_bokeh_renderer.py** (`contourpy-1.3.3/tests/test_bokeh_renderer.py`) — 17 outbound dependencies
4. **test.yml** (`contourpy-1.3.3/.github/workflows/test.yml`) — 15 outbound dependencies
5. **test_filled.py** (`contourpy-1.3.3/tests/test_filled.py`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `BaseContourGenerator::init_cache_levels_and_starts` **(Compute Cores)** (@ `contourpy-1.3.3/src/base_impl.h`) -> Impact: **682.0** | LOC: 658
- `BaseContourGenerator::follow_interior` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/src/base_impl.h`) -> Impact: **310.7** | LOC: 311
- `Mpl2014ContourGenerator::single_quad_filled` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> Impact: **277.7** | LOC: 187
- `Mpl2014ContourGenerator::follow_interior` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> Impact: **268.4** | LOC: 149
- `contour_generator` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/lib/contourpy/__init__.py`) -> Impact: **189.5** | LOC: 198
- `Mpl2014ContourGenerator::follow_boundary` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> Impact: **188.6** | LOC: 120
- `by_name_and_type` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/benchmarks/plot_benchmarks.py`) -> Impact: **185.1** | LOC: 125
- `BaseContourGenerator::march_chunk` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/src/base_impl.h`) -> Impact: **145.6** | LOC: 211
- `zone_crosser` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/src/mpl2005_original.cpp`) -> Impact: **138.3** | LOC: 206
  * *Intent:* /* ------------------------------------------------------------------------ */ /* zone_crosser assumes you are sitting at a cut edge about to cross * ...
- `comparison_two_benchmarks` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/benchmarks/plot_benchmarks.py`) -> Impact: **114.2** | LOC: 128

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `contourpy-1.3.3/src` | 32 | 8431.02 | 23.5% | 25.75% |
| `contourpy-1.3.3/tests` | 24 | 4822.62 | 27.79% | 0.0% |
| `contourpy-1.3.3/lib/contourpy` | 10 | 1888.04 | 36.95% | 11.0% |
| `contourpy-1.3.3/lib/contourpy/util` | 9 | 1030.4 | 34.57% | 13.57% |
| `contourpy-1.3.3/benchmarks` | 4 | 764.14 | 46.17% | 0.0% |
| `contourpy-1.3.3/benchmarks/benchmarks` | 19 | 259.58 | 4.32% | 68.85% |
| `contourpy-1.3.3/.github/workflows` | 3 | 117.64 | 9.57% | 6.72% |
| `contourpy-1.3.3/.github` | 4 | 33.24 | 0.0% | 0.0% |
| `contourpy-1.3.3` | 3 | 3.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `contourpy-1.3.3/lib/contourpy/_contourpy.pyi` -> **100.0%** Exposure
- `contourpy-1.3.3/src/mpl2005.cpp` -> **99.9608%** Exposure
- `contourpy-1.3.3/src/chunk_local.cpp` -> **97.0688%** Exposure
- `contourpy-1.3.3/src/util.cpp` -> **97.0688%** Exposure
- `contourpy-1.3.3/src/mpl2014.cpp` -> **85.4551%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `contourpy-1.3.3/benchmarks/loader.py` -> **100.0%** Exposure
- `contourpy-1.3.3/benchmarks/plot_benchmarks.py` -> **100.0%** Exposure
- `contourpy-1.3.3/lib/contourpy/__init__.py` -> **100.0%** Exposure
- `contourpy-1.3.3/lib/contourpy/convert.py` -> **100.0%** Exposure
- `contourpy-1.3.3/lib/contourpy/util/bokeh_renderer.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `contourpy-1.3.3/src/mpl2014.cpp` -> **53** Orphaned Functions | **0** Duplicates
- `contourpy-1.3.3/tests/test_filled.py` -> **31** Orphaned Functions | **0** Duplicates
- `contourpy-1.3.3/tests/test_lines.py` -> **31** Orphaned Functions | **0** Duplicates
- `contourpy-1.3.3/lib/contourpy/_contourpy.pyi` -> **0** Orphaned Functions | **30** Duplicates
- `contourpy-1.3.3/tests/test_constructor.py` -> **30** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `461` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `contourpy-1.3.3/src/base_impl.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.797)
- **Top Global Matches:** file_cluster_6: 7.797, file_cluster_8: 12.857, file_cluster_4: 13.892
- **Magnitude:** 3437.54 | **LOC:** 2525 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 6.078; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BaseContourGenerator::init_cache_levels_and_starts` **(Compute Cores)** (Impact: 682.0)
  * `BaseContourGenerator::follow_interior` **(Many-Argument Workhorses)** (Impact: 310.7)
  * `BaseContourGenerator::march_chunk` **(Many-Argument Workhorses)** (Impact: 145.6)
  * `BaseContourGenerator::follow_boundary` **(Many-Argument Workhorses)** (Impact: 112.3)
  * `BaseContourGenerator::move_to_next_boundary_edge` **(Many-Argument Workhorses)** (Impact: 111.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 453 instances
* *State Mutation (weighted view):* 1371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1057`, `structural_boundaries: 235`, `args: 102`, `func_start: 55`
* *Risk/State:* `state_mutation: 465`, `fragile_debt: 6`
* *Architecture:* `api: 55`, `import: 4`
* *Defense:* `safety: 82`, `sync_locks: 4`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.078
  * `Choke Point (Betweenness):` 0.001176 | `Ripple Effect (Closeness):` 0.028037
  * `Imports (Out-Degree: 4):` base.h, converter.h, iostream, util.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/src/mpl2014.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.71)
- **Top Global Matches:** file_cluster_6: 8.71, file_cluster_8: 10.35, file_cluster_4: 16.061
- **Magnitude:** 2338.22 | **LOC:** 1711 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 4.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.4%), Debt Markers (formerly Tech Debt) (85.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Mpl2014ContourGenerator::single_quad_filled` **(Many-Argument Workhorses)** (Impact: 277.7)
  * `Mpl2014ContourGenerator::follow_interior` **(Many-Argument Workhorses)** (Impact: 268.4)
  * `Mpl2014ContourGenerator::follow_boundary` **(Many-Argument Workhorses)** (Impact: 188.6)
  * `Mpl2014ContourGenerator::init_cache_grid` **(Compute Cores)** (Impact: 96.7)
  * `Mpl2014ContourGenerator::lines` **(Compute Cores)** (Impact: 89.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 219 instances
* *State Mutation (weighted view):* 660
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 741`, `structural_boundaries: 117`, `args: 57`, `func_start: 57`
* *Risk/State:* `state_mutation: 222`, `unreferenced_by_name: 53`
* *Architecture:* `import: 3`
* *Defense:* `safety: 88`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` algorithm, mpl2014.h, mpl_kind_code.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/mpl2005_original.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.782)
- **Top Global Matches:** file_cluster_3: 7.782, file_cluster_8: 16.561, file_cluster_6: 29.504
- **Magnitude:** 1700.86 | **LOC:** 1527 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 6.018; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.7%), Complexity Load (formerly Cognitive Load) (84.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `zone_crosser` **(Many-Argument Workhorses)** (Impact: 138.3)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* zone_crosser assum...
  * `curve_tracer` **(Many-Argument Workhorses)** (Impact: 113.2)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* curve_tracer finds...
  * `edge_walker` **(Many-Argument Workhorses)** (Impact: 103.4)
    * *Intent:* /* edge_walker assumes that the current edge is being drawn CCW * around the current zone. Since onl...
  * `reorder` **(Many-Argument Workhorses)** (Impact: 99.2)
  * `data_init` **(Compute Cores)** (Impact: 93.1)
    * *Intent:* /* ------------------------------------------------------------------------ */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 322 instances
* *State Mutation (weighted view):* 985
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `structural_boundaries: 32`, `args: 18`, `func_start: 13`
* *Risk/State:* `state_mutation: 341`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `import: 2`
* *Defense:* `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.018
  * `Choke Point (Betweenness):` 0.000162 | `Ripple Effect (Closeness):` 0.009346
  * `Imports (Out-Degree: 2):` mpl2005_original.h, mpl_kind_code.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/tests/test_filled.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.257)
- **Top Global Matches:** file_cluster_5: 9.257, file_cluster_12: 9.314, file_cluster_4: 9.864
- **Magnitude:** 796.54 | **LOC:** 1045 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 4.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (31.8%), Connectivity (formerly Api Exposure) (10.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_return_by_fill_type_chunk` **(Defensive Guards)** (Impact: 77.4)
  * `test_return_by_fill_type` **(Defensive Guards)** (Impact: 48.6)
  * `test_filled_random_chunk` **(Many-Argument Workhorses)** (Impact: 18.0)
  * `test_multi_filled_invalid_levels` **(Compute Cores)** (Impact: 17.2)
  * `test_filled_random_big` **(Defensive Guards)** (Impact: 16.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 384
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 264`, `args: 41`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 188`, `unreferenced_by_name: 31`
* *Architecture:* `api: 41`, `import: 52`
* *Defense:* `safety: 124`, `test: 128`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .image_comparison, .util_test, __future__, contourpy, contourpy._contourpy, contourpy.util.data, contourpy.util.mpl_renderer, functools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/util_config.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.54)
- **Top Global Matches:** file_cluster_6: 8.54, file_cluster_4: 13.897, file_cluster_8: 14.352
- **Magnitude:** 773.1 | **LOC:** 602 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 5.42; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (47.3%), Connectivity (formerly Api Exposure) (26.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 98.2)
  * `_next_quad` **(Many-Argument Workhorses)** (Impact: 89.5)
  * `_quad_lines` **(Many-Argument Workhorses)** (Impact: 81.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `_decode_config` **(Stateful Encapsulated Methods)** (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 324
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 71`, `args: 21`, `func_start: 21`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 136`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 13`, `import: 13`
* *Defense:* `safety: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.42
  * `Choke Point (Betweenness):` 0.000397 | `Ripple Effect (Closeness):` 0.009346
  * `Imports (Out-Degree: 2):` __future__, abc, collections.abc, contourpy, contourpy._contourpy, enum, io, matplotlib...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/lib/contourpy/convert.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 13.071)
- **Top Global Matches:** file_cluster_3: 13.071, file_cluster_8: 20.231, file_cluster_6: 31.9
- **Magnitude:** 710.78 | **LOC:** 622 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 17.159; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_convert_filled_from_ChunkCombinedOffsetOffset` **(Defensive Guards)** (Impact: 46.6)
  * `_convert_filled_from_ChunkCombinedCodeOffset` **(Defensive Guards)** (Impact: 42.7)
  * `_convert_lines_from_ChunkCombinedCode` **(Stateful Encapsulated Methods)** (Impact: 38.3)
  * `_convert_lines_from_ChunkCombinedOffset` **(Stateful Encapsulated Methods)** (Impact: 36.6)
  * `_convert_lines_from_ChunkCombinedNan` **(Stateful Encapsulated Methods)** (Impact: 31.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 96 instances
* *State Mutation (weighted view):* 293
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 122`, `args: 15`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 101`
* *Architecture:* `api: 4`, `import: 10`
* *Defense:* `safety: 19`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.159
  * `Choke Point (Betweenness):` 0.006427 | `Ripple Effect (Closeness):` 0.217314
  * `Imports (Out-Degree: 5):` __future__, contourpy._contourpy, contourpy.array, contourpy.enum_util, contourpy.typecheck, contourpy.types, itertools, numpy...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/benchmarks/plot_benchmarks.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.321)
- **Top Global Matches:** file_cluster_8: 10.321, file_cluster_6: 11.732, file_cluster_4: 19.244
- **Magnitude:** 598.38 | **LOC:** 340 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 4.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.7%), Guard Balance (formerly Safety Score) (87.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 55.6% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `by_name_and_type` **(Many-Argument Workhorses)** (Impact: 185.1)
  * `comparison_two_benchmarks` **(Many-Argument Workhorses)** (Impact: 114.2)
  * `main` **(I/O & Config Routines)** (Impact: 9.9)
  * `get_corner_mask_label` **(Generic / Templated Code)** (Impact: 4.5)
  * `in_bar_label` **(Generic / Templated Code)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 35`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 95`
* *Architecture:* `api: 8`, `import: 10`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, asv.util, contourpy, loader, matplotlib.axes, matplotlib.patches, matplotlib.pyplot, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_lines.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.169)
- **Top Global Matches:** file_cluster_5: 8.169, file_cluster_12: 8.662, file_cluster_0: 9.8
- **Magnitude:** 561.88 | **LOC:** 878 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 4.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.7%), Complexity Load (formerly Cognitive Load) (42.6%), Connectivity (formerly Api Exposure) (10.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_return_by_line_type_chunk` **(Many-Argument Workhorses)** (Impact: 51.0)
  * `test_return_by_line_type` **(Defensive Guards)** (Impact: 27.0)
  * `test_multi_lines_levels_type` **(Many-Argument Workhorses)** (Impact: 13.5)
  * `test_e_to_w` **(Defensive Guards)** (Impact: 12.9)
  * `test_lines_random_big` **(Defensive Guards)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 251`, `args: 35`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 146`, `unreferenced_by_name: 31`
* *Architecture:* `api: 35`, `import: 49`
* *Defense:* `safety: 125`, `test: 122`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .image_comparison, .util_test, __future__, contourpy, contourpy._contourpy, contourpy.util.data, contourpy.util.mpl_renderer, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/lib/contourpy/util/mpl_renderer.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.225)
- **Top Global Matches:** file_cluster_5: 7.225, file_cluster_12: 7.731, file_cluster_0: 9.056
- **Magnitude:** 416.62 | **LOC:** 536 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **18**; blast radius 10.155; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.9%), Connectivity (formerly Api Exposure) (51.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 78.9474% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filled` **(Many-Argument Workhorses)** (Impact: 51.1)
  * `lines` **(Many-Argument Workhorses)** (Impact: 41.7)
  * `z_levels` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `z_values` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 18.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 66`, `args: 21`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 64`
* *Architecture:* `api: 18`, `import: 18`
* *Defense:* `safety: 2`, `doc: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.155
  * `Choke Point (Betweenness):` 0.002689 | `Ripple Effect (Closeness):` 0.084112
  * `Imports (Out-Degree: 6):` __future__, collections.abc, contourpy, contourpy._contourpy, contourpy.convert, contourpy.enum_util, contourpy.util.mpl_util, contourpy.util.renderer...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/tests/util_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 12.391)
- **Top Global Matches:** file_cluster_5: 12.391, file_cluster_4: 12.952, file_cluster_6: 14.318
- **Magnitude:** 291.66 | **LOC:** 342 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **8**; blast radius 14.043; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (75.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (43.3%), Guard Balance (formerly Safety Score) (37.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_filled` **(Defensive Guards)** (Impact: 77.5)
  * `assert_lines` **(Defensive Guards)** (Impact: 51.5)
  * `assert_equal_recursive` **(Defensive Guards)** (Impact: 14.7)
  * `sort_by_first_xy` **(Generic / Templated Code)** (Impact: 10.9)
  * `assert_point_array` **(Defensive Guards)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 129`, `args: 20`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 29`
* *Architecture:* `api: 19`, `import: 8`
* *Defense:* `safety: 113`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.043
  * `Choke Point (Betweenness):` 0.001705 | `Ripple Effect (Closeness):` 0.093458
  * `Imports (Out-Degree: 3):` __future__, contourpy, contourpy._contourpy, contourpy.types, numpy, numpy.testing, numpy.typing, typing
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/lib/contourpy/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.16)
- **Top Global Matches:** file_cluster_3: 9.16, file_cluster_8: 21.39, file_cluster_6: 33.879
- **Magnitude:** 271.66 | **LOC:** 286 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **41** in-repo importer(s); it depends on **11**; blast radius 70.021; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (72.6%), Guard Balance (formerly Safety Score) (72.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `contour_generator` **(Many-Argument Workhorses)** (Impact: 189.5)
  * `_remove_z_mask` **(Stateful Encapsulated Methods)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 31`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 24`, `planned_debt: 1`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 70.021
  * `Choke Point (Betweenness):` 0.026552 | `Ripple Effect (Closeness):` 0.389526
  * `Imports (Out-Degree: 6):` ._contourpy, __future__, contourpy._contourpy, contourpy._version, contourpy.chunk, contourpy.convert, contourpy.dechunk, contourpy.enum_util...
  * `Imported By (In-Degree: 41):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/tests/test_renderer.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.988)
- **Top Global Matches:** file_cluster_8: 8.988, file_cluster_6: 18.425, file_cluster_3: 20.651
- **Magnitude:** 264.36 | **LOC:** 230 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 4.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (69.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (38.5%), Connectivity (formerly Api Exposure) (7.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_renderer_lines` **(Many-Argument Workhorses)** (Impact: 44.8)
  * `test_renderer_filled` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `test_debug_renderer_lines` **(Many-Argument Workhorses)** (Impact: 15.3)
  * `test_debug_renderer_filled` **(Many-Argument Workhorses)** (Impact: 13.3)
  * `test_save_svg` **(Defensive Guards)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 54`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 45`, `unreferenced_by_name: 6`
* *Architecture:* `io: 2`, `api: 6`, `import: 19`
* *Defense:* `safety: 8`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .image_comparison, PIL, __future__, _pytest._py.path, contourpy, contourpy.util.data, contourpy.util.mpl_renderer, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/lib/contourpy/typecheck.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 14.064)
- **Top Global Matches:** file_cluster_8: 14.064, file_cluster_6: 21.418, file_cluster_3: 23.148
- **Magnitude:** 262.96 | **LOC:** 204 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 15.93; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.4%), Complexity Load (formerly Cognitive Load) (75.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_filled` **(Compute Cores)** (Impact: 101.0)
  * `check_lines` **(Compute Cores)** (Impact: 59.8)
  * `_check_tuple_of_lists_with_same_length` **(Stateful Encapsulated Methods)** (Impact: 18.9)
  * `check_code_array` **(Defensive Guards)** (Impact: 8.9)
    * *Intent:* # Minimalist array-checking functions that check dtype, ndims and shape only. # They do not walk the...
  * `check_offset_array` **(Defensive Guards)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 27`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 16`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.93
  * `Choke Point (Betweenness):` 0.001411 | `Ripple Effect (Closeness):` 0.161288
  * `Imports (Out-Degree: 4):` __future__, contourpy, contourpy._contourpy, contourpy.enum_util, contourpy.types, numpy, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/tests/test_constructor.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.167)
- **Top Global Matches:** file_cluster_0: 6.167, file_cluster_13: 9.713, file_cluster_15: 10.738
- **Magnitude:** 246.06 | **LOC:** 420 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 4.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (37.4%), Complexity Load (formerly Cognitive Load) (17.5%), Connectivity (formerly Api Exposure) (11.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_chunk_size_2d` **(Defensive Guards)** (Impact: 12.3)
  * `test_thread_count` **(Defensive Guards)** (Impact: 8.9)
  * `test_chunk_size_and_count` **(Generic / Templated Code)** (Impact: 7.6)
  * `test_chunk_size_negative` **(Generic / Templated Code)** (Impact: 7.4)
  * `test_chunk_size_1d` **(Defensive Guards)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 118`, `args: 32`, `func_start: 32`
* *Risk/State:* `state_mutation: 47`, `unreferenced_by_name: 30`
* *Architecture:* `api: 32`, `import: 9`
* *Defense:* `safety: 43`, `test: 98`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .util_test, __future__, contourpy, contourpy._contourpy, math, numpy, numpy.typing, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/lib/contourpy/util/bokeh_renderer.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.046)
- **Top Global Matches:** file_cluster_5: 7.046, file_cluster_12: 7.706, file_cluster_0: 8.679
- **Magnitude:** 227.62 | **LOC:** 340 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 4.941; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (84.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.7%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `z_values` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 14.6)
  * `save` **(Many-Argument Workhorses)** (Impact: 12.6)
  * `grid` **(Many-Argument Workhorses)** (Impact: 11.6)
  * `lines` **(Many-Argument Workhorses)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 57`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 46`, `unreferenced_by_name: 8`
* *Architecture:* `api: 10`, `import: 20`
* *Defense:* `safety: 3`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.941
  * `Choke Point (Betweenness):` 0.000184 | `Ripple Effect (Closeness):` 0.009346
  * `Imports (Out-Degree: 5):` __future__, bokeh.core.enums, bokeh.io, bokeh.io.export, bokeh.layouts, bokeh.models, bokeh.models.annotations.labels, bokeh.palettes...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/tests/test_dechunk.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.205)
- **Top Global Matches:** file_cluster_5: 8.205, file_cluster_12: 9.041, file_cluster_7: 9.885
- **Magnitude:** 222.5 | **LOC:** 226 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 4.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (36.3%), Connectivity (formerly Api Exposure) (7.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_dechunk_filled` **(Defensive Guards)** (Impact: 32.8)
  * `test_dechunk_lines` **(Defensive Guards)** (Impact: 28.4)
  * `test_dechunk_lines_empty` **(Defensive Guards)** (Impact: 12.8)
  * `test_dechunk_multi_filled` **(Defensive Guards)** (Impact: 10.9)
  * `test_dechunk_multi_lines` **(Defensive Guards)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 58`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 39`, `unreferenced_by_name: 6`
* *Architecture:* `api: 6`, `import: 8`
* *Defense:* `safety: 39`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .util_test, __future__, contourpy, contourpy._contourpy, numpy, numpy.testing, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/threaded.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.305)
- **Top Global Matches:** file_cluster_8: 6.305, file_cluster_6: 12.848, file_cluster_4: 21.371
- **Magnitude:** 221.04 | **LOC:** 317 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 4.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ThreadedContourGenerator::export_filled` **(Many-Argument Workhorses)** (Impact: 45.2)
  * `ThreadedContourGenerator::export_lines` **(Many-Argument Workhorses)** (Impact: 37.3)
  * `ThreadedContourGenerator::thread_function` **(Compute Cores)** (Impact: 18.3)
  * `ThreadedContourGenerator::limit_n_threads` **(Type Conversions)** (Impact: 5.6)
  * `ThreadedContourGenerator::march` **(Compute Cores)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 27`, `args: 8`, `func_start: 7`
* *Risk/State:* `state_mutation: 29`, `unreferenced_by_name: 6`
* *Architecture:* `concurrency: 4`, `import: 5`
* *Defense:* `safety: 17`, `sync_locks: 16`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` base_impl.h, converter.h, thread, threaded.h, util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_array.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.519)
- **Top Global Matches:** file_cluster_0: 7.519, file_cluster_15: 8.011, file_cluster_2: 8.308
- **Magnitude:** 205.98 | **LOC:** 575 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 4.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.5%), Complexity Load (formerly Cognitive Load) (13.5%), Connectivity (formerly Api Exposure) (9.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_codes_from_offsets_and_points` **(I/O & Config Routines)** (Impact: 11.2)
  * `test_insert_nan_at_offsets` **(I/O & Config Routines)** (Impact: 11.2)
  * `test_split_codes_by_offsets` **(Defensive Guards)** (Impact: 6.4)
  * `test_split_points_at_nan` **(Defensive Guards)** (Impact: 6.4)
  * `test_split_points_by_offsets` **(Defensive Guards)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 131`, `args: 20`, `func_start: 20`
* *Risk/State:* `state_mutation: 85`, `unreferenced_by_name: 20`
* *Architecture:* `api: 20`, `import: 7`
* *Defense:* `safety: 41`, `test: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .util_test, __future__, contourpy.array, contourpy.types, numpy, numpy.testing, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_typecheck.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.374)
- **Top Global Matches:** file_cluster_6: 10.374, file_cluster_4: 12.197, file_cluster_9: 16.713
- **Magnitude:** 195.62 | **LOC:** 389 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 4.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (35.8%), Complexity Load (formerly Cognitive Load) (16.9%), Connectivity (formerly Api Exposure) (9.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_check_filled_ChunkCombinedOffsetOffset` **(I/O & Config Routines)** (Impact: 18.2)
    * *Intent:* # Valid filled, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]], ...
  * `test_check_filled_ChunkCombinedCodeOffset` **(I/O & Config Routines)** (Impact: 18.1)
    * *Intent:* # Valid filled, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]], ...
  * `test_check_filled_ChunkCombinedCode` **(I/O & Config Routines)** (Impact: 13.6)
    * *Intent:* # Valid filled, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6]], dtype=point_...
  * `test_check_filled_ChunkCombinedOffset` **(I/O & Config Routines)** (Impact: 13.6)
    * *Intent:* # Valid filled, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]], ...
  * `test_check_lines_ChunkCombinedCode` **(I/O & Config Routines)** (Impact: 13.6)
    * *Intent:* # Valid lines, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]], d...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 178`, `args: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 22`, `unreferenced_by_name: 14`
* *Architecture:* `api: 14`, `import: 6`
* *Defense:* `test: 120`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, contourpy, contourpy.typecheck, contourpy.types, numpy, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/lib/contourpy/array.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.312)
- **Top Global Matches:** file_cluster_0: 5.312, file_cluster_15: 10.214, file_cluster_13: 10.342
- **Magnitude:** 185.7 | **LOC:** 262 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **7**; blast radius 14.334; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.2%), Guard Balance (formerly Safety Score) (65.5%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `concat_points_with_nan` **(Generic / Templated Code)** (Impact: 7.7)
    * *Intent:* """Concatenate a list of points into a single point array with NaNs used to separate each line. """
  * `concat_offsets_or_none` **(Generic / Templated Code)** (Impact: 7.6)
  * `concat_points_or_none` **(Generic / Templated Code)** (Impact: 7.6)
  * `concat_points_or_none_with_nan` **(Generic / Templated Code)** (Impact: 7.6)
  * `concat_codes_or_none` **(Generic / Templated Code)** (Impact: 7.5)
    * *Intent:* """Concatenate a list of codes arrays or None into a single code array or None. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 64`, `args: 20`, `func_start: 20`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 20`, `import: 7`
* *Defense:* `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.334
  * `Choke Point (Betweenness):` 0.000517 | `Ripple Effect (Closeness):` 0.161288
  * `Imports (Out-Degree: 3):` __future__, contourpy._contourpy, contourpy.typecheck, contourpy.types, itertools, numpy, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/tests/test_minimal.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 18.883)
- **Top Global Matches:** file_cluster_3: 18.883, file_cluster_1: 35.438, file_cluster_8: 38.286
- **Magnitude:** 180.54 | **LOC:** 181 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 4.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (78.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (36.6%), Connectivity (formerly Api Exposure) (4.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_minimal_filled` **(Many-Argument Workhorses)** (Impact: 44.1)
  * `test_minimal_lines` **(Many-Argument Workhorses)** (Impact: 39.2)
  * `z` **(Generic / Templated Code)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 24`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 33`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `safety: 7`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .util_test, __future__, contourpy, contourpy._contourpy, numpy, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_internal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.411)
- **Top Global Matches:** file_cluster_0: 6.411, file_cluster_5: 9.363, file_cluster_12: 9.874
- **Magnitude:** 175.6 | **LOC:** 209 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 4.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (33.4%), Connectivity (formerly Api Exposure) (9.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_xyz_ndim` **(Compute Cores)** (Impact: 14.9)
  * `test_xyz_shape` **(Generic / Templated Code)** (Impact: 9.3)
  * `default_kwargs` **(Generic / Templated Code)** (Impact: 8.1)
  * `test_chunk_size_not_negative` **(Generic / Templated Code)** (Impact: 7.6)
  * `test_xy_at_least_2x2` **(Generic / Templated Code)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 63`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 12`, `import: 7`
* *Defense:* `safety: 2`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, contourpy._contourpy, io, pytest, sys, typing, wurlitzer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_bokeh_renderer.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.871)
- **Top Global Matches:** file_cluster_0: 7.871, file_cluster_13: 9.259, file_cluster_15: 9.272
- **Magnitude:** 167.34 | **LOC:** 197 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 4.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (34.4%), Connectivity (formerly Api Exposure) (7.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_renderer_lines_bokeh` **(Many-Argument Workhorses)** (Impact: 31.1)
  * `test_renderer_filled_bokeh` **(Many-Argument Workhorses)** (Impact: 31.0)
  * `test_save_svg` **(Defensive Guards)** (Impact: 7.7)
  * `driver` **(Generic / Templated Code)** (Impact: 5.3)
    * *Intent:* # Based on Bokeh's tests/support/plugins/selenium.py def chrome() -> WebDriver: from selenium.webdri...
  * `chrome` **(Interface Declarations)** (Impact: 3.7)
    * *Intent:* # Based on Bokeh's tests/support/plugins/selenium.py
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 55`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 28`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 7`, `import: 18`
* *Defense:* `safety: 7`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .image_comparison, PIL, __future__, _pytest._py.path, _pytest.logging, collections.abc, contourpy, contourpy.util.data...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/lib/contourpy/dechunk.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 13.747)
- **Top Global Matches:** file_cluster_8: 13.747, file_cluster_6: 14.846, file_cluster_4: 21.448
- **Magnitude:** 163.1 | **LOC:** 208 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 16.618; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (51.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dechunk_filled` **(Many-Argument Workhorses)** (Impact: 39.8)
    * *Intent:* """Return the specified filled contours with chunked data moved into the first chunk. Filled contour...
  * `dechunk_lines` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* """Return the specified contour lines with chunked data moved into the first chunk. Contour lines th...
  * `dechunk_multi_filled` **(Generic / Templated Code)** (Impact: 6.6)
  * `dechunk_multi_lines` **(Generic / Templated Code)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 33`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 25`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.618
  * `Choke Point (Betweenness):` 0.003349 | `Ripple Effect (Closeness):` 0.217314
  * `Imports (Out-Degree: 4):` __future__, contourpy._contourpy, contourpy.array, contourpy.enum_util, contourpy.typecheck, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/benchmarks/loader.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 11.811)
- **Top Global Matches:** file_cluster_6: 11.811, file_cluster_8: 15.704, file_cluster_4: 16.762
- **Magnitude:** 149.24 | **LOC:** 102 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 6.018; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.0%), Guard Balance (formerly Safety Score) (83.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 55.6% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 13.0)
  * `_find_benchmark_by_name` **(Encapsulated Accessors)** (Impact: 5.4)
  * `commit` **(Generic / Templated Code)** (Impact: 1.5)
  * `machine` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 35`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 27`
* *Architecture:* `api: 5`, `import: 12`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.018
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.009346
  * `Imports (Out-Degree: 2):` __future__, asv.benchmark, asv.benchmarks, asv.config, asv.results, asv_runner.statistics, contourpy, copy...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `contourpy-1.3.3/lib/contourpy/util/_build_config.py.in` (PYTHON) | Magnitude: 4.2 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, core_var_decl: 31, design_snake_case: 31, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `contourpy-1.3.3/tests/test_filled.py` (PYTHON) | Magnitude: 796.54 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 682, structural_boundaries: 264, core_var_decl: 264, design_snake_case: 264

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `contourpy-1.3.3/lib/contourpy/__init__.py` -> **Severity: 2.655** (Bridge: 0.0266 * Flux: 100.0%)
- `contourpy-1.3.3/lib/contourpy/convert.py` -> **Severity: 0.643** (Bridge: 0.0064 * Flux: 100.0%)
- `contourpy-1.3.3/lib/contourpy/dechunk.py` -> **Severity: 0.335** (Bridge: 0.0033 * Flux: 100.0%)
- `contourpy-1.3.3/lib/contourpy/util/mpl_renderer.py` -> **Severity: 0.269** (Bridge: 0.0027 * Flux: 100.0%)
- `contourpy-1.3.3/benchmarks/benchmarks/bench_base.py` -> **Severity: 0.141** (Bridge: 0.0014 * Flux: 99.9932%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `contourpy-1.3.3/lib/contourpy/__init__.py` -> **Severity: 28.079** (Embedded: 0.3895 * Error Risk: 72.084%)
- `contourpy-1.3.3/lib/contourpy/dechunk.py` -> **Severity: 18.09** (Embedded: 0.2173 * Error Risk: 83.2448%)
- `contourpy-1.3.3/lib/contourpy/convert.py` -> **Severity: 17.465** (Embedded: 0.2173 * Error Risk: 80.3662%)
- `contourpy-1.3.3/lib/contourpy/chunk.py` -> **Severity: 16.494** (Embedded: 0.22 * Error Risk: 74.9753%)
- `contourpy-1.3.3/lib/contourpy/typecheck.py` -> **Severity: 12.33** (Embedded: 0.1613 * Error Risk: 76.4481%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `contourpy-1.3.3/lib/contourpy/_contourpy.pyi` -> **Severity: 12478.0** (Blast Radius: 124.78 * Doc Risk: 100.0%)
- `contourpy-1.3.3/lib/contourpy/__init__.py` -> **Severity: 7002.1** (Blast Radius: 70.021 * Doc Risk: 100.0%)
- `contourpy-1.3.3/lib/contourpy/util/data.py` -> **Severity: 2144.2** (Blast Radius: 21.442 * Doc Risk: 100.0%)
- `contourpy-1.3.3/benchmarks/benchmarks/bench_base.py` -> **Severity: 1750.5** (Blast Radius: 17.505 * Doc Risk: 100.0%)
- `contourpy-1.3.3/benchmarks/benchmarks/util_bench.py` -> **Severity: 1750.5** (Blast Radius: 17.505 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2684 call pairs -- scoped 38.9%, unique 0.2%, ambiguous 1.9%, external 59.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 2018 | 44.1% | 0.0% | 1.5% | 54.4% |
| cpp | 666 | 23.0% | 0.8% | 3.3% | 73.0% |

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
