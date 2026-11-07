# ARCHITECTURAL_BRIEF: microzig
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ZigEmbeddedGroup/microzig.git` |
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
- **Scope:** 881 analyzed artifact(s), 102024 LOC.
- **Load-bearing artifact:** `core/src/microzig.zig` -- 338 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `drivers/framework.zig` -- pulls in 36 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `port/raspberrypi/rp2xxx/src/hal/pio/assembler/tokenizer.zig` at magnitude 1195.36 (structural weight, not risk).
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
| Total Artifacts | 1014 |
| Analyzed Artifacts (Scanned) | 881 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 133 |
| Total LOC | 102024 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 86.9% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6269 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3288 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5314 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 46 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 645 | 91067 | 73.2% |
| ASSEMBLY | 58 | 1812 | 6.6% |
| CPP | 56 | 3316 | 6.4% |
| JSON | 42 | 4452 | 4.8% |
| MARKDOWN | 40 | 0 | 4.5% |
| XML | 20 | 3 | 2.3% |
| YAML | 8 | 849 | 0.9% |
| C | 5 | 191 | 0.6% |
| PYTHON | 3 | 106 | 0.3% |
| SHELL | 1 | 3 | 0.1% |
| PLAINTEXT | 1 | 0 | 0.1% |
| JAVASCRIPT | 1 | 77 | 0.1% |
| CSS | 1 | 148 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 881 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 21%, Large Core Modules (2) 16%, Declarative / Non-Code 15%, Large Core Modules 13%, Large Core Modules (3) 12%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 837 | 95.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 41 | 4.7% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 133*

**Composition by Extension & Reason:**
- `.elf`: 42x Excluded (Unsupported Extension: '.elf')
- `.pio`: 27x Unsupported Format (.pio)
- `.ld`: 13x Excluded (Unsupported Extension: '.ld'), 1x Unsupported Format (.ld)
- `.smd`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Unsupported Extension: '.smd')
- `.svd`: 7x Unsupported Format (.svd)
- `.png`: 5x Excluded (Explicitly Denied Extension: '.png')
- `.zon`: 2x Zero-Density Threshold (LOC: 72, Signals: 0), 1x Zero-Density Threshold (LOC: 63, Signals: 0), 1x Zero-Density Threshold (LOC: 462, Signals: 0)
- `.bin`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.shtml`: 4x Excluded (Unsupported Extension: '.shtml')
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xcf`: 2x Excluded (Unsupported Extension: '.xcf')
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zig`: 1x Excluded (Machine-Generated Source Code Signature: 42879 LOC)
- `.pdf`: 1x Excluded (Explicitly Denied Extension: '.pdf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.2 | 6.6 | 3.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 84.0 | 23.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 26.6 | 14.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 69.6 | 0.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 14.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 97.1 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 29.2 | 3.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 55.3 | 73.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2920 | 278 | 10 | `port/raspberrypi/rp2xxx/src/hal/pio/assembler/encoder.zig` |
| cleanup | 760 | 65 | 0 | `tools/regz/src/gen.zig` |
| guards | 9114 | 431 | 24 | `tools/regz/src/gen.zig` |
| danger | 3430 | 357 | 11 | `port/espressif/esp/src/hal/radio/osi.zig` |
| concurrency | 184 | 35 | 0 | `modules/rtt/src/lock.zig` |
| connectivity | 7285 | 647 | 22 | `modules/riscv32-common/src/riscv32_common.zig` |
| io | 244 | 73 | 0 | `sim/aviron/build.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 3 | 0 | `scripts/usb/device_loopback.py` |
| time | 8 | 3 | 0 | `port/raspberrypi/rp2xxx/tools/rp2040-flash.zig` |
| serialization | 4 | 3 | 0 | `tools/regz/src/embassy.zig` |
| regex | 33 | 17 | 0 | `tools/regz/src/svd.zig` |
| events | 498 | 146 | 1 | `examples/wch/ch32v/src/sharp_niceview.zig` |
| tests | 1043 | 68 | 0 | `drivers/base/DateTime.zig` |
| docs | 7115 | 280 | 23 | `sim/aviron/src/lib/Cpu.zig` |
| debt | 535 | 160 | 2 | `sim/aviron/src/lib/Cpu.zig` |
| mutation | 23490 | 620 | 76 | `tools/regz/src/gen.zig` |
| dead_code | 398 | 219 | 1 | `modules/riscv32-common/src/riscv32_common.zig` |
| credential | 15 | 11 | 0 | `tools/sorcerer/build.zig.zon` |
| threat | 2 | 2 | 0 | `drivers/wireless/cyw43439/ioctl.zig` |
| ml_ai | 634 | 98 | 1 | `drivers/sensor/MLX90640.zig` |
| ui | 5 | 2 | 0 | `website/assets/style.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `sim/aviron/build.zig` (Hits: 15)
- `port/raspberrypi/rp2xxx/tools/rp2040-flash.zig` (Hits: 11)
- `sim/aviron/testsuite/instructions/in-stdio.S` (Hits: 11)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **microzig.zig** (`core/src/microzig.zig`) — 338 inbound connections
2. **ICM-20948.zig** (`drivers/sensor/ICM-20948.zig`) — 89 inbound connections
3. **framework.zig** (`drivers/framework.zig`) — 51 inbound connections
4. **cortex_m.zig** (`core/src/cpus/cortex_m.zig`) — 18 inbound connections
5. **drivers.zig** (`port/espressif/esp/src/hal/drivers.zig`) — 18 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **framework.zig** (`drivers/framework.zig`) — 36 outbound dependencies
2. **hal.zig** (`port/raspberrypi/rp2xxx/src/hal.zig`) — 31 outbound dependencies
3. **comparison_tests.zig** (`port/raspberrypi/rp2xxx/src/hal/pio/assembler/comparison_tests.zig`) — 31 outbound dependencies
4. **hal.zig** (`port/espressif/esp/src/hal.zig`) — 23 outbound dependencies
5. **README.md** (`examples/raspberrypi/rp2xxx/README.md`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `write_device` **(Many-Argument Workhorses)** (@ `tools/regz/src/gen.zig`) -> Impact: **509.3** | LOC: 1465
- `write_interrupt_list` **(Many-Argument Workhorses)** (@ `tools/regz/src/gen.zig`) -> Impact: **471.6** | LOC: 1472
- `write_struct` **(Many-Argument Workhorses)** (@ `tools/regz/src/gen.zig`) -> Impact: **455.2** | LOC: 1461
- `Tokenizer` **(Defensive Guards)** (@ `port/raspberrypi/rp2xxx/src/hal/pio/assembler/tokenizer.zig`) -> Impact: **369.6** | LOC: 1056
  * *Intent:* // the characters we're interested in are: // ';' -> line comment // '/' -> '/' -> line comment // '/' -> '*' -> block comment // '%' -> <whitespace> ...
- `write_fields` **(Many-Argument Workhorses)** (@ `tools/regz/src/gen.zig`) -> Impact: **225.7** | LOC: 1551
- `load_into_db` **(Many-Argument Workhorses)** (@ `tools/regz/src/embassy.zig`) -> Impact: **194.2** | LOC: 445
- `Encoder` **(Many-Argument Workhorses)** (@ `port/raspberrypi/rp2xxx/src/hal/pio/assembler/encoder.zig`) -> Impact: **148.2** | LOC: 540
- `MicroBuild` **(Many-Argument Workhorses)** (@ `build.zig`) -> Impact: **131.5** | LOC: 651
  * *Intent:* /// const optimize = b.standardOptimizeOption(.{}); /// /// const mz_dep = b.dependency("microzig", .{}); /// const mb = MicroBuild.init(b, mz_dep) or...
- `PioImpl` **(Many-Argument Workhorses)** (@ `port/raspberrypi/rp2xxx/src/hal/pio/common.zig`) -> Impact: **116.2** | LOC: 453
- `DeviceController` **(Many-Argument Workhorses)** (@ `core/src/core/usb.zig`) -> Impact: **112.9** | LOC: 388
  * *Intent:* /// USB device controller /// /// Responds to host requests and dispatches to the appropriate drivers. /// When this type is build (at comptime), it b...

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `port/raspberrypi/rp2xxx/src/hal` | 34 | 3473.7 | 12.78% | 8.22% |
| `port/espressif/esp/src/hal` | 19 | 2046.54 | 10.0% | 5.45% |
| `port/raspberrypi/rp2xxx/src/hal/pio/assembler` | 4 | 1830.08 | 15.61% | 4.3% |
| `port/stmicro/stm32/src/hals/STM32F103` | 17 | 1813.88 | 13.22% | 3.25% |
| `drivers/sensor` | 9 | 1634.76 | 11.16% | 6.46% |
| `port/wch/ch32v/src/hals` | 13 | 1525.1 | 10.59% | 18.13% |
| `port/stmicro/stm32/src/hals/common` | 13 | 1129.74 | 23.84% | 4.2% |
| `drivers/base` | 7 | 1096.9 | 10.47% | 1.15% |
| `drivers/display` | 7 | 1029.14 | 4.17% | 5.48% |
| `sim/aviron/src/lib` | 5 | 1002.52 | 18.8% | 22.75% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `modules/freertos/src/picosdk_stubs.c` -> **100.0%** Exposure
- `modules/foundation-libc/src/modules/string.zig` -> **99.999%** Exposure
- `port/gigadevice/gd32/src/hals/GD32VF103.zig` -> **99.999%** Exposure
- `port/stmicro/stm32/src/hals/STM32F429.zig` -> **99.9673%** Exposure
- `port/nxp/mcx/src/boards/frdm_mcxn947.zig` -> **99.8104%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `drivers/sensor/MLX90640.zig` -> **100.0%** Exposure
- `port/stmicro/stm32/src/hals/common/dma_common.zig` -> **100.0%** Exposure
- `port/stmicro/stm32/src/hals/common/spi_v2.zig` -> **100.0%** Exposure
- `port/stmicro/stm32/src/hals/common/systick.zig` -> **100.0%** Exposure
- `port/stmicro/stm32/src/hals/common/timer_v1.zig` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `modules/riscv32-common/src/riscv32_common.zig` -> **16** Orphaned Functions | **0** Duplicates
- `port/raspberrypi/rp2xxx/src/cpus/hazard3.zig` -> **11** Orphaned Functions | **0** Duplicates
- `port/stmicro/stm32/src/hals/STM32F407.zig` -> **10** Orphaned Functions | **0** Duplicates
- `port/espressif/esp/src/cpus/esp_riscv.zig` -> **9** Orphaned Functions | **0** Duplicates
- `core/src/cpus/avr5.zig` -> **8** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `53` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1593` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `port/raspberrypi/rp2xxx/src/hal/pio/assembler/tokenizer.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.923)
- **Top Global Matches:** file_cluster_4: 6.923, file_cluster_12: 10.84, file_cluster_15: 11.136
- **Magnitude:** 1195.36 | **LOC:** 2286 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 0.848; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (60.1%), Mutation Surface (formerly State Flux) (55.9%), Complexity Load (formerly Cognitive Load) (34.7%), Guard Balance (formerly Safety Score) (32.7%)
- **Documentation Coverage:** 96.7391% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Tokenizer` **(Defensive Guards)** (Impact: 369.6)
    * *Intent:* // the characters we're interested in are: // ';' -> line comment // '/' -> '/' -> line comment // '...
  * `get_mov` **(Defensive Guards)** (Impact: 50.1)
  * `get_wait` **(Defensive Guards)** (Impact: 46.1)
  * `get_irq` **(Defensive Guards)** (Impact: 45.6)
  * `peek_arg_impl` **(Many-Argument Workhorses)** (Impact: 45.4)
    * *Intent:* /// gets next arg without consuming the stream
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 41 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 161`, `args: 84`, `func_start: 82`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 47`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `api: 37`, `import: 5`
* *Defense:* `safety: 418`, `doc: 3`, `test: 54`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.848
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.00704
  * `Imports (Out-Degree: 4):` chip.zig, assembler.zig, Expression.zig, bounded-array, std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `drivers/sensor/MLX90640.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 11.253)
