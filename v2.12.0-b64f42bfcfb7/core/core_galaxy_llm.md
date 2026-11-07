# ARCHITECTURAL_BRIEF: core
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/home-assistant/core.git` |
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
- **Scope:** 22700 analyzed artifact(s), 2860007 LOC.
- **Load-bearing artifact:** `homeassistant/core.py` -- 12291 in-repo importer(s) depend on it. Changes here propagate furthest.
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
| Analyzed Artifacts (Scanned) | 22700 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2118 |
| Total LOC | 2860007 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 91.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3586 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1495 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.1951 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 205 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 16679 | 2397211 | 73.5% |
| JSON | 5373 | 444655 | 23.7% |
| YAML | 542 | 17876 | 2.4% |
| XML | 63 | 0 | 0.3% |
| PLAINTEXT | 15 | 1 | 0.1% |
| MARKDOWN | 12 | 0 | 0.1% |
| SHELL | 12 | 192 | 0.1% |
| JAVASCRIPT | 2 | 24 | 0.0% |
| DOCKERFILE | 1 | 43 | 0.0% |
| CSV | 1 | 5 | 0.0% |

## 4.1 SOURCE ENCODINGS
All 22700 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 35%, Generic / Templated Code Files 29%, Large Core Modules (2) 18%, Encapsulated Accessors Files 5%, Declarative / Non-Code 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 22673 | 99.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 26 | 0.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2118*

**Composition by Extension & Reason:**
- `.ambr`: 1490x Excluded (Unsupported Extension: '.ambr')
- `.yaml`: 11x Zero-Density Threshold (LOC: 65, Signals: 0), 11x Zero-Density Threshold (LOC: 69, Signals: 0), 11x Zero-Density Threshold (LOC: 53, Signals: 0)
- `.json`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1366 LOC), 2x Excluded (Static Asset Blob without Intent: 1431 LOC)
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Unsupported Format (.undeterminable), 8x Excluded (Machine-Generated Source Code Signature: 8 LOC)
- `.xml`: 17x Excluded (Saturation: Line 1 exceeds 500 chars), 7x Excluded (Saturation: Line 2 exceeds 500 chars), 3x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 11 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 349 LOC)
- `.tar`: 17x Excluded (Explicitly Denied Extension: '.tar')
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.pls`: 9x Excluded (Unsupported Extension: '.pls')
- `.toml`: 8x Excluded (Unsupported Extension: '.toml')
- `.jpg`: 8x Excluded (Explicitly Denied Extension: '.jpg')
- `.md`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 39 LOC)
- `.mp3`: 7x Excluded (Explicitly Denied Extension: '.mp3')
- `.pcm`: 5x Excluded (Unsupported Extension: '.pcm')
- `.m3u`: 5x Excluded (Unsupported Extension: '.m3u')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 81.6 | 13.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.5 | 34.6 | 44.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 22.5 | 7.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 48.8 | 32.5 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 51.7 | 55.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 17.5 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.9 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 31.8 | 11.1 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 14584 | 3956 | 2 | `tests/components/statistics/test_sensor.py` |
| cleanup | 434 | 258 | 0 | `tests/helpers/test_aiohttp_client.py` |
| guards | 214689 | 11896 | 22 | `tests/components/zwave_js/test_config_flow.py` |
| danger | 50468 | 8266 | 6 | `homeassistant/helpers/config_validation.py` |
| concurrency | 210093 | 12920 | 22 | `tests/test_config_entries.py` |
| connectivity | 106814 | 14403 | 11 | `tests/test_config_entries.py` |
| io | 6077 | 2258 | 0 | `tests/test_config.py` |
| crypto | 81 | 70 | 0 | `homeassistant/components/http/__init__.py` |
| ipc | 279 | 168 | 0 | `homeassistant/util/package.py` |
| time | 8653 | 2103 | 0 | `tests/components/sensor/test_recorder.py` |
| serialization | 3 | 3 | 0 | `homeassistant/components/flux_led/light.py` |
| regex | 244 | 134 | 0 | `pylint/plugins/hass_imports.py` |
| events | 12712 | 3046 | 2 | `homeassistant/components/teslemetry/sensor.py` |
| tests | 116858 | 6129 | 16 | `tests/test_config_entries.py` |
| docs | 132192 | 16732 | 14 | `tests/test_config_entries.py` |
| debt | 4300 | 780 | 0 | `tests/test_config_entries.py` |
| mutation | 749302 | 14887 | 81 | `tests/test_config_entries.py` |
| dead_code | 20417 | 3712 | 2 | `tests/test_core.py` |
| credential | 888 | 378 | 0 | `tests/components/freedompro/const.py` |
| threat | 755 | 115 | 0 | `tests/components/switchbot/__init__.py` |
| ml_ai | 88 | 42 | 0 | `homeassistant/components/openai_conversation/entity.py` |
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

