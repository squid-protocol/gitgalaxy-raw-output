# ARCHITECTURAL_BRIEF: alembic
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
- **Scope:** 124 analyzed artifact(s), 43104 LOC.
- **Load-bearing artifact:** `alembic-1.18.4/alembic/util/__init__.py` -- 47 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `alembic-1.18.4/alembic/ddl/postgresql.py` -- pulls in 27 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `alembic-1.18.4/alembic/script/revision.py` at magnitude 1354.12 (structural weight, not risk).
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
| Total Artifacts | 144 |
| Analyzed Artifacts (Scanned) | 124 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 20 |
| Total LOC | 43104 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 86.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3258 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.126 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 37.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0733 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 117 | 43104 | 94.4% |
| MARKDOWN | 5 | 0 | 4.0% |
| PLAINTEXT | 2 | 0 | 1.6% |

## 4.1 SOURCE ENCODINGS
All 124 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 23%, Parameter Forwarders Files 23%, Data / Markup / Trivial 18%, Large Core Modules (3) 13%, Large Core Modules 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 117 | 94.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7 | 5.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 20*

**Composition by Extension & Reason:**
- `.mako`: 12x Excluded (Unsupported Extension: '.mako')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.7 | 26.0 | 19.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 85.0 | 54.0 | 56.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 39.5 | 2.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 87.4 | 27.3 | 13.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 39.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 18.4 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 70.5 | 91.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 457 | 59 | 11 | `alembic-1.18.4/alembic/script/revision.py` |
| cleanup | 15 | 11 | 0 | `alembic-1.18.4/tests/test_command.py` |
| guards | 1300 | 84 | 24 | `alembic-1.18.4/alembic/script/revision.py` |
| danger | 1013 | 78 | 24 | `alembic-1.18.4/alembic/operations/ops.py` |
| concurrency | 121 | 30 | 4 | `alembic-1.18.4/alembic/testing/fixtures.py` |
| connectivity | 3226 | 99 | 69 | `alembic-1.18.4/tests/test_autogen_render.py` |
| io | 1092 | 88 | 22 | `alembic-1.18.4/tests/test_script_production.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 10 | 4 | 0 | `alembic-1.18.4/alembic/script/write_hooks.py` |
| time | 24 | 3 | 0 | `alembic-1.18.4/tests/test_script_production.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 111 | 27 | 4 | `alembic-1.18.4/tests/test_autogen_render.py` |
| events | 20 | 7 | 0 | `alembic-1.18.4/tests/test_config.py` |
| tests | 1926 | 43 | 57 | `alembic-1.18.4/tests/test_batch.py` |
| docs | 844 | 72 | 23 | `alembic-1.18.4/alembic/runtime/environment.py` |
| debt | 203 | 42 | 5 | `alembic-1.18.4/tests/test_command.py` |
| mutation | 13651 | 100 | 287 | `alembic-1.18.4/tests/test_autogen_render.py` |
| dead_code | 1240 | 32 | 32 | `alembic-1.18.4/tests/test_autogen_render.py` |
| credential | 1 | 1 | 0 | `alembic-1.18.4/tests/test_autogen_render.py` |
| threat | 1 | 1 | 0 | `alembic-1.18.4/tests/test_autogen_render.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 103 | 8 | 0 | `alembic-1.18.4/tests/test_autogen_render.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.697**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `alembic-1.18.4/tests/test_script_production.py` (Hits: 63)
- `alembic-1.18.4/tests/test_command.py` (Hits: 44)
- `alembic-1.18.4/tests/test_autogen_diffs.py` (Hits: 41)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`alembic-1.18.4/alembic/util/__init__.py`) — 47 inbound connections
2. **__init__.py** (`alembic-1.18.4/alembic/testing/__init__.py`) — 40 inbound connections
3. **__init__.py** (`alembic-1.18.4/alembic/__init__.py`) — 36 inbound connections
4. **assertions.py** (`alembic-1.18.4/alembic/testing/assertions.py`) — 30 inbound connections
5. **fixtures.py** (`alembic-1.18.4/alembic/testing/fixtures.py`) — 28 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **postgresql.py** (`alembic-1.18.4/alembic/ddl/postgresql.py`) — 27 outbound dependencies
2. **base.py** (`alembic-1.18.4/alembic/operations/base.py`) — 23 outbound dependencies
3. **fixtures.py** (`alembic-1.18.4/alembic/testing/fixtures.py`) — 22 outbound dependencies
4. **write_pyi.py** (`alembic-1.18.4/tools/write_pyi.py`) — 22 outbound dependencies
5. **api.py** (`alembic-1.18.4/alembic/autogenerate/api.py`) — 19 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_compare_indexes_and_uniques` **(Many-Argument Workhorses)** (@ `alembic-1.18.4/alembic/autogenerate/compare/constraints.py`) -> Impact: **236.4** | LOC: 389
- `alter_column` **(Many-Argument Workhorses)** (@ `alembic-1.18.4/alembic/ddl/mysql.py`) -> Impact: **170.9** | LOC: 119
- `_generate_stub_for_meth` **(Many-Argument Workhorses)** (@ `alembic-1.18.4/tools/write_pyi.py`) -> Impact: **129.2** | LOC: 123
- `generate_revision` **(Many-Argument Workhorses)** (@ `alembic-1.18.4/alembic/script/base.py`) -> Impact: **123.6** | LOC: 151
- `tox_parameters` **(Many-Argument Workhorses)** (@ `alembic-1.18.4/tools/toxnox.py`) -> Impact: **108.0** | LOC: 151
- `_compare_foreign_keys` **(Many-Argument Workhorses)** (@ `alembic-1.18.4/alembic/autogenerate/compare/constraints.py`) -> Impact: **104.1** | LOC: 125
- `configure` **(Many-Argument Workhorses)** (@ `alembic-1.18.4/alembic/runtime/environment.py`) -> Impact: **80.7** | LOC: 532
- `alter_column` **(Many-Argument Workhorses)** (@ `alembic-1.18.4/alembic/ddl/mssql.py`) -> Impact: **77.2** | LOC: 102
- `_recur_param` **(Many-Argument Workhorses)** (@ `alembic-1.18.4/tools/toxnox.py`) -> Impact: **65.7** | LOC: 74
- `init` **(Many-Argument Workhorses)** (@ `alembic-1.18.4/alembic/command.py`) -> Impact: **65.6** | LOC: 150

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `alembic-1.18.4/tests` | 35 | 12237.08 | 13.18% | 0.0% |
| `alembic-1.18.4/alembic/ddl` | 9 | 2712.1 | 36.54% | 7.48% |
| `alembic-1.18.4/alembic/operations` | 6 | 2554.22 | 49.35% | 6.94% |
| `alembic-1.18.4/alembic/script` | 4 | 2302.84 | 44.79% | 2.86% |
| `alembic-1.18.4/alembic/autogenerate/compare` | 8 | 1728.3 | 48.91% | 1.02% |
| `alembic-1.18.4/alembic/autogenerate` | 4 | 1567.66 | 47.08% | 2.09% |
| `alembic-1.18.4/alembic` | 10 | 1308.06 | 7.69% | 2.68% |
| `alembic-1.18.4/alembic/runtime` | 4 | 1140.12 | 31.93% | 2.0% |
| `alembic-1.18.4/alembic/testing/suite` | 9 | 1093.6 | 13.62% | 0.0% |
| `alembic-1.18.4/alembic/util` | 8 | 1060.3 | 39.44% | 5.48% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `alembic-1.18.4/alembic/ddl/_autogen.py` -> **39.5247%** Exposure
- `alembic-1.18.4/alembic/util/compat.py` -> **32.4034%** Exposure
- `alembic-1.18.4/noxfile.py` -> **27.657%** Exposure
- `alembic-1.18.4/alembic/command.py` -> **17.6491%** Exposure
- `alembic-1.18.4/alembic/operations/ops.py` -> **12.0649%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `alembic-1.18.4/alembic/autogenerate/compare/tables.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/autogenerate/render.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/operations/batch.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/operations/schemaobj.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/templates/multidb/env.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `alembic-1.18.4/tests/test_autogen_render.py` -> **153** Orphaned Functions | **3** Duplicates
- `alembic-1.18.4/tests/test_revision.py` -> **123** Orphaned Functions | **0** Duplicates
- `alembic-1.18.4/tests/test_batch.py` -> **100** Orphaned Functions | **12** Duplicates
- `alembic-1.18.4/tests/test_postgresql.py` -> **108** Orphaned Functions | **4** Duplicates
- `alembic-1.18.4/tests/test_command.py` -> **96** Orphaned Functions | **15** Duplicates

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
- **Unknown Dependencies:** `806` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `alembic-1.18.4/alembic/script/revision.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.441)
- **Top Global Matches:** file_cluster_4: 9.441, file_cluster_6: 9.813, file_cluster_5: 14.578
- **Magnitude:** 1354.12 | **LOC:** 1729 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **6**; blast radius 15.997; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (68.0%), Guard Balance (formerly Safety Score) (66.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 75.2688% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parse_downgrade_target` **(Many-Argument Workhorses)** (Impact: 64.1)
  * `_parse_upgrade_target` **(Many-Argument Workhorses)** (Impact: 61.4)
  * `_collect_upgrade_revisions` **(Many-Argument Workhorses)** (Impact: 60.6)
  * `_collect_downgrade_revisions` **(Many-Argument Workhorses)** (Impact: 58.0)
  * `_walk` **(Many-Argument Workhorses)** (Impact: 52.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 141 instances
* *State Mutation (weighted view):* 461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 226`, `args: 69`, `func_start: 65`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 179`, `planned_debt: 11`
* *Architecture:* `io: 1`, `api: 37`, `import: 26`
* *Defense:* `safety: 38`, `doc: 33`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.997
  * `Choke Point (Betweenness):` 0.003668 | `Ripple Effect (Closeness):` 0.322704
  * `Imports (Out-Degree: 3):` ..util, __future__, collections, re, sqlalchemy, typing
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_autogen_diffs.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.284)
- **Top Global Matches:** file_cluster_12: 6.284, file_cluster_15: 7.228, file_cluster_16: 7.796
- **Magnitude:** 1246.4 | **LOC:** 2686 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 2.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (63.2%), Guard Balance (formerly Safety Score) (58.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (18.9%)
- **Documentation Coverage:** 90.5882% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_drop_fk_with_mixed_case_name` **(Many-Argument Workhorses)** (Impact: 30.2)
    * *Intent:* """Test #1743"""
  * `test_include_object` **(Defensive Guards)** (Impact: 22.3)
  * `include_object` **(Defensive Guards)** (Impact: 20.4)
  * `test_include_name` **(Compute Cores)** (Impact: 17.5)
  * `test_compare_metadata_include_name` **(Compute Cores)** (Impact: 15.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 411
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 406`, `args: 138`, `func_start: 138`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 303`, `planned_debt: 2`, `duplicate_logic: 8`
* *Architecture:* `io: 41`, `api: 148`, `import: 67`
* *Defense:* `safety: 17`, `doc: 16`, `test: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` alembic, alembic.autogenerate, alembic.autogenerate.compare.tables, alembic.autogenerate.compare.types, alembic.autogenerate.compare.util, alembic.ddl, alembic.migration, alembic.operations...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/autogenerate/render.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.715)
- **Top Global Matches:** file_cluster_4: 8.715, file_cluster_5: 11.039, file_cluster_12: 11.598
- **Magnitude:** 1125.72 | **LOC:** 1173 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **17**; blast radius 13.663; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%), Complexity Load (formerly Cognitive Load) (72.7%)
- **Documentation Coverage:** 98.7342% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_repr_type` **(Stateful Encapsulated Methods)** (Impact: 40.1)
  * `_alter_column` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `_uq_constraint` **(Stateful Encapsulated Methods)** (Impact: 32.1)
  * `_add_table` **(Many-Argument Workhorses)** (Impact: 30.5)
  * `_render_column` **(Many-Argument Workhorses)** (Impact: 30.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 495
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 235`, `args: 50`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 183`, `planned_debt: 2`
* *Architecture:* `io: 30`, `api: 26`, `import: 43`
* *Defense:* `safety: 20`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.663
  * `Choke Point (Betweenness):` 0.004569 | `Ripple Effect (Closeness):` 0.248308
  * `Imports (Out-Degree: 8):` ..operations, ..util, __future__, alembic.autogenerate.api, alembic.config, alembic.operations.ops, io, mako.pygen...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_autogen_render.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.707)
- **Top Global Matches:** file_cluster_15: 5.707, file_cluster_11: 7.836, file_cluster_2: 7.862
- **Magnitude:** 1114.88 | **LOC:** 2723 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 2.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (14.7%), Connectivity (formerly Api Exposure) (13.0%)
- **Documentation Coverage:** 83.6364% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_repr_custom_type` **(Many-Argument Workhorses)** (Impact: 19.6)
    * *Intent:* """test #1167 as well as other user defined type variations"""
  * `render` **(Defensive Guards)** (Impact: 16.8)
  * `test_render_custom` **(Compute Cores)** (Impact: 13.7)
  * `test_render_create_table_comment_op_batch` **(Compute Cores)** (Impact: 13.6)
    * *Intent:* """test #1361"""
  * `test_render_drop_table_comment_op_batch` **(Compute Cores)** (Impact: 13.5)
    * *Intent:* """test #1361"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 439
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 324`, `args: 169`, `func_start: 166`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 399`, `duplicate_logic: 3`, `unreferenced_by_name: 153`
* *Architecture:* `io: 39`, `api: 174`, `import: 54`
* *Defense:* `safety: 4`, `doc: 28`, `test: 157`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` alembic, alembic.autogenerate, alembic.migration, alembic.operations, alembic.testing, alembic.testing.fixtures, alembic.util, mypackage...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/test_batch.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.231)
- **Top Global Matches:** file_cluster_12: 8.231, file_cluster_15: 8.386, file_cluster_16: 8.866
- **Magnitude:** 1039.7 | **LOC:** 2580 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 2.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (13.0%), Connectivity (formerly Api Exposure) (10.2%)
- **Documentation Coverage:** 96.2264% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_assert_impl` **(Many-Argument Workhorses)** (Impact: 50.0)
  * `test_change_type_int_to_boolean` **(Compute Cores)** (Impact: 11.2)
  * `test_add_col_table_has_native_boolean` **(Compute Cores)** (Impact: 10.4)
  * `_multi_fk_fixture` **(Stateful Encapsulated Methods)** (Impact: 7.9)
  * `_literal_ck_fixture` **(Stateful Encapsulated Methods)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 338
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 528`, `args: 177`, `func_start: 177`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 260`, `duplicate_logic: 12`, `unreferenced_by_name: 100`
* *Architecture:* `io: 26`, `api: 148`, `import: 55`
* *Defense:* `safety: 35`, `doc: 8`, `test: 137`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` alembic, alembic.ddl, alembic.operations, alembic.operations.batch, alembic.runtime.migration, alembic.script, alembic.testing, alembic.testing.env...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/operations/ops.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.257)
- **Top Global Matches:** file_cluster_5: 6.257, file_cluster_12: 10.027, file_cluster_7: 10.597
- **Magnitude:** 1027.02 | **LOC:** 2919 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **19**; blast radius 24.348; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Connectivity (formerly Api Exposure) (87.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.1%)
- **Documentation Coverage:** 93.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_foreign_key` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `from_constraint` **(Many-Argument Workhorses)** (Impact: 19.3)
  * `batch_create_foreign_key` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `reverse` **(Compute Cores)** (Impact: 17.1)
  * `to_table` **(Compute Cores)** (Impact: 16.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 349
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 349`, `args: 124`, `func_start: 124`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 223`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 21`, `api: 125`, `import: 49`
* *Defense:* `safety: 7`, `doc: 62`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.348
  * `Choke Point (Betweenness):` 0.018371 | `Ripple Effect (Closeness):` 0.33174
  * `Imports (Out-Degree: 9):` ..autogenerate.rewriter, ..ddl.base, ..runtime.migration, ..script.revision, ..util, .base, .schemaobj, __future__...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_autogen_indexes.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.157)
