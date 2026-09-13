# ARCHITECTURAL_BRIEF: micropython
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/micropython/micropython` |
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
| Total Artifacts | 6478 |
| Analyzed Artifacts (Scanned) | 4990 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1488 |
| Total LOC | 419704 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 77.0% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6165 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1173 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.9034 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 202 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 2149 | 316846 | 43.1% |
| PYTHON | 1724 | 59442 | 34.5% |
| CSV | 262 | 20030 | 5.3% |
| MAKEFILE | 241 | 7250 | 4.8% |
| JSON | 214 | 4425 | 4.3% |
| EMBEDDED_PYTHON | 151 | 7148 | 3.0% |
| MARKDOWN | 133 | 0 | 2.7% |
| JAVASCRIPT | 46 | 1718 | 0.9% |
| SHELL | 22 | 1674 | 0.4% |
| ASSEMBLY | 19 | 724 | 0.4% |
| PLAINTEXT | 14 | 0 | 0.3% |
| XML | 9 | 0 | 0.2% |
| CPP | 2 | 83 | 0.0% |
| YAML | 2 | 37 | 0.0% |
| PROTO | 1 | 326 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4841 | 97.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 148 | 3.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1488*

**Composition by Extension & Reason:**
- `.exp`: 623x Excluded (Unsupported Extension: '.exp'), 9x Unsupported Format (.exp)
- `.rst`: 241x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cmake`: 125x Excluded (Unsupported Extension: '.cmake')
- `.ld`: 115x Excluded (Unsupported Extension: '.ld')
- `.h`: 12x Excluded (Machine-Generated Source Code Signature: 6 LOC), 7x Excluded (Machine-Generated Source Code Signature: 63 LOC), 7x Excluded (Machine-Generated Source Code Signature: 12 LOC)
- `.yml`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 153 LOC), 1x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.conf`: 28x Excluded (Unsupported Extension: '.conf')
- `.board`: 26x Excluded (Unsupported Extension: '.board')
- `.c`: 2x Excluded (Machine-Generated Source Code Signature: 72 LOC), 2x Excluded (Machine-Generated Source Code Signature: 6 LOC), 2x Excluded (Machine-Generated Source Code Signature: 54 LOC)
- `no_extension`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.p4_wifi_common')
- `.jpg`: 14x Excluded (Explicitly Denied Extension: '.jpg')
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.overlay`: 8x Excluded (Unsupported Extension: '.overlay')
- `.props`: 7x Excluded (Unsupported Extension: '.props')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 37.8 | 41.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 9.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.3 | 0.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 20.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 91.7 | 0.9 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 49.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 42.6 | 0.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 36.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 78573 | 1823 | 33 | `lib/littlefs/lfs2.c` |
| cleanup | 326 | 171 | 0 | `tools/pyboard.py` |
| guards | 30535 | 2372 | 17 | `lib/littlefs/lfs2.c` |
| danger | 6497 | 1592 | 3 | `tools/ci.sh` |
| concurrency | 1681 | 277 | 0 | `tests/extmod/asyncio_wait_for.py` |
| connectivity | 16878 | 2444 | 9 | `py/obj.h` |
| io | 2994 | 472 | 0 | `tests/ports/cc3200/pin.py` |
| crypto | 59 | 58 | 0 | `tools/mpremote/mpremote/transport.py` |
| ipc | 805 | 90 | 0 | `extmod/modlwip.c` |
| time | 197 | 91 | 0 | `tests/run-multitests.py` |
| serialization | 20 | 7 | 0 | `tests/extmod/marshal_basic.py` |
| regex | 302 | 79 | 0 | `tests/extmod/re1.py` |
| events | 1029 | 237 | 0 | `ports/stm32/timer.c` |
| tests | 285 | 55 | 0 | `tests/extmod_hardware/machine_i2c_target.py` |
| docs | 22988 | 603 | 1 | `lib/cmsis/inc/core_cm55.h` |
| debt | 13582 | 1881 | 8 | `tools/mpy-tool.py` |
| mutation | 82091 | 2722 | 41 | `lib/oofatfs/ff.c` |
| dead_code | 6074 | 1339 | 3 | `tools/ci.sh` |
| credential | 2 | 2 | 0 | `ports/stm32/boards/NUCLEO_WB55/rfcore_makefirmware.py` |
| threat | 3626 | 696 | 1 | `py/obj.h` |
| ml_ai | 298 | 113 | 0 | `py/emitinlinerv32.c` |
| ui | 46 | 9 | 0 | `ports/nrf/examples/seeed_tft.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/ports/cc3200/pin.py` (Hits: 110)
- `tests/run-tests.py` (Hits: 65)
- `tools/ci.sh` (Hits: 62)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **runtime.h** (`py/runtime.h`) — 476 inbound connections
2. **mphal.h** (`py/mphal.h`) — 410 inbound connections
3. **obj.h** (`py/obj.h`) — 190 inbound connections
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

