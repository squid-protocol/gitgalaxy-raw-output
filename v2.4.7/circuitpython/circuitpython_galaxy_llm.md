# ARCHITECTURAL_BRIEF: circuitpython
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/circuitpython` |
| **Timestamp** | `2026-08-07T03:48:31.187326+00:00` |
| **Scan Duration** | `28.97s` |
| **Git Branch** | `main` |
| **Git Commit** | `f7f0fd6c45bc71410dfb0acd439bc69516145463` |
| **Git Remote** | `https://github.com/adafruit/circuitpython` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6728 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
| Total Artifacts | 8392 |
| Analyzed Artifacts (Scanned) | 6840 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1552 |
| Total LOC | 308178 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 81.5% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.271 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 166 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 4618 | 238686 | 67.5% |
| PYTHON | 1388 | 50462 | 20.3% |
| MAKEFILE | 667 | 14218 | 9.8% |
| MARKDOWN | 50 | 0 | 0.7% |
| EMBEDDED_PYTHON | 43 | 2138 | 0.6% |
| CSV | 21 | 668 | 0.3% |
| PLAINTEXT | 20 | 1 | 0.3% |
| SHELL | 6 | 777 | 0.1% |
| ASSEMBLY | 6 | 298 | 0.1% |
| XML | 5 | 0 | 0.1% |
| HTML | 5 | 198 | 0.1% |
| JAVASCRIPT | 4 | 456 | 0.1% |
| JSON | 3 | 196 | 0.0% |
| CSHARP | 1 | 34 | 0.0% |
| CPP | 1 | 15 | 0.0% |
| YAML | 1 | 13 | 0.0% |
| CSS | 1 | 18 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.085`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4506 | 65.9% |
| file_cluster_13 | 2024 | 29.6% |
| file_cluster_9 | 117 | 1.7% |
| file_cluster_17 | 40 | 0.6% |
| file_cluster_4 | 34 | 0.5% |
| file_cluster_0 | 20 | 0.3% |
| file_cluster_6 | 7 | 0.1% |
| file_cluster_11 | 7 | 0.1% |
| file_cluster_7 | 5 | 0.1% |
| file_cluster_16 | 4 | 0.1% |
| file_cluster_12 | 3 | 0.0% |
| Unknown | 1 | 0.0% |
| file_cluster_2 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 69 | 1.0% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1552*

**Composition by Extension & Reason:**
- `.exp`: 377x Excluded (Unsupported Extension: '.exp'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 249x Unsupported Format (.undeterminable), 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)
- `.h`: 114x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Machine-Generated Source Code Signature: 22 LOC), 3x Excluded (Machine-Generated Source Code Signature: 307 LOC)
- `.c`: 170x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ld`: 66x Excluded (Unsupported Extension: '.ld')
- `.py`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 153 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2770 LOC)
- `.defaults`: 44x Excluded (Unsupported Extension: '.defaults'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 37x Excluded (Unsupported Extension: '.toml')
- `.rst`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Unsupported Extension: '.rst')
- `.png`: 31x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.license`: 20x Excluded (Unsupported Extension: '.license'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.license)
- `.conf`: 21x Excluded (Unsupported Extension: '.conf'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.po`: 21x Excluded (Unsupported Extension: '.po')
- `.wav`: 18x Excluded (Explicitly Denied Extension: '.wav')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 15.5 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 30.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.3 | 1.7 | 2.3 |
| API Exposure | 0.0 | 19.8 | 4.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 24.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 72.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 9.9 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 36.2 | 15.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 99.4 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ports/raspberrypi/common-hal/socketpool/Socket.c` (Hits: 181)
- `supervisor/shared/web_workflow/web_workflow.c` (Hits: 88)
- `tests/run-tests.py` (Hits: 80)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **runtime.h** (`py/runtime.h`) — 809 inbound connections
2. **obj.h** (`py/obj.h`) — 742 inbound connections
3. **__init__.h** (`shared-bindings/board/__init__.h`) — 699 inbound connections
4. **board.h** (`supervisor/board.h`) — 674 inbound connections
5. **Pin.h** (`shared-bindings/microcontroller/Pin.h`) — 358 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **stm32h7xx_hal_conf.h** (`ports/stm/hal_conf/stm32h7xx_hal_conf.h`) — 60 outbound dependencies
2. **main.c** (`main.c`) — 58 outbound dependencies
3. **port.c** (`ports/espressif/supervisor/port.c`) — 51 outbound dependencies
4. **stm32l4xx_hal_conf.h** (`ports/stm/hal_conf/stm32l4xx_hal_conf.h`) — 50 outbound dependencies
5. **stm32f7xx_hal_conf.h** (`ports/stm/hal_conf/stm32f7xx_hal_conf.h`) — 48 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `mp_obj_str_format_helper` (@ `py/objstr.c`) -> Impact: **605.2** | LOC: 568
- `run_micropython` (@ `tests/run-tests.py`) -> Impact: **597.2** | LOC: 970
- `do_all_the_things` (@ `tools/chart_code_size.py`) -> Impact: **280.4** | LOC: 447
- `run_one_test` (@ `tests/run-tests.py`) -> Impact: **244.7** | LOC: 460
- `emit_inline_thumb_op` (@ `py/emitinlinethumb.c`) -> Impact: **229.6** | LOC: 411
- `zephyr_dts_to_cp_board` (@ `ports/zephyr-cp/cptools/zephyr2cp.py`) -> Impact: **225.7** | LOC: 311
- `_reply_with_file` (@ `supervisor/shared/web_workflow/web_workflow.c`) -> Impact: **199.6** | LOC: 458
- `pre_process_options` (@ `ports/unix/main.c`) -> Impact: **198.1** | LOC: 360
- `update` (@ `ports/espressif/tools/update_sdkconfig.py`) -> Impact: **195.1** | LOC: 342
  * *Intent:* """Updates related sdkconfig files based on the build directory version that was likely modified by menuconfig."""
- `mp_prof_opcode_decode` (@ `py/profile.c`) -> Impact: **182.9** | LOC: 459
  * *Intent:* /******************************************************************************/ // DEBUG // This section is for debugging the settrace feature itself...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `py` | 215 | 44711.28 | 47.78% | 25.95% |
| `tests/basics` | 556 | 8839.12 | 7.37% | 0.0% |
| `ports/nordic` | 16 | 6493.82 | 19.14% | 18.19% |
| `extmod` | 34 | 5029.22 | 51.57% | 11.85% |
| `ports/unix` | 32 | 4363.72 | 41.42% | 38.64% |
| `tests/extmod` | 134 | 4314.96 | 15.89% | 0.0% |
| `shared-module/displayio` | 21 | 3806.52 | 42.95% | 38.39% |
| `devices/ble_hci/common-hal/_bleio` | 25 | 3439.6 | 37.95% | 40.96% |
| `supervisor/shared` | 38 | 3198.0 | 37.32% | 35.94% |
| `ports/espressif` | 9 | 2759.7 | 11.14% | 23.97% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `ports/raspberrypi/boards/hack_club_sprig/mpconfigboard.mk` -> **100.0%** Exposure
- `ports/raspberrypi/boards/orpheus_pico/mpconfigboard.mk` -> **100.0%** Exposure
- `ports/raspberrypi/boards/waveshare_rp2040_lcd_1_28/mpconfigboard.mk` -> **100.0%** Exposure
- `ports/raspberrypi/boards/waveshare_rp2040_touch_lcd_1_28/mpconfigboard.mk` -> **100.0%** Exposure
- `ports/raspberrypi/boards/waveshare_rp2350_lcd_1_28/mpconfigboard.mk` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `mpy-cross/Makefile` -> **100.0%** Exposure
- `ports/atmel-samd/Makefile` -> **100.0%** Exposure
- `ports/atmel-samd/boards/pyportal/mpconfigboard.mk` -> **100.0%** Exposure
- `ports/atmel-samd/boards/pyportal_titano/mpconfigboard.mk` -> **100.0%** Exposure
- `ports/atmel-samd/boards/winterbloom_big_honking_button/usermods/_bhb/micropython.mk` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tools/ci.sh` -> **85** Orphaned Functions | **0** Duplicates
- `shared-module/_eve/__init__.c` -> **54** Orphaned Functions | **0** Duplicates
- `ports/zephyr-cp/common-hal/wifi/Radio.c` -> **44** Orphaned Functions | **0** Duplicates
- `py/asmx86.c` -> **41** Orphaned Functions | **0** Duplicates
- `ports/espressif/common-hal/wifi/Radio.c` -> **39** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`extmod/moddeflate.c`** -> AI Confidence: **99.48%**
2. **`extmod/modjson.c`** -> AI Confidence: **99.48%**
3. **`extmod/modos.c`** -> AI Confidence: **99.48%**
4. **`ports/analog/common-hal/microcontroller/__init__.c`** -> AI Confidence: **99.48%**
5. **`ports/atmel-samd/common-hal/microcontroller/__init__.c`** -> AI Confidence: **99.48%**
6. **`ports/atmel-samd/common-hal/spitarget/SPITarget.c`** -> AI Confidence: **99.48%**
7. **`ports/atmel-samd/eic_handler.c`** -> AI Confidence: **99.48%**
8. **`ports/broadcom/common-hal/neopixel_write/__init__.c`** -> AI Confidence: **99.48%**
9. **`ports/espressif/common-hal/microcontroller/__init__.c`** -> AI Confidence: **99.48%**
10. **`ports/espressif/module/cardputer_keyboard.c`** -> AI Confidence: **99.48%**
11. **`ports/stm/common-hal/neopixel_write/__init__.c`** -> AI Confidence: **99.48%**
12. **`ports/stm/peripherals/stm32f4/clocks.c`** -> AI Confidence: **99.48%**
13. **`ports/unix/input.c`** -> AI Confidence: **99.48%**
14. **`py/binary.c`** -> AI Confidence: **99.48%**
15. **`py/compile.c`** -> AI Confidence: **99.48%**
16. **`py/emitglue.c`** -> AI Confidence: **99.48%**
17. **`py/emitinlinethumb.c`** -> AI Confidence: **99.48%**
18. **`py/formatfloat.c`** -> AI Confidence: **99.48%**
19. **`py/modstruct.c`** -> AI Confidence: **99.48%**
20. **`py/modsys.c`** -> AI Confidence: **99.48%**
21. **`py/mpprint.c`** -> AI Confidence: **99.48%**
22. **`py/objstr.c`** -> AI Confidence: **99.48%**
23. **`py/parsenum.c`** -> AI Confidence: **99.48%**
24. **`py/vm.c`** -> AI Confidence: **99.48%**
25. **`shared-module/bitmapfilter/__init__.c`** -> AI Confidence: **99.48%**
26. **`shared-module/terminalio/Terminal.c`** -> AI Confidence: **99.48%**
27. **`shared/readline/readline.c`** -> AI Confidence: **99.48%**
28. **`shared/runtime/pyexec.c`** -> AI Confidence: **99.48%**
29. **`supervisor/shared/safe_mode.c`** -> AI Confidence: **99.48%**
30. **`supervisor/shared/usb.c`** -> AI Confidence: **99.48%**
31. **`ports/stm/hal_conf/stm32f4xx_hal_conf.h`** -> AI Confidence: **99.48%**
32. **`ports/stm/hal_conf/stm32f7xx_hal_conf.h`** -> AI Confidence: **99.48%**
33. **`ports/stm/hal_conf/stm32h7xx_hal_conf.h`** -> AI Confidence: **99.48%**
34. **`ports/stm/hal_conf/stm32l4xx_hal_conf.h`** -> AI Confidence: **99.48%**
35. **`tools/analyze_heap_dump.py`** -> AI Confidence: **99.39%**
36. **`tools/ci_fetch_deps.py`** -> AI Confidence: **99.39%**
37. **`extmod/modbinascii.c`** -> AI Confidence: **99.39%**
38. **`extmod/modselect.c`** -> AI Confidence: **99.39%**
39. **`mpy-cross/main.c`** -> AI Confidence: **99.39%**
40. **`ports/atmel-samd/common-hal/imagecapture/ParallelImageCapture.c`** -> AI Confidence: **99.39%**
41. **`ports/atmel-samd/timer_handler.c`** -> AI Confidence: **99.39%**
42. **`ports/espressif/common-hal/_bleio/Characteristic.c`** -> AI Confidence: **99.39%**
43. **`ports/espressif/common-hal/analogio/AnalogIn.c`** -> AI Confidence: **99.39%**
44. **`ports/espressif/common-hal/espidf/__init__.c`** -> AI Confidence: **99.39%**
45. **`ports/espressif/common-hal/espulp/ULP.c`** -> AI Confidence: **99.39%**
46. **`ports/espressif/common-hal/neopixel_write/__init__.c`** -> AI Confidence: **99.39%**
47. **`ports/mimxrt10xx/common-hal/busio/UART.c`** -> AI Confidence: **99.39%**
48. **`ports/mimxrt10xx/peripherals/mimxrt10xx/MIMXRT1176/clocks.c`** -> AI Confidence: **99.39%**
49. **`ports/raspberrypi/common-hal/picodvi/Framebuffer_RP2040.c`** -> AI Confidence: **99.39%**
50. **`ports/silabs/common-hal/_bleio/__init__.c`** -> AI Confidence: **99.39%**
51. **`ports/stm/peripherals/sdram.c`** -> AI Confidence: **99.39%**
52. **`ports/unix/main.c`** -> AI Confidence: **99.39%**
53. **`py/asmthumb.c`** -> AI Confidence: **99.39%**
54. **`py/map.c`** -> AI Confidence: **99.39%**
55. **`py/objcomplex.c`** -> AI Confidence: **99.39%**
56. **`py/objexcept.c`** -> AI Confidence: **99.39%**
57. **`py/objfloat.c`** -> AI Confidence: **99.39%**
58. **`py/objfun.c`** -> AI Confidence: **99.39%**
59. **`py/objgenerator.c`** -> AI Confidence: **99.39%**
60. **`py/objmodule.c`** -> AI Confidence: **99.39%**
61. **`py/persistentcode.c`** -> AI Confidence: **99.39%**
62. **`py/qstr.c`** -> AI Confidence: **99.39%**
63. **`py/repl.c`** -> AI Confidence: **99.39%**
64. **`shared-bindings/_pew/PewPew.c`** -> AI Confidence: **99.39%**
65. **`shared-bindings/supervisor/__init__.c`** -> AI Confidence: **99.39%**
66. **`shared-bindings/synthio/__init__.c`** -> AI Confidence: **99.39%**
67. **`shared-module/audiocore/WaveFile.c`** -> AI Confidence: **99.39%**
68. **`shared-module/audiomixer/Mixer.c`** -> AI Confidence: **99.39%**
69. **`shared-module/bitmaptools/__init__.c`** -> AI Confidence: **99.39%**
70. **`shared-module/displayio/OnDiskBitmap.c`** -> AI Confidence: **99.39%**
71. **`shared-module/floppyio/__init__.c`** -> AI Confidence: **99.39%**
72. **`supervisor/shared/workflow.c`** -> AI Confidence: **99.39%**
73. **`tests/run-tests.py`** -> AI Confidence: **99.35%**
74. **`extmod/modre.c`** -> AI Confidence: **99.35%**
75. **`main.c`** -> AI Confidence: **99.35%**
76. **`ports/atmel-samd/common-hal/audiobusio/PDMIn.c`** -> AI Confidence: **99.35%**
77. **`shared-module/displayio/__init__.c`** -> AI Confidence: **99.35%**
78. **`ports/espressif/tools/update_sdkconfig.py`** -> AI Confidence: **99.34%**
79. **`ports/mimxrt10xx/common-hal/usb_host/Port.c`** -> AI Confidence: **99.34%**
80. **`ports/mimxrt10xx/peripherals/mimxrt10xx/MIMXRT1052/clocks.c`** -> AI Confidence: **99.34%**
81. **`ports/mimxrt10xx/peripherals/mimxrt10xx/MIMXRT1062/clocks.c`** -> AI Confidence: **99.34%**
82. **`ports/nordic/common-hal/_bleio/Characteristic.c`** -> AI Confidence: **99.34%**
83. **`ports/nordic/common-hal/neopixel_write/__init__.c`** -> AI Confidence: **99.34%**
84. **`ports/stm/peripherals/stm32h7/clocks.c`** -> AI Confidence: **99.34%**
85. **`ports/stm/peripherals/stm32l4/clocks.c`** -> AI Confidence: **99.34%**
86. **`ports/unix/modtermios.c`** -> AI Confidence: **99.34%**
87. **`py/lexer.c`** -> AI Confidence: **99.34%**
88. **`py/objarray.c`** -> AI Confidence: **99.34%**
89. **`py/profile.c`** -> AI Confidence: **99.34%**
90. **`shared-bindings/audiobusio/PDMIn.c`** -> AI Confidence: **99.34%**
91. **`shared-bindings/keypad/ShiftRegisterKeys.c`** -> AI Confidence: **99.34%**
92. **`shared-module/_stage/__init__.c`** -> AI Confidence: **99.34%**
93. **`shared-module/os/__init__.c`** -> AI Confidence: **99.34%**
94. **`ports/nordic/mpconfigport.h`** -> AI Confidence: **99.34%**
95. **`tests/import/builtin_import.py`** -> AI Confidence: **99.32%**
96. **`tools/fixup_translations.py`** -> AI Confidence: **99.32%**
97. **`ports/espressif/boards/makerfabs_tft7/pins.c`** -> AI Confidence: **99.32%**
98. **`ports/espressif/common-hal/wifi/Network.c`** -> AI Confidence: **99.32%**
99. **`ports/raspberrypi/peripherals/pins.c`** -> AI Confidence: **99.32%**
100. **`ports/stm/packages/LQFP100_f4.c`** -> AI Confidence: **99.32%**
101. **`ports/stm/packages/LQFP64.c`** -> AI Confidence: **99.32%**
102. **`py/emitnarm.c`** -> AI Confidence: **99.32%**
103. **`py/emitnrv32.c`** -> AI Confidence: **99.32%**
104. **`py/emitnthumb.c`** -> AI Confidence: **99.32%**
105. **`py/emitnx64.c`** -> AI Confidence: **99.32%**
106. **`py/emitnxtensa.c`** -> AI Confidence: **99.32%**
107. **`py/emitnxtensawin.c`** -> AI Confidence: **99.32%**
108. **`py/parsenumbase.c`** -> AI Confidence: **99.32%**
109. **`shared-bindings/framebufferio/__init__.c`** -> AI Confidence: **99.32%**
110. **`shared-module/_bleio/Attribute.c`** -> AI Confidence: **99.32%**
111. **`shared-module/getpass/__init__.c`** -> AI Confidence: **99.32%**
112. **`supervisor/shared/external_flash/qspi_flash.c`** -> AI Confidence: **99.32%**
113. **`ports/atmel-samd/mpconfigport.h`** -> AI Confidence: **99.32%**
114. **`ports/espressif/mpconfigport.h`** -> AI Confidence: **99.32%**
115. **`ports/cxd56/tools/flash_writer.py`** -> AI Confidence: **99.31%**
116. **`ports/zephyr-cp/cptools/build_all_boards.py`** -> AI Confidence: **99.31%**
117. **`ports/zephyr-cp/cptools/build_circuitpython.py`** -> AI Confidence: **99.31%**
118. **`py/makecompresseddata.py`** -> AI Confidence: **99.31%**
119. **`py/makeqstrdefs.py`** -> AI Confidence: **99.31%**
120. **`py/maketranslationdata.py`** -> AI Confidence: **99.31%**
121. **`tests/run-internalbench.py`** -> AI Confidence: **99.31%**
122. **`tests/run-multitests.py`** -> AI Confidence: **99.31%**
123. **`tests/run-natmodtests.py`** -> AI Confidence: **99.31%**
124. **`tests/run-perfbench-table.py`** -> AI Confidence: **99.31%**
125. **`tools/board_stubs/build_board_specific_stubs/board_stub_builder.py`** -> AI Confidence: **99.31%**
126. **`tools/board_stubs/circuitpython_setboard/__init__.py`** -> AI Confidence: **99.31%**
127. **`tools/build_release_files.py`** -> AI Confidence: **99.31%**
128. **`tools/ci_set_matrix.py`** -> AI Confidence: **99.31%**
129. **`tools/codeformat.py`** -> AI Confidence: **99.31%**
130. **`tools/cpboard.py`** -> AI Confidence: **99.31%**
131. **`tools/extract_pyi.py`** -> AI Confidence: **99.31%**
132. **`tools/gen_crt_bundle.py`** -> AI Confidence: **99.31%**
133. **`tools/makemanifest.py`** -> AI Confidence: **99.31%**
134. **`tools/manifestfile.py`** -> AI Confidence: **99.31%**
135. **`tools/mpy_ld.py`** -> AI Confidence: **99.31%**
136. **`tools/msgfmt.py`** -> AI Confidence: **99.31%**
137. **`tools/pydfu.py`** -> AI Confidence: **99.31%**
138. **`tools/safe_mode_finder.py`** -> AI Confidence: **99.31%**
139. **`devices/ble_hci/common-hal/_bleio/Adapter.c`** -> AI Confidence: **99.31%**
140. **`devices/ble_hci/common-hal/_bleio/Characteristic.c`** -> AI Confidence: **99.31%**
141. **`devices/ble_hci/common-hal/_bleio/PacketBuffer.c`** -> AI Confidence: **99.31%**
142. **`devices/ble_hci/common-hal/_bleio/att.c`** -> AI Confidence: **99.31%**
143. **`extmod/vfs.c`** -> AI Confidence: **99.31%**
144. **`extmod/vfs_blockdev.c`** -> AI Confidence: **99.31%**
145. **`extmod/vfs_fat.c`** -> AI Confidence: **99.31%**
146. **`extmod/vfs_fat_diskio.c`** -> AI Confidence: **99.31%**
147. **`extmod/vfs_fat_file.c`** -> AI Confidence: **99.31%**
148. **`extmod/vfs_lfsx.c`** -> AI Confidence: **99.31%**
149. **`extmod/vfs_posix.c`** -> AI Confidence: **99.31%**
150. **`extmod/vfs_posix_file.c`** -> AI Confidence: **99.31%**
151. **`extmod/vfs_reader.c`** -> AI Confidence: **99.31%**
152. **`ports/analog/common-hal/busio/UART.c`** -> AI Confidence: **99.31%**
153. **`ports/analog/supervisor/internal_flash.c`** -> AI Confidence: **99.31%**
154. **`ports/atmel-samd/audio_dma.c`** -> AI Confidence: **99.31%**
155. **`ports/atmel-samd/common-hal/alarm/__init__.c`** -> AI Confidence: **99.31%**
156. **`ports/atmel-samd/common-hal/alarm/pin/PinAlarm.c`** -> AI Confidence: **99.31%**
157. **`ports/atmel-samd/common-hal/busio/I2C.c`** -> AI Confidence: **99.31%**
158. **`ports/atmel-samd/common-hal/busio/SPI.c`** -> AI Confidence: **99.31%**
159. **`ports/atmel-samd/common-hal/busio/UART.c`** -> AI Confidence: **99.31%**
160. **`ports/atmel-samd/common-hal/canio/Listener.c`** -> AI Confidence: **99.31%**
161. **`ports/atmel-samd/common-hal/countio/Counter.c`** -> AI Confidence: **99.31%**
162. **`ports/atmel-samd/common-hal/frequencyio/FrequencyIn.c`** -> AI Confidence: **99.31%**
163. **`ports/atmel-samd/common-hal/i2ctarget/I2CTarget.c`** -> AI Confidence: **99.31%**
164. **`ports/atmel-samd/common-hal/max3421e/Max3421E.c`** -> AI Confidence: **99.31%**
165. **`ports/atmel-samd/common-hal/neopixel_write/__init__.c`** -> AI Confidence: **99.31%**
166. **`ports/atmel-samd/common-hal/ps2io/Ps2.c`** -> AI Confidence: **99.31%**
167. **`ports/atmel-samd/common-hal/pulseio/PulseIn.c`** -> AI Confidence: **99.31%**
168. **`ports/atmel-samd/common-hal/watchdog/WatchDogTimer.c`** -> AI Confidence: **99.31%**
169. **`ports/atmel-samd/supervisor/port.c`** -> AI Confidence: **99.31%**
170. **`ports/broadcom/common-hal/busio/I2C.c`** -> AI Confidence: **99.31%**
171. **`ports/broadcom/common-hal/busio/SPI.c`** -> AI Confidence: **99.31%**
172. **`ports/broadcom/common-hal/busio/UART.c`** -> AI Confidence: **99.31%**
173. **`ports/broadcom/common-hal/sdioio/SDCard.c`** -> AI Confidence: **99.31%**
174. **`ports/cxd56/common-hal/analogio/AnalogIn.c`** -> AI Confidence: **99.31%**
175. **`ports/cxd56/mkspk/mkspk.c`** -> AI Confidence: **99.31%**
176. **`ports/espressif/boards/mixgo_ce_serial/board.c`** -> AI Confidence: **99.31%**
177. **`ports/espressif/common-hal/_bleio/Adapter.c`** -> AI Confidence: **99.31%**
178. **`ports/espressif/common-hal/_bleio/Connection.c`** -> AI Confidence: **99.31%**
179. **`ports/espressif/common-hal/_bleio/Descriptor.c`** -> AI Confidence: **99.31%**
180. **`ports/espressif/common-hal/_bleio/PacketBuffer.c`** -> AI Confidence: **99.31%**
181. **`ports/espressif/common-hal/_bleio/ble_events.c`** -> AI Confidence: **99.31%**
182. **`ports/espressif/common-hal/_bleio/bonding.c`** -> AI Confidence: **99.31%**
183. **`ports/espressif/common-hal/alarm/__init__.c`** -> AI Confidence: **99.31%**
184. **`ports/espressif/common-hal/alarm/pin/PinAlarm.c`** -> AI Confidence: **99.31%**
185. **`ports/espressif/common-hal/analogbufio/BufferedIn.c`** -> AI Confidence: **99.31%**
186. **`ports/espressif/common-hal/busio/UART.c`** -> AI Confidence: **99.31%**
187. **`ports/espressif/common-hal/canio/CAN.c`** -> AI Confidence: **99.31%**
188. **`ports/espressif/common-hal/max3421e/Max3421E.c`** -> AI Confidence: **99.31%**
189. **`ports/espressif/common-hal/microcontroller/Processor.c`** -> AI Confidence: **99.31%**
190. **`ports/espressif/common-hal/nvm/ByteArray.c`** -> AI Confidence: **99.31%**
191. **`ports/espressif/common-hal/os/__init__.c`** -> AI Confidence: **99.31%**
192. **`ports/espressif/common-hal/sdioio/SDCard.c`** -> AI Confidence: **99.31%**
193. **`ports/espressif/common-hal/socketpool/Socket.c`** -> AI Confidence: **99.31%**
194. **`ports/espressif/common-hal/socketpool/SocketPool.c`** -> AI Confidence: **99.31%**
195. **`ports/espressif/common-hal/wifi/Radio.c`** -> AI Confidence: **99.31%**
196. **`ports/espressif/common-hal/wifi/ScannedNetworks.c`** -> AI Confidence: **99.31%**
197. **`ports/espressif/common-hal/wifi/__init__.c`** -> AI Confidence: **99.31%**
198. **`ports/espressif/supervisor/internal_flash.c`** -> AI Confidence: **99.31%**
199. **`ports/espressif/supervisor/usb_serial_jtag.c`** -> AI Confidence: **99.31%**
200. **`ports/mimxrt10xx/common-hal/busio/SPI.c`** -> AI Confidence: **99.31%**
201. **`ports/mimxrt10xx/common-hal/canio/Listener.c`** -> AI Confidence: **99.31%**
202. **`ports/mimxrt10xx/common-hal/microcontroller/Processor.c`** -> AI Confidence: **99.31%**
203. **`ports/nordic/bluetooth/ble_drv.c`** -> AI Confidence: **99.31%**
204. **`ports/nordic/common-hal/_bleio/Adapter.c`** -> AI Confidence: **99.31%**
205. **`ports/nordic/common-hal/_bleio/CharacteristicBuffer.c`** -> AI Confidence: **99.31%**
206. **`ports/nordic/common-hal/_bleio/Connection.c`** -> AI Confidence: **99.31%**
207. **`ports/nordic/common-hal/_bleio/PacketBuffer.c`** -> AI Confidence: **99.31%**
208. **`ports/nordic/common-hal/_bleio/Service.c`** -> AI Confidence: **99.31%**
209. **`ports/nordic/common-hal/_bleio/__init__.c`** -> AI Confidence: **99.31%**
210. **`ports/nordic/common-hal/_bleio/bonding.c`** -> AI Confidence: **99.31%**
211. **`ports/nordic/common-hal/alarm/__init__.c`** -> AI Confidence: **99.31%**
212. **`ports/nordic/common-hal/busio/I2C.c`** -> AI Confidence: **99.31%**
213. **`ports/nordic/common-hal/busio/UART.c`** -> AI Confidence: **99.31%**
214. **`ports/nordic/common-hal/microcontroller/Processor.c`** -> AI Confidence: **99.31%**
215. **`ports/nordic/common-hal/microcontroller/__init__.c`** -> AI Confidence: **99.31%**
216. **`ports/nordic/common-hal/os/__init__.c`** -> AI Confidence: **99.31%**
217. **`ports/nordic/common-hal/watchdog/WatchDogTimer.c`** -> AI Confidence: **99.31%**
218. **`ports/raspberrypi/audio_dma.c`** -> AI Confidence: **99.31%**
219. **`ports/raspberrypi/boards/bradanlanestudio_explorer_rp2040/board.c`** -> AI Confidence: **99.31%**
220. **`ports/raspberrypi/common-hal/alarm/__init__.c`** -> AI Confidence: **99.31%**
221. **`ports/raspberrypi/common-hal/analogio/AnalogIn.c`** -> AI Confidence: **99.31%**
222. **`ports/raspberrypi/common-hal/busio/SPI.c`** -> AI Confidence: **99.31%**
223. **`ports/raspberrypi/common-hal/mdns/Server.c`** -> AI Confidence: **99.31%**
224. **`ports/raspberrypi/common-hal/microcontroller/Processor.c`** -> AI Confidence: **99.31%**
225. **`ports/raspberrypi/common-hal/microcontroller/__init__.c`** -> AI Confidence: **99.31%**
226. **`ports/raspberrypi/common-hal/nvm/ByteArray.c`** -> AI Confidence: **99.31%**
227. **`ports/raspberrypi/common-hal/os/__init__.c`** -> AI Confidence: **99.31%**
228. **`ports/raspberrypi/common-hal/picodvi/__init__.c`** -> AI Confidence: **99.31%**
229. **`ports/raspberrypi/common-hal/socketpool/Socket.c`** -> AI Confidence: **99.31%**
230. **`ports/raspberrypi/common-hal/socketpool/SocketPool.c`** -> AI Confidence: **99.31%**
231. **`ports/raspberrypi/common-hal/socketpool/__init__.c`** -> AI Confidence: **99.31%**
232. **`ports/raspberrypi/common-hal/wifi/Radio.c`** -> AI Confidence: **99.31%**
233. **`ports/raspberrypi/supervisor/port.c`** -> AI Confidence: **99.31%**
234. **`ports/renode/common-hal/microcontroller/__init__.c`** -> AI Confidence: **99.31%**
235. **`ports/silabs/common-hal/_bleio/Characteristic.c`** -> AI Confidence: **99.31%**
236. **`ports/silabs/common-hal/_bleio/Connection.c`** -> AI Confidence: **99.31%**
237. **`ports/silabs/common-hal/_bleio/PacketBuffer.c`** -> AI Confidence: **99.31%**
238. **`ports/silabs/common-hal/_bleio/Service.c`** -> AI Confidence: **99.31%**
239. **`ports/stm/common-hal/analogio/AnalogIn.c`** -> AI Confidence: **99.31%**
240. **`ports/stm/common-hal/busio/UART.c`** -> AI Confidence: **99.31%**
241. **`ports/stm/common-hal/canio/CAN.c`** -> AI Confidence: **99.31%**
242. **`ports/stm/common-hal/canio/Listener.c`** -> AI Confidence: **99.31%**
243. **`ports/stm/common-hal/os/__init__.c`** -> AI Confidence: **99.31%**
244. **`ports/stm/common-hal/sdioio/SDCard.c`** -> AI Confidence: **99.31%**
245. **`ports/stm/peripherals/timers.c`** -> AI Confidence: **99.31%**
246. **`ports/unix/coverage.c`** -> AI Confidence: **99.31%**
247. **`ports/unix/modjni.c`** -> AI Confidence: **99.31%**
248. **`ports/unix/modos.c`** -> AI Confidence: **99.31%**
249. **`ports/unix/modtime.c`** -> AI Confidence: **99.31%**
250. **`ports/unix/mpconfigport.h`** -> AI Confidence: **99.31%**
251. **`ports/unix/mpthreadport.c`** -> AI Confidence: **99.31%**
252. **`ports/unix/unix_mphal.c`** -> AI Confidence: **99.31%**
253. **`ports/zephyr-cp/common-hal/_bleio/Adapter.c`** -> AI Confidence: **99.31%**
254. **`ports/zephyr-cp/common-hal/microcontroller/__init__.c`** -> AI Confidence: **99.31%**
255. **`ports/zephyr-cp/common-hal/rotaryio/IncrementalEncoder.c`** -> AI Confidence: **99.31%**
256. **`ports/zephyr-cp/common-hal/socketpool/Socket.c`** -> AI Confidence: **99.31%**
257. **`ports/zephyr-cp/common-hal/socketpool/SocketPool.c`** -> AI Confidence: **99.31%**
258. **`ports/zephyr-cp/common-hal/wifi/ScannedNetworks.c`** -> AI Confidence: **99.31%**
259. **`ports/zephyr-cp/common-hal/wifi/__init__.c`** -> AI Confidence: **99.31%**
260. **`py/asmrv32.c`** -> AI Confidence: **99.31%**
261. **`py/builtinimport.c`** -> AI Confidence: **99.31%**
262. **`py/emitbc.c`** -> AI Confidence: **99.31%**
263. **`py/emitinlinerv32.c`** -> AI Confidence: **99.31%**
264. **`py/emitinlinextensa.c`** -> AI Confidence: **99.31%**
265. **`py/gc.c`** -> AI Confidence: **99.31%**
266. **`py/malloc.c`** -> AI Confidence: **99.31%**
267. **`py/modbuiltins.c`** -> AI Confidence: **99.31%**
268. **`py/nativeglue.c`** -> AI Confidence: **99.31%**
269. **`py/obj.c`** -> AI Confidence: **99.31%**
270. **`py/objint.c`** -> AI Confidence: **99.31%**
271. **`py/objint_mpz.c`** -> AI Confidence: **99.31%**
272. **`py/parse.c`** -> AI Confidence: **99.31%**
273. **`py/runtime.c`** -> AI Confidence: **99.31%**
274. **`py/vstr.c`** -> AI Confidence: **99.31%**
275. **`shared-bindings/_bleio/Address.c`** -> AI Confidence: **99.31%**
276. **`shared-bindings/_bleio/Characteristic.c`** -> AI Confidence: **99.31%**
277. **`shared-bindings/_bleio/__init__.c`** -> AI Confidence: **99.31%**
278. **`shared-bindings/_stage/__init__.c`** -> AI Confidence: **99.31%**
279. **`shared-bindings/adafruit_pixelbuf/PixelBuf.c`** -> AI Confidence: **99.31%**
280. **`shared-bindings/alarm/time/TimeAlarm.c`** -> AI Confidence: **99.31%**
281. **`shared-bindings/audiocore/RawSample.c`** -> AI Confidence: **99.31%**
282. **`shared-bindings/audiocore/WaveFile.c`** -> AI Confidence: **99.31%**
283. **`shared-bindings/bitmaptools/__init__.c`** -> AI Confidence: **99.31%**
284. **`shared-bindings/busio/UART.c`** -> AI Confidence: **99.31%**
285. **`shared-bindings/digitalio/DigitalInOutProtocol.c`** -> AI Confidence: **99.31%**
286. **`shared-bindings/digitalio/Direction.c`** -> AI Confidence: **99.31%**
287. **`shared-bindings/displayio/Bitmap.c`** -> AI Confidence: **99.31%**
288. **`shared-bindings/displayio/Palette.c`** -> AI Confidence: **99.31%**
289. **`shared-bindings/displayio/TileGrid.c`** -> AI Confidence: **99.31%**
290. **`shared-bindings/displayio/__init__.c`** -> AI Confidence: **99.31%**
291. **`shared-bindings/floppyio/__init__.c`** -> AI Confidence: **99.31%**
292. **`shared-bindings/i2cioexpander/IOExpander.c`** -> AI Confidence: **99.31%**
293. **`shared-bindings/i2ctarget/I2CTarget.c`** -> AI Confidence: **99.31%**
294. **`shared-bindings/ipaddress/IPv4Address.c`** -> AI Confidence: **99.31%**
295. **`shared-bindings/jpegio/JpegDecoder.c`** -> AI Confidence: **99.31%**
296. **`shared-bindings/keypad/KeyMatrix.c`** -> AI Confidence: **99.31%**
297. **`shared-bindings/keypad/Keys.c`** -> AI Confidence: **99.31%**
298. **`shared-bindings/microcontroller/__init__.c`** -> AI Confidence: **99.31%**
299. **`shared-bindings/socketpool/Socket.c`** -> AI Confidence: **99.31%**
300. **`shared-bindings/spitarget/SPITarget.c`** -> AI Confidence: **99.31%**
301. **`shared-bindings/ssl/SSLSocket.c`** -> AI Confidence: **99.31%**
302. **`shared-bindings/supervisor/Runtime.c`** -> AI Confidence: **99.31%**
303. **`shared-bindings/terminalio/Terminal.c`** -> AI Confidence: **99.31%**
304. **`shared-bindings/tilepalettemapper/TilePaletteMapper.c`** -> AI Confidence: **99.31%**
305. **`shared-bindings/time/__init__.c`** -> AI Confidence: **99.31%**
306. **`shared-bindings/usb/core/__init__.c`** -> AI Confidence: **99.31%**
307. **`shared-module/adafruit_pixelbuf/PixelBuf.c`** -> AI Confidence: **99.31%**
308. **`shared-module/audiocore/__init__.c`** -> AI Confidence: **99.31%**
309. **`shared-module/audiofilters/Distortion.c`** -> AI Confidence: **99.31%**
310. **`shared-module/audiomp3/MP3Decoder.c`** -> AI Confidence: **99.31%**
311. **`shared-module/aurora_epaper/aurora_framebuffer.c`** -> AI Confidence: **99.31%**
312. **`shared-module/bitbangio/SPI.c`** -> AI Confidence: **99.31%**
313. **`shared-module/board/__init__.c`** -> AI Confidence: **99.31%**
314. **`shared-module/busdisplay/BusDisplay.c`** -> AI Confidence: **99.31%**
315. **`shared-module/displayio/TileGrid.c`** -> AI Confidence: **99.31%**
316. **`shared-module/displayio/bus_core.c`** -> AI Confidence: **99.31%**
317. **`shared-module/epaperdisplay/EPaperDisplay.c`** -> AI Confidence: **99.31%**
318. **`shared-module/gifio/GifWriter.c`** -> AI Confidence: **99.31%**
319. **`shared-module/i2cioexpander/IOExpander.c`** -> AI Confidence: **99.31%**
320. **`shared-module/is31fl3741/FrameBuffer.c`** -> AI Confidence: **99.31%**
321. **`shared-module/keypad_demux/DemuxKeyMatrix.c`** -> AI Confidence: **99.31%**
322. **`shared-module/lvfontio/OnDiskFont.c`** -> AI Confidence: **99.31%**
323. **`shared-module/msgpack/__init__.c`** -> AI Confidence: **99.31%**
324. **`shared-module/rgbmatrix/RGBMatrix.c`** -> AI Confidence: **99.31%**
325. **`shared-module/ssl/SSLSocket.c`** -> AI Confidence: **99.31%**
326. **`shared-module/synthio/__init__.c`** -> AI Confidence: **99.31%**
327. **`shared-module/uheap/__init__.c`** -> AI Confidence: **99.31%**
328. **`shared-module/usb/core/Device.c`** -> AI Confidence: **99.31%**
329. **`shared-module/usb_hid/Device.c`** -> AI Confidence: **99.31%**
330. **`shared-module/vectorio/Polygon.c`** -> AI Confidence: **99.31%**
331. **`shared-module/vectorio/VectorShape.c`** -> AI Confidence: **99.31%**
332. **`shared/libc/printf.c`** -> AI Confidence: **99.31%**
333. **`shared/netutils/dhcpserver.c`** -> AI Confidence: **99.31%**
334. **`supervisor/shared/bluetooth/bluetooth.c`** -> AI Confidence: **99.31%**
335. **`supervisor/shared/bluetooth/file_transfer.c`** -> AI Confidence: **99.31%**
336. **`supervisor/shared/display.c`** -> AI Confidence: **99.31%**
337. **`supervisor/shared/external_flash/external_flash.c`** -> AI Confidence: **99.31%**
338. **`supervisor/shared/fatfs.c`** -> AI Confidence: **99.31%**
339. **`supervisor/shared/serial.c`** -> AI Confidence: **99.31%**
340. **`supervisor/shared/settings.c`** -> AI Confidence: **99.31%**
341. **`supervisor/shared/status_leds.c`** -> AI Confidence: **99.31%**
342. **`supervisor/shared/tick.c`** -> AI Confidence: **99.31%**
343. **`supervisor/shared/translate/translate.c`** -> AI Confidence: **99.31%**
344. **`supervisor/shared/usb/host_keyboard.c`** -> AI Confidence: **99.31%**
345. **`supervisor/shared/usb/usb.c`** -> AI Confidence: **99.31%**
346. **`supervisor/shared/usb/usb_desc.c`** -> AI Confidence: **99.31%**
347. **`supervisor/shared/web_workflow/web_workflow.c`** -> AI Confidence: **99.31%**
348. **`supervisor/shared/web_workflow/websocket.c`** -> AI Confidence: **99.31%**
349. **`tests/circuitpython-manual/pwmio/code_extremes.py`** -> AI Confidence: **99.31%**
350. **`tests/circuitpython-manual/pwmio/code_ramps.py`** -> AI Confidence: **99.31%**
351. **`py/circuitpy_defns.mk`** -> AI Confidence: **99.29%**
352. **`ports/atmel-samd/tools/mkcandata.py`** -> AI Confidence: **99.29%**
353. **`ports/stm/hal_conf/sort_defines.py`** -> AI Confidence: **99.29%**
354. **`ports/stm/tools/parse_af_csv.py`** -> AI Confidence: **99.29%**
355. **`tests/basics/andor.py`** -> AI Confidence: **99.29%**
356. **`tests/basics/assign_expr_syntaxerror.py`** -> AI Confidence: **99.29%**
357. **`tests/basics/async_syntaxerror.py`** -> AI Confidence: **99.29%**
358. **`tests/basics/bit_length.py`** -> AI Confidence: **99.29%**
359. **`tests/basics/bool1.py`** -> AI Confidence: **99.29%**
360. **`tests/basics/builtin_allany.py`** -> AI Confidence: **99.29%**
361. **`tests/basics/builtin_chr.py`** -> AI Confidence: **99.29%**
362. **`tests/basics/builtin_divmod.py`** -> AI Confidence: **99.29%**
363. **`tests/basics/builtin_divmod_intbig.py`** -> AI Confidence: **99.29%**
364. **`tests/basics/builtin_eval.py`** -> AI Confidence: **99.29%**
365. **`tests/basics/builtin_eval_buffer.py`** -> AI Confidence: **99.29%**
366. **`tests/basics/builtin_eval_error.py`** -> AI Confidence: **99.29%**
367. **`tests/basics/builtin_exec_buffer.py`** -> AI Confidence: **99.29%**
368. **`tests/basics/builtin_filter.py`** -> AI Confidence: **99.29%**
369. **`tests/basics/builtin_map.py`** -> AI Confidence: **99.29%**
370. **`tests/basics/builtin_minmax.py`** -> AI Confidence: **99.29%**
371. **`tests/basics/builtin_ord.py`** -> AI Confidence: **99.29%**
372. **`tests/basics/builtin_pow3.py`** -> AI Confidence: **99.29%**
373. **`tests/basics/builtin_pow3_intbig.py`** -> AI Confidence: **99.29%**
374. **`tests/basics/builtin_range.py`** -> AI Confidence: **99.29%**
375. **`tests/basics/builtin_range_attrs.py`** -> AI Confidence: **99.29%**
376. **`tests/basics/builtin_range_binop.py`** -> AI Confidence: **99.29%**
377. **`tests/basics/builtin_round.py`** -> AI Confidence: **99.29%**
378. **`tests/basics/builtin_round_int.py`** -> AI Confidence: **99.29%**
379. **`tests/basics/builtin_round_intbig.py`** -> AI Confidence: **99.29%**
380. **`tests/basics/builtin_sorted.py`** -> AI Confidence: **99.29%**
381. **`tests/basics/builtin_str_hex.py`** -> AI Confidence: **99.29%**
382. **`tests/basics/builtin_sum.py`** -> AI Confidence: **99.29%**
383. **`tests/basics/builtin_super.py`** -> AI Confidence: **99.29%**
384. **`tests/basics/builtin_zip.py`** -> AI Confidence: **99.29%**
385. **`tests/basics/bytearray_add.py`** -> AI Confidence: **99.29%**
386. **`tests/basics/bytearray_add_self.py`** -> AI Confidence: **99.29%**
387. **`tests/basics/bytearray_append.py`** -> AI Confidence: **99.29%**
388. **`tests/basics/bytearray_construct.py`** -> AI Confidence: **99.29%**
389. **`tests/basics/bytearray_count.py`** -> AI Confidence: **99.29%**
390. **`tests/basics/bytearray_decode.py`** -> AI Confidence: **99.29%**
391. **`tests/basics/bytearray_partition.py`** -> AI Confidence: **99.29%**
392. **`tests/basics/bytearray_slice_assign.py`** -> AI Confidence: **99.29%**
393. **`tests/basics/bytes.py`** -> AI Confidence: **99.29%**
394. **`tests/basics/bytes_center.py`** -> AI Confidence: **99.29%**
395. **`tests/basics/bytes_construct.py`** -> AI Confidence: **99.29%**
396. **`tests/basics/bytes_format_modulo.py`** -> AI Confidence: **99.29%**
397. **`tests/basics/bytes_mult.py`** -> AI Confidence: **99.29%**
398. **`tests/basics/bytes_partition.py`** -> AI Confidence: **99.29%**
399. **`tests/basics/bytes_split.py`** -> AI Confidence: **99.29%**
400. **`tests/basics/comprehension1.py`** -> AI Confidence: **99.29%**
401. **`tests/basics/containment.py`** -> AI Confidence: **99.29%**
402. **`tests/basics/deque1.py`** -> AI Confidence: **99.29%**
403. **`tests/basics/dict1.py`** -> AI Confidence: **99.29%**
404. **`tests/basics/dict_copy.py`** -> AI Confidence: **99.29%**
405. **`tests/basics/dict_del.py`** -> AI Confidence: **99.29%**
406. **`tests/basics/dict_from_iter.py`** -> AI Confidence: **99.29%**
407. **`tests/basics/dict_get.py`** -> AI Confidence: **99.29%**
408. **`tests/basics/dict_iterator.py`** -> AI Confidence: **99.29%**
409. **`tests/basics/dict_pop.py`** -> AI Confidence: **99.29%**
410. **`tests/basics/dict_popitem.py`** -> AI Confidence: **99.29%**
411. **`tests/basics/dict_views.py`** -> AI Confidence: **99.29%**
412. **`tests/basics/except_match_tuple.py`** -> AI Confidence: **99.29%**
413. **`tests/basics/exceptpoly.py`** -> AI Confidence: **99.29%**
414. **`tests/basics/exceptpoly2.py`** -> AI Confidence: **99.29%**
415. **`tests/basics/for1.py`** -> AI Confidence: **99.29%**
416. **`tests/basics/for3.py`** -> AI Confidence: **99.29%**
417. **`tests/basics/for_else.py`** -> AI Confidence: **99.29%**
418. **`tests/basics/for_range.py`** -> AI Confidence: **99.29%**
419. **`tests/basics/frozenset1.py`** -> AI Confidence: **99.29%**
420. **`tests/basics/frozenset_add.py`** -> AI Confidence: **99.29%**
421. **`tests/basics/frozenset_binop.py`** -> AI Confidence: **99.29%**
422. **`tests/basics/frozenset_set.py`** -> AI Confidence: **99.29%**
423. **`tests/basics/fun_error2.py`** -> AI Confidence: **99.29%**
424. **`tests/basics/generator2.py`** -> AI Confidence: **99.29%**
425. **`tests/basics/generator_throw_nested.py`** -> AI Confidence: **99.29%**
426. **`tests/basics/ifcond.py`** -> AI Confidence: **99.29%**
427. **`tests/basics/ifexpr.py`** -> AI Confidence: **99.29%**
428. **`tests/basics/int_big1.py`** -> AI Confidence: **99.29%**
429. **`tests/basics/int_big_cmp.py`** -> AI Confidence: **99.29%**
430. **`tests/basics/int_big_div.py`** -> AI Confidence: **99.29%**
431. **`tests/basics/int_big_error.py`** -> AI Confidence: **99.29%**
432. **`tests/basics/int_big_lshift.py`** -> AI Confidence: **99.29%**
433. **`tests/basics/int_big_mod.py`** -> AI Confidence: **99.29%**
434. **`tests/basics/int_big_mul.py`** -> AI Confidence: **99.29%**
435. **`tests/basics/int_big_zeroone.py`** -> AI Confidence: **99.29%**
436. **`tests/basics/int_bytes.py`** -> AI Confidence: **99.29%**
437. **`tests/basics/int_constfolding.py`** -> AI Confidence: **99.29%**
438. **`tests/basics/int_divmod.py`** -> AI Confidence: **99.29%**
439. **`tests/basics/int_divzero.py`** -> AI Confidence: **99.29%**
440. **`tests/basics/int_length.py`** -> AI Confidence: **99.29%**
441. **`tests/basics/int_parse.py`** -> AI Confidence: **99.29%**
442. **`tests/basics/int_small.py`** -> AI Confidence: **99.29%**
443. **`tests/basics/lexer.py`** -> AI Confidence: **99.29%**
444. **`tests/basics/list1.py`** -> AI Confidence: **99.29%**
445. **`tests/basics/list_compare.py`** -> AI Confidence: **99.29%**
446. **`tests/basics/list_index.py`** -> AI Confidence: **99.29%**
447. **`tests/basics/list_mult.py`** -> AI Confidence: **99.29%**
448. **`tests/basics/list_pop.py`** -> AI Confidence: **99.29%**
449. **`tests/basics/list_remove.py`** -> AI Confidence: **99.29%**
450. **`tests/basics/list_reverse.py`** -> AI Confidence: **99.29%**
451. **`tests/basics/list_slice.py`** -> AI Confidence: **99.29%**
452. **`tests/basics/memoryerror.py`** -> AI Confidence: **99.29%**
453. **`tests/basics/memoryview1.py`** -> AI Confidence: **99.29%**
454. **`tests/basics/memoryview_gc.py`** -> AI Confidence: **99.29%**
455. **`tests/basics/memoryview_slice_assign.py`** -> AI Confidence: **99.29%**
456. **`tests/basics/namedtuple1.py`** -> AI Confidence: **99.29%**
457. **`tests/basics/op_error.py`** -> AI Confidence: **99.29%**
458. **`tests/basics/op_error_bytearray.py`** -> AI Confidence: **99.29%**
459. **`tests/basics/op_error_literal.py`** -> AI Confidence: **99.29%**
460. **`tests/basics/op_error_memoryview.py`** -> AI Confidence: **99.29%**
461. **`tests/basics/parser.py`** -> AI Confidence: **99.29%**
462. **`tests/basics/seq_unpack.py`** -> AI Confidence: **99.29%**
463. **`tests/basics/set_basic.py`** -> AI Confidence: **99.29%**
464. **`tests/basics/set_binop.py`** -> AI Confidence: **99.29%**
465. **`tests/basics/set_comprehension.py`** -> AI Confidence: **99.29%**
466. **`tests/basics/set_containment.py`** -> AI Confidence: **99.29%**
467. **`tests/basics/set_copy.py`** -> AI Confidence: **99.29%**
468. **`tests/basics/set_difference.py`** -> AI Confidence: **99.29%**
469. **`tests/basics/set_isfooset.py`** -> AI Confidence: **99.29%**
470. **`tests/basics/set_pop.py`** -> AI Confidence: **99.29%**
471. **`tests/basics/set_remove.py`** -> AI Confidence: **99.29%**
472. **`tests/basics/set_unop.py`** -> AI Confidence: **99.29%**
473. **`tests/basics/slice_op.py`** -> AI Confidence: **99.29%**
474. **`tests/basics/string1.py`** -> AI Confidence: **99.29%**
475. **`tests/basics/string_center.py`** -> AI Confidence: **99.29%**
476. **`tests/basics/string_endswith.py`** -> AI Confidence: **99.29%**
477. **`tests/basics/string_find.py`** -> AI Confidence: **99.29%**
478. **`tests/basics/string_format2.py`** -> AI Confidence: **99.29%**
479. **`tests/basics/string_format_error.py`** -> AI Confidence: **99.29%**
480. **`tests/basics/string_format_modulo.py`** -> AI Confidence: **99.29%**
481. **`tests/basics/string_format_modulo_int.py`** -> AI Confidence: **99.29%**
482. **`tests/basics/string_fstring_invalid.py`** -> AI Confidence: **99.29%**
483. **`tests/basics/string_index.py`** -> AI Confidence: **99.29%**
484. **`tests/basics/string_join.py`** -> AI Confidence: **99.29%**
485. **`tests/basics/string_mult.py`** -> AI Confidence: **99.29%**
486. **`tests/basics/string_partition.py`** -> AI Confidence: **99.29%**
487. **`tests/basics/string_replace.py`** -> AI Confidence: **99.29%**
488. **`tests/basics/string_repr.py`** -> AI Confidence: **99.29%**
489. **`tests/basics/string_rindex.py`** -> AI Confidence: **99.29%**
490. **`tests/basics/string_rpartition.py`** -> AI Confidence: **99.29%**
491. **`tests/basics/string_rsplit.py`** -> AI Confidence: **99.29%**
492. **`tests/basics/string_split.py`** -> AI Confidence: **99.29%**
493. **`tests/basics/string_splitlines.py`** -> AI Confidence: **99.29%**
494. **`tests/basics/string_startswith.py`** -> AI Confidence: **99.29%**
495. **`tests/basics/string_strip.py`** -> AI Confidence: **99.29%**
496. **`tests/basics/struct1.py`** -> AI Confidence: **99.29%**
497. **`tests/basics/struct2.py`** -> AI Confidence: **99.29%**
498. **`tests/basics/true_value.py`** -> AI Confidence: **99.29%**
499. **`tests/basics/try1.py`** -> AI Confidence: **99.29%**
500. **`tests/basics/try2.py`** -> AI Confidence: **99.29%**
501. **`tests/basics/try4.py`** -> AI Confidence: **99.29%**
502. **`tests/basics/try_else.py`** -> AI Confidence: **99.29%**
503. **`tests/basics/try_else_finally.py`** -> AI Confidence: **99.29%**
504. **`tests/basics/try_finally1.py`** -> AI Confidence: **99.29%**
505. **`tests/basics/tuple1.py`** -> AI Confidence: **99.29%**
506. **`tests/basics/tuple_compare.py`** -> AI Confidence: **99.29%**
507. **`tests/basics/tuple_index.py`** -> AI Confidence: **99.29%**
508. **`tests/basics/tuple_mult.py`** -> AI Confidence: **99.29%**
509. **`tests/basics/unpack1.py`** -> AI Confidence: **99.29%**
510. **`tests/basics/while1.py`** -> AI Confidence: **99.29%**
511. **`tests/cmdline/cmd_showbc_const.py`** -> AI Confidence: **99.29%**
512. **`tests/cmdline/repl_autoindent.py`** -> AI Confidence: **99.29%**
513. **`tests/cpydiff/syntax_assign_expr.py`** -> AI Confidence: **99.29%**
514. **`tests/cpydiff/syntax_spaces.py`** -> AI Confidence: **99.29%**
515. **`tests/cpydiff/types_exception_chaining.py`** -> AI Confidence: **99.29%**
516. **`tests/cpydiff/types_exception_loops.py`** -> AI Confidence: **99.29%**
517. **`tests/extmod/binascii_a2b_base64.py`** -> AI Confidence: **99.29%**
518. **`tests/extmod/binascii_unhexlify.py`** -> AI Confidence: **99.29%**
519. **`tests/extmod/json_dumps_separators.py`** -> AI Confidence: **99.29%**
520. **`tests/extmod/json_loads.py`** -> AI Confidence: **99.29%**
521. **`tests/extmod/re1.py`** -> AI Confidence: **99.29%**
522. **`tests/extmod/re_groups.py`** -> AI Confidence: **99.29%**
523. **`tests/extmod/re_namedclass.py`** -> AI Confidence: **99.29%**
524. **`tests/extmod/re_span.py`** -> AI Confidence: **99.29%**
525. **`tests/extmod/uctypes_array_load_store.py`** -> AI Confidence: **99.29%**
526. **`tests/feature_check/bytearray.py`** -> AI Confidence: **99.29%**
527. **`tests/feature_check/complex.py`** -> AI Confidence: **99.29%**
528. **`tests/feature_check/coverage.py`** -> AI Confidence: **99.29%**
529. **`tests/feature_check/float.py`** -> AI Confidence: **99.29%**
530. **`tests/feature_check/slice.py`** -> AI Confidence: **99.29%**
531. **`tests/float/builtin_float_abs.py`** -> AI Confidence: **99.29%**
532. **`tests/float/builtin_float_minmax.py`** -> AI Confidence: **99.29%**
533. **`tests/float/builtin_float_round_intbig.py`** -> AI Confidence: **99.29%**
534. **`tests/float/cmath_fun.py`** -> AI Confidence: **99.29%**
535. **`tests/float/cmath_fun_special.py`** -> AI Confidence: **99.29%**
536. **`tests/float/complex1.py`** -> AI Confidence: **99.29%**
537. **`tests/float/float1.py`** -> AI Confidence: **99.29%**
538. **`tests/float/float2int_doubleprec_intbig.py`** -> AI Confidence: **99.29%**
539. **`tests/float/float2int_fp30_intbig.py`** -> AI Confidence: **99.29%**
540. **`tests/float/float2int_intbig.py`** -> AI Confidence: **99.29%**
541. **`tests/float/float_format.py`** -> AI Confidence: **99.29%**
542. **`tests/float/float_format_ints.py`** -> AI Confidence: **99.29%**
543. **`tests/float/float_format_ints_power10.py`** -> AI Confidence: **99.29%**
544. **`tests/float/float_parse.py`** -> AI Confidence: **99.29%**
545. **`tests/float/inf_nan_arith.py`** -> AI Confidence: **99.29%**
546. **`tests/float/int_big_float.py`** -> AI Confidence: **99.29%**
547. **`tests/float/int_divzero.py`** -> AI Confidence: **99.29%**
548. **`tests/float/list_index.py`** -> AI Confidence: **99.29%**
549. **`tests/float/math_domain.py`** -> AI Confidence: **99.29%**
550. **`tests/float/math_domain_python311.py`** -> AI Confidence: **99.29%**
551. **`tests/float/math_domain_special.py`** -> AI Confidence: **99.29%**
552. **`tests/float/string_format_modulo2.py`** -> AI Confidence: **99.29%**
553. **`tests/float/string_format_modulo2_intbig.py`** -> AI Confidence: **99.29%**
554. **`tests/float/true_value.py`** -> AI Confidence: **99.29%**
555. **`tests/inlineasm/rv32/asmsanity.py`** -> AI Confidence: **99.29%**
556. **`tests/io/file1.py`** -> AI Confidence: **99.29%**
557. **`tests/io/file_iter.py`** -> AI Confidence: **99.29%**
558. **`tests/io/file_readinto.py`** -> AI Confidence: **99.29%**
559. **`tests/io/file_readline.py`** -> AI Confidence: **99.29%**
560. **`tests/io/file_seek.py`** -> AI Confidence: **99.29%**
561. **`tests/micropython/native_try_deep.py`** -> AI Confidence: **99.29%**
562. **`tests/micropython/viper_binop_comp.py`** -> AI Confidence: **99.29%**
563. **`tests/micropython/viper_binop_multi_comp.py`** -> AI Confidence: **99.29%**
564. **`tests/micropython/viper_globals.py`** -> AI Confidence: **99.29%**
565. **`tests/misc/non_compliant_lexer.py`** -> AI Confidence: **99.29%**
566. **`tests/stress/dict_copy.py`** -> AI Confidence: **99.29%**
567. **`tests/stress/dict_create.py`** -> AI Confidence: **99.29%**
568. **`tests/stress/gc_trace.py`** -> AI Confidence: **99.29%**
569. **`tests/stress/recursive_iternext.py`** -> AI Confidence: **99.29%**
570. **`tests/unicode/file2.py`** -> AI Confidence: **99.29%**
571. **`tests/unicode/file_invalid.py`** -> AI Confidence: **99.29%**
572. **`tests/unicode/unicode.py`** -> AI Confidence: **99.29%**
573. **`tests/unicode/unicode_iter.py`** -> AI Confidence: **99.29%**
574. **`tests/unicode/unicode_subscr.py`** -> AI Confidence: **99.29%**
575. **`tools/cortex-m-fault-gdb.py`** -> AI Confidence: **99.29%**
576. **`tools/mpconfig_category_reader.py`** -> AI Confidence: **99.29%**
577. **`devices/ble_hci/supervisor/bluetooth.c`** -> AI Confidence: **99.29%**
578. **`ports/espressif/boards/arduino_nano_esp32s3/mpconfigboard.h`** -> AI Confidence: **99.29%**
579. **`ports/espressif/boards/arduino_nano_esp32s3_inverted_statusled/mpconfigboard.h`** -> AI Confidence: **99.29%**
580. **`ports/espressif/common-hal/memorymap/AddressRange.c`** -> AI Confidence: **99.29%**
581. **`ports/mimxrt10xx/boards/imxrt1050_evkb/pins.c`** -> AI Confidence: **99.29%**
582. **`ports/mimxrt10xx/boards/imxrt1060_evk/pins.c`** -> AI Confidence: **99.29%**
583. **`ports/mimxrt10xx/boards/imxrt1060_evkb/pins.c`** -> AI Confidence: **99.29%**
584. **`ports/mimxrt10xx/common-hal/neopixel_write/__init__.c`** -> AI Confidence: **99.29%**
585. **`ports/nordic/boards/Seeed_XIAO_nRF52840_Sense/mpconfigboard.h`** -> AI Confidence: **99.29%**
586. **`ports/nordic/boards/TG-Watch/mpconfigboard.h`** -> AI Confidence: **99.29%**
587. **`ports/nordic/boards/adafruit_led_glasses_nrf52840/mpconfigboard.h`** -> AI Confidence: **99.29%**
588. **`ports/nordic/boards/bastble/mpconfigboard.h`** -> AI Confidence: **99.29%**
589. **`ports/nordic/boards/challenger_840/mpconfigboard.h`** -> AI Confidence: **99.29%**
590. **`ports/nordic/boards/circuitplayground_bluefruit/mpconfigboard.h`** -> AI Confidence: **99.29%**
591. **`ports/nordic/boards/clue_nrf52840_express/mpconfigboard.h`** -> AI Confidence: **99.29%**
592. **`ports/nordic/boards/espruino_banglejs2/mpconfigboard.h`** -> AI Confidence: **99.29%**
593. **`ports/nordic/boards/feather_bluefruit_sense/mpconfigboard.h`** -> AI Confidence: **99.29%**
594. **`ports/nordic/boards/feather_nrf52840_express/mpconfigboard.h`** -> AI Confidence: **99.29%**
595. **`ports/nordic/boards/hiibot_bluefi/mpconfigboard.h`** -> AI Confidence: **99.29%**
596. **`ports/nordic/boards/itsybitsy_nrf52840_express/mpconfigboard.h`** -> AI Confidence: **99.29%**
597. **`ports/nordic/boards/makerdiary_nrf52840_connectkit/mpconfigboard.h`** -> AI Confidence: **99.29%**
598. **`ports/nordic/boards/metro_nrf52840_express/mpconfigboard.h`** -> AI Confidence: **99.29%**
599. **`ports/nordic/boards/ohs2020_badge/mpconfigboard.h`** -> AI Confidence: **99.29%**
600. **`ports/nordic/boards/omnimo_nrf52840/mpconfigboard.h`** -> AI Confidence: **99.29%**
601. **`ports/nordic/boards/particle_argon/mpconfigboard.h`** -> AI Confidence: **99.29%**
602. **`ports/nordic/boards/particle_boron/mpconfigboard.h`** -> AI Confidence: **99.29%**
603. **`ports/nordic/boards/particle_xenon/mpconfigboard.h`** -> AI Confidence: **99.29%**
604. **`ports/nordic/boards/pca10056/mpconfigboard.h`** -> AI Confidence: **99.29%**
605. **`ports/nordic/boards/simmel/mpconfigboard.h`** -> AI Confidence: **99.29%**
606. **`ports/nordic/boards/sparkfun_nrf52840_micromod/mpconfigboard.h`** -> AI Confidence: **99.29%**
607. **`ports/nordic/boards/tinkeringtech_scoutmakes_azul/mpconfigboard.h`** -> AI Confidence: **99.29%**
608. **`ports/nordic/common-hal/_bleio/Attribute.c`** -> AI Confidence: **99.29%**
609. **`ports/nordic/common-hal/memorymap/AddressRange.c`** -> AI Confidence: **99.29%**
610. **`ports/raspberrypi/common-hal/memorymap/AddressRange.c`** -> AI Confidence: **99.29%**
611. **`ports/raspberrypi/common-hal/picodvi/Framebuffer.h`** -> AI Confidence: **99.29%**
612. **`ports/stm/boards/system_stm32f4xx.c`** -> AI Confidence: **99.29%**
613. **`ports/stm/boards/system_stm32f7xx.c`** -> AI Confidence: **99.29%**
614. **`ports/stm/boards/system_stm32h7xx.c`** -> AI Confidence: **99.29%**
615. **`ports/stm/boards/system_stm32l4xx.c`** -> AI Confidence: **99.29%**
616. **`ports/zephyr-cp/common-hal/zephyr_kernel/__init__.c`** -> AI Confidence: **99.29%**
617. **`py/emitnx86.c`** -> AI Confidence: **99.29%**
618. **`py/modarray.c`** -> AI Confidence: **99.29%**
619. **`py/modcollections.c`** -> AI Confidence: **99.29%**
620. **`py/mpstate.c`** -> AI Confidence: **99.29%**
621. **`py/nlrpowerpc.c`** -> AI Confidence: **99.29%**
622. **`py/nlrthumb.c`** -> AI Confidence: **99.29%**
623. **`py/nlrx64.c`** -> AI Confidence: **99.29%**
624. **`py/objslice.c`** -> AI Confidence: **99.29%**
625. **`py/qstrdefs.h`** -> AI Confidence: **99.29%**
626. **`py/showbc.c`** -> AI Confidence: **99.29%**
627. **`py/vmentrytable.h`** -> AI Confidence: **99.29%**
628. **`shared-bindings/microcontroller/RunMode.c`** -> AI Confidence: **99.29%**
629. **`shared-module/_stage/Layer.c`** -> AI Confidence: **99.29%**
630. **`shared-module/rainbowio/__init__.c`** -> AI Confidence: **99.29%**
631. **`shared-module/supervisor/__init__.c`** -> AI Confidence: **99.29%**
632. **`shared-module/usb_video/descriptor.c`** -> AI Confidence: **99.29%**
633. **`shared/netutils/trace.c`** -> AI Confidence: **99.29%**
634. **`shared/runtime/buffer_helper.c`** -> AI Confidence: **99.29%**
635. **`supervisor/shared/usb/tusb_config.h`** -> AI Confidence: **99.29%**
636. **`extmod/lwip-include/lwipopts_common.h`** -> AI Confidence: **99.29%**
637. **`ports/atmel-samd/sd_mmc/sd_mmc_protocol.h`** -> AI Confidence: **99.29%**
638. **`ports/broadcom/mpconfigport.h`** -> AI Confidence: **99.29%**
639. **`ports/espressif/module/cardputer_keymap.h`** -> AI Confidence: **99.29%**
640. **`ports/nordic/bluetooth/s140_nrf52_6.1.0/s140_nrf52_6.1.0_API/include/nrf_svc.h`** -> AI Confidence: **99.29%**
641. **`ports/nordic/nrfx_config.h`** -> AI Confidence: **99.29%**
642. **`ports/raspberrypi/lwip_inc/lwipopts.h`** -> AI Confidence: **99.29%**
643. **`ports/silabs/mpconfigport.h`** -> AI Confidence: **99.29%**
644. **`ports/unix/mbedtls/mbedtls_config_port.h`** -> AI Confidence: **99.29%**
645. **`ports/unix/variants/mpconfigvariant_common.h`** -> AI Confidence: **99.29%**
646. **`shared-module/qrio/quirc_alloc.h`** -> AI Confidence: **99.29%**
647. **`ports/zephyr-cp/cptools/zephyr2cp.py`** -> AI Confidence: **99.28%**
648. **`supervisor/shared/translate/translate.h`** -> AI Confidence: **99.27%**
649. **`supervisor/shared/translate/translate_impl.h`** -> AI Confidence: **99.27%**
650. **`tools/build_board_info.py`** -> AI Confidence: **99.25%**
651. **`tools/pyboard.py`** -> AI Confidence: **99.25%**
652. **`py/emitnative.c`** -> AI Confidence: **99.25%**
653. **`py/circuitpy_mkenv.mk`** -> AI Confidence: **99.24%**
654. **`conf.py`** -> AI Confidence: **99.24%**
655. **`tests/extmod/vfs_rom.py`** -> AI Confidence: **99.24%**
656. **`tools/ar_util.py`** -> AI Confidence: **99.24%**
657. **`tools/ruff_bindings.py`** -> AI Confidence: **99.24%**
658. **`devices/ble_hci/common-hal/_bleio/CharacteristicBuffer.c`** -> AI Confidence: **99.24%**
659. **`ports/atmel-samd/bindings/samd/Clock.c`** -> AI Confidence: **99.24%**
660. **`ports/atmel-samd/common-hal/canio/CAN.c`** -> AI Confidence: **99.24%**
661. **`ports/atmel-samd/common-hal/sdioio/SDCard.c`** -> AI Confidence: **99.24%**
662. **`ports/atmel-samd/sd_mmc/sd_mmc.c`** -> AI Confidence: **99.24%**
663. **`ports/cxd56/common-hal/busio/UART.c`** -> AI Confidence: **99.24%**
664. **`ports/cxd56/common-hal/microcontroller/__init__.c`** -> AI Confidence: **99.24%**
665. **`ports/espressif/common-hal/_bleio/CharacteristicBuffer.c`** -> AI Confidence: **99.24%**
666. **`ports/espressif/common-hal/_bleio/__init__.c`** -> AI Confidence: **99.24%**
667. **`ports/espressif/common-hal/canio/Listener.c`** -> AI Confidence: **99.24%**
668. **`ports/espressif/common-hal/espnow/ESPNow.c`** -> AI Confidence: **99.24%**
669. **`ports/espressif/common-hal/qspibus/QSPIBus.c`** -> AI Confidence: **99.24%**
670. **`ports/espressif/supervisor/port.c`** -> AI Confidence: **99.24%**
671. **`ports/espressif/supervisor/usb.c`** -> AI Confidence: **99.24%**
672. **`ports/mimxrt10xx/common-hal/microcontroller/__init__.c`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `tools/gen_crt_bundle.py` -> **99.3517%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `15698` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `shared-module/busdisplay/BusDisplay.c` (C) -> Cumulative Risk: **759.95**
- **Archetype:** `file_cluster_13` (Distance: 13.606 IQR)
- **Magnitude:** 375.58 | **LOC:** 444 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `common_hal_busdisplay_busdisplay_set_bri` (Impact: 21.6), `common_hal_busdisplay_busdisplay_constru` (Impact: 19.2), `common_hal_busdisplay_busdisplay_refresh` (Impact: 8.2)