- **Top Global Matches:** file_cluster_15: 6.157, file_cluster_10: 6.805, file_cluster_16: 8.068
- **Magnitude:** 870.74 | **LOC:** 2135 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 2.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (16.0%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 96.319% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_remove_connection_uq` **(Many-Argument Workhorses)** (Impact: 18.9)
  * `test_remove_connection_index` **(Compute Cores)** (Impact: 18.5)
  * `include_object` **(Defensive Guards)** (Impact: 15.2)
  * `test_drop_table_w_uq_constraint` **(Defensive Guards)** (Impact: 13.2)
  * `include_object` **(Defensive Guards)** (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 199`, `args: 161`, `func_start: 83`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 252`, `duplicate_logic: 2`, `unreferenced_by_name: 57`
* *Architecture:* `io: 20`, `api: 88`, `import: 36`
* *Defense:* `safety: 17`, `doc: 8`, `test: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` alembic, alembic.operations.base, alembic.testing, alembic.testing.assertions, alembic.testing.env, alembic.testing.suite._autogen_fixtures, alembic.util, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/test_op.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.543)
- **Top Global Matches:** file_cluster_15: 5.543, file_cluster_13: 7.299, file_cluster_10: 7.433
- **Magnitude:** 822.5 | **LOC:** 1770 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 2.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (77.9%), Guard Balance (formerly Safety Score) (52.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (21.2%)
- **Documentation Coverage:** 95.0617% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_generic_alter_column_type_and_nullability` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `test_alter_column_schema_type_unnamed` **(Compute Cores)** (Impact: 10.0)
  * `test_add_column_primary_key` **(Compute Cores)** (Impact: 9.9)
  * `test_add_foreign_key_dialect_kw` **(I/O & Config Routines)** (Impact: 7.7)
  * `test_alter_column_computed_not_supported` **(Compute Cores)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *Api Near Db Sink:* 7 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 280`, `args: 175`, `func_start: 162`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 220`, `planned_debt: 4`
* *Architecture:* `io: 22`, `api: 166`, `concurrency: 3`, `import: 41`
* *Defense:* `safety: 10`, `doc: 11`, `test: 156`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` alembic, alembic.operations, alembic.operations.toimpl, alembic.testing, alembic.testing.assertions, alembic.testing.fixtures, alembic.util, sqlalchemy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/script/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.426)
- **Top Global Matches:** file_cluster_4: 9.426, file_cluster_5: 10.144, file_cluster_12: 11.389
- **Magnitude:** 822.48 | **LOC:** 1053 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **18**; blast radius 14.516; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (68.7%), Guard Balance (formerly Safety Score) (67.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 67.1642% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_revision` **(Many-Argument Workhorses)** (Impact: 123.6)
  * `_head_only` **(Many-Argument Workhorses)** (Impact: 57.5)
  * `_from_path` **(Many-Argument Workhorses)** (Impact: 38.6)
  * `_stamp_revs` **(Many-Argument Workhorses)** (Impact: 32.6)
  * `_catch_revision_errors` **(Many-Argument Workhorses)** (Impact: 28.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 198`, `args: 40`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 104`
* *Architecture:* `io: 10`, `api: 27`, `import: 36`
* *Defense:* `safety: 24`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.516
  * `Choke Point (Betweenness):` 0.016603 | `Ripple Effect (Closeness):` 0.320212
  * `Imports (Out-Degree: 10):` ..config, ..runtime, ..runtime.migration, ..util, ..util.pyfiles, .revision, .write_hooks, __future__...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/alembic/autogenerate/compare/constraints.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.27)
- **Top Global Matches:** file_cluster_6: 9.27, file_cluster_8: 10.089, file_cluster_4: 17.053
- **Magnitude:** 808.7 | **LOC:** 813 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 3.524; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.0%), Guard Balance (formerly Safety Score) (69.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_compare_indexes_and_uniques` **(Many-Argument Workhorses)** (Impact: 236.4)
  * `_compare_foreign_keys` **(Many-Argument Workhorses)** (Impact: 104.1)
  * `_correct_for_uq_duplicates_uix` **(Many-Argument Workhorses)** (Impact: 45.4)
  * `_compare_nullable` **(Many-Argument Workhorses)** (Impact: 24.7)
  * `_make_foreign_key` **(Many-Argument Workhorses)** (Impact: 22.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 271
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 114`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 97`, `planned_debt: 1`
* *Architecture:* `io: 13`, `api: 4`, `import: 37`
* *Defense:* `safety: 14`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.524
  * `Choke Point (Betweenness):` 0.004737 | `Ripple Effect (Closeness):` 0.187636
  * `Imports (Out-Degree: 9):` ...autogenerate.api, ...ddl._autogen, ...ddl.impl, ...operations, ...operations.ops, ...runtime.plugins, ...util, .util...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_postgresql.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.156)
- **Top Global Matches:** file_cluster_15: 6.156, file_cluster_10: 7.186, file_cluster_12: 7.655
- **Magnitude:** 808.58 | **LOC:** 1894 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 2.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (15.1%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 94.5312% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_compare_default_roundtrip` **(Many-Argument Workhorses)** (Impact: 12.1)
  * `test_add_identity_to_column` **(Compute Cores)** (Impact: 10.7)
  * `test_add_column_identity` **(Compute Cores)** (Impact: 10.6)
  * `test_toggle_not_distinct` **(Many-Argument Workhorses)** (Impact: 10.1)
  * `test_add` **(Many-Argument Workhorses)** (Impact: 10.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *Api Near Db Sink:* 6 instances
* *State Mutation (weighted view):* 272
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 324`, `args: 180`, `func_start: 132`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 202`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 4`, `unreferenced_by_name: 108`
* *Architecture:* `io: 37`, `api: 134`, `import: 65`
* *Defense:* `safety: 15`, `doc: 12`, `test: 106`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` alembic, alembic.autogenerate, alembic.autogenerate.compare.server_defaults, alembic.autogenerate.compare.tables, alembic.migration, alembic.operations, alembic.script, alembic.testing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/runtime/migration.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.546)
- **Top Global Matches:** file_cluster_5: 6.546, file_cluster_0: 8.236, file_cluster_12: 8.717
- **Magnitude:** 775.06 | **LOC:** 1347 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); it depends on **19**; blast radius 28.208; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.8%), Guard Balance (formerly Safety Score) (62.6%)
- **Documentation Coverage:** 79.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `configure` **(Many-Argument Workhorses)** (Impact: 29.7)
  * `run_migrations` **(Many-Argument Workhorses)** (Impact: 27.8)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 26.5)
  * `begin_transaction` **(Many-Argument Workhorses)** (Impact: 25.7)
  * `autocommit_block` **(Stateful Encapsulated Methods)** (Impact: 20.2)
    * *Intent:* """Enter an "autocommit" block, for databases that support AUTOCOMMIT isolation levels. This special...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 70 instances
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 286`, `args: 81`, `func_start: 81`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 102`, `planned_debt: 1`
* *Architecture:* `io: 14`, `api: 69`, `import: 41`
* *Defense:* `safety: 33`, `doc: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.208
  * `Choke Point (Betweenness):` 0.061227 | `Ripple Effect (Closeness):` 0.371906
  * `Imports (Out-Degree: 12):` ..config, ..ddl, ..script.base, ..script.revision, ..util, ..util.compat, .environment, __future__...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_command.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.672)
- **Top Global Matches:** file_cluster_15: 6.672, file_cluster_12: 7.858, file_cluster_16: 8.121
- **Magnitude:** 766.22 | **LOC:** 1709 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 2.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.8%), Complexity Load (formerly Cognitive Load) (16.7%), Connectivity (formerly Api Exposure) (12.4%)
- **Documentation Coverage:** 96.0289% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_assert_sql` **(Stateful Encapsulated Methods)** (Impact: 21.3)
  * `test_help_text` **(Defensive Guards)** (Impact: 16.0)
  * `_eq_cmd_output` **(Stateful Encapsulated Methods)** (Impact: 11.2)
  * `test_init_file_exists_and_is_empty` **(Type Conversions)** (Impact: 9.7)
  * `test_init_custom_template_location` **(Many-Argument Workhorses)** (Impact: 9.1)
    * *Intent:* """test #1660"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 220
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 433`, `args: 142`, `func_start: 142`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 162`, `planned_debt: 4`, `duplicate_logic: 15`, `unreferenced_by_name: 96`
* *Architecture:* `io: 44`, `api: 146`, `import: 45`
* *Defense:* `safety: 59`, `doc: 16`, `test: 120`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` alembic, alembic.script, alembic.testing, alembic.testing.env, alembic.testing.fixtures, alembic.util, alembic.util.sqla_compat, configparser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/operations/batch.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.403)
- **Top Global Matches:** file_cluster_5: 8.403, file_cluster_12: 9.48, file_cluster_4: 9.794
- **Magnitude:** 682.12 | **LOC:** 721 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **12**; blast radius 7.039; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.0%), Guard Balance (formerly Safety Score) (74.5%), Connectivity (formerly Api Exposure) (53.1%)
- **Documentation Coverage:** 91.3043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `alter_column` **(Many-Argument Workhorses)** (Impact: 50.2)
  * `_setup_dependencies_for_add_column` **(Many-Argument Workhorses)** (Impact: 47.1)
  * `_grab_table_elements` **(Stateful Encapsulated Methods)** (Impact: 24.9)
  * `_setup_referent` **(Stateful Encapsulated Methods)** (Impact: 21.8)
  * `drop_constraint` **(Defensive Guards)** (Impact: 20.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 294
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 155`, `args: 39`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 118`, `planned_debt: 2`
* *Architecture:* `io: 18`, `api: 30`, `import: 41`
* *Defense:* `safety: 20`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.039
  * `Choke Point (Betweenness):` 0.000919 | `Ripple Effect (Closeness):` 0.255184
  * `Imports (Out-Degree: 5):` ..ddl.base, ..ddl.impl, ..util, ..util.sqla_compat, __future__, sqlalchemy, sqlalchemy.engine, sqlalchemy.sql.elements...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/alembic/ddl/impl.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.267)
- **Top Global Matches:** file_cluster_5: 6.267, file_cluster_12: 9.513, file_cluster_7: 10.451
- **Magnitude:** 620.64 | **LOC:** 922 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **19**; blast radius 17.746; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.4%), Connectivity (formerly Api Exposure) (65.4%)
- **Documentation Coverage:** 91.3978% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `alter_column` **(Many-Argument Workhorses)** (Impact: 59.4)
  * `_exec` **(Many-Argument Workhorses)** (Impact: 41.4)
  * `bulk_insert` **(Many-Argument Workhorses)** (Impact: 33.2)
  * `compare_indexes` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `_column_args_match` **(Stateful Encapsulated Methods)** (Impact: 19.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 209`, `args: 49`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 71`
* *Architecture:* `io: 25`, `api: 42`, `import: 54`
* *Defense:* `safety: 13`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.746
  * `Choke Point (Betweenness):` 0.028526 | `Ripple Effect (Closeness):` 0.284024
  * `Imports (Out-Degree: 8):` ..autogenerate.api, ..operations.batch, ..util, ._autogen, .base, __future__, logging, re...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_revision.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.143)
- **Top Global Matches:** file_cluster_15: 7.143, file_cluster_10: 7.193, file_cluster_11: 8.313
- **Magnitude:** 612.96 | **LOC:** 1684 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.5%), Connectivity (formerly Api Exposure) (13.3%), Complexity Load (formerly Cognitive Load) (5.3%)
- **Documentation Coverage:** 99.3311% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_assert_iteration` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `test_all` **(Type Conversions)** (Impact: 9.5)
  * `test_no_revision_exists` **(Compute Cores)** (Impact: 6.5)
  * `test_partial_id_resolve_too_short` **(Compute Cores)** (Impact: 4.7)
  * `test_ancestor_nodes` **(I/O & Config Routines)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 210`, `args: 200`, `func_start: 152`, `class_start: 19`
* *Risk/State:* `state_mutation: 75`, `unreferenced_by_name: 123`
* *Architecture:* `io: 1`, `api: 165`, `import: 14`
* *Defense:* `safety: 3`, `doc: 2`, `test: 130`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ._large_map, alembic.script.revision, alembic.testing, alembic.testing.fixtures, sqlalchemy.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/ddl/postgresql.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.392)
- **Top Global Matches:** file_cluster_5: 6.392, file_cluster_12: 8.294, file_cluster_7: 9.935
- **Magnitude:** 604.96 | **LOC:** 865 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **27**; blast radius 3.634; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.8%), Complexity Load (formerly Cognitive Load) (58.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_exclude_constraint` **(Many-Argument Workhorses)** (Impact: 33.0)
  * `_cleanup_index_expr` **(Stateful Encapsulated Methods)** (Impact: 31.6)
  * `compare_indexes` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `autogen_column_reflect` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `compare_server_default` **(Many-Argument Workhorses)** (Impact: 27.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 229`, `args: 34`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 97`, `planned_debt: 1`
* *Architecture:* `io: 32`, `api: 29`, `import: 66`
* *Defense:* `safety: 9`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.634
  * `Choke Point (Betweenness):` 0.003492 | `Ripple Effect (Closeness):` 0.209432
  * `Imports (Out-Degree: 15):` ..autogenerate, ..autogenerate.api, ..autogenerate.render, ..operations, ..operations.base, ..runtime.migration, ..util, ..util.sqla_compat...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_script_production.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.389)