- `dir_alloc` (@ `lib/oofatfs/ff.c`) -> Impact: **1252.7** | LOC: 1949
  * *Intent:* #if !FF_FS_READONLY /*-----------------------------------------------------------------------*/ /* Directory handling - Reserve a block of directory e...
- `lfs2_file_opencfg_` (@ `lib/littlefs/lfs2.c`) -> Impact: **852.4** | LOC: 1862
  * *Intent:* /// Top level file operations ///
- `f_mkfs` (@ `lib/oofatfs/ff.c`) -> Impact: **473.4** | LOC: 454
  * *Intent:* #endif /* FF_USE_FORWARD */ #if FF_USE_MKFS && !FF_FS_READONLY /*-----------------------------------------------------------------------*/ /* Create a...
- `uart_init` (@ `ports/stm32/uart.c`) -> Impact: **457.2** | LOC: 490
  * *Intent:* // assumes Init parameters have been set up correctly
- `mp_obj_str_format_helper` (@ `py/objstr.c`) -> Impact: **443.0** | LOC: 446
  * *Intent:* #else // define to nothing to improve coverage #define terse_str_format_value_error() #endif
- `adc_wait_for_eoc_or_timeout` (@ `ports/stm32/adc.c`) -> Impact: **406.0** | LOC: 845
- `emit_inline_thumb_op` (@ `py/emitinlinethumb.c`) -> Impact: **405.2** | LOC: 411
  * *Intent:* // shorthand alias for whether we allow ARMv7-M instructions #define ARMV7M asm_thumb_allow_armv7m(&emit->as)
- `parse_string_literal` (@ `py/lexer.c`) -> Impact: **307.0** | LOC: 371
- `run_tests` (@ `tests/run-tests.py`) -> Impact: **301.2** | LOC: 440
- `mp_bytecode_print_str` (@ `py/showbc.c`) -> Impact: **239.9** | LOC: 388

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `py` | 206 | 40262.14 | 38.42% | 24.87% |
| `ports/stm32` | 161 | 28017.92 | 27.71% | 28.42% |
| `extmod` | 92 | 16135.02 | 35.5% | 11.18% |
| `tests/basics` | 571 | 9954.66 | 3.97% | 0.0% |
| `lib/oofatfs` | 4 | 9463.28 | 27.25% | 8.34% |
| `lib/littlefs` | 9 | 8242.26 | 39.48% | 17.24% |
| `ports/esp32` | 74 | 8220.8 | 24.62% | 28.2% |
| `tests/extmod` | 195 | 7408.3 | 14.14% | 0.0% |
| `ports/mimxrt` | 68 | 6436.0 | 26.22% | 38.37% |
| `lib/cmsis/inc` | 30 | 6249.09 | 7.9% | 12.76% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ports/cc3200/hal/systick.c` -> **100.0%** Exposure
- `ports/pic16bit/pic16bit_mphal.c` -> **100.0%** Exposure
- `ports/renesas-ra/ra/ra_utils.c` -> **100.0%** Exposure
- `ports/stm32/usbhost/Core/Src/usbh_conf_template.c` -> **100.0%** Exposure
- `py/asmarm.c` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `drivers/cc3100/src/fs.c` -> **100.0%** Exposure
- `drivers/cc3100/src/socket.c` -> **100.0%** Exposure
- `drivers/cc3100/src/spawn.c` -> **100.0%** Exposure
- `extmod/machine_timer.c` -> **100.0%** Exposure
- `extmod/modbinascii.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tools/ci.sh` -> **103** Orphaned Functions | **0** Duplicates
- `ports/stm32/stm32_it.c` -> **78** Orphaned Functions | **2** Duplicates
- `ports/cc3200/hal/i2c.c` -> **51** Orphaned Functions | **0** Duplicates
- `ports/cc3200/hal/prcm.c` -> **48** Orphaned Functions | **0** Duplicates
- `lib/cmsis/inc/core_starmc1.h` -> **41** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `11` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10377` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `extmod/asyncio/stream.py` (PYTHON) -> Cumulative Risk: **792.66**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 244.26 | **LOC:** 223 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `_serve` (Impact: 12.7), `open_connection` (Impact: 12.4), `stream_awrite` (Impact: 9.3)

### 2. `extmod/asyncio/core.py` (PYTHON) -> Cumulative Risk: **743.99**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 315.16 | **LOC:** 325 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.3447%)
- **Heaviest Functions:** `run_until_complete` (Impact: 37.1), `wait_io_event` (Impact: 18.2), `remove` (Impact: 12.7)

### 3. `ports/webassembly/asyncio/core.py` (PYTHON) -> Cumulative Risk: **743.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 228.0 | **LOC:** 268 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.1163%)
- **Heaviest Functions:** `_run_iter` (Impact: 18.8), `__next__` (Impact: 4.6), `_promote_to_task` (Impact: 4.3)

