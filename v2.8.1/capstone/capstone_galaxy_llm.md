# ARCHITECTURAL_BRIEF: capstone
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/capstone-engine/capstone.git` |
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
| Total Artifacts | 3963 |
| Analyzed Artifacts (Scanned) | 2035 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1928 |
| Total LOC | 208636 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 51.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5766 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3329 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3383 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 36 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 906 | 16565 | 44.5% |
| YAML | 471 | 12898 | 23.1% |
| C | 413 | 161614 | 20.3% |
| PYTHON | 127 | 11132 | 6.2% |
| MARKDOWN | 35 | 0 | 1.7% |
| JAVA | 19 | 2149 | 0.9% |
| PLAINTEXT | 18 | 0 | 0.9% |
| MAKEFILE | 10 | 959 | 0.5% |
| SHELL | 8 | 312 | 0.4% |
| JSON | 7 | 947 | 0.3% |
| APEX | 6 | 669 | 0.3% |
| CPP | 5 | 370 | 0.2% |
| POWERSHELL | 3 | 369 | 0.1% |
| M4 | 3 | 33 | 0.1% |
| BATCH | 2 | 232 | 0.1% |
| RUBY | 1 | 387 | 0.0% |
| XML | 1 | 0 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z -0.55; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 46%, Declarative / Non-Code 36%, Large Core Modules 4%, Generic / Templated Code Files 3%, Interface Declarations Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1978 | 97.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 57 | 2.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1928*

**Composition by Extension & Reason:**
- `.yaml`: 132x Zero-Density Threshold (LOC: 109, Signals: 0), 131x Zero-Density Threshold (LOC: 73, Signals: 0), 115x Zero-Density Threshold (LOC: 145, Signals: 0)
- `.cs`: 10x Zero-Density Threshold (LOC: 169, Signals: 0), 10x Zero-Density Threshold (LOC: 57, Signals: 0), 10x Zero-Density Threshold (LOC: 65, Signals: 0)
- `.inc`: 3x Excluded (Machine-Generated Source Code Signature: 120 LOC), 2x Excluded (Embedded Array/Matrix Payload: 17385 commas in 5380 LOC), 2x Excluded (Machine-Generated Source Code Signature: 205 LOC)
- `.ml`: 35x Excluded (Unsupported Extension: '.ml')
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 338 LOC), 1x Excluded (Machine-Generated Source Code Signature: 4316 LOC)
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.xcworkspacedata')
- `.java`: 1x Excluded (Saturation: Line 40 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 3011 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1333 LOC)
- `.patch`: 15x Excluded (Unsupported Extension: '.patch')
- `.yml`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 125 LOC), 1x Excluded (Machine-Generated Source Code Signature: 96 LOC)
- `.cmake`: 10x Excluded (Unsupported Extension: '.cmake')
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 352 LOC), 1x Excluded (Machine-Generated Source Code Signature: 62 LOC), 1x Excluded (Machine-Generated Source Code Signature: 55 LOC)
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 113 LOC), 1x Excluded (Machine-Generated Source Code Signature: 142 LOC), 1x Excluded (Machine-Generated Source Code Signature: 518 LOC)
- `.xcscheme`: 4x Excluded (Unsupported Extension: '.xcscheme')
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.6 | 13.5 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 12.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 97.6 | 0.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 22.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.0 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 16.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 22805 | 366 | 13 | `arch/M68K/M68KDisassembler.c` |
| cleanup | 72 | 25 | 0 | `suite/cstest/src/helper.c` |
| guards | 7385 | 408 | 4 | `arch/ARM/ARMDisassembler.c` |
| danger | 568 | 132 | 0 | `arch/X86/X86DisassemblerDecoder.c` |
| concurrency | 48 | 8 | 0 | `suite/run_invalid_cstool.sh` |
| connectivity | 4144 | 518 | 5 | `bindings/java/capstone/Capstone.java` |
| io | 359 | 44 | 0 | `Makefile` |
| crypto | 1 | 1 | 0 | `suite/auto-sync/src/autosync/Helper.py` |
| ipc | 35 | 13 | 0 | `Makefile` |
| time | 4 | 2 | 0 | `arch/X86/X86MappingInsnName.inc` |
| serialization | 0 | 0 | 0 | - |
| regex | 106 | 22 | 0 | `suite/auto-sync/src/autosync/MCUpdater.py` |
| events | 48 | 12 | 0 | `arch/M680X/M680XDisassembler.c` |
| tests | 391 | 19 | 0 | `suite/auto-sync/src/autosync/cpptranslator/Tests/test_patches.py` |
| docs | 2836 | 189 | 0 | `include/capstone/capstone.h` |
| debt | 1273 | 145 | 0 | `cstool/cstool_aarch64.c` |
| mutation | 27854 | 461 | 14 | `include/capstone/arm64.h` |
| dead_code | 1621 | 262 | 1 | `arch/M68K/M68KDisassembler.c` |
| credential | 3 | 3 | 0 | `suite/auto-sync/src/autosync/cpptranslator/arch_config.json` |
| threat | 682 | 110 | 0 | `arch/M68K/M68KDisassembler.c` |
| ml_ai | 306 | 87 | 0 | `arch/SystemZ/SystemZMCTargetDesc.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Makefile` (Hits: 68)
- `suite/run_invalid_cstool.sh` (Hits: 52)
- `bindings/python/setup.py` (Hits: 48)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **capstone.h** (`include/capstone/capstone.h`) — 166 inbound connections
2. **utils.h** (`utils.h`) — 102 inbound connections
3. **MCInst.h** (`MCInst.h`) — 73 inbound connections
4. **Patch.py** (`suite/auto-sync/src/autosync/cpptranslator/patches/Patch.py`) — 66 inbound connections
5. **MCRegisterInfo.h** (`MCRegisterInfo.h`) — 65 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CppTranslator.py** (`suite/auto-sync/src/autosync/cpptranslator/CppTranslator.py`) — 77 outbound dependencies
2. **test_patches.py** (`suite/auto-sync/src/autosync/cpptranslator/Tests/test_patches.py`) — 72 outbound dependencies
3. **cs.c** (`cs.c`) — 35 outbound dependencies
4. **capstone.h** (`include/capstone/capstone.h`) — 31 outbound dependencies
5. **test_detail.h** (`suite/cstest/include/test_detail.h`) — 26 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `WASM_getInstruction` **(Many-Argument Workhorses)** (@ `arch/WASM/WASMDisassembler.c`) -> Impact: **611.9** | LOC: 416
- `translateImmediate` **(Many-Argument Workhorses)** (@ `arch/X86/X86Disassembler.c`) -> Impact: **552.2** | LOC: 669
  * *Intent:* /// translateImmediate - Appends an immediate operand to an MCInst. /// /// @param mcInst - The MCInst to append to. /// @param immediate - The immedi...
- `DecodeVLDInstruction` **(Many-Argument Workhorses)** (@ `arch/ARM/ARMDisassembler.c`) -> Impact: **491.2** | LOC: 299
- `DecodeVSTInstruction` **(Many-Argument Workhorses)** (@ `arch/ARM/ARMDisassembler.c`) -> Impact: **474.7** | LOC: 281
- `_cs_disasm` **(Many-Argument Workhorses)** (@ `bindings/ocaml/ocaml.c`) -> Impact: **428.8** | LOC: 1697
- `printInst` **(Many-Argument Workhorses)** (@ `arch/AArch64/AArch64InstPrinter.c`) -> Impact: **403.3** | LOC: 508
- `add_cs_detail_general` **(Many-Argument Workhorses)** (@ `arch/ARM/ARMMapping.c`) -> Impact: **398.8** | LOC: 736
  * *Intent:* /// Fills cs_detail with the data of the operand. /// This function handles operands which's original printer function has no /// specialities.
- `DecodeSignedLdStInstruction` **(Many-Argument Workhorses)** (@ `arch/AArch64/AArch64Disassembler.c`) -> Impact: **352.0** | LOC: 198
- `DecodeCopMemInstruction` **(Many-Argument Workhorses)** (@ `arch/ARM/ARMDisassembler.c`) -> Impact: **328.7** | LOC: 179
- `DecodeAddrMode3Instruction` **(Many-Argument Workhorses)** (@ `arch/ARM/ARMDisassembler.c`) -> Impact: **305.0** | LOC: 197

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `arch/ARM` | 14 | 9718.62 | 24.22% | 30.57% |
| `arch/AArch64` | 12 | 7176.38 | 23.5% | 24.23% |
| `arch/X86` | 21 | 6960.28 | 16.31% | 14.08% |
| `__monolith__` | 41 | 5743.58 | 14.86% | 17.96% |
| `suite/MC/AArch64` | 355 | 5156.28 | 0.71% | 0.0% |
| `suite/cstest/src` | 28 | 4182.28 | 64.27% | 55.14% |
| `bindings/vb6` | 9 | 4169.1 | 30.93% | 11.11% |
| `arch/HPPA` | 9 | 3702.7 | 9.3% | 14.82% |
| `arch/M68K` | 6 | 2947.0 | 30.56% | 36.39% |
| `arch/Mips` | 10 | 2782.52 | 17.54% | 13.16% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `bindings/vb6/vbCapstone.cpp` -> **100.0%** Exposure
- `arch/ARM/ARMDisassemblerExtension.c` -> **99.9968%** Exposure
- `MCInst.c` -> **99.9918%** Exposure
- `MCInstrDesc.c` -> **99.9797%** Exposure
- `arch/SystemZ/SystemZDisassembler.c` -> **99.9512%** Exposure
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
- **Binary Anomalies (X-Ray):** `53` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2147` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `arch/RISCV/RISCVMapping.c` (C) -> Cumulative Risk: **711.98**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.21)
- **Magnitude:** 320.44 | **LOC:** 448 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 42.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Documentation (100.0%), State Flux (99.9928%)
- **Heaviest Functions:** `RISCV_add_cs_detail_0` (Many-Argument Workhorses, Impact: 58.5), `RISCV_add_ret_group` (Compute Cores, Impact: 24.2), `RISCV_add_privileged_group` (Compute Cores, Impact: 12.6)