- **Top Global Matches:** file_cluster_12: 6.389, file_cluster_15: 6.908, file_cluster_16: 7.774
- **Magnitude:** 572.0 | **LOC:** 1593 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 2.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (10.9%), Complexity Load (formerly Cognitive Load) (10.3%)
- **Documentation Coverage:** 97.7011% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_reordering_example_wo_copy` **(I/O & Config Routines)** (Impact: 11.6)
    * *Intent:* """test related to #1692 in that we identified the recipe for rewriting column ordering was using co...
  * `order_columns` **(Many-Argument Workhorses)** (Impact: 11.3)
  * `test_file_template_with_directory_path` **(Defensive Guards)** (Impact: 11.0)
  * `test_create_script_branches_old_template` **(Compute Cores)** (Impact: 8.4)
  * `_test_tz` **(Stateful Encapsulated Methods)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 287`, `args: 97`, `func_start: 92`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 149`, `duplicate_logic: 12`, `unreferenced_by_name: 47`
* *Architecture:* `io: 63`, `api: 93`, `import: 49`
* *Defense:* `safety: 29`, `doc: 13`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` alembic, alembic.environment, alembic.operations, alembic.script, alembic.testing, alembic.testing.env, alembic.testing.fixtures, alembic.util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/test_version_traversal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.869)
- **Top Global Matches:** file_cluster_0: 6.869, file_cluster_15: 8.222, file_cluster_13: 9.045
- **Magnitude:** 570.78 | **LOC:** 1526 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (18.8%), Connectivity (formerly Api Exposure) (12.9%)
- **Documentation Coverage:** 82.0755% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_downgrade_branch_dependency` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* """c2branch depends on c1branch so taking down c1branch requires taking down both"""
  * `_assert_downgrade` **(Stateful Encapsulated Methods)** (Impact: 5.3)
  * `_assert_upgrade` **(Stateful Encapsulated Methods)** (Impact: 5.3)
  * `test_upgrade` **(I/O & Config Routines)** (Impact: 4.1)
  * `setup_class` **(Generic / Templated Code)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 162`, `args: 107`, `func_start: 107`, `class_start: 17`