### 4. `extmod/asyncio/funcs.py` (PYTHON) -> Cumulative Risk: **714.75**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 198.78 | **LOC:** 146 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `gather` (Impact: 42.2), `wait_for` (Impact: 11.4), `done` (Impact: 11.3)

### 5. `py/runtime.c` (C) -> Cumulative Risk: **699.21**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1151.28 | **LOC:** 1787 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 37.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9976%), Cognitive Load (94.4663%)
- **Heaviest Functions:** `mp_call_prepare_args_n_kw_var` (Impact: 86.0), `mp_unary_op` (Impact: 68.1), `mp_convert_member_lookup` (Impact: 45.2)

### 6. `py/makeqstrdefs.py` (PYTHON) -> Cumulative Risk: **687.77**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 240.38 | **LOC:** 238 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9244%)
- **Heaviest Functions:** `process_file` (Impact: 28.8), `preprocess` (Impact: 14.1), `cat_together` (Impact: 9.8)

### 7. `shared/libc/string0.c` (C) -> Cumulative Risk: **675.07**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 330.04 | **LOC:** 262 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9996%)
- **Heaviest Functions:** `strncmp` (Impact: 26.6), `strcmp` (Impact: 17.9), `memcpy` (Impact: 17.7)

### 8. `ports/renesas-ra/ra/ra_rtc.c` (C) -> Cumulative Risk: **672.84**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 343.14 | **LOC:** 431 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (97.7023%)
- **Heaviest Functions:** `ra_rtc_set_adjustment` (Impact: 30.4), `ra_rtc_init` (Impact: 16.3), `ra_rtc_set_subclock` (Impact: 13.1)

### 9. `py/objint_longlong.c` (C) -> Cumulative Risk: **666.37**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 337.02 | **LOC:** 366 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9956%), Tech Debt (98.8556%)
- **Heaviest Functions:** `mp_obj_int_binary_op` (Impact: 129.1), `mp_obj_int_to_bytes_impl` (Impact: 24.1), `mp_obj_int_unary_op` (Impact: 20.7)