### 2. `ports/zephyr-cp/supervisor/port.c` (C) -> Cumulative Risk: **753.14**
- **Archetype:** `file_cluster_13` (Distance: 12.969 IQR)
- **Magnitude:** 279.76 | **LOC:** 386 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 90.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (99.2138%)
- **Heaviest Functions:** `port_realloc` (Impact: 15.1), `port_free` (Impact: 11.1), `perfetto_emit_outer_heap_stats` (Impact: 7.8)

### 3. `ports/unix/mpthreadport.c` (C) -> Cumulative Risk: **727.63**
- **Archetype:** `file_cluster_13` (Distance: 12.919 IQR)
- **Magnitude:** 233.26 | **LOC:** 378 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.548%), Safety Score (89.4951%)
- **Heaviest Functions:** `mp_thread_gc_others` (Impact: 12.3), `mp_thread_start` (Impact: 9.4), `mp_thread_finish` (Impact: 9.3)

### 4. `shared-module/displayio/TileGrid.c` (C) -> Cumulative Risk: **722.91**
- **Archetype:** `file_cluster_13` (Distance: 14.198 IQR)
- **Magnitude:** 802.68 | **LOC:** 735 | **CtrlFlow:** 50.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9636%)
- **Heaviest Functions:** `displayio_tilegrid_get_refresh_areas` (Impact: 30.8), `common_hal_displayio_tilegrid_construct` (Impact: 19.5), `displayio_tilegrid_finish_refresh` (Impact: 14.3)

