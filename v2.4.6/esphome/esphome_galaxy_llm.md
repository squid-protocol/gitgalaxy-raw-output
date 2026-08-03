# ARCHITECTURAL_BRIEF: esphome
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/esphome` |
| **Timestamp** | `2026-08-03T19:38:49.875492+00:00` |
| **Scan Duration** | `15.23s` |
| **Git Branch** | `dev` |
| **Git Commit** | `710186998baa241b360f30ad08e90218eaea8a3a` |
| **Git Remote** | `https://github.com/esphome/esphome.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4401 malicious artifacts.

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
| Total Artifacts | 7498 |
| Analyzed Artifacts (Scanned) | 5438 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2060 |
| Total LOC | 421206 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 72.5% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2109 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 207 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 2532 | 224213 | 46.6% |
| PYTHON | 1841 | 164044 | 33.9% |
| YAML | 1014 | 29606 | 18.6% |
| PLAINTEXT | 13 | 1 | 0.2% |
| SHELL | 12 | 221 | 0.2% |
| MARKDOWN | 8 | 0 | 0.1% |
| JAVASCRIPT | 7 | 699 | 0.1% |
| C | 4 | 188 | 0.1% |
| PROTO | 2 | 2151 | 0.0% |
| DOCKERFILE | 1 | 60 | 0.0% |
| BATCH | 1 | 16 | 0.0% |
| XML | 1 | 0 | 0.0% |
| CSV | 1 | 6 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.154`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 3667 | 67.4% |
| file_cluster_13 | 1484 | 27.3% |
| file_cluster_4 | 204 | 3.8% |
| file_cluster_16 | 40 | 0.7% |
| file_cluster_0 | 8 | 0.1% |
| file_cluster_17 | 4 | 0.1% |
| file_cluster_12 | 3 | 0.1% |
| file_cluster_7 | 3 | 0.1% |
| Unknown | 2 | 0.0% |
| file_cluster_11 | 2 | 0.0% |
| file_cluster_15 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 20 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2060*

**Composition by Extension & Reason:**
- `.yaml`: 1852x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1331 LOC)
- `no_extension`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 604 LOC)
- `.py`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 68 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1464 LOC)
- `.yml`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpp`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3900 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2684 LOC)
- `.h`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3291 LOC), 1x Excluded (Machine-Generated Source Code Signature: 13 LOC)
- `.script`: 8x Excluded (Unsupported Extension: '.script'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 691 LOC), 1x Excluded (Machine-Generated Source Code Signature: 249 LOC)
- `.ttf`: 6x Excluded (Explicitly Denied Extension: '.ttf')
- `.conf`: 5x Excluded (Unsupported Extension: '.conf')
- `.j2`: 5x Excluded (Unsupported Extension: '.j2')
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.gtpl`: 2x Excluded (Unsupported Extension: '.gtpl')
- `.wav`: 2x Excluded (Explicitly Denied Extension: '.wav')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 28.6 | 13.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 17.6 | 7.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 31.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 13.8 | 2.3 | 0.0 |
| API Exposure | 0.0 | 15.0 | 2.6 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 21.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 48.7 | 41.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 66.2 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 85.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.9 | 1.1 | 0.3 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 9.8 | 4.5 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 49.0 | 46.2 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 20.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/unit_tests/test_helpers.py` (Hits: 67)
- `script/ci_memory_impact_comment.py` (Hits: 31)
- `script/helpers.py` (Hits: 27)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **config_validation.py** (`esphome/config_validation.py`) — 1058 inbound connections
2. **const.py** (`esphome/const.py`) — 1023 inbound connections
3. **log.h** (`esphome/core/log.h`) — 1011 inbound connections
4. **helpers.h** (`esphome/core/helpers.h`) — 538 inbound connections
5. **hal.h** (`esphome/core/hal.h`) — 363 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **web_server.py** (`esphome/dashboard/web_server.py`) — 61 outbound dependencies
2. **application.h** (`esphome/core/application.h`) — 50 outbound dependencies
3. **__main__.py** (`esphome/__main__.py`) — 44 outbound dependencies
4. **__init__.py** (`esphome/components/lvgl/__init__.py`) — 34 outbound dependencies
5. **config.py** (`esphome/config.py`) — 31 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `date_time` (@ `esphome/config_validation.py`) -> Impact: **1535.9** | LOC: 1308
- `_write_exclude_components` (@ `esphome/components/esp32/__init__.py`) -> Impact: **1392.0** | LOC: 719
  * *Intent:* # User specified their own value - respect it but warn if insufficient if user_max_sockets is not None: _LOGGER.info( "Using user-provided CONFIG_LWIP...
- `ThermostatClimate::setup` (@ `esphome/components/thermostat/thermostat_climate.cpp`) -> Impact: **1147.9** | LOC: 770
- `_validate` (@ `esphome/components/ethernet/__init__.py`) -> Impact: **1066.1** | LOC: 468
- `BLEClientBase::loop` (@ `esphome/components/esp32_ble_client/ble_client_base.cpp`) -> Impact: **1063.7** | LOC: 456
- `Nextion::process_nextion_commands_` (@ `esphome/components/nextion/nextion.cpp`) -> Impact: **1010.2** | LOC: 465
  * *Intent:* // nextion.tech/instruction-set/
- `convert` (@ `script/build_language_schema.py`) -> Impact: **906.0** | LOC: 200
- `ESP32BLETracker::loop` (@ `esphome/components/esp32_ble_tracker/esp32_ble_tracker.cpp`) -> Impact: **891.3** | LOC: 466
  * *Intent:* #endif
