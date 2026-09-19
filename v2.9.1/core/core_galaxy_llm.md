# ARCHITECTURAL_BRIEF: core
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/home-assistant/core.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 22671 analyzed artifact(s), 2855839 LOC.
- **Load-bearing artifact:** `homeassistant/core.py` -- 12259 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tests/conftest.py` -- pulls in 75 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/test_config_entries.py` at magnitude 6283.84 (structural weight, not risk).
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
| Total Artifacts | 24818 |
| Analyzed Artifacts (Scanned) | 22671 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2147 |
| Total LOC | 2855839 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 91.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3509 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2332 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.765 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 321 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 16674 | 2396779 | 73.5% |
| JSON | 5361 | 444032 | 23.6% |
| YAML | 527 | 14759 | 2.3% |
| XML | 63 | 0 | 0.3% |
| PLAINTEXT | 16 | 2 | 0.1% |
| SHELL | 12 | 192 | 0.1% |
| MARKDOWN | 11 | 0 | 0.0% |
| BINARY_THREAT | 3 | 3 | 0.0% |
| JAVASCRIPT | 2 | 24 | 0.0% |
| DOCKERFILE | 1 | 43 | 0.0% |
| CSV | 1 | 5 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `4.493`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +4.49; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 35%, Generic / Templated Code Files 29%, Large Core Modules (2) 18%, Encapsulated Accessors Files 5%, Declarative / Non-Code 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 22641 | 99.9% |
| Unknown | 4 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 25 | 0.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2147*