### 5. `py/mpz.c` (C) -> Cumulative Risk: **707.45**
- **Archetype:** `file_cluster_11` (Distance: 15.65 IQR)
- **Magnitude:** 1897.24 | **LOC:** 1757 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.5281%)
- **Heaviest Functions:** `mpz_set_from_bytes` (Impact: 175.1), `mpz_as_str_inpl` (Impact: 23.1), `mpn_div` (Impact: 22.9)

### 6. `ports/raspberrypi/common-hal/rp2pio/StateMachine.c` (C) -> Cumulative Risk: **707.18**
- **Archetype:** `file_cluster_13` (Distance: 13.93 IQR)
- **Magnitude:** 1236.6 | **LOC:** 1537 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.1208%)
- **Heaviest Functions:** `_transfer` (Impact: 124.4), `consider_instruction` (Impact: 41.5), `common_hal_rp2pio_statemachine_backgroun` (Impact: 25.1)

### 7. `shared-module/audiodelays/Chorus.c` (C) -> Cumulative Risk: **703.15**
- **Archetype:** `file_cluster_13` (Distance: 13.932 IQR)
- **Magnitude:** 323.14 | **LOC:** 341 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.0367%)
- **Heaviest Functions:** `audiodelays_chorus_get_buffer` (Impact: 40.5), `common_hal_audiodelays_chorus_construct` (Impact: 11.3), `common_hal_audiodelays_chorus_deinited` (Impact: 2.3)

