# ARCHITECTURAL_BRIEF: keystone
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/keystone` |
| **Timestamp** | `2026-08-03T19:27:26.798584+00:00` |
| **Scan Duration** | `1.71s` |
| **Git Branch** | `master` |
| **Git Commit** | `fb92f32391c6cced868252167509590319eeb58b` |
| **Git Remote** | `https://github.com/keystone-engine/keystone.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 416 malicious artifacts.

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
| Total Artifacts | 1095 |
| Analyzed Artifacts (Scanned) | 475 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 620 |
| Total LOC | 31368 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 43.4% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.733 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4725 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9636 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 14 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 242 | 22996 | 50.9% |
| PYTHON | 70 | 2699 | 14.7% |
| PLAINTEXT | 35 | 0 | 7.4% |
| MAKEFILE | 29 | 1714 | 6.1% |
| JAVA | 22 | 718 | 4.6% |
| MARKDOWN | 19 | 0 | 4.0% |
| CPP | 10 | 1436 | 2.1% |
| SHELL | 9 | 135 | 1.9% |
| CSHARP | 5 | 311 | 1.1% |
| RUST | 5 | 344 | 1.1% |
| HASKELL | 4 | 140 | 0.8% |
| RUBY | 4 | 45 | 0.8% |
| M4 | 3 | 65 | 0.6% |
| GO | 3 | 115 | 0.6% |
| XML | 3 | 0 | 0.6% |
| JAVASCRIPT | 3 | 105 | 0.6% |
| ASSEMBLY | 2 | 271 | 0.4% |
| POWERSHELL | 2 | 195 | 0.4% |
| PHP | 2 | 4 | 0.4% |
| BATCH | 2 | 36 | 0.4% |
| APEX | 1 | 39 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.887`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 210 | 44.2% |
| file_cluster_13 | 183 | 38.5% |
| file_cluster_16 | 8 | 1.7% |
| file_cluster_7 | 7 | 1.5% |
| file_cluster_0 | 6 | 1.3% |
| file_cluster_9 | 3 | 0.6% |
| file_cluster_12 | 2 | 0.4% |
| file_cluster_4 | 1 | 0.2% |
| file_cluster_2 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 54 | 11.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 620*

**Composition by Extension & Reason:**
- `.cpp`: 154x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 87x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 60 LOC), 1x Excluded (Machine-Generated Source Code Signature: 358 LOC)
- `.txt`: 86x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 25x Unsupported Format (.undeterminable), 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.inc`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cmake`: 21x Excluded (Unsupported Extension: '.cmake'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 10x Excluded (Machine-Generated Source Code Signature: 5 LOC), 1x Excluded (Machine-Generated Source Code Signature: 437 LOC), 1x Excluded (Machine-Generated Source Code Signature: 95 LOC)
- `.go`: 10x Excluded (Machine-Generated Source Code Signature: 10 LOC), 1x Excluded (Machine-Generated Source Code Signature: 112 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rb`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 10x Excluded (Machine-Generated Source Code Signature: 5 LOC), 1x Excluded (Machine-Generated Source Code Signature: 95 LOC)
- `.cs`: 8x Excluded (Machine-Generated Source Code Signature: 10 LOC), 1x Excluded (Machine-Generated Source Code Signature: 107 LOC), 1x Excluded (Machine-Generated Source Code Signature: 95 LOC)
- `.chs`: 10x Unsupported Format (.chs)
- `.rc`: 8x Excluded (Unsupported Extension: '.Rc'), 2x Excluded (Unsupported Extension: '.rc')
- `.ml`: 6x Excluded (Unsupported Extension: '.ml'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 24.6 | 9.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 29.9 | 14.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 46.3 | 33.1 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.8 | 2.3 | 2.3 |
| API Exposure | 0.0 | 18.6 | 8.0 | 8.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 46.0 | 22.9 | 0.0 |
| Commented Logic Exposure | 0.0 | 42.2 | 1.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 71.7 | 98.3 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 27.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 7.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.3 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `bindings/python/setup.py` (Hits: 65)
- `suite/fuzz/gentargets.sh` (Hits: 46)
- `llvm/utils/llvm-build/llvmbuild/main.py` (Hits: 41)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **regress.py** (`suite/regress/regress.py`) — 54 inbound connections
2. **iterator.h** (`llvm/include/llvm/ADT/iterator.h`) — 10 inbound connections
3. **JnaEnum.java** (`bindings/java/src/main/java/keystone/jna/JnaEnum.java`) — 5 inbound connections
4. **util.py** (`llvm/utils/llvm-build/llvmbuild/util.py`) — 5 inbound connections
5. **KeystoneError.java** (`bindings/java/src/main/java/keystone/KeystoneError.java`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ELFObjectFile.h** (`llvm/include/llvm/Object/ELFObjectFile.h`) — 17 outbound dependencies
2. **MCContext.h** (`llvm/include/llvm/MC/MCContext.h`) — 16 outbound dependencies
3. **ELF.h** (`llvm/include/llvm/Support/ELF.h`) — 16 outbound dependencies
4. **DenseMap.h** (`llvm/include/llvm/ADT/DenseMap.h`) — 15 outbound dependencies
5. **keystone.h** (`include/keystone/keystone.h`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `load_infos_from_path` (@ `llvm/utils/llvm-build/llvmbuild/main.py`) -> Impact: **1052.8** | LOC: 444
  * *Intent:* """ make_install_dir(path) -> None Create the given directory path for installation, including any parents. """
- `add_magic_target_components` (@ `llvm/utils/llvm-build/llvmbuild/main.py`) -> Impact: **810.5** | LOC: 250
  * *Intent:* # Explicit library dependency information. # # names to required libraries, in a way that is easily accessed from CMake. """) self.foreach_cmake_libra...
- `ks_open` (@ `llvm/keystone/ks.cpp`) -> Impact: **589.3** | LOC: 267
- `__init__` (@ `llvm/utils/llvm-build/llvmbuild/componentinfo.py`) -> Impact: **582.6** | LOC: 336
- `main` (@ `kstool/kstool.cpp`) -> Impact: **338.0** | LOC: 265
- `HeaderWords` (@ `llvm/include/llvm/Support/ARMWinEH.h`) -> Impact: **311.1** | LOC: 63
- `Get-KeystoneAssembly` (@ `bindings/powershell/Keystone/Keystone.psm1`) -> Impact: **299.9** | LOC: 236
- `copy_sources` (@ `bindings/python/setup.py`) -> Impact: **278.6** | LOC: 168
  * *Intent:* """Copy the C sources into the source directory. This rearranges the source files under the python distribution directory. """
- `swap` (@ `llvm/include/llvm/ADT/DenseMap.h`) -> Impact: **136.2** | LOC: 65
- `Assemble` (@ `bindings/csharp/Keystone.Net/Engine.cs`) -> Impact: **121.7** | LOC: 33
  * *Intent:* /// <summary> /// Encodes the given statement(s) into the given buffer. /// </summary> /// <param name="toEncode">String that contains the statements ...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `Assemble` (@ `bindings/csharp/Keystone.Net/Engine.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Encodes the given statement(s) into the given buffer. /// </summary> /// <param name="toEncode">String that contains the statements ...
- `Assemble` (@ `bindings/csharp/Keystone.Net/Engine.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Encodes the given statement(s). /// </summary> /// <param name="toEncode">String that contains the statements to encode.</param> ///...
- `getMaxValue` (@ `llvm/include/llvm/ADT/APSInt.h`) -> **O(2^N) [Recursive]**
  * *Intent:* /// getMaxValue - Return the APSInt representing the maximum integer value /// with the given bit width and signedness.
- `getMinValue` (@ `llvm/include/llvm/ADT/APSInt.h`) -> **O(2^N) [Recursive]**
  * *Intent:* /// getMinValue - Return the APSInt representing the minimum integer value /// with the given bit width and signedness.
- `swap` (@ `llvm/include/llvm/ADT/DenseMap.h`) -> **O(2^N) [Recursive]**
- `getEmptyKey` (@ `llvm/include/llvm/ADT/DenseMapInfo.h`) -> **O(2^N) [Recursive]**
- `getTombstoneKey` (@ `llvm/include/llvm/ADT/DenseMapInfo.h`) -> **O(2^N) [Recursive]**
- `find` (@ `llvm/include/llvm/ADT/MapVector.h`) -> **O(2^N) [Recursive]**
- `get` (@ `llvm/include/llvm/ADT/PointerUnion.h`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Returns the value of the specified pointer type. /// /// If the specified pointer type is incorrect, assert.
- `isEqual` (@ `llvm/include/llvm/ADT/PointerUnion.h`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `copy_sources` (@ `bindings/python/setup.py`) -> DB Complexity: **194**
  * *Intent:* """Copy the C sources into the source directory. This rearranges the source files under the python distribution directory. """
- `main` (@ `kstool/kstool.cpp`) -> DB Complexity: **106**
- `load_infos_from_path` (@ `llvm/utils/llvm-build/llvmbuild/main.py`) -> DB Complexity: **96**
  * *Intent:* """ make_install_dir(path) -> None Create the given directory path for installation, including any parents. """
- `ks_open` (@ `llvm/keystone/ks.cpp`) -> DB Complexity: **58**
- `main` (@ `suite/fuzz/onefile.c`) -> DB Complexity: **33**
- `Get-KeystoneAssembly` (@ `bindings/powershell/Keystone/Keystone.psm1`) -> DB Complexity: **28**
- `add_magic_target_components` (@ `llvm/utils/llvm-build/llvmbuild/main.py`) -> DB Complexity: **28**
  * *Intent:* # Explicit library dependency information. # # names to required libraries, in a way that is easily accessed from CMake. """) self.foreach_cmake_libra...
- `__init__` (@ `llvm/utils/llvm-build/llvmbuild/componentinfo.py`) -> DB Complexity: **25**
- `ks_asm` (@ `llvm/keystone/ks.cpp`) -> DB Complexity: **25**
  * *Intent:* /*
- `ComputeEditDistance` (@ `llvm/include/llvm/ADT/edit_distance.h`) -> DB Complexity: **24**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `llvm/include/llvm/Support` | 56 | 6138.52 | 15.47% | 32.14% |
| `llvm/include/llvm/ADT` | 36 | 5586.18 | 19.77% | 60.15% |
| `llvm/include/llvm/MC` | 47 | 4105.08 | 9.94% | 32.97% |
| `llvm/utils/llvm-build/llvmbuild` | 5 | 2844.18 | 12.49% | 6.98% |
| `llvm/include/llvm/Object` | 9 | 2028.78 | 17.13% | 12.08% |
| `suite/fuzz` | 30 | 1914.88 | 67.29% | 64.33% |
| `bindings/python/keystone` | 2 | 1713.96 | 36.36% | 0.0% |
| `suite/regress/c-crashers` | 42 | 1343.82 | 70.5% | 97.5% |
| `llvm/keystone` | 6 | 1319.76 | 29.5% | 17.7% |
| `kstool` | 5 | 895.94 | 35.79% | 2.41% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bindings/haskell/src/cbits/keystone_wrapper.c` -> **100.0%** Exposure
- `llvm/include/llvm/ADT/DenseMapInfo.h` -> **100.0%** Exposure
- `llvm/include/llvm/ADT/FoldingSet.h` -> **100.0%** Exposure
- `llvm/include/llvm/ADT/IntrusiveRefCntPtr.h` -> **100.0%** Exposure
- `llvm/include/llvm/ADT/PointerUnion.h` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bindings/csharp/Keystone.Net/Engine.cs` -> **100.0%** Exposure
- `bindings/go/keystone/samples/main.go` -> **100.0%** Exposure
- `suite/fuzz/fuzz_asm_arm64_arm.c` -> **100.0%** Exposure
- `suite/fuzz/fuzz_asm_arm_arm.c` -> **100.0%** Exposure
- `suite/fuzz/fuzz_asm_arm_armbe.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `llvm/include/llvm/ADT/DenseMapInfo.h` -> **0** Orphaned Functions | **42** Duplicates
- `llvm/include/llvm/Support/MachO.h` -> **0** Orphaned Functions | **41** Duplicates
- `llvm/include/llvm/ADT/PointerUnion.h` -> **0** Orphaned Functions | **31** Duplicates
- `llvm/include/llvm/ADT/FoldingSet.h` -> **4** Orphaned Functions | **19** Duplicates
- `llvm/include/llvm/ADT/DenseMap.h` -> **0** Orphaned Functions | **18** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`kstool/kstool.cpp`** -> AI Confidence: **99.48%**
2. **`llvm/include/llvm/ADT/Optional.h`** -> AI Confidence: **99.34%**
3. **`llvm/include/llvm/Support/ErrorOr.h`** -> AI Confidence: **99.34%**
4. **`llvm/utils/llvm-build/llvmbuild/main.py`** -> AI Confidence: **99.34%**
5. **`llvm/include/llvm/Support/Compiler.h`** -> AI Confidence: **99.32%**
6. **`bindings/haskell/src/Keystone.hs`** -> AI Confidence: **99.31%**
7. **`llvm/include/llvm/ADT/SmallVector.h`** -> AI Confidence: **99.31%**
8. **`bindings/python/Makefile`** -> AI Confidence: **99.29%**
9. **`bindings/rust/Makefile`** -> AI Confidence: **99.29%**
10. **`llvm/include/llvm/Config/AsmParsers.def.in`** -> AI Confidence: **99.29%**
11. **`llvm/include/llvm/Config/Targets.def.in`** -> AI Confidence: **99.29%**
12. **`llvm/include/llvm/Support/ARMTargetParser.def`** -> AI Confidence: **99.29%**
13. **`llvm/include/llvm/Support/Dwarf.def`** -> AI Confidence: **99.29%**
14. **`llvm/include/llvm/Support/ELFRelocs/PowerPC.def`** -> AI Confidence: **99.29%**
15. **`llvm/include/llvm/Support/ELFRelocs/PowerPC64.def`** -> AI Confidence: **99.29%**
16. **`suite/fuzz/fuzz_asm_arm64_arm.c`** -> AI Confidence: **99.29%**
17. **`suite/fuzz/fuzz_asm_arm_arm.c`** -> AI Confidence: **99.29%**
18. **`suite/fuzz/fuzz_asm_arm_armbe.c`** -> AI Confidence: **99.29%**
19. **`suite/fuzz/fuzz_asm_arm_armv8be.c`** -> AI Confidence: **99.29%**
20. **`suite/fuzz/fuzz_asm_arm_thumb.c`** -> AI Confidence: **99.29%**
21. **`suite/fuzz/fuzz_asm_arm_thumbbe.c`** -> AI Confidence: **99.29%**
22. **`suite/fuzz/fuzz_asm_arm_thumbv8.c`** -> AI Confidence: **99.29%**
23. **`suite/fuzz/fuzz_asm_arm_thumbv8be.c`** -> AI Confidence: **99.29%**
24. **`suite/fuzz/fuzz_asm_armv8_arm.c`** -> AI Confidence: **99.29%**
25. **`suite/fuzz/fuzz_asm_evm.c`** -> AI Confidence: **99.29%**
26. **`suite/fuzz/fuzz_asm_hex.c`** -> AI Confidence: **99.29%**
27. **`suite/fuzz/fuzz_asm_mips.c`** -> AI Confidence: **99.29%**
28. **`suite/fuzz/fuzz_asm_mips64.c`** -> AI Confidence: **99.29%**
29. **`suite/fuzz/fuzz_asm_mips64be.c`** -> AI Confidence: **99.29%**
30. **`suite/fuzz/fuzz_asm_mipsbe.c`** -> AI Confidence: **99.29%**
31. **`suite/fuzz/fuzz_asm_ppc32be.c`** -> AI Confidence: **99.29%**
32. **`suite/fuzz/fuzz_asm_ppc64.c`** -> AI Confidence: **99.29%**
33. **`suite/fuzz/fuzz_asm_ppc64be.c`** -> AI Confidence: **99.29%**
34. **`suite/fuzz/fuzz_asm_riscv32.c`** -> AI Confidence: **99.29%**
35. **`suite/fuzz/fuzz_asm_riscv64.c`** -> AI Confidence: **99.29%**
36. **`suite/fuzz/fuzz_asm_sparc.c`** -> AI Confidence: **99.29%**
37. **`suite/fuzz/fuzz_asm_sparc64be.c`** -> AI Confidence: **99.29%**
38. **`suite/fuzz/fuzz_asm_sparcbe.c`** -> AI Confidence: **99.29%**
39. **`suite/fuzz/fuzz_asm_systemz.c`** -> AI Confidence: **99.29%**
40. **`suite/fuzz/fuzz_asm_x86_16.c`** -> AI Confidence: **99.29%**
41. **`suite/fuzz/fuzz_asm_x86_32.c`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `llvm/include/llvm/Support/COFF.h` -> **0.0009%** Exposure
### Exploit Generation Surface
- `bindings/csharp/Keystone.Net.Tests/Tests.cs` -> **100.0%** Exposure
- `bindings/csharp/Keystone.Net/Engine.cs` -> **100.0%** Exposure
- `bindings/java/src/main/java/keystone/KeystoneOptionValue.java` -> **100.0%** Exposure
- `bindings/java/src/main/java/keystone/exceptions/SetOptionFailedKeystoneException.java` -> **100.0%** Exposure
- `bindings/java/src/main/java/keystone/utilities/Version.java` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `bindings/python/setup.py` -> **100.0%** Exposure
- `bindings/python/Makefile` -> **99.9991%** Exposure
### Raw Memory Manipulation
- `llvm/include/llvm/ADT/SmallVector.h` -> **10.0%** Exposure
- `llvm/include/llvm/Support/FileSystem.h` -> **10.0%** Exposure
- `llvm/include/llvm/Support/TargetRegistry.h` -> **9.9992%** Exposure
- `llvm/include/llvm/ADT/FoldingSet.h` -> **9.9974%** Exposure
- `llvm/keystone/ks.cpp` -> **9.9885%** Exposure
### Algorithmic DoS Exposure
- `bindings/csharp/Keystone.Net.Tests/Tests.cs` -> **100.0%** Exposure
- `bindings/csharp/Keystone.Net/EncodedData.cs` -> **100.0%** Exposure
- `bindings/csharp/Keystone.Net/Engine.cs` -> **100.0%** Exposure
- `samples/sample.c` -> **100.0%** Exposure
- `suite/fuzz/fuzz_asm_arm64_arm.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `45` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1056` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `bindings/csharp/Keystone.Net/Engine.cs` (CSHARP) -> Cumulative Risk: **818.76**
- **Archetype:** `file_cluster_13` (Distance: 14.513 IQR)
- **Magnitude:** 526.78 | **LOC:** 371 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `Assemble` (Impact: 121.7), `Assemble` (Impact: 79.9), `SetOption` (Impact: 42.3)

### 2. `llvm/include/llvm/Support/LEB128.h` (C) -> Cumulative Risk: **743.96**
- **Archetype:** `file_cluster_13` (Distance: 14.589 IQR)
- **Magnitude:** 209.5 | **LOC:** 122 | **CtrlFlow:** 80.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9845%)
- **Heaviest Functions:** `encodeULEB128` (Impact: 25.4), `encodeULEB128` (Impact: 25.4), `encodeSLEB128` (Impact: 14.7)

### 3. `bindings/java/src/main/java/keystone/Keystone.java` (JAVA) -> Cumulative Risk: **721.81**
- **Archetype:** `file_cluster_13` (Distance: 11.6 IQR)
- **Magnitude:** 131.12 | **LOC:** 250 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9999%)
- **Heaviest Functions:** `close` (Impact: 16.4), `assemble` (Impact: 9.7), `initializeKeystoneEngine` (Impact: 7.4)

### 4. `llvm/include/llvm/ADT/DenseMap.h` (C) -> Cumulative Risk: **711.32**
- **Archetype:** `file_cluster_13` (Distance: 13.294 IQR)
- **Magnitude:** 793.14 | **LOC:** 1075 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%), Documentation (99.9986%)
- **Heaviest Functions:** `swap` (Impact: 136.2), `grow` (Impact: 45.9), `clear` (Impact: 14.8)

### 5. `bindings/python/setup.py` (PYTHON) -> Cumulative Risk: **694.8**
- **Archetype:** `file_cluster_13` (Distance: 10.849 IQR)
- **Magnitude:** 329.94 | **LOC:** 244 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `copy_sources` (Impact: 278.6)

### 6. `llvm/keystone/ks.cpp` (CPP) -> Cumulative Risk: **691.17**
- **Archetype:** `file_cluster_8` (Distance: 13.15 IQR)
- **Magnitude:** 1106.48 | **LOC:** 717 | **CtrlFlow:** 66.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (93.8921%)
- **Heaviest Functions:** `ks_open` (Impact: 589.3), `ks_option` (Impact: 55.9), `InitKs` (Impact: 46.7)

### 7. `llvm/include/llvm/ADT/Hashing.h` (C) -> Cumulative Risk: **666.19**
- **Archetype:** `file_cluster_7` (Distance: 14.564 IQR)
- **Magnitude:** 314.66 | **LOC:** 662 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9997%), State Flux (99.9996%)
- **Heaviest Functions:** `hash_combine_range_impl` (Impact: 22.6), `hash_short` (Impact: 18.7), `store_and_advance` (Impact: 13.9)

