# ARCHITECTURAL_BRIEF: circuitpython
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/adafruit/circuitpython` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 8374 |
| Analyzed Artifacts (Scanned) | 7146 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1228 |
| Total LOC | 398760 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 85.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2397 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 213 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 4897 | 327865 | 68.5% |
| PYTHON | 1406 | 51439 | 19.7% |
| MAKEFILE | 657 | 14103 | 9.2% |
| MARKDOWN | 55 | 0 | 0.8% |
| EMBEDDED_PYTHON | 44 | 1992 | 0.6% |
| PLAINTEXT | 22 | 1 | 0.3% |
| CSV | 21 | 668 | 0.3% |
| HTML | 10 | 598 | 0.1% |
| SHELL | 9 | 788 | 0.1% |
| ASSEMBLY | 6 | 192 | 0.1% |
| XML | 5 | 0 | 0.1% |
| JAVASCRIPT | 4 | 456 | 0.1% |
| CPP | 3 | 343 | 0.0% |
| JSON | 3 | 196 | 0.0% |
| CSS | 2 | 72 | 0.0% |
| CSHARP | 1 | 34 | 0.0% |
| YAML | 1 | 13 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 7067 | 98.9% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 76 | 1.1% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1228*

**Composition by Extension & Reason:**
- `.exp`: 381x Excluded (Unsupported Extension: '.exp')
- `no_extension`: 250x Unsupported Format (.undeterminable), 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)
- `.ld`: 66x Excluded (Unsupported Extension: '.ld')
- `.h`: 4x Excluded (Machine-Generated Source Code Signature: 22 LOC), 3x Excluded (Machine-Generated Source Code Signature: 307 LOC), 3x Excluded (Machine-Generated Source Code Signature: 173 LOC)
- `.defaults`: 45x Excluded (Unsupported Extension: '.defaults')
- `.toml`: 37x Excluded (Unsupported Extension: '.toml')
- `.rst`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Unsupported Extension: '.rst')
- `.png`: 31x Excluded (Explicitly Denied Extension: '.png')
- `.py`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 153 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2770 LOC)
- `.yml`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.license`: 20x Excluded (Unsupported Extension: '.license'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.license)
- `.conf`: 22x Excluded (Unsupported Extension: '.conf')
- `.po`: 21x Excluded (Unsupported Extension: '.po')
- `.wav`: 18x Excluded (Explicitly Denied Extension: '.wav')
- `.overlay`: 14x Excluded (Unsupported Extension: '.overlay')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 24.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.9 | 0.9 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 40.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 9.9 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 30.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.4 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 120845 | 3725 | 46 | `lib/littlefs/lfs2.c` |
| cleanup | 235 | 92 | 0 | `tools/pyboard.py` |
| guards | 33530 | 3343 | 12 | `py/obj.h` |
| danger | 5546 | 1217 | 2 | `ports/raspberrypi/Makefile` |
| concurrency | 1168 | 188 | 0 | `tests/extmod/asyncio_wait_for.py` |
| connectivity | 20172 | 2918 | 8 | `py/obj.h` |
| io | 1740 | 317 | 0 | `tests/run-tests.py` |
| crypto | 11 | 11 | 0 | `ports/unix/variants/manifest.py` |
| ipc | 714 | 71 | 0 | `ports/raspberrypi/common-hal/socketpool/Socket.c` |
| time | 101 | 43 | 0 | `tests/run-multitests.py` |
| serialization | 16 | 7 | 0 | `tests/extmod/marshal_basic.py` |
| regex | 273 | 86 | 0 | `tests/extmod/re1.py` |
| events | 452 | 129 | 0 | `shared-module/atexit/__init__.c` |
| tests | 341 | 54 | 0 | `ports/zephyr-cp/tests/zephyr_display/test_zephyr_display.py` |
| docs | 15311 | 355 | 0 | `lib/cmsis/inc/core_armv81mml.h` |
| debt | 10321 | 1613 | 4 | `tools/mpy-tool.py` |
| mutation | 84388 | 3155 | 26 | `lib/oofatfs/ff.c` |
| dead_code | 6478 | 1239 | 2 | `ports/zephyr-cp/common-hal/wifi/Radio.c` |
| credential | 4 | 3 | 0 | `ports/zephyr-cp/cptools/zephyr2cp.py` |
| threat | 2548 | 417 | 0 | `py/obj.h` |
| ml_ai | 372 | 158 | 0 | `py/emitinlinerv32.c` |
| ui | 62 | 14 | 0 | `ports/zephyr-cp/tests/zephyr_display/test_zephyr_display.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/run-tests.py` (Hits: 76)
- `tools/pyboard.py` (Hits: 43)
- `tests/extmod/vfs_basic.py` (Hits: 41)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **runtime.h** (`py/runtime.h`) — 867 inbound connections
2. **obj.h** (`py/obj.h`) — 780 inbound connections
3. **__init__.h** (`shared-bindings/board/__init__.h`) — 700 inbound connections
4. **board.h** (`supervisor/board.h`) — 675 inbound connections
5. **Pin.h** (`shared-bindings/microcontroller/Pin.h`) — 389 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **stm32h7xx_hal_conf.h** (`ports/stm/hal_conf/stm32h7xx_hal_conf.h`) — 60 outbound dependencies
2. **main.c** (`main.c`) — 58 outbound dependencies
3. **port.c** (`ports/espressif/supervisor/port.c`) — 51 outbound dependencies
4. **stm32l4xx_hal_conf.h** (`ports/stm/hal_conf/stm32l4xx_hal_conf.h`) — 50 outbound dependencies
5. **stm32f7xx_hal_conf.h** (`ports/stm/hal_conf/stm32f7xx_hal_conf.h`) — 48 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `dir_alloc` (@ `lib/oofatfs/ff.c`) -> Impact: **1259.2** | LOC: 1940
  * *Intent:* #if !FF_FS_READONLY /*-----------------------------------------------------------------------*/ /* Directory handling - Reserve a block of directory e...
