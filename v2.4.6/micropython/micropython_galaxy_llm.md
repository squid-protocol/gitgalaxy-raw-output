# ARCHITECTURAL_BRIEF: micropython
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/micropython` |
| **Timestamp** | `2026-08-03T21:06:29.286130+00:00` |
| **Scan Duration** | `25.34s` |
| **Git Branch** | `master` |
| **Git Commit** | `2dc2e30d98ee225070e990586526f8e43b3c95a2` |
| **Git Remote** | `https://github.com/micropython/micropython` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4155 malicious artifacts.

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
| Total Artifacts | 6501 |
| Analyzed Artifacts (Scanned) | 4796 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1705 |
| Total LOC | 317610 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 73.8% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5628 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1373 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.8949 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 162 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 1997 | 217392 | 41.6% |
| PYTHON | 1701 | 58552 | 35.5% |
| CSV | 256 | 17771 | 5.3% |
| MAKEFILE | 240 | 7246 | 5.0% |
| JSON | 213 | 4406 | 4.4% |
| EMBEDDED_PYTHON | 150 | 7460 | 3.1% |
| MARKDOWN | 129 | 0 | 2.7% |
| JAVASCRIPT | 45 | 1566 | 0.9% |
| ASSEMBLY | 19 | 1151 | 0.4% |
| SHELL | 18 | 1631 | 0.4% |
| PLAINTEXT | 13 | 0 | 0.3% |
| XML | 9 | 0 | 0.2% |
| CPP | 2 | 71 | 0.0% |
| YAML | 2 | 37 | 0.0% |
| PROTO | 1 | 326 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.367`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 3497 | 72.9% |
| file_cluster_13 | 865 | 18.0% |
| file_cluster_9 | 161 | 3.4% |
| file_cluster_4 | 55 | 1.1% |
| file_cluster_17 | 31 | 0.6% |
| file_cluster_0 | 18 | 0.4% |
| file_cluster_12 | 8 | 0.2% |
| file_cluster_11 | 7 | 0.1% |
| file_cluster_16 | 3 | 0.1% |
| file_cluster_6 | 3 | 0.1% |
| file_cluster_7 | 2 | 0.0% |
| file_cluster_2 | 2 | 0.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 143 | 3.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1705*

**Composition by Extension & Reason:**
- `.exp`: 611x Excluded (Unsupported Extension: '.exp'), 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Unsupported Format (.exp)
- `.rst`: 241x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 81x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Excluded (Machine-Generated Source Code Signature: 6 LOC), 7x Excluded (Machine-Generated Source Code Signature: 63 LOC)
- `.c`: 127x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 4808 LOC), 1x Excluded (Machine-Generated Source Code Signature: 525 LOC)
- `.cmake`: 125x Excluded (Unsupported Extension: '.cmake')
- `.ld`: 115x Excluded (Unsupported Extension: '.ld')
- `.py`: 43x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 153 LOC), 1x Excluded (Saturation: Line 4 exceeds 500 chars)
- `no_extension`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.p4_wifi_common')
- `.yml`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.conf`: 28x Excluded (Unsupported Extension: '.conf')
- `.board`: 26x Excluded (Unsupported Extension: '.board')
- `.jpg`: 14x Excluded (Explicitly Denied Extension: '.jpg')
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.overlay`: 8x Excluded (Unsupported Extension: '.overlay')
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 107 LOC), 1x Excluded (Machine-Generated Source Code Signature: 268 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 19.1 | 5.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 16.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.8 | 1.4 | 0.0 |
| API Exposure | 0.0 | 18.3 | 3.9 | 1.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 23.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 91.7 | 0.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 81.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 42.6 | 0.9 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.3 | 11.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 98.9 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `extmod/network_ninaw10.c` (Hits: 113)
- `tests/ports/cc3200/pin.py` (Hits: 110)
- `extmod/modlwip.c` (Hits: 67)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **runtime.h** (`py/runtime.h`) — 473 inbound connections
2. **mphal.h** (`py/mphal.h`) — 410 inbound connections
3. **obj.h** (`py/obj.h`) — 189 inbound connections
4. **mperrno.h** (`py/mperrno.h`) — 169 inbound connections
5. **modmachine.h** (`extmod/modmachine.h`) — 90 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **stm32u5xx_hal_conf_base.h** (`ports/stm32/boards/stm32u5xx_hal_conf_base.h`) — 64 outbound dependencies
2. **stm32n6xx_hal_conf_base.h** (`ports/stm32/boards/stm32n6xx_hal_conf_base.h`) — 59 outbound dependencies
3. **main.c** (`ports/stm32/main.c`) — 56 outbound dependencies
4. **mptask.c** (`ports/cc3200/mptask.c`) — 44 outbound dependencies
5. **deprecated_definitions.h** (`ports/cc3200/FreeRTOS/Source/include/deprecated_definitions.h`) — 44 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run_micropython` (@ `tests/run-tests.py`) -> Impact: **3067.6** | LOC: 653
- `raise_exc` (@ `py/parsenum.c`) -> Impact: **1817.1** | LOC: 342
  * *Intent:* * This file is part of the MicroPython project, http://micropython.org/ * * The MIT License (MIT) * * Copyright (c) 2013, 2014 Damien P. George * * Pe...
- `do_filesystem_tree` (@ `tools/mpremote/mpremote/commands.py`) -> Impact: **1532.2** | LOC: 403
  * *Intent:* """Print a tree of the device's filesystem starting at path."""
- `freeze` (@ `tools/mpy-tool.py`) -> Impact: **1281.0** | LOC: 644
- `calculate_brp` (@ `extmod/machine_can.c`) -> Impact: **1028.2** | LOC: 457
  * *Intent:* #endif #if MICROPY_HW_ENABLE_FDCAN // CAN-FD BRS (Baud Rate Switch) default limits #ifndef CAN_FD_BRS_TSEG1_MIN #define CAN_FD_BRS_TSEG1_MIN 1 #endif ...
- `next_cell` (@ `tests/perf_bench/bm_hexiom.py`) -> Impact: **1018.2** | LOC: 205
- `USBD_CDC_MSC_HID_Init` (@ `ports/stm32/usbdev/class/src/usbd_cdc_msc_hid.c`) -> Impact: **923.8** | LOC: 415
  * *Intent:* #endif #endif #if MICROPY_HW_USB_CDC_NUM >= 2
- `run_feature_test` (@ `tests/run-perfbench.py`) -> Impact: **782.7** | LOC: 274
- `emit_inline_thumb_op` (@ `py/emitinlinethumb.c`) -> Impact: **752.0** | LOC: 411
- `uart_rx_char` (@ `ports/stm32/uart.c`) -> Impact: **749.7** | LOC: 248

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `USBD_CDC_MSC_HID_Init` (@ `ports/stm32/usbdev/class/src/usbd_cdc_msc_hid.c`) -> **O(2^N) [Recursive]**
  * *Intent:* #endif #endif #if MICROPY_HW_USB_CDC_NUM >= 2
- `raise_exc` (@ `py/parsenum.c`) -> **O(2^N) [Recursive]**
  * *Intent:* * This file is part of the MicroPython project, http://micropython.org/ * * The MIT License (MIT) * * Copyright (c) 2013, 2014 Damien P. George * * Pe...