### 10. `ports/rp2/boards/make-pins.py` (PYTHON) -> Cumulative Risk: **659.66**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 149.04 | **LOC:** 162 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8305%), Safety Score (94.8811%)
- **Heaviest Functions:** `add_af` (Impact: 23.6), `validate_cpu_pin_name` (Impact: 13.4), `load_inputs` (Impact: 9.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `lib/oofatfs/ff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9338.02 | **LOC:** 5948 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.1749%), Tech Debt (12.5468%)
**Top Internal Functions/Classes:**
  * `dir_alloc` (Impact: 1252.7)
    * *Intent:* #if !FF_FS_READONLY /*-----------------------------------------------------------------------*/ /* D...
  * `f_mkfs` (Impact: 473.4)
    * *Intent:* #endif /* FF_USE_FORWARD */ #if FF_USE_MKFS && !FF_FS_READONLY /*-----------------------------------...
  * `create_name` (Impact: 182.7)
    * *Intent:* #endif /* FF_USE_FIND && FF_FS_MINIMIZE <= 1 */ /*--------------------------------------------------...
  * `find_volume` (Impact: 168.6)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Determine logical dri...
  * `f_open` (Impact: 156.7)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Open or Create a File...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1449 instances
* *State Mutation (weighted view):* 4441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1803`, `structural_boundaries: 391`, `args: 137`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1543`, `unreferenced_by_name: 26`
* *Architecture:* `api: 31`, `import: 3`
* *Defense:* `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` diskio.h, ff.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/littlefs/lfs2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5538.14 | **LOC:** 6550 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (89.9365%), Tech Debt (14.1278%)
**Top Internal Functions/Classes:**
  * `lfs2_file_opencfg_` (Impact: 852.4)
    * *Intent:* /// Top level file operations ///
  * `lfs2_dir_fetchmatch` (Impact: 208.9)
    * *Intent:* #endif
  * `lfs2_dir_relocatingcommit` (Impact: 132.9)
    * *Intent:* #endif #ifndef LFS2_READONLY
  * `lfs2_dir_traverse` (Impact: 106.9)
  * `lfs2_dir_orphaningcommit` (Impact: 96.7)
    * *Intent:* #endif #ifndef LFS2_READONLY
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 558 instances
* *State Mutation (weighted view):* 1898
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 937`, `structural_boundaries: 964`, `args: 279`, `func_start: 187`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 74`, `state_mutation: 782`, `dead_code: 11`, `unreferenced_by_name: 34`
* *Architecture:* `io: 2`, `api: 52`, `import: 2`
* *Defense:* `safety: 1`, `doc: 21`, `immutability_locks: 134`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` lfs2.h, lfs2_util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/compile.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2665.92 | **LOC:** 3699 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (67.9462%), Tech Debt (45.5428%)
**Top Internal Functions/Classes:**
  * `mp_compile_to_raw_code` (Impact: 135.9)
    * *Intent:* #if !MICROPY_EXPOSE_MP_COMPILE_TO_RAW_CODE
  * `compile_scope_inline_asm` (Impact: 102.8)
    * *Intent:* #if MICROPY_EMIT_INLINE_ASM // requires 3 passes: SCOPE, CODE_SIZE, EMIT
  * `compile_expr_stmt` (Impact: 76.7)
    * *Intent:* #endif
  * `compile_atom_brace_helper` (Impact: 75.0)
  * `compile_scope` (Impact: 72.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 248 instances
* *State Mutation (weighted view):* 778
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 781`, `structural_boundaries: 276`, `args: 167`, `func_start: 100`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 89`, `state_mutation: 282`, `dead_code: 23`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 40`
* *Architecture:* `api: 7`, `import: 16`
* *Defense:* `safety: 118`, `doc: 2`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` assert.h, asmbase.h, compile.h, emit.h, grammar.h, nativeglue.h, persistentcode.h, runtime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/objstr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2294.42 | **LOC:** 2471 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (94.188%), Tech Debt (17.9374%)
**Top Internal Functions/Classes:**
  * `mp_obj_str_format_helper` (Impact: 443.0)
    * *Intent:* #else // define to nothing to improve coverage #define terse_str_format_value_error() #endif
  * `str_modulo_format` (Impact: 173.4)
    * *Intent:* #if MICROPY_PY_BUILTINS_STR_OP_MODULO
  * `mp_obj_str_binary_op` (Impact: 63.6)
    * *Intent:* // Note: this function is used to check if an object is a str or bytes, which // works because both ...
  * `bytes_make_new` (Impact: 55.9)
  * `mp_str_print_quoted` (Impact: 55.6)
    * *Intent:* /******************************************************************************/ /* str */...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 243 instances
* *State Mutation (weighted view):* 751
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 607`, `structural_boundaries: 234`, `args: 165`, `func_start: 83`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 265`, `dead_code: 8`, `planned_debt: 7`, `unreferenced_by_name: 9`
* *Architecture:* `api: 30`, `import: 8`
* *Defense:* `safety: 89`, `doc: 2`, `immutability_locks: 147`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` assert.h, cstack.h, objlist.h, objstr.h, objtuple.h, runtime.h, unicode.h, string.h
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` inttypes.h, lfs1.h, lfs1_util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/mpz.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1849.8 | **LOC:** 1759 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.9054%), Tech Debt (53.8504%)
**Top Internal Functions/Classes:**
  * `mpz_as_str_inpl` (Impact: 54.5)
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
* *Structure:* `branch: 256`, `structural_boundaries: 98`, `args: 64`, `func_start: 50`
* *Risk/State:* `state_mutation: 387`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 16`
* *Architecture:* `api: 31`, `import: 3`
* *Defense:* `safety: 65`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, mpz.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/uart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1680.24 | **LOC:** 1387 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (84.7887%), Tech Debt (21.6945%)
**Top Internal Functions/Classes:**
  * `uart_init` (Impact: 457.2)
    * *Intent:* // assumes Init parameters have been set up correctly
  * `uart_deinit` (Impact: 87.5)
  * `uart_get_source_freq` (Impact: 78.6)
  * `uart_irq_handler` (Impact: 64.0)
    * *Intent:* // This IRQ handler is set up to handle RXNE, IDLE and ORE interrupts only. // Notes: // - ORE (over...
  * `uart_exists` (Impact: 60.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 221 instances
* *State Mutation (weighted view):* 680
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 482`, `structural_boundaries: 128`, `args: 350`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 238`, `unreferenced_by_name: 14`
* *Architecture:* `api: 19`, `import: 12`
* *Defense:* `safety: 5`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` irq.h, pendsv.h, mperrno.h, mphal.h, runtime.h, stream.h, interrupt_char.h, mpirq.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/emitnative.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1603.26 | **LOC:** 3123 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (52.4584%), Tech Debt (11.102%)
**Top Internal Functions/Classes:**
  * `emit_native_binary_op` (Impact: 146.3)
  * `emit_native_start_pass` (Impact: 140.6)
  * `emit_native_store_subscr` (Impact: 65.9)
  * `emit_native_load_subscr` (Impact: 48.2)
  * `emit_native_call_function` (Impact: 45.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 105 instances
* *State Mutation (weighted view):* 369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 492`, `structural_boundaries: 241`, `args: 168`, `func_start: 115`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 159`, `dead_code: 14`, `planned_debt: 13`, `fragile_debt: 2`
* *Architecture:* `api: 8`, `import: 7`
* *Defense:* `safety: 63`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` assert.h, emit.h, nativeglue.h, objfun.h, objstr.h, stdio.h, string.h
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `drivers/cc3100/inc/simplelink.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1467.92 | **LOC:** 949 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.0738%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 14`, `args: 10`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 1`, `api: 36`, `import: 12`
* *Defense:* `doc: 17`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.608
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` device.h, fs.h, netapp.h, netcfg.h, nonos.h, objInclusion.h, socket.h, spawn.h...
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

### `ports/stm32/usbhost/Class/AUDIO/Src/usbh_audio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1464.48 | **LOC:** 1995 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.2334%), Tech Debt (12.5432%)
**Top Internal Functions/Classes:**
  * `USBH_AUDIO_ClassRequest` (Impact: 45.5)
    * *Intent:* /** * @brief USBH_AUDIO_ClassRequest * The function is responsible for handling Standard requests * ...
  * `ParseCSDescriptors` (Impact: 34.6)
    * *Intent:* /** * @brief Parse AC interfaces * @param phost: Host handle * @retval USBH Status */
  * `USBH_AUDIO_CSRequest` (Impact: 29.9)
    * *Intent:* /** * @brief USBH_AUDIO_CSRequest * The function is responsible for handling AC Specific requests fo...
  * `USBH_AUDIO_InterfaceInit` (Impact: 29.6)
    * *Intent:* /** * @} */ /** @defgroup USBH_AUDIO_CORE_Private_Functions * @{ */ /** * @brief USBH_AUDIO_Interfac...
  * `USBH_AUDIO_SetFrequency` (Impact: 25.2)
    * *Intent:* /** * @brief USBH_AUDIO_SetFrequency * Set Audio sampling parameters * @param phost: Host handle * @...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 273 instances
* *State Mutation (weighted view):* 916
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 111`, `args: 72`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 370`, `unreferenced_by_name: 7`
* *Architecture:* `api: 14`, `import: 1`
* *Defense:* `doc: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` usbh_audio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/run-tests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1373.86 | **LOC:** 1366 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 45.7%
- **Risk Profile:** Cognitive Load (46.466%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 301.2)
  * `run_micropython` (Impact: 121.6)
  * `run_one_test` (Impact: 100.4)
  * `detect_test_platform` (Impact: 28.3)
    * *Intent:* # Run a script to detect various bits of information about the target test instance. output = run_fe...
  * `detect_target_wiring_script` (Impact: 26.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 6 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 213 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 16
* *Sec Tainted Injection (weighted view):* 6
* *State Mutation (weighted view):* 676
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 115`, `args: 21`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 6`, `state_mutation: 250`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 65`, `api: 20`, `concurrency: 6`, `import: 16`
* *Defense:* `safety: 22`, `doc: 2`, `test: 8`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` argparse, glob, json, multiprocessing, multiprocessing.pool, os, platform, pty...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extmod/modlwip.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1324.46 | **LOC:** 1961 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (62.9543%), Tech Debt (18.5699%)
**Top Internal Functions/Classes:**
  * `lwip_socket_ioctl` (Impact: 109.1)
  * `lwip_tcp_receive` (Impact: 63.0)
    * *Intent:* // Helper function for recv/recvfrom to handle TCP packets
  * `lwip_getaddrinfo` (Impact: 49.1)
    * *Intent:* // lwip.getaddrinfo
  * `lwip_socket_make_new` (Impact: 46.8)
    * *Intent:* // FIXME: Only supports two arguments at present
  * `lwip_raw_udp_send` (Impact: 37.0)
    * *Intent:* /*******************************************************************************/ // Functions for s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 152 instances
* *State Mutation (weighted view):* 497
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 225`, `args: 151`, `func_start: 50`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 193`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`, `api: 14`, `import: 20`
* *Defense:* `safety: 16`, `doc: 8`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` dns.h, igmp.h, init.h, tcp_priv.h, raw.h, sio.h, tcp.h, tcp_impl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/usbhost/Class/MTP/Src/usbh_mtp_ptp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1296.6 | **LOC:** 1770 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.4195%), Tech Debt (26.8941%)
**Top Internal Functions/Classes:**
  * `USBH_PTP_Process` (Impact: 89.8)
    * *Intent:* /** * @brief USBH_PTP_Process * The function handle the BOT protocol. * @param phost: Host handle * ...
  * `PTP_GetDevicePropValue` (Impact: 37.3)
    * *Intent:* /** * @brief PTP_GetDevicePropValue * Gets objectInfo and fills object_info structure. * @param phos...
  * `USBH_PTP_GetPartialObject` (Impact: 21.7)
    * *Intent:* /** * @brief USBH_PTP_GetPartialObject * Gets object partially * @param phost: Host handle * @param ...
  * `USBH_PTP_GetObjectHandles` (Impact: 17.4)
    * *Intent:* /** * @brief USBH_PTP_GetObjectHandles * Gets device info dataset and fills deviceinfo structure. * ...
  * `USBH_PTP_GetNumObjects` (Impact: 17.1)
    * *Intent:* /** * @brief USBH_PTP_GetNumObjects * Gets device info dataset and fills deviceinfo structure. * @pa...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 211 instances
* *State Mutation (weighted view):* 823
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 115`, `args: 45`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 401`, `unreferenced_by_name: 16`
* *Architecture:* `api: 20`, `import: 2`
* *Defense:* `doc: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` usbh_mtp.h, usbh_mtp_ptp.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/adc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1282.24 | **LOC:** 1126 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (48.1899%), Tech Debt (12.3211%)
**Top Internal Functions/Classes:**
  * `adc_wait_for_eoc_or_timeout` (Impact: 406.0)
  * `adc_config_channel` (Impact: 58.0)
  * `adc_read_timed_multi` (Impact: 54.6)
    * *Intent:* // read_timed_multi((adcx, adcy, ...), (bufx, bufy, ...), timer) // // Read analog values from multi...
  * `adcx_init_periph` (Impact: 49.6)
  * `adc_read_timed` (Impact: 49.6)
    * *Intent:* /// tim = pyb.Timer(6, freq=10) # create a timer running at 10Hz /// buf = bytearray(100) # creat a ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 117 instances
* *State Mutation (weighted view):* 375
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 57`, `args: 296`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 141`, `dead_code: 4`, `planned_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `safety: 10`, `doc: 56`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` adc.h, pin.h, binary.h, mphal.h, runtime.h, stdio.h, string.h, timer.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extmod/nimble/modbluetooth_nimble.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1276.48 | **LOC:** 2051 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (55.1047%), Tech Debt (89.9986%)
**Top Internal Functions/Classes:**
  * `l2cap_channel_event` (Impact: 38.9)
  * `characteristic_access_cb` (Impact: 33.9)
  * `mp_bluetooth_gatts_register_service` (Impact: 33.5)
  * `central_gap_event_cb` (Impact: 33.3)
  * `mp_bluetooth_l2cap_send` (Impact: 27.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 126 instances
* *State Mutation (weighted view):* 423
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 389`, `args: 161`, `func_start: 79`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 171`, `dead_code: 1`, `planned_debt: 17`, `unreferenced_by_name: 37`
* *Architecture:* `api: 51`, `import: 18`
* *Defense:* `safety: 46`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` modbluetooth.h, mpbthci.h, modbluetooth_nimble.h, ble_hs.h, util.h, ble.h, ble_hs_hci_priv.h, ble_hs_priv.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/cc3200/FreeRTOS/Source/queue.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1170.6 | **LOC:** 2567 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.8299%), Tech Debt (61.1719%)
**Top Internal Functions/Classes:**
  * `xQueueGenericSend` (Impact: 92.5)
    * *Intent:* #endif /* ( ( configUSE_COUNTING_SEMAPHORES == 1 ) && ( configSUPPORT_DYNAMIC_ALLOCATION == 1 ) ) */...
  * `xQueueGenericReceive` (Impact: 90.2)
    * *Intent:* /*-----------------------------------------------------------*/
  * `xQueueGenericSendFromISR` (Impact: 70.1)
    * *Intent:* /*-----------------------------------------------------------*/
  * `xQueueGiveFromISR` (Impact: 53.2)
    * *Intent:* /*-----------------------------------------------------------*/
  * `prvCopyDataToQueue` (Impact: 35.9)
    * *Intent:* #endif /* configUSE_TRACE_FACILITY */ /*-----------------------------------------------------------*...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 121 instances
