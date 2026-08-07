# ARCHITECTURAL_BRIEF: capstone
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/capstone` |
| **Timestamp** | `2026-08-07T03:49:23.546582+00:00` |
| **Scan Duration** | `8.96s` |
| **Git Branch** | `next` |
| **Git Commit** | `95fe762a411783c7507218e3d895f3b93e3238d5` |
| **Git Remote** | `https://github.com/capstone-engine/capstone.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1633 malicious artifacts.

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
| Error & Exception Exposure | 0.0 | 100.0 | 13.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 18.7 | 1.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 97.6 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 87.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.0 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 11.2 | 0.0 | 0.0 |
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

- `readPrefixes` (@ `arch/X86/X86DisassemblerDecoder.c`) -> Impact: **514.1** | LOC: 682
  * *Intent:* // return decision->opcodeDecisions[insnContext].modRMDecisions[opcode].modrm_type != MODRM_ONEENTRY;
- `DecodeMemMultipleWritebackInstruction` (@ `arch/ARM/ARMDisassembler.c`) -> Impact: **474.6** | LOC: 1040
- `add_alias_details` (@ `arch/ARM/ARMMapping.c`) -> Impact: **440.1** | LOC: 1222
- `AArch64_add_vas` (@ `arch/AArch64/AArch64Mapping.c`) -> Impact: **352.5** | LOC: 433
  * *Intent:* /// Very annoyingly LLVM hard codes the vector layout post-fixes into the asm string. /// In this function we check for these cases and add the vector...
- `getNextVectorRegister` (@ `arch/AArch64/AArch64InstPrinter.c`) -> Impact: **298.4** | LOC: 253
- `add_cs_detail_general` (@ `arch/ARM/ARMMapping.c`) -> Impact: **283.8** | LOC: 736
- `_cs_disasm` (@ `bindings/ocaml/ocaml.c`) -> Impact: **278.9** | LOC: 1697
- `readModRM` (@ `arch/X86/X86DisassemblerDecoder.c`) -> Impact: **266.2** | LOC: 365
  * *Intent:* case 0xf2: /* REPNE/REPNZ */ case 0xf3: /* REP or REPE/REPZ */ case 0xf0: /* LOCK */
