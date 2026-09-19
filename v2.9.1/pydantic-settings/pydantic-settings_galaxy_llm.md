# ARCHITECTURAL_BRIEF: pydantic-settings
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 38 analyzed artifact(s), 10765 LOC.
- **Load-bearing artifact:** `pydantic_settings-2.13.1/pydantic_settings/main.py` -- 15 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pydantic_settings-2.13.1/pydantic_settings/sources/providers/cli.py` -- pulls in 29 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pydantic_settings-2.13.1/pydantic_settings/sources/providers/cli.py` at magnitude 2198.06 (structural weight, not risk).
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
| Total Artifacts | 47 |
| Analyzed Artifacts (Scanned) | 38 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9 |
| Total LOC | 10765 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 80.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2033 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4317 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 12.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6961 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 35 | 10735 | 92.1% |
| MAKEFILE | 1 | 29 | 2.6% |
| MARKDOWN | 1 | 0 | 2.6% |
| JSON | 1 | 1 | 2.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `1.259`
> **Composition Archetype:** `Small Flat Repo (2)` (z +1.26; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 34%, Data / Markup / Trivial 13%, Large Core Modules (3) 13%, Large Core Modules (2) 11%, Declarative / Non-Code 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 37 | 97.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 2.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.yml`: 1x Zero-Density Threshold (LOC: 61, Signals: 0)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 88.4 | 26.8 | 16.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.3 | 64.1 | 61.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 59.5 | 2.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 22.5 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 54.7 | 22.1 | 16.7 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 66.2 | 2.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 47.0 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 9.6 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 69.8 | 90.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 323 | 14 | 10 | `pydantic_settings-2.13.1/tests/test_settings.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 1136 | 30 | 33 | `pydantic_settings-2.13.1/tests/test_settings.py` |
| danger | 458 | 26 | 34 | `pydantic_settings-2.13.1/pydantic_settings/sources/providers/cli.py` |
| concurrency | 25 | 6 | 2 | `pydantic_settings-2.13.1/tests/conftest.py` |
| connectivity | 1174 | 35 | 33 | `pydantic_settings-2.13.1/tests/test_settings.py` |
| io | 72 | 20 | 5 | `pydantic_settings-2.13.1/tests/test_settings.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 5 | 3 | 0 | `pydantic_settings-2.13.1/pydantic_settings/sources/providers/cli.py` |
| events | 0 | 0 | 0 | - |
| tests | 699 | 14 | 31 | `pydantic_settings-2.13.1/tests/test_settings.py` |
| docs | 228 | 28 | 16 | `pydantic_settings-2.13.1/tests/test_source_cli.py` |
| debt | 77 | 13 | 7 | `pydantic_settings-2.13.1/tests/test_settings.py` |
| mutation | 3915 | 35 | 213 | `pydantic_settings-2.13.1/tests/test_settings.py` |
| dead_code | 370 | 14 | 14 | `pydantic_settings-2.13.1/tests/test_settings.py` |
| credential | 0 | 0 | 0 | - |
| threat | 165 | 20 | 14 | `pydantic_settings-2.13.1/tests/test_source_cli.py` |
| ml_ai | 2 | 1 | 0 | `pydantic_settings-2.13.1/tests/test_settings.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pydantic_settings-2.13.1/tests/test_settings.py` (Hits: 13)
- `pydantic_settings-2.13.1/tests/test_source_json.py` (Hits: 9)
- `pydantic_settings-2.13.1/tests/test_source_pyproject_toml.py` (Hits: 9)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **main.py** (`pydantic_settings-2.13.1/pydantic_settings/main.py`) — 15 inbound connections
2. **types.py** (`pydantic_settings-2.13.1/pydantic_settings/sources/types.py`) — 14 inbound connections
3. **exceptions.py** (`pydantic_settings-2.13.1/pydantic_settings/exceptions.py`) — 9 inbound connections
4. **env.py** (`pydantic_settings-2.13.1/pydantic_settings/sources/providers/env.py`) — 8 inbound connections
5. **json.py** (`pydantic_settings-2.13.1/pydantic_settings/sources/providers/json.py`) — 8 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **cli.py** (`pydantic_settings-2.13.1/pydantic_settings/sources/providers/cli.py`) — 29 outbound dependencies
2. **main.py** (`pydantic_settings-2.13.1/pydantic_settings/main.py`) — 19 outbound dependencies
3. **test_settings.py** (`pydantic_settings-2.13.1/tests/test_settings.py`) — 19 outbound dependencies
4. **base.py** (`pydantic_settings-2.13.1/pydantic_settings/sources/base.py`) — 17 outbound dependencies
5. **utils.py** (`pydantic_settings-2.13.1/pydantic_settings/sources/utils.py`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_settings_init_sources` **(Many-Argument Workhorses)** (@ `pydantic_settings-2.13.1/pydantic_settings/main.py`) -> Impact: **359.6** | LOC: 181
- `__init__` **(Many-Argument Workhorses)** (@ `pydantic_settings-2.13.1/pydantic_settings/sources/providers/cli.py`) -> Impact: **230.8** | LOC: 129
- `_add_parser_args` **(Many-Argument Workhorses)** (@ `pydantic_settings-2.13.1/pydantic_settings/sources/providers/cli.py`) -> Impact: **158.9** | LOC: 150
- `_add_parser_submodels` **(Many-Argument Workhorses)** (@ `pydantic_settings-2.13.1/pydantic_settings/sources/providers/cli.py`) -> Impact: **116.2** | LOC: 83
- `_serialized_args` **(Many-Argument Workhorses)** (@ `pydantic_settings-2.13.1/pydantic_settings/sources/providers/cli.py`) -> Impact: **91.2** | LOC: 77
- `_help_format` **(Stateful Encapsulated Methods)** (@ `pydantic_settings-2.13.1/pydantic_settings/sources/providers/cli.py`) -> Impact: **65.0** | LOC: 26
- `explode_env_vars` **(Many-Argument Workhorses)** (@ `pydantic_settings-2.13.1/pydantic_settings/sources/providers/env.py`) -> Impact: **61.5** | LOC: 67
  * *Intent:* """ Process env_vars and extract the values of keys containing env_nested_delimiter into nested dictionaries. This is applied to a single field, hence...
- `__init__` **(Many-Argument Workhorses)** (@ `pydantic_settings-2.13.1/pydantic_settings/sources/providers/nested_secrets.py`) -> Impact: **57.5** | LOC: 111
- `_get_alias_names` **(Many-Argument Workhorses)** (@ `pydantic_settings-2.13.1/pydantic_settings/sources/utils.py`) -> Impact: **51.3** | LOC: 43
- `_annotation_contains_types` **(Many-Argument Workhorses)** (@ `pydantic_settings-2.13.1/pydantic_settings/sources/utils.py`) -> Impact: **49.8** | LOC: 43

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pydantic_settings-2.13.1/tests` | 14 | 4041.78 | 12.53% | 0.0% |
| `pydantic_settings-2.13.1/pydantic_settings/sources/providers` | 13 | 3437.72 | 48.6% | 0.0% |
| `pydantic_settings-2.13.1/pydantic_settings` | 5 | 960.04 | 15.3% | 7.55% |
| `pydantic_settings-2.13.1/pydantic_settings/sources` | 4 | 905.88 | 27.37% | 14.87% |
| `pydantic_settings-2.13.1` | 2 | 22.08 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pydantic_settings-2.13.1/pydantic_settings/sources/base.py` -> **59.4986%** Exposure
- `pydantic_settings-2.13.1/pydantic_settings/utils.py` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pydantic_settings-2.13.1/pydantic_settings/main.py` -> **100.0%** Exposure
- `pydantic_settings-2.13.1/pydantic_settings/sources/base.py` -> **100.0%** Exposure
- `pydantic_settings-2.13.1/pydantic_settings/sources/providers/cli.py` -> **100.0%** Exposure
- `pydantic_settings-2.13.1/pydantic_settings/sources/providers/env.py` -> **100.0%** Exposure
- `pydantic_settings-2.13.1/pydantic_settings/sources/providers/gcp.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pydantic_settings-2.13.1/tests/test_settings.py` -> **183** Orphaned Functions | **8** Duplicates
- `pydantic_settings-2.13.1/tests/test_source_cli.py` -> **76** Orphaned Functions | **5** Duplicates
- `pydantic_settings-2.13.1/tests/test_source_yaml.py` -> **17** Orphaned Functions | **17** Duplicates
- `pydantic_settings-2.13.1/tests/test_source_gcp_secret_manager.py` -> **24** Orphaned Functions | **8** Duplicates
- `pydantic_settings-2.13.1/tests/test_source_pyproject_toml.py` -> **12** Orphaned Functions | **7** Duplicates

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
- **Unknown Dependencies:** `264` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pydantic_settings-2.13.1/pydantic_settings/sources/providers/cli.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2198.06 | **LOC:** 1523 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **29**; blast radius 9.232; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.5%)
- **Documentation Coverage:** 90.3226% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 230.8)
  * `_add_parser_args` **(Many-Argument Workhorses)** (Impact: 158.9)
  * `_add_parser_submodels` **(Many-Argument Workhorses)** (Impact: 116.2)
  * `_serialized_args` **(Many-Argument Workhorses)** (Impact: 91.2)
  * `_help_format` **(Stateful Encapsulated Methods)** (Impact: 65.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 214 instances
* *State Mutation (weighted view):* 685
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 479`, `structural_boundaries: 259`, `args: 62`, `func_start: 62`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 122`, `state_mutation: 257`
* *Architecture:* `api: 23`, `import: 30`
* *Defense:* `safety: 59`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.232
  * `Choke Point (Betweenness):` 0.000699 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 5):` ...exceptions, ...utils, ..types, ..utils, .env, __future__, argparse, collections...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pydantic_settings-2.13.1/tests/test_settings.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1473.84 | **LOC:** 3443 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 8.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (23.8%), Complexity Load (formerly Cognitive Load) (15.3%), Connectivity (formerly Api Exposure) (15.0%)
- **Documentation Coverage:** 94.2982% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_env_parse_enums` **(Type Conversions)** (Impact: 13.9)
  * `test_discriminated_union_with_callable_discriminator` **(Defensive Guards)** (Impact: 10.3)
  * `get_discriminator_value` **(Defensive Guards)** (Impact: 9.1)
  * `test_alias_resolution_init_source` **(Defensive Guards)** (Impact: 8.5)
  * `check_for_deprecated_attributes` **(Defensive Guards)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 396
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 987`, `args: 219`, `func_start: 217`, `class_start: 256`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 344`, `planned_debt: 1`, `fragile_debt: 9`, `duplicate_logic: 8`, `unreferenced_by_name: 183`
* *Architecture:* `io: 13`, `api: 458`, `import: 23`
* *Defense:* `safety: 349`, `doc: 22`, `test: 257`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` annotated_types, collections.abc, dataclasses, datetime, dotenv, enum, json, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pydantic_settings-2.13.1/tests/test_source_cli.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1141.74 | **LOC:** 3207 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 8.113; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (31.2%), Concurrency Surface (formerly Concurrency) (21.6%), Complexity Load (formerly Cognitive Load) (14.8%)
- **Documentation Coverage:** 98.3051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_cli_annotation_exceptions` **(Compute Cores)** (Impact: 26.2)
  * `test_cli_metavar_format` **(Defensive Guards)** (Impact: 24.8)
  * `test_cli_bool_flags` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `test_cli_dict_arg` **(Many-Argument Workhorses)** (Impact: 16.4)
  * `test_cli_user_settings_source` **(Defensive Guards)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 58 instances
* *Concurrency (weighted view):* 20
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 710`, `args: 118`, `func_start: 104`, `class_start: 175`
* *Risk/State:* `safety_bypasses: 48`, `high_risk_execution: 1`, `state_mutation: 212`, `duplicate_logic: 5`, `unreferenced_by_name: 76`
* *Architecture:* `io: 4`, `api: 278`, `concurrency: 5`, `import: 17`
* *Defense:* `safety: 293`, `doc: 46`, `test: 184`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` argparse, asyncio, enum, pathlib, pydantic, pydantic._internal._repr, pydantic_settings, pydantic_settings.sources...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pydantic_settings-2.13.1/pydantic_settings/main.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 900.28 | **LOC:** 902 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **19**; blast radius 218.73; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.3%)
- **Documentation Coverage:** 96.2963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_settings_init_sources` **(Many-Argument Workhorses)** (Impact: 359.6)
  * `run` **(Many-Argument Workhorses)** (Impact: 45.8)
  * `_settings_restore_init_kwarg_names` **(Stateful Encapsulated Methods)** (Impact: 30.1)
  * `_settings_build_values` **(Stateful Encapsulated Methods)** (Impact: 23.5)
  * `run_subcommand` **(Many-Argument Workhorses)** (Impact: 22.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 87 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 90`, `args: 15`, `func_start: 15`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 103`
* *Architecture:* `api: 13`, `concurrency: 6`, `import: 19`
* *Defense:* `safety: 24`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 218.73
  * `Choke Point (Betweenness):` 0.029113 | `Ripple Effect (Closeness):` 0.479605
  * `Imports (Out-Degree: 3):` .exceptions, .sources, .sources.utils, __future__, argparse, asyncio, collections.abc, inspect...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `pydantic_settings-2.13.1/pydantic_settings/sources/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 561.76 | **LOC:** 580 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **17**; blast radius 40.322; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (59.5%)
- **Documentation Coverage:** 56.5217% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_extract_field_info` **(Many-Argument Workhorses)** (Impact: 48.6)
    * *Intent:* """ Extracts field info. This info is used to get the value of field from environment variables. It ...
  * `_replace_field_names_case_insensitively` **(Many-Argument Workhorses)** (Impact: 41.9)
    * *Intent:* """ Replace field names in values dict by looking in models fields insensitively. By having the foll...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 40.1)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `get_subcommand` **(Many-Argument Workhorses)** (Impact: 34.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 196
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 114`, `args: 28`, `func_start: 28`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 68`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 18`, `import: 17`
* *Defense:* `safety: 22`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 40.322
  * `Choke Point (Betweenness):` 0.012501 | `Ripple Effect (Closeness):` 0.322368
  * `Imports (Out-Degree: 4):` ..exceptions, ..utils, .types, .utils, __future__, abc, collections.abc, dataclasses...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pydantic_settings-2.13.1/tests/test_source_gcp_secret_manager.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 429.28 | **LOC:** 748 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 8.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (28.6%), Connectivity (formerly Api Exposure) (11.9%)
- **Documentation Coverage:** 75.2475% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mock_secret_client_factory` **(Stateful Encapsulated Methods)** (Impact: 14.2)
  * `_create_client` **(Stateful Encapsulated Methods)** (Impact: 14.1)
  * `test_secret_version_annotation` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `test_secret_manager_mapping_collision` **(Many-Argument Workhorses)** (Impact: 10.7)
  * `test_secret_version_no_fallback` **(Many-Argument Workhorses)** (Impact: 10.0)
    * *Intent:* """ Test that we do NOT fallback to 'latest' if a specific version is requested but missing. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 157`, `args: 47`, `func_start: 46`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 95`, `fragile_debt: 3`, `duplicate_logic: 8`, `unreferenced_by_name: 24`
* *Architecture:* `api: 57`, `import: 12`
* *Defense:* `safety: 36`, `doc: 13`, `test: 95`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` google.cloud.secretmanager, if, pydantic, pydantic_core._pydantic_core, pydantic_settings, pydantic_settings.sources, pydantic_settings.sources.providers.gcp, pydantic_settings.sources.types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pydantic_settings-2.13.1/pydantic_settings/sources/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 301.02 | **LOC:** 284 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 70.087; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.0%)
- **Documentation Coverage:** 68.4211% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_alias_names` **(Many-Argument Workhorses)** (Impact: 51.3)
  * `_annotation_contains_types` **(Many-Argument Workhorses)** (Impact: 49.8)
  * `_annotation_is_complex` **(Stateful Encapsulated Methods)** (Impact: 22.3)
    * *Intent:* # If the model is a root model, the root annotation should be used to # evaluate the complexity. ann...
  * `_substitute_typevars` **(Stateful Encapsulated Methods)** (Impact: 13.2)
    * *Intent:* """Substitute TypeVars in a type annotation with concrete types from param_map."""
  * `parse_env_vars` **(Generic / Templated Code)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 96`, `args: 16`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 30`
* *Architecture:* `api: 3`, `import: 18`
* *Defense:* `safety: 17`, `doc: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 70.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.295142
  * `Imports (Out-Degree: 2):` ..exceptions, ..utils, .types, __future__, collections, collections.abc, dataclasses, enum...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pydantic_settings-2.13.1/pydantic_settings/sources/providers/env.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 298.44 | **LOC:** 311 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **14**; blast radius 26.077; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (50.9%)
- **Documentation Coverage:** 46.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `explode_env_vars` **(Many-Argument Workhorses)** (Impact: 61.5)
    * *Intent:* """ Process env_vars and extract the values of keys containing env_nested_delimiter into nested dict...
  * `next_field` **(Many-Argument Workhorses)** (Impact: 40.8)
    * *Intent:* # Default value of `case_sensitive` is `None`, because we don't want to break existing behavior. # W...
  * `prepare_field_value` **(Many-Argument Workhorses)** (Impact: 36.5)
    * *Intent:* """ Prepare value for the field. * Extract value for nested field. * Deserialize value to python obj...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 21.4)
  * `_coerce_env_val_strict` **(Stateful Encapsulated Methods)** (Impact: 13.1)
    * *Intent:* """ Coerce environment string values based on field annotation if model config is `strict=True`. Arg...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 65`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 32`
* *Architecture:* `api: 8`, `import: 14`
* *Defense:* `safety: 17`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.077
  * `Choke Point (Betweenness):` 0.006982 | `Ripple Effect (Closeness):` 0.247076
  * `Imports (Out-Degree: 3):` ...utils, ..base, ..types, ..utils, __future__, collections.abc, os, pydantic...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pydantic_settings-2.13.1/tests/test_source_yaml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 237.0 | **LOC:** 614 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 8.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (38.0%), Connectivity (formerly Api Exposure) (12.6%), Complexity Load (formerly Cognitive Load) (12.1%)
- **Documentation Coverage:** 80.2198% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multiple_file_yaml_deep_merge` **(Generic / Templated Code)** (Impact: 7.2)
  * `test_yaml_config_section_unusual_literal_keys` **(Generic / Templated Code)** (Impact: 5.0)
    * *Intent:* """Test that keys with leading/trailing/consecutive dots can be accessed as literal keys."""
  * `test_invalid_yaml_config_section_nested_path` **(Generic / Templated Code)** (Impact: 4.3)
  * `test_yaml_config_section_with_literal_dots` **(Generic / Templated Code)** (Impact: 4.3)
    * *Intent:* """Test that keys containing literal dots can be accessed using greedy matching."""
  * `test_yaml_config_section_non_dict_intermediate` **(Generic / Templated Code)** (Impact: 4.3)
    * *Intent:* """Test that traversing through non-dict intermediate values raises clear error."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 129`, `args: 36`, `func_start: 36`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 50`, `duplicate_logic: 17`, `unreferenced_by_name: 17`
* *Architecture:* `io: 1`, `api: 57`, `import: 5`
* *Defense:* `safety: 26`, `doc: 22`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pathlib, pydantic, pydantic_settings, pytest, yaml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pydantic_settings-2.13.1/pydantic_settings/sources/providers/gcp.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 206.2 | **LOC:** 242 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 12.68; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.3%), Complexity Load (formerly Cognitive Load) (88.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 43.5)
  * `get_field_value` **(Many-Argument Workhorses)** (Impact: 28.2)
    * *Intent:* """Override get_field_value to get the secret value from GCP Secret Manager. Look for a SecretVersio...
  * `__getitem__` **(Compute Cores)** (Impact: 11.1)
  * `_secret_name_map` **(Stateful Encapsulated Methods)** (Impact: 9.5)
  * `_select_case_insensitive_secret` **(Stateful Encapsulated Methods)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 77`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 30`, `dead_code: 1`
* *Architecture:* `api: 10`, `import: 15`
* *Defense:* `safety: 6`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.68
  * `Choke Point (Betweenness):` 0.00352 | `Ripple Effect (Closeness):` 0.078947
  * `Imports (Out-Degree: 3):` ..types, .env, __future__, collections.abc, functools, google.auth, google.auth.credentials, google.cloud.secretmanager...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pydantic_settings-2.13.1/pydantic_settings/sources/providers/azure.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 140.0 | **LOC:** 160 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 11.531; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 17.9)
  * `_load_remote` **(Stateful Encapsulated Methods)** (Impact: 16.5)
  * `__getitem__` **(Compute Cores)** (Impact: 14.8)
  * `_extract_field_info` **(Stateful Encapsulated Methods)** (Impact: 10.4)
  * `__init__` **(Encapsulated Accessors)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 56`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 24`