- **Top Global Matches:** file_cluster_7: 11.253, file_cluster_12: 12.121, file_cluster_14: 12.457
- **Magnitude:** 782.34 | **LOC:** 943 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 2.81; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.0%), Complexity Load (formerly Cognitive Load) (55.7%), Connectivity (formerly Api Exposure) (39.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `temperature` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `extract_deviating_pixels` **(Defensive Guards)** (Impact: 28.1)
  * `extract_alpha` **(Type Conversions)** (Impact: 23.5)
  * `extract_kta_pixel` **(Type Conversions)** (Impact: 23.2)
  * `extract_ky_pixel` **(Type Conversions)** (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 152 instances
* *State Mutation (weighted view):* 510
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 72`, `args: 29`, `func_start: 29`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 94`, `state_mutation: 206`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 2`
* *Defense:* `safety: 62`, `doc: 10`, `test: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.81
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.142118
  * `Imports (Out-Degree: 1):` framework.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sim/aviron/src/lib/Cpu.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.406)
- **Top Global Matches:** file_cluster_12: 7.406, file_cluster_7: 9.487, file_cluster_5: 9.977
- **Magnitude:** 728.84 | **LOC:** 1825 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 0.879; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.6%), Guard Balance (formerly Safety Score) (52.4%)
- **Documentation Coverage:** 24.0175% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 47.1)
  * `format` **(Type Conversions)** (Impact: 30.0)
  * `read_wide_reg` **(Defensive Guards)** (Impact: 22.8)
  * `generic_sub_cp` **(Many-Argument Workhorses)** (Impact: 22.4)
  * `format_instruction` **(Defensive Guards)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 58`, `args: 132`, `func_start: 132`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 33`, `high_risk_execution: 6`, `state_mutation: 109`, `planned_debt: 10`
