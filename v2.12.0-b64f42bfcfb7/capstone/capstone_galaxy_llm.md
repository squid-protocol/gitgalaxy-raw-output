# ARCHITECTURAL_BRIEF: capstone
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/capstone-engine/capstone.git` |
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
- **Scope:** 2048 analyzed artifact(s), 607568 LOC.
- **Load-bearing artifact:** `include/capstone/capstone.h` -- 155 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `suite/auto-sync/src/autosync/cpptranslator/CppTranslator.py` -- pulls in 77 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `arch/ARM/ARMDisassembler.c` at magnitude 6136.32 (structural weight, not risk).
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
| Total Artifacts | 3963 |
| Analyzed Artifacts (Scanned) | 2048 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1915 |
| Total LOC | 607568 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 51.7% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5267 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3443 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2799 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 37 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 906 | 16565 | 44.2% |
| YAML | 481 | 13660 | 23.5% |
| C | 433 | 562470 | 21.1% |
| PYTHON | 91 | 7356 | 4.4% |
| MARKDOWN | 39 | 0 | 1.9% |
| PLAINTEXT | 28 | 0 | 1.4% |
| JAVA | 20 | 2312 | 1.0% |
| CPP | 11 | 1318 | 0.5% |
| MAKEFILE | 10 | 959 | 0.5% |
| SHELL | 8 | 312 | 0.4% |
| JSON | 7 | 947 | 0.3% |
| APEX | 6 | 669 | 0.3% |
| POWERSHELL | 3 | 369 | 0.1% |
| BATCH | 2 | 232 | 0.1% |
| RUBY | 1 | 387 | 0.0% |
| M4 | 1 | 12 | 0.0% |
| XML | 1 | 0 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2047 |
| cp1252 | cp1252-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 47%, Declarative / Non-Code 36%, Generic / Templated Code Files 3%, Large Core Modules (3) 3%, Compute Cores Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1975 | 96.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 73 | 3.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1915*

**Composition by Extension & Reason:**
- `.yaml`: 132x Zero-Density Threshold (LOC: 109, Signals: 0), 131x Zero-Density Threshold (LOC: 73, Signals: 0), 115x Zero-Density Threshold (LOC: 145, Signals: 0)
- `.cs`: 10x Zero-Density Threshold (LOC: 169, Signals: 0), 10x Zero-Density Threshold (LOC: 57, Signals: 0), 10x Zero-Density Threshold (LOC: 65, Signals: 0)
- `.inc`: 3x Excluded (Machine-Generated Source Code Signature: 120 LOC), 2x Excluded (Machine-Generated Source Code Signature: 5380 LOC), 2x Excluded (Machine-Generated Source Code Signature: 205 LOC)
- `.py`: 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 338 LOC), 1x Statistical Anomaly (Z-Score: -5.35 < -4.75)
- `.ml`: 35x Excluded (Unsupported Extension: '.ml')
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.xcworkspacedata')
- `.patch`: 15x Excluded (Unsupported Extension: '.patch')
- `.java`: 1x Excluded (Machine-Generated Source Code Signature: 3011 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1333 LOC), 1x Excluded (Machine-Generated Source Code Signature: 167 LOC)
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 352 LOC), 1x Excluded (Machine-Generated Source Code Signature: 62 LOC), 1x Excluded (Machine-Generated Source Code Signature: 55 LOC)
- `.md`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 173, Signals: 0)
- `.txt`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xcscheme`: 4x Excluded (Unsupported Extension: '.xcscheme')
- `.toml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.toml')
- `.bas`: 3x Excluded (Unsupported Extension: '.bas')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.3 | 6.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 84.1 | 10.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 12.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 18.3 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.4 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 15.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 322 | 111 | 0 | `suite/auto-sync/src/autosync/cpptranslator/Differ.py` |
| cleanup | 73 | 26 | 0 | `suite/cstest/src/helper.c` |
| guards | 7669 | 424 | 5 | `arch/ARM/ARMDisassembler.c` |
| danger | 491 | 104 | 0 | `arch/X86/X86DisassemblerDecoder.c` |
| concurrency | 55 | 15 | 0 | `suite/run_invalid_cstool.sh` |
| connectivity | 3923 | 506 | 5 | `bindings/java/capstone/Capstone.java` |
| io | 319 | 46 | 0 | `Makefile` |
| crypto | 1 | 1 | 0 | `suite/auto-sync/src/autosync/Helper.py` |
| ipc | 35 | 13 | 0 | `Makefile` |
| time | 4 | 2 | 0 | `arch/X86/X86MappingInsnName.inc` |
| serialization | 0 | 0 | 0 | - |
| regex | 101 | 21 | 0 | `suite/auto-sync/src/autosync/MCUpdater.py` |
| events | 47 | 13 | 0 | `arch/M680X/M680XDisassembler.c` |
| tests | 361 | 14 | 0 | `suite/auto-sync/src/autosync/cpptranslator/Tests/test_patches.py` |
| docs | 2884 | 203 | 0 | `include/capstone/capstone.h` |
| debt | 1246 | 148 | 0 | `cstool/cstool_aarch64.c` |
| mutation | 30590 | 452 | 15 | `include/capstone/arm64.h` |
| dead_code | 1708 | 229 | 1 | `arch/M68K/M68KDisassembler.c` |
| credential | 3 | 3 | 0 | `suite/auto-sync/src/autosync/cpptranslator/arch_config.json` |
| threat | 25 | 4 | 0 | `tests/integration/test_iter.c` |
| ml_ai | 107 | 21 | 0 | `arch/SystemZ/SystemZMCTargetDesc.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Makefile` (Hits: 68)
- `suite/run_invalid_cstool.sh` (Hits: 52)
- `suite/run_clang_tidy.sh` (Hits: 24)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **capstone.h** (`include/capstone/capstone.h`) — 155 inbound connections
2. **utils.h** (`utils.h`) — 127 inbound connections
3. **platform.h** (`include/capstone/platform.h`) — 83 inbound connections
4. **MCInst.h** (`MCInst.h`) — 77 inbound connections
5. **MCRegisterInfo.h** (`MCRegisterInfo.h`) — 66 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CppTranslator.py** (`suite/auto-sync/src/autosync/cpptranslator/CppTranslator.py`) — 77 outbound dependencies
2. **test_patches.py** (`suite/auto-sync/src/autosync/cpptranslator/Tests/test_patches.py`) — 72 outbound dependencies
3. **cs.c** (`cs.c`) — 35 outbound dependencies
4. **capstone.h** (`include/capstone/capstone.h`) — 31 outbound dependencies
5. **test_detail.h** (`suite/cstest/include/test_detail.h`) — 26 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `compressInst` **(Many-Argument Workhorses)** (@ `arch/RISCV/RISCVGenCompressedInstructionsInfo.inc`) -> Impact: **1128.2** | LOC: 1259
- `isCompressibleInst` **(Compute Cores)** (@ `arch/RISCV/RISCVGenCompressedInstructionsInfo.inc`) -> Impact: **972.9** | LOC: 989
- `uncompressInst` **(Many-Argument Workhorses)** (@ `arch/RISCV/RISCVGenCompressedInstructionsInfo.inc`) -> Impact: **932.6** | LOC: 1124
- `WASM_getInstruction` **(Many-Argument Workhorses)** (@ `arch/WASM/WASMDisassembler.c`) -> Impact: **611.9** | LOC: 416
- `translateImmediate` **(Many-Argument Workhorses)** (@ `arch/X86/X86Disassembler.c`) -> Impact: **552.2** | LOC: 669
  * *Intent:* /// translateImmediate - Appends an immediate operand to an MCInst. /// /// @param mcInst - The MCInst to append to. /// @param immediate - The immedi...
- `DecodeVLDInstruction` **(Many-Argument Workhorses)** (@ `arch/ARM/ARMDisassembler.c`) -> Impact: **491.2** | LOC: 299
- `DecodeVSTInstruction` **(Many-Argument Workhorses)** (@ `arch/ARM/ARMDisassembler.c`) -> Impact: **474.7** | LOC: 281
- `_cs_disasm` **(Many-Argument Workhorses)** (@ `bindings/ocaml/ocaml.c`) -> Impact: **428.8** | LOC: 1697
- `printInst` **(Many-Argument Workhorses)** (@ `arch/AArch64/AArch64InstPrinter.c`) -> Impact: **403.3** | LOC: 508
- `add_cs_detail_general` **(Many-Argument Workhorses)** (@ `arch/ARM/ARMMapping.c`) -> Impact: **398.8** | LOC: 736
  * *Intent:* /// Fills cs_detail with the data of the operand. /// This function handles operands which's original printer function has no /// specialities.

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `arch/X86` | 31 | 16505.12 | 11.9% | 9.51% |
| `arch/ARM` | 14 | 9668.18 | 23.87% | 29.6% |
| `arch/AArch64` | 12 | 7147.48 | 23.08% | 20.41% |
| `__monolith__` | 43 | 5623.44 | 13.83% | 16.73% |
| `suite/MC/AArch64` | 355 | 5156.28 | 0.71% | 0.0% |
| `arch/RISCV` | 14 | 4636.74 | 18.9% | 30.59% |
| `suite/cstest/src` | 28 | 4182.28 | 64.27% | 47.59% |
| `arch/HPPA` | 9 | 3697.4 | 9.22% | 13.33% |
| `arch/Mips` | 11 | 3101.02 | 19.47% | 14.91% |
| `arch/M68K` | 6 | 2937.3 | 30.32% | 34.27% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `bindings/vb6/vbCapstone.cpp` -> **100.0%** Exposure
- `arch/PowerPC/PPCDisassembler.c` -> **99.9999%** Exposure
- `arch/ARM/ARMDisassemblerExtension.c` -> **99.9946%** Exposure
- `MCInst.c` -> **99.9901%** Exposure
- `MCInstrDesc.c` -> **99.9447%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `arch/AArch64/AArch64Module.c` -> **100.0%** Exposure
- `arch/ARC/ARCModule.c` -> **100.0%** Exposure
- `arch/ARM/ARMModule.c` -> **100.0%** Exposure
- `arch/Alpha/AlphaModule.c` -> **100.0%** Exposure
- `arch/LoongArch/LoongArchModule.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `arch/M68K/M68KDisassembler.c` -> **299** Orphaned Functions | **0** Duplicates
- `arch/ARM/ARMInstPrinter.c` -> **74** Orphaned Functions | **0** Duplicates
- `suite/auto-sync/src/autosync/cpptranslator/Tests/test_patches.py` -> **66** Orphaned Functions | **0** Duplicates
- `arch/SH/SHDisassembler.c` -> **52** Orphaned Functions | **0** Duplicates
- `arch/Xtensa/XtensaDisassembler.c` -> **50** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2142` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `arch/ARM/ARMDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.027)
- **Top Global Matches:** file_cluster_6: 7.027, file_cluster_8: 12.784, file_cluster_4: 13.312
- **Magnitude:** 6136.32 | **LOC:** 7307 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 0.237; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.5%), Guard Balance (formerly Safety Score) (57.7%)
- **Documentation Coverage:** 98.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DecodeVLDInstruction` **(Many-Argument Workhorses)** (Impact: 491.2)
  * `DecodeVSTInstruction` **(Many-Argument Workhorses)** (Impact: 474.7)
  * `DecodeCopMemInstruction` **(Many-Argument Workhorses)** (Impact: 328.7)
  * `DecodeAddrMode3Instruction` **(Many-Argument Workhorses)** (Impact: 305.0)
  * `DecodeMSRMask` **(Many-Argument Workhorses)** (Impact: 139.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 307 instances
* *State Mutation (weighted view):* 973
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1956`, `structural_boundaries: 1414`, `args: 1773`, `func_start: 178`, `class_start: 1`
* *Risk/State:* `state_mutation: 359`, `dead_code: 12`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 23`
* *Defense:* `safety: 4`, `doc: 21`, `immutability_locks: 389`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.237
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000535
  * `Imports (Out-Degree: 19):` LEB128.h, MCDisassembler.h, MCFixedLenDisassembler.h, MCInst.h, MCInstrDesc.h, MCRegisterInfo.h, MathExtras.h, cs_priv.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `arch/RISCV/RISCVGenCompressedInstructionsInfo.inc` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 17.619)
- **Top Global Matches:** file_cluster_1: 17.619, file_cluster_3: 31.922, file_cluster_8: 53.597
- **Magnitude:** 3328.06 | **LOC:** 3670 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.245; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.0%), Complexity Load (formerly Cognitive Load) (30.3%), Connectivity (formerly Api Exposure) (19.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compressInst` **(Many-Argument Workhorses)** (Impact: 1128.2)
  * `isCompressibleInst` **(Compute Cores)** (Impact: 972.9)
  * `uncompressInst` **(Many-Argument Workhorses)** (Impact: 932.6)
  * `RISCVValidateMCOperandForCompress` **(Many-Argument Workhorses)** (Impact: 88.9)
    * *Intent:* \*===----------------------------------------------------------------------===*/ #ifdef GEN_COMPRESS...
  * `RISCVValidateMachineOperand` **(Many-Argument Workhorses)** (Impact: 57.6)
    * *Intent:* #endif //GEN_UNCOMPRESS_INSTR #ifdef GEN_CHECK_COMPRESS_INSTR #undef GEN_CHECK_COMPRESS_INSTR
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1851`, `structural_boundaries: 260`, `args: 2360`, `func_start: 6`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `api: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.245
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000765
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `arch/HPPA/HPPADisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.394)
- **Top Global Matches:** file_cluster_8: 10.394, file_cluster_3: 14.29, file_cluster_6: 22.693
- **Magnitude:** 3193.32 | **LOC:** 3841 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.226; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.4%), Mutation Surface (formerly State Flux) (30.8%), Complexity Load (formerly Cognitive Load) (25.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fill_alu_mods` **(Many-Argument Workhorses)** (Impact: 179.8)
  * `getInstruction` **(Many-Argument Workhorses)** (Impact: 161.8)
  * `fill_alu_insn_name` **(Compute Cores)** (Impact: 131.2)
  * `decode_alu` **(Many-Argument Workhorses)** (Impact: 124.3)
  * `fill_copr_mods` **(Many-Argument Workhorses)** (Impact: 122.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1332`, `structural_boundaries: 716`, `args: 765`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 71`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 4`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` Mapping.h, MathExtras.h, utils.h, HPPAConstants.h, HPPADisassembler.h, stddef.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/M68K/M68KDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.52)
