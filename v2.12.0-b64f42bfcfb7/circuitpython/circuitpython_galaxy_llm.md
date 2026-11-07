# ARCHITECTURAL_BRIEF: circuitpython
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/adafruit/circuitpython` |
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
- **Scope:** 7149 analyzed artifact(s), 397612 LOC.
- **Load-bearing artifact:** `py/obj.h` -- 964 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `ports/stm/hal_conf/stm32h7xx_hal_conf.h` -- pulls in 60 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/oofatfs/ff.c` at magnitude 8790.58 (structural weight, not risk).
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
| Total Artifacts | 8374 |
| Analyzed Artifacts (Scanned) | 7149 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1225 |
| Total LOC | 397612 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 85.4% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5262 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1977 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.7587 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 370 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 4864 | 325213 | 68.0% |
| EMBEDDED_PYTHON | 953 | 24991 | 13.3% |
| MAKEFILE | 654 | 13669 | 9.1% |
| PYTHON | 502 | 28560 | 7.0% |
| MARKDOWN | 57 | 0 | 0.8% |
| PLAINTEXT | 27 | 1 | 0.4% |
| YAML | 22 | 1083 | 0.3% |
| CSV | 21 | 668 | 0.3% |
| HTML | 10 | 598 | 0.1% |
| SHELL | 9 | 788 | 0.1% |
| CPP | 8 | 1077 | 0.1% |
| ASSEMBLY | 6 | 192 | 0.1% |
| XML | 5 | 0 | 0.1% |
| JSON | 4 | 210 | 0.1% |
| JAVASCRIPT | 4 | 456 | 0.1% |
| CSS | 2 | 72 | 0.0% |
| CSHARP | 1 | 34 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 7144 |
| utf-8 | bom | 3 |
| cp1252 | cp1252-fallback | 1 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 43%, Data / Markup / Trivial 28%, Parameter Forwarders Files 8%, Encapsulated Accessors Files 5%, Large Core Modules (3) 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 7063 | 98.8% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 83 | 1.2% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1225*

