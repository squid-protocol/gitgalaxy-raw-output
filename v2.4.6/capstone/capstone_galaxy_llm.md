# ARCHITECTURAL_BRIEF: capstone
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/capstone` |
| **Timestamp** | `2026-08-03T19:27:01.096155+00:00` |
| **Scan Duration** | `9.55s` |
| **Git Branch** | `next` |
| **Git Commit** | `95fe762a411783c7507218e3d895f3b93e3238d5` |
| **Git Remote** | `https://github.com/capstone-engine/capstone.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1633 malicious artifacts.

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
| Total Artifacts | 3963 |
| Analyzed Artifacts (Scanned) | 3307 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 656 |
| Total LOC | 439629 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 83.4% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2934 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.3334 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 101 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| YAML | 1615 | 243127 | 48.8% |
| CSHARP | 1065 | 39421 | 32.2% |
| C | 384 | 139530 | 11.6% |
| PYTHON | 127 | 11086 | 3.8% |
| MARKDOWN | 33 | 0 | 1.0% |
| JAVA | 19 | 2054 | 0.6% |
| PLAINTEXT | 18 | 0 | 0.5% |
| MAKEFILE | 10 | 958 | 0.3% |
| SHELL | 8 | 288 | 0.2% |
| JSON | 7 | 947 | 0.2% |
| APEX | 6 | 669 | 0.2% |
| CPP | 5 | 370 | 0.2% |
| POWERSHELL | 3 | 495 | 0.1% |
| M4 | 3 | 33 | 0.1% |
| BATCH | 2 | 264 | 0.1% |
| RUBY | 1 | 387 | 0.0% |
| XML | 1 | 0 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `8.069`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 3018 | 91.3% |
| file_cluster_13 | 176 | 5.3% |
| file_cluster_16 | 46 | 1.4% |
| file_cluster_9 | 5 | 0.2% |
| file_cluster_0 | 2 | 0.1% |
| file_cluster_17 | 2 | 0.1% |
| file_cluster_12 | 2 | 0.1% |
| file_cluster_4 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 55 | 1.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 656*