- **Top Global Matches:** file_cluster_16: 7.52, file_cluster_15: 9.91, file_cluster_17: 10.605
- **Magnitude:** 2542.16 | **LOC:** 3946 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.226; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Complexity Load (formerly Cognitive Load) (93.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.7319% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_ea_mode_op` **(Many-Argument Workhorses)** (Impact: 163.8)
    * *Intent:* /* Make string of effective address mode */
  * `d68020_cpgen` **(Compute Cores)** (Impact: 106.3)
  * `get_with_index_address_mode` **(Many-Argument Workhorses)** (Impact: 91.5)
  * `update_am_reg_list` **(Stateful Encapsulated Methods)** (Impact: 35.8)
  * `d68010_movec` **(Compute Cores)** (Impact: 35.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 313 instances
* *State Mutation (weighted view):* 1169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 306`, `structural_boundaries: 522`, `args: 440`, `func_start: 372`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 543`, `unreferenced_by_name: 299`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` MCInst.h, MCInstrDesc.h, MCRegisterInfo.h, MathExtras.h, cs_priv.h, utils.h, M68KDisassembler.h, M68KInstPrinter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/AArch64/AArch64Mapping.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.557)
- **Top Global Matches:** file_cluster_6: 5.557, file_cluster_8: 11.932, file_cluster_4: 12.725
- **Magnitude:** 2535.3 | **LOC:** 2910 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 0.273; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.8%), Complexity Load (formerly Cognitive Load) (43.6%)
- **Documentation Coverage:** 54.9451% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AArch64_add_cs_detail_1` **(Many-Argument Workhorses)** (Impact: 273.6)
    * *Intent:* /// Fills cs_detail with the data of the operand. /// This function handles operands which original ...
  * `AArch64_add_cs_detail_0` **(Many-Argument Workhorses)** (Impact: 218.6)
    * *Intent:* /// Fills cs_detail with the data of the operand. /// This function handles operands which's origina...
  * `add_non_alias_details` **(Compute Cores)** (Impact: 171.3)
  * `AArch64_add_cs_detail_2` **(Many-Argument Workhorses)** (Impact: 163.5)
    * *Intent:* /// Fills cs_detail with the data of the operand. /// This function handles operands which original ...
  * `AArch64_add_cs_detail_4` **(Many-Argument Workhorses)** (Impact: 105.1)
    * *Intent:* /// Fills cs_detail with the data of the operand. /// This function handles operands which original ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 212 instances
* *State Mutation (weighted view):* 644
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 818`, `structural_boundaries: 386`, `args: 621`, `func_start: 56`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 220`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 12`
* *Architecture:* `api: 32`, `import: 17`
* *Defense:* `safety: 2`, `doc: 60`, `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.273
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000595
  * `Imports (Out-Degree: 18):` Mapping.h, MathExtras.h, cs_simple_types.h, utils.h, AArch64AddressingModes.h, AArch64BaseInfo.h, AArch64DisassemblerExtension.h, AArch64GenCSAliasMnemMap.inc...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `arch/X86/X86DisassemblerDecoder.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.183)
