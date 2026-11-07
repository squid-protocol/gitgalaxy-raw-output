# ARCHITECTURAL_BRIEF: micropython
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/micropython/micropython` |
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
- **Scope:** 5252 analyzed artifact(s), 429519 LOC.
- **Load-bearing artifact:** `py/runtime.h` -- 497 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `ports/stm32/boards/stm32u5xx_hal_conf_base.h` -- pulls in 64 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/oofatfs/ff.c` at magnitude 8742.32 (structural weight, not risk).
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
| Total Artifacts | 6478 |
| Analyzed Artifacts (Scanned) | 5252 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1226 |
| Total LOC | 429519 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 81.1% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5013 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0684 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6349 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 203 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 2229 | 323597 | 42.4% |
| EMBEDDED_PYTHON | 1209 | 39233 | 23.0% |
| PYTHON | 672 | 27694 | 12.8% |
| CSV | 262 | 20030 | 5.0% |
| MAKEFILE | 242 | 7322 | 4.6% |
| JSON | 214 | 4425 | 4.1% |
| PLAINTEXT | 138 | 0 | 2.6% |
| MARKDOWN | 135 | 0 | 2.6% |
| JAVASCRIPT | 46 | 1718 | 0.9% |
| YAML | 38 | 1612 | 0.7% |
| SHELL | 22 | 1674 | 0.4% |
| ASSEMBLY | 19 | 724 | 0.4% |
| CPP | 16 | 1164 | 0.3% |
| XML | 9 | 0 | 0.2% |
| PROTO | 1 | 326 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 2 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 5249 |
| cp1252 | cp1252-fallback | 2 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 32%, Declarative / Non-Code 29%, Parameter Forwarders Files 9%, Large Core Modules (3) 7%, Encapsulated Accessors Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4978 | 94.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 273 | 5.2% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1226*