- `print_header` (@ `ports/nrf/boards/make-pins.py`) -> **O(2^N) [Recursive]**
- `get_details` (@ `ports/stm32/boards/NUCLEO_WB55/rfcore_makefirmware.py`) -> **O(2^N) [Recursive]**
- `print_adc_externs` (@ `ports/stm32/boards/make-pins.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Print externs for the adc pin tables.
- `wait_empty_response` (@ `ports/stm32/mboot/mboot.py`) -> **O(2^N) [Recursive]**
- `_save_data` (@ `ports/stm32/mboot/mboot_pack_dfu.py`) -> **O(2^N) [Recursive]**
- `test_one` (@ `tests/net_inet/test_tls_nonblock.py`) -> **O(2^N) [Recursive]**
- `next_cell` (@ `tests/perf_bench/bm_hexiom.py`) -> **O(2^N) [Recursive]**
- `run_micropython` (@ `tests/run-tests.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `ci_code_size_build` (@ `tools/ci.sh`) -> DB Complexity: **199**
- `SystemClock_Config` (@ `ports/stm32/system_stm32.c`) -> DB Complexity: **196**
  * *Intent:* /* * This file is part of the MicroPython project, http://micropython.org/ * * Taken from ST Cube library and modified. See below for original header....
- `BOARD_BootClockRUN` (@ `ports/mimxrt/boards/MIMXRT1176_clock_config.c`) -> DB Complexity: **174**
  * *Intent:* /******************************************************************************* ********************** Configuration BOARD_BootClockRUN *************...
- `uart_init` (@ `ports/stm32/uart.c`) -> DB Complexity: **169**
- `mp_prof_opcode_decode` (@ `py/profile.c`) -> DB Complexity: **166**
  * *Intent:* /******************************************************************************/ // DEBUG // This section is for debugging the settrace feature itself...
- `mpz_set_from_bytes` (@ `py/mpz.c`) -> DB Complexity: **134**
- `Anonymous_Block_[Truncated]` (@ `tools/mpremote/tests/test_filesystem.sh`) -> DB Complexity: **128**
- `run_micropython` (@ `tests/run-tests.py`) -> DB Complexity: **124**
- `emit_inline_thumb_op` (@ `py/emitinlinethumb.c`) -> DB Complexity: **119**
- `bluetooth_gatts_register_service` (@ `extmod/modbluetooth.c`) -> DB Complexity: **118**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `py` | 206 | 67167.74 | 48.98% | 23.5% |
| `ports/stm32` | 161 | 43550.65 | 37.32% | 27.38% |
| `extmod` | 90 | 23699.59 | 49.69% | 14.37% |
| `ports/esp32` | 74 | 12646.52 | 40.79% | 29.43% |
| `tests/basics` | 568 | 11447.8 | 7.45% | 0.0% |
| `ports/mimxrt` | 68 | 9414.22 | 38.49% | 39.13% |
| `ports/renesas-ra` | 78 | 9065.04 | 36.87% | 32.84% |
| `tests/extmod` | 199 | 8873.06 | 13.78% | 0.0% |
| `tests` | 7 | 6413.14 | 14.87% | 0.0% |
| `ports/cc3200/hal` | 45 | 6252.24 | 14.96% | 42.75% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `extmod/mpbthci.c` -> **100.0%** Exposure
- `extmod/virtpin.c` -> **100.0%** Exposure
- `ports/alif/fatfs_port.c` -> **100.0%** Exposure
- `ports/alif/machine_i2c_target.c` -> **100.0%** Exposure
- `ports/alif/mbedtls/mbedtls_port.c` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `drivers/bus/qspi.h` -> **100.0%** Exposure
- `drivers/bus/softqspi.c` -> **100.0%** Exposure
- `drivers/bus/softspi.c` -> **100.0%** Exposure
- `drivers/cc3100/src/fs.c` -> **100.0%** Exposure
- `drivers/cc3100/src/netcfg.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `py/asmx86.c` -> **41** Orphaned Functions | **0** Duplicates
- `ports/cc3200/hal/uart.c` -> **33** Orphaned Functions | **0** Duplicates
- `py/asmx64.c` -> **32** Orphaned Functions | **0** Duplicates
- `drivers/ninaw10/nina_wifi_drv.c` -> **30** Orphaned Functions | **0** Duplicates
- `py/asmarm.c` -> **29** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`extmod/modos.c`** -> AI Confidence: **99.48%**
2. **`extmod/network_lwip.c`** -> AI Confidence: **99.48%**
3. **`extmod/os_dupterm.c`** -> AI Confidence: **99.48%**
4. **`ports/cc3200/fatfs/src/drivers/sd_diskio.c`** -> AI Confidence: **99.48%**
5. **`ports/cc3200/mods/modssl.c`** -> AI Confidence: **99.48%**
6. **`ports/esp32/machine_touchpad.c`** -> AI Confidence: **99.48%**
7. **`ports/esp32/modesp32.c`** -> AI Confidence: **99.48%**
8. **`ports/esp32/mpconfigport.h`** -> AI Confidence: **99.48%**
9. **`ports/esp32/network_common.c`** -> AI Confidence: **99.48%**
10. **`ports/esp32/network_lan.c`** -> AI Confidence: **99.48%**
11. **`ports/nrf/modules/board/modboard.c`** -> AI Confidence: **99.48%**
12. **`ports/renesas-ra/ra/ra_icu.c`** -> AI Confidence: **99.48%**
13. **`ports/rp2/main.c`** -> AI Confidence: **99.48%**
14. **`ports/samd/machine_spi.c`** -> AI Confidence: **99.48%**
15. **`ports/stm32/adc.c`** -> AI Confidence: **99.48%**
16. **`ports/stm32/extint.c`** -> AI Confidence: **99.48%**
17. **`ports/stm32/flash.c`** -> AI Confidence: **99.48%**
18. **`ports/stm32/lcd.c`** -> AI Confidence: **99.48%**
19. **`ports/stm32/main.c`** -> AI Confidence: **99.48%**
20. **`ports/stm32/modstm.c`** -> AI Confidence: **99.48%**
21. **`ports/stm32/powerctrl.c`** -> AI Confidence: **99.48%**
22. **`ports/stm32/pyb_can.c`** -> AI Confidence: **99.48%**
23. **`ports/stm32/pyb_i2c.c`** -> AI Confidence: **99.48%**
24. **`ports/stm32/systick.c`** -> AI Confidence: **99.48%**
25. **`ports/stm32/timer.c`** -> AI Confidence: **99.48%**
26. **`ports/stm32/uart.c`** -> AI Confidence: **99.48%**
27. **`ports/unix/input.c`** -> AI Confidence: **99.48%**
28. **`py/asmthumb.c`** -> AI Confidence: **99.48%**
29. **`py/binary.c`** -> AI Confidence: **99.48%**
30. **`py/compile.c`** -> AI Confidence: **99.48%**
31. **`py/emitglue.c`** -> AI Confidence: **99.48%**
32. **`py/emitinlinethumb.c`** -> AI Confidence: **99.48%**
33. **`py/modstruct.c`** -> AI Confidence: **99.48%**
34. **`py/modsys.c`** -> AI Confidence: **99.48%**
35. **`py/mpprint.c`** -> AI Confidence: **99.48%**
36. **`py/objstr.c`** -> AI Confidence: **99.48%**
37. **`py/parsenum.c`** -> AI Confidence: **99.48%**
38. **`py/vm.c`** -> AI Confidence: **99.48%**
39. **`shared/readline/readline.c`** -> AI Confidence: **99.48%**
40. **`ports/stm32/boards/stm32g0xx_hal_conf_base.h`** -> AI Confidence: **99.48%**
41. **`extmod/moddeflate.c`** -> AI Confidence: **99.44%**
42. **`extmod/modbinascii.c`** -> AI Confidence: **99.39%**
43. **`extmod/modselect.c`** -> AI Confidence: **99.39%**
44. **`mpy-cross/main.c`** -> AI Confidence: **99.39%**
45. **`ports/alif/machine_spi.c`** -> AI Confidence: **99.39%**
46. **`ports/cc3200/hal/crc.c`** -> AI Confidence: **99.39%**
47. **`ports/cc3200/hal/timer.c`** -> AI Confidence: **99.39%**
48. **`ports/esp32/modmachine.c`** -> AI Confidence: **99.39%**
49. **`ports/esp32/network_wlan.c`** -> AI Confidence: **99.39%**
50. **`ports/esp8266/machine_spi.c`** -> AI Confidence: **99.39%**
51. **`ports/mimxrt/network_lan.c`** -> AI Confidence: **99.39%**
52. **`ports/nrf/main.c`** -> AI Confidence: **99.39%**
53. **`ports/nrf/modules/machine/spi.c`** -> AI Confidence: **99.39%**
54. **`ports/renesas-ra/machine_spi.c`** -> AI Confidence: **99.39%**
55. **`ports/renesas-ra/main.c`** -> AI Confidence: **99.39%**
56. **`ports/renesas-ra/ra/ra_sci.c`** -> AI Confidence: **99.39%**
57. **`ports/rp2/clocks_extra.c`** -> AI Confidence: **99.39%**
58. **`ports/rp2/rp2_psram.c`** -> AI Confidence: **99.39%**
59. **`ports/stm32/dac.c`** -> AI Confidence: **99.39%**
60. **`ports/stm32/eth.c`** -> AI Confidence: **99.39%**
61. **`ports/stm32/modpyb.c`** -> AI Confidence: **99.39%**
62. **`ports/stm32/sdio.c`** -> AI Confidence: **99.39%**
63. **`ports/unix/mpconfigport.h`** -> AI Confidence: **99.39%**
64. **`py/formatfloat.c`** -> AI Confidence: **99.39%**
65. **`py/map.c`** -> AI Confidence: **99.39%**
66. **`py/objfloat.c`** -> AI Confidence: **99.39%**
67. **`py/objmodule.c`** -> AI Confidence: **99.39%**
68. **`py/persistentcode.c`** -> AI Confidence: **99.39%**
69. **`ports/renesas-ra/RA4M1_hal.h`** -> AI Confidence: **99.39%**
70. **`ports/renesas-ra/RA4W1_hal.h`** -> AI Confidence: **99.39%**
71. **`ports/renesas-ra/RA6M1_hal.h`** -> AI Confidence: **99.39%**
72. **`ports/renesas-ra/RA6M2_hal.h`** -> AI Confidence: **99.39%**
73. **`ports/renesas-ra/RA6M5_hal.h`** -> AI Confidence: **99.39%**
74. **`tests/run-tests.py`** -> AI Confidence: **99.39%**
75. **`tools/metrics.py`** -> AI Confidence: **99.39%**
76. **`ports/stm32/mboot/main.c`** -> AI Confidence: **99.35%**
77. **`ports/stm32/modmachine.c`** -> AI Confidence: **99.35%**
78. **`py/modbuiltins.c`** -> AI Confidence: **99.35%**
79. **`tools/mpremote/mpremote/commands.py`** -> AI Confidence: **99.35%**
80. **`drivers/dht/dht.c`** -> AI Confidence: **99.34%**
81. **`extmod/machine_can.c`** -> AI Confidence: **99.34%**
82. **`extmod/modjson.c`** -> AI Confidence: **99.34%**
83. **`extmod/modsocket.c`** -> AI Confidence: **99.34%**
84. **`extmod/modvfs.c`** -> AI Confidence: **99.34%**
85. **`ports/cc3200/hal/gpio.c`** -> AI Confidence: **99.34%**
86. **`ports/esp32/machine_i2c.c`** -> AI Confidence: **99.34%**
87. **`ports/qemu/main.c`** -> AI Confidence: **99.34%**
88. **`ports/renesas-ra/ra/ra_gpt.c`** -> AI Confidence: **99.34%**
89. **`ports/rp2/machine_spi.c`** -> AI Confidence: **99.34%**
90. **`ports/samd/boards/pins_prefix.c`** -> AI Confidence: **99.34%**
91. **`ports/stm32/machine_i2c.c`** -> AI Confidence: **99.34%**
92. **`ports/stm32/rtc.c`** -> AI Confidence: **99.34%**
93. **`ports/stm32/spi.c`** -> AI Confidence: **99.34%**
94. **`ports/stm32/usbd_desc.c`** -> AI Confidence: **99.34%**
95. **`ports/unix/modtermios.c`** -> AI Confidence: **99.34%**
96. **`py/objcomplex.c`** -> AI Confidence: **99.34%**
97. **`py/profile.c`** -> AI Confidence: **99.34%**
98. **`py/qstr.c`** -> AI Confidence: **99.34%**
99. **`py/repl.c`** -> AI Confidence: **99.34%**
100. **`ports/nrf/nrfx_glue.h`** -> AI Confidence: **99.34%**
101. **`py/emitnative.c`** -> AI Confidence: **99.33%**
102. **`extmod/machine_bitstream.c`** -> AI Confidence: **99.32%**
103. **`ports/cc3200/FreeRTOS/Source/portable/MemMang/heap_4.c`** -> AI Confidence: **99.32%**
104. **`ports/mimxrt/modmimxrt.c`** -> AI Confidence: **99.32%**
105. **`ports/nrf/modules/ubluepy/ubluepy_constants.c`** -> AI Confidence: **99.32%**
106. **`ports/renesas-ra/ra/ra_int.c`** -> AI Confidence: **99.32%**
107. **`ports/rp2/machine_adc.c`** -> AI Confidence: **99.32%**
108. **`ports/rp2/machine_bitstream.c`** -> AI Confidence: **99.32%**
109. **`ports/stm32/boards/WEACT_F411_BLACKPILL/bdev.c`** -> AI Confidence: **99.32%**
110. **`ports/stm32/mboot/sdcard.c`** -> AI Confidence: **99.32%**
111. **`ports/stm32/system_stm32.c`** -> AI Confidence: **99.32%**
112. **`ports/stm32/usbhost/Class/MSC/Src/usbh_msc.c`** -> AI Confidence: **99.32%**
113. **`ports/stm32/usbhost/Class/MSC/Src/usbh_msc_scsi.c`** -> AI Confidence: **99.32%**
114. **`ports/windows/realpath.c`** -> AI Confidence: **99.32%**
115. **`py/argcheck.c`** -> AI Confidence: **99.32%**
116. **`py/emitnarm.c`** -> AI Confidence: **99.32%**
117. **`py/emitnrv32.c`** -> AI Confidence: **99.32%**
118. **`py/emitnthumb.c`** -> AI Confidence: **99.32%**
119. **`py/emitnx64.c`** -> AI Confidence: **99.32%**
120. **`py/emitnxtensa.c`** -> AI Confidence: **99.32%**
121. **`py/emitnxtensawin.c`** -> AI Confidence: **99.32%**
122. **`py/objslice.c`** -> AI Confidence: **99.32%**
123. **`py/parsenumbase.c`** -> AI Confidence: **99.32%**
124. **`drivers/cc3100/inc/simplelink.h`** -> AI Confidence: **99.32%**
125. **`ports/nrf/nrfx_log.h`** -> AI Confidence: **99.32%**
126. **`ports/renesas-ra/mpconfigport.h`** -> AI Confidence: **99.32%**
127. **`ports/stm32/mpconfigport.h`** -> AI Confidence: **99.32%**
128. **`tests/float/float_format_accuracy.py`** -> AI Confidence: **99.32%**
129. **`tests/import/builtin_import.py`** -> AI Confidence: **99.32%**
130. **`tools/autobuild/remove_old_firmware.py`** -> AI Confidence: **99.32%**
131. **`drivers/esp-hosted/esp_hosted_wifi.c`** -> AI Confidence: **99.31%**
132. **`drivers/ninaw10/machine_pin_nina.c`** -> AI Confidence: **99.31%**
133. **`drivers/ninaw10/nina_wifi_bsp.c`** -> AI Confidence: **99.31%**
134. **`drivers/ninaw10/nina_wifi_drv.c`** -> AI Confidence: **99.31%**
135. **`extmod/machine_i2c.c`** -> AI Confidence: **99.31%**
136. **`extmod/mbedtls/mbedtls_alt.c`** -> AI Confidence: **99.31%**
137. **`extmod/modbluetooth.c`** -> AI Confidence: **99.31%**
138. **`extmod/modlwip.c`** -> AI Confidence: **99.31%**
139. **`extmod/modnetwork.c`** -> AI Confidence: **99.31%**
140. **`extmod/modopenamp.c`** -> AI Confidence: **99.31%**
141. **`extmod/modopenamp_remoteproc.c`** -> AI Confidence: **99.31%**
142. **`extmod/modtls_mbedtls.c`** -> AI Confidence: **99.31%**
143. **`extmod/moductypes.c`** -> AI Confidence: **99.31%**
144. **`extmod/modwebrepl.c`** -> AI Confidence: **99.31%**
145. **`extmod/network_cyw43.c`** -> AI Confidence: **99.31%**
146. **`extmod/network_esp_hosted.c`** -> AI Confidence: **99.31%**
147. **`extmod/network_ninaw10.c`** -> AI Confidence: **99.31%**
148. **`extmod/network_ppp_lwip.c`** -> AI Confidence: **99.31%**
149. **`extmod/network_wiznet5k.c`** -> AI Confidence: **99.31%**
150. **`extmod/nimble/hal/hal_uart.c`** -> AI Confidence: **99.31%**
151. **`extmod/nimble/modbluetooth_nimble.c`** -> AI Confidence: **99.31%**
152. **`extmod/vfs.c`** -> AI Confidence: **99.31%**
153. **`extmod/vfs_fat.c`** -> AI Confidence: **99.31%**
154. **`extmod/vfs_fat_diskio.c`** -> AI Confidence: **99.31%**
155. **`extmod/vfs_fat_file.c`** -> AI Confidence: **99.31%**
156. **`extmod/vfs_lfsx.c`** -> AI Confidence: **99.31%**
157. **`extmod/vfs_posix.c`** -> AI Confidence: **99.31%**
158. **`extmod/vfs_posix_file.c`** -> AI Confidence: **99.31%**
159. **`extmod/vfs_reader.c`** -> AI Confidence: **99.31%**
160. **`ports/alif/main.c`** -> AI Confidence: **99.31%**
161. **`ports/alif/mphalport.c`** -> AI Confidence: **99.31%**
162. **`ports/alif/tinyusb_port/tusb_alif_dcd.c`** -> AI Confidence: **99.31%**
163. **`ports/alif/vfs_rom_ioctl.c`** -> AI Confidence: **99.31%**
164. **`ports/cc3200/ftp/ftp.c`** -> AI Confidence: **99.31%**
165. **`ports/cc3200/hal/adc.c`** -> AI Confidence: **99.31%**
166. **`ports/cc3200/hal/aes.c`** -> AI Confidence: **99.31%**
167. **`ports/cc3200/hal/des.c`** -> AI Confidence: **99.31%**
168. **`ports/cc3200/hal/shamd5.c`** -> AI Confidence: **99.31%**
169. **`ports/cc3200/hal/spi.c`** -> AI Confidence: **99.31%**
170. **`ports/cc3200/main.c`** -> AI Confidence: **99.31%**
171. **`ports/cc3200/misc/antenna.c`** -> AI Confidence: **99.31%**
172. **`ports/cc3200/mods/modnetwork.c`** -> AI Confidence: **99.31%**
173. **`ports/cc3200/mods/modsocket.c`** -> AI Confidence: **99.31%**
174. **`ports/cc3200/mods/modwlan.c`** -> AI Confidence: **99.31%**
175. **`ports/cc3200/mods/pybpin.c`** -> AI Confidence: **99.31%**
176. **`ports/cc3200/mods/pybsd.c`** -> AI Confidence: **99.31%**
177. **`ports/cc3200/mods/pybspi.c`** -> AI Confidence: **99.31%**
178. **`ports/cc3200/mods/pybtimer.c`** -> AI Confidence: **99.31%**
179. **`ports/cc3200/mods/pybuart.c`** -> AI Confidence: **99.31%**
180. **`ports/cc3200/mptask.c`** -> AI Confidence: **99.31%**
181. **`ports/cc3200/simplelink/cc_pal.c`** -> AI Confidence: **99.31%**
182. **`ports/cc3200/telnet/telnet.c`** -> AI Confidence: **99.31%**
183. **`ports/esp32/boards/ARDUINO_NANO_ESP32/board_init.c`** -> AI Confidence: **99.31%**
184. **`ports/esp32/esp32_partition.c`** -> AI Confidence: **99.31%**
185. **`ports/esp32/esp32_rmt.c`** -> AI Confidence: **99.31%**
186. **`ports/esp32/gccollect.c`** -> AI Confidence: **99.31%**
187. **`ports/esp32/machine_bitstream.c`** -> AI Confidence: **99.31%**
188. **`ports/esp32/machine_hw_spi.c`** -> AI Confidence: **99.31%**
189. **`ports/esp32/machine_pin.c`** -> AI Confidence: **99.31%**
190. **`ports/esp32/machine_pwm.c`** -> AI Confidence: **99.31%**
191. **`ports/esp32/machine_rtc.c`** -> AI Confidence: **99.31%**
192. **`ports/esp32/machine_sdcard.c`** -> AI Confidence: **99.31%**
193. **`ports/esp32/machine_timer.c`** -> AI Confidence: **99.31%**
194. **`ports/esp32/machine_uart.c`** -> AI Confidence: **99.31%**
195. **`ports/esp32/main.c`** -> AI Confidence: **99.31%**
196. **`ports/esp32/modespnow.c`** -> AI Confidence: **99.31%**
197. **`ports/esp32/modsocket.c`** -> AI Confidence: **99.31%**
198. **`ports/esp32/mphalport.c`** -> AI Confidence: **99.31%**
199. **`ports/esp32/network_ppp.c`** -> AI Confidence: **99.31%**
200. **`ports/esp32/uart.c`** -> AI Confidence: **99.31%**
201. **`ports/esp32/usb_serial_jtag.c`** -> AI Confidence: **99.31%**
202. **`ports/esp8266/ets_alt_task.c`** -> AI Confidence: **99.31%**
203. **`ports/esp8266/machine_pin.c`** -> AI Confidence: **99.31%**
204. **`ports/esp8266/main.c`** -> AI Confidence: **99.31%**
205. **`ports/esp8266/modesp.c`** -> AI Confidence: **99.31%**
206. **`ports/esp8266/modespnow.c`** -> AI Confidence: **99.31%**
207. **`ports/esp8266/modmachine.c`** -> AI Confidence: **99.31%**
208. **`ports/esp8266/network_wlan.c`** -> AI Confidence: **99.31%**
209. **`ports/esp8266/uart.c`** -> AI Confidence: **99.31%**
210. **`ports/mimxrt/board_init.c`** -> AI Confidence: **99.31%**
211. **`ports/mimxrt/eth.c`** -> AI Confidence: **99.31%**
212. **`ports/mimxrt/machine_encoder.c`** -> AI Confidence: **99.31%**
213. **`ports/mimxrt/machine_i2c.c`** -> AI Confidence: **99.31%**
214. **`ports/mimxrt/machine_i2s.c`** -> AI Confidence: **99.31%**
215. **`ports/mimxrt/machine_pin.c`** -> AI Confidence: **99.31%**
216. **`ports/mimxrt/machine_sdcard.c`** -> AI Confidence: **99.31%**
217. **`ports/mimxrt/machine_spi.c`** -> AI Confidence: **99.31%**
218. **`ports/mimxrt/machine_uart.c`** -> AI Confidence: **99.31%**
219. **`ports/mimxrt/main.c`** -> AI Confidence: **99.31%**
220. **`ports/mimxrt/modmachine.c`** -> AI Confidence: **99.31%**
221. **`ports/mimxrt/mphalport.c`** -> AI Confidence: **99.31%**
222. **`ports/mimxrt/mpnetworkport.c`** -> AI Confidence: **99.31%**
223. **`ports/mimxrt/sdio.c`** -> AI Confidence: **99.31%**
224. **`ports/minimal/main.c`** -> AI Confidence: **99.31%**
225. **`ports/nrf/boards/MICROBIT/modules/microbitdisplay.c`** -> AI Confidence: **99.31%**
226. **`ports/nrf/drivers/bluetooth/ble_drv.c`** -> AI Confidence: **99.31%**
227. **`ports/nrf/drivers/bluetooth/ble_uart.c`** -> AI Confidence: **99.31%**
228. **`ports/nrf/drivers/softpwm.c`** -> AI Confidence: **99.31%**
229. **`ports/nrf/modules/machine/i2c.c`** -> AI Confidence: **99.31%**
230. **`ports/nrf/modules/machine/modmachine.c`** -> AI Confidence: **99.31%**
231. **`ports/nrf/modules/machine/pin.c`** -> AI Confidence: **99.31%**
232. **`ports/nrf/modules/machine/uart.c`** -> AI Confidence: **99.31%**
233. **`ports/nrf/modules/music/modmusic.c`** -> AI Confidence: **99.31%**
234. **`ports/nrf/modules/nrf/flashbdev.c`** -> AI Confidence: **99.31%**
235. **`ports/nrf/modules/os/microbitfs.c`** -> AI Confidence: **99.31%**
236. **`ports/nrf/mphalport.c`** -> AI Confidence: **99.31%**
237. **`ports/pic16bit/main.c`** -> AI Confidence: **99.31%**
238. **`ports/powerpc/main.c`** -> AI Confidence: **99.31%**
239. **`ports/renesas-ra/gccollect.c`** -> AI Confidence: **99.31%**
240. **`ports/renesas-ra/machine_dac.c`** -> AI Confidence: **99.31%**
241. **`ports/renesas-ra/machine_pin.c`** -> AI Confidence: **99.31%**
242. **`ports/renesas-ra/machine_rtc.c`** -> AI Confidence: **99.31%**
243. **`ports/renesas-ra/machine_sdcard.c`** -> AI Confidence: **99.31%**
244. **`ports/renesas-ra/machine_uart.c`** -> AI Confidence: **99.31%**
245. **`ports/renesas-ra/mphalport.c`** -> AI Confidence: **99.31%**
246. **`ports/renesas-ra/ra/ra_adc.c`** -> AI Confidence: **99.31%**
247. **`ports/renesas-ra/ra/ra_i2c.c`** -> AI Confidence: **99.31%**
248. **`ports/renesas-ra/ra/ra_rtc.c`** -> AI Confidence: **99.31%**
249. **`ports/renesas-ra/ra/ra_timer.c`** -> AI Confidence: **99.31%**
250. **`ports/renesas-ra/storage.c`** -> AI Confidence: **99.31%**
251. **`ports/renesas-ra/systick.c`** -> AI Confidence: **99.31%**
252. **`ports/renesas-ra/timer.c`** -> AI Confidence: **99.31%**
253. **`ports/rp2/machine_i2s.c`** -> AI Confidence: **99.31%**
254. **`ports/rp2/machine_pin.c`** -> AI Confidence: **99.31%**
255. **`ports/rp2/machine_pin_cyw43.c`** -> AI Confidence: **99.31%**
256. **`ports/rp2/machine_uart.c`** -> AI Confidence: **99.31%**
257. **`ports/rp2/modmachine.c`** -> AI Confidence: **99.31%**
258. **`ports/rp2/modrp2.c`** -> AI Confidence: **99.31%**
259. **`ports/rp2/mpconfigport.h`** -> AI Confidence: **99.31%**
260. **`ports/rp2/mphalport.c`** -> AI Confidence: **99.31%**
261. **`ports/rp2/rp2_dma.c`** -> AI Confidence: **99.31%**
262. **`ports/rp2/rp2_flash.c`** -> AI Confidence: **99.31%**
263. **`ports/rp2/rp2_pio.c`** -> AI Confidence: **99.31%**
264. **`ports/samd/machine_dac.c`** -> AI Confidence: **99.31%**
265. **`ports/samd/main.c`** -> AI Confidence: **99.31%**
266. **`ports/samd/mphalport.c`** -> AI Confidence: **99.31%**
267. **`ports/samd/pin_af.c`** -> AI Confidence: **99.31%**
268. **`ports/samd/samd_flash.c`** -> AI Confidence: **99.31%**
269. **`ports/samd/samd_qspiflash.c`** -> AI Confidence: **99.31%**
270. **`ports/samd/samd_spiflash.c`** -> AI Confidence: **99.31%**
271. **`ports/stm32/boardctrl.c`** -> AI Confidence: **99.31%**
272. **`ports/stm32/boards/LEGO_HUB_NO6/board_init.c`** -> AI Confidence: **99.31%**
273. **`ports/stm32/boards/LEGO_HUB_NO7/board_init.c`** -> AI Confidence: **99.31%**
274. **`ports/stm32/dma.c`** -> AI Confidence: **99.31%**
275. **`ports/stm32/factoryreset.c`** -> AI Confidence: **99.31%**
276. **`ports/stm32/machine_can.c`** -> AI Confidence: **99.31%**
277. **`ports/stm32/machine_uart.c`** -> AI Confidence: **99.31%**
278. **`ports/stm32/mphalport.c`** -> AI Confidence: **99.31%**
279. **`ports/stm32/mpnetworkport.c`** -> AI Confidence: **99.31%**
280. **`ports/stm32/qspi.c`** -> AI Confidence: **99.31%**
281. **`ports/stm32/sdcard.c`** -> AI Confidence: **99.31%**
282. **`ports/stm32/sdram.c`** -> AI Confidence: **99.31%**
283. **`ports/stm32/stm32_it.c`** -> AI Confidence: **99.31%**
284. **`ports/stm32/storage.c`** -> AI Confidence: **99.31%**
285. **`ports/stm32/usb.c`** -> AI Confidence: **99.31%**
286. **`ports/stm32/usbd_cdc_interface.c`** -> AI Confidence: **99.31%**
287. **`ports/stm32/vfs_rom_ioctl.c`** -> AI Confidence: **99.31%**
288. **`ports/unix/coverage.c`** -> AI Confidence: **99.31%**
289. **`ports/unix/main.c`** -> AI Confidence: **99.31%**
290. **`ports/unix/modjni.c`** -> AI Confidence: **99.31%**
291. **`ports/unix/modsocket.c`** -> AI Confidence: **99.31%**
292. **`ports/unix/modtime.c`** -> AI Confidence: **99.31%**
293. **`ports/unix/mphalport.h`** -> AI Confidence: **99.31%**
294. **`ports/unix/mpthreadport.c`** -> AI Confidence: **99.31%**
295. **`ports/unix/unix_mphal.c`** -> AI Confidence: **99.31%**
296. **`ports/zephyr/machine_adc.c`** -> AI Confidence: **99.31%**
297. **`ports/zephyr/machine_pin.c`** -> AI Confidence: **99.31%**
298. **`ports/zephyr/machine_timer.c`** -> AI Confidence: **99.31%**
299. **`ports/zephyr/main.c`** -> AI Confidence: **99.31%**
300. **`ports/zephyr/modsocket.c`** -> AI Confidence: **99.31%**
301. **`ports/zephyr/zephyr_filesystem.c`** -> AI Confidence: **99.31%**
302. **`py/asmrv32.c`** -> AI Confidence: **99.31%**
303. **`py/builtinimport.c`** -> AI Confidence: **99.31%**
304. **`py/emitbc.c`** -> AI Confidence: **99.31%**
305. **`py/emitinlinerv32.c`** -> AI Confidence: **99.31%**
306. **`py/emitinlinextensa.c`** -> AI Confidence: **99.31%**
307. **`py/malloc.c`** -> AI Confidence: **99.31%**
308. **`py/nativeglue.c`** -> AI Confidence: **99.31%**
309. **`py/obj.c`** -> AI Confidence: **99.31%**
310. **`py/objarray.c`** -> AI Confidence: **99.31%**
311. **`py/objexcept.c`** -> AI Confidence: **99.31%**
312. **`py/objfun.c`** -> AI Confidence: **99.31%**
313. **`py/objint.c`** -> AI Confidence: **99.31%**
314. **`py/objint_longlong.c`** -> AI Confidence: **99.31%**
315. **`py/objint_mpz.c`** -> AI Confidence: **99.31%**
316. **`py/parse.c`** -> AI Confidence: **99.31%**
317. **`py/runtime.c`** -> AI Confidence: **99.31%**
318. **`py/vstr.c`** -> AI Confidence: **99.31%**
319. **`shared/libc/printf.c`** -> AI Confidence: **99.31%**
320. **`shared/runtime/pyexec.c`** -> AI Confidence: **99.31%**
321. **`shared/tinyusb/mp_usbd_runtime.c`** -> AI Confidence: **99.31%**
322. **`examples/bluetooth/ble_bonding_peripheral.py`** -> AI Confidence: **99.31%**
323. **`ports/cc3200/tools/update-wipy.py`** -> AI Confidence: **99.31%**
324. **`ports/stm32/mboot/fwupdate.py`** -> AI Confidence: **99.31%**
325. **`py/makeqstrdefs.py`** -> AI Confidence: **99.31%**
326. **`tests/run-internalbench.py`** -> AI Confidence: **99.31%**
327. **`tests/run-multitests.py`** -> AI Confidence: **99.31%**
328. **`tests/run-natmodtests.py`** -> AI Confidence: **99.31%**
329. **`tools/manifestfile.py`** -> AI Confidence: **99.31%**
330. **`tools/mpremote/mpremote/mip.py`** -> AI Confidence: **99.31%**
331. **`tools/mpremote/mpremote/transport_serial.py`** -> AI Confidence: **99.31%**
332. **`tools/mpy-tool.py`** -> AI Confidence: **99.31%**
333. **`tools/mpy_ld.py`** -> AI Confidence: **99.31%**
334. **`tools/pydfu.py`** -> AI Confidence: **99.31%**
335. **`tools/uf2conv.py`** -> AI Confidence: **99.31%**
336. **`ports/esp8266/Makefile`** -> AI Confidence: **99.31%**
337. **`ports/samd/Makefile`** -> AI Confidence: **99.31%**
338. **`ports/stm32/Makefile`** -> AI Confidence: **99.31%**
339. **`examples/natmod/random/random.c`** -> AI Confidence: **99.29%**
340. **`extmod/machine_mem.c`** -> AI Confidence: **99.29%**
341. **`extmod/mpbthci.c`** -> AI Confidence: **99.29%**
342. **`ports/cc3200/FreeRTOS/Source/portable/GCC/ARM_CM3/port.c`** -> AI Confidence: **99.29%**
343. **`ports/esp32/help.c`** -> AI Confidence: **99.29%**
344. **`ports/esp32/machine_i2c.h`** -> AI Confidence: **99.29%**
345. **`ports/esp32/modnetwork_globals.h`** -> AI Confidence: **99.29%**
346. **`ports/esp8266/help.c`** -> AI Confidence: **99.29%**
347. **`ports/esp8266/machine_bitstream.c`** -> AI Confidence: **99.29%**
348. **`ports/esp8266/strtoll.c`** -> AI Confidence: **99.29%**
349. **`ports/mimxrt/hal/fsl_flexspi_nor_boot.c`** -> AI Confidence: **99.29%**
350. **`ports/mimxrt/hal/qspi_hyper_flash_config.c`** -> AI Confidence: **99.29%**
351. **`ports/mimxrt/hal/qspi_nor_flash_config.c`** -> AI Confidence: **99.29%**
352. **`ports/mimxrt/help.c`** -> AI Confidence: **99.29%**
353. **`ports/mimxrt/machine_bitstream.c`** -> AI Confidence: **99.29%**
354. **`ports/mimxrt/mimxrt_sdram.c`** -> AI Confidence: **99.29%**
355. **`ports/nrf/help.c`** -> AI Confidence: **99.29%**
356. **`ports/nrf/modules/ubluepy/modubluepy.c`** -> AI Confidence: **99.29%**
357. **`ports/renesas-ra/help.c`** -> AI Confidence: **99.29%**
358. **`ports/renesas-ra/irq.h`** -> AI Confidence: **99.29%**
359. **`ports/renesas-ra/machine_pwm.c`** -> AI Confidence: **99.29%**
360. **`ports/renesas-ra/ra/ra_gpio.c`** -> AI Confidence: **99.29%**
361. **`ports/rp2/help.c`** -> AI Confidence: **99.29%**
362. **`ports/samd/help.c`** -> AI Confidence: **99.29%**
363. **`ports/samd/mcu/samd21/clock_config.c`** -> AI Confidence: **99.29%**
364. **`ports/samd/mcu/samd51/clock_config.c`** -> AI Confidence: **99.29%**
365. **`ports/stm32/boards/ARDUINO_GIGA/bdev.c`** -> AI Confidence: **99.29%**
366. **`ports/stm32/boards/ARDUINO_NICLA_VISION/bdev.c`** -> AI Confidence: **99.29%**
367. **`ports/stm32/boards/ARDUINO_OPTA/bdev.c`** -> AI Confidence: **99.29%**
368. **`ports/stm32/boards/ARDUINO_PORTENTA_H7/bdev.c`** -> AI Confidence: **99.29%**
369. **`ports/stm32/boards/STM32F469DISC/bdev.c`** -> AI Confidence: **99.29%**
370. **`ports/stm32/boards/STM32H573I_DK/bdev.c`** -> AI Confidence: **99.29%**
371. **`ports/stm32/boards/stm32f4xx_prefix.c`** -> AI Confidence: **99.29%**
372. **`ports/stm32/help.c`** -> AI Confidence: **99.29%**
373. **`ports/stm32/i2cslave.c`** -> AI Confidence: **99.29%**
374. **`ports/stm32/machine_adc.c`** -> AI Confidence: **99.29%**
375. **`ports/stm32/mboot/adc.c`** -> AI Confidence: **99.29%**
376. **`ports/stm32/mboot/version.c`** -> AI Confidence: **99.29%**
377. **`ports/stm32/powerctrlboot.c`** -> AI Confidence: **99.29%**
378. **`ports/stm32/usbdev/class/src/usbd_cdc_msc_hid.c`** -> AI Confidence: **99.29%**
379. **`ports/stm32/usbdev/core/src/usbd_ctlreq.c`** -> AI Confidence: **99.29%**
380. **`ports/stm32/usbhost/Class/AUDIO/Src/usbh_audio.c`** -> AI Confidence: **99.29%**
381. **`ports/stm32/usbhost/Class/CDC/Src/usbh_cdc.c`** -> AI Confidence: **99.29%**
382. **`ports/stm32/usbhost/Class/MSC/Src/usbh_msc_bot.c`** -> AI Confidence: **99.29%**
383. **`ports/stm32/usbhost/Class/MTP/Src/usbh_mtp_ptp.c`** -> AI Confidence: **99.29%**
384. **`ports/stm32/usbhost/Core/Inc/usbh_conf_template.h`** -> AI Confidence: **99.29%**
385. **`ports/stm32/usbhost/Core/Src/usbh_core.c`** -> AI Confidence: **99.29%**
386. **`ports/stm32/usbhost/Core/Src/usbh_ctlreq.c`** -> AI Confidence: **99.29%**
387. **`ports/zephyr/help.c`** -> AI Confidence: **99.29%**
388. **`ports/zephyr/mpconfigport.h`** -> AI Confidence: **99.29%**
389. **`py/emitnx86.c`** -> AI Confidence: **99.29%**
390. **`py/modarray.c`** -> AI Confidence: **99.29%**
391. **`py/modcollections.c`** -> AI Confidence: **99.29%**
392. **`py/modstring.c`** -> AI Confidence: **99.29%**
393. **`py/mpstate.c`** -> AI Confidence: **99.29%**
394. **`py/nlrpowerpc.c`** -> AI Confidence: **99.29%**
395. **`py/nlrthumb.c`** -> AI Confidence: **99.29%**
396. **`py/nlrx64.c`** -> AI Confidence: **99.29%**
397. **`py/qstrdefs.h`** -> AI Confidence: **99.29%**
398. **`py/showbc.c`** -> AI Confidence: **99.29%**
399. **`py/smallint.c`** -> AI Confidence: **99.29%**
400. **`py/vmentrytable.h`** -> AI Confidence: **99.29%**
401. **`shared/netutils/trace.c`** -> AI Confidence: **99.29%**
402. **`shared/timeutils/timeutils.c`** -> AI Confidence: **99.29%**
403. **`extmod/littlefs-include/lfs2_defines.h`** -> AI Confidence: **99.29%**
404. **`ports/cc3200/FreeRTOS/Source/include/StackMacros.h`** -> AI Confidence: **99.29%**
405. **`ports/cc3200/hal/inc/asmdefs.h`** -> AI Confidence: **99.29%**
406. **`ports/esp8266/boards/ESP8266_GENERIC/mpconfigboard.h`** -> AI Confidence: **99.29%**
407. **`ports/mimxrt/boards/PHYBOARD_RT1170/mpconfigboard.h`** -> AI Confidence: **99.29%**
408. **`ports/nrf/boards/PARTICLE_XENON/mpconfigboard.h`** -> AI Confidence: **99.29%**
409. **`ports/nrf/boards/PCA10056/mpconfigboard.h`** -> AI Confidence: **99.29%**
410. **`ports/nrf/boards/PCA10059/mpconfigboard.h`** -> AI Confidence: **99.29%**
411. **`ports/nrf/modules/ble/help_sd.h`** -> AI Confidence: **99.29%**
412. **`ports/nrf/mpconfigport.h`** -> AI Confidence: **99.29%**
413. **`ports/renesas-ra/mpconfigboard_common.h`** -> AI Confidence: **99.29%**
414. **`ports/renesas-ra/qstrdefsport.h`** -> AI Confidence: **99.29%**
415. **`ports/samd/mcu/samd21/mpconfigmcu.h`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `tests/micropython/import_mpy_native.py` -> **98.8647%** Exposure
- `tests/extmod/websocket_basic.py` -> **4.0765%** Exposure
- `tests/extmod/vfs_rom.py` -> **1.5292%** Exposure
- `ports/cc3200/hal/inc/hw_mmchs.h` -> **0.0013%** Exposure
- `ports/cc3200/hal/timer.c` -> **0.0002%** Exposure
### Exploit Generation Surface
- `examples/rp2/pio_exec.py` -> **100.0%** Exposure
- `examples/rp2/pio_pwm.py` -> **100.0%** Exposure
- `ports/stm32/boards/NUCLEO_WB55/rfcore_firmware.py` -> **100.0%** Exposure
- `tests/ports/esp32/partition_ota.py` -> **100.0%** Exposure
- `examples/bluetooth/ble_simple_central.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `examples/rp2/pio_exec.py` -> **100.0%** Exposure
- `examples/rp2/pio_pwm.py` -> **100.0%** Exposure
- `tests/ports/esp32/partition_ota.py` -> **100.0%** Exposure
- `ports/cc3200/tools/uniflash.py` -> **100.0%** Exposure
- `ports/esp32/tools/metrics_esp32.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `extmod/modbluetooth.c` -> **10.0%** Exposure
- `extmod/modwebsocket.c` -> **10.0%** Exposure
- `extmod/network_cyw43.c` -> **10.0%** Exposure
- `extmod/nimble/modbluetooth_nimble.c` -> **10.0%** Exposure
- `extmod/vfs_fat.c` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `drivers/bus/qspi.h` -> **100.0%** Exposure
- `drivers/bus/softqspi.c` -> **100.0%** Exposure
- `drivers/bus/softspi.c` -> **100.0%** Exposure
- `drivers/cc3100/src/device.c` -> **100.0%** Exposure
- `drivers/cc3100/src/driver.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `17` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `9923` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `extmod/asyncio/event.py` (PYTHON) -> Cumulative Risk: **907.83**
- **Archetype:** `file_cluster_4` (Distance: 11.858 IQR)
- **Magnitude:** 87.66 | **LOC:** 67 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `ioctl` (Impact: 10.2), `wait` (Impact: 10.2), `set` (Impact: 7.3)

### 2. `ports/webassembly/asyncio/core.py` (PYTHON) -> Cumulative Risk: **900.24**
- **Archetype:** `file_cluster_13` (Distance: 11.875 IQR)
- **Magnitude:** 273.8 | **LOC:** 268 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_run_iter` (Impact: 100.8), `__next__` (Impact: 10.8), `wait` (Impact: 7.5)

### 3. `extmod/asyncio/core.py` (PYTHON) -> Cumulative Risk: **887.18**
- **Archetype:** `file_cluster_8` (Distance: 10.869 IQR)
- **Magnitude:** 413.36 | **LOC:** 325 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `run_until_complete` (Impact: 150.1), `wait_io_event` (Impact: 44.2), `remove` (Impact: 37.0)

### 4. `ports/unix/mpthreadport.c` (C) -> Cumulative Risk: **859.13**
- **Archetype:** `file_cluster_13` (Distance: 13.02 IQR)
- **Magnitude:** 294.02 | **LOC:** 411 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `mp_thread_gc_others` (Impact: 23.6), `mp_thread_finish` (Impact: 22.1), `mp_thread_start` (Impact: 20.8)

### 5. `ports/stm32/machine_can.c` (C) -> Cumulative Risk: **805.16**
- **Archetype:** `file_cluster_8` (Distance: 14.225 IQR)
- **Magnitude:** 630.22 | **LOC:** 490 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `machine_can_irq_handler` (Impact: 66.0), `machine_can_port_send` (Impact: 52.8), `machine_can_port_recv` (Impact: 26.5)

### 6. `extmod/asyncio/stream.py` (PYTHON) -> Cumulative Risk: **805.11**
- **Archetype:** `file_cluster_4` (Distance: 10.31 IQR)
- **Magnitude:** 357.36 | **LOC:** 223 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `_serve` (Impact: 55.2), `read` (Impact: 52.5), `readline` (Impact: 43.8)

### 7. `shared/libc/string0.c` (C) -> Cumulative Risk: **801.17**
- **Archetype:** `file_cluster_0` (Distance: 15.432 IQR)
- **Magnitude:** 610.94 | **LOC:** 262 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `strncmp` (Impact: 39.6), `memcpy` (Impact: 33.7), `memset` (Impact: 33.1)

### 8. `tools/ar_util.py` (PYTHON) -> Cumulative Risk: **799.91**
- **Archetype:** `file_cluster_13` (Distance: 10.833 IQR)
- **Magnitude:** 0.31 | **LOC:** 237 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `resolve` (Impact: 85.8), `load_symbols` (Impact: 49.9), `cached` (Impact: 25.6)

### 9. `tools/manifestfile.py` (PYTHON) -> Cumulative Risk: **795.5**
- **Archetype:** `file_cluster_13` (Distance: 12.01 IQR)
- **Magnitude:** 0.99 | **LOC:** 655 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `include` (Impact: 205.6), `require` (Impact: 144.5), `_search` (Impact: 127.5)

### 10. `ports/renesas-ra/ra/ra_gpio.c` (C) -> Cumulative Risk: **794.45**
- **Archetype:** `file_cluster_13` (Distance: 13.19 IQR)
- **Magnitude:** 313.3 | **LOC:** 186 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9997%)
- **Heaviest Functions:** `ra_gpio_config` (Impact: 67.5), `ra_gpio_get_mode` (Impact: 23.1), `ra_gpio_get_drive` (Impact: 23.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `ports/stm32/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.369 IQR)
- **Top Global Matches:** file_cluster_17: 12.369, file_cluster_8: 12.685, file_cluster_13: 12.83
- **Magnitude:** 9001.8 | **LOC:** 734 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (57.4596%), Tech Debt (19.8801%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 55`, `args: 48`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 236`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 9`, `api: 2`, `import: 10`
* *Defense:* `safety: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mkenv.mk, mkrules.mk, mpconfigvariant.mk, extmod.mk, stm32.mk, tinyusb.mk, mpconfigvariant_$(BOARD_VARIANT).mk, py.mk...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/emitnative.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.33%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.816 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.966 IQR)
- **Top Global Matches:** file_cluster_8: 12.816, file_cluster_0: 13.118, file_cluster_13: 13.147
- **Magnitude:** 8726.64 | **LOC:** 3123 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (53.487%), Tech Debt (11.8177%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 364`, `structural_boundaries: 133`, `args: 3`, `func_start: 87`
* *Risk/State:* `state_mutation: 455`, `dead_code: 10`, `planned_debt: 9`, `fragile_debt: 2`
* *Architecture:* `api: 123`, `import: 7`
* *Defense:* `safety: 33`, `test: 29`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.527
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` stdio.h, objstr.h, string.h, nativeglue.h, objfun.h, assert.h, emit.h
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `py/gc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.543 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.275 IQR)
- **Top Global Matches:** file_cluster_11: 14.543, file_cluster_13: 14.56, file_cluster_0: 14.578
- **Magnitude:** 8162.58 | **LOC:** 1408 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (82.1453%), Tech Debt (8.9548%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 76`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 419`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 77`, `import: 6`
* *Defense:* `safety: 43`, `test: 10`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` stdio.h, string.h, gc.h, memcheck.h, runtime.h, assert.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/usb.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.972 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.174 IQR)
- **Top Global Matches:** file_cluster_13: 12.972, file_cluster_8: 13.129, file_cluster_11: 13.286
- **Magnitude:** 3603.99 | **LOC:** 1162 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (78.6481%), Tech Debt (18.8308%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 42`, `args: 10`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `state_mutation: 188`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 65`, `import: 18`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` usbd_cdc_msc_hid.h, usbh_usr.h, objstr.h, string.h, storage.h, mphal.h, mperrno.h, usbd_msc_interface.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/run-tests.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.23 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.152 IQR)
- **Top Global Matches:** file_cluster_8: 11.23, file_cluster_13: 11.541, file_cluster_7: 11.722
- **Magnitude:** 3408.66 | **LOC:** 1366 | **CtrlFlow:** 73.8% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 124
- **Risk Profile:** Cognitive Load (19.793%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_micropython` (Impact: 3067.6 | O(2^N) | DB: 124)
  * `detect_target_wiring_script` (Impact: 71.0 | O(N^4) | DB: 9)
  * `detect_test_platform` (Impact: 54.3 | O(N^3))
    * *Intent:* # Run a script to detect various bits of information about the target test instance. output = run_fe...
  * `convert_regex_escapes` (Impact: 25.1 | O(N^3) | DB: 3)
    * *Intent:* # unescape wanted regex chars and escape unwanted ones
  * `__call__` (Impact: 20.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 101`, `args: 21`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 1`, `state_mutation: 82`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 67`, `api: 20`, `concurrency: 11`, `import: 17`
* *Defense:* `safety: 22`, `doc: 4`, `test: 8`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` json, test_utils, target_wiring, pty, subprocess, select, platform, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/renesas-ra/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.231 IQR)
- **Top Global Matches:** file_cluster_17: 12.231, file_cluster_8: 12.365, file_cluster_13: 12.596
- **Magnitude:** 3108.72 | **LOC:** 511 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (53.8094%), Tech Debt (11.3578%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 45`, `args: 14`, `func_start: 1`
* *Risk/State:* `state_mutation: 230`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 2`, `import: 6`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mkenv.mk, mkrules.mk, extmod.mk, py.mk, mpconfigport.mk, mpconfigboard.mk
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/uart.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.982 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.142 IQR)
- **Top Global Matches:** file_cluster_8: 13.982, file_cluster_13: 14.165, file_cluster_11: 14.314
- **Magnitude:** 2674.44 | **LOC:** 1387 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 169
- **Risk Profile:** Cognitive Load (86.1049%), Tech Debt (17.8422%)
**Top Internal Functions/Classes:**
  * `uart_rx_char` (Impact: 749.7 | O(N^6) | DB: 53)
  * `uart_init` (Impact: 439.5 | O(N^4) | DB: 169)
  * `uart_get_source_freq` (Impact: 161.5 | O(N^4) | DB: 31)
    * *Intent:* #else
  * `uart_exists` (Impact: 142.1 | O(N^3))
    * *Intent:* #elif defined(STM32N6) // UART clock configuration, IC14 (max 100MHz).
  * `uart_deinit` (Impact: 92.4 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 507`, `structural_boundaries: 102`, `args: 4`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 795`, `orphaned_logic: 11`
* *Architecture:* `api: 124`, `import: 12`
* *Defense:* `safety: 5`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` mpirq.h, uart.h, pendsv.h, mphal.h, stdio.h, irq.h, string.h, stdarg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/compile.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.352 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.922 IQR)
- **Top Global Matches:** file_cluster_11: 14.352, file_cluster_13: 14.406, file_cluster_0: 14.443
- **Magnitude:** 2557.42 | **LOC:** 3699 | **CtrlFlow:** 79.4% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (88.5804%), Tech Debt (39.6969%)
**Top Internal Functions/Classes:**
  * `scope_compute_things` (Impact: 217.0 | O(N^6) | DB: 46)
  * `compile_scope_inline_asm` (Impact: 215.2 | O(N^6) | DB: 29)
  * `c_assign` (Impact: 151.3 | O(N^6) | DB: 4)
  * `compile_funcdef_lambdef_param` (Impact: 130.5 | O(N^6) | DB: 15)
  * `c_if_cond` (Impact: 128.3 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 471`, `structural_boundaries: 122`, `args: 2`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 739`, `dead_code: 12`, `planned_debt: 3`, `orphaned_logic: 18`
* *Architecture:* `api: 165`, `import: 16`
* *Defense:* `safety: 49`, `test: 31`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` persistentcode.h, stdint.h, asmbase.h, scope.h, stdio.h, string.h, nativeglue.h, smallint.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extmod/modlwip.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.646 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 6.797 IQR)
- **Top Global Matches:** file_cluster_13: 13.646, file_cluster_11: 13.835, file_cluster_0: 13.875
- **Magnitude:** 2510.55 | **LOC:** 1961 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 45.5%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (71.1533%), Tech Debt (15.0489%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 59`, `args: 7`, `func_start: 14`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 177`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 67`, `api: 66`, `import: 20`
* *Defense:* `safety: 3`, `doc: 2`, `test: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` stdio.h, string.h, tcp.h, raw.h, objlist.h, udp.h, mphal.h, timers.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extmod/btstack/modbluetooth_btstack.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.74 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.649 IQR)
- **Top Global Matches:** file_cluster_8: 13.74, file_cluster_13: 13.911, file_cluster_11: 13.945
- **Magnitude:** 2432.8 | **LOC:** 1552 | **CtrlFlow:** 59.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 72
- **Risk Profile:** Cognitive Load (91.7158%), Tech Debt (45.7003%)
**Top Internal Functions/Classes:**
  * `btstack_packet_handler_generic` (Impact: 428.9 | O(2^N) | DB: 72)
  * `mp_bluetooth_gatts_register_service` (Impact: 88.5 | O(2^N) | DB: 17)
  * `mp_bluetooth_gatts_notify_indicate` (Impact: 88.3 | O(2^N) | DB: 16)
  * `mp_bluetooth_gatts_write` (Impact: 72.5 | O(2^N) | DB: 8)
  * `set_random_address` (Impact: 59.0 | O(2^N) | DB: 3)
    * *Intent:* // Stop waiting for initialisation. // This signals both the loops in mp_bluetooth_init and mp_bluet...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 188`, `args: 15`, `func_start: 62`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 764`, `planned_debt: 5`, `orphaned_logic: 15`