### 2. `arch/M68K/M68KDisassembler.c` (C) -> Cumulative Risk: **691.86**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.02)
- **Magnitude:** 2542.16 | **LOC:** 3946 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9996%), Tech Debt (99.9299%), Documentation (99.7319%)
- **Heaviest Functions:** `get_ea_mode_op` (Many-Argument Workhorses, Impact: 163.8), `d68020_cpgen` (Compute Cores, Impact: 106.3), `get_with_index_address_mode` (Many-Argument Workhorses, Impact: 91.5)

### 3. `bindings/java/capstone/Capstone.java` (JAVA) -> Cumulative Risk: **673.18**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.75)
- **Magnitude:** 504.82 | **LOC:** 550 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), State Flux (99.9902%), Documentation (95.5556%)
- **Heaviest Functions:** `getOptInfo` (Compute Cores, Impact: 33.8), `CsInsn` (Many-Argument Workhorses, Impact: 23.8), `Capstone` (Compute Cores, Impact: 7.9)

### 4. `arch/Xtensa/XtensaMapping.c` (C) -> Cumulative Risk: **655.61**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.41)
- **Magnitude:** 278.56 | **LOC:** 278 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9921%), Cognitive Load (90.7905%)
- **Heaviest Functions:** `Xtensa_add_cs_detail_0` (Compute Cores, Impact: 106.5), `Xtensa_reg_access` (Many-Argument Workhorses, Impact: 39.5), `Xtensa_L32R_Value` (Compute Cores, Impact: 9.3)