**Composition by Extension & Reason:**
- `.exp`: 623x Excluded (Unsupported Extension: '.exp'), 9x Unsupported Format (.exp)
- `.rst`: 241x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ld`: 115x Excluded (Unsupported Extension: '.ld')
- `.conf`: 28x Excluded (Unsupported Extension: '.conf')
- `.board`: 26x Excluded (Unsupported Extension: '.board')
- `no_extension`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.p4_wifi_common')
- `.py`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 4 exceeds 500 chars), 1x Excluded (Saturation: Line 10 exceeds 500 chars)
- `.h`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 118 LOC), 1x Excluded (Machine-Generated Source Code Signature: 46 LOC)
- `.jpg`: 14x Excluded (Explicitly Denied Extension: '.jpg')
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.overlay`: 8x Excluded (Unsupported Extension: '.overlay')
- `.props`: 7x Excluded (Unsupported Extension: '.props')
- `.c`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.der`: 6x Excluded (Explicitly Denied Extension: '.der')
- `.cfg`: 4x Excluded (Unsupported Extension: '.cfg'), 1x Unsupported Format (.cfg)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.0 | 29.5 | 40.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.2 | 0.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 42.6 | 0.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 36.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3589 | 945 | 2 | `lib/littlefs/lfs2.c` |
| cleanup | 356 | 184 | 0 | `tools/pyboard.py` |
| guards | 30868 | 2414 | 16 | `lib/littlefs/lfs2.c` |
| danger | 6632 | 1628 | 3 | `tools/ci.sh` |
| concurrency | 2030 | 264 | 0 | `tests/extmod/asyncio_gather.py` |
| connectivity | 18068 | 2543 | 9 | `py/obj.h` |
| io | 2746 | 419 | 0 | `tests/ports/cc3200/pin.py` |
| crypto | 55 | 55 | 0 | `ports/stm32/mboot/mboot.py` |
| ipc | 790 | 68 | 0 | `extmod/modlwip.c` |
| time | 153 | 54 | 0 | `tests/run-multitests.py` |
| serialization | 8 | 5 | 0 | `tools/pyboard.py` |
| regex | 205 | 65 | 0 | `ports/stm32/Makefile` |
| events | 1049 | 240 | 0 | `ports/stm32/timer.c` |
| tests | 281 | 56 | 0 | `tests/extmod_hardware/machine_i2c_target.py` |
| docs | 8680 | 649 | 1 | `ports/stm32/timer.c` |
| debt | 13684 | 1896 | 7 | `tools/mpy-tool.py` |
| mutation | 82782 | 2748 | 39 | `lib/oofatfs/ff.c` |
| dead_code | 5786 | 1248 | 3 | `tools/ci.sh` |
| credential | 5 | 5 | 0 | `ports/stm32/boards/NUCLEO_WB55/rfcore_makefirmware.py` |
| threat | 125 | 52 | 0 | `tests/extmod/deflate_decompress.py` |
| ml_ai | 539 | 161 | 0 | `py/emitinlinerv32.c` |
| ui | 369 | 36 | 0 | `tests/extmod/framebuf_bounds.py` |

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

1. **runtime.h** (`py/runtime.h`) — 497 inbound connections
2. **mphal.h** (`py/mphal.h`) — 410 inbound connections
3. **runtime.c** (`py/runtime.c`) — 389 inbound connections
4. **obj.h** (`py/obj.h`) — 371 inbound connections
5. **obj.c** (`py/obj.c`) — 336 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **stm32u5xx_hal_conf_base.h** (`ports/stm32/boards/stm32u5xx_hal_conf_base.h`) — 64 outbound dependencies
2. **stm32n6xx_hal_conf_base.h** (`ports/stm32/boards/stm32n6xx_hal_conf_base.h`) — 59 outbound dependencies
3. **main.c** (`ports/stm32/main.c`) — 56 outbound dependencies
4. **deprecated_definitions.h** (`ports/cc3200/FreeRTOS/Source/include/deprecated_definitions.h`) — 44 outbound dependencies
5. **mptask.c** (`ports/cc3200/mptask.c`) — 44 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `dir_alloc` **(Many-Argument Workhorses)** (@ `lib/oofatfs/ff.c`) -> Impact: **1046.6** | LOC: 1949
  * *Intent:* #if !FF_FS_READONLY /*-----------------------------------------------------------------------*/ /* Directory handling - Reserve a block of directory e...
- `lfs2_file_opencfg_` **(Many-Argument Workhorses)** (@ `lib/littlefs/lfs2.c`) -> Impact: **837.7** | LOC: 1862
  * *Intent:* /// Top level file operations ///
- `f_mkfs` **(Many-Argument Workhorses)** (@ `lib/oofatfs/ff.c`) -> Impact: **453.8** | LOC: 454
  * *Intent:* #endif /* FF_USE_FORWARD */ #if FF_USE_MKFS && !FF_FS_READONLY /*-----------------------------------------------------------------------*/ /* Create a...
- `emit_inline_thumb_op` **(Many-Argument Workhorses)** (@ `py/emitinlinethumb.c`) -> Impact: **405.2** | LOC: 411
  * *Intent:* // shorthand alias for whether we allow ARMv7-M instructions #define ARMV7M asm_thumb_allow_armv7m(&emit->as)
- `mp_obj_str_format_helper` **(Many-Argument Workhorses)** (@ `py/objstr.c`) -> Impact: **347.7** | LOC: 446
  * *Intent:* #else // define to nothing to improve coverage #define terse_str_format_value_error() #endif
- `run_tests` **(Many-Argument Workhorses)** (@ `tests/run-tests.py`) -> Impact: **301.2** | LOC: 440
- `parse_string_literal` **(Many-Argument Workhorses)** (@ `py/lexer.c`) -> Impact: **271.2** | LOC: 371
- `mp_bytecode_print_str` **(Many-Argument Workhorses)** (@ `py/showbc.c`) -> Impact: **235.0** | LOC: 388
- `lfs2_dir_fetchmatch` **(Many-Argument Workhorses)** (@ `lib/littlefs/lfs2.c`) -> Impact: **208.9** | LOC: 279
  * *Intent:* #endif
- `mp_prof_opcode_decode` **(Many-Argument Workhorses)** (@ `py/profile.c`) -> Impact: **196.9** | LOC: 459

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `py` | 210 | 37792.02 | 30.51% | 21.0% |
| `ports/stm32` | 161 | 23003.42 | 22.69% | 26.89% |
| `extmod` | 93 | 15525.86 | 31.83% | 9.53% |
| `tests/basics` | 570 | 9945.54 | 4.18% | 0.0% |
| `lib/oofatfs` | 5 | 9275.06 | 29.63% | 6.87% |
| `tests/extmod` | 200 | 8796.08 | 14.93% | 0.0% |
| `lib/littlefs` | 9 | 8064.86 | 33.91% | 11.75% |
| `ports/esp32` | 76 | 7780.16 | 19.44% | 24.51% |
| `lib/cmsis/inc` | 30 | 6671.2 | 6.18% | 12.34% |
| `ports/mimxrt` | 68 | 6108.3 | 22.19% | 36.02% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/ports_unix.yml` -> **100.0%** Exposure
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
- `ports/cc3200/FreeRTOS/Source/tasks.c` -> **54** Orphaned Functions | **0** Duplicates
- `ports/cc3200/hal/i2c.c` -> **51** Orphaned Functions | **0** Duplicates
- `ports/cc3200/hal/prcm.c` -> **48** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10391` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/oofatfs/ff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.082)
- **Top Global Matches:** file_cluster_8: 10.082, file_cluster_3: 16.367, file_cluster_6: 21.578
- **Magnitude:** 8742.32 | **LOC:** 5948 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **3**; blast radius 0.158; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.4%), Complexity Load (formerly Cognitive Load) (80.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dir_alloc` **(Many-Argument Workhorses)** (Impact: 1046.6)
    * *Intent:* #if !FF_FS_READONLY /*-----------------------------------------------------------------------*/ /* D...
  * `f_mkfs` **(Many-Argument Workhorses)** (Impact: 453.8)
    * *Intent:* #endif /* FF_USE_FORWARD */ #if FF_USE_MKFS && !FF_FS_READONLY /*-----------------------------------...
  * `create_name` **(Many-Argument Workhorses)** (Impact: 167.1)
    * *Intent:* #endif /* FF_USE_FIND && FF_FS_MINIMIZE <= 1 */ /*--------------------------------------------------...
  * `find_volume` **(Many-Argument Workhorses)** (Impact: 147.8)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Determine logical dri...
  * `f_open` **(Many-Argument Workhorses)** (Impact: 127.6)
    * *Intent:* /*-----------------------------------------------------------------------*/ /* Open or Create a File...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1430 instances
* *State Mutation (weighted view):* 4403
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1489`, `structural_boundaries: 391`, `args: 137`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1543`, `unreferenced_by_name: 26`
* *Architecture:* `api: 31`, `import: 3`
* *Defense:* `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.158
  * `Choke Point (Betweenness):` 5.4e-05 | `Ripple Effect (Closeness):` 0.002791
  * `Imports (Out-Degree: 6):` diskio.h, ff.h, string.h
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `lib/littlefs/lfs2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.529)
- **Top Global Matches:** file_cluster_4: 8.529, file_cluster_6: 11.258, file_cluster_16: 13.747
- **Magnitude:** 5513.54 | **LOC:** 6550 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.1; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.0%)
- **Documentation Coverage:** 68.6432% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lfs2_file_opencfg_` **(Many-Argument Workhorses)** (Impact: 837.7)
    * *Intent:* /// Top level file operations ///
  * `lfs2_dir_fetchmatch` **(Many-Argument Workhorses)** (Impact: 208.9)
    * *Intent:* #endif
  * `lfs2_dir_relocatingcommit` **(Many-Argument Workhorses)** (Impact: 132.9)
    * *Intent:* #endif #ifndef LFS2_READONLY
  * `lfs2_dir_traverse` **(Many-Argument Workhorses)** (Impact: 106.9)
  * `lfs2_dir_orphaningcommit` **(Many-Argument Workhorses)** (Impact: 92.2)
    * *Intent:* #endif #ifndef LFS2_READONLY
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 557 instances
* *State Mutation (weighted view):* 1896
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 925`, `structural_boundaries: 964`, `args: 279`, `func_start: 187`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 74`, `state_mutation: 782`, `unreferenced_by_name: 34`
* *Architecture:* `io: 2`, `api: 52`, `import: 2`
* *Defense:* `safety: 1`, `doc: 21`, `immutability_locks: 134`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` lfs2.h, lfs2_util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/compile.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.558)
- **Top Global Matches:** file_cluster_6: 7.558, file_cluster_4: 12.527, file_cluster_8: 14.833
- **Magnitude:** 2503.62 | **LOC:** 3699 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **14**; blast radius 0.421; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.1%), Guard Balance (formerly Safety Score) (63.7%)
- **Documentation Coverage:** 98.4962% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compile_scope_inline_asm` **(Many-Argument Workhorses)** (Impact: 100.8)
    * *Intent:* #if MICROPY_EMIT_INLINE_ASM // requires 3 passes: SCOPE, CODE_SIZE, EMIT
  * `mp_compile_to_raw_code` **(Many-Argument Workhorses)** (Impact: 95.7)
    * *Intent:* #if !MICROPY_EXPOSE_MP_COMPILE_TO_RAW_CODE
  * `compile_expr_stmt` **(Many-Argument Workhorses)** (Impact: 68.1)
    * *Intent:* #endif
  * `compile_scope` **(Many-Argument Workhorses)** (Impact: 66.1)
  * `c_assign` **(Many-Argument Workhorses)** (Impact: 58.3)
    * *Intent:* // assigns top of stack to pn
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 242 instances
* *State Mutation (weighted view):* 766
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 683`, `structural_boundaries: 276`, `args: 167`, `func_start: 100`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 89`, `state_mutation: 282`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 40`
* *Architecture:* `api: 7`, `import: 16`
* *Defense:* `safety: 118`, `doc: 2`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.000523 | `Ripple Effect (Closeness):` 0.059159
  * `Imports (Out-Degree: 28):` assert.h, asmbase.h, compile.h, emit.h, grammar.h, nativeglue.h, persistentcode.h, runtime.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `lib/littlefs/lfs1.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.862)
- **Top Global Matches:** file_cluster_4: 5.862, file_cluster_6: 7.994, file_cluster_16: 12.63
- **Magnitude:** 2264.7 | **LOC:** 2584 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.1; role: Pure Consumer (Orchestrator)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` inttypes.h, lfs1.h, lfs1_util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/objstr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.946)
- **Top Global Matches:** file_cluster_4: 5.946, file_cluster_6: 10.837, file_cluster_16: 11.204
- **Magnitude:** 2124.22 | **LOC:** 2471 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **134** in-repo importer(s); it depends on **8**; blast radius 3.221; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.9%)
- **Documentation Coverage:** 98.3051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mp_obj_str_format_helper` **(Many-Argument Workhorses)** (Impact: 347.7)
    * *Intent:* #else // define to nothing to improve coverage #define terse_str_format_value_error() #endif
  * `str_modulo_format` **(Many-Argument Workhorses)** (Impact: 155.5)
    * *Intent:* #if MICROPY_PY_BUILTINS_STR_OP_MODULO
  * `mp_obj_str_binary_op` **(Many-Argument Workhorses)** (Impact: 59.6)
    * *Intent:* // Note: this function is used to check if an object is a str or bytes, which // works because both ...
  * `mp_str_print_quoted` **(Many-Argument Workhorses)** (Impact: 55.6)
    * *Intent:* /******************************************************************************/ /* str */...
  * `mp_obj_str_split` **(Many-Argument Workhorses)** (Impact: 47.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 242 instances
* *State Mutation (weighted view):* 749
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 493`, `structural_boundaries: 234`, `args: 165`, `func_start: 83`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 265`, `planned_debt: 7`, `unreferenced_by_name: 9`
* *Architecture:* `api: 30`, `import: 8`
* *Defense:* `safety: 89`, `doc: 2`, `immutability_locks: 147`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.221
  * `Choke Point (Betweenness):` 0.000295 | `Ripple Effect (Closeness):` 0.070924
  * `Imports (Out-Degree: 23):` assert.h, cstack.h, objlist.h, objstr.h, objtuple.h, runtime.h, unicode.h, string.h
  * `Imported By (In-Degree: 134):` (Excluded from Brief to save tokens)

### `ports/cc3200/FreeRTOS/Source/tasks.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.205)
- **Top Global Matches:** file_cluster_4: 6.205, file_cluster_15: 9.132, file_cluster_16: 9.425
- **Magnitude:** 1855.8 | **LOC:** 4808 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **8**; blast radius 0.324; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.3%), Debt Markers (formerly Tech Debt) (59.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xTaskGenericNotifyFromISR` **(Many-Argument Workhorses)** (Impact: 47.5)
    * *Intent:* #endif /* configUSE_TASK_NOTIFICATIONS */ /*--------------------------------------------------------...
  * `vTaskPrioritySet` **(Many-Argument Workhorses)** (Impact: 46.0)
    * *Intent:* #endif /* INCLUDE_uxTaskPriorityGet */ /*-----------------------------------------------------------...
  * `prvInitialiseNewTask` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* #endif /* configSUPPORT_DYNAMIC_ALLOCATION */ /*----------------------------------------------------...
  * `xTaskGenericNotify` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* #endif /* configUSE_TASK_NOTIFICATIONS */ /*--------------------------------------------------------...
  * `prvAddCurrentTaskToDelayedList` **(Many-Argument Workhorses)** (Impact: 29.7)
    * *Intent:* #endif /* configUSE_TASK_NOTIFICATIONS */ /*--------------------------------------------------------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 261 instances
* *State Mutation (weighted view):* 847
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 387`, `structural_boundaries: 182`, `args: 96`, `func_start: 77`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 325`, `fragile_debt: 1`, `unreferenced_by_name: 54`
* *Architecture:* `api: 24`, `import: 8`
* *Defense:* `safety: 5`, `doc: 3`, `immutability_locks: 77`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.324
  * `Choke Point (Betweenness):` 0.000235 | `Ripple Effect (Closeness):` 0.007036
  * `Imports (Out-Degree: 13):` FreeRTOS.h, StackMacros.h, stdio.h, stdlib.h, string.h, task.h, tasks_test_access_functions.h, timers.h
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `py/mpz.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.418)
- **Top Global Matches:** file_cluster_4: 5.418, file_cluster_16: 8.762, file_cluster_15: 9.251
- **Magnitude:** 1817.4 | **LOC:** 1759 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 0.149; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mpz_as_str_inpl` **(Many-Argument Workhorses)** (Impact: 54.5)
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
* *Structure:* `branch: 229`, `structural_boundaries: 98`, `args: 64`, `func_start: 50`
* *Risk/State:* `state_mutation: 387`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 16`
* *Architecture:* `api: 31`, `import: 3`
* *Defense:* `safety: 65`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.045029
  * `Imports (Out-Degree: 3):` assert.h, mpz.h, string.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `py/emitnative.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.788)
- **Top Global Matches:** file_cluster_16: 6.788, file_cluster_4: 7.179, file_cluster_15: 9.321
- **Magnitude:** 1483.16 | **LOC:** 3123 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **7**; blast radius 0.404; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.0%), Complexity Load (formerly Cognitive Load) (45.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emit_native_binary_op` **(Many-Argument Workhorses)** (Impact: 127.2)
  * `emit_native_start_pass` **(Many-Argument Workhorses)** (Impact: 104.6)
  * `emit_native_store_subscr` **(Compute Cores)** (Impact: 49.0)
  * `emit_native_call_function` **(Many-Argument Workhorses)** (Impact: 45.2)
  * `emit_native_load_subscr` **(Compute Cores)** (Impact: 39.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 400`, `structural_boundaries: 241`, `args: 168`, `func_start: 115`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 159`, `planned_debt: 13`, `fragile_debt: 2`
* *Architecture:* `api: 8`, `import: 7`
* *Defense:* `safety: 63`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.404
  * `Choke Point (Betweenness):` 3.5e-05 | `Ripple Effect (Closeness):` 0.001523
  * `Imports (Out-Degree: 25):` assert.h, emit.h, nativeglue.h, objfun.h, objstr.h, stdio.h, string.h
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `ports/stm32/usbhost/Class/AUDIO/Src/usbh_audio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.785)
- **Top Global Matches:** file_cluster_4: 5.785, file_cluster_16: 9.317, file_cluster_9: 9.65
- **Magnitude:** 1451.78 | **LOC:** 1995 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.1; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (40.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `USBH_AUDIO_ClassRequest` **(Compute Cores)** (Impact: 38.4)
    * *Intent:* /** * @brief USBH_AUDIO_ClassRequest * The function is responsible for handling Standard requests * ...
  * `ParseCSDescriptors` **(Many-Argument Workhorses)** (Impact: 34.6)
    * *Intent:* /** * @brief Parse AC interfaces * @param phost: Host handle * @retval USBH Status */
  * `USBH_AUDIO_CSRequest` **(Many-Argument Workhorses)** (Impact: 29.9)
    * *Intent:* /** * @brief USBH_AUDIO_CSRequest * The function is responsible for handling AC Specific requests fo...
  * `USBH_AUDIO_InterfaceInit` **(I/O & Config Routines)** (Impact: 28.2)
    * *Intent:* /** * @} */ /** @defgroup USBH_AUDIO_CORE_Private_Functions * @{ */ /** * @brief USBH_AUDIO_Interfac...
  * `USBH_AUDIO_SetFrequency` **(Many-Argument Workhorses)** (Impact: 25.2)
    * *Intent:* /** * @brief USBH_AUDIO_SetFrequency * Set Audio sampling parameters * @param phost: Host handle * @...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 273 instances
* *State Mutation (weighted view):* 916
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 111`, `args: 72`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 370`, `unreferenced_by_name: 7`
* *Architecture:* `api: 14`, `import: 1`
* *Defense:* `doc: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` usbh_audio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/run-tests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.88)
- **Top Global Matches:** file_cluster_6: 6.88, file_cluster_8: 12.397, file_cluster_4: 13.542
- **Magnitude:** 1439.86 | **LOC:** 1366 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.1; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (78.6%), Complexity Load (formerly Cognitive Load) (46.3%), Concurrency Surface (formerly Concurrency) (28.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_tests` **(Many-Argument Workhorses)** (Impact: 301.2)
  * `run_micropython` **(Many-Argument Workhorses)** (Impact: 121.6)
  * `run_one_test` **(Compute Cores)** (Impact: 100.4)
  * `main` **(I/O & Config Routines)** (Impact: 67.2)
  * `detect_test_platform` **(Many-Argument Workhorses)** (Impact: 28.3)
    * *Intent:* # Run a script to detect various bits of information about the target test instance. output = run_fe...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 213 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 16
* *State Mutation (weighted view):* 676
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 115`, `args: 21`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 6`, `state_mutation: 250`, `unreferenced_by_name: 1`
* *Architecture:* `io: 65`, `api: 20`, `concurrency: 6`, `import: 16`
* *Defense:* `safety: 22`, `doc: 2`, `test: 8`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` argparse, glob, json, multiprocessing, multiprocessing.pool, os, platform, pty...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/usbhost/Class/MTP/Src/usbh_mtp_ptp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.253)
- **Top Global Matches:** file_cluster_4: 7.253, file_cluster_9: 8.053, file_cluster_16: 8.142
- **Magnitude:** 1283.9 | **LOC:** 1770 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.114; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (35.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `USBH_PTP_Process` **(Compute Cores)** (Impact: 77.1)
    * *Intent:* /** * @brief USBH_PTP_Process * The function handle the BOT protocol. * @param phost: Host handle * ...
  * `PTP_GetDevicePropValue` **(Many-Argument Workhorses)** (Impact: 37.3)
    * *Intent:* /** * @brief PTP_GetDevicePropValue * Gets objectInfo and fills object_info structure. * @param phos...
  * `USBH_PTP_GetPartialObject` **(Many-Argument Workhorses)** (Impact: 21.7)
    * *Intent:* /** * @brief USBH_PTP_GetPartialObject * Gets object partially * @param phost: Host handle * @param ...
  * `USBH_PTP_GetObjectHandles` **(Many-Argument Workhorses)** (Impact: 17.4)
    * *Intent:* /** * @brief USBH_PTP_GetObjectHandles * Gets device info dataset and fills deviceinfo structure. * ...
  * `USBH_PTP_GetNumObjects` **(Many-Argument Workhorses)** (Impact: 17.1)
    * *Intent:* /** * @brief USBH_PTP_GetNumObjects * Gets device info dataset and fills deviceinfo structure. * @pa...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 211 instances
* *State Mutation (weighted view):* 823
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 115`, `args: 45`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 401`, `unreferenced_by_name: 16`
* *Architecture:* `api: 20`, `import: 2`
* *Defense:* `doc: 55`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00019
  * `Imports (Out-Degree: 4):` usbh_mtp.h, usbh_mtp_ptp.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `extmod/modlwip.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.979)