- `format_change` (@ `script/ci_memory_impact_comment.py`) -> Impact: **881.3** | LOC: 346
- `HonClimate::get_alarm_status_answer_hand` (@ `esphome/components/haier/hon_climate.cpp`) -> Impact: **868.4** | LOC: 539

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `_resolve_with_cache` (@ `esphome/__main__.py`) -> **O(2^N) [Recursive]**
- `validate_format` (@ `esphome/components/display_menu_base/__init__.py`) -> **O(2^N) [Recursive]**
- `ota_esphome_final_validate` (@ `esphome/components/esphome/ota/__init__.py`) -> **O(2^N) [Recursive]**
- `_validate` (@ `esphome/components/ethernet/__init__.py`) -> **O(2^N) [Recursive]**
- `pixels_or_percent_validator` (@ `esphome/components/lvgl/lv_validation.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """A length in one axis - either a number (pixels) or a percentage"""
- `create_to_code` (@ `esphome/components/lvgl/widgets/meter.py`) -> **O(2^N) [Recursive]**
- `_validate` (@ `esphome/components/mlx90393/sensor.py`) -> **O(2^N) [Recursive]**
- `_extract_tz_string` (@ `esphome/components/time/__init__.py`) -> **O(2^N) [Recursive]**
- `resolve_extend_remove` (@ `esphome/config.py`) -> **O(2^N) [Recursive]**
- `_get_variable_with_full_id_generator` (@ `esphome/core/__init__.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Fast path, check if already registered without awaiting

### Highest Data Gravity (Database Complexity)
- `ATM90E32Component::log_calibration_statu` (@ `esphome/components/atm90e32/atm90e32.cpp`) -> DB Complexity: **460**
- `ThermostatClimate::setup` (@ `esphome/components/thermostat/thermostat_climate.cpp`) -> DB Complexity: **197**
- `HonClimate::get_alarm_status_answer_hand` (@ `esphome/components/haier/hon_climate.cpp`) -> DB Complexity: **191**
- `MCP2515::set_bitrate_` (@ `esphome/components/mcp2515/mcp2515.cpp`) -> DB Complexity: **163**
- `VL53L0XSensor::setup` (@ `esphome/components/vl53l0x/vl53l0x_sensor.cpp`) -> DB Complexity: **154**
- `ATM90E32Component::clear_power_offset_ca` (@ `esphome/components/atm90e32/atm90e32.cpp`) -> DB Complexity: **146**
- `ATM90E32Component::clear_offset_calibrat` (@ `esphome/components/atm90e32/atm90e32.cpp`) -> DB Complexity: **134**
- `APIConnection::loop` (@ `esphome/components/api/api_connection.cpp`) -> DB Complexity: **132**
- `ATM90E32Component::clear_gain_calibratio` (@ `esphome/components/atm90e32/atm90e32.cpp`) -> DB Complexity: **132**
- `WaveshareEPaperTypeA::display` (@ `esphome/components/waveshare_epaper/waveshare_epaper.cpp`) -> DB Complexity: **127**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `esphome` | 36 | 15002.9 | 20.49% | 27.41% |
| `script` | 34 | 11478.07 | 17.32% | 15.38% |
| `esphome/core` | 56 | 10477.23 | 37.86% | 40.29% |
| `esphome/components/remote_base` | 73 | 10273.42 | 59.7% | 50.07% |
| `tests/integration` | 101 | 9591.18 | 17.03% | 0.0% |
| `esphome/components/mqtt` | 53 | 5756.42 | 38.42% | 53.13% |
| `tests/components/http_request` | 3 | 5018.98 | 0.88% | 0.0% |
| `esphome/components/api` | 30 | 4909.24 | 39.18% | 29.31% |
| `esphome/components/light` | 34 | 4891.52 | 45.06% | 51.77% |
| `esphome/components/wifi` | 9 | 4832.4 | 57.56% | 62.06% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `docker/docker_entrypoint.sh` -> **100.0%** Exposure
- `docker/ha-addon-rootfs/etc/s6-overlay/s6-rc.d/discovery/run` -> **100.0%** Exposure
- `docker/ha-addon-rootfs/etc/s6-overlay/s6-rc.d/esphome/run` -> **100.0%** Exposure
- `docker/ha-addon-rootfs/etc/s6-overlay/s6-rc.d/nginx/run` -> **100.0%** Exposure
- `script/devcontainer-post-create` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `docker/ha-addon-rootfs/etc/cont-init.d/30-esphome-fork.sh` -> **100.0%** Exposure
- `esphome/components/a4988/stepper.py` -> **100.0%** Exposure
- `esphome/components/addressable_light/display.py` -> **100.0%** Exposure
- `esphome/components/ade7880/sensor.py` -> **100.0%** Exposure
- `esphome/components/aht10/sensor.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `esphome/components/sprinkler/sprinkler.cpp` -> **98** Orphaned Functions | **6** Duplicates
- `tests/unit_tests/test_main.py` -> **55** Orphaned Functions | **27** Duplicates
- `esphome/components/bytebuffer/bytebuffer.h` -> **0** Orphaned Functions | **74** Duplicates
- `esphome/components/vbus/sensor/vbus_sensor.h` -> **0** Orphaned Functions | **74** Duplicates
- `tests/components/time/posix_tz_parser.cpp` -> **3** Orphaned Functions | **70** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`esphome/components/bthome_mithermometer/bthome_ble.cpp`** -> AI Confidence: **99.48%**
2. **`esphome/components/dlms_meter/dlms_meter.cpp`** -> AI Confidence: **99.48%**
3. **`esphome/components/haier/hon_climate.cpp`** -> AI Confidence: **99.48%**
4. **`esphome/components/mdns/mdns_rp2040.cpp`** -> AI Confidence: **99.48%**
5. **`esphome/components/resampler/speaker/resampler_speaker.cpp`** -> AI Confidence: **99.48%**
6. **`esphome/components/uart/uart_component_rp2040.cpp`** -> AI Confidence: **99.48%**
7. **`esphome/components/xiaomi_ble/xiaomi_ble.cpp`** -> AI Confidence: **99.48%**
8. **`esphome/core/time_64.cpp`** -> AI Confidence: **99.48%**
9. **`script/test_build_components`** -> AI Confidence: **99.39%**
10. **`script/test_build_components.py`** -> AI Confidence: **99.39%**
11. **`esphome/components/beken_spi_led_strip/led_strip.cpp`** -> AI Confidence: **99.39%**
12. **`esphome/components/esp32_ble_beacon/esp32_ble_beacon.cpp`** -> AI Confidence: **99.39%**
13. **`esphome/components/esp32_ble_tracker/esp32_ble_tracker.cpp`** -> AI Confidence: **99.39%**
14. **`esphome/components/esp32_improv/esp32_improv_component.cpp`** -> AI Confidence: **99.39%**
15. **`esphome/components/http_request/http_request_arduino.cpp`** -> AI Confidence: **99.39%**
16. **`esphome/components/i2s_audio/speaker/i2s_audio_speaker.cpp`** -> AI Confidence: **99.39%**
17. **`esphome/components/improv_serial/improv_serial_component.cpp`** -> AI Confidence: **99.39%**
18. **`esphome/components/logger/logger_esp32.cpp`** -> AI Confidence: **99.39%**
19. **`esphome/components/mixer/speaker/mixer_speaker.cpp`** -> AI Confidence: **99.39%**
20. **`esphome/components/nextion/nextion_upload_arduino.cpp`** -> AI Confidence: **99.39%**
21. **`esphome/components/tuya/tuya.cpp`** -> AI Confidence: **99.39%**
22. **`esphome/components/uart/uart_component_libretiny.cpp`** -> AI Confidence: **99.39%**
23. **`esphome/components/water_heater/water_heater.cpp`** -> AI Confidence: **99.39%**
24. **`esphome/components/wifi/wifi_component.cpp`** -> AI Confidence: **99.39%**
25. **`esphome/components/zigbee/zigbee_number_zephyr.cpp`** -> AI Confidence: **99.39%**
26. **`esphome/components/zigbee/zigbee_switch_zephyr.cpp`** -> AI Confidence: **99.39%**
27. **`esphome/components/zwave_proxy/zwave_proxy.cpp`** -> AI Confidence: **99.39%**
28. **`esphome/core/helpers.cpp`** -> AI Confidence: **99.39%**
29. **`esphome/components/esp32/crash_handler.cpp`** -> AI Confidence: **99.35%**
30. **`esphome/components/esp32_ble/ble.cpp`** -> AI Confidence: **99.35%**
31. **`esphome/components/wifi/wifi_component_esp_idf.cpp`** -> AI Confidence: **99.35%**
32. **`esphome/components/async_tcp/async_tcp.h`** -> AI Confidence: **99.34%**
33. **`esphome/components/daly_bms/daly_bms.cpp`** -> AI Confidence: **99.34%**
34. **`esphome/components/graph/graph.cpp`** -> AI Confidence: **99.34%**
35. **`esphome/components/haier/smartair2_climate.cpp`** -> AI Confidence: **99.34%**
36. **`esphome/components/rd03d/rd03d.cpp`** -> AI Confidence: **99.34%**
37. **`esphome/components/remote_receiver/remote_receiver_rmt.cpp`** -> AI Confidence: **99.34%**
38. **`esphome/components/rp2040/crash_handler.cpp`** -> AI Confidence: **99.34%**
39. **`esphome/components/seeed_mr60fda2/seeed_mr60fda2.cpp`** -> AI Confidence: **99.34%**
40. **`esphome/components/sml/text_sensor/sml_text_sensor.cpp`** -> AI Confidence: **99.34%**
41. **`esphome/components/speaker/media_player/audio_pipeline.cpp`** -> AI Confidence: **99.34%**
42. **`esphome/components/vbus/vbus.cpp`** -> AI Confidence: **99.34%**
43. **`esphome/components/zigbee/zigbee_sensor_zephyr.cpp`** -> AI Confidence: **99.34%**
44. **`script/list-components.py`** -> AI Confidence: **99.32%**
45. **`esphome/components/adc/adc_sensor_esp32.cpp`** -> AI Confidence: **99.32%**
46. **`esphome/components/ads1115/ads1115.cpp`** -> AI Confidence: **99.32%**
47. **`esphome/components/coolix/coolix.cpp`** -> AI Confidence: **99.32%**
48. **`esphome/components/dht/dht.cpp`** -> AI Confidence: **99.32%**
49. **`esphome/components/hlw8032/hlw8032.cpp`** -> AI Confidence: **99.32%**
50. **`esphome/components/hmc5883l/hmc5883l.cpp`** -> AI Confidence: **99.32%**
51. **`esphome/components/image/image.cpp`** -> AI Confidence: **99.32%**
52. **`esphome/components/internal_temperature/internal_temperature_esp32.cpp`** -> AI Confidence: **99.32%**
53. **`esphome/components/lightwaverf/LwRx.cpp`** -> AI Confidence: **99.32%**
54. **`esphome/components/mitsubishi/mitsubishi.cpp`** -> AI Confidence: **99.32%**
55. **`esphome/components/nau7802/nau7802.cpp`** -> AI Confidence: **99.32%**
56. **`esphome/components/noblex/noblex.cpp`** -> AI Confidence: **99.32%**
57. **`esphome/components/pipsolar/pipsolar.cpp`** -> AI Confidence: **99.32%**
58. **`esphome/components/pulse_meter/pulse_meter_sensor.cpp`** -> AI Confidence: **99.32%**
59. **`esphome/components/radon_eye_rd200/radon_eye_rd200.cpp`** -> AI Confidence: **99.32%**
60. **`esphome/components/rdm6300/rdm6300.cpp`** -> AI Confidence: **99.32%**
61. **`esphome/components/remote_base/beo4_protocol.cpp`** -> AI Confidence: **99.32%**
62. **`esphome/components/remote_base/brennenstuhl_protocol.cpp`** -> AI Confidence: **99.32%**
63. **`esphome/components/remote_base/drayton_protocol.cpp`** -> AI Confidence: **99.32%**
64. **`esphome/components/remote_base/gobox_protocol.cpp`** -> AI Confidence: **99.32%**
65. **`esphome/components/vbus/sensor/vbus_sensor.cpp`** -> AI Confidence: **99.32%**
66. **`esphome/components/veml3235/veml3235.cpp`** -> AI Confidence: **99.32%**
67. **`esphome/__main__.py`** -> AI Confidence: **99.31%**
68. **`esphome/analyze_memory/cli.py`** -> AI Confidence: **99.31%**
69. **`esphome/analyze_memory/ram_strings.py`** -> AI Confidence: **99.31%**
70. **`esphome/components/api/__init__.py`** -> AI Confidence: **99.31%**
71. **`esphome/components/audio/__init__.py`** -> AI Confidence: **99.31%**
72. **`esphome/components/climate/__init__.py`** -> AI Confidence: **99.31%**
73. **`esphome/components/dashboard_import/__init__.py`** -> AI Confidence: **99.31%**
74. **`esphome/components/esp32/__init__.py`** -> AI Confidence: **99.31%**
75. **`esphome/components/esp32_touch/__init__.py`** -> AI Confidence: **99.31%**
76. **`esphome/components/esp8266/__init__.py`** -> AI Confidence: **99.31%**
77. **`esphome/components/esp8266/gpio.py`** -> AI Confidence: **99.31%**
78. **`esphome/components/ethernet/__init__.py`** -> AI Confidence: **99.31%**
79. **`esphome/components/external_components/__init__.py`** -> AI Confidence: **99.31%**
80. **`esphome/components/font/__init__.py`** -> AI Confidence: **99.31%**
81. **`esphome/components/http_request/__init__.py`** -> AI Confidence: **99.31%**
82. **`esphome/components/hub75/display.py`** -> AI Confidence: **99.31%**
83. **`esphome/components/i2c/__init__.py`** -> AI Confidence: **99.31%**
84. **`esphome/components/ili9xxx/display.py`** -> AI Confidence: **99.31%**
85. **`esphome/components/libretiny/__init__.py`** -> AI Confidence: **99.31%**
86. **`esphome/components/libretiny/gpio.py`** -> AI Confidence: **99.31%**
87. **`esphome/components/logger/__init__.py`** -> AI Confidence: **99.31%**
88. **`esphome/components/mipi_spi/display.py`** -> AI Confidence: **99.31%**
89. **`esphome/components/neopixelbus/light.py`** -> AI Confidence: **99.31%**
90. **`esphome/components/network/__init__.py`** -> AI Confidence: **99.31%**
91. **`esphome/components/speaker/media_player/__init__.py`** -> AI Confidence: **99.31%**
92. **`esphome/components/spi/__init__.py`** -> AI Confidence: **99.31%**
93. **`esphome/components/sprinkler/__init__.py`** -> AI Confidence: **99.31%**
94. **`esphome/components/substitutions/__init__.py`** -> AI Confidence: **99.31%**
95. **`esphome/components/sx127x/__init__.py`** -> AI Confidence: **99.31%**
96. **`esphome/components/uart/__init__.py`** -> AI Confidence: **99.31%**
97. **`esphome/components/web_server/__init__.py`** -> AI Confidence: **99.31%**
98. **`esphome/components/wifi/__init__.py`** -> AI Confidence: **99.31%**
99. **`esphome/config.py`** -> AI Confidence: **99.31%**
100. **`esphome/config_validation.py`** -> AI Confidence: **99.31%**
101. **`esphome/core/config.py`** -> AI Confidence: **99.31%**
102. **`esphome/espota2.py`** -> AI Confidence: **99.31%**
103. **`esphome/platformio_api.py`** -> AI Confidence: **99.31%**
104. **`esphome/wizard.py`** -> AI Confidence: **99.31%**
105. **`esphome/writer.py`** -> AI Confidence: **99.31%**
106. **`script/analyze_component_buses.py`** -> AI Confidence: **99.31%**
107. **`script/build_language_schema.py`** -> AI Confidence: **99.31%**
108. **`script/ci-custom.py`** -> AI Confidence: **99.31%**
109. **`script/ci_memory_impact_comment.py`** -> AI Confidence: **99.31%**
110. **`script/ci_memory_impact_extract.py`** -> AI Confidence: **99.31%**
111. **`script/clang-tidy`** -> AI Confidence: **99.31%**
112. **`script/clang_tidy_hash.py`** -> AI Confidence: **99.31%**
113. **`script/cpp_benchmark.py`** -> AI Confidence: **99.31%**
114. **`script/determine-jobs.py`** -> AI Confidence: **99.31%**
115. **`script/helpers.py`** -> AI Confidence: **99.31%**
116. **`script/merge_component_configs.py`** -> AI Confidence: **99.31%**
117. **`script/split_components_for_ci.py`** -> AI Confidence: **99.31%**
118. **`tests/integration/test_sensor_filters_value_list.py`** -> AI Confidence: **99.31%**
119. **`tests/integration/test_uart_mock_modbus.py`** -> AI Confidence: **99.31%**
120. **`esphome/components/ac_dimmer/ac_dimmer.cpp`** -> AI Confidence: **99.31%**
121. **`esphome/components/alarm_control_panel/alarm_control_panel.cpp`** -> AI Confidence: **99.31%**
122. **`esphome/components/api/api_connection.cpp`** -> AI Confidence: **99.31%**
123. **`esphome/components/api/api_frame_helper.cpp`** -> AI Confidence: **99.31%**
124. **`esphome/components/api/api_frame_helper_noise.cpp`** -> AI Confidence: **99.31%**
125. **`esphome/components/api/api_frame_helper_plaintext.cpp`** -> AI Confidence: **99.31%**
126. **`esphome/components/api/api_server.cpp`** -> AI Confidence: **99.31%**
127. **`esphome/components/ble_nus/ble_nus.cpp`** -> AI Confidence: **99.31%**
128. **`esphome/components/bluetooth_proxy/bluetooth_proxy.cpp`** -> AI Confidence: **99.31%**
129. **`esphome/components/bme280_base/bme280_base.cpp`** -> AI Confidence: **99.31%**
130. **`esphome/components/bme680_bsec/bme680_bsec.cpp`** -> AI Confidence: **99.31%**
131. **`esphome/components/e131/e131_packet.cpp`** -> AI Confidence: **99.31%**
132. **`esphome/components/esp32/gpio.cpp`** -> AI Confidence: **99.31%**
133. **`esphome/components/esp32/helpers.cpp`** -> AI Confidence: **99.31%**
134. **`esphome/components/esp32/preferences.cpp`** -> AI Confidence: **99.31%**
135. **`esphome/components/esp32_ble_server/ble_server.cpp`** -> AI Confidence: **99.31%**
136. **`esphome/components/esp32_camera_web_server/camera_web_server.cpp`** -> AI Confidence: **99.31%**
137. **`esphome/components/esp32_hosted/update/esp32_hosted_update.cpp`** -> AI Confidence: **99.31%**
138. **`esphome/components/esphome/ota/ota_esphome.cpp`** -> AI Confidence: **99.31%**
139. **`esphome/components/espnow/espnow_component.cpp`** -> AI Confidence: **99.31%**
140. **`esphome/components/http_request/http_request_host.cpp`** -> AI Confidence: **99.31%**
141. **`esphome/components/http_request/http_request_idf.cpp`** -> AI Confidence: **99.31%**
142. **`esphome/components/http_request/ota/ota_http_request.cpp`** -> AI Confidence: **99.31%**
143. **`esphome/components/i2c/i2c_bus_esp_idf.cpp`** -> AI Confidence: **99.31%**
144. **`esphome/components/ld2450/ld2450.cpp`** -> AI Confidence: **99.31%**
145. **`esphome/components/ledc/ledc_output.cpp`** -> AI Confidence: **99.31%**
146. **`esphome/components/light/light_state.cpp`** -> AI Confidence: **99.31%**
147. **`esphome/components/logger/logger_zephyr.cpp`** -> AI Confidence: **99.31%**
148. **`esphome/components/max7219digit/max7219digit.cpp`** -> AI Confidence: **99.31%**
149. **`esphome/components/mdns/mdns_component.cpp`** -> AI Confidence: **99.31%**
150. **`esphome/components/mdns/mdns_esp8266.cpp`** -> AI Confidence: **99.31%**
151. **`esphome/components/micro_wake_word/micro_wake_word.cpp`** -> AI Confidence: **99.31%**
152. **`esphome/components/mipi_rgb/mipi_rgb.cpp`** -> AI Confidence: **99.31%**
153. **`esphome/components/mqtt/mqtt_client.cpp`** -> AI Confidence: **99.31%**
154. **`esphome/components/nextion/nextion_upload_esp32.cpp`** -> AI Confidence: **99.31%**
155. **`esphome/components/openthread/openthread.cpp`** -> AI Confidence: **99.31%**
156. **`esphome/components/openthread/openthread_esp.cpp`** -> AI Confidence: **99.31%**
157. **`esphome/components/ota/ota_backend_esp8266.cpp`** -> AI Confidence: **99.31%**
158. **`esphome/components/rp2040/helpers.cpp`** -> AI Confidence: **99.31%**
159. **`esphome/components/rp2040_pio_led_strip/led_strip.cpp`** -> AI Confidence: **99.31%**
160. **`esphome/components/runtime_image/jpeg_decoder.cpp`** -> AI Confidence: **99.31%**
161. **`esphome/components/runtime_image/runtime_image.cpp`** -> AI Confidence: **99.31%**
162. **`esphome/components/safe_mode/safe_mode.cpp`** -> AI Confidence: **99.31%**
163. **`esphome/components/shelly_dimmer/shelly_dimmer.cpp`** -> AI Confidence: **99.31%**
164. **`esphome/components/shelly_dimmer/stm32flash.cpp`** -> AI Confidence: **99.31%**
165. **`esphome/components/sprinkler/sprinkler.cpp`** -> AI Confidence: **99.31%**
166. **`esphome/components/template/alarm_control_panel/template_alarm_control_panel.cpp`** -> AI Confidence: **99.31%**
167. **`esphome/components/time/real_time_clock.cpp`** -> AI Confidence: **99.31%**
168. **`esphome/components/uart/uart.cpp`** -> AI Confidence: **99.31%**
169. **`esphome/components/uart/uart_component_esp_idf.cpp`** -> AI Confidence: **99.31%**
170. **`esphome/components/uart/uart_component_host.cpp`** -> AI Confidence: **99.31%**
171. **`esphome/components/usb_cdc_acm/usb_cdc_acm_esp32.cpp`** -> AI Confidence: **99.31%**
172. **`esphome/components/web_server/web_server.cpp`** -> AI Confidence: **99.31%**
173. **`esphome/components/web_server_idf/web_server_idf.cpp`** -> AI Confidence: **99.31%**
174. **`esphome/components/wifi/wifi_component_esp8266.cpp`** -> AI Confidence: **99.31%**
175. **`esphome/components/wifi/wifi_component_libretiny.cpp`** -> AI Confidence: **99.31%**
176. **`esphome/components/wifi/wifi_component_pico_w.cpp`** -> AI Confidence: **99.31%**
177. **`esphome/components/wireguard/wireguard.cpp`** -> AI Confidence: **99.31%**
178. **`esphome/components/zigbee/zigbee_binary_sensor_zephyr.cpp`** -> AI Confidence: **99.31%**
179. **`esphome/components/zigbee/zigbee_zephyr.cpp`** -> AI Confidence: **99.31%**
180. **`esphome/core/application.cpp`** -> AI Confidence: **99.31%**
181. **`esphome/core/scheduler.cpp`** -> AI Confidence: **99.31%**
182. **`esphome/components/ethernet/esp_eth_phy_jl1101.c`** -> AI Confidence: **99.31%**
183. **`docker/ha-addon-rootfs/etc/s6-overlay/s6-rc.d/esphome/finish`** -> AI Confidence: **99.29%**
184. **`docker/ha-addon-rootfs/etc/s6-overlay/s6-rc.d/nginx/finish`** -> AI Confidence: **99.29%**
185. **`docker/ha-addon-rootfs/etc/s6-overlay/s6-rc.d/nginx/run`** -> AI Confidence: **99.29%**
186. **`docker/generate_tags.py`** -> AI Confidence: **99.29%**
187. **`esphome/components/esp8266/boards.py`** -> AI Confidence: **99.29%**
188. **`esphome/components/audio_file/media_source/audio_file_media_source.cpp`** -> AI Confidence: **99.29%**
189. **`esphome/components/ballu/ballu.cpp`** -> AI Confidence: **99.29%**
190. **`esphome/components/climate_ir_lg/climate_ir_lg.cpp`** -> AI Confidence: **99.29%**
191. **`esphome/components/cst816/touchscreen/cst816_touchscreen.cpp`** -> AI Confidence: **99.29%**
192. **`esphome/components/daikin/daikin.cpp`** -> AI Confidence: **99.29%**
193. **`esphome/components/daikin_arc/daikin_arc.cpp`** -> AI Confidence: **99.29%**
194. **`esphome/components/daikin_brc/daikin_brc.cpp`** -> AI Confidence: **99.29%**
195. **`esphome/components/delonghi/delonghi.cpp`** -> AI Confidence: **99.29%**
196. **`esphome/components/display_menu_base/display_menu_base.cpp`** -> AI Confidence: **99.29%**
197. **`esphome/components/feedback/feedback_cover.cpp`** -> AI Confidence: **99.29%**
198. **`esphome/components/fingerprint_grow/fingerprint_grow.cpp`** -> AI Confidence: **99.29%**
199. **`esphome/components/fujitsu_general/fujitsu_general.cpp`** -> AI Confidence: **99.29%**
200. **`esphome/components/hydreon_rgxx/hydreon_rgxx.cpp`** -> AI Confidence: **99.29%**
201. **`esphome/components/light/esp_hsv_color.cpp`** -> AI Confidence: **99.29%**
202. **`esphome/components/logger/logger_libretiny.cpp`** -> AI Confidence: **99.29%**
203. **`esphome/components/modbus/modbus_helpers.cpp`** -> AI Confidence: **99.29%**
204. **`esphome/components/pid/pid_climate.cpp`** -> AI Confidence: **99.29%**
205. **`esphome/components/pzem004t/pzem004t.cpp`** -> AI Confidence: **99.29%**
206. **`esphome/components/remote_base/nexa_protocol.cpp`** -> AI Confidence: **99.29%**
207. **`esphome/components/remote_base/pioneer_protocol.cpp`** -> AI Confidence: **99.29%**
208. **`esphome/components/remote_base/rc5_protocol.cpp`** -> AI Confidence: **99.29%**
209. **`esphome/components/remote_base/rc6_protocol.cpp`** -> AI Confidence: **99.29%**
210. **`esphome/components/seeed_mr24hpc1/seeed_mr24hpc1.cpp`** -> AI Confidence: **99.29%**
211. **`esphome/components/sim800l/sim800l.cpp`** -> AI Confidence: **99.29%**
212. **`esphome/components/speaker/media_player/speaker_media_player.cpp`** -> AI Confidence: **99.29%**
213. **`esphome/components/speaker_source/speaker_source_media_player.cpp`** -> AI Confidence: **99.29%**
214. **`esphome/components/tcl112/tcl112.cpp`** -> AI Confidence: **99.29%**
215. **`esphome/components/tuya/climate/tuya_climate.cpp`** -> AI Confidence: **99.29%**
216. **`esphome/components/uptime/text_sensor/uptime_text_sensor.cpp`** -> AI Confidence: **99.29%**
217. **`esphome/components/whirlpool/whirlpool.cpp`** -> AI Confidence: **99.29%**
218. **`esphome/components/whynter/whynter.cpp`** -> AI Confidence: **99.29%**
219. **`esphome/components/zhlt01/zhlt01.cpp`** -> AI Confidence: **99.29%**
220. **`esphome/core/component_iterator.cpp`** -> AI Confidence: **99.29%**
221. **`esphome/components/socket/headers.h`** -> AI Confidence: **99.28%**
222. **`script/build_helpers.py`** -> AI Confidence: **99.25%**
223. **`esphome/components/sha256/sha256.h`** -> AI Confidence: **99.25%**
224. **`esphome/components/adc/sensor.py`** -> AI Confidence: **99.24%**
225. **`esphome/components/deep_sleep/__init__.py`** -> AI Confidence: **99.24%**
226. **`esphome/components/esp32_ble/__init__.py`** -> AI Confidence: **99.24%**
227. **`esphome/components/esp32_ble_server/__init__.py`** -> AI Confidence: **99.24%**
228. **`esphome/components/esp32_camera/__init__.py`** -> AI Confidence: **99.24%**
229. **`esphome/components/image/__init__.py`** -> AI Confidence: **99.24%**
230. **`esphome/components/lvgl/__init__.py`** -> AI Confidence: **99.24%**
231. **`esphome/components/modbus_controller/__init__.py`** -> AI Confidence: **99.24%**
232. **`esphome/components/mqtt/__init__.py`** -> AI Confidence: **99.24%**
233. **`esphome/components/nrf52/__init__.py`** -> AI Confidence: **99.24%**
234. **`esphome/components/remote_receiver/__init__.py`** -> AI Confidence: **99.24%**
235. **`esphome/components/speaker_source/media_player.py`** -> AI Confidence: **99.24%**
236. **`esphome/components/time/__init__.py`** -> AI Confidence: **99.24%**
237. **`esphome/core/entity_helpers.py`** -> AI Confidence: **99.24%**
238. **`esphome/espidf_api.py`** -> AI Confidence: **99.24%**
239. **`esphome/git.py`** -> AI Confidence: **99.24%**
240. **`esphome/mqtt.py`** -> AI Confidence: **99.24%**
241. **`esphome/pins.py`** -> AI Confidence: **99.24%**
242. **`esphome/util.py`** -> AI Confidence: **99.24%**
243. **`tests/integration/test_light_constant_brightness.py`** -> AI Confidence: **99.24%**
244. **`tests/unit_tests/test_git.py`** -> AI Confidence: **99.24%**
245. **`esphome/components/api/homeassistant_service.h`** -> AI Confidence: **99.24%**
246. **`esphome/components/logger/logger.h`** -> AI Confidence: **99.24%**
247. **`esphome/components/remote_base/abbwelcome_protocol.h`** -> AI Confidence: **99.24%**
248. **`esphome/components/socket/lwip_raw_tcp_impl.cpp`** -> AI Confidence: **99.24%**
249. **`esphome/core/component.cpp`** -> AI Confidence: **99.24%**
250. **`esphome/core/log.h`** -> AI Confidence: **99.24%**
251. **`esphome/components/haier/climate.py`** -> AI Confidence: **99.23%**
252. **`esphome/components/nextion/display.py`** -> AI Confidence: **99.23%**
253. **`esphome/components/openthread/__init__.py`** -> AI Confidence: **99.23%**
254. **`esphome/components/psram/__init__.py`** -> AI Confidence: **99.23%**
255. **`esphome/components/rp2040/gpio.py`** -> AI Confidence: **99.23%**
256. **`esphome/components/template/select/__init__.py`** -> AI Confidence: **99.23%**
257. **`esphome/components/thermostat/climate.py`** -> AI Confidence: **99.23%**
258. **`script/generate-esp32-boards.py`** -> AI Confidence: **99.23%**
259. **`tests/component_tests/sntp/test_init.py`** -> AI Confidence: **99.23%**
260. **`tests/integration/test_host_preferences.py`** -> AI Confidence: **99.23%**
261. **`tests/integration/test_uart_mock_ld2420.py`** -> AI Confidence: **99.23%**
262. **`esphome/components/atm90e32/atm90e32.cpp`** -> AI Confidence: **99.23%**
263. **`esphome/components/ble_client/sensor/ble_sensor.cpp`** -> AI Confidence: **99.23%**
264. **`esphome/components/ble_client/text_sensor/ble_text_sensor.cpp`** -> AI Confidence: **99.23%**
265. **`esphome/components/bme68x_bsec2/bme68x_bsec2.cpp`** -> AI Confidence: **99.23%**
266. **`esphome/components/cse7766/cse7766.cpp`** -> AI Confidence: **99.23%**
267. **`esphome/components/deep_sleep/deep_sleep_esp32.cpp`** -> AI Confidence: **99.23%**
268. **`esphome/components/ili9xxx/ili9xxx_display.cpp`** -> AI Confidence: **99.23%**
269. **`esphome/components/improv_base/improv_base.cpp`** -> AI Confidence: **99.23%**
270. **`esphome/components/lightwaverf/LwTx.cpp`** -> AI Confidence: **99.23%**
271. **`esphome/components/lvgl/lvgl_esphome.cpp`** -> AI Confidence: **99.23%**
272. **`esphome/components/mdns/mdns_libretiny.cpp`** -> AI Confidence: **99.23%**
273. **`esphome/components/mqtt/mqtt_backend_esp32.cpp`** -> AI Confidence: **99.23%**
274. **`esphome/components/mqtt/mqtt_component.cpp`** -> AI Confidence: **99.23%**
275. **`esphome/components/remote_transmitter/remote_transmitter_rmt.cpp`** -> AI Confidence: **99.23%**
276. **`esphome/components/runtime_image/bmp_decoder.cpp`** -> AI Confidence: **99.23%**
277. **`esphome/components/seeed_mr60bha2/seeed_mr60bha2.cpp`** -> AI Confidence: **99.23%**
278. **`esphome/components/sensor/filter.cpp`** -> AI Confidence: **99.23%**
279. **`esphome/components/sgp4x/sgp4x.cpp`** -> AI Confidence: **99.23%**
280. **`esphome/components/tcs34725/tcs34725.cpp`** -> AI Confidence: **99.23%**
281. **`esphome/components/uponor_smatrix/climate/uponor_smatrix_climate.cpp`** -> AI Confidence: **99.23%**
282. **`esphome/components/uponor_smatrix/uponor_smatrix.cpp`** -> AI Confidence: **99.23%**
283. **`tests/integration/fixtures/external_components/scheduler_heap_stress_component/heap_scheduler_stress_component.cpp`** -> AI Confidence: **99.23%**
284. **`tests/integration/fixtures/external_components/scheduler_rapid_cancellation_component/rapid_cancellation_component.cpp`** -> AI Confidence: **99.23%**
285. **`tests/integration/fixtures/external_components/scheduler_string_name_stress_component/string_name_stress_component.cpp`** -> AI Confidence: **99.23%**
286. **`esphome/components/esp32_rmt_led_strip/led_strip.cpp`** -> AI Confidence: **99.22%**
287. **`esphome/components/i2s_audio/microphone/i2s_audio_microphone.cpp`** -> AI Confidence: **99.22%**
288. **`esphome/components/inkplate/inkplate.cpp`** -> AI Confidence: **99.22%**
289. **`esphome/components/light/light_call.cpp`** -> AI Confidence: **99.22%**
290. **`esphome/components/nextion/nextion.cpp`** -> AI Confidence: **99.22%**
291. **`esphome/components/sen5x/sen5x.cpp`** -> AI Confidence: **99.22%**
292. **`esphome/components/sgp30/sgp30.cpp`** -> AI Confidence: **99.22%**
293. **`esphome/components/uart/uart_component_esp8266.cpp`** -> AI Confidence: **99.22%**
294. **`esphome/components/voice_assistant/voice_assistant.cpp`** -> AI Confidence: **99.22%**
295. **`esphome/core/defines.h`** -> AI Confidence: **99.22%**
296. **`esphome/core/log_const_en.h`** -> AI Confidence: **99.22%**
297. **`esphome/components/ads1118/ads1118.cpp`** -> AI Confidence: **99.2%**
298. **`esphome/components/am43/sensor/am43_sensor.cpp`** -> AI Confidence: **99.2%**
299. **`esphome/components/audio/audio_decoder.cpp`** -> AI Confidence: **99.2%**
300. **`esphome/components/bh1750/bh1750.cpp`** -> AI Confidence: **99.2%**
301. **`esphome/components/ble_client/output/ble_binary_output.cpp`** -> AI Confidence: **99.2%**
302. **`esphome/components/dfplayer/dfplayer.cpp`** -> AI Confidence: **99.2%**
303. **`esphome/components/hbridge/switch/hbridge_switch.cpp`** -> AI Confidence: **99.2%**
304. **`esphome/components/jsn_sr04t/jsn_sr04t.cpp`** -> AI Confidence: **99.2%**
305. **`esphome/components/ld2420/ld2420.cpp`** -> AI Confidence: **99.2%**
306. **`esphome/components/mcp23x17_base/mcp23x17_base.cpp`** -> AI Confidence: **99.2%**
307. **`esphome/components/mics_4514/mics_4514.cpp`** -> AI Confidence: **99.2%**
308. **`esphome/components/modbus_controller/switch/modbus_switch.cpp`** -> AI Confidence: **99.2%**
309. **`esphome/components/nextion/sensor/nextion_sensor.cpp`** -> AI Confidence: **99.2%**
310. **`esphome/components/pid/sensor/pid_climate_sensor.cpp`** -> AI Confidence: **99.2%**
311. **`esphome/components/pmsx003/pmsx003.cpp`** -> AI Confidence: **99.2%**
312. **`esphome/components/remote_base/keeloq_protocol.cpp`** -> AI Confidence: **99.2%**
313. **`esphome/components/rotary_encoder/rotary_encoder.cpp`** -> AI Confidence: **99.2%**
314. **`esphome/components/sx126x/sx126x.cpp`** -> AI Confidence: **99.2%**
315. **`esphome/components/sx127x/sx127x.cpp`** -> AI Confidence: **99.2%**
316. **`esphome/components/tuya/light/tuya_light.cpp`** -> AI Confidence: **99.2%**
317. **`esphome/components/tuya/text_sensor/tuya_text_sensor.cpp`** -> AI Confidence: **99.2%**
318. **`esphome/components/uart/packet_transport/uart_transport.cpp`** -> AI Confidence: **99.2%**
319. **`esphome/components/uponor_smatrix/sensor/uponor_smatrix_sensor.cpp`** -> AI Confidence: **99.2%**
320. **`esphome/components/vbus/binary_sensor/vbus_binary_sensor.cpp`** -> AI Confidence: **99.2%**
321. **`esphome/components/xiaomi_cgd1/xiaomi_cgd1.cpp`** -> AI Confidence: **99.2%**
322. **`esphome/components/xiaomi_cgdk2/xiaomi_cgdk2.cpp`** -> AI Confidence: **99.2%**
323. **`esphome/components/xiaomi_cgg1/xiaomi_cgg1.cpp`** -> AI Confidence: **99.2%**
324. **`esphome/components/xiaomi_cgpr1/xiaomi_cgpr1.cpp`** -> AI Confidence: **99.2%**
325. **`esphome/components/xiaomi_lywsd02mmc/xiaomi_lywsd02mmc.cpp`** -> AI Confidence: **99.2%**
326. **`esphome/components/xiaomi_lywsd03mmc/xiaomi_lywsd03mmc.cpp`** -> AI Confidence: **99.2%**
327. **`esphome/components/xiaomi_mhoc401/xiaomi_mhoc401.cpp`** -> AI Confidence: **99.2%**
328. **`esphome/components/xiaomi_miscale/xiaomi_miscale.cpp`** -> AI Confidence: **99.2%**
329. **`esphome/components/xiaomi_mjyd02yla/xiaomi_mjyd02yla.cpp`** -> AI Confidence: **99.2%**
330. **`esphome/components/xiaomi_rtcgq02lm/xiaomi_rtcgq02lm.cpp`** -> AI Confidence: **99.2%**
331. **`esphome/components/xiaomi_xmwsdj04mmc/xiaomi_xmwsdj04mmc.cpp`** -> AI Confidence: **99.2%**
332. **`esphome/components/bl0906/sensor.py`** -> AI Confidence: **99.18%**
333. **`esphome/components/ble_client/__init__.py`** -> AI Confidence: **99.18%**
334. **`esphome/components/ble_nus/__init__.py`** -> AI Confidence: **99.18%**
335. **`esphome/components/bluetooth_proxy/__init__.py`** -> AI Confidence: **99.18%**
336. **`esphome/components/captive_portal/__init__.py`** -> AI Confidence: **99.18%**
337. **`esphome/components/datetime/__init__.py`** -> AI Confidence: **99.18%**
338. **`esphome/components/display/__init__.py`** -> AI Confidence: **99.18%**
339. **`esphome/components/display_menu_base/__init__.py`** -> AI Confidence: **99.18%**
340. **`esphome/components/esp32_can/canbus.py`** -> AI Confidence: **99.18%**
341. **`esphome/components/esp32_hosted/__init__.py`** -> AI Confidence: **99.18%**
342. **`esphome/components/factory_reset/__init__.py`** -> AI Confidence: **99.18%**
343. **`esphome/components/lvgl/gradient.py`** -> AI Confidence: **99.18%**
344. **`esphome/components/lvgl/keypads.py`** -> AI Confidence: **99.18%**
345. **`esphome/components/lvgl/styles.py`** -> AI Confidence: **99.18%**
346. **`esphome/components/lvgl/widgets/arc.py`** -> AI Confidence: **99.18%**
347. **`esphome/components/lvgl/widgets/buttonmatrix.py`** -> AI Confidence: **99.18%**
348. **`esphome/components/lvgl/widgets/canvas.py`** -> AI Confidence: **99.18%**
349. **`esphome/components/lvgl/widgets/dropdown.py`** -> AI Confidence: **99.18%**
350. **`esphome/components/lvgl/widgets/lv_bar.py`** -> AI Confidence: **99.18%**
351. **`esphome/components/lvgl/widgets/tileview.py`** -> AI Confidence: **99.18%**
352. **`esphome/components/micronova/__init__.py`** -> AI Confidence: **99.18%**
353. **`esphome/components/mipi_dsi/display.py`** -> AI Confidence: **99.18%**
354. **`esphome/components/modbus_controller/number/__init__.py`** -> AI Confidence: **99.18%**
355. **`esphome/components/modbus_controller/output/__init__.py`** -> AI Confidence: **99.18%**
356. **`esphome/components/modbus_controller/select/__init__.py`** -> AI Confidence: **99.18%**
357. **`esphome/components/nextion/sensor/__init__.py`** -> AI Confidence: **99.18%**
358. **`esphome/components/number/__init__.py`** -> AI Confidence: **99.18%**
359. **`esphome/components/substitutions/jinja.py`** -> AI Confidence: **99.18%**
360. **`esphome/components/switch/__init__.py`** -> AI Confidence: **99.18%**
361. **`esphome/components/template/water_heater/__init__.py`** -> AI Confidence: **99.18%**
362. **`esphome/components/udp/__init__.py`** -> AI Confidence: **99.18%**
363. **`esphome/components/usb_host/__init__.py`** -> AI Confidence: **99.18%**
364. **`esphome/components/usb_uart/__init__.py`** -> AI Confidence: **99.18%**
365. **`esphome/components/valve/__init__.py`** -> AI Confidence: **99.18%**
366. **`esphome/components/web_server/ota/__init__.py`** -> AI Confidence: **99.18%**
367. **`esphome/components/web_server_base/__init__.py`** -> AI Confidence: **99.18%**
368. **`esphome/components/zephyr_mcumgr/ota/__init__.py`** -> AI Confidence: **99.18%**
369. **`esphome/components/zigbee/__init__.py`** -> AI Confidence: **99.18%**
370. **`esphome/components/zigbee/zigbee_zephyr.py`** -> AI Confidence: **99.18%**
371. **`esphome/coroutine.py`** -> AI Confidence: **99.18%**
372. **`esphome/cpp_generator.py`** -> AI Confidence: **99.18%**
373. **`esphome/dashboard/core.py`** -> AI Confidence: **99.18%**
374. **`esphome/dashboard/dashboard.py`** -> AI Confidence: **99.18%**
375. **`esphome/dashboard/entries.py`** -> AI Confidence: **99.18%**
376. **`esphome/dashboard/settings.py`** -> AI Confidence: **99.18%**
377. **`esphome/dashboard/status/mqtt.py`** -> AI Confidence: **99.18%**
378. **`esphome/loader.py`** -> AI Confidence: **99.18%**
379. **`script/generate-rp2040-boards.py`** -> AI Confidence: **99.18%**
380. **`script/sync-device_class.py`** -> AI Confidence: **99.18%**
381. **`tests/component_tests/font/test_font.py`** -> AI Confidence: **99.18%**
382. **`tests/component_tests/light/test_effect_validation.py`** -> AI Confidence: **99.18%**
383. **`tests/component_tests/ota/test_web_server_ota.py`** -> AI Confidence: **99.18%**
384. **`tests/integration/test_api_action_responses.py`** -> AI Confidence: **99.18%**
385. **`tests/integration/test_uart_mock_ld2450.py`** -> AI Confidence: **99.18%**
386. **`tests/script/test_determine_jobs.py`** -> AI Confidence: **99.18%**
387. **`tests/script/test_helpers.py`** -> AI Confidence: **99.18%**
388. **`tests/unit_tests/test_config_validation.py`** -> AI Confidence: **99.18%**
389. **`tests/unit_tests/test_substitutions.py`** -> AI Confidence: **99.18%**
390. **`esphome/components/dlms_meter/dlms_meter.h`** -> AI Confidence: **99.18%**
391. **`esphome/components/esp32_rmt_led_strip/led_strip.h`** -> AI Confidence: **99.18%**
392. **`esphome/components/host/core.cpp`** -> AI Confidence: **99.18%**
393. **`esphome/components/watchdog/watchdog.cpp`** -> AI Confidence: **99.18%**
394. **`.github/scripts/auto-label-pr/detectors.js`** -> AI Confidence: **99.17%**
395. **`docker/docker_entrypoint.sh`** -> AI Confidence: **99.17%**
396. **`script/devcontainer-post-create`** -> AI Confidence: **99.17%**
397. **`esphome/components/absolute_humidity/absolute_humidity.cpp`** -> AI Confidence: **99.17%**
398. **`esphome/components/airthings_wave_plus/airthings_wave_plus.cpp`** -> AI Confidence: **99.17%**
399. **`esphome/components/api/api_frame_helper.h`** -> AI Confidence: **99.17%**
400. **`esphome/components/ble_client/sensor/automation.h`** -> AI Confidence: **99.17%**
401. **`esphome/components/bp1658cj/bp1658cj.cpp`** -> AI Confidence: **99.17%**
402. **`esphome/components/bp5758d/bp5758d.cpp`** -> AI Confidence: **99.17%**
403. **`esphome/components/ccs811/ccs811.cpp`** -> AI Confidence: **99.17%**
404. **`esphome/components/cse7761/cse7761.cpp`** -> AI Confidence: **99.17%**
405. **`esphome/components/datetime/datetime_entity.cpp`** -> AI Confidence: **99.17%**
406. **`esphome/components/display/display_buffer.cpp`** -> AI Confidence: **99.17%**
407. **`esphome/components/display/rect.cpp`** -> AI Confidence: **99.17%**
408. **`esphome/components/gcja5/gcja5.cpp`** -> AI Confidence: **99.17%**
409. **`esphome/components/gps/gps.cpp`** -> AI Confidence: **99.17%**
410. **`esphome/components/gree/gree.cpp`** -> AI Confidence: **99.17%**
411. **`esphome/components/haier/logger_handler.cpp`** -> AI Confidence: **99.17%**
412. **`esphome/components/havells_solar/havells_solar.cpp`** -> AI Confidence: **99.17%**
413. **`esphome/components/hitachi_ac344/hitachi_ac344.cpp`** -> AI Confidence: **99.17%**
414. **`esphome/components/hitachi_ac424/hitachi_ac424.cpp`** -> AI Confidence: **99.17%**
415. **`esphome/components/hlk_fm22x/hlk_fm22x.cpp`** -> AI Confidence: **99.17%**
416. **`esphome/components/hlw8012/hlw8012.cpp`** -> AI Confidence: **99.17%**
417. **`esphome/components/i2c/i2c_bus_arduino.cpp`** -> AI Confidence: **99.17%**
418. **`esphome/components/internal_temperature/internal_temperature_bk72xx.cpp`** -> AI Confidence: **99.17%**
419. **`esphome/components/kamstrup_kmp/kamstrup_kmp.cpp`** -> AI Confidence: **99.17%**
420. **`esphome/components/kuntze/kuntze.cpp`** -> AI Confidence: **99.17%**
421. **`esphome/components/light/light_json_schema.cpp`** -> AI Confidence: **99.17%**
422. **`esphome/components/mcp2515/mcp2515.cpp`** -> AI Confidence: **99.17%**
423. **`esphome/components/micronova/switch/micronova_switch.cpp`** -> AI Confidence: **99.17%**
424. **`esphome/components/mipi_spi/mipi_spi.cpp`** -> AI Confidence: **99.17%**
425. **`esphome/components/modbus/modbus.cpp`** -> AI Confidence: **99.17%**
426. **`esphome/components/modbus_controller/text_sensor/modbus_textsensor.cpp`** -> AI Confidence: **99.17%**
427. **`esphome/components/mpl3115a2/mpl3115a2.cpp`** -> AI Confidence: **99.17%**
428. **`esphome/components/mqtt/mqtt_alarm_control_panel.cpp`** -> AI Confidence: **99.17%**
429. **`esphome/components/mqtt/mqtt_fan.cpp`** -> AI Confidence: **99.17%**
430. **`esphome/components/network/util.h`** -> AI Confidence: **99.17%**
431. **`esphome/components/nfc/ndef_message.cpp`** -> AI Confidence: **99.17%**
432. **`esphome/components/qwiic_pir/qwiic_pir.cpp`** -> AI Confidence: **99.17%**
433. **`esphome/components/remote_base/canalsat_protocol.cpp`** -> AI Confidence: **99.17%**
434. **`esphome/components/remote_base/dooya_protocol.cpp`** -> AI Confidence: **99.17%**
435. **`esphome/components/remote_base/nec_protocol.cpp`** -> AI Confidence: **99.17%**
436. **`esphome/components/remote_receiver/remote_receiver.cpp`** -> AI Confidence: **99.17%**
437. **`esphome/components/ruuvi_ble/ruuvi_ble.cpp`** -> AI Confidence: **99.17%**
438. **`esphome/components/sdl/sdl_esphome.cpp`** -> AI Confidence: **99.17%**
439. **`esphome/components/sdp3x/sdp3x.cpp`** -> AI Confidence: **99.17%**
440. **`esphome/components/selec_meter/selec_meter.cpp`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `esphome/__main__.py` -> **100.0%** Exposure
- `esphome/analyze_memory/cli.py` -> **100.0%** Exposure
- `esphome/analyze_memory/ram_strings.py` -> **100.0%** Exposure
- `esphome/automation.py` -> **100.0%** Exposure
- `esphome/components/alarm_control_panel/__init__.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `esphome/components/rp2040/generate_boards.py` -> **100.0%** Exposure
- `esphome/git.py` -> **100.0%** Exposure
- `script/clang-tidy` -> **100.0%** Exposure
- `script/helpers.py` -> **100.0%** Exposure
- `script/run-in-env.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `esphome/components/api/proto.h` -> **10.0%** Exposure
- `esphome/components/bme680_bsec/bme680_bsec.cpp` -> **10.0%** Exposure
- `esphome/components/fingerprint_grow/fingerprint_grow.cpp` -> **10.0%** Exposure
- `esphome/components/ld2420/ld2420.cpp` -> **10.0%** Exposure
- `esphome/components/mpr121/mpr121.cpp` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `docker/generate_tags.py` -> **100.0%** Exposure
- `esphome/__main__.py` -> **100.0%** Exposure
- `esphome/analyze_memory/cli.py` -> **100.0%** Exposure
- `esphome/analyze_memory/ram_strings.py` -> **100.0%** Exposure
- `esphome/components/as5600/__init__.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `16895` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `esphome/components/modbus/modbus.cpp` (CPP) -> Cumulative Risk: **906.88**
- **Archetype:** `file_cluster_8` (Distance: 13.551 IQR)
- **Magnitude:** 426.78 | **LOC:** 430 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 54.5%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Modbus::send` (Impact: 74.9), `Modbus::tx_blocked` (Impact: 64.8), `Modbus::loop` (Impact: 64.1)

### 2. `esphome/components/valve/__init__.py` (PYTHON) -> Cumulative Risk: **901.97**
- **Archetype:** `file_cluster_4` (Distance: 9.872 IQR)
- **Magnitude:** 169.16 | **LOC:** 246 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `_setup_valve_core` (Impact: 31.5), `valve_control_to_code` (Impact: 14.1), `register_valve` (Impact: 10.7)

### 3. `esphome/components/alarm_control_panel/__init__.py` (PYTHON) -> Cumulative Risk: **900.53**
- **Archetype:** `file_cluster_4` (Distance: 9.667 IQR)
- **Magnitude:** 216.04 | **LOC:** 295 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setup_alarm_control_panel_core_` (Impact: 41.0), `register_alarm_control_panel` (Impact: 10.7), `alarm_action_arm_away_to_code` (Impact: 7.1)

### 4. `esphome/components/lvgl/widgets/keyboard.py` (PYTHON) -> Cumulative Risk: **895.16**
- **Archetype:** `file_cluster_4` (Distance: 9.808 IQR)
- **Magnitude:** 92.1 | **LOC:** 71 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `to_code` (Impact: 43.0), `__init__` (Impact: 7.3), `get_uses` (Impact: 2.7)

### 5. `esphome/components/lvgl/widgets/buttonmatrix.py` (PYTHON) -> Cumulative Risk: **893.45**
- **Archetype:** `file_cluster_13` (Distance: 10.977 IQR)
- **Magnitude:** 296.2 | **LOC:** 277 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `button_update_to_code` (Impact: 81.8), `get_button_data` (Impact: 35.8), `to_code` (Impact: 20.8)

### 6. `esphome/components/lvgl/widgets/__init__.py` (PYTHON) -> Cumulative Risk: **881.3**
- **Archetype:** `file_cluster_4` (Distance: 12.507 IQR)
- **Magnitude:** 826.92 | **LOC:** 674 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 85.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `set_obj_properties` (Impact: 213.5), `create_to_code` (Impact: 64.8), `collect_props` (Impact: 22.4)

### 7. `esphome/components/cover/__init__.py` (PYTHON) -> Cumulative Risk: **872.54**
- **Archetype:** `file_cluster_4` (Distance: 10.057 IQR)
- **Magnitude:** 228.12 | **LOC:** 340 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `setup_cover_core_` (Impact: 39.7), `_validate_mqtt_state_topics` (Impact: 26.5), `cover_control_to_code` (Impact: 17.6)

### 8. `esphome/core/__init__.py` (PYTHON) -> Cumulative Risk: **870.62**
- **Archetype:** `file_cluster_0` (Distance: 12.977 IQR)
- **Magnitude:** 1420.78 | **LOC:** 1044 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 35.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `comment_remover` (Impact: 625.9), `_get_variable_with_full_id_generator` (Impact: 97.9), `add_global` (Impact: 77.3)

### 9. `esphome/cpp_generator.py` (PYTHON) -> Cumulative Risk: **870.14**
- **Archetype:** `file_cluster_16` (Distance: 12.788 IQR)
- **Magnitude:** 1072.78 | **LOC:** 1151 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 69.2%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `safe_exp` (Impact: 170.3), `__str__` (Impact: 103.9), `__imod__` (Impact: 47.6)

### 10. `esphome/components/wake_on_lan/wake_on_lan.cpp` (CPP) -> Cumulative Risk: **865.09**
- **Archetype:** `file_cluster_13` (Distance: 12.876 IQR)
- **Magnitude:** 142.92 | **LOC:** 90 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `WakeOnLanButton::press_action` (Impact: 74.6), `WakeOnLanButton::setup` (Impact: 9.5), `WakeOnLanButton::dump_config` (Impact: 7.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/components/http_request/test_ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/atm90e32/atm90e32.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.307 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.533 IQR)
- **Top Global Matches:** file_cluster_8: 16.307, file_cluster_13: 16.542, file_cluster_11: 16.574
- **Magnitude:** 4064.14 | **LOC:** 1255 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 460
- **Risk Profile:** Cognitive Load (90.0002%), Tech Debt (95.914%)
**Top Internal Functions/Classes:**
  * `ATM90E32Component::run_gain_calibrations` (Impact: 138.0 | O(N^6) | DB: 88)
  * `ATM90E32Component::restore_offset_calibr` (Impact: 135.1 | O(N^6) | DB: 28)
  * `ATM90E32Component::restore_power_offset_` (Impact: 135.1 | O(N^6) | DB: 28)
  * `ATM90E32Component::log_calibration_statu` (Impact: 89.8 | O(N^3) | DB: 460)
  * `ATM90E32Component::setup` (Impact: 83.3 | O(N^5) | DB: 28)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 81`, `args: 211`, `func_start: 59`
* *Risk/State:* `state_mutation: 2951`, `dead_code: 1`, `orphaned_logic: 59`
* *Architecture:* `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` atm90e32.h, cmath, numbers, log.h, cinttypes
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/config_validation.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.649 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.954 IQR)
- **Top Global Matches:** file_cluster_8: 12.649, file_cluster_13: 12.735, file_cluster_0: 12.813
- **Magnitude:** 2579.3 | **LOC:** 2325 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 30.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (14.6455%), Tech Debt (10.2059%)
**Top Internal Functions/Classes:**
  * `date_time` (Impact: 1535.9 | O(N^5) | DB: 29)
  * `validate_id_name` (Impact: 62.3 | O(N^4))
    * *Intent:* """Validate that the config option is an integer in the given range."""
  * `time_period_str_unit` (Impact: 50.6 | O(N^3))
  * `icon` (Impact: 49.4 | O(2^N))
  * `use_id` (Impact: 42.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 434`, `structural_boundaries: 459`, `args: 145`, `func_start: 144`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 85`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 151`, `import: 27`
* *Defense:* `safety: 131`, `doc: 122`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.13
  * `Choke Point (Betweenness):` 0.003548 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` esphome.const, datetime, esphome.util, dataclasses, esphome.components.esp32, collections.abc, esphome.core, contextlib...
  * `Imported By (In-Degree: 1058):` (Excluded from Brief to save tokens)

### `script/build_helpers.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.934 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.137 IQR)
- **Top Global Matches:** file_cluster_13: 10.934, file_cluster_16: 11.061, file_cluster_8: 11.093
- **Magnitude:** 2503.85 | **LOC:** 461 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.2147%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 67`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 19`
* *Architecture:* `io: 9`, `api: 8`, `import: 17`
* *Defense:* `safety: 18`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.16
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` esphome.const, tests.testing_helpers, pathlib, importlib.util, subprocess, helpers, hashlib, __future__...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `script/build_language_schema.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.525 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.264 IQR)
- **Top Global Matches:** file_cluster_13: 11.525, file_cluster_8: 11.538, file_cluster_17: 11.773
- **Magnitude:** 2339.14 | **LOC:** 1093 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (27.1078%), Tech Debt (8.4897%)
**Top Internal Functions/Classes:**
  * `convert` (Impact: 906.0 | O(2^N) | DB: 4)
  * `add_referenced_recursive` (Impact: 252.8 | O(2^N) | DB: 1)
  * `shrink` (Impact: 192.1 | O(N^6) | DB: 8)
    * *Intent:* # added mostly because of schema_name == "microphone.MICROPHONE_SCHEMA" # which is shrunk because th...
  * `build_schema` (Impact: 169.5 | O(N^6) | DB: 1)
  * `add_module_registries` (Impact: 99.1 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 149`, `args: 45`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 73`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 38`, `import: 25`
* *Defense:* `safety: 37`, `doc: 6`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` esphome.const, json, esphome.util, esphome.core, re, esphome.components.adc, voluptuous, esphome.components.mapping...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/esp32/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.341 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.714 IQR)
- **Top Global Matches:** file_cluster_8: 11.341, file_cluster_7: 11.674, file_cluster_13: 11.691
- **Magnitude:** 2329.88 | **LOC:** 2292 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 51.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (11.479%), Tech Debt (9.4966%)
**Top Internal Functions/Classes:**
  * `_write_exclude_components` (Impact: 1392.0 | O(2^N) | DB: 14)
    * *Intent:* # User specified their own value - respect it but warn if insufficient if user_max_sockets is not No...
  * `_check_versions` (Impact: 203.7 | O(N^5))
  * `final_validate` (Impact: 161.7 | O(N^5) | DB: 11)
  * `set_core_data` (Impact: 81.3 | O(N^4) | DB: 2)
  * `_write_idf_component_yml` (Impact: 76.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 160`, `args: 54`, `func_start: 54`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 64`, `dead_code: 2`, `planned_debt: 7`
* *Architecture:* `io: 7`, `api: 43`, `concurrency: 5`, `import: 25`
* *Defense:* `safety: 22`, `doc: 68`, `test: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` esphome.const, esphome.writer, dataclasses, esphome.types, esphome.core, contextlib, re, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/nextion/nextion.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.098 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.506 IQR)
- **Top Global Matches:** file_cluster_8: 14.098, file_cluster_7: 14.385, file_cluster_13: 14.426
- **Magnitude:** 2257.08 | **LOC:** 1304 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 62.5%
- **Algorithmic:** O(N^6) | **DB Complexity:** 64
- **Risk Profile:** Cognitive Load (58.1539%), Tech Debt (91.3545%)
**Top Internal Functions/Classes:**
  * `Nextion::process_nextion_commands_` (Impact: 1010.2 | O(N^6) | DB: 64)
    * *Intent:* // nextion.tech/instruction-set/
  * `Nextion::set_nextion_sensor_state` (Impact: 55.8 | O(N^2) | DB: 2)
  * `Nextion::check_connect_` (Impact: 52.9 | O(N^3) | DB: 21)
  * `Nextion::recv_ret_string_` (Impact: 47.2 | O(N^2) | DB: 16)
  * `Nextion::add_no_result_to_queue_with_set` (Impact: 39.6 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 118`, `args: 146`, `func_start: 37`
* *Risk/State:* `state_mutation: 594`, `duplicate_logic: 8`, `orphaned_logic: 29`
* *Architecture:* `import: 6`
* *Defense:* `safety: 1`, `doc: 30`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` util.h, application.h, nextion.h, helpers.h, log.h, cinttypes
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/display/display.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.355 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.505 IQR)
- **Top Global Matches:** file_cluster_8: 14.355, file_cluster_13: 14.587, file_cluster_11: 14.741
- **Magnitude:** 2229.46 | **LOC:** 932 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (93.798%), Tech Debt (99.5633%)
**Top Internal Functions/Classes:**
  * `Display::filled_gauge` (Impact: 347.1 | O(N^6) | DB: 44)
  * `Display::get_text_bounds` (Impact: 212.2 | O(N^6) | DB: 13)
  * `Display::draw_pixels_at` (Impact: 171.4 | O(N^6) | DB: 14)
  * `Display::regular_polygon` (Impact: 74.5 | O(N^6) | DB: 6)
  * `Display::filled_ring` (Impact: 65.3 | O(N^2) | DB: 28)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 106`, `args: 87`, `func_start: 72`
* *Risk/State:* `state_mutation: 784`, `duplicate_logic: 24`
* *Architecture:* `api: 48`, `import: 6`
* *Defense:* `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` log.h, utility, display.h, hal.h, numbers, display_color_utils.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/pn7160/pn7160.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.1 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.758 IQR)
- **Top Global Matches:** file_cluster_8: 13.1, file_cluster_0: 13.449, file_cluster_13: 13.456
- **Magnitude:** 1970.46 | **LOC:** 1191 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (76.1755%), Tech Debt (95.307%)
**Top Internal Functions/Classes:**
  * `PN7160::process_rf_intf_activated_oid_` (Impact: 370.9 | O(N^6) | DB: 23)
  * `PN7160::process_message_` (Impact: 202.2 | O(N^5))
  * `PN7160::card_emu_t4t_get_response_` (Impact: 156.2 | O(N^6) | DB: 18)
  * `PN7160::set_test_mode` (Impact: 122.0 | O(N^6) | DB: 7)
  * `PN7160::transceive_` (Impact: 111.9 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 130`, `args: 208`, `func_start: 48`