- `WASM_getInstruction` (@ `arch/WASM/WASMDisassembler.c`) -> Impact: **242.8** | LOC: 416
- `main` (@ `suite/fuzz/drivermc.c`) -> Impact: **215.8** | LOC: 194
  * *Intent:* #define MAX_INSTR_SIZE 64 #define MAX_LINE_SIZE 128

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `suite/MC/AArch64` | 441 | 17849.18 | 10.95% | 0.0% |
| `__monolith__` | 42 | 10722.29 | 20.02% | 22.31% |
| `include/capstone` | 23 | 8346.78 | 8.03% | 1.06% |
| `arch/ARM` | 14 | 6650.3 | 33.18% | 31.41% |
| `tests/MC/AArch64/SVE` | 328 | 6049.22 | 0.52% | 0.0% |
| `arch/AArch64` | 12 | 5936.82 | 39.79% | 38.65% |
| `arch/X86` | 21 | 5193.04 | 22.68% | 15.6% |
| `suite/cstest/src` | 28 | 5009.8 | 71.2% | 2.2% |
| `arch/HPPA` | 9 | 3851.7 | 24.64% | 15.65% |
| `bindings/vb6` | 9 | 3822.29 | 34.58% | 11.11% |

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
- `arch/M68K/M68KDisassembler.c` -> **299** Orphaned Functions | **0** Duplicates
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
159. **`suite/MC/HPPA/sysctrl20.s.cs`** -> AI Confidence: **99.29%**
160. **`suite/MC/HPPA/system_op11.s.cs`** -> AI Confidence: **99.29%**
161. **`suite/MC/LoongArch/arith.s.cs`** -> AI Confidence: **99.29%**
162. **`suite/MC/LoongArch/misc.s.cs`** -> AI Confidence: **99.29%**
163. **`suite/MC/Mips/micromips-alu-instructions-EB.s.cs`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `49` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2024` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `arch/RISCV/RISCVMapping.c` (C) -> Cumulative Risk: **762.3**
- **Archetype:** `file_cluster_13` (Distance: 13.273 IQR)
- **Magnitude:** 507.24 | **LOC:** 448 | **CtrlFlow:** 73.8% | **Authorship Centralization:** 37.5%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `RISCV_add_cs_detail_0` (Impact: 197.3), `RISCV_add_ret_group` (Impact: 17.6), `RISCV_map_insn` (Impact: 10.8)

### 2. `arch/AArch64/AArch64InstPrinter.c` (C) -> Cumulative Risk: **718.76**
- **Archetype:** `file_cluster_8` (Distance: 12.987 IQR)
- **Magnitude:** 1425.5 | **LOC:** 2600 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Cognitive Load (96.2586%)
- **Heaviest Functions:** `getNextVectorRegister` (Impact: 298.4), `printAdrAdrpLabel` (Impact: 130.3), `printVectorList` (Impact: 32.8)

### 3. `arch/X86/X86ATTInstPrinter.c` (C) -> Cumulative Risk: **691.43**
- **Archetype:** `file_cluster_8` (Distance: 13.021 IQR)
- **Magnitude:** 875.04 | **LOC:** 1204 | **CtrlFlow:** 84.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Cognitive Load (91.9172%)
- **Heaviest Functions:** `printOperand` (Impact: 78.0), `printopaquemem` (Impact: 44.9), `printMemReference` (Impact: 30.9)

### 4. `arch/RISCV/RISCVDisassembler.c` (C) -> Cumulative Risk: **689.53**
- **Archetype:** `file_cluster_8` (Distance: 12.431 IQR)
- **Magnitude:** 602.46 | **LOC:** 754 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (87.3772%)
- **Heaviest Functions:** `RISCV_getInstruction` (Impact: 18.2), `decodeXTHeadMemPair` (Impact: 7.3), `DecodeGPRRegisterClass` (Impact: 4.7)

### 5. `arch/M68K/M68KDisassembler.c` (C) -> Cumulative Risk: **687.57**
- **Archetype:** `file_cluster_8` (Distance: 13.627 IQR)
- **Magnitude:** 2626.22 | **LOC:** 3946 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9325%)
- **Heaviest Functions:** `d68020_cpgen` (Impact: 122.9), `get_ea_mode_op` (Impact: 90.2), `d68010_movec` (Impact: 42.0)

### 6. `arch/X86/X86IntelInstPrinter.c` (C) -> Cumulative Risk: **685.14**
- **Archetype:** `file_cluster_8` (Distance: 13.007 IQR)
- **Magnitude:** 908.98 | **LOC:** 1274 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9996%), Cognitive Load (91.5043%)
- **Heaviest Functions:** `printImm` (Impact: 66.7), `printOperand` (Impact: 58.5), `printopaquemem` (Impact: 57.8)

### 7. `arch/Sparc/SparcInstPrinter.c` (C) -> Cumulative Risk: **680.48**
- **Archetype:** `file_cluster_13` (Distance: 12.852 IQR)
- **Magnitude:** 441.16 | **LOC:** 342 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.0812%)
- **Heaviest Functions:** `printSparcAliasInstr` (Impact: 47.0), `printCCOperand` (Impact: 41.5), `printOperand` (Impact: 15.8)

### 8. `arch/Xtensa/XtensaMapping.c` (C) -> Cumulative Risk: **673.18**
- **Archetype:** `file_cluster_13` (Distance: 12.68 IQR)
- **Magnitude:** 318.16 | **LOC:** 278 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (95.7336%)
- **Heaviest Functions:** `Xtensa_add_cs_detail_0` (Impact: 60.5), `Xtensa_reg_access` (Impact: 19.8), `Xtensa_L32R_Value` (Impact: 5.7)

### 9. `arch/Mips/MipsDisassembler.c` (C) -> Cumulative Risk: **667.67**
- **Archetype:** `file_cluster_8` (Distance: 12.653 IQR)
- **Magnitude:** 1353.86 | **LOC:** 3432 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9991%), Cognitive Load (89.7897%)
- **Heaviest Functions:** `DecodeMemMMImm4` (Impact: 34.8), `DecodeMovePRegPair` (Impact: 21.1), `DecodeINSVE_DF` (Impact: 15.2)

### 10. `arch/PowerPC/PPCInstPrinter.c` (C) -> Cumulative Risk: **667.49**
- **Archetype:** `file_cluster_8` (Distance: 12.78 IQR)
- **Magnitude:** 703.02 | **LOC:** 761 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (89.8625%)
- **Heaviest Functions:** `printPredicateOperand` (Impact: 70.0), `printInst` (Impact: 57.7), `printcrbitm` (Impact: 21.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.387 IQR)
- **Top Global Matches:** file_cluster_17: 12.387, file_cluster_8: 12.765, file_cluster_11: 12.915
- **Magnitude:** 5496.97 | **LOC:** 672 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.259%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 120`, `args: 7`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 10`, `state_mutation: 353`, `dead_code: 2`
* *Architecture:* `io: 68`, `api: 4`, `import: 4`
* *Defense:* `safety: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` config.mk, pkgconfig.mk, functions.mk, $(AUTODEPS)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `include/capstone/arm64.h` (C | Tier 4 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.537 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.157 IQR)
- **Top Global Matches:** file_cluster_8: 13.537, file_cluster_7: 13.998, file_cluster_13: 14.112
- **Magnitude:** 4582.36 | **LOC:** 4664 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (43.5464%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ARM64CC_getCondCodeName` (Impact: 21.9)
  * `ARM64CC_getNZCVToSatisfyCondCode` (Impact: 19.8)
  * `ARM64CC_isReflexive` (Impact: 11.8)
  * `ARM64CC_isIrreflexive` (Impact: 9.7)
  * `ARM64CC_getInvertedCondCode` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 111`, `func_start: 5`, `class_start: 30`
* *Risk/State:* `state_mutation: 4321`
* *Architecture:* `api: 106`, `import: 4`
* *Defense:* `safety: 3`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.436
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` assert.h, cs_operand.h, aarch64.h, platform.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `arch/HPPA/HPPADisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.06 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.822 IQR)
- **Top Global Matches:** file_cluster_8: 12.06, file_cluster_7: 12.476, file_cluster_13: 12.6
- **Magnitude:** 3217.62 | **LOC:** 3841 | **CtrlFlow:** 79.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (62.3257%), Tech Debt (7.8765%)
**Top Internal Functions/Classes:**
  * `fill_alu_insn_name` (Impact: 112.2)
  * `fill_alu_mods` (Impact: 100.8)
  * `getInstruction` (Impact: 77.5)
  * `fill_idxmem_insn_name` (Impact: 69.0)
  * `decode_alu` (Impact: 67.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1650`, `structural_boundaries: 420`, `args: 10`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 746`, `orphaned_logic: 1`
* *Architecture:* `api: 492`, `import: 8`
* *Defense:* `safety: 4`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` HPPADisassembler.h, stddef.h, string.h, Mapping.h, HPPAConstants.h, utils.h, stdio.h, MathExtras.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/M68K/M68KDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.627 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.394 IQR)
- **Top Global Matches:** file_cluster_8: 13.627, file_cluster_7: 13.899, file_cluster_13: 13.968
- **Magnitude:** 2626.22 | **LOC:** 3946 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (84.3719%), Tech Debt (99.9325%)
**Top Internal Functions/Classes:**
  * `d68020_cpgen` (Impact: 122.9)
  * `get_ea_mode_op` (Impact: 90.2)
  * `d68010_movec` (Impact: 42.0)
  * `get_with_index_address_mode` (Impact: 40.8)
  * `update_am_reg_list` (Impact: 23.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 410`, `structural_boundaries: 427`, `args: 4`, `func_start: 371`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1321`, `orphaned_logic: 299`
* *Architecture:* `io: 16`, `api: 310`, `import: 12`
* *Defense:* `safety: 1`, `doc: 39`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` M68KDisassembler.h, string.h, MCInst.h, M68KInstructionTable.inc, MCRegisterInfo.h, utils.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/ARM/ARMDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.995 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.356 IQR)
- **Top Global Matches:** file_cluster_8: 12.995, file_cluster_13: 13.092, file_cluster_7: 13.22
- **Magnitude:** 2624.44 | **LOC:** 7307 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (86.1446%), Tech Debt (11.2905%)
**Top Internal Functions/Classes:**
  * `DecodeMemMultipleWritebackInstruction` (Impact: 474.6)
  * `DecodeAddrMode3Instruction` (Impact: 158.8)
  * `DecodeAddrMode2IdxInstruction` (Impact: 60.5)
  * `DecodeLOLoop` (Impact: 30.6)
  * `DecodeMVEOverlappingLongShift` (Impact: 27.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 568`, `structural_boundaries: 470`, `args: 2`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `state_mutation: 720`, `dead_code: 4`, `fragile_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 842`, `import: 23`
* *Defense:* `safety: 2`, `doc: 20`, `immutability_locks: 237`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` MCInst.h, LEB128.h, stdlib.h, MathExtras.h, ARMMapping.h, ARMAddressingModes.h, ARMBaseInfo.h, MCInstrDesc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/ARM/ARMMapping.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.722 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.668 IQR)
- **Top Global Matches:** file_cluster_8: 13.722, file_cluster_13: 13.774, file_cluster_7: 13.884
- **Magnitude:** 2112.74 | **LOC:** 2268 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (71.7677%), Tech Debt (15.6547%)
**Top Internal Functions/Classes:**
  * `add_alias_details` (Impact: 440.1)
  * `add_cs_detail_general` (Impact: 283.8)
  * `add_cs_detail_template_1` (Impact: 56.2)
  * `ARM_add_cs_detail` (Impact: 28.2)
  * `ARM_set_detail_op_mem` (Impact: 18.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 426`, `structural_boundaries: 161`, `args: 2`, `func_start: 25`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 813`, `orphaned_logic: 10`
* *Architecture:* `api: 309`, `import: 16`
* *Defense:* `safety: 6`, `doc: 38`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ARMGenCSFeatureName.inc, ARMGenCSAliasMnemMap.inc, ARMGenCSMappingInsnName.inc, capstone.h, ARMGenRegisterInfo.inc, ARMMapping.h, ARMAddressingModes.h, Mapping.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.448 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.974 IQR)
- **Top Global Matches:** file_cluster_13: 14.448, file_cluster_8: 14.492, file_cluster_11: 14.628
- **Magnitude:** 2027.38 | **LOC:** 2179 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (92.3023%), Tech Debt (65.3303%)
**Top Internal Functions/Classes:**
  * `cs_op_index` (Impact: 129.8)
  * `cs_op_count` (Impact: 96.8)
  * `cs_disasm` (Impact: 50.6)
  * `cs_option` (Impact: 41.3)
  * `fill_insn` (Impact: 29.5)
    * *Intent:* #endif // fill insn with mnemonic & operands info
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 497`, `structural_boundaries: 268`, `args: 28`, `func_start: 41`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1085`, `dead_code: 4`, `fragile_debt: 1`, `orphaned_logic: 36`
* *Architecture:* `api: 309`, `import: 35`
* *Defense:* `safety: 31`, `doc: 3`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` stddef.h, SHModule.h, HPPAModule.h, WASMModule.h, stdlib.h, utils.h, capstone.h, ARMModule.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/SH/SHDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.117 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.023 IQR)
- **Top Global Matches:** file_cluster_8: 13.117, file_cluster_7: 13.399, file_cluster_13: 13.407
- **Magnitude:** 1983.76 | **LOC:** 2184 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (84.8989%), Tech Debt (52.3771%)
**Top Internal Functions/Classes:**
  * `decode_dsp_3op` (Impact: 80.5)
  * `sh_disassemble` (Impact: 30.6)
  * `decode_long` (Impact: 29.8)
    * *Intent:* #include "SHInsnTable.inc"
  * `opfxxd` (Impact: 29.1)
  * `lookup_insn` (Impact: 28.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 420`, `structural_boundaries: 312`, `args: 2`, `func_start: 84`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 883`, `orphaned_logic: 52`
* *Architecture:* `io: 76`, `api: 445`, `import: 9`
* *Defense:* `safety: 1`, `doc: 18`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` string.h, MCInst.h, SHDisassembler.h, utils.h, SHInsnTable.inc, sh.h, MCDisassembler.h, cs_priv.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/M680X/M680XDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.685 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.266 IQR)
- **Top Global Matches:** file_cluster_8: 13.685, file_cluster_13: 13.836, file_cluster_7: 13.926
- **Magnitude:** 1924.96 | **LOC:** 2343 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (80.5715%), Tech Debt (20.0025%)
**Top Internal Functions/Classes:**
  * `is_sufficient_code_size` (Impact: 86.8)
  * `indexed09_hdlr` (Impact: 57.2)
    * *Intent:* // M6809/M6309 indexed mode handler
  * `indexed12_hdlr` (Impact: 31.5)
    * *Intent:* // CPU12 indexed mode handler
  * `M680X_getInstruction` (Impact: 30.1)
  * `get_indexed09_post_byte_size` (Impact: 27.5)
    * *Intent:* // If successful return the additional byte size needed for M6809 // indexed addressing mode (includ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 231`, `args: 1`, `func_start: 65`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1041`, `fragile_debt: 6`, `orphaned_logic: 4`
* *Architecture:* `api: 281`, `import: 23`
* *Defense:* `safety: 3`, `doc: 26`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` cpu12.inc, MCInst.h, M680XInstPrinter.h, M680XDisassemblerInternals.h, stdlib.h, rs08.inc, m6809.inc, m6801.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/TriCore/TriCoreDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.36 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.638 IQR)
- **Top Global Matches:** file_cluster_8: 13.36, file_cluster_13: 13.468, file_cluster_7: 13.661
- **Magnitude:** 1835.16 | **LOC:** 1752 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.5679%), Tech Debt (9.6269%)
**Top Internal Functions/Classes:**
  * `DecodeBOInstruction` (Impact: 43.2)
  * `DecodeRRInstruction` (Impact: 26.6)
  * `DecodeSROInstruction` (Impact: 26.4)
  * `DecodeBOLInstruction` (Impact: 24.1)
  * `DecodeSCInstruction` (Impact: 23.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 281`, `args: 1`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `state_mutation: 788`, `orphaned_logic: 3`
* *Architecture:* `api: 587`, `import: 19`
* *Defense:* `safety: 3`, `doc: 3`, `immutability_locks: 124`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` TriCoreMapping.h, TriCoreLinkage.h, TriCoreGenInstrInfo.inc, string.h, MCInst.h, TriCoreDisassembler.h, TriCoreGenSubtargetInfo.inc, TriCoreGenRegisterInfo.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/X86/X86DisassemblerDecoder.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.871 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.351 IQR)
- **Top Global Matches:** file_cluster_13: 13.871, file_cluster_8: 13.987, file_cluster_7: 14.082
- **Magnitude:** 1576.28 | **LOC:** 2573 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (48.4199%), Tech Debt (33.9%)
**Top Internal Functions/Classes:**
  * `readPrefixes` (Impact: 514.1)
    * *Intent:* // return decision->opcodeDecisions[insnContext].modRMDecisions[opcode].modrm_type != MODRM_ONEENTRY...
  * `readModRM` (Impact: 266.2)
    * *Intent:* case 0xf2: /* REPNE/REPNZ */ case 0xf3: /* REP or REPE/REPZ */ case 0xf0: /* LOCK */
  * `readOperands` (Impact: 127.0)
  * `readSIB` (Impact: 53.5)
  * `readImmediate` (Impact: 31.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 106`, `args: 16`, `func_start: 16`, `class_start: 5`
* *Risk/State:* `state_mutation: 340`, `dead_code: 2`, `fragile_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 75`, `import: 14`
* *Defense:* `safety: 1`, `doc: 51`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` libkern.h, X86Mapping.h, X86GenDisassemblerTables_reduce.inc, X86GenDisassemblerTables_reduce2.inc, X86GenInstrInfo.inc, X86Lookup16_reduce.inc, X86DisassemblerDecoder.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/ocaml/ocaml.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.78 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.208 IQR)
- **Top Global Matches:** file_cluster_8: 12.78, file_cluster_7: 13.207, file_cluster_13: 13.286
- **Magnitude:** 1471.06 | **LOC:** 2132 | **CtrlFlow:** 96.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (90.0095%), Tech Debt (11.6899%)
**Top Internal Functions/Classes:**
  * `_cs_disasm` (Impact: 278.9)
  * `ocaml_cs_disasm` (Impact: 90.7)
  * `ocaml_open` (Impact: 90.4)
  * `ocaml_option` (Impact: 16.7)
  * `list_count` (Impact: 3.5)
    * *Intent:* /* By Nguyen Anh Quynh <aquynh@gmail.com>, 2013> */ #include <stdio.h> // debug #include <string.h> ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 12`, `args: 1`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 834`, `dead_code: 1`, `orphaned_logic: 9`