### 5. `arch/AArch64/AArch64InstPrinter.c` (C) -> Cumulative Risk: **648.8**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.06)
- **Magnitude:** 1782.82 | **LOC:** 2600 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8785%), Documentation (98.2301%), Safety Score (80.5858%)
- **Heaviest Functions:** `printInst` (Many-Argument Workhorses, Impact: 403.3), `getNextVectorRegister` (Compute Cores, Impact: 159.9), `printVectorList` (Many-Argument Workhorses, Impact: 93.9)

### 6. `arch/X86/X86ATTInstPrinter.c` (C) -> Cumulative Risk: **645.59**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Encapsulated Accessors Files` (z +0.08)
- **Magnitude:** 900.86 | **LOC:** 1204 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.6962%), Documentation (97.5%), Tech Debt (90.3645%)
- **Heaviest Functions:** `X86_ATT_printInst` (Many-Argument Workhorses, Impact: 173.9), `printOperand` (Many-Argument Workhorses, Impact: 128.0), `printopaquemem` (Compute Cores, Impact: 64.8)

### 7. `suite/cstest/src/helper.c` (C) -> Cumulative Risk: **642.01**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.04)
- **Magnitude:** 248.1 | **LOC:** 217 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.2355%), Documentation (85.7143%)
- **Heaviest Functions:** `replace_negative` (Many-Argument Workhorses, Impact: 27.4), `replace_hex` (Many-Argument Workhorses, Impact: 25.1), `trim_str` (Compute Cores, Impact: 9.5)

### 8. `arch/ARM/ARMDisassemblerExtension.c` (C) -> Cumulative Risk: **629.79**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.28)
- **Magnitude:** 190.12 | **LOC:** 220 | **CtrlFlow:** 44.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9968%), State Flux (99.8035%), Documentation (93.75%)
- **Heaviest Functions:** `ARM_getFeatureBits` (Compute Cores, Impact: 48.9), `isVPTOpcode` (Compute Cores, Impact: 33.3), `isValidCoprocessorNumber` (Compute Cores, Impact: 11.4)

### 9. `arch/X86/X86IntelInstPrinter.c` (C) -> Cumulative Risk: **627.69**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Encapsulated Accessors Files` (z +0.35)
- **Magnitude:** 862.3 | **LOC:** 1274 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7155%), Documentation (97.619%), Tech Debt (88.9273%)
- **Heaviest Functions:** `printImm` (Many-Argument Workhorses, Impact: 124.2), `printOperand` (Many-Argument Workhorses, Impact: 95.5), `printopaquemem` (Compute Cores, Impact: 85.8)