* *Architecture:* `io: 5`, `api: 281`, `import: 6`
* *Defense:* `safety: 27`, `test: 5`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` modbluetooth_btstack.h, mphal.h, mperrno.h, runtime.h, modbluetooth.h, btstack.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/usbhost/Class/AUDIO/Src/usbh_audio.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.352 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.612 IQR)
- **Top Global Matches:** file_cluster_8: 14.352, file_cluster_7: 14.417, file_cluster_13: 14.635
- **Magnitude:** 2314.08 | **LOC:** 1995 | **CtrlFlow:** 86.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (38.716%), Tech Debt (12.5432%)
**Top Internal Functions/Classes:**
  * `USBH_AUDIO_ClassRequest` (Impact: 124.9 | O(N^6) | DB: 22)
  * `ParseCSDescriptors` (Impact: 93.7 | O(N^6) | DB: 14)
  * `USBH_AUDIO_Control` (Impact: 73.5 | O(N^6) | DB: 13)
  * `USBH_AUDIO_CSRequest` (Impact: 66.9 | O(N^6) | DB: 17)
  * `USBH_AUDIO_InterfaceInit` (Impact: 63.0 | O(N^6) | DB: 32)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 44`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 1099`, `orphaned_logic: 7`
* *Architecture:* `api: 254`, `import: 1`
* *Defense:* `doc: 171`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` usbh_audio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/mpz.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.623 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.904 IQR)
- **Top Global Matches:** file_cluster_11: 15.623, file_cluster_0: 15.641, file_cluster_8: 15.666
- **Magnitude:** 2301.78 | **LOC:** 1759 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 134
- **Risk Profile:** Cognitive Load (91.7397%), Tech Debt (68.7877%)
**Top Internal Functions/Classes:**
  * `mpz_set_from_bytes` (Impact: 572.3 | O(N^4) | DB: 134)
  * `mpn_div` (Impact: 46.9 | O(N^4) | DB: 60)
  * `mpz_set_from_float` (Impact: 45.2 | O(N^4) | DB: 16)
  * `mpz_set_from_str` (Impact: 33.8 | O(N^3) | DB: 11)
  * `mpn_cmp` (Impact: 13.0 | O(N^3) | DB: 6)
    * *Intent:* * in the Software without restriction, including without limitation the rights * to use, copy, modif...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 90`, `args: 4`, `func_start: 47`
* *Risk/State:* `state_mutation: 1240`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 2`, `orphaned_logic: 15`
* *Architecture:* `api: 197`, `import: 3`
* *Defense:* `safety: 65`, `test: 8`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, string.h, mpz.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/qstr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.646 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.616 IQR)
- **Top Global Matches:** file_cluster_13: 14.646, file_cluster_11: 14.813, file_cluster_0: 14.83
- **Magnitude:** 2293.22 | **LOC:** 531 | **CtrlFlow:** 69.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (76.0389%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 23`, `args: 12`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 215`, `dead_code: 1`
* *Architecture:* `api: 43`, `import: 8`
* *Defense:* `safety: 20`, `test: 2`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` qstrdefs.generated.h, stdio.h, string.h, gc.h, runtime.h, compressed.data.h, qstr.h, assert.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/cc3200/ftp/ftp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.126 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.275 IQR)
- **Top Global Matches:** file_cluster_13: 13.126, file_cluster_8: 13.127, file_cluster_7: 13.425
- **Magnitude:** 2202.82 | **LOC:** 1153 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (87.847%), Tech Debt (11.5175%)
**Top Internal Functions/Classes:**
  * `ftp_process_cmd` (Impact: 581.5 | O(N^6) | DB: 24)
  * `ftp_run` (Impact: 407.6 | O(N^6) | DB: 29)
  * `ftp_list_dir` (Impact: 146.6 | O(N^5) | DB: 15)
  * `ftp_send_from_fifo` (Impact: 80.8 | O(N^6) | DB: 3)
  * `ftp_print_eplf_item` (Impact: 43.2 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 150`, `args: 43`, `func_start: 38`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 457`, `orphaned_logic: 4`
* *Architecture:* `api: 181`, `import: 23`
* *Defense:* `safety: 9`, `doc: 7`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` modsocket.h, stdio.h, simplelink.h, updater.h, hw_types.h, debug.h, prcm.h, serverstask.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/parsenum.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.078 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.865 IQR)
- **Top Global Matches:** file_cluster_13: 14.078, file_cluster_11: 14.132, file_cluster_0: 14.283
- **Magnitude:** 2060.26 | **LOC:** 506 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 65
- **Risk Profile:** Cognitive Load (91.9392%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `raise_exc` (Impact: 1817.1 | O(2^N) | DB: 65)
    * *Intent:* * This file is part of the MicroPython project, http://micropython.org/ * * The MIT License (MIT) * ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 28`, `args: 3`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `state_mutation: 195`, `dead_code: 3`
* *Architecture:* `api: 43`, `import: 8`
* *Defense:* `safety: 4`, `test: 1`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` math.h, smallint.h, runtime.h, parsenumbase.h, misc.h, stdbool.h, stdlib.h, parsenum.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/usbhost/Class/MTP/Src/usbh_mtp_ptp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.422 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.677 IQR)
- **Top Global Matches:** file_cluster_8: 14.422, file_cluster_7: 14.474, file_cluster_13: 14.658
- **Magnitude:** 2005.4 | **LOC:** 1770 | **CtrlFlow:** 85.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (38.7922%), Tech Debt (26.8941%)
**Top Internal Functions/Classes:**
  * `USBH_PTP_Process` (Impact: 243.1 | O(N^6) | DB: 42)
    * *Intent:* */ /** * @} */ /** @defgroup USBH_MTP_PTP_Private_Macros * @{ */ /** * @} */ /** @defgroup USBH_MTP_...
  * `PTP_GetDevicePropValue` (Impact: 94.0 | O(N^6) | DB: 21)
  * `USBH_PTP_GetPartialObject` (Impact: 38.1 | O(N^6) | DB: 21)
  * `USBH_PTP_GetObject` (Impact: 37.9 | O(N^6) | DB: 18)
  * `USBH_PTP_GetObjectPropList` (Impact: 34.4 | O(N^6) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 40`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 919`, `orphaned_logic: 16`
* *Architecture:* `api: 236`, `import: 2`
* *Defense:* `doc: 143`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` usbh_mtp.h, usbh_mtp_ptp.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/runtime.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.513 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.588 IQR)
- **Top Global Matches:** file_cluster_13: 12.513, file_cluster_8: 12.77, file_cluster_11: 12.777
- **Magnitude:** 1942.93 | **LOC:** 1787 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (85.922%), Tech Debt (17.0671%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 43`, `args: 2`, `func_start: 10`
* *Risk/State:* `state_mutation: 126`, `planned_debt: 4`
* *Architecture:* `api: 82`, `import: 20`
* *Defense:* `safety: 2`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` cstack.h, objmodule.h, unistd.h, stdio.h, objstr.h, string.h, smallint.h, objtuple.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/esp32/boards/UM_TINYPICO/modules/dotstar.py` (EMBEDDED_PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.692 IQR)
- **Top Global Matches:** file_cluster_2: 11.692, file_cluster_8: 11.802, file_cluster_13: 11.803
- **Magnitude:** 1926.04 | **LOC:** 228 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (38.7429%), Tech Debt (26.5079%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 24`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 45`, `planned_debt: 2`
* *Architecture:* `io: 9`, `api: 6`, `import: 2`
* *Defense:* `safety: 3`, `doc: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dotstar, machine
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/mboot/main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.671 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.593 IQR)
- **Top Global Matches:** file_cluster_8: 13.671, file_cluster_13: 13.747, file_cluster_11: 13.953
- **Magnitude:** 1767.32 | **LOC:** 1807 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (89.0101%), Tech Debt (32.3656%)
**Top Internal Functions/Classes:**
  * `dfu_handle_tx` (Impact: 586.4 | O(N^4) | DB: 58)
  * `i2c_slave_process_rx_end` (Impact: 154.8 | O(N^5) | DB: 36)
  * `dfu_process_dnload` (Impact: 69.6 | O(N^5) | DB: 8)
  * `dfu_handle_rx` (Impact: 37.1 | O(N^3) | DB: 12)
    * *Intent:* #if __GNUC__ >= 11 #pragma GCC diagnostic push #pragma GCC diagnostic ignored "-Warray-bounds"
  * `SystemClock_Config` (Impact: 34.9 | O(N^3) | DB: 3)
    * *Intent:* #define MBOOT_FLASH_LATENCY FLASH_LATENCY_1 #endif #define MBOOT_CLK_AHB_DIV (RCC_SYSCLK_DIV1) #defi...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 125`, `args: 31`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 573`, `planned_debt: 3`, `orphaned_logic: 10`