- **Top Global Matches:** file_cluster_4: 6.979, file_cluster_6: 8.792, file_cluster_16: 13.238
- **Magnitude:** 1255.96 | **LOC:** 1961 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 0.104; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.5%), Complexity Load (formerly Cognitive Load) (59.1%)
- **Documentation Coverage:** 93.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lwip_socket_ioctl` **(Many-Argument Workhorses)** (Impact: 104.6)
  * `lwip_tcp_receive` **(Many-Argument Workhorses)** (Impact: 63.0)
    * *Intent:* // Helper function for recv/recvfrom to handle TCP packets
  * `lwip_getaddrinfo` **(Many-Argument Workhorses)** (Impact: 43.9)
    * *Intent:* // lwip.getaddrinfo
  * `lwip_socket_make_new` **(Many-Argument Workhorses)** (Impact: 40.1)
    * *Intent:* // FIXME: Only supports two arguments at present
  * `lwip_socket_setsockopt` **(Many-Argument Workhorses)** (Impact: 36.2)
    * *Intent:* #if LWIP_VERSION_MAJOR < 2 #define MP_IGMP_IP_ADDR_TYPE ip_addr_t #else #define MP_IGMP_IP_ADDR_TYPE...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 148 instances
* *State Mutation (weighted view):* 489
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 225`, `args: 151`, `func_start: 50`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 193`, `planned_debt: 4`, `fragile_debt: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`, `api: 14`, `import: 20`
* *Defense:* `safety: 16`, `doc: 8`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000338
  * `Imports (Out-Degree: 22):` dns.h, igmp.h, init.h, tcp_priv.h, raw.h, sio.h, tcp.h, tcp_impl.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `extmod/nimble/modbluetooth_nimble.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.756)