**Composition by Extension & Reason:**
- `.exp`: 381x Excluded (Unsupported Extension: '.exp')
- `no_extension`: 250x Unsupported Format (.undeterminable), 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)
- `.h`: 7x Excluded (Machine-Generated Source Code Signature: 27 LOC), 6x Excluded (Machine-Generated Source Code Signature: 45 LOC), 4x Excluded (Machine-Generated Source Code Signature: 22 LOC)
- `.ld`: 66x Excluded (Unsupported Extension: '.ld')
- `.defaults`: 45x Excluded (Unsupported Extension: '.defaults')
- `.toml`: 37x Excluded (Unsupported Extension: '.toml')
- `.rst`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Unsupported Extension: '.rst')
- `.png`: 31x Excluded (Explicitly Denied Extension: '.png')
- `.py`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 526 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2770 LOC)
- `.license`: 20x Excluded (Unsupported Extension: '.license'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.license)
- `.conf`: 22x Excluded (Unsupported Extension: '.conf')
- `.po`: 21x Excluded (Unsupported Extension: '.po')
- `.wav`: 18x Excluded (Explicitly Denied Extension: '.wav')
- `.c`: 2x Excluded (Machine-Generated Source Code Signature: 356 LOC), 2x Excluded (Machine-Generated Source Code Signature: 150 LOC), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mk`: 3x Statistical Anomaly (Z-Score: -4.78 < -4.55), 2x Statistical Anomaly (Z-Score: -7.93 < -4.55), 2x Statistical Anomaly (Z-Score: -8.53 < -4.55)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.7 | 20.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 10.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.8 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 30.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.4 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2868 | 784 | 1 | `lib/littlefs/lfs2.c` |
| cleanup | 248 | 99 | 0 | `tools/pyboard.py` |
| guards | 32558 | 3318 | 11 | `py/obj.h` |
| danger | 5637 | 1227 | 1 | `ports/raspberrypi/Makefile` |
| concurrency | 1436 | 163 | 0 | `tests/extmod/asyncio_gather.py` |
| connectivity | 20605 | 2912 | 8 | `py/obj.h` |
| io | 1494 | 291 | 0 | `tests/run-tests.py` |
| crypto | 13 | 11 | 0 | `tools/gen_crt_bundle.py` |
| ipc | 717 | 68 | 0 | `ports/raspberrypi/common-hal/socketpool/Socket.c` |
| time | 74 | 22 | 0 | `tests/run-multitests.py` |
| serialization | 9 | 5 | 0 | `tools/pyboard.py` |
| regex | 167 | 71 | 0 | `tools/board_stubs/build_board_specific_stubs/board_stub_builder.py` |
| events | 415 | 113 | 0 | `shared-module/atexit/__init__.c` |
| tests | 340 | 55 | 0 | `ports/zephyr-cp/tests/zephyr_display/test_zephyr_display.py` |
| docs | 6969 | 377 | 0 | `ports/nordic/bluetooth/s140_nrf52_7.0.1/s140_nrf52_7.0.1_API/include/ble_gap.h` |
| debt | 10392 | 1627 | 4 | `tools/mpy-tool.py` |
| mutation | 83752 | 3161 | 25 | `lib/oofatfs/ff.c` |
| dead_code | 7290 | 1406 | 3 | `ports/zephyr-cp/common-hal/wifi/Radio.c` |
| credential | 5 | 4 | 0 | `ports/zephyr-cp/cptools/zephyr2cp.py` |
| threat | 120 | 27 | 0 | `tests/extmod/deflate_decompress.py` |
| ml_ai | 568 | 193 | 0 | `tests/basics/struct1.py` |
| ui | 96 | 21 | 0 | `ports/zephyr-cp/tests/zephyr_display/test_zephyr_display.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/run-tests.py` (Hits: 76)
- `tools/pyboard.py` (Hits: 43)
- `tools/manifestfile.py` (Hits: 41)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **obj.h** (`py/obj.h`) — 964 inbound connections
2. **runtime.h** (`py/runtime.h`) — 866 inbound connections
3. **__init__.h** (`shared-bindings/board/__init__.h`) — 700 inbound connections
4. **board.h** (`supervisor/board.h`) — 675 inbound connections
5. **runtime.c** (`py/runtime.c`) — 551 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **stm32h7xx_hal_conf.h** (`ports/stm/hal_conf/stm32h7xx_hal_conf.h`) — 60 outbound dependencies
2. **main.c** (`main.c`) — 58 outbound dependencies
3. **port.c** (`ports/espressif/supervisor/port.c`) — 51 outbound dependencies
4. **stm32l4xx_hal_conf.h** (`ports/stm/hal_conf/stm32l4xx_hal_conf.h`) — 50 outbound dependencies
5. **stm32f7xx_hal_conf.h** (`ports/stm/hal_conf/stm32f7xx_hal_conf.h`) — 48 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `dir_alloc` **(Many-Argument Workhorses)** (@ `lib/oofatfs/ff.c`) -> Impact: **1051.4** | LOC: 1940
  * *Intent:* #if !FF_FS_READONLY /*-----------------------------------------------------------------------*/ /* Directory handling - Reserve a block of directory e...
- `lfs2_file_rawopencfg` **(Many-Argument Workhorses)** (@ `lib/littlefs/lfs2.c`) -> Impact: **828.2** | LOC: 1868
  * *Intent:* /// Top level file operations ///
- `do_all_the_things` **(Many-Argument Workhorses)** (@ `tools/analyze_heap_dump.py`) -> Impact: **686.4** | LOC: 675
- `f_mkfs` **(Many-Argument Workhorses)** (@ `lib/oofatfs/ff.c`) -> Impact: **463.4** | LOC: 498
  * *Intent:* #endif /* FF_USE_FORWARD */ #if FF_USE_MKFS && !FF_FS_READONLY /*-----------------------------------------------------------------------*/ /* Create a...
- `emit_inline_thumb_op` **(Many-Argument Workhorses)** (@ `py/emitinlinethumb.c`) -> Impact: **405.2** | LOC: 411
  * *Intent:* // shorthand alias for whether we allow ARMv7-M instructions #define ARMV7M asm_thumb_allow_armv7m(&emit->as)
- `parse_compile_execute` **(Many-Argument Workhorses)** (@ `shared/runtime/pyexec.c`) -> Impact: **360.3** | LOC: 767
  * *Intent:* #define EXEC_FLAG_SOURCE_IS_RAW_CODE (1 << 3) #define EXEC_FLAG_SOURCE_IS_VSTR (1 << 4) #define EXEC_FLAG_SOURCE_IS_FILENAME (1 << 5) #define EXEC_FLA...
- `mp_obj_str_format_helper` **(Many-Argument Workhorses)** (@ `py/objstr.c`) -> Impact: **345.4** | LOC: 452
  * *Intent:* #else // define to nothing to improve coverage #define terse_str_format_value_error() #endif
- `common_hal_busio_uart_construct` **(Many-Argument Workhorses)** (@ `ports/atmel-samd/common-hal/busio/UART.c`) -> Impact: **290.3** | LOC: 286
  * *Intent:* // shared-bindings validates that the tx and rx are not both missing, // and that the pins are distinct.
- `run_tests` **(Many-Argument Workhorses)** (@ `tests/run-tests.py`) -> Impact: **269.2** | LOC: 486
- `common_hal_picodvi_framebuffer_construct` **(Many-Argument Workhorses)** (@ `ports/raspberrypi/common-hal/picodvi/Framebuffer_RP2350.c`) -> Impact: **267.2** | LOC: 369

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `py` | 216 | 38612.54 | 29.33% | 20.97% |
| `lib/oofatfs` | 5 | 9331.14 | 29.67% | 6.6% |
| `tests/basics` | 558 | 8990.72 | 3.43% | 0.0% |
| `lib/littlefs` | 9 | 7981.04 | 34.42% | 11.78% |
| `tests/extmod` | 135 | 6913.8 | 15.29% | 0.0% |
| `ports/nordic` | 16 | 5329.98 | 5.1% | 18.75% |
| `lib/cmsis/inc` | 24 | 4910.86 | 6.2% | 11.75% |
| `extmod` | 36 | 4795.76 | 39.87% | 9.18% |
| `shared-module/displayio` | 21 | 3499.5 | 36.99% | 35.31% |
| `ports/zephyr-cp/cptools` | 9 | 3173.74 | 65.35% | 3.77% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `devices/ble_hci/common-hal/_bleio/Connection.c` -> **100.0%** Exposure
- `ports/analog/common-hal/microcontroller/Processor.c` -> **100.0%** Exposure
- `ports/atmel-samd/common-hal/alarm/time/TimeAlarm.c` -> **100.0%** Exposure
- `ports/broadcom/common-hal/videocore/Framebuffer.c` -> **100.0%** Exposure
- `ports/cxd56/supervisor/port.c` -> **100.0%** Exposure
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
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `16600` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/oofatfs/ff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.879)
- **Top Global Matches:** file_cluster_8: 10.879, file_cluster_3: 15.414, file_cluster_6: 22.598
- **Magnitude:** 8790.58 | **LOC:** 6028 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **3**; blast radius 0.121; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.3%), Complexity Load (formerly Cognitive Load) (80.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dir_alloc` **(Many-Argument Workhorses)** (Impact: 1051.4)
    * *Intent:* #if !FF_FS_READONLY /*-----------------------------------------------------------------------*/ /* D...
  * `f_mkfs` **(Many-Argument Workhorses)** (Impact: 463.4)
    * *Intent:* #endif /* FF_USE_FORWARD */ #if FF_USE_MKFS && !FF_FS_READONLY /*-----------------------------------...
  * `create_name` **(Many-Argument Workhorses)** (Impact: 170.8)
    * *Intent:* #endif /* FF_USE_FIND && FF_FS_MINIMIZE <= 1 */ /*--------------------------------------------------...
  * `find_volume` **(Many-Argument Workhorses)** (Impact: 147.8)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Determine logical dri...
  * `f_open` **(Many-Argument Workhorses)** (Impact: 127.6)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Open or Create a File...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1436 instances