* *Architecture:* `api: 128`, `import: 17`
* *Defense:* `safety: 9`, `doc: 7`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` powerctrl.h, i2cslave.h, mpu.h, pack.h, xspi.h, mphal.h, flash.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extmod/nimble/modbluetooth_nimble.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.911 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.777 IQR)
- **Top Global Matches:** file_cluster_13: 13.911, file_cluster_8: 13.987, file_cluster_11: 14.003
- **Magnitude:** 1740.7 | **LOC:** 2051 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (72.4701%), Tech Debt (78.5211%)
**Top Internal Functions/Classes:**
  * `l2cap_channel_event` (Impact: 466.0 | O(2^N) | DB: 66)
  * `gatts_register_cb` (Impact: 89.1 | O(2^N) | DB: 14)
  * `characteristic_access_cb` (Impact: 87.6 | O(2^N) | DB: 22)
  * `mp_bluetooth_set_address_mode` (Impact: 36.7 | O(N^4) | DB: 5)
    * *Intent:* #if !MICROPY_BLUETOOTH_NIMBLE_BINDINGS_ONLY // On ports such as ESP32 where we only implement the bi...
  * `ble_hs_err_to_errno` (Impact: 31.8 | O(2^N))
    * *Intent:* #endif // Used by both of the above.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 211`, `args: 40`, `func_start: 49`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 532`, `planned_debt: 14`, `orphaned_logic: 13`
* *Architecture:* `io: 2`, `api: 169`, `import: 18`
* *Defense:* `safety: 26`, `test: 15`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ble_hs_pvcy_priv.h, ble_hs_priv.h, mphal.h, util.h, mperrno.h, ble_hs.h, modbluetooth_nimble.h, ble_svc_gatt.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/usbdev/class/src/usbd_cdc_msc_hid.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.46 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.349 IQR)
- **Top Global Matches:** file_cluster_8: 13.46, file_cluster_13: 13.756, file_cluster_0: 13.792
- **Magnitude:** 1644.58 | **LOC:** 1295 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 92
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (11.285%)
**Top Internal Functions/Classes:**
  * `USBD_CDC_MSC_HID_Init` (Impact: 923.8 | O(2^N) | DB: 70)
    * *Intent:* #endif #endif #if MICROPY_HW_USB_CDC_NUM >= 2
  * `USBD_SelectMode` (Impact: 84.6 | O(N^3) | DB: 92)
  * `make_cdc_desc` (Impact: 18.1 | O(N^2) | DB: 10)
  * `make_cdc_desc_ep` (Impact: 3.5 | O(N^2) | DB: 5)
  * `usbd_cdc_state_init` (Impact: 2.0 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 40`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 489`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 101`, `import: 2`