* *Architecture:* `api: 98`, `import: 4`
* *Defense:* `safety: 83`, `doc: 416`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.879
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.003139
  * `Imports (Out-Degree: 3):` bus.zig, decoder.zig, std, hexdump.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `port/espressif/esp/src/hal/rtos.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.98)
- **Top Global Matches:** file_cluster_12: 5.98, file_cluster_7: 8.879, file_cluster_15: 9.001
- **Magnitude:** 692.6 | **LOC:** 1460 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **4**; blast radius 0.9; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (79.4%), Guard Balance (formerly Safety Score) (56.6%)
- **Documentation Coverage:** 92.1053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `yield_inner` **(Compute Cores)** (Impact: 20.4)
  * `spawn` **(Many-Argument Workhorses)** (Impact: 17.1)
  * `interrupt_handler_c` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* // Can't be preempted by a higher priority interrupt so already in a "critical // section".
  * `put` **(Many-Argument Workhorses)** (Impact: 12.5)
  * `get` **(Many-Argument Workhorses)** (Impact: 12.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 60 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 117`, `args: 81`, `func_start: 81`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 70`, `planned_debt: 8`
* *Architecture:* `api: 92`, `import: 4`
* *Defense:* `safety: 64`, `doc: 23`, `test: 2`, `sync_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.9
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.008564
  * `Imports (Out-Degree: 5):` microzig, std, system.zig, systimer.zig
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `port/espressif/esp/src/hal/radio/osi.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.733)
- **Top Global Matches:** file_cluster_7: 7.733, file_cluster_12: 7.933, file_cluster_5: 8.815
- **Magnitude:** 596.72 | **LOC:** 1273 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 0.578; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (85.8%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.5%)
- **Documentation Coverage:** 98.8593% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__assert_func` **(Defensive Guards)** (Impact: 12.2)
  * `set_isr` **(Type Conversions)** (Impact: 10.9)
  * `limit` **(Compute Cores)** (Impact: 10.2)
  * `task_create_common` **(Many-Argument Workhorses)** (Impact: 9.9)
  * `queue_send` **(Type Conversions)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 30
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 99`, `args: 137`, `func_start: 135`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 73`, `high_risk_execution: 33`, `state_mutation: 23`, `planned_debt: 3`
* *Architecture:* `api: 152`, `import: 10`
* *Defense:* `safety: 33`, `doc: 1`, `test: 3`, `sync_locks: 10`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.578
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.002542
  * `Imports (Out-Degree: 10):` radio.zig, rng.zig, rtos.zig, time.zig, builtin, esp-wifi-driver, microzig, std...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `drivers/base/DateTime.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.015)
- **Top Global Matches:** file_cluster_4: 9.015, file_cluster_6: 9.041, file_cluster_12: 14.494
- **Magnitude:** 517.4 | **LOC:** 944 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 2.81; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (55.4%), Guard Balance (formerly Safety Score) (50.6%)
- **Documentation Coverage:** 6.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_string` **(Many-Argument Workhorses)** (Impact: 103.4)
    * *Intent:* /// %p AM or PM indicator /// /// %M Minute as a zero-padded decimal number. 00, 01, ..., 59 /// %-M...
  * `from_timestamp` **(Type Conversions)** (Impact: 25.5)
    * *Intent:* /// Create a DateTime from a timestamp in milliseconds since the epoch /// 1970-01-01 00:00:00 UTC
  * `from_string` **(Compute Cores)** (Impact: 17.8)
    * *Intent:* /// Convert a string in the form "±00:00" or "±0000" to a Timezone /// This allows for leading chara...
  * `to_string` **(Many-Argument Workhorses)** (Impact: 17.8)
    * *Intent:* /// Convert a Timezone to a string like "+00:00" or "-00:00" /// /// Parameters: /// /// * `out_stri...
  * `timestamp` **(Type Conversions)** (Impact: 17.6)
    * *Intent:* /// Convert a DateTime to a timestamp in milliseconds since the epoch /// 1970-01-01 00:00:00 /// //...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 97`, `args: 16`, `func_start: 16`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 90`, `planned_debt: 1`
* *Architecture:* `api: 27`, `import: 2`
* *Defense:* `safety: 97`, `doc: 76`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.81
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.142118
  * `Imports (Out-Degree: 1):` framework.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `port/stmicro/stm32/src/hals/STM32F103/adc.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.548)
- **Top Global Matches:** file_cluster_12: 6.548, file_cluster_15: 8.508, file_cluster_7: 9.748
- **Magnitude:** 495.86 | **LOC:** 1122 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 0.77; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.5%), Mutation Surface (formerly State Flux) (69.2%), Guard Balance (formerly Safety Score) (49.9%)
- **Documentation Coverage:** 52.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_regular_simultaneous` **(Compute Cores)** (Impact: 23.3)
  * `check_injected_simultaneous` **(Compute Cores)** (Impact: 23.3)
  * `set_regular_seq` **(Defensive Guards)** (Impact: 17.4)
  * `set_regular_discontinuous` **(Defensive Guards)** (Impact: 17.1)
  * `set_injected_discontinuous` **(Defensive Guards)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 64`, `args: 46`, `func_start: 46`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 32`