* *State Mutation (weighted view):* 376
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 336`, `structural_boundaries: 119`, `args: 54`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `state_mutation: 134`, `planned_debt: 2`, `unreferenced_by_name: 31`
* *Architecture:* `api: 15`, `import: 6`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 92`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` FreeRTOS.h, croutine.h, queue.h, stdlib.h, string.h, task.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extmod/modbluetooth.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1168.8 | **LOC:** 1774 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.6621%), Tech Debt (30.8084%)
**Top Internal Functions/Classes:**
  * `bluetooth_ble_config` (Impact: 62.2)
  * `invoke_irq_handler_run` (Impact: 61.0)
    * *Intent:* #endif // !MICROPY_PY_BLUETOOTH_USE_SYNC_EVENTS // -------------------------------------------------...
  * `bluetooth_ble_invoke_irq` (Impact: 57.5)
  * `ringbuf_extract` (Impact: 41.0)
    * *Intent:* // Helpers #if !MICROPY_PY_BLUETOOTH_USE_SYNC_EVENTS
  * `bluetooth_uuid_make_new` (Impact: 36.3)
    * *Intent:* // ---------------------------------------------------------------------------- // UUID object // --...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 366
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 180`, `args: 218`, `func_start: 88`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 142`, `dead_code: 1`, `planned_debt: 4`, `unreferenced_by_name: 13`
* *Architecture:* `api: 43`, `import: 11`
* *Defense:* `safety: 87`, `immutability_locks: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` modbluetooth.h, binary.h, gc.h, misc.h, mperrno.h, mphal.h, obj.h, objarray.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/mboot/main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1163.46 | **LOC:** 1807 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (86.3836%), Tech Debt (64.4004%)
**Top Internal Functions/Classes:**
  * `stm32_main` (Impact: 76.5)
  * `i2c_slave_process_rx_end` (Impact: 75.5)
  * `dfu_handle_tx` (Impact: 38.8)
  * `pyb_usbdd_StrDescriptor` (Impact: 36.0)
  * `hw_read` (Impact: 33.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 147 instances
* *State Mutation (weighted view):* 482
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 179`, `args: 227`, `func_start: 71`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 188`, `planned_debt: 3`, `unreferenced_by_name: 26`
* *Architecture:* `api: 48`, `import: 17`
* *Defense:* `safety: 10`, `doc: 8`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` boardctrl.h, dfu.h, flash.h, i2cslave.h, irq.h, sha256.c, mboot.h, mpu.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/runtime.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1151.28 | **LOC:** 1787 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (94.4663%), Tech Debt (83.688%)
**Top Internal Functions/Classes:**
  * `mp_call_prepare_args_n_kw_var` (Impact: 86.0)
    * *Intent:* // This function only needs to be exposed externally when in stackless mode. #if !MICROPY_STACKLESS
  * `mp_unary_op` (Impact: 68.1)
  * `mp_convert_member_lookup` (Impact: 45.2)
    * *Intent:* #endif // MICROPY_BUILTIN_METHOD_CHECK_SELF_ARG // Given a member that was extracted from an instanc...
  * `mp_resume` (Impact: 39.8)
  * `mp_init` (Impact: 36.5)
    * *Intent:* #define TYPE_HAS_ITERNEXT(type) (type->flags & (MP_TYPE_FLAG_ITER_IS_ITERNEXT | MP_TYPE_FLAG_ITER_IS...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 140 instances