* *Architecture:* `api: 105`, `import: 7`
* *Defense:* `safety: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` string.h, stdio.h, mlvalues.h, memory.h, capstone.h, alloc.h, fail.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/AArch64/AArch64InstPrinter.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.987 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.095 IQR)
- **Top Global Matches:** file_cluster_8: 12.987, file_cluster_7: 13.338, file_cluster_13: 13.437
- **Magnitude:** 1425.5 | **LOC:** 2600 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (96.2586%), Tech Debt (92.551%)
**Top Internal Functions/Classes:**
  * `getNextVectorRegister` (Impact: 298.4)
  * `printAdrAdrpLabel` (Impact: 130.3)
  * `printVectorList` (Impact: 32.8)
  * `printArithExtend` (Impact: 12.7)
  * `printMemExtendImpl` (Impact: 11.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 120`, `args: 3`, `func_start: 41`
* *Risk/State:* `state_mutation: 538`, `fragile_debt: 4`, `orphaned_logic: 36`
* *Architecture:* `api: 261`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` AArch64GenAsmWriter.inc, AArch64Mapping.h, string.h, MCInst.h, SStream.h, AArch64BaseInfo.h, platform.h, MCRegisterInfo.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/Mips/MipsDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.653 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.127 IQR)
- **Top Global Matches:** file_cluster_8: 12.653, file_cluster_7: 12.99, file_cluster_0: 13.001
- **Magnitude:** 1353.86 | **LOC:** 3432 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (89.7897%), Tech Debt (83.0893%)
**Top Internal Functions/Classes:**
  * `DecodeMemMMImm4` (Impact: 34.8)
  * `DecodeMovePRegPair` (Impact: 21.1)
  * `DecodeINSVE_DF` (Impact: 15.2)
  * `DecodeSimm9SP` (Impact: 13.2)
  * `DecodeDINS` (Impact: 12.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 246`, `func_start: 74`
* *Risk/State:* `state_mutation: 496`, `dead_code: 3`, `orphaned_logic: 52`
* *Architecture:* `api: 474`, `import: 1`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` MipsGenDisassemblerTables.inc, MipsGenInstrInfo.inc, string.h, MCInst.h, MipsGenRegisterInfo.inc, platform.h, MCRegisterInfo.h, utils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/vb6/CX86Operand.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.207 IQR)
- **Top Global Matches:** file_cluster_13: 11.207, file_cluster_8: 11.425, file_cluster_0: 11.992
- **Magnitude:** 1345.95 | **LOC:** 203 | **CtrlFlow:** 97.4% | **Authorship Centralization:** 0.0%
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
- **Magnitude:** 1282.08 | **LOC:** 1003 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.6134%), Tech Debt (13.1302%)
**Top Internal Functions/Classes:**
  * `AArch64_AM_isAdvSIMDModImmType10` (Impact: 38.3)
    * *Intent:* // aaaaaaaa bbbbbbbb cccccccc dddddddd eeeeeeee ffffffff gggggggg hhhhhhhh // cmode: 1110, op: 1
  * `AArch64_AM_getExtendType` (Impact: 21.9)
    * *Intent:* /// getExtendType - Extract the extend type for operands of arithmetic ops.
  * `AArch64_AM_getExtendEncoding` (Impact: 21.6)
    * *Intent:* /// Mapping from extend bits to required operation: /// shifter: 000 ==> uxtb /// 001 ==> uxth /// 0...
  * `AArch64_AM_getShiftExtendName` (Impact: 18.8)
    * *Intent:* /// getShiftName - Get the string encoding for the shift type.
  * `AArch64_AM_processLogicalImmediate` (Impact: 16.1)
    * *Intent:* /// processLogicalImmediate - Determine if an immediate value can be encoded /// as the immediate op...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 176`, `args: 8`, `func_start: 64`, `class_start: 5`