- **Top Global Matches:** file_cluster_8: 6.183, file_cluster_6: 16.07, file_cluster_3: 21.085
- **Magnitude:** 2227.92 | **LOC:** 2573 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.241; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.7%)
- **Documentation Coverage:** 10.3448% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkPrefix` **(Compute Cores)** (Impact: 238.7)
    * *Intent:* // return True if instruction is illegal to use with prefixes // This also check & fix the isPrefixN...
  * `readPrefixes` **(Compute Cores)** (Impact: 208.7)
    * *Intent:* /* * readPrefixes - Consumes all of an instruction's prefix bytes, and marks the * instruction as ha...
  * `getID` **(Compute Cores)** (Impact: 170.1)
    * *Intent:* /* * getID - Determines the ID of an instruction, consuming the ModR/M byte as * appropriate for ext...
  * `readOperands` **(Compute Cores)** (Impact: 99.8)
    * *Intent:* /* * readOperands - Consults the specifier for an instruction and consumes all * operands for that i...
  * `decode` **(Many-Argument Workhorses)** (Impact: 87.9)
    * *Intent:* /* * decode - Reads the appropriate instruction table to obtain the unique ID of * an instruction. *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 301 instances
* *State Mutation (weighted view):* 933
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 727`, `structural_boundaries: 362`, `args: 32`, `func_start: 28`, `class_start: 7`
* *Risk/State:* `state_mutation: 331`, `dead_code: 43`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 16`
* *Defense:* `safety: 2`, `doc: 84`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000396
  * `Imports (Out-Degree: 10):` cs_priv.h, utils.h, X86DisassemblerDecoder.h, X86GenDisassemblerTables.inc, X86GenDisassemblerTables2.inc, X86GenDisassemblerTables_reduce.inc, X86GenDisassemblerTables_reduce2.inc, X86GenInstrInfo.inc...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `arch/X86/X86GenDisassemblerTables2.inc` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.635)
- **Top Global Matches:** file_cluster_2: 4.635, file_cluster_17: 6.392, file_cluster_15: 7.451
- **Magnitude:** 2057.64 | **LOC:** 102152 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.247; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000446
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.842)
- **Top Global Matches:** file_cluster_6: 6.842, file_cluster_4: 6.949, file_cluster_16: 14.643
- **Magnitude:** 1856.42 | **LOC:** 2179 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 14.3%
- **Blast Radius:** changing it is visible to **63** in-repo importer(s); it depends on **35**; blast radius 3.443; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (87.7%), Guard Balance (formerly Safety Score) (72.2%)
- **Documentation Coverage:** 49.4624% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cs_op_index` **(Many-Argument Workhorses)** (Impact: 217.5)
  * `cs_op_count` **(Many-Argument Workhorses)** (Impact: 143.8)
  * `cs_disasm` **(Many-Argument Workhorses)** (Impact: 101.6)
    * *Intent:* #endif // dynamically allocate memory to contain disasm insn // NOTE: caller must free() the allocat...
  * `cs_option` **(Many-Argument Workhorses)** (Impact: 67.3)
  * `skipdata_size` **(Compute Cores)** (Impact: 42.0)
    * *Intent:* // how many bytes will we skip when encountering data (CS_OPT_SKIPDATA)? // this very much depends o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 302 instances