* *Architecture:* `api: 72`, `import: 4`
* *Defense:* `safety: 55`, `doc: 78`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.77
  * `Choke Point (Betweenness):` 0.000111 | `Ripple Effect (Closeness):` 0.00339
  * `Imports (Out-Degree: 3):` enums.zig, microzig, std, time.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `port/raspberrypi/rp2xxx/src/hal/pio/assembler/encoder.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.509)
- **Top Global Matches:** file_cluster_6: 8.509, file_cluster_4: 9.466, file_cluster_12: 15.338
- **Magnitude:** 442.14 | **LOC:** 1203 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 1.101; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (58.4%), Guard Balance (formerly Safety Score) (30.0%), Mutation Surface (formerly State Flux) (29.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Encoder` **(Many-Argument Workhorses)** (Impact: 148.2)
  * `encode_instruction` **(Many-Argument Workhorses)** (Impact: 47.4)
  * `encode_instruction_body` **(Defensive Guards)** (Impact: 34.7)
  * `calc_delay_side_set` **(Defensive Guards)** (Impact: 27.1)
  * `evaluate_impl` **(Many-Argument Workhorses)** (Impact: 22.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 55`, `args: 22`, `func_start: 22`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 15`
* *Architecture:* `api: 22`, `import: 6`
* *Defense:* `safety: 253`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.101
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.009387
  * `Imports (Out-Degree: 4):` chip.zig, assembler.zig, Expression.zig, bounded-array, std, tokenizer.zig
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `modules/riscv32-common/src/riscv32_common.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.875)
- **Top Global Matches:** file_cluster_12: 7.875, file_cluster_5: 8.783, file_cluster_7: 9.795
- **Magnitude:** 436.98 | **LOC:** 590 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.513; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (91.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.1%)
- **Documentation Coverage:** 95.1807% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Csr` **(Type Conversions)** (Impact: 34.9)
  * `modify` **(Generic / Templated Code)** (Impact: 6.3)
  * `get_bits` **(Type Conversions)** (Impact: 6.3)
  * `write_raw` **(State Mutators)** (Impact: 4.9)
  * `set_raw` **(State Mutators)** (Impact: 4.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 19`, `args: 30`, `func_start: 30`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 14`, `planned_debt: 2`, `unreferenced_by_name: 16`
* *Architecture:* `api: 325`, `import: 2`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00352
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `port/raspberrypi/rp2xxx/src/hal/pio/common.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.719)
- **Top Global Matches:** file_cluster_12: 7.719, file_cluster_5: 8.589, file_cluster_7: 9.657
- **Magnitude:** 433.58 | **LOC:** 648 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **7**; blast radius 1.161; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (96.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.2%), Mutation Surface (formerly State Flux) (28.5%)
- **Documentation Coverage:** 93.4066% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PioImpl` **(Many-Argument Workhorses)** (Impact: 116.2)
  * `sm_set_pin_mappings` **(Defensive Guards)** (Impact: 34.5)
  * `sm_load_and_start_program` **(Many-Argument Workhorses)** (Impact: 31.4)
  * `find_offset_for_program` **(Defensive Guards)** (Impact: 14.5)
  * `add_program_at_offset_unlocked` **(Type Conversions)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 42`, `args: 48`, `func_start: 48`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 1`, `state_mutation: 13`, `dead_code: 1`, `planned_debt: 6`
* *Architecture:* `api: 64`, `import: 7`
* *Defense:* `safety: 35`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.161
  * `Choke Point (Betweenness):` 0.000274 | `Ripple Effect (Closeness):` 0.007345
  * `Imports (Out-Degree: 6):` chip.zig, gpio.zig, hw.zig, assembler.zig, encoder.zig, microzig, std
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `core/src/allocator.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.364)
- **Top Global Matches:** file_cluster_12: 9.364, file_cluster_7: 9.851, file_cluster_5: 11.234
- **Magnitude:** 423.5 | **LOC:** 1626 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 10.089; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (46.1%), Guard Balance (formerly Safety Score) (43.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dbg_integrity_check` **(Compute Cores)** (Impact: 32.1)
    * *Intent:* /// Check the integrity of the allocator memory pool. /// This function is intended for use in a deb...
  * `do_alloc` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* /// Allocate memory /// /// Parameters: /// - `len` : The length of the memory to allocate /// - `al...
  * `do_resize` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* /// Resize memory. This function attempts to resize the memory in place. /// /// Parameters: /// - `...
  * `combine_and_free` **(Many-Argument Workhorses)** (Impact: 12.5)
    * *Intent:* /// Combine this chunk with any neighboring free chunks and /// add the result to the appropriate fr...
  * `dbg_log_free_chains` **(Defensive Guards)** (Impact: 10.1)
    * *Intent:* //------------------------------------------------------------------------------ // Debugging Functi...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 65 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 189`, `args: 21`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 65`, `high_risk_execution: 2`, `state_mutation: 88`
* *Architecture:* `api: 19`, `import: 2`
* *Defense:* `safety: 239`, `doc: 135`, `test: 42`, `sync_locks: 13`, `cleanup: 84`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.089
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.200679
  * `Imports (Out-Degree: 2):` microzig.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `drivers/wireless/cyw43439/wifi.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.086)
- **Top Global Matches:** file_cluster_12: 6.086, file_cluster_15: 8.689, file_cluster_7: 9.122
- **Magnitude:** 396.02 | **LOC:** 1029 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 1.003; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.2%), Connectivity (formerly Api Exposure) (69.3%), Guard Balance (formerly Safety Score) (50.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.8%)
- **Documentation Coverage:** 87.8788% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `join` **(Many-Argument Workhorses)** (Impact: 27.9)
  * `handle_event` **(Many-Argument Workhorses)** (Impact: 20.7)
  * `response_poll` **(Defensive Guards)** (Impact: 17.6)
  * `log_read` **(Defensive Guards)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 82`, `args: 41`, `func_start: 41`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 52`, `dead_code: 1`
* *Architecture:* `api: 37`, `import: 4`
* *Defense:* `safety: 70`, `doc: 32`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.003
  * `Choke Point (Betweenness):` 0.001162 | `Ripple Effect (Closeness):` 0.111553
  * `Imports (Out-Degree: 4):` bus.zig, ioctl.zig, nvram.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `build.zig` (ZIG | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.837)
- **Top Global Matches:** file_cluster_4: 6.837, file_cluster_6: 8.635, file_cluster_12: 13.416
- **Magnitude:** 393.68 | **LOC:** 857 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.406; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.5%), Connectivity (formerly Api Exposure) (59.4%), Mutation Surface (formerly State Flux) (53.0%), Guard Balance (formerly Safety Score) (43.6%)
- **Documentation Coverage:** 25.4859% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MicroBuild` **(Many-Argument Workhorses)** (Impact: 131.5)
    * *Intent:* /// const optimize = b.standardOptimizeOption(.{}); /// /// const mz_dep = b.dependency("microzig", ...
  * `add_firmware` **(Many-Argument Workhorses)** (Impact: 74.7)
    * *Intent:* /// Creates a new firmware for a given target.
  * `get_default_cpu` **(Compute Cores)** (Impact: 19.6)
  * `init` **(Defensive Guards)** (Impact: 15.5)
    * *Intent:* /// Initializes the microzig build system. Returns null when there are ports /// that haven't been f...
  * `get_emitted_bin` **(Defensive Guards)** (Impact: 11.8)
    * *Intent:* /// Returns the emitted binary for this firmware. The file is either in the preferred file format fo...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 39`, `args: 18`, `func_start: 18`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 12`, `state_mutation: 15`, `planned_debt: 1`
* *Architecture:* `api: 33`, `import: 9`
* *Defense:* `safety: 63`, `doc: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.406
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` build-internals, root, std, dfu, esp-image, generate_linker_script.zig, regz, uf2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/core/usb.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.187)
- **Top Global Matches:** file_cluster_5: 8.187, file_cluster_12: 8.856, file_cluster_4: 10.645
- **Magnitude:** 387.5 | **LOC:** 656 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 4.624; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.2%), Guard Balance (formerly Safety Score) (58.2%)
- **Documentation Coverage:** 40.2778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DeviceController` **(Many-Argument Workhorses)** (Impact: 112.9)
    * *Intent:* /// USB device controller /// /// Responds to host requests and dispatches to the appropriate driver...
  * `process_set_config` **(Many-Argument Workhorses)** (Impact: 24.1)
  * `on_buffer` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* /// Called by the device implementation when a packet has been sent or received.
  * `process_device_setup` **(Many-Argument Workhorses)** (Impact: 15.8)
    * *Intent:* // Utility functions
  * `on_setup_req` **(Many-Argument Workhorses)** (Impact: 12.9)
    * *Intent:* /// Called by the device implementation when a setup request has been received.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 54`, `args: 33`, `func_start: 27`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 28`, `planned_debt: 2`
* *Architecture:* `api: 39`, `import: 6`
* *Defense:* `safety: 16`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.624
  * `Choke Point (Betweenness):` 0.002939 | `Ripple Effect (Closeness):` 0.138549
  * `Imports (Out-Degree: 6):` std, descriptor.zig, CDC.zig, EchoExample.zig, hid.zig, types.zig
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `core/src/cpus/cortex_m.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.591)
- **Top Global Matches:** file_cluster_12: 6.591, file_cluster_15: 7.273, file_cluster_11: 8.5
- **Magnitude:** 386.02 | **LOC:** 1222 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 22.2%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **13**; blast radius 3.404; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.0%), Guard Balance (formerly Safety Score) (54.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.0%)
- **Documentation Coverage:** 83.4951% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_pending` **(Compute Cores)** (Impact: 13.0)
  * `set_pending` **(I/O & Config Routines)** (Impact: 12.9)
  * `clear_pending` **(Type Conversions)** (Impact: 12.9)
  * `cmpxchg` **(Many-Argument Workhorses)** (Impact: 11.7)
    * *Intent:* /// Atomic compare and swap
  * `is_enabled` **(Compute Cores)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 68`, `args: 56`, `func_start: 54`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 7`, `state_mutation: 23`
* *Architecture:* `api: 83`, `concurrency: 4`, `import: 13`
* *Defense:* `safety: 12`, `doc: 87`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.404
  * `Choke Point (Betweenness):` 0.000862 | `Ripple Effect (Closeness):` 0.024999
  * `Imports (Out-Degree: 11):` builtin, m0.zig, m0plus.zig, m3.zig, m33.zig, m4.zig, m55.zig, m7.zig...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `port/stmicro/stm32/src/hals/STM32F407.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.457)