1. **core.py** (`homeassistant/core.py`) — 12291 inbound connections
2. **const.py** (`homeassistant/const.py`) — 8757 inbound connections
3. **config_entries.py** (`homeassistant/config_entries.py`) — 5185 inbound connections
4. **common.py** (`tests/common.py`) — 4700 inbound connections
5. **__init__.py** (`homeassistant/helpers/__init__.py`) — 4618 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **conftest.py** (`tests/conftest.py`) — 75 outbound dependencies
2. **__init__.py** (`homeassistant/components/homekit/__init__.py`) — 62 outbound dependencies
3. **__init__.py** (`homeassistant/components/http/__init__.py`) — 54 outbound dependencies
4. **config.py** (`homeassistant/components/template/config.py`) — 52 outbound dependencies
5. **helpers.py** (`homeassistant/components/zha/helpers.py`) — 50 outbound dependencies

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
| `tests/helpers` | 69 | 37168.12 | 35.54% | 0.0% |
| `tests/components/mqtt` | 43 | 31196.68 | 23.68% | 0.0% |
| `homeassistant/helpers` | 74 | 28735.12 | 40.17% | 3.42% |
| `tests/components/recorder` | 39 | 21033.62 | 20.48% | 0.0% |
| `tests` | 25 | 19886.1 | 18.06% | 0.0% |
| `tests/components/zwave_js` | 34 | 19141.5 | 18.87% | 0.0% |
| `homeassistant/components/mqtt` | 52 | 12396.64 | 29.01% | 3.25% |
| `tests/components/shelly` | 25 | 12353.94 | 23.71% | 0.0% |
| `tests/components/esphome` | 41 | 12061.38 | 9.86% | 0.0% |
| `homeassistant/components/zwave_js` | 40 | 11490.26 | 31.68% | 10.52% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `homeassistant/components/nest/quality_scale.yaml` -> **100.0%** Exposure
- `homeassistant/components/rainbird/quality_scale.yaml` -> **100.0%** Exposure
- `homeassistant/components/russound_rnet/quality_scale.yaml` -> **100.0%** Exposure
- `homeassistant/components/local_todo/todo.py` -> **100.0%** Exposure
- `homeassistant/components/risco/switch.py` -> **100.0%** Exposure
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
- `tests/components/ecobee/fixtures/ecobee-token.json` -> **100.0%** Exposure
- `tests/components/github/fixtures/device_activate.json` -> **100.0%** Exposure
- `tests/components/homewizard/fixtures/v2/generic/token.json` -> **100.0%** Exposure
- `tests/components/intellifire/fixtures/user_data_3.json` -> **100.0%** Exposure
- `tests/components/lametric/fixtures/cloud_devices.json` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `42` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `127710` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/test_config_entries.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.258)
- **Top Global Matches:** file_cluster_12: 8.258, file_cluster_5: 8.957, file_cluster_0: 9.27
- **Magnitude:** 6283.84 | **LOC:** 10053 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **34**; blast radius 0.019; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (72.3%), Guard Balance (formerly Safety Score) (43.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.2%)
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
* *Risk/State:* `safety_bypasses: 109`, `state_mutation: 826`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 97`
* *Architecture:* `io: 1`, `api: 505`, `concurrency: 989`, `import: 34`
* *Defense:* `safety: 895`, `doc: 453`, `test: 431`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 4.4e-05
  * `Imports (Out-Degree: 22):` .common, __future__, asyncio, collections.abc, contextlib, datetime, freezegun.api, homeassistant...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/components/zwave_js/test_api.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.064)
- **Top Global Matches:** file_cluster_15: 8.064, file_cluster_12: 8.586, file_cluster_0: 8.606
- **Magnitude:** 4633.6 | **LOC:** 6045 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (43.1%), Guard Balance (formerly Safety Score) (41.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` aiohttp, asyncio, copy, homeassistant.components.websocket_api, homeassistant.components.zwave_js.api, homeassistant.components.zwave_js.const, homeassistant.components.zwave_js.helpers, homeassistant.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/helpers/test_script.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.657)
- **Top Global Matches:** file_cluster_15: 7.657, file_cluster_0: 8.178, file_cluster_16: 8.619
- **Magnitude:** 4392.08 | **LOC:** 6901 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.7%), Guard Balance (formerly Safety Score) (48.7%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` asyncio, contextlib, datetime, freezegun, functools, homeassistant, homeassistant.components, homeassistant.const...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/sensor/test_recorder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.578)
- **Top Global Matches:** file_cluster_15: 8.578, file_cluster_16: 8.645, file_cluster_12: 9.319
- **Magnitude:** 4374.84 | **LOC:** 6922 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (50.9%), Complexity Load (formerly Cognitive Load) (43.5%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` .common, collections.abc, datetime, freezegun, freezegun.api, homeassistant, homeassistant.components.recorder, homeassistant.components.recorder.db_schema...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/logbook/test_websocket_api.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.659)
- **Top Global Matches:** file_cluster_12: 7.659, file_cluster_16: 8.799, file_cluster_0: 8.911
- **Magnitude:** 3933.54 | **LOC:** 3205 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (42.2%), Guard Balance (formerly Safety Score) (38.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` asyncio, collections.abc, datetime, freezegun, homeassistant, homeassistant.components, homeassistant.components.automation, homeassistant.components.logbook...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/zwave_js/test_config_flow.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.644)
- **Top Global Matches:** file_cluster_12: 8.644, file_cluster_0: 9.434, file_cluster_15: 10.108
- **Magnitude:** 3546.68 | **LOC:** 5566 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.018; role: Pure Consumer (Orchestrator)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` aiohasupervisor, aiohasupervisor.models, aiohttp, asyncio, collections.abc, copy, homeassistant, homeassistant.components.zwave_js.config_flow...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/recorder/test_websocket_api.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.459)
- **Top Global Matches:** file_cluster_4: 8.459, file_cluster_12: 9.242, file_cluster_16: 9.445
- **Magnitude:** 3464.96 | **LOC:** 4757 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (47.9%), Complexity Load (formerly Cognitive Load) (44.9%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` .common, .conftest, _pytest.python_api, collections.abc, datetime, freezegun, freezegun.api, homeassistant.components...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/shelly/test_config_flow.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.598)
- **Top Global Matches:** file_cluster_12: 7.598, file_cluster_5: 9.007, file_cluster_0: 9.11
- **Magnitude:** 3397.96 | **LOC:** 5273 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (80.6%), Guard Balance (formerly Safety Score) (41.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` .init_integration, aioshelly.const, aioshelly.exceptions, collections.abc, dataclasses, datetime, homeassistant, homeassistant.components.bluetooth...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/helpers/test_event.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.101)
- **Top Global Matches:** file_cluster_5: 7.101, file_cluster_12: 8.359, file_cluster_7: 10.003
- **Magnitude:** 3210.86 | **LOC:** 5000 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.8%), Guard Balance (formerly Safety Score) (46.2%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` astral, astral.sun, asyncio, collections.abc, contextlib, datetime, freezegun, freezegun.api...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/alexa/test_smart_home.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.117)
- **Top Global Matches:** file_cluster_0: 8.117, file_cluster_15: 8.492, file_cluster_12: 8.813
- **Magnitude:** 3129.08 | **LOC:** 5871 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (39.5%), Complexity Load (formerly Cognitive Load) (38.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` .test_common, homeassistant.components, homeassistant.components.alexa, homeassistant.components.climate, homeassistant.components.cover, homeassistant.components.media_player, homeassistant.components.vacuum, homeassistant.components.valve...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/websocket_api/test_commands.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.808)
- **Top Global Matches:** file_cluster_12: 7.808, file_cluster_0: 8.171, file_cluster_15: 8.425
- **Magnitude:** 3057.08 | **LOC:** 4349 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (40.8%), Complexity Load (formerly Cognitive Load) (35.9%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` asyncio, copy, homeassistant, homeassistant.components.device_automation, homeassistant.components.group, homeassistant.components.light, homeassistant.components.logger, homeassistant.components.websocket_api...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/config_entries.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.581)
- **Top Global Matches:** file_cluster_5: 7.581, file_cluster_12: 9.422, file_cluster_0: 11.056
- **Magnitude:** 3019.06 | **LOC:** 4084 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5185** in-repo importer(s); it depends on **43**; blast radius 21.289; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (76.5%), Guard Balance (formerly Safety Score) (66.2%)
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
* *Risk/State:* `safety_bypasses: 93`, `state_mutation: 368`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 146`, `concurrency: 173`, `import: 45`
* *Defense:* `safety: 53`, `doc: 212`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.289
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.368887
  * `Imports (Out-Degree: 26):` .components.bluetooth, .const, .core, .data_entry_flow, .exceptions, .helpers, .helpers.debounce, .helpers.discovery_flow...
  * `Imported By (In-Degree: 5185):` (Excluded from Brief to save tokens)

### `tests/components/backup/test_manager.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.89)
- **Top Global Matches:** file_cluster_12: 7.89, file_cluster_0: 8.807, file_cluster_16: 9.256
- **Magnitude:** 2999.92 | **LOC:** 3996 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.4%), Guard Balance (formerly Safety Score) (46.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` .common, __future__, aiohttp, asyncio, collections.abc, dataclasses, datetime, freezegun.api...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/assist_pipeline/test_websocket.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.625)
- **Top Global Matches:** file_cluster_12: 7.625, file_cluster_15: 8.389, file_cluster_0: 8.806
- **Magnitude:** 2967.92 | **LOC:** 2731 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (44.3%), Complexity Load (formerly Cognitive Load) (38.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` .conftest, asyncio, base64, collections.abc, homeassistant.components, homeassistant.components.assist_pipeline.const, homeassistant.components.assist_pipeline.pipeline, homeassistant.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_core.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.15)
- **Top Global Matches:** file_cluster_5: 8.15, file_cluster_12: 9.174, file_cluster_0: 11.186
- **Magnitude:** 2730.08 | **LOC:** 3325 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (38.8%), Complexity Load (formerly Cognitive Load) (25.0%), Connectivity (formerly Api Exposure) (11.6%)
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
* *Risk/State:* `safety_bypasses: 72`, `state_mutation: 296`, `duplicate_logic: 54`, `unreferenced_by_name: 147`
* *Architecture:* `api: 233`, `concurrency: 418`, `import: 26`
* *Defense:* `safety: 426`, `doc: 183`, `test: 228`, `sync_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` .common, __future__, array, asyncio, datetime, freezegun, functools, gc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/logbook/test_init.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.111)
- **Top Global Matches:** file_cluster_0: 8.111, file_cluster_15: 8.754, file_cluster_16: 8.94
- **Magnitude:** 2721.78 | **LOC:** 3005 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (73.5%), Guard Balance (formerly Safety Score) (39.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` .common, asyncio, collections.abc, datetime, freezegun, homeassistant, homeassistant.components, homeassistant.components.alexa.smart_home...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/config/test_config_entries.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.866)
- **Top Global Matches:** file_cluster_12: 7.866, file_cluster_0: 8.875, file_cluster_5: 8.998
- **Magnitude:** 2677.24 | **LOC:** 3666 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.1%), Complexity Load (formerly Cognitive Load) (50.9%), Guard Balance (formerly Safety Score) (47.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` aiohttp.test_utils, collections.abc, freezegun.api, homeassistant, homeassistant.components.config, homeassistant.config_entries, homeassistant.const, homeassistant.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/components/google_assistant/trait.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.859)
- **Top Global Matches:** file_cluster_5: 6.859, file_cluster_12: 8.268, file_cluster_7: 10.01
- **Magnitude:** 2573.48 | **LOC:** 2895 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **28**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.1%)
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
* *Risk/State:* `safety_bypasses: 98`, `state_mutation: 456`, `planned_debt: 1`, `duplicate_logic: 13`
* *Architecture:* `io: 4`, `api: 137`, `concurrency: 82`, `import: 28`
* *Defense:* `safety: 4`, `doc: 149`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.107667
  * `Imports (Out-Degree: 23):` .const, .error, __future__, abc, datetime, homeassistant.components, homeassistant.components.alarm_control_panel, homeassistant.components.camera...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/components/zha/test_config_flow.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.708)