* *State Mutation (weighted view):* 921
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 341`, `structural_boundaries: 327`, `args: 150`, `func_start: 46`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 317`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 40`
* *Architecture:* `api: 45`, `import: 35`
* *Defense:* `safety: 31`, `doc: 3`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.443
  * `Choke Point (Betweenness):` 0.000212 | `Ripple Effect (Closeness):` 0.0188
  * `Imports (Out-Degree: 33):` Availability.h, MCRegisterInfo.h, Mapping.h, SStream.h, AArch64Module.h, ARCModule.h, ARMModule.h, AlphaModule.h...
  * `Imported By (In-Degree: 63):` (Excluded from Brief to save tokens)

### `arch/SH/SHDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.086)
- **Top Global Matches:** file_cluster_4: 6.086, file_cluster_6: 9.995, file_cluster_16: 10.879
- **Magnitude:** 1839.46 | **LOC:** 2184 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.226; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.5%), Guard Balance (formerly Safety Score) (64.5%)
- **Documentation Coverage:** 97.6744% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decode_dsp_3op` **(Many-Argument Workhorses)** (Impact: 150.6)
  * `sh_disassemble` **(Many-Argument Workhorses)** (Impact: 75.7)
  * `decode_long` **(Many-Argument Workhorses)** (Impact: 56.2)
    * *Intent:* #include "SHInsnTable.inc"
  * `opfxxd` **(Many-Argument Workhorses)** (Impact: 54.3)
  * `op4xxb` **(Many-Argument Workhorses)** (Impact: 51.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 193 instances
* *State Mutation (weighted view):* 608
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 361`, `structural_boundaries: 363`, `args: 207`, `func_start: 84`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 222`, `unreferenced_by_name: 52`
* *Architecture:* `api: 7`, `import: 9`
* *Defense:* `safety: 1`, `doc: 18`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` MCDisassembler.h, MCInst.h, cs_priv.h, utils.h, SHDisassembler.h, SHInsnTable.inc, sh.h, stdarg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/X86/X86MappingInsn.inc` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.335)
- **Top Global Matches:** file_cluster_2: 5.335, file_cluster_17: 5.611, file_cluster_15: 7.814
- **Magnitude:** 1831.68 | **LOC:** 105978 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.247; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (2.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001338
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `arch/M680X/M680XDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.655)
- **Top Global Matches:** file_cluster_6: 6.655, file_cluster_4: 7.799, file_cluster_16: 14.608
- **Magnitude:** 1813.36 | **LOC:** 2343 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **23**; blast radius 0.25; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.8%)
- **Documentation Coverage:** 98.5507% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_sufficient_code_size` **(Many-Argument Workhorses)** (Impact: 137.8)
  * `indexed09_hdlr` **(Many-Argument Workhorses)** (Impact: 80.2)
    * *Intent:* // M6809/M6309 indexed mode handler
  * `M680X_getInstruction` **(Many-Argument Workhorses)** (Impact: 79.5)
  * `indexed12_hdlr` **(Many-Argument Workhorses)** (Impact: 48.5)
    * *Intent:* // CPU12 indexed mode handler
  * `get_indexed09_post_byte_size` **(Compute Cores)** (Impact: 45.8)
    * *Intent:* // If successful return the additional byte size needed for M6809 // indexed addressing mode (includ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 249 instances
* *State Mutation (weighted view):* 813
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 363`, `structural_boundaries: 284`, `args: 116`, `func_start: 65`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 315`, `fragile_debt: 6`, `unreferenced_by_name: 4`
* *Architecture:* `api: 12`, `import: 23`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.25
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000297
  * `Imports (Out-Degree: 21):` MCInst.h, MCInstrDesc.h, MCRegisterInfo.h, cs_priv.h, utils.h, M680XDisassembler.h, M680XDisassemblerInternals.h, M680XInstPrinter.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `arch/X86/X86GenDisassemblerTables.inc` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.527)
- **Top Global Matches:** file_cluster_2: 4.527, file_cluster_17: 6.332, file_cluster_15: 7.394
- **Magnitude:** 1807.7 | **LOC:** 112962 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.247; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000446
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `arch/Mips/MipsDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.263)
- **Top Global Matches:** file_cluster_16: 6.263, file_cluster_4: 8.546, file_cluster_15: 8.863
- **Magnitude:** 1802.44 | **LOC:** 3432 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 0.265; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.0%), Complexity Load (formerly Cognitive Load) (49.8%)
- **Documentation Coverage:** 97.541% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getInstruction` **(Many-Argument Workhorses)** (Impact: 157.3)
  * `Mips_getFeatureBits` **(Compute Cores)** (Impact: 93.7)
    * *Intent:* #define GET_SUBTARGETINFO_ENUM #include "MipsGenSubtargetInfo.inc" #define GET_INSTRINFO_ENUM #inclu...
  * `DecodeMemMMImm4` **(Many-Argument Workhorses)** (Impact: 60.9)
  * `DecodeINSVE_DF` **(Many-Argument Workhorses)** (Impact: 31.3)
  * `DecodeMSA128Mem` **(Many-Argument Workhorses)** (Impact: 26.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 155 instances
* *State Mutation (weighted view):* 506
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 629`, `args: 802`, `func_start: 120`
* *Risk/State:* `state_mutation: 196`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 17`
* *Defense:* `safety: 6`, `doc: 8`, `immutability_locks: 252`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001384
  * `Imports (Out-Degree: 12):` MCDisassembler.h, MCFixedLenDisassembler.h, MCInst.h, MCInstPrinter.h, MCRegisterInfo.h, MathExtras.h, cs_priv.h, utils.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `arch/AArch64/AArch64InstPrinter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.303)