* *Risk/State:* `state_mutation: 171`, `duplicate_logic: 16`, `unreferenced_by_name: 63`
* *Architecture:* `api: 122`, `import: 10`
* *Defense:* `safety: 5`, `doc: 24`, `test: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` alembic, alembic.migration, alembic.testing, alembic.testing.env, alembic.testing.fixtures
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/config.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.426)
- **Top Global Matches:** file_cluster_5: 6.426, file_cluster_12: 8.994, file_cluster_0: 10.677
- **Magnitude:** 552.78 | **LOC:** 1052 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **16**; blast radius 15.019; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%), Connectivity (formerly Api Exposure) (61.9%)
- **Documentation Coverage:** 68.4211% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_inis_from_config` **(Stateful Encapsulated Methods)** (Impact: 27.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 20.3)
  * `_inspect_function` **(Stateful Encapsulated Methods)** (Impact: 18.8)
  * `_generate_args` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `get_prepend_sys_paths_list` **(Compute Cores)** (Impact: 14.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 236
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 151`, `args: 39`, `func_start: 39`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 82`
* *Architecture:* `io: 8`, `api: 34`, `import: 27`
* *Defense:* `safety: 12`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.019
  * `Choke Point (Betweenness):` 0.023462 | `Ripple Effect (Closeness):` 0.322704
  * `Imports (Out-Degree: 6):` .__version__, .command, .util, .util.pyfiles, __future__, alembic, argparse, configparser...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/alembic/command.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.372)
- **Top Global Matches:** file_cluster_4: 6.372, file_cluster_15: 10.376, file_cluster_0: 10.56
- **Magnitude:** 523.52 | **LOC:** 849 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 5.132; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.2%), Connectivity (formerly Api Exposure) (53.4%)
- **Documentation Coverage:** 78.1818% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 65.6)
  * `history` **(Stateful Encapsulated Methods)** (Impact: 41.4)
  * `revision` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `stamp` **(Many-Argument Workhorses)** (Impact: 27.7)
  * `current` **(Many-Argument Workhorses)** (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 104`, `args: 29`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 56`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `api: 26`, `import: 16`
* *Defense:* `safety: 4`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.132
  * `Choke Point (Betweenness):` 0.01703 | `Ripple Effect (Closeness):` 0.258364
  * `Imports (Out-Degree: 13):` .autogenerate, .runtime.environment, .script, .util, __future__, alembic.config, alembic.script.base, alembic.script.revision...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_script_consumption.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.211)
- **Top Global Matches:** file_cluster_15: 6.211, file_cluster_16: 6.774, file_cluster_12: 7.284
- **Magnitude:** 469.88 | **LOC:** 1221 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 2.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (20.6%), Connectivity (formerly Api Exposure) (9.0%)
- **Documentation Coverage:** 96.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_setup_revision_files` **(Stateful Encapsulated Methods)** (Impact: 19.0)
  * `_assert_setup` **(Many-Argument Workhorses)** (Impact: 16.6)
  * `test_steps` **(Defensive Guards)** (Impact: 11.7)
  * `_opened_transaction_fixture` **(Many-Argument Workhorses)** (Impact: 10.9)
  * `_setup_for_fixture` **(Stateful Encapsulated Methods)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 239`, `args: 64`, `func_start: 64`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 123`, `duplicate_logic: 7`, `unreferenced_by_name: 27`