* *State Mutation (weighted view):* 4419
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1500`, `structural_boundaries: 393`, `args: 137`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1547`, `unreferenced_by_name: 25`
* *Architecture:* `api: 31`, `import: 3`
* *Defense:* `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.000147 | `Ripple Effect (Closeness):` 0.06896
  * `Imports (Out-Degree: 5):` diskio.h, ff.h, string.h
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `lib/littlefs/lfs2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.044)
- **Top Global Matches:** file_cluster_4: 9.044, file_cluster_6: 10.446, file_cluster_16: 14.849
- **Magnitude:** 5432.42 | **LOC:** 6331 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.6%)
- **Documentation Coverage:** 67.031% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lfs2_file_rawopencfg` **(Many-Argument Workhorses)** (Impact: 828.2)
    * *Intent:* /// Top level file operations ///
  * `lfs2_dir_fetchmatch` **(Many-Argument Workhorses)** (Impact: 208.9)
    * *Intent:* #endif
  * `lfs2_dir_relocatingcommit` **(Many-Argument Workhorses)** (Impact: 124.8)
    * *Intent:* #endif #ifndef LFS2_READONLY
  * `lfs2_dir_traverse` **(Many-Argument Workhorses)** (Impact: 106.9)
  * `lfs2_dir_orphaningcommit` **(Many-Argument Workhorses)** (Impact: 92.2)
    * *Intent:* #endif #ifndef LFS2_READONLY
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 561 instances
* *State Mutation (weighted view):* 1904
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 891`, `structural_boundaries: 934`, `args: 273`, `func_start: 181`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 782`, `unreferenced_by_name: 34`
* *Architecture:* `io: 2`, `api: 51`, `import: 2`
* *Defense:* `safety: 1`, `doc: 21`, `immutability_locks: 131`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` lfs2.h, lfs2_util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/nordic/espruino_dfu_private_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/compile.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.553)
- **Top Global Matches:** file_cluster_6: 7.553, file_cluster_4: 12.525, file_cluster_8: 14.829
- **Magnitude:** 2498.12 | **LOC:** 3703 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **14**; blast radius 0.22; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.7%), Complexity Load (formerly Cognitive Load) (63.7%)
- **Documentation Coverage:** 98.4733% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compile_scope_inline_asm` **(Many-Argument Workhorses)** (Impact: 98.7)
    * *Intent:* #if MICROPY_EMIT_INLINE_ASM // requires 3 passes: SCOPE, CODE_SIZE, EMIT
  * `mp_compile_to_raw_code` **(Many-Argument Workhorses)** (Impact: 90.6)
    * *Intent:* #if !MICROPY_EXPOSE_MP_COMPILE_TO_RAW_CODE
  * `compile_expr_stmt` **(Many-Argument Workhorses)** (Impact: 68.1)
    * *Intent:* #endif
  * `compile_scope` **(Many-Argument Workhorses)** (Impact: 66.1)
  * `c_assign` **(Many-Argument Workhorses)** (Impact: 58.3)
    * *Intent:* // assigns top of stack to pn
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 242 instances
* *State Mutation (weighted view):* 765
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 681`, `structural_boundaries: 278`, `args: 168`, `func_start: 100`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 89`, `state_mutation: 281`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 40`
* *Architecture:* `api: 7`, `import: 16`
* *Defense:* `safety: 119`, `doc: 2`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.00125 | `Ripple Effect (Closeness):` 0.100528
  * `Imports (Out-Degree: 28):` assert.h, asmbase.h, compile.h, emit.h, grammar.h, nativeglue.h, persistentcode.h, runtime.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `lib/littlefs/lfs1.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.862)
- **Top Global Matches:** file_cluster_4: 5.862, file_cluster_6: 7.994, file_cluster_16: 12.63
- **Magnitude:** 2264.7 | **LOC:** 2584 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.0%), Complexity Load (formerly Cognitive Load) (72.2%)
- **Documentation Coverage:** 79.3207% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lfs1_dir_commit` **(Many-Argument Workhorses)** (Impact: 72.3)
  * `lfs1_file_opencfg` **(Many-Argument Workhorses)** (Impact: 70.8)
    * *Intent:* /// Top level file operations ///
  * `lfs1_dir_find` **(Many-Argument Workhorses)** (Impact: 65.7)
  * `lfs1_ctz_extend` **(Many-Argument Workhorses)** (Impact: 58.6)
  * `lfs1_rename` **(Many-Argument Workhorses)** (Impact: 55.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 306 instances
* *State Mutation (weighted view):* 991
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 450`, `structural_boundaries: 370`, `args: 79`, `func_start: 73`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 379`, `unreferenced_by_name: 17`
* *Architecture:* `io: 2`, `api: 29`, `import: 3`
* *Defense:* `safety: 2`, `doc: 12`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` inttypes.h, lfs1.h, lfs1_util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/objstr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.927)
- **Top Global Matches:** file_cluster_4: 5.927, file_cluster_6: 10.823, file_cluster_16: 11.215
- **Magnitude:** 2144.98 | **LOC:** 2512 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **113** in-repo importer(s); it depends on **7**; blast radius 2.702; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.9%)
- **Documentation Coverage:** 98.3193% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mp_obj_str_format_helper` **(Many-Argument Workhorses)** (Impact: 345.4)
    * *Intent:* #else // define to nothing to improve coverage #define terse_str_format_value_error() #endif
  * `str_modulo_format` **(Many-Argument Workhorses)** (Impact: 155.6)
    * *Intent:* #if MICROPY_PY_BUILTINS_STR_OP_MODULO
  * `mp_obj_str_binary_op` **(Many-Argument Workhorses)** (Impact: 64.0)
    * *Intent:* // Note: this function is used to check if an object is a str or bytes, which // works because both ...
  * `mp_str_print_quoted` **(Many-Argument Workhorses)** (Impact: 55.6)
    * *Intent:* /******************************************************************************/ /* str */...
  * `mp_obj_str_split` **(Many-Argument Workhorses)** (Impact: 47.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 245 instances
* *State Mutation (weighted view):* 758
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 497`, `structural_boundaries: 236`, `args: 176`, `func_start: 83`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 268`, `planned_debt: 8`, `unreferenced_by_name: 10`
* *Architecture:* `api: 31`, `import: 7`
* *Defense:* `safety: 91`, `doc: 2`, `immutability_locks: 149`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.702
  * `Choke Point (Betweenness):` 0.00053 | `Ripple Effect (Closeness):` 0.123074
  * `Imports (Out-Degree: 22):` assert.h, cstack.h, objlist.h, objstr.h, runtime.h, unicode.h, string.h
  * `Imported By (In-Degree: 113):` (Excluded from Brief to save tokens)

### `lib/tjpgd/src/tjpgd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 5.452)
- **Top Global Matches:** file_cluster_3: 5.452, file_cluster_8: 24.75, file_cluster_6: 37.819
- **Magnitude:** 1861.3 | **LOC:** 1158 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.064; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jd_prepare` **(Many-Argument Workhorses)** (Impact: 174.0)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Analyze the JPEG imag...
  * `mcu_output` **(Many-Argument Workhorses)** (Impact: 124.6)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Output an MCU: Conver...
  * `huffext` **(Many-Argument Workhorses)** (Impact: 70.7)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Extract a huffman dec...
  * `create_huffman_tbl` **(Many-Argument Workhorses)** (Impact: 52.0)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Create huffman code t...
  * `mcu_load` **(Compute Cores)** (Impact: 44.9)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Load all blocks in an...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 398 instances
* *State Mutation (weighted view):* 1260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 252`, `structural_boundaries: 97`, `args: 13`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 464`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 12`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000186
  * `Imports (Out-Degree: 2):` tjpgd.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/mpz.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.428)
- **Top Global Matches:** file_cluster_4: 5.428, file_cluster_16: 8.75, file_cluster_15: 9.237
- **Magnitude:** 1814.46 | **LOC:** 1757 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 0.084; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mpz_as_str_inpl` **(Many-Argument Workhorses)** (Impact: 51.7)
    * *Intent:* #endif // assumes enough space in str as calculated by mp_int_format_size // base must be between 2 ...
  * `mpn_div` **(Many-Argument Workhorses)** (Impact: 49.2)
    * *Intent:* */
  * `mpz_as_bytes` **(Many-Argument Workhorses)** (Impact: 44.0)
  * `mpz_set_from_str` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* #endif // returns number of bytes from str that were processed
  * `mpz_set_from_float` **(Many-Argument Workhorses)** (Impact: 28.7)
    * *Intent:* #if MICROPY_PY_BUILTINS_FLOAT
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 352 instances
* *State Mutation (weighted view):* 1091
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 98`, `args: 64`, `func_start: 50`
* *Risk/State:* `state_mutation: 387`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 16`
* *Architecture:* `api: 31`, `import: 3`
* *Defense:* `safety: 65`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.077389
  * `Imports (Out-Degree: 4):` assert.h, mpz.h, string.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `py/emitnative.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.663)
