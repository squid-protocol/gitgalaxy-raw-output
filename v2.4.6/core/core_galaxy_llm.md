# ARCHITECTURAL_BRIEF: core
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/core` |
| **Timestamp** | `2026-08-03T19:38:03.249126+00:00` |
| **Scan Duration** | `168.29s` |
| **Git Branch** | `dev` |
| **Git Commit** | `375bd55ae6ea27814de1eaaf7c66846c4e767dc5` |
| **Git Remote** | `https://github.com/home-assistant/core.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 15872 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 24818 |
| Analyzed Artifacts (Scanned) | 22091 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2727 |
| Total LOC | 2809376 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 89.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2412 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 371 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 15852 | 2326209 | 71.8% |
| JSON | 5329 | 441540 | 24.1% |
| YAML | 804 | 41333 | 3.6% |
| XML | 61 | 0 | 0.3% |
| SHELL | 14 | 217 | 0.1% |
| PLAINTEXT | 13 | 2 | 0.1% |
| MARKDOWN | 11 | 0 | 0.0% |
| BINARY_THREAT | 3 | 3 | 0.0% |
| JAVASCRIPT | 2 | 24 | 0.0% |
| DOCKERFILE | 1 | 43 | 0.0% |
| CSV | 1 | 5 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.761`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 12432 | 56.3% |
| file_cluster_13 | 8572 | 38.8% |
| file_cluster_16 | 600 | 2.7% |
| file_cluster_4 | 419 | 1.9% |
| file_cluster_0 | 28 | 0.1% |
| file_cluster_2 | 6 | 0.0% |
| Unknown | 4 | 0.0% |
| file_cluster_7 | 4 | 0.0% |
| file_cluster_12 | 2 | 0.0% |
| file_cluster_17 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 22 | 0.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2727*

**Composition by Extension & Reason:**
- `.ambr`: 1485x Excluded (Unsupported Extension: '.ambr'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 841x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 11 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 349 LOC)
- `.json`: 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1366 LOC), 2x Excluded (Static Asset Blob without Intent: 1431 LOC)
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Excluded (Machine-Generated Source Code Signature: 8 LOC), 8x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.xml`: 17x Excluded (Saturation: Line 1 exceeds 500 chars), 7x Excluded (Saturation: Line 2 exceeds 500 chars), 3x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.tar`: 17x Excluded (Explicitly Denied Extension: '.tar')
- `.yml`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pls`: 9x Excluded (Unsupported Extension: '.pls')
- `.toml`: 8x Excluded (Unsupported Extension: '.toml')
- `.jpg`: 8x Excluded (Explicitly Denied Extension: '.jpg')
- `.mp3`: 7x Excluded (Explicitly Denied Extension: '.mp3')
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 247 LOC), 1x Excluded (Machine-Generated Source Code Signature: 3408 LOC)
- `.yaml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1201 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 11.1 | 5.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.2 | 11.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 9.2 | 1.5 | 0.0 |
| API Exposure | 0.0 | 13.8 | 3.1 | 2.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 49.7 | 40.5 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 47.6 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 87.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.3 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 40.2 | 29.5 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 24.6 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/test_config.py` (Hits: 59)
- `tests/components/backup/test_manager.py` (Hits: 58)
- `tests/helpers/test_aiohttp_client.py` (Hits: 54)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **core.py** (`homeassistant/core.py`) — 11843 inbound connections
2. **config_entries.py** (`homeassistant/config_entries.py`) — 4104 inbound connections
3. **common.py** (`tests/common.py`) — 4093 inbound connections
4. **logging.py** (`homeassistant/util/logging.py`) — 3361 inbound connections
5. **entity_platform.py** (`homeassistant/helpers/entity_platform.py`) — 2923 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`homeassistant/components/http/__init__.py`) — 56 outbound dependencies
2. **__init__.py** (`homeassistant/components/homekit/__init__.py`) — 51 outbound dependencies
3. **helpers.py** (`homeassistant/components/zha/helpers.py`) — 50 outbound dependencies
4. **__init__.py** (`homeassistant/helpers/template/__init__.py`) — 50 outbound dependencies
5. **common.py** (`tests/common.py`) — 50 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `query_attributes` (@ `homeassistant/components/google_assistant/trait.py`) -> Impact: **2796.3** | LOC: 1609
- `_substitute_name_placeholders` (@ `homeassistant/helpers/entity.py`) -> Impact: **2183.7** | LOC: 996
- `_hk_hvac_mode_from_state` (@ `homeassistant/components/homekit/type_thermostats.py`) -> Impact: **1554.3** | LOC: 566
- `json_repr` (@ `homeassistant/helpers/device_registry.py`) -> Impact: **1549.1** | LOC: 1520
  * *Intent:* # The config_entries list can be removed from the storage