- **Top Global Matches:** file_cluster_4: 5.303, file_cluster_15: 9.653, file_cluster_16: 10.329
- **Magnitude:** 1766.82 | **LOC:** 2600 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.9%), Guard Balance (formerly Safety Score) (61.2%)
- **Documentation Coverage:** 98.2301% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printInst` **(Many-Argument Workhorses)** (Impact: 403.3)
  * `getNextVectorRegister` **(Many-Argument Workhorses)** (Impact: 159.9)
  * `printVectorList` **(Many-Argument Workhorses)** (Impact: 93.9)
  * `printSysAlias` **(Many-Argument Workhorses)** (Impact: 93.7)
  * `printMemExtendImpl` **(Stateful Encapsulated Methods)** (Impact: 27.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 174 instances
* *State Mutation (weighted view):* 530
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 458`, `structural_boundaries: 331`, `args: 849`, `func_start: 55`
* *Risk/State:* `state_mutation: 182`, `fragile_debt: 4`, `unreferenced_by_name: 39`
* *Architecture:* `api: 50`, `import: 18`
* *Defense:* `doc: 3`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000396
  * `Imports (Out-Degree: 23):` MCInst.h, MCInstPrinter.h, MCRegisterInfo.h, Mapping.h, SStream.h, utils.h, AArch64AddressingModes.h, AArch64BaseInfo.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `arch/ARM/ARMMapping.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.175)
- **Top Global Matches:** file_cluster_4: 6.175, file_cluster_6: 7.202, file_cluster_16: 13.881
- **Magnitude:** 1717.72 | **LOC:** 2268 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **20**; blast radius 0.263; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.6%), Complexity Load (formerly Cognitive Load) (46.4%)
- **Documentation Coverage:** 54.878% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_cs_detail_general` **(Many-Argument Workhorses)** (Impact: 398.8)
    * *Intent:* /// Fills cs_detail with the data of the operand. /// This function handles operands which's origina...
  * `ARM_add_not_defined_ops` **(Compute Cores)** (Impact: 233.8)
    * *Intent:* /// Some instructions have their operands not defined but /// hardcoded as string. /// Here we add t...
  * `add_cs_detail_template_1` **(Many-Argument Workhorses)** (Impact: 98.9)
    * *Intent:* /// Fills cs_detail with the data of the operand. /// This function handles operands which original ...
  * `ARM_add_cs_detail` **(Many-Argument Workhorses)** (Impact: 65.9)
    * *Intent:* /// Fills cs_detail with the data of the operand. /// Calls to this function are should not be added...
  * `ARM_reg_access` **(Many-Argument Workhorses)** (Impact: 44.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 121 instances
* *State Mutation (weighted view):* 377
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 588`, `structural_boundaries: 374`, `args: 581`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 135`, `unreferenced_by_name: 13`
* *Architecture:* `api: 31`, `import: 20`
* *Defense:* `safety: 7`, `doc: 64`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000595
  * `Imports (Out-Degree: 21):` MCDisassembler.h, Mapping.h, cs_priv.h, cs_simple_types.h, ARMAddressingModes.h, ARMBaseInfo.h, ARMDisassemblerExtension.h, ARMGenCSAliasMnemMap.inc...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `arch/X86/X86Disassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.678)
- **Top Global Matches:** file_cluster_8: 6.678, file_cluster_6: 17.299, file_cluster_3: 19.889
- **Magnitude:** 1615.4 | **LOC:** 1406 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.8%)
- **Documentation Coverage:** 29.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `translateImmediate` **(Many-Argument Workhorses)** (Impact: 552.2)
    * *Intent:* /// translateImmediate - Appends an immediate operand to an MCInst. /// /// @param mcInst - The MCIn...
  * `translateRMMemory` **(Many-Argument Workhorses)** (Impact: 71.4)
    * *Intent:* /// translateRMMemory - Translates a memory operand stored in the Mod and R/M /// fields of an inter...
  * `X86_getInstruction` **(Many-Argument Workhorses)** (Impact: 55.3)
    * *Intent:* // Public interface for the disassembler
  * `translateOperand` **(Many-Argument Workhorses)** (Impact: 46.6)
    * *Intent:* /// translateOperand - Translates an operand stored in an internal instruction /// to LLVM's format ...
  * `translateRM` **(Stateful Encapsulated Methods)** (Impact: 41.4)
    * *Intent:* /// translateRM - Translates an operand stored in the R/M (and possibly SIB) /// byte of an instruct...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 241 instances
* *State Mutation (weighted view):* 731
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 362`, `structural_boundaries: 291`, `args: 17`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `state_mutation: 249`, `dead_code: 18`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 14`
* *Defense:* `safety: 1`, `doc: 59`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000297
  * `Imports (Out-Degree: 14):` MCInst.h, cs_priv.h, utils.h, Availability.h, X86BaseInfo.h, X86Disassembler.h, X86DisassemblerDecoder.h, X86DisassemblerDecoderCommon.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bindings/ocaml/ocaml.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.554)
- **Top Global Matches:** file_cluster_8: 6.554, file_cluster_6: 11.33, file_cluster_4: 19.784
- **Magnitude:** 1540.66 | **LOC:** 2132 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.226; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.2%)
- **Documentation Coverage:** 83.92% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_cs_disasm` **(Many-Argument Workhorses)** (Impact: 428.8)
  * `ocaml_cs_disasm` **(Many-Argument Workhorses)** (Impact: 117.9)
  * `ocaml_open` **(Many-Argument Workhorses)** (Impact: 85.3)
  * `ocaml_option` **(Compute Cores)** (Impact: 19.7)
  * `list_count` **(Stateful Encapsulated Methods)** (Impact: 5.7)
    * *Intent:* /* By Nguyen Anh Quynh <aquynh@gmail.com>, 2013> */ #include <stdio.h> // debug #include <string.h> ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 269 instances
* *State Mutation (weighted view):* 815
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 158`, `args: 20`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 277`, `dead_code: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` alloc.h, fail.h, memory.h, mlvalues.h, capstone.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/AArch64/AArch64Disassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.869)
- **Top Global Matches:** file_cluster_4: 6.869, file_cluster_16: 9.836, file_cluster_15: 11.69
- **Magnitude:** 1516.68 | **LOC:** 2218 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.4%), Complexity Load (formerly Cognitive Load) (26.3%), Debt Markers (formerly Tech Debt) (8.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DecodeSignedLdStInstruction` **(Many-Argument Workhorses)** (Impact: 352.0)
  * `DecodePairLdStInstruction` **(Many-Argument Workhorses)** (Impact: 190.1)
  * `DecodeExclusiveLdStInstruction` **(Many-Argument Workhorses)** (Impact: 111.5)
  * `DecodeThreeAddrSRegInstruction` **(Many-Argument Workhorses)** (Impact: 70.2)
  * `DecodeUnsignedLdStInstruction` **(Many-Argument Workhorses)** (Impact: 63.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 503`, `structural_boundaries: 408`, `args: 431`, `func_start: 90`
* *Risk/State:* `state_mutation: 22`, `dead_code: 8`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 19`
* *Defense:* `safety: 2`, `immutability_locks: 181`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000535
  * `Imports (Out-Degree: 17):` LEB128.h, MCDisassembler.h, MCFixedLenDisassembler.h, MCInst.h, MCInstrDesc.h, MCRegisterInfo.h, cs_priv.h, utils.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bindings/vb6/CX86Operand.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 4.068)
- **Top Global Matches:** file_cluster_7: 4.068, file_cluster_12: 7.631, file_cluster_5: 8.528
- **Magnitude:** 1260.08 | **LOC:** 203 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.2%), Complexity Load (formerly Cognitive Load) (69.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 1`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 28`
* *Architecture:* None
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/X86/X86Mapping.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.323)
- **Top Global Matches:** file_cluster_6: 6.323, file_cluster_4: 7.329, file_cluster_15: 15.214
- **Magnitude:** 1175.24 | **LOC:** 2482 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **19**; blast radius 0.442; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.8%)
- **Documentation Coverage:** 96.875% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `X86_get_insn_id` **(Many-Argument Workhorses)** (Impact: 265.6)
    * *Intent:* // given internal insn id, return public instruction info
  * `valid_repne` **(Compute Cores)** (Impact: 67.4)
    * *Intent:* // given MCInst's id, find out if this insn is valid for REPNE prefix
  * `X86_lockrep` **(Compute Cores)** (Impact: 58.6)
    * *Intent:* #endif // return true if we patch the mnemonic
  * `valid_bnd` **(Compute Cores)** (Impact: 50.6)
    * *Intent:* // given MCInst's id, find out if this insn is valid for BND prefix // BND prefix is valid for CALL/...
  * `valid_rep` **(Compute Cores)** (Impact: 46.0)
    * *Intent:* #endif // given MCInst's id, find out if this insn is valid for REP prefix
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 103 instances
* *State Mutation (weighted view):* 316
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 348`, `structural_boundaries: 233`, `args: 63`, `func_start: 37`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 110`, `dead_code: 1`, `unreferenced_by_name: 26`
* *Architecture:* `api: 30`, `import: 19`
* *Defense:* `doc: 4`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.442
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.002115
  * `Imports (Out-Degree: 18):` MCInstPrinter.h, Mapping.h, utils.h, Availability.h, X86DisassemblerDecoder.h, X86GenInstrInfo.inc, X86GenInstrInfo_reduce.inc, X86GenRegisterInfo.inc...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `arch/WASM/WASMDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.972)
