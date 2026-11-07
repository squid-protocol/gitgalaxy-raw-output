# ARCHITECTURAL_BRIEF: esphome
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/esphome/esphome.git` |
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
- **Scope:** 7246 analyzed artifact(s), 468640 LOC.
- **Load-bearing artifact:** `esphome/config_validation.py` -- 1059 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `esphome/dashboard/web_server.py` -- pulls in 61 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `esphome/components/http_request/httplib.h` at magnitude 6992.2 (structural weight, not risk).
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
| Total Artifacts | 7498 |
| Analyzed Artifacts (Scanned) | 7246 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 252 |
| Total LOC | 468640 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 96.6% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5666 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1078 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.1171 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 193 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| YAML | 2774 | 33010 | 38.3% |
| CPP | 2546 | 262176 | 35.1% |
| PYTHON | 1867 | 169807 | 25.8% |
| PLAINTEXT | 13 | 0 | 0.2% |
| MARKDOWN | 12 | 0 | 0.2% |
| SHELL | 11 | 136 | 0.2% |
| JAVASCRIPT | 7 | 740 | 0.1% |
| JSON | 6 | 127 | 0.1% |
| C | 4 | 409 | 0.1% |
| PROTO | 2 | 2153 | 0.0% |
| DOCKERFILE | 1 | 60 | 0.0% |
| BATCH | 1 | 16 | 0.0% |
| XML | 1 | 0 | 0.0% |
| CSV | 1 | 6 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 7243 |
| utf-8 | bom | 3 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 47%, Parameter Forwarders Files 16%, Large Core Modules (3) 9%, Compute Cores Files 7%, Large Core Modules (2) 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 7221 | 99.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 25 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 252*

**Composition by Extension & Reason:**
- `.yaml`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Zero-Density Threshold (LOC: 51, Signals: 0), 4x Zero-Density Threshold (LOC: 54, Signals: 0)
- `no_extension`: 22x Unsupported Format (.undeterminable), 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 604 LOC)
- `.py`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 68 LOC), 1x Excluded (Machine-Generated Source Code Signature: 141 LOC)
- `.script`: 13x Excluded (Unsupported Extension: '.script')
- `.cpp`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3900 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2684 LOC)
- `.h`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3291 LOC), 1x Excluded (Machine-Generated Source Code Signature: 13 LOC)
- `.ttf`: 6x Excluded (Explicitly Denied Extension: '.ttf')
- `.conf`: 5x Excluded (Unsupported Extension: '.conf')
- `.j2`: 5x Excluded (Unsupported Extension: '.j2')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 249 LOC)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gtpl`: 2x Excluded (Unsupported Extension: '.gtpl')
- `.wav`: 2x Excluded (Explicitly Denied Extension: '.wav')
- `.bdf`: 2x Excluded (Unsupported Extension: '.bdf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 17.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.6 | 26.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 17.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 15.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 32.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 94.4 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.9 | 0.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 45.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5066 | 1065 | 1 | `esphome/components/http_request/httplib.h` |
| cleanup | 387 | 146 | 0 | `esphome/components/sprinkler/sprinkler.cpp` |
| guards | 37515 | 2938 | 13 | `esphome/components/http_request/httplib.h` |
| danger | 3617 | 665 | 0 | `esphome/config_validation.py` |
| concurrency | 11064 | 1493 | 4 | `tests/dashboard/test_web_server.py` |
| connectivity | 14812 | 2665 | 5 | `esphome/components/http_request/httplib.h` |
| io | 1445 | 311 | 0 | `esphome/components/web_server/web_server.cpp` |
| crypto | 30 | 24 | 0 | `esphome/components/wifi/wpa2_eap.py` |
| ipc | 199 | 45 | 0 | `script/helpers.py` |
| time | 93 | 28 | 0 | `esphome/components/http_request/httplib.h` |
| serialization | 0 | 0 | 0 | - |
| regex | 381 | 111 | 0 | `esphome/components/http_request/httplib.h` |
| events | 875 | 185 | 0 | `esphome/components/http_request/httplib.h` |
| tests | 5436 | 212 | 0 | `tests/unit_tests/test_main.py` |
| docs | 11433 | 1503 | 3 | `esphome/core/helpers.h` |
| debt | 1394 | 271 | 0 | `.github/workflows/ci.yml` |
| mutation | 134545 | 3770 | 49 | `esphome/const.py` |
| dead_code | 12406 | 2032 | 4 | `esphome/components/waveshare_epaper/waveshare_epaper.cpp` |
| credential | 25 | 17 | 0 | `script/api_protobuf/api_protobuf.py` |
| threat | 28 | 8 | 0 | `esphome/core/helpers.cpp` |
| ml_ai | 8 | 5 | 0 | `esphome/components/display/display.cpp` |
| ui | 19 | 6 | 0 | `esphome/components/substitutions/jinja.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `esphome/components/web_server/web_server.cpp` (Hits: 99)
- `esphome/components/http_request/httplib.h` (Hits: 92)
- `tests/unit_tests/test_helpers.py` (Hits: 67)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **config_validation.py** (`esphome/config_validation.py`) — 1059 inbound connections
2. **codegen.py** (`esphome/codegen.py`) — 1038 inbound connections
3. **const.py** (`esphome/const.py`) — 1027 inbound connections
4. **log.h** (`esphome/core/log.h`) — 1014 inbound connections
5. **__init__.py** (`esphome/components/__init__.py`) — 872 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **web_server.py** (`esphome/dashboard/web_server.py`) — 61 outbound dependencies
2. **httplib.h** (`esphome/components/http_request/httplib.h`) — 61 outbound dependencies
3. **application.h** (`esphome/core/application.h`) — 50 outbound dependencies
4. **__main__.py** (`esphome/__main__.py`) — 43 outbound dependencies
5. **__init__.py** (`esphome/components/lvgl/__init__.py`) — 34 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `PrometheusHandler::print_metric_labels_` **(Many-Argument Workhorses)** (@ `esphome/components/prometheus/prometheus_handler.cpp`) -> Impact: **299.0** | LOC: 953
  * *Intent:* #ifdef USE_ESP8266
- `SSLSocketStream::read` **(Many-Argument Workhorses)** (@ `esphome/components/http_request/httplib.h`) -> Impact: **288.1** | LOC: 1051
- `run_grouped_component_tests` **(Many-Argument Workhorses)** (@ `script/test_build_components`) -> Impact: **282.8** | LOC: 315
- `run_grouped_component_tests` **(Many-Argument Workhorses)** (@ `script/test_build_components.py`) -> Impact: **282.8** | LOC: 315
- `MCP2515::set_bitrate_` **(Many-Argument Workhorses)** (@ `esphome/components/mcp2515/mcp2515.cpp`) -> Impact: **242.7** | LOC: 316
- `test_text_sensor_raw_state` **(Many-Argument Workhorses)** (@ `tests/integration/test_text_sensor_raw_state.py`) -> Impact: **227.8** | LOC: 395
- `Sim800LComponent::parse_cmd_` **(Compute Cores)** (@ `esphome/components/sim800l/sim800l.cpp`) -> Impact: **203.0** | LOC: 354
- `MQTTClientComponent::dns_found_callback` **(Many-Argument Workhorses)** (@ `esphome/components/mqtt/mqtt_client.cpp`) -> Impact: **199.2** | LOC: 503
  * *Intent:* #if defined(USE_ESP8266) && LWIP_VERSION_MAJOR == 1
- `SpeakerMediaPlayer::watch_media_commands_` **(I/O & Config Routines)** (@ `esphome/components/speaker/media_player/speaker_media_player.cpp`) -> Impact: **193.9** | LOC: 499
- `BLEClientBase::gattc_event_handler` **(Many-Argument Workhorses)** (@ `esphome/components/esp32_ble_client/ble_client_base.cpp`) -> Impact: **185.4** | LOC: 268

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/integration` | 108 | 16956.08 | 30.32% | 0.0% |
| `esphome` | 37 | 13731.86 | 45.88% | 9.49% |
| `script` | 43 | 8738.72 | 35.62% | 3.56% |
| `esphome/core` | 58 | 8214.48 | 19.14% | 20.33% |
| `esphome/components/http_request` | 10 | 8150.66 | 38.67% | 23.56% |
| `tests/unit_tests` | 32 | 7185.0 | 11.17% | 0.0% |
| `esphome/components/remote_base` | 73 | 6345.72 | 40.0% | 39.19% |
| `esphome/components/api` | 30 | 4735.08 | 27.14% | 26.75% |
| `esphome/components/lvgl` | 19 | 4313.84 | 64.21% | 15.67% |
| `esphome/components/wifi` | 9 | 4225.06 | 57.08% | 61.79% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `esphome/components/ade7880/ade7880_i2c.cpp` -> **100.0%** Exposure
- `esphome/components/climate/climate.h` -> **100.0%** Exposure
- `esphome/components/esp32/core.cpp` -> **100.0%** Exposure
- `esphome/components/esp8266/core.cpp` -> **100.0%** Exposure
- `esphome/components/globals/globals_component.h` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `docker/build.py` -> **100.0%** Exposure
- `docker/generate_tags.py` -> **100.0%** Exposure
- `esphome/address_cache.py` -> **100.0%** Exposure
- `esphome/analyze_memory/__init__.py` -> **100.0%** Exposure
- `esphome/analyze_memory/cli.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `esphome/components/waveshare_epaper/waveshare_epaper.cpp` -> **255** Orphaned Functions | **0** Duplicates
- `esphome/components/api/api_connection.cpp` -> **168** Orphaned Functions | **0** Duplicates
- `esphome/components/thermostat/thermostat_climate.cpp` -> **152** Orphaned Functions | **0** Duplicates
- `esphome/components/sprinkler/sprinkler.cpp` -> **144** Orphaned Functions | **0** Duplicates
- `tests/unit_tests/test_main.py` -> **138** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/unit_tests/fixtures/yaml_util/secrets.yaml` -> **100.0%** Exposure
- `tests/components/web_server/test_ota.esp32-idf.yaml` -> **99.9977%** Exposure
- `tests/components/ota/common.yaml` -> **99.9954%** Exposure
- `tests/components/opentherm/common.yaml` -> **83.3175%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `17188` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `esphome/components/http_request/httplib.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.753)
- **Top Global Matches:** file_cluster_4: 10.753, file_cluster_15: 11.696, file_cluster_12: 12.673
- **Magnitude:** 6992.2 | **LOC:** 9696 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **61**; blast radius 0.09; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.9%), Connectivity (formerly Api Exposure) (63.7%)
- **Documentation Coverage:** 99.8891% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SSLSocketStream::read` **(Many-Argument Workhorses)** (Impact: 288.1)
  * `Server::process_request` **(Many-Argument Workhorses)** (Impact: 129.0)
  * `parse` **(Many-Argument Workhorses)** (Impact: 103.6)
  * `find_content_type` **(Many-Argument Workhorses)** (Impact: 101.3)
  * `status_message` **(Compute Cores)** (Impact: 99.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 591 instances
* *Concurrency (weighted view):* 72
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 2004
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1407`, `structural_boundaries: 2539`, `args: 1215`, `func_start: 639`, `class_start: 65`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 822`, `planned_debt: 8`, `fragile_debt: 5`
* *Architecture:* `io: 92`, `api: 278`, `concurrency: 27`, `import: 63`
* *Defense:* `safety: 137`, `doc: 4`, `sync_locks: 40`, `immutability_locks: 1867`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.09
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.000803
  * `Imports (Out-Degree: 3):` CoreFoundation.h, Security.h, TargetConditionals.h, algorithm, inet.h, array, atomic, decode.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `script/api_protobuf/api_protobuf.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.028)
- **Top Global Matches:** file_cluster_5: 8.028, file_cluster_0: 9.266, file_cluster_12: 10.033
- **Magnitude:** 2513.88 | **LOC:** 3253 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 90.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.059; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (74.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.0%)
- **Documentation Coverage:** 81.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_message_type` **(Many-Argument Workhorses)** (Impact: 140.9)
  * `main` **(I/O & Config Routines)** (Impact: 82.8)
    * *Intent:* """Main function to generate the C++ classes."""
  * `build_type_usage_map` **(Compute Cores)** (Impact: 77.8)
  * `build_service_message_type` **(Compute Cores)** (Impact: 55.2)
  * `get_size_calculation` **(Many-Argument Workhorses)** (Impact: 50.2)
    * *Intent:* # For repeated fields, we always need to pass force=True to the underlying type's calculation # This...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 284 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1036
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 446`, `structural_boundaries: 656`, `args: 217`, `func_start: 216`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 1`, `state_mutation: 468`, `planned_debt: 1`, `duplicate_logic: 61`, `unreferenced_by_name: 3`
* *Architecture:* `io: 8`, `api: 230`, `import: 12`
* *Defense:* `safety: 13`, `doc: 79`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, abc, aioesphomeapi.api_options_pb2, clang_format, enum, google.protobuf.descriptor_pb2, pathlib, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/config_validation.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.71)
- **Top Global Matches:** file_cluster_12: 6.71, file_cluster_15: 8.444, file_cluster_16: 9.206
- **Magnitude:** 1961.4 | **LOC:** 2325 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 27.8%
- **Blast Radius:** changing it is visible to **1059** in-repo importer(s); it depends on **26**; blast radius 16.253; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.1%)
- **Documentation Coverage:** 63.8989% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `date_time` **(Many-Argument Workhorses)** (Impact: 55.0)
  * `validator` **(Defensive Guards)** (Impact: 33.6)
  * `one_of` **(Compute Cores)** (Impact: 28.6)
    * *Intent:* """Validate that the config option is one of the given values. :param values: The valid values for t...
  * `require_framework_version` **(Compute Cores)** (Impact: 28.1)
  * `validate_registry_entry` **(Defensive Guards)** (Impact: 24.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 219 instances
* *State Mutation (weighted view):* 751
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 381`, `structural_boundaries: 479`, `args: 146`, `func_start: 144`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 313`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 2`, `api: 141`, `import: 27`
* *Defense:* `safety: 128`, `doc: 60`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.253
  * `Choke Point (Betweenness):` 0.000741 | `Ripple Effect (Closeness):` 0.129397
  * `Imports (Out-Degree: 11):` __future__, collections.abc, contextlib, dataclasses, datetime, difflib, esphome, esphome.codegen...
  * `Imported By (In-Degree: 1059):` (Excluded from Brief to save tokens)

### `esphome/components/remote_base/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.143)
- **Top Global Matches:** file_cluster_12: 7.143, file_cluster_7: 7.674, file_cluster_5: 9.236
- **Magnitude:** 1775.4 | **LOC:** 2234 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 0.071; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.9%), Connectivity (formerly Api Exposure) (82.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `abbwelcome_action` **(Many-Argument Workhorses)** (Impact: 12.2)
  * `validate_rc_switch_code` **(Defensive Guards)** (Impact: 12.1)
  * `validate_rc_switch_raw_code` **(Defensive Guards)** (Impact: 12.1)
  * `validate_raw_alternating` **(Defensive Guards)** (Impact: 9.1)
    * *Intent:* # Raw
  * `raw_action` **(Compute Cores)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 135 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 838
* *State Mutation (weighted view):* 292
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 416`, `args: 177`, `func_start: 177`
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 222`
* *Architecture:* `api: 177`, `concurrency: 163`, `import: 8`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000273
  * `Imports (Out-Degree: 10):` esphome, esphome.codegen, esphome.components, esphome.config_validation, esphome.const, esphome.core, esphome.schema_extractors, esphome.util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `esphome/dashboard/web_server.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.234)
- **Top Global Matches:** file_cluster_5: 6.234, file_cluster_12: 8.095, file_cluster_0: 9.714
- **Magnitude:** 1517.72 | **LOC:** 1638 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 85.7%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **61**; blast radius 0.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%)
- **Documentation Coverage:** 74.4048% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_cache_arguments` **(Many-Argument Workhorses)** (Impact: 39.2)
  * `get` **(Many-Argument Workhorses)** (Impact: 29.6)
    * *Intent:* """Download a binary file."""
  * `post` **(Compute Cores)** (Impact: 21.1)
  * `get` **(Compute Cores)** (Impact: 21.1)
    * *Intent:* # filter all ESP32 variants by requested platform if platform.startswith("esp32"): from esphome.comp...
  * `make_app` **(Compute Cores)** (Impact: 19.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 45 instances
* *Amplified Cascading Flux:* 159 instances
* *Concurrency (weighted view):* 295
* *State Mutation (weighted view):* 539
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 408`, `args: 95`, `func_start: 93`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 37`, `high_risk_execution: 1`, `state_mutation: 221`
* *Architecture:* `io: 18`, `api: 113`, `concurrency: 70`, `import: 66`
* *Defense:* `safety: 29`, `doc: 39`, `sync_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000273
  * `Imports (Out-Degree: 18):` ..helpers, .const, .core, .entries, .models, .util.subprocess, .util.text, __future__...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `esphome/const.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.91)
- **Top Global Matches:** file_cluster_2: 2.91, file_cluster_17: 5.354, file_cluster_15: 6.31
- **Magnitude:** 1492.46 | **LOC:** 1410 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 43.9%
- **Blast Radius:** changing it is visible to **1027** in-repo importer(s); it depends on **2**; blast radius 17.037; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.7%), Complexity Load (formerly Cognitive Load) (48.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 1447
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 11`, `args: 1`, `class_start: 4`
* *Risk/State:* `state_mutation: 1315`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.037
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.137125
  * `Imports (Out-Degree: 1):` enum, esphome.enum
  * `Imported By (In-Degree: 1027):` (Excluded from Brief to save tokens)

### `esphome/components/web_server/web_server.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.995)
- **Top Global Matches:** file_cluster_12: 7.995, file_cluster_4: 8.588, file_cluster_15: 9.49
- **Magnitude:** 1490.26 | **LOC:** 2535 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 89.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.0%), Mutation Surface (formerly State Flux) (97.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WebServer::handleRequest` **(Compute Cores)** (Impact: 80.2)
  * `WebServer::climate_json_` **(Many-Argument Workhorses)** (Impact: 58.9)
  * `WebServer::canHandle` **(Compute Cores)** (Impact: 55.1)
    * *Intent:* #endif
  * `match_url` **(Many-Argument Workhorses)** (Impact: 53.2)
    * *Intent:* #define PSTR_LOCAL(mode_s) ESPHOME_strncpy_P(buf, (ESPHOME_PGM_P) ((mode_s)), PSTR_LOCAL_SIZE - 1) /...
  * `WebServer::handle_fan_request` **(Compute Cores)** (Impact: 38.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 292
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 474`, `structural_boundaries: 468`, `args: 216`, `func_start: 146`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 116`, `dead_code: 2`, `unreferenced_by_name: 136`
* *Architecture:* `io: 99`, `import: 21`
* *Defense:* `sync_locks: 23`, `immutability_locks: 108`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` StreamString.h, cstdlib, climate.h, infrared.h, json_util.h, light_json_schema.h, logger.h, util.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/api/api_connection.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.246)
- **Top Global Matches:** file_cluster_15: 6.246, file_cluster_11: 8.282, file_cluster_16: 8.311
- **Magnitude:** 1432.78 | **LOC:** 2421 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 85.4%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (99.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `APIConnection::try_send_climate_state` **(Many-Argument Workhorses)** (Impact: 31.7)
  * `APIConnection::dispatch_message_` **(Many-Argument Workhorses)** (Impact: 30.1)
    * *Intent:* // Dispatch message encoding based on message_type // Switch assigns function pointer, single call s...
  * `APIConnection::on_serial_proxy_request` **(Compute Cores)** (Impact: 28.7)
  * `APIConnection::process_batch_multi_` **(Many-Argument Workhorses)** (Impact: 28.7)
    * *Intent:* // Separated from process_batch_() so the single-message fast path gets a minimal // stack frame wit...
  * `APIConnection::on_alarm_control_panel_command_request` **(Compute Cores)** (Impact: 24.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 124 instances
* *State Mutation (weighted view):* 550
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 323`, `args: 204`, `func_start: 170`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 302`, `planned_debt: 3`, `unreferenced_by_name: 168`
* *Architecture:* `io: 8`, `import: 25`
* *Defense:* `safety: 9`, `sync_locks: 11`, `immutability_locks: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.000864
  * `Imports (Out-Degree: 25):` api_connection.h, api_frame_helper_noise.h, api_frame_helper_plaintext.h, cerrno, cinttypes, bluetooth_proxy.h, climate_mode.h, deep_sleep_component.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `esphome/__main__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.125)
- **Top Global Matches:** file_cluster_4: 7.125, file_cluster_12: 9.513, file_cluster_0: 10.271
- **Magnitude:** 1428.32 | **LOC:** 1935 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **43**; blast radius 0.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.7%)
- **Documentation Coverage:** 76.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `choose_upload_log_host` **(Many-Argument Workhorses)** (Impact: 119.8)
  * `parse_args` **(I/O & Config Routines)** (Impact: 48.3)
  * `command_rename` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `upload_using_esptool` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `upload_program` **(Many-Argument Workhorses)** (Impact: 32.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 188 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 607
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 306`, `structural_boundaries: 348`, `args: 62`, `func_start: 62`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 2`, `state_mutation: 231`
* *Architecture:* `io: 22`, `api: 57`, `concurrency: 2`, `import: 64`
* *Defense:* `safety: 38`, `doc: 21`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.087
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000669
  * `Imports (Out-Degree: 24):` aioesphomeapi, argcomplete, argparse, click, collections.abc, contextlib, datetime, esphome...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `esphome/config.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.162)
- **Top Global Matches:** file_cluster_4: 9.162, file_cluster_5: 9.432, file_cluster_12: 9.892
- **Magnitude:** 1407.8 | **LOC:** 1381 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 62.5%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **31**; blast radius 0.431; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%), Connectivity (formerly Api Exposure) (69.6%)
- **Documentation Coverage:** 91.1504% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Compute Cores)** (Impact: 105.6)
  * `dump_dict` **(Many-Argument Workhorses)** (Impact: 70.3)
  * `run` **(Many-Argument Workhorses)** (Impact: 51.1)
  * `validate_config` **(Many-Argument Workhorses)** (Impact: 30.2)
  * `resolve_extend_remove` **(Defensive Guards)** (Impact: 30.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 189 instances
* *State Mutation (weighted view):* 615
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 305`, `structural_boundaries: 280`, `args: 68`, `func_start: 67`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 237`, `duplicate_logic: 6`
* *Architecture:* `api: 59`, `import: 32`
* *Defense:* `safety: 82`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.431
  * `Choke Point (Betweenness):` 0.000126 | `Ripple Effect (Closeness):` 0.047546
  * `Imports (Out-Degree: 20):` __future__, abc, contextlib, contextvars, difflib, esphome, esphome.components.external_components, esphome.components.packages...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `esphome/components/haier/hon_climate.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.902)
- **Top Global Matches:** file_cluster_4: 6.902, file_cluster_6: 7.796, file_cluster_15: 14.066
- **Magnitude:** 1378.32 | **LOC:** 1383 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 71.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HonClimate::process_status_message_` **(Many-Argument Workhorses)** (Impact: 168.9)
    * *Intent:* #endif // USE_SWITCH
  * `HonClimate::process_phase` **(Compute Cores)** (Impact: 98.6)
  * `HonClimate::fill_control_messages_queue_` **(I/O & Config Routines)** (Impact: 81.6)
  * `HonClimate::get_control_message` **(I/O & Config Routines)** (Impact: 76.9)
  * `HonClimate::status_handler_` **(Many-Argument Workhorses)** (Impact: 54.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 197 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 630
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 419`, `structural_boundaries: 80`, `args: 103`, `func_start: 41`
* *Risk/State:* `state_mutation: 236`, `unreferenced_by_name: 41`
* *Architecture:* `import: 7`
* *Defense:* `safety: 1`, `immutability_locks: 44`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` chrono, climate.h, uart.h, helpers.h, hon_climate.h, hon_packet.h, string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/thermostat/thermostat_climate.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.755)
- **Top Global Matches:** file_cluster_4: 6.755, file_cluster_15: 8.53, file_cluster_11: 9.609
- **Magnitude:** 1361.76 | **LOC:** 1683 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Complexity Load (formerly Cognitive Load) (91.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ThermostatClimate::compute_action_` **(Compute Cores)** (Impact: 78.9)
  * `ThermostatClimate::switch_to_action_` **(Many-Argument Workhorses)** (Impact: 75.1)
  * `ThermostatClimate::switch_to_fan_mode_` **(Compute Cores)** (Impact: 52.0)
  * `ThermostatClimate::call_timer_callback_` **(Compute Cores)** (Impact: 37.2)
  * `ThermostatClimate::dump_config` **(I/O & Config Routines)** (Impact: 37.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 124 instances
* *State Mutation (weighted view):* 429
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 485`, `structural_boundaries: 227`, `args: 131`, `func_start: 156`
* *Risk/State:* `state_mutation: 181`, `dead_code: 15`, `fragile_debt: 1`, `unreferenced_by_name: 152`
* *Architecture:* `import: 5`
* *Defense:* `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` cinttypes, application.h, helpers.h, log.h, thermostat_climate.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/dashboard/test_web_server.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.835)
- **Top Global Matches:** file_cluster_0: 7.835, file_cluster_13: 9.542, file_cluster_15: 10.159
- **Magnitude:** 1349.28 | **LOC:** 1827 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (40.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.7%), Complexity Load (formerly Cognitive Load) (25.0%)
- **Documentation Coverage:** 60.625% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetch` **(Generic / Templated Code)** (Impact: 6.4)
    * *Intent:* """Get a response for the given path."""
  * `test_dashboard_yaml_loading_with_packages_and_secrets` **(I/O & Config Routines)** (Impact: 6.1)
  * `test_download_binary_handler_compressed` **(Defensive Guards)** (Impact: 5.5)
  * `test_archive_handler_with_build_folder` **(Many-Argument Workhorses)** (Impact: 5.0)
  * `test_download_binary_handler_path_traversal_protection` **(Many-Argument Workhorses)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 97 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 671
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 453`, `args: 81`, `func_start: 81`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 319`, `fragile_debt: 2`, `unreferenced_by_name: 67`
* *Architecture:* `io: 3`, `api: 80`, `concurrency: 186`, `import: 33`
* *Defense:* `safety: 169`, `doc: 77`, `test: 254`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` .common, __future__, argparse, asyncio, base64, collections.abc, contextlib, esphome...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/unit_tests/test_main.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.491)
- **Top Global Matches:** file_cluster_12: 8.491, file_cluster_5: 8.558, file_cluster_0: 8.834
- **Magnitude:** 1338.14 | **LOC:** 3887 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 56.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.0%), Guard Balance (formerly Safety Score) (43.9%), Connectivity (formerly Api Exposure) (12.1%), Complexity Load (formerly Cognitive Load) (11.5%)
- **Documentation Coverage:** 50.3012% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_setup_build_info_test` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `setup_core` **(Many-Argument Workhorses)** (Impact: 13.9)
  * `read` **(Compute Cores)** (Impact: 11.8)
    * *Intent:* """Read up to size bytes from the current chunk. This method respects the size argument and keeps an...
  * `test_run_esphome_multiple_configs_with_secrets` **(Many-Argument Workhorses)** (Impact: 9.8)
  * `test_command_rename_success` **(Many-Argument Workhorses)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 47 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 621
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 639`, `args: 168`, `func_start: 168`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 2`, `state_mutation: 527`, `fragile_debt: 1`, `unreferenced_by_name: 138`
* *Architecture:* `io: 4`, `api: 167`, `import: 22`
* *Defense:* `safety: 276`, `doc: 179`, `test: 477`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` __future__, collections.abc, dataclasses, esphome, esphome.__main__, esphome.components.esp32, esphome.const, esphome.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/waveshare_epaper/waveshare_epaper.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 9.061)
- **Top Global Matches:** file_cluster_15: 9.061, file_cluster_11: 9.324, file_cluster_16: 10.097
- **Magnitude:** 1295.38 | **LOC:** 4775 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.076; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.2%), Mutation Surface (formerly State Flux) (94.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WaveshareEPaperTypeA::display` **(I/O & Config Routines)** (Impact: 68.1)
  * `WaveshareEPaperTypeA::dump_config` **(Compute Cores)** (Impact: 24.0)
  * `WaveshareEPaperBWR::draw_absolute_pixel_internal` **(Compute Cores)** (Impact: 23.1)
  * `WaveshareEPaper7C::color_to_hex` **(Compute Cores)** (Impact: 22.8)
  * `WaveshareEPaper7C::draw_absolute_pixel_internal` **(Many-Argument Workhorses)** (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 128 instances
* *State Mutation (weighted view):* 408
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 337`, `structural_boundaries: 306`, `args: 177`, `func_start: 255`
* *Risk/State:* `state_mutation: 152`, `dead_code: 6`, `unreferenced_by_name: 255`
* *Architecture:* `import: 6`
* *Defense:* `immutability_locks: 92`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000182
  * `Imports (Out-Degree: 6):` bitset, cinttypes, application.h, helpers.h, log.h, waveshare_epaper.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `script/build_language_schema.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.262)