### 10. `bindings/python/cstest_py/src/cstest_py/cstest.py` (PYTHON) -> Cumulative Risk: **624.49**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.20)
- **Magnitude:** 386.98 | **LOC:** 489 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Safety Score (87.6872%)
- **Heaviest Functions:** `compare` (Many-Argument Workhorses, Impact: 28.3), `__init__` (Many-Argument Workhorses, Impact: 21.2), `setup` (Compute Cores, Impact: 17.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `arch/ARM/ARMDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 6158.32 | **LOC:** 7307 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (62.2957%), Tech Debt (8.11%)
**Top Internal Functions/Classes:**
  * `DecodeVLDInstruction` **(Many-Argument Workhorses)** (Impact: 491.2)
  * `DecodeVSTInstruction` **(Many-Argument Workhorses)** (Impact: 474.7)
  * `DecodeCopMemInstruction` **(Many-Argument Workhorses)** (Impact: 328.7)
  * `DecodeAddrMode3Instruction` **(Many-Argument Workhorses)** (Impact: 305.0)
  * `DecodeMSRMask` **(Many-Argument Workhorses)** (Impact: 139.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 318 instances
* *State Mutation (weighted view):* 995
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2005`, `structural_boundaries: 1414`, `args: 1773`, `func_start: 178`, `class_start: 1`
* *Risk/State:* `state_mutation: 359`, `dead_code: 6`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 23`
* *Defense:* `safety: 4`, `doc: 21`, `immutability_locks: 389`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` LEB128.h, MCDisassembler.h, MCFixedLenDisassembler.h, MCInst.h, MCInstrDesc.h, MCRegisterInfo.h, MathExtras.h, cs_priv.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/HPPA/HPPADisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3193.32 | **LOC:** 3841 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.8706%), Tech Debt (7.8765%)
**Top Internal Functions/Classes:**
  * `fill_alu_mods` **(Many-Argument Workhorses)** (Impact: 179.8)
  * `getInstruction` **(Many-Argument Workhorses)** (Impact: 161.8)
  * `fill_alu_insn_name` **(Compute Cores)** (Impact: 131.2)
  * `decode_alu` **(Compute Cores)** (Impact: 124.3)
  * `fill_copr_mods` **(Many-Argument Workhorses)** (Impact: 122.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1346`, `structural_boundaries: 716`, `args: 765`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 71`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 4`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Mapping.h, MathExtras.h, utils.h, HPPAConstants.h, HPPADisassembler.h, stddef.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/AArch64/AArch64Mapping.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2554.1 | **LOC:** 2910 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.0721%), Tech Debt (17.5364%)
**Top Internal Functions/Classes:**
  * `AArch64_add_cs_detail_1` **(Many-Argument Workhorses)** (Impact: 284.8)
    * *Intent:* /// Fills cs_detail with the data of the operand. /// This function handles operands which original ...
  * `AArch64_add_cs_detail_0` **(Many-Argument Workhorses)** (Impact: 218.6)
    * *Intent:* /// Fills cs_detail with the data of the operand. /// This function handles operands which's origina...
  * `add_non_alias_details` **(Compute Cores)** (Impact: 171.3)
  * `AArch64_add_cs_detail_2` **(Many-Argument Workhorses)** (Impact: 163.5)
    * *Intent:* /// Fills cs_detail with the data of the operand. /// This function handles operands which original ...
  * `AArch64_add_cs_detail_4` **(Many-Argument Workhorses)** (Impact: 105.1)
    * *Intent:* /// Fills cs_detail with the data of the operand. /// This function handles operands which original ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 214 instances
* *State Mutation (weighted view):* 648
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 825`, `structural_boundaries: 386`, `args: 621`, `func_start: 56`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 220`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 12`
* *Architecture:* `api: 32`, `import: 17`
* *Defense:* `safety: 2`, `doc: 60`, `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Mapping.h, MathExtras.h, cs_simple_types.h, utils.h, AArch64AddressingModes.h, AArch64BaseInfo.h, AArch64DisassemblerExtension.h, AArch64GenCSAliasMnemMap.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/M68K/M68KDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2542.16 | **LOC:** 3946 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.2278%), Tech Debt (99.9299%)
**Top Internal Functions/Classes:**
  * `get_ea_mode_op` **(Many-Argument Workhorses)** (Impact: 163.8)
    * *Intent:* /* Make string of effective address mode */
  * `d68020_cpgen` **(Compute Cores)** (Impact: 106.3)
  * `get_with_index_address_mode` **(Many-Argument Workhorses)** (Impact: 91.5)
  * `update_am_reg_list` **(Compute Cores)** (Impact: 35.8)
  * `d68010_movec` **(Compute Cores)** (Impact: 35.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 313 instances
* *State Mutation (weighted view):* 1169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 522`, `args: 440`, `func_start: 372`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 543`, `dead_code: 1`, `unreferenced_by_name: 299`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` MCInst.h, MCInstrDesc.h, MCRegisterInfo.h, MathExtras.h, cs_priv.h, utils.h, M68KDisassembler.h, M68KInstPrinter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/X86/X86DisassemblerDecoder.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2267.42 | **LOC:** 2573 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.7743%), Tech Debt (10.7277%)
**Top Internal Functions/Classes:**
  * `checkPrefix` **(Compute Cores)** (Impact: 240.2)
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
* *Amplified Cascading Flux:* 320 instances
* *State Mutation (weighted view):* 971
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 764`, `structural_boundaries: 362`, `args: 32`, `func_start: 28`, `class_start: 7`
* *Risk/State:* `state_mutation: 331`, `dead_code: 4`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 16`
* *Defense:* `safety: 2`, `doc: 84`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` cs_priv.h, utils.h, X86DisassemblerDecoder.h, X86GenDisassemblerTables.inc, X86GenDisassemblerTables2.inc, X86GenDisassemblerTables_reduce.inc, X86GenDisassemblerTables_reduce2.inc, X86GenInstrInfo.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1927.42 | **LOC:** 2179 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 14.3%
- **Risk Profile:** Cognitive Load (73.0434%), Tech Debt (71.925%)
**Top Internal Functions/Classes:**
  * `cs_op_index` **(Many-Argument Workhorses)** (Impact: 219.7)
  * `cs_op_count` **(Many-Argument Workhorses)** (Impact: 143.8)
  * `cs_disasm` **(Many-Argument Workhorses)** (Impact: 104.3)
    * *Intent:* #endif // dynamically allocate memory to contain disasm insn // NOTE: caller must free() the allocat...
  * `cs_option` **(Many-Argument Workhorses)** (Impact: 67.3)
  * `skipdata_size` **(Compute Cores)** (Impact: 42.0)
    * *Intent:* // how many bytes will we skip when encountering data (CS_OPT_SKIPDATA)? // this very much depends o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 308 instances
* *State Mutation (weighted view):* 933
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 440`, `structural_boundaries: 327`, `args: 150`, `func_start: 46`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 317`, `dead_code: 4`, `fragile_debt: 1`, `unreferenced_by_name: 40`
* *Architecture:* `api: 45`, `import: 35`
* *Defense:* `safety: 31`, `doc: 3`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` Availability.h, MCRegisterInfo.h, Mapping.h, SStream.h, AArch64Module.h, ARCModule.h, ARMModule.h, AlphaModule.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/SH/SHDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1847.46 | **LOC:** 2184 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.3916%), Tech Debt (52.3771%)
**Top Internal Functions/Classes:**
  * `decode_dsp_3op` **(Many-Argument Workhorses)** (Impact: 150.6)
  * `sh_disassemble` **(Many-Argument Workhorses)** (Impact: 75.7)
  * `decode_long` **(Many-Argument Workhorses)** (Impact: 56.2)
    * *Intent:* #include "SHInsnTable.inc"
  * `opfxxd` **(Many-Argument Workhorses)** (Impact: 54.3)
  * `op4xxb` **(Many-Argument Workhorses)** (Impact: 51.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 197 instances
* *State Mutation (weighted view):* 616
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 369`, `structural_boundaries: 363`, `args: 207`, `func_start: 84`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 222`, `unreferenced_by_name: 52`
* *Architecture:* `api: 7`, `import: 9`
* *Defense:* `safety: 1`, `doc: 18`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` MCDisassembler.h, MCInst.h, cs_priv.h, utils.h, SHDisassembler.h, SHInsnTable.inc, sh.h, stdarg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/M680X/M680XDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1813.36 | **LOC:** 2343 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (89.6479%), Tech Debt (20.0025%)
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
* *Structure:* `branch: 364`, `structural_boundaries: 284`, `args: 116`, `func_start: 65`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 315`, `fragile_debt: 6`, `unreferenced_by_name: 4`
* *Architecture:* `api: 12`, `import: 23`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` MCInst.h, MCInstrDesc.h, MCRegisterInfo.h, cs_priv.h, utils.h, M680XDisassembler.h, M680XDisassemblerInternals.h, M680XInstPrinter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/Mips/MipsDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1812.44 | **LOC:** 3432 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.3237%), Tech Debt (8.844%)
**Top Internal Functions/Classes:**
  * `getInstruction` **(Many-Argument Workhorses)** (Impact: 157.3)
  * `Mips_getFeatureBits` **(Compute Cores)** (Impact: 93.7)
    * *Intent:* #define GET_SUBTARGETINFO_ENUM #include "MipsGenSubtargetInfo.inc" #define GET_INSTRINFO_ENUM #inclu...
  * `DecodeMemMMImm4` **(Many-Argument Workhorses)** (Impact: 60.9)
  * `DecodeINSVE_DF` **(Many-Argument Workhorses)** (Impact: 31.3)
  * `DecodeMSA128Mem` **(Many-Argument Workhorses)** (Impact: 26.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 516
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 386`, `structural_boundaries: 629`, `args: 802`, `func_start: 120`
* *Risk/State:* `state_mutation: 196`, `dead_code: 3`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 17`
* *Defense:* `safety: 6`, `doc: 8`, `immutability_locks: 252`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` MCDisassembler.h, MCFixedLenDisassembler.h, MCInst.h, MCInstPrinter.h, MCRegisterInfo.h, MathExtras.h, cs_priv.h, utils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/AArch64/AArch64InstPrinter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1782.82 | **LOC:** 2600 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (80.0919%), Tech Debt (61.599%)
**Top Internal Functions/Classes:**
  * `printInst` **(Many-Argument Workhorses)** (Impact: 403.3)
  * `getNextVectorRegister` **(Compute Cores)** (Impact: 159.9)
  * `printVectorList` **(Many-Argument Workhorses)** (Impact: 93.9)
  * `printSysAlias` **(Compute Cores)** (Impact: 93.7)
  * `printMemExtendImpl` **(Many-Argument Workhorses)** (Impact: 27.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 182 instances
* *State Mutation (weighted view):* 546
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 530`, `structural_boundaries: 331`, `args: 849`, `func_start: 55`
* *Risk/State:* `state_mutation: 182`, `fragile_debt: 4`, `unreferenced_by_name: 39`
* *Architecture:* `api: 50`, `import: 18`
* *Defense:* `doc: 3`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` MCInst.h, MCInstPrinter.h, MCRegisterInfo.h, Mapping.h, SStream.h, utils.h, AArch64AddressingModes.h, AArch64BaseInfo.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/ARM/ARMMapping.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1722.72 | **LOC:** 2268 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.4362%), Tech Debt (13.8594%)
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
* *Structure:* `branch: 591`, `structural_boundaries: 374`, `args: 581`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 135`, `unreferenced_by_name: 13`
* *Architecture:* `api: 31`, `import: 20`
* *Defense:* `safety: 7`, `doc: 64`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` MCDisassembler.h, Mapping.h, cs_priv.h, cs_simple_types.h, ARMAddressingModes.h, ARMBaseInfo.h, ARMDisassemblerExtension.h, ARMGenCSAliasMnemMap.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/X86/X86Disassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1629.8 | **LOC:** 1406 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.0083%), Tech Debt (9.3584%)
**Top Internal Functions/Classes:**
  * `translateImmediate` **(Many-Argument Workhorses)** (Impact: 552.2)
    * *Intent:* /// translateImmediate - Appends an immediate operand to an MCInst. /// /// @param mcInst - The MCIn...
  * `translateRMMemory` **(Compute Cores)** (Impact: 78.3)
    * *Intent:* /// translateRMMemory - Translates a memory operand stored in the Mod and R/M /// fields of an inter...
  * `X86_getInstruction` **(Many-Argument Workhorses)** (Impact: 55.3)
    * *Intent:* // Public interface for the disassembler
  * `translateOperand` **(Compute Cores)** (Impact: 46.6)
    * *Intent:* /// translateOperand - Translates an operand stored in an internal instruction /// to LLVM's format ...
  * `translateRM` **(Compute Cores)** (Impact: 41.4)
    * *Intent:* /// translateRM - Translates an operand stored in the R/M (and possibly SIB) /// byte of an instruct...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 243 instances