**Composition by Extension & Reason:**
- `.ambr`: 1490x Excluded (Unsupported Extension: '.ambr')
- `.yaml`: 11x Zero-Density Threshold (LOC: 65, Signals: 0), 11x Zero-Density Threshold (LOC: 69, Signals: 0), 11x Zero-Density Threshold (LOC: 53, Signals: 0)
- `.json`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1366 LOC), 2x Excluded (Static Asset Blob without Intent: 1431 LOC)
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Unsupported Format (.undeterminable), 8x Excluded (Machine-Generated Source Code Signature: 8 LOC)
- `.py`: 1x Excluded (Saturation: Line 11 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 349 LOC), 1x Excluded (Machine-Generated Source Code Signature: 175 LOC)
- `.xml`: 17x Excluded (Saturation: Line 1 exceeds 500 chars), 7x Excluded (Saturation: Line 2 exceeds 500 chars), 3x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.tar`: 17x Excluded (Explicitly Denied Extension: '.tar')
- `.yml`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 52, Signals: 0)
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pls`: 9x Excluded (Unsupported Extension: '.pls')
- `.toml`: 8x Excluded (Unsupported Extension: '.toml')
- `.jpg`: 8x Excluded (Explicitly Denied Extension: '.jpg')
- `.mp3`: 7x Excluded (Explicitly Denied Extension: '.mp3')
- `.pcm`: 5x Excluded (Unsupported Extension: '.pcm')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 81.6 | 13.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 39.6 | 37.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.7 | 7.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 48.9 | 32.5 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 51.7 | 55.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 47.6 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.9 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 31.8 | 11.1 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 14583 | 3955 | 2 | `tests/components/statistics/test_sensor.py` |
| cleanup | 434 | 258 | 0 | `tests/helpers/test_aiohttp_client.py` |
| guards | 214480 | 11882 | 22 | `tests/components/zwave_js/test_config_flow.py` |
| danger | 50450 | 8261 | 6 | `homeassistant/helpers/config_validation.py` |
| concurrency | 210063 | 12909 | 22 | `tests/test_config_entries.py` |
| connectivity | 106618 | 14391 | 11 | `tests/test_config_entries.py` |
| io | 6039 | 2252 | 0 | `tests/test_config.py` |
| crypto | 120 | 104 | 0 | `homeassistant/components/http/__init__.py` |
| ipc | 857 | 524 | 0 | `homeassistant/util/package.py` |
| time | 8653 | 2103 | 0 | `tests/components/sensor/test_recorder.py` |
| serialization | 3 | 3 | 0 | `homeassistant/components/flux_led/light.py` |
| regex | 244 | 134 | 0 | `pylint/plugins/hass_imports.py` |
| events | 12700 | 3039 | 2 | `homeassistant/components/teslemetry/sensor.py` |
| tests | 116795 | 6127 | 16 | `tests/test_config_entries.py` |
| docs | 132063 | 16715 | 14 | `tests/test_config_entries.py` |
| debt | 4177 | 773 | 0 | `tests/test_config_entries.py` |
| mutation | 749002 | 14876 | 81 | `tests/test_config_entries.py` |
| dead_code | 22071 | 4209 | 2 | `tests/test_core.py` |
| credential | 704 | 289 | 0 | `tests/components/freedompro/const.py` |
| threat | 11257 | 3508 | 1 | `homeassistant/components/sonarr/helpers.py` |
| ml_ai | 929 | 319 | 0 | `tests/components/melcloud/test_config_flow.py` |
| ui | 683 | 44 | 0 | `tests/helpers/template/test_init.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.3333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/test_config.py` (Hits: 59)
- `tests/components/backup/test_manager.py` (Hits: 58)
- `tests/helpers/test_aiohttp_client.py` (Hits: 54)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **core.py** (`homeassistant/core.py`) — 12259 inbound connections
2. **common.py** (`tests/common.py`) — 4675 inbound connections
3. **config_entries.py** (`homeassistant/config_entries.py`) — 4199 inbound connections
4. **logging.py** (`homeassistant/util/logging.py`) — 3387 inbound connections
5. **entity_platform.py** (`homeassistant/helpers/entity_platform.py`) — 2942 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **conftest.py** (`tests/conftest.py`) — 75 outbound dependencies
2. **__init__.py** (`homeassistant/components/http/__init__.py`) — 56 outbound dependencies
3. **__init__.py** (`homeassistant/components/homekit/__init__.py`) — 51 outbound dependencies
4. **helpers.py** (`homeassistant/components/zha/helpers.py`) — 50 outbound dependencies
5. **__init__.py** (`homeassistant/helpers/template/__init__.py`) — 50 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_async_update_device` **(Many-Argument Workhorses)** (@ `homeassistant/helpers/device_registry.py`) -> Impact: **349.0** | LOC: 303
- `async_match_targets` **(Many-Argument Workhorses)** (@ `homeassistant/helpers/intent.py`) -> Impact: **251.0** | LOC: 267
- `async_get_broker_settings` **(Many-Argument Workhorses)** (@ `homeassistant/components/mqtt/config_flow.py`) -> Impact: **196.0** | LOC: 322
- `async_get_or_create` **(Many-Argument Workhorses)** (@ `homeassistant/helpers/device_registry.py`) -> Impact: **193.8** | LOC: 177
- `_async_update_entity` **(Many-Argument Workhorses)** (@ `homeassistant/helpers/entity_registry.py`) -> Impact: **192.4** | LOC: 173
- `compile_statistics` **(Many-Argument Workhorses)** (@ `homeassistant/components/sensor/recorder.py`) -> Impact: **166.6** | LOC: 294
- `put` **(Many-Argument Workhorses)** (@ `homeassistant/components/emulated_hue/hue_api.py`) -> Impact: **157.4** | LOC: 286
- `get_accessory` **(Many-Argument Workhorses)** (@ `homeassistant/components/homekit/accessories.py`) -> Impact: **155.8** | LOC: 177
- `async_get_or_create` **(Many-Argument Workhorses)** (@ `homeassistant/helpers/entity_registry.py`) -> Impact: **155.4** | LOC: 200
- `_create_or_update_task` **(Many-Argument Workhorses)** (@ `homeassistant/components/habitica/services.py`) -> Impact: **145.6** | LOC: 282
  * *Intent:* """Create or update task action."""

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/helpers` | 69 | 37157.32 | 35.54% | 0.0% |
| `tests/components/mqtt` | 43 | 31193.68 | 23.68% | 0.0% |
| `homeassistant/helpers` | 74 | 28735.12 | 40.17% | 3.99% |
| `tests/components/recorder` | 39 | 21033.62 | 20.48% | 0.0% |
| `tests` | 25 | 19886.1 | 18.06% | 0.0% |
| `tests/components/zwave_js` | 34 | 19141.5 | 18.87% | 0.0% |
| `homeassistant/components/mqtt` | 52 | 12385.64 | 29.01% | 10.41% |
| `tests/components/shelly` | 25 | 12353.94 | 23.71% | 0.0% |
| `tests/components/esphome` | 41 | 12061.38 | 9.86% | 0.0% |
| `homeassistant/components/zwave_js` | 40 | 11490.26 | 31.68% | 11.73% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `homeassistant/components/nest/quality_scale.yaml` -> **100.0%** Exposure
- `homeassistant/components/rainbird/quality_scale.yaml` -> **100.0%** Exposure
- `homeassistant/components/russound_rnet/quality_scale.yaml` -> **100.0%** Exposure
- `homeassistant/components/ezviz/entity.py` -> **100.0%** Exposure
- `homeassistant/components/local_todo/todo.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `homeassistant/auth/auth_store.py` -> **100.0%** Exposure
- `homeassistant/components/abode/__init__.py` -> **100.0%** Exposure
- `homeassistant/components/abode/camera.py` -> **100.0%** Exposure
- `homeassistant/components/abode/config_flow.py` -> **100.0%** Exposure
- `homeassistant/components/abode/const.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_core.py` -> **147** Orphaned Functions | **54** Duplicates
- `tests/helpers/test_event.py` -> **87** Orphaned Functions | **67** Duplicates
- `tests/helpers/test_script.py` -> **127** Orphaned Functions | **5** Duplicates
- `tests/helpers/test_entity.py` -> **80** Orphaned Functions | **39** Duplicates
- `tests/components/config/test_config_entries.py` -> **56** Orphaned Functions | **54** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `homeassistant/components/growatt_server/number.py` -> **100.0%** Exposure
- `tests/components/anglian_water/const.py` -> **100.0%** Exposure
- `tests/components/senz/const.py` -> **100.0%** Exposure
- `tests/components/plex/fixtures/security_token.xml` -> **100.0%** Exposure
- `tests/components/lidarr/fixtures/initialize-wrong.js` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `46` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `127912` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/test_config_entries.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 6283.84 | **LOC:** 10053 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **36**; blast radius 0.017; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (72.3%), Guard Balance (formerly Safety Score) (31.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.2%)
- **Documentation Coverage:** 61.6628% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_update_entry_and_reload` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `test_unique_id_collision_issues` **(Many-Argument Workhorses)** (Impact: 16.4)
  * `test_saving_and_loading` **(Many-Argument Workhorses)** (Impact: 14.2)
  * `test_as_dict` **(Defensive Guards)** (Impact: 12.1)
    * *Intent:* """Test ConfigEntry.as_dict."""
  * `test_create_entry_next_flow` **(Defensive Guards)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 425 instances