* *Architecture:* `io: 19`, `api: 65`, `import: 37`
* *Defense:* `safety: 58`, `doc: 18`, `test: 35`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` __future__, alembic, alembic.config, alembic.environment, alembic.script, alembic.testing, alembic.testing.env, alembic.testing.fixtures...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/ddl/mysql.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.306)
- **Top Global Matches:** file_cluster_6: 8.306, file_cluster_4: 9.333, file_cluster_12: 16.045
- **Magnitude:** 462.3 | **LOC:** 527 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 3.634; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `alter_column` **(Many-Argument Workhorses)** (Impact: 170.9)
  * `compare_server_default` **(Many-Argument Workhorses)** (Impact: 52.3)
  * `correct_for_autogen_constraints` **(Many-Argument Workhorses)** (Impact: 26.3)
  * `correct_for_autogen_foreignkeys` **(Many-Argument Workhorses)** (Impact: 21.4)
  * `_mysql_colspec` **(Stateful Encapsulated Methods)** (Impact: 19.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 110`, `args: 15`, `func_start: 15`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 33`, `planned_debt: 3`
* *Architecture:* `io: 10`, `api: 16`, `import: 31`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.634
  * `Choke Point (Betweenness):` 9.2e-05 | `Ripple Effect (Closeness):` 0.210495
  * `Imports (Out-Degree: 5):` ..util, ..util.sqla_compat, .base, .impl, __future__, re, sqlalchemy, sqlalchemy.dialects.mysql.base...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_config.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.54)
- **Top Global Matches:** file_cluster_15: 5.54, file_cluster_12: 7.985, file_cluster_13: 8.055
- **Magnitude:** 385.58 | **LOC:** 779 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 2.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (31.3%), Connectivity (formerly Api Exposure) (11.5%)
- **Documentation Coverage:** 97.8495% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_bool` **(Many-Argument Workhorses)** (Impact: 24.3)
  * `test_truncate_slug_length_types` **(Many-Argument Workhorses)** (Impact: 24.1)
  * `test_prepend_sys_path_locations` **(Many-Argument Workhorses)** (Impact: 19.5)
  * `test_version_locations` **(Many-Argument Workhorses)** (Impact: 17.0)
  * `test_write_hooks` **(Compute Cores)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 132`, `args: 39`, `func_start: 39`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 96`, `duplicate_logic: 3`, `unreferenced_by_name: 32`