- **Top Global Matches:** file_cluster_16: 6.756, file_cluster_4: 7.367, file_cluster_15: 7.758
- **Magnitude:** 1243.38 | **LOC:** 2051 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (89.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `l2cap_channel_event` **(Many-Argument Workhorses)** (Impact: 38.9)
  * `mp_bluetooth_gatts_register_service` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `central_gap_event_cb` **(Many-Argument Workhorses)** (Impact: 31.6)
  * `characteristic_access_cb` **(Many-Argument Workhorses)** (Impact: 29.4)
  * `mp_bluetooth_l2cap_send` **(Many-Argument Workhorses)** (Impact: 27.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 121 instances
* *State Mutation (weighted view):* 413
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 389`, `args: 161`, `func_start: 79`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 171`, `planned_debt: 17`, `unreferenced_by_name: 37`
* *Architecture:* `api: 51`, `import: 18`
* *Defense:* `safety: 46`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.001058
  * `Imports (Out-Degree: 12):` modbluetooth.h, mpbthci.h, modbluetooth_nimble.h, ble_hs.h, util.h, ble.h, ble_hs_hci_priv.h, ble_hs_priv.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `extmod/modbluetooth.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.635)
- **Top Global Matches:** file_cluster_16: 6.635, file_cluster_15: 7.733, file_cluster_4: 8.06
- **Magnitude:** 1141.2 | **LOC:** 1774 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.3%), Guard Balance (formerly Safety Score) (57.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bluetooth_ble_config` **(Many-Argument Workhorses)** (Impact: 56.2)
  * `bluetooth_ble_invoke_irq` **(Compute Cores)** (Impact: 54.7)
  * `invoke_irq_handler_run` **(Many-Argument Workhorses)** (Impact: 51.5)
    * *Intent:* #endif // !MICROPY_PY_BLUETOOTH_USE_SYNC_EVENTS // -------------------------------------------------...
  * `ringbuf_extract` **(Many-Argument Workhorses)** (Impact: 38.0)
    * *Intent:* // Helpers #if !MICROPY_PY_BLUETOOTH_USE_SYNC_EVENTS
  * `bluetooth_uuid_make_new` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* // ---------------------------------------------------------------------------- // UUID object // --...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 110 instances
* *State Mutation (weighted view):* 362
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 180`, `args: 218`, `func_start: 88`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 142`, `planned_debt: 4`, `unreferenced_by_name: 13`
* *Architecture:* `api: 43`, `import: 11`
* *Defense:* `safety: 87`, `immutability_locks: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000828
  * `Imports (Out-Degree: 27):` modbluetooth.h, binary.h, gc.h, misc.h, mperrno.h, mphal.h, obj.h, objarray.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ports/cc3200/FreeRTOS/Source/queue.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.898)
- **Top Global Matches:** file_cluster_4: 5.898, file_cluster_6: 8.489, file_cluster_15: 12.616
- **Magnitude:** 1115.1 | **LOC:** 2567 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **6**; blast radius 0.175; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.5%), Debt Markers (formerly Tech Debt) (60.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xQueueGenericSend` **(Many-Argument Workhorses)** (Impact: 83.6)
    * *Intent:* #endif /* ( ( configUSE_COUNTING_SEMAPHORES == 1 ) && ( configSUPPORT_DYNAMIC_ALLOCATION == 1 ) ) */...
  * `xQueueGenericReceive` **(Many-Argument Workhorses)** (Impact: 81.3)
    * *Intent:* /*-----------------------------------------------------------*/
  * `xQueueGenericSendFromISR` **(Many-Argument Workhorses)** (Impact: 65.6)
    * *Intent:* /*-----------------------------------------------------------*/
  * `xQueueGiveFromISR` **(Many-Argument Workhorses)** (Impact: 49.7)
    * *Intent:* /*-----------------------------------------------------------*/
  * `prvCopyDataToQueue` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* #endif /* configUSE_TRACE_FACILITY */ /*-----------------------------------------------------------*...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 118 instances
* *State Mutation (weighted view):* 370
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 119`, `args: 54`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `state_mutation: 134`, `planned_debt: 2`, `unreferenced_by_name: 31`
* *Architecture:* `api: 15`, `import: 6`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 92`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.005507
  * `Imports (Out-Degree: 10):` FreeRTOS.h, croutine.h, queue.h, stdlib.h, string.h, task.h
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `ports/stm32/uart.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.348)
- **Top Global Matches:** file_cluster_6: 8.348, file_cluster_8: 8.763, file_cluster_4: 16.442
- **Magnitude:** 1070.74 | **LOC:** 1387 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **12**; blast radius 0.127; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.8%), Complexity Load (formerly Cognitive Load) (68.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `uart_init` **(Many-Argument Workhorses)** (Impact: 168.7)
    * *Intent:* // assumes Init parameters have been set up correctly
  * `uart_get_source_freq` **(Compute Cores)** (Impact: 60.2)
  * `uart_deinit` **(Compute Cores)** (Impact: 55.0)
  * `uart_irq_handler` **(Compute Cores)** (Impact: 34.3)
    * *Intent:* // This IRQ handler is set up to handle RXNE, IDLE and ORE interrupts only. // Notes: // - ORE (over...
  * `uart_exists` **(Compute Cores)** (Impact: 26.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 164 instances
* *State Mutation (weighted view):* 566
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 128`, `args: 350`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 238`, `unreferenced_by_name: 14`
* *Architecture:* `api: 19`, `import: 12`
* *Defense:* `safety: 5`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.001448
  * `Imports (Out-Degree: 11):` irq.h, pendsv.h, mperrno.h, mphal.h, runtime.h, stream.h, interrupt_char.h, mpirq.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `py/runtime.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 4.647)
- **Top Global Matches:** file_cluster_4: 4.647, file_cluster_15: 9.809, file_cluster_12: 10.374
- **Magnitude:** 1034.68 | **LOC:** 1787 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **389** in-repo importer(s); it depends on **20**; blast radius 11.832; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.9%), Debt Markers (formerly Tech Debt) (82.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mp_call_prepare_args_n_kw_var` **(Many-Argument Workhorses)** (Impact: 86.0)
    * *Intent:* // This function only needs to be exposed externally when in stackless mode. #if !MICROPY_STACKLESS
  * `mp_unary_op` **(Compute Cores)** (Impact: 57.7)
  * `mp_convert_member_lookup` **(Many-Argument Workhorses)** (Impact: 42.9)
    * *Intent:* #endif // MICROPY_BUILTIN_METHOD_CHECK_SELF_ARG // Given a member that was extracted from an instanc...
  * `mp_resume` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `mp_unpack_ex` **(Many-Argument Workhorses)** (Impact: 26.9)
    * *Intent:* // unpacked items are stored in reverse order into the array pointed to by items
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 135 instances
* *State Mutation (weighted view):* 436
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 151`, `args: 99`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 166`, `planned_debt: 10`, `unreferenced_by_name: 31`
* *Architecture:* `api: 54`, `import: 20`
* *Defense:* `safety: 48`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.832
  * `Choke Point (Betweenness):` 0.002048 | `Ripple Effect (Closeness):` 0.084222
  * `Imports (Out-Degree: 37):` assert.h, vfs.h, builtin.h, compile.h, cstack.h, gc.h, objgenerator.h, objlist.h...
  * `Imported By (In-Degree: 389):` (Excluded from Brief to save tokens)

### `py/lexer.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.7)
- **Top Global Matches:** file_cluster_4: 6.7, file_cluster_6: 8.044, file_cluster_16: 13.056
- **Magnitude:** 1031.32 | **LOC:** 1162 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **6**; blast radius 0.218; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_string_literal` **(Many-Argument Workhorses)** (Impact: 271.2)
  * `mp_lexer_to_next` **(Compute Cores)** (Impact: 165.1)
  * `is_string_or_bytes` **(Stateful Encapsulated Methods)** (Impact: 26.3)
  * `next_char` **(Compute Cores)** (Impact: 25.8)
  * `skip_whitespace` **(Stateful Encapsulated Methods)** (Impact: 25.5)
    * *Intent:* // This function returns whether it has crossed a newline or not. // It therefore always return true...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 122 instances
* *State Mutation (weighted view):* 388
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 122`, `args: 40`, `func_start: 33`
* *Risk/State:* `state_mutation: 144`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 25`, `immutability_locks: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.045957
  * `Imports (Out-Degree: 10):` assert.h, lexer.h, reader.h, runtime.h, stdio.h, string.h
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `extmod/btstack/modbluetooth_btstack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.919)
- **Top Global Matches:** file_cluster_4: 6.919, file_cluster_16: 7.71, file_cluster_15: 8.204
- **Magnitude:** 1010.84 | **LOC:** 1552 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.1; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Debt Markers (formerly Tech Debt) (86.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `btstack_packet_handler_generic` **(Many-Argument Workhorses)** (Impact: 138.6)
    * *Intent:* #endif
  * `mp_bluetooth_gatts_register_service` **(Many-Argument Workhorses)** (Impact: 54.5)
  * `mp_bluetooth_gatts_notify_indicate` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `mp_bluetooth_gatts_write` **(Many-Argument Workhorses)** (Impact: 31.5)
  * `btstack_packet_handler_att_server` **(Many-Argument Workhorses)** (Impact: 30.8)
    * *Intent:* #endif // This needs to be separate to btstack_packet_handler otherwise we get // dual-delivery of t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 208`, `args: 103`, `func_start: 63`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 109`, `planned_debt: 5`, `unreferenced_by_name: 32`
* *Architecture:* `api: 42`, `import: 6`
* *Defense:* `safety: 28`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` modbluetooth_btstack.h, modbluetooth.h, btstack.h, mperrno.h, mphal.h, runtime.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ports/stm32/mboot/main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.447)
- **Top Global Matches:** file_cluster_4: 7.447, file_cluster_12: 8.058, file_cluster_16: 8.891
- **Magnitude:** 1009.86 | **LOC:** 1807 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **17**; blast radius 0.246; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.2%), Guard Balance (formerly Safety Score) (66.9%)
- **Documentation Coverage:** 48.2456% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `i2c_slave_process_rx_end` **(Compute Cores)** (Impact: 69.9)
  * `dfu_handle_tx` **(Many-Argument Workhorses)** (Impact: 38.8)
  * `stm32_main` **(Compute Cores)** (Impact: 35.5)
  * `pyb_usbdd_StrDescriptor` **(Many-Argument Workhorses)** (Impact: 30.1)
  * `hw_read` **(Many-Argument Workhorses)** (Impact: 27.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 438
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 179`, `args: 227`, `func_start: 71`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 188`, `planned_debt: 3`, `unreferenced_by_name: 26`
* *Architecture:* `api: 48`, `import: 17`
* *Defense:* `safety: 10`, `doc: 8`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.001523
  * `Imports (Out-Degree: 20):` boardctrl.h, dfu.h, flash.h, i2cslave.h, irq.h, sha256.c, mboot.h, mpu.h...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `py/parse.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.592)
- **Top Global Matches:** file_cluster_6: 8.592, file_cluster_8: 9.73, file_cluster_4: 16.424
- **Magnitude:** 1003.7 | **LOC:** 1408 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **14**; blast radius 0.456; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mp_parse` **(Many-Argument Workhorses)** (Impact: 161.4)
  * `fold_constants` **(Many-Argument Workhorses)** (Impact: 114.3)
  * `push_result_rule` **(Many-Argument Workhorses)** (Impact: 55.2)
    * *Intent:* #endif
  * `fold_logical_constants` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `mp_parse_node_print` **(Many-Argument Workhorses)** (Impact: 36.6)
    * *Intent:* #if MICROPY_DEBUG_PRINTERS
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 335
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 173`, `args: 58`, `func_start: 30`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 135`, `unreferenced_by_name: 5`
* *Architecture:* `api: 10`, `import: 27`
* *Defense:* `safety: 81`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.00017 | `Ripple Effect (Closeness):` 0.059281
  * `Imports (Out-Degree: 23):` assert.h, builtin.h, grammar.h, lexer.h, objint.h, objstr.h, parse.h, parsenum.h...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `ports/stm32/timer.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.47)
- **Top Global Matches:** file_cluster_6: 6.47, file_cluster_4: 8.167, file_cluster_16: 15.512
- **Magnitude:** 981.78 | **LOC:** 1775 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **9**; blast radius 0.137; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.5%)
- **Documentation Coverage:** 36.1702% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pyb_timer_channel` **(Many-Argument Workhorses)** (Impact: 116.8)
    * *Intent:* /// /// Notes for Timer.ENC modes: /// /// - Requires 2 pins, so one or both pins will need to be co...
  * `pyb_timer_init_helper` **(Many-Argument Workhorses)** (Impact: 49.4)
    * *Intent:* /// measures ticks of `source_freq` divided by `div` clock ticks. /// `deadtime` is only available o...
  * `timer_clock_enable` **(Compute Cores)** (Impact: 39.6)
  * `pyb_timer_channel_callback` **(Compute Cores)** (Impact: 35.3)
    * *Intent:* /// \method callback(fun) /// Set the function to be called when the timer channel triggers. /// `fu...
  * `timer_get_source_freq` **(Compute Cores)** (Impact: 33.6)
    * *Intent:* // Get the frequency (in Hz) of the source clock for the given timer. // On STM32F405/407/415/417 th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 117 instances
* *State Mutation (weighted view):* 393
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 109`, `args: 293`, `func_start: 35`, `class_start: 7`
* *Risk/State:* `state_mutation: 159`, `dead_code: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `safety: 12`, `doc: 208`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.137
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.001036
  * `Imports (Out-Degree: 19):` irq.h, pin.h, gc.h, runtime.h, servo.h, mpirq.h, stdint.h, string.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `py/profile.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.534)
- **Top Global Matches:** file_cluster_4: 5.534, file_cluster_6: 10.489, file_cluster_16: 10.843
- **Magnitude:** 922.06 | **LOC:** 846 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 0.131; role: Pure Consumer (Orchestrator)
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
* *Structure:* `branch: 119`, `structural_boundaries: 110`, `args: 19`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `state_mutation: 229`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 6`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `safety: 12`, `doc: 3`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.037509
  * `Imports (Out-Degree: 13):` bc0.h, gc.h, objfun.h, profile.h, runtime0.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `extmod/modframebuf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.061)
- **Top Global Matches:** file_cluster_4: 8.061, file_cluster_12: 10.191, file_cluster_16: 10.875
- **Magnitude:** 910.64 | **LOC:** 930 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `framebuf_poly` **(Many-Argument Workhorses)** (Impact: 54.0)
  * `line` **(Many-Argument Workhorses)** (Impact: 53.1)
  * `framebuf_make_new_helper` **(Many-Argument Workhorses)** (Impact: 45.7)
  * `framebuf_scroll` **(Many-Argument Workhorses)** (Impact: 24.1)
  * `framebuf_blit` **(Many-Argument Workhorses)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 140 instances
* *State Mutation (weighted view):* 431
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 79`, `args: 82`, `func_start: 43`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 151`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 23`, `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00019
  * `Imports (Out-Degree: 11):` font_petme128_8x8.h, binary.h, runtime.h, stdio.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/objtype.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.916)
- **Top Global Matches:** file_cluster_6: 5.916, file_cluster_4: 8.101, file_cluster_16: 15.688
- **Magnitude:** 881.82 | **LOC:** 1552 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **6**; blast radius 1.596; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.1%), Complexity Load (formerly Cognitive Load) (42.0%)
- **Documentation Coverage:** 90.6977% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mp_obj_class_lookup` **(Many-Argument Workhorses)** (Impact: 57.4)
  * `mp_obj_new_type` **(Many-Argument Workhorses)** (Impact: 51.1)
  * `mp_obj_instance_store_attr` **(Many-Argument Workhorses)** (Impact: 46.1)
  * `type_attr` **(Many-Argument Workhorses)** (Impact: 44.5)
  * `mp_obj_instance_load_attr` **(Many-Argument Workhorses)** (Impact: 39.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 275
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 170`, `args: 79`, `func_start: 35`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 99`, `planned_debt: 7`, `unreferenced_by_name: 3`
* *Architecture:* `api: 11`, `import: 6`
* *Defense:* `safety: 45`, `doc: 5`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.596
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.066552
  * `Imports (Out-Degree: 18):` assert.h, objtype.h, runtime.h, stddef.h, stdio.h, string.h
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/basics/weakref_finalize_basic.py` (EMBEDDED_PYTHON) | Magnitude: 13.4 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: debug_prints: 20, indent_spaces: 14, structural_boundaries: 10, state_mutation: 7
- `tests/basics/fun_code.py` (EMBEDDED_PYTHON) | Magnitude: 7.6 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 8, debug_prints: 7, safety: 6, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `shared/tinyusb/mp_usbd_descriptor.c` (C) | Magnitude: 73.2 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 79, macros: 18, structural_boundaries: 15, branch: 14
- `ports/alif/mpmetalport.c` (C) | Magnitude: 32.12 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 23, pointers: 13, args: 12
- `ports/cc3200/misc/mperror.c` (C) | Magnitude: 86.14 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 39, args: 31, import: 22
- `tests/basics/async_with_break.py` (EMBEDDED_PYTHON) | Magnitude: 31.42 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 38, debug_prints: 20, safety: 15, structural_boundaries: 13
- `ports/mimxrt/mpmetalport.c` (C) | Magnitude: 29.52 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 32, args: 20, structural_boundaries: 19, pointers: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `drivers/ninaw10/nina_wifi_bsp.c` (C) | Magnitude: 39.94 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 62, args: 32, structural_boundaries: 16, macros: 13
- `tests/basics/memoryview1.py` (EMBEDDED_PYTHON) | Magnitude: 28.2 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: debug_prints: 33, memory_alloc: 28, state_mutation: 12, indent_spaces: 12
- `tests/basics/for_range.py` (EMBEDDED_PYTHON) | Magnitude: 16.18 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, debug_prints: 23, safety: 22, branch: 16
- `tests/basics/scope_class.py` (EMBEDDED_PYTHON) | Magnitude: 33.96 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 28, args: 12, func_start: 11
- `lib/cmsis/inc/core_starmc1.h` (C) | Magnitude: 599.4 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: macros: 1084, indent_spaces: 986, bitwise_ops: 395, args: 172

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/inlineasm/thumb/asmit.py` (PYTHON) | Magnitude: 4.16 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 2, args: 2, func_start: 2
- `tests/inlineasm/thumb/asmdiv.py` (PYTHON) | Magnitude: 5.86 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: debug_prints: 7, structural_boundaries: 2, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests/ports/rp2/rp2_thread_reset_part1.py` (EMBEDDED_PYTHON) | Magnitude: 6.22 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 3, concurrency: 3, indent_spaces: 2, branch: 1
- `tests/thread/stress_create.py` (EMBEDDED_PYTHON) | Magnitude: 29.84 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, branch: 3, safety_bypasses: 3
- `tests/basics/struct2.py` (EMBEDDED_PYTHON) | Magnitude: 16.14 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: debug_prints: 23, indent_spaces: 23, scientific: 13, safety: 12
- `tests/internal_bench/class_create-7.1-inherit_initsubclass.py` (PYTHON) | Magnitude: 6.0 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 7, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `ports/mimxrt/hal/resethandler_MIMXRT10xx.S` (ASSEMBLY) | Magnitude: 22.4 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: args: 106, indent_spaces: 102, structural_boundaries: 38, pointers: 22
- `tests/ports/stm32/pyb_can.py` (EMBEDDED_PYTHON) | Magnitude: 76.78 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 89, core_var_decl: 54, design_snake_case: 52, debug_prints: 47
- `tests/inlineasm/thumb/asmblbx.py` (PYTHON) | Magnitude: 2.48 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, debug_prints: 2, structural_boundaries: 1, args: 1
- `tests/ports/unix/ffi_int_base.py` (EMBEDDED_PYTHON) | Magnitude: 14.18 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 6, safety: 4, debug_prints: 4
- `tests/inlineasm/thumb/asmfpldrstr.py` (PYTHON) | Magnitude: 3.9 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `ports/mimxrt/systick.h` (C) | Magnitude: 12.0 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 10, macros: 8, structural_boundaries: 7, api: 6
- `ports/renesas-ra/systick.h` (C) | Magnitude: 12.0 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 10, macros: 8, structural_boundaries: 7, api: 6
- `ports/stm32/systick.h` (C) | Magnitude: 12.0 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 10, macros: 8, structural_boundaries: 7, api: 6
- `tests/extmod/cryptolib_aes128_ctr.py` (EMBEDDED_PYTHON) | Magnitude: 9.22 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, debug_prints: 5, safety: 4
- `ports/webassembly/proxy_c.h` (C) | Magnitude: 17.8 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 16, api: 14, args: 11, pointers: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `ports/renesas-ra/usbd.c` (C) | Magnitude: 2.92 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 5, import: 4, indent_spaces: 3, macros: 2
- `ports/cc3200/hal/utils.c` (C) | Magnitude: 4.28 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 14, macros: 6, args: 3, inline_asm: 3
- `ports/stm32/modos.c` (C) | Magnitude: 17.34 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 29, macros: 12, structural_boundaries: 8, pointers: 7
- `ports/renesas-ra/boards/EK_RA6M1/ra_gen/pin_data.c` (C) | Magnitude: 20.92 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 69, macros: 8, core_var_decl: 6, design_snake_case: 6
- `ports/embed/port/mphalport.c` (C) | Magnitude: 3.0 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: import: 2, pointers: 2, structural_boundaries: 1, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/import/import_override.py` (EMBEDDED_PYTHON) | Magnitude: 10.68 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, reflection_metaprogramming: 3, safety: 2
- `tests/float/string_format.py` (PYTHON) | Magnitude: 3.38 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: debug_prints: 3, explicit_casts: 3, indent_spaces: 3, safety: 2
- `ports/renesas-ra/boards/EK_RA6M2/ra_gen/pin_data.c` (C) | Magnitude: 21.02 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 74, macros: 8, core_var_decl: 6, design_snake_case: 6
- `ports/renesas-ra/gccollect.h` (C) | Magnitude: 27.3 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: api: 12, globals: 12, macros: 2
- `ports/stm32/gccollect.h` (C) | Magnitude: 27.3 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: api: 12, globals: 12, macros: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `ports/webassembly/api.js` (JAVASCRIPT) | Magnitude: 208.2 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 227, structural_boundaries: 37, branch: 36, core_var_decl: 30
- `ports/rp2/rp2_pio.c` (C) | Magnitude: 601.38 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 628, pointers: 340, branch: 118, args: 100
- `ports/renesas-ra/ra/ra_i2c.c` (C) | Magnitude: 619.52 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 485, pointers: 217, state_mutation: 140, branch: 87

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `py/makeqstrdefs.py` (PYTHON) | Magnitude: 240.38 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 166, branch: 53, state_mutation: 52, structural_boundaries: 47
- `ports/esp8266/network_wlan.c` (C) | Magnitude: 513.44 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 560, pointers: 181, branch: 149, structural_boundaries: 104
- `ports/mimxrt/hal/phy/device/phydp83867/fsl_phydp83867.c` (C) | Magnitude: 267.84 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 167, pointers: 77, branch: 48, state_mutation: 46
- `ports/alif/machine_spi.c` (C) | Magnitude: 278.28 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 248, pointers: 97, branch: 57, state_mutation: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/multi_wlan/getaddrinfo.py` (PYTHON) | Magnitude: 4.7 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 6, safety: 5, io: 3
- `tests/basics/subclass_native_exc_new.py` (EMBEDDED_PYTHON) | Magnitude: 9.78 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 15, debug_prints: 5, safety_bypasses: 4
- `tests/basics/decorator.py` (EMBEDDED_PYTHON) | Magnitude: 7.7 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 7, args: 5, func_start: 4
- `tests/thread/thread_sleep2.py` (EMBEDDED_PYTHON) | Magnitude: 46.24 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 11, debug_prints: 6, concurrency: 5, structural_boundaries: 4
- `tests/basics/nanbox_smallint.py` (EMBEDDED_PYTHON) | Magnitude: 17.66 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 11, debug_prints: 8, explicit_casts: 6, safety: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tools/mpremote/mpremote/commands.py` (PYTHON) | Magnitude: 0.83 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 540, branch: 190, core_var_decl: 127, design_snake_case: 127

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `ports/nrf/boards/PCA10059/modules/recover_uicr_regout0.c` (C) | Magnitude: 20.94 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 14, pointers: 8, structural_boundaries: 7, branch: 6
- `ports/nrf/examples/ubluepy_temp.py` (EMBEDDED_PYTHON) | Magnitude: 67.54 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 23, state_mutation: 22, structural_boundaries: 14, core_var_decl: 13

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tools/ci.sh` -> Churn: **84.24%** | Cog Load: 29.9748% | Debt: 100.0%
- `ports/stm32/pyb_can.c` -> Churn: **56.17%** | Cog Load: 75.8759% | Debt: 10.8891%
- `ports/stm32/fdcan.c` -> Churn: **55.53%** | Cog Load: 66.3364% | Debt: 94.6641%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/littlefs/lfs2.c` -> **Daniël van de Giessen** (100.0% isolated ownership) | Magnitude: 5513.54
- `py/compile.c` -> **Alessandro Gatti** (100.0% isolated ownership) | Magnitude: 2503.62
- `py/emitnative.c` -> **Alessandro Gatti** (100.0% isolated ownership) | Magnitude: 1483.16
- `extmod/nimble/modbluetooth_nimble.c` -> **Alessandro Gatti** (100.0% isolated ownership) | Magnitude: 1243.38
- `ports/stm32/uart.c` -> **Damien George** (100.0% isolated ownership) | Magnitude: 1070.74

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `py/runtime.c` -> **Severity: 0.205** (Bridge: 0.002 * Flux: 99.9967%)
- `py/obj.c` -> **Severity: 0.103** (Bridge: 0.0011 * Flux: 96.0526%)
- `py/compile.c` -> **Severity: 0.052** (Bridge: 0.0005 * Flux: 99.9785%)
- `py/mpprint.c` -> **Severity: 0.044** (Bridge: 0.0004 * Flux: 100.0%)
- `extmod/vfs.c` -> **Severity: 0.032** (Bridge: 0.0003 * Flux: 99.981%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `py/mpprint.c` -> **Severity: 6.293** (Embedded: 0.0783 * Error Risk: 80.3623%)
- `py/runtime.c` -> **Severity: 5.325** (Embedded: 0.0842 * Error Risk: 63.22%)
- `py/obj.c` -> **Severity: 5.079** (Embedded: 0.0898 * Error Risk: 56.5311%)
- `py/objexcept.c` -> **Severity: 4.883** (Embedded: 0.0753 * Error Risk: 64.8781%)
- `py/obj.h` -> **Severity: 4.745** (Embedded: 0.1025 * Error Risk: 46.299%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `py/obj.h` -> **Severity: 4525.5** (Blast Radius: 45.255 * Doc Risk: 100.0%)
- `py/misc.h` -> **Severity: 2326.4** (Blast Radius: 23.264 * Doc Risk: 100.0%)
- `py/vstr.c` -> **Severity: 2055.2** (Blast Radius: 20.552 * Doc Risk: 100.0%)
- `py/runtime.h` -> **Severity: 1517.0** (Blast Radius: 15.17 * Doc Risk: 100.0%)
- `py/obj.c` -> **Severity: 1454.0** (Blast Radius: 14.54 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 12913 literal sites + 317 sites through wrappers = 13230
- **`memory_alloc`:** 644 literal sites + 84 sites through wrappers = 728
- **`panics_and_aborts`:** 1898 literal sites + 35 sites through wrappers = 1933

- `list` (function, debug_prints, primitive): 69 call sites in 34 files -- `ports/nrf/examples/mountsd.py`
- `log` (function, debug_prints, primitive): 53 call sites in 1 files -- `ports/stm32/boards/NUCLEO_WB55/rfcore_firmware.py`
- `malloc` (macro, memory_alloc, via nimble_malloc): 19 call sites in 13 files -- `extmod/nimble/syscfg/syscfg.h`
- `sub` (function, debug_prints, primitive): 15 call sites in 8 files -- `tests/micropython/viper_binop_arith.py`
- `m_new_obj_maybe` (macro, memory_alloc, via m_new_maybe): 12 call sites in 9 files -- `py/misc.h`
- `m_new_maybe` (macro, memory_alloc, via m_malloc_maybe): 10 call sites in 7 files -- `py/misc.h`
- `mp_local_alloc` (macro, memory_alloc, primitive): 10 call sites in 8 files -- `py/pystack.h`
- `dump_version` (function, debug_prints, primitive): 7 call sites in 1 files -- `ports/stm32/boards/NUCLEO_WB55/rfcore_debug.py`
- `lfs2_malloc` (function, memory_alloc, primitive): 7 call sites in 1 files -- `lib/littlefs/lfs2_util.h`
- `task` (function, debug_prints, primitive): 7 call sites in 1 files -- `tests/extmod/asyncio_gather.py`
- `task` (function, debug_prints, primitive): 6 call sites in 1 files -- `tests/extmod/asyncio_event.py`
- `dump_memory_size` (function, debug_prints, primitive): 5 call sites in 1 files -- `ports/stm32/boards/NUCLEO_WB55/rfcore_debug.py`
*(+111 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 60780 call pairs -- scoped 20.1%, unique 20.7%, ambiguous 9.5%, external 49.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 42273 | 20.4% | 29.7% | 7.3% | 42.6% |
| embedded_python | 9889 | 16.9% | 0.0% | 15.3% | 67.8% |
| python | 8018 | 22.9% | 0.0% | 14.1% | 63.0% |
| shell | 409 | 21.3% | 0.0% | 0.0% | 78.7% |
| javascript | 157 | 7.6% | 0.0% | 9.6% | 82.8% |
| makefile | 24 | 0.0% | 0.0% | 0.0% | 100.0% |
| cpp | 10 | 10.0% | 20.0% | 20.0% | 50.0% |

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