* *Amplified Cascading Flux:* 71 instances
* *Concurrency (weighted view):* 3114
* *State Mutation (weighted view):* 968
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 2524`, `args: 434`, `func_start: 434`, `class_start: 104`
* *Risk/State:* `safety_bypasses: 109`, `state_mutation: 826`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 97`
* *Architecture:* `io: 1`, `api: 505`, `concurrency: 989`, `import: 34`
* *Defense:* `safety: 895`, `doc: 453`, `test: 431`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 4.4e-05
  * `Imports (Out-Degree: 16):` .common, __future__, asyncio, collections.abc, contextlib, datetime, freezegun.api, homeassistant...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/components/elmax/fixtures/direct/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/zwave_js/test_api.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 4633.6 | **LOC:** 6045 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (43.1%), Guard Balance (formerly Safety Score) (25.3%)
- **Documentation Coverage:** 97.2028% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_add_node` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `test_replace_failed_node` **(Many-Argument Workhorses)** (Impact: 30.2)
  * `test_update_log_config` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `test_node_metadata` **(Many-Argument Workhorses)** (Impact: 17.4)
  * `test_restore_nvm` **(Many-Argument Workhorses)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 511 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 3295
* *State Mutation (weighted view):* 663
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 1635`, `args: 71`, `func_start: 71`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 637`, `unreferenced_by_name: 66`
* *Architecture:* `io: 1`, `api: 71`, `concurrency: 740`, `import: 25`
* *Defense:* `safety: 736`, `doc: 68`, `test: 124`, `sync_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` aiohttp, asyncio, copy, homeassistant.components.websocket_api, homeassistant.components.zwave_js.api, homeassistant.components.zwave_js.const, homeassistant.components.zwave_js.helpers, homeassistant.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/helpers/test_script.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 4389.88 | **LOC:** 6901 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.7%), Guard Balance (formerly Safety Score) (46.2%)
- **Documentation Coverage:** 55.9871% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_repeat_nested` **(Many-Argument Workhorses)** (Impact: 42.6)
  * `test_if` **(Many-Argument Workhorses)** (Impact: 39.1)
  * `test_max_exceeded` **(Many-Argument Workhorses)** (Impact: 32.2)
  * `test_wait_variables_out` **(Defensive Guards)** (Impact: 29.3)
    * *Intent:* """Test the wait output variable."""
  * `test_repeat_conditional` **(Many-Argument Workhorses)** (Impact: 27.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 303 instances
* *Amplified Cascading Flux:* 162 instances
* *Concurrency (weighted view):* 2016
* *State Mutation (weighted view):* 1037
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 954`, `args: 156`, `func_start: 156`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 713`, `duplicate_logic: 5`, `unreferenced_by_name: 127`
* *Architecture:* `api: 154`, `concurrency: 501`, `import: 23`
* *Defense:* `safety: 464`, `doc: 144`, `test: 254`, `sync_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` asyncio, contextlib, datetime, freezegun, functools, homeassistant, homeassistant.components, homeassistant.const...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/sensor/test_recorder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 4374.84 | **LOC:** 6922 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (52.8%), Complexity Load (formerly Cognitive Load) (43.5%)
- **Documentation Coverage:** 85.9756% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_compile_statistics_hourly_daily_monthly_summary` **(Many-Argument Workhorses)** (Impact: 94.7)
  * `test_compile_hourly_statistics_changing_device_class_1` **(Many-Argument Workhorses)** (Impact: 29.6)
  * `verify_stats` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `test_list_statistic_ids` **(Many-Argument Workhorses)** (Impact: 27.1)
  * `test_compile_hourly_sum_statistics_amount` **(Many-Argument Workhorses)** (Impact: 25.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 390 instances
* *Amplified Cascading Flux:* 106 instances
* *Concurrency (weighted view):* 2558
* *State Mutation (weighted view):* 801
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 1010`, `args: 96`, `func_start: 87`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 589`, `fragile_debt: 3`, `duplicate_logic: 10`, `unreferenced_by_name: 59`
* *Architecture:* `api: 77`, `concurrency: 608`, `import: 28`
* *Defense:* `safety: 188`, `doc: 77`, `test: 344`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` .common, collections.abc, datetime, freezegun, freezegun.api, homeassistant, homeassistant.components.recorder, homeassistant.components.recorder.db_schema...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/logbook/test_websocket_api.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 3933.54 | **LOC:** 3205 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (42.2%), Guard Balance (formerly Safety Score) (20.0%)
- **Documentation Coverage:** 92.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_subscribe_unsubscribe_logbook_stream_included_entities` **(Many-Argument Workhorses)** (Impact: 22.4)
  * `test_subscribe_unsubscribe_logbook_stream` **(Many-Argument Workhorses)** (Impact: 19.3)
  * `test_subscribe_entities_some_have_uom_multiple` **(Defensive Guards)** (Impact: 17.2)
  * `test_subscribe_all_entities_are_continuous_with_device` **(Many-Argument Workhorses)** (Impact: 16.0)
  * `test_logbook_stream_excluded_entities_inherits_filters_from_recorder` **(Many-Argument Workhorses)** (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 507 instances
* *Amplified Cascading Flux:* 48 instances
* *Concurrency (weighted view):* 3140
* *State Mutation (weighted view):* 354
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 1158`, `args: 46`, `func_start: 46`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 258`, `unreferenced_by_name: 31`
* *Architecture:* `api: 39`, `concurrency: 605`, `import: 26`
* *Defense:* `safety: 479`, `doc: 42`, `test: 102`, `sync_locks: 5`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` asyncio, collections.abc, datetime, freezegun, homeassistant, homeassistant.components, homeassistant.components.automation, homeassistant.components.logbook...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/zwave_js/test_config_flow.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 3546.68 | **LOC:** 5566 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (79.3%), Complexity Load (formerly Cognitive Load) (39.9%)
- **Documentation Coverage:** 66.3551% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_reconfigure_migrate_with_addon` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `test_addon_rf_region_migrate_network` **(Many-Argument Workhorses)** (Impact: 10.5)
  * `test_usb_discovery_migration` **(Many-Argument Workhorses)** (Impact: 9.8)
  * `test_usb_discovery_migration_restore_driver_ready_timeout` **(Many-Argument Workhorses)** (Impact: 9.4)
  * `test_reconfigure_migrate_restore_driver_ready_timeout` **(Defensive Guards)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 379 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 2378
* *State Mutation (weighted view):* 535
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 1888`, `args: 108`, `func_start: 107`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 525`, `duplicate_logic: 17`
* *Architecture:* `io: 19`, `api: 107`, `concurrency: 483`, `import: 28`
* *Defense:* `safety: 984`, `doc: 91`, `test: 241`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` aiohasupervisor, aiohasupervisor.models, aiohttp, asyncio, collections.abc, copy, homeassistant, homeassistant.components.zwave_js.config_flow...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/recorder/test_websocket_api.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3464.96 | **LOC:** 4757 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (44.9%), Guard Balance (formerly Safety Score) (43.9%)
- **Documentation Coverage:** 91.4894% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_statistic_during_period` **(Many-Argument Workhorses)** (Impact: 113.1)
  * `test_statistic_during_period_hole` **(Many-Argument Workhorses)** (Impact: 36.9)
  * `test_statistic_during_period_partial_overlap` **(Many-Argument Workhorses)** (Impact: 27.6)
  * `test_list_statistic_ids` **(Many-Argument Workhorses)** (Impact: 25.7)
  * `test_statistic_during_period_circular_mean` **(Many-Argument Workhorses)** (Impact: 24.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 350 instances
* *Amplified Cascading Flux:* 86 instances
* *Concurrency (weighted view):* 2209
* *State Mutation (weighted view):* 623
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 978`, `args: 48`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 451`, `unreferenced_by_name: 42`
* *Architecture:* `io: 1`, `api: 46`, `concurrency: 459`, `import: 30`
* *Defense:* `safety: 324`, `doc: 43`, `test: 208`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` .common, .conftest, API, _pytest.python_api, collections.abc, datetime, freezegun, freezegun.api...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/shelly/test_config_flow.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 3397.96 | **LOC:** 5273 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (80.6%), Complexity Load (formerly Cognitive Load) (36.5%)
- **Documentation Coverage:** 87.9518% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_user_flow_with_ble_devices` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `test_bluetooth_provisioning_clears_match_history` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `test_zeroconf` **(Many-Argument Workhorses)** (Impact: 11.2)
  * `test_zeroconf_sleeping_device` **(Many-Argument Workhorses)** (Impact: 9.9)
  * `test_bluetooth_provision_timeout_ble_fallback_succeeds` **(Many-Argument Workhorses)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 340 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 2148
* *State Mutation (weighted view):* 553
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 1342`, `args: 112`, `func_start: 112`
* *Risk/State:* `safety_bypasses: 61`, `state_mutation: 479`
* *Architecture:* `api: 112`, `concurrency: 448`, `import: 26`
* *Defense:* `safety: 501`, `doc: 109`, `test: 380`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` , aioshelly.const, aioshelly.exceptions, collections.abc, dataclasses, datetime, homeassistant, homeassistant.components.bluetooth...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/helpers/test_event.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 3204.26 | **LOC:** 5000 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.8%), Guard Balance (formerly Safety Score) (39.0%)
- **Documentation Coverage:** 73.2804% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_track_template_result_super_template_2` **(Defensive Guards)** (Impact: 29.4)
  * `test_track_template_result_super_template_2_initially_false` **(Defensive Guards)** (Impact: 29.4)
  * `test_track_template_result_super_template_initially_false` **(Defensive Guards)** (Impact: 24.7)
  * `test_track_template_result_super_template` **(Defensive Guards)** (Impact: 24.5)
    * *Intent:* """Test tracking template with super template listening to same entity."""
  * `test_track_template_result_none` **(Defensive Guards)** (Impact: 19.3)
    * *Intent:* """Test tracking template."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 161 instances
* *Amplified Cascading Flux:* 95 instances
* *Concurrency (weighted view):* 1290
* *State Mutation (weighted view):* 827
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 1385`, `args: 230`, `func_start: 191`
* *Risk/State:* `safety_bypasses: 159`, `state_mutation: 637`, `duplicate_logic: 67`, `unreferenced_by_name: 87`
* *Architecture:* `io: 4`, `api: 187`, `concurrency: 485`, `import: 22`
* *Defense:* `safety: 728`, `doc: 95`, `test: 121`, `sync_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` astral, astral.sun, asyncio, collections.abc, contextlib, datetime, freezegun, freezegun.api...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/alexa/test_smart_home.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3129.08 | **LOC:** 5871 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (38.0%), Guard Balance (formerly Safety Score) (21.8%)
- **Documentation Coverage:** 17.5439% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_thermostat` **(Defensive Guards)** (Impact: 16.3)
    * *Intent:* """Test thermostat discovery."""
  * `test_valve_position` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `assert_percentage_changes` **(Many-Argument Workhorses)** (Impact: 13.0)
  * `test_water_heater` **(Defensive Guards)** (Impact: 12.9)
    * *Intent:* """Test water_heater discovery."""
  * `get_capability` **(Compute Cores)** (Impact: 12.4)
    * *Intent:* """Search a set of capabilities for a specific one."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 282 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 1830
* *State Mutation (weighted view):* 598
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 1339`, `args: 114`, `func_start: 114`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 570`, `unreferenced_by_name: 105`
* *Architecture:* `io: 20`, `api: 114`, `concurrency: 420`, `import: 19`
* *Defense:* `safety: 762`, `doc: 115`, `test: 154`, `sync_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .test_common, homeassistant.components, homeassistant.components.alexa, homeassistant.components.climate, homeassistant.components.cover, homeassistant.components.media_player, homeassistant.components.vacuum, homeassistant.components.valve...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/websocket_api/test_commands.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 3057.08 | **LOC:** 4349 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (35.9%), Guard Balance (formerly Safety Score) (24.9%)
- **Documentation Coverage:** 94.7644% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_assert_extract_from_target_command_result` **(Stateful Encapsulated Methods)** (Impact: 25.1)
  * `test_get_triggers_conditions_for_target` **(Many-Argument Workhorses)** (Impact: 23.5)
  * `test_get_services_for_target` **(Many-Argument Workhorses)** (Impact: 21.8)
  * `_apply_entities_changes` **(Stateful Encapsulated Methods)** (Impact: 16.6)
    * *Intent:* """Apply a diff set to a dict. Port of the client side merging """
  * `test_render_template_error_in_template_code` **(Many-Argument Workhorses)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 290 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 1885
* *State Mutation (weighted view):* 489
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 1365`, `args: 119`, `func_start: 101`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 403`, `duplicate_logic: 7`, `unreferenced_by_name: 71`
* *Architecture:* `api: 93`, `concurrency: 435`, `import: 33`
* *Defense:* `safety: 521`, `doc: 97`, `test: 149`, `sync_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` asyncio, copy, homeassistant, homeassistant.components.device_automation, homeassistant.components.group, homeassistant.components.light, homeassistant.components.logger, homeassistant.components.websocket_api...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/config_entries.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 3019.06 | **LOC:** 4084 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4199** in-repo importer(s); it depends on **47**; blast radius 16.303; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.3%), Connectivity (formerly Api Exposure) (76.5%)
- **Documentation Coverage:** 46.7532% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__async_setup_with_context` **(Many-Argument Workhorses)** (Impact: 81.0)
  * `async_finish_flow` **(Many-Argument Workhorses)** (Impact: 64.2)
  * `_async_update_entry` **(Many-Argument Workhorses)** (Impact: 62.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 50.1)
  * `async_init` **(Many-Argument Workhorses)** (Impact: 49.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 77 instances
* *Amplified Cascading Flux:* 233 instances
* *Concurrency (weighted view):* 558
* *State Mutation (weighted view):* 834
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 446`, `structural_boundaries: 641`, `args: 178`, `func_start: 175`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 93`, `state_mutation: 368`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 146`, `concurrency: 173`, `import: 45`
* *Defense:* `safety: 53`, `doc: 212`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.303
  * `Choke Point (Betweenness):` 0.000294 | `Ripple Effect (Closeness):` 0.247765
  * `Imports (Out-Degree: 18):` , .components.bluetooth, .const, .core, .data_entry_flow, .exceptions, .helpers, .helpers.debounce...
  * `Imported By (In-Degree: 4199):` (Excluded from Brief to save tokens)