- `lfs2_file_rawopencfg` (@ `lib/littlefs/lfs2.c`) -> Impact: **838.0** | LOC: 1868
  * *Intent:* /// Top level file operations ///
- `do_all_the_things` (@ `tools/analyze_heap_dump.py`) -> Impact: **686.4** | LOC: 675
- `f_mkfs` (@ `lib/oofatfs/ff.c`) -> Impact: **507.4** | LOC: 498
  * *Intent:* #endif /* FF_USE_FORWARD */ #if FF_USE_MKFS && !FF_FS_READONLY /*-----------------------------------------------------------------------*/ /* Create a...
- `mp_obj_str_format_helper` (@ `py/objstr.c`) -> Impact: **440.6** | LOC: 452
  * *Intent:* #else // define to nothing to improve coverage #define terse_str_format_value_error() #endif
- `parse_compile_execute` (@ `shared/runtime/pyexec.c`) -> Impact: **416.2** | LOC: 767
  * *Intent:* #define EXEC_FLAG_SOURCE_IS_RAW_CODE (1 << 3) #define EXEC_FLAG_SOURCE_IS_VSTR (1 << 4) #define EXEC_FLAG_SOURCE_IS_FILENAME (1 << 5) #define EXEC_FLA...
- `emit_inline_thumb_op` (@ `py/emitinlinethumb.c`) -> Impact: **405.2** | LOC: 411
  * *Intent:* // shorthand alias for whether we allow ARMv7-M instructions #define ARMV7M asm_thumb_allow_armv7m(&emit->as)
- `common_hal_busio_uart_construct` (@ `ports/atmel-samd/common-hal/busio/UART.c`) -> Impact: **290.3** | LOC: 286
  * *Intent:* // shared-bindings validates that the tx and rx are not both missing, // and that the pins are distinct.
- `common_hal_terminalio_terminal_write` (@ `shared-module/terminalio/Terminal.c`) -> Impact: **277.8** | LOC: 279
- `common_hal_busio_uart_construct` (@ `ports/mimxrt10xx/common-hal/busio/UART.c`) -> Impact: **273.1** | LOC: 261

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `py` | 215 | 41077.8 | 37.01% | 24.66% |
| `lib/oofatfs` | 4 | 9542.54 | 27.32% | 7.52% |
| `tests/basics` | 559 | 9006.84 | 3.27% | 0.0% |
| `lib/littlefs` | 9 | 8152.94 | 39.57% | 17.27% |
| `tests/extmod` | 131 | 5717.8 | 14.41% | 0.0% |
| `ports/nordic` | 16 | 5331.98 | 8.83% | 20.39% |
| `extmod` | 36 | 4958.56 | 43.07% | 10.64% |
| `lib/cmsis/inc` | 24 | 4687.75 | 7.88% | 12.25% |
| `shared-module/displayio` | 21 | 3591.4 | 38.32% | 36.25% |
| `lib/libm` | 31 | 3221.1 | 41.05% | 47.85% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `tools/convert_release_notes.py` -> **100.0%** Exposure
- `devices/ble_hci/common-hal/_bleio/Connection.c` -> **100.0%** Exposure
- `ports/analog/common-hal/microcontroller/Pin.c` -> **100.0%** Exposure
- `ports/analog/common-hal/microcontroller/Processor.c` -> **100.0%** Exposure
- `ports/atmel-samd/common-hal/alarm/time/TimeAlarm.c` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `mpy-cross/Makefile` -> **100.0%** Exposure
- `ports/atmel-samd/Makefile` -> **100.0%** Exposure
- `ports/broadcom/Makefile` -> **100.0%** Exposure
- `ports/espressif/Makefile` -> **100.0%** Exposure
- `ports/litex/Makefile` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tools/ci.sh` -> **84** Orphaned Functions | **0** Duplicates
- `shared-module/_eve/__init__.c` -> **54** Orphaned Functions | **0** Duplicates
- `ports/zephyr-cp/common-hal/wifi/Radio.c` -> **43** Orphaned Functions | **0** Duplicates
- `py/compile.c` -> **40** Orphaned Functions | **0** Duplicates
- `py/runtime.c` -> **38** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tools/gen_crt_bundle.py` -> **99.3517%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `16778` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `ports/zephyr-cp/cptools/build_circuitpython.py` (PYTHON) -> Cumulative Risk: **773.09**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 774.68 | **LOC:** 651 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.5538%)
- **Heaviest Functions:** `build_circuitpython` (Impact: 77.3), `determine_enabled_modules` (Impact: 30.9), `preprocess_and_split_defs` (Impact: 5.6)