- **Top Global Matches:** file_cluster_16: 6.663, file_cluster_4: 7.108, file_cluster_15: 9.223
- **Magnitude:** 1515.5 | **LOC:** 3238 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **7**; blast radius 0.238; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.6%), Complexity Load (formerly Cognitive Load) (43.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emit_native_binary_op` **(Many-Argument Workhorses)** (Impact: 127.2)
  * `emit_native_start_pass` **(Many-Argument Workhorses)** (Impact: 97.2)
  * `emit_native_store_subscr` **(Compute Cores)** (Impact: 73.1)
  * `emit_native_load_subscr` **(Compute Cores)** (Impact: 62.9)
  * `emit_native_call_function` **(Many-Argument Workhorses)** (Impact: 45.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 351
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 268`, `args: 166`, `func_start: 115`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 155`, `planned_debt: 17`, `fragile_debt: 2`
* *Architecture:* `api: 8`, `import: 7`
* *Defense:* `safety: 62`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 7.6e-05 | `Ripple Effect (Closeness):` 0.001117
  * `Imports (Out-Degree: 27):` assert.h, emit.h, nativeglue.h, objfun.h, objstr.h, stdio.h, string.h
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `ports/raspberrypi/common-hal/rp2pio/StateMachine.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.369)
- **Top Global Matches:** file_cluster_4: 5.369, file_cluster_6: 10.07, file_cluster_12: 11.307
- **Magnitude:** 1480.48 | **LOC:** 1537 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **17**; blast radius 0.116; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (78.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_transfer` **(Many-Argument Workhorses)** (Impact: 225.7)
  * `rp2pio_statemachine_construct` **(Many-Argument Workhorses)** (Impact: 207.6)
  * `common_hal_rp2pio_statemachine_construct` **(Many-Argument Workhorses)** (Impact: 101.3)
  * `consider_instruction` **(Many-Argument Workhorses)** (Impact: 87.3)
  * `common_hal_rp2pio_statemachine_background_write` **(Many-Argument Workhorses)** (Impact: 44.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 129 instances
* *State Mutation (weighted view):* 458
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 284`, `args: 93`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 200`, `planned_debt: 5`, `unreferenced_by_name: 30`
* *Architecture:* `api: 42`, `import: 17`
* *Defense:* `safety: 39`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.00157
  * `Imports (Out-Degree: 16):` StateMachine.h, __init__.h, clocks.h, dma.h, irq.h, pio_instructions.h, platform_defs.h, iobank0.h...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `tests/run-tests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.263)
- **Top Global Matches:** file_cluster_6: 6.263, file_cluster_4: 9.428, file_cluster_8: 16.383
- **Magnitude:** 1386.12 | **LOC:** 1356 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (76.8%), Concurrency Surface (formerly Concurrency) (57.2%), Complexity Load (formerly Cognitive Load) (46.4%), Connectivity (formerly Api Exposure) (8.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_tests` **(Many-Argument Workhorses)** (Impact: 269.2)
  * `run_micropython` **(Many-Argument Workhorses)** (Impact: 124.0)
  * `run_one_test` **(Compute Cores)** (Impact: 89.7)
  * `main` **(I/O & Config Routines)** (Impact: 58.2)
  * `get_test_instance` **(Many-Argument Workhorses)** (Impact: 25.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 188 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 612
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 131`, `args: 27`, `func_start: 26`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 7`, `state_mutation: 236`, `unreferenced_by_name: 1`
* *Architecture:* `io: 76`, `api: 26`, `concurrency: 6`, `import: 17`
* *Defense:* `safety: 27`, `doc: 3`, `test: 8`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` argparse, glob, inspect, json, multiprocessing, multiprocessing.pool, os, platform...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shared-module/bitmaptools/__init__.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 4.778)
- **Top Global Matches:** file_cluster_8: 4.778, file_cluster_6: 13.219, file_cluster_4: 22.214
- **Magnitude:** 1378.66 | **LOC:** 1119 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 0.067; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `common_hal_bitmaptools_rotozoom` **(Many-Argument Workhorses)** (Impact: 135.4)
    * *Intent:* #include "shared-module/displayio/Bitmap.h" #include "py/mperrno.h" #include "py/runtime.h" #include...
  * `common_hal_bitmaptools_alphablend` **(Many-Argument Workhorses)** (Impact: 117.4)
  * `common_hal_bitmaptools_blit` **(Many-Argument Workhorses)** (Impact: 86.3)
  * `common_hal_bitmaptools_readinto` **(Many-Argument Workhorses)** (Impact: 72.3)
  * `draw_line` **(Many-Argument Workhorses)** (Impact: 48.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 215 instances
* *State Mutation (weighted view):* 669
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 71`, `args: 18`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 239`
* *Architecture:* `io: 1`, `api: 13`, `import: 13`
* *Defense:* `safety: 11`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000314
  * `Imports (Out-Degree: 18):` math.h, mperrno.h, runtime.h, stream.h, __init__.h, Bitmap.h, ColorConverter.h, Palette.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/AnimatedGIF/gif.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.949)
- **Top Global Matches:** file_cluster_4: 5.949, file_cluster_6: 8.614, file_cluster_12: 12.793
- **Magnitude:** 1315.44 | **LOC:** 1044 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 0.076; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.8%), Guard Balance (formerly Safety Score) (89.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.162% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GIFParseInfo` **(Many-Argument Workhorses)** (Impact: 111.4)
    * *Intent:* } /* GIFInit() */ // // Parse the GIF header, gather the size and palette info // If called with bIn...
  * `GIF_getInfo` **(Many-Argument Workhorses)** (Impact: 71.7)
    * *Intent:* } /* GIFParseInfo() */ // // Gather info about an animated GIF file //
  * `GIFMakePels` **(Many-Argument Workhorses)** (Impact: 44.7)
    * *Intent:* } /* ConvertNewPixels() */ // // GIFMakePels //
  * `DecodeLZW` **(Many-Argument Workhorses)** (Impact: 25.0)
    * *Intent:* // // Decode LZW into an image //
  * `GIF_playFrame` **(Compute Cores)** (Impact: 17.4)
    * *Intent:* } /* GIF_reset() */ // // Return value: // 1 = good decode, more frames exist // 0 = good decode, no...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 273 instances
* *State Mutation (weighted view):* 894
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 59`, `args: 43`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 348`, `dead_code: 16`, `fragile_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `io: 5`, `api: 16`, `import: 1`
* *Defense:* `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000314
  * `Imports (Out-Degree: 2):` AnimatedGIF_circuitpy.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `supervisor/shared/web_workflow/web_workflow.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.077)