### 8. `bindings/csharp/Keystone.Net.Tests/Tests.cs` (CSHARP) -> Cumulative Risk: **655.32**
- **Archetype:** `file_cluster_8` (Distance: 9.667 IQR)
- **Magnitude:** 50.24 | **LOC:** 79 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `ShouldHaveValidExample` (Impact: 13.4), `ShouldThrowOnError` (Impact: 6.3), `ShouldEmitValidX86Data` (Impact: 6.0)

### 9. `bindings/rust/src/lib.rs` (RUST) -> Cumulative Risk: **641.72**
- **Archetype:** `file_cluster_13` (Distance: 13.184 IQR)
- **Magnitude:** 138.04 | **LOC:** 169 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9939%), State Flux (99.8921%)
- **Heaviest Functions:** `fmt` (Impact: 21.1), `new` (Impact: 18.1), `asm` (Impact: 16.9)

### 10. `llvm/utils/llvm-build/llvmbuild/componentinfo.py` (PYTHON) -> Cumulative Risk: **635.89**
- **Archetype:** `file_cluster_13` (Distance: 11.309 IQR)
- **Magnitude:** 783.36 | **LOC:** 476 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 582.6), `get_bool` (Impact: 69.8), `get_string` (Impact: 26.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `llvm/utils/llvm-build/llvmbuild/main.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.576 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.908 IQR)
- **Top Global Matches:** file_cluster_8: 10.576, file_cluster_7: 10.69, file_cluster_13: 10.735
- **Magnitude:** 1980.24 | **LOC:** 997 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 96
- **Risk Profile:** Cognitive Load (21.1267%), Tech Debt (21.0409%)
**Top Internal Functions/Classes:**
  * `load_infos_from_path` (Impact: 1052.8 | O(2^N) | DB: 96)
    * *Intent:* """ make_install_dir(path) -> None Create the given directory path for installation, including any p...
  * `add_magic_target_components` (Impact: 810.5 | O(2^N) | DB: 28)
    * *Intent:* # Explicit library dependency information. # # names to required libraries, in a way that is easily ...
  * `write_make_fragment` (Impact: 17.6 | O(N^4) | DB: 9)
    * *Intent:* # Write out the CMake fragment.
  * `make_install_dir` (Impact: 5.5 | O(N^2) | DB: 6)
  * `write_cmake_exports_fragment` (Impact: 3.5 | O(N^2) | DB: 6)
    * *Intent:* # Skip disabled targets. if skip_disabled: tg = ci.get_parent_target_group() if tg and not tg.enable...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 64`, `args: 29`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 48`, `fragile_debt: 4`
* *Architecture:* `io: 41`, `api: 25`, `import: 8`
* *Defense:* `safety: 4`, `doc: 52`, `test: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.284
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.002105
  * `Imports (Out-Degree: 3):` sys, llvmbuild.util, os, optparse, __future__, llvmbuild.componentinfo, llvmbuild.configutil, filecmp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bindings/python/keystone/keystone.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.909 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.99 IQR)