### 2. `shared-module/busdisplay/BusDisplay.c` (C) -> Cumulative Risk: **738.48**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 422.06 | **LOC:** 444 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Documentation (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `common_hal_busdisplay_busdisplay_construct` (Impact: 101.8), `_refresh_area` (Impact: 34.3), `common_hal_busdisplay_busdisplay_set_brightness` (Impact: 29.9)

### 3. `ports/zephyr-cp/cptools/cpbuild.py` (PYTHON) -> Cumulative Risk: **731.02**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 679.04 | **LOC:** 429 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `run_command` (Impact: 130.4), `compile` (Impact: 22.0), `run_function` (Impact: 15.1)

### 4. `shared-module/displayio/TileGrid.c` (C) -> Cumulative Risk: **719.55**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 869.38 | **LOC:** 735 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.7959%)
- **Heaviest Functions:** `displayio_tilegrid_fill_area` (Impact: 112.0), `common_hal_displayio_tilegrid_construct` (Impact: 61.2), `displayio_tilegrid_get_refresh_areas` (Impact: 49.8)

### 5. `ports/zephyr-cp/supervisor/port.c` (C) -> Cumulative Risk: **706.47**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 206.36 | **LOC:** 386 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 90.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.6936%), Tech Debt (99.2795%)
- **Heaviest Functions:** `port_realloc` (Impact: 15.1), `port_heap_init` (Impact: 10.4), `port_malloc` (Impact: 9.6)

### 6. `supervisor/shared/web_workflow/static/directory.js` (JAVASCRIPT) -> Cumulative Risk: **702.13**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 323.24 | **LOC:** 323 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `refresh_list` (Impact: 28.8), `compareValues` (Impact: 14.3), `upload` (Impact: 14.1)

### 7. `shared-module/audiodelays/Chorus.c` (C) -> Cumulative Risk: **698.18**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 294.74 | **LOC:** 341 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.5648%)
- **Heaviest Functions:** `audiodelays_chorus_get_buffer` (Impact: 88.3), `common_hal_audiodelays_chorus_construct` (Impact: 27.5), `common_hal_audiodelays_chorus_deinited` (Impact: 3.1)

### 8. `ports/espressif/common-hal/_bleio/Characteristic.c` (C) -> Cumulative Risk: **697.98**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 341.2 | **LOC:** 339 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Cognitive Load (92.0369%)
- **Heaviest Functions:** `common_hal_bleio_characteristic_construct` (Impact: 87.5), `bleio_characteristic_access_cb` (Impact: 38.0), `characteristic_on_ble_gap_evt` (Impact: 22.5)

### 9. `supervisor/shared/filesystem.c` (C) -> Cumulative Risk: **695.75**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 273.1 | **LOC:** 344 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.1899%)
- **Heaviest Functions:** `filesystem_init` (Impact: 53.9), `filesystem_for_path` (Impact: 9.7), `filesystem_set_writable_by_usb` (Impact: 5.5)