* *Risk/State:* `state_mutation: 704`, `fragile_debt: 3`
* *Architecture:* `api: 254`, `import: 7`
* *Defense:* `safety: 1`, `doc: 61`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.841
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` string.h, platform.h, stdio.h, stdlib.h, assert.h, MathExtras.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `arch/AArch64/AArch64Mapping.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.019 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.272 IQR)
- **Top Global Matches:** file_cluster_8: 13.019, file_cluster_13: 13.059, file_cluster_7: 13.204
- **Magnitude:** 1259.14 | **LOC:** 2910 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (69.9883%), Tech Debt (39.5313%)
**Top Internal Functions/Classes:**
  * `AArch64_add_vas` (Impact: 352.5)
    * *Intent:* /// Very annoyingly LLVM hard codes the vector layout post-fixes into the asm string. /// In this fu...
  * `AArch64_add_not_defined_ops` (Impact: 105.2)
  * `sme_reg_to_vas` (Impact: 37.2)
    * *Intent:* #endif // CAPSTONE_DIET
  * `getNextVectorRegister` (Impact: 20.2)
  * `AArch64_set_detail_op_sme` (Impact: 17.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 105`, `args: 3`, `func_start: 24`
* *Risk/State:* `state_mutation: 350`, `orphaned_logic: 15`
* *Architecture:* `api: 249`, `import: 14`
* *Defense:* `doc: 24`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` aarch64.h, AArch64Mapping.h, string.h, AArch64GenCSMappingInsnName.inc, AArch64BaseInfo.h, AArch64GenCSMappingInsnOp.inc, AArch64AddressingModes.h, Mapping.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/python/cstest_py/src/cstest_py/details.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.994 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.845 IQR)
- **Top Global Matches:** file_cluster_8: 8.994, file_cluster_7: 9.812, file_cluster_13: 9.937
- **Magnitude:** 1154.86 | **LOC:** 1589 | **CtrlFlow:** 45.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (21.7989%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_expected_arm` (Impact: 105.3)
  * `test_expected_aarch64` (Impact: 102.4)
  * `test_expected_x86` (Impact: 85.4)
  * `test_expected_m68k` (Impact: 78.6)
  * `compare_details` (Impact: 60.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 570`, `structural_boundaries: 685`, `args: 25`, `func_start: 25`
* *Risk/State:* None
* *Architecture:* `api: 26`, `import: 26`
* *Defense:* `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` capstone.mips_const, capstone.alpha_const, capstone.systemz_const, capstone.m68k_const, capstone.riscv, cstest_py.compare, capstone.ppc_const, capstone.sh_const...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bindings/vb6/CDisassembler.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.547 IQR)
- **Top Global Matches:** file_cluster_13: 11.547, file_cluster_8: 11.852, file_cluster_0: 12.265
- **Magnitude:** 1081.51 | **LOC:** 154 | **CtrlFlow:** 94.3% | **Authorship Centralization:** 0.0%
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