- **Top Global Matches:** file_cluster_0: 13.909, file_cluster_13: 13.977, file_cluster_17: 14.121
- **Magnitude:** 1702.4 | **LOC:** 246 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (67.7253%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 50`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 42`, `dead_code: 4`
* *Architecture:* `io: 3`, `api: 12`, `import: 9`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys, , ctypes, os.path, inspect, .keystone_const, distutils.sysconfig, platform
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/keystone/ks.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.15 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.608 IQR)
- **Top Global Matches:** file_cluster_8: 13.15, file_cluster_13: 13.353, file_cluster_11: 13.487
- **Magnitude:** 1106.48 | **LOC:** 717 | **CtrlFlow:** 66.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (81.0723%), Tech Debt (93.8921%)
**Top Internal Functions/Classes:**
  * `ks_open` (Impact: 589.3 | O(N^6) | DB: 58)
  * `ks_option` (Impact: 55.9 | O(N^5) | DB: 3)
  * `InitKs` (Impact: 46.7 | O(N^3) | DB: 20)
  * `ks_asm` (Impact: 45.2 | O(N^3) | DB: 25)
    * *Intent:* /*
  * `ks_arch_supported` (Impact: 21.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 101`, `args: 63`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 322`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 7`, `orphaned_logic: 8`
* *Architecture:* `import: 6`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` stdio.h, EVMMapping.h, libkern.h, MCObjectFileInfo.h, MCCodeEmitter.h, ks_priv.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/Support/MachO.h` (C | Tier 4 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.951 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.988 IQR)
- **Top Global Matches:** file_cluster_8: 10.951, file_cluster_7: 11.334, file_cluster_13: 11.566
- **Magnitude:** 1012.56 | **LOC:** 1676 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (38.1902%), Tech Debt (99.9882%)
**Top Internal Functions/Classes:**
  * `swapStruct` (Impact: 6.2 | O(2^N))
  * `swapStruct` (Impact: 6.2 | O(2^N))
  * `swapStruct` (Impact: 6.2 | O(2^N))
  * `swapStruct` (Impact: 2.0 | O(N^1))
  * `swapStruct` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 156`, `args: 1`, `func_start: 48`, `class_start: 108`
* *Risk/State:* `state_mutation: 407`, `planned_debt: 3`, `duplicate_logic: 41`
* *Architecture:* `api: 499`, `import: 3`
* *Defense:* `doc: 47`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Host.h, Compiler.h, DataTypes.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/ADT/DenseMap.h` (C | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.294 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.751 IQR)
- **Top Global Matches:** file_cluster_13: 13.294, file_cluster_8: 13.449, file_cluster_0: 13.586
- **Magnitude:** 793.14 | **LOC:** 1075 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (51.2099%), Tech Debt (99.4436%)
**Top Internal Functions/Classes:**
  * `swap` (Impact: 136.2 | O(2^N) | DB: 20)
  * `grow` (Impact: 45.9 | O(N^4) | DB: 12)
  * `clear` (Impact: 14.8 | O(N^2) | DB: 8)
  * `AdvancePastEmptyBuckets` (Impact: 14.4 | O(N^6) | DB: 3)
    * *Intent:* *RHSB = &RHS.getInlineBuckets()[i];
  * `shrink_and_clear` (Impact: 13.0 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 136`, `args: 11`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `state_mutation: 272`, `dead_code: 1`, `duplicate_logic: 18`
* *Architecture:* `api: 206`, `import: 15`
* *Defense:* `safety: 22`, `doc: 22`, `test: 16`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` EpochTracker.h, cassert, climits, Compiler.h, type_traits.h, cstring, AlignOf.h, cstddef...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/utils/llvm-build/llvmbuild/componentinfo.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.309 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.308 IQR)
- **Top Global Matches:** file_cluster_13: 11.309, file_cluster_0: 11.339, file_cluster_7: 11.468
- **Magnitude:** 783.36 | **LOC:** 476 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (21.1197%), Tech Debt (13.8374%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 582.6 | O(2^N) | DB: 25)
  * `get_bool` (Impact: 69.8 | O(N^6) | DB: 6)
    * *Intent:* # Check if the value is defined.
  * `get_string` (Impact: 26.7 | O(N^5))
  * `parse_items` (Impact: 7.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 98`, `args: 41`, `func_start: 41`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 47`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 44`, `import: 6`
* *Defense:* `safety: 7`, `doc: 22`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.705
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002807
  * `Imports (Out-Degree: 1):` sys, ConfigParser, llvmbuild.util, configparser, __future__, traceback
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kstool/kstool.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.341 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.316 IQR)
- **Top Global Matches:** file_cluster_13: 14.341, file_cluster_8: 14.344, file_cluster_11: 14.665
- **Magnitude:** 722.08 | **LOC:** 360 | **CtrlFlow:** 90.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 106
- **Risk Profile:** Cognitive Load (79.805%), Tech Debt (12.0278%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 338.0 | O(N^4) | DB: 106)
  * `usage` (Impact: 45.2 | O(N^3) | DB: 3)
    * *Intent:* #include <errno.h> #include <limits.h> #if !defined(WIN32) && !defined(WIN64) && !defined(_WIN32) &&...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 10`, `args: 55`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 333`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `import: 10`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdio.h, keystone.h, string.h, inttypes.h, unistd.h, fcntl.h, limits.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/Object/ELFObjectFile.h` (C | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.257 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.313 IQR)
- **Top Global Matches:** file_cluster_8: 12.257, file_cluster_13: 12.392, file_cluster_0: 12.655
- **Magnitude:** 655.34 | **LOC:** 950 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (52.1653%), Tech Debt (24.0736%)
**Top Internal Functions/Classes:**
  * `classof` (Impact: 3.7 | O(N^6))
  * `classof` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 184`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 266`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 369`, `import: 17`
* *Defense:* `safety: 10`, `doc: 2`, `test: 8`, `immutability_locks: 212`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PointerIntPair.h, ObjectFile.h, DenseMap.h, ErrorHandling.h, Endian.h, cctype, ELF.h, utility...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/masm/KSExample_x86/KSExample_x86.Inc` (C | Tier 4 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.347 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.158 IQR)
- **Top Global Matches:** file_cluster_8: 16.347, file_cluster_0: 16.54, file_cluster_13: 16.555
- **Magnitude:** 602.52 | **LOC:** 87 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (64.0825%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`
* *Risk/State:* `state_mutation: 528`
* *Architecture:* `api: 58`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/masm/KSExample_x64/KSExample_x64.Inc` (C | Tier 4 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.449 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.154 IQR)
- **Top Global Matches:** file_cluster_8: 16.449, file_cluster_0: 16.636, file_cluster_13: 16.65
- **Magnitude:** 584.4 | **LOC:** 83 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (63.9093%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`
* *Risk/State:* `state_mutation: 518`
* *Architecture:* `api: 50`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/csharp/Keystone.Net/Engine.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.513 IQR)
- **Top Global Matches:** file_cluster_13: 14.513, file_cluster_7: 14.692, file_cluster_8: 14.695
- **Magnitude:** 526.78 | **LOC:** 371 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (41.8173%), Tech Debt (99.9774%)
**Top Internal Functions/Classes:**
  * `Assemble` (Impact: 121.7 | O(2^N) | DB: 5)
    * *Intent:* /// <summary> /// Encodes the given statement(s) into the given buffer. /// </summary> /// <param na...
  * `Assemble` (Impact: 79.9 | O(2^N) | DB: 8)
    * *Intent:* /// <summary> /// Encodes the given statement(s). /// </summary> /// <param name="toEncode">String t...
  * `SetOption` (Impact: 42.3 | O(2^N))
    * *Intent:* /// <summary> /// Sets an option in the engine. /// </summary> /// <param name="type">Type of the op...
  * `Assemble` (Impact: 37.4 | O(2^N) | DB: 4)
    * *Intent:* /// <summary> /// Encodes the given statement(s) into the given stream. /// </summary> /// <param na...
  * `ErrorToString` (Impact: 24.9 | O(2^N))
    * *Intent:* /// <summary> /// Returns the string associated with a given error code. /// </summary>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 32`, `args: 18`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `state_mutation: 87`, `duplicate_logic: 7`, `orphaned_logic: 2`
* *Architecture:* `api: 18`, `concurrency: 6`, `import: 4`
* *Defense:* `safety: 9`, `doc: 133`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System.IO, System.Threading, System.Runtime.InteropServices
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/Support/Dwarf.h` (C | Tier 4 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.173 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.393 IQR)
- **Top Global Matches:** file_cluster_8: 13.173, file_cluster_13: 13.248, file_cluster_7: 13.365
- **Magnitude:** 495.54 | **LOC:** 701 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (25.3465%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isType` (Impact: 24.4 | O(N^1))
  * `toBits` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 32`, `args: 23`, `func_start: 2`, `class_start: 26`
* *Risk/State:* `state_mutation: 370`, `dead_code: 1`
* *Architecture:* `api: 90`, `import: 8`
* *Defense:* `doc: 33`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` StringRef.h, Dwarf.def, Compiler.h, DataTypes.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/ADT/PointerUnion.h` (C | Tier 4 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.179 IQR)
- **Top Global Matches:** file_cluster_16: 13.179, file_cluster_8: 13.49, file_cluster_13: 13.675
- **Magnitude:** 435.76 | **LOC:** 475 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (30.3195%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `get` (Impact: 51.8 | O(2^N))
    * *Intent:* /// Returns the value of the specified pointer type. /// /// If the specified pointer type is incorr...
  * `isEqual` (Impact: 48.8 | O(2^N))
  * `get` (Impact: 22.5 | O(2^N))
    * *Intent:* /// Returns the value of the specified pointer type. /// /// If the specified pointer type is incorr...
  * `is` (Impact: 10.8 | O(N^6))
    * *Intent:* /// Test if the Union currently holds the type matching T.
  * `getAddrOfPtr1` (Impact: 10.7 | O(N^2))
    * *Intent:* /// If the union is set to the first pointer type get an address pointing to /// it.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 32`, `args: 81`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 118`, `duplicate_logic: 31`
* *Architecture:* `import: 3`
* *Defense:* `doc: 68`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DenseMapInfo.h, PointerIntPair.h, Compiler.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/Support/ELF.h` (C | Tier 4 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.621 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.163 IQR)
- **Top Global Matches:** file_cluster_8: 11.621, file_cluster_13: 11.849, file_cluster_7: 12.066
- **Magnitude:** 419.42 | **LOC:** 1325 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (94.2754%)
**Top Internal Functions/Classes:**
  * `setBinding` (Impact: 2.0 | O(N^1))
  * `setType` (Impact: 2.0 | O(N^1))
  * `setBinding` (Impact: 2.0 | O(N^1))
  * `setType` (Impact: 2.0 | O(N^1))
  * `setBindingAndType` (Impact: 1.9 | O(N^1) | DB: 1)
    * *Intent:* // Hexagon-specific e_flags
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 63`, `args: 6`, `func_start: 6`, `class_start: 33`
* *Risk/State:* `state_mutation: 307`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 91`, `import: 9`
* *Defense:* `doc: 6`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Compiler.h, DataTypes.h, cstring, RISCV.def, Sparc.def, Mips.def, SystemZ.def, WebAssembly.def...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/powershell/Keystone/Keystone.psm1` (POWERSHELL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.402 IQR)
- **Top Global Matches:** file_cluster_8: 12.402, file_cluster_0: 12.609, file_cluster_15: 12.658
- **Magnitude:** 391.62 | **LOC:** 313 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (45.5056%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Get-KeystoneAssembly` (Impact: 299.9 | O(N^4) | DB: 28)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 15`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 78`
* *Architecture:* `api: 10`
* *Defense:* `safety: 3`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/ADT/SmallVector.h` (C | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.29 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 6.57 IQR)
- **Top Global Matches:** file_cluster_13: 14.29, file_cluster_11: 14.529, file_cluster_8: 14.575
- **Magnitude:** 389.68 | **LOC:** 955 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (28.4371%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `resize` (Impact: 9.6 | O(N^2) | DB: 3)
  * `insert` (Impact: 9.4 | O(N^1) | DB: 5)
  * `erase` (Impact: 8.7 | O(2^N) | DB: 2)
  * `resize` (Impact: 8.1 | O(N^2))
  * `insert` (Impact: 6.9 | O(N^1) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 77`, `args: 2`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 188`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 17`
* *Architecture:* `api: 98`, `import: 13`
* *Defense:* `safety: 40`, `doc: 44`, `test: 12`, `immutability_locks: 26`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cassert, initializer_list, Compiler.h, type_traits.h, cstring, AlignOf.h, cstddef, iterator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/MC/MCRegisterInfo.h` (C | Tier 4 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.917 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.287 IQR)
- **Top Global Matches:** file_cluster_13: 14.917, file_cluster_0: 14.968, file_cluster_11: 15.079
- **Magnitude:** 389.48 | **LOC:** 695 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (25.6187%), Tech Debt (57.6272%)
**Top Internal Functions/Classes:**
  * `mapLLVMRegsToDwarfRegs` (Impact: 11.0 | O(N^6) | DB: 4)
  * `mapDwarfRegsToLLVMRegs` (Impact: 11.0 | O(N^6) | DB: 4)
  * `advance` (Impact: 4.8 | O(N^1) | DB: 6)
  * `advance` (Impact: 2.3 | O(N^1) | DB: 3)
    * *Intent:* /// DiffListIterator - Base iterator class that can traverse the /// differentially encoded register...
  * `mapLLVMRegToSEHReg` (Impact: 1.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 97`, `args: 28`, `func_start: 5`, `class_start: 3`
* *Risk/State:* `state_mutation: 157`, `dead_code: 7`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 194`, `import: 3`
* *Defense:* `safety: 11`, `doc: 164`, `test: 10`, `immutability_locks: 106`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DenseMap.h, ErrorHandling.h, cassert
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/masm/keystone_x64.inc` (C | Tier 4 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.483 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.629 IQR)
- **Top Global Matches:** file_cluster_8: 14.483, file_cluster_0: 14.724, file_cluster_13: 14.794
- **Magnitude:** 371.78 | **LOC:** 154 | **CtrlFlow:** 73.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (59.2449%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 4`
* *Risk/State:* `state_mutation: 248`
* *Architecture:* `api: 106`
* *Defense:* `safety: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/masm/keystone_x86.inc` (C | Tier 4 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.414 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.58 IQR)
- **Top Global Matches:** file_cluster_8: 14.414, file_cluster_0: 14.661, file_cluster_13: 14.731
- **Magnitude:** 365.78 | **LOC:** 153 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (58.5483%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 4`
* *Risk/State:* `state_mutation: 242`
* *Architecture:* `api: 106`
* *Defense:* `safety: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/ADT/APInt.h` (C | Tier 4 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.731 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 7.589 IQR)
- **Top Global Matches:** file_cluster_13: 13.731, file_cluster_7: 13.756, file_cluster_8: 13.892
- **Magnitude:** 358.42 | **LOC:** 1916 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (17.9959%), Tech Debt (10.1238%)
**Top Internal Functions/Classes:**
  * `getBitsSet` (Impact: 16.4 | O(N^3))
  * `getLowBitsSet` (Impact: 9.3 | O(N^1))
  * `getHighBitsSet` (Impact: 7.5 | O(N^1) | DB: 1)
  * `getSplat` (Impact: 5.6 | O(N^1) | DB: 3)
  * `isMask` (Impact: 5.4 | O(N^2))
    * *Intent:* /// \brief Bitwise OR assignment operator.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 127`, `args: 32`, `func_start: 43`, `class_start: 2`
* *Risk/State:* `state_mutation: 52`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 183`, `import: 7`
* *Defense:* `safety: 8`, `doc: 482`, `test: 8`, `immutability_locks: 116`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cassert, climits, Compiler.h, string, cstring, MathExtras.h, ArrayRef.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/Object/COFF.h` (C | Tier 4 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.707 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.935 IQR)
- **Top Global Matches:** file_cluster_8: 9.707, file_cluster_7: 10.375, file_cluster_13: 10.436
- **Magnitude:** 344.32 | **LOC:** 916 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.5514%), Tech Debt (16.6171%)
**Top Internal Functions/Classes:**
  * `classof` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 160`, `args: 1`, `func_start: 1`, `class_start: 30`
* *Risk/State:* `state_mutation: 36`, `fragile_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 292`, `import: 5`
* *Defense:* `safety: 22`, `doc: 3`, `test: 7`, `immutability_locks: 231`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ErrorOr.h, ObjectFile.h, Endian.h, PointerUnion.h, COFF.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/Support/ARMWinEH.h` (C | Tier 4 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_7` (Drift: 12.855 IQR)
- **Top Global Matches:** file_cluster_7: 12.855, file_cluster_8: 12.856, file_cluster_1: 13.06
- **Magnitude:** 337.26 | **LOC:** 383 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (12.7307%), Tech Debt (99.9417%)
**Top Internal Functions/Classes:**
  * `HeaderWords` (Impact: 311.1 | O(2^N) | DB: 3)
  * `HeaderWords` (Impact: 6.9 | O(N^1))
    * *Intent:* /// skipped) /// Epilogue Count : 5-bit field that differs in meaning based on the E field. /// /// ...
  * `EpilogueStartOffset` (Impact: 2.1 | O(N^1))
  * `Res` (Impact: 2.1 | O(N^1))
  * `Condition` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 5`, `args: 10`, `func_start: 17`
* *Risk/State:* `state_mutation: 9`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `import: 2`
* *Defense:* `doc: 133`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Endian.h, ArrayRef.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/haskell/src/Keystone.hs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.059 IQR)
- **Top Global Matches:** file_cluster_13: 12.059, file_cluster_8: 12.22, file_cluster_7: 12.492
- **Magnitude:** 335.8 | **LOC:** 129 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (17.8427%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 9`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `io: 1`, `import: 7`
* *Defense:* `safety: 4`, `doc: 24`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Control.Monad.Trans.Except, Keystone.Internal.Core, Data.List, Data.ByteString, Control.Monad.Trans.Class, Keystone.Internal.Keystone, Foreign
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/python/setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.849 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.592 IQR)
- **Top Global Matches:** file_cluster_13: 10.849, file_cluster_0: 11.384, file_cluster_8: 11.435
- **Magnitude:** 329.94 | **LOC:** 244 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 194
- **Risk Profile:** Cognitive Load (26.124%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `copy_sources` (Impact: 278.6 | O(2^N) | DB: 194)
    * *Intent:* """Copy the C sources into the source directory. This rearranges the source files under the python d...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 44`, `args: 7`, `func_start: 7`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 3`, `state_mutation: 37`, `dead_code: 1`
* *Architecture:* `io: 65`, `api: 11`, `import: 14`
* *Defense:* `safety: 4`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` shutil, subprocess, sys, distutils, distutils.util, os, stat, distutils.command.build...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/MC/MCStreamer.h` (C | Tier 4 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.416 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 7.411 IQR)
- **Top Global Matches:** file_cluster_13: 13.416, file_cluster_7: 13.637, file_cluster_6: 13.71
- **Magnitude:** 319.56 | **LOC:** 780 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (16.1825%), Tech Debt (60.0363%)
**Top Internal Functions/Classes:**
  * `SwitchSectionNoChange` (Impact: 14.4 | O(N^6) | DB: 4)
  * `PopSection` (Impact: 3.7 | O(N^1) | DB: 5)
  * `EmitRelocDirective` (Impact: 3.7 | O(N^6))
    * *Intent:* /// \brief Emit some number of copies of \p Value until the byte alignment \p
  * `EmitVersionMin` (Impact: 3.6 | O(N^6))
    * *Intent:* /// \brief Add a textual command. /// /// Typically for comments that can be emitted to the generate...
  * `SubSection` (Impact: 2.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 165`, `args: 27`, `func_start: 15`
* *Risk/State:* `state_mutation: 52`, `dead_code: 1`, `planned_debt: 11`, `fragile_debt: 1`
* *Architecture:* `api: 223`, `import: 10`
* *Defense:* `safety: 4`, `doc: 362`, `test: 1`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SMLoc.h, MCWinEH.h, MCDirectives.h, string, DataTypes.h, MCSymbol.h, MCLinkerOptimizationHint.h, MCDwarf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `llvm/include/llvm/ADT/ilist.h` (C) | Magnitude: 93.36 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 76, api: 43, pointers: 37, structural_boundaries: 35
- `bindings/python/keystone/keystone.py` (PYTHON) | Magnitude: 1702.4 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 130, encapsulation: 98, structural_boundaries: 50, state_mutation: 42
- `bindings/python/Makefile` (MAKEFILE) | Magnitude: 158.24 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 45, cleanup: 19, branch: 11, func_start: 9
- `llvm/include/llvm/MC/MCSchedule.h` (C) | Magnitude: 73.46 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 63, api: 47, immutability_locks: 25, structural_boundaries: 23
- `bindings/java/src/test/java/keystone/KeystoneTest.java` (JAVA) | Magnitude: 114.3 | Delta: **0.163 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 142, structural_boundaries: 67, func_start: 44, test: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `llvm/include/llvm/Support/Debug.h` (C) | Magnitude: 21.36 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 26, macros: 9, api: 6, reflection_metaprogramming: 5
- `suite/fuzz/gentargets.sh` (SHELL) | Magnitude: 3.28 | Delta: **0.6 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 46, reflection_metaprogramming: 46, serialization_parsing: 46, regex_execution: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `kstool/kstool.cpp` (CPP) | Magnitude: 722.08 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 333, indent_spaces: 270, branch: 94, args: 55
- `suite/regress/x86_lea_three.py` (PYTHON) | Magnitude: 5.22 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, api: 2, import: 2
- `llvm/include/llvm/ADT/IntEqClasses.h` (C) | Magnitude: 13.66 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, indent_spaces: 14, api: 9, structural_boundaries: 4
- `bindings/ruby/keystone_gem/Rakefile` (RUBY) | Magnitude: 2.14 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 1, structural_boundaries: 1, import: 1, orphaned_logic: 1
- `llvm/include/llvm/MC/MachineLocation.h` (C) | Magnitude: 38.66 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 23, api: 19, state_mutation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `llvm/include/llvm/ADT/iterator_range.h` (C) | Magnitude: 4.6 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 16, indent_spaces: 12, branch: 7, args: 6
- `llvm/include/llvm/ADT/IntrusiveRefCntPtr.h` (C) | Magnitude: 123.7 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 143, state_mutation: 58, args: 38, immutability_locks: 26
- `llvm/include/llvm/ADT/Optional.h` (C) | Magnitude: 93.44 | Delta: **0.173 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 98, state_mutation: 52, branch: 50, args: 45
- `llvm/include/llvm/Support/ErrorOr.h` (C) | Magnitude: 113.86 | Delta: **0.202 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 140, args: 50, branch: 40, doc: 36
- `llvm/include/llvm/Object/Binary.h` (C) | Magnitude: 127.2 | Delta: **0.216 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 91, state_mutation: 43, branch: 39, generics: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `suite/regress/c-crashers/run-all-overview.sh` (SHELL) | Magnitude: 31.22 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 16, indent_spaces: 14, state_mutation: 12, debug_prints: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `bindings/java/src/test/java/keystone/natives/CleanerContainerTest.java` (JAVA) | Magnitude: 63.28 | Delta: **0.738 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 42, indent_spaces: 21, structural_boundaries: 16, func_start: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `llvm/include/llvm/Support/ARMWinEH.h` (C) | Magnitude: 337.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 133, indent_spaces: 70, bitwise_ops: 28, branch: 27
- `llvm/include/llvm/MC/SectionKind.h` (C) | Magnitude: 250.82 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 86, state_mutation: 84, branch: 53, doc: 52
- `bindings/csharp/Keystone.Net/EncodedData.cs` (CSHARP) | Magnitude: 12.6 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 15, indent_spaces: 12, api: 5, state_mutation: 3
- `llvm/include/llvm/ADT/Hashing.h` (C) | Magnitude: 314.66 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 153, api: 102, state_mutation: 101, doc: 83
- `llvm/include/llvm/MC/MCInstrItineraries.h` (C) | Magnitude: 36.66 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 53, api: 19, indent_spaces: 19, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `llvm/include/llvm/Support/CBindingWrapping.h` (C) | Magnitude: 42.58 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, api: 9, macros: 5, pointers: 5
- `llvm/include/llvm/MC/MCInst.h` (C) | Magnitude: 164.98 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 130, api: 93, structural_boundaries: 60, immutability_locks: 39
- `llvm/utils/llvm-build/llvmbuild/configutil.py` (PYTHON) | Magnitude: 64.86 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, branch: 11, safety: 8, io: 8
- `llvm/include/llvm/Support/StringSaver.h` (C) | Magnitude: 15.34 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: pointers: 9, api: 7, immutability_locks: 6, indent_spaces: 6
- `llvm/include/llvm/ADT/StringSet.h` (C) | Magnitude: 23.4 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, api: 4, state_mutation: 4, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `kstool/getopt.h` (CPP) | Magnitude: 14.68 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 3, immutability_locks: 3, indent_spaces: 3, globals: 2
- `llvm/include/llvm/Support/ELFRelocs/WebAssembly.def` (MAKEFILE) | Magnitude: 11.56 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1
- `debian/rules` (MAKEFILE) | Magnitude: 12.08 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 2, func_start: 1, dead_code: 1, sec_high_risk_execution: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `bindings/java/src/main/java/keystone/KeystoneError.java` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 26.6762%)
- `llvm/utils/llvm-build/llvmbuild/main.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 88.3448%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `llvm/include/llvm/ADT/iterator.h` -> **Severity: 0.669** (Embedded: 0.0211 * Error Risk: 31.7812%)
- `suite/regress/regress.py` -> **Severity: 0.504** (Embedded: 0.1137 * Error Risk: 4.4337%)
- `bindings/java/src/main/java/keystone/KeystoneError.java` -> **Severity: 0.356** (Embedded: 0.0095 * Error Risk: 37.5499%)
- `bindings/java/src/main/java/keystone/utilities/Version.java` -> **Severity: 0.216** (Embedded: 0.0042 * Error Risk: 51.3041%)
- `bindings/java/src/main/java/keystone/KeystoneOptionType.java` -> **Severity: 0.2** (Embedded: 0.0038 * Error Risk: 52.7246%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `suite/regress/regress.py` -> **Severity: 7125.461** (Blast Radius: 83.265 * Doc Risk: 85.5757%)
- `llvm/include/llvm/ADT/iterator.h` -> **Severity: 1684.809** (Blast Radius: 16.866 * Doc Risk: 99.8938%)
- `llvm/utils/llvm-build/llvmbuild/util.py` -> **Severity: 633.962** (Blast Radius: 9.533 * Doc Risk: 66.5018%)
- `llvm/include/llvm/Object/Error.h` -> **Severity: 479.249** (Blast Radius: 4.793 * Doc Risk: 99.9894%)
- `llvm/include/llvm/Support/type_traits.h` -> **Severity: 416.85** (Blast Radius: 4.793 * Doc Risk: 86.9706%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
