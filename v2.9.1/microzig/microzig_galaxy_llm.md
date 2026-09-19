# ARCHITECTURAL_BRIEF: microzig
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ZigEmbeddedGroup/microzig.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 761 analyzed artifact(s), 94803 LOC.
- **Load-bearing artifact:** `core/src/microzig.zig` -- 315 in-repo importer(s) depend on it. Changes here propagate furthest.
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
| Analyzed Artifacts (Scanned) | 761 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 253 |
| Total LOC | 94803 |
| Volatility Index | 0.012 |
| % Scanned of codebase = | 75.0% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6663 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4363 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7682 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 40 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 546 | 84882 | 71.7% |
| C | 61 | 3507 | 8.0% |
| ASSEMBLY | 54 | 1758 | 7.1% |
| JSON | 42 | 4452 | 5.5% |
| MARKDOWN | 40 | 0 | 5.3% |
| XML | 6 | 2 | 0.8% |
| BINARY_THREAT | 4 | 4 | 0.5% |
| PYTHON | 3 | 106 | 0.4% |
| PLAINTEXT | 2 | 0 | 0.3% |
| YAML | 1 | 12 | 0.1% |
| SHELL | 1 | 3 | 0.1% |
| JAVASCRIPT | 1 | 77 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `2.04`
> **Composition Archetype:** `Hub-Coupled App` (z +2.04; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 20%, Large Core Modules (2) 17%, Large Core Modules 14%, Large Core Modules (3) 13%, Declarative / Non-Code 12%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 709 | 93.2% |
| Unknown | 4 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 46 | 6.0% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 253*

**Composition by Extension & Reason:**
- `.zig`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1222 LOC), 1x Excluded (Embedded Hex Payload: 3430 hex tokens in 943 LOC)
- `.zon`: 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Zero-Density Threshold (LOC: 72, Signals: 0), 1x Zero-Density Threshold (LOC: 270, Signals: 0)
- `.elf`: 42x Excluded (Unsupported Extension: '.elf')
- `.pio`: 27x Unsupported Format (.pio)
- `.svg`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ld`: 13x Excluded (Unsupported Extension: '.ld'), 1x Unsupported Format (.ld)
- `.smd`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.smd')
- `.svd`: 2x Unsupported Format (.svd), 1x Excluded (Monolithic Amalgamation: 36933 LOC exceeds safe regex boundaries), 1x Excluded (Monolithic Amalgamation: 38097 LOC exceeds safe regex boundaries)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 5x Excluded (Explicitly Denied Extension: '.png')
- `.s`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.shtml`: 4x Excluded (Unsupported Extension: '.shtml')
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xcf`: 1x Excluded (Unsupported Extension: '.xcf'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.2 | 7.6 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.8 | 27.2 | 4.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.5 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 27.6 | 10.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 35.0 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 16.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 97.1 | 1.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 29.2 | 4.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 14.3 | 10.9 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.4 | 79.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5990 | 365 | 22 | `sim/aviron/src/lib/Cpu.zig` |
| cleanup | 752 | 62 | 0 | `tools/regz/src/gen.zig` |
| guards | 9030 | 398 | 29 | `tools/regz/src/gen.zig` |
| danger | 3168 | 340 | 14 | `port/espressif/esp/src/hal/radio/osi.zig` |
| concurrency | 167 | 31 | 0 | `modules/rtt/src/lock.zig` |
| connectivity | 7245 | 590 | 25 | `modules/riscv32-common/src/riscv32_common.zig` |
| io | 207 | 64 | 0 | `port/raspberrypi/rp2xxx/tools/rp2040-flash.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 3 | 0 | `scripts/usb/device_loopback.py` |
| time | 8 | 3 | 0 | `port/raspberrypi/rp2xxx/tools/rp2040-flash.zig` |
| serialization | 4 | 3 | 0 | `tools/regz/src/embassy.zig` |
| regex | 31 | 16 | 0 | `tools/regz/src/svd.zig` |
| events | 496 | 144 | 2 | `examples/wch/ch32v/src/sharp_niceview.zig` |
| tests | 1029 | 62 | 0 | `drivers/base/DateTime.zig` |
| docs | 6804 | 265 | 28 | `sim/aviron/src/lib/Cpu.zig` |
| debt | 489 | 144 | 2 | `sim/aviron/src/lib/Cpu.zig` |
| mutation | 22045 | 559 | 80 | `tools/regz/src/gen.zig` |
| dead_code | 591 | 264 | 2 | `modules/riscv32-common/src/riscv32_common.zig` |
| credential | 6 | 4 | 0 | `tools/sorcerer/build.zig.zon` |
| threat | 571 | 123 | 2 | `port/raspberrypi/rp2xxx/src/hal/pio/assembler/tokenizer.zig` |
| ml_ai | 532 | 95 | 1 | `port/raspberrypi/rp2xxx/src/hal/rom/rp2040.zig` |
| ui | 1 | 1 | 0 | `tools/arm-docs-userscript/tablegen.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.1707**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `port/raspberrypi/rp2xxx/tools/rp2040-flash.zig` (Hits: 11)
- `sim/aviron/testsuite/instructions/in-stdio.S` (Hits: 11)
- `tools/sorcerer/src/RegzWindow.zig` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **microzig.zig** (`core/src/microzig.zig`) — 315 inbound connections
2. **framework.zig** (`drivers/framework.zig`) — 25 inbound connections
3. **enums.zig** (`port/stmicro/stm32/src/hals/common/enums.zig`) — 16 inbound connections
4. **Database.zig** (`tools/regz/src/Database.zig`) — 14 inbound connections
5. **hw.zig** (`port/raspberrypi/rp2xxx/src/hal/hw.zig`) — 11 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **framework.zig** (`drivers/framework.zig`) — 36 outbound dependencies
2. **comparison_tests.zig** (`port/raspberrypi/rp2xxx/src/hal/pio/assembler/comparison_tests.zig`) — 31 outbound dependencies
3. **hal.zig** (`port/raspberrypi/rp2xxx/src/hal.zig`) — 28 outbound dependencies
4. **hal.zig** (`port/espressif/esp/src/hal.zig`) — 23 outbound dependencies
5. **README.md** (`examples/raspberrypi/rp2xxx/README.md`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `write_device` **(Many-Argument Workhorses)** (@ `tools/regz/src/gen.zig`) -> Impact: **518.2** | LOC: 1465
- `write_interrupt_list` **(Many-Argument Workhorses)** (@ `tools/regz/src/gen.zig`) -> Impact: **478.3** | LOC: 1472
- `write_struct` **(Many-Argument Workhorses)** (@ `tools/regz/src/gen.zig`) -> Impact: **462.5** | LOC: 1461
- `Tokenizer` **(Defensive Guards)** (@ `port/raspberrypi/rp2xxx/src/hal/pio/assembler/tokenizer.zig`) -> Impact: **369.6** | LOC: 1056
  * *Intent:* // the characters we're interested in are: // ';' -> line comment // '/' -> '/' -> line comment // '/' -> '*' -> block comment // '%' -> <whitespace> ...
- `write_fields` **(Many-Argument Workhorses)** (@ `tools/regz/src/gen.zig`) -> Impact: **228.4** | LOC: 1551
- `load_into_db` **(Many-Argument Workhorses)** (@ `tools/regz/src/embassy.zig`) -> Impact: **194.2** | LOC: 445
- `Encoder` **(Many-Argument Workhorses)** (@ `port/raspberrypi/rp2xxx/src/hal/pio/assembler/encoder.zig`) -> Impact: **155.2** | LOC: 540
- `PioImpl` **(Many-Argument Workhorses)** (@ `port/raspberrypi/rp2xxx/src/hal/pio/common.zig`) -> Impact: **116.2** | LOC: 453
- `DeviceController` **(Many-Argument Workhorses)** (@ `core/src/core/usb.zig`) -> Impact: **114.7** | LOC: 388
  * *Intent:* /// USB device controller /// /// Responds to host requests and dispatches to the appropriate drivers. /// When this type is build (at comptime), it b...
- `to_string` **(Many-Argument Workhorses)** (@ `drivers/base/DateTime.zig`) -> Impact: **103.4** | LOC: 144
  * *Intent:* /// %p AM or PM indicator /// /// %M Minute as a zero-padded decimal number. 00, 01, ..., 59 /// %-M Minute as a decimal number. 0, 1, ..., 59 /// ///...

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `port/raspberrypi/rp2xxx/src/hal` | 34 | 3481.7 | 12.91% | 14.03% |
| `port/espressif/esp/src/hal` | 19 | 2021.34 | 10.51% | 6.5% |
| `drivers/wireless/cyw43/firmware` | 6 | 2002.0 | 0.0% | 0.0% |
| `port/raspberrypi/rp2xxx/src/hal/pio/assembler` | 4 | 1845.98 | 15.67% | 4.41% |
| `port/stmicro/stm32/src/hals/STM32F103` | 17 | 1827.28 | 13.31% | 3.65% |
| `port/wch/ch32v/src/hals` | 13 | 1528.5 | 10.65% | 22.52% |
| `port/stmicro/stm32/src/hals/common` | 13 | 1130.14 | 23.93% | 4.76% |
| `drivers/base` | 7 | 1096.9 | 10.54% | 1.19% |
| `drivers/display` | 7 | 1029.14 | 4.17% | 5.9% |
| `sim/aviron/src/lib` | 5 | 1002.52 | 18.8% | 23.84% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `modules/freertos/src/picosdk_stubs.c` -> **100.0%** Exposure
- `modules/foundation-libc/src/modules/string.zig` -> **99.9994%** Exposure
- `port/gigadevice/gd32/src/hals/GD32VF103.zig` -> **99.9993%** Exposure
- `port/raspberrypi/rp2xxx/src/hal/always_on_timer.zig` -> **99.9984%** Exposure
- `port/stmicro/stm32/src/hals/STM32F429.zig` -> **99.9831%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `port/stmicro/stm32/src/hals/common/dma_common.zig` -> **100.0%** Exposure
- `port/stmicro/stm32/src/hals/common/spi_v2.zig` -> **100.0%** Exposure
- `port/stmicro/stm32/src/hals/common/systick.zig` -> **100.0%** Exposure
- `port/stmicro/stm32/src/hals/common/timer_v1.zig` -> **100.0%** Exposure
- `port/stmicro/stm32/src/hals/common/uart_v3.zig` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `modules/riscv32-common/src/riscv32_common.zig` -> **16** Orphaned Functions | **0** Duplicates
- `port/wch/ch32v/src/cpus/main.zig` -> **15** Orphaned Functions | **0** Duplicates
- `port/raspberrypi/rp2xxx/src/hal/always_on_timer.zig` -> **13** Orphaned Functions | **0** Duplicates
- `port/raspberrypi/rp2xxx/src/cpus/hazard3.zig` -> **11** Orphaned Functions | **0** Duplicates
- `port/stmicro/stm32/src/hals/STM32F407.zig` -> **10** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `54` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1445` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `port/raspberrypi/rp2xxx/src/hal/pio/assembler/tokenizer.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1195.36 | **LOC:** 2286 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 2.432; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (60.1%), Mutation Surface (formerly State Flux) (55.9%), Complexity Load (formerly Cognitive Load) (34.7%), Guard Balance (formerly Safety Score) (10.4%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.432
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.005352
  * `Imports (Out-Degree: 2):` chip.zig, assembler.zig, Expression.zig, bounded-array, std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `sim/aviron/src/lib/Cpu.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 728.84 | **LOC:** 1825 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 2.094; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.2%), Guard Balance (formerly Safety Score) (57.4%)
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
* *Risk/State:* `safety_bypasses: 33`, `high_risk_execution: 6`, `state_mutation: 109`, `dead_code: 1`, `planned_debt: 10`
* *Architecture:* `api: 98`, `import: 4`
* *Defense:* `safety: 83`, `doc: 416`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.094
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.003641
  * `Imports (Out-Degree: 2):` bus.zig, decoder.zig, std, hexdump.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `port/espressif/esp/src/hal/rtos.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 675.1 | **LOC:** 1460 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.597; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (79.4%)
- **Documentation Coverage:** 92.1053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spawn` **(Many-Argument Workhorses)** (Impact: 17.1)
  * `interrupt_handler_c` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* // Can't be preempted by a higher priority interrupt so already in a "critical // section".
  * `put` **(Many-Argument Workhorses)** (Impact: 12.5)
  * `get` **(Many-Argument Workhorses)** (Impact: 12.5)
  * `wait` **(Defensive Guards)** (Impact: 11.8)
    * *Intent:* /// Puts the task to sleep. Must execute inside a critical section.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 60 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 117`, `args: 81`, `func_start: 81`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 70`, `dead_code: 4`, `planned_debt: 8`