* *State Mutation (weighted view):* 446
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 382`, `structural_boundaries: 151`, `args: 99`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 166`, `dead_code: 7`, `planned_debt: 10`, `unreferenced_by_name: 31`
* *Architecture:* `api: 54`, `import: 20`
* *Defense:* `safety: 48`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` assert.h, vfs.h, builtin.h, compile.h, cstack.h, gc.h, objgenerator.h, objlist.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/timer.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1136.88 | **LOC:** 1775 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (37.3556%), Tech Debt (13.9499%)
**Top Internal Functions/Classes:**
  * `pyb_timer_channel` (Impact: 144.8)
    * *Intent:* /// /// Notes for Timer.ENC modes: /// /// - Requires 2 pins, so one or both pins will need to be co...
  * `timer_clock_enable` (Impact: 69.3)
  * `pyb_timer_init_helper` (Impact: 67.3)
    * *Intent:* /// measures ticks of `source_freq` divided by `div` clock ticks. /// `deadtime` is only available o...
  * `timer_get_source_freq` (Impact: 53.4)
    * *Intent:* // Get the frequency (in Hz) of the source clock for the given timer. // On STM32F405/407/415/417 th...
  * `pyb_timer_channel_callback` (Impact: 38.8)
    * *Intent:* /// \method callback(fun) /// Set the function to be called when the timer channel triggers. /// `fu...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 129 instances