- **Top Global Matches:** file_cluster_4: 5.972, file_cluster_16: 9.901, file_cluster_6: 11.114
- **Magnitude:** 1098.0 | **LOC:** 1066 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.226; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WASM_getInstruction` **(Many-Argument Workhorses)** (Impact: 611.9)
  * `read_brtable` **(Many-Argument Workhorses)** (Impact: 25.8)
    * *Intent:* // input | code : code pointer start from brtable // | code_len : start from the code pointer to the...
  * `read_memoryimmediate` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* // input | code : code pointer start from memoryimmediate // | code_len : start from the code pointe...
  * `get_varuint64` **(Stateful Encapsulated Methods)** (Impact: 15.4)
    * *Intent:* // input | code : code pointer start from varuint64 // | code_len : real code len count from varint ...
  * `get_varuint32` **(Stateful Encapsulated Methods)** (Impact: 15.3)
    * *Intent:* // input | code: code pointer start from varuint32 // | code_len: real code len count from varint //...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 101`, `args: 14`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 133`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 19`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` cs_priv.h, WASMDisassembler.h, WASMMapping.h, stddef.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/TriCore/TriCoreDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.242)
- **Top Global Matches:** file_cluster_6: 7.242, file_cluster_4: 7.306, file_cluster_16: 14.055
- **Magnitude:** 1083.86 | **LOC:** 1752 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **18**; blast radius 0.306; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.4%), Complexity Load (formerly Cognitive Load) (32.4%)
- **Documentation Coverage:** 98.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DecodeBOInstruction` **(Many-Argument Workhorses)** (Impact: 88.0)
  * `DecodeRRInstruction` **(Many-Argument Workhorses)** (Impact: 52.8)
  * `DecodeSROInstruction` **(Many-Argument Workhorses)** (Impact: 49.4)
  * `DecodeBOLInstruction` **(Many-Argument Workhorses)** (Impact: 45.5)
  * `DecodeSRRInstruction` **(Many-Argument Workhorses)** (Impact: 40.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 299`, `args: 427`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `state_mutation: 80`, `dead_code: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 19`
* *Defense:* `safety: 3`, `doc: 3`, `immutability_locks: 124`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.306
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.001293
  * `Imports (Out-Degree: 14):` MCDisassembler.h, MCFixedLenDisassembler.h, MCInst.h, MCInstrDesc.h, MCRegisterInfo.h, MathExtras.h, cs_priv.h, utils.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `arch/X86/X86GenAsmWriter.inc` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.551)
- **Top Global Matches:** file_cluster_2: 6.551, file_cluster_17: 7.827, file_cluster_15: 7.829
- **Magnitude:** 988.56 | **LOC:** 49200 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.238; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Mutation Surface (formerly State Flux) (8.3%), Complexity Load (formerly Cognitive Load) (4.9%), Dead Code Surface (formerly Dead Code) (4.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printInstruction` **(Many-Argument Workhorses)** (Impact: 3.7)
    * *Intent:* \*===----------------------------------------------------------------------===*/ /// printInstructio...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 386`, `args: 578`, `func_start: 1`
* *Risk/State:* `state_mutation: 3`, `dead_code: 10`
* *Architecture:* `api: 1`
* *Defense:* `doc: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000297
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `suite/auto-sync/src/autosync/cpptranslator/Differ.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.242)
- **Top Global Matches:** file_cluster_4: 7.242, file_cluster_9: 10.123, file_cluster_15: 10.342
- **Magnitude:** 948.32 | **LOC:** 1009 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **14**; blast radius 0.298; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.4%), Complexity Load (formerly Cognitive Load) (69.9%)
- **Documentation Coverage:** 40.4762% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `diff_nodes` **(Many-Argument Workhorses)** (Impact: 92.6)
  * `all_choices_saved` **(Many-Argument Workhorses)** (Impact: 31.1)
  * `determine_patch_coordinates` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `get_user_choice` **(Compute Cores)** (Impact: 29.7)
  * `patch_files` **(Compute Cores)** (Impact: 29.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 128 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 438
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 149`, `args: 39`, `func_start: 35`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 182`
* *Architecture:* `io: 8`, `api: 32`, `import: 14`
* *Defense:* `safety: 7`, `doc: 10`, `test: 19`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.298
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000595
  * `Imports (Out-Degree: 3):` argparse, autosync.Helper, autosync.Targets, autosync.cpptranslator.Configurator, difflib, enum, json, logging...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `arch/X86/X86ATTInstPrinter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.604)
- **Top Global Matches:** file_cluster_4: 7.604, file_cluster_6: 7.735, file_cluster_16: 13.67
- **Magnitude:** 900.86 | **LOC:** 1204 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.226; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Debt Markers (formerly Tech Debt) (89.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.2%)
- **Documentation Coverage:** 97.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `X86_ATT_printInst` **(Many-Argument Workhorses)** (Impact: 173.9)
  * `printOperand` **(Many-Argument Workhorses)** (Impact: 128.0)
  * `printopaquemem` **(Many-Argument Workhorses)** (Impact: 64.8)
  * `printMemReference` **(Many-Argument Workhorses)** (Impact: 55.9)
  * `_printOperand` **(Stateful Encapsulated Methods)** (Impact: 38.2)
    * *Intent:* // local printOperand, without updating public operands
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 208
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 91`, `args: 184`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `state_mutation: 98`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `api: 1`, `import: 21`
* *Defense:* `safety: 1`, `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` MCInst.h, MCRegisterInfo.h, SStream.h, utils.h, Availability.h, X86BaseInfo.h, X86GenAsmWriter.inc, X86GenAsmWriter_reduce.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `suite/auto-sync/src/autosync/IncGenerator.py` (PYTHON) | Magnitude: 131.76 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 28, branch: 27, state_mutation: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/integration/test_poc.c` (C) | Magnitude: 17.7 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 41, pointers: 19, structural_boundaries: 14, safety: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `bindings/java/capstone/Sparc.java` (JAVA) | Magnitude: 53.72 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 26, api: 26, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `arch/Mips/MipsMapping.c` (C) | Magnitude: 336.5 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 280, args: 151, pointers: 118, branch: 93
- `MCInst.h` (C) | Magnitude: 48.64 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: pointers: 50, structural_boundaries: 45, api: 45, indent_tabs: 44
- `arch/Alpha/AlphaInstPrinter.c` (C) | Magnitude: 36.88 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 31, args: 25, pointers: 18, import: 12
- `arch/Alpha/AlphaDisassembler.c` (C) | Magnitude: 42.18 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 35, pointers: 21, structural_boundaries: 18, args: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `arch/SystemZ/SystemZMCTargetDesc.c` (C) | Magnitude: 16.12 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 60, scientific: 24, globals: 14, immutability_locks: 12
- `utils.h` (C) | Magnitude: 24.72 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: pointers: 38, args: 20, api: 19, immutability_locks: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `arch/X86/X86ATTInstPrinter.c` (C) | Magnitude: 900.86 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 798, pointers: 753, branch: 270, args: 184

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `arch/TriCore/TriCoreDisassembler.c` (C) | Magnitude: 1083.86 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1030, args: 427, pointers: 424, structural_boundaries: 299
- `cs.c` (C) | Magnitude: 1856.42 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1179, pointers: 578, branch: 341, structural_boundaries: 327

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `suite/cstest/src/test_detail_sparc.c` (C) | Magnitude: 128.58 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 112, indent_tabs: 96, structural_boundaries: 33, branch: 29

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `arch/RISCV/RISCVMapping.c` -> Churn: **100.0%** | Cog Load: 61.7904% | Debt: 69.3156%
- `cs.c` -> Churn: **87.7%** | Cog Load: 90.2405% | Debt: 71.0905%
- `Mapping.c` -> Churn: **66.67%** | Cog Load: 36.1479% | Debt: 99.3048%
- `arch/RISCV/RISCVInstPrinter.c` -> Churn: **66.67%** | Cog Load: 23.2421% | Debt: 99.1845%
- `suite/cstest/src/helper.c` -> Churn: **52.83%** | Cog Load: 52.9191% | Debt: 56.9001%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `arch/ARM/ARMDisassembler.c` -> **billow** (100.0% isolated ownership) | Magnitude: 6136.32
- `arch/RISCV/RISCVGenCompressedInstructionsInfo.inc` -> **مصطفي محمود كمال الدين** (100.0% isolated ownership) | Magnitude: 3328.06
- `arch/M68K/M68KDisassembler.c` -> **Carsten Elton Sørensen** (100.0% isolated ownership) | Magnitude: 2542.16
- `arch/AArch64/AArch64Mapping.c` -> **Rot127** (100.0% isolated ownership) | Magnitude: 2535.3
- `arch/X86/X86DisassemblerDecoder.c` -> **Jos** (100.0% isolated ownership) | Magnitude: 2227.92

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `include/capstone/capstone.h` -> **Severity: 0.027** (Bridge: 0.0006 * Flux: 43.3485%)
- `cs.c` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 100.0%)
- `MCInst.c` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9996%)
- `Mapping.c` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9993%)
- `utils.c` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `include/capstone/capstone.h` -> **Severity: 2.751** (Embedded: 0.0614 * Error Risk: 44.7885%)
- `include/capstone/cs_operand.h` -> **Severity: 2.201** (Embedded: 0.043 * Error Risk: 51.1427%)
- `include/capstone/aarch64.h` -> **Severity: 1.931** (Embedded: 0.0386 * Error Risk: 50.0521%)
- `include/capstone/ppc.h` -> **Severity: 1.916** (Embedded: 0.0381 * Error Risk: 50.3218%)
- `include/capstone/arm64.h` -> **Severity: 1.888** (Embedded: 0.0376 * Error Risk: 50.208%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `suite/auto-sync/src/autosync/Helper.py` -> **Severity: 1033.92** (Blast Radius: 12.924 * Doc Risk: 80.0%)
- `suite/auto-sync/src/autosync/PathVarHandler.py` -> **Severity: 1027.1** (Blast Radius: 10.271 * Doc Risk: 100.0%)
- `utils.h` -> **Severity: 652.65** (Blast Radius: 13.053 * Doc Risk: 50.0%)
- `MCInst.h` -> **Severity: 423.75** (Blast Radius: 8.475 * Doc Risk: 50.0%)
- `suite/auto-sync/src/autosync/cpptranslator/patches/Helper.py` -> **Severity: 321.818** (Blast Radius: 7.08 * Doc Risk: 45.4545%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1176 literal sites + 2 sites through wrappers = 1178
- **`memory_alloc`:** 57 literal sites + 9 sites through wrappers = 66
- **`panics_and_aborts`:** 270 literal sites + 13 sites through wrappers = 283

- `fail_exit` (function, panics_and_aborts, primitive): 10 call sites in 5 files -- `suite/auto-sync/src/autosync/Helper.py`
- `str_append` (function, memory_alloc, primitive): 9 call sites in 2 files -- `utils.c`
- `error_exit` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `suite/auto-sync/src/autosync/HeaderPatcher.py`
- `help` (function, debug_prints, primitive): 1 call sites in 1 files -- `suite/cstest/src/cstest.c`
- `print_objdump_dumpheader` (function, debug_prints, primitive): 1 call sites in 1 files -- `contrib/objdump/objdump-m68k.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 11744 call pairs -- scoped 33.5%, unique 31.6%, ambiguous 1.9%, external 33.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 9643 | 32.8% | 37.7% | 2.1% | 27.4% |
| python | 1517 | 41.9% | 0.0% | 1.1% | 57.0% |
| java | 335 | 31.0% | 0.0% | 2.1% | 66.9% |
| cpp | 174 | 19.0% | 42.5% | 0.0% | 38.5% |
| shell | 42 | 0.0% | 0.0% | 0.0% | 100.0% |
| ruby | 14 | 0.0% | 0.0% | 0.0% | 100.0% |
| powershell | 13 | 0.0% | 0.0% | 0.0% | 100.0% |
| makefile | 6 | 0.0% | 0.0% | 0.0% | 100.0% |

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