* *Risk/State:* `state_mutation: 401`, `dead_code: 4`, `duplicate_logic: 5`, `orphaned_logic: 42`
* *Architecture:* `io: 1`, `import: 6`
* *Defense:* `safety: 4`, `test: 1`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` utility, automation.h, pn7160.h, hal.h, helpers.h, log.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/pn7150/pn7150.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.123 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.752 IQR)
- **Top Global Matches:** file_cluster_8: 13.123, file_cluster_0: 13.461, file_cluster_13: 13.469
- **Magnitude:** 1954.38 | **LOC:** 1165 | **CtrlFlow:** 68.7% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (76.3223%), Tech Debt (95.8783%)
**Top Internal Functions/Classes:**
  * `PN7150::process_rf_intf_activated_oid_` (Impact: 370.9 | O(N^6) | DB: 23)
  * `PN7150::process_message_` (Impact: 202.2 | O(N^5))
  * `PN7150::card_emu_t4t_get_response_` (Impact: 156.2 | O(N^6) | DB: 18)
  * `PN7150::set_test_mode` (Impact: 122.0 | O(N^6) | DB: 7)
  * `PN7150::transceive_` (Impact: 111.9 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 129`, `args: 205`, `func_start: 48`
* *Risk/State:* `state_mutation: 400`, `dead_code: 4`, `duplicate_logic: 5`, `orphaned_logic: 42`
* *Architecture:* `io: 1`, `import: 6`
* *Defense:* `safety: 4`, `test: 2`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` pn7150.h, utility, automation.h, hal.h, helpers.h, log.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/config.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.459 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.316 IQR)
- **Top Global Matches:** file_cluster_13: 12.459, file_cluster_8: 12.628, file_cluster_16: 12.66
- **Magnitude:** 1917.3 | **LOC:** 1381 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 58.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (25.206%), Tech Debt (95.9244%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 362.8 | O(N^6) | DB: 3)
  * `resolve_extend_remove` (Impact: 232.7 | O(2^N) | DB: 3)
  * `run` (Impact: 149.8 | O(N^5) | DB: 4)
  * `strip_default_ids` (Impact: 113.7 | O(2^N) | DB: 4)
  * `iter_ids` (Impact: 104.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 329`, `structural_boundaries: 270`, `args: 68`, `func_start: 67`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 119`, `duplicate_logic: 23`
* *Architecture:* `api: 64`, `import: 32`
* *Defense:* `safety: 86`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.335
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` esphome.config_helpers, esphome.const, esphome.util, esphome.types, esphome.core, contextlib, esphome.core.config, re...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `esphome/__main__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.519 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.334 IQR)
- **Top Global Matches:** file_cluster_8: 11.519, file_cluster_13: 11.529, file_cluster_16: 11.79
- **Magnitude:** 1775.22 | **LOC:** 1935 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 52.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (20.1355%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_resolve_with_cache` (Impact: 745.8 | O(2^N) | DB: 19)
  * `parse_args` (Impact: 375.4 | O(2^N) | DB: 27)
  * `show_logs` (Impact: 82.0 | O(2^N) | DB: 1)
  * `choose_prompt` (Impact: 66.5 | O(N^4))
  * `check_permissions` (Impact: 55.8 | O(N^4) | DB: 18)
    * *Intent:* """ def _port_found() -> bool: if port is not None: if os.name == "posix": return os.path.exists(por...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 338`, `args: 62`, `func_start: 62`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 67`, `dead_code: 1`
* *Architecture:* `io: 24`, `api: 58`, `concurrency: 2`, `import: 64`
* *Defense:* `safety: 49`, `doc: 42`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` esphome.const, datetime, json, esphome.analyze_memory.cli, esphome.components., modules, esphome.dashboard, subprocess...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `esphome/components/haier/hon_climate.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.022 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.172 IQR)
- **Top Global Matches:** file_cluster_8: 14.022, file_cluster_13: 14.242, file_cluster_11: 14.398
- **Magnitude:** 1765.28 | **LOC:** 1383 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 191
- **Risk Profile:** Cognitive Load (95.9266%), Tech Debt (50.5109%)
**Top Internal Functions/Classes:**
  * `HonClimate::get_alarm_status_answer_hand` (Impact: 868.4 | O(N^6) | DB: 191)
  * `HonClimate::status_handler_` (Impact: 171.1 | O(N^6) | DB: 8)
  * `HonClimate::get_device_version_answer_ha` (Impact: 32.8 | O(N^6) | DB: 19)
  * `HonClimate::get_device_id_answer_handler` (Impact: 15.5 | O(N^6) | DB: 1)
  * `HonClimate::set_quiet_mode_state` (Impact: 14.7 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 51`, `args: 33`, `func_start: 27`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 605`, `dead_code: 2`, `orphaned_logic: 18`
* *Architecture:* `import: 7`
* *Defense:* `safety: 1`, `immutability_locks: 23`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` uart.h, hon_climate.h, chrono, climate.h, string, helpers.h, hon_packet.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/dashboard/web_server.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.651 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.622 IQR)
- **Top Global Matches:** file_cluster_13: 11.651, file_cluster_16: 11.77, file_cluster_4: 11.885
- **Magnitude:** 1724.32 | **LOC:** 1638 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (17.5857%), Tech Debt (43.4924%)
**Top Internal Functions/Classes:**
  * `get` (Impact: 760.5 | O(2^N) | DB: 16)
  * `_redirect_stdout` (Impact: 99.5 | O(N^6))
  * `post` (Impact: 71.7 | O(N^5))
  * `make_app` (Impact: 66.8 | O(N^4) | DB: 21)
  * `is_authenticated` (Impact: 43.1 | O(N^5) | DB: 1)
    * *Intent:* """Check if the request is authenticated."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 403`, `args: 95`, `func_start: 93`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 37`, `high_risk_execution: 1`, `state_mutation: 80`, `duplicate_logic: 11`