* *State Mutation (weighted view):* 417
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 411`, `structural_boundaries: 109`, `args: 293`, `func_start: 35`, `class_start: 7`
* *Risk/State:* `state_mutation: 159`, `dead_code: 5`, `unreferenced_by_name: 8`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `safety: 12`, `doc: 208`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` irq.h, pin.h, gc.h, runtime.h, servo.h, mpirq.h, stdint.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/lexer.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1097.92 | **LOC:** 1162 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (97.264%), Tech Debt (12.0649%)
**Top Internal Functions/Classes:**
  * `parse_string_literal` (Impact: 307.0)
  * `mp_lexer_to_next` (Impact: 176.5)
  * `is_string_or_bytes` (Impact: 29.1)
  * `next_char` (Impact: 27.2)
  * `skip_whitespace` (Impact: 25.5)
    * *Intent:* // This function returns whether it has crossed a newline or not. // It therefore always return true...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 128 instances
* *State Mutation (weighted view):* 400
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 122`, `args: 40`, `func_start: 33`
* *Risk/State:* `state_mutation: 144`, `dead_code: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 25`, `immutability_locks: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` assert.h, lexer.h, reader.h, runtime.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/parse.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1068.6 | **LOC:** 1408 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.5036%), Tech Debt (11.8966%)
**Top Internal Functions/Classes:**
  * `mp_parse` (Impact: 170.1)
  * `fold_constants` (Impact: 118.3)
  * `push_result_rule` (Impact: 59.7)
    * *Intent:* #endif
  * `mp_parse_node_print` (Impact: 44.6)
    * *Intent:* #if MICROPY_DEBUG_PRINTERS
  * `fold_logical_constants` (Impact: 42.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 108 instances
* *State Mutation (weighted view):* 351
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 173`, `args: 58`, `func_start: 30`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 135`, `dead_code: 3`, `unreferenced_by_name: 5`
* *Architecture:* `api: 10`, `import: 27`
* *Defense:* `safety: 81`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` assert.h, builtin.h, grammar.h, lexer.h, objint.h, objstr.h, parse.h, parsenum.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/eth.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1048.4 | **LOC:** 1216 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (91.7043%), Tech Debt (13.7438%)
**Top Internal Functions/Classes:**
  * `eth_mac_init` (Impact: 185.2)
  * `ETH_IRQHandler` (Impact: 33.0)
  * `eth_init` (Impact: 32.3)
  * `eth_tx_buf_get` (Impact: 26.1)
    * *Intent:* #if !USE_PBUF_REF_FOR_TX
  * `eth_netif_output` (Impact: 25.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 176 instances
* *State Mutation (weighted view):* 563
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 79`, `args: 183`, `func_start: 22`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 211`, `unreferenced_by_name: 6`
* *Architecture:* `api: 16`, `import: 13`
* *Defense:* `safety: 13`, `doc: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` eth.h, eth_phy.h, modnetwork.h, dhcp.h, dns.h, etharp.h, mpu.h, ethernet.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extmod/btstack/modbluetooth_btstack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1038.74 | **LOC:** 1552 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.9171%), Tech Debt (87.0384%)
**Top Internal Functions/Classes:**
  * `btstack_packet_handler_generic` (Impact: 154.2)
    * *Intent:* #endif
  * `mp_bluetooth_gatts_register_service` (Impact: 54.5)
  * `mp_bluetooth_gatts_notify_indicate` (Impact: 35.2)
  * `mp_bluetooth_gatts_write` (Impact: 33.8)
  * `btstack_packet_handler_att_server` (Impact: 30.8)
    * *Intent:* #endif // This needs to be separate to btstack_packet_handler otherwise we get // dual-delivery of t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 208`, `args: 103`, `func_start: 63`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 109`, `planned_debt: 5`, `unreferenced_by_name: 32`