* *Architecture:* `api: 10`, `import: 13`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.531
  * `Choke Point (Betweenness):` 0.002033 | `Ripple Effect (Closeness):` 0.078947
  * `Imports (Out-Degree: 4):` .env, __future__, azure.core.credentials, azure.core.exceptions, azure.keyvault.secrets, collections.abc, pydantic.alias_generators, pydantic.fields...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pydantic_settings-2.13.1/tests/test_source_nested_secrets.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 134.06 | **LOC:** 429 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 8.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (38.8%), Connectivity (formerly Api Exposure) (11.3%), Complexity Load (formerly Cognitive Load) (9.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multiple_secrets_dirs` **(Defensive Guards)** (Impact: 31.4)
  * `test_env_ignore_empty` **(Many-Argument Workhorses)** (Impact: 5.8)
  * `test_invalid_options` **(Compute Cores)** (Impact: 3.4)
  * `settings_customise_sources` **(Parameter Forwarders)** (Impact: 3.3)
  * `settings_customise_sources` **(Parameter Forwarders)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 62`, `args: 14`, `func_start: 14`, `class_start: 16`
* *Risk/State:* `state_mutation: 18`, `duplicate_logic: 2`, `unreferenced_by_name: 11`
* *Architecture:* `api: 30`, `import: 6`
* *Defense:* `safety: 20`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` enum, os, pydantic, pydantic_settings, pydantic_settings.sources.providers.nested_secrets, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pydantic_settings-2.13.1/pydantic_settings/sources/providers/nested_secrets.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 133.72 | **LOC:** 167 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **14**; blast radius 15.501; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 57.5)
  * `validate_secrets_path` **(Compute Cores)** (Impact: 19.9)
  * `load_secrets` **(Generic / Templated Code)** (Impact: 4.5)
  * `__repr__` **(Generic / Templated Code)** (Impact: 1.5)
  * `first_not_none` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 37`, `args: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 14`
* *Architecture:* `io: 2`, `api: 6`, `import: 14`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.501
  * `Choke Point (Betweenness):` 0.006645 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 5):` ...exceptions, ...main, ...sources, ...utils, ..base, ..utils, .env, .secrets...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pydantic_settings-2.13.1/tests/test_source_pyproject_toml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 131.8 | **LOC:** 320 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 8.113; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (20.6%), Connectivity (formerly Api Exposure) (12.2%), Complexity Load (formerly Cognitive Load) (11.5%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_pyproject_toml_file_parent` **(Generic / Templated Code)** (Impact: 3.7)
  * `test_pyproject_toml_no_file_too_shallow` **(Generic / Templated Code)** (Impact: 3.5)
  * `test_pyproject_toml_file_explicit` **(Defensive Guards)** (Impact: 3.4)
  * `test_pyproject_toml_file` **(Generic / Templated Code)** (Impact: 2.9)
  * `test___init___no_file` **(Defensive Guards)** (Impact: 2.8)
    * *Intent:* """Test __init__ no file."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 84`, `args: 19`, `func_start: 19`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 34`, `duplicate_logic: 7`, `unreferenced_by_name: 12`
* *Architecture:* `io: 9`, `api: 33`, `import: 7`
* *Defense:* `safety: 33`, `doc: 16`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pathlib, pydantic, pydantic_settings, pytest, pytest_mock, sys, tomli
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pydantic_settings-2.13.1/tests/test_source_azure_key_vault.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 125.0 | **LOC:** 315 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 8.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (36.9%), Connectivity (formerly Api Exposure) (10.4%), Complexity Load (formerly Cognitive Load) (10.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_snake_case_conversion` **(Defensive Guards)** (Impact: 23.2)
    * *Intent:* """Test that secret names are mapped to snake case in field names."""
  * `test_snake_case_conversion_missing_alias` **(Generic / Templated Code)** (Impact: 5.4)
  * `test_azure_key_vault_settings_source` **(Generic / Templated Code)** (Impact: 4.1)
    * *Intent:* """Test AzureKeyVaultSettingsSource."""
  * `_raise_resource_not_found_when_getting_parent_secret_name` **(Stateful Encapsulated Methods)** (Impact: 3.9)
  * `test_dash_to_underscore_translation` **(Generic / Templated Code)** (Impact: 3.9)
    * *Intent:* """Test that dashes in secret names are mapped to underscores in field names."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 78`, `args: 12`, `func_start: 12`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`, `unreferenced_by_name: 7`