- **Top Global Matches:** file_cluster_4: 7.077, file_cluster_6: 8.469, file_cluster_16: 13.368
- **Magnitude:** 1230.54 | **LOC:** 1697 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **29**; blast radius 0.076; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_reply` **(Many-Argument Workhorses)** (Impact: 207.6)
  * `_process_request` **(Many-Argument Workhorses)** (Impact: 120.1)
  * `_write_file_and_reply` **(Many-Argument Workhorses)** (Impact: 56.6)
  * `_reply_with_file` **(Many-Argument Workhorses)** (Impact: 45.4)
  * `_base64_in_place` **(Many-Argument Workhorses)** (Impact: 36.8)
    * *Intent:* // in_len is the number of bytes to encode. out_len is the number of bytes we // have to do it.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 138 instances
* *State Mutation (weighted view):* 441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 344`, `structural_boundaries: 242`, `args: 62`, `func_start: 51`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 165`, `planned_debt: 5`, `unreferenced_by_name: 6`
* *Architecture:* `api: 12`, `import: 29`
* *Defense:* `safety: 42`, `immutability_locks: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.000693 | `Ripple Effect (Closeness):` 0.064093
  * `Imports (Out-Degree: 39):` __init__.h, vfs.h, vfs_fat.h, mpversion.h, mperrno.h, mpstate.h, Hash.h, __init__.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `py/parse.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.516)
- **Top Global Matches:** file_cluster_8: 8.516, file_cluster_6: 9.773, file_cluster_4: 17.942
- **Magnitude:** 1044.84 | **LOC:** 1411 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **14**; blast radius 0.24; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mp_parse` **(Many-Argument Workhorses)** (Impact: 176.3)
  * `fold_constants` **(Many-Argument Workhorses)** (Impact: 125.0)
  * `push_result_rule` **(Many-Argument Workhorses)** (Impact: 55.2)
    * *Intent:* #endif
  * `fold_logical_constants` **(Many-Argument Workhorses)** (Impact: 42.8)
    * *Intent:* #endif
  * `mp_parse_node_print` **(Many-Argument Workhorses)** (Impact: 36.6)
    * *Intent:* #if MICROPY_DEBUG_PRINTERS
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 113 instances
* *State Mutation (weighted view):* 366
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 168`, `args: 55`, `func_start: 28`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 140`, `unreferenced_by_name: 4`
* *Architecture:* `api: 10`, `import: 27`
* *Defense:* `safety: 81`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.000293 | `Ripple Effect (Closeness):` 0.100594
  * `Imports (Out-Degree: 22):` assert.h, builtin.h, grammar.h, lexer.h, objint.h, objstr.h, parse.h, parsenum.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `devices/ble_hci/common-hal/_bleio/att.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.317)
- **Top Global Matches:** file_cluster_4: 5.317, file_cluster_16: 10.591, file_cluster_6: 10.651
- **Magnitude:** 1009.38 | **LOC:** 1802 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 0.077; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Dead Code Surface (formerly Dead Code) (85.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `att_process_data` **(Many-Argument Workhorses)** (Impact: 56.6)
  * `process_read_or_read_blob_req` **(Many-Argument Workhorses)** (Impact: 54.9)
  * `process_read_type_req` **(Many-Argument Workhorses)** (Impact: 54.2)
  * `process_write_req_or_cmd` **(Many-Argument Workhorses)** (Impact: 40.1)
    * *Intent:* // Handles BT_ATT_OP_WRITE_REQ or BT_ATT_OP_WRITE_
  * `process_find_info_req` **(Many-Argument Workhorses)** (Impact: 38.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 384
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 311`, `args: 50`, `func_start: 48`, `class_start: 63`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 170`, `dead_code: 95`, `unreferenced_by_name: 19`
* *Architecture:* `api: 22`, `import: 13`
* *Defense:* `safety: 33`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` 0.000419 | `Ripple Effect (Closeness):` 0.065113
  * `Imports (Out-Degree: 22):` att.h, Adapter.h, Attribute.h, hci.h, att_internal.h, l2cap_internal.h, obj.h, Characteristic.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ports/raspberrypi/common-hal/socketpool/Socket.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.353)
- **Top Global Matches:** file_cluster_4: 6.353, file_cluster_6: 10.672, file_cluster_12: 11.494
- **Magnitude:** 975.44 | **LOC:** 1329 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.061; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.4%), Complexity Load (formerly Cognitive Load) (66.0%)
- **Documentation Coverage:** 97.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `common_hal_socketpool_socket_connect` **(Many-Argument Workhorses)** (Impact: 51.1)
  * `lwip_tcp_receive` **(Many-Argument Workhorses)** (Impact: 44.0)
    * *Intent:* // Helper function for recv/recvfrom to handle TCP packets
  * `socketpool_socket_accept` **(Many-Argument Workhorses)** (Impact: 42.4)
  * `lwip_tcp_send` **(Many-Argument Workhorses)** (Impact: 40.0)
    * *Intent:* // Helper function for send/sendto to handle TCP packets
  * `socketpool_socket` **(Many-Argument Workhorses)** (Impact: 35.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 201`, `args: 67`, `func_start: 44`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 139`, `unreferenced_by_name: 17`
* *Architecture:* `api: 26`, `import: 25`
* *Defense:* `safety: 12`, `doc: 4`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.061
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000186
  * `Imports (Out-Degree: 24):` __init__.h, dns.h, err.h, igmp.h, init.h, netdb.h, tcp_priv.h, raw.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ports/zephyr-cp/cptools/zephyr2cp.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.983)