### 10. `ports/raspberrypi/supervisor/port.c` (C) -> Cumulative Risk: **695.22**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 311.5 | **LOC:** 668 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9689%), Tech Debt (96.6955%)
- **Heaviest Functions:** `port_idle_until_interrupt` (Impact: 36.0), `port_realloc` (Impact: 14.7), `port_init` (Impact: 14.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `lib/oofatfs/ff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9415.88 | **LOC:** 6028 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.3392%), Tech Debt (12.2535%)
**Top Internal Functions/Classes:**
  * `dir_alloc` (Impact: 1259.2)
    * *Intent:* #if !FF_FS_READONLY /*-----------------------------------------------------------------------*/ /* D...
  * `f_mkfs` (Impact: 507.4)
    * *Intent:* #endif /* FF_USE_FORWARD */ #if FF_USE_MKFS && !FF_FS_READONLY /*-----------------------------------...
  * `create_name` (Impact: 189.9)
    * *Intent:* #endif /* FF_USE_FIND && FF_FS_MINIMIZE <= 1 */ /*--------------------------------------------------...
  * `find_volume` (Impact: 168.6)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Determine logical dri...
  * `f_open` (Impact: 156.7)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Open or Create a File...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1455 instances
* *State Mutation (weighted view):* 4457
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1830`, `structural_boundaries: 393`, `args: 137`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1547`, `unreferenced_by_name: 25`
* *Architecture:* `api: 31`, `import: 3`
* *Defense:* `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` diskio.h, ff.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/littlefs/lfs2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5454.32 | **LOC:** 6331 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.7694%), Tech Debt (14.3672%)
**Top Internal Functions/Classes:**
  * `lfs2_file_rawopencfg` (Impact: 838.0)
    * *Intent:* /// Top level file operations ///
  * `lfs2_dir_fetchmatch` (Impact: 208.9)
    * *Intent:* #endif
  * `lfs2_dir_relocatingcommit` (Impact: 124.8)
    * *Intent:* #endif #ifndef LFS2_READONLY
  * `lfs2_dir_traverse` (Impact: 106.9)
  * `lfs2_dir_orphaningcommit` (Impact: 96.7)
    * *Intent:* #endif #ifndef LFS2_READONLY
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 562 instances
* *State Mutation (weighted view):* 1906
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 901`, `structural_boundaries: 934`, `args: 273`, `func_start: 181`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 782`, `dead_code: 9`, `unreferenced_by_name: 34`
* *Architecture:* `io: 2`, `api: 51`, `import: 2`
* *Defense:* `safety: 1`, `doc: 21`, `immutability_locks: 131`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` lfs2.h, lfs2_util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/compile.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2655.72 | **LOC:** 3703 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.3634%), Tech Debt (45.5428%)
**Top Internal Functions/Classes:**
  * `mp_compile_to_raw_code` (Impact: 126.4)
    * *Intent:* #if !MICROPY_EXPOSE_MP_COMPILE_TO_RAW_CODE
  * `compile_scope_inline_asm` (Impact: 100.7)
    * *Intent:* #if MICROPY_EMIT_INLINE_ASM // requires 3 passes: SCOPE, CODE_SIZE, EMIT
  * `compile_expr_stmt` (Impact: 76.7)
    * *Intent:* #endif
  * `compile_atom_brace_helper` (Impact: 75.0)
  * `compile_scope` (Impact: 72.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 247 instances
* *State Mutation (weighted view):* 775
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 778`, `structural_boundaries: 278`, `args: 168`, `func_start: 100`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 89`, `state_mutation: 281`, `dead_code: 24`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 40`
* *Architecture:* `api: 7`, `import: 16`
* *Defense:* `safety: 119`, `doc: 2`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` assert.h, asmbase.h, compile.h, emit.h, grammar.h, nativeglue.h, persistentcode.h, runtime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/objstr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2312.78 | **LOC:** 2512 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.1962%), Tech Debt (19.5074%)
**Top Internal Functions/Classes:**
  * `mp_obj_str_format_helper` (Impact: 440.6)
    * *Intent:* #else // define to nothing to improve coverage #define terse_str_format_value_error() #endif
  * `str_modulo_format` (Impact: 173.5)
    * *Intent:* #if MICROPY_PY_BUILTINS_STR_OP_MODULO
  * `mp_obj_str_binary_op` (Impact: 68.0)
    * *Intent:* // Note: this function is used to check if an object is a str or bytes, which // works because both ...
  * `bytes_make_new` (Impact: 56.2)
  * `mp_str_print_quoted` (Impact: 55.6)
    * *Intent:* /******************************************************************************/ /* str */...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 246 instances
* *State Mutation (weighted view):* 760
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 611`, `structural_boundaries: 236`, `args: 176`, `func_start: 83`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 268`, `dead_code: 8`, `planned_debt: 8`, `unreferenced_by_name: 10`
* *Architecture:* `api: 31`, `import: 7`
* *Defense:* `safety: 91`, `doc: 2`, `immutability_locks: 149`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` assert.h, cstack.h, objlist.h, objstr.h, runtime.h, unicode.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/littlefs/lfs1.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2264.7 | **LOC:** 2584 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.2285%), Tech Debt (16.5735%)
**Top Internal Functions/Classes:**
  * `lfs1_dir_commit` (Impact: 72.3)
  * `lfs1_file_opencfg` (Impact: 70.8)
    * *Intent:* /// Top level file operations ///
  * `lfs1_dir_find` (Impact: 65.7)
  * `lfs1_ctz_extend` (Impact: 58.6)
  * `lfs1_rename` (Impact: 55.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 306 instances
* *State Mutation (weighted view):* 991
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 450`, `structural_boundaries: 370`, `args: 79`, `func_start: 73`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 379`, `dead_code: 3`, `unreferenced_by_name: 17`
* *Architecture:* `io: 2`, `api: 29`, `import: 3`
* *Defense:* `safety: 2`, `doc: 12`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` inttypes.h, lfs1.h, lfs1_util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/tjpgd/src/tjpgd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1920.8 | **LOC:** 1158 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.6859%), Tech Debt (9.8189%)
**Top Internal Functions/Classes:**
  * `jd_prepare` (Impact: 174.0)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Analyze the JPEG imag...
  * `mcu_output` (Impact: 124.6)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Output an MCU: Conver...
  * `huffext` (Impact: 78.7)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Extract a huffman dec...
  * `create_huffman_tbl` (Impact: 54.0)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Create huffman code t...
  * `mcu_load` (Impact: 44.9)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Load all blocks in an...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 417 instances