- **Top Global Matches:** file_cluster_4: 9.457, file_cluster_12: 9.612, file_cluster_5: 9.931
- **Magnitude:** 348.24 | **LOC:** 624 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.719; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (93.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.2%), Mutation Surface (formerly State Flux) (22.1%)
- **Documentation Coverage:** 89.8305% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Uart` **(Many-Argument Workhorses)** (Impact: 71.2)
  * `I2CController` **(Many-Argument Workhorses)** (Impact: 69.0)
  * `init` **(Compute Cores)** (Impact: 20.6)
  * `is_valid_pin` **(Many-Argument Workhorses)** (Impact: 13.2)
    * *Intent:* /// Checks if a pin is valid for a given uart index and direction
  * `is_valid_pin` **(Compute Cores)** (Impact: 12.9)
    * *Intent:* /// Checks if a pin is valid for a given i2c index and line
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 36`, `args: 31`, `func_start: 31`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 2`, `state_mutation: 4`, `planned_debt: 9`, `unreferenced_by_name: 10`
* *Architecture:* `api: 40`, `import: 2`
* *Defense:* `safety: 14`, `doc: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002393
  * `Imports (Out-Degree: 1):` microzig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `port/raspberrypi/rp2xxx/src/hal/pins.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.465)
- **Top Global Matches:** file_cluster_4: 6.465, file_cluster_12: 9.283, file_cluster_15: 10.354
- **Magnitude:** 342.46 | **LOC:** 973 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.439; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.4%), Guard Balance (formerly Safety Score) (52.6%), Mutation Surface (formerly State Flux) (42.7%)
- **Documentation Coverage:** 88.7097% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `apply` **(Defensive Guards)** (Impact: 79.8)
  * `get_direction` **(Compute Cores)** (Impact: 30.9)
  * `pins` **(Defensive Guards)** (Impact: 18.6)
    * *Intent:* /// Populate and return the PinsType struct /// /// Can be called at comptime or runtime
  * `PinsType` **(Defensive Guards)** (Impact: 16.1)
  * `is_pwm` **(I/O & Config Routines)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 39`, `args: 28`, `func_start: 28`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 16`, `planned_debt: 2`
* *Architecture:* `api: 31`, `import: 7`
* *Defense:* `safety: 19`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.439
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00346
  * `Imports (Out-Degree: 6):` adc.zig, compatibility.zig, gpio.zig, microzig, pwm.zig, resets.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `core/src/utilities.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.666)