### 8. `supervisor/shared/filesystem.c` (C) -> Cumulative Risk: **702.33**
- **Archetype:** `file_cluster_13` (Distance: 12.657 IQR)
- **Magnitude:** 177.36 | **LOC:** 344 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.9255%)
- **Heaviest Functions:** `filesystem_for_path` (Impact: 9.7), `filesystem_tick` (Impact: 6.3), `filesystem_set_writable_by_usb` (Impact: 3.4)

### 9. `ports/broadcom/common-hal/sdioio/SDCard.c` (C) -> Cumulative Risk: **699.87**
- **Archetype:** `file_cluster_13` (Distance: 13.789 IQR)
- **Magnitude:** 483.24 | **LOC:** 433 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.8606%)
- **Heaviest Functions:** `_do_transaction` (Impact: 71.7), `_set_card_clk` (Impact: 20.9), `common_hal_sdioio_sdcard_construct` (Impact: 12.8)

### 10. `ports/zephyr-cp/cptools/build_circuitpython.py` (PYTHON) -> Cumulative Risk: **699.11**
- **Archetype:** `file_cluster_4` (Distance: 11.68 IQR)
- **Magnitude:** 514.78 | **LOC:** 651 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9948%), Cognitive Load (96.3099%)
- **Heaviest Functions:** `build_circuitpython` (Impact: 148.3), `determine_enabled_modules` (Impact: 30.5), `preprocess_and_split_defs` (Impact: 7.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `ports/nordic/espruino_dfu_private_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/circuitpy_defns.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.072 IQR)
- **Top Global Matches:** file_cluster_8: 12.072, file_cluster_17: 12.53, file_cluster_7: 12.669
- **Magnitude:** 3954.96 | **LOC:** 1073 | **CtrlFlow:** 93.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (78.5764%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 22`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 468`, `dead_code: 2`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/espressif/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.253 IQR)
- **Top Global Matches:** file_cluster_8: 12.253, file_cluster_17: 12.41, file_cluster_13: 12.659
- **Magnitude:** 2669.36 | **LOC:** 924 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 78.6%
- **Risk Profile:** Cognitive Load (52.2824%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 98`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 235`, `state_mutation: 359`, `dead_code: 4`
* *Architecture:* `io: 10`, `api: 4`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` circuitpy_mkenv.mk, mkrules.mk
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/objstr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.394 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.604 IQR)
- **Top Global Matches:** file_cluster_8: 14.394, file_cluster_11: 14.427, file_cluster_0: 14.45
- **Magnitude:** 2408.32 | **LOC:** 2512 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.7077%), Tech Debt (15.8435%)
**Top Internal Functions/Classes:**
  * `mp_obj_str_format_helper` (Impact: 605.2)
  * `str_modulo_format` (Impact: 95.2)
  * `bytes_make_new` (Impact: 48.1)
  * `str_uni_strip` (Impact: 35.4)
  * `mp_obj_str_split` (Impact: 32.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 518`, `structural_boundaries: 139`, `args: 10`, `func_start: 54`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 989`, `dead_code: 5`, `planned_debt: 4`, `orphaned_logic: 6`
* *Architecture:* `api: 287`, `import: 7`
* *Defense:* `safety: 68`, `doc: 1`, `test: 5`, `immutability_locks: 115`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` string.h, runtime.h, objlist.h, objstr.h, assert.h, cstack.h, unicode.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/mpz.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.65 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.896 IQR)
- **Top Global Matches:** file_cluster_11: 15.65, file_cluster_0: 15.665, file_cluster_8: 15.693
- **Magnitude:** 1897.24 | **LOC:** 1757 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (91.118%), Tech Debt (92.3348%)
**Top Internal Functions/Classes:**
  * `mpz_set_from_bytes` (Impact: 175.1)
  * `mpz_as_str_inpl` (Impact: 23.1)
    * *Intent:* /* computes dest = lhs << rhs
  * `mpn_div` (Impact: 22.9)
    * *Intent:* *idig = *jdig ^ *kdig;
  * `mpz_as_bytes` (Impact: 20.4)
  * `mpz_set_from_float` (Impact: 19.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 90`, `args: 4`, `func_start: 47`
* *Risk/State:* `state_mutation: 1231`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 2`, `orphaned_logic: 25`
* *Architecture:* `api: 196`, `import: 3`
* *Defense:* `safety: 65`, `test: 8`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mpz.h, assert.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/tjpgd/src/tjpgd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.84 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.273 IQR)
- **Top Global Matches:** file_cluster_8: 14.84, file_cluster_13: 15.085, file_cluster_11: 15.093
- **Magnitude:** 1748.5 | **LOC:** 1158 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.5359%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `huffext` (Impact: 44.6)
    * *Intent:* ti = ph[i] << (HUFF_BIT - 1 - b) & HUFF_MASK; /* Index of input pattern for the code */
  * `mcu_load` (Impact: 33.9)
  * `create_huffman_tbl` (Impact: 29.0)
    * *Intent:* while (ndata) { /* Process all tables in the segment */
  * `bitext` (Impact: 28.9)
    * *Intent:* #endif for ( ; bl <= 16; bl++) { /* Incremental search */
  * `restart` (Impact: 19.1)
    * *Intent:* if (flg) { /* In flag sequence? */ flg = 0; /* Exit flag sequence */ if (d != 0) jd->marker = d; /* ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 88`, `args: 1`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1448`
* *Architecture:* `api: 109`, `import: 1`
* *Defense:* `safety: 12`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tjpgd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/compile.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.384 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.931 IQR)
- **Top Global Matches:** file_cluster_11: 14.384, file_cluster_13: 14.444, file_cluster_0: 14.474
- **Magnitude:** 1506.92 | **LOC:** 3703 | **CtrlFlow:** 79.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.1524%), Tech Debt (42.2134%)
**Top Internal Functions/Classes:**
  * `compile_scope_inline_asm` (Impact: 65.7)
  * `scope_compute_things` (Impact: 64.0)
  * `c_assign` (Impact: 46.3)
  * `compile_scope_func_lambda_param` (Impact: 45.9)
  * `compile_funcdef_lambdef_param` (Impact: 40.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 466`, `structural_boundaries: 124`, `args: 2`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 736`, `dead_code: 13`, `planned_debt: 3`, `orphaned_logic: 19`
* *Architecture:* `api: 163`, `import: 16`
* *Defense:* `safety: 50`, `test: 32`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` string.h, runtime.h, scope.h, emit.h, nativeglue.h, smallint.h, assert.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/qstr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.616 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.896 IQR)
- **Top Global Matches:** file_cluster_13: 14.616, file_cluster_11: 14.811, file_cluster_0: 14.823
- **Magnitude:** 1483.65 | **LOC:** 561 | **CtrlFlow:** 75.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.7011%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 14`, `args: 6`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 196`, `dead_code: 1`
* *Architecture:* `api: 32`, `import: 7`
* *Defense:* `safety: 12`, `test: 2`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` string.h, runtime.h, qstr.h, assert.h, stdio.h, qstrdefs.generated.h, compressed.data.h, gc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/emitnative.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.88 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.601 IQR)
- **Top Global Matches:** file_cluster_13: 13.88, file_cluster_8: 13.888, file_cluster_0: 13.937
- **Magnitude:** 1353.64 | **LOC:** 3238 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.5699%), Tech Debt (9.1743%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 37`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 244`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `api: 39`, `import: 7`
* *Defense:* `safety: 23`, `test: 10`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` string.h, objstr.h, nativeglue.h, emit.h, assert.h, stdio.h, objfun.h
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `ports/nordic/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.025 IQR)
- **Top Global Matches:** file_cluster_17: 13.025, file_cluster_13: 13.484, file_cluster_11: 13.517
- **Magnitude:** 1265.24 | **LOC:** 287 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (52.224%), Tech Debt (17.3049%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 23`, `args: 8`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 117`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 3`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` circuitpy_mkenv.mk, mkrules.mk
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/raspberrypi/common-hal/rp2pio/StateMachine.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.93 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.906 IQR)
- **Top Global Matches:** file_cluster_13: 13.93, file_cluster_8: 13.998, file_cluster_11: 14.06
- **Magnitude:** 1236.6 | **LOC:** 1537 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (92.6538%), Tech Debt (99.1208%)
**Top Internal Functions/Classes:**
  * `_transfer` (Impact: 124.4)
  * `consider_instruction` (Impact: 41.5)
  * `common_hal_rp2pio_statemachine_backgroun` (Impact: 25.1)
  * `common_hal_rp2pio_statemachine_backgroun` (Impact: 25.0)
  * `common_hal_rp2pio_statemachine_construct` (Impact: 14.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 232`, `args: 7`, `func_start: 49`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 592`, `dead_code: 2`, `planned_debt: 3`, `duplicate_logic: 8`, `orphaned_logic: 24`
* *Architecture:* `api: 230`, `import: 17`
* *Defense:* `safety: 31`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` AddressRange.h, __init__.h, string.h, platform_defs.h, dma.h, clocks.h, pio_instructions.h, runtime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/profile.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.635 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.805 IQR)
- **Top Global Matches:** file_cluster_13: 14.635, file_cluster_11: 14.671, file_cluster_8: 14.68
- **Magnitude:** 1138.1 | **LOC:** 846 | **CtrlFlow:** 86.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.7087%), Tech Debt (29.747%)
**Top Internal Functions/Classes:**
  * `mp_prof_opcode_decode` (Impact: 182.9)
    * *Intent:* /******************************************************************************/ // DEBUG // This se...
  * `frame_attr` (Impact: 15.4)
  * `mp_prof_instr_tick` (Impact: 10.8)
  * `mp_prof_frame_enter` (Impact: 6.8)
  * `mp_prof_print_instr` (Impact: 6.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 33`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `state_mutation: 732`, `dead_code: 3`, `planned_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 150`, `import: 5`
* *Defense:* `safety: 12`, `doc: 3`, `test: 8`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` runtime0.h, objfun.h, profile.h, bc0.h, gc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/run-tests.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.83 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.273 IQR)
- **Top Global Matches:** file_cluster_8: 10.83, file_cluster_13: 11.075, file_cluster_7: 11.301
- **Magnitude:** 1094.52 | **LOC:** 1356 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.5461%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_micropython` (Impact: 597.2)
  * `run_one_test` (Impact: 244.7)
  * `prepare_script_for_target` (Impact: 36.3)
  * `get_test_instance` (Impact: 25.8)
  * `run_script_on_remote_target` (Impact: 14.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 116`, `args: 27`, `func_start: 26`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 82`, `dead_code: 1`
* *Architecture:* `io: 80`, `api: 26`, `concurrency: 11`, `import: 17`
* *Defense:* `safety: 27`, `doc: 6`, `test: 8`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` sysconfig, multiprocessing, pyboard, tempfile, __injected_test, glob, vfs, platform...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devices/ble_hci/common-hal/_bleio/att.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 19.542 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.031 IQR)
- **Top Global Matches:** file_cluster_0: 19.542, file_cluster_9: 19.553, file_cluster_11: 19.58
- **Magnitude:** 1006.36 | **LOC:** 1802 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.9175%), Tech Debt (39.7986%)
**Top Internal Functions/Classes:**
  * `att_process_data` (Impact: 49.6)
  * `check_att_err` (Impact: 45.6)
  * `process_read_or_read_blob_req` (Impact: 25.9)
  * `att_remove_connection` (Impact: 11.5)
    * *Intent:* // if (service == NULL) { // return false; // } // device->addService(service); // } // reqStart_han...
  * `att_disconnect_all` (Impact: 9.6)
    * *Intent:* // BLERemoteCharacteristic* nextCharacteristic = (j == (characteristicCount - 1)) ? NULL : service->...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 184`, `args: 3`, `func_start: 33`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 529`, `dead_code: 63`, `orphaned_logic: 15`