* *State Mutation (weighted view):* 1298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 97`, `args: 13`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 464`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 12`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tjpgd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/mpz.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1846.86 | **LOC:** 1757 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (69.8653%), Tech Debt (53.9591%)
**Top Internal Functions/Classes:**
  * `mpz_as_str_inpl` (Impact: 51.7)
    * *Intent:* #endif // assumes enough space in str as calculated by mp_int_format_size // base must be between 2 ...
  * `mpn_div` (Impact: 49.2)
    * *Intent:* */
  * `mpz_as_bytes` (Impact: 44.0)
  * `mpz_set_from_str` (Impact: 36.0)
    * *Intent:* #endif // returns number of bytes from str that were processed
  * `mpz_set_from_float` (Impact: 32.2)
    * *Intent:* #if MICROPY_PY_BUILTINS_FLOAT
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 356 instances
* *State Mutation (weighted view):* 1099
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 98`, `args: 64`, `func_start: 50`
* *Risk/State:* `state_mutation: 387`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 16`
* *Architecture:* `api: 31`, `import: 3`
* *Defense:* `safety: 65`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, mpz.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/emitnative.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1641.8 | **LOC:** 3238 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.0398%), Tech Debt (11.7318%)
**Top Internal Functions/Classes:**
  * `emit_native_binary_op` (Impact: 146.3)
  * `emit_native_start_pass` (Impact: 127.2)
  * `emit_native_store_subscr` (Impact: 98.6)
  * `emit_native_load_subscr` (Impact: 77.1)
  * `emit_native_call_function` (Impact: 45.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 357
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 527`, `structural_boundaries: 268`, `args: 166`, `func_start: 115`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 155`, `dead_code: 14`, `planned_debt: 17`, `fragile_debt: 2`
* *Architecture:* `api: 8`, `import: 7`
* *Defense:* `safety: 62`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` assert.h, emit.h, nativeglue.h, objfun.h, objstr.h, stdio.h, string.h
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `ports/raspberrypi/common-hal/rp2pio/StateMachine.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1520.68 | **LOC:** 1537 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (91.4473%), Tech Debt (79.7414%)
**Top Internal Functions/Classes:**
  * `_transfer` (Impact: 232.0)
  * `rp2pio_statemachine_construct` (Impact: 226.6)
  * `common_hal_rp2pio_statemachine_construct` (Impact: 108.0)
  * `consider_instruction` (Impact: 87.3)
  * `common_hal_rp2pio_statemachine_background_write` (Impact: 44.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 130 instances
* *State Mutation (weighted view):* 460
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 284`, `args: 93`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 200`, `dead_code: 2`, `planned_debt: 5`, `unreferenced_by_name: 30`
* *Architecture:* `api: 42`, `import: 17`
* *Defense:* `safety: 39`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` StateMachine.h, __init__.h, clocks.h, dma.h, irq.h, pio_instructions.h, platform_defs.h, iobank0.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shared-module/bitmaptools/__init__.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1378.66 | **LOC:** 1119 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (71.4181%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `common_hal_bitmaptools_rotozoom` (Impact: 135.4)
    * *Intent:* #include "shared-module/displayio/Bitmap.h" #include "py/mperrno.h" #include "py/runtime.h" #include...
  * `common_hal_bitmaptools_alphablend` (Impact: 117.4)
  * `common_hal_bitmaptools_blit` (Impact: 86.3)
  * `common_hal_bitmaptools_readinto` (Impact: 72.3)
  * `draw_line` (Impact: 48.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 215 instances
* *State Mutation (weighted view):* 669
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 71`, `args: 18`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 239`, `dead_code: 3`
* *Architecture:* `io: 1`, `api: 13`, `import: 13`
* *Defense:* `safety: 11`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` math.h, mperrno.h, runtime.h, stream.h, __init__.h, Bitmap.h, ColorConverter.h, Palette.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/run-tests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1329.12 | **LOC:** 1356 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.5525%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 269.2)
  * `run_micropython` (Impact: 124.0)
  * `run_one_test` (Impact: 89.7)
  * `get_test_instance` (Impact: 25.8)
  * `prepare_script_for_target` (Impact: 24.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Rce:* 7 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 188 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 31
* *Sec Tainted Injection (weighted view):* 7
* *State Mutation (weighted view):* 612
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 131`, `args: 27`, `func_start: 26`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 7`, `state_mutation: 236`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 76`, `api: 26`, `concurrency: 6`, `import: 17`
* *Defense:* `safety: 27`, `doc: 3`, `test: 8`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __injected_test, an, argparse, glob, inspect, io, json, multiprocessing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/AnimatedGIF/gif.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1321.44 | **LOC:** 1044 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.0864%), Tech Debt (62.0803%)
**Top Internal Functions/Classes:**
  * `GIFParseInfo` (Impact: 111.4)
    * *Intent:* } /* GIFInit() */ // // Parse the GIF header, gather the size and palette info // If called with bIn...
  * `GIF_getInfo` (Impact: 71.7)
    * *Intent:* } /* GIFParseInfo() */ // // Gather info about an animated GIF file //
  * `GIFMakePels` (Impact: 44.7)
    * *Intent:* } /* ConvertNewPixels() */ // // GIFMakePels //
  * `DecodeLZW` (Impact: 25.0)
    * *Intent:* // // Decode LZW into an image //
  * `GIF_playFrame` (Impact: 17.4)
    * *Intent:* } /* GIF_reset() */ // // Return value: // 1 = good decode, more frames exist // 0 = good decode, no...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 276 instances