* *Architecture:* `api: 22`, `import: 8`
* *Defense:* `safety: 20`, `doc: 11`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` azure.core.exceptions, azure.identity, azure.keyvault.secrets, pydantic, pydantic_settings, pydantic_settings.sources.providers.azure, pytest, pytest_mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pydantic_settings-2.13.1/tests/test_source_json.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 121.92 | **LOC:** 223 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 8.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (24.8%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `json_config_path` **(C Struct Operations)** (Impact: 10.4)
  * `test_multiple_file_json_merge` **(Generic / Templated Code)** (Impact: 6.7)
  * `settings_customise_sources` **(Generic / Templated Code)** (Impact: 3.1)
  * `settings_customise_sources` **(Generic / Templated Code)** (Impact: 3.1)
  * `settings_customise_sources` **(Generic / Templated Code)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 84`, `args: 22`, `func_start: 22`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `duplicate_logic: 3`, `unreferenced_by_name: 14`
* *Architecture:* `io: 9`, `api: 29`, `import: 9`
* *Defense:* `safety: 11`, `doc: 2`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` importlib.abc, importlib.resources, importlib.resources.abc, json, pathlib, pydantic, pydantic_settings, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pydantic_settings-2.13.1/pydantic_settings/sources/providers/dotenv.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 118.02 | **LOC:** 171 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 12.68; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.8%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Compute Cores)** (Impact: 27.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 19.5)
  * `_read_env_files` **(Stateful Encapsulated Methods)** (Impact: 7.8)
  * `read_env_file` **(Generic / Templated Code)** (Impact: 5.8)
  * `_static_read_env_file` **(Stateful Encapsulated Methods)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 46`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 13`
* *Architecture:* `io: 2`, `api: 7`, `import: 13`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.68
  * `Choke Point (Betweenness):` 0.002335 | `Ripple Effect (Closeness):` 0.078947
  * `Imports (Out-Degree: 3):` ..types, ..utils, .env, __future__, collections.abc, dotenv, os, pathlib...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pydantic_settings-2.13.1/pydantic_settings/sources/providers/yaml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 88.0 | **LOC:** 131 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 18.426; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 22.5)
  * `_traverse_nested_section` **(Many-Argument Workhorses)** (Impact: 16.2)
  * `_read_file` **(Encapsulated Accessors)** (Impact: 3.7)
  * `import_yaml` **(Defensive Guards)** (Impact: 2.4)
  * `__repr__` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 33`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 12`
* *Architecture:* `io: 2`, `api: 6`, `import: 8`
* *Defense:* `safety: 7`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.426
  * `Choke Point (Betweenness):` 0.006199 | `Ripple Effect (Closeness):` 0.105263
  * `Imports (Out-Degree: 3):` ..base, ..types, __future__, pathlib, pydantic_settings.main, typing, yaml
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pydantic_settings-2.13.1/pydantic_settings/sources/providers/secrets.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 80.08 | **LOC:** 133 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **11**; blast radius 16.616; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (88.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (50.7%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Defensive Guards)** (Impact: 16.9)
    * *Intent:* """ Build fields from "secrets" files. """
  * `get_field_value` **(Many-Argument Workhorses)** (Impact: 13.5)
    * *Intent:* """ Gets the value for field from secret file and a flag to determine whether value is complex. Args...
  * `find_case_path` **(Many-Argument Workhorses)** (Impact: 12.1)
    * *Intent:* """ Find a file within path's directory matching filename, optionally ignoring case. Args: dir_path:...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 10.5)
  * `__repr__` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 38`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 6`
* *Architecture:* `io: 2`, `api: 6`, `import: 11`
* *Defense:* `safety: 1`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.616
  * `Choke Point (Betweenness):` 0.009258 | `Ripple Effect (Closeness):` 0.135338
  * `Imports (Out-Degree: 5):` ...exceptions, ..base, ..types, __future__, os, pathlib, pydantic.fields, pydantic_settings.main...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pydantic_settings-2.13.1/tests/test_source_toml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 66.84 | **LOC:** 161 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 8.113; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.7%), Complexity Load (formerly Cognitive Load) (16.5%), Connectivity (formerly Api Exposure) (10.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multiple_file_toml_merge` **(Generic / Templated Code)** (Impact: 7.2)
  * `test_toml_file` **(Generic / Templated Code)** (Impact: 3.1)
  * `settings_customise_sources` **(Generic / Templated Code)** (Impact: 3.1)
  * `settings_customise_sources` **(Generic / Templated Code)** (Impact: 3.1)
  * `settings_customise_sources` **(Generic / Templated Code)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 38`, `args: 9`, `func_start: 9`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`, `duplicate_logic: 2`, `unreferenced_by_name: 5`