* *Architecture:* `api: 203`
* *Defense:* `safety: 26`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` UUID.h, tick.h, Attribute.h, l2cap_internal.h, Characteristic.h, Service.h, Adapter.h, att_internal.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/modsys.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.372 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.316 IQR)
- **Top Global Matches:** file_cluster_8: 11.372, file_cluster_13: 11.4, file_cluster_7: 11.938
- **Magnitude:** 975.66 | **LOC:** 385 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.0112%), Tech Debt (11.0389%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 10`, `args: 1`, `func_start: 5`
* *Risk/State:* `state_mutation: 53`, `planned_debt: 1`
* *Architecture:* `api: 19`, `import: 18`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` persistentcode.h, objtype.h, modplatform.h, runtime.h, profile.h, objlist.h, objstr.h, stream.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/unix/main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.659 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.903 IQR)
- **Top Global Matches:** file_cluster_13: 13.659, file_cluster_11: 13.944, file_cluster_8: 14.017
- **Magnitude:** 975.64 | **LOC:** 839 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (95.7447%), Tech Debt (12.4936%)
**Top Internal Functions/Classes:**
  * `pre_process_options` (Impact: 198.1)
  * `main_` (Impact: 143.1)
    * *Intent:* // Don't bring unneeded libc dependencies like tolower() // If there's 'w' immediately after number,...
  * `do_repl` (Impact: 59.4)
  * `execute_from_lexer` (Impact: 34.2)
    * *Intent:* #define FORCED_EXIT (0x100) // If exc is SystemExit, return value where FORCED_EXIT bit set, // and ...
  * `print_help` (Impact: 21.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 58`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 412`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 76`, `import: 29`