* *Architecture:* `io: 23`, `api: 115`, `concurrency: 120`, `import: 66`
* *Defense:* `safety: 34`, `doc: 78`, `test: 1`, `sync_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` secrets, datetime, json, tornado.httputil, tornado, tornado.log, esphome.components.rtl87xx.boards, subprocess...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `esphome/components/prometheus/prometheus_handler.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.643 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.345 IQR)
- **Top Global Matches:** file_cluster_8: 13.643, file_cluster_7: 14.137, file_cluster_13: 14.215
- **Magnitude:** 1660.98 | **LOC:** 1104 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 72.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (61.6916%), Tech Debt (86.4638%)
**Top Internal Functions/Classes:**
  * `PrometheusHandler::climate_row_` (Impact: 193.8 | O(N^6) | DB: 33)
  * `PrometheusHandler::light_row_` (Impact: 80.0 | O(N^6) | DB: 18)
  * `PrometheusHandler::cover_row_` (Impact: 53.9 | O(N^6) | DB: 13)
  * `PrometheusHandler::update_entity_row_` (Impact: 45.7 | O(N^6) | DB: 17)
  * `PrometheusHandler::fan_row_` (Impact: 45.4 | O(N^6) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 87`, `args: 301`, `func_start: 44`
* *Risk/State:* `state_mutation: 568`, `orphaned_logic: 43`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* `sync_locks: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` application.h, prometheus_handler.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/thermostat/thermostat_climate.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.069 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.373 IQR)
- **Top Global Matches:** file_cluster_8: 14.069, file_cluster_13: 14.289, file_cluster_11: 14.401
- **Magnitude:** 1595.7 | **LOC:** 1683 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 43.8%
- **Algorithmic:** O(N^6) | **DB Complexity:** 197
- **Risk Profile:** Cognitive Load (74.3962%), Tech Debt (9.2574%)
**Top Internal Functions/Classes:**
  * `ThermostatClimate::setup` (Impact: 1147.9 | O(N^6) | DB: 197)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 142`, `args: 71`, `func_start: 79`
* *Risk/State:* `state_mutation: 434`, `dead_code: 4`, `orphaned_logic: 1`
* *Architecture:* `import: 5`
* *Defense:* `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` application.h, thermostat_climate.h, helpers.h, log.h, cinttypes
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/seeed_mr24hpc1/seeed_mr24hpc1.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.595 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.13 IQR)
- **Top Global Matches:** file_cluster_8: 13.595, file_cluster_13: 14.05, file_cluster_7: 14.059
- **Magnitude:** 1553.88 | **LOC:** 1009 | **CtrlFlow:** 82.6% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (97.6527%), Tech Debt (95.7054%)
**Top Internal Functions/Classes:**
  * `MR24HPC1Component::r24_frame_parse_open_` (Impact: 348.0 | O(N^6) | DB: 8)
    * *Intent:* // Parsing the underlying open parameters
  * `MR24HPC1Component::loop` (Impact: 151.4 | O(N^3) | DB: 47)
    * *Intent:* // main loop
  * `MR24HPC1Component::r24_split_data_frame_` (Impact: 131.9 | O(N^2) | DB: 38)
    * *Intent:* // split data frame
  * `MR24HPC1Component::r24_frame_parse_work_` (Impact: 96.6 | O(N^2) | DB: 2)
  * `MR24HPC1Component::r24_parse_data_frame_` (Impact: 63.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 303`, `structural_boundaries: 64`, `args: 66`, `func_start: 53`