### `tests/components/backup/test_manager.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2999.92 | **LOC:** 3996 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.4%), Complexity Load (formerly Cognitive Load) (43.6%)
- **Documentation Coverage:** 84.7826% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_upload_progress_debounced` **(Defensive Guards)** (Impact: 24.4)
  * `test_initiate_backup` **(Many-Argument Workhorses)** (Impact: 24.2)
  * `test_initiate_backup_per_agent_encryption` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `test_initiate_backup_with_agent_error` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `test_upload_progress_event` **(Defensive Guards)** (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 350 instances
* *Amplified Cascading Flux:* 27 instances
* *Concurrency (weighted view):* 2166
* *State Mutation (weighted view):* 402
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 929`, `args: 47`, `func_start: 47`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 348`, `unreferenced_by_name: 39`
* *Architecture:* `io: 58`, `api: 45`, `concurrency: 416`, `import: 28`
* *Defense:* `safety: 305`, `doc: 44`, `test: 166`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .common, __future__, aiohttp, asyncio, collections.abc, dataclasses, datetime, freezegun.api...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/assist_pipeline/test_websocket.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2967.92 | **LOC:** 2731 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (38.8%), Guard Balance (formerly Safety Score) (33.6%)
- **Documentation Coverage:** 92.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_device_capture_override` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `test_device_capture` **(Many-Argument Workhorses)** (Impact: 17.4)
  * `test_wake_word_cooldown_different_entities` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `test_intent_progress_event` **(Many-Argument Workhorses)** (Impact: 12.8)
  * `test_wake_word_cooldown_same_id` **(Many-Argument Workhorses)** (Impact: 11.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 338 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 2102
* *State Mutation (weighted view):* 488
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 1020`, `args: 50`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 424`, `duplicate_logic: 2`, `unreferenced_by_name: 45`
* *Architecture:* `api: 51`, `concurrency: 412`, `import: 16`
* *Defense:* `safety: 357`, `doc: 48`, `test: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .conftest, asyncio, base64, collections.abc, homeassistant.components, homeassistant.components.assist_pipeline.const, homeassistant.components.assist_pipeline.pipeline, homeassistant.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_core.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2730.08 | **LOC:** 3325 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (25.0%), Guard Balance (formerly Safety Score) (20.5%), Connectivity (formerly Api Exposure) (11.6%)
- **Documentation Coverage:** 38.9222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_async_get_hass_can_be_called` **(Stateful Encapsulated Methods)** (Impact: 11.6)
    * *Intent:* """Test calling async_get_hass via different paths. The test asserts async_get_hass can be called fr...
  * `test_stage_shutdown_with_exit_code` **(Defensive Guards)** (Impact: 10.4)
    * *Intent:* """Simulate a shutdown, test calling stuff with exit code checks."""
  * `test_async_all` **(Defensive Guards)** (Impact: 6.9)
    * *Intent:* """Test async_all."""
  * `test_chained_logging_hits_log_timeout` **(Stateful Encapsulated Methods)** (Impact: 6.5)
  * `test_chained_logging_misses_log_timeout` **(Stateful Encapsulated Methods)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 219 instances
* *Amplified Cascading Flux:* 33 instances
* *Concurrency (weighted view):* 1513
* *State Mutation (weighted view):* 362
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 993`, `args: 273`, `func_start: 268`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 72`, `state_mutation: 296`, `dead_code: 2`, `duplicate_logic: 54`, `unreferenced_by_name: 147`
* *Architecture:* `api: 233`, `concurrency: 418`, `import: 26`
* *Defense:* `safety: 426`, `doc: 183`, `test: 228`, `sync_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .common, __future__, array, asyncio, datetime, freezegun, functools, gc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/logbook/test_init.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2721.78 | **LOC:** 3005 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (73.5%), Complexity Load (formerly Cognitive Load) (36.7%)
- **Documentation Coverage:** 83.6066% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_assert_entry` **(Stateful Encapsulated Methods)** (Impact: 20.8)
  * `test_logbook_entity_context_parent_id` **(Defensive Guards)** (Impact: 12.5)
  * `test_logbook_entity_context_id` **(Defensive Guards)** (Impact: 11.0)
  * `test_get_events_with_device_ids` **(Defensive Guards)** (Impact: 10.9)
  * `test_logbook_select_entities_context_id` **(Defensive Guards)** (Impact: 10.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 291 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 1918
* *State Mutation (weighted view):* 392
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 910`, `args: 64`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 346`
* *Architecture:* `api: 60`, `concurrency: 463`, `import: 28`
* *Defense:* `safety: 404`, `doc: 64`, `test: 119`, `sync_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` .common, asyncio, collections.abc, datetime, freezegun, homeassistant, homeassistant.components, homeassistant.components.alexa.smart_home...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/config/test_config_entries.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2677.24 | **LOC:** 3666 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.1%), Complexity Load (formerly Cognitive Load) (50.9%), Guard Balance (formerly Safety Score) (41.2%)
- **Documentation Coverage:** 73.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_get_matching_entries_ws` **(Many-Argument Workhorses)** (Impact: 20.7)
  * `test_get_progress_subscribe_in_progress` **(Defensive Guards)** (Impact: 16.3)
  * `test_get_progress_subscribe` **(Defensive Guards)** (Impact: 16.0)
  * `test_get_progress_subscribe_in_progress_bad_flow` **(Defensive Guards)** (Impact: 14.3)
  * `test_subscribe_entries_ws_filtered` **(Many-Argument Workhorses)** (Impact: 13.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 248 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 1620
* *State Mutation (weighted view):* 351
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 1005`, `args: 134`, `func_start: 133`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 317`, `duplicate_logic: 54`, `unreferenced_by_name: 56`
* *Architecture:* `io: 1`, `api: 176`, `concurrency: 380`, `import: 23`
* *Defense:* `safety: 279`, `doc: 85`, `test: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` aiohttp.test_utils, collections.abc, freezegun.api, homeassistant, homeassistant.components.config, homeassistant.config_entries, homeassistant.const, homeassistant.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/components/google_assistant/trait.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2573.48 | **LOC:** 2895 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 4.1152% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `execute` **(Many-Argument Workhorses)** (Impact: 62.7)
    * *Intent:* """Execute a temperature point or mode command."""
  * `execute` **(Many-Argument Workhorses)** (Impact: 36.8)
    * *Intent:* """Execute an Open, close, Set position command."""
  * `execute` **(Many-Argument Workhorses)** (Impact: 29.8)
    * *Intent:* """Execute a SetModes command."""
  * `execute` **(Many-Argument Workhorses)** (Impact: 29.7)
    * *Intent:* """Execute a media command."""
  * `execute` **(Many-Argument Workhorses)** (Impact: 28.8)
    * *Intent:* """Execute an ArmDisarm command."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 43 instances
* *Amplified Cascading Flux:* 288 instances
* *Concurrency (weighted view):* 297
* *State Mutation (weighted view):* 1032
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 364`, `structural_boundaries: 424`, `args: 130`, `func_start: 130`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 98`, `state_mutation: 456`, `planned_debt: 1`, `duplicate_logic: 13`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 137`, `concurrency: 82`, `import: 28`
* *Defense:* `safety: 4`, `doc: 149`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .const, .error, __future__, abc, datetime, homeassistant.components, homeassistant.components.alarm_control_panel, homeassistant.components.camera...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/zha/test_config_flow.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2528.6 | **LOC:** 3630 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.4%), Connectivity (formerly Api Exposure) (80.9%), Complexity Load (formerly Cognitive Load) (34.7%)
- **Documentation Coverage:** 48.3871% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_plug_in_new_radio_retry` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `consume_progress_flow` **(Defensive Guards)** (Impact: 10.2)
  * `test_options_flow_defaults` **(Many-Argument Workhorses)** (Impact: 9.5)
  * `test_plug_in_old_radio_retry` **(Many-Argument Workhorses)** (Impact: 9.4)
    * *Intent:* """Test plug_in_old_radio step when reset fails due to unplugged adapter."""
  * `test_plug_in_old_radio_config_entry_removed` **(Many-Argument Workhorses)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 275 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 1716
* *State Mutation (weighted view):* 333
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 926`, `args: 94`, `func_start: 92`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 321`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 9`, `api: 93`, `concurrency: 341`, `import: 33`
* *Defense:* `safety: 328`, `doc: 88`, `test: 264`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` asyncio, collections.abc, datetime, homeassistant, homeassistant.components.hassio, homeassistant.components.usb, homeassistant.components.zha, homeassistant.components.zha.const...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/helpers/test_condition.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2522.68 | **LOC:** 3942 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 62.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (69.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.5%)
- **Documentation Coverage:** 48.4305% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_async_get_all_descriptions` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `test_numeric_state_raises` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* """Test that numeric_state raises ConditionError on errors."""
  * `assert_element` **(Defensive Guards)** (Impact: 12.9)
    * *Intent:* """Assert a trace element is as expected. Note: Unused variable 'path' is passed to get helpful erro...
  * `test_subscribe_conditions_experimental_conditions` **(Many-Argument Workhorses)** (Impact: 11.0)
  * `test_subscribe_conditions` **(Stateful Encapsulated Methods)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 224 instances
* *Amplified Cascading Flux:* 64 instances
* *Concurrency (weighted view):* 1428
* *State Mutation (weighted view):* 426
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 836`, `args: 117`, `func_start: 114`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 298`, `duplicate_logic: 16`, `unreferenced_by_name: 83`
* *Architecture:* `io: 3`, `api: 111`, `concurrency: 308`, `import: 30`
* *Defense:* `safety: 284`, `doc: 107`, `test: 211`, `sync_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` collections.abc, contextlib, datetime, freezegun, homeassistant.components.device_automation, homeassistant.components.light, homeassistant.components.sensor, homeassistant.components.sun...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/conversation/test_default_agent.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2498.06 | **LOC:** 3668 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (34.7%), Guard Balance (formerly Safety Score) (28.1%)
- **Documentation Coverage:** 59.375% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_satellite_area_context` **(Many-Argument Workhorses)** (Impact: 47.0)
  * `test_fuzzy_matching` **(Many-Argument Workhorses)** (Impact: 15.8)
  * `test_intent_tool_call_in_chat_log` **(Defensive Guards)** (Impact: 13.7)
    * *Intent:* """Test that intent tool calls are stored in the chat log."""
  * `test_handle_failed_intents` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `test_handle_intents_with_response_errors` **(Many-Argument Workhorses)** (Impact: 11.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 206 instances
* *Amplified Cascading Flux:* 52 instances
* *Concurrency (weighted view):* 1319
* *State Mutation (weighted view):* 565
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 844`, `args: 94`, `func_start: 94`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 461`, `duplicate_logic: 6`, `unreferenced_by_name: 83`
* *Architecture:* `io: 7`, `api: 94`, `concurrency: 289`, `import: 25`
* *Defense:* `safety: 433`, `doc: 87`, `test: 180`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` , collections, hassil.recognize, homeassistant.components, homeassistant.components.conversation, homeassistant.components.conversation.chat_log, homeassistant.components.conversation.default_agent, homeassistant.components.conversation.models...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/hassio/test_backup.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2451.7 | **LOC:** 2996 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (50.6%), Complexity Load (formerly Cognitive Load) (41.6%)
- **Documentation Coverage:** 88.3721% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_reader_writer_create_per_agent_encryption` **(Many-Argument Workhorses)** (Impact: 27.7)
  * `test_agent_upload` **(Many-Argument Workhorses)** (Impact: 24.1)
  * `test_reader_writer_create_report_progress` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `test_reader_writer_restore_report_progress` **(Many-Argument Workhorses)** (Impact: 15.0)
  * `mock_backup_agent` **(Generic / Templated Code)** (Impact: 14.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 261 instances
* *Amplified Cascading Flux:* 53 instances
* *Concurrency (weighted view):* 1621
* *State Mutation (weighted view):* 437
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 700`, `args: 43`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 331`, `unreferenced_by_name: 33`
* *Architecture:* `io: 1`, `api: 42`, `concurrency: 316`, `import: 26`
* *Defense:* `safety: 223`, `doc: 44`, `test: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .test_init, aiohasupervisor.exceptions, aiohasupervisor.models, aiohasupervisor.models.backups, aiohasupervisor.models.mounts, collections.abc, dataclasses, datetime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/components/recorder/statistics.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2423.7 | **LOC:** 3203 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **37**; blast radius 0.068; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.6%)
- **Documentation Coverage:** 71.8954% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `statistic_during_period` **(Many-Argument Workhorses)** (Impact: 105.5)
  * `_statistics_during_period_with_session` **(Many-Argument Workhorses)** (Impact: 81.6)
  * `_reduce_statistics` **(Many-Argument Workhorses)** (Impact: 72.2)
  * `_sorted_statistics_to_dict` **(Many-Argument Workhorses)** (Impact: 70.2)
  * `_get_max_mean_min_statistic_in_sub_period` **(Many-Argument Workhorses)** (Impact: 67.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 310 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 1005
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 399`, `args: 127`, `func_start: 103`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 385`, `dead_code: 4`
* *Architecture:* `io: 5`, `api: 48`, `concurrency: 4`, `import: 37`
* *Defense:* `safety: 16`, `doc: 109`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.068
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001135
  * `Imports (Out-Degree: 13):` , .const, .db_schema, .migration, .models, .util, __future__, collections...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `tests/helpers/test_entity.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2370.4 | **LOC:** 2968 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (52.5%), Guard Balance (formerly Safety Score) (30.2%)
- **Documentation Coverage:** 54.1254% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_async_parallel_updates_with_one` **(Defensive Guards)** (Impact: 15.0)
    * *Intent:* """Test parallel updates with 1 (sequential)."""
  * `test_extending_entity_description` **(Defensive Guards)** (Impact: 14.2)
    * *Intent:* """Test extending entity descriptions."""
  * `test_async_parallel_updates_with_two` **(Defensive Guards)** (Impact: 11.8)
    * *Intent:* """Test parallel updates with 2 (parallel)."""
  * `test_cached_entity_property_class_attribute` **(Defensive Guards)** (Impact: 10.4)
    * *Intent:* """Test entity properties on class level work in derived classes."""
  * `test_entity_name_translation_placeholder_errors` **(Many-Argument Workhorses)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 183 instances
* *Amplified Cascading Flux:* 26 instances
* *Concurrency (weighted view):* 1169
* *State Mutation (weighted view):* 528
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 806`, `args: 153`, `func_start: 147`, `class_start: 62`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 476`, `dead_code: 1`, `fragile_debt: 4`, `duplicate_logic: 39`, `unreferenced_by_name: 80`
* *Architecture:* `api: 185`, `concurrency: 254`, `import: 23`
* *Defense:* `safety: 383`, `doc: 139`, `test: 151`, `sync_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` asyncio, collections.abc, dataclasses, datetime, freezegun.api, homeassistant.config_entries, homeassistant.const, homeassistant.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `homeassistant/helpers/trigger.py` -> Churn: **79.42%** | Cog Load: 51.9357% | Debt: 15.6075%
- `homeassistant/bootstrap.py` -> Churn: **76.98%** | Cog Load: 66.4212% | Debt: 9.7112%
- `tests/helpers/test_trigger.py` -> Churn: **61.61%** | Cog Load: 64.9849% | Debt: 0.0%
- `homeassistant/components/unifi_access/__init__.py` -> Churn: **56.46%** | Cog Load: 47.0238% | Debt: 92.4142%
- `tests/helpers/test_condition.py` -> Churn: **56.46%** | Cog Load: 69.2111% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/components/zwave_js/test_api.py` -> **AlCalzone** (100.0% isolated ownership) | Magnitude: 4633.6
- `tests/components/sensor/test_recorder.py` -> **Sab44** (100.0% isolated ownership) | Magnitude: 4374.84
- `tests/components/zwave_js/test_config_flow.py` -> **Mike Degatano** (100.0% isolated ownership) | Magnitude: 3546.68
- `tests/components/assist_pipeline/test_websocket.py` -> **Artur Pragacz** (100.0% isolated ownership) | Magnitude: 2967.92
- `homeassistant/components/google_assistant/trait.py` -> **Kyle Johnson** (100.0% isolated ownership) | Magnitude: 2573.48

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `homeassistant/core.py` -> **Severity: 0.071** (Bridge: 0.0007 * Flux: 99.9945%)
- `homeassistant/config_entries.py` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 99.9906%)
- `homeassistant/core_config.py` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 99.9935%)
- `homeassistant/helpers/entity.py` -> **Severity: 0.018** (Bridge: 0.0002 * Flux: 100.0%)
- `homeassistant/helpers/entity_platform.py` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `homeassistant/core.py` -> **Severity: 51.161** (Embedded: 0.5321 * Error Risk: 96.1546%)
- `homeassistant/util/logging.py` -> **Severity: 34.347** (Embedded: 0.3447 * Error Risk: 99.6285%)
- `homeassistant/helpers/typing.py` -> **Severity: 28.904** (Embedded: 0.3119 * Error Risk: 92.6705%)
- `homeassistant/util/async_.py` -> **Severity: 26.822** (Embedded: 0.295 * Error Risk: 90.9162%)
- `homeassistant/helpers/entity.py` -> **Severity: 26.768** (Embedded: 0.2931 * Error Risk: 91.334%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `homeassistant/core.py` -> **Severity: 5702.51** (Blast Radius: 151.698 * Doc Risk: 37.5912%)
- `homeassistant/util/logging.py` -> **Severity: 4666.819** (Blast Radius: 87.846 * Doc Risk: 53.125%)
- `homeassistant/helpers/translation.py` -> **Severity: 1283.158** (Blast Radius: 19.504 * Doc Risk: 65.7895%)
- `homeassistant/util/async_.py` -> **Severity: 1105.342** (Blast Radius: 23.335 * Doc Risk: 47.3684%)
- `homeassistant/util/json.py` -> **Severity: 890.871** (Blast Radius: 20.787 * Doc Risk: 42.8571%)

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