- **Top Global Matches:** file_cluster_4: 7.666, file_cluster_12: 9.847, file_cluster_5: 11.13
- **Magnitude:** 329.32 | **LOC:** 664 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 10.089; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (60.7%), Guard Balance (formerly Safety Score) (48.4%)
- **Documentation Coverage:** 67.2131% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SliceVector` **(Compute Cores)** (Impact: 37.5)
    * *Intent:* /// A helper class that allows operating on a slice of slices /// with similar operations to those o...
  * `CircularBuffer` **(Many-Argument Workhorses)** (Impact: 34.2)
    * *Intent:* /// A naive circular buffer implementation. At time of writing, it's intended /// to fill in where t...
  * `next_chunk` **(Defensive Guards)** (Impact: 11.7)
    * *Intent:* /// Returns the next available chunk of data. /// /// If `max_length` is given, that chunk never exc...
  * `init` **(Defensive Guards)** (Impact: 9.7)
    * *Intent:* /// Initializes a new vector with the given slice of slices. /// Optimizes the `slices` array by rem...
  * `write_assume_capacity` **(Defensive Guards)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 66`, `args: 27`, `func_start: 27`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 2`, `state_mutation: 32`
* *Architecture:* `api: 31`, `import: 2`
* *Defense:* `safety: 54`, `doc: 32`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.089
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.200679
  * `Imports (Out-Degree: 2):` microzig.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `port/stmicro/stm32/src/hals/common/timer_v1.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.926)
- **Top Global Matches:** file_cluster_15: 6.926, file_cluster_2: 8.581, file_cluster_16: 8.619
- **Magnitude:** 316.58 | **LOC:** 598 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.52; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (82.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.1%)
- **Documentation Coverage:** 85.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `configure_output` **(Many-Argument Workhorses)** (Impact: 23.4)
  * `configure_input` **(Many-Argument Workhorses)** (Impact: 10.9)
  * `configure_channel` **(State Mutators)** (Impact: 6.8)
    * *Intent:* ///This function configures the output channel for PWM mode.
  * `set_channel_interrupt` **(Type Conversions)** (Impact: 6.4)
  * `set_channel_dma_request` **(Type Conversions)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 13`, `args: 55`, `func_start: 55`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`, `planned_debt: 2`
* *Architecture:* `api: 74`, `import: 3`
* *Defense:* `safety: 4`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.52
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.005443
  * `Imports (Out-Degree: 2):` enums.zig, microzig, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `port/espressif/esp/src/hal/i2c.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.719)
- **Top Global Matches:** file_cluster_12: 6.719, file_cluster_7: 8.914, file_cluster_5: 9.965
- **Magnitude:** 312.86 | **LOC:** 661 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 0.777; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (67.0%), Connectivity (formerly Api Exposure) (62.8%), Guard Balance (formerly Safety Score) (49.9%)
- **Documentation Coverage:** 46.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup_read` **(Many-Argument Workhorses)** (Impact: 43.0)
  * `writev_operation_blocking` **(Many-Argument Workhorses)** (Impact: 26.5)
  * `setup_write` **(Many-Argument Workhorses)** (Impact: 23.2)
  * `write_operation_blocking` **(Many-Argument Workhorses)** (Impact: 20.3)
  * `set_filter` **(Defensive Guards)** (Impact: 18.4)
    * *Intent:* /// Set the filter threshold in clock cycles
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 40`, `args: 30`, `func_start: 30`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 16`, `planned_debt: 4`
* *Architecture:* `api: 16`, `import: 4`
* *Defense:* `safety: 42`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.777
  * `Choke Point (Betweenness):` 0.000179 | `Ripple Effect (Closeness):` 0.004708
  * `Imports (Out-Degree: 4):` gpio.zig, microzig, std, time.zig
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `modules/network/src/root.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.58)
- **Top Global Matches:** file_cluster_12: 6.58, file_cluster_7: 8.101, file_cluster_5: 8.841
- **Magnitude:** 307.9 | **LOC:** 620 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.476; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.8%), Connectivity (formerly Api Exposure) (81.4%), Guard Balance (formerly Safety Score) (55.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.2%)
- **Documentation Coverage:** 85.9649% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `c_on_recv` **(Defensive Guards)** (Impact: 24.2)
  * `poll` **(Defensive Guards)** (Impact: 17.9)
    * *Intent:* /// Poll underlying link layer for data packet.
  * `init` **(Defensive Guards)** (Impact: 13.8)
  * `c_netif_linkoutput` **(Defensive Guards)** (Impact: 13.6)
    * *Intent:* /// Called by lwip when there is a packet to send. /// pbuf chain total_len is <= netif.mtu + ethern...
  * `connect` **(Defensive Guards)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 62`, `args: 41`, `func_start: 35`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 2`, `state_mutation: 32`
* *Architecture:* `api: 32`, `import: 13`
* *Defense:* `safety: 48`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.476
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.00113
  * `Imports (Out-Degree: 3):` config, link, dhcp.h, etharp.h, ethip6.h, init.h, netif.h, tcp.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `port/raspberrypi/rp2xxx/src/hal/gpio.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.628)
- **Top Global Matches:** file_cluster_7: 7.628, file_cluster_12: 7.953, file_cluster_5: 9.709
- **Magnitude:** 291.62 | **LOC:** 585 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **5**; blast radius 1.104; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (67.8%), Guard Balance (formerly Safety Score) (66.3%)
- **Documentation Coverage:** 82.0513% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read` **(Compute Cores)** (Impact: 15.3)
  * `set_direction` **(Compute Cores)** (Impact: 13.3)
  * `put` **(Compute Cores)** (Impact: 13.3)
    * *Intent:* /// Drive a single GPIO high/low
  * `set_irq_enabled` **(Many-Argument Workhorses)** (Impact: 11.2)
    * *Intent:* /// Set or clear IRQ event enable for the input events /// if enable=true irqs will be enabled for t...
  * `next` **(Type Conversions)** (Impact: 9.7)
    * *Intent:* /// return the next IRQ event that triggered. /// Attempts to inline to minimize execution overhead ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 17`, `args: 40`, `func_start: 40`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 2`, `state_mutation: 17`
* *Architecture:* `api: 54`, `import: 5`
* *Defense:* `safety: 10`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.104
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.013293
  * `Imports (Out-Degree: 4):` compatibility.zig, hw.zig, microzig, resets.zig, std
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `modules/rtt/src/rtt.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.021)
- **Top Global Matches:** file_cluster_12: 7.021, file_cluster_5: 8.877, file_cluster_4: 9.345
- **Magnitude:** 289.94 | **LOC:** 588 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.67; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (58.8%), Guard Balance (formerly Safety Score) (56.4%)
- **Documentation Coverage:** 31.3725% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Up` **(Many-Argument Workhorses)** (Impact: 38.1)
    * *Intent:* /// Represents a target -> host communication channel. /// /// Implements a ring buffer of size - 1 ...
  * `Down` **(Many-Argument Workhorses)** (Impact: 21.3)
    * *Intent:* /// Represents a host -> target communication channel. /// /// Implements a ring buffer of size - 1 ...
  * `RTT` **(Defensive Guards)** (Impact: 14.7)
    * *Intent:* /// Creates an RTT namespace given the compile time configuration with functions for writing/reading...
  * `write_available` **(Many-Argument Workhorses)** (Impact: 10.8)
    * *Intent:* /// Writes up to available space left in buffer for reading by probe, returning number of bytes /// ...
  * `ControlBlock` **(Many-Argument Workhorses)** (Impact: 10.7)
    * *Intent:* /// Creates a control block struct for the given channel configs. Buffer storage is also contained w...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 46`, `args: 31`, `func_start: 31`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 31`, `planned_debt: 2`
* *Architecture:* `api: 26`, `import: 3`
* *Defense:* `safety: 8`, `doc: 79`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.00013 | `Ripple Effect (Closeness):` 0.017921
  * `Imports (Out-Degree: 2):` lock.zig, memory_barrier.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `drivers/display/ssd1306.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.962)