* *Defense:* `safety: 11`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` usbd_ioreq.h, usbd_cdc_msc_hid.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/nrf/nrfx_glue.h` (C | Tier 4 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.162 IQR)
- **Top Global Matches:** file_cluster_8: 11.162, file_cluster_13: 11.473, file_cluster_7: 11.876
- **Magnitude:** 1597.59 | **LOC:** 153 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (44.5817%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `args: 16`, `func_start: 1`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.164
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` nrfx_irqs.h, nrf_soc.h, mpconfig.h, misc.h, ble_drv.h, nrf_nvic.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/emitinlinethumb.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.621 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.123 IQR)
- **Top Global Matches:** file_cluster_8: 13.621, file_cluster_11: 13.622, file_cluster_13: 13.628
- **Magnitude:** 1583.32 | **LOC:** 866 | **CtrlFlow:** 80.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 119
- **Risk Profile:** Cognitive Load (99.4553%), Tech Debt (9.6922%)
**Top Internal Functions/Classes:**
  * `emit_inline_thumb_op` (Impact: 752.0 | O(N^6) | DB: 119)
  * `get_arg_reglist` (Impact: 47.5 | O(N^5) | DB: 11)
  * `get_arg_reg` (Impact: 32.6 | O(N^6) | DB: 4)
  * `get_arg_vfpreg` (Impact: 28.3 | O(N^5) | DB: 6)
  * `emit_inline_thumb_count_params` (Impact: 14.9 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 67`, `func_start: 19`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 467`, `dead_code: 2`, `planned_debt: 3`
* *Architecture:* `api: 162`, `import: 9`
* *Defense:* `safety: 5`, `test: 3`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` stdint.h, asmthumb.h, stdio.h, string.h, stdarg.h, grammar.h, assert.h, emit.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/nrf/examples/powerup.py` (EMBEDDED_PYTHON | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.355 IQR)
- **Top Global Matches:** file_cluster_8: 11.355, file_cluster_13: 11.463, file_cluster_0: 11.885
- **Magnitude:** 1542.24 | **LOC:** 217 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (71.2672%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 42`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 47`
* *Architecture:* `io: 15`, `api: 20`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` time, ubluepy, machine
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/nrf/drivers/bluetooth/ble_drv.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.658 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.804 IQR)
- **Top Global Matches:** file_cluster_8: 13.658, file_cluster_13: 13.749, file_cluster_11: 13.922
- **Magnitude:** 1520.5 | **LOC:** 1199 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 80
- **Risk Profile:** Cognitive Load (91.8413%), Tech Debt (80.823%)
**Top Internal Functions/Classes:**
  * `ble_evt_handler` (Impact: 238.2 | O(N^6) | DB: 61)
  * `ble_drv_advertise_data` (Impact: 151.8 | O(N^6) | DB: 80)
  * `ble_drv_stack_enable` (Impact: 74.8 | O(N^6) | DB: 39)
  * `ble_drv_characteristic_add` (Impact: 45.8 | O(N^6) | DB: 36)
  * `SWI2_IRQHandler` (Impact: 26.2 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 89`, `args: 8`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 618`, `dead_code: 1`, `planned_debt: 2`, `orphaned_logic: 22`
* *Architecture:* `io: 12`, `api: 147`, `import: 12`
* *Defense:* `safety: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` nrf_sdm.h, mphal.h, stdio.h, string.h, flash.h, ble.h, ble_gap.h, nrf_nvic.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `tests/import/pkg3/__init__.py` (PYTHON) | **Drift Ratio: 1.59x**
  * **Global Archetype:** `file_cluster_8` (Drift: 5.875 IQR)
  * **Local Reality:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 9.33 IQR)