* *Architecture:* `api: 42`, `import: 6`
* *Defense:* `safety: 28`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` modbluetooth_btstack.h, modbluetooth.h, btstack.h, mperrno.h, mphal.h, runtime.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/objtype.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 966.52 | **LOC:** 1552 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.1092%), Tech Debt (17.0262%)
**Top Internal Functions/Classes:**
  * `mp_obj_new_type` (Impact: 71.1)
  * `mp_obj_class_lookup` (Impact: 64.3)
  * `mp_obj_instance_store_attr` (Impact: 56.1)
  * `type_attr` (Impact: 52.5)
  * `mp_obj_instance_load_attr` (Impact: 49.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 89 instances
* *State Mutation (weighted view):* 277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 170`, `args: 79`, `func_start: 35`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 99`, `dead_code: 2`, `planned_debt: 7`, `unreferenced_by_name: 3`
* *Architecture:* `api: 11`, `import: 6`
* *Defense:* `safety: 45`, `doc: 5`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` assert.h, objtype.h, runtime.h, stddef.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tools/ci.sh` -> Churn: **94.84%** | Cog Load: 29.9748% | Debt: 100.0%
- `ports/stm32/pyb_can.c` -> Churn: **50.42%** | Cog Load: 78.579% | Debt: 11.5494%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/littlefs/lfs2.c` -> **Daniël van de Giessen** (100.0% isolated ownership) | Magnitude: 5538.14
- `py/compile.c` -> **Alessandro Gatti** (100.0% isolated ownership) | Magnitude: 2665.92
- `py/emitnative.c` -> **Alessandro Gatti** (100.0% isolated ownership) | Magnitude: 1603.26
- `extmod/nimble/modbluetooth_nimble.c` -> **Alessandro Gatti** (100.0% isolated ownership) | Magnitude: 1276.48
- `ports/stm32/mboot/main.c` -> **Oliver Joos** (100.0% isolated ownership) | Magnitude: 1163.46

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `extmod/modre.c` -> **Severity: 0.015** (Bridge: 0.0001 * Flux: 99.9917%)
- `py/runtime.h` -> **Severity: 0.014** (Bridge: 0.0002 * Flux: 75.0692%)
- `py/dynruntime.h` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 78.3897%)
- `py/objstr.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 77.9365%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `py/obj.h` -> **Severity: 5236.6** (Blast Radius: 52.366 * Doc Risk: 100.0%)
- `py/misc.h` -> **Severity: 2732.3** (Blast Radius: 27.323 * Doc Risk: 100.0%)
- `py/runtime.h` -> **Severity: 1837.7** (Blast Radius: 18.377 * Doc Risk: 100.0%)
- `tests/internal_bench/bench.py` -> **Severity: 902.1** (Blast Radius: 9.021 * Doc Risk: 100.0%)
- `py/cstack.h` -> **Severity: 572.1** (Blast Radius: 5.721 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