- **Top Global Matches:** file_cluster_12: 7.962, file_cluster_15: 8.648, file_cluster_16: 9.776
- **Magnitude:** 289.36 | **LOC:** 973 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 2.896; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (65.7%), Guard Balance (formerly Safety Score) (25.8%), Debt Markers (formerly Tech Debt) (13.3%), Mutation Surface (formerly State Flux) (13.0%)
- **Documentation Coverage:** 74.026% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SSD1306_Generic` **(Defensive Guards)** (Impact: 87.1)
  * `init_with_mode` **(Defensive Guards)** (Impact: 8.5)
  * `clear_screen` **(Defensive Guards)** (Impact: 7.9)
  * `set_dc_pin` **(Defensive Guards)** (Impact: 7.6)
    * *Intent:* /// If present, sets the D/C pin to the required mode. /// NOTE: This function must be called *befor...
  * `execute_command` **(Defensive Guards)** (Impact: 6.9)
    * *Intent:* /// Sends command data to the SSD1306 controller.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 74`, `args: 41`, `func_start: 41`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 8`, `planned_debt: 8`
* *Architecture:* `api: 52`, `import: 3`
* *Defense:* `safety: 165`, `doc: 42`, `test: 37`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.896
  * `Choke Point (Betweenness):` 0.000291 | `Ripple Effect (Closeness):` 0.142205
  * `Imports (Out-Degree: 2):` framework.zig, common.zig, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `drivers/wireless/cyw43/wifi.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.772)
- **Top Global Matches:** file_cluster_12: 6.772, file_cluster_7: 8.227, file_cluster_5: 9.617
- **Magnitude:** 287.84 | **LOC:** 726 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 1.815; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Connectivity (formerly Api Exposure) (68.4%), Guard Balance (formerly Safety Score) (53.8%), Complexity Load (formerly Cognitive Load) (13.0%)
- **Documentation Coverage:** 19.3548% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `join` **(Many-Argument Workhorses)** (Impact: 27.1)
    * *Intent:* /// Join a WiFi network
  * `handle_event` **(Many-Argument Workhorses)** (Impact: 26.5)
    * *Intent:* /// Handle event from chip
  * `pack_scan_params` **(Defensive Guards)** (Impact: 19.9)
  * `parse_escan_partial` **(Type Conversions)** (Impact: 9.4)
    * *Intent:* /// Parse an escan partial result into a BSS_Info struct
  * `scan` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 41`, `args: 20`, `func_start: 20`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 39`
* *Architecture:* `api: 33`, `import: 4`
* *Defense:* `safety: 58`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.815
  * `Choke Point (Betweenness):` 0.000581 | `Ripple Effect (Closeness):` 0.111713
  * `Imports (Out-Degree: 4):` bus.zig, consts.zig, sdpcm.zig, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `port/nxp/mcx/src/mcxa153/hal/port.zig` (ZIG) | Magnitude: 11.34 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 15, core_var_decl: 5, api: 4, globals: 4