- **Top Global Matches:** file_cluster_6: 8.262, file_cluster_4: 11.211, file_cluster_8: 16.996
- **Magnitude:** 1285.54 | **LOC:** 1093 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.2%), Complexity Load (formerly Cognitive Load) (76.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.7%)
- **Documentation Coverage:** 90.2439% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convert` **(Many-Argument Workhorses)** (Impact: 136.1)
    * *Intent:* """config_var can be a config_var or a schema: both are dicts config_var has a S_TYPE property, if t...
  * `convert_keys` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `add_referenced_recursive` **(Many-Argument Workhorses)** (Impact: 38.2)
  * `shrink` **(I/O & Config Routines)** (Impact: 35.4)
    * *Intent:* """Shrink the extending schemas which has just an end type, e.g. at this point ota / port is type sc...
  * `build_schema` **(I/O & Config Routines)** (Impact: 32.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 234 instances
* *State Mutation (weighted view):* 744
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 149`, `args: 45`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 276`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 38`, `import: 24`
* *Defense:* `safety: 33`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` an, argparse, esphome, esphome.components, esphome.components.adc, esphome.components.esp32.boards, esphome.components.esp8266.boards, esphome.components.globals...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/esp32/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.089)
- **Top Global Matches:** file_cluster_4: 6.089, file_cluster_6: 10.259, file_cluster_12: 11.99
- **Magnitude:** 1190.28 | **LOC:** 2292 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 51.4%
- **Blast Radius:** changing it is visible to **78** in-repo importer(s); it depends on **25**; blast radius 3.075; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (94.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.2%)
- **Documentation Coverage:** 40.9639% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_code` **(I/O & Config Routines)** (Impact: 137.7)
  * `final_validate` **(Compute Cores)** (Impact: 45.4)
    * *Intent:* # Imported locally to avoid circular import issues from esphome.components.psram import DOMAIN as PS...
  * `_check_versions` **(Compute Cores)** (Impact: 31.6)
  * `_validate_partition` **(Stateful Encapsulated Methods)** (Impact: 30.3)
  * `set_core_data` **(Compute Cores)** (Impact: 28.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 148 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 559
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 170`, `args: 54`, `func_start: 54`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 263`, `planned_debt: 7`
* *Architecture:* `io: 5`, `api: 31`, `concurrency: 5`, `import: 25`
* *Defense:* `safety: 18`, `doc: 34`, `test: 5`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.075
  * `Choke Point (Betweenness):` 0.000549 | `Ripple Effect (Closeness):` 0.082719
  * `Imports (Out-Degree: 16):` .boards, .const, .gpio, contextlib, dataclasses, esphome, esphome.codegen, esphome.components.psram...
  * `Imported By (In-Degree: 78):` (Excluded from Brief to save tokens)

### `esphome/components/display/display.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.652)
- **Top Global Matches:** file_cluster_4: 5.652, file_cluster_15: 8.793, file_cluster_16: 10.322
- **Magnitude:** 1164.22 | **LOC:** 932 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **6**; blast radius 0.254; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.9%), Complexity Load (formerly Cognitive Load) (93.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Display::filled_gauge` **(Many-Argument Workhorses)** (Impact: 102.4)
  * `Display::filled_flat_side_triangle_` **(Many-Argument Workhorses)** (Impact: 63.5)
  * `Display::get_text_bounds` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* #endif // USE_GRAPHICAL_DISPLAY_MENU
  * `Display::draw_pixels_at` **(Many-Argument Workhorses)** (Impact: 50.1)
  * `Display::image` **(Many-Argument Workhorses)** (Impact: 46.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 140 instances
* *State Mutation (weighted view):* 432
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 106`, `args: 80`, `func_start: 74`
* *Risk/State:* `state_mutation: 152`, `unreferenced_by_name: 50`
* *Architecture:* `import: 6`
* *Defense:* `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.254
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.002914
  * `Imports (Out-Degree: 6):` display.h, display_color_utils.h, hal.h, log.h, numbers, utility
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `esphome/components/toshiba/toshiba.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.402)
- **Top Global Matches:** file_cluster_8: 9.402, file_cluster_3: 16.722, file_cluster_6: 20.965
- **Magnitude:** 1149.9 | **LOC:** 1377 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.2%), Complexity Load (formerly Cognitive Load) (74.7%)
- **Documentation Coverage:** 73.6842% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ToshibaClimate::on_receive` **(Compute Cores)** (Impact: 142.7)
  * `ToshibaClimate::transmit_rac_pt1411hwru_` **(I/O & Config Routines)** (Impact: 51.1)
  * `ToshibaClimate::transmit_ras_2819t_` **(I/O & Config Routines)** (Impact: 45.1)
  * `ToshibaClimate::process_ras_2819t_command_` **(Compute Cores)** (Impact: 40.9)
  * `is_valid_ras_2819t_command` **(Compute Cores)** (Impact: 35.5)
    * *Intent:* /** * Validate RAS-2819T IR command structure and content */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 199 instances
* *State Mutation (weighted view):* 620
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 81`, `args: 44`, `func_start: 19`, `class_start: 3`
* *Risk/State:* `state_mutation: 222`, `unreferenced_by_name: 13`
* *Architecture:* `import: 4`
* *Defense:* `doc: 6`, `immutability_locks: 112`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` toshiba_ac_protocol.h, helpers.h, toshiba.h, vector
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/analyze_memory/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.843)
- **Top Global Matches:** file_cluster_4: 9.843, file_cluster_6: 10.402, file_cluster_5: 14.443
- **Magnitude:** 1119.86 | **LOC:** 1464 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **13**; blast radius 0.225; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.6%)
- **Documentation Coverage:** 21.7391% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_identify_component` **(Many-Argument Workhorses)** (Impact: 52.4)
    * *Intent:* """Identify which component a symbol belongs to."""
  * `_parse_map_file` **(Stateful Encapsulated Methods)** (Impact: 33.6)
    * *Intent:* """Parse linker map file to build authoritative symbol-to-library mapping. The linker map file conta...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 30.3)
  * `_source_file_to_component` **(Stateful Encapsulated Methods)** (Impact: 29.9)
    * *Intent:* """Map a source object file path to its component name. Args: source_file: Relative path like 'src/e...
  * `_parse_nm_source_output` **(Many-Argument Workhorses)** (Impact: 27.1)
    * *Intent:* """Parse nm output to map non-namespaced symbols to ESPHome components. Extracts global defined symb...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 177 instances
* *State Mutation (weighted view):* 552
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 169`, `args: 39`, `func_start: 35`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 20`, `high_risk_execution: 2`, `state_mutation: 198`
* *Architecture:* `io: 1`, `api: 13`, `import: 13`
* *Defense:* `safety: 11`, `doc: 40`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.225
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000855
  * `Imports (Out-Degree: 6):` .cli, .const, .demangle, .helpers, .toolchain, collections, dataclasses, esphome.platformio_api...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `esphome/components/sprinkler/sprinkler.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.511)
- **Top Global Matches:** file_cluster_15: 6.511, file_cluster_11: 7.79, file_cluster_4: 8.436
- **Magnitude:** 1093.9 | **LOC:** 1660 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 71.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Sprinkler::load_next_valve_run_request_` **(Compute Cores)** (Impact: 29.1)
  * `Sprinkler::pump_in_use` **(Compute Cores)** (Impact: 28.7)
  * `Sprinkler::fsm_transition_from_valve_run_` **(I/O & Config Routines)** (Impact: 19.5)
  * `Sprinkler::next_valve_number_` **(Compute Cores)** (Impact: 19.1)
  * `Sprinkler::previous_valve_number_` **(Compute Cores)** (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 96 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 349
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 367`, `structural_boundaries: 276`, `args: 116`, `func_start: 150`
* *Risk/State:* `state_mutation: 157`, `dead_code: 2`, `unreferenced_by_name: 144`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 42`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` automation.h, cinttypes, application.h, helpers.h, log.h, progmem.h, sprinkler.h, utility
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esphome/components/wifi/wifi_component.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.474)
- **Top Global Matches:** file_cluster_4: 6.474, file_cluster_15: 10.13, file_cluster_11: 11.134
- **Magnitude:** 1092.46 | **LOC:** 2488 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 85.3%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **23**; blast radius 0.095; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (93.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 92.5234% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WiFiComponent::loop` **(I/O & Config Routines)** (Impact: 61.4)
  * `WiFiComponent::check_connecting_finished` **(Compute Cores)** (Impact: 43.6)
  * `WiFiComponent::transition_to_phase_` **(Compute Cores)** (Impact: 37.3)
    * *Intent:* /// Transition from current retry phase to a new phase with logging and phase-specific setup /// Thi...
  * `WiFiComponent::determine_next_phase_` **(I/O & Config Routines)** (Impact: 34.5)
    * *Intent:* /// Determine the next retry phase based on current state and failure conditions /// This function e...
  * `WiFiComponent::start_connecting` **(Compute Cores)** (Impact: 31.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 99 instances
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 413`, `structural_boundaries: 238`, `args: 178`, `func_start: 105`
* *Risk/State:* `state_mutation: 147`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 84`
* *Architecture:* `import: 23`
* *Defense:* `safety: 9`, `doc: 290`, `sync_locks: 1`, `immutability_locks: 103`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.095
  * `Choke Point (Betweenness):` 3.7e-05 | `Ripple Effect (Closeness):` 0.002143
  * `Imports (Out-Degree: 12):` algorithm, cassert, cinttypes, cmath, esp_eap_client.h, esp_wifi.h, esp_wpa2.h, captive_portal.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `esphome/core/helpers.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.421)
- **Top Global Matches:** file_cluster_15: 6.421, file_cluster_4: 7.758, file_cluster_16: 8.415
- **Magnitude:** 1071.68 | **LOC:** 895 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 81.8%
- **Blast Radius:** changing it is visible to **70** in-repo importer(s); it depends on **14**; blast radius 1.033; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.4%)
- **Documentation Coverage:** 98.0952% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hsv_to_rgb` **(Many-Argument Workhorses)** (Impact: 52.3)
  * `crc16` **(Many-Argument Workhorses)** (Impact: 44.3)
  * `crc16be` **(Many-Argument Workhorses)** (Impact: 36.0)
  * `format_hex_pretty_to` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `format_hex_internal` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* // Internal helper for hex formatting - base is 'a' for lowercase or 'A' for uppercase
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 464
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 116`, `args: 79`, `func_start: 72`
* *Risk/State:* `state_mutation: 164`
* *Architecture:* `api: 33`, `import: 14`
* *Defense:* `safety: 4`, `doc: 4`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.033
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.08069
  * `Imports (Out-Degree: 6):` algorithm, cctype, cmath, cstdarg, cstdio, cstring, defines.h, hal.h...
  * `Imported By (In-Degree: 70):` (Excluded from Brief to save tokens)

### `esphome/cpp_generator.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.8)
- **Top Global Matches:** file_cluster_0: 7.8, file_cluster_12: 9.285, file_cluster_5: 9.332
- **Magnitude:** 1046.98 | **LOC:** 1151 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 63.6%
- **Blast Radius:** changing it is visible to **260** in-repo importer(s); it depends on **13**; blast radius 16.604; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 81.7352% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_lambda` **(Many-Argument Workhorses)** (Impact: 41.0)
  * `safe_exp` **(Defensive Guards)** (Impact: 30.6)
    * *Intent:* """Try to convert obj to an expression by automatically converting native python types to expression...
  * `templatable` **(Many-Argument Workhorses)** (Impact: 17.3)
  * `Pvariable` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* """Declare a new pointer variable in the code generation. :param id_: The ID used to declare the var...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 11.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 109 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 422
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 373`, `args: 139`, `func_start: 139`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 204`, `planned_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `api: 106`, `concurrency: 11`, `import: 14`
* *Defense:* `safety: 42`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.604
  * `Choke Point (Betweenness):` 7.8e-05 | `Ripple Effect (Closeness):` 0.092035
  * `Imports (Out-Degree: 7):` abc, collections.abc, esphome.components.globals, esphome.core, esphome.cpp_types, esphome.helpers, esphome.types, esphome.util...
  * `Imported By (In-Degree: 260):` (Excluded from Brief to save tokens)

### `esphome/components/wifi/wifi_component_esp_idf.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.444)
- **Top Global Matches:** file_cluster_6: 6.444, file_cluster_4: 11.109, file_cluster_8: 14.794
- **Magnitude:** 1033.4 | **LOC:** 1227 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 71.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.2%), Debt Markers (formerly Tech Debt) (82.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WiFiComponent::wifi_process_event_` **(Compute Cores)** (Impact: 177.3)
    * *Intent:* // Events are processed from queue in main loop context, but listener notifications // must be defer...
  * `event_handler` **(Compute Cores)** (Impact: 114.5)
    * *Intent:* // general design: event handler translates events and pushes them to a queue, // events get process...
  * `get_disconnect_reason_str` **(Compute Cores)** (Impact: 63.9)
  * `WiFiComponent::wifi_sta_connect_` **(Compute Cores)** (Impact: 62.7)
    * *Intent:* #endif
  * `WiFiComponent::wifi_mode_` **(Compute Cores)** (Impact: 58.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 121 instances
* *State Mutation (weighted view):* 377
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 155`, `args: 112`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 135`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 26`
* *Architecture:* `import: 25`
* *Defense:* `safety: 3`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` algorithm, cinttypes, dhcpserver.h, esp_eap_client.h, esp_event.h, esp_netif.h, esp_system.h, esp_wifi.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `esphome/components/event/automation.h` (CPP) | Magnitude: 6.48 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 7, pointers: 6, indent_spaces: 5, args: 4
- `esphome/components/duty_time/duty_time_sensor.h` (CPP) | Magnitude: 28.08 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 38, indent_spaces: 29, pointers: 18, args: 10
- `esphome/components/hlk_fm22x/hlk_fm22x.h` (CPP) | Magnitude: 62.38 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 74, core_var_decl: 48, pointers: 46
- `tests/integration/test_light_initial_state.py` (PYTHON) | Magnitude: 27.62 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 15, test: 7, safety: 5
- `esphome/components/mapping/mapping.h` (CPP) | Magnitude: 24.88 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 18, args: 14, pointers: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `esphome/components/ade7880/ade7880.cpp` (CPP) | Magnitude: 82.0 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 243, indent_spaces: 225, args: 70, structural_boundaries: 59
- `esphome/components/output/button/output_button.cpp` (CPP) | Magnitude: 2.8 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: pointers: 8, structural_boundaries: 4, indent_spaces: 4, args: 2
- `esphome/components/zigbee/time/zigbee_time_zephyr.cpp` (CPP) | Magnitude: 51.28 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 48, pointers: 29, args: 18, branch: 15
- `esphome/components/copy/text_sensor/copy_text_sensor.cpp` (CPP) | Magnitude: 3.56 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: pointers: 7, structural_boundaries: 4, immutability_locks: 3, indent_spaces: 3
- `esphome/components/binary_sensor/automation.cpp` (CPP) | Magnitude: 71.98 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 86, pointers: 68, args: 29, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `esphome/components/deep_sleep/deep_sleep_bk72xx.cpp` (CPP) | Magnitude: 28.1 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 34, pointers: 23, branch: 14, structural_boundaries: 7
- `esphome/components/template/number/template_number.cpp` (CPP) | Magnitude: 30.26 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 30, pointers: 23, branch: 10, structural_boundaries: 9
- `esphome/components/epaper_spi/epaper_waveshare.cpp` (CPP) | Magnitude: 26.64 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 37, indent_spaces: 31, state_mutation: 6, branch: 5
- `esphome/components/aic3204/aic3204.cpp` (CPP) | Magnitude: 33.58 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 71, pointers: 55, args: 45, structural_boundaries: 15
- `esphome/components/alarm_control_panel/alarm_control_panel_call.cpp` (CPP) | Magnitude: 51.92 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 72, indent_spaces: 58, structural_boundaries: 22, branch: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/integration/test_uart_mock_ld2410.py` (PYTHON) | Magnitude: 129.18 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 181, structural_boundaries: 53, safety: 37, test: 33
- `docker/ha-addon-rootfs/etc/cont-init.d/30-esphome-fork.sh` (SHELL) | Magnitude: 3.2 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 20, io: 9, branch: 8
- `esphome/helpers.py` (PYTHON) | Magnitude: 448.86 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 324, structural_boundaries: 167, core_var_decl: 84, branch: 77
- `esphome/platformio_api.py` (PYTHON) | Magnitude: 361.38 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 296, structural_boundaries: 89, branch: 85, state_mutation: 60
- `tests/integration/test_host_mode_entity_fields.py` (PYTHON) | Magnitude: 60.78 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 19, state_mutation: 8, concurrency: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/integration/test_object_id_friendly_name_no_mac_suffix.py` (PYTHON) | Magnitude: 48.62 | Delta: **0.144** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 25, safety: 10, core_var_decl: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `script/integration_test` (SHELL) | Magnitude: 5.62 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 3, io: 2, branch: 1, safety: 1
- `tests/testing_helpers.py` (PYTHON) | Magnitude: 22.74 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 13, generics: 9, args: 6
- `esphome/components/lvgl/widgets/obj.py` (PYTHON) | Magnitude: 8.92 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 6, api: 3, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `esphome/components/api/api_connection.h` (CPP) | Magnitude: 174.2 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 405, pointers: 318, structural_boundaries: 184, args: 162
- `esphome/components/midea/ir_transmitter.h` (CPP) | Magnitude: 37.9 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 21, pointers: 21, func_start: 13
- `esphome/components/hmc5883l/sensor.py` (PYTHON) | Magnitude: 131.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 96, core_var_decl: 37, design_snake_case: 28, state_mutation: 27
- `esphome/components/as5600/sensor/as5600_sensor.h` (CPP) | Magnitude: 21.3 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 15, pointers: 14, structural_boundaries: 11, api: 7
- `esphome/components/pn7150/pn7150.h` (CPP) | Magnitude: 37.58 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 182, structural_boundaries: 56, pointers: 54, immutability_locks: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `esphome/components/sgp4x/sensor.py` (PYTHON) | Magnitude: 104.22 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 112, core_var_decl: 32, design_snake_case: 24, state_mutation: 21
- `esphome/components/factory_reset/__init__.py` (PYTHON) | Magnitude: 58.12 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 22, state_mutation: 12, core_var_decl: 12
- `esphome/components/web_server_base/__init__.py` (PYTHON) | Magnitude: 41.36 | Delta: **0.163** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 24, import: 8, branch: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `esphome/components/adc/adc_sensor_rp2040.cpp` (CPP) | Magnitude: 34.5 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 51, pointers: 13, branch: 11, core_var_decl: 11
- `esphome/components/nextion/nextion_component.h` (CPP) | Magnitude: 6.2 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 12, args: 7, class_start: 3
- `esphome/components/speaker/media_player/automation.h` (CPP) | Magnitude: 2.98 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 6, pointers: 5, args: 3
- `esphome/components/demo/demo_text_sensor.h` (CPP) | Magnitude: 6.92 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 10, branch: 4, structural_boundaries: 4, import: 3
- `esphome/core/progmem.h` (CPP) | Magnitude: 26.94 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 48, macros: 24, structural_boundaries: 22, reflection_metaprogramming: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `esphome/components/kamstrup_kmp/sensor.py` (PYTHON) | Magnitude: 68.78 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 98, core_var_decl: 49, design_snake_case: 38, state_mutation: 19
- `esphome/components/as7341/sensor.py` (PYTHON) | Magnitude: 61.8 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, core_var_decl: 31, state_mutation: 26, design_upper_case: 19
- `esphome/components/qmp6988/sensor.py` (PYTHON) | Magnitude: 64.92 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 73, core_var_decl: 27, design_snake_case: 20, state_mutation: 17
- `esphome/components/gps/__init__.py` (PYTHON) | Magnitude: 61.5 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 85, core_var_decl: 47, design_snake_case: 30, state_mutation: 23
- `esphome/components/dfrobot_sen0395/commands.h` (CPP) | Magnitude: 66.7 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 72, args: 21, structural_boundaries: 18, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `esphome/components/speaker_source/speaker_source_media_player.cpp` (CPP) | Magnitude: 715.98 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 602, pointers: 258, branch: 238, state_mutation: 86
- `esphome/components/ssd1306_base/ssd1306_base.cpp` (CPP) | Magnitude: 144.36 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 208, pointers: 148, branch: 73, args: 38
- `esphome/components/dfplayer/dfplayer.cpp` (CPP) | Magnitude: 229.14 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 205, branch: 76, pointers: 74, args: 56
- `esphome/components/esp32_ble_server/ble_characteristic.cpp` (CPP) | Magnitude: 285.54 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 228, pointers: 173, branch: 75, state_mutation: 42
- `script/ci_memory_impact_comment.py` (PYTHON) | Magnitude: 495.1 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 426, core_var_decl: 178, design_snake_case: 155, state_mutation: 115

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `esphome/analyze_memory/ram_strings.py` (PYTHON) | Magnitude: 458.16 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 301, state_mutation: 115, core_var_decl: 77, branch: 76
- `esphome/components/media_player/automation.h` (CPP) | Magnitude: 31.64 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 113, generics: 32, pointers: 30, indent_spaces: 30
- `tests/integration/test_udp.py` (PYTHON) | Magnitude: 260.22 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 54, concurrency: 34, core_var_decl: 30
- `tests/component_tests/psram/test_psram.py` (PYTHON) | Magnitude: 43.72 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 144, structural_boundaries: 28, core_var_decl: 24, design_snake_case: 21
- `esphome/components/lock/automation.h` (CPP) | Magnitude: 23.74 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 25, indent_spaces: 21, pointers: 20, sync_locks: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `esphome/components/seeed_mr60fda2/seeed_mr60fda2.cpp` (CPP) | Magnitude: 304.5 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 254, pointers: 138, branch: 78, state_mutation: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `esphome/components/socket/bsd_sockets_impl.h` (CPP) | Magnitude: 73.14 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 68, pointers: 57, structural_boundaries: 46, args: 30
- `esphome/components/openthread/openthread.h` (CPP) | Magnitude: 24.72 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 31, pointers: 30, immutability_locks: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `esphome/components/mopeka_std_check/sensor.py` (PYTHON) | Magnitude: 97.78 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 92, core_var_decl: 38, design_snake_case: 27, state_mutation: 21
- `esphome/components/bl0906/sensor.py` (PYTHON) | Magnitude: 175.06 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 151, core_var_decl: 63, design_snake_case: 56, state_mutation: 30
- `esphome/components/ble_client/sensor/automation.h` (CPP) | Magnitude: 31.0 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 19, pointers: 17, branch: 10, structural_boundaries: 4
- `esphome/components/sps30/sensor.py` (PYTHON) | Magnitude: 168.88 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 149, core_var_decl: 70, design_snake_case: 59, structural_boundaries: 28
- `tests/integration/fixtures/external_components/scheduler_bulk_cleanup_component/scheduler_bulk_cleanup_component.cpp` (CPP) | Magnitude: 0.03 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 39, args: 15, core_var_decl: 10, design_snake_case: 9

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `esphome/components/api/api_connection.cpp` -> Churn: **99.51%** | Cog Load: 72.7631% | Debt: 99.9944%
- `esphome/components/esp32/__init__.py` -> Churn: **94.27%** | Cog Load: 68.2282% | Debt: 9.2361%
- `esphome/components/wifi/wifi_component.cpp` -> Churn: **93.64%** | Cog Load: 35.6796% | Debt: 99.6754%
- `esphome/core/helpers.h` -> Churn: **93.64%** | Cog Load: 30.6923% | Debt: 99.6599%
- `esphome/components/wifi/wifi_component.h` -> Churn: **88.22%** | Cog Load: 3.4206% | Debt: 84.8368%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `script/api_protobuf/api_protobuf.py` -> **J. Nick Koston** (90.3% isolated ownership) | Magnitude: 2513.88
- `esphome/dashboard/web_server.py` -> **J. Nick Koston** (85.7% isolated ownership) | Magnitude: 1517.72
- `esphome/components/web_server/web_server.cpp` -> **J. Nick Koston** (89.5% isolated ownership) | Magnitude: 1490.26
- `esphome/components/api/api_connection.cpp` -> **J. Nick Koston** (85.4% isolated ownership) | Magnitude: 1432.78
- `tests/dashboard/test_web_server.py` -> **J. Nick Koston** (100.0% isolated ownership) | Magnitude: 1349.28

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `esphome/core/application.h` -> **Severity: 0.173** (Bridge: 0.0036 * Flux: 48.1746%)
- `esphome/core/component.cpp` -> **Severity: 0.083** (Bridge: 0.0024 * Flux: 35.2298%)
- `esphome/config_validation.py` -> **Severity: 0.074** (Bridge: 0.0007 * Flux: 100.0%)
- `esphome/components/esp32/__init__.py` -> **Severity: 0.055** (Bridge: 0.0005 * Flux: 100.0%)
- `esphome/core/entity_base.cpp` -> **Severity: 0.045** (Bridge: 0.0005 * Flux: 97.5683%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `esphome/const.py` -> **Severity: 12.286** (Embedded: 0.1371 * Error Risk: 89.5985%)
- `esphome/core/helpers.h` -> **Severity: 10.027** (Embedded: 0.1698 * Error Risk: 59.066%)
- `esphome/core/log.h` -> **Severity: 9.08** (Embedded: 0.1826 * Error Risk: 49.7297%)
- `esphome/core/component.h` -> **Severity: 9.07** (Embedded: 0.1755 * Error Risk: 51.6772%)
- `esphome/config_validation.py` -> **Severity: 8.489** (Embedded: 0.1294 * Error Risk: 65.6021%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `esphome/core/__init__.py` -> **Severity: 1549.275** (Blast Radius: 17.025 * Doc Risk: 91.0%)
- `esphome/core/hal.h` -> **Severity: 1513.7** (Blast Radius: 15.137 * Doc Risk: 100.0%)
- `esphome/core/helpers.h` -> **Severity: 1393.422** (Blast Radius: 32.583 * Doc Risk: 42.7653%)
- `esphome/cpp_generator.py` -> **Severity: 1357.131** (Blast Radius: 16.604 * Doc Risk: 81.7352%)
- `esphome/core/component.h` -> **Severity: 1194.665** (Blast Radius: 26.88 * Doc Risk: 44.4444%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 673 literal sites + 1 sites through wrappers = 674
- **`memory_alloc`:** 328 literal sites + 2 sites through wrappers = 330
- **`panics_and_aborts`:** 1338 literal sites + 14 sites through wrappers = 1352

- `_extract_tz_string` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `esphome/components/time/__init__.py`
- `_validate_load_certificate` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `esphome/components/wifi/wpa2_eap.py`
- `load_image` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `esphome/components/ili9xxx/display.py`
- `RingBuffer` (function, memory_alloc, primitive): 1 call sites in 1 files -- `esphome/components/usb_uart/usb_uart.h`
- `_exit` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `tests/unit_tests/test_vscode.py`
- `_load_yaml_internal` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `esphome/yaml_util.py`
- `_read_file_content_from_json_on_stdin` (function, debug_prints, primitive): 1 call sites in 1 files -- `esphome/vscode.py`
- `angle_to_position` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `esphome/components/as5600/__init__.py`
- `assign_from_initializer_list_` (function, memory_alloc, primitive): 1 call sites in 1 files -- `esphome/core/helpers.h`
- `ipaddress` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `esphome/config_validation.py`
- `ipv4address` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `esphome/config_validation.py`
- `smpmgr_upload` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `esphome/components/nrf52/ota.py`
*(+2 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 86867 call pairs -- scoped 22.6%, unique 1.5%, ambiguous 28.2%, external 47.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 46999 | 26.5% | 2.7% | 38.6% | 32.2% |
| python | 39607 | 18.1% | 0.0% | 16.1% | 65.8% |
| javascript | 165 | 17.6% | 0.0% | 0.0% | 82.4% |
| c | 69 | 11.6% | 0.0% | 0.0% | 88.4% |
| shell | 27 | 0.0% | 0.0% | 0.0% | 100.0% |

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