* *Architecture:* `io: 5`, `api: 15`, `import: 6`
* *Defense:* `safety: 11`, `doc: 6`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pathlib, pydantic, pydantic_settings, pytest, sys, tomli
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pydantic_settings-2.13.1/tests/test_source_aws_secrets_manager.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 58.66 | **LOC:** 161 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 8.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (34.7%), Connectivity (formerly Api Exposure) (10.9%), Complexity Load (formerly Cognitive Load) (8.9%)
- **Documentation Coverage:** 35.2941% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_secret_manager_case_insensitive_success` **(Generic / Templated Code)** (Impact: 3.2)
    * *Intent:* """Test secret manager getitem case insensitive success."""
  * `settings_customise_sources` **(Generic / Templated Code)** (Impact: 3.1)
  * `settings_customise_sources` **(Generic / Templated Code)** (Impact: 3.1)
  * `test_aws_secrets_manager_settings_source` **(Generic / Templated Code)** (Impact: 3.0)
    * *Intent:* """Test AWSSecretsManagerSettingsSource."""
  * `test___call__` **(Defensive Guards)** (Impact: 2.6)
    * *Intent:* """Test __call__."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 39`, `args: 7`, `func_start: 7`, `class_start: 8`
* *Risk/State:* `state_mutation: 19`, `unreferenced_by_name: 5`
* *Architecture:* `io: 6`, `api: 15`, `import: 9`
* *Defense:* `safety: 15`, `doc: 10`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` boto3, json, moto, os, pydantic, pydantic_settings, pydantic_settings.sources.providers.aws, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pydantic_settings-2.13.1/tests/test_precedence_and_merging.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 54.16 | **LOC:** 137 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 8.113; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.6%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_merging_preserves_earlier_values` **(Defensive Guards)** (Impact: 3.6)
    * *Intent:* # Prove that merging preserves earlier source values: init -> env -> dotenv -> secrets -> defaults #...
  * `settings_customise_sources` **(Generic / Templated Code)** (Impact: 3.1)
  * `test_precedence_env_over_dotenv` **(Type Conversions)** (Impact: 2.3)
  * `test_precedence_dotenv_over_secrets` **(Defensive Guards)** (Impact: 2.3)
    * *Intent:* # create dotenv env_file = tmp_path / '.env' env_file.write_text('FOO=from-dotenv\n') # create secre...
  * `test_init_kwargs_override_env_with_alias_and_extra_forbid` **(Type Conversions)** (Impact: 2.2)
    * *Intent:* # Reproduction for https://github.com/pydantic/pydantic-settings/issues/744 class Settings(BaseSetti...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 49`, `args: 8`, `func_start: 8`, `class_start: 7`