- **Top Global Matches:** file_cluster_3: 8.983, file_cluster_8: 21.528, file_cluster_6: 34.028
- **Magnitude:** 973.3 | **LOC:** 897 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 0.094; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.2%), Guard Balance (formerly Safety Score) (89.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `zephyr_dts_to_cp_board` **(Many-Argument Workhorses)** (Impact: 231.4)
  * `find_flash_devices` **(Compute Cores)** (Impact: 35.0)
    * *Intent:* """ Find all flash devices from a device tree. Args: device_tree: Parsed device tree (dtlib.DT objec...
  * `find_ram_regions` **(Compute Cores)** (Impact: 24.5)
    * *Intent:* """ Find all RAM regions from a device tree. Includes the zephyr,sram node and any zephyr,memory-reg...
  * `_label_to_end` **(Encapsulated Accessors)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 210 instances
* *State Mutation (weighted view):* 664
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 39`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 244`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 3`, `import: 6`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000279
  * `Imports (Out-Degree: 1):` compat2driver, cpbuild, devicetree, logging, pathlib, yaml
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `py/runtime.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.081)
- **Top Global Matches:** file_cluster_4: 6.081, file_cluster_15: 7.528, file_cluster_12: 8.498
- **Magnitude:** 965.78 | **LOC:** 1978 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **551** in-repo importer(s); it depends on **22**; blast radius 6.988; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.4%), Debt Markers (formerly Tech Debt) (89.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mp_unary_op` **(Compute Cores)** (Impact: 57.7)
  * `mp_convert_member_lookup` **(Many-Argument Workhorses)** (Impact: 57.4)
    * *Intent:* #endif // MICROPY_BUILTIN_METHOD_CHECK_SELF_ARG // Given a member that was extracted from an instanc...
  * `mp_resume` **(Many-Argument Workhorses)** (Impact: 42.3)
  * `mp_store_attr` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `mp_load_method_maybe` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* // no attribute found, returns: dest[0] == MP_OBJ_NULL, dest[1] == MP_OBJ_NULL // normal attribute f...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 134 instances
* *State Mutation (weighted view):* 433
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 305`, `structural_boundaries: 172`, `args: 128`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 165`, `planned_debt: 12`, `unreferenced_by_name: 38`
* *Architecture:* `api: 72`, `import: 22`
* *Defense:* `safety: 49`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.988
  * `Choke Point (Betweenness):` 0.007988 | `Ripple Effect (Closeness):` 0.135479
  * `Imports (Out-Degree: 39):` assert.h, vfs.h, builtin.h, compile.h, cstack.h, gc.h, mperrno.h, objgenerator.h...
  * `Imported By (In-Degree: 551):` (Excluded from Brief to save tokens)

### `py/profile.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.544)
- **Top Global Matches:** file_cluster_4: 5.544, file_cluster_6: 10.494, file_cluster_16: 10.845
- **Magnitude:** 922.06 | **LOC:** 846 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 0.077; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.6%), Guard Balance (formerly Safety Score) (85.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mp_prof_opcode_decode` **(Many-Argument Workhorses)** (Impact: 196.9)
  * `frame_attr` **(Stateful Encapsulated Methods)** (Impact: 19.4)
  * `mp_prof_instr_tick` **(Defensive Guards)** (Impact: 16.6)
  * `mp_prof_frame_enter` **(Compute Cores)** (Impact: 11.9)
  * `mp_prof_print_instr` **(Compute Cores)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 193 instances
* *State Mutation (weighted view):* 615
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 111`, `args: 18`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `state_mutation: 229`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 6`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `safety: 12`, `doc: 3`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.066586
  * `Imports (Out-Degree: 13):` bc0.h, gc.h, objfun.h, profile.h, runtime0.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `py/objtype.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.052)