* *Risk/State:* `high_risk_execution: 17`, `state_mutation: 513`, `orphaned_logic: 51`
* *Architecture:* `import: 4`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` utility, helpers.h, log.h, seeed_mr24hpc1.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/pipsolar/pipsolar.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.097 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.555 IQR)
- **Top Global Matches:** file_cluster_8: 14.097, file_cluster_13: 14.525, file_cluster_7: 14.54
- **Magnitude:** 1541.68 | **LOC:** 812 | **CtrlFlow:** 81.9% | **Authorship Centralization:** 62.5%
- **Algorithmic:** O(N^6) | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (78.7327%), Tech Debt (82.0501%)
**Top Internal Functions/Classes:**
  * `Pipsolar::loop` (Impact: 243.3 | O(N^6) | DB: 45)
  * `Pipsolar::handle_qpiws_` (Impact: 236.4 | O(N^2) | DB: 42)
  * `Pipsolar::handle_qflag_` (Impact: 184.9 | O(N^6) | DB: 15)
  * `Pipsolar::send_next_poll_` (Impact: 48.6 | O(N^6) | DB: 8)
  * `Pipsolar::handle_qpiri_` (Impact: 44.1 | O(N^1) | DB: 45)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 51`, `args: 42`, `func_start: 28`
* *Risk/State:* `state_mutation: 599`, `orphaned_logic: 28`
* *Architecture:* `import: 3`
* *Defense:* `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` pipsolar.h, helpers.h, log.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/tuya/tuya.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.768 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.992 IQR)
- **Top Global Matches:** file_cluster_8: 13.768, file_cluster_13: 14.023, file_cluster_11: 14.173
- **Magnitude:** 1524.64 | **LOC:** 765 | **CtrlFlow:** 73.8% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (95.059%), Tech Debt (94.8012%)
**Top Internal Functions/Classes:**
  * `Tuya::handle_command_` (Impact: 421.7 | O(N^6) | DB: 54)
  * `Tuya::handle_datapoints_` (Impact: 170.0 | O(N^4) | DB: 24)
  * `Tuya::dump_config` (Impact: 105.8 | O(N^5) | DB: 1)
  * `Tuya::set_numeric_datapoint_value_` (Impact: 103.2 | O(N^6) | DB: 3)
  * `Tuya::send_raw_command_` (Impact: 43.6 | O(N^2) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 73`, `args: 85`, `func_start: 35`
* *Risk/State:* `state_mutation: 498`, `dead_code: 1`, `orphaned_logic: 35`
* *Architecture:* `io: 1`, `import: 8`
* *Defense:* `immutability_locks: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` util.h, captive_portal.h, wifi_component.h, gpio.h, tuya.h, helpers.h, log.h, util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/toshiba/toshiba.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.16 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.337 IQR)
- **Top Global Matches:** file_cluster_8: 14.16, file_cluster_13: 14.468, file_cluster_7: 14.513
- **Magnitude:** 1517.46 | **LOC:** 1377 | **CtrlFlow:** 77.1% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 89
- **Risk Profile:** Cognitive Load (72.8997%), Tech Debt (30.656%)
**Top Internal Functions/Classes:**
  * `ToshibaClimate::on_receive` (Impact: 327.6 | O(N^3) | DB: 70)
  * `ToshibaClimate::setup` (Impact: 100.1 | O(N^2) | DB: 89)
  * `ToshibaClimate::process_ras_2819t_comman` (Impact: 71.6 | O(N^2) | DB: 34)
  * `is_valid_ras_2819t_command` (Impact: 31.1 | O(N^2) | DB: 32)
  * `ToshibaClimate::encode_` (Impact: 30.7 | O(N^6) | DB: 7)
    * *Intent:* // Log final messages being transmitted
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 66`, `args: 34`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `state_mutation: 843`, `duplicate_logic: 2`, `orphaned_logic: 6`
* *Architecture:* `import: 4`
* *Defense:* `doc: 6`, `immutability_locks: 109`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` toshiba_ac_protocol.h, toshiba.h, vector, helpers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/waveshare_epaper/waveshare_epaper.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.685 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.409 IQR)
- **Top Global Matches:** file_cluster_8: 12.685, file_cluster_7: 13.178, file_cluster_13: 13.287
- **Magnitude:** 1509.62 | **LOC:** 4775 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 127
- **Risk Profile:** Cognitive Load (76.3143%), Tech Debt (36.1544%)
**Top Internal Functions/Classes:**
  * `WaveshareEPaperTypeA::display` (Impact: 664.4 | O(N^6) | DB: 127)
  * `WaveshareEPaper7C::draw_absolute_pixel_i` (Impact: 50.4 | O(N^6) | DB: 15)
  * `WaveshareEPaper7C::color_to_hex` (Impact: 40.6 | O(N^2) | DB: 8)
  * `WaveshareEPaperTypeA::dump_config` (Impact: 40.1 | O(N^1))
  * `WaveshareEPaper7C::init_internal_7c_` (Impact: 24.6 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 141`, `args: 69`, `func_start: 116`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 505`, `orphaned_logic: 31`
* *Architecture:* `import: 6`
* *Defense:* `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` bitset, application.h, waveshare_epaper.h, helpers.h, log.h, cinttypes
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/wifi/wifi_component_esp_idf.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.97 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.031 IQR)
- **Top Global Matches:** file_cluster_13: 14.97, file_cluster_8: 15.125, file_cluster_11: 15.204
- **Magnitude:** 1483.3 | **LOC:** 1227 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 71.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 116
- **Risk Profile:** Cognitive Load (87.5893%), Tech Debt (52.048%)
**Top Internal Functions/Classes:**
  * `WiFiComponent::wifi_process_event_` (Impact: 489.3 | O(N^6) | DB: 116)
  * `event_handler` (Impact: 202.2 | O(N^2) | DB: 59)
    * *Intent:* // general design: event handler translates events and pushes them to a queue, // events get process...
  * `WiFiComponent::wifi_ap_ip_config_` (Impact: 34.7 | O(N^1) | DB: 35)
  * `WiFiComponent::wifi_scan_start_` (Impact: 13.8 | O(N^1) | DB: 12)
  * `WiFiComponent::wifi_sta_ip_addresses` (Impact: 13.2 | O(N^1) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 103`, `args: 48`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 12`, `state_mutation: 699`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 8`
* *Architecture:* `import: 25`
* *Defense:* `safety: 2`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` esp_wifi_types.h, application.h, wifi_component.h, algorithm, memory, task.h, err.h, esp_wifi.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/shelly_dimmer/stm32flash.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.889 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.646 IQR)
- **Top Global Matches:** file_cluster_8: 13.889, file_cluster_13: 14.057, file_cluster_11: 14.085
- **Magnitude:** 1476.98 | **LOC:** 1066 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (74.6649%), Tech Debt (18.6234%)
**Top Internal Functions/Classes:**
  * `stm32_init` (Impact: 191.7 | O(N^3) | DB: 45)
  * `stm32_write_memory` (Impact: 63.6 | O(N^6) | DB: 21)
  * `stm32_crc_memory` (Impact: 63.5 | O(N^6) | DB: 8)
  * `stm32_read_memory` (Impact: 50.4 | O(N^6) | DB: 3)
  * `stm32_get_ack_timeout` (Impact: 34.6 | O(N^2) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 197`, `args: 59`, `func_start: 30`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 753`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 1`, `import: 8`
* *Defense:* `safety: 7`, `immutability_locks: 139`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` stm32flash.h, memory, algorithm, defines.h, debug.h, dev_table.h, cstdint, log.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/core/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.977 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.074 IQR)
- **Top Global Matches:** file_cluster_0: 12.977, file_cluster_13: 13.097, file_cluster_11: 13.187
- **Magnitude:** 1420.78 | **LOC:** 1044 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 35.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 76
- **Risk Profile:** Cognitive Load (66.4082%), Tech Debt (55.0062%)
**Top Internal Functions/Classes:**
  * `comment_remover` (Impact: 625.9 | O(2^N) | DB: 76)
  * `_get_variable_with_full_id_generator` (Impact: 97.9 | O(2^N))
    * *Intent:* # Fast path, check if already registered without awaiting
  * `add_global` (Impact: 77.3 | O(N^4) | DB: 3)
  * `add_define` (Impact: 40.4 | O(N^4))
  * `as_dict` (Impact: 28.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 346`, `args: 114`, `func_start: 114`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 203`, `dead_code: 4`, `duplicate_logic: 8`
* *Architecture:* `io: 2`, `api: 114`, `concurrency: 4`, `import: 26`
* *Defense:* `safety: 33`, `doc: 27`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` esphome.const, esphome.util, esphome.components.esp32, math, contextlib, collections, re, esphome.config_validation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/xiaomi_ble/xiaomi_ble.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.482 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.262 IQR)
- **Top Global Matches:** file_cluster_8: 14.482, file_cluster_13: 14.604, file_cluster_11: 14.818
- **Magnitude:** 1398.3 | **LOC:** 467 | **CtrlFlow:** 86.8% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 70
- **Risk Profile:** Cognitive Load (91.8398%), Tech Debt (10.8091%)
**Top Internal Functions/Classes:**
  * `parse_xiaomi_header` (Impact: 351.9 | O(2^N) | DB: 58)
  * `decrypt_xiaomi_payload` (Impact: 230.3 | O(2^N) | DB: 54)
  * `parse_xiaomi_message` (Impact: 113.5 | O(2^N) | DB: 21)
  * `report_xiaomi_results` (Impact: 61.1 | O(2^N) | DB: 1)
  * `parse_xiaomi_value` (Impact: 59.6 | O(N^1) | DB: 70)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 23`, `args: 44`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 16`, `state_mutation: 573`, `orphaned_logic: 1`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` crypto.h, xiaomi_ble.h, vector, ccm.h, esp_idf_version.h, helpers.h, log.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `esphome/components/lightwaverf/LwRx.cpp` (CPP) | Magnitude: 775.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 323, indent_spaces: 270, pointers: 153, branch: 123
- `tests/unit_tests/test_espota2.py` (PYTHON) | Magnitude: 276.02 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 420, test: 163, structural_boundaries: 107, explicit_casts: 102
- `tests/dashboard/status/test_mdns.py` (PYTHON) | Magnitude: 129.1 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 124, test: 86, structural_boundaries: 59, doc: 30
- `esphome/components/hub75/hub75.cpp` (CPP) | Magnitude: 382.1 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 104, branch: 37, pointers: 33
- `.github/scripts/codeowners.js` (JAVASCRIPT) | Magnitude: 147.34 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 118, branch: 38, immutability_locks: 36, state_mutation: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `esphome/components/rp2040/gpio.cpp` (CPP) | Magnitude: 140.3 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, state_mutation: 56, pointers: 35, branch: 29
- `esphome/components/feedback/feedback_cover.cpp` (CPP) | Magnitude: 536.04 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 255, indent_spaces: 225, pointers: 161, branch: 96

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/unit_tests/test_wizard.py` (PYTHON) | Magnitude: 110.5 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 245, structural_boundaries: 108, test: 80, doc: 62
- `docker/ha-addon-rootfs/etc/cont-init.d/30-esphome-fork.sh` (SHELL) | Magnitude: 4.11 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, state_mutation: 21, branch: 15, structural_boundaries: 14
- `docker/docker_entrypoint.sh` (SHELL) | Magnitude: 2.93 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 13, state_mutation: 6, reflection_metaprogramming: 6, indent_spaces: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `esphome/components/bang_bang/bang_bang_climate.h` (CPP) | Magnitude: 20.96 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 16, doc: 12, pointers: 11
- `esphome/components/es7243e/audio_adc.py` (PYTHON) | Magnitude: 8.84 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 13, import: 5, concurrency: 3
- `esphome/components/audio_dac/audio_dac.h` (CPP) | Magnitude: 21.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, state_mutation: 5, import: 2
- `esphome/components/mipi_spi/mipi_spi.h` (CPP) | Magnitude: 1372.22 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 423, state_mutation: 413, pointers: 234, branch: 118
- `esphome/components/adalight/__init__.py` (PYTHON) | Magnitude: 5.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 8, import: 6, concurrency: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `esphome/components/heatpumpir/heatpumpir.cpp` (CPP) | Magnitude: 463.58 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 196, state_mutation: 115, structural_boundaries: 70, branch: 66

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `esphome/dashboard/util/subprocess.py` (PYTHON) | Magnitude: 28.48 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, concurrency: 16, structural_boundaries: 14, ipc_rpc_bridges: 6
- `tests/component_tests/light/test_effect_validation.py` (PYTHON) | Magnitude: 162.52 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 160, structural_boundaries: 68, test: 48, encapsulation: 46
- `esphome/components/mqtt/custom_mqtt_device.h` (CPP) | Magnitude: 67.94 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 47, state_mutation: 47, pointers: 37, immutability_locks: 34
- `tests/component_tests/deep_sleep/test_deep_sleep.py` (PYTHON) | Magnitude: 11.56 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 10, doc: 10, test: 10
- `tests/dashboard/common.py` (PYTHON) | Magnitude: 4.26 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, io: 3, api: 2, doc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/integration/test_varint_five_byte_device_id.py` (PYTHON) | Magnitude: 62.3 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 72, branch: 26, structural_boundaries: 23, safety: 15
- `tests/integration/test_text_sensor_raw_state.py` (PYTHON) | Magnitude: 347.78 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 286, branch: 118, safety: 64, structural_boundaries: 63
- `tests/integration/test_api_message_size_batching.py` (PYTHON) | Magnitude: 47.3 | Delta: **0.12 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 39, branch: 28, safety: 28
- `tests/integration/test_duplicate_entities.py` (PYTHON) | Magnitude: 39.88 | Delta: **0.267 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 116, branch: 50, structural_boundaries: 37, test: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `esphome/components/rpi_dpi_rgb/display.py` (PYTHON) | Magnitude: 157.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 154, structural_boundaries: 30, concurrency: 30, state_mutation: 28
- `esphome/components/mipi_rgb/display.py` (PYTHON) | Magnitude: 274.72 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 244, concurrency: 62, structural_boundaries: 55, state_mutation: 36
- `esphome/components/ble_rssi/sensor.py` (PYTHON) | Magnitude: 93.28 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 60, state_mutation: 21, structural_boundaries: 14, concurrency: 14
- `esphome/components/ade7880/sensor.py` (PYTHON) | Magnitude: 175.32 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 222, concurrency: 69, state_mutation: 35, structural_boundaries: 33
- `tests/integration/test_light_constant_brightness.py` (PYTHON) | Magnitude: 93.66 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 122, structural_boundaries: 35, concurrency: 25, branch: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `esphome/components/time/posix_tz.h` (CPP) | Magnitude: 17.0 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 99, pointers: 15, indent_spaces: 15, state_mutation: 14
- `esphome/components/bmp581_base/bmp581_base.cpp` (CPP) | Magnitude: 69.16 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 245, indent_spaces: 76, pointers: 44, state_mutation: 30
- `esphome/components/weikai/wk_reg_def.h` (CPP) | Magnitude: 67.12 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 343, state_mutation: 51, immutability_locks: 51, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `esphome/components/opentherm/sensor/__init__.py` (PYTHON) | Magnitude: 27.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, import: 4, branch: 3
- `tests/script/test_test_helpers.py` (PYTHON) | Magnitude: 102.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 129, structural_boundaries: 59, test: 54, safety: 22
- `esphome/components/a01nyub/a01nyub.cpp` (CPP) | Magnitude: 54.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 21, pointers: 18, branch: 9
- `esphome/components/adc/adc_sensor_esp8266.cpp` (CPP) | Magnitude: 37.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 21, indent_spaces: 20, pointers: 11, macros: 8
- `esphome/components/weikai/weikai.cpp` (CPP) | Magnitude: 777.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 446, indent_spaces: 373, doc: 252, pointers: 176

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `esphome/core/defines.h` -> Churn: **100.0%** | Cog Load: 85.0% | Debt: 0.0%
- `esphome/components/api/api_connection.cpp` -> Churn: **98.98%** | Cog Load: 92.4766% | Debt: 32.5313%
- `esphome/components/wifi/wifi_component.cpp` -> Churn: **95.32%** | Cog Load: 47.9401% | Debt: 86.3872%
- `esphome/core/helpers.h` -> Churn: **94.56%** | Cog Load: 38.1199% | Debt: 98.4265%
- `esphome/components/wifi/wifi_component.h` -> Churn: **90.61%** | Cog Load: 25.2761% | Debt: 99.958%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `script/build_helpers.py` -> **Javier Peletier** (100.0% isolated ownership) | Magnitude: 2503.85
- `esphome/components/shelly_dimmer/stm32flash.cpp` -> **Jonathan Swoboda** (100.0% isolated ownership) | Magnitude: 1476.98
- `script/ci_memory_impact_comment.py` -> **J. Nick Koston** (100.0% isolated ownership) | Magnitude: 1305.5
- `esphome/components/esp32_ble_client/ble_client_base.cpp` -> **J. Nick Koston** (85.7% isolated ownership) | Magnitude: 1257.86
- `esphome/components/speaker_source/speaker_source_media_player.cpp` -> **Kevin Ahrendt** (100.0% isolated ownership) | Magnitude: 1236.98

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `esphome/core/application.h` -> **Severity: 0.38** (Bridge: 0.0038 * Flux: 99.9888%)
- `esphome/core/component.cpp` -> **Severity: 0.308** (Bridge: 0.0031 * Flux: 100.0%)
- `esphome/loader.py` -> **Severity: 0.228** (Bridge: 0.0031 * Flux: 73.3825%)
- `esphome/config_validation.py` -> **Severity: 0.154** (Bridge: 0.0035 * Flux: 43.3357%)
- `esphome/core/preferences.h` -> **Severity: 0.139** (Bridge: 0.0014 * Flux: 99.9694%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `esphome/config_validation.py` -> **Severity: 3713.0** (Blast Radius: 37.13 * Doc Risk: 100.0%)
- `esphome/core/optional.h` -> **Severity: 1895.625** (Blast Radius: 35.543 * Doc Risk: 53.3333%)
- `esphome/core/macros.h` -> **Severity: 1647.999** (Blast Radius: 30.9 * Doc Risk: 53.3333%)
- `esphome/helpers.py` -> **Severity: 839.9** (Blast Radius: 8.399 * Doc Risk: 100.0%)
- `esphome/util.py` -> **Severity: 823.3** (Blast Radius: 8.233 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