- `tests/import/pkg3/subpkg1/__init__.py` (PYTHON) | **Drift Ratio: 1.59x**
  * **Global Archetype:** `file_cluster_8` (Drift: 5.875 IQR)
  * **Local Reality:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 9.33 IQR)
- `tests/import/pkg7/__init__.py` (PYTHON) | **Drift Ratio: 1.59x**
  * **Global Archetype:** `file_cluster_8` (Drift: 5.875 IQR)
  * **Local Reality:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 9.33 IQR)
- `tests/import/pkg7/subpkg1/__init__.py` (PYTHON) | **Drift Ratio: 1.59x**
  * **Global Archetype:** `file_cluster_8` (Drift: 5.875 IQR)
  * **Local Reality:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 9.33 IQR)
- `tests/import/pkg7/subpkg1/subpkg2/__init__.py` (PYTHON) | **Drift Ratio: 1.59x**
  * **Global Archetype:** `file_cluster_8` (Drift: 5.875 IQR)
  * **Local Reality:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 9.33 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/basics/class2.py` (PYTHON) | Magnitude: 13.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 8, debug_prints: 5, args: 3
- `ports/esp32/machine_uart.c` (C) | Magnitude: 279.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 142, state_mutation: 139, pointers: 93, branch: 41
- `py/obj.h` (C) | Magnitude: 548.68 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 255, api: 253, macros: 189, indent_spaces: 181
- `shared/libc/string0.c` (C) | Magnitude: 610.94 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 267, indent_spaces: 148, pointers: 125, branch: 66
- `tests/cpydiff/core_class_initsubclass_autoclassmethod.py` (PYTHON) | Magnitude: 13.12 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 9, encapsulation: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `py/argcheck.c` (C) | Magnitude: 181.08 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 94, state_mutation: 48, branch: 38, pointers: 27
- `py/gc.c` (C) | Magnitude: 8162.58 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 476, state_mutation: 419, branch: 164, pointers: 139
- `py/mpz.c` (C) | Magnitude: 2301.78 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 1240, indent_spaces: 747, pointers: 473, branch: 206
- `ports/esp8266/machine_uart.c` (C) | Magnitude: 397.42 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 198, indent_spaces: 181, pointers: 77, branch: 60
- `py/objlist.c` (C) | Magnitude: 705.54 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 348, state_mutation: 272, pointers: 269, api: 133

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tools/ci.sh` (SHELL) | Magnitude: 0.4 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 532, reflection_metaprogramming: 187, func_start: 124, state_mutation: 105
- `tools/mpremote/tests/test_mip_local_install.sh` (SHELL) | Magnitude: 0.02 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 20, indent_spaces: 19, io: 10, debug_prints: 8
- `drivers/cc3100/inc/trace.h` (C) | Magnitude: 44.08 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 96, reflection_metaprogramming: 43, state_mutation: 26, branch: 22
- `tools/mpremote/tests/test_filesystem.sh` (SHELL) | Magnitude: 0.04 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety_bypasses: 104, structural_boundaries: 88, reflection_metaprogramming: 53, io: 46
- `py/dynruntime.h` (C) | Magnitude: 127.68 | Delta: **0.12 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 126, indent_spaces: 80, pointers: 78, reflection_metaprogramming: 74

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ports/cc3200/ftp/ftp.c` (C) | Magnitude: 2202.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 807, state_mutation: 457, branch: 270, api: 181
- `ports/unix/coverage.c` (C) | Magnitude: 390.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 527, pointers: 366, state_mutation: 266, api: 66
- `py/ringbuf.c` (C) | Magnitude: 77.98 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 36, pointers: 33, branch: 13
- `tests/io/open_append.py` (PYTHON) | Magnitude: 21.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 6, state_mutation: 6, indent_spaces: 6, safety: 5
- `ports/mimxrt/dma_manager.h` (C) | Magnitude: 16.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 4, args: 3, api: 3, ownership: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/inlineasm/rv32/asmrettype.py` (PYTHON) | Magnitude: 11.52 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 6, args: 4, func_start: 4, api: 4
- `tests/inlineasm/thumb/asmrettype.py` (PYTHON) | Magnitude: 11.52 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 6, args: 4, func_start: 4, api: 4
- `tests/basics/fun_annotations.py` (PYTHON) | Magnitude: 2.86 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/basics/builtin_setattr.py` (PYTHON) | Magnitude: 4.04 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 7, safety: 4, reflection_metaprogramming: 4, debug_prints: 4
- `tests/extmod/vfs_posix.py` (PYTHON) | Magnitude: 337.45 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 29, indent_spaces: 29, debug_prints: 19, structural_boundaries: 18
- `tests/basics/del_attr.py` (PYTHON) | Magnitude: 3.26 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 12, safety: 10, structural_boundaries: 8, debug_prints: 8
- `ports/nrf/boards/PARTICLE_XENON/mpconfigboard.mk` (MAKEFILE) | Magnitude: 16.16 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 6, state_mutation: 2, dead_code: 1
- `tests/basics/assign_expr_scope.py` (PYTHON) | Magnitude: 72.62 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 33, indent_spaces: 27, debug_prints: 23, structural_boundaries: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `ports/nrf/examples/seeed_tft.py` (EMBEDDED_PYTHON) | Magnitude: 340.32 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 144, memory_alloc: 26, structural_boundaries: 24, ui_framework: 20
- `ports/esp32/boards/UM_TINYPICO/modules/dotstar.py` (EMBEDDED_PYTHON) | Magnitude: 1926.04 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 143, branch: 47, state_mutation: 45, encapsulation: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/basics/async_for2.py` (PYTHON) | Magnitude: 34.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, debug_prints: 8, branch: 7
- `tests/multi_espnow/80_asyncio_client.py` (PYTHON) | Magnitude: 98.38 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 21, branch: 18, debug_prints: 13
- `tests/extmod/asyncio_lock_cancel.py` (PYTHON) | Magnitude: 44.6 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, concurrency: 22, structural_boundaries: 9, debug_prints: 6
- `tests/net_hosted/asyncio_loopback.py` (PYTHON) | Magnitude: 37.7 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 37, concurrency: 21, structural_boundaries: 17, debug_prints: 16
- `tests/extmod/asyncio_lock.py` (PYTHON) | Magnitude: 104.6 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 63, concurrency: 57, structural_boundaries: 20, debug_prints: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `ports/stm32/boards/NUCLEO_H563ZI/mpconfigboard.mk` (MAKEFILE) | Magnitude: 15.32 | Delta: **0.263 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 13, branch: 3, dead_code: 1, planned_debt: 1
- `tests/float/float_struct.py` (PYTHON) | Magnitude: 15.2 | Delta: **0.317 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, branch: 2, safety: 2, debug_prints: 2
- `ports/stm32/boards/WEACTSTUDIO_MINI_STM32U585/mpconfigboard.mk` (MAKEFILE) | Magnitude: 15.24 | Delta: **0.332 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 9, branch: 3, dead_code: 2, planned_debt: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `ports/stm32/usbhost/Core/Src/usbh_pipes.c` (C) | Magnitude: 54.2 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 43, indent_spaces: 32, api: 18, state_mutation: 18
- `ports/stm32/usbhost/Class/Template/Src/usbh_template.c` (C) | Magnitude: 40.96 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 42, indent_spaces: 34, pointers: 14, api: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `py/emitinlinethumb.c` (C) | Magnitude: 1583.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 647, state_mutation: 467, branch: 270, pointers: 209
- `tests/perf_bench/bm_nqueens.py` (PYTHON) | Magnitude: 74.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 36, branch: 13, structural_boundaries: 10, explicit_casts: 8
- `ports/rp2/rp2_pio.c` (C) | Magnitude: 593.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 381, state_mutation: 301, pointers: 227, api: 103
- `ports/mimxrt/hal/phy/device/phydp83867/fsl_phydp83867.h` (C) | Magnitude: 25.38 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 34, pointers: 14, api: 10, macros: 6
- `ports/mimxrt/hal/phy/device/phydp83825/fsl_phydp83825.h` (C) | Magnitude: 25.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 36, pointers: 14, api: 10, macros: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `ports/cc3200/mods/pybflash.c` (C) | Magnitude: 54.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, pointers: 23, state_mutation: 18, api: 17
- `ports/renesas-ra/factoryreset.h` (C) | Magnitude: 15.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ownership: 3, structural_boundaries: 2, api: 2, macros: 2
- `ports/stm32/factoryreset.h` (C) | Magnitude: 15.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ownership: 3, structural_boundaries: 2, api: 2, macros: 2
- `extmod/machine_can.h` (C) | Magnitude: 15.12 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ownership: 3, structural_boundaries: 2, api: 2, macros: 2
- `ports/esp8266/boards/ESP8266_GENERIC/mpconfigvariant_FLASH_1M.mk` (MAKEFILE) | Magnitude: 13.6 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, state_mutation: 1, dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tools/ci.sh` -> Churn: **90.48%** | Cog Load: 99.8333% | Debt: 45.9593%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `py/emitnative.c` -> **Alessandro Gatti** (100.0% isolated ownership) | Magnitude: 8726.64
- `ports/renesas-ra/Makefile` -> **Angus Gratton** (100.0% isolated ownership) | Magnitude: 3108.72
- `py/parsenum.c` -> **Jeff Epler** (100.0% isolated ownership) | Magnitude: 2060.26
- `ports/stm32/mboot/main.c` -> **Oliver Joos** (100.0% isolated ownership) | Magnitude: 1767.32
- `extmod/nimble/modbluetooth_nimble.c` -> **Alessandro Gatti** (100.0% isolated ownership) | Magnitude: 1740.7

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `py/runtime.h` -> **Severity: 0.042** (Bridge: 0.0004 * Flux: 96.4477%)
- `py/obj.h` -> **Severity: 0.023** (Bridge: 0.0002 * Flux: 99.9996%)
- `extmod/cyw43_config_common.h` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 95.9865%)
- `shared/tinyusb/mp_usbd.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 78.824%)
- `py/bc.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `py/obj.h` -> **Severity: 5722.3** (Blast Radius: 57.223 * Doc Risk: 100.0%)
- `py/mpstate.h` -> **Severity: 2156.4** (Blast Radius: 21.564 * Doc Risk: 100.0%)
- `py/runtime.h` -> **Severity: 2019.3** (Blast Radius: 20.193 * Doc Risk: 100.0%)
- `py/mphal.h` -> **Severity: 2002.722** (Blast Radius: 20.272 * Doc Risk: 98.7925%)
- `extmod/virtpin.h` -> **Severity: 1642.93** (Blast Radius: 17.648 * Doc Risk: 93.0944%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