* *State Mutation (weighted view):* 900
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 59`, `args: 43`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 348`, `dead_code: 16`, `fragile_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `io: 5`, `api: 16`, `import: 1`
* *Defense:* `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AnimatedGIF_circuitpy.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `supervisor/shared/web_workflow/web_workflow.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1288.64 | **LOC:** 1697 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (94.0484%), Tech Debt (17.4995%)
**Top Internal Functions/Classes:**
  * `_reply` (Impact: 211.0)
  * `_process_request` (Impact: 120.1)
  * `_write_file_and_reply` (Impact: 56.6)
  * `_reply_with_file` (Impact: 45.4)
  * `supervisor_start_web_workflow` (Impact: 41.5)
    * *Intent:* #endif
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 143 instances
* *State Mutation (weighted view):* 451
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 242`, `args: 62`, `func_start: 51`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 165`, `dead_code: 1`, `planned_debt: 5`, `unreferenced_by_name: 6`
* *Architecture:* `api: 12`, `import: 29`
* *Defense:* `safety: 42`, `immutability_locks: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` __init__.h, vfs.h, vfs_fat.h, mpversion.h, mperrno.h, mpstate.h, Hash.h, __init__.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/parse.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1100.04 | **LOC:** 1411 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.6976%), Tech Debt (10.9911%)
**Top Internal Functions/Classes:**
  * `mp_parse` (Impact: 185.0)
  * `fold_constants` (Impact: 129.0)
  * `push_result_rule` (Impact: 59.7)
    * *Intent:* #endif
  * `mp_parse_node_print` (Impact: 44.6)
    * *Intent:* #if MICROPY_DEBUG_PRINTERS
  * `fold_logical_constants` (Impact: 42.8)
    * *Intent:* #endif
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 119 instances
* *State Mutation (weighted view):* 378
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 168`, `args: 55`, `func_start: 28`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 140`, `dead_code: 3`, `unreferenced_by_name: 4`
* *Architecture:* `api: 10`, `import: 27`
* *Defense:* `safety: 81`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` assert.h, builtin.h, grammar.h, lexer.h, objint.h, objstr.h, parse.h, parsenum.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/runtime.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1061.58 | **LOC:** 1978 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.5574%), Tech Debt (90.061%)
**Top Internal Functions/Classes:**
  * `mp_unary_op` (Impact: 68.1)
  * `mp_convert_member_lookup` (Impact: 61.8)
    * *Intent:* #endif // MICROPY_BUILTIN_METHOD_CHECK_SELF_ARG // Given a member that was extracted from an instanc...
  * `mp_resume` (Impact: 44.5)
  * `mp_store_attr` (Impact: 36.6)
  * `mp_init` (Impact: 34.6)
    * *Intent:* #define TYPE_HAS_ITERNEXT(type) (type->flags & (MP_TYPE_FLAG_ITER_IS_ITERNEXT | MP_TYPE_FLAG_ITER_IS...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 140 instances