**Composition by Extension & Reason:**
- `.yaml`: 60x Excluded (Saturation: Line 4 exceeds 500 chars), 13x Excluded (Static Asset Blob without Intent: 1021 LOC), 10x Excluded (Static Asset Blob without Intent: 1681 LOC)
- `.inc`: 3x Excluded (Machine-Generated Source Code Signature: 120 LOC), 2x Excluded (Embedded Array/Matrix Payload: 17385 commas in 5380 LOC), 2x Excluded (Machine-Generated Source Code Signature: 205 LOC)
- `.h`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 352 LOC), 1x Excluded (Machine-Generated Source Code Signature: 62 LOC)
- `.ml`: 35x Excluded (Unsupported Extension: '.ml')
- `.py`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 338 LOC), 1x Excluded (Machine-Generated Source Code Signature: 4316 LOC)
- `.cs`: 1x Excluded (Embedded Hex Payload: 3818 hex tokens in 956 LOC), 1x Excluded (Embedded Hex Payload: 4168 hex tokens in 1044 LOC), 1x Excluded (Embedded Hex Payload: 8411 hex tokens in 2102 LOC)
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.xcworkspacedata')
- `.java`: 1x Excluded (Saturation: Line 40 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 3011 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1333 LOC)
- `.patch`: 14x Excluded (Unsupported Extension: '.patch'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 125 LOC), 1x Excluded (Machine-Generated Source Code Signature: 96 LOC)
- `.cmake`: 10x Excluded (Unsupported Extension: '.cmake')
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 113 LOC), 1x Excluded (Machine-Generated Source Code Signature: 142 LOC), 1x Excluded (Machine-Generated Source Code Signature: 518 LOC)
- `.xcscheme`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.xcscheme')
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 7.8 | 3.9 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.9 | 0.0 | 0.0 |
| API Exposure | 0.0 | 18.7 | 1.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 97.6 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 87.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.0 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 14.9 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 7.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 99.9 | 0.1 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `arch/SH/SHDisassembler.c` (Hits: 76)
- `Makefile` (Hits: 68)
- `suite/run_invalid_cstool.sh` (Hits: 52)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Patch.py** (`suite/auto-sync/src/autosync/cpptranslator/patches/Patch.py`) — 66 inbound connections
2. **Helper.py** (`suite/auto-sync/src/autosync/cpptranslator/patches/Helper.py`) — 56 inbound connections
3. **cstool.h** (`cstool/cstool.h`) — 23 inbound connections
4. **cs_operand.h** (`include/capstone/cs_operand.h`) — 22 inbound connections
5. **capstone.h** (`include/capstone/capstone.h`) — 19 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CppTranslator.py** (`suite/auto-sync/src/autosync/cpptranslator/CppTranslator.py`) — 77 outbound dependencies
2. **test_patches.py** (`suite/auto-sync/src/autosync/cpptranslator/Tests/test_patches.py`) — 72 outbound dependencies
3. **cs.c** (`cs.c`) — 35 outbound dependencies
4. **capstone.h** (`include/capstone/capstone.h`) — 31 outbound dependencies
5. **details.py** (`bindings/python/cstest_py/src/cstest_py/details.py`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `readPrefixes` (@ `arch/X86/X86DisassemblerDecoder.c`) -> Impact: **1954.1** | LOC: 682
  * *Intent:* // return decision->opcodeDecisions[insnContext].modRMDecisions[opcode].modrm_type != MODRM_ONEENTRY;
- `DecodeMemMultipleWritebackInstruction` (@ `arch/ARM/ARMDisassembler.c`) -> Impact: **897.2** | LOC: 1040
- `add_alias_details` (@ `arch/ARM/ARMMapping.c`) -> Impact: **819.1** | LOC: 1222
- `AArch64_add_vas` (@ `arch/AArch64/AArch64Mapping.c`) -> Impact: **517.9** | LOC: 433
  * *Intent:* /// Very annoyingly LLVM hard codes the vector layout post-fixes into the asm string. /// In this function we check for these cases and add the vector...
- `_cs_disasm` (@ `bindings/ocaml/ocaml.c`) -> Impact: **472.9** | LOC: 1697
- `print_ins_detail` (@ `bindings/java/TestX86.java`) -> Impact: **399.2** | LOC: 145
- `init_patches` (@ `suite/auto-sync/src/autosync/cpptranslator/CppTranslator.py`) -> Impact: **365.6** | LOC: 141
- `WASM_getInstruction` (@ `arch/WASM/WASMDisassembler.c`) -> Impact: **353.8** | LOC: 416
- `main` (@ `suite/fuzz/drivermc.c`) -> Impact: **318.9** | LOC: 194
  * *Intent:* #define MAX_INSTR_SIZE 64 #define MAX_LINE_SIZE 128
- `DecodeAddrMode3Instruction` (@ `arch/ARM/ARMDisassembler.c`) -> Impact: **307.9** | LOC: 197

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `copy_sources` (@ `bindings/python/setup.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ Copy the C sources into the source directory. This rearranges the source files under the python distribution directory. """
- `test_file` (@ `suite/test_corpus3.py`) -> **O(2^N) [Recursive]**
- `test_compatibility` (@ `bindings/python/tests/test_compatibility_layer.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Test arm64 and sysz compatibility layer
- `test_class` (@ `bindings/python/tests/test_lite.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # ## Test class Cs
- `test_class` (@ `bindings/python/tests/test_skipdata.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # ## Test class Cs
- `readPrefixes` (@ `arch/X86/X86DisassemblerDecoder.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // return decision->opcodeDecisions[insnContext].modRMDecisions[opcode].modrm_type != MODRM_ONEENTRY;
- `parse_args` (@ `suite/auto-sync/src/autosync/ASUpdater.py`) -> **O(2^N) [Recursive]**
- `find_id_by_type` (@ `suite/auto-sync/src/autosync/Helper.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ Recursively searches for a node sequence with given node types. A valid sequence is a path from node_n to node_{(n + |node_types|-1)} where forall...
- `__call__` (@ `suite/auto-sync/src/autosync/PathVarHandler.py`) -> **O(2^N) [Recursive]**
- `tryAddingSymbolicOperand` (@ `arch/ARM/ARMDisassembler.c`) -> **O(2^N) [Recursive]**
  * *Intent:* /// tryAddingSymbolicOperand - trys to add a symbolic operand in place of the /// immediate Value in the MCInst. The immediate Value has had any PC //...

### Highest Data Gravity (Database Complexity)
- `AArch64CC_getInvertedCondCode` (@ `include/capstone/aarch64.h`) -> DB Complexity: **743**
- `add_alias_details` (@ `arch/ARM/ARMMapping.c`) -> DB Complexity: **236**
- `_cs_disasm` (@ `bindings/ocaml/ocaml.c`) -> DB Complexity: **172**
- `copy_sources` (@ `bindings/python/setup.py`) -> DB Complexity: **123**
  * *Intent:* """ Copy the C sources into the source directory. This rearranges the source files under the python distribution directory. """
- `DecodeMemMultipleWritebackInstruction` (@ `arch/ARM/ARMDisassembler.c`) -> DB Complexity: **106**
- `readPrefixes` (@ `arch/X86/X86DisassemblerDecoder.c`) -> DB Complexity: **106**
  * *Intent:* // return decision->opcodeDecisions[insnContext].modRMDecisions[opcode].modrm_type != MODRM_ONEENTRY;
- `fillDetails` (@ `arch/MOS65XX/MOS65XXDisassembler.c`) -> DB Complexity: **91**
  * *Intent:* #endif #ifndef CAPSTONE_DIET
- `AArch64_add_vas` (@ `arch/AArch64/AArch64Mapping.c`) -> DB Complexity: **87**
  * *Intent:* /// Very annoyingly LLVM hard codes the vector layout post-fixes into the asm string. /// In this function we check for these cases and add the vector...
- `getNextVectorRegister` (@ `arch/AArch64/AArch64InstPrinter.c`) -> DB Complexity: **81**
- `cs_op_index` (@ `cs.c`) -> DB Complexity: **73**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `suite/MC/AArch64` | 441 | 17853.18 | 10.95% | 0.0% |
| `__monolith__` | 42 | 10969.09 | 20.07% | 22.31% |
| `include/capstone` | 23 | 8346.78 | 8.03% | 1.06% |
| `arch/ARM` | 14 | 6939.5 | 33.1% | 31.04% |
| `arch/X86` | 21 | 6288.44 | 22.72% | 14.93% |
| `arch/AArch64` | 12 | 6079.72 | 39.82% | 35.97% |
| `tests/MC/AArch64/SVE` | 328 | 6049.22 | 0.52% | 0.0% |
| `suite/cstest/src` | 28 | 5480.4 | 71.24% | 2.2% |
| `arch/HPPA` | 9 | 4259.4 | 24.64% | 15.65% |
| `cstool` | 29 | 4173.08 | 66.4% | 31.68% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `MCInstrDesc.c` -> **100.0%** Exposure
- `arch/ARM/ARMInstPrinter.c` -> **100.0%** Exposure
- `suite/auto-sync/src/autosync/cpptranslator/Tests/Patches/template_src.c` -> **100.0%** Exposure
- `bindings/java/capstone/M680x.java` -> **100.0%** Exposure
- `bindings/java/capstone/Mips.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `MCInst.c` -> **100.0%** Exposure
- `MCRegisterInfo.c` -> **100.0%** Exposure
- `Mapping.c` -> **100.0%** Exposure
- `arch/AArch64/AArch64BaseInfo.c` -> **100.0%** Exposure
- `arch/AArch64/AArch64Mapping.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `arch/M68K/M68KDisassembler.c` -> **188** Orphaned Functions | **0** Duplicates
- `arch/Mips/MipsDisassembler.c` -> **52** Orphaned Functions | **0** Duplicates
- `arch/SH/SHDisassembler.c` -> **52** Orphaned Functions | **0** Duplicates
- `arch/Xtensa/XtensaDisassembler.c` -> **50** Orphaned Functions | **0** Duplicates
- `arch/Xtensa/XtensaInstPrinter.c` -> **38** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`arch/HPPA/HPPADisassembler.c`** -> AI Confidence: **99.48%**
2. **`arch/LoongArch/LoongArchMapping.c`** -> AI Confidence: **99.48%**
3. **`arch/M68K/M68KInstPrinter.c`** -> AI Confidence: **99.48%**
4. **`arch/MOS65XX/MOS65XXDisassembler.c`** -> AI Confidence: **99.48%**
5. **`arch/TMS320C64x/TMS320C64xInstPrinter.c`** -> AI Confidence: **99.48%**
6. **`arch/TriCore/TriCoreInstPrinter.c`** -> AI Confidence: **99.48%**
7. **`arch/X86/X86ATTInstPrinter.c`** -> AI Confidence: **99.48%**
8. **`arch/X86/X86Disassembler.c`** -> AI Confidence: **99.48%**
9. **`arch/X86/X86InstPrinterCommon.c`** -> AI Confidence: **99.48%**
10. **`arch/X86/X86IntelInstPrinter.c`** -> AI Confidence: **99.48%**
11. **`arch/XCore/XCoreInstPrinter.c`** -> AI Confidence: **99.48%**
12. **`arch/Xtensa/XtensaInstPrinter.c`** -> AI Confidence: **99.48%**
13. **`arch/Xtensa/XtensaMapping.c`** -> AI Confidence: **99.48%**
14. **`bindings/ocaml/ocaml.c`** -> AI Confidence: **99.48%**
15. **`arch/AArch64/AArch64InstPrinter.c`** -> AI Confidence: **99.39%**
16. **`arch/AArch64/AArch64Mapping.c`** -> AI Confidence: **99.39%**
17. **`arch/ARM/ARMMapping.c`** -> AI Confidence: **99.39%**
18. **`arch/M680X/M680XInstPrinter.c`** -> AI Confidence: **99.39%**
19. **`arch/RISCV/RISCVMapping.c`** -> AI Confidence: **99.39%**
20. **`arch/Sparc/SparcMapping.c`** -> AI Confidence: **99.39%**
21. **`arch/SystemZ/SystemZMapping.c`** -> AI Confidence: **99.39%**
22. **`arch/X86/X86DisassemblerDecoder.c`** -> AI Confidence: **99.39%**
23. **`suite/cstest/src/helper.c`** -> AI Confidence: **99.39%**
24. **`arch/BPF/BPFDisassembler.c`** -> AI Confidence: **99.34%**
25. **`arch/MOS65XX/MOS65XXModule.c`** -> AI Confidence: **99.34%**
26. **`arch/X86/X86Module.c`** -> AI Confidence: **99.34%**
27. **`cstool/cstool_aarch64.c`** -> AI Confidence: **99.34%**
28. **`cstool/cstool_arm.c`** -> AI Confidence: **99.34%**
29. **`cstool/cstool_hppa.c`** -> AI Confidence: **99.34%**
30. **`suite/fuzz/driverbin.c`** -> AI Confidence: **99.34%**
31. **`suite/fuzz/fuzz_disasm.c`** -> AI Confidence: **99.34%**
32. **`bindings/java/TestX86.java`** -> AI Confidence: **99.34%**
33. **`arch/SH/SHInstPrinter.c`** -> AI Confidence: **99.32%**
34. **`cstool/cstool_arc.c`** -> AI Confidence: **99.32%**
35. **`cstool/cstool_loongarch.c`** -> AI Confidence: **99.32%**
36. **`cstool/cstool_m680x.c`** -> AI Confidence: **99.32%**
37. **`cstool/cstool_m68k.c`** -> AI Confidence: **99.32%**
38. **`cstool/cstool_sh.c`** -> AI Confidence: **99.32%**
39. **`cstool/cstool_sparc.c`** -> AI Confidence: **99.32%**
40. **`cstool/cstool_systemz.c`** -> AI Confidence: **99.32%**
41. **`cstool/cstool_tms320c64x.c`** -> AI Confidence: **99.32%**
42. **`cstool/cstool_tricore.c`** -> AI Confidence: **99.32%**
43. **`cstool/cstool_xcore.c`** -> AI Confidence: **99.32%**
44. **`cstool/cstool_xtensa.c`** -> AI Confidence: **99.32%**
45. **`tests/integration/compat_header/src/test_sysz_compatibility_header.c`** -> AI Confidence: **99.32%**
46. **`SStream.c`** -> AI Confidence: **99.31%**
47. **`arch/AArch64/AArch64Disassembler.c`** -> AI Confidence: **99.31%**
48. **`arch/ARC/ARCInstPrinter.c`** -> AI Confidence: **99.31%**
49. **`arch/ARC/ARCMapping.c`** -> AI Confidence: **99.31%**
50. **`arch/ARM/ARMDisassembler.c`** -> AI Confidence: **99.31%**
51. **`arch/Alpha/AlphaInstPrinter.c`** -> AI Confidence: **99.31%**
52. **`arch/Alpha/AlphaMapping.c`** -> AI Confidence: **99.31%**
53. **`arch/M680X/M680XDisassembler.c`** -> AI Confidence: **99.31%**
54. **`arch/M68K/M68KDisassembler.c`** -> AI Confidence: **99.31%**
55. **`arch/Mips/MipsDisassembler.c`** -> AI Confidence: **99.31%**
56. **`arch/Mips/MipsInstPrinter.c`** -> AI Confidence: **99.31%**
57. **`arch/PowerPC/PPCInstPrinter.c`** -> AI Confidence: **99.31%**
58. **`arch/PowerPC/PPCMapping.c`** -> AI Confidence: **99.31%**
59. **`arch/SH/SHDisassembler.c`** -> AI Confidence: **99.31%**
60. **`arch/Sparc/SparcInstPrinter.c`** -> AI Confidence: **99.31%**
61. **`arch/SystemZ/SystemZMCTargetDesc.c`** -> AI Confidence: **99.31%**
62. **`arch/TMS320C64x/TMS320C64xDisassembler.c`** -> AI Confidence: **99.31%**
63. **`arch/TriCore/TriCoreDisassembler.c`** -> AI Confidence: **99.31%**
64. **`arch/TriCore/TriCoreMapping.c`** -> AI Confidence: **99.31%**
65. **`arch/XCore/XCoreMapping.c`** -> AI Confidence: **99.31%**
66. **`arch/Xtensa/XtensaDisassembler.c`** -> AI Confidence: **99.31%**
67. **`cs.c`** -> AI Confidence: **99.31%**
68. **`suite/cstest/src/cstest.c`** -> AI Confidence: **99.31%**
69. **`suite/cstest/src/test_case.c`** -> AI Confidence: **99.31%**
70. **`suite/cstest/src/test_detail_riscv.c`** -> AI Confidence: **99.31%**
71. **`suite/cstest/src/test_run.c`** -> AI Confidence: **99.31%**
72. **`bindings/python/cstest_py/src/cstest_py/cstest.py`** -> AI Confidence: **99.31%**
73. **`bindings/python/setup.py`** -> AI Confidence: **99.31%**
74. **`suite/auto-sync/src/autosync/IncGenerator.py`** -> AI Confidence: **99.31%**
75. **`suite/auto-sync/src/autosync/MCUpdater.py`** -> AI Confidence: **99.31%**
76. **`suite/auto-sync/src/autosync/cpptranslator/Differ.py`** -> AI Confidence: **99.31%**
77. **`arch/EVM/EVMDisassembler.c`** -> AI Confidence: **99.29%**
78. **`arch/WASM/WASMInstPrinter.c`** -> AI Confidence: **99.29%**
79. **`cstool/cstool_alpha.c`** -> AI Confidence: **99.29%**
80. **`cstool/cstool_bpf.c`** -> AI Confidence: **99.29%**
81. **`cstool/cstool_mips.c`** -> AI Confidence: **99.29%**
82. **`cstool/cstool_powerpc.c`** -> AI Confidence: **99.29%**
83. **`cstool/cstool_riscv.c`** -> AI Confidence: **99.29%**
84. **`cstool/cstool_wasm.c`** -> AI Confidence: **99.29%**
85. **`suite/fuzz/drivermc.c`** -> AI Confidence: **99.29%**
86. **`arch/M680X/m6800.inc`** -> AI Confidence: **99.29%**
87. **`cs_simple_types.h`** -> AI Confidence: **99.29%**
88. **`include/windowsce/intrin.h`** -> AI Confidence: **99.29%**
89. **`suite/auto-sync/src/autosync/Tests/test_include.inc`** -> AI Confidence: **99.29%**
90. **`arch/SH/mktable.rb`** -> AI Confidence: **99.29%**
91. **`cmake.sh`** -> AI Confidence: **99.29%**
92. **`bindings/powershell/Capstone/Capstone.psm1`** -> AI Confidence: **99.29%**
93. **`bindings/vb6/CDisassembler.cls`** -> AI Confidence: **99.29%**
94. **`bindings/vb6/CInstruction.cls`** -> AI Confidence: **99.29%**
95. **`bindings/vb6/CX86Inst.cls`** -> AI Confidence: **99.29%**
96. **`bindings/vb6/CX86OpMem.cls`** -> AI Confidence: **99.29%**
97. **`bindings/vb6/CX86Operand.cls`** -> AI Confidence: **99.29%**
98. **`suite/MC/AArch64/add.s.cs`** -> AI Confidence: **99.29%**
99. **`suite/MC/AArch64/arm64-advsimd.txt.cs`** -> AI Confidence: **99.29%**
100. **`suite/MC/AArch64/arm64-arithmetic.txt.cs`** -> AI Confidence: **99.29%**
101. **`suite/MC/AArch64/arm64-branch.txt.cs`** -> AI Confidence: **99.29%**
102. **`suite/MC/AArch64/arm64-compact-unwind-fallback.s.cs`** -> AI Confidence: **99.29%**
103. **`suite/MC/AArch64/arm64-crc32.txt.cs`** -> AI Confidence: **99.29%**
104. **`suite/MC/AArch64/arm64-invalid-logical.txt.cs`** -> AI Confidence: **99.29%**
105. **`suite/MC/AArch64/arm64-leaf-compact-unwind.s.cs`** -> AI Confidence: **99.29%**
106. **`suite/MC/AArch64/arm64-logical-encoding.s.cs`** -> AI Confidence: **99.29%**
107. **`suite/MC/AArch64/armv8.1a-atomic.txt.cs`** -> AI Confidence: **99.29%**
108. **`suite/MC/AArch64/armv8.1a-lor.txt.cs`** -> AI Confidence: **99.29%**
109. **`suite/MC/AArch64/armv8.1a-pan.txt.cs`** -> AI Confidence: **99.29%**
110. **`suite/MC/AArch64/armv8.1a-vhe.txt.cs`** -> AI Confidence: **99.29%**
111. **`suite/MC/AArch64/armv8.3a-ID_ISAR6_EL1.txt.cs`** -> AI Confidence: **99.29%**
112. **`suite/MC/AArch64/armv8.5a-ssbs.txt.cs`** -> AI Confidence: **99.29%**
113. **`suite/MC/AArch64/armv8.9a-ats1a.s.cs`** -> AI Confidence: **99.29%**
114. **`suite/MC/AArch64/armv8.9a-ats1a.txt.cs`** -> AI Confidence: **99.29%**
115. **`suite/MC/AArch64/armv9-sysp.txt.cs`** -> AI Confidence: **99.29%**
116. **`suite/MC/AArch64/armv9.4a-chk.s.cs`** -> AI Confidence: **99.29%**
117. **`suite/MC/AArch64/armv9.4a-chk.txt.cs`** -> AI Confidence: **99.29%**
118. **`suite/MC/AArch64/armv9.4a-gcs.s.cs`** -> AI Confidence: **99.29%**
119. **`suite/MC/AArch64/armv9.4a-gcs.txt.cs`** -> AI Confidence: **99.29%**
120. **`suite/MC/AArch64/armv9.5a-cpa.s.cs`** -> AI Confidence: **99.29%**
121. **`suite/MC/AArch64/armv9.5a-cpa.txt.cs`** -> AI Confidence: **99.29%**
122. **`suite/MC/AArch64/armv9.5a-e3dse.s.cs`** -> AI Confidence: **99.29%**
123. **`suite/MC/AArch64/armv9.5a-e3dse.txt.cs`** -> AI Confidence: **99.29%**
124. **`suite/MC/AArch64/armv9.5a-fgwte3.s.cs`** -> AI Confidence: **99.29%**
125. **`suite/MC/AArch64/armv9.5a-fgwte3.txt.cs`** -> AI Confidence: **99.29%**
126. **`suite/MC/AArch64/armv9.5a-hacdbs.s.cs`** -> AI Confidence: **99.29%**
127. **`suite/MC/AArch64/armv9.5a-hacdbs.txt.cs`** -> AI Confidence: **99.29%**
128. **`suite/MC/AArch64/armv9.5a-hdbss.s.cs`** -> AI Confidence: **99.29%**
129. **`suite/MC/AArch64/armv9.5a-hdbss.txt.cs`** -> AI Confidence: **99.29%**
130. **`suite/MC/AArch64/armv9.5a-pauthlr.txt.cs`** -> AI Confidence: **99.29%**
131. **`suite/MC/AArch64/armv9.5a-spmu2.s.cs`** -> AI Confidence: **99.29%**
132. **`suite/MC/AArch64/armv9.5a-spmu2.txt.cs`** -> AI Confidence: **99.29%**
133. **`suite/MC/AArch64/armv9.5a-step2.s.cs`** -> AI Confidence: **99.29%**
134. **`suite/MC/AArch64/armv9.5a-step2.txt.cs`** -> AI Confidence: **99.29%**
135. **`suite/MC/AArch64/basic-a64-undefined.txt.cs`** -> AI Confidence: **99.29%**
136. **`suite/MC/AArch64/basic-a64-unpredictable.txt.cs`** -> AI Confidence: **99.29%**
137. **`suite/MC/AArch64/colored.txt.cs`** -> AI Confidence: **99.29%**
138. **`suite/MC/AArch64/gicv3-regs.txt.cs`** -> AI Confidence: **99.29%**
139. **`suite/MC/AArch64/ldp-offset-predictable.txt.cs`** -> AI Confidence: **99.29%**
140. **`suite/MC/AArch64/ldp-postind.predictable.txt.cs`** -> AI Confidence: **99.29%**
141. **`suite/MC/AArch64/ldp-preind.predictable.txt.cs`** -> AI Confidence: **99.29%**
142. **`suite/MC/AArch64/marked-up.txt.cs`** -> AI Confidence: **99.29%**
143. **`suite/MC/AArch64/neon-bitwise-instructions.s.cs`** -> AI Confidence: **99.29%**
144. **`suite/MC/AArch64/neon-simd-misc.s.cs`** -> AI Confidence: **99.29%**
145. **`suite/MC/AArch64/trace-regs.txt.cs`** -> AI Confidence: **99.29%**
146. **`suite/MC/ARC/alu_arc.s.cs`** -> AI Confidence: **99.29%**
147. **`suite/MC/ARM/arm-aliases.s.cs`** -> AI Confidence: **99.29%**
148. **`suite/MC/ARM/arm-arithmetic-aliases.s.cs`** -> AI Confidence: **99.29%**
149. **`suite/MC/ARM/arm_instructions.s.cs`** -> AI Confidence: **99.29%**
150. **`suite/MC/ARM/negative-immediates.s.cs`** -> AI Confidence: **99.29%**
151. **`suite/MC/ARM/thumb-shift-encoding.s.cs`** -> AI Confidence: **99.29%**
152. **`suite/MC/ARM/thumb2-narrow-dp.ll.cs`** -> AI Confidence: **99.29%**
153. **`suite/MC/Alpha/insn-alpha-be.s.cs`** -> AI Confidence: **99.29%**
154. **`suite/MC/Alpha/insn-alpha.s.cs`** -> AI Confidence: **99.29%**
155. **`suite/MC/BPF/classic-all.cs`** -> AI Confidence: **99.29%**
156. **`suite/MC/BPF/extended-all.cs`** -> AI Confidence: **99.29%**
157. **`suite/MC/HPPA/alu11.s.cs`** -> AI Confidence: **99.29%**
158. **`suite/MC/HPPA/computation20.s.cs`** -> AI Confidence: **99.29%**
159. **`suite/MC/HPPA/float11.s.cs`** -> AI Confidence: **99.29%**
160. **`suite/MC/HPPA/sysctrl20.s.cs`** -> AI Confidence: **99.29%**
161. **`suite/MC/HPPA/system_op11.s.cs`** -> AI Confidence: **99.29%**
162. **`suite/MC/LoongArch/arith.s.cs`** -> AI Confidence: **99.29%**
163. **`suite/MC/LoongArch/misc.s.cs`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `bindings/python/tests/test_skipdata.py` -> **99.9473%** Exposure
- `bindings/python/tests/test_compatibility_layer.py` -> **97.458%** Exposure
- `bindings/java/TestX86.java` -> **66.9082%** Exposure
- `bindings/java/TestArm.java` -> **0.5803%** Exposure
- `bindings/java/TestArm64.java` -> **0.0757%** Exposure
### Exploit Generation Surface
- `bindings/java/TestArm.java` -> **100.0%** Exposure
- `bindings/java/TestArm64.java` -> **100.0%** Exposure
- `bindings/java/TestM680x.java` -> **100.0%** Exposure
- `bindings/java/TestMips.java` -> **100.0%** Exposure
- `bindings/java/TestPpc.java` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `Makefile` -> **100.0%** Exposure
- `make.sh` -> **100.0%** Exposure
- `bindings/python/setup.py` -> **100.0%** Exposure
- `arch/X86/X86MappingInsnName_reduce.inc` -> **40.438%** Exposure
- `suite/auto-sync/src/autosync/MCUpdater.py` -> **1.1112%** Exposure
### Raw Memory Manipulation
- `MCInst.c` -> **10.0%** Exposure
- `suite/cstest/src/test_case.c` -> **10.0%** Exposure
- `suite/cstest/src/test_detail.c` -> **10.0%** Exposure
- `suite/cstest/src/test_detail_aarch64.c` -> **10.0%** Exposure
- `suite/cstest/src/test_detail_arm.c` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `MCInst.c` -> **100.0%** Exposure
- `MCInstPrinter.c` -> **100.0%** Exposure
- `Mapping.c` -> **100.0%** Exposure
- `arch/AArch64/AArch64Disassembler.c` -> **100.0%** Exposure
- `arch/AArch64/AArch64InstPrinter.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `49` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2024` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `arch/AArch64/AArch64InstPrinter.c` (C) -> Cumulative Risk: **775.32**
- **Archetype:** `file_cluster_8` (Distance: 12.964 IQR)
- **Magnitude:** 1485.4 | **LOC:** 2600 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `getNextVectorRegister` (Impact: 298.4), `printAdrAdrpLabel` (Impact: 185.3), `printVectorList` (Impact: 60.8)

### 2. `make.sh` (SHELL) -> Cumulative Risk: **763.26**
- **Archetype:** `file_cluster_12` (Distance: 14.271 IQR)
- **Magnitude:** 156.5 | **LOC:** 156 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `build_android` (Impact: 27.4), `install` (Impact: 14.8), `uninstall` (Impact: 10.6)

### 3. `arch/RISCV/RISCVDisassembler.c` (C) -> Cumulative Risk: **762.16**
- **Archetype:** `file_cluster_8` (Distance: 12.431 IQR)
- **Magnitude:** 639.56 | **LOC:** 754 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `RISCV_getInstruction` (Impact: 23.2), `decodeXTHeadMemPair` (Impact: 7.3), `DecodeGPRRegisterClass` (Impact: 6.7)

### 4. `bindings/python/cstest_py/src/cstest_py/cstest.py` (PYTHON) -> Cumulative Risk: **761.2**
- **Archetype:** `file_cluster_8` (Distance: 11.862 IQR)
- **Magnitude:** 659.98 | **LOC:** 489 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__str__` (Impact: 72.4), `__init__` (Impact: 71.5), `setup` (Impact: 58.8)

### 5. `arch/X86/X86ATTInstPrinter.c` (C) -> Cumulative Risk: **758.65**
- **Archetype:** `file_cluster_8` (Distance: 13.021 IQR)
- **Magnitude:** 986.44 | **LOC:** 1204 | **CtrlFlow:** 84.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.9997%)
- **Heaviest Functions:** `printOperand` (Impact: 146.0), `printMemReference` (Impact: 55.9), `printopaquemem` (Impact: 44.9)

### 6. `arch/M68K/M68KDisassembler.c` (C) -> Cumulative Risk: **757.59**
- **Archetype:** `file_cluster_8` (Distance: 13.568 IQR)
- **Magnitude:** 2426.02 | **LOC:** 3946 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `d68020_cpgen` (Impact: 122.9), `get_ea_mode_op` (Impact: 90.2), `get_with_index_address_mode` (Impact: 58.2)

### 7. `arch/Sparc/SparcInstPrinter.c` (C) -> Cumulative Risk: **757.49**
- **Archetype:** `file_cluster_13` (Distance: 12.852 IQR)
- **Magnitude:** 475.66 | **LOC:** 342 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `printCCOperand` (Impact: 61.0), `printSparcAliasInstr` (Impact: 47.0), `printOperand` (Impact: 29.8)

### 8. `arch/Sparc/SparcDisassembler.c` (C) -> Cumulative Risk: **754.61**
- **Archetype:** `file_cluster_13` (Distance: 12.835 IQR)
- **Magnitude:** 391.78 | **LOC:** 356 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getInstruction` (Impact: 10.7), `DecodeIntPairRegisterClass` (Impact: 6.8), `DecodeQFPRegsRegisterClass` (Impact: 6.7)

### 9. `arch/X86/X86IntelInstPrinter.c` (C) -> Cumulative Risk: **751.93**
- **Archetype:** `file_cluster_8` (Distance: 13.007 IQR)
- **Magnitude:** 1050.08 | **LOC:** 1274 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.9996%)
- **Heaviest Functions:** `printImm` (Impact: 127.7), `printOperand` (Impact: 107.5), `printopaquemem` (Impact: 57.8)

### 10. `arch/Xtensa/XtensaMapping.c` (C) -> Cumulative Risk: **751.87**
- **Archetype:** `file_cluster_13` (Distance: 12.68 IQR)
- **Magnitude:** 329.66 | **LOC:** 278 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Xtensa_add_cs_detail_0` (Impact: 60.5), `Xtensa_reg_access` (Impact: 28.2), `Xtensa_disasm` (Impact: 6.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.387 IQR)
- **Top Global Matches:** file_cluster_17: 12.387, file_cluster_8: 12.765, file_cluster_11: 12.915
- **Magnitude:** 5496.97 | **LOC:** 672 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (63.0198%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 120`, `args: 7`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 10`, `state_mutation: 353`, `dead_code: 2`
* *Architecture:* `io: 68`, `api: 4`, `import: 4`
* *Defense:* `safety: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` $(AUTODEPS), pkgconfig.mk, config.mk, functions.mk
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `include/capstone/arm64.h` (C | Tier 4 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.537 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.157 IQR)
- **Top Global Matches:** file_cluster_8: 13.537, file_cluster_7: 13.998, file_cluster_13: 14.112
- **Magnitude:** 4582.36 | **LOC:** 4664 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (43.5464%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ARM64CC_getCondCodeName` (Impact: 21.9 | O(N^1))
  * `ARM64CC_getNZCVToSatisfyCondCode` (Impact: 19.8 | O(N^1) | DB: 4)
  * `ARM64CC_isReflexive` (Impact: 11.8 | O(N^1))
  * `ARM64CC_isIrreflexive` (Impact: 9.7 | O(N^1))
  * `ARM64CC_getInvertedCondCode` (Impact: 1.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 111`, `func_start: 5`, `class_start: 30`
* *Risk/State:* `state_mutation: 4321`
* *Architecture:* `api: 106`, `import: 4`
* *Defense:* `safety: 3`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.436
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` assert.h, platform.h, cs_operand.h, aarch64.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `arch/HPPA/HPPADisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.06 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.822 IQR)
- **Top Global Matches:** file_cluster_8: 12.06, file_cluster_7: 12.476, file_cluster_13: 12.6
- **Magnitude:** 3581.82 | **LOC:** 3841 | **CtrlFlow:** 79.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (62.3257%), Tech Debt (7.8765%)
**Top Internal Functions/Classes:**
  * `getInstruction` (Impact: 147.5 | O(N^3) | DB: 2)
  * `fill_alu_mods` (Impact: 147.2 | O(N^2) | DB: 6)
  * `decode_copr` (Impact: 122.6 | O(N^3) | DB: 17)
  * `fill_alu_insn_name` (Impact: 112.2 | O(N^1) | DB: 1)
  * `fill_idxmem_mods` (Impact: 93.4 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1650`, `structural_boundaries: 420`, `args: 10`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 746`, `orphaned_logic: 1`
* *Architecture:* `api: 492`, `import: 8`
* *Defense:* `safety: 4`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` stdio.h, Mapping.h, HPPAConstants.h, HPPADisassembler.h, MathExtras.h, utils.h, string.h, stddef.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/ARM/ARMDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.997 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.357 IQR)
- **Top Global Matches:** file_cluster_8: 12.997, file_cluster_13: 13.093, file_cluster_7: 13.222
- **Magnitude:** 3022.14 | **LOC:** 7307 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 106
- **Risk Profile:** Cognitive Load (85.4216%), Tech Debt (10.5788%)
**Top Internal Functions/Classes:**
  * `DecodeMemMultipleWritebackInstruction` (Impact: 897.2 | O(N^3) | DB: 106)
  * `DecodeAddrMode3Instruction` (Impact: 307.9 | O(N^3) | DB: 36)
  * `DecodeAddrMode2IdxInstruction` (Impact: 88.0 | O(N^2) | DB: 25)
  * `checkDecodedInstruction` (Impact: 28.5 | O(N^2) | DB: 2)
    * *Intent:* #include "ARMGenDisassemblerTables.inc" // Post-decoding checks
  * `AddThumb1SBit` (Impact: 23.2 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 568`, `structural_boundaries: 470`, `args: 2`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `state_mutation: 720`, `dead_code: 4`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 842`, `import: 23`
* *Defense:* `safety: 2`, `doc: 20`, `immutability_locks: 237`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` stdio.h, ARMBaseInfo.h, string.h, utils.h, MCRegisterInfo.h, LEB128.h, MCDisassembler.h, MathExtras.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/python/cstest_py/src/cstest_py/details.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.994 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.845 IQR)
- **Top Global Matches:** file_cluster_8: 8.994, file_cluster_7: 9.812, file_cluster_13: 9.937
- **Magnitude:** 2720.96 | **LOC:** 1589 | **CtrlFlow:** 45.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (21.7989%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_expected_arm` (Impact: 253.4 | O(N^4))
  * `test_expected_aarch64` (Impact: 242.7 | O(N^4))
  * `test_expected_x86` (Impact: 204.9 | O(N^4))
  * `test_expected_m68k` (Impact: 187.8 | O(N^4))
  * `test_expected_tms320c64x` (Impact: 165.0 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 570`, `structural_boundaries: 685`, `args: 25`, `func_start: 25`
* *Risk/State:* None
* *Architecture:* `api: 26`, `import: 26`
* *Defense:* `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` capstone.wasm_const, capstone.loongarch_const, capstone.aarch64_const, capstone.tms320c64x_const, capstone.systemz_const, cstest_py.compare, capstone.tricore_const, capstone.mips_const...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `arch/M68K/M68KDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.568 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.37 IQR)
- **Top Global Matches:** file_cluster_8: 13.568, file_cluster_7: 13.841, file_cluster_13: 13.91
- **Magnitude:** 2426.02 | **LOC:** 3946 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^3) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (84.4055%), Tech Debt (97.5113%)
**Top Internal Functions/Classes:**
  * `d68020_cpgen` (Impact: 122.9 | O(N^1) | DB: 48)
  * `get_ea_mode_op` (Impact: 90.2 | O(N^1) | DB: 30)
  * `get_with_index_address_mode` (Impact: 58.2 | O(N^2) | DB: 31)
  * `d68010_movec` (Impact: 42.0 | O(N^1) | DB: 25)
  * `fmovem` (Impact: 15.6 | O(N^2) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 410`, `structural_boundaries: 427`, `args: 4`, `func_start: 371`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1325`, `orphaned_logic: 188`
* *Architecture:* `io: 16`, `api: 310`, `import: 12`
* *Defense:* `safety: 1`, `doc: 39`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` stdlib.h, cs_priv.h, MCRegisterInfo.h, stdio.h, M68KInstPrinter.h, MCInstrDesc.h, string.h, MathExtras.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/X86/X86DisassemblerDecoder.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.854 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.356 IQR)
- **Top Global Matches:** file_cluster_13: 13.854, file_cluster_8: 13.969, file_cluster_7: 14.064
- **Magnitude:** 2419.18 | **LOC:** 2573 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 106
- **Risk Profile:** Cognitive Load (48.6933%), Tech Debt (19.7713%)
**Top Internal Functions/Classes:**
  * `readPrefixes` (Impact: 1954.1 | O(2^N) | DB: 106)
    * *Intent:* // return decision->opcodeDecisions[insnContext].modRMDecisions[opcode].modrm_type != MODRM_ONEENTRY...
  * `setSegmentOverride` (Impact: 28.6 | O(N^2) | DB: 4)
  * `consumeByte` (Impact: 3.9 | O(N^1) | DB: 2)
    * *Intent:* #ifdef CAPSTONE_X86_REDUCE #include "X86GenDisassemblerTables_reduce.inc" #include "X86GenDisassembl...
  * `unconsumeByte` (Impact: 2.2 | O(N^1) | DB: 1)
  * `lookAtByte` (Impact: 1.9 | O(N^1))
    * *Intent:* #include "X86GenDisassemblerTables_reduce.inc" #include "X86GenDisassemblerTables_reduce2.inc" #incl...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 106`, `args: 16`, `func_start: 16`, `class_start: 5`
* *Risk/State:* `state_mutation: 340`, `dead_code: 2`, `fragile_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 75`, `import: 14`
* *Defense:* `safety: 1`, `doc: 51`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` stdlib.h, cs_priv.h, X86GenDisassemblerTables.inc, X86Lookup16.inc, X86GenInstrInfo.inc, X86Mapping.h, libkern.h, stdarg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.448 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.974 IQR)
- **Top Global Matches:** file_cluster_13: 14.448, file_cluster_8: 14.492, file_cluster_11: 14.628
- **Magnitude:** 2180.78 | **LOC:** 2179 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 73
- **Risk Profile:** Cognitive Load (92.3023%), Tech Debt (65.3303%)
**Top Internal Functions/Classes:**
  * `cs_op_index` (Impact: 188.8 | O(N^2) | DB: 73)
  * `cs_op_count` (Impact: 96.8 | O(N^1) | DB: 67)
  * `cs_option` (Impact: 75.3 | O(N^3) | DB: 29)
  * `cs_disasm` (Impact: 70.2 | O(N^2) | DB: 70)
  * `fill_insn` (Impact: 56.0 | O(N^3) | DB: 12)
    * *Intent:* #endif // fill insn with mnemonic & operands info
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 497`, `structural_boundaries: 268`, `args: 28`, `func_start: 41`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1085`, `dead_code: 4`, `fragile_debt: 1`, `orphaned_logic: 36`
* *Architecture:* `api: 309`, `import: 35`
* *Defense:* `safety: 31`, `doc: 3`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` Availability.h, stdio.h, HPPAModule.h, ARCModule.h, TriCoreModule.h, XtensaModule.h, string.h, M680XModule.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/SH/SHDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.117 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.023 IQR)
- **Top Global Matches:** file_cluster_8: 13.117, file_cluster_7: 13.399, file_cluster_13: 13.407
- **Magnitude:** 2121.56 | **LOC:** 2184 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (84.8989%), Tech Debt (52.3771%)
**Top Internal Functions/Classes:**
  * `decode_dsp_3op` (Impact: 150.6 | O(N^3) | DB: 28)
  * `sh_disassemble` (Impact: 44.1 | O(N^2) | DB: 16)
  * `opfxxd` (Impact: 41.5 | O(N^2) | DB: 32)
  * `op0xx3` (Impact: 32.9 | O(N^2) | DB: 13)
  * `decode_long` (Impact: 29.8 | O(N^1) | DB: 36)
    * *Intent:* #include "SHInsnTable.inc"
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 420`, `structural_boundaries: 312`, `args: 2`, `func_start: 84`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 883`, `orphaned_logic: 52`
* *Architecture:* `io: 76`, `api: 445`, `import: 9`
* *Defense:* `safety: 1`, `doc: 18`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cs_priv.h, stdarg.h, sh.h, MCDisassembler.h, string.h, MCInst.h, SHDisassembler.h, utils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/ARM/ARMMapping.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.723 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.67 IQR)
- **Top Global Matches:** file_cluster_8: 13.723, file_cluster_13: 13.774, file_cluster_7: 13.886
- **Magnitude:** 2044.44 | **LOC:** 2268 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 236
- **Risk Profile:** Cognitive Load (71.5753%), Tech Debt (11.1784%)
**Top Internal Functions/Classes:**
  * `add_alias_details` (Impact: 819.1 | O(N^3) | DB: 236)
  * `ARM_add_cs_groups` (Impact: 17.3 | O(N^1) | DB: 1)
    * *Intent:* /// Adds group to the instruction which are not defined in LLVM.
  * `patch_cs_reg_alias` (Impact: 16.7 | O(N^1) | DB: 34)
    * *Intent:* /// Patches the register names with Capstone specific alias. /// Those are common alias for register...
  * `get_custom_reg_alias` (Impact: 16.6 | O(N^1))
  * `ARM_reg_name` (Impact: 9.3 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 426`, `structural_boundaries: 161`, `args: 2`, `func_start: 25`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 815`, `orphaned_logic: 5`
* *Architecture:* `api: 309`, `import: 16`
* *Defense:* `safety: 6`, `doc: 38`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` stdio.h, ARMBaseInfo.h, ARMGenCSMappingInsn.inc, cs_simple_types.h, ARMGenCSMappingInsnName.inc, string.h, arm.h, Mapping.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/M680X/M680XDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.685 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.266 IQR)
- **Top Global Matches:** file_cluster_8: 13.685, file_cluster_13: 13.836, file_cluster_7: 13.926
- **Magnitude:** 2017.26 | **LOC:** 2343 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (80.5715%), Tech Debt (20.0025%)
**Top Internal Functions/Classes:**
  * `is_sufficient_code_size` (Impact: 126.3 | O(N^2) | DB: 47)
  * `indexed09_hdlr` (Impact: 57.2 | O(N^1) | DB: 44)
    * *Intent:* // M6809/M6309 indexed mode handler
  * `decode_insn` (Impact: 34.2 | O(N^2) | DB: 29)
    * *Intent:* // Check for a valid M680X instruction AND for enough bytes in the code buffer // Return an instruct...
  * `indexed12_hdlr` (Impact: 31.5 | O(N^1) | DB: 31)
    * *Intent:* // CPU12 indexed mode handler
  * `m680x_disassemble` (Impact: 31.4 | O(N^2) | DB: 17)
    * *Intent:* }; /* handler function pointers */ /* Disasemble one instruction at address and store in str_buff */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 231`, `args: 1`, `func_start: 65`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1041`, `fragile_debt: 6`, `orphaned_logic: 4`
* *Architecture:* `api: 281`, `import: 23`
* *Defense:* `safety: 3`, `doc: 26`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` stdio.h, m6811.inc, string.h, utils.h, MCRegisterInfo.h, M680XDisassembler.h, cpu12.inc, MCInst.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/TriCore/TriCoreDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.36 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.638 IQR)
- **Top Global Matches:** file_cluster_8: 13.36, file_cluster_13: 13.468, file_cluster_7: 13.661
- **Magnitude:** 1909.26 | **LOC:** 1752 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (70.5679%), Tech Debt (9.6269%)
**Top Internal Functions/Classes:**
  * `DecodeBOInstruction` (Impact: 81.2 | O(N^3) | DB: 16)
  * `DecodeRRInstruction` (Impact: 49.6 | O(N^3) | DB: 10)
  * `DecodeSROInstruction` (Impact: 26.4 | O(N^1) | DB: 5)
  * `DecodeBOLInstruction` (Impact: 24.1 | O(N^1) | DB: 12)
  * `DecodeSCInstruction` (Impact: 23.8 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 281`, `args: 1`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `state_mutation: 788`, `orphaned_logic: 3`
* *Architecture:* `api: 587`, `import: 19`
* *Defense:* `safety: 3`, `doc: 3`, `immutability_locks: 124`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` stdlib.h, cs_priv.h, MCRegisterInfo.h, MathExtras.h, TriCoreDisassembler.h, TriCoreLinkage.h, stdio.h, MCDisassembler.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/ocaml/ocaml.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.78 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.208 IQR)
- **Top Global Matches:** file_cluster_8: 12.78, file_cluster_7: 13.207, file_cluster_13: 13.286
- **Magnitude:** 1706.56 | **LOC:** 2132 | **CtrlFlow:** 96.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 172
- **Risk Profile:** Cognitive Load (90.0095%), Tech Debt (11.6899%)
**Top Internal Functions/Classes:**
  * `_cs_disasm` (Impact: 472.9 | O(N^3) | DB: 172)
  * `ocaml_cs_disasm` (Impact: 132.2 | O(N^2) | DB: 46)
  * `ocaml_open` (Impact: 90.4 | O(N^1) | DB: 43)
  * `ocaml_option` (Impact: 16.7 | O(N^1) | DB: 7)
  * `list_count` (Impact: 3.5 | O(N^1) | DB: 2)
    * *Intent:* /* By Nguyen Anh Quynh <aquynh@gmail.com>, 2013> */ #include <stdio.h> // debug #include <string.h> ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 12`, `args: 1`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 834`, `dead_code: 1`, `orphaned_logic: 9`
* *Architecture:* `api: 105`, `import: 7`
* *Defense:* `safety: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdio.h, fail.h, memory.h, alloc.h, string.h, mlvalues.h, capstone.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/Mips/MipsDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.653 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.127 IQR)
- **Top Global Matches:** file_cluster_8: 12.653, file_cluster_7: 12.99, file_cluster_0: 13.001
- **Magnitude:** 1497.86 | **LOC:** 3432 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (89.7897%), Tech Debt (83.0893%)
**Top Internal Functions/Classes:**
  * `DecodeMemMMImm4` (Impact: 50.8 | O(N^2) | DB: 3)
  * `DecodeMovePRegPair` (Impact: 30.6 | O(N^2))
  * `DecodePOP65GroupBranchMMR6` (Impact: 17.9 | O(N^3) | DB: 5)
    * *Intent:* // end anonymous namespace // Forward declare these because the autogenerated code will reference th...
  * `DecodePOP75GroupBranchMMR6` (Impact: 17.9 | O(N^3) | DB: 5)
  * `DecodeMemMMReglistImm4Lsl2` (Impact: 17.2 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 246`, `func_start: 74`
* *Risk/State:* `state_mutation: 496`, `dead_code: 3`, `orphaned_logic: 52`
* *Architecture:* `api: 474`, `import: 1`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdlib.h, MCRegisterInfo.h, MathExtras.h, cs_priv.h, stdio.h, platform.h, MCDisassembler.h, MipsGenDisassemblerTables.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/AArch64/AArch64InstPrinter.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.964 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.088 IQR)
- **Top Global Matches:** file_cluster_8: 12.964, file_cluster_7: 13.315, file_cluster_13: 13.415
- **Magnitude:** 1485.4 | **LOC:** 2600 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^3) | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (96.2632%), Tech Debt (77.2147%)
**Top Internal Functions/Classes:**
  * `getNextVectorRegister` (Impact: 298.4 | O(N^1) | DB: 81)
  * `printAdrAdrpLabel` (Impact: 185.3 | O(N^2) | DB: 38)
  * `printVectorList` (Impact: 60.8 | O(N^3) | DB: 13)
  * `printArithExtend` (Impact: 23.6 | O(N^3) | DB: 5)
  * `printMemExtendImpl` (Impact: 16.1 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 120`, `args: 3`, `func_start: 41`
* *Risk/State:* `state_mutation: 538`, `fragile_debt: 4`, `orphaned_logic: 25`
* *Architecture:* `api: 261`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` stdlib.h, MCRegisterInfo.h, AArch64Linkage.h, AArch64Mapping.h, stdio.h, AArch64InstPrinter.h, platform.h, AArch64AddressingModes.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/vb6/CX86Operand.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.207 IQR)
- **Top Global Matches:** file_cluster_13: 11.207, file_cluster_8: 11.425, file_cluster_0: 11.992
- **Magnitude:** 1345.95 | **LOC:** 203 | **CtrlFlow:** 97.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (71.145%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 1`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 59`
* *Architecture:* `import: 30`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/AArch64/AArch64AddressingModes.h` (C | Tier 4 | 🚨 AI THREAT: 99.05%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.937 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.884 IQR)
- **Top Global Matches:** file_cluster_8: 13.937, file_cluster_13: 14.023, file_cluster_7: 14.031
- **Magnitude:** 1335.08 | **LOC:** 1003 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (39.6134%), Tech Debt (13.1302%)
**Top Internal Functions/Classes:**
  * `AArch64_AM_isAdvSIMDModImmType10` (Impact: 56.3 | O(N^2) | DB: 17)
    * *Intent:* // aaaaaaaa bbbbbbbb cccccccc dddddddd eeeeeeee ffffffff gggggggg hhhhhhhh // cmode: 1110, op: 1
  * `AArch64_AM_processLogicalImmediate` (Impact: 29.1 | O(N^3) | DB: 17)
    * *Intent:* /// processLogicalImmediate - Determine if an immediate value can be encoded /// as the immediate op...
  * `AArch64_AM_getExtendType` (Impact: 21.9 | O(N^1))
    * *Intent:* /// getExtendType - Extract the extend type for operands of arithmetic ops.
  * `AArch64_AM_getExtendEncoding` (Impact: 21.6 | O(N^1))
    * *Intent:* /// Mapping from extend bits to required operation: /// shifter: 000 ==> uxtb /// 001 ==> uxth /// 0...
  * `AArch64_AM_getShiftExtendName` (Impact: 18.8 | O(N^1))
    * *Intent:* /// getShiftName - Get the string encoding for the shift type.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 176`, `args: 8`, `func_start: 64`, `class_start: 5`
* *Risk/State:* `state_mutation: 704`, `fragile_debt: 3`
* *Architecture:* `api: 254`, `import: 7`
* *Defense:* `safety: 1`, `doc: 61`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.841
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdlib.h, stdio.h, platform.h, assert.h, string.h, MathExtras.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `arch/AArch64/AArch64Mapping.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.995 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.267 IQR)
- **Top Global Matches:** file_cluster_8: 12.995, file_cluster_13: 13.036, file_cluster_7: 13.181
- **Magnitude:** 1257.14 | **LOC:** 2910 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^2) | **DB Complexity:** 87
- **Risk Profile:** Cognitive Load (70.3334%), Tech Debt (22.6489%)
**Top Internal Functions/Classes:**
  * `AArch64_add_vas` (Impact: 517.9 | O(N^2) | DB: 87)
    * *Intent:* /// Very annoyingly LLVM hard codes the vector layout post-fixes into the asm string. /// In this fu...
  * `sme_reg_to_vas` (Impact: 37.2 | O(N^1))
    * *Intent:* #endif // CAPSTONE_DIET
  * `AArch64_set_detail_op_sme` (Impact: 24.7 | O(N^2) | DB: 21)
  * `AArch64_set_detail_op_pred` (Impact: 10.2 | O(N^1) | DB: 6)
  * `aarch64_exact_fp_to_fp` (Impact: 8.8 | O(N^1))
    * *Intent:* #include "../../cs_simple_types.h" #include "../../Mapping.h" #include "../../MathExtras.h" #include...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 105`, `args: 3`, `func_start: 24`
* *Risk/State:* `state_mutation: 350`, `orphaned_logic: 9`
* *Architecture:* `api: 249`, `import: 14`
* *Defense:* `doc: 24`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` aarch64.h, AArch64Linkage.h, AArch64Mapping.h, AArch64GenCSMappingInsnOp.inc, stdio.h, AArch64GenCSAliasMnemMap.inc, AArch64GenCSFeatureName.inc, AArch64AddressingModes.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/vb6/CDisassembler.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.547 IQR)
- **Top Global Matches:** file_cluster_13: 11.547, file_cluster_8: 11.852, file_cluster_0: 12.265
- **Magnitude:** 1081.51 | **LOC:** 154 | **CtrlFlow:** 94.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (78.5691%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 2`, `args: 7`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 59`
* *Architecture:* `import: 22`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/WASM/WASMDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.109 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.619 IQR)
- **Top Global Matches:** file_cluster_0: 14.109, file_cluster_13: 14.147, file_cluster_11: 14.168
- **Magnitude:** 1079.2 | **LOC:** 1066 | **CtrlFlow:** 75.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (95.0314%), Tech Debt (8.8784%)
**Top Internal Functions/Classes:**
  * `WASM_getInstruction` (Impact: 353.8 | O(N^2) | DB: 60)
  * `get_varuint64` (Impact: 13.4 | O(N^2) | DB: 7)
    * *Intent:* // input | code : code pointer start from varuint64 // | code_len : real code len count from varint ...
  * `read_brtable` (Impact: 13.4 | O(N^1) | DB: 18)
    * *Intent:* // input | code : code pointer start from brtable // | code_len : start from the code pointer to the...
  * `get_varuint32` (Impact: 13.3 | O(N^2) | DB: 7)
    * *Intent:* // input | code: code pointer start from varuint32 // | code_len: real code len count from varint //...
  * `read_memoryimmediate` (Impact: 8.2 | O(N^1) | DB: 17)
    * *Intent:* // input | code : code pointer start from memoryimmediate // | code_len : start from the code pointe...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 86`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 395`, `dead_code: 12`, `orphaned_logic: 1`
* *Architecture:* `api: 237`, `import: 5`
* *Defense:* `safety: 19`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cs_priv.h, WASMDisassembler.h, string.h, WASMMapping.h, stddef.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/Xtensa/XtensaDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.414 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.045 IQR)
- **Top Global Matches:** file_cluster_8: 12.414, file_cluster_13: 12.539, file_cluster_7: 12.738
- **Magnitude:** 1054.56 | **LOC:** 1140 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (81.6928%), Tech Debt (94.1111%)
**Top Internal Functions/Classes:**
  * `CheckRegister` (Impact: 166.8 | O(N^2) | DB: 49)
    * *Intent:* // Verify SR and UR
  * `getInstruction` (Impact: 26.5 | O(N^2) | DB: 16)
  * `decodeBranchOperand` (Impact: 13.2 | O(N^1))
  * `decodeOffset_256_16Operand` (Impact: 8.6 | O(N^3))
  * `readInstruction24` (Impact: 6.9 | O(N^2) | DB: 3)
    * *Intent:* /// Read three bytes from the ArrayRef and return 24 bit data
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 178`, `args: 1`, `func_start: 63`
* *Risk/State:* `state_mutation: 309`, `dead_code: 2`, `orphaned_logic: 50`
* *Architecture:* `api: 295`, `import: 13`
* *Defense:* `safety: 6`, `doc: 5`, `immutability_locks: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdlib.h, cs_priv.h, stdio.h, platform.h, MCDisassembler.h, XtensaGenDisassemblerTables.inc, XtensaGenInstrInfo.inc, MCFixedLenDisassembler.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/X86/X86IntelInstPrinter.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.007 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.191 IQR)
- **Top Global Matches:** file_cluster_8: 13.007, file_cluster_13: 13.168, file_cluster_7: 13.376
- **Magnitude:** 1050.08 | **LOC:** 1274 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (91.5043%), Tech Debt (88.969%)
**Top Internal Functions/Classes:**
  * `printImm` (Impact: 127.7 | O(N^3) | DB: 6)
  * `printOperand` (Impact: 107.5 | O(N^3) | DB: 28)
  * `printopaquemem` (Impact: 57.8 | O(N^1) | DB: 7)
  * `printMemReference` (Impact: 42.1 | O(N^2) | DB: 23)
  * `printanymem` (Impact: 21.6 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 279`, `structural_boundaries: 78`, `args: 1`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 395`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 30`
* *Architecture:* `api: 120`, `import: 21`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` X86InstPrinter.h, X86GenAsmWriter1.inc, Availability.h, stdio.h, string.h, utils.h, MCRegisterInfo.h, libkern.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/X86/X86ATTInstPrinter.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.021 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.225 IQR)
- **Top Global Matches:** file_cluster_8: 13.021, file_cluster_13: 13.202, file_cluster_7: 13.373
- **Magnitude:** 986.44 | **LOC:** 1204 | **CtrlFlow:** 84.9% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^3) | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (91.9172%), Tech Debt (89.4798%)
**Top Internal Functions/Classes:**
  * `printOperand` (Impact: 146.0 | O(N^3) | DB: 29)
  * `printMemReference` (Impact: 55.9 | O(N^3) | DB: 20)
  * `printopaquemem` (Impact: 44.9 | O(N^1) | DB: 7)
  * `_printOperand` (Impact: 24.2 | O(N^1) | DB: 6)
  * `printanymem` (Impact: 21.6 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 55`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `state_mutation: 374`, `planned_debt: 1`, `orphaned_logic: 30`
* *Architecture:* `api: 166`, `import: 21`
* *Defense:* `safety: 1`, `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` X86InstPrinter.h, Availability.h, stdio.h, string.h, utils.h, MCRegisterInfo.h, libkern.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/AArch64/AArch64BaseInfo.h` (C | Tier 0 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.509 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.672 IQR)
- **Top Global Matches:** file_cluster_8: 10.509, file_cluster_13: 10.532, file_cluster_7: 10.729
- **Magnitude:** 984.9 | **LOC:** 987 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.079%), Tech Debt (11.4865%)
**Top Internal Functions/Classes:**
  * `atomicBarrierDroppedOnZero` (Impact: 132.1 | O(N^1))
  * `getWRegFromXReg` (Impact: 64.3 | O(N^1))
    * *Intent:* #define GET_SUBTARGETINFO_ENUM #include "AArch64GenSubtargetInfo.inc" #define GET_REGINFO_ENUM #defi...
  * `getXRegFromWReg` (Impact: 64.3 | O(N^1))
  * `getBRegFromDReg` (Impact: 62.4 | O(N^1))
  * `getDRegFromBReg` (Impact: 62.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 201`, `args: 10`, `func_start: 10`, `class_start: 11`
* *Risk/State:* `state_mutation: 33`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 448`, `import: 31`
* *Defense:* `doc: 53`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.742
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdlib.h, aarch64.h, AArch64GenInstrInfo.inc, stdio.h, platform.h, AArch64GenSystemOperands.inc, AArch64GenRegisterInfo.inc, AArch64GenSubtargetInfo.inc...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `include/capstone/aarch64.h` (C | Tier 4 | 🚨 AI THREAT: 98.77%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.367 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.213 IQR)
- **Top Global Matches:** file_cluster_8: 11.367, file_cluster_7: 11.846, file_cluster_1: 12.082
- **Magnitude:** 941.28 | **LOC:** 4865 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 743
- **Risk Profile:** Cognitive Load (25.0502%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `AArch64CC_getCondCodeName` (Impact: 21.9 | O(N^1))
  * `AArch64CC_getInvertedCondCode` (Impact: 7.5 | O(N^1) | DB: 743)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 40`, `func_start: 2`, `class_start: 11`
* *Risk/State:* `state_mutation: 810`
* *Architecture:* `api: 45`, `import: 3`
* *Defense:* `safety: 2`, `doc: 39`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.621
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, platform.h, cs_operand.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `arch/WASM/WASMDisassembler.c` (C) | Magnitude: 1079.2 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 807, pointers: 450, state_mutation: 395, branch: 261
- `arch/AArch64/AArch64Disassembler.c` (C) | Magnitude: 540.72 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 316, api: 184, state_mutation: 170, branch: 114

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `bindings/java/run.sh` (SHELL) | Magnitude: 18.98 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, reflection_metaprogramming: 12, structural_boundaries: 8, io: 8
- `make.sh` (SHELL) | Magnitude: 156.5 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 99, state_mutation: 73, reflection_metaprogramming: 40, branch: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cstool/cstool_arc.c` (C) | Magnitude: 88.78 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 53, state_mutation: 33, branch: 25, pointers: 18
- `suite/cstest/src/test_detail_m68k.c` (C) | Magnitude: 240.54 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 215, indent_tabs: 157, state_mutation: 115, branch: 48
- `arch/XCore/XCoreInstPrinter.h` (C) | Magnitude: 17.68 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 8, structural_boundaries: 4, api: 3, import: 3
- `arch/Xtensa/XtensaInstPrinter.h` (C) | Magnitude: 17.24 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 5, macros: 4, pointers: 3, api: 2
- `suite/auto-sync/src/autosync/cpptranslator/patches/TemplateDefinition.py` (PYTHON) | Magnitude: 26.02 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 21, api: 7, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `suite/auto-sync/src/autosync/Helper.py` (PYTHON) | Magnitude: 211.4 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 56, api: 24, branch: 23
- `suite/auto-sync/src/autosync/cpptranslator/patches/Override.py` (PYTHON) | Magnitude: 22.76 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 14, api: 7, args: 4
- `suite/auto-sync/src/autosync/cpptranslator/patches/SignExtend.py` (PYTHON) | Magnitude: 23.06 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 16, api: 7, args: 4
- `suite/auto-sync/src/autosync/cpptranslator/patches/isUInt.py` (PYTHON) | Magnitude: 23.16 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 16, api: 7, args: 4
- `suite/auto-sync/src/autosync/cpptranslator/patches/ReferencesDecl.py` (PYTHON) | Magnitude: 22.52 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 15, api: 7, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `suite/fuzz.py` (PYTHON) | Magnitude: 36.0 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, branch: 20, structural_boundaries: 19, debug_prints: 5
- `Makefile` (MAKEFILE) | Magnitude: 5496.97 | Delta: **0.378 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 353, branch: 171, indent_tabs: 140, structural_boundaries: 120

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `suite/run_invalid_cstool.sh` (SHELL) | Magnitude: 53.16 | Delta: **0.169 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 52, structural_boundaries: 26, regex_execution: 26, branch: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `arch/SystemZ/SystemZMapping.c` (C) | Magnitude: 315.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 212, state_mutation: 90, branch: 75, api: 60
- `bindings/java/capstone/Mips.java` (JAVA) | Magnitude: 83.66 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 27, api: 24, func_start: 11
- `suite/auto-sync/src/autosync/ASUpdater.py` (PYTHON) | Magnitude: 303.5 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 278, state_mutation: 53, structural_boundaries: 48, branch: 39
- `arch/PowerPC/PPCMapping.c` (C) | Magnitude: 781.74 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 468, state_mutation: 294, branch: 197, api: 138
- `arch/Sparc/SparcMCTargetDesc.h` (C) | Magnitude: 24.7 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 13, macros: 10, api: 9, indent_tabs: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `arch/X86/X86Mapping.h` (C) | Magnitude: 62.1 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 46, pointers: 36, structural_boundaries: 25, args: 10
- `arch/BPF/BPFDisassembler.h` (C) | Magnitude: 27.34 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 12, indent_tabs: 10, pointers: 5, structural_boundaries: 4
- `config.mk` (MAKEFILE) | Magnitude: 14.16 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 8, dead_code: 2, sec_high_risk_execution: 1
- `cstool/getopt.h` (C) | Magnitude: 17.68 | Delta: **0.115 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: api: 3, pointers: 3, immutability_locks: 3, indent_tabs: 3
- `arch/ARM/ARMInstPrinter.c` (C) | Magnitude: 12.08 | Delta: **0.125 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: fragile_debt: 4, dead_code: 1, indent_tabs: 1, sec_dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `arch/RISCV/RISCVMapping.c` -> Churn: **100.0%** | Cog Load: 75.8204% | Debt: 15.1408%
- `cs.c` -> Churn: **88.15%** | Cog Load: 92.3023% | Debt: 65.3303%
- `Mapping.c` -> Churn: **73.25%** | Cog Load: 39.5696% | Debt: 95.5022%
- `arch/RISCV/RISCVDisassembler.c` -> Churn: **54.52%** | Cog Load: 67.7158% | Debt: 86.9682%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `include/capstone/arm64.h` -> **Rot127** (100.0% isolated ownership) | Magnitude: 4582.36
- `arch/HPPA/HPPADisassembler.c` -> **Rot127** (100.0% isolated ownership) | Magnitude: 3581.82
- `arch/SH/SHDisassembler.c` -> **Rot127** (100.0% isolated ownership) | Magnitude: 2121.56
- `arch/ARM/ARMMapping.c` -> **Rot127** (100.0% isolated ownership) | Magnitude: 2044.44
- `bindings/ocaml/ocaml.c` -> **Rot127** (100.0% isolated ownership) | Magnitude: 1706.56

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `suite/auto-sync/src/autosync/Helper.py` -> **Severity: 1634.201** (Blast Radius: 16.346 * Doc Risk: 99.9756%)
- `suite/auto-sync/src/autosync/PathVarHandler.py` -> **Severity: 1347.8** (Blast Radius: 13.478 * Doc Risk: 100.0%)
- `suite/auto-sync/src/autosync/cpptranslator/patches/Patch.py` -> **Severity: 885.39** (Blast Radius: 8.854 * Doc Risk: 99.9989%)
- `suite/auto-sync/src/autosync/cpptranslator/patches/Helper.py` -> **Severity: 834.591** (Blast Radius: 8.347 * Doc Risk: 99.987%)
- `include/windowsce/stdint.h` -> **Severity: 635.3** (Blast Radius: 6.353 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