- `async_process_zeroconf_match_dict` (@ `homeassistant/loader.py`) -> Impact: **1413.4** | LOC: 867
- `validator` (@ `homeassistant/helpers/config_validation.py`) -> Impact: **1268.5** | LOC: 1130
- `_try_command` (@ `homeassistant/components/xiaomi_miio/light.py`) -> Impact: **1249.0** | LOC: 877
- `_filter_bad_internal_external_urls` (@ `homeassistant/core_config.py`) -> Impact: **1185.3** | LOC: 746
- `run` (@ `homeassistant/scripts/check_config.py`) -> Impact: **1106.8** | LOC: 295
- `distance` (@ `homeassistant/helpers/template/__init__.py`) -> Impact: **1104.9** | LOC: 516

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `async_load` (@ `homeassistant/auth/auth_store.py`) -> **O(2^N) [Recursive]**
- `async_load_base_functionality` (@ `homeassistant/bootstrap.py`) -> **O(2^N) [Recursive]**
- `_async_abode_login` (@ `homeassistant/components/abode/config_flow.py`) -> **O(2^N) [Recursive]**
- `set_update_interval` (@ `homeassistant/components/airly/coordinator.py`) -> **O(2^N) [Recursive]**
- `get` (@ `homeassistant/components/api/__init__.py`) -> **O(2^N) [Recursive]**
- `process` (@ `homeassistant/components/assist_pipeline/vad.py`) -> **O(2^N) [Recursive]**
- `async_setup` (@ `homeassistant/components/assist_satellite/__init__.py`) -> **O(2^N) [Recursive]**
- `async_added_to_hass` (@ `homeassistant/components/automation/__init__.py`) -> **O(2^N) [Recursive]**
- `_cleanup_failed_upload` (@ `homeassistant/components/backblaze_b2/backup.py`) -> **O(2^N) [Recursive]**
- `apply` (@ `homeassistant/components/backup/config.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `__init__` (@ `tests/components/devolo_home_control/mocks.py`) -> DB Complexity: **75**
  * *Intent:* """devolo Home Control multi level switch mock."""
- `_try_command` (@ `homeassistant/components/xiaomi_miio/light.py`) -> DB Complexity: **70**
- `test_track_template_rate_limit_super_3` (@ `tests/helpers/test_event.py`) -> DB Complexity: **70**
- `log_ha_config` (@ `tests/helpers/test_check_config.py`) -> DB Complexity: **69**
- `_assert_subscription_order` (@ `tests/components/mqtt/test_client.py`) -> DB Complexity: **66**
- `_substitute_name_placeholders` (@ `homeassistant/helpers/entity.py`) -> DB Complexity: **65**
- `test_cleanup_name_for_homekit` (@ `tests/components/homekit/test_util.py`) -> DB Complexity: **60**
- `async_process_zeroconf_match_dict` (@ `homeassistant/loader.py`) -> DB Complexity: **57**
- `add_stream_from_template` (@ `tests/components/stream/test_worker.py`) -> DB Complexity: **53**
- `mock_session_response` (@ `tests/components/tomato/test_device_tracker.py`) -> DB Complexity: **53**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `homeassistant/helpers` | 73 | 22977.26 | 23.9% | 26.97% |
| `tests/helpers` | 68 | 20481.16 | 18.11% | 0.0% |
| `tests/components/recorder` | 38 | 12897.24 | 7.05% | 0.0% |
| `homeassistant` | 17 | 12066.98 | 22.57% | 22.27% |
| `tests` | 24 | 11885.76 | 9.93% | 0.0% |
| `homeassistant/components/mqtt` | 52 | 11742.34 | 19.55% | 9.35% |
| `tests/components/mqtt` | 42 | 11179.32 | 6.42% | 0.0% |
| `homeassistant/components/zwave_js` | 41 | 10456.22 | 18.41% | 39.75% |
| `homeassistant/components/homekit` | 29 | 8648.06 | 17.6% | 17.58% |
| `homeassistant/components/shelly` | 30 | 7667.7 | 21.52% | 41.17% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `homeassistant/components/airpatrol/quality_scale.yaml` -> **100.0%** Exposure
- `homeassistant/components/chess_com/quality_scale.yaml` -> **100.0%** Exposure
- `homeassistant/components/cync/quality_scale.yaml` -> **100.0%** Exposure
- `homeassistant/components/firefly_iii/quality_scale.yaml` -> **100.0%** Exposure
- `homeassistant/components/fitbit/quality_scale.yaml` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `homeassistant/components/abode/camera.py` -> **100.0%** Exposure
- `homeassistant/components/abode/entity.py` -> **100.0%** Exposure
- `homeassistant/components/acaia/entity.py` -> **100.0%** Exposure
- `homeassistant/components/acaia/sensor.py` -> **100.0%** Exposure
- `homeassistant/components/accuweather/coordinator.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/helpers/test_entity_platform.py` -> **71** Orphaned Functions | **37** Duplicates
- `tests/components/config/test_config_entries.py` -> **55** Orphaned Functions | **43** Duplicates
- `tests/test_config_entries.py` -> **0** Orphaned Functions | **91** Duplicates
- `tests/helpers/test_condition.py` -> **72** Orphaned Functions | **17** Duplicates
- `tests/helpers/test_entity_registry.py` -> **80** Orphaned Functions | **8** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`homeassistant/components/foscam/coordinator.py`** -> AI Confidence: **99.34%**
2. **`homeassistant/components/home_connect/const.py`** -> AI Confidence: **99.32%**
3. **`homeassistant/components/alexa/handlers.py`** -> AI Confidence: **99.31%**
4. **`homeassistant/components/anthropic/entity.py`** -> AI Confidence: **99.31%**
5. **`homeassistant/components/assist_pipeline/pipeline.py`** -> AI Confidence: **99.31%**
6. **`homeassistant/components/backup/config.py`** -> AI Confidence: **99.31%**
7. **`homeassistant/components/bluetooth/match.py`** -> AI Confidence: **99.31%**
8. **`homeassistant/components/buienradar/sensor.py`** -> AI Confidence: **99.31%**
9. **`homeassistant/components/cloud/entity.py`** -> AI Confidence: **99.31%**
10. **`homeassistant/components/conversation/chat_log.py`** -> AI Confidence: **99.31%**
11. **`homeassistant/components/conversation/default_agent.py`** -> AI Confidence: **99.31%**
12. **`homeassistant/components/doods/image_processing.py`** -> AI Confidence: **99.31%**
13. **`homeassistant/components/energy/validate.py`** -> AI Confidence: **99.31%**
14. **`homeassistant/components/energyid/__init__.py`** -> AI Confidence: **99.31%**
15. **`homeassistant/components/esphome/light.py`** -> AI Confidence: **99.31%**
16. **`homeassistant/components/esphome/manager.py`** -> AI Confidence: **99.31%**
17. **`homeassistant/components/fibaro/climate.py`** -> AI Confidence: **99.31%**
18. **`homeassistant/components/fibaro/light.py`** -> AI Confidence: **99.31%**
19. **`homeassistant/components/gios/sensor.py`** -> AI Confidence: **99.31%**
20. **`homeassistant/components/google_generative_ai_conversation/entity.py`** -> AI Confidence: **99.31%**
21. **`homeassistant/components/growatt_server/coordinator.py`** -> AI Confidence: **99.31%**
22. **`homeassistant/components/gtfs/sensor.py`** -> AI Confidence: **99.31%**
23. **`homeassistant/components/habitica/button.py`** -> AI Confidence: **99.31%**
24. **`homeassistant/components/habitica/sensor.py`** -> AI Confidence: **99.31%**
25. **`homeassistant/components/habitica/services.py`** -> AI Confidence: **99.31%**
26. **`homeassistant/components/habitica/util.py`** -> AI Confidence: **99.31%**
27. **`homeassistant/components/hisense_aehw4a1/climate.py`** -> AI Confidence: **99.31%**
28. **`homeassistant/components/history_stats/data.py`** -> AI Confidence: **99.31%**
29. **`homeassistant/components/home_connect/coordinator.py`** -> AI Confidence: **99.31%**
30. **`homeassistant/components/homeassistant/triggers/time.py`** -> AI Confidence: **99.31%**
31. **`homeassistant/components/homekit/accessories.py`** -> AI Confidence: **99.31%**
32. **`homeassistant/components/homekit/type_air_purifiers.py`** -> AI Confidence: **99.31%**
33. **`homeassistant/components/homekit/type_fans.py`** -> AI Confidence: **99.31%**
34. **`homeassistant/components/homekit/type_lights.py`** -> AI Confidence: **99.31%**
35. **`homeassistant/components/homekit/type_thermostats.py`** -> AI Confidence: **99.31%**
36. **`homeassistant/components/homematic/__init__.py`** -> AI Confidence: **99.31%**
37. **`homeassistant/components/http/forwarded.py`** -> AI Confidence: **99.31%**
38. **`homeassistant/components/hue/migration.py`** -> AI Confidence: **99.31%**
39. **`homeassistant/components/husqvarna_automower/coordinator.py`** -> AI Confidence: **99.31%**
40. **`homeassistant/components/influxdb/__init__.py`** -> AI Confidence: **99.31%**
41. **`homeassistant/components/intent/timers.py`** -> AI Confidence: **99.31%**
42. **`homeassistant/components/isy994/helpers.py`** -> AI Confidence: **99.31%**
43. **`homeassistant/components/knx/config_flow.py`** -> AI Confidence: **99.31%**
44. **`homeassistant/components/lg_soundbar/media_player.py`** -> AI Confidence: **99.31%**
45. **`homeassistant/components/light/__init__.py`** -> AI Confidence: **99.31%**
46. **`homeassistant/components/logbook/helpers.py`** -> AI Confidence: **99.31%**
47. **`homeassistant/components/matter/climate.py`** -> AI Confidence: **99.31%**
48. **`homeassistant/components/matter/fan.py`** -> AI Confidence: **99.31%**
49. **`homeassistant/components/matter/lock_helpers.py`** -> AI Confidence: **99.31%**
50. **`homeassistant/components/media_player/reproduce_state.py`** -> AI Confidence: **99.31%**
51. **`homeassistant/components/modbus/climate.py`** -> AI Confidence: **99.31%**
52. **`homeassistant/components/modbus/validators.py`** -> AI Confidence: **99.31%**
53. **`homeassistant/components/mqtt/config_flow.py`** -> AI Confidence: **99.31%**
54. **`homeassistant/components/mqtt/cover.py`** -> AI Confidence: **99.31%**
55. **`homeassistant/components/mqtt/discovery.py`** -> AI Confidence: **99.31%**
56. **`homeassistant/components/mqtt/entity.py`** -> AI Confidence: **99.31%**
57. **`homeassistant/components/mqtt/light/schema_basic.py`** -> AI Confidence: **99.31%**
58. **`homeassistant/components/mqtt/light/schema_json.py`** -> AI Confidence: **99.31%**
59. **`homeassistant/components/mqtt/light/schema_template.py`** -> AI Confidence: **99.31%**
60. **`homeassistant/components/neato/vacuum.py`** -> AI Confidence: **99.31%**
61. **`homeassistant/components/nfandroidtv/notify.py`** -> AI Confidence: **99.31%**
62. **`homeassistant/components/openai_conversation/entity.py`** -> AI Confidence: **99.31%**
63. **`homeassistant/components/openrgb/light.py`** -> AI Confidence: **99.31%**
64. **`homeassistant/components/opower/sensor.py`** -> AI Confidence: **99.31%**
65. **`homeassistant/components/owntracks/messages.py`** -> AI Confidence: **99.31%**
66. **`homeassistant/components/paperless_ngx/sensor.py`** -> AI Confidence: **99.31%**
67. **`homeassistant/components/plex/services.py`** -> AI Confidence: **99.31%**
68. **`homeassistant/components/recorder/purge.py`** -> AI Confidence: **99.31%**
69. **`homeassistant/components/recorder/statistics.py`** -> AI Confidence: **99.31%**
70. **`homeassistant/components/reolink/host.py`** -> AI Confidence: **99.31%**
71. **`homeassistant/components/search/__init__.py`** -> AI Confidence: **99.31%**
72. **`homeassistant/components/sensor/recorder.py`** -> AI Confidence: **99.31%**
73. **`homeassistant/components/shelly/diagnostics.py`** -> AI Confidence: **99.31%**
74. **`homeassistant/components/smappee/sensor.py`** -> AI Confidence: **99.31%**
75. **`homeassistant/components/smartthings/sensor.py`** -> AI Confidence: **99.31%**
76. **`homeassistant/components/sonos/speaker.py`** -> AI Confidence: **99.31%**
77. **`homeassistant/components/spotify/browse_media.py`** -> AI Confidence: **99.31%**
78. **`homeassistant/components/switchbot_cloud/__init__.py`** -> AI Confidence: **99.31%**
79. **`homeassistant/components/systemmonitor/coordinator.py`** -> AI Confidence: **99.31%**
80. **`homeassistant/components/systemmonitor/util.py`** -> AI Confidence: **99.31%**
81. **`homeassistant/components/telegram/notify.py`** -> AI Confidence: **99.31%**
82. **`homeassistant/components/template/light.py`** -> AI Confidence: **99.31%**
83. **`homeassistant/components/template/validators.py`** -> AI Confidence: **99.31%**
84. **`homeassistant/components/teslemetry/sensor.py`** -> AI Confidence: **99.31%**
85. **`homeassistant/components/todoist/calendar.py`** -> AI Confidence: **99.31%**
86. **`homeassistant/components/unifi/diagnostics.py`** -> AI Confidence: **99.31%**
87. **`homeassistant/components/unifiprotect/event.py`** -> AI Confidence: **99.31%**
88. **`homeassistant/components/victron_remote_monitoring/sensor.py`** -> AI Confidence: **99.31%**
89. **`homeassistant/components/xbox/sensor.py`** -> AI Confidence: **99.31%**
90. **`homeassistant/components/yolink/binary_sensor.py`** -> AI Confidence: **99.31%**
91. **`homeassistant/components/youless/sensor.py`** -> AI Confidence: **99.31%**
92. **`homeassistant/components/zwave_js/light.py`** -> AI Confidence: **99.31%**
93. **`homeassistant/components/zwave_js/services.py`** -> AI Confidence: **99.31%**
94. **`homeassistant/helpers/device_registry.py`** -> AI Confidence: **99.31%**
95. **`homeassistant/helpers/entity_registry.py`** -> AI Confidence: **99.31%**
96. **`homeassistant/helpers/intent.py`** -> AI Confidence: **99.31%**
97. **`homeassistant/helpers/network.py`** -> AI Confidence: **99.31%**
98. **`homeassistant/helpers/script.py`** -> AI Confidence: **99.31%**
99. **`homeassistant/helpers/target.py`** -> AI Confidence: **99.31%**
100. **`homeassistant/scripts/check_config.py`** -> AI Confidence: **99.31%**
101. **`pylint/plugins/hass_enforce_type_hints.py`** -> AI Confidence: **99.31%**
102. **`script/hassfest/__main__.py`** -> AI Confidence: **99.31%**
103. **`script/hassfest/conditions.py`** -> AI Confidence: **99.31%**
104. **`script/hassfest/dependencies.py`** -> AI Confidence: **99.31%**
105. **`script/hassfest/requirements.py`** -> AI Confidence: **99.31%**
106. **`script/hassfest/services.py`** -> AI Confidence: **99.31%**
107. **`script/hassfest/translations.py`** -> AI Confidence: **99.31%**
108. **`script/hassfest/triggers.py`** -> AI Confidence: **99.31%**
109. **`script/licenses.py`** -> AI Confidence: **99.31%**
110. **`script/scaffold/__main__.py`** -> AI Confidence: **99.31%**
111. **`script/translations/migrate.py`** -> AI Confidence: **99.31%**
112. **`homeassistant/util/dt.py`** -> AI Confidence: **99.31%**
113. **`homeassistant/components/aurora/const.py`** -> AI Confidence: **99.29%**
114. **`homeassistant/components/go2rtc/const.py`** -> AI Confidence: **99.29%**
115. **`homeassistant/components/konnected/const.py`** -> AI Confidence: **99.29%**
116. **`tests/components/switchbee/__init__.py`** -> AI Confidence: **99.29%**
117. **`rootfs/init`** -> AI Confidence: **99.29%**
118. **`script/run-in-env.sh`** -> AI Confidence: **99.29%**
119. **`homeassistant/auth/auth_store.py`** -> AI Confidence: **99.24%**
120. **`homeassistant/backup_restore.py`** -> AI Confidence: **99.24%**
121. **`homeassistant/components/airzone_cloud/climate.py`** -> AI Confidence: **99.24%**
122. **`homeassistant/components/alarmdecoder/binary_sensor.py`** -> AI Confidence: **99.24%**
123. **`homeassistant/components/alexa/flash_briefings.py`** -> AI Confidence: **99.24%**
124. **`homeassistant/components/alpha_vantage/sensor.py`** -> AI Confidence: **99.24%**
125. **`homeassistant/components/analytics/analytics.py`** -> AI Confidence: **99.24%**
126. **`homeassistant/components/androidtv/config_flow.py`** -> AI Confidence: **99.24%**
127. **`homeassistant/components/anthropic/config_flow.py`** -> AI Confidence: **99.24%**
128. **`homeassistant/components/anthropic/repairs.py`** -> AI Confidence: **99.24%**
129. **`homeassistant/components/arcam_fmj/sensor.py`** -> AI Confidence: **99.24%**
130. **`homeassistant/components/assist_pipeline/websocket_api.py`** -> AI Confidence: **99.24%**
131. **`homeassistant/components/assist_satellite/entity.py`** -> AI Confidence: **99.24%**
132. **`homeassistant/components/aws/notify.py`** -> AI Confidence: **99.24%**
133. **`homeassistant/components/backup/manager.py`** -> AI Confidence: **99.24%**
134. **`homeassistant/components/bayesian/binary_sensor.py`** -> AI Confidence: **99.24%**
135. **`homeassistant/components/bitcoin/sensor.py`** -> AI Confidence: **99.24%**
136. **`homeassistant/components/bluesound/media_player.py`** -> AI Confidence: **99.24%**
137. **`homeassistant/components/bluetooth/manager.py`** -> AI Confidence: **99.24%**
138. **`homeassistant/components/bluetooth/passive_update_processor.py`** -> AI Confidence: **99.24%**
139. **`homeassistant/components/bluetooth_le_tracker/device_tracker.py`** -> AI Confidence: **99.24%**
140. **`homeassistant/components/caldav/coordinator.py`** -> AI Confidence: **99.24%**
141. **`homeassistant/components/cast/media_player.py`** -> AI Confidence: **99.24%**
142. **`homeassistant/components/climate/reproduce_state.py`** -> AI Confidence: **99.24%**
143. **`homeassistant/components/compensation/sensor.py`** -> AI Confidence: **99.24%**
144. **`homeassistant/components/config/entity_registry.py`** -> AI Confidence: **99.24%**
145. **`homeassistant/components/cover/reproduce_state.py`** -> AI Confidence: **99.24%**
146. **`homeassistant/components/deconz/light.py`** -> AI Confidence: **99.24%**
147. **`homeassistant/components/derivative/sensor.py`** -> AI Confidence: **99.24%**
148. **`homeassistant/components/discord/notify.py`** -> AI Confidence: **99.24%**
149. **`homeassistant/components/downloader/services.py`** -> AI Confidence: **99.24%**
150. **`homeassistant/components/dsmr/sensor.py`** -> AI Confidence: **99.24%**
151. **`homeassistant/components/ecobee/climate.py`** -> AI Confidence: **99.24%**
152. **`homeassistant/components/electrasmart/climate.py`** -> AI Confidence: **99.24%**
153. **`homeassistant/components/emulated_hue/config.py`** -> AI Confidence: **99.24%**
154. **`homeassistant/components/emulated_hue/hue_api.py`** -> AI Confidence: **99.24%**
155. **`homeassistant/components/emulated_kasa/__init__.py`** -> AI Confidence: **99.24%**
156. **`homeassistant/components/energy/data.py`** -> AI Confidence: **99.24%**
157. **`homeassistant/components/energy/sensor.py`** -> AI Confidence: **99.24%**
158. **`homeassistant/components/esphome/climate.py`** -> AI Confidence: **99.24%**
159. **`homeassistant/components/esphome/ffmpeg_proxy.py`** -> AI Confidence: **99.24%**
160. **`homeassistant/components/fritzbox/coordinator.py`** -> AI Confidence: **99.24%**
161. **`homeassistant/components/generic_thermostat/climate.py`** -> AI Confidence: **99.24%**
162. **`homeassistant/components/ghost/sensor.py`** -> AI Confidence: **99.24%**
163. **`homeassistant/components/google/calendar.py`** -> AI Confidence: **99.24%**
164. **`homeassistant/components/google_assistant/trait.py`** -> AI Confidence: **99.24%**
165. **`homeassistant/components/google_generative_ai_conversation/__init__.py`** -> AI Confidence: **99.24%**
166. **`homeassistant/components/google_generative_ai_conversation/config_flow.py`** -> AI Confidence: **99.24%**
167. **`homeassistant/components/group/entity.py`** -> AI Confidence: **99.24%**
168. **`homeassistant/components/group/media_player.py`** -> AI Confidence: **99.24%**
169. **`homeassistant/components/group/sensor.py`** -> AI Confidence: **99.24%**
170. **`homeassistant/components/hassio/backup.py`** -> AI Confidence: **99.24%**
171. **`homeassistant/components/hassio/http.py`** -> AI Confidence: **99.24%**
172. **`homeassistant/components/hassio/jobs.py`** -> AI Confidence: **99.24%**
173. **`homeassistant/components/hdmi_cec/__init__.py`** -> AI Confidence: **99.24%**
174. **`homeassistant/components/history/websocket_api.py`** -> AI Confidence: **99.24%**
175. **`homeassistant/components/hko/coordinator.py`** -> AI Confidence: **99.24%**
176. **`homeassistant/components/home_connect/fan.py`** -> AI Confidence: **99.24%**
177. **`homeassistant/components/home_connect/number.py`** -> AI Confidence: **99.24%**
178. **`homeassistant/components/home_connect/select.py`** -> AI Confidence: **99.24%**
179. **`homeassistant/components/home_connect/services.py`** -> AI Confidence: **99.24%**
180. **`homeassistant/components/homeassistant/triggers/event.py`** -> AI Confidence: **99.24%**
181. **`homeassistant/components/homeassistant/triggers/state.py`** -> AI Confidence: **99.24%**
182. **`homeassistant/components/homekit/type_media_players.py`** -> AI Confidence: **99.24%**
183. **`homeassistant/components/homekit_controller/connection.py`** -> AI Confidence: **99.24%**
184. **`homeassistant/components/homematicip_cloud/entity.py`** -> AI Confidence: **99.24%**
185. **`homeassistant/components/homematicip_cloud/services.py`** -> AI Confidence: **99.24%**
186. **`homeassistant/components/homewizard/sensor.py`** -> AI Confidence: **99.24%**
187. **`homeassistant/components/huawei_lte/__init__.py`** -> AI Confidence: **99.24%**
188. **`homeassistant/components/hue/v1/light.py`** -> AI Confidence: **99.24%**
189. **`homeassistant/components/hue/v2/group.py`** -> AI Confidence: **99.24%**
190. **`homeassistant/components/ibeacon/coordinator.py`** -> AI Confidence: **99.24%**
191. **`homeassistant/components/immich/media_source.py`** -> AI Confidence: **99.24%**
192. **`homeassistant/components/iqvia/sensor.py`** -> AI Confidence: **99.24%**
193. **`homeassistant/components/jellyfin/media_player.py`** -> AI Confidence: **99.24%**
194. **`homeassistant/components/keyboard_remote/__init__.py`** -> AI Confidence: **99.24%**
195. **`homeassistant/components/knx/climate.py`** -> AI Confidence: **99.24%**
196. **`homeassistant/components/knx/light.py`** -> AI Confidence: **99.24%**
197. **`homeassistant/components/knx/validation.py`** -> AI Confidence: **99.24%**
198. **`homeassistant/components/lg_thinq/climate.py`** -> AI Confidence: **99.24%**
199. **`homeassistant/components/lg_thinq/sensor.py`** -> AI Confidence: **99.24%**
200. **`homeassistant/components/light/reproduce_state.py`** -> AI Confidence: **99.24%**
201. **`homeassistant/components/litterrobot/sensor.py`** -> AI Confidence: **99.24%**
202. **`homeassistant/components/matter/adapter.py`** -> AI Confidence: **99.24%**
203. **`homeassistant/components/matter/discovery.py`** -> AI Confidence: **99.24%**
204. **`homeassistant/components/matter/number.py`** -> AI Confidence: **99.24%**
205. **`homeassistant/components/matter/vacuum.py`** -> AI Confidence: **99.24%**
206. **`homeassistant/components/maxcube/climate.py`** -> AI Confidence: **99.24%**
207. **`homeassistant/components/media_player/browse_media.py`** -> AI Confidence: **99.24%**
208. **`homeassistant/components/media_player/intent.py`** -> AI Confidence: **99.24%**
209. **`homeassistant/components/meteo_france/__init__.py`** -> AI Confidence: **99.24%**
210. **`homeassistant/components/miele/sensor.py`** -> AI Confidence: **99.24%**
211. **`homeassistant/components/modbus/entity.py`** -> AI Confidence: **99.24%**
212. **`homeassistant/components/moehlenhoff_alpha2/coordinator.py`** -> AI Confidence: **99.24%**
213. **`homeassistant/components/motion_blinds/entity.py`** -> AI Confidence: **99.24%**
214. **`homeassistant/components/motioneye/media_source.py`** -> AI Confidence: **99.24%**
215. **`homeassistant/components/mqtt/client.py`** -> AI Confidence: **99.24%**
216. **`homeassistant/components/mqtt/climate.py`** -> AI Confidence: **99.24%**
217. **`homeassistant/components/mqtt/sensor.py`** -> AI Confidence: **99.24%**
218. **`homeassistant/components/music_assistant/media_browser.py`** -> AI Confidence: **99.24%**
219. **`homeassistant/components/nest/climate.py`** -> AI Confidence: **99.24%**
220. **`homeassistant/components/network/util.py`** -> AI Confidence: **99.24%**
221. **`homeassistant/components/nibe_heatpump/climate.py`** -> AI Confidence: **99.24%**
222. **`homeassistant/components/nina/config_flow.py`** -> AI Confidence: **99.24%**
223. **`homeassistant/components/notify_events/notify.py`** -> AI Confidence: **99.24%**
224. **`homeassistant/components/ntfy/sensor.py`** -> AI Confidence: **99.24%**
225. **`homeassistant/components/ollama/__init__.py`** -> AI Confidence: **99.24%**
226. **`homeassistant/components/ollama/entity.py`** -> AI Confidence: **99.24%**
227. **`homeassistant/components/onkyo/media_player.py`** -> AI Confidence: **99.24%**
228. **`homeassistant/components/openai_conversation/ai_task.py`** -> AI Confidence: **99.24%**
229. **`homeassistant/components/openai_conversation/config_flow.py`** -> AI Confidence: **99.24%**
230. **`homeassistant/components/osramlightify/light.py`** -> AI Confidence: **99.24%**
231. **`homeassistant/components/philips_js/light.py`** -> AI Confidence: **99.24%**
232. **`homeassistant/components/plant/__init__.py`** -> AI Confidence: **99.24%**
233. **`homeassistant/components/plex/server.py`** -> AI Confidence: **99.24%**
234. **`homeassistant/components/plugwise/climate.py`** -> AI Confidence: **99.24%**
235. **`homeassistant/components/portainer/sensor.py`** -> AI Confidence: **99.24%**
236. **`homeassistant/components/private_ble_device/coordinator.py`** -> AI Confidence: **99.24%**
237. **`homeassistant/components/recorder/core.py`** -> AI Confidence: **99.24%**
238. **`homeassistant/components/recorder/filters.py`** -> AI Confidence: **99.24%**
239. **`homeassistant/components/recorder/history/__init__.py`** -> AI Confidence: **99.24%**
240. **`homeassistant/components/recorder/migration.py`** -> AI Confidence: **99.24%**
241. **`homeassistant/components/recorder/table_managers/statistics_meta.py`** -> AI Confidence: **99.24%**
242. **`homeassistant/components/recorder/util.py`** -> AI Confidence: **99.24%**
243. **`homeassistant/components/reolink/__init__.py`** -> AI Confidence: **99.24%**
244. **`homeassistant/components/reolink/media_source.py`** -> AI Confidence: **99.24%**
245. **`homeassistant/components/reolink/select.py`** -> AI Confidence: **99.24%**
246. **`homeassistant/components/rest/data.py`** -> AI Confidence: **99.24%**
247. **`homeassistant/components/rest/notify.py`** -> AI Confidence: **99.24%**
248. **`homeassistant/components/rfxtrx/config_flow.py`** -> AI Confidence: **99.24%**
249. **`homeassistant/components/roon/media_player.py`** -> AI Confidence: **99.24%**
250. **`homeassistant/components/rtorrent/sensor.py`** -> AI Confidence: **99.24%**
251. **`homeassistant/components/sensor/__init__.py`** -> AI Confidence: **99.24%**
252. **`homeassistant/components/shelly/coordinator.py`** -> AI Confidence: **99.24%**
253. **`homeassistant/components/shelly/event.py`** -> AI Confidence: **99.24%**
254. **`homeassistant/components/shelly/light.py`** -> AI Confidence: **99.24%**
255. **`homeassistant/components/shelly/sensor.py`** -> AI Confidence: **99.24%**
256. **`homeassistant/components/shelly/utils.py`** -> AI Confidence: **99.24%**
257. **`homeassistant/components/sia/utils.py`** -> AI Confidence: **99.24%**
258. **`homeassistant/components/smartthings/__init__.py`** -> AI Confidence: **99.24%**
259. **`homeassistant/components/smartthings/binary_sensor.py`** -> AI Confidence: **99.24%**
260. **`homeassistant/components/smartthings/button.py`** -> AI Confidence: **99.24%**
261. **`homeassistant/components/smartthings/light.py`** -> AI Confidence: **99.24%**
262. **`homeassistant/components/smartthings/select.py`** -> AI Confidence: **99.24%**
263. **`homeassistant/components/smartthings/switch.py`** -> AI Confidence: **99.24%**
264. **`homeassistant/components/sonos/media.py`** -> AI Confidence: **99.24%**
265. **`homeassistant/components/sonos/media_browser.py`** -> AI Confidence: **99.24%**
266. **`homeassistant/components/squeezebox/browse_media.py`** -> AI Confidence: **99.24%**
267. **`homeassistant/components/synology_dsm/common.py`** -> AI Confidence: **99.24%**
268. **`homeassistant/components/synology_dsm/diagnostics.py`** -> AI Confidence: **99.24%**
269. **`homeassistant/components/tado/climate.py`** -> AI Confidence: **99.24%**
270. **`homeassistant/components/tasmota/discovery.py`** -> AI Confidence: **99.24%**
271. **`homeassistant/components/telegram_bot/__init__.py`** -> AI Confidence: **99.24%**
272. **`homeassistant/components/telegram_bot/bot.py`** -> AI Confidence: **99.24%**
273. **`homeassistant/components/template/config_flow.py`** -> AI Confidence: **99.24%**
274. **`homeassistant/components/template/template_entity.py`** -> AI Confidence: **99.24%**
275. **`homeassistant/components/template/trigger_entity.py`** -> AI Confidence: **99.24%**
276. **`homeassistant/components/tesla_fleet/sensor.py`** -> AI Confidence: **99.24%**
277. **`homeassistant/components/teslemetry/climate.py`** -> AI Confidence: **99.24%**
278. **`homeassistant/components/teslemetry/update.py`** -> AI Confidence: **99.24%**
279. **`homeassistant/components/thread/dataset_store.py`** -> AI Confidence: **99.24%**
280. **`homeassistant/components/tplink/__init__.py`** -> AI Confidence: **99.24%**
281. **`homeassistant/components/tradfri/light.py`** -> AI Confidence: **99.24%**
282. **`homeassistant/components/trane/climate.py`** -> AI Confidence: **99.24%**
283. **`homeassistant/components/tts/__init__.py`** -> AI Confidence: **99.24%**
284. **`homeassistant/components/tuya/light.py`** -> AI Confidence: **99.24%**
285. **`homeassistant/components/twitch/coordinator.py`** -> AI Confidence: **99.24%**
286. **`homeassistant/components/unifi_access/coordinator.py`** -> AI Confidence: **99.24%**
287. **`homeassistant/components/unifiprotect/camera.py`** -> AI Confidence: **99.24%**
288. **`homeassistant/components/unifiprotect/data.py`** -> AI Confidence: **99.24%**
289. **`homeassistant/components/unifiprotect/entity.py`** -> AI Confidence: **99.24%**
290. **`homeassistant/components/unifiprotect/media_source.py`** -> AI Confidence: **99.24%**
291. **`homeassistant/components/utility_meter/sensor.py`** -> AI Confidence: **99.24%**
292. **`homeassistant/components/vacuum/reproduce_state.py`** -> AI Confidence: **99.24%**
293. **`homeassistant/components/vasttrafik/sensor.py`** -> AI Confidence: **99.24%**
294. **`homeassistant/components/vera/sensor.py`** -> AI Confidence: **99.24%**
295. **`homeassistant/components/vesync/fan.py`** -> AI Confidence: **99.24%**
296. **`homeassistant/components/vizio/media_player.py`** -> AI Confidence: **99.24%**
297. **`homeassistant/components/water_heater/reproduce_state.py`** -> AI Confidence: **99.24%**
298. **`homeassistant/components/watergate/sensor.py`** -> AI Confidence: **99.24%**
299. **`homeassistant/components/waze_travel_time/coordinator.py`** -> AI Confidence: **99.24%**
300. **`homeassistant/components/webostv/media_player.py`** -> AI Confidence: **99.24%**
301. **`homeassistant/components/workday/config_flow.py`** -> AI Confidence: **99.24%**
302. **`homeassistant/components/workday/util.py`** -> AI Confidence: **99.24%**
303. **`homeassistant/components/xiaomi_aqara/binary_sensor.py`** -> AI Confidence: **99.24%**
304. **`homeassistant/components/xiaomi_aqara/sensor.py`** -> AI Confidence: **99.24%**
305. **`homeassistant/components/xiaomi_aqara/switch.py`** -> AI Confidence: **99.24%**
306. **`homeassistant/components/xiaomi_miio/config_flow.py`** -> AI Confidence: **99.24%**
307. **`homeassistant/components/xiaomi_miio/humidifier.py`** -> AI Confidence: **99.24%**
308. **`homeassistant/components/yamaha_musiccast/media_player.py`** -> AI Confidence: **99.24%**
309. **`homeassistant/components/zeroconf/discovery.py`** -> AI Confidence: **99.24%**
310. **`homeassistant/components/zha/logbook.py`** -> AI Confidence: **99.24%**
311. **`homeassistant/components/ziggo_mediabox_xl/media_player.py`** -> AI Confidence: **99.24%**
312. **`homeassistant/components/zwave_js/__init__.py`** -> AI Confidence: **99.24%**
313. **`homeassistant/components/zwave_js/discovery.py`** -> AI Confidence: **99.24%**
314. **`homeassistant/components/zwave_js/migrate.py`** -> AI Confidence: **99.24%**
315. **`homeassistant/config.py`** -> AI Confidence: **99.24%**
316. **`homeassistant/config_entries.py`** -> AI Confidence: **99.24%**
317. **`homeassistant/core_config.py`** -> AI Confidence: **99.24%**
318. **`homeassistant/helpers/condition.py`** -> AI Confidence: **99.24%**
319. **`homeassistant/helpers/config_validation.py`** -> AI Confidence: **99.24%**
320. **`homeassistant/helpers/entity.py`** -> AI Confidence: **99.24%**
321. **`homeassistant/helpers/entity_platform.py`** -> AI Confidence: **99.24%**
322. **`homeassistant/helpers/entity_values.py`** -> AI Confidence: **99.24%**
323. **`homeassistant/helpers/entityfilter.py`** -> AI Confidence: **99.24%**
324. **`homeassistant/helpers/event.py`** -> AI Confidence: **99.24%**
325. **`homeassistant/helpers/frame.py`** -> AI Confidence: **99.24%**
326. **`homeassistant/helpers/llm.py`** -> AI Confidence: **99.24%**
327. **`homeassistant/helpers/service.py`** -> AI Confidence: **99.24%**
328. **`homeassistant/helpers/translation.py`** -> AI Confidence: **99.24%**
329. **`homeassistant/helpers/update_coordinator.py`** -> AI Confidence: **99.24%**
330. **`homeassistant/requirements.py`** -> AI Confidence: **99.24%**
331. **`homeassistant/setup.py`** -> AI Confidence: **99.24%**
332. **`homeassistant/util/__init__.py`** -> AI Confidence: **99.24%**
333. **`homeassistant/util/loop.py`** -> AI Confidence: **99.24%**
334. **`pylint/plugins/hass_imports.py`** -> AI Confidence: **99.24%**
335. **`script/gen_requirements_all.py`** -> AI Confidence: **99.24%**
336. **`script/hassfest/icons.py`** -> AI Confidence: **99.24%**
337. **`script/hassfest/manifest.py`** -> AI Confidence: **99.24%**
338. **`script/translations/develop.py`** -> AI Confidence: **99.24%**
339. **`script/version_bump.py`** -> AI Confidence: **99.24%**
340. **`tests/components/music_assistant/test_media_browser.py`** -> AI Confidence: **99.24%**
341. **`tests/components/template/test_validators.py`** -> AI Confidence: **99.24%**
342. **`tests/components/tplink/__init__.py`** -> AI Confidence: **99.24%**
343. **`tests/components/unifiprotect/test_diagnostics.py`** -> AI Confidence: **99.24%**
344. **`tests/test_block_async_io.py`** -> AI Confidence: **99.24%**
345. **`homeassistant/components/airzone_cloud/diagnostics.py`** -> AI Confidence: **99.23%**
346. **`homeassistant/components/anthropic/__init__.py`** -> AI Confidence: **99.23%**
347. **`homeassistant/components/auth/indieauth.py`** -> AI Confidence: **99.23%**
348. **`homeassistant/components/fan/reproduce_state.py`** -> AI Confidence: **99.23%**
349. **`homeassistant/components/netatmo/media_source.py`** -> AI Confidence: **99.23%**
350. **`homeassistant/components/obihai/sensor.py`** -> AI Confidence: **99.23%**
351. **`homeassistant/components/simplepush/notify.py`** -> AI Confidence: **99.23%**
352. **`homeassistant/components/teslemetry/calendar.py`** -> AI Confidence: **99.23%**
353. **`homeassistant/helpers/debounce.py`** -> AI Confidence: **99.23%**
354. **`tests/components/ring/device_mocks.py`** -> AI Confidence: **99.23%**
355. **`homeassistant/util/language.py`** -> AI Confidence: **99.23%**
356. **`homeassistant/auth/permissions/util.py`** -> AI Confidence: **99.18%**
357. **`homeassistant/auth/providers/command_line.py`** -> AI Confidence: **99.18%**
358. **`homeassistant/auth/providers/insecure_example.py`** -> AI Confidence: **99.18%**
359. **`homeassistant/components/abode/services.py`** -> AI Confidence: **99.18%**
360. **`homeassistant/components/acaia/config_flow.py`** -> AI Confidence: **99.18%**
361. **`homeassistant/components/acaia/sensor.py`** -> AI Confidence: **99.18%**
362. **`homeassistant/components/acer_projector/switch.py`** -> AI Confidence: **99.18%**
363. **`homeassistant/components/acmeda/helpers.py`** -> AI Confidence: **99.18%**
364. **`homeassistant/components/actiontec/device_tracker.py`** -> AI Confidence: **99.18%**
365. **`homeassistant/components/actron_air/config_flow.py`** -> AI Confidence: **99.18%**
366. **`homeassistant/components/adax/climate.py`** -> AI Confidence: **99.18%**
367. **`homeassistant/components/adax/coordinator.py`** -> AI Confidence: **99.18%**
368. **`homeassistant/components/adguard/entity.py`** -> AI Confidence: **99.18%**
369. **`homeassistant/components/ads/light.py`** -> AI Confidence: **99.18%**
370. **`homeassistant/components/advantage_air/cover.py`** -> AI Confidence: **99.18%**
371. **`homeassistant/components/airgradient/sensor.py`** -> AI Confidence: **99.18%**
372. **`homeassistant/components/airly/config_flow.py`** -> AI Confidence: **99.18%**
373. **`homeassistant/components/airly/coordinator.py`** -> AI Confidence: **99.18%**
374. **`homeassistant/components/airobot/diagnostics.py`** -> AI Confidence: **99.18%**
375. **`homeassistant/components/airos/config_flow.py`** -> AI Confidence: **99.18%**
376. **`homeassistant/components/airpatrol/climate.py`** -> AI Confidence: **99.18%**
377. **`homeassistant/components/airthings_ble/config_flow.py`** -> AI Confidence: **99.18%**
378. **`homeassistant/components/airthings_ble/sensor.py`** -> AI Confidence: **99.18%**
379. **`homeassistant/components/airzone/binary_sensor.py`** -> AI Confidence: **99.18%**
380. **`homeassistant/components/airzone/select.py`** -> AI Confidence: **99.18%**
381. **`homeassistant/components/airzone/sensor.py`** -> AI Confidence: **99.18%**
382. **`homeassistant/components/airzone_cloud/binary_sensor.py`** -> AI Confidence: **99.18%**
383. **`homeassistant/components/airzone_cloud/config_flow.py`** -> AI Confidence: **99.18%**
384. **`homeassistant/components/airzone_cloud/select.py`** -> AI Confidence: **99.18%**
385. **`homeassistant/components/airzone_cloud/sensor.py`** -> AI Confidence: **99.18%**
386. **`homeassistant/components/alarm_control_panel/device_trigger.py`** -> AI Confidence: **99.18%**
387. **`homeassistant/components/alert/reproduce_state.py`** -> AI Confidence: **99.18%**
388. **`homeassistant/components/alexa/smart_home.py`** -> AI Confidence: **99.18%**
389. **`homeassistant/components/alexa_devices/sensor.py`** -> AI Confidence: **99.18%**
390. **`homeassistant/components/alexa_devices/services.py`** -> AI Confidence: **99.18%**
391. **`homeassistant/components/alexa_devices/utils.py`** -> AI Confidence: **99.18%**
392. **`homeassistant/components/amberelectric/config_flow.py`** -> AI Confidence: **99.18%**
393. **`homeassistant/components/amberelectric/sensor.py`** -> AI Confidence: **99.18%**
394. **`homeassistant/components/ambient_station/sensor.py`** -> AI Confidence: **99.18%**
395. **`homeassistant/components/amcrest/camera.py`** -> AI Confidence: **99.18%**
396. **`homeassistant/components/amcrest/sensor.py`** -> AI Confidence: **99.18%**
397. **`homeassistant/components/analytics_insights/config_flow.py`** -> AI Confidence: **99.18%**
398. **`homeassistant/components/androidtv/__init__.py`** -> AI Confidence: **99.18%**
399. **`homeassistant/components/androidtv/entity.py`** -> AI Confidence: **99.18%**
400. **`homeassistant/components/androidtv/remote.py`** -> AI Confidence: **99.18%**
401. **`homeassistant/components/androidtv_remote/media_player.py`** -> AI Confidence: **99.18%**
402. **`homeassistant/components/anglian_water/coordinator.py`** -> AI Confidence: **99.18%**
403. **`homeassistant/components/aosmith/coordinator.py`** -> AI Confidence: **99.18%**
404. **`homeassistant/components/aosmith/water_heater.py`** -> AI Confidence: **99.18%**
405. **`homeassistant/components/apcupsd/config_flow.py`** -> AI Confidence: **99.18%**
406. **`homeassistant/components/apple_tv/__init__.py`** -> AI Confidence: **99.18%**
407. **`homeassistant/components/apple_tv/config_flow.py`** -> AI Confidence: **99.18%**
408. **`homeassistant/components/apple_tv/remote.py`** -> AI Confidence: **99.18%**
409. **`homeassistant/components/application_credentials/__init__.py`** -> AI Confidence: **99.18%**
410. **`homeassistant/components/aprilaire/select.py`** -> AI Confidence: **99.18%**
411. **`homeassistant/components/aprs/device_tracker.py`** -> AI Confidence: **99.18%**
412. **`homeassistant/components/aquostv/media_player.py`** -> AI Confidence: **99.18%**
413. **`homeassistant/components/aranet/config_flow.py`** -> AI Confidence: **99.18%**
414. **`homeassistant/components/arcam_fmj/coordinator.py`** -> AI Confidence: **99.18%**
415. **`homeassistant/components/arcam_fmj/media_player.py`** -> AI Confidence: **99.18%**
416. **`homeassistant/components/arwn/sensor.py`** -> AI Confidence: **99.18%**
417. **`homeassistant/components/assist_pipeline/select.py`** -> AI Confidence: **99.18%**
418. **`homeassistant/components/assist_satellite/websocket_api.py`** -> AI Confidence: **99.18%**
419. **`homeassistant/components/august/binary_sensor.py`** -> AI Confidence: **99.18%**
420. **`homeassistant/components/august/event.py`** -> AI Confidence: **99.18%**
421. **`homeassistant/components/august/lock.py`** -> AI Confidence: **99.18%**
422. **`homeassistant/components/auth/__init__.py`** -> AI Confidence: **99.18%**
423. **`homeassistant/components/auth/login_flow.py`** -> AI Confidence: **99.18%**
424. **`homeassistant/components/automation/config.py`** -> AI Confidence: **99.18%**
425. **`homeassistant/components/automation/reproduce_state.py`** -> AI Confidence: **99.18%**
426. **`homeassistant/components/autoskope/device_tracker.py`** -> AI Confidence: **99.18%**
427. **`homeassistant/components/avea/light.py`** -> AI Confidence: **99.18%**
428. **`homeassistant/components/awair/config_flow.py`** -> AI Confidence: **99.18%**
429. **`homeassistant/components/aws_s3/backup.py`** -> AI Confidence: **99.18%**
430. **`homeassistant/components/aws_s3/helpers.py`** -> AI Confidence: **99.18%**
431. **`homeassistant/components/axis/config_flow.py`** -> AI Confidence: **99.18%**
432. **`homeassistant/components/axis/hub/entity_loader.py`** -> AI Confidence: **99.18%**
433. **`homeassistant/components/azure_devops/config_flow.py`** -> AI Confidence: **99.18%**
434. **`homeassistant/components/azure_devops/sensor.py`** -> AI Confidence: **99.18%**
435. **`homeassistant/components/baf/climate.py`** -> AI Confidence: **99.18%**
436. **`homeassistant/components/baf/fan.py`** -> AI Confidence: **99.18%**
437. **`homeassistant/components/bang_olufsen/websocket.py`** -> AI Confidence: **99.18%**
438. **`homeassistant/components/bbox/sensor.py`** -> AI Confidence: **99.18%**
439. **`homeassistant/components/binary_sensor/device_condition.py`** -> AI Confidence: **99.18%**
440. **`homeassistant/components/binary_sensor/device_trigger.py`** -> AI Confidence: **99.18%**
441. **`homeassistant/components/blebox/climate.py`** -> AI Confidence: **99.18%**
442. **`homeassistant/components/blebox/light.py`** -> AI Confidence: **99.18%**
443. **`homeassistant/components/blue_current/services.py`** -> AI Confidence: **99.18%**
444. **`homeassistant/components/bluemaestro/config_flow.py`** -> AI Confidence: **99.18%**
445. **`homeassistant/components/blueprint/models.py`** -> AI Confidence: **99.18%**
446. **`homeassistant/components/bluetooth/__init__.py`** -> AI Confidence: **99.18%**
447. **`homeassistant/components/bluetooth/active_update_coordinator.py`** -> AI Confidence: **99.18%**
448. **`homeassistant/components/bluetooth/active_update_processor.py`** -> AI Confidence: **99.18%**
449. **`homeassistant/components/bluetooth/config_flow.py`** -> AI Confidence: **99.18%**
450. **`homeassistant/components/bond/button.py`** -> AI Confidence: **99.18%**
451. **`homeassistant/components/bond/cover.py`** -> AI Confidence: **99.18%**
452. **`homeassistant/components/bond/fan.py`** -> AI Confidence: **99.18%**
453. **`homeassistant/components/bosch_alarm/binary_sensor.py`** -> AI Confidence: **99.18%**
454. **`homeassistant/components/bosch_shc/sensor.py`** -> AI Confidence: **99.18%**
455. **`homeassistant/components/brands/__init__.py`** -> AI Confidence: **99.18%**
456. **`homeassistant/components/bring/event.py`** -> AI Confidence: **99.18%**
457. **`homeassistant/components/broadlink/config_flow.py`** -> AI Confidence: **99.18%**
458. **`homeassistant/components/broadlink/heartbeat.py`** -> AI Confidence: **99.18%**
459. **`homeassistant/components/brottsplatskartan/sensor.py`** -> AI Confidence: **99.18%**
460. **`homeassistant/components/bryant_evolution/config_flow.py`** -> AI Confidence: **99.18%**
461. **`homeassistant/components/bsblan/climate.py`** -> AI Confidence: **99.18%**
462. **`homeassistant/components/bsblan/config_flow.py`** -> AI Confidence: **99.18%**
463. **`homeassistant/components/bsblan/sensor.py`** -> AI Confidence: **99.18%**
464. **`homeassistant/components/bsblan/water_heater.py`** -> AI Confidence: **99.18%**
465. **`homeassistant/components/bt_smarthub/device_tracker.py`** -> AI Confidence: **99.18%**
466. **`homeassistant/components/bthome/__init__.py`** -> AI Confidence: **99.18%**
467. **`homeassistant/components/bthome/config_flow.py`** -> AI Confidence: **99.18%**
468. **`homeassistant/components/bthome/device_trigger.py`** -> AI Confidence: **99.18%**
469. **`homeassistant/components/bthome/repairs.py`** -> AI Confidence: **99.18%**
470. **`homeassistant/components/buienradar/camera.py`** -> AI Confidence: **99.18%**
471. **`homeassistant/components/buienradar/util.py`** -> AI Confidence: **99.18%**
472. **`homeassistant/components/buienradar/weather.py`** -> AI Confidence: **99.18%**
473. **`homeassistant/components/caldav/calendar.py`** -> AI Confidence: **99.18%**
474. **`homeassistant/components/cambridge_audio/media_player.py`** -> AI Confidence: **99.18%**
475. **`homeassistant/components/camera/__init__.py`** -> AI Confidence: **99.18%**
476. **`homeassistant/components/camera/diagnostics.py`** -> AI Confidence: **99.18%**
477. **`homeassistant/components/camera/media_source.py`** -> AI Confidence: **99.18%**
478. **`homeassistant/components/camera/prefs.py`** -> AI Confidence: **99.18%**
479. **`homeassistant/components/casper_glow/config_flow.py`** -> AI Confidence: **99.18%**
480. **`homeassistant/components/cast/home_assistant_cast.py`** -> AI Confidence: **99.18%**
481. **`homeassistant/components/cert_expiry/config_flow.py`** -> AI Confidence: **99.18%**
482. **`homeassistant/components/cisco_ios/device_tracker.py`** -> AI Confidence: **99.18%**
483. **`homeassistant/components/citybikes/sensor.py`** -> AI Confidence: **99.18%**
484. **`homeassistant/components/climate/__init__.py`** -> AI Confidence: **99.18%**
485. **`homeassistant/components/climate/device_action.py`** -> AI Confidence: **99.18%**
486. **`homeassistant/components/climate/device_condition.py`** -> AI Confidence: **99.18%**
487. **`homeassistant/components/cloud/account_link.py`** -> AI Confidence: **99.18%**
488. **`homeassistant/components/cloud/ai_task.py`** -> AI Confidence: **99.18%**
489. **`homeassistant/components/cloud/assist_pipeline.py`** -> AI Confidence: **99.18%**
490. **`homeassistant/components/cloud/client.py`** -> AI Confidence: **99.18%**
491. **`homeassistant/components/cloud/tts.py`** -> AI Confidence: **99.18%**
492. **`homeassistant/components/cloudflare/coordinator.py`** -> AI Confidence: **99.18%**
493. **`homeassistant/components/cloudflare_r2/backup.py`** -> AI Confidence: **99.18%**
494. **`homeassistant/components/cloudflare_r2/config_flow.py`** -> AI Confidence: **99.18%**
495. **`homeassistant/components/coinbase/config_flow.py`** -> AI Confidence: **99.18%**
496. **`homeassistant/components/comed_hourly_pricing/sensor.py`** -> AI Confidence: **99.18%**
497. **`homeassistant/components/comelit/climate.py`** -> AI Confidence: **99.18%**
498. **`homeassistant/components/comelit/config_flow.py`** -> AI Confidence: **99.18%**
499. **`homeassistant/components/comelit/diagnostics.py`** -> AI Confidence: **99.18%**
500. **`homeassistant/components/comelit/sensor.py`** -> AI Confidence: **99.18%**
501. **`homeassistant/components/comelit/utils.py`** -> AI Confidence: **99.18%**
502. **`homeassistant/components/comfoconnect/fan.py`** -> AI Confidence: **99.18%**
503. **`homeassistant/components/command_line/notify.py`** -> AI Confidence: **99.18%**
504. **`homeassistant/components/command_line/sensor.py`** -> AI Confidence: **99.18%**
505. **`homeassistant/components/command_line/switch.py`** -> AI Confidence: **99.18%**
506. **`homeassistant/components/compensation/__init__.py`** -> AI Confidence: **99.18%**
507. **`homeassistant/components/compit/fan.py`** -> AI Confidence: **99.18%**
508. **`homeassistant/components/compit/sensor.py`** -> AI Confidence: **99.18%**
509. **`homeassistant/components/concord232/alarm_control_panel.py`** -> AI Confidence: **99.18%**
510. **`homeassistant/components/config/auth_provider_homeassistant.py`** -> AI Confidence: **99.18%**
511. **`homeassistant/components/config/config_entries.py`** -> AI Confidence: **99.18%**
512. **`homeassistant/components/config/core.py`** -> AI Confidence: **99.18%**
513. **`homeassistant/components/config/device_registry.py`** -> AI Confidence: **99.18%**
514. **`homeassistant/components/config/view.py`** -> AI Confidence: **99.18%**
515. **`homeassistant/components/configurator/__init__.py`** -> AI Confidence: **99.18%**
516. **`homeassistant/components/conversation/agent_manager.py`** -> AI Confidence: **99.18%**
517. **`homeassistant/components/conversation/http.py`** -> AI Confidence: **99.18%**
518. **`homeassistant/components/cookidoo/config_flow.py`** -> AI Confidence: **99.18%**
519. **`homeassistant/components/cookidoo/todo.py`** -> AI Confidence: **99.18%**
520. **`homeassistant/components/coolmaster/config_flow.py`** -> AI Confidence: **99.18%**
521. **`homeassistant/components/coolmaster/coordinator.py`** -> AI Confidence: **99.18%**
522. **`homeassistant/components/counter/__init__.py`** -> AI Confidence: **99.18%**
523. **`homeassistant/components/cover/device_trigger.py`** -> AI Confidence: **99.18%**
524. **`homeassistant/components/crownstone/light.py`** -> AI Confidence: **99.18%**
525. **`homeassistant/components/daikin/__init__.py`** -> AI Confidence: **99.18%**
526. **`homeassistant/components/deconz/config_flow.py`** -> AI Confidence: **99.18%**
527. **`homeassistant/components/deconz/device_trigger.py`** -> AI Confidence: **99.18%**
528. **`homeassistant/components/deconz/sensor.py`** -> AI Confidence: **99.18%**
529. **`homeassistant/components/deluge/sensor.py`** -> AI Confidence: **99.18%**
530. **`homeassistant/components/demo/__init__.py`** -> AI Confidence: **99.18%**
531. **`homeassistant/components/demo/text.py`** -> AI Confidence: **99.18%**
532. **`homeassistant/components/demo/valve.py`** -> AI Confidence: **99.18%**
533. **`homeassistant/components/denonavr/media_player.py`** -> AI Confidence: **99.18%**
534. **`homeassistant/components/derivative/__init__.py`** -> AI Confidence: **99.18%**
535. **`homeassistant/components/devialet/media_player.py`** -> AI Confidence: **99.18%**
536. **`homeassistant/components/device_automation/__init__.py`** -> AI Confidence: **99.18%**
537. **`homeassistant/components/device_automation/helpers.py`** -> AI Confidence: **99.18%**
538. **`homeassistant/components/device_automation/toggle_entity.py`** -> AI Confidence: **99.18%**
539. **`homeassistant/components/devolo_home_control/light.py`** -> AI Confidence: **99.18%**
540. **`homeassistant/components/devolo_home_control/siren.py`** -> AI Confidence: **99.18%**
541. **`homeassistant/components/devolo_home_network/sensor.py`** -> AI Confidence: **99.18%**
542. **`homeassistant/components/dialogflow/__init__.py`** -> AI Confidence: **99.18%**
543. **`homeassistant/components/discogs/sensor.py`** -> AI Confidence: **99.18%**
544. **`homeassistant/components/dlink/config_flow.py`** -> AI Confidence: **99.18%**
545. **`homeassistant/components/dlna_dmr/data.py`** -> AI Confidence: **99.18%**
546. **`homeassistant/components/doorbird/device.py`** -> AI Confidence: **99.18%**
547. **`homeassistant/components/dormakaba_dkey/config_flow.py`** -> AI Confidence: **99.18%**
548. **`homeassistant/components/dovado/sensor.py`** -> AI Confidence: **99.18%**
549. **`homeassistant/components/dropbox/backup.py`** -> AI Confidence: **99.18%**
550. **`homeassistant/components/dunehd/config_flow.py`** -> AI Confidence: **99.18%**
551. **`homeassistant/components/dwd_weather_warnings/coordinator.py`** -> AI Confidence: **99.18%**
552. **`homeassistant/components/dwd_weather_warnings/sensor.py`** -> AI Confidence: **99.18%**
553. **`homeassistant/components/dynalite/panel.py`** -> AI Confidence: **99.18%**
554. **`homeassistant/components/easyenergy/coordinator.py`** -> AI Confidence: **99.18%**
555. **`homeassistant/components/ebusd/__init__.py`** -> AI Confidence: **99.18%**
556. **`homeassistant/components/ecobee/__init__.py`** -> AI Confidence: **99.18%**
557. **`homeassistant/components/ecobee/humidifier.py`** -> AI Confidence: **99.18%**
558. **`homeassistant/components/ecobee/number.py`** -> AI Confidence: **99.18%**
559. **`homeassistant/components/ecobee/weather.py`** -> AI Confidence: **99.18%**
560. **`homeassistant/components/econet/sensor.py`** -> AI Confidence: **99.18%**
561. **`homeassistant/components/ecovacs/button.py`** -> AI Confidence: **99.18%**
562. **`homeassistant/components/ecovacs/config_flow.py`** -> AI Confidence: **99.18%**
563. **`homeassistant/components/ecovacs/select.py`** -> AI Confidence: **99.18%**
564. **`homeassistant/components/ecovacs/sensor.py`** -> AI Confidence: **99.18%**
565. **`homeassistant/components/edl21/sensor.py`** -> AI Confidence: **99.18%**
566. **`homeassistant/components/efergy/sensor.py`** -> AI Confidence: **99.18%**
567. **`homeassistant/components/egardia/__init__.py`** -> AI Confidence: **99.18%**
568. **`homeassistant/components/egardia/alarm_control_panel.py`** -> AI Confidence: **99.18%**
569. **`homeassistant/components/eheimdigital/light.py`** -> AI Confidence: **99.18%**
570. **`homeassistant/components/electrasmart/config_flow.py`** -> AI Confidence: **99.18%**
571. **`homeassistant/components/elevenlabs/stt.py`** -> AI Confidence: **99.18%**
572. **`homeassistant/components/elgato/switch.py`** -> AI Confidence: **99.18%**
573. **`homeassistant/components/elkm1/discovery.py`** -> AI Confidence: **99.18%**
574. **`homeassistant/components/elkm1/entity.py`** -> AI Confidence: **99.18%**
575. **`homeassistant/components/elmax/alarm_control_panel.py`** -> AI Confidence: **99.18%**
576. **`homeassistant/components/elmax/config_flow.py`** -> AI Confidence: **99.18%**
577. **`homeassistant/components/elmax/coordinator.py`** -> AI Confidence: **99.18%**
578. **`homeassistant/components/emby/media_player.py`** -> AI Confidence: **99.18%**
579. **`homeassistant/components/emoncms/config_flow.py`** -> AI Confidence: **99.18%**
580. **`homeassistant/components/emoncms/sensor.py`** -> AI Confidence: **99.18%**
581. **`homeassistant/components/energy/websocket_api.py`** -> AI Confidence: **99.18%**
582. **`homeassistant/components/energyid/config_flow.py`** -> AI Confidence: **99.18%**
583. **`homeassistant/components/energyzero/coordinator.py`** -> AI Confidence: **99.18%**
584. **`homeassistant/components/energyzero/services.py`** -> AI Confidence: **99.18%**
585. **`homeassistant/components/enigma2/coordinator.py`** -> AI Confidence: **99.18%**
586. **`homeassistant/components/enocean/binary_sensor.py`** -> AI Confidence: **99.18%**
587. **`homeassistant/components/enocean/sensor.py`** -> AI Confidence: **99.18%**
588. **`homeassistant/components/enocean/switch.py`** -> AI Confidence: **99.18%**
589. **`homeassistant/components/enphase_envoy/coordinator.py`** -> AI Confidence: **99.18%**
590. **`homeassistant/components/entur_public_transport/sensor.py`** -> AI Confidence: **99.18%**
591. **`homeassistant/components/envisalink/alarm_control_panel.py`** -> AI Confidence: **99.18%**
592. **`homeassistant/components/ephember/climate.py`** -> AI Confidence: **99.18%**
593. **`homeassistant/components/esphome/alarm_control_panel.py`** -> AI Confidence: **99.18%**
594. **`homeassistant/components/esphome/dashboard.py`** -> AI Confidence: **99.18%**
595. **`homeassistant/components/esphome/fan.py`** -> AI Confidence: **99.18%**
596. **`homeassistant/components/esphome/media_player.py`** -> AI Confidence: **99.18%**
597. **`homeassistant/components/esphome/select.py`** -> AI Confidence: **99.18%**
598. **`homeassistant/components/esphome/sensor.py`** -> AI Confidence: **99.18%**
599. **`homeassistant/components/essent/sensor.py`** -> AI Confidence: **99.18%**
600. **`homeassistant/components/evil_genius_labs/light.py`** -> AI Confidence: **99.18%**
601. **`homeassistant/components/evohome/coordinator.py`** -> AI Confidence: **99.18%**
602. **`homeassistant/components/ezviz/__init__.py`** -> AI Confidence: **99.18%**
603. **`homeassistant/components/ezviz/config_flow.py`** -> AI Confidence: **99.18%**
604. **`homeassistant/components/ezviz/image.py`** -> AI Confidence: **99.18%**
605. **`homeassistant/components/ezviz/light.py`** -> AI Confidence: **99.18%**
606. **`homeassistant/components/ezviz/number.py`** -> AI Confidence: **99.18%**
607. **`homeassistant/components/ezviz/siren.py`** -> AI Confidence: **99.18%**
608. **`homeassistant/components/fail2ban/sensor.py`** -> AI Confidence: **99.18%**
609. **`homeassistant/components/ffmpeg/__init__.py`** -> AI Confidence: **99.18%**
610. **`homeassistant/components/fibaro/cover.py`** -> AI Confidence: **99.18%**
611. **`homeassistant/components/fibaro/sensor.py`** -> AI Confidence: **99.18%**
612. **`homeassistant/components/file_upload/__init__.py`** -> AI Confidence: **99.18%**
613. **`homeassistant/components/fing/config_flow.py`** -> AI Confidence: **99.18%**
614. **`homeassistant/components/fireservicerota/sensor.py`** -> AI Confidence: **99.18%**
615. **`homeassistant/components/firmata/__init__.py`** -> AI Confidence: **99.18%**
616. **`homeassistant/components/fitbit/sensor.py`** -> AI Confidence: **99.18%**
617. **`homeassistant/components/fjaraskupan/fan.py`** -> AI Confidence: **99.18%**
618. **`homeassistant/components/flexit/climate.py`** -> AI Confidence: **99.18%**
619. **`homeassistant/components/flexit_bacnet/climate.py`** -> AI Confidence: **99.18%**
620. **`homeassistant/components/flume/coordinator.py`** -> AI Confidence: **99.18%**
621. **`homeassistant/components/flux_led/__init__.py`** -> AI Confidence: **99.18%**
622. **`homeassistant/components/flux_led/light.py`** -> AI Confidence: **99.18%**
623. **`homeassistant/components/fortios/device_tracker.py`** -> AI Confidence: **99.18%**
624. **`homeassistant/components/foscam/camera.py`** -> AI Confidence: **99.18%**
625. **`homeassistant/components/freebox/binary_sensor.py`** -> AI Confidence: **99.18%**
626. **`homeassistant/components/freebox/router.py`** -> AI Confidence: **99.18%**
627. **`homeassistant/components/freedns/__init__.py`** -> AI Confidence: **99.18%**
628. **`homeassistant/components/freedompro/climate.py`** -> AI Confidence: **99.18%**
629. **`homeassistant/components/freedompro/coordinator.py`** -> AI Confidence: **99.18%**
630. **`homeassistant/components/freedompro/light.py`** -> AI Confidence: **99.18%**
631. **`homeassistant/components/freshr/diagnostics.py`** -> AI Confidence: **99.18%**
632. **`homeassistant/components/fressnapf_tracker/light.py`** -> AI Confidence: **99.18%**
633. **`homeassistant/components/fritz/config_flow.py`** -> AI Confidence: **99.18%**
634. **`homeassistant/components/fritz/services.py`** -> AI Confidence: **99.18%**
635. **`homeassistant/components/fritz/switch.py`** -> AI Confidence: **99.18%**
636. **`homeassistant/components/fritzbox/__init__.py`** -> AI Confidence: **99.18%**
637. **`homeassistant/components/fritzbox/config_flow.py`** -> AI Confidence: **99.18%**
638. **`homeassistant/components/fritzbox/light.py`** -> AI Confidence: **99.18%**
639. **`homeassistant/components/fritzbox/sensor.py`** -> AI Confidence: **99.18%**
640. **`homeassistant/components/fritzbox_callmonitor/base.py`** -> AI Confidence: **99.18%**
641. **`homeassistant/components/fritzbox_callmonitor/sensor.py`** -> AI Confidence: **99.18%**
642. **`homeassistant/components/fronius/config_flow.py`** -> AI Confidence: **99.18%**
643. **`homeassistant/components/fronius/sensor.py`** -> AI Confidence: **99.18%**
644. **`homeassistant/components/frontier_silicon/config_flow.py`** -> AI Confidence: **99.18%**
645. **`homeassistant/components/fully_kiosk/entity.py`** -> AI Confidence: **99.18%**
646. **`homeassistant/components/fully_kiosk/media_player.py`** -> AI Confidence: **99.18%**
647. **`homeassistant/components/fyta/coordinator.py`** -> AI Confidence: **99.18%**
648. **`homeassistant/components/fyta/sensor.py`** -> AI Confidence: **99.18%**
649. **`homeassistant/components/gardena_bluetooth/sensor.py`** -> AI Confidence: **99.18%**
650. **`homeassistant/components/gdacs/sensor.py`** -> AI Confidence: **99.18%**
651. **`homeassistant/components/generic/camera.py`** -> AI Confidence: **99.18%**
652. **`homeassistant/components/generic/diagnostics.py`** -> AI Confidence: **99.18%**
653. **`homeassistant/components/generic_thermostat/__init__.py`** -> AI Confidence: **99.18%**
654. **`homeassistant/components/geniushub/__init__.py`** -> AI Confidence: **99.18%**
655. **`homeassistant/components/geniushub/config_flow.py`** -> AI Confidence: **99.18%**
656. **`homeassistant/components/geniushub/sensor.py`** -> AI Confidence: **99.18%**
657. **`homeassistant/components/geo_rss_events/sensor.py`** -> AI Confidence: **99.18%**
658. **`homeassistant/components/geofency/device_tracker.py`** -> AI Confidence: **99.18%**
659. **`homeassistant/components/geonetnz_volcano/sensor.py`** -> AI Confidence: **99.18%**
660. **`homeassistant/components/ghost/config_flow.py`** -> AI Confidence: **99.18%**
661. **`homeassistant/components/glances/sensor.py`** -> AI Confidence: **99.18%**
662. **`homeassistant/components/go2rtc/__init__.py`** -> AI Confidence: **99.18%**
663. **`homeassistant/components/goodwe/select.py`** -> AI Confidence: **99.18%**
664. **`homeassistant/components/google_air_quality/config_flow.py`** -> AI Confidence: **99.18%**
665. **`homeassistant/components/google_air_quality/sensor.py`** -> AI Confidence: **99.18%**
666. **`homeassistant/components/google_assistant/__init__.py`** -> AI Confidence: **99.18%**
667. **`homeassistant/components/google_assistant/http.py`** -> AI Confidence: **99.18%**
668. **`homeassistant/components/google_cloud/tts.py`** -> AI Confidence: **99.18%**
669. **`homeassistant/components/google_drive/api.py`** -> AI Confidence: **99.18%**
670. **`homeassistant/components/google_generative_ai_conversation/tts.py`** -> AI Confidence: **99.18%**
671. **`homeassistant/components/google_mail/notify.py`** -> AI Confidence: **99.18%**
672. **`homeassistant/components/google_mail/services.py`** -> AI Confidence: **99.18%**
673. **`homeassistant/components/google_maps/device_tracker.py`** -> AI Confidence: **99.18%**
674. **`homeassistant/components/google_photos/services.py`** -> AI Confidence: **99.18%**
675. **`homeassistant/components/google_tasks/todo.py`** -> AI Confidence: **99.18%**
676. **`homeassistant/components/google_travel_time/config_flow.py`** -> AI Confidence: **99.18%**
677. **`homeassistant/components/google_travel_time/helpers.py`** -> AI Confidence: **99.18%**
678. **`homeassistant/components/google_weather/config_flow.py`** -> AI Confidence: **99.18%**
679. **`homeassistant/components/govee_ble/event.py`** -> AI Confidence: **99.18%**
680. **`homeassistant/components/govee_light_local/config_flow.py`** -> AI Confidence: **99.18%**
681. **`homeassistant/components/gree/coordinator.py`** -> AI Confidence: **99.18%**
682. **`homeassistant/components/green_planet_energy/sensor.py`** -> AI Confidence: **99.18%**
683. **`homeassistant/components/greeneye_monitor/sensor.py`** -> AI Confidence: **99.18%**
684. **`homeassistant/components/group/fan.py`** -> AI Confidence: **99.18%**
685. **`homeassistant/components/group/notify.py`** -> AI Confidence: **99.18%**
686. **`homeassistant/components/habitica/__init__.py`** -> AI Confidence: **99.18%**
687. **`homeassistant/components/hassio/__init__.py`** -> AI Confidence: **99.18%**
688. **`homeassistant/components/hassio/addon_manager.py`** -> AI Confidence: **99.18%**
689. **`homeassistant/components/hassio/entity.py`** -> AI Confidence: **99.18%**
690. **`homeassistant/components/hassio/services.py`** -> AI Confidence: **99.18%**
691. **`homeassistant/components/haveibeenpwned/sensor.py`** -> AI Confidence: **99.18%**
692. **`homeassistant/components/hddtemp/sensor.py`** -> AI Confidence: **99.18%**
693. **`homeassistant/components/hdmi_cec/media_player.py`** -> AI Confidence: **99.18%**
694. **`homeassistant/components/hegel/config_flow.py`** -> AI Confidence: **99.18%**
695. **`homeassistant/components/heos/__init__.py`** -> AI Confidence: **99.18%**
696. **`homeassistant/components/heos/media_player.py`** -> AI Confidence: **99.18%**
697. **`homeassistant/components/history/__init__.py`** -> AI Confidence: **99.18%**
698. **`homeassistant/components/history_stats/__init__.py`** -> AI Confidence: **99.18%**
699. **`homeassistant/components/history_stats/config_flow.py`** -> AI Confidence: **99.18%**
700. **`homeassistant/components/hive/binary_sensor.py`** -> AI Confidence: **99.18%**
701. **`homeassistant/components/hive/config_flow.py`** -> AI Confidence: **99.18%**
702. **`homeassistant/components/holiday/calendar.py`** -> AI Confidence: **99.18%**
703. **`homeassistant/components/home_connect/__init__.py`** -> AI Confidence: **99.18%**
704. **`homeassistant/components/home_connect/switch.py`** -> AI Confidence: **99.18%**
705. **`homeassistant/components/homeassistant_hardware/firmware_config_flow.py`** -> AI Confidence: **99.18%**
706. **`homeassistant/components/homeassistant_hardware/helpers.py`** -> AI Confidence: **99.18%**
707. **`homeassistant/components/homeassistant_hardware/silabs_multiprotocol_addon.py`** -> AI Confidence: **99.18%**
708. **`homeassistant/components/homeassistant_hardware/update.py`** -> AI Confidence: **99.18%**
709. **`homeassistant/components/homeassistant_hardware/util.py`** -> AI Confidence: **99.18%**
710. **`homeassistant/components/homeassistant_sky_connect/__init__.py`** -> AI Confidence: **99.18%**
711. **`homeassistant/components/homee/__init__.py`** -> AI Confidence: **99.18%**
712. **`homeassistant/components/homee/button.py`** -> AI Confidence: **99.18%**
713. **`homeassistant/components/homee/climate.py`** -> AI Confidence: **99.18%**
714. **`homeassistant/components/homee/sensor.py`** -> AI Confidence: **99.18%**
715. **`homeassistant/components/homee/switch.py`** -> AI Confidence: **99.18%**
716. **`homeassistant/components/homekit/aidmanager.py`** -> AI Confidence: **99.18%**
717. **`homeassistant/components/homekit/diagnostics.py`** -> AI Confidence: **99.18%**
718. **`homeassistant/components/homekit/doorbell.py`** -> AI Confidence: **99.18%**
719. **`homeassistant/components/homekit/type_sensors.py`** -> AI Confidence: **99.18%**
720. **`homeassistant/components/homekit/type_triggers.py`** -> AI Confidence: **99.18%**
721. **`homeassistant/components/homekit_controller/cover.py`** -> AI Confidence: **99.18%**
722. **`homeassistant/components/homekit_controller/device_trigger.py`** -> AI Confidence: **99.18%**
723. **`homeassistant/components/homekit_controller/diagnostics.py`** -> AI Confidence: **99.18%**
724. **`homeassistant/components/homekit_controller/entity.py`** -> AI Confidence: **99.18%**
725. **`homeassistant/components/homekit_controller/fan.py`** -> AI Confidence: **99.18%**
726. **`homeassistant/components/homekit_controller/light.py`** -> AI Confidence: **99.18%**
727. **`homeassistant/components/homekit_controller/media_player.py`** -> AI Confidence: **99.18%**
728. **`homeassistant/components/homematic/binary_sensor.py`** -> AI Confidence: **99.18%**
729. **`homeassistant/components/homematic/cover.py`** -> AI Confidence: **99.18%**
730. **`homeassistant/components/homematicip_cloud/__init__.py`** -> AI Confidence: **99.18%**
731. **`homeassistant/components/homematicip_cloud/config_flow.py`** -> AI Confidence: **99.18%**
732. **`homeassistant/components/homematicip_cloud/helpers.py`** -> AI Confidence: **99.18%**
733. **`homeassistant/components/homematicip_cloud/light.py`** -> AI Confidence: **99.18%**
734. **`homeassistant/components/homematicip_cloud/sensor.py`** -> AI Confidence: **99.18%**
735. **`homeassistant/components/homevolt/config_flow.py`** -> AI Confidence: **99.18%**
736. **`homeassistant/components/homewizard/config_flow.py`** -> AI Confidence: **99.18%**
737. **`homeassistant/components/homewizard/select.py`** -> AI Confidence: **99.18%**
738. **`homeassistant/components/homeworks/config_flow.py`** -> AI Confidence: **99.18%**
739. **`homeassistant/components/hr_energy_qube/config_flow.py`** -> AI Confidence: **99.18%**
740. **`homeassistant/components/http/__init__.py`** -> AI Confidence: **99.18%**
741. **`homeassistant/components/http/ban.py`** -> AI Confidence: **99.18%**
742. **`homeassistant/components/http/cors.py`** -> AI Confidence: **99.18%**
743. **`homeassistant/components/hue/config_flow.py`** -> AI Confidence: **99.18%**
744. **`homeassistant/components/hue/device_trigger.py`** -> AI Confidence: **99.18%**
745. **`homeassistant/components/hue/scene.py`** -> AI Confidence: **99.18%**
746. **`homeassistant/components/hue/v1/device_trigger.py`** -> AI Confidence: **99.18%**
747. **`homeassistant/components/hue/v1/hue_event.py`** -> AI Confidence: **99.18%**
748. **`homeassistant/components/hue/v1/sensor_base.py`** -> AI Confidence: **99.18%**
749. **`homeassistant/components/hue_ble/config_flow.py`** -> AI Confidence: **99.18%**
750. **`homeassistant/components/hue_ble/light.py`** -> AI Confidence: **99.18%**
751. **`homeassistant/components/huisbaasje/coordinator.py`** -> AI Confidence: **99.18%**
752. **`homeassistant/components/humidifier/device_action.py`** -> AI Confidence: **99.18%**
753. **`homeassistant/components/humidifier/device_condition.py`** -> AI Confidence: **99.18%**
754. **`homeassistant/components/humidifier/device_trigger.py`** -> AI Confidence: **99.18%**
755. **`homeassistant/components/husqvarna_automower/calendar.py`** -> AI Confidence: **99.18%**
756. **`homeassistant/components/husqvarna_automower/event.py`** -> AI Confidence: **99.18%**
757. **`homeassistant/components/husqvarna_automower/lawn_mower.py`** -> AI Confidence: **99.18%**
758. **`homeassistant/components/husqvarna_automower/number.py`** -> AI Confidence: **99.18%**
759. **`homeassistant/components/husqvarna_automower_ble/lawn_mower.py`** -> AI Confidence: **99.18%**
760. **`homeassistant/components/hvv_departures/binary_sensor.py`** -> AI Confidence: **99.18%**
761. **`homeassistant/components/hydrawise/entity.py`** -> AI Confidence: **99.18%**
762. **`homeassistant/components/hyperion/config_flow.py`** -> AI Confidence: **99.18%**
763. **`homeassistant/components/iammeter/sensor.py`** -> AI Confidence: **99.18%**
764. **`homeassistant/components/iaqualink/__init__.py`** -> AI Confidence: **99.18%**
765. **`homeassistant/components/ibeacon/config_flow.py`** -> AI Confidence: **99.18%**
766. **`homeassistant/components/icloud/config_flow.py`** -> AI Confidence: **99.18%**
767. **`homeassistant/components/idasen_desk/config_flow.py`** -> AI Confidence: **99.18%**
768. **`homeassistant/components/idrive_e2/backup.py`** -> AI Confidence: **99.18%**
769. **`homeassistant/components/ifttt/__init__.py`** -> AI Confidence: **99.18%**
770. **`homeassistant/components/ihc/manual_setup.py`** -> AI Confidence: **99.18%**
771. **`homeassistant/components/image_processing/__init__.py`** -> AI Confidence: **99.18%**
772. **`homeassistant/components/imap/config_flow.py`** -> AI Confidence: **99.18%**
773. **`homeassistant/components/immich/config_flow.py`** -> AI Confidence: **99.18%**
774. **`homeassistant/components/immich/sensor.py`** -> AI Confidence: **99.18%**
775. **`homeassistant/components/indevolt/sensor.py`** -> AI Confidence: **99.18%**
776. **`homeassistant/components/influxdb/config_flow.py`** -> AI Confidence: **99.18%**
777. **`homeassistant/components/inkbird/config_flow.py`** -> AI Confidence: **99.18%**
778. **`homeassistant/components/input_boolean/reproduce_state.py`** -> AI Confidence: **99.18%**
779. **`homeassistant/components/input_number/reproduce_state.py`** -> AI Confidence: **99.18%**
780. **`homeassistant/components/insteon/api/config.py`** -> AI Confidence: **99.18%**
781. **`homeassistant/components/insteon/api/device.py`** -> AI Confidence: **99.18%**
782. **`homeassistant/components/intelliclima/fan.py`** -> AI Confidence: **99.18%**
783. **`homeassistant/components/intelliclima/select.py`** -> AI Confidence: **99.18%**
784. **`homeassistant/components/intellifire/__init__.py`** -> AI Confidence: **99.18%**
785. **`homeassistant/components/iotty/coordinator.py`** -> AI Confidence: **99.18%**
786. **`homeassistant/components/iotty/cover.py`** -> AI Confidence: **99.18%**
787. **`homeassistant/components/iperf3/__init__.py`** -> AI Confidence: **99.18%**
788. **`homeassistant/components/ipma/weather.py`** -> AI Confidence: **99.18%**
789. **`homeassistant/components/ipp/config_flow.py`** -> AI Confidence: **99.18%**
790. **`homeassistant/components/irm_kmi/weather.py`** -> AI Confidence: **99.18%**
791. **`homeassistant/components/iron_os/config_flow.py`** -> AI Confidence: **99.18%**
792. **`homeassistant/components/iron_os/number.py`** -> AI Confidence: **99.18%**
793. **`homeassistant/components/iron_os/select.py`** -> AI Confidence: **99.18%**
794. **`homeassistant/components/ista_ecotrend/config_flow.py`** -> AI Confidence: **99.18%**
795. **`homeassistant/components/isy994/__init__.py`** -> AI Confidence: **99.18%**
796. **`homeassistant/components/isy994/climate.py`** -> AI Confidence: **99.18%**
797. **`homeassistant/components/isy994/config_flow.py`** -> AI Confidence: **99.18%**
798. **`homeassistant/components/isy994/cover.py`** -> AI Confidence: **99.18%**
799. **`homeassistant/components/isy994/light.py`** -> AI Confidence: **99.18%**
800. **`homeassistant/components/isy994/number.py`** -> AI Confidence: **99.18%**
801. **`homeassistant/components/isy994/select.py`** -> AI Confidence: **99.18%**
802. **`homeassistant/components/isy994/sensor.py`** -> AI Confidence: **99.18%**
803. **`homeassistant/components/itunes/media_player.py`** -> AI Confidence: **99.18%**
804. **`homeassistant/components/ituran/config_flow.py`** -> AI Confidence: **99.18%**
805. **`homeassistant/components/izone/climate.py`** -> AI Confidence: **99.18%**
806. **`homeassistant/components/jellyfin/media_source.py`** -> AI Confidence: **99.18%**
807. **`homeassistant/components/jellyfin/remote.py`** -> AI Confidence: **99.18%**
808. **`homeassistant/components/joaoapps_join/__init__.py`** -> AI Confidence: **99.18%**
809. **`homeassistant/components/keenetic_ndms2/__init__.py`** -> AI Confidence: **99.18%**
810. **`homeassistant/components/keenetic_ndms2/config_flow.py`** -> AI Confidence: **99.18%**
811. **`homeassistant/components/keenetic_ndms2/device_tracker.py`** -> AI Confidence: **99.18%**
812. **`homeassistant/components/kegtron/config_flow.py`** -> AI Confidence: **99.18%**
813. **`homeassistant/components/keymitt_ble/config_flow.py`** -> AI Confidence: **99.18%**
814. **`homeassistant/components/kitchen_sink/weather.py`** -> AI Confidence: **99.18%**
815. **`homeassistant/components/knx/__init__.py`** -> AI Confidence: **99.18%**
816. **`homeassistant/components/knx/cover.py`** -> AI Confidence: **99.18%**
817. **`homeassistant/components/knx/fan.py`** -> AI Confidence: **99.18%**
818. **`homeassistant/components/knx/knx_module.py`** -> AI Confidence: **99.18%**
819. **`homeassistant/components/knx/project.py`** -> AI Confidence: **99.18%**
820. **`homeassistant/components/knx/schema.py`** -> AI Confidence: **99.18%**
821. **`homeassistant/components/knx/storage/config_store.py`** -> AI Confidence: **99.18%**
822. **`homeassistant/components/knx/storage/entity_store_schema.py`** -> AI Confidence: **99.18%**
823. **`homeassistant/components/knx/storage/serialize.py`** -> AI Confidence: **99.18%**
824. **`homeassistant/components/kodi/config_flow.py`** -> AI Confidence: **99.18%**
825. **`homeassistant/components/kodi/media_player.py`** -> AI Confidence: **99.18%**
826. **`homeassistant/components/kodi/notify.py`** -> AI Confidence: **99.18%**
827. **`homeassistant/components/kostal_plenticore/select.py`** -> AI Confidence: **99.18%**
828. **`homeassistant/components/kraken/sensor.py`** -> AI Confidence: **99.18%**
829. **`homeassistant/components/kulersky/__init__.py`** -> AI Confidence: **99.18%**
830. **`homeassistant/components/kwb/sensor.py`** -> AI Confidence: **99.18%**
831. **`homeassistant/components/labs/websocket_api.py`** -> AI Confidence: **99.18%**
832. **`homeassistant/components/lacrosse_view/sensor.py`** -> AI Confidence: **99.18%**
833. **`homeassistant/components/lamarzocco/calendar.py`** -> AI Confidence: **99.18%**
834. **`homeassistant/components/lamarzocco/config_flow.py`** -> AI Confidence: **99.18%**
835. **`homeassistant/components/lametric/config_flow.py`** -> AI Confidence: **99.18%**
836. **`homeassistant/components/lastfm/coordinator.py`** -> AI Confidence: **99.18%**
837. **`homeassistant/components/lcn/__init__.py`** -> AI Confidence: **99.18%**
838. **`homeassistant/components/lcn/climate.py`** -> AI Confidence: **99.18%**
839. **`homeassistant/components/lcn/device_trigger.py`** -> AI Confidence: **99.18%**
840. **`homeassistant/components/lcn/scene.py`** -> AI Confidence: **99.18%**
841. **`homeassistant/components/lcn/sensor.py`** -> AI Confidence: **99.18%**
842. **`homeassistant/components/lcn/switch.py`** -> AI Confidence: **99.18%**
843. **`homeassistant/components/ld2410_ble/config_flow.py`** -> AI Confidence: **99.18%**
844. **`homeassistant/components/leaone/config_flow.py`** -> AI Confidence: **99.18%**
845. **`homeassistant/components/led_ble/__init__.py`** -> AI Confidence: **99.18%**
846. **`homeassistant/components/letpot/select.py`** -> AI Confidence: **99.18%**
847. **`homeassistant/components/lg_infrared/config_flow.py`** -> AI Confidence: **99.18%**
848. **`homeassistant/components/lg_netcast/media_player.py`** -> AI Confidence: **99.18%**
849. **`homeassistant/components/lg_thinq/binary_sensor.py`** -> AI Confidence: **99.18%**
850. **`homeassistant/components/lg_thinq/event.py`** -> AI Confidence: **99.18%**
851. **`homeassistant/components/lg_thinq/select.py`** -> AI Confidence: **99.18%**
852. **`homeassistant/components/lg_thinq/switch.py`** -> AI Confidence: **99.18%**
853. **`homeassistant/components/lg_thinq/vacuum.py`** -> AI Confidence: **99.18%**
854. **`homeassistant/components/lidarr/sensor.py`** -> AI Confidence: **99.18%**
855. **`homeassistant/components/liebherr/__init__.py`** -> AI Confidence: **99.18%**
856. **`homeassistant/components/liebherr/light.py`** -> AI Confidence: **99.18%**
857. **`homeassistant/components/liebherr/number.py`** -> AI Confidence: **99.18%**
858. **`homeassistant/components/liebherr/switch.py`** -> AI Confidence: **99.18%**
859. **`homeassistant/components/lifx/__init__.py`** -> AI Confidence: **99.18%**
860. **`homeassistant/components/lifx/config_flow.py`** -> AI Confidence: **99.18%**
861. **`homeassistant/components/lifx/coordinator.py`** -> AI Confidence: **99.18%**
862. **`homeassistant/components/lifx/manager.py`** -> AI Confidence: **99.18%**
863. **`homeassistant/components/lightwave/__init__.py`** -> AI Confidence: **99.18%**
864. **`homeassistant/components/linkplay/media_player.py`** -> AI Confidence: **99.18%**
865. **`homeassistant/components/linksys_smart/device_tracker.py`** -> AI Confidence: **99.18%**
866. **`homeassistant/components/linode/switch.py`** -> AI Confidence: **99.18%**
867. **`homeassistant/components/litterrobot/__init__.py`** -> AI Confidence: **99.18%**
868. **`homeassistant/components/litterrobot/coordinator.py`** -> AI Confidence: **99.18%**
869. **`homeassistant/components/local_calendar/calendar.py`** -> AI Confidence: **99.18%**
870. **`homeassistant/components/lock/device_trigger.py`** -> AI Confidence: **99.18%**
871. **`homeassistant/components/lock/reproduce_state.py`** -> AI Confidence: **99.18%**
872. **`homeassistant/components/logbook/queries/__init__.py`** -> AI Confidence: **99.18%**
873. **`homeassistant/components/logbook/rest_api.py`** -> AI Confidence: **99.18%**
874. **`homeassistant/components/logger/helpers.py`** -> AI Confidence: **99.18%**
875. **`homeassistant/components/lojack/config_flow.py`** -> AI Confidence: **99.18%**
876. **`homeassistant/components/lookin/__init__.py`** -> AI Confidence: **99.18%**
877. **`homeassistant/components/lookin/climate.py`** -> AI Confidence: **99.18%**
878. **`homeassistant/components/lookin/media_player.py`** -> AI Confidence: **99.18%**
879. **`homeassistant/components/loqed/coordinator.py`** -> AI Confidence: **99.18%**
880. **`homeassistant/components/lovelace/dashboard.py`** -> AI Confidence: **99.18%**
881. **`homeassistant/components/lutron/event.py`** -> AI Confidence: **99.18%**
882. **`homeassistant/components/lutron/fan.py`** -> AI Confidence: **99.18%**
883. **`homeassistant/components/lutron/light.py`** -> AI Confidence: **99.18%**
884. **`homeassistant/components/lutron_caseta/__init__.py`** -> AI Confidence: **99.18%**
885. **`homeassistant/components/lutron_caseta/config_flow.py`** -> AI Confidence: **99.18%**
886. **`homeassistant/components/lutron_caseta/device_trigger.py`** -> AI Confidence: **99.18%**
887. **`homeassistant/components/lutron_caseta/light.py`** -> AI Confidence: **99.18%**
888. **`homeassistant/components/madvr/config_flow.py`** -> AI Confidence: **99.18%**
889. **`homeassistant/components/mailgun/__init__.py`** -> AI Confidence: **99.18%**
890. **`homeassistant/components/mastodon/services.py`** -> AI Confidence: **99.18%**
891. **`homeassistant/components/matter/__init__.py`** -> AI Confidence: **99.18%**
892. **`homeassistant/components/matter/config_flow.py`** -> AI Confidence: **99.18%**
893. **`homeassistant/components/matter/cover.py`** -> AI Confidence: **99.18%**
894. **`homeassistant/components/matter/entity.py`** -> AI Confidence: **99.18%**
895. **`homeassistant/components/matter/event.py`** -> AI Confidence: **99.18%**
896. **`homeassistant/components/matter/helpers.py`** -> AI Confidence: **99.18%**
897. **`homeassistant/components/matter/select.py`** -> AI Confidence: **99.18%**
898. **`homeassistant/components/matter/valve.py`** -> AI Confidence: **99.18%**
899. **`homeassistant/components/mcp/config_flow.py`** -> AI Confidence: **99.18%**
900. **`homeassistant/components/mcp/coordinator.py`** -> AI Confidence: **99.18%**
901. **`homeassistant/components/mcp_server/config_flow.py`** -> AI Confidence: **99.18%**
902. **`homeassistant/components/mealie/calendar.py`** -> AI Confidence: **99.18%**
903. **`homeassistant/components/media_player/__init__.py`** -> AI Confidence: **99.18%**
904. **`homeassistant/components/media_player/device_condition.py`** -> AI Confidence: **99.18%**
905. **`homeassistant/components/media_player/device_trigger.py`** -> AI Confidence: **99.18%**
906. **`homeassistant/components/media_source/models.py`** -> AI Confidence: **99.18%**
907. **`homeassistant/components/melcloud/climate.py`** -> AI Confidence: **99.18%**
908. **`homeassistant/components/melcloud/coordinator.py`** -> AI Confidence: **99.18%**
909. **`homeassistant/components/melcloud/sensor.py`** -> AI Confidence: **99.18%**
910. **`homeassistant/components/melnor/config_flow.py`** -> AI Confidence: **99.18%**
911. **`homeassistant/components/met/__init__.py`** -> AI Confidence: **99.18%**
912. **`homeassistant/components/met/config_flow.py`** -> AI Confidence: **99.18%**
913. **`homeassistant/components/met/weather.py`** -> AI Confidence: **99.18%**
914. **`homeassistant/components/met_eireann/weather.py`** -> AI Confidence: **99.18%**
915. **`homeassistant/components/meteo_lt/config_flow.py`** -> AI Confidence: **99.18%**
916. **`homeassistant/components/meteo_lt/weather.py`** -> AI Confidence: **99.18%**
917. **`homeassistant/components/metoffice/sensor.py`** -> AI Confidence: **99.18%**
918. **`homeassistant/components/mfi/sensor.py`** -> AI Confidence: **99.18%**
919. **`homeassistant/components/microbees/climate.py`** -> AI Confidence: **99.18%**
920. **`homeassistant/components/microbees/coordinator.py`** -> AI Confidence: **99.18%**
921. **`homeassistant/components/microbees/cover.py`** -> AI Confidence: **99.18%**
922. **`homeassistant/components/microsoft_face_detect/image_processing.py`** -> AI Confidence: **99.18%**
923. **`homeassistant/components/microsoft_face_identify/image_processing.py`** -> AI Confidence: **99.18%**
924. **`homeassistant/components/miele/climate.py`** -> AI Confidence: **99.18%**
925. **`homeassistant/components/miele/diagnostics.py`** -> AI Confidence: **99.18%**
926. **`homeassistant/components/miele/fan.py`** -> AI Confidence: **99.18%**
927. **`homeassistant/components/miele/services.py`** -> AI Confidence: **99.18%**
928. **`homeassistant/components/mikrotik/coordinator.py`** -> AI Confidence: **99.18%**
929. **`homeassistant/components/mikrotik/device_tracker.py`** -> AI Confidence: **99.18%**
930. **`homeassistant/components/mill/sensor.py`** -> AI Confidence: **99.18%**
931. **`homeassistant/components/minecraft_server/__init__.py`** -> AI Confidence: **99.18%**
932. **`homeassistant/components/minecraft_server/api.py`** -> AI Confidence: **99.18%**
933. **`homeassistant/components/mjpeg/camera.py`** -> AI Confidence: **99.18%**
934. **`homeassistant/components/moat/config_flow.py`** -> AI Confidence: **99.18%**
935. **`homeassistant/components/mobile_app/__init__.py`** -> AI Confidence: **99.18%**
936. **`homeassistant/components/mobile_app/logbook.py`** -> AI Confidence: **99.18%**
937. **`homeassistant/components/mobile_app/sensor.py`** -> AI Confidence: **99.18%**
938. **`homeassistant/components/mobile_app/util.py`** -> AI Confidence: **99.18%**
939. **`homeassistant/components/mobile_app/webhook.py`** -> AI Confidence: **99.18%**
940. **`homeassistant/components/mochad/light.py`** -> AI Confidence: **99.18%**
941. **`homeassistant/components/mochad/switch.py`** -> AI Confidence: **99.18%**
942. **`homeassistant/components/modbus/cover.py`** -> AI Confidence: **99.18%**
943. **`homeassistant/components/monoprice/config_flow.py`** -> AI Confidence: **99.18%**
944. **`homeassistant/components/monoprice/media_player.py`** -> AI Confidence: **99.18%**
945. **`homeassistant/components/moon/sensor.py`** -> AI Confidence: **99.18%**
946. **`homeassistant/components/mopeka/config_flow.py`** -> AI Confidence: **99.18%**
947. **`homeassistant/components/motion_blinds/coordinator.py`** -> AI Confidence: **99.18%**
948. **`homeassistant/components/motion_blinds/cover.py`** -> AI Confidence: **99.18%**
949. **`homeassistant/components/motionblinds_ble/config_flow.py`** -> AI Confidence: **99.18%**
950. **`homeassistant/components/motionblinds_ble/sensor.py`** -> AI Confidence: **99.18%**
951. **`homeassistant/components/motioneye/camera.py`** -> AI Confidence: **99.18%**
952. **`homeassistant/components/motioneye/config_flow.py`** -> AI Confidence: **99.18%**
953. **`homeassistant/components/motionmount/config_flow.py`** -> AI Confidence: **99.18%**
954. **`homeassistant/components/mqtt/__init__.py`** -> AI Confidence: **99.18%**
955. **`homeassistant/components/mqtt/alarm_control_panel.py`** -> AI Confidence: **99.18%**
956. **`homeassistant/components/mqtt/device_tracker.py`** -> AI Confidence: **99.18%**
957. **`homeassistant/components/mqtt/lock.py`** -> AI Confidence: **99.18%**
958. **`homeassistant/components/mqtt/number.py`** -> AI Confidence: **99.18%**
959. **`homeassistant/components/mqtt/update.py`** -> AI Confidence: **99.18%**
960. **`homeassistant/components/mqtt/vacuum.py`** -> AI Confidence: **99.18%**
961. **`homeassistant/components/music_assistant/config_flow.py`** -> AI Confidence: **99.18%**
962. **`homeassistant/components/music_assistant/schemas.py`** -> AI Confidence: **99.18%**
963. **`homeassistant/components/mvglive/sensor.py`** -> AI Confidence: **99.18%**
964. **`homeassistant/components/myneomitis/__init__.py`** -> AI Confidence: **99.18%**
965. **`homeassistant/components/mysensors/__init__.py`** -> AI Confidence: **99.18%**
966. **`homeassistant/components/mysensors/climate.py`** -> AI Confidence: **99.18%**
967. **`homeassistant/components/mysensors/gateway.py`** -> AI Confidence: **99.18%**
968. **`homeassistant/components/mysensors/helpers.py`** -> AI Confidence: **99.18%**
969. **`homeassistant/components/mystrom/sensor.py`** -> AI Confidence: **99.18%**
970. **`homeassistant/components/myuplink/binary_sensor.py`** -> AI Confidence: **99.18%**
971. **`homeassistant/components/myuplink/number.py`** -> AI Confidence: **99.18%**
972. **`homeassistant/components/namecheapdns/config_flow.py`** -> AI Confidence: **99.18%**
973. **`homeassistant/components/nanoleaf/light.py`** -> AI Confidence: **99.18%**
974. **`homeassistant/components/nasweb/coordinator.py`** -> AI Confidence: **99.18%**
975. **`homeassistant/components/nasweb/switch.py`** -> AI Confidence: **99.18%**
976. **`homeassistant/components/neato/camera.py`** -> AI Confidence: **99.18%**
977. **`homeassistant/components/neato/switch.py`** -> AI Confidence: **99.18%**
978. **`homeassistant/components/nest/__init__.py`** -> AI Confidence: **99.18%**
979. **`homeassistant/components/nest/config_flow.py`** -> AI Confidence: **99.18%**
980. **`homeassistant/components/nest/device_info.py`** -> AI Confidence: **99.18%**
981. **`homeassistant/components/nest/diagnostics.py`** -> AI Confidence: **99.18%**
982. **`homeassistant/components/nest/event.py`** -> AI Confidence: **99.18%**
983. **`homeassistant/components/netatmo/select.py`** -> AI Confidence: **99.18%**
984. **`homeassistant/components/netdata/sensor.py`** -> AI Confidence: **99.18%**
985. **`homeassistant/components/netgear/__init__.py`** -> AI Confidence: **99.18%**
986. **`homeassistant/components/netgear/config_flow.py`** -> AI Confidence: **99.18%**
987. **`homeassistant/components/netgear/sensor.py`** -> AI Confidence: **99.18%**
988. **`homeassistant/components/nextbus/coordinator.py`** -> AI Confidence: **99.18%**
989. **`homeassistant/components/nextcloud/coordinator.py`** -> AI Confidence: **99.18%**
990. **`homeassistant/components/nibe_heatpump/number.py`** -> AI Confidence: **99.18%**
991. **`homeassistant/components/nice_go/coordinator.py`** -> AI Confidence: **99.18%**
992. **`homeassistant/components/nina/binary_sensor.py`** -> AI Confidence: **99.18%**
993. **`homeassistant/components/nina/sensor.py`** -> AI Confidence: **99.18%**
994. **`homeassistant/components/nintendo_parental_controls/config_flow.py`** -> AI Confidence: **99.18%**
995. **`homeassistant/components/nintendo_parental_controls/services.py`** -> AI Confidence: **99.18%**
996. **`homeassistant/components/nissan_leaf/sensor.py`** -> AI Confidence: **99.18%**
997. **`homeassistant/components/nmap_tracker/config_flow.py`** -> AI Confidence: **99.18%**
998. **`homeassistant/components/noaa_tides/sensor.py`** -> AI Confidence: **99.18%**
999. **`homeassistant/components/nobo_hub/select.py`** -> AI Confidence: **99.18%**
1000. **`homeassistant/components/nordpool/coordinator.py`** -> AI Confidence: **99.18%**
1001. **`homeassistant/components/notion/__init__.py`** -> AI Confidence: **99.18%**
1002. **`homeassistant/components/notion/coordinator.py`** -> AI Confidence: **99.18%**
1003. **`homeassistant/components/notion/sensor.py`** -> AI Confidence: **99.18%**
1004. **`homeassistant/components/nrgkick/config_flow.py`** -> AI Confidence: **99.18%**
1005. **`homeassistant/components/ntfy/config_flow.py`** -> AI Confidence: **99.18%**
1006. **`homeassistant/components/ntfy/notify.py`** -> AI Confidence: **99.18%**
1007. **`homeassistant/components/nuheat/climate.py`** -> AI Confidence: **99.18%**
1008. **`homeassistant/components/nuki/__init__.py`** -> AI Confidence: **99.18%**
1009. **`homeassistant/components/nuki/coordinator.py`** -> AI Confidence: **99.18%**
1010. **`homeassistant/components/number/__init__.py`** -> AI Confidence: **99.18%**
1011. **`homeassistant/components/nut/button.py`** -> AI Confidence: **99.18%**
1012. **`homeassistant/components/nut/device_action.py`** -> AI Confidence: **99.18%**
1013. **`homeassistant/components/nut/switch.py`** -> AI Confidence: **99.18%**
1014. **`homeassistant/components/nws/coordinator.py`** -> AI Confidence: **99.18%**
1015. **`homeassistant/components/nx584/binary_sensor.py`** -> AI Confidence: **99.18%**
1016. **`homeassistant/components/nzbget/config_flow.py`** -> AI Confidence: **99.18%**
1017. **`homeassistant/components/oasa_telematics/sensor.py`** -> AI Confidence: **99.18%**
1018. **`homeassistant/components/octoprint/__init__.py`** -> AI Confidence: **99.18%**
1019. **`homeassistant/components/octoprint/number.py`** -> AI Confidence: **99.18%**
1020. **`homeassistant/components/ombi/sensor.py`** -> AI Confidence: **99.18%**
1021. **`homeassistant/components/omnilogic/sensor.py`** -> AI Confidence: **99.18%**
1022. **`homeassistant/components/onboarding/__init__.py`** -> AI Confidence: **99.18%**
1023. **`homeassistant/components/onedrive/config_flow.py`** -> AI Confidence: **99.18%**
1024. **`homeassistant/components/onedrive_for_business/config_flow.py`** -> AI Confidence: **99.18%**
1025. **`homeassistant/components/onewire/binary_sensor.py`** -> AI Confidence: **99.18%**
1026. **`homeassistant/components/onewire/config_flow.py`** -> AI Confidence: **99.18%**
1027. **`homeassistant/components/onkyo/coordinator.py`** -> AI Confidence: **99.18%**
1028. **`homeassistant/components/onkyo/receiver.py`** -> AI Confidence: **99.18%**
1029. **`homeassistant/components/onvif/binary_sensor.py`** -> AI Confidence: **99.18%**
1030. **`homeassistant/components/onvif/sensor.py`** -> AI Confidence: **99.18%**
1031. **`homeassistant/components/open_meteo/weather.py`** -> AI Confidence: **99.18%**
1032. **`homeassistant/components/open_router/config_flow.py`** -> AI Confidence: **99.18%**
1033. **`homeassistant/components/openai_conversation/tts.py`** -> AI Confidence: **99.18%**
1034. **`homeassistant/components/openalpr_cloud/image_processing.py`** -> AI Confidence: **99.18%**
1035. **`homeassistant/components/opendisplay/config_flow.py`** -> AI Confidence: **99.18%**
1036. **`homeassistant/components/opendisplay/services.py`** -> AI Confidence: **99.18%**
1037. **`homeassistant/components/openevse/config_flow.py`** -> AI Confidence: **99.18%**
1038. **`homeassistant/components/opengarage/cover.py`** -> AI Confidence: **99.18%**
1039. **`homeassistant/components/openhardwaremonitor/sensor.py`** -> AI Confidence: **99.18%**
1040. **`homeassistant/components/openrgb/coordinator.py`** -> AI Confidence: **99.18%**
1041. **`homeassistant/components/opensky/config_flow.py`** -> AI Confidence: **99.18%**
1042. **`homeassistant/components/opentherm_gw/climate.py`** -> AI Confidence: **99.18%**
1043. **`homeassistant/components/opentherm_gw/select.py`** -> AI Confidence: **99.18%**
1044. **`homeassistant/components/openuv/coordinator.py`** -> AI Confidence: **99.18%**
1045. **`homeassistant/components/openweathermap/coordinator.py`** -> AI Confidence: **99.18%**
1046. **`homeassistant/components/opower/config_flow.py`** -> AI Confidence: **99.18%**
1047. **`homeassistant/components/opple/light.py`** -> AI Confidence: **99.18%**
1048. **`homeassistant/components/oralb/config_flow.py`** -> AI Confidence: **99.18%**
1049. **`homeassistant/components/oralb/sensor.py`** -> AI Confidence: **99.18%**
1050. **`homeassistant/components/otbr/websocket_api.py`** -> AI Confidence: **99.18%**
1051. **`homeassistant/components/otp/config_flow.py`** -> AI Confidence: **99.18%**
1052. **`homeassistant/components/ourgroceries/todo.py`** -> AI Confidence: **99.18%**
1053. **`homeassistant/components/overkiz/__init__.py`** -> AI Confidence: **99.18%**
1054. **`homeassistant/components/overkiz/climate/atlantic_heat_recovery_ventilation.py`** -> AI Confidence: **99.18%**
1055. **`homeassistant/components/overkiz/climate/hitachi_air_to_water_heating_zone.py`** -> AI Confidence: **99.18%**
1056. **`homeassistant/components/overkiz/climate/somfy_thermostat.py`** -> AI Confidence: **99.18%**
1057. **`homeassistant/components/overkiz/config_flow.py`** -> AI Confidence: **99.18%**
1058. **`homeassistant/components/overkiz/cover/__init__.py`** -> AI Confidence: **99.18%**
1059. **`homeassistant/components/overkiz/entity.py`** -> AI Confidence: **99.18%**
1060. **`homeassistant/components/overkiz/light.py`** -> AI Confidence: **99.18%**
1061. **`homeassistant/components/overkiz/number.py`** -> AI Confidence: **99.18%**
1062. **`homeassistant/components/overkiz/sensor.py`** -> AI Confidence: **99.18%**
1063. **`homeassistant/components/overseerr/event.py`** -> AI Confidence: **99.18%**
1064. **`homeassistant/components/ovo_energy/config_flow.py`** -> AI Confidence: **99.18%**
1065. **`homeassistant/components/owntracks/__init__.py`** -> AI Confidence: **99.18%**
1066. **`homeassistant/components/owntracks/config_flow.py`** -> AI Confidence: **99.18%**
1067. **`homeassistant/components/panasonic_bluray/media_player.py`** -> AI Confidence: **99.18%**
1068. **`homeassistant/components/peblar/config_flow.py`** -> AI Confidence: **99.18%**
1069. **`homeassistant/components/permobil/config_flow.py`** -> AI Confidence: **99.18%**
1070. **`homeassistant/components/pglab/discovery.py`** -> AI Confidence: **99.18%**
1071. **`homeassistant/components/philips_js/coordinator.py`** -> AI Confidence: **99.18%**
1072. **`homeassistant/components/philips_js/remote.py`** -> AI Confidence: **99.18%**
1073. **`homeassistant/components/pi_hole/__init__.py`** -> AI Confidence: **99.18%**
1074. **`homeassistant/components/pi_hole/coordinator.py`** -> AI Confidence: **99.18%**
1075. **`homeassistant/components/picnic/coordinator.py`** -> AI Confidence: **99.18%**
1076. **`homeassistant/components/picnic/services.py`** -> AI Confidence: **99.18%**
1077. **`homeassistant/components/pilight/__init__.py`** -> AI Confidence: **99.18%**
1078. **`homeassistant/components/pilight/binary_sensor.py`** -> AI Confidence: **99.18%**
1079. **`homeassistant/components/pioneer/media_player.py`** -> AI Confidence: **99.18%**
1080. **`homeassistant/components/pjlink/media_player.py`** -> AI Confidence: **99.18%**
1081. **`homeassistant/components/plaato/sensor.py`** -> AI Confidence: **99.18%**
1082. **`homeassistant/components/playstation_network/entity.py`** -> AI Confidence: **99.18%**
1083. **`homeassistant/components/playstation_network/notify.py`** -> AI Confidence: **99.18%**
1084. **`homeassistant/components/plex/config_flow.py`** -> AI Confidence: **99.18%**
1085. **`homeassistant/components/plugwise/__init__.py`** -> AI Confidence: **99.18%**
1086. **`homeassistant/components/plugwise/binary_sensor.py`** -> AI Confidence: **99.18%**
1087. **`homeassistant/components/plugwise/coordinator.py`** -> AI Confidence: **99.18%**
1088. **`homeassistant/components/pooldose/select.py`** -> AI Confidence: **99.18%**
1089. **`homeassistant/components/portainer/binary_sensor.py`** -> AI Confidence: **99.18%**
1090. **`homeassistant/components/portainer/entity.py`** -> AI Confidence: **99.18%**
1091. **`homeassistant/components/powerfox/config_flow.py`** -> AI Confidence: **99.18%**
1092. **`homeassistant/components/powerfox/sensor.py`** -> AI Confidence: **99.18%**
1093. **`homeassistant/components/powerwall/__init__.py`** -> AI Confidence: **99.18%**
1094. **`homeassistant/components/prana/fan.py`** -> AI Confidence: **99.18%**
1095. **`homeassistant/components/proxmoxve/button.py`** -> AI Confidence: **99.18%**
1096. **`homeassistant/components/pulseaudio_loopback/switch.py`** -> AI Confidence: **99.18%**
1097. **`homeassistant/components/purpleair/config_flow.py`** -> AI Confidence: **99.18%**
1098. **`homeassistant/components/pushover/notify.py`** -> AI Confidence: **99.18%**
1099. **`homeassistant/components/pyload/config_flow.py`** -> AI Confidence: **99.18%**
1100. **`homeassistant/components/qbus/config_flow.py`** -> AI Confidence: **99.18%**
1101. **`homeassistant/components/qbus/coordinator.py`** -> AI Confidence: **99.18%**
1102. **`homeassistant/components/qbus/entity.py`** -> AI Confidence: **99.18%**
1103. **`homeassistant/components/qingping/config_flow.py`** -> AI Confidence: **99.18%**
1104. **`homeassistant/components/qnap/config_flow.py`** -> AI Confidence: **99.18%**
1105. **`homeassistant/components/qnap_qsw/entity.py`** -> AI Confidence: **99.18%**
1106. **`homeassistant/components/qnap_qsw/sensor.py`** -> AI Confidence: **99.18%**
1107. **`homeassistant/components/rachio/device.py`** -> AI Confidence: **99.18%**
1108. **`homeassistant/components/rachio/webhooks.py`** -> AI Confidence: **99.18%**
1109. **`homeassistant/components/rainbird/__init__.py`** -> AI Confidence: **99.18%**
1110. **`homeassistant/components/rainforest_eagle/coordinator.py`** -> AI Confidence: **99.18%**
1111. **`homeassistant/components/rainforest_raven/config_flow.py`** -> AI Confidence: **99.18%**
1112. **`homeassistant/components/rainforest_raven/coordinator.py`** -> AI Confidence: **99.18%**
1113. **`homeassistant/components/rainmachine/__init__.py`** -> AI Confidence: **99.18%**
1114. **`homeassistant/components/rainmachine/sensor.py`** -> AI Confidence: **99.18%**
1115. **`homeassistant/components/rainmachine/switch.py`** -> AI Confidence: **99.18%**
1116. **`homeassistant/components/rainmachine/util.py`** -> AI Confidence: **99.18%**
1117. **`homeassistant/components/rapt_ble/config_flow.py`** -> AI Confidence: **99.18%**
1118. **`homeassistant/components/recollect_waste/sensor.py`** -> AI Confidence: **99.18%**
1119. **`homeassistant/components/recorder/db_schema.py`** -> AI Confidence: **99.18%**
1120. **`homeassistant/components/recorder/entity_registry.py`** -> AI Confidence: **99.18%**
1121. **`homeassistant/components/recorder/repack.py`** -> AI Confidence: **99.18%**
1122. **`homeassistant/components/recorder/services.py`** -> AI Confidence: **99.18%**
1123. **`homeassistant/components/recorder/table_managers/event_data.py`** -> AI Confidence: **99.18%**
1124. **`homeassistant/components/recorder/table_managers/state_attributes.py`** -> AI Confidence: **99.18%**
1125. **`homeassistant/components/recorder/table_managers/states_meta.py`** -> AI Confidence: **99.18%**
1126. **`homeassistant/components/remote/reproduce_state.py`** -> AI Confidence: **99.18%**
1127. **`homeassistant/components/renault/device_tracker.py`** -> AI Confidence: **99.18%**
1128. **`homeassistant/components/renault/renault_hub.py`** -> AI Confidence: **99.18%**
1129. **`homeassistant/components/renault/services.py`** -> AI Confidence: **99.18%**
1130. **`homeassistant/components/reolink/config_flow.py`** -> AI Confidence: **99.18%**
1131. **`homeassistant/components/reolink/sensor.py`** -> AI Confidence: **99.18%**
1132. **`homeassistant/components/reolink/services.py`** -> AI Confidence: **99.18%**
1133. **`homeassistant/components/reolink/switch.py`** -> AI Confidence: **99.18%**
1134. **`homeassistant/components/reolink/update.py`** -> AI Confidence: **99.18%**
1135. **`homeassistant/components/reolink/util.py`** -> AI Confidence: **99.18%**
1136. **`homeassistant/components/reolink/views.py`** -> AI Confidence: **99.18%**
1137. **`homeassistant/components/repetier/__init__.py`** -> AI Confidence: **99.18%**
1138. **`homeassistant/components/repetier/sensor.py`** -> AI Confidence: **99.18%**
1139. **`homeassistant/components/rest/__init__.py`** -> AI Confidence: **99.18%**
1140. **`homeassistant/components/rest/binary_sensor.py`** -> AI Confidence: **99.18%**
1141. **`homeassistant/components/rflink/light.py`** -> AI Confidence: **99.18%**
1142. **`homeassistant/components/rflink/sensor.py`** -> AI Confidence: **99.18%**
1143. **`homeassistant/components/rfxtrx/cover.py`** -> AI Confidence: **99.18%**
1144. **`homeassistant/components/rfxtrx/light.py`** -> AI Confidence: **99.18%**
1145. **`homeassistant/components/rfxtrx/siren.py`** -> AI Confidence: **99.18%**
1146. **`homeassistant/components/ridwell/calendar.py`** -> AI Confidence: **99.18%**
1147. **`homeassistant/components/ring/camera.py`** -> AI Confidence: **99.18%**
1148. **`homeassistant/components/ring/coordinator.py`** -> AI Confidence: **99.18%**
1149. **`homeassistant/components/risco/alarm_control_panel.py`** -> AI Confidence: **99.18%**
1150. **`homeassistant/components/risco/config_flow.py`** -> AI Confidence: **99.18%**
1151. **`homeassistant/components/rituals_perfume_genie/__init__.py`** -> AI Confidence: **99.18%**
1152. **`homeassistant/components/rmvtransport/sensor.py`** -> AI Confidence: **99.18%**
1153. **`homeassistant/components/roborock/__init__.py`** -> AI Confidence: **99.18%**
1154. **`homeassistant/components/roborock/binary_sensor.py`** -> AI Confidence: **99.18%**
1155. **`homeassistant/components/roborock/image.py`** -> AI Confidence: **99.18%**
1156. **`homeassistant/components/roborock/vacuum.py`** -> AI Confidence: **99.18%**
1157. **`homeassistant/components/roku/select.py`** -> AI Confidence: **99.18%**
1158. **`homeassistant/components/roon/event.py`** -> AI Confidence: **99.18%**
1159. **`homeassistant/components/roon/server.py`** -> AI Confidence: **99.18%**
1160. **`homeassistant/components/russound_rio/__init__.py`** -> AI Confidence: **99.18%**
1161. **`homeassistant/components/russound_rio/media_player.py`** -> AI Confidence: **99.18%**
1162. **`homeassistant/components/ruuvitag_ble/config_flow.py`** -> AI Confidence: **99.18%**
1163. **`homeassistant/components/samsungtv/entity.py`** -> AI Confidence: **99.18%**
1164. **`homeassistant/components/samsungtv/helpers.py`** -> AI Confidence: **99.18%**
1165. **`homeassistant/components/samsungtv/media_player.py`** -> AI Confidence: **99.18%**
1166. **`homeassistant/components/samsungtv/triggers/turn_on.py`** -> AI Confidence: **99.18%**
1167. **`homeassistant/components/satel_integra/alarm_control_panel.py`** -> AI Confidence: **99.18%**
1168. **`homeassistant/components/saunum/climate.py`** -> AI Confidence: **99.18%**
1169. **`homeassistant/components/saunum/diagnostics.py`** -> AI Confidence: **99.18%**
1170. **`homeassistant/components/schlage/coordinator.py`** -> AI Confidence: **99.18%**
1171. **`homeassistant/components/schlage/lock.py`** -> AI Confidence: **99.18%**
1172. **`homeassistant/components/screenlogic/binary_sensor.py`** -> AI Confidence: **99.18%**
1173. **`homeassistant/components/screenlogic/climate.py`** -> AI Confidence: **99.18%**
1174. **`homeassistant/components/screenlogic/number.py`** -> AI Confidence: **99.18%**
1175. **`homeassistant/components/screenlogic/sensor.py`** -> AI Confidence: **99.18%**
1176. **`homeassistant/components/screenlogic/services.py`** -> AI Confidence: **99.18%**
1177. **`homeassistant/components/script/config.py`** -> AI Confidence: **99.18%**
1178. **`homeassistant/components/season/sensor.py`** -> AI Confidence: **99.18%**
1179. **`homeassistant/components/select/device_action.py`** -> AI Confidence: **99.18%**
1180. **`homeassistant/components/sensibo/binary_sensor.py`** -> AI Confidence: **99.18%**
1181. **`homeassistant/components/sensibo/climate.py`** -> AI Confidence: **99.18%**
1182. **`homeassistant/components/sensibo/coordinator.py`** -> AI Confidence: **99.18%**
1183. **`homeassistant/components/sensibo/sensor.py`** -> AI Confidence: **99.18%**
1184. **`homeassistant/components/sensirion_ble/config_flow.py`** -> AI Confidence: **99.18%**
1185. **`homeassistant/components/sensor/device_trigger.py`** -> AI Confidence: **99.18%**
1186. **`homeassistant/components/sensorpro/config_flow.py`** -> AI Confidence: **99.18%**
1187. **`homeassistant/components/sensorpush/config_flow.py`** -> AI Confidence: **99.18%**
1188. **`homeassistant/components/serial/sensor.py`** -> AI Confidence: **99.18%**
1189. **`homeassistant/components/sfr_box/config_flow.py`** -> AI Confidence: **99.18%**
1190. **`homeassistant/components/sfr_box/sensor.py`** -> AI Confidence: **99.18%**
1191. **`homeassistant/components/sftp_storage/client.py`** -> AI Confidence: **99.18%**
1192. **`homeassistant/components/sharkiq/coordinator.py`** -> AI Confidence: **99.18%**
1193. **`homeassistant/components/shelly/__init__.py`** -> AI Confidence: **99.18%**
1194. **`homeassistant/components/shelly/binary_sensor.py`** -> AI Confidence: **99.18%**
1195. **`homeassistant/components/shelly/device_trigger.py`** -> AI Confidence: **99.18%**
1196. **`homeassistant/components/shelly/logbook.py`** -> AI Confidence: **99.18%**
1197. **`homeassistant/components/shelly/repairs.py`** -> AI Confidence: **99.18%**
1198. **`homeassistant/components/shopping_list/__init__.py`** -> AI Confidence: **99.18%**
1199. **`homeassistant/components/sia/alarm_control_panel.py`** -> AI Confidence: **99.18%**
1200. **`homeassistant/components/sia/binary_sensor.py`** -> AI Confidence: **99.18%**
1201. **`homeassistant/components/sia/hub.py`** -> AI Confidence: **99.18%**
1202. **`homeassistant/components/sighthound/image_processing.py`** -> AI Confidence: **99.18%**
1203. **`homeassistant/components/simplisafe/alarm_control_panel.py`** -> AI Confidence: **99.18%**
1204. **`homeassistant/components/siren/__init__.py`** -> AI Confidence: **99.18%**
1205. **`homeassistant/components/sisyphus/__init__.py`** -> AI Confidence: **99.18%**
1206. **`homeassistant/components/sleep_as_android/sensor.py`** -> AI Confidence: **99.18%**
1207. **`homeassistant/components/sleepiq/select.py`** -> AI Confidence: **99.18%**
1208. **`homeassistant/components/slide/cover.py`** -> AI Confidence: **99.18%**
1209. **`homeassistant/components/slimproto/media_player.py`** -> AI Confidence: **99.18%**
1210. **`homeassistant/components/sma/config_flow.py`** -> AI Confidence: **99.18%**
1211. **`homeassistant/components/smappee/binary_sensor.py`** -> AI Confidence: **99.18%**
1212. **`homeassistant/components/smappee/config_flow.py`** -> AI Confidence: **99.18%**
1213. **`homeassistant/components/smappee/switch.py`** -> AI Confidence: **99.18%**
1214. **`homeassistant/components/smartthings/fan.py`** -> AI Confidence: **99.18%**
1215. **`homeassistant/components/smhi/weather.py`** -> AI Confidence: **99.18%**
1216. **`homeassistant/components/smlight/light.py`** -> AI Confidence: **99.18%**
1217. **`homeassistant/components/smlight/sensor.py`** -> AI Confidence: **99.18%**
1218. **`homeassistant/components/snapcast/media_player.py`** -> AI Confidence: **99.18%**
1219. **`homeassistant/components/solarlog/__init__.py`** -> AI Confidence: **99.18%**
1220. **`homeassistant/components/solarlog/config_flow.py`** -> AI Confidence: **99.18%**
1221. **`homeassistant/components/solarlog/coordinator.py`** -> AI Confidence: **99.18%**
1222. **`homeassistant/components/solarlog/sensor.py`** -> AI Confidence: **99.18%**
1223. **`homeassistant/components/somfy_mylink/cover.py`** -> AI Confidence: **99.18%**
1224. **`homeassistant/components/sonos/alarms.py`** -> AI Confidence: **99.18%**
1225. **`homeassistant/components/sonos/switch.py`** -> AI Confidence: **99.18%**
1226. **`homeassistant/components/soundtouch/__init__.py`** -> AI Confidence: **99.18%**
1227. **`homeassistant/components/spotify/coordinator.py`** -> AI Confidence: **99.18%**
1228. **`homeassistant/components/spotify/media_player.py`** -> AI Confidence: **99.18%**
1229. **`homeassistant/components/squeezebox/config_flow.py`** -> AI Confidence: **99.18%**
1230. **`homeassistant/components/squeezebox/coordinator.py`** -> AI Confidence: **99.18%**
1231. **`homeassistant/components/squeezebox/update.py`** -> AI Confidence: **99.18%**
1232. **`homeassistant/components/srp_energy/config_flow.py`** -> AI Confidence: **99.18%**
1233. **`homeassistant/components/starline/config_flow.py`** -> AI Confidence: **99.18%**
1234. **`homeassistant/components/starlink/coordinator.py`** -> AI Confidence: **99.18%**
1235. **`homeassistant/components/statistics/config_flow.py`** -> AI Confidence: **99.18%**
1236. **`homeassistant/components/steam_online/coordinator.py`** -> AI Confidence: **99.18%**
1237. **`homeassistant/components/steam_online/sensor.py`** -> AI Confidence: **99.18%**
1238. **`homeassistant/components/steamist/config_flow.py`** -> AI Confidence: **99.18%**
1239. **`homeassistant/components/stt/__init__.py`** -> AI Confidence: **99.18%**
1240. **`homeassistant/components/stt/legacy.py`** -> AI Confidence: **99.18%**
1241. **`homeassistant/components/subaru/sensor.py`** -> AI Confidence: **99.18%**
1242. **`homeassistant/components/suez_water/config_flow.py`** -> AI Confidence: **99.18%**
1243. **`homeassistant/components/sun/entity.py`** -> AI Confidence: **99.18%**
1244. **`homeassistant/components/sunricher_dali/__init__.py`** -> AI Confidence: **99.18%**
1245. **`homeassistant/components/sunricher_dali/config_flow.py`** -> AI Confidence: **99.18%**
1246. **`homeassistant/components/supla/__init__.py`** -> AI Confidence: **99.18%**
1247. **`homeassistant/components/surepetcare/binary_sensor.py`** -> AI Confidence: **99.18%**
1248. **`homeassistant/components/surepetcare/lock.py`** -> AI Confidence: **99.18%**
1249. **`homeassistant/components/swisscom/device_tracker.py`** -> AI Confidence: **99.18%**
1250. **`homeassistant/components/switch/reproduce_state.py`** -> AI Confidence: **99.18%**
1251. **`homeassistant/components/switch_as_x/__init__.py`** -> AI Confidence: **99.18%**
1252. **`homeassistant/components/switchbee/__init__.py`** -> AI Confidence: **99.18%**
1253. **`homeassistant/components/switchbee/climate.py`** -> AI Confidence: **99.18%**
1254. **`homeassistant/components/switchbee/light.py`** -> AI Confidence: **99.18%**
1255. **`homeassistant/components/switchbot/sensor.py`** -> AI Confidence: **99.18%**
1256. **`homeassistant/components/switchbot/services.py`** -> AI Confidence: **99.18%**
1257. **`homeassistant/components/switchbot_cloud/climate.py`** -> AI Confidence: **99.18%**
1258. **`homeassistant/components/switchbot_cloud/light.py`** -> AI Confidence: **99.18%**
1259. **`homeassistant/components/switcher_kis/entity.py`** -> AI Confidence: **99.18%**
1260. **`homeassistant/components/syncthing/__init__.py`** -> AI Confidence: **99.18%**
1261. **`homeassistant/components/synology_dsm/backup.py`** -> AI Confidence: **99.18%**
1262. **`homeassistant/components/synology_dsm/coordinator.py`** -> AI Confidence: **99.18%**
1263. **`homeassistant/components/system_bridge/__init__.py`** -> AI Confidence: **99.18%**
1264. **`homeassistant/components/system_bridge/coordinator.py`** -> AI Confidence: **99.18%**
1265. **`homeassistant/components/system_bridge/sensor.py`** -> AI Confidence: **99.18%**
1266. **`homeassistant/components/systemnexa2/config_flow.py`** -> AI Confidence: **99.18%**
1267. **`homeassistant/components/systemnexa2/coordinator.py`** -> AI Confidence: **99.18%**
1268. **`homeassistant/components/tado/__init__.py`** -> AI Confidence: **99.18%**
1269. **`homeassistant/components/tado/binary_sensor.py`** -> AI Confidence: **99.18%**
1270. **`homeassistant/components/tado/coordinator.py`** -> AI Confidence: **99.18%**
1271. **`homeassistant/components/tado/water_heater.py`** -> AI Confidence: **99.18%**
1272. **`homeassistant/components/tag/trigger.py`** -> AI Confidence: **99.18%**
1273. **`homeassistant/components/tami4/config_flow.py`** -> AI Confidence: **99.18%**
1274. **`homeassistant/components/tankerkoenig/sensor.py`** -> AI Confidence: **99.18%**
1275. **`homeassistant/components/tasmota/__init__.py`** -> AI Confidence: **99.18%**
1276. **`homeassistant/components/tasmota/config_flow.py`** -> AI Confidence: **99.18%**
1277. **`homeassistant/components/tasmota/device_trigger.py`** -> AI Confidence: **99.18%**
1278. **`homeassistant/components/tautulli/sensor.py`** -> AI Confidence: **99.18%**
1279. **`homeassistant/components/telegram_bot/config_flow.py`** -> AI Confidence: **99.18%**
1280. **`homeassistant/components/tellduslive/__init__.py`** -> AI Confidence: **99.18%**
1281. **`homeassistant/components/tellstick/entity.py`** -> AI Confidence: **99.18%**
1282. **`homeassistant/components/teltonika/config_flow.py`** -> AI Confidence: **99.18%**
1283. **`homeassistant/components/template/__init__.py`** -> AI Confidence: **99.18%**
1284. **`homeassistant/components/template/config.py`** -> AI Confidence: **99.18%**
1285. **`homeassistant/components/template/cover.py`** -> AI Confidence: **99.18%**
1286. **`homeassistant/components/template/entity.py`** -> AI Confidence: **99.18%**
1287. **`homeassistant/components/template/fan.py`** -> AI Confidence: **99.18%**
1288. **`homeassistant/components/template/lock.py`** -> AI Confidence: **99.18%**
1289. **`homeassistant/components/template/update.py`** -> AI Confidence: **99.18%**
1290. **`homeassistant/components/template/weather.py`** -> AI Confidence: **99.18%**
1291. **`homeassistant/components/tesla_fleet/__init__.py`** -> AI Confidence: **99.18%**
1292. **`homeassistant/components/tesla_fleet/binary_sensor.py`** -> AI Confidence: **99.18%**
1293. **`homeassistant/components/tesla_fleet/config_flow.py`** -> AI Confidence: **99.18%**
1294. **`homeassistant/components/tesla_fleet/media_player.py`** -> AI Confidence: **99.18%**
1295. **`homeassistant/components/tesla_fleet/select.py`** -> AI Confidence: **99.18%**
1296. **`homeassistant/components/teslemetry/device_tracker.py`** -> AI Confidence: **99.18%**
1297. **`homeassistant/components/teslemetry/lock.py`** -> AI Confidence: **99.18%**
1298. **`homeassistant/components/teslemetry/number.py`** -> AI Confidence: **99.18%**
1299. **`homeassistant/components/tessie/coordinator.py`** -> AI Confidence: **99.18%**
1300. **`homeassistant/components/text/__init__.py`** -> AI Confidence: **99.18%**
1301. **`homeassistant/components/thermobeacon/config_flow.py`** -> AI Confidence: **99.18%**
1302. **`homeassistant/components/thermopro/config_flow.py`** -> AI Confidence: **99.18%**
1303. **`homeassistant/components/thethingsnetwork/config_flow.py`** -> AI Confidence: **99.18%**
1304. **`homeassistant/components/thingspeak/__init__.py`** -> AI Confidence: **99.18%**
1305. **`homeassistant/components/thinkingcleaner/sensor.py`** -> AI Confidence: **99.18%**
1306. **`homeassistant/components/tibber/services.py`** -> AI Confidence: **99.18%**
1307. **`homeassistant/components/tile/device_tracker.py`** -> AI Confidence: **99.18%**
1308. **`homeassistant/components/tilt_ble/config_flow.py`** -> AI Confidence: **99.18%**
1309. **`homeassistant/components/timer/__init__.py`** -> AI Confidence: **99.18%**
1310. **`homeassistant/components/tod/binary_sensor.py`** -> AI Confidence: **99.18%**
1311. **`homeassistant/components/togrill/number.py`** -> AI Confidence: **99.18%**
1312. **`homeassistant/components/tomorrowio/coordinator.py`** -> AI Confidence: **99.18%**
1313. **`homeassistant/components/tomorrowio/sensor.py`** -> AI Confidence: **99.18%**
1314. **`homeassistant/components/toon/coordinator.py`** -> AI Confidence: **99.18%**
1315. **`homeassistant/components/totalconnect/alarm_control_panel.py`** -> AI Confidence: **99.18%**
1316. **`homeassistant/components/totalconnect/binary_sensor.py`** -> AI Confidence: **99.18%**
1317. **`homeassistant/components/totalconnect/config_flow.py`** -> AI Confidence: **99.18%**
1318. **`homeassistant/components/touchline_sl/__init__.py`** -> AI Confidence: **99.18%**
1319. **`homeassistant/components/tplink/deprecate.py`** -> AI Confidence: **99.18%**
1320. **`homeassistant/components/tplink_omada/binary_sensor.py`** -> AI Confidence: **99.18%**
1321. **`homeassistant/components/tplink_omada/coordinator.py`** -> AI Confidence: **99.18%**
1322. **`homeassistant/components/tplink_omada/services.py`** -> AI Confidence: **99.18%**
1323. **`homeassistant/components/tplink_omada/switch.py`** -> AI Confidence: **99.18%**
1324. **`homeassistant/components/traccar_server/diagnostics.py`** -> AI Confidence: **99.18%**
1325. **`homeassistant/components/tradfri/__init__.py`** -> AI Confidence: **99.18%**
1326. **`homeassistant/components/tradfri/config_flow.py`** -> AI Confidence: **99.18%**
1327. **`homeassistant/components/tradfri/coordinator.py`** -> AI Confidence: **99.18%**
1328. **`homeassistant/components/trafikverket_train/coordinator.py`** -> AI Confidence: **99.18%**
1329. **`homeassistant/components/transmission/sensor.py`** -> AI Confidence: **99.18%**
1330. **`homeassistant/components/trend/binary_sensor.py`** -> AI Confidence: **99.18%**
1331. **`homeassistant/components/tuya/config_flow.py`** -> AI Confidence: **99.18%**
1332. **`homeassistant/components/tuya/cover.py`** -> AI Confidence: **99.18%**
1333. **`homeassistant/components/tuya/diagnostics.py`** -> AI Confidence: **99.18%**
1334. **`homeassistant/components/tuya/fan.py`** -> AI Confidence: **99.18%**
1335. **`homeassistant/components/tuya/number.py`** -> AI Confidence: **99.18%**
1336. **`homeassistant/components/tuya/sensor.py`** -> AI Confidence: **99.18%**
1337. **`homeassistant/components/tuya/vacuum.py`** -> AI Confidence: **99.18%**
1338. **`homeassistant/components/twentemilieu/calendar.py`** -> AI Confidence: **99.18%**
1339. **`homeassistant/components/twinkly/coordinator.py`** -> AI Confidence: **99.18%**
1340. **`homeassistant/components/twitter/notify.py`** -> AI Confidence: **99.18%**
1341. **`homeassistant/components/unifi/device_tracker.py`** -> AI Confidence: **99.18%**
1342. **`homeassistant/components/unifi/light.py`** -> AI Confidence: **99.18%**
1343. **`homeassistant/components/unifi/sensor.py`** -> AI Confidence: **99.18%**
1344. **`homeassistant/components/unifi_access/select.py`** -> AI Confidence: **99.18%**
1345. **`homeassistant/components/unifi_access/sensor.py`** -> AI Confidence: **99.18%**
1346. **`homeassistant/components/unifiprotect/__init__.py`** -> AI Confidence: **99.18%**
1347. **`homeassistant/components/unifiprotect/light.py`** -> AI Confidence: **99.18%**
1348. **`homeassistant/components/unifiprotect/migrate.py`** -> AI Confidence: **99.18%**
1349. **`homeassistant/components/unifiprotect/repairs.py`** -> AI Confidence: **99.18%**
1350. **`homeassistant/components/unifiprotect/sensor.py`** -> AI Confidence: **99.18%**
1351. **`homeassistant/components/unifiprotect/services.py`** -> AI Confidence: **99.18%**
1352. **`homeassistant/components/upb/config_flow.py`** -> AI Confidence: **99.18%**
1353. **`homeassistant/components/upb/light.py`** -> AI Confidence: **99.18%**
1354. **`homeassistant/components/upnp/__init__.py`** -> AI Confidence: **99.18%**
1355. **`homeassistant/components/upnp/config_flow.py`** -> AI Confidence: **99.18%**
1356. **`homeassistant/components/uptime_kuma/config_flow.py`** -> AI Confidence: **99.18%**
1357. **`homeassistant/components/uptime_kuma/coordinator.py`** -> AI Confidence: **99.18%**
1358. **`homeassistant/components/uptimerobot/config_flow.py`** -> AI Confidence: **99.18%**
1359. **`homeassistant/components/uptimerobot/coordinator.py`** -> AI Confidence: **99.18%**
1360. **`homeassistant/components/usage_prediction/common_control.py`** -> AI Confidence: **99.18%**
1361. **`homeassistant/components/usb/__init__.py`** -> AI Confidence: **99.18%**
1362. **`homeassistant/components/uvc/camera.py`** -> AI Confidence: **99.18%**
1363. **`homeassistant/components/vacuum/__init__.py`** -> AI Confidence: **99.18%**
1364. **`homeassistant/components/vacuum/device_condition.py`** -> AI Confidence: **99.18%**
1365. **`homeassistant/components/vegehub/coordinator.py`** -> AI Confidence: **99.18%**
1366. **`homeassistant/components/velbus/config_flow.py`** -> AI Confidence: **99.18%**
1367. **`homeassistant/components/velux/__init__.py`** -> AI Confidence: **99.18%**
1368. **`homeassistant/components/venstar/sensor.py`** -> AI Confidence: **99.18%**
1369. **`homeassistant/components/vera/__init__.py`** -> AI Confidence: **99.18%**
1370. **`homeassistant/components/vera/climate.py`** -> AI Confidence: **99.18%**
1371. **`homeassistant/components/vera/entity.py`** -> AI Confidence: **99.18%**
1372. **`homeassistant/components/vera/light.py`** -> AI Confidence: **99.18%**
1373. **`homeassistant/components/verisure/config_flow.py`** -> AI Confidence: **99.18%**
1374. **`homeassistant/components/versasense/__init__.py`** -> AI Confidence: **99.18%**
1375. **`homeassistant/components/versasense/switch.py`** -> AI Confidence: **99.18%**
1376. **`homeassistant/components/vesync/light.py`** -> AI Confidence: **99.18%**
1377. **`homeassistant/components/vesync/select.py`** -> AI Confidence: **99.18%**
1378. **`homeassistant/components/viaggiatreno/sensor.py`** -> AI Confidence: **99.18%**
1379. **`homeassistant/components/vicare/__init__.py`** -> AI Confidence: **99.18%**
1380. **`homeassistant/components/vicare/entity.py`** -> AI Confidence: **99.18%**
1381. **`homeassistant/components/vicare/number.py`** -> AI Confidence: **99.18%**
1382. **`homeassistant/components/vicare/water_heater.py`** -> AI Confidence: **99.18%**
1383. **`homeassistant/components/victron_ble/config_flow.py`** -> AI Confidence: **99.18%**
1384. **`homeassistant/components/victron_ble/sensor.py`** -> AI Confidence: **99.18%**
1385. **`homeassistant/components/victron_remote_monitoring/config_flow.py`** -> AI Confidence: **99.18%**
1386. **`homeassistant/components/vlc_telnet/media_player.py`** -> AI Confidence: **99.18%**
1387. **`homeassistant/components/volvo/button.py`** -> AI Confidence: **99.18%**
1388. **`homeassistant/components/volvo/coordinator.py`** -> AI Confidence: **99.18%**
1389. **`homeassistant/components/volvo/device_tracker.py`** -> AI Confidence: **99.18%**
1390. **`homeassistant/components/volvo/lock.py`** -> AI Confidence: **99.18%**
1391. **`homeassistant/components/wallbox/coordinator.py`** -> AI Confidence: **99.18%**
1392. **`homeassistant/components/waqi/config_flow.py`** -> AI Confidence: **99.18%**
1393. **`homeassistant/components/waterfurnace/config_flow.py`** -> AI Confidence: **99.18%**
1394. **`homeassistant/components/waterfurnace/coordinator.py`** -> AI Confidence: **99.18%**
1395. **`homeassistant/components/watergate/__init__.py`** -> AI Confidence: **99.18%**
1396. **`homeassistant/components/watergate/config_flow.py`** -> AI Confidence: **99.18%**
1397. **`homeassistant/components/watts/coordinator.py`** -> AI Confidence: **99.18%**
1398. **`homeassistant/components/waze_travel_time/__init__.py`** -> AI Confidence: **99.18%**
1399. **`homeassistant/components/webhook/__init__.py`** -> AI Confidence: **99.18%**
1400. **`homeassistant/components/webmin/helpers.py`** -> AI Confidence: **99.18%**
1401. **`homeassistant/components/webostv/config_flow.py`** -> AI Confidence: **99.18%**
1402. **`homeassistant/components/webostv/triggers/turn_on.py`** -> AI Confidence: **99.18%**
1403. **`homeassistant/components/websocket_api/decorators.py`** -> AI Confidence: **99.18%**
1404. **`homeassistant/components/wemo/__init__.py`** -> AI Confidence: **99.18%**
1405. **`homeassistant/components/wemo/coordinator.py`** -> AI Confidence: **99.18%**
1406. **`homeassistant/components/wemo/light.py`** -> AI Confidence: **99.18%**
1407. **`homeassistant/components/wemo/switch.py`** -> AI Confidence: **99.18%**
1408. **`homeassistant/components/whois/sensor.py`** -> AI Confidence: **99.18%**
1409. **`homeassistant/components/wilight/config_flow.py`** -> AI Confidence: **99.18%**
1410. **`homeassistant/components/wilight/fan.py`** -> AI Confidence: **99.18%**
1411. **`homeassistant/components/withings/__init__.py`** -> AI Confidence: **99.18%**
1412. **`homeassistant/components/withings/coordinator.py`** -> AI Confidence: **99.18%**
1413. **`homeassistant/components/withings/diagnostics.py`** -> AI Confidence: **99.18%**
1414. **`homeassistant/components/wiz/discovery.py`** -> AI Confidence: **99.18%**
1415. **`homeassistant/components/wiz/fan.py`** -> AI Confidence: **99.18%**
1416. **`homeassistant/components/wled/__init__.py`** -> AI Confidence: **99.18%**
1417. **`homeassistant/components/wled/select.py`** -> AI Confidence: **99.18%**
1418. **`homeassistant/components/wled/sensor.py`** -> AI Confidence: **99.18%**
1419. **`homeassistant/components/wled/update.py`** -> AI Confidence: **99.18%**
1420. **`homeassistant/components/wolflink/__init__.py`** -> AI Confidence: **99.18%**
1421. **`homeassistant/components/workday/calendar.py`** -> AI Confidence: **99.18%**
1422. **`homeassistant/components/workday/repairs.py`** -> AI Confidence: **99.18%**
1423. **`homeassistant/components/ws66i/config_flow.py`** -> AI Confidence: **99.18%**
1424. **`homeassistant/components/wyoming/config_flow.py`** -> AI Confidence: **99.18%**
1425. **`homeassistant/components/wyoming/devices.py`** -> AI Confidence: **99.18%**
1426. **`homeassistant/components/xbox/config_flow.py`** -> AI Confidence: **99.18%**
1427. **`homeassistant/components/xbox/image.py`** -> AI Confidence: **99.18%**
1428. **`homeassistant/components/xbox/media_player.py`** -> AI Confidence: **99.18%**
1429. **`homeassistant/components/xeoma/camera.py`** -> AI Confidence: **99.18%**
1430. **`homeassistant/components/xiaomi/camera.py`** -> AI Confidence: **99.18%**
1431. **`homeassistant/components/xiaomi_aqara/__init__.py`** -> AI Confidence: **99.18%**
1432. **`homeassistant/components/xiaomi_aqara/cover.py`** -> AI Confidence: **99.18%**
1433. **`homeassistant/components/xiaomi_aqara/entity.py`** -> AI Confidence: **99.18%**
1434. **`homeassistant/components/xiaomi_ble/__init__.py`** -> AI Confidence: **99.18%**
1435. **`homeassistant/components/xiaomi_ble/config_flow.py`** -> AI Confidence: **99.18%**
1436. **`homeassistant/components/xiaomi_ble/sensor.py`** -> AI Confidence: **99.18%**
1437. **`homeassistant/components/xiaomi_miio/number.py`** -> AI Confidence: **99.18%**
1438. **`homeassistant/components/xiaomi_tv/media_player.py`** -> AI Confidence: **99.18%**
1439. **`homeassistant/components/yale/binary_sensor.py`** -> AI Confidence: **99.18%**
1440. **`homeassistant/components/yale/event.py`** -> AI Confidence: **99.18%**
1441. **`homeassistant/components/yale/lock.py`** -> AI Confidence: **99.18%**
1442. **`homeassistant/components/yalexs_ble/__init__.py`** -> AI Confidence: **99.18%**
1443. **`homeassistant/components/yalexs_ble/config_flow.py`** -> AI Confidence: **99.18%**
1444. **`homeassistant/components/yeelight/config_flow.py`** -> AI Confidence: **99.18%**
1445. **`homeassistant/components/yeelight/device.py`** -> AI Confidence: **99.18%**
1446. **`homeassistant/components/yeelight/light.py`** -> AI Confidence: **99.18%**
1447. **`homeassistant/components/yeelight/scanner.py`** -> AI Confidence: **99.18%**
1448. **`homeassistant/components/yolink/__init__.py`** -> AI Confidence: **99.18%**
1449. **`homeassistant/components/yolink/climate.py`** -> AI Confidence: **99.18%**
1450. **`homeassistant/components/youtube/config_flow.py`** -> AI Confidence: **99.18%**
1451. **`homeassistant/components/zeroconf/__init__.py`** -> AI Confidence: **99.18%**
1452. **`homeassistant/components/zerproc/light.py`** -> AI Confidence: **99.18%**
1453. **`homeassistant/components/zestimate/sensor.py`** -> AI Confidence: **99.18%**
1454. **`homeassistant/components/zha/__init__.py`** -> AI Confidence: **99.18%**
1455. **`homeassistant/components/zha/device_action.py`** -> AI Confidence: **99.18%**
1456. **`homeassistant/components/zha/entity.py`** -> AI Confidence: **99.18%**
1457. **`homeassistant/components/zha/light.py`** -> AI Confidence: **99.18%**
1458. **`homeassistant/components/zha/radio_manager.py`** -> AI Confidence: **99.18%**
1459. **`homeassistant/components/zhong_hong/climate.py`** -> AI Confidence: **99.18%**
1460. **`homeassistant/components/zone/__init__.py`** -> AI Confidence: **99.18%**
1461. **`homeassistant/components/zwave_js/device_condition.py`** -> AI Confidence: **99.18%**
1462. **`homeassistant/components/zwave_js/diagnostics.py`** -> AI Confidence: **99.18%**
1463. **`homeassistant/components/zwave_js/discovery_data_template.py`** -> AI Confidence: **99.18%**
1464. **`homeassistant/components/zwave_js/fan.py`** -> AI Confidence: **99.18%**
1465. **`homeassistant/components/zwave_js/humidifier.py`** -> AI Confidence: **99.18%**
1466. **`homeassistant/components/zwave_js/logbook.py`** -> AI Confidence: **99.18%**
1467. **`homeassistant/components/zwave_js/number.py`** -> AI Confidence: **99.18%**
1468. **`homeassistant/components/zwave_js/select.py`** -> AI Confidence: **99.18%**
1469. **`homeassistant/components/zwave_js/triggers/value_updated.py`** -> AI Confidence: **99.18%**
1470. **`homeassistant/components/zwave_me/config_flow.py`** -> AI Confidence: **99.18%**
1471. **`homeassistant/helpers/automation.py`** -> AI Confidence: **99.18%**
1472. **`homeassistant/helpers/category_registry.py`** -> AI Confidence: **99.18%**
1473. **`homeassistant/helpers/chat_session.py`** -> AI Confidence: **99.18%**
1474. **`homeassistant/helpers/entity_component.py`** -> AI Confidence: **99.18%**
1475. **`homeassistant/helpers/floor_registry.py`** -> AI Confidence: **99.18%**
1476. **`homeassistant/helpers/recorder.py`** -> AI Confidence: **99.18%**
1477. **`homeassistant/helpers/restore_state.py`** -> AI Confidence: **99.18%**
1478. **`homeassistant/helpers/significant_change.py`** -> AI Confidence: **99.18%**
1479. **`homeassistant/helpers/state.py`** -> AI Confidence: **99.18%**
1480. **`homeassistant/helpers/sun.py`** -> AI Confidence: **99.18%**
1481. **`homeassistant/helpers/system_info.py`** -> AI Confidence: **99.18%**
1482. **`homeassistant/helpers/template/extensions/labels.py`** -> AI Confidence: **99.18%**
1483. **`homeassistant/runner.py`** -> AI Confidence: **99.18%**
1484. **`homeassistant/util/async_.py`** -> AI Confidence: **99.18%**
1485. **`tests/common.py`** -> AI Confidence: **99.18%**
1486. **`tests/components/actron_air/test_climate.py`** -> AI Confidence: **99.18%**
1487. **`tests/components/aemet/util.py`** -> AI Confidence: **99.18%**
1488. **`tests/components/ai_task/test_init.py`** -> AI Confidence: **99.18%**
1489. **`tests/components/airzone_cloud/util.py`** -> AI Confidence: **99.18%**
1490. **`tests/components/amberelectric/helpers.py`** -> AI Confidence: **99.18%**
1491. **`tests/components/androidtv/test_remote.py`** -> AI Confidence: **99.18%**
1492. **`tests/components/backblaze_b2/test_config_flow.py`** -> AI Confidence: **99.18%**
1493. **`tests/components/backup/common.py`** -> AI Confidence: **99.18%**
1494. **`tests/components/bluetooth/__init__.py`** -> AI Confidence: **99.18%**
1495. **`tests/components/bluetooth/test_advertisement_tracker.py`** -> AI Confidence: **99.18%**
1496. **`tests/components/broadlink/test_sensor.py`** -> AI Confidence: **99.18%**
1497. **`tests/components/dlna_dms/test_dms_device_source.py`** -> AI Confidence: **99.18%**
1498. **`tests/components/dlna_dms/test_media_source.py`** -> AI Confidence: **99.18%**
1499. **`tests/components/enphase_envoy/test_switch.py`** -> AI Confidence: **99.18%**
1500. **`tests/components/fan/test_init.py`** -> AI Confidence: **99.18%**
1501. **`tests/components/filter/test_sensor.py`** -> AI Confidence: **99.18%**
1502. **`tests/components/fritzbox/__init__.py`** -> AI Confidence: **99.18%**
1503. **`tests/components/fronius/__init__.py`** -> AI Confidence: **99.18%**
1504. **`tests/components/google_assistant/test_report_state.py`** -> AI Confidence: **99.18%**
1505. **`tests/components/google_photos/test_services.py`** -> AI Confidence: **99.18%**
1506. **`tests/components/home_connect/test_entity.py`** -> AI Confidence: **99.18%**
1507. **`tests/components/homeassistant_alerts/test_init.py`** -> AI Confidence: **99.18%**
1508. **`tests/components/homeassistant_hardware/test_helpers.py`** -> AI Confidence: **99.18%**
1509. **`tests/components/influxdb/test_sensor.py`** -> AI Confidence: **99.18%**
1510. **`tests/components/insteon/mock_devices.py`** -> AI Confidence: **99.18%**
1511. **`tests/components/lifx/__init__.py`** -> AI Confidence: **99.18%**
1512. **`tests/components/matrix/test_commands.py`** -> AI Confidence: **99.18%**
1513. **`tests/components/matter/common.py`** -> AI Confidence: **99.18%**
1514. **`tests/components/mikrotik/__init__.py`** -> AI Confidence: **99.18%**
1515. **`tests/components/mqtt/common.py`** -> AI Confidence: **99.18%**
1516. **`tests/components/netatmo/test_binary_sensor.py`** -> AI Confidence: **99.18%**
1517. **`tests/components/netatmo/test_device_trigger.py`** -> AI Confidence: **99.18%**
1518. **`tests/components/nice_go/test_light.py`** -> AI Confidence: **99.18%**
1519. **`tests/components/openai_conversation/test_init.py`** -> AI Confidence: **99.18%**
1520. **`tests/components/portainer/test_services.py`** -> AI Confidence: **99.18%**
1521. **`tests/components/recorder/common.py`** -> AI Confidence: **99.18%**
1522. **`tests/components/recorder/db_schema_16.py`** -> AI Confidence: **99.18%**
1523. **`tests/components/recorder/db_schema_18.py`** -> AI Confidence: **99.18%**
1524. **`tests/components/recorder/db_schema_22.py`** -> AI Confidence: **99.18%**
1525. **`tests/components/recorder/db_schema_23.py`** -> AI Confidence: **99.18%**
1526. **`tests/components/recorder/db_schema_23_with_newer_columns.py`** -> AI Confidence: **99.18%**
1527. **`tests/components/recorder/db_schema_32.py`** -> AI Confidence: **99.18%**
1528. **`tests/components/recorder/db_schema_50.py`** -> AI Confidence: **99.18%**
1529. **`tests/components/recorder/db_schema_51.py`** -> AI Confidence: **99.18%**
1530. **`tests/components/recorder/db_schema_9.py`** -> AI Confidence: **99.18%**
1531. **`tests/components/recorder/test_purge.py`** -> AI Confidence: **99.18%**
1532. **`tests/components/recorder/test_statistics_v23_migration.py`** -> AI Confidence: **99.18%**
1533. **`tests/components/refoss/__init__.py`** -> AI Confidence: **99.18%**
1534. **`tests/components/ring/common.py`** -> AI Confidence: **99.18%**
1535. **`tests/components/ruckus_unleashed/__init__.py`** -> AI Confidence: **99.18%**
1536. **`tests/components/smartthings/__init__.py`** -> AI Confidence: **99.18%**
1537. **`tests/components/snooz/__init__.py`** -> AI Confidence: **99.18%**
1538. **`tests/components/stream/test_worker.py`** -> AI Confidence: **99.18%**
1539. **`tests/components/sun/test_init.py`** -> AI Confidence: **99.18%**
1540. **`tests/components/switchbot/test_light.py`** -> AI Confidence: **99.18%**
1541. **`tests/components/teslemetry/test_services.py`** -> AI Confidence: **99.18%**
1542. **`tests/components/tplink/test_init.py`** -> AI Confidence: **99.18%**
1543. **`tests/components/tradfri/common.py`** -> AI Confidence: **99.18%**
1544. **`tests/components/tuya/__init__.py`** -> AI Confidence: **99.18%**
1545. **`tests/components/unifiprotect/__init__.py`** -> AI Confidence: **99.18%**
1546. **`tests/components/usage_prediction/test_common_control.py`** -> AI Confidence: **99.18%**
1547. **`tests/components/vera/common.py`** -> AI Confidence: **99.18%**
1548. **`tests/components/weatherkit/__init__.py`** -> AI Confidence: **99.18%**
1549. **`tests/components/wyoming/test_satellite.py`** -> AI Confidence: **99.18%**
1550. **`tests/hassfest/test_conditions.py`** -> AI Confidence: **99.18%**
1551. **`tests/hassfest/test_triggers.py`** -> AI Confidence: **99.18%**
1552. **`tests/helpers/test_chat_session.py`** -> AI Confidence: **99.18%**
1553. **`tests/helpers/test_check_config.py`** -> AI Confidence: **99.18%**
1554. **`tests/helpers/test_frame.py`** -> AI Confidence: **99.18%**
1555. **`tests/helpers/test_script.py`** -> AI Confidence: **99.18%**
1556. **`tests/helpers/test_sun.py`** -> AI Confidence: **99.18%**
1557. **`tests/pylint/test_decorator.py`** -> AI Confidence: **99.18%**
1558. **`tests/test_backup_restore.py`** -> AI Confidence: **99.18%**
1559. **`tests/test_util/aiohttp.py`** -> AI Confidence: **99.18%**
1560. **`tests/util/test_unit_system.py`** -> AI Confidence: **99.18%**
1561. **`homeassistant/util/unit_conversion.py`** -> AI Confidence: **99.18%**
1562. **`script/hassfest/docker/entrypoint.sh`** -> AI Confidence: **99.17%**
1563. **`script/setup`** -> AI Confidence: **99.17%**
1564. **`tests/auth/providers/test_command_line_cmd.sh`** -> AI Confidence: **99.17%**
1565. **`homeassistant/auth/__init__.py`** -> AI Confidence: **99.16%**
1566. **`homeassistant/auth/providers/homeassistant.py`** -> AI Confidence: **99.16%**
1567. **`homeassistant/auth/providers/trusted_networks.py`** -> AI Confidence: **99.16%**
1568. **`homeassistant/bootstrap.py`** -> AI Confidence: **99.16%**
1569. **`homeassistant/components/acmeda/config_flow.py`** -> AI Confidence: **99.16%**
1570. **`homeassistant/components/ads/cover.py`** -> AI Confidence: **99.16%**
1571. **`homeassistant/components/advantage_air/climate.py`** -> AI Confidence: **99.16%**
1572. **`homeassistant/components/ai_task/task.py`** -> AI Confidence: **99.16%**
1573. **`homeassistant/components/airgradient/select.py`** -> AI Confidence: **99.16%**
1574. **`homeassistant/components/airtouch5/climate.py`** -> AI Confidence: **99.16%**
1575. **`homeassistant/components/airvisual/__init__.py`** -> AI Confidence: **99.16%**
1576. **`homeassistant/components/airzone/climate.py`** -> AI Confidence: **99.16%**
1577. **`homeassistant/components/alarm_control_panel/device_action.py`** -> AI Confidence: **99.16%**
1578. **`homeassistant/components/alarm_control_panel/device_condition.py`** -> AI Confidence: **99.16%**
1579. **`homeassistant/components/alarmdecoder/alarm_control_panel.py`** -> AI Confidence: **99.16%**
1580. **`homeassistant/components/alarmdecoder/config_flow.py`** -> AI Confidence: **99.16%**
1581. **`homeassistant/components/alert/entity.py`** -> AI Confidence: **99.16%**
1582. **`homeassistant/components/alexa/capabilities.py`** -> AI Confidence: **99.16%**
1583. **`homeassistant/components/alexa/entities.py`** -> AI Confidence: **99.16%**
1584. **`homeassistant/components/alexa/intent.py`** -> AI Confidence: **99.16%**
1585. **`homeassistant/components/alexa/state_report.py`** -> AI Confidence: **99.16%**
1586. **`homeassistant/components/amberelectric/coordinator.py`** -> AI Confidence: **99.16%**
1587. **`homeassistant/components/amcrest/__init__.py`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `tests/components/rfxtrx/test_cover.py` -> **100.0%** Exposure
- `tests/components/thread/test_diagnostics.py` -> **100.0%** Exposure
- `tests/components/dhcp/test_init.py` -> **99.9999%** Exposure
- `tests/components/xiaomi_ble/test_event.py` -> **43.6497%** Exposure
- `tests/components/bthome/test_sensor.py` -> **14.76%** Exposure
### Exploit Generation Surface
- `homeassistant/__main__.py` -> **100.0%** Exposure
- `homeassistant/auth/__init__.py` -> **100.0%** Exposure
- `homeassistant/auth/auth_store.py` -> **100.0%** Exposure
- `homeassistant/auth/mfa_modules/insecure_example.py` -> **100.0%** Exposure
- `homeassistant/auth/mfa_modules/notify.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `homeassistant/components/dnsip/sensor.py` -> **100.0%** Exposure
- `homeassistant/components/ecovacs/button.py` -> **100.0%** Exposure
- `homeassistant/components/ecovacs/lawn_mower.py` -> **100.0%** Exposure
- `homeassistant/components/ecovacs/vacuum.py` -> **100.0%** Exposure
- `homeassistant/components/google_assistant/trait.py` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `homeassistant/components/growatt_server/number.py` -> **100.0%** Exposure
- `tests/components/anglian_water/const.py` -> **100.0%** Exposure
- `tests/components/senz/const.py` -> **100.0%** Exposure
- `tests/components/plex/fixtures/security_token.xml` -> **100.0%** Exposure
- `tests/components/lidarr/fixtures/initialize-wrong.js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `homeassistant/__main__.py` -> **100.0%** Exposure
- `homeassistant/auth/__init__.py` -> **100.0%** Exposure
- `homeassistant/auth/auth_store.py` -> **100.0%** Exposure
- `homeassistant/auth/mfa_modules/insecure_example.py` -> **100.0%** Exposure
- `homeassistant/auth/mfa_modules/notify.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `51` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `121598` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `homeassistant/components/automation/__init__.py` (PYTHON) -> Cumulative Risk: **942.4**
- **Archetype:** `file_cluster_16` (Distance: 12.128 IQR)
- **Magnitude:** 1200.96 | **LOC:** 1297 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 67.9%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Churn (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `async_added_to_hass` (Impact: 428.9), `_log_callback` (Impact: 69.4), `referenced_entities` (Impact: 44.0)

### 2. `homeassistant/helpers/restore_state.py` (PYTHON) -> Cumulative Risk: **927.29**
- **Archetype:** `file_cluster_13` (Distance: 12.088 IQR)
- **Magnitude:** 480.1 | **LOC:** 348 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `async_load` (Impact: 195.5), `async_internal_will_remove_from_hass` (Impact: 61.5), `from_dict` (Impact: 28.4)

### 3. `homeassistant/components/zwave_js/cover.py` (PYTHON) -> Cumulative Risk: **918.51**
- **Archetype:** `file_cluster_13` (Distance: 12.862 IQR)
- **Magnitude:** 468.18 | **LOC:** 582 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `on_value_update` (Impact: 28.5), `async_add_cover` (Impact: 24.8), `async_stop_cover` (Impact: 11.1)

### 4. `homeassistant/util/aiohttp.py` (PYTHON) -> Cumulative Risk: **917.95**
- **Archetype:** `file_cluster_13` (Distance: 13.635 IQR)
- **Magnitude:** 133.0 | **LOC:** 137 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Logic Bomb (99.9999%)
- **Heaviest Functions:** `serialize_response` (Impact: 21.9), `read` (Impact: 14.2), `readchunk` (Impact: 3.2)

### 5. `homeassistant/components/evohome/entity.py` (PYTHON) -> Cumulative Risk: **915.94**
- **Archetype:** `file_cluster_13` (Distance: 12.111 IQR)
- **Magnitude:** 161.44 | **LOC:** 183 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `_update_schedule` (Impact: 38.1), `setpoints` (Impact: 14.9), `_handle_coordinator_update` (Impact: 14.4)

### 6. `homeassistant/components/switchbee/cover.py` (PYTHON) -> Cumulative Risk: **912.72**
- **Archetype:** `file_cluster_4` (Distance: 12.67 IQR)
- **Magnitude:** 168.28 | **LOC:** 156 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `async_set_cover_position` (Impact: 18.3), `_update_from_coordinator` (Impact: 14.9), `_fire_somfy_command` (Impact: 13.4)

### 7. `homeassistant/components/tuya/humidifier.py` (PYTHON) -> Cumulative Risk: **911.46**
- **Archetype:** `file_cluster_13` (Distance: 11.649 IQR)
- **Magnitude:** 131.38 | **LOC:** 178 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `async_discover_device` (Impact: 30.9), `async_turn_on` (Impact: 13.4), `async_turn_off` (Impact: 13.4)

### 8. `homeassistant/components/fritz/switch.py` (PYTHON) -> Cumulative Risk: **908.99**
- **Archetype:** `file_cluster_16` (Distance: 11.569 IQR)
- **Magnitude:** 302.86 | **LOC:** 597 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `async_update` (Impact: 16.2), `_async_fetch_update` (Impact: 13.6), `available` (Impact: 10.6)

### 9. `homeassistant/components/androidtv/remote.py` (PYTHON) -> Cumulative Risk: **908.53**
- **Archetype:** `file_cluster_4` (Distance: 12.376 IQR)
- **Magnitude:** 138.0 | **LOC:** 78 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `async_send_command` (Impact: 50.1), `async_turn_on` (Impact: 10.8), `async_turn_off` (Impact: 10.8)

### 10. `homeassistant/components/lovelace/dashboard.py` (PYTHON) -> Cumulative Risk: **907.69**
- **Archetype:** `file_cluster_16` (Distance: 12.306 IQR)
- **Magnitude:** 381.66 | **LOC:** 333 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `async_save` (Impact: 40.7), `__init__` (Impact: 27.7), `_load_config` (Impact: 27.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/components/elmax/fixtures/direct/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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

### `homeassistant/components/google_assistant/trait.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.333 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.163 IQR)
- **Top Global Matches:** file_cluster_8: 11.333, file_cluster_16: 11.374, file_cluster_7: 11.466
- **Magnitude:** 4180.58 | **LOC:** 2895 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (18.2369%), Tech Debt (99.8192%)
**Top Internal Functions/Classes:**
  * `query_attributes` (Impact: 2796.3 | O(2^N) | DB: 25)
  * `execute` (Impact: 122.6 | O(N^6) | DB: 3)
  * `execute` (Impact: 83.7 | O(N^5))
  * `sync_attributes` (Impact: 54.1 | O(N^5))
  * `query_attributes` (Impact: 53.7 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 366`, `structural_boundaries: 424`, `args: 130`, `func_start: 130`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 98`, `state_mutation: 69`, `planned_debt: 1`, `duplicate_logic: 51`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 137`, `concurrency: 97`, `import: 28`
* *Defense:* `safety: 4`, `doc: 298`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` homeassistant.components.lawn_mower, homeassistant.components.valve, .error, .const, homeassistant.const, homeassistant.core, homeassistant.components.cover, homeassistant.components.humidifier...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_config_entries.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.491 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.471 IQR)
- **Top Global Matches:** file_cluster_8: 12.491, file_cluster_4: 12.715, file_cluster_16: 12.731
- **Magnitude:** 2903.64 | **LOC:** 10053 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (14.1975%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_as_dict` (Impact: 33.6 | O(N^3))
  * `mock_handlers` (Impact: 23.4 | O(N^5))
  * `test_setup_race_only_setup_once` (Impact: 22.1 | O(N^3) | DB: 1)
  * `test_async_setup_update_entry` (Impact: 16.3 | O(N^5))
  * `test_entry_setup_without_lock_raises` (Impact: 15.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 2362`, `args: 434`, `func_start: 434`, `class_start: 104`
* *Risk/State:* `safety_bypasses: 109`, `state_mutation: 56`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 91`
* *Architecture:* `io: 1`, `api: 648`, `concurrency: 1249`, `import: 34`
* *Defense:* `safety: 902`, `doc: 906`, `test: 1291`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` .common, homeassistant.helpers.service_info.zeroconf, contextlib, homeassistant.util.async_, homeassistant.const, homeassistant.core, ipaddress, homeassistant.util...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `homeassistant/helpers/entity.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.303 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.166 IQR)
- **Top Global Matches:** file_cluster_16: 13.303, file_cluster_13: 13.325, file_cluster_0: 13.361
- **Magnitude:** 2864.56 | **LOC:** 1775 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 65
- **Risk Profile:** Cognitive Load (49.9582%), Tech Debt (9.3355%)
**Top Internal Functions/Classes:**
  * `_substitute_name_placeholders` (Impact: 2183.7 | O(2^N) | DB: 65)
  * `wrap_attr` (Impact: 37.8 | O(N^6) | DB: 3)
  * `has_entity_name` (Impact: 21.2 | O(2^N))
  * `setter` (Impact: 18.9 | O(N^5) | DB: 2)
  * `_unit_of_measurement_translation_key` (Impact: 18.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 330`, `args: 96`, `func_start: 96`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 205`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 87`, `concurrency: 133`, `import: 33`
* *Defense:* `safety: 55`, `doc: 212`, `test: 5`, `sync_locks: 6`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.627
  * `Choke Point (Betweenness):` 0.000196 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` .typing, homeassistant.loader, homeassistant.core_config, homeassistant.const, .group, homeassistant.core, .device_registry, homeassistant.util...
  * `Imported By (In-Degree: 429):` (Excluded from Brief to save tokens)

### `homeassistant/config_entries.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.471 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.817 IQR)
- **Top Global Matches:** file_cluster_16: 12.471, file_cluster_13: 12.657, file_cluster_8: 12.682
- **Magnitude:** 2744.56 | **LOC:** 4084 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (37.532%), Tech Debt (53.1013%)
**Top Internal Functions/Classes:**
  * `_async_process_on_state_change` (Impact: 1059.1 | O(N^6) | DB: 36)
  * `async_remove` (Impact: 170.4 | O(N^5) | DB: 13)
  * `async_setup` (Impact: 109.5 | O(2^N))
  * `async_update_issues` (Impact: 88.6 | O(N^6) | DB: 2)
  * `async_unload` (Impact: 50.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 481`, `structural_boundaries: 610`, `args: 175`, `func_start: 175`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 93`, `state_mutation: 232`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 19`
* *Architecture:* `api: 157`, `concurrency: 293`, `import: 45`
* *Defense:* `safety: 60`, `doc: 433`, `test: 1`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.509
  * `Choke Point (Betweenness):` 0.000293 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` .util.dt, .exceptions, .components.bluetooth, copy, .helpers.service_info.dhcp, contextvars, .const, .util.enum...
  * `Imported By (In-Degree: 4104):` (Excluded from Brief to save tokens)

### `tests/helpers/test_script.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.633 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.961 IQR)
- **Top Global Matches:** file_cluster_8: 11.633, file_cluster_7: 12.015, file_cluster_4: 12.056
- **Magnitude:** 2479.38 | **LOC:** 6901 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (26.7614%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_multiple_runs_no_wait` (Impact: 807.9 | O(N^6) | DB: 9)
  * `test_referenced_devices` (Impact: 78.4 | O(N^6))
  * `test_repeat_var_in_condition` (Impact: 45.5 | O(N^5))
  * `test_script_mode_queued` (Impact: 38.3 | O(N^4) | DB: 3)
  * `test_parallel` (Impact: 36.1 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 924`, `args: 156`, `func_start: 156`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 49`, `duplicate_logic: 2`, `orphaned_logic: 51`
* *Architecture:* `api: 154`, `concurrency: 791`, `import: 23`
* *Defense:* `safety: 464`, `doc: 288`, `test: 659`, `sync_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` homeassistant.helpers.dispatcher, tests.common, contextlib, homeassistant.const, homeassistant.core, homeassistant.util, voluptuous, homeassistant.setup...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/helpers/config_validation.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.798 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.128 IQR)
- **Top Global Matches:** file_cluster_16: 11.798, file_cluster_8: 11.921, file_cluster_13: 11.979
- **Magnitude:** 2365.7 | **LOC:** 2161 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (6.0212%), Tech Debt (12.2368%)
**Top Internal Functions/Classes:**
  * `validator` (Impact: 1268.5 | O(2^N) | DB: 14)
  * `template_complex` (Impact: 56.9 | O(2^N))
  * `boolean` (Impact: 48.8 | O(2^N))
  * `string` (Impact: 42.9 | O(2^N))
  * `entities_domain` (Impact: 38.0 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 351`, `args: 113`, `func_start: 101`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 146`, `state_mutation: 45`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 12`, `api: 107`, `concurrency: 4`, `import: 33`
* *Defense:* `safety: 94`, `doc: 188`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.108
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` .typing, contextvars, contextlib, homeassistant.const, homeassistant.generated.countries, homeassistant.core, voluptuous_serialize, voluptuous...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `tests/test_core.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.346 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.108 IQR)
- **Top Global Matches:** file_cluster_4: 13.346, file_cluster_16: 13.643, file_cluster_0: 13.732
- **Magnitude:** 2303.18 | **LOC:** 3325 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (24.8775%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_state_repr` (Impact: 462.9 | O(N^5) | DB: 23)
  * `test_async_get_hass_can_be_called` (Impact: 81.1 | O(N^4) | DB: 10)
  * `test_stage_shutdown_with_exit_code` (Impact: 28.8 | O(N^3))
  * `test_split_entity_id` (Impact: 16.3 | O(N^2))
  * `test_eventbus_max_length_exceeded` (Impact: 11.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 938`, `args: 273`, `func_start: 268`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 72`, `state_mutation: 107`, `dead_code: 2`, `duplicate_logic: 6`, `orphaned_logic: 68`
* *Architecture:* `io: 1`, `api: 233`, `concurrency: 998`, `import: 26`
* *Defense:* `safety: 428`, `doc: 366`, `test: 626`, `sync_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .common, homeassistant.util.async_, homeassistant.const, homeassistant.core, homeassistant.util, voluptuous, datetime, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/loader.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.746 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.031 IQR)
- **Top Global Matches:** file_cluster_16: 12.746, file_cluster_13: 12.843, file_cluster_4: 12.877
- **Magnitude:** 2125.58 | **LOC:** 1789 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (45.5765%), Tech Debt (24.5297%)
**Top Internal Functions/Classes:**
  * `async_process_zeroconf_match_dict` (Impact: 1413.4 | O(2^N) | DB: 57)
  * `resolve_dependencies_impl` (Impact: 163.8 | O(2^N) | DB: 4)
  * `_get_custom_components` (Impact: 31.4 | O(N^2) | DB: 3)
  * `async_get_application_credentials` (Impact: 14.1 | O(N^3))
    * *Intent:* # These properties keys used to be at the top level, we relocate # them for backwards compat
  * `_async_mount_config_dir` (Impact: 6.5 | O(N^2) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 385`, `args: 101`, `func_start: 101`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 140`, `dead_code: 1`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `io: 13`, `api: 112`, `concurrency: 170`, `import: 41`
* *Defense:* `safety: 49`, `doc: 232`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.788
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` otherwise., .generated.mqtt, .generated.dhcp, .generated.config_flows, its, awesomeversion, contextlib, .const...
  * `Imported By (In-Degree: 129):` (Excluded from Brief to save tokens)

### `homeassistant/components/alexa/capabilities.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.182 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.666 IQR)
- **Top Global Matches:** file_cluster_16: 12.182, file_cluster_8: 12.424, file_cluster_7: 12.5
- **Magnitude:** 1926.38 | **LOC:** 2509 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (21.8073%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `serialize_properties` (Impact: 275.9 | O(N^5) | DB: 10)
  * `capability_resources` (Impact: 126.2 | O(N^5) | DB: 14)
  * `configuration` (Impact: 94.9 | O(2^N) | DB: 1)
  * `get_property` (Impact: 87.4 | O(N^6))
  * `get_property` (Impact: 84.9 | O(N^4) | DB: 8)
    * *Intent:* """Read and return a property."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 417`, `args: 153`, `func_start: 153`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 295`, `planned_debt: 1`, `duplicate_logic: 85`
* *Architecture:* `api: 172`, `import: 14`
* *Defense:* `safety: 10`, `doc: 368`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.092
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` homeassistant.util, .resources, homeassistant.components.climate, .errors, homeassistant.core, logging, typing, homeassistant.components...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `homeassistant/components/homekit/type_thermostats.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.265 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.388 IQR)
- **Top Global Matches:** file_cluster_8: 11.265, file_cluster_13: 11.474, file_cluster_16: 11.502
- **Magnitude:** 1920.78 | **LOC:** 942 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (30.6383%), Tech Debt (10.2825%)
**Top Internal Functions/Classes:**
  * `_hk_hvac_mode_from_state` (Impact: 1554.3 | O(2^N) | DB: 44)
  * `set_heat_cool` (Impact: 106.0 | O(N^6))
  * `__init__` (Impact: 46.3 | O(2^N) | DB: 10)
  * `async_update_state` (Impact: 40.2 | O(N^4))
    * *Intent:* # Update target operation mode if new_state.state: if new_state.state == STATE_OFF and self._off_mod...
  * `_get_target_temperature` (Impact: 5.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 79`, `args: 23`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 134`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 9`, `import: 12`
* *Defense:* `safety: 16`, `doc: 36`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` homeassistant.util.percentage, homeassistant.components.climate, logging, typing, pyhap.const, homeassistant.components.water_heater, .accessories, .util...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `homeassistant/helpers/device_registry.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.005 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.03 IQR)
- **Top Global Matches:** file_cluster_16: 11.005, file_cluster_8: 11.088, file_cluster_13: 11.199
- **Magnitude:** 1796.66 | **LOC:** 1923 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (12.9373%), Tech Debt (17.8097%)
**Top Internal Functions/Classes:**
  * `json_repr` (Impact: 1549.1 | O(N^6) | DB: 17)
    * *Intent:* # The config_entries list can be removed from the storage
  * `format_mac` (Impact: 27.9 | O(N^2))
    * *Intent:* # Not sure how formatted, return original
  * `_validate_configuration_url` (Impact: 18.6 | O(N^2))
  * `__init__` (Impact: 18.3 | O(2^N) | DB: 2)
  * `dict_repr` (Impact: 10.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 232`, `args: 64`, `func_start: 64`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 45`, `fragile_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 51`, `concurrency: 27`, `import: 35`
* *Defense:* `safety: 14`, `doc: 168`, `test: 4`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.306
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` attr, .typing, homeassistant.loader, __future__, homeassistant.util.hass_dict, homeassistant.const, homeassistant.core, .registry...
  * `Imported By (In-Degree: 1169):` (Excluded from Brief to save tokens)

### `homeassistant/core.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.358 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.276 IQR)
- **Top Global Matches:** file_cluster_16: 12.358, file_cluster_0: 12.474, file_cluster_13: 12.493
- **Magnitude:** 1785.62 | **LOC:** 2868 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (32.7334%), Tech Debt (24.9084%)
**Top Internal Functions/Classes:**
  * `async_start` (Impact: 303.2 | O(N^5) | DB: 1)
  * `_async_log_running_tasks` (Impact: 266.7 | O(N^6) | DB: 15)
  * `__repr__` (Impact: 189.3 | O(N^5) | DB: 7)
  * `_async_remove` (Impact: 140.4 | O(N^6) | DB: 3)
  * `_as_dict` (Impact: 35.8 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 433`, `args: 153`, `func_start: 153`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 179`, `state_mutation: 184`, `dead_code: 4`, `duplicate_logic: 10`
* *Architecture:* `api: 136`, `concurrency: 161`, `import: 46`
* *Defense:* `safety: 45`, `doc: 346`, `test: 1`, `sync_locks: 18`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 153.06
  * `Choke Point (Betweenness):` 0.000821 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` .exceptions, it, .util.read_only_dict, .const, .helpers.signal, .helpers.typing, .auth, voluptuous...
  * `Imported By (In-Degree: 11843):` (Excluded from Brief to save tokens)

### `homeassistant/components/xiaomi_miio/light.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.515 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.674 IQR)
- **Top Global Matches:** file_cluster_4: 12.515, file_cluster_13: 12.554, file_cluster_8: 12.663
- **Magnitude:** 1752.26 | **LOC:** 1148 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 70
- **Risk Profile:** Cognitive Load (48.9171%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_try_command` (Impact: 1249.0 | O(2^N) | DB: 70)
  * `async_service_handler` (Impact: 68.5 | O(N^5) | DB: 2)
  * `async_turn_on` (Impact: 13.9 | O(N^4))
  * `brightness` (Impact: 5.4 | O(2^N))
  * `_current_mireds` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 207`, `args: 61`, `func_start: 61`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 181`
* *Architecture:* `api: 52`, `concurrency: 148`, `import: 22`
* *Defense:* `safety: 20`, `doc: 142`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` homeassistant.helpers.device_registry, miio, .typing, .entity, .const, homeassistant.const, homeassistant.core, homeassistant.util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/components/recorder/core.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.73 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.049 IQR)
- **Top Global Matches:** file_cluster_13: 12.73, file_cluster_16: 12.834, file_cluster_0: 12.954
- **Magnitude:** 1749.2 | **LOC:** 1501 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (43.0746%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_commit_event_session_or_retry` (Impact: 610.1 | O(2^N) | DB: 22)
  * `_lock_database` (Impact: 269.9 | O(N^6) | DB: 18)
  * `_run` (Impact: 214.3 | O(N^5) | DB: 16)
  * `_async_check_queue` (Impact: 133.1 | O(N^4) | DB: 12)
  * `async_initialize` (Impact: 56.8 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 255`, `args: 81`, `func_start: 81`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 221`, `dead_code: 1`
* *Architecture:* `io: 6`, `api: 29`, `concurrency: 95`, `import: 45`
* *Defense:* `safety: 44`, `doc: 158`, `test: 9`, `sync_locks: 22`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` sqlalchemy.engine, .table_managers.states, queue, homeassistant.helpers.start, it, contextlib, .const, homeassistant.const...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `homeassistant/components/esphome/manager.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.089 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.554 IQR)
- **Top Global Matches:** file_cluster_8: 11.089, file_cluster_13: 11.149, file_cluster_4: 11.312
- **Magnitude:** 1702.72 | **LOC:** 1413 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (23.8391%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `on_connect_error` (Impact: 924.7 | O(2^N) | DB: 12)
  * `_async_on_log` (Impact: 365.8 | O(2^N) | DB: 6)
  * `async_on_service_call` (Impact: 167.4 | O(N^6) | DB: 1)
  * `on_connect` (Impact: 20.7 | O(N^4))
  * `cleanup_instance` (Impact: 7.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 186`, `args: 33`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 81`, `dead_code: 3`
* *Architecture:* `api: 17`, `concurrency: 78`, `import: 29`
* *Defense:* `safety: 33`, `doc: 70`, `test: 10`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` homeassistant.helpers.device_registry, .encryption_key_storage, homeassistant.helpers.template, homeassistant.helpers.service, __future__, .domain_data, awesomeversion, aioesphomeapi...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/helpers/test_event.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.98 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.186 IQR)
- **Top Global Matches:** file_cluster_4: 12.98, file_cluster_8: 13.122, file_cluster_0: 13.13
- **Magnitude:** 1699.36 | **LOC:** 5000 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 70
- **Risk Profile:** Cognitive Load (43.3493%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_track_template_rate_limit_super_3` (Impact: 450.5 | O(N^4) | DB: 70)
  * `test_track_template` (Impact: 10.9 | O(N^2) | DB: 4)
  * `test_async_track_state_change_filtered` (Impact: 10.1 | O(N^2) | DB: 2)
  * `test_async_track_state_change_event` (Impact: 8.0 | O(N^2) | DB: 2)
  * `test_track_state_change_from_to_state_ma` (Impact: 7.5 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 1343`, `args: 225`, `func_start: 191`
* *Risk/State:* `safety_bypasses: 159`, `state_mutation: 270`, `duplicate_logic: 2`, `orphaned_logic: 17`
* *Architecture:* `io: 4`, `api: 187`, `concurrency: 625`, `import: 22`
* *Defense:* `safety: 728`, `doc: 190`, `test: 843`, `sync_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` homeassistant.helpers.device_registry, homeassistant.helpers.entity_registry, tests.common, contextlib, homeassistant.const, homeassistant.core, homeassistant.util, homeassistant.setup...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/helpers/template/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.769 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.533 IQR)
- **Top Global Matches:** file_cluster_13: 12.769, file_cluster_16: 12.88, file_cluster_0: 13.068
- **Magnitude:** 1691.3 | **LOC:** 2182 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (26.1512%), Tech Debt (28.401%)
**Top Internal Functions/Classes:**
  * `distance` (Impact: 1104.9 | O(2^N) | DB: 10)
  * `_env` (Impact: 31.3 | O(N^4) | DB: 1)
  * `_cached_parse_result` (Impact: 29.4 | O(N^3))
  * `is_safe_attribute` (Impact: 27.4 | O(2^N))
  * `ensure_valid` (Impact: 26.8 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 497`, `args: 147`, `func_start: 146`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 74`, `state_mutation: 155`, `dead_code: 2`, `duplicate_logic: 9`
* *Architecture:* `io: 3`, `api: 98`, `concurrency: 13`, `import: 54`
* *Defense:* `safety: 83`, `doc: 262`, `test: 8`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` copy, json, homeassistant.helpers.entity, awesomeversion, homeassistant.util.async_, jinja2.runtime, homeassistant.util.hass_dict, .render_info...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/components/template/test_config_flow.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.504 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.784 IQR)
- **Top Global Matches:** file_cluster_8: 9.504, file_cluster_7: 10.267, file_cluster_16: 10.345
- **Magnitude:** 1660.93 | **LOC:** 1998 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.058%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 353`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 6`
* *Architecture:* `io: 5`, `api: 14`, `concurrency: 135`, `import: 13`
* *Defense:* `safety: 147`, `doc: 30`, `test: 182`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` pytest, tests.typing, homeassistant, homeassistant.helpers, homeassistant.data_entry_flow, typing, homeassistant.config_entries, tests.common...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/components/shelly/config_flow.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.208 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.579 IQR)
- **Top Global Matches:** file_cluster_4: 12.208, file_cluster_13: 12.418, file_cluster_16: 12.539
- **Magnitude:** 1610.62 | **LOC:** 1342 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (49.237%), Tech Debt (9.1358%)
**Top Internal Functions/Classes:**
  * `_async_secure_device_after_provision` (Impact: 878.8 | O(2^N) | DB: 17)
  * `_async_ensure_ble_connected` (Impact: 142.9 | O(2^N) | DB: 4)
  * `_abort_idle_ble_flows` (Impact: 106.5 | O(2^N) | DB: 1)
  * `_async_get_in_progress_discovery_macs` (Impact: 17.8 | O(N^3) | DB: 1)
  * `_get_name_from_mac_and_ble_model` (Impact: 1.6 | O(N^2))
    * *Intent:* """Generate device name from MAC and BLE manufacturer data model ID. For devices without a Shelly na...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 283`, `args: 38`, `func_start: 37`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 131`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 26`, `concurrency: 269`, `import: 32`
* *Defense:* `safety: 75`, `doc: 84`, `test: 7`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` homeassistant.helpers.device_registry, aioshelly.zeroconf, collections.abc, .ble_provisioning, homeassistant.helpers.service_info.zeroconf, contextlib, homeassistant.helpers.aiohttp_client, .const...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/helpers/test_condition.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.591 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.289 IQR)
- **Top Global Matches:** file_cluster_8: 11.591, file_cluster_16: 11.97, file_cluster_7: 11.971
- **Magnitude:** 1585.58 | **LOC:** 3942 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (16.0519%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_numeric_state_raises` (Impact: 61.5 | O(N^2))
  * `test_time_using_input_datetime` (Impact: 56.3 | O(N^4))
  * `test_and_condition_raises` (Impact: 34.9 | O(N^6))
  * `test_or_condition_raises` (Impact: 34.9 | O(N^6))
  * `test_time_using_sensor` (Impact: 34.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 759`, `args: 117`, `func_start: 114`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 4`, `duplicate_logic: 17`, `orphaned_logic: 72`
* *Architecture:* `io: 3`, `api: 111`, `concurrency: 358`, `import: 30`
* *Defense:* `safety: 284`, `doc: 214`, `test: 492`, `sync_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` homeassistant.helpers.automation, tests.typing, homeassistant.helpers.template, homeassistant.components.device_automation, homeassistant.loader, tests.common, contextlib, homeassistant.const...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/components/yamaha_musiccast/media_player.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.026 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.833 IQR)
- **Top Global Matches:** file_cluster_4: 12.026, file_cluster_13: 12.126, file_cluster_16: 12.128
- **Magnitude:** 1560.02 | **LOC:** 932 | **CtrlFlow:** 42.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (45.2148%), Tech Debt (8.6989%)
**Top Internal Functions/Classes:**
  * `async_browse_media` (Impact: 171.6 | O(2^N) | DB: 3)
  * `async_unjoin_player` (Impact: 136.8 | O(N^5) | DB: 3)
  * `async_server_close_group` (Impact: 101.9 | O(2^N))
  * `async_join_players` (Impact: 88.2 | O(N^6) | DB: 1)
  * `supported_features` (Impact: 70.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 226`, `args: 72`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 65`, `planned_debt: 1`
* *Architecture:* `api: 96`, `concurrency: 133`, `import: 17`
* *Defense:* `safety: 4`, `doc: 138`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` homeassistant.util, homeassistant.components.media_player, homeassistant.helpers.entity_platform, .entity, logging, .const, homeassistant.helpers.entity, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/components/sensor/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.373 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.269 IQR)
- **Top Global Matches:** file_cluster_13: 12.373, file_cluster_0: 12.46, file_cluster_16: 12.539
- **Magnitude:** 1548.98 | **LOC:** 1031 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (36.2646%), Tech Debt (14.9271%)
**Top Internal Functions/Classes:**
  * `state` (Impact: 664.4 | O(2^N) | DB: 7)
  * `unit_of_measurement` (Impact: 116.4 | O(2^N) | DB: 3)
  * `_get_adjusted_display_precision` (Impact: 75.5 | O(N^6))
  * `state_attributes` (Impact: 42.4 | O(N^5) | DB: 1)
  * `from_dict` (Impact: 31.4 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 237`, `args: 38`, `func_start: 38`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 116`, `duplicate_logic: 2`
* *Architecture:* `api: 38`, `concurrency: 32`, `import: 26`
* *Defense:* `safety: 45`, `doc: 86`, `test: 5`, `sync_locks: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` .websocket_api, __future__, homeassistant.helpers.entity, contextlib, .const, homeassistant.util.hass_dict, homeassistant.const, homeassistant.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `homeassistant/components/reolink/host.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.104 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.182 IQR)
- **Top Global Matches:** file_cluster_4: 12.104, file_cluster_13: 12.276, file_cluster_8: 12.352
- **Magnitude:** 1517.32 | **LOC:** 921 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (49.4287%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `async_init` (Impact: 389.4 | O(N^6) | DB: 14)
  * `_async_stop_long_polling` (Impact: 293.1 | O(2^N) | DB: 8)
  * `_async_check_onvif` (Impact: 171.6 | O(N^6) | DB: 5)
  * `_async_long_polling` (Impact: 118.1 | O(N^5) | DB: 8)
  * `_renew` (Impact: 44.5 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 167`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 123`
* *Architecture:* `io: 4`, `api: 21`, `concurrency: 215`, `import: 27`
* *Defense:* `safety: 42`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` homeassistant.helpers.device_registry, .exceptions, homeassistant.util.ssl, homeassistant.helpers.dispatcher, reolink_aio.api, homeassistant.helpers.aiohttp_client, .const, homeassistant.const...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `homeassistant/components/sonos/speaker.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.939 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.117 IQR)
- **Top Global Matches:** file_cluster_4: 12.939, file_cluster_13: 13.006, file_cluster_16: 13.037
- **Magnitude:** 1466.42 | **LOC:** 1296 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (49.2935%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `async_update_groups` (Impact: 318.2 | O(N^6) | DB: 24)
  * `setup` (Impact: 127.1 | O(N^5) | DB: 15)
  * `async_update_volume` (Impact: 93.7 | O(N^6) | DB: 5)
  * `async_update_battery_info` (Impact: 75.4 | O(N^5) | DB: 5)
  * `async_subscribe` (Impact: 74.2 | O(N^5) | DB: 2)
    * *Intent:* """Create event subscriptions."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 218`, `args: 64`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 213`
* *Architecture:* `api: 53`, `concurrency: 192`, `import: 33`
* *Defense:* `safety: 32`, `doc: 132`, `test: 5`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` homeassistant.helpers.dispatcher, soco.snapshot, contextlib, homeassistant.helpers.aiohttp_client, .const, homeassistant.core, defusedxml.ElementTree, .alarms...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/components/google_photos/test_media_source.py` (PYTHON) | Magnitude: 84.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 72, test: 59, safety: 30
- `homeassistant/components/cloud/http_api.py` (PYTHON) | Magnitude: 644.48 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 766, structural_boundaries: 233, concurrency: 115, branch: 101
- `tests/components/teslemetry/test_calendar.py` (PYTHON) | Magnitude: 86.5 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 235, structural_boundaries: 91, test: 69, doc: 32
- `tests/components/renault/test_button.py` (PYTHON) | Magnitude: 74.42 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 122, structural_boundaries: 84, test: 51, concurrency: 43
- `tests/components/roborock/test_button.py` (PYTHON) | Magnitude: 56.52 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 191, test: 71, structural_boundaries: 68, doc: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `homeassistant/components/sonarr/helpers.py` (PYTHON) | Magnitude: 769.86 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 250, safety: 73, reflection_metaprogramming: 70, state_mutation: 57
- `rootfs/etc/services.d/home-assistant/finish` (SHELL) | Magnitude: 25.18 | Delta: **0.191 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 13, reflection_metaprogramming: 11, branch: 8, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `homeassistant/components/assist_pipeline/error.py` (PYTHON) | Magnitude: 46.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 34, structural_boundaries: 24, indent_spaces: 22, class_start: 11
- `homeassistant/components/google_tasks/todo.py` (PYTHON) | Magnitude: 105.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 42, concurrency: 28, doc: 24
- `homeassistant/components/modern_forms/switch.py` (PYTHON) | Magnitude: 46.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 35, doc: 28, encapsulation: 12
- `homeassistant/components/habitica/sensor.py` (PYTHON) | Magnitude: 245.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 419, structural_boundaries: 64, branch: 61, args: 48
- `homeassistant/components/opower/diagnostics.py` (PYTHON) | Magnitude: 8.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 16, branch: 10, import: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `homeassistant/components/alexa/state_report.py` (PYTHON) | Magnitude: 437.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 345, structural_boundaries: 120, branch: 50, generics: 49
- `homeassistant/components/arve/__init__.py` (PYTHON) | Magnitude: 27.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 19, indent_spaces: 15, doc: 8, concurrency: 6
- `homeassistant/components/moehlenhoff_alpha2/climate.py` (PYTHON) | Magnitude: 117.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 47, doc: 30, api: 21
- `homeassistant/components/proxmoxve/entity.py` (PYTHON) | Magnitude: 139.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 152, encapsulation: 48, structural_boundaries: 43, doc: 36
- `homeassistant/components/recorder/table_managers/states.py` (PYTHON) | Magnitude: 109.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 33, doc: 28, api: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `homeassistant/components/wyoming/data.py` (PYTHON) | Magnitude: 237.24 | Delta: **0.145 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 75, branch: 53, structural_boundaries: 37, state_mutation: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/helpers/template/extensions/test_crypto.py` (PYTHON) | Magnitude: 13.58 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 18, test: 12, indent_spaces: 12, doc: 10
- `tests/helpers/template/test_init.py` (PYTHON) | Magnitude: 1132.52 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 2218, structural_boundaries: 647, test: 622, safety: 412
- `tests/helpers/template/extensions/test_collection.py` (PYTHON) | Magnitude: 99.76 | Delta: **0.181 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 158, test: 65, structural_boundaries: 64, ui_framework: 41
- `tests/helpers/template/extensions/test_string.py` (PYTHON) | Magnitude: 48.52 | Delta: **0.22 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 29, test: 23, safety: 16
- `tests/helpers/template/extensions/test_regex.py` (PYTHON) | Magnitude: 47.58 | Delta: **0.237 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 76, indent_spaces: 76, structural_boundaries: 44, test: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/components/litterrobot/test_init.py` (PYTHON) | Magnitude: 100.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 183, structural_boundaries: 102, concurrency: 58, test: 51
- `homeassistant/components/airpatrol/coordinator.py` (PYTHON) | Magnitude: 151.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 47, concurrency: 33, doc: 14
- `homeassistant/components/minecraft_server/api.py` (PYTHON) | Magnitude: 159.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 45, encapsulation: 38, doc: 30
- `tests/components/imeon_inverter/test_config_flow.py` (PYTHON) | Magnitude: 76.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 115, structural_boundaries: 86, concurrency: 40, test: 39
- `homeassistant/components/powerfox/__init__.py` (PYTHON) | Magnitude: 59.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 33, concurrency: 26, import: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `homeassistant/components/cert_expiry/errors.py` (PYTHON) | Magnitude: 21.16 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 16, structural_boundaries: 9, class_start: 7, api: 7
- `tests/components/insteon/mock_connection.py` (PYTHON) | Magnitude: 9.88 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, api: 4, structural_boundaries: 3, args: 2
- `script/scaffold/error.py` (PYTHON) | Magnitude: 7.28 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, indent_spaces: 3, structural_boundaries: 2, api: 2
- `homeassistant/components/madvr/errors.py` (PYTHON) | Magnitude: 11.52 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 1, class_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `homeassistant/bootstrap.py` (PYTHON) | Magnitude: 623.1 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 643, structural_boundaries: 179, branch: 97, encapsulation: 89
- `homeassistant/components/omnilogic/entity.py` (PYTHON) | Magnitude: 10.84 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 10, encapsulation: 9, state_mutation: 7
- `homeassistant/components/opensky/coordinator.py` (PYTHON) | Magnitude: 82.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 29, encapsulation: 19, branch: 15
- `homeassistant/components/switch_as_x/light.py` (PYTHON) | Magnitude: 5.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 20, import: 8, doc: 6
- `homeassistant/components/upnp/__init__.py` (PYTHON) | Magnitude: 110.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 129, structural_boundaries: 51, concurrency: 17, branch: 16

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `homeassistant/components/automation/__init__.py` -> Churn: **100.0%** | Cog Load: 34.3622% | Debt: 99.802%
- `homeassistant/components/huum/quality_scale.yaml` -> Churn: **63.44%** | Cog Load: 32.7765% | Debt: 94.1678%
- `homeassistant/components/unifi_access/quality_scale.yaml` -> Churn: **59.31%** | Cog Load: 33.352% | Debt: 99.825%
- `homeassistant/helpers/selector.py` -> Churn: **57.41%** | Cog Load: 12.4247% | Debt: 99.9928%
- `homeassistant/components/growatt_server/quality_scale.yaml` -> Churn: **56.95%** | Cog Load: 34.6069% | Debt: 99.9996%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `homeassistant/components/google_assistant/trait.py` -> **Kyle Johnson** (100.0% isolated ownership) | Magnitude: 4180.58
- `homeassistant/helpers/config_validation.py` -> **balloob-travel** (100.0% isolated ownership) | Magnitude: 2365.7
- `homeassistant/loader.py` -> **Franck Nijhof** (100.0% isolated ownership) | Magnitude: 2125.58
- `homeassistant/components/homekit/type_thermostats.py` -> **Jon Culver** (100.0% isolated ownership) | Magnitude: 1920.78
- `homeassistant/helpers/device_registry.py` -> **Artur Pragacz** (100.0% isolated ownership) | Magnitude: 1796.66

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `homeassistant/core.py` -> **Severity: 0.07** (Bridge: 0.0008 * Flux: 84.9254%)
- `homeassistant/core_config.py` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 94.2849%)
- `homeassistant/config_entries.py` -> **Severity: 0.021** (Bridge: 0.0003 * Flux: 72.4526%)
- `homeassistant/helpers/entity.py` -> **Severity: 0.02** (Bridge: 0.0002 * Flux: 100.0%)
- `homeassistant/helpers/entity_platform.py` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 95.9438%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `homeassistant/core.py` -> **Severity: 10047.333** (Blast Radius: 153.06 * Doc Risk: 65.6431%)
- `homeassistant/util/logging.py` -> **Severity: 7109.235** (Blast Radius: 89.021 * Doc Risk: 79.8602%)
- `homeassistant/util/enum.py` -> **Severity: 3380.112** (Blast Radius: 44.211 * Doc Risk: 76.4541%)
- `homeassistant/exceptions.py` -> **Severity: 2455.6** (Blast Radius: 24.556 * Doc Risk: 100.0%)
- `homeassistant/util/async_.py` -> **Severity: 2030.303** (Blast Radius: 20.319 * Doc Risk: 99.9214%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