* *Risk/State:* `state_mutation: 18`, `unreferenced_by_name: 8`
* *Architecture:* `io: 1`, `api: 15`, `import: 5`
* *Defense:* `safety: 9`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, pathlib, pydantic, pydantic_settings, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pydantic_settings-2.13.1/tests/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 53.28 | **LOC:** 125 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 8.113; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (23.4%), Connectivity (formerly Api Exposure) (10.3%)
- **Documentation Coverage:** 90.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write` **(Generic / Templated Code)** (Impact: 3.7)
  * `clear` **(Parameter Forwarders)** (Impact: 3.0)
  * `cd_tmp_path` **(Defensive Guards)** (Impact: 2.7)
    * *Intent:* """Change directory into the value of the ``tmp_path`` fixture. .. rubric:: Example .. code-block:: ...
  * `set` **(Type Conversions)** (Impact: 2.1)
  * `docs_test_env` **(Type Conversions)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 23`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 14`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `io: 3`, `api: 11`, `import: 6`
* *Defense:* `safety: 2`, `doc: 1`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, collections.abc, os, pathlib, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pydantic_settings-2.13.1/pydantic_settings/sources/providers/toml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 45.22 | **LOC:** 68 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 13.156; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (45.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Generic / Templated Code)** (Impact: 7.2)
  * `import_toml` **(Defensive Guards)** (Impact: 5.7)
  * `_read_file` **(Encapsulated Accessors)** (Impact: 3.8)
  * `__repr__` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 35`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7`
* *Architecture:* `io: 5`, `api: 5`, `import: 11`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.156
  * `Choke Point (Betweenness):` 0.00224 | `Ripple Effect (Closeness):` 0.078947
  * `Imports (Out-Degree: 3):` ..base, ..types, __future__, pathlib, pydantic_settings.main, sys, tomli, tomllib...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pydantic_settings-2.13.1/pydantic_settings/sources/providers/pyproject.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 40.12 | **LOC:** 63 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 9.232; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (36.2%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_pick_pyproject_toml_file` **(Stateful Encapsulated Methods)** (Impact: 11.5)
    * *Intent:* """Pick a `pyproject.toml` file path to use. Args: provided: Explicit path provided when instantiati...
  * `__init__` **(Generic / Templated Code)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 19`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `io: 1`, `api: 3`, `import: 5`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.232
  * `Choke Point (Betweenness):` 0.000231 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 2):` .toml, __future__, pathlib, pydantic_settings.main, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pydantic_settings-2.13.1/pydantic_settings/main.py` -> **Severity: 2.911** (Bridge: 0.0291 * Flux: 100.0%)
- `pydantic_settings-2.13.1/pydantic_settings/sources/base.py` -> **Severity: 1.25** (Bridge: 0.0125 * Flux: 100.0%)
- `pydantic_settings-2.13.1/pydantic_settings/sources/providers/secrets.py` -> **Severity: 0.925** (Bridge: 0.0093 * Flux: 99.8788%)
- `pydantic_settings-2.13.1/pydantic_settings/sources/providers/json.py` -> **Severity: 0.866** (Bridge: 0.0087 * Flux: 99.6316%)
- `pydantic_settings-2.13.1/pydantic_settings/sources/providers/env.py` -> **Severity: 0.698** (Bridge: 0.007 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pydantic_settings-2.13.1/pydantic_settings/main.py` -> **Severity: 46.226** (Embedded: 0.4796 * Error Risk: 96.383%)
- `pydantic_settings-2.13.1/pydantic_settings/sources/types.py` -> **Severity: 45.635** (Embedded: 0.4679 * Error Risk: 97.53%)
- `pydantic_settings-2.13.1/pydantic_settings/sources/base.py` -> **Severity: 32.015** (Embedded: 0.3224 * Error Risk: 99.3111%)
- `pydantic_settings-2.13.1/pydantic_settings/sources/utils.py` -> **Severity: 28.91** (Embedded: 0.2951 * Error Risk: 97.9545%)
- `pydantic_settings-2.13.1/pydantic_settings/exceptions.py` -> **Severity: 24.072** (Embedded: 0.3751 * Error Risk: 64.1725%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pydantic_settings-2.13.1/pydantic_settings/main.py` -> **Severity: 21062.89** (Blast Radius: 218.73 * Doc Risk: 96.2963%)
- `pydantic_settings-2.13.1/pydantic_settings/sources/types.py` -> **Severity: 17635.6** (Blast Radius: 176.356 * Doc Risk: 100.0%)
- `pydantic_settings-2.13.1/pydantic_settings/sources/utils.py` -> **Severity: 4795.43** (Blast Radius: 70.087 * Doc Risk: 68.4211%)
- `pydantic_settings-2.13.1/pydantic_settings/sources/providers/json.py` -> **Severity: 3501.7** (Blast Radius: 35.017 * Doc Risk: 100.0%)
- `pydantic_settings-2.13.1/pydantic_settings/sources/base.py` -> **Severity: 2279.068** (Blast Radius: 40.322 * Doc Risk: 56.5217%)

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