- **Top Global Matches:** file_cluster_12: 7.708, file_cluster_5: 8.963, file_cluster_0: 9.678
- **Magnitude:** 2528.6 | **LOC:** 3630 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.4%), Connectivity (formerly Api Exposure) (80.9%), Guard Balance (formerly Safety Score) (42.2%)
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
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 321`, `duplicate_logic: 2`
* *Architecture:* `io: 9`, `api: 93`, `concurrency: 341`, `import: 33`
* *Defense:* `safety: 328`, `doc: 88`, `test: 264`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` asyncio, collections.abc, datetime, homeassistant, homeassistant.components.hassio, homeassistant.components.usb, homeassistant.components.zha, homeassistant.components.zha.const...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/helpers/test_condition.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.791)
- **Top Global Matches:** file_cluster_0: 7.791, file_cluster_12: 8.503, file_cluster_16: 9.046
- **Magnitude:** 2522.68 | **LOC:** 3942 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 62.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 0.018; role: Pure Consumer (Orchestrator)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` collections.abc, contextlib, datetime, freezegun, homeassistant.components.device_automation, homeassistant.components.light, homeassistant.components.sensor, homeassistant.components.sun...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/conversation/test_default_agent.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.542)
- **Top Global Matches:** file_cluster_0: 8.542, file_cluster_12: 8.917, file_cluster_15: 9.381
- **Magnitude:** 2498.06 | **LOC:** 3668 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (42.2%), Complexity Load (formerly Cognitive Load) (34.7%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` .expose_entity, .expose_new, collections, hassil.recognize, homeassistant.components, homeassistant.components.conversation, homeassistant.components.conversation.chat_log, homeassistant.components.conversation.default_agent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/hassio/test_backup.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.393)
- **Top Global Matches:** file_cluster_12: 7.393, file_cluster_5: 8.463, file_cluster_0: 9.055
- **Magnitude:** 2451.7 | **LOC:** 2996 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (50.1%), Complexity Load (formerly Cognitive Load) (41.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` .test_init, aiohasupervisor.exceptions, aiohasupervisor.models, aiohasupervisor.models.backups, aiohasupervisor.models.mounts, collections.abc, dataclasses, datetime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/components/recorder/statistics.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.386)
- **Top Global Matches:** file_cluster_4: 8.386, file_cluster_5: 10.866, file_cluster_12: 11.588
- **Magnitude:** 2423.7 | **LOC:** 3203 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **37**; blast radius 0.14; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.4%), Complexity Load (formerly Cognitive Load) (49.6%)
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
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 385`
* *Architecture:* `io: 5`, `api: 48`, `concurrency: 4`, `import: 37`
* *Defense:* `safety: 16`, `doc: 109`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.013829
  * `Imports (Out-Degree: 20):` .Recorder, .const, .db_schema, .migration, .models, .util, __future__, collections...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `tests/helpers/test_entity.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.303)
- **Top Global Matches:** file_cluster_12: 8.303, file_cluster_5: 8.511, file_cluster_0: 9.125
- **Magnitude:** 2370.4 | **LOC:** 2968 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **23**; blast radius 0.019; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (52.5%), Guard Balance (formerly Safety Score) (43.0%)
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
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 476`, `fragile_debt: 4`, `duplicate_logic: 39`, `unreferenced_by_name: 80`
* *Architecture:* `api: 185`, `concurrency: 254`, `import: 23`
* *Defense:* `safety: 383`, `doc: 139`, `test: 151`, `sync_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 4.4e-05
  * `Imports (Out-Degree: 12):` asyncio, collections.abc, dataclasses, datetime, freezegun.api, homeassistant.config_entries, homeassistant.const, homeassistant.core...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/components/recorder/test_init.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.759)
- **Top Global Matches:** file_cluster_12: 7.759, file_cluster_5: 7.92, file_cluster_0: 9.048
- **Magnitude:** 2289.72 | **LOC:** 2824 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (81.3%), Guard Balance (formerly Safety Score) (44.7%)
- **Documentation Coverage:** 81.3853% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_database_lock_and_overflow_checks_available_memory` **(Stateful Encapsulated Methods)** (Impact: 16.2)
  * `test_saving_event_exclude_event_type` **(Stateful Encapsulated Methods)** (Impact: 9.4)
  * `test_commit_before_commits_pending_writes` **(Many-Argument Workhorses)** (Impact: 9.3)
  * `test_service_disable_events_not_recording` **(Defensive Guards)** (Impact: 9.2)
  * `test_deduplication_event_data_inside_commit_interval` **(Defensive Guards)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 195 instances
* *Amplified Cascading Flux:* 43 instances
* *Api Near Db Sink:* 3 instances
* *Concurrency (weighted view):* 1280
* *State Mutation (weighted view):* 401
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 833`, `args: 124`, `func_start: 121`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 315`, `duplicate_logic: 11`
* *Architecture:* `io: 5`, `api: 117`, `concurrency: 305`, `import: 34`
* *Defense:* `safety: 258`, `doc: 93`, `test: 211`, `sync_locks: 13`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` .common, __future__, asyncio, collections.abc, datetime, freezegun.api, homeassistant.components, homeassistant.components.lock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/components/mcp/test_config_flow.py` (PYTHON) | Magnitude: 516.04 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 659, structural_boundaries: 189, core_var_decl: 142, design_snake_case: 129
- `tests/components/flux_led/test_diagnostics.py` (PYTHON) | Magnitude: 31.86 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 18, import: 6, concurrency: 4
- `tests/util/test_executor.py` (PYTHON) | Magnitude: 64.98 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 27, test: 14, args: 8
- `homeassistant/components/youtube/entity.py` (PYTHON) | Magnitude: 10.72 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 14, import: 6, state_mutation: 5
- `tests/components/huum/test_init.py` (PYTHON) | Magnitude: 63.84 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 48, safety: 14, test: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `homeassistant/components/matter/binary_sensor.py` (PYTHON) | Magnitude: 46.44 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 518, core_var_decl: 306, design_snake_case: 305, structural_boundaries: 35
- `tests/components/traccar_server/test_diagnostics.py` (PYTHON) | Magnitude: 81.4 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 34, core_var_decl: 16, design_snake_case: 16
- `tests/util/test_variance.py` (PYTHON) | Magnitude: 5.18 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 8, time_date_logic: 4, test: 3
- `tests/components/fressnapf_tracker/test_config_flow.py` (PYTHON) | Magnitude: 334.28 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 306, structural_boundaries: 144, safety: 53, concurrency: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/components/minecraft_server/conftest.py` (PYTHON) | Magnitude: 8.7 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 33, core_var_decl: 18, design_snake_case: 18, structural_boundaries: 17
- `tests/components/mikrotik/test_config_flow.py` (PYTHON) | Magnitude: 220.22 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 152, structural_boundaries: 93, core_var_decl: 40, design_snake_case: 38
- `tests/components/uptime_kuma/conftest.py` (PYTHON) | Magnitude: 23.28 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 109, core_var_decl: 74, design_snake_case: 73, structural_boundaries: 30
- `tests/components/shelly/test_update.py` (PYTHON) | Magnitude: 324.86 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 594, structural_boundaries: 262, safety: 183, state_mutation: 55
- `tests/components/insteon/test_lock.py` (PYTHON) | Magnitude: 75.38 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 45, test: 15, concurrency: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `homeassistant/components/switchbot_cloud/sensor.py` (PYTHON) | Magnitude: 95.26 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 242, core_var_decl: 103, design_snake_case: 72, state_mutation: 43
- `tests/components/obihai/test_config_flow.py` (PYTHON) | Magnitude: 138.8 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 73, safety: 26, core_var_decl: 26
- `tests/components/airzone_cloud/util.py` (PYTHON) | Magnitude: 72.8 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 509, structural_boundaries: 45, core_var_decl: 20, branch: 14
- `homeassistant/components/eheimdigital/select.py` (PYTHON) | Magnitude: 114.82 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 204, core_var_decl: 67, design_snake_case: 64, structural_boundaries: 41
- `homeassistant/components/opendisplay/__init__.py` (PYTHON) | Magnitude: 124.94 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 56, core_var_decl: 27, design_snake_case: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/components/whois/test_config_flow.py` (PYTHON) | Magnitude: 67.66 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 53, safety: 19, core_var_decl: 13
- `tests/components/deconz/test_siren.py` (PYTHON) | Magnitude: 22.32 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 26, import: 7, safety: 6
- `tests/components/trane/test_config_flow.py` (PYTHON) | Magnitude: 73.36 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 47, core_var_decl: 14, design_snake_case: 14
- `tests/components/twentemilieu/test_sensor.py` (PYTHON) | Magnitude: 9.88 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 17, safety: 7, state_mutation: 4
- `tests/components/lastfm/test_sensor.py` (PYTHON) | Magnitude: 15.02 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 12, test: 7, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `homeassistant/components/mullvad/config_flow.py` (PYTHON) | Magnitude: 31.46 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 14, state_mutation: 5, import: 5
- `tests/components/fjaraskupan/__init__.py` (PYTHON) | Magnitude: 16.32 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: core_var_decl: 13, indent_spaces: 12, design_snake_case: 12, structural_boundaries: 4
- `tests/components/casper_glow/__init__.py` (PYTHON) | Magnitude: 7.84 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 32, core_var_decl: 27, design_snake_case: 25, structural_boundaries: 10
- `homeassistant/components/toon/helpers.py` (PYTHON) | Magnitude: 11.62 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 19, indent_spaces: 12, import: 6, safety_bypasses: 5
- `homeassistant/components/rdw/diagnostics.py` (PYTHON) | Magnitude: 4.34 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 14, import: 6, indent_spaces: 4, safety_bypasses: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `homeassistant/components/coinbase/__init__.py` (PYTHON) | Magnitude: 76.44 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 38, state_mutation: 19, core_var_decl: 13
- `tests/components/number/test_reproduce_state.py` (PYTHON) | Magnitude: 17.48 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 18, safety: 5, import: 5
- `tests/components/met/__init__.py` (PYTHON) | Magnitude: 23.2 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 15, import: 5, core_var_decl: 5
- `tests/components/aurora_abb_powerone/test_init.py` (PYTHON) | Magnitude: 11.2 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 20, test: 8, core_var_decl: 8
- `tests/components/eheimdigital/test_climate.py` (PYTHON) | Magnitude: 186.74 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 174, structural_boundaries: 75, concurrency: 35, test: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/components/ssdp/test_init.py` (PYTHON) | Magnitude: 550.76 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 808, structural_boundaries: 240, safety: 118, core_var_decl: 114
- `homeassistant/components/overseerr/coordinator.py` (PYTHON) | Magnitude: 43.38 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 33, core_var_decl: 16, design_snake_case: 15
- `homeassistant/components/apsystems/entity.py` (PYTHON) | Magnitude: 26.5 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, core_var_decl: 10, design_snake_case: 10
- `homeassistant/components/google_drive/coordinator.py` (PYTHON) | Magnitude: 49.26 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 29, core_var_decl: 12, design_snake_case: 10
- `homeassistant/components/steamist/entity.py` (PYTHON) | Magnitude: 20.5 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 23, indent_spaces: 20, import: 9, core_var_decl: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `homeassistant/components/modem_callerid/const.py` (PYTHON) | Magnitude: 21.3 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 7, core_var_decl: 6, state_mutation: 5
- `homeassistant/components/adax/const.py` (PYTHON) | Magnitude: 21.2 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 8, state_mutation: 6, design_upper_case: 6, structural_boundaries: 3
- `homeassistant/components/mikrotik/const.py` (PYTHON) | Magnitude: 15.98 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: immutability_locks: 27, core_var_decl: 26, design_pascal_case: 26, indent_spaces: 20
- `homeassistant/components/brands/const.py` (PYTHON) | Magnitude: 15.78 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, immutability_locks: 12, structural_boundaries: 9, core_var_decl: 9
- `homeassistant/components/brother/const.py` (PYTHON) | Magnitude: 22.24 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 9, state_mutation: 7, design_upper_case: 7, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/components/airzone/test_binary_sensor.py` (PYTHON) | Magnitude: 44.64 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 36, safety: 26, state_mutation: 25
- `tests/components/water_heater/test_reproduce_state.py` (PYTHON) | Magnitude: 41.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 99, structural_boundaries: 41, safety: 26, state_mutation: 11
- `tests/components/luftdaten/test_sensor.py` (PYTHON) | Magnitude: 25.0 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 105, structural_boundaries: 81, safety: 66, state_mutation: 13
- `tests/components/aemet/test_sensor.py` (PYTHON) | Magnitude: 74.52 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 52, safety: 35, state_mutation: 35
- `homeassistant/components/cover/intent.py` (PYTHON) | Magnitude: 5.14 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 9, core_var_decl: 6, design_snake_case: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/components/tplink/test_init.py` (PYTHON) | Magnitude: 828.48 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 961, core_var_decl: 285, design_snake_case: 284, structural_boundaries: 264
- `homeassistant/components/huawei_lte/__init__.py` (PYTHON) | Magnitude: 401.98 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 371, structural_boundaries: 108, branch: 65, state_mutation: 60
- `homeassistant/helpers/service.py` (PYTHON) | Magnitude: 1003.64 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 805, structural_boundaries: 196, core_var_decl: 167, branch: 150
- `homeassistant/components/husqvarna_automower/coordinator.py` (PYTHON) | Magnitude: 300.62 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 243, branch: 66, structural_boundaries: 64, state_mutation: 43
- `homeassistant/components/hassio/issues.py` (PYTHON) | Magnitude: 263.08 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 291, structural_boundaries: 89, core_var_decl: 59, design_snake_case: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tests/components/webdav/test_backup.py` (PYTHON) | Magnitude: 525.56 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 348, structural_boundaries: 165, state_mutation: 71, concurrency: 69
- `tests/components/lg_infrared/conftest.py` (PYTHON) | Magnitude: 55.14 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 46, indent_spaces: 45, test: 15, import: 12
- `homeassistant/components/vodafone_station/button.py` (PYTHON) | Magnitude: 32.14 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 38, core_var_decl: 34, design_snake_case: 32
- `tests/components/statistics/test_init.py` (PYTHON) | Magnitude: 208.76 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 260, structural_boundaries: 122, core_var_decl: 70, design_snake_case: 70
- `tests/components/cloud/test_system_health.py` (PYTHON) | Magnitude: 66.4 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 35, concurrency: 11, import: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `homeassistant/components/immich/media_source.py` (PYTHON) | Magnitude: 310.32 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 267, core_var_decl: 91, design_snake_case: 88, structural_boundaries: 79
- `homeassistant/components/history/websocket_api.py` (PYTHON) | Magnitude: 449.76 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 415, structural_boundaries: 89, branch: 61, state_mutation: 52
- `homeassistant/components/proximity/coordinator.py` (PYTHON) | Magnitude: 210.64 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 267, structural_boundaries: 58, core_var_decl: 36, branch: 33
- `homeassistant/components/elevenlabs/tts.py` (PYTHON) | Magnitude: 285.82 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 214, structural_boundaries: 67, state_mutation: 56, core_var_decl: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `homeassistant/components/update/significant_change.py` (PYTHON) | Magnitude: 12.9 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 13, import: 4, branch: 3
- `tests/components/kegtron/__init__.py` (PYTHON) | Magnitude: 19.86 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 34, core_var_decl: 32, design_snake_case: 28, safety_bypasses: 8
- `tests/components/weatherkit/test_sensor.py` (PYTHON) | Magnitude: 11.88 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 11, import: 4, test: 3
- `homeassistant/components/alarmdecoder/const.py` (PYTHON) | Magnitude: 46.72 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: core_var_decl: 32, state_mutation: 31, design_upper_case: 31, indent_spaces: 3
- `tests/components/airthings_ble/__init__.py` (PYTHON) | Magnitude: 44.32 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 262, core_var_decl: 161, design_snake_case: 145, structural_boundaries: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/pylint/__init__.py` (PYTHON) | Magnitude: 30.16 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 7, branch: 5, state_mutation: 5
- `homeassistant/components/letpot/__init__.py` (PYTHON) | Magnitude: 96.52 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 41, import: 13, core_var_decl: 13
- `homeassistant/components/hr_energy_qube/config_flow.py` (PYTHON) | Magnitude: 57.26 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 21, core_var_decl: 10, state_mutation: 9
- `homeassistant/components/alarm_control_panel/significant_change.py` (PYTHON) | Magnitude: 29.98 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 12, branch: 7, import: 4
- `homeassistant/components/cover/device_action.py` (PYTHON) | Magnitude: 136.06 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 30, state_mutation: 28, core_var_decl: 20

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `homeassistant/helpers/trigger.py` -> Churn: **79.42%** | Cog Load: 51.9357% | Debt: 14.7365%
- `homeassistant/bootstrap.py` -> Churn: **76.98%** | Cog Load: 66.4212% | Debt: 9.1347%
- `.github/workflows/ci.yaml` -> Churn: **72.8%** | Cog Load: 7.6263% | Debt: 83.2165%
- `tests/helpers/test_trigger.py` -> Churn: **61.61%** | Cog Load: 64.9849% | Debt: 0.0%
- `homeassistant/components/unifi_access/__init__.py` -> Churn: **56.46%** | Cog Load: 47.0238% | Debt: 81.7574%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/components/zwave_js/test_api.py` -> **AlCalzone** (100.0% isolated ownership) | Magnitude: 4633.6
- `tests/components/sensor/test_recorder.py` -> **Sab44** (100.0% isolated ownership) | Magnitude: 4374.84
- `tests/components/zwave_js/test_config_flow.py` -> **Mike Degatano** (100.0% isolated ownership) | Magnitude: 3546.68
- `tests/components/assist_pipeline/test_websocket.py` -> **Artur Pragacz** (100.0% isolated ownership) | Magnitude: 2967.92
- `homeassistant/components/google_assistant/trait.py` -> **Kyle Johnson** (100.0% isolated ownership) | Magnitude: 2573.48

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `homeassistant/core.py` -> **Severity: 42.813** (Embedded: 0.5418 * Error Risk: 79.0142%)
- `homeassistant/const.py` -> **Severity: 27.891** (Embedded: 0.4433 * Error Risk: 62.9199%)
- `homeassistant/helpers/typing.py` -> **Severity: 26.087** (Embedded: 0.3261 * Error Risk: 80.0%)
- `homeassistant/config_entries.py` -> **Severity: 24.405** (Embedded: 0.3689 * Error Risk: 66.1576%)
- `homeassistant/helpers/json.py` -> **Severity: 24.14** (Embedded: 0.3017 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `homeassistant/core.py` -> **Severity: 2784.418** (Blast Radius: 74.071 * Doc Risk: 37.5912%)
- `homeassistant/config_entries.py` -> **Severity: 995.329** (Blast Radius: 21.289 * Doc Risk: 46.7532%)
- `homeassistant/exceptions.py` -> **Severity: 880.491** (Blast Radius: 28.616 * Doc Risk: 30.7692%)
- `homeassistant/util/event_type.pyi` -> **Severity: 636.0** (Blast Radius: 6.36 * Doc Risk: 100.0%)
- `homeassistant/helpers/translation.py` -> **Severity: 583.948** (Blast Radius: 8.876 * Doc Risk: 65.7895%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 360 literal sites + 1 sites through wrappers = 361
- **`panics_and_aborts`:** 7934 literal sites + 91 sites through wrappers = 8025

- `parse_yaml` (function, panics_and_aborts, primitive): 22 call sites in 8 files -- `homeassistant/util/yaml/loader.py`
- `load_json_from_path` (function, panics_and_aborts, primitive): 16 call sites in 6 files -- `script/translations/util.py`
- `await_or_reraise` (function, panics_and_aborts, primitive): 12 call sites in 4 files -- `homeassistant/components/iaqualink/utils.py`
- `get_knx_module` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `homeassistant/components/knx/services.py`
- `test_task` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `tests/test_config_entries.py`
- `unsupported` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `homeassistant/helpers/template/__init__.py`
- `parse_calendar` (function, panics_and_aborts, primitive): 3 call sites in 2 files -- `homeassistant/components/remote_calendar/ics.py`
- `raise_unsupported_forecast` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `homeassistant/components/weather/__init__.py`
- `_raise_timeout_error` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `homeassistant/components/lamarzocco/update.py`
- `_unhandled_exception` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `tests/test_runner.py`
- `async_raise` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `tests/test_runner.py`
- `job` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `tests/util/test_logging.py`
*(+10 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 385670 call pairs -- scoped 45.0%, unique 0.0%, ambiguous 17.7%, external 37.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 385638 | 45.0% | 0.0% | 17.7% | 37.4% |
| shell | 32 | 3.1% | 0.0% | 0.0% | 96.9% |

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