- `sim/aviron/src/testconfig.zig` (ZIG) | Magnitude: 11.1 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 83, core_var_decl: 16, design_snake_case: 10, design_short_vars: 7
- `port/wch/ch32v/src/hals/ch32v003.zig` (ZIG) | Magnitude: 12.28 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 13, globals: 9, core_var_decl: 9, api: 7
- `modules/freertos/build.zig` (ZIG) | Magnitude: 46.3 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 129, core_var_decl: 27, design_snake_case: 20, branch: 16
- `drivers/sensor/TMP117.zig` (ZIG) | Magnitude: 73.34 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 127, core_var_decl: 37, design_snake_case: 29, structural_boundaries: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `port/stmicro/stm32/src/hals/STM32F103.zig` (ZIG) | Magnitude: 22.58 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: globals: 21, core_var_decl: 21, api: 20, design_snake_case: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `examples/stmicro/stm32/src/hts221.zig` (ZIG) | Magnitude: 10.86 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 36, core_var_decl: 12, design_snake_case: 11, safety: 9
- `port/raspberrypi/rp2xxx/src/hal/pio/assembler/comparison_tests/nec_carrier_control.pio.h` (CPP) | Magnitude: 7.16 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 27, macros: 7, structural_boundaries: 5, pointers: 5
- `port/raspberrypi/rp2xxx/src/hal/pio/assembler/comparison_tests/nec_receive.pio.h` (CPP) | Magnitude: 7.7 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 29, macros: 7, pointers: 7, structural_boundaries: 5
- `drivers/input/rotary-encoder.zig` (ZIG) | Magnitude: 41.32 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 86, safety: 48, test: 20, core_var_decl: 17
- `port/raspberrypi/rp2xxx/src/hal/pio/assembler/comparison_tests/differential_manchester.pio.h` (CPP) | Magnitude: 13.42 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 56, pointers: 14, macros: 13, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `port/raspberrypi/rp2xxx/src/hal/pio/assembler/comparison_tests/apa102.pio.h` (CPP) | Magnitude: 10.46 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 44, macros: 13, pointers: 9, structural_boundaries: 8
- `modules/freertos/src/root.zig` (ZIG) | Magnitude: 18.64 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 31, import: 15, api: 13, globals: 9
- `port/raspberrypi/rp2xxx/src/hal/pio/assembler/comparison_tests/clocked_input.pio.h` (CPP) | Magnitude: 6.88 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 23, macros: 7, structural_boundaries: 5, pointers: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `core/src/cpus/cortex_m/m33.zig` (ZIG) | Magnitude: 35.72 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 223, indent_spaces: 200, core_var_decl: 39, design_snake_case: 31
- `port/espressif/esp/src/tools/cat.zig` (ZIG) | Magnitude: 0.01 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 7, core_var_decl: 7, safety: 6
- `port/stmicro/stm32/src/boards/STM32L476DISCOVERY.zig` (ZIG) | Magnitude: 37.3 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 150, bitwise_ops: 47, core_var_decl: 23, api: 13
- `port/espressif/esp/src/hal/gpio.zig` (ZIG) | Magnitude: 89.78 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 286, core_var_decl: 160, design_snake_case: 142, api: 30
- `examples/stmicro/stm32/src/stm32f1xx/timer_capture.zig` (ZIG) | Magnitude: 14.66 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 61, core_var_decl: 28, design_snake_case: 25, globals: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `drivers/base/DateTime.zig` (ZIG) | Magnitude: 517.4 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 670, branch: 101, structural_boundaries: 97, safety: 97
- `tools/linter/src/main.zig` (ZIG) | Magnitude: 0.24 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 464, safety: 125, branch: 88, structural_boundaries: 85
- `port/stmicro/stm32/src/hals/STM32F407.zig` (ZIG) | Magnitude: 348.24 | Delta: **0.155** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 400, branch: 82, core_var_decl: 76, design_snake_case: 60
- `sim/aviron/src/testrunner.zig` (ZIG) | Magnitude: 201.04 | Delta: **0.169** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 378, core_var_decl: 94, design_snake_case: 83, branch: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `port/stmicro/stm32/src/hals/common/pins_v2.zig` (ZIG) | Magnitude: 110.86 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 201, core_var_decl: 45, branch: 32, globals: 25
- `port/stmicro/stm32/src/hals/STM32F429.zig` (ZIG) | Magnitude: 26.14 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 43, doc: 22, core_var_decl: 16, design_snake_case: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `port/nxp/mcx/src/mcxn947/hal/flexcomm/LP_I2C.zig` (ZIG) | Magnitude: 212.86 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 326, core_var_decl: 84, design_snake_case: 63, structural_boundaries: 49
- `port/raspberrypi/rp2xxx/src/hal/resets.zig` (ZIG) | Magnitude: 55.12 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 112, core_var_decl: 74, design_snake_case: 69, state_mutation: 14
- `tools/printer/tests/generate_test_data.zig` (ZIG) | Magnitude: 0.01 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 38, core_var_decl: 17, design_snake_case: 17, structural_boundaries: 12
- `drivers/stepper/common.zig` (ZIG) | Magnitude: 6.72 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 11, test: 9, safety: 7, scientific: 3

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `sim/aviron/src/lib/Cpu.zig` -> **Grazfather** (100.0% isolated ownership) | Magnitude: 728.84
- `port/espressif/esp/src/hal/rtos.zig` -> **Tudor Andrei Dicu** (100.0% isolated ownership) | Magnitude: 692.6
- `port/espressif/esp/src/hal/radio/osi.zig` -> **Tudor Andrei Dicu** (100.0% isolated ownership) | Magnitude: 596.72
- `port/stmicro/stm32/src/hals/STM32F103/adc.zig` -> **Mathieu Suen** (100.0% isolated ownership) | Magnitude: 495.86
- `drivers/wireless/cyw43439/wifi.zig` -> **Igor Anić** (100.0% isolated ownership) | Magnitude: 396.02

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `drivers/sensor/ICM-20948.zig` -> **Severity: 0.368** (Bridge: 0.0215 * Flux: 17.1227%)
- `core/src/core/usb.zig` -> **Severity: 0.284** (Bridge: 0.0029 * Flux: 96.6856%)
- `drivers/wireless/cyw43/runner.zig` -> **Severity: 0.111** (Bridge: 0.0014 * Flux: 76.445%)
- `drivers/wireless/cyw43439/wifi.zig` -> **Severity: 0.105** (Bridge: 0.0012 * Flux: 90.2306%)
- `drivers/wireless/cyw43439.zig` -> **Severity: 0.073** (Bridge: 0.0029 * Flux: 25.3257%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `drivers/sensor/MLX90640.zig` -> **Severity: 11.939** (Embedded: 0.1421 * Error Risk: 84.0066%)
- `drivers/wireless/cyw43/bus.zig` -> **Severity: 11.425** (Embedded: 0.1428 * Error Risk: 80.0%)
- `drivers/base/Block_Memory.zig` -> **Severity: 11.406** (Embedded: 0.1426 * Error Risk: 80.0%)
- `drivers/sensor/HTS221.zig` -> **Severity: 11.383** (Embedded: 0.1423 * Error Risk: 80.0%)
- `drivers/io_expander/pcf8574.zig` -> **Severity: 11.369** (Embedded: 0.1421 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/src/microzig.zig` -> **Severity: 4174.396** (Blast Radius: 125.232 * Doc Risk: 33.3333%)
- `drivers/sensor/ICM-20948.zig` -> **Severity: 3717.188** (Blast Radius: 45.75 * Doc Risk: 81.25%)
- `drivers/framework.zig` -> **Severity: 3025.524** (Blast Radius: 99.017 * Doc Risk: 30.5556%)
- `core/src/cpus/avr5.zig` -> **Severity: 1104.9** (Blast Radius: 11.049 * Doc Risk: 100.0%)
- `core/test/cpu.zig` -> **Severity: 1008.9** (Blast Radius: 10.089 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 471 literal sites + 12 sites through wrappers = 483

- `to_s` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `modules/network/build.zig`
- `panic` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `modules/foundation-libc/src/libc.zig`
- `set_addr` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `examples/stmicro/stm32/src/stm32f1xx/usb_cdc.zig`
- `set_addr` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `examples/stmicro/stm32/src/stm32f1xx/usb_hid.zig`
- `set_addr` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `examples/stmicro/stm32/src/stm32f1xx/usb_remote_hid.zig`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 17052 call pairs -- scoped 25.2%, unique 0.1%, ambiguous 23.2%, external 51.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 16589 | 25.6% | 0.0% | 23.8% | 50.6% |
| cpp | 377 | 8.5% | 3.2% | 0.0% | 88.3% |
| c | 40 | 32.5% | 0.0% | 0.0% | 67.5% |
| python | 31 | 0.0% | 0.0% | 0.0% | 100.0% |
| javascript | 14 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