* *Architecture:* `io: 18`, `api: 45`, `import: 25`
* *Defense:* `safety: 15`, `doc: 10`, `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` alembic, alembic.migration, alembic.operations, alembic.script, alembic.testing, alembic.testing.assertions, alembic.testing.env, alembic.testing.fixtures...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/operations/base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.885)
- **Top Global Matches:** file_cluster_5: 6.885, file_cluster_7: 10.818, file_cluster_12: 11.487
- **Magnitude:** 372.1 | **LOC:** 2002 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **23**; blast radius 24.559; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%), Connectivity (formerly Api Exposure) (77.2%)
- **Documentation Coverage:** 88.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `register_operation` **(Many-Argument Workhorses)** (Impact: 20.9)
  * `register` **(Compute Cores)** (Impact: 15.1)
  * `create_foreign_key` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `run_async` **(Many-Argument Workhorses)** (Impact: 10.9)
  * `batch_alter_table` **(Many-Argument Workhorses)** (Impact: 10.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 16 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 184`, `args: 51`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 52`, `high_risk_execution: 1`, `state_mutation: 32`, `planned_debt: 5`
* *Architecture:* `io: 12`, `api: 53`, `concurrency: 1`, `import: 60`
* *Defense:* `safety: 2`, `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.559
  * `Choke Point (Betweenness):` 0.03036 | `Ripple Effect (Closeness):` 0.318981
  * `Imports (Out-Degree: 10):` ..ddl, ..ddl.base, ..runtime.migration, ..util, ..util.compat, ..util.sqla_compat, .batch, .ops...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `alembic-1.18.4/alembic/autogenerate/compare/__init__.py` (PYTHON) | Magnitude: 10.02 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 30, indent_spaces: 15, import: 14, core_var_decl: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `alembic-1.18.4/tests/test_external_dialect.py` (PYTHON) | Magnitude: 73.22 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 51, state_mutation: 13, core_var_decl: 13
- `alembic-1.18.4/tests/test_autogen_composition.py` (PYTHON) | Magnitude: 83.94 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 180, structural_boundaries: 58, core_var_decl: 29, design_snake_case: 29
- `alembic-1.18.4/tests/test_batch.py` (PYTHON) | Magnitude: 1039.7 | Delta: **0.155** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 2079, structural_boundaries: 528, core_var_decl: 508, design_snake_case: 508

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `alembic-1.18.4/tests/test_revision.py` (PYTHON) | Magnitude: 612.96 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 1375, structural_boundaries: 210, args: 200, api: 165

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `alembic-1.18.4/alembic/util/__init__.py` (PYTHON) | Magnitude: 15.66 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 99, import: 33
- `alembic-1.18.4/alembic/ddl/__init__.py` (PYTHON) | Magnitude: 13.12 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 13, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `alembic-1.18.4/alembic/testing/fixtures.py` (PYTHON) | Magnitude: 339.2 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 245, structural_boundaries: 146, state_mutation: 73, core_var_decl: 64

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `alembic-1.18.4/alembic/autogenerate/api.py` -> **Severity: 7.228** (Bridge: 0.0723 * Flux: 99.9995%)
- `alembic-1.18.4/alembic/runtime/migration.py` -> **Severity: 6.122** (Bridge: 0.0612 * Flux: 99.9894%)
- `alembic-1.18.4/alembic/runtime/environment.py` -> **Severity: 3.685** (Bridge: 0.0368 * Flux: 99.9967%)
- `alembic-1.18.4/alembic/autogenerate/compare/__init__.py` -> **Severity: 3.32** (Bridge: 0.0481 * Flux: 68.9974%)
- `alembic-1.18.4/alembic/ddl/impl.py` -> **Severity: 2.851** (Bridge: 0.0285 * Flux: 99.95%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `alembic-1.18.4/alembic/util/langhelpers.py` -> **Severity: 32.115** (Embedded: 0.3776 * Error Risk: 85.0473%)
- `alembic-1.18.4/alembic/util/sqla_compat.py` -> **Severity: 26.437** (Embedded: 0.4106 * Error Risk: 64.3843%)
- `alembic-1.18.4/alembic/operations/base.py` -> **Severity: 24.787** (Embedded: 0.319 * Error Risk: 77.7064%)
- `alembic-1.18.4/alembic/runtime/migration.py` -> **Severity: 23.294** (Embedded: 0.3719 * Error Risk: 62.6341%)
- `alembic-1.18.4/alembic/util/pyfiles.py` -> **Severity: 22.735** (Embedded: 0.3252 * Error Risk: 69.9044%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `alembic-1.18.4/alembic/util/exc.py` -> **Severity: 4294.4** (Blast Radius: 42.944 * Doc Risk: 100.0%)
- `alembic-1.18.4/alembic/util/sqla_compat.py` -> **Severity: 3874.716** (Blast Radius: 39.214 * Doc Risk: 98.8095%)
- `alembic-1.18.4/alembic/util/compat.py` -> **Severity: 3564.794** (Blast Radius: 40.401 * Doc Risk: 88.2353%)
- `alembic-1.18.4/alembic/util/langhelpers.py` -> **Severity: 3098.482** (Blast Radius: 34.365 * Doc Risk: 90.1639%)
- `alembic-1.18.4/alembic/util/messaging.py` -> **Severity: 2648.3** (Blast Radius: 26.483 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 11540 call pairs -- scoped 40.8%, unique 0.0%, ambiguous 8.2%, external 51.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 11540 | 40.8% | 0.0% | 8.2% | 51.0% |

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