* *Architecture:* `api: 92`, `import: 4`
* *Defense:* `safety: 64`, `doc: 23`, `test: 2`, `sync_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001311
  * `Imports (Out-Degree: 2):` microzig, std, system.zig, systimer.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `port/espressif/esp/src/hal/radio/osi.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 596.72 | **LOC:** 1273 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 0.902; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (93.4%), Connectivity (formerly Api Exposure) (85.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.5%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.902
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.002949
  * `Imports (Out-Degree: 3):` radio.zig, rng.zig, rtos.zig, time.zig, builtin, esp-wifi-driver, microzig, std...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `drivers/base/DateTime.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 517.4 | **LOC:** 944 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.205; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (55.4%), Guard Balance (formerly Safety Score) (52.2%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.017038
  * `Imports (Out-Degree: 1):` framework.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `drivers/wireless/cyw43/firmware/43439A0_7_95_61.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/wireless/cyw43/firmware/43439A0_7_95_88.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/wireless/cyw43/firmware/43439A0_btfw.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/wireless/cyw43/firmware/43439A0_clm.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `port/stmicro/stm32/src/hals/STM32F103/adc.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 495.86 | **LOC:** 1122 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.579; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.5%), Mutation Surface (formerly State Flux) (69.2%), Guard Balance (formerly Safety Score) (50.1%)
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
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 32`, `dead_code: 2`
* *Architecture:* `api: 72`, `import: 4`
* *Defense:* `safety: 55`, `doc: 78`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.579
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001311
  * `Imports (Out-Degree: 2):` enums.zig, microzig, std, time.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `port/raspberrypi/rp2xxx/src/hal/pio/assembler/encoder.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 458.04 | **LOC:** 1203 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 2.885; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (58.4%), Mutation Surface (formerly State Flux) (29.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (24.7%), Complexity Load (formerly Cognitive Load) (11.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Encoder` **(Many-Argument Workhorses)** (Impact: 155.2)
  * `encode_instruction` **(Many-Argument Workhorses)** (Impact: 52.3)
  * `encode_instruction_body` **(Defensive Guards)** (Impact: 38.7)
  * `calc_delay_side_set` **(Defensive Guards)** (Impact: 27.1)
  * `evaluate_impl` **(Many-Argument Workhorses)** (Impact: 22.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 55`, `args: 22`, `func_start: 22`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 15`
* *Architecture:* `api: 22`, `import: 6`
* *Defense:* `safety: 253`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.885
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.006422
  * `Imports (Out-Degree: 3):` chip.zig, assembler.zig, Expression.zig, bounded-array, std, tokenizer.zig
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `modules/riscv32-common/src/riscv32_common.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 436.98 | **LOC:** 590 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.554; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (92.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.6%)
- **Documentation Coverage:** 95.1807% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Csr` **(Type Conversions)** (Impact: 34.9)
  * `modify` **(Generic / Templated Code)** (Impact: 6.3)
  * `get_bits` **(Type Conversions)** (Impact: 6.3)
  * `write_raw` **(State Mutators)** (Impact: 4.9)
  * `set_raw` **(State Mutators)** (Impact: 4.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 19`, `args: 30`, `func_start: 30`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 14`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 16`
* *Architecture:* `api: 325`, `import: 2`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `port/raspberrypi/rp2xxx/src/hal/pio/common.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 431.48 | **LOC:** 648 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.678; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (96.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.1%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.001747
  * `Imports (Out-Degree: 4):` chip.zig, gpio.zig, hw.zig, assembler.zig, encoder.zig, microzig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `core/src/allocator.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 423.5 | **LOC:** 1626 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.554; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (46.1%), Guard Balance (formerly Safety Score) (31.5%)
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
* *Risk/State:* `safety_bypasses: 65`, `high_risk_execution: 2`, `state_mutation: 88`, `dead_code: 5`
* *Architecture:* `api: 19`, `import: 2`
* *Defense:* `safety: 239`, `doc: 135`, `test: 42`, `sync_locks: 13`, `cleanup: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` microzig.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/core/usb.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 390.7 | **LOC:** 656 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 11.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.2%), Guard Balance (formerly Safety Score) (73.5%)
- **Documentation Coverage:** 40.2778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DeviceController` **(Many-Argument Workhorses)** (Impact: 114.7)
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
* *Structure:* `branch: 67`, `structural_boundaries: 54`, `args: 33`, `func_start: 27`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 28`, `planned_debt: 2`
* *Architecture:* `api: 39`, `import: 6`
* *Defense:* `safety: 16`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.053
  * `Choke Point (Betweenness):` 0.003548 | `Ripple Effect (Closeness):` 0.147427
  * `Imports (Out-Degree: 5):` std, descriptor.zig, CDC.zig, EchoExample.zig, hid.zig, types.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `drivers/wireless/cyw43439/wifi.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 384.02 | **LOC:** 1029 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.893; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.2%), Connectivity (formerly Api Exposure) (69.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.3%), Guard Balance (formerly Safety Score) (51.2%)
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
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 52`, `dead_code: 4`
* *Architecture:* `api: 37`, `import: 4`
* *Defense:* `safety: 70`, `doc: 32`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.012531
  * `Imports (Out-Degree: 1):` bus.zig, ioctl.zig, nvram.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `port/stmicro/stm32/src/hals/STM32F407.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 358.24 | **LOC:** 624 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.554; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (94.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.8%), Mutation Surface (formerly State Flux) (22.1%)
- **Documentation Coverage:** 89.8305% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Uart` **(Many-Argument Workhorses)** (Impact: 76.4)
  * `I2CController` **(Many-Argument Workhorses)** (Impact: 72.4)
  * `init` **(Compute Cores)** (Impact: 22.0)
  * `is_valid_pin` **(Many-Argument Workhorses)** (Impact: 13.2)
    * *Intent:* /// Checks if a pin is valid for a given uart index and direction
  * `is_valid_pin` **(Compute Cores)** (Impact: 12.9)
    * *Intent:* /// Checks if a pin is valid for a given i2c index and line
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 36`, `args: 31`, `func_start: 31`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 2`, `state_mutation: 4`, `planned_debt: 9`, `unreferenced_by_name: 10`
* *Architecture:* `api: 40`, `import: 2`
* *Defense:* `safety: 14`, `doc: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` microzig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `port/raspberrypi/rp2xxx/src/hal/pins.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 345.36 | **LOC:** 973 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.583; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.4%), Guard Balance (formerly Safety Score) (58.0%), Mutation Surface (formerly State Flux) (42.7%)
- **Documentation Coverage:** 88.7097% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `apply` **(Compute Cores)** (Impact: 82.7)
  * `get_direction` **(Compute Cores)** (Impact: 30.9)
  * `pins` **(Defensive Guards)** (Impact: 18.6)
    * *Intent:* /// Populate and return the PinsType struct /// /// Can be called at comptime or runtime
  * `PinsType` **(Defensive Guards)** (Impact: 16.1)
  * `is_pwm` **(I/O & Config Routines)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 39`, `args: 28`, `func_start: 28`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 16`, `planned_debt: 2`
* *Architecture:* `api: 31`, `import: 7`
* *Defense:* `safety: 19`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.583
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001311
  * `Imports (Out-Degree: 2):` adc.zig, compatibility.zig, gpio.zig, microzig, pwm.zig, resets.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `core/src/utilities.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 323.52 | **LOC:** 664 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 36.105; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (60.7%), Guard Balance (formerly Safety Score) (45.7%)
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
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 2`, `state_mutation: 32`, `dead_code: 1`
* *Architecture:* `api: 31`, `import: 2`
* *Defense:* `safety: 54`, `doc: 32`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.215209
  * `Imports (Out-Degree: 1):` microzig.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `port/stmicro/stm32/src/hals/common/timer_v1.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 316.58 | **LOC:** 598 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.743; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (82.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.1%)
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
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`, `dead_code: 10`, `planned_debt: 2`
* *Architecture:* `api: 74`, `import: 3`
* *Defense:* `safety: 4`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.743
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.002621
  * `Imports (Out-Degree: 2):` enums.zig, microzig, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `port/espressif/esp/src/hal/i2c.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 312.86 | **LOC:** 661 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.554; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (67.0%), Connectivity (formerly Api Exposure) (62.8%), Guard Balance (formerly Safety Score) (50.4%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` gpio.zig, microzig, std, time.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/network/src/root.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 307.9 | **LOC:** 620 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.554; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.8%), Connectivity (formerly Api Exposure) (80.4%), Guard Balance (formerly Safety Score) (65.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (33.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` config, link, dhcp.h, etharp.h, ethip6.h, init.h, netif.h, tcp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `port/raspberrypi/rp2xxx/src/hal/gpio.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 291.62 | **LOC:** 585 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.554; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (67.8%)
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
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 2`, `state_mutation: 17`, `dead_code: 2`
* *Architecture:* `api: 54`, `import: 5`
* *Defense:* `safety: 10`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` compatibility.zig, hw.zig, microzig, resets.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/wireless/cyw43/wifi.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 290.04 | **LOC:** 726 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.554; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Connectivity (formerly Api Exposure) (68.4%), Guard Balance (formerly Safety Score) (61.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.8%)
- **Documentation Coverage:** 19.3548% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `join` **(Many-Argument Workhorses)** (Impact: 29.3)
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
* *Structure:* `branch: 53`, `structural_boundaries: 41`, `args: 20`, `func_start: 20`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 39`
* *Architecture:* `api: 33`, `import: 4`
* *Defense:* `safety: 58`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bus.zig, consts.zig, sdpcm.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/rtt/src/rtt.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 289.94 | **LOC:** 588 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.554; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.0%), Debt Markers (formerly Tech Debt) (21.6%)
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
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 31`, `planned_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 26`, `import: 3`
* *Defense:* `safety: 8`, `doc: 79`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` lock.zig, memory_barrier.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `port/wch/ch32v/src/cpus/main.zig` -> Churn: **86.05%** | Cog Load: 4.7758% | Debt: 77.5171%
- `port/stmicro/stm32/src/hals/STM32F303.zig` -> Churn: **73.88%** | Cog Load: 0.0% | Debt: 88.0797%
- `port/stmicro/stm32/src/boards/STM32F3DISCOVERY.zig` -> Churn: **68.56%** | Cog Load: 0.0% | Debt: 66.1282%
- `port/stmicro/stm32/src/hals/STM32L47X.zig` -> Churn: **68.56%** | Cog Load: 0.0% | Debt: 88.0797%
- `tools/linter/src/main.zig` -> Churn: **59.82%** | Cog Load: 14.3208% | Debt: 60.9546%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `sim/aviron/src/lib/Cpu.zig` -> **Grazfather** (100.0% isolated ownership) | Magnitude: 728.84
- `port/espressif/esp/src/hal/rtos.zig` -> **Tudor Andrei Dicu** (100.0% isolated ownership) | Magnitude: 675.1
- `port/espressif/esp/src/hal/radio/osi.zig` -> **Tudor Andrei Dicu** (100.0% isolated ownership) | Magnitude: 596.72
- `port/stmicro/stm32/src/hals/STM32F103/adc.zig` -> **Mathieu Suen** (100.0% isolated ownership) | Magnitude: 495.86
- `drivers/wireless/cyw43439/wifi.zig` -> **Igor Anić** (100.0% isolated ownership) | Magnitude: 384.02

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/src/core/usb.zig` -> **Severity: 0.343** (Bridge: 0.0035 * Flux: 96.6856%)
- `tools/regz/src/Database.zig` -> **Severity: 0.011** (Bridge: 0.0003 * Flux: 32.4145%)
- `port/stmicro/stm32/src/hals/common/uart_v3.zig` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 100.0%)
- `drivers/wireless/cyw43439.zig` -> **Severity: 0.005** (Bridge: 0.0002 * Flux: 25.3257%)
- `port/raspberrypi/rp2xxx/src/hal/pio/assembler.zig` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 48.4421%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `core/src/interrupt.zig` -> **Severity: 14.689** (Embedded: 0.2152 * Error Risk: 68.255%)
- `core/src/core/usb.zig` -> **Severity: 10.834** (Embedded: 0.1474 * Error Risk: 73.4857%)
- `core/src/utilities.zig` -> **Severity: 9.844** (Embedded: 0.2152 * Error Risk: 45.7405%)
- `core/src/core/arm_semihosting.zig` -> **Severity: 9.239** (Embedded: 0.1474 * Error Risk: 62.6694%)
- `core/src/core/usb/drivers/CDC.zig` -> **Severity: 7.087** (Embedded: 0.1117 * Error Risk: 63.4669%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/src/microzig.zig` -> **Severity: 6970.16** (Blast Radius: 209.105 * Doc Risk: 33.3333%)
- `core/src/utilities.zig` -> **Severity: 2426.729** (Blast Radius: 36.105 * Doc Risk: 67.2131%)
- `core/src/core/arm_semihosting.zig` -> **Severity: 866.008** (Blast Radius: 11.053 * Doc Risk: 78.3505%)
- `core/src/interrupt.zig` -> **Severity: 849.529** (Blast Radius: 36.105 * Doc Risk: 23.5294%)
- `drivers/framework.zig` -> **Severity: 790.534** (Blast Radius: 25.872 * Doc Risk: 30.5556%)

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