### `arch/ARM/ARMAddressingModes.h` (C | Tier 4 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.636 IQR)
- **Local Micro-Species:** `Cluster 1: Algorithmic Bitwise & Encapsulated Core` (Drift: 5.244 IQR)
- **Top Global Matches:** file_cluster_13: 14.636, file_cluster_8: 14.672, file_cluster_7: 14.71
- **Magnitude:** 999.68 | **LOC:** 793 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.1842%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ARM_AM_getT2SOImmTwoPartSecond` (Impact: 83.2)
  * `ARM_AM_decodeVMOVModImm` (Impact: 26.1)
  * `ARM_AM_encodeNEONi32splat` (Impact: 16.1)
    * *Intent:* // 32-bit vector elements, one byte with low bits set
  * `ARM_AM_isT2SOImmTwoPartVal` (Impact: 13.4)
  * `ARM_AM_getT2SOImmValSplatVal` (Impact: 11.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 110`, `args: 43`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `state_mutation: 539`, `dead_code: 1`
* *Architecture:* `api: 127`, `import: 4`
* *Defense:* `safety: 1`, `doc: 54`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.813
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cs_priv.h, MathExtras.h, platform.h, assert.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `arch/AArch64/AArch64BaseInfo.h` (C | Tier 0 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.509 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.672 IQR)
- **Top Global Matches:** file_cluster_8: 10.509, file_cluster_13: 10.532, file_cluster_7: 10.729
- **Magnitude:** 984.9 | **LOC:** 987 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.079%), Tech Debt (11.4865%)
**Top Internal Functions/Classes:**
  * `atomicBarrierDroppedOnZero` (Impact: 132.1)
  * `getWRegFromXReg` (Impact: 64.3)
    * *Intent:* #define GET_SUBTARGETINFO_ENUM #include "AArch64GenSubtargetInfo.inc" #define GET_REGINFO_ENUM #defi...
  * `getXRegFromWReg` (Impact: 64.3)
  * `getBRegFromDReg` (Impact: 62.4)
  * `getDRegFromBReg` (Impact: 62.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 201`, `args: 10`, `func_start: 10`, `class_start: 11`
* *Risk/State:* `state_mutation: 33`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 448`, `import: 31`
* *Defense:* `doc: 53`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.742
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` aarch64.h, AArch64GenRegisterInfo.inc, string.h, platform.h, utils.h, stdio.h, stdlib.h, AArch64GenSubtargetInfo.inc...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `arch/WASM/WASMDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.109 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.619 IQR)
- **Top Global Matches:** file_cluster_0: 14.109, file_cluster_13: 14.147, file_cluster_11: 14.168
- **Magnitude:** 960.2 | **LOC:** 1066 | **CtrlFlow:** 75.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (95.0314%), Tech Debt (8.8784%)
**Top Internal Functions/Classes:**
  * `WASM_getInstruction` (Impact: 242.8)
  * `read_brtable` (Impact: 13.4)
    * *Intent:* // input | code : code pointer start from brtable // | code_len : start from the code pointer to the...
  * `get_varuint64` (Impact: 9.4)
    * *Intent:* // input | code : code pointer start from varuint64 // | code_len : real code len count from varint ...
  * `get_varuint32` (Impact: 9.3)
    * *Intent:* // input | code: code pointer start from varuint32 // | code_len: real code len count from varint //...
  * `read_memoryimmediate` (Impact: 8.2)
    * *Intent:* // input | code : code pointer start from memoryimmediate // | code_len : start from the code pointe...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 86`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 395`, `dead_code: 12`, `orphaned_logic: 1`