- **Top Global Matches:** file_cluster_6: 5.052, file_cluster_4: 10.852, file_cluster_8: 13.97
- **Magnitude:** 886.04 | **LOC:** 1562 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **6**; blast radius 1.57; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.8%), Complexity Load (formerly Cognitive Load) (42.6%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mp_obj_class_lookup` **(Many-Argument Workhorses)** (Impact: 51.8)
  * `mp_obj_instance_store_attr` **(Many-Argument Workhorses)** (Impact: 50.2)
  * `mp_obj_new_type` **(Many-Argument Workhorses)** (Impact: 48.3)
  * `type_attr` **(Many-Argument Workhorses)** (Impact: 44.5)
  * `super_attr` **(Many-Argument Workhorses)** (Impact: 40.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 165`, `args: 80`, `func_start: 34`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 98`, `planned_debt: 7`, `unreferenced_by_name: 4`
* *Architecture:* `api: 11`, `import: 6`
* *Defense:* `safety: 49`, `doc: 5`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.57
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.120971
  * `Imports (Out-Degree: 17):` assert.h, objtype.h, runtime.h, stddef.h, stdio.h, string.h
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `tests/perf_bench/bm_hexiom.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.353)
- **Top Global Matches:** file_cluster_4: 6.353, file_cluster_12: 8.624, file_cluster_15: 8.681
- **Magnitude:** 872.96 | **LOC:** 658 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.059; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (88.5%), Complexity Load (formerly Cognitive Load) (29.3%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constraint_pass` **(Compute Cores)** (Impact: 78.3)
    * *Intent:* ##################################
  * `solved` **(Compute Cores)** (Impact: 33.9)
  * `solve_step` **(Many-Argument Workhorses)** (Impact: 28.3)
  * `print_pos` **(Compute Cores)** (Impact: 23.9)
  * `read_file` **(Compute Cores)** (Impact: 19.3)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` io
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/maketranslationdata.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.571)
- **Top Global Matches:** file_cluster_12: 7.571, file_cluster_4: 8.065, file_cluster_15: 9.423
- **Magnitude:** 867.48 | **LOC:** 659 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.3%), Guard Balance (formerly Safety Score) (88.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compute_huffman_coding` **(Many-Argument Workhorses)** (Impact: 161.8)
    * *Intent:* # possible future improvement: some languages are better when consider len(k) > 2. try both? qstrs =...
  * `decompress` **(Many-Argument Workhorses)** (Impact: 24.3)
  * `compress` **(Many-Argument Workhorses)** (Impact: 21.8)
  * `compute_unicode_offset` **(Compute Cores)** (Impact: 13.7)
  * `parse_input_headers` **(Compute Cores)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 495
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 83`, `args: 30`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 195`, `unreferenced_by_name: 3`
* *Architecture:* `io: 7`, `api: 27`, `import: 12`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, argparse, bisect, collections, dataclasses, gettext, html.entities, huffman...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shared-module/displayio/TileGrid.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.118)
- **Top Global Matches:** file_cluster_4: 7.118, file_cluster_12: 8.495, file_cluster_15: 10.036
- **Magnitude:** 859.68 | **LOC:** 735 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **8**; blast radius 0.082; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Complexity Load (formerly Cognitive Load) (92.2%), Guard Balance (formerly Safety Score) (81.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `displayio_tilegrid_fill_area` **(Many-Argument Workhorses)** (Impact: 109.6)
  * `common_hal_displayio_tilegrid_construct` **(Many-Argument Workhorses)** (Impact: 57.6)
    * *Intent:* #include "shared-bindings/displayio/TileGrid.h" #include "py/runtime.h" #include "shared-bindings/di...
  * `displayio_tilegrid_get_refresh_areas` **(Compute Cores)** (Impact: 49.8)
  * `displayio_tilegrid_finish_refresh` **(Compute Cores)** (Impact: 19.7)
  * `common_hal_displayio_tilegrid_set_all_tiles` **(Compute Cores)** (Impact: 18.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 126 instances
* *State Mutation (weighted view):* 416
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 122`, `args: 39`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 164`, `dead_code: 4`, `planned_debt: 3`, `unreferenced_by_name: 33`
* *Architecture:* `api: 34`, `import: 8`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.082
  * `Choke Point (Betweenness):` 0.000334 | `Ripple Effect (Closeness):` 0.057253
  * `Imports (Out-Degree: 18):` runtime.h, Bitmap.h, ColorConverter.h, OnDiskBitmap.h, Palette.h, TileGrid.h, TilePaletteMapper.h, serial.h
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `py/emitinlinethumb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.503)
- **Top Global Matches:** file_cluster_4: 6.503, file_cluster_16: 8.095, file_cluster_15: 9.892
- **Magnitude:** 838.52 | **LOC:** 866 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emit_inline_thumb_op` **(Many-Argument Workhorses)** (Impact: 405.2)
    * *Intent:* // shorthand alias for whether we allow ARMv7-M instructions #define ARMV7M asm_thumb_allow_armv7m(&...
  * `get_arg_reglist` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `get_arg_reg` **(Stateful Encapsulated Methods)** (Impact: 21.3)
  * `get_arg_vfpreg` **(Stateful Encapsulated Methods)** (Impact: 17.3)
  * `emit_inline_thumb_count_params` **(Stateful Encapsulated Methods)** (Impact: 14.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 69`, `args: 45`, `func_start: 19`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 95`, `planned_debt: 3`
* *Architecture:* `api: 10`, `import: 9`
* *Defense:* `safety: 5`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` assert.h, asmthumb.h, emit.h, grammar.h, stdarg.h, stdint.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tools/ci_set_idf_constraint.py` (PYTHON) | Magnitude: 0.03 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 18, core_var_decl: 10, state_mutation: 8, design_snake_case: 8
- `ports/zephyr-cp/tests/bsim/conftest.py` (PYTHON) | Magnitude: 176.26 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 137, core_var_decl: 47, state_mutation: 45, design_snake_case: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/basics/async_with_break.py` (EMBEDDED_PYTHON) | Magnitude: 31.42 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 38, debug_prints: 20, safety: 15, structural_boundaries: 13
- `ports/espressif/boards/makerfabs_tft7/board.c` (C) | Magnitude: 51.44 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 63, pointers: 34, state_mutation: 14, core_var_decl: 11
- `ports/stm/supervisor/port.c` (C) | Magnitude: 186.62 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 184, structural_boundaries: 85, pointers: 64, args: 58
- `ports/stm/common-hal/alarm/SleepMemory.c` (C) | Magnitude: 22.78 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 16, macros: 9, args: 5
- `ports/nordic/common-hal/rtc/RTC.c` (C) | Magnitude: 21.4 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 14, args: 8, import: 8, pointers: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `ports/espressif/common-hal/_bleio/Connection.c` (C) | Magnitude: 250.98 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 294, pointers: 197, structural_boundaries: 72, branch: 60
- `tests/micropython/heapalloc_super.py` (EMBEDDED_PYTHON) | Magnitude: 8.74 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, debug_prints: 4, args: 3
- `tests/basics/memoryview1.py` (EMBEDDED_PYTHON) | Magnitude: 28.2 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: debug_prints: 33, memory_alloc: 28, state_mutation: 12, indent_spaces: 12
- `tests/thread/thread_sleep2.py` (EMBEDDED_PYTHON) | Magnitude: 46.24 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 11, debug_prints: 6, concurrency: 5, structural_boundaries: 4
- `tests/basics/nanbox_smallint.py` (EMBEDDED_PYTHON) | Magnitude: 17.66 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 11, debug_prints: 8, explicit_casts: 6, safety: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/inlineasm/thumb/asmit.py` (PYTHON) | Magnitude: 4.16 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 2, args: 2, func_start: 2
- `tests/inlineasm/thumb/asmdiv.py` (PYTHON) | Magnitude: 5.86 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: debug_prints: 7, structural_boundaries: 2, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `ports/nordic/common-hal/memorymap/AddressRange.c` (C) | Magnitude: 88.6 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 61, pointers: 32, branch: 26, safety: 16
- `tests/thread/stress_create.py` (EMBEDDED_PYTHON) | Magnitude: 29.84 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, branch: 3, safety_bypasses: 3
- `tests/basics/struct2.py` (EMBEDDED_PYTHON) | Magnitude: 16.14 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: debug_prints: 23, indent_spaces: 23, scientific: 13, safety: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `ports/espressif/common-hal/_bleio/ble_events.c` (C) | Magnitude: 73.7 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 57, pointers: 42, structural_boundaries: 18, branch: 13
- `tests/inlineasm/thumb/asmblbx.py` (PYTHON) | Magnitude: 2.48 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, debug_prints: 2, structural_boundaries: 1, args: 1
- `ports/espressif/common-hal/alarm/SleepMemory.c` (C) | Magnitude: 16.98 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 10, import: 5, pointers: 5
- `ports/analog/common-hal/microcontroller/__init__.c` (C) | Magnitude: 33.48 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 324, args: 305, macros: 198, pointers: 100
- `shared-module/usb_cdc/__init__.c` (C) | Magnitude: 156.52 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 205, pointers: 57, structural_boundaries: 40, state_mutation: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `py/mpz.h` (C) | Magnitude: 57.08 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: pointers: 92, structural_boundaries: 52, api: 47, immutability_locks: 40
- `ports/atmel-samd/common-hal/alarm/__init__.c` (C) | Magnitude: 104.56 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 98, pointers: 30, structural_boundaries: 28, branch: 22
- `supervisor/shared/usb/usb_msc_flash.c` (C) | Magnitude: 244.44 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 230, structural_boundaries: 91, branch: 56, pointers: 47
- `ports/zephyr-cp/common-hal/wifi/ScannedNetworks.c` (C) | Magnitude: 60.9 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 71, pointers: 58, branch: 17, structural_boundaries: 15
- `py/objcode.h` (C) | Magnitude: 18.12 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: pointers: 30, indent_spaces: 21, structural_boundaries: 17, immutability_locks: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `ports/atmel-samd/boards/dynossat_edu_eps/pins.c` (C) | Magnitude: 15.78 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, args: 34, pointers: 34, globals: 1
- `ports/atmel-samd/boards/metro_m4_express/pins.c` (C) | Magnitude: 15.78 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, args: 34, pointers: 34, globals: 1
- `ports/atmel-samd/boards/pyruler/pins.c` (C) | Magnitude: 15.78 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, args: 34, pointers: 34, globals: 1
- `ports/nordic/boards/challenger_840/pins.c` (C) | Magnitude: 15.78 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, args: 34, pointers: 34, globals: 1
- `ports/nordic/boards/itsybitsy_nrf52840_express/pins.c` (C) | Magnitude: 15.78 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, args: 34, pointers: 34, globals: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `ports/atmel-samd/boards/monster_m4sk/board.c` (C) | Magnitude: 7.66 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 51, pointers: 19, structural_boundaries: 12, import: 7
- `ports/atmel-samd/boards/cp32-m4/pins.c` (C) | Magnitude: 15.8 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 36, args: 35, pointers: 35, globals: 1
- `ports/atmel-samd/boards/escornabot_makech/pins.c` (C) | Magnitude: 15.8 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 36, args: 35, pointers: 35, globals: 1
- `ports/atmel-samd/boards/feather_m0_adalogger/pins.c` (C) | Magnitude: 15.8 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 36, args: 35, pointers: 35, globals: 1
- `ports/atmel-samd/boards/pewpew10/pins.c` (C) | Magnitude: 15.8 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 36, args: 35, pointers: 35, globals: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `supervisor/shared/external_flash/external_flash.c` (C) | Magnitude: 332.4 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 347, structural_boundaries: 144, branch: 106, core_var_decl: 56
- `ports/zephyr-cp/cptools/cpbuild.py` (PYTHON) | Magnitude: 679.04 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 312, state_mutation: 105, core_var_decl: 90, design_snake_case: 86
- `ports/zephyr-cp/supervisor/flash.c` (C) | Magnitude: 360.96 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 382, structural_boundaries: 131, branch: 95, core_var_decl: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tools/diff_nm_sizes.py` (PYTHON) | Magnitude: 0.05 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, core_var_decl: 13, design_snake_case: 13, state_mutation: 12
- `tools/safe_mode_finder.py` (PYTHON) | Magnitude: 0.13 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 97, state_mutation: 45, core_var_decl: 43, design_snake_case: 43
- `ports/espressif/tools/decode_backtrace.py` (PYTHON) | Magnitude: 0.05 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, branch: 12, state_mutation: 11, core_var_decl: 11
- `ports/zephyr-cp/cptools/get_west_shield_args.py` (PYTHON) | Magnitude: 57.04 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 16, core_var_decl: 15, design_snake_case: 15
- `tests/basics/subclass_native_exc_new.py` (EMBEDDED_PYTHON) | Magnitude: 9.78 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 15, debug_prints: 5, safety_bypasses: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `py/sequence.c` (C) | Magnitude: 196.96 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 119, pointers: 57, branch: 46, structural_boundaries: 39
- `shared-module/sdcardio/__init__.c` (C) | Magnitude: 66.58 | Delta: **0.17** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 76, pointers: 39, structural_boundaries: 23, state_mutation: 22

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `shared-module/busdisplay/BusDisplay.c` -> Churn: **100.0%** | Cog Load: 68.3813% | Debt: 79.5231%
- `ports/zephyr-cp/supervisor/port.c` -> Churn: **95.43%** | Cog Load: 50.1051% | Debt: 99.1513%
- `ports/espressif/common-hal/qspibus/QSPIBus.c` -> Churn: **93.55%** | Cog Load: 66.7472% | Debt: 46.6448%
- `ports/zephyr-cp/cptools/zephyr2cp.py` -> Churn: **89.15%** | Cog Load: 63.3589% | Debt: 0.0%
- `ports/zephyr-cp/cptools/build_circuitpython.py` -> Churn: **88.61%** | Cog Load: 98.1236% | Debt: 9.0074%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `py/mpz.c` -> **Scott Shawcroft** (100.0% isolated ownership) | Magnitude: 1814.46
- `shared-module/bitmaptools/__init__.c` -> **foamyguy** (100.0% isolated ownership) | Magnitude: 1378.66
- `ports/raspberrypi/common-hal/socketpool/Socket.c` -> **Scott Shawcroft** (100.0% isolated ownership) | Magnitude: 975.44
- `ports/zephyr-cp/cptools/zephyr2cp.py` -> **Scott Shawcroft** (100.0% isolated ownership) | Magnitude: 973.3
- `shared-module/displayio/TileGrid.c` -> **P. Patrick Socha** (100.0% isolated ownership) | Magnitude: 859.68

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `py/gc.c` -> **Severity: 1.81** (Bridge: 0.0181 * Flux: 99.9995%)
- `main.c` -> **Severity: 1.731** (Bridge: 0.0173 * Flux: 99.9363%)
- `py/objexcept.c` -> **Severity: 1.399** (Bridge: 0.014 * Flux: 100.0%)
- `py/runtime.c` -> **Severity: 0.799** (Bridge: 0.008 * Flux: 99.9911%)
- `shared-module/displayio/__init__.c` -> **Severity: 0.427** (Bridge: 0.0043 * Flux: 99.6184%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `py/objexcept.c` -> **Severity: 10.268** (Embedded: 0.1506 * Error Risk: 68.1767%)
- `py/obj.h` -> **Severity: 10.196** (Embedded: 0.225 * Error Risk: 45.3086%)
- `shared/libc/string0.c` -> **Severity: 10.19** (Embedded: 0.1288 * Error Risk: 79.0893%)
- `py/mpprint.c` -> **Severity: 9.798** (Embedded: 0.1241 * Error Risk: 78.9234%)
- `py/obj.c` -> **Severity: 9.382** (Embedded: 0.1591 * Error Risk: 58.9844%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `py/obj.h` -> **Severity: 8050.2** (Blast Radius: 80.502 * Doc Risk: 100.0%)
- `py/misc.h` -> **Severity: 2716.3** (Blast Radius: 27.163 * Doc Risk: 100.0%)
- `py/obj.c` -> **Severity: 1490.8** (Blast Radius: 14.908 * Doc Risk: 100.0%)
- `py/objexcept.c` -> **Severity: 1235.3** (Blast Radius: 12.353 * Doc Risk: 100.0%)
- `supervisor/shared/translate/translate_impl.h` -> **Severity: 1089.7** (Blast Radius: 10.897 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 9726 literal sites + 147 sites through wrappers = 9873
- **`memory_alloc`:** 458 literal sites + 85 sites through wrappers = 543
- **`panics_and_aborts`:** 1238 literal sites + 88 sites through wrappers = 1326

- `port_malloc` (macro, memory_alloc, primitive): 46 call sites in 30 files -- `shared-module/bitmapfilter/__init__.c`
- `reset_into_safe_mode` (function, panics_and_aborts, primitive): 46 call sites in 24 files -- `supervisor/stub/safe_mode.c`
- `skip` (function, debug_prints, primitive): 10 call sites in 1 files -- `tests/testlib/skip_if.py`
- `skip` (function, panics_and_aborts, primitive): 10 call sites in 1 files -- `tests/testlib/skip_if.py`
- `lfs2_malloc` (function, memory_alloc, primitive): 7 call sites in 1 files -- `lib/littlefs/lfs2_util.h`
- `task` (function, debug_prints, primitive): 7 call sites in 1 files -- `tests/extmod/asyncio_gather.py`
- `sub` (function, debug_prints, primitive): 6 call sites in 5 files -- `tests/micropython/viper_binop_arith.py`
- `task` (function, debug_prints, primitive): 6 call sites in 1 files -- `tests/extmod/asyncio_event.py`
- `invalid_args` (function, debug_prints, primitive): 5 call sites in 1 files -- `ports/unix/main.c`
- `lfs1_malloc` (function, memory_alloc, primitive): 5 call sites in 1 files -- `lib/littlefs/lfs1_util.h`
- `task` (function, debug_prints, primitive): 5 call sites in 1 files -- `tests/extmod/asyncio_wait_for.py`
- `bar` (function, debug_prints, primitive): 4 call sites in 1 files -- `tests/basics/closure_defargs.py`
*(+89 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 54263 call pairs -- scoped 19.8%, unique 24.7%, ambiguous 10.4%, external 45.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 40979 | 19.5% | 32.7% | 10.0% | 37.8% |
| python | 7057 | 20.7% | 0.0% | 13.3% | 65.9% |
| embedded_python | 5887 | 20.9% | 0.0% | 10.5% | 68.6% |
| shell | 240 | 22.9% | 0.0% | 0.0% | 77.1% |
| javascript | 80 | 17.5% | 0.0% | 0.0% | 82.5% |
| cpp | 11 | 9.1% | 72.7% | 9.1% | 9.1% |
| csharp | 5 | 0.0% | 0.0% | 0.0% | 100.0% |
| assembly | 2 | 0.0% | 50.0% | 50.0% | 0.0% |
| makefile | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