* *Defense:* `safety: 4`, `test: 1`, `immutability_locks: 15`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` mphal.h, signal.h, stdio.h, compile.h, stdarg.h, stdlib.h, stdbool.h, gc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/emitinlinethumb.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.621 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.123 IQR)
- **Top Global Matches:** file_cluster_8: 13.621, file_cluster_11: 13.623, file_cluster_13: 13.628
- **Magnitude:** 960.42 | **LOC:** 866 | **CtrlFlow:** 80.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (99.4553%), Tech Debt (9.6922%)
**Top Internal Functions/Classes:**
  * `emit_inline_thumb_op` (Impact: 229.6)
  * `get_arg_reglist` (Impact: 17.6)
  * `get_arg_vfpreg` (Impact: 10.3)
  * `get_arg_reg` (Impact: 10.2)
  * `get_arg_addr` (Impact: 8.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 67`, `func_start: 19`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 467`, `dead_code: 2`, `planned_debt: 3`
* *Architecture:* `api: 162`, `import: 9`
* *Defense:* `safety: 5`, `test: 3`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` string.h, emit.h, assert.h, stdio.h, asmthumb.h, grammar.h, stdarg.h, stdint.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shared-module/bitmaptools/__init__.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.298 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.574 IQR)
- **Top Global Matches:** file_cluster_13: 14.298, file_cluster_11: 14.441, file_cluster_0: 14.48
- **Magnitude:** 922.02 | **LOC:** 1119 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (73.2523%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `common_hal_bitmaptools_readinto` (Impact: 37.5)
  * `common_hal_bitmaptools_blit` (Impact: 26.4)
  * `common_hal_bitmaptools_rotozoom` (Impact: 22.5)
    * *Intent:* #include "shared-module/displayio/Bitmap.h" #include "py/mperrno.h" #include "py/runtime.h" #include...
  * `draw_line` (Impact: 20.9)
  * `common_hal_bitmaptools_arrayblit` (Impact: 14.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 44`, `args: 1`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 614`, `dead_code: 3`
* *Architecture:* `io: 3`, `api: 120`, `import: 13`
* *Defense:* `safety: 11`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` stdlib.h, string.h, runtime.h, Palette.h, stream.h, interrupt_char.h, math.h, __init__.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/unix/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.326 IQR)
- **Top Global Matches:** file_cluster_17: 15.326, file_cluster_11: 15.373, file_cluster_13: 15.52
- **Magnitude:** 916.88 | **LOC:** 329 | **CtrlFlow:** 69.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (63.4337%), Tech Debt (25.3038%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 31`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 102`, `dead_code: 8`, `planned_debt: 3`
* *Architecture:* `io: 3`, `api: 4`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mkrules.mk, mkenv.mk, mpconfigport.mk, extmod.mk, mpconfigvariant.mk, py.mk
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shared-module/lvfontio/OnDiskFont.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.208 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.156 IQR)
- **Top Global Matches:** file_cluster_13: 14.208, file_cluster_8: 14.296, file_cluster_11: 14.486
- **Magnitude:** 907.7 | **LOC:** 886 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (76.3006%), Tech Debt (25.7751%)
**Top Internal Functions/Classes:**
  * `load_font_header` (Impact: 80.0)
    * *Intent:* // Load font header data from file
  * `load_glyph_bitmap` (Impact: 77.3)
    * *Intent:* // Load glyph bitmap data into a slot // This function assumes the file is already open and position...
  * `common_hal_lvfontio_ondiskfont_cache_gly` (Impact: 55.5)
  * `get_char_id` (Impact: 24.1)
    * *Intent:* // Get character ID (glyph index) for a codepoint
  * `read_glyph_dimensions` (Impact: 12.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 88`, `func_start: 14`
* *Risk/State:* `state_mutation: 483`, `orphaned_logic: 7`
* *Architecture:* `api: 124`, `import: 14`
* *Defense:* `safety: 11`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` ff.h, string.h, OnDiskFont.h, runtime.h, translate.h, port.h, serial.h, objstr.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/atmel-samd/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.78 IQR)
- **Top Global Matches:** file_cluster_17: 12.78, file_cluster_8: 13.082, file_cluster_13: 13.204
- **Magnitude:** 894.52 | **LOC:** 363 | **CtrlFlow:** 62.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (51.5703%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 37`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 130`, `dead_code: 5`
* *Architecture:* `io: 4`, `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` circuitpy_mkenv.mk, mkrules.mk
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/builtinimport.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.674 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.978 IQR)
- **Top Global Matches:** file_cluster_13: 12.674, file_cluster_8: 12.933, file_cluster_0: 13.058
- **Magnitude:** 891.24 | **LOC:** 676 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (74.6239%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 26`, `args: 1`, `func_start: 6`
* *Risk/State:* `state_mutation: 91`
* *Architecture:* `io: 11`, `api: 43`, `import: 10`
* *Defense:* `safety: 5`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` persistentcode.h, frozenmod.h, string.h, runtime.h, builtin.h, assert.h, stdio.h, compile.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm/boards/swan_r5/tests/board_voltage.py` (EMBEDDED_PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.556 IQR)
- **Top Global Matches:** file_cluster_8: 8.556, file_cluster_7: 9.215, file_cluster_13: 9.224
- **Magnitude:** 833.16 | **LOC:** 147 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.4153%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 19`, `args: 5`, `func_start: 5`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 3`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` board, time, digitalio, supervisor
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/mkrules.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.128 IQR)
- **Top Global Matches:** file_cluster_17: 15.128, file_cluster_0: 15.317, file_cluster_11: 15.337
- **Magnitude:** 830.34 | **LOC:** 296 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.6575%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 16`, `args: 2`, `func_start: 8`
* *Risk/State:* `state_mutation: 39`, `dead_code: 9`
* *Architecture:* `io: 2`, `api: 7`, `import: 2`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $(dir, $(OBJ:.o=.P)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shared-module/displayio/TileGrid.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.198 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.751 IQR)
- **Top Global Matches:** file_cluster_13: 14.198, file_cluster_8: 14.225, file_cluster_11: 14.304
- **Magnitude:** 802.68 | **LOC:** 735 | **CtrlFlow:** 50.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (91.8414%), Tech Debt (99.9636%)
**Top Internal Functions/Classes:**
  * `displayio_tilegrid_get_refresh_areas` (Impact: 30.8)
  * `common_hal_displayio_tilegrid_construct` (Impact: 19.5)
    * *Intent:* #include "shared-bindings/displayio/TileGrid.h" #include "py/runtime.h" #include "shared-bindings/di...
  * `displayio_tilegrid_finish_refresh` (Impact: 14.3)
  * `displayio_tilegrid_fill_area` (Impact: 11.7)
  * `common_hal_displayio_tilegrid_set_all_ti` (Impact: 11.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 119`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 506`, `dead_code: 1`, `planned_debt: 3`, `orphaned_logic: 33`
* *Architecture:* `api: 119`, `import: 8`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` TilePaletteMapper.h, runtime.h, serial.h, TileGrid.h, Palette.h, OnDiskBitmap.h, Bitmap.h, ColorConverter.h
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
- `tests/basics/class2.py` (PYTHON) | Magnitude: 10.78 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 8, debug_prints: 5, args: 3
- `py/obj.h` (C) | Magnitude: 360.12 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: api: 318, pointers: 207, structural_boundaries: 147, immutability_locks: 146
- `devices/ble_hci/common-hal/_bleio/att.c` (C) | Magnitude: 1006.36 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 676, state_mutation: 529, branch: 207, api: 203
- `tests/basics/iter1.py` (PYTHON) | Magnitude: 31.86 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 38, branch: 16, debug_prints: 15, structural_boundaries: 14
- `tests/misc/sys_settrace_loop.py` (PYTHON) | Magnitude: 17.52 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 6, debug_prints: 6, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `py/argcheck.c` (C) | Magnitude: 235.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 194, state_mutation: 82, branch: 72, api: 59
- `py/objarray.c` (C) | Magnitude: 375.42 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 297, state_mutation: 196, pointers: 175, branch: 92
- `py/objint_longlong.c` (C) | Magnitude: 350.16 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 199, state_mutation: 118, api: 113, branch: 85
- `py/mpz.c` (C) | Magnitude: 1897.24 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 1231, indent_spaces: 745, pointers: 473, branch: 205
- `py/objlist.c` (C) | Magnitude: 554.02 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 359, pointers: 301, state_mutation: 267, api: 142

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tools/ci.sh` (SHELL) | Magnitude: 0.31 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 411, reflection_metaprogramming: 149, func_start: 96, state_mutation: 86
- `py/dynruntime.h` (C) | Magnitude: 120.02 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 127, indent_spaces: 84, pointers: 79, reflection_metaprogramming: 75
- `ports/nordic/nrfx_log.h` (C) | Magnitude: 16.32 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 36, macros: 12, reflection_metaprogramming: 9, ownership: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ports/nordic/background.c` (C) | Magnitude: 16.28 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, macros: 10, indent_spaces: 7, import: 6
- `tests/io/open_append.py` (PYTHON) | Magnitude: 21.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 6, state_mutation: 6, indent_spaces: 6, safety: 5
- `shared-module/keypad/EventQueue.h` (C) | Magnitude: 21.22 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, api: 6, indent_spaces: 4, class_start: 2
- `ports/nordic/supervisor/internal_flash.h` (C) | Magnitude: 13.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 3, macros: 3, reflection_metaprogramming: 1, ownership: 1
- `ports/zephyr-cp/supervisor/internal_flash.h` (C) | Magnitude: 13.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 3, macros: 3, reflection_metaprogramming: 1, ownership: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/inlineasm/rv32/asmrettype.py` (PYTHON) | Magnitude: 11.52 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 6, args: 4, func_start: 4, api: 4
- `tests/inlineasm/thumb/asmrettype.py` (PYTHON) | Magnitude: 11.52 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 6, args: 4, func_start: 4, api: 4
- `tests/basics/fun_annotations.py` (PYTHON) | Magnitude: 2.86 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, api: 1
- `stubs/micropython/__init__.pyi` (PYTHON) | Magnitude: 15.66 | Delta: **0.757 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 1, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/basics/builtin_setattr.py` (PYTHON) | Magnitude: 3.14 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 7, safety: 4, reflection_metaprogramming: 4, debug_prints: 4
- `tests/basics/del_attr.py` (PYTHON) | Magnitude: 2.36 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 12, safety: 10, structural_boundaries: 8, debug_prints: 8
- `tests/extmod/vfs_posix.py` (PYTHON) | Magnitude: 299.17 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 29, indent_spaces: 25, debug_prints: 19, structural_boundaries: 16
- `tests/basics/assign_expr_scope.py` (PYTHON) | Magnitude: 78.32 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 33, indent_spaces: 27, debug_prints: 23, structural_boundaries: 15
- `tools/makemanifest.py` (PYTHON) | Magnitude: 0.14 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 168, state_mutation: 49, branch: 37, structural_boundaries: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `supervisor/shared/web_workflow/static/serial.js` (JAVASCRIPT) | Magnitude: 74.62 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, branch: 21, state_mutation: 21, func_start: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/extmod/asyncio_lock.py` (PYTHON) | Magnitude: 87.4 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 63, concurrency: 57, structural_boundaries: 20, debug_prints: 20
- `tests/basics/async_for2.py` (PYTHON) | Magnitude: 28.98 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, debug_prints: 8, args: 6
- `tests/extmod/asyncio_new_event_loop.py` (PYTHON) | Magnitude: 32.76 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 17, indent_spaces: 17, structural_boundaries: 8, branch: 5
- `tests/extmod/asyncio_wait_task.py` (PYTHON) | Magnitude: 53.44 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 42, concurrency: 32, structural_boundaries: 16, debug_prints: 10
- `tests/extmod/asyncio_cancel_task.py` (PYTHON) | Magnitude: 66.58 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, concurrency: 44, debug_prints: 21, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `ports/atmel-samd/boards/bradanlanestudio_coin_m0/mpconfigboard.mk` (MAKEFILE) | Magnitude: 17.48 | Delta: **0.238 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 22, dead_code: 3, state_mutation: 2, planned_debt: 1
- `ports/analog/mpconfigport.mk` (MAKEFILE) | Magnitude: 16.66 | Delta: **0.312 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 32, dead_code: 4, planned_debt: 2, state_mutation: 1
- `tests/float/float_struct.py` (PYTHON) | Magnitude: 15.2 | Delta: **0.317 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, branch: 2, safety: 2, debug_prints: 2
- `ports/raspberrypi/boards/waveshare_rp2350_lcd_1_28/mpconfigboard.mk` (MAKEFILE) | Magnitude: 14.68 | Delta: **0.482 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 9, dead_code: 2, planned_debt: 2
- `ports/raspberrypi/boards/waveshare_rp2350_touch_lcd_1_28/mpconfigboard.mk` (MAKEFILE) | Magnitude: 14.68 | Delta: **0.482 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 9, dead_code: 2, planned_debt: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `ports/atmel-samd/sd_mmc/sd_mmc.h` (C) | Magnitude: 42.24 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 133, macros: 30, api: 26, structural_boundaries: 13
- `ports/nordic/bluetooth/s140_nrf52_6.1.0/s140_nrf52_6.1.0_API/include/ble_gap.h` (C) | Magnitude: 213.28 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 520, macros: 205, indent_spaces: 127, state_mutation: 116
- `ports/nordic/bluetooth/s140_nrf52_7.0.1/s140_nrf52_7.0.1_API/include/ble_gap.h` (C) | Magnitude: 218.78 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 601, macros: 210, indent_spaces: 132, state_mutation: 121
- `ports/nordic/bluetooth/s140_nrf52_6.1.0/s140_nrf52_6.1.0_API/include/ble_gattc.h` (C) | Magnitude: 134.28 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 235, indent_spaces: 114, api: 110, structural_boundaries: 54
- `ports/nordic/bluetooth/s140_nrf52_7.0.1/s140_nrf52_7.0.1_API/include/ble_gattc.h` (C) | Magnitude: 134.28 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 235, indent_spaces: 114, api: 110, structural_boundaries: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `ports/raspberrypi/common-hal/picodvi/Framebuffer_RP2350.c` (C) | Magnitude: 191.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 181, state_mutation: 121, pointers: 86, macros: 37
- `tests/perf_bench/bm_nqueens.py` (PYTHON) | Magnitude: 44.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 36, branch: 13, structural_boundaries: 10, explicit_casts: 8
- `py/asmthumb.c` (C) | Magnitude: 245.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 170, state_mutation: 70, branch: 69, macros: 35
- `shared-bindings/busio/I2C.c` (C) | Magnitude: 167.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 164, state_mutation: 83, pointers: 55, api: 52
- `shared-bindings/watchdog/WatchDogTimer.h` (C) | Magnitude: 24.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 9, structural_boundaries: 7, pointers: 7, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `ports/espressif/boards/unexpectedmaker_blizzard_s3/mpconfigboard.mk` (MAKEFILE) | Magnitude: 16.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 12, state_mutation: 1, dead_code: 1
- `ports/espressif/boards/unexpectedmaker_tinys3/mpconfigboard.mk` (MAKEFILE) | Magnitude: 16.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 12, state_mutation: 1, dead_code: 1
- `ports/espressif/boards/unexpectedmaker_tinywatch_s3/mpconfigboard.mk` (MAKEFILE) | Magnitude: 16.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 12, state_mutation: 1, dead_code: 1
- `extmod/vfs.h` (C) | Magnitude: 58.02 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 45, api: 41, macros: 35, indent_spaces: 21
- `ports/espressif/boards/esp32-wrover-dev-cam/board.c` (C) | Magnitude: 10.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ownership: 3, import: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `shared-module/busdisplay/BusDisplay.c` -> Churn: **100.0%** | Cog Load: 70.2063% | Debt: 94.115%
- `ports/zephyr-cp/supervisor/port.c` -> Churn: **95.43%** | Cog Load: 88.5539% | Debt: 99.2138%
- `ports/espressif/common-hal/qspibus/QSPIBus.c` -> Churn: **93.55%** | Cog Load: 67.3175% | Debt: 49.328%
- `ports/espressif/Makefile` -> Churn: **93.31%** | Cog Load: 52.2824% | Debt: 0.0%
- `py/circuitpy_mpconfig.mk` -> Churn: **90.4%** | Cog Load: 72.2843% | Debt: 17.1636%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `py/mpz.c` -> **Scott Shawcroft** (100.0% isolated ownership) | Magnitude: 1897.24
- `ports/unix/main.c` -> **Dan Halbert** (100.0% isolated ownership) | Magnitude: 975.64
- `py/emitinlinethumb.c` -> **Angus Gratton** (100.0% isolated ownership) | Magnitude: 960.42
- `shared-module/bitmaptools/__init__.c` -> **foamyguy** (100.0% isolated ownership) | Magnitude: 922.02
- `ports/atmel-samd/Makefile` -> **Scott Shawcroft** (100.0% isolated ownership) | Magnitude: 894.52

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `py/runtime.h` -> **Severity: 0.011** (Bridge: 0.0002 * Flux: 44.4069%)
- `py/misc.h` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 99.9741%)
- `py/objstr.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 98.7711%)
- `shared-bindings/epaperdisplay/EPaperDisplay.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.9991%)
- `py/cstack.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9894%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `py/obj.h` -> **Severity: 8532.6** (Blast Radius: 85.326 * Doc Risk: 100.0%)
- `shared-bindings/board/__init__.h` -> **Severity: 3069.3** (Blast Radius: 30.693 * Doc Risk: 100.0%)
- `supervisor/shared/safe_mode.h` -> **Severity: 2450.416** (Blast Radius: 24.934 * Doc Risk: 98.2761%)
- `py/mpprint.h` -> **Severity: 1953.093** (Blast Radius: 19.539 * Doc Risk: 99.9587%)
- `supervisor/shared/translate/translate.h` -> **Severity: 1858.507** (Blast Radius: 34.029 * Doc Risk: 54.6154%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