* *Architecture:* `api: 237`, `import: 5`
* *Defense:* `safety: 19`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` WASMDisassembler.h, stddef.h, string.h, WASMMapping.h, cs_priv.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `arch/Xtensa/XtensaDisassembler.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.414 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.045 IQR)
- **Top Global Matches:** file_cluster_8: 12.414, file_cluster_13: 12.539, file_cluster_7: 12.738
- **Magnitude:** 946.06 | **LOC:** 1140 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.6928%), Tech Debt (94.1111%)
**Top Internal Functions/Classes:**
  * `CheckRegister` (Impact: 114.3)
    * *Intent:* // Verify SR and UR
  * `getInstruction` (Impact: 19.0)
  * `decodeBranchOperand` (Impact: 13.2)
  * `DecodeSRRegisterClass` (Impact: 6.2)
  * `DecodeURRegisterClass` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 178`, `args: 1`, `func_start: 63`
* *Risk/State:* `state_mutation: 309`, `dead_code: 2`, `orphaned_logic: 50`
* *Architecture:* `api: 295`, `import: 13`
* *Defense:* `safety: 6`, `doc: 5`, `immutability_locks: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string.h, SStream.h, XtensaGenInstrInfo.inc, platform.h, priv.h, utils.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `include/capstone/aarch64.h` (C | Tier 4 | 🚨 AI THREAT: 98.77%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.367 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.213 IQR)
- **Top Global Matches:** file_cluster_8: 11.367, file_cluster_7: 11.846, file_cluster_1: 12.082
- **Magnitude:** 941.28 | **LOC:** 4865 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (25.0502%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `AArch64CC_getCondCodeName` (Impact: 21.9)
  * `AArch64CC_getInvertedCondCode` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 40`, `func_start: 2`, `class_start: 11`
* *Risk/State:* `state_mutation: 810`
* *Architecture:* `api: 45`, `import: 3`
* *Defense:* `safety: 2`, `doc: 39`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.621
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, cs_operand.h, platform.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `suite/MC/AArch64/mova.s.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.36 IQR)
- **Top Global Matches:** file_cluster_8: 11.36, file_cluster_7: 12.059, file_cluster_1: 12.207
- **Magnitude:** 933.02 | **LOC:** 902 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 900`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `arch/WASM/WASMDisassembler.c` (C) | Magnitude: 960.2 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 807, pointers: 450, state_mutation: 395, branch: 261
- `arch/AArch64/AArch64Disassembler.c` (C) | Magnitude: 508.72 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 316, api: 184, state_mutation: 170, branch: 114

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `bindings/java/run.sh` (SHELL) | Magnitude: 22.98 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, reflection_metaprogramming: 12, branch: 11, structural_boundaries: 8
- `make.sh` (SHELL) | Magnitude: 155.5 | Delta: **0.136 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 99, state_mutation: 73, branch: 46, reflection_metaprogramming: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cstool/cstool_arc.c` (C) | Magnitude: 75.78 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 53, state_mutation: 33, branch: 25, pointers: 18
- `suite/cstest/src/test_detail_m68k.c` (C) | Magnitude: 222.04 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 215, indent_tabs: 157, state_mutation: 115, branch: 48
- `arch/XCore/XCoreInstPrinter.h` (C) | Magnitude: 17.68 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 8, structural_boundaries: 4, api: 3, import: 3
- `arch/Xtensa/XtensaInstPrinter.h` (C) | Magnitude: 17.24 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 5, macros: 4, pointers: 3, api: 2
- `suite/auto-sync/src/autosync/cpptranslator/patches/TemplateDefinition.py` (PYTHON) | Magnitude: 18.82 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 21, api: 7, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `suite/auto-sync/src/autosync/Helper.py` (PYTHON) | Magnitude: 106.5 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 56, api: 24, branch: 23
- `suite/auto-sync/src/autosync/cpptranslator/patches/Override.py` (PYTHON) | Magnitude: 15.36 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 14, api: 7, args: 4
- `suite/auto-sync/src/autosync/cpptranslator/patches/SignExtend.py` (PYTHON) | Magnitude: 15.56 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 16, api: 7, args: 4
- `suite/auto-sync/src/autosync/cpptranslator/patches/isUInt.py` (PYTHON) | Magnitude: 15.66 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 16, api: 7, args: 4
- `suite/auto-sync/src/autosync/cpptranslator/patches/ReferencesDecl.py` (PYTHON) | Magnitude: 15.12 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 15, api: 7, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `suite/fuzz.py` (PYTHON) | Magnitude: 23.9 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, branch: 20, structural_boundaries: 19, debug_prints: 5
- `Makefile` (MAKEFILE) | Magnitude: 5496.97 | Delta: **0.378 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 353, branch: 171, indent_tabs: 140, structural_boundaries: 120

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `suite/run_invalid_cstool.sh` (SHELL) | Magnitude: 53.16 | Delta: **0.169 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 52, structural_boundaries: 26, regex_execution: 26, branch: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `arch/SystemZ/SystemZMapping.c` (C) | Magnitude: 259.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 212, state_mutation: 90, branch: 75, api: 60
- `bindings/java/capstone/Mips.java` (JAVA) | Magnitude: 62.86 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 27, api: 24, func_start: 11
- `suite/auto-sync/src/autosync/ASUpdater.py` (PYTHON) | Magnitude: 161.5 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 278, state_mutation: 53, structural_boundaries: 48, branch: 39
- `arch/PowerPC/PPCMapping.c` (C) | Magnitude: 714.54 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
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