* *State Mutation (weighted view):* 735
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 370`, `structural_boundaries: 291`, `args: 17`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `state_mutation: 249`, `dead_code: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 14`
* *Defense:* `safety: 1`, `doc: 59`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` MCInst.h, cs_priv.h, utils.h, Availability.h, X86BaseInfo.h, X86Disassembler.h, X86DisassemblerDecoder.h, X86DisassemblerDecoderCommon.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/ocaml/ocaml.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1540.66 | **LOC:** 2132 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.8341%), Tech Debt (11.6899%)
**Top Internal Functions/Classes:**
  * `_cs_disasm` **(Many-Argument Workhorses)** (Impact: 428.8)
  * `ocaml_cs_disasm` **(Many-Argument Workhorses)** (Impact: 117.9)
  * `ocaml_open` **(Compute Cores)** (Impact: 85.3)
  * `ocaml_option` **(Many-Argument Workhorses)** (Impact: 19.7)
  * `list_count` **(Compute Cores)** (Impact: 5.7)
    * *Intent:* /* By Nguyen Anh Quynh <aquynh@gmail.com>, 2013> */ #include <stdio.h> // debug #include <string.h> ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 269 instances
* *State Mutation (weighted view):* 815
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 158`, `args: 20`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 277`, `dead_code: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` alloc.h, fail.h, memory.h, mlvalues.h, capstone.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/AArch64/AArch64Disassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1518.68 | **LOC:** 2218 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.9333%), Tech Debt (8.5645%)
**Top Internal Functions/Classes:**
  * `DecodeSignedLdStInstruction` **(Many-Argument Workhorses)** (Impact: 352.0)
  * `DecodePairLdStInstruction` **(Many-Argument Workhorses)** (Impact: 190.1)
  * `DecodeExclusiveLdStInstruction` **(Many-Argument Workhorses)** (Impact: 111.5)
  * `DecodeThreeAddrSRegInstruction` **(Many-Argument Workhorses)** (Impact: 70.2)
  * `DecodeUnsignedLdStInstruction` **(Many-Argument Workhorses)** (Impact: 63.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 509`, `structural_boundaries: 408`, `args: 431`, `func_start: 90`
* *Risk/State:* `state_mutation: 22`, `dead_code: 9`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 19`
* *Defense:* `safety: 2`, `immutability_locks: 181`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` LEB128.h, MCDisassembler.h, MCFixedLenDisassembler.h, MCInst.h, MCInstrDesc.h, MCRegisterInfo.h, cs_priv.h, utils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/vb6/CX86Operand.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1354.95 | **LOC:** 203 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.145%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 1`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 28`
* *Architecture:* None
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/python/cstest_py/src/cstest_py/details.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1162.86 | **LOC:** 1589 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (22.5929%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_expected_arm` **(Compute Cores)** (Impact: 105.3)
  * `test_expected_aarch64` **(Compute Cores)** (Impact: 102.4)
  * `test_expected_x86` **(Compute Cores)** (Impact: 85.4)
  * `test_expected_m68k` **(Compute Cores)** (Impact: 78.6)
  * `compare_details` **(Compute Cores)** (Impact: 60.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 570`, `structural_boundaries: 685`, `args: 25`, `func_start: 25`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 25`, `import: 26`
* *Defense:* `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.318
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000398
  * `Imports (Out-Degree: 3):` __future__, capstone, capstone.aarch64_const, capstone.alpha_const, capstone.arc_const, capstone.arm_const, capstone.bpf_const, capstone.hppa_const...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `arch/WASM/WASMDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1098.0 | **LOC:** 1066 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (94.4593%), Tech Debt (8.8784%)
**Top Internal Functions/Classes:**
  * `WASM_getInstruction` **(Many-Argument Workhorses)** (Impact: 611.9)
  * `read_brtable` **(Many-Argument Workhorses)** (Impact: 25.8)
    * *Intent:* // input | code : code pointer start from brtable // | code_len : start from the code pointer to the...
  * `read_memoryimmediate` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* // input | code : code pointer start from memoryimmediate // | code_len : start from the code pointe...
  * `get_varuint64` **(Many-Argument Workhorses)** (Impact: 15.4)
    * *Intent:* // input | code : code pointer start from varuint64 // | code_len : real code len count from varint ...
  * `get_varuint32` **(Many-Argument Workhorses)** (Impact: 15.3)
    * *Intent:* // input | code: code pointer start from varuint32 // | code_len: real code len count from varint //...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 101`, `args: 14`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 133`, `dead_code: 12`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 19`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cs_priv.h, WASMDisassembler.h, WASMMapping.h, stddef.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/vb6/CDisassembler.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1087.51 | **LOC:** 154 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.5508%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 2`, `args: 7`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 25`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/TriCore/TriCoreDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1085.86 | **LOC:** 1752 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.6842%), Tech Debt (9.6269%)
**Top Internal Functions/Classes:**
  * `DecodeBOInstruction` **(Many-Argument Workhorses)** (Impact: 88.0)
  * `DecodeRRInstruction` **(Many-Argument Workhorses)** (Impact: 52.8)
  * `DecodeSROInstruction` **(Many-Argument Workhorses)** (Impact: 49.4)
  * `DecodeBOLInstruction` **(Many-Argument Workhorses)** (Impact: 45.5)
  * `DecodeSRRInstruction` **(Many-Argument Workhorses)** (Impact: 40.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 299`, `args: 427`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `state_mutation: 80`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 19`
* *Defense:* `safety: 3`, `doc: 3`, `immutability_locks: 124`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` MCDisassembler.h, MCFixedLenDisassembler.h, MCInst.h, MCInstrDesc.h, MCRegisterInfo.h, MathExtras.h, cs_priv.h, utils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/auto-sync/src/autosync/cpptranslator/Differ.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 948.32 | **LOC:** 1009 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.9452%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `diff_nodes` **(Many-Argument Workhorses)** (Impact: 92.6)
  * `all_choices_saved` **(Many-Argument Workhorses)** (Impact: 31.1)
  * `determine_patch_coordinates` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `get_user_choice` **(Compute Cores)** (Impact: 29.7)
  * `patch_files` **(Compute Cores)** (Impact: 29.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 128 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 438
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 149`, `args: 39`, `func_start: 35`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 182`
* *Architecture:* `io: 8`, `api: 32`, `import: 14`
* *Defense:* `safety: 7`, `doc: 10`, `test: 19`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.305
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000598
  * `Imports (Out-Degree: 3):` argparse, autosync.Helper, autosync.Targets, autosync.cpptranslator.Configurator, difflib, enum, json, logging...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `arch/X86/X86ATTInstPrinter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 900.86 | **LOC:** 1204 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (68.0874%), Tech Debt (90.3645%)
**Top Internal Functions/Classes:**
  * `X86_ATT_printInst` **(Many-Argument Workhorses)** (Impact: 173.9)
  * `printOperand` **(Many-Argument Workhorses)** (Impact: 128.0)
  * `printopaquemem` **(Compute Cores)** (Impact: 64.8)
  * `printMemReference` **(Many-Argument Workhorses)** (Impact: 55.9)
  * `_printOperand` **(Compute Cores)** (Impact: 38.2)
    * *Intent:* // local printOperand, without updating public operands
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 208
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 278`, `structural_boundaries: 91`, `args: 184`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `state_mutation: 98`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `api: 1`, `import: 21`
* *Defense:* `safety: 1`, `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` MCInst.h, MCRegisterInfo.h, SStream.h, utils.h, Availability.h, X86BaseInfo.h, X86GenAsmWriter.inc, X86GenAsmWriter_reduce.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/X86/X86IntelInstPrinter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 862.3 | **LOC:** 1274 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (62.5732%), Tech Debt (88.9273%)
**Top Internal Functions/Classes:**
  * `printImm` **(Many-Argument Workhorses)** (Impact: 124.2)
  * `printOperand` **(Many-Argument Workhorses)** (Impact: 95.5)
  * `printopaquemem` **(Compute Cores)** (Impact: 85.8)
  * `printMemReference` **(Many-Argument Workhorses)** (Impact: 54.1)
  * `printanymem` **(Compute Cores)** (Impact: 31.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 224
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 119`, `args: 225`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 98`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 30`
* *Architecture:* `api: 1`, `import: 21`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` MCInst.h, MCRegisterInfo.h, SStream.h, utils.h, Availability.h, X86BaseInfo.h, X86GenAsmWriter1.inc, X86GenAsmWriter1_reduce.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/Xtensa/XtensaDisassembler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 816.06 | **LOC:** 1140 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.8855%), Tech Debt (94.1111%)
**Top Internal Functions/Classes:**
  * `CheckRegister` **(Compute Cores)** (Impact: 144.4)
    * *Intent:* // Verify SR and UR
  * `getInstruction` **(Many-Argument Workhorses)** (Impact: 40.7)
  * `decodeBranchOperand` **(Many-Argument Workhorses)** (Impact: 25.8)
  * `readInstruction24` **(Many-Argument Workhorses)** (Impact: 12.9)
    * *Intent:* /// Read three bytes from the ArrayRef and return 24 bit data
  * `DecodeSRRegisterClass` **(Many-Argument Workhorses)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 223
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 206`, `args: 183`, `func_start: 63`
* *Risk/State:* `state_mutation: 75`, `dead_code: 2`, `unreferenced_by_name: 50`
* *Architecture:* `api: 3`, `import: 13`
* *Defense:* `safety: 6`, `doc: 5`, `immutability_locks: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` MCDisassembler.h, MCFixedLenDisassembler.h, MathExtras.h, SStream.h, cs_priv.h, utils.h, XtensaGenDisassemblerTables.inc, XtensaGenInstrInfo.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/ARM/ARMInstPrinter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 806.02 | **LOC:** 2021 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.3364%), Tech Debt (99.3126%)
**Top Internal Functions/Classes:**
  * `printInst` **(Many-Argument Workhorses)** (Impact: 200.3)
    * *Intent:* #define PRINT_ALIAS_INSTR #include "ARMGenAsmWriter.inc"
  * `printMSRMaskOperand` **(Many-Argument Workhorses)** (Impact: 58.6)
  * `printRegImmShift` **(Many-Argument Workhorses)** (Impact: 23.1)
    * *Intent:* /// Prints the shift value with an immediate value.
  * `printModImmOperand` **(Many-Argument Workhorses)** (Impact: 18.3)
  * `printOperandAddr` **(Many-Argument Workhorses)** (Impact: 14.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 195`, `args: 909`, `func_start: 86`
* *Risk/State:* `state_mutation: 35`, `dead_code: 1`, `fragile_debt: 6`, `unreferenced_by_name: 74`
* *Architecture:* `api: 3`, `import: 15`
* *Defense:* `doc: 4`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` MCInst.h, MCInstPrinter.h, MCRegisterInfo.h, Mapping.h, SStream.h, ARMAddressingModes.h, ARMBaseInfo.h, ARMDisassemblerExtension.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/auto-sync/src/autosync/MCUpdater.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 711.34 | **LOC:** 659 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (68.4533%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 53.6)
  * `init_tests` **(Compute Cores)** (Impact: 41.0)
  * `extract_llvm_mc_cmds` **(Compute Cores)** (Impact: 37.5)
  * `write_to_build_dir` **(Compute Cores)** (Impact: 34.9)
  * `parse_llvm_mc_line` **(Compute Cores)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 102 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 97`, `args: 40`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 132`
* *Architecture:* `io: 5`, `api: 28`, `import: 9`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.355
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000598
  * `Imports (Out-Degree: 2):` argparse, autosync.Helper, autosync.Targets, json, logging, pathlib, re, subprocess...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `arch/RISCV/RISCVMapping.c` -> Churn: **100.0%** | Cog Load: 62.051% | Debt: 72.1726%
- `cs.c` -> Churn: **87.7%** | Cog Load: 73.0434% | Debt: 71.925%
- `Mapping.c` -> Churn: **66.67%** | Cog Load: 36.9504% | Debt: 99.4252%
- `suite/cstest/src/helper.c` -> Churn: **52.83%** | Cog Load: 52.9191% | Debt: 63.5424%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `arch/ARM/ARMDisassembler.c` -> **billow** (100.0% isolated ownership) | Magnitude: 6158.32
- `arch/AArch64/AArch64Mapping.c` -> **Rot127** (100.0% isolated ownership) | Magnitude: 2554.1
- `arch/M68K/M68KDisassembler.c` -> **Carsten Elton Sørensen** (100.0% isolated ownership) | Magnitude: 2542.16
- `arch/X86/X86DisassemblerDecoder.c` -> **Jos** (100.0% isolated ownership) | Magnitude: 2267.42
- `arch/M680X/M680XDisassembler.c` -> **Naren Sirigere** (100.0% isolated ownership) | Magnitude: 1813.36

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `include/capstone/capstone.h` -> **Severity: 0.026** (Bridge: 0.0006 * Flux: 43.3485%)
- `suite/auto-sync/src/autosync/cpptranslator/patches/Helper.py` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `LEB128.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.8341%)
- `arch/PowerPC/PPCMCTargetDesc.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 95.264%)
- `suite/cstest/include/test_compare.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 22.0349%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `include/capstone/cs_operand.h` -> **Severity: 2.687** (Embedded: 0.0435 * Error Risk: 61.7748%)
- `include/capstone/capstone.h` -> **Severity: 2.272** (Embedded: 0.0635 * Error Risk: 35.7758%)
- `include/capstone/ppc.h` -> **Severity: 1.979** (Embedded: 0.0386 * Error Risk: 51.2262%)
- `include/capstone/aarch64.h` -> **Severity: 1.975** (Embedded: 0.0393 * Error Risk: 50.2864%)
- `include/capstone/tms320c64x.h` -> **Severity: 1.961** (Embedded: 0.0385 * Error Risk: 50.9347%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `suite/auto-sync/src/autosync/PathVarHandler.py` -> **Severity: 1171.7** (Blast Radius: 11.717 * Doc Risk: 100.0%)
- `suite/auto-sync/src/autosync/Helper.py` -> **Severity: 1066.56** (Blast Radius: 13.332 * Doc Risk: 80.0%)
- `utils.h` -> **Severity: 556.35** (Blast Radius: 11.127 * Doc Risk: 50.0%)
- `MCInst.h` -> **Severity: 398.65** (Blast Radius: 7.973 * Doc Risk: 50.0%)
- `suite/auto-sync/src/autosync/cpptranslator/patches/Helper.py` -> **Severity: 329.909** (Blast Radius: 7.258 * Doc Risk: 45.4545%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