* *State Mutation (weighted view):* 445
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 172`, `args: 128`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 165`, `dead_code: 7`, `planned_debt: 12`, `unreferenced_by_name: 38`
* *Architecture:* `api: 72`, `import: 22`
* *Defense:* `safety: 49`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` assert.h, vfs.h, builtin.h, compile.h, cstack.h, gc.h, mperrno.h, objgenerator.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/raspberrypi/common-hal/socketpool/Socket.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1018.04 | **LOC:** 1329 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (68.6748%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `common_hal_socketpool_socket_connect` (Impact: 53.3)
  * `lwip_tcp_receive` (Impact: 44.0)
    * *Intent:* // Helper function for recv/recvfrom to handle TCP packets
  * `socketpool_socket_accept` (Impact: 42.4)
  * `socketpool_socket` (Impact: 40.1)
  * `lwip_tcp_send` (Impact: 40.0)
    * *Intent:* // Helper function for send/sendto to handle TCP packets
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 201`, `args: 67`, `func_start: 44`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 139`, `dead_code: 1`
* *Architecture:* `api: 26`, `import: 25`
* *Defense:* `safety: 12`, `doc: 4`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` __init__.h, dns.h, err.h, igmp.h, init.h, netdb.h, tcp_priv.h, raw.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devices/ble_hci/common-hal/_bleio/att.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1009.38 | **LOC:** 1802 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.8306%), Tech Debt (33.7185%)
**Top Internal Functions/Classes:**
  * `att_process_data` (Impact: 56.6)
  * `process_read_or_read_blob_req` (Impact: 54.9)
  * `process_read_type_req` (Impact: 54.2)
  * `process_write_req_or_cmd` (Impact: 40.1)
    * *Intent:* // Handles BT_ATT_OP_WRITE_REQ or BT_ATT_OP_WRITE_
  * `process_find_info_req` (Impact: 38.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 384
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 311`, `args: 50`, `func_start: 48`, `class_start: 63`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 170`, `dead_code: 69`, `unreferenced_by_name: 19`
* *Architecture:* `api: 22`, `import: 13`
* *Defense:* `safety: 33`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` att.h, Adapter.h, Attribute.h, hci.h, att_internal.h, l2cap_internal.h, obj.h, Characteristic.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/zephyr-cp/cptools/zephyr2cp.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 965.6 | **LOC:** 897 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (63.3589%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `zephyr_dts_to_cp_board` (Impact: 225.7)
  * `find_flash_devices` (Impact: 35.0)
    * *Intent:* """ Find all flash devices from a device tree. Args: device_tree: Parsed device tree (dtlib.DT objec...
  * `find_ram_regions` (Impact: 24.5)
    * *Intent:* """ Find all RAM regions from a device tree. Includes the zephyr,sram node and any zephyr,memory-reg...
  * `_label_to_end` (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 209 instances
* *State Mutation (weighted view):* 662
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 39`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 244`, `dead_code: 3`
* *Architecture:* `io: 2`, `api: 3`, `import: 6`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` compat2driver, cpbuild, devicetree, logging, pathlib, yaml
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `py/objtype.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 962.84 | **LOC:** 1562 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.0656%), Tech Debt (19.0835%)
**Top Internal Functions/Classes:**
  * `mp_obj_new_type` (Impact: 60.3)
  * `mp_obj_instance_store_attr` (Impact: 60.2)
  * `mp_obj_class_lookup` (Impact: 57.0)
  * `type_attr` (Impact: 52.5)
  * `mp_obj_instance_load_attr` (Impact: 47.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 165`, `args: 80`, `func_start: 34`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 98`, `dead_code: 2`, `planned_debt: 7`, `unreferenced_by_name: 4`
* *Architecture:* `api: 11`, `import: 6`
* *Defense:* `safety: 49`, `doc: 5`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` assert.h, objtype.h, runtime.h, stddef.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/profile.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 944.06 | **LOC:** 846 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.3486%), Tech Debt (29.5873%)
**Top Internal Functions/Classes:**
  * `mp_prof_opcode_decode` (Impact: 198.9)
  * `frame_attr` (Impact: 19.4)
  * `mp_prof_instr_tick` (Impact: 16.6)
  * `mp_prof_frame_enter` (Impact: 11.9)
  * `mp_prof_print_instr` (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 203 instances
* *State Mutation (weighted view):* 635
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 111`, `args: 18`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `state_mutation: 229`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 6`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `safety: 12`, `doc: 3`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` bc0.h, gc.h, objfun.h, profile.h, runtime0.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/gc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 929.54 | **LOC:** 1565 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (96.9493%), Tech Debt (10.2581%)
**Top Internal Functions/Classes:**
  * `gc_alloc` (Impact: 89.3)
  * `gc_realloc` (Impact: 69.1)
  * `gc_dump_alloc_table` (Impact: 59.0)
  * `gc_info` (Impact: 31.9)
  * `gc_free` (Impact: 25.3)
    * *Intent:* // force the freeing of a piece of memory // TODO: freeing here does not call finaliser
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 451
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 179`, `args: 62`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 161`, `dead_code: 6`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 21`, `import: 13`
* *Defense:* `safety: 80`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` assert.h, perfetto_encoder.h, gc.h, runtime.h, __init__.h, stdio.h, string.h, safe_mode.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/perf_bench/bm_hexiom.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 872.96 | **LOC:** 658 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.2939%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constraint_pass` (Impact: 78.3)
    * *Intent:* ##################################
  * `solved` (Impact: 33.9)
  * `solve_step` (Impact: 28.3)
  * `print_pos` (Impact: 23.9)
  * `read_file` (Impact: 19.3)
    * *Intent:* # TODO Write an 'iterator' to go over all x,y positions
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 460
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 86`, `args: 38`, `func_start: 38`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 170`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 37`, `import: 1`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` io
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shared-module/displayio/TileGrid.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 869.38 | **LOC:** 735 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (92.423%), Tech Debt (99.7959%)
**Top Internal Functions/Classes:**
  * `displayio_tilegrid_fill_area` (Impact: 112.0)
  * `common_hal_displayio_tilegrid_construct` (Impact: 61.2)
    * *Intent:* #include "shared-bindings/displayio/TileGrid.h" #include "py/runtime.h" #include "shared-bindings/di...
  * `displayio_tilegrid_get_refresh_areas` (Impact: 49.8)
  * `displayio_tilegrid_finish_refresh` (Impact: 19.7)
  * `common_hal_displayio_tilegrid_set_all_tiles` (Impact: 18.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 127 instances
* *State Mutation (weighted view):* 418
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 122`, `args: 39`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 164`, `dead_code: 2`, `planned_debt: 3`, `unreferenced_by_name: 33`
* *Architecture:* `api: 34`, `import: 8`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` runtime.h, Bitmap.h, ColorConverter.h, OnDiskBitmap.h, Palette.h, TileGrid.h, TilePaletteMapper.h, serial.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/maketranslationdata.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 867.48 | **LOC:** 659 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.3164%), Tech Debt (14.2022%)
**Top Internal Functions/Classes:**
  * `compute_huffman_coding` (Impact: 161.8)
    * *Intent:* # possible future improvement: some languages are better when consider len(k) > 2. try both? qstrs =...
  * `decompress` (Impact: 24.3)
  * `compress` (Impact: 21.8)
  * `compute_unicode_offset` (Impact: 13.7)
  * `parse_input_headers` (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 495
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 83`, `args: 30`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 195`, `dead_code: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 7`, `api: 27`, `import: 12`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, argparse, bisect, collections, dataclasses, gettext, html.entities, huffman...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `shared-module/busdisplay/BusDisplay.c` -> Churn: **100.0%** | Cog Load: 71.3941% | Debt: 81.6751%
- `ports/zephyr-cp/supervisor/port.c` -> Churn: **95.43%** | Cog Load: 55.6889% | Debt: 99.2795%
- `ports/espressif/common-hal/qspibus/QSPIBus.c` -> Churn: **93.55%** | Cog Load: 66.7472% | Debt: 49.328%
- `ports/espressif/Makefile` -> Churn: **93.31%** | Cog Load: 63.5402% | Debt: 15.1086%
- `py/circuitpy_mpconfig.mk` -> Churn: **90.4%** | Cog Load: 70.1412% | Debt: 15.6698%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `py/mpz.c` -> **Scott Shawcroft** (100.0% isolated ownership) | Magnitude: 1846.86
- `ports/raspberrypi/common-hal/rp2pio/StateMachine.c` -> **Dan Halbert** (100.0% isolated ownership) | Magnitude: 1520.68
- `shared-module/bitmaptools/__init__.c` -> **foamyguy** (100.0% isolated ownership) | Magnitude: 1378.66
- `ports/zephyr-cp/cptools/zephyr2cp.py` -> **Scott Shawcroft** (100.0% isolated ownership) | Magnitude: 965.6
- `shared-module/displayio/TileGrid.c` -> **P. Patrick Socha** (100.0% isolated ownership) | Magnitude: 869.38

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `py/runtime.h` -> **Severity: 0.003** (Bridge: 0.0003 * Flux: 9.5943%)
- `py/misc.h` -> **Severity: 0.002** (Bridge: 0.0001 * Flux: 16.5448%)
- `py/objstr.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 63.026%)
- `shared/netutils/trace.c` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `py/obj.h` -> **Severity: 8362.8** (Blast Radius: 83.628 * Doc Risk: 100.0%)
- `py/misc.h` -> **Severity: 3638.6** (Blast Radius: 36.386 * Doc Risk: 100.0%)
- `supervisor/shared/translate/translate_impl.h` -> **Severity: 1443.1** (Blast Radius: 14.431 * Doc Risk: 100.0%)
- `py/runtime.h` -> **Severity: 1277.6** (Blast Radius: 12.776 * Doc Risk: 100.0%)
- `py/objarray.h` -> **Severity: 463.2** (Blast Radius: 4.632 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