- `arch/RISCV/RISCVMapping.c` -> Churn: **100.0%** | Cog Load: 93.6816% | Debt: 79.931%
- `cs.c` -> Churn: **88.15%** | Cog Load: 92.3023% | Debt: 65.3303%
- `Mapping.c` -> Churn: **73.25%** | Cog Load: 39.5696% | Debt: 95.5022%
- `arch/RISCV/RISCVDisassembler.c` -> Churn: **54.52%** | Cog Load: 67.7158% | Debt: 86.9682%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `include/capstone/arm64.h` -> **Rot127** (100.0% isolated ownership) | Magnitude: 4582.36
- `arch/HPPA/HPPADisassembler.c` -> **Rot127** (100.0% isolated ownership) | Magnitude: 3217.62
- `arch/ARM/ARMMapping.c` -> **Rot127** (100.0% isolated ownership) | Magnitude: 2112.74
- `arch/SH/SHDisassembler.c` -> **Rot127** (100.0% isolated ownership) | Magnitude: 1983.76
- `bindings/ocaml/ocaml.c` -> **Rot127** (100.0% isolated ownership) | Magnitude: 1471.06

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `suite/auto-sync/src/autosync/Helper.py` -> **Severity: 1623.07** (Blast Radius: 16.346 * Doc Risk: 99.2946%)
- `suite/auto-sync/src/autosync/PathVarHandler.py` -> **Severity: 1089.746** (Blast Radius: 13.478 * Doc Risk: 80.8537%)
- `suite/auto-sync/src/autosync/cpptranslator/patches/Patch.py` -> **Severity: 865.422** (Blast Radius: 8.854 * Doc Risk: 97.7436%)
- `suite/auto-sync/src/autosync/cpptranslator/patches/Helper.py` -> **Severity: 640.877** (Blast Radius: 8.347 * Doc Risk: 76.7793%)
- `include/windowsce/stdint.h` -> **Severity: 635.3** (Blast Radius: 6.353 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
