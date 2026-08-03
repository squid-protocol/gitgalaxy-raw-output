# ARCHITECTURAL_BRIEF: nasm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/nasm` |
| **Timestamp** | `2026-08-03T19:27:30.535610+00:00` |
| **Scan Duration** | `1.4s` |
| **Git Branch** | `master` |
| **Git Commit** | `3cb6231581679a9ab1a8eeb0342375eb7002cebe` |
| **Git Remote** | `https://github.com/netwide-assembler/nasm.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 137 malicious artifacts.

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
| Total Artifacts | 1337 |
| Analyzed Artifacts (Scanned) | 187 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1150 |
| Total LOC | 31706 |
| Volatility Index | 0.016 |
| % Scanned of codebase = | 14.0% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2753 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3769 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1751 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 88 | 22243 | 47.1% |
| M4 | 39 | 552 | 20.9% |
| PERL | 31 | 7278 | 16.6% |
| PLAINTEXT | 10 | 0 | 5.3% |
| MARKDOWN | 5 | 0 | 2.7% |
| MAKEFILE | 5 | 817 | 2.7% |
| SHELL | 3 | 47 | 1.6% |
| CSS | 2 | 239 | 1.1% |
| BATCH | 1 | 9 | 0.5% |
| ASSEMBLY | 1 | 0 | 0.5% |
| PYTHON | 1 | 504 | 0.5% |
| JSON | 1 | 17 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.518`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 141 | 75.4% |
| file_cluster_13 | 23 | 12.3% |
| file_cluster_0 | 5 | 2.7% |
| file_cluster_9 | 2 | 1.1% |
| file_cluster_17 | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 15 | 8.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1150*

**Composition by Extension & Reason:**
- `.asm`: 472x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.t`: 217x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 191x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 86x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 81 LOC)
- `.src`: 24x Excluded (Unsupported Extension: '.src')
- `.mac`: 21x Excluded (Unsupported Extension: '.mac'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 349 LOC)
- `.h`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 231 LOC), 1x Excluded (Machine-Generated Source Code Signature: 33 LOC)
- `.pl`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 362 LOC), 1x Excluded (Machine-Generated Source Code Signature: 36 LOC)
- `.sh`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 23 LOC)
- `.dat`: 6x Excluded (Unsupported Extension: '.dat')
- `.in`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 672 LOC)
- `.ph`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 98.8 | 37.3 | 13.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 32.4 | 8.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 19.5 | 2.3 | 80.0 |
| API Exposure | 0.0 | 16.9 | 5.4 | 3.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 46.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 92.7 | 2.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 83.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.8 | 1.6 | 2.2 | 2.2 |
| Volatility Exposure | 0.0 | 100.0 | 12.1 | 4.7 | 4.5 |
| Documentation Exposure | 0.0 | 100.0 | 59.6 | 66.6 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 31.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `travis/nasm-t.py` (Hits: 33)
- `misc/nasmstab` (Hits: 22)
- `doc/genps.pl` (Hits: 17)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **compiler.h** (`include/compiler.h`) — 57 inbound connections
2. **nasm.h** (`include/nasm.h`) — 35 inbound connections
3. **error.h** (`include/error.h`) — 26 inbound connections
4. **nctype.h** (`include/nctype.h`) — 20 inbound connections
5. **outform.h** (`output/outform.h`) — 11 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **compiler.h** (`include/compiler.h`) — 24 outbound dependencies
2. **nasm.c** (`asm/nasm.c`) — 20 outbound dependencies
3. **outelf.c** (`output/outelf.c`) — 17 outbound dependencies
4. **directiv.c** (`asm/directiv.c`) — 16 outbound dependencies
5. **outmacho.c** (`output/outmacho.c`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `user_error` (@ `asm/preproc.c`) -> Impact: **5816.6** | LOC: 2120
  * *Intent:* /* A macro or preprocessor function identifier? */
- `assemble` (@ `asm/assemble.c`) -> Impact: **4464.2** | LOC: 1868
- `parse_eops` (@ `asm/parser.c`) -> Impact: **3821.7** | LOC: 778
  * *Intent:* if (vect->type <= EXPR_REG_END) /* false if a register is present */
- `elf32_out` (@ `output/outelf.c`) -> Impact: **3337.0** | LOC: 1625
  * *Intent:* /* * If sym->section == SHN_ABS, then the first line of the * else section would cause a core dump, because its a reference * beyond the end of the se...
- `show_bytecodes` (@ `x86/insns.pl`) -> Impact: **2246.2** | LOC: 756
  * *Intent:* # # Extract byte codes in human-friendly form. Added as a comment # to insnsa.c/insnsd.c to help debugging. #
- `elf_deflabel` (@ `output/outelf.c`) -> Impact: **1380.8** | LOC: 181
- `show_diff` (@ `travis/nasm-t.py`) -> Impact: **1258.2** | LOC: 245
- `process_ea` (@ `asm/assemble.c`) -> Impact: **894.8** | LOC: 466
- `expr6` (@ `asm/eval.c`) -> Impact: **781.8** | LOC: 192
- `html_filename` (@ `doc/rdsrc.pl`) -> Impact: **765.7** | LOC: 454

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `out_eops` (@ `asm/assemble.c`) -> **O(2^N) [Recursive]**
- `die_hard` (@ `asm/error.c`) -> **O(2^N) [Recursive]**
- `expr6` (@ `asm/eval.c`) -> **O(2^N) [Recursive]**
- `cexpr` (@ `asm/eval.c`) -> **O(2^N) [Recursive]**
- `parse_eops` (@ `asm/parser.c`) -> **O(2^N) [Recursive]**
  * *Intent:* if (vect->type <= EXPR_REG_END) /* false if a register is present */
- `user_error` (@ `asm/preproc.c`) -> **O(2^N) [Recursive]**
  * *Intent:* /* A macro or preprocessor function identifier? */
- `bin_cleanup` (@ `output/outbin.c`) -> **O(2^N) [Recursive]**
  * *Intent:* int64_t length; /* section length in bytes */
- `elf32_out` (@ `output/outelf.c`) -> **O(2^N) [Recursive]**
  * *Intent:* /* * If sym->section == SHN_ABS, then the first line of the * else section would cause a core dump, because its a reference * beyond the end of the se...
- `elf_deflabel` (@ `output/outelf.c`) -> **O(2^N) [Recursive]**
- `show_diff` (@ `travis/nasm-t.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `user_error` (@ `asm/preproc.c`) -> DB Complexity: **649**
  * *Intent:* /* A macro or preprocessor function identifier? */
- `elf32_out` (@ `output/outelf.c`) -> DB Complexity: **435**
  * *Intent:* /* * If sym->section == SHN_ABS, then the first line of the * else section would cause a core dump, because its a reference * beyond the end of the se...
- `assemble` (@ `asm/assemble.c`) -> DB Complexity: **380**
- `show_bytecodes` (@ `x86/insns.pl`) -> DB Complexity: **277**
  * *Intent:* # # Extract byte codes in human-friendly form. Added as a comment # to insnsa.c/insnsd.c to help debugging. #
- `parse_eops` (@ `asm/parser.c`) -> DB Complexity: **226**
  * *Intent:* if (vect->type <= EXPR_REG_END) /* false if a register is present */
- `html_filename` (@ `doc/rdsrc.pl`) -> DB Complexity: **176**
- `process_ea` (@ `asm/assemble.c`) -> DB Complexity: **152**
- `addidx` (@ `doc/rdsrc.pl`) -> DB Complexity: **112**
- `read_tokhash_c` (@ `editors/nasmtok.pl`) -> DB Complexity: **102**
- `nasm_quote` (@ `asm/quote.c`) -> DB Complexity: **87**
  * *Intent:* /* SPDX-License-Identifier: BSD-2-Clause */ /* Copyright 1996-2020 The NASM Authors - All Rights Reserved */ /* * quote.c */ #include "compiler.h" #in...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `asm` | 33 | 34501.0 | 53.73% | 27.89% |
| `output` | 18 | 14376.9 | 40.01% | 12.35% |
| `x86` | 7 | 5935.84 | 57.97% | 11.24% |
| `doc` | 14 | 5059.0 | 56.35% | 28.54% |
| `disasm` | 7 | 2729.88 | 52.61% | 30.46% |
| `include` | 23 | 2544.09 | 22.18% | 8.51% |
| `misc` | 9 | 1885.46 | 47.53% | 0.0% |
| `travis` | 3 | 1833.16 | 19.36% | 4.71% |
| `autoconf/m4` | 39 | 1076.69 | 8.24% | 22.91% |
| `editors` | 1 | 487.4 | 83.38% | 16.62% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `include/ilog2.h` -> **100.0%** Exposure
- `autoconf/m4/pa_prog_cc.m4` -> **100.0%** Exposure
- `autoconf/m4/pa_variadic_macros.m4` -> **100.0%** Exposure
- `templates/template.sh` -> **100.0%** Exposure
- `tools/Nindent` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `asm/assemble.c` -> **100.0%** Exposure
- `asm/directiv.c` -> **100.0%** Exposure
- `asm/error.c` -> **100.0%** Exposure
- `asm/eval.c` -> **100.0%** Exposure
- `asm/getbool.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `asm/preproc.c` -> **13** Orphaned Functions | **0** Duplicates
- `include/ilog2.h` -> **0** Orphaned Functions | **10** Duplicates
- `asm/nasm.c` -> **8** Orphaned Functions | **0** Duplicates
- `asm/stdscan.c` -> **7** Orphaned Functions | **0** Duplicates
- `common/errstubs.c` -> **7** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`asm/assemble.c`** -> AI Confidence: **99.48%**
2. **`asm/directiv.c`** -> AI Confidence: **99.48%**
3. **`asm/parser.c`** -> AI Confidence: **99.48%**
4. **`disasm/disasm.c`** -> AI Confidence: **99.48%**
5. **`include/compiler.h`** -> AI Confidence: **99.42%**
6. **`disasm/ndisasm.c`** -> AI Confidence: **99.39%**
7. **`output/outas86.c`** -> AI Confidence: **99.39%**
8. **`asm/eval.c`** -> AI Confidence: **99.34%**
9. **`asm/quote.c`** -> AI Confidence: **99.34%**
10. **`asm/listing.c`** -> AI Confidence: **99.31%**
11. **`asm/nasm.c`** -> AI Confidence: **99.31%**
12. **`asm/preproc.c`** -> AI Confidence: **99.31%**
13. **`asm/stdscan.c`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `asm/warnings.pl` -> **100.0%** Exposure
- `doc/findfont.ph` -> **100.0%** Exposure
- `doc/genps.pl` -> **100.0%** Exposure
- `doc/pspdf.pl` -> **100.0%** Exposure
- `doc/rdsrc.pl` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `asm/warnings.pl` -> **100.0%** Exposure
- `doc/pspdf.pl` -> **100.0%** Exposure
- `misc/nasmstab` -> **100.0%** Exposure
- `misc/nxdisasm.pl` -> **100.0%** Exposure
- `nsis/getpearch.pl` -> **100.0%** Exposure
### Raw Memory Manipulation
- `output/outelf.c` -> **10.0%** Exposure
- `asm/labels.c` -> **9.4557%** Exposure
- `asm/nasm.c` -> **8.2955%** Exposure
- `asm/srcfile.h` -> **1.6844%** Exposure
- `asm/error.c` -> **0.1799%** Exposure
### Algorithmic DoS Exposure
- `asm/assemble.c` -> **100.0%** Exposure
- `asm/assemble.h` -> **100.0%** Exposure
- `asm/directiv.c` -> **100.0%** Exposure
- `asm/error.c` -> **100.0%** Exposure
- `asm/eval.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `7` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `490` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `output/outform.c` (C) -> Cumulative Risk: **797.0**
- **Archetype:** `file_cluster_13` (Distance: 13.33 IQR)
- **Magnitude:** 191.52 | **LOC:** 106 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `ofmt_list` (Impact: 35.7), `dfmt_list` (Impact: 29.3), `ofmt_find` (Impact: 22.1)

### 2. `asm/stdscan.c` (C) -> Cumulative Risk: **796.43**
- **Archetype:** `file_cluster_13` (Distance: 13.962 IQR)
- **Magnitude:** 461.86 | **LOC:** 479 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `stdscan_parse_braces` (Impact: 136.9), `stdscan_alloc` (Impact: 12.8), `stdscan_reset` (Impact: 8.3)

### 3. `asm/preproc.c` (C) -> Cumulative Risk: **792.14**
- **Archetype:** `file_cluster_8` (Distance: 15.259 IQR)
- **Magnitude:** 9346.24 | **LOC:** 9262 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 66.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `user_error` (Impact: 5816.6), `list_smacro_def` (Impact: 145.3), `assign_smacro` (Impact: 40.6)

### 4. `x86/insns.pl` (PERL) -> Cumulative Risk: **790.97**
- **Archetype:** `file_cluster_8` (Distance: 15.046 IQR)
- **Magnitude:** 4577.02 | **LOC:** 1672 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 61.9%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `show_bytecodes` (Impact: 2246.2), `format_insn` (Impact: 260.8), `relaxed_forms` (Impact: 125.5)

### 5. `asm/assemble.c` (C) -> Cumulative Risk: **775.05**
- **Archetype:** `file_cluster_8` (Distance: 14.545 IQR)
- **Magnitude:** 9162.6 | **LOC:** 4164 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 61.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `assemble` (Impact: 4464.2), `process_ea` (Impact: 894.8), `no_match_error` (Impact: 331.1)

### 6. `asm/nasm.c` (C) -> Cumulative Risk: **773.75**
- **Archetype:** `file_cluster_13` (Distance: 13.676 IQR)
- **Magnitude:** 1565.98 | **LOC:** 2170 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `assemble_file` (Impact: 347.5), `nasm_set_limit` (Impact: 173.3), `main` (Impact: 134.9)

### 7. `doc/pspdf.pl` (PERL) -> Cumulative Risk: **764.12**
- **Archetype:** `file_cluster_0` (Distance: 12.342 IQR)
- **Magnitude:** 181.46 | **LOC:** 137 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `win32_gs_help` (Impact: 104.5)

### 8. `asm/parser.c` (C) -> Cumulative Risk: **757.12**
- **Archetype:** `file_cluster_8` (Distance: 14.36 IQR)
- **Magnitude:** 5317.94 | **LOC:** 1475 | **CtrlFlow:** 78.7% | **Authorship Centralization:** 76.9%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `parse_eops` (Impact: 3821.7), `process_size_override` (Impact: 157.7), `parse_mref` (Impact: 96.3)

### 9. `asm/quote.c` (C) -> Cumulative Risk: **755.68**
- **Archetype:** `file_cluster_8` (Distance: 14.606 IQR)
- **Magnitude:** 1506.32 | **LOC:** 571 | **CtrlFlow:** 93.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `nasm_unquote_anystr` (Impact: 673.9), `nasm_quote` (Impact: 191.5), `emit_utf8` (Impact: 33.5)

### 10. `asm/getbool.c` (C) -> Cumulative Risk: **745.59**
- **Archetype:** `file_cluster_13` (Distance: 12.519 IQR)
- **Magnitude:** 112.28 | **LOC:** 77 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `get_boolean_option` (Impact: 63.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `asm/preproc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.259 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.111 IQR)
- **Top Global Matches:** file_cluster_8: 15.259, file_cluster_13: 15.384, file_cluster_11: 15.427
- **Magnitude:** 9346.24 | **LOC:** 9262 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 66.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 649
- **Risk Profile:** Cognitive Load (96.3415%), Tech Debt (19.2531%)
**Top Internal Functions/Classes:**
  * `user_error` (Impact: 5816.6 | O(2^N) | DB: 649)
    * *Intent:* /* A macro or preprocessor function identifier? */
  * `list_smacro_def` (Impact: 145.3 | O(N^6) | DB: 53)
    * *Intent:* /*
  * `assign_smacro` (Impact: 40.6 | O(N^6) | DB: 6)
    * *Intent:* /* * Counters to trap on insane macro recursion or processing. * Note: for smacros these count *down...
  * `pp_strcat` (Impact: 40.5 | O(N^6) | DB: 8)
  * `check_mmacro_refcounts` (Impact: 40.4 | O(N^5) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 675`, `structural_boundaries: 344`, `args: 30`, `func_start: 77`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 2552`, `planned_debt: 3`, `fragile_debt: 2`, `orphaned_logic: 13`
* *Architecture:* `io: 1`, `api: 483`, `import: 15`
* *Defense:* `safety: 19`, `immutability_locks: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` nasm.h, hashtbl.h, assemble.h, stdscan.h, dbginfo.h, eval.h, quote.h, error.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/assemble.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.545 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.557 IQR)
- **Top Global Matches:** file_cluster_8: 14.545, file_cluster_13: 14.773, file_cluster_11: 14.793
- **Magnitude:** 9162.6 | **LOC:** 4164 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 61.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 380
- **Risk Profile:** Cognitive Load (98.8357%), Tech Debt (13.3941%)
**Top Internal Functions/Classes:**
  * `assemble` (Impact: 4464.2 | O(N^6) | DB: 380)
  * `process_ea` (Impact: 894.8 | O(N^6) | DB: 152)
  * `no_match_error` (Impact: 331.1 | O(N^6))
  * `out_eops` (Impact: 306.6 | O(2^N) | DB: 22)
  * `add_asp` (Impact: 146.2 | O(N^5) | DB: 32)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1303`, `structural_boundaries: 280`, `args: 27`, `func_start: 52`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2073`, `dead_code: 1`, `fragile_debt: 4`, `orphaned_logic: 6`
* *Architecture:* `io: 2`, `api: 435`, `import: 10`
* *Defense:* `safety: 14`, `immutability_locks: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` nasm.h, assemble.h, dbginfo.h, insns.h, disp8.h, error.h, compiler.h, tables.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outelf.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.274 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.151 IQR)
- **Top Global Matches:** file_cluster_8: 14.274, file_cluster_13: 14.367, file_cluster_0: 14.48
- **Magnitude:** 7633.18 | **LOC:** 3636 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 435
- **Risk Profile:** Cognitive Load (90.7874%), Tech Debt (12.2894%)
**Top Internal Functions/Classes:**
  * `elf32_out` (Impact: 3337.0 | O(2^N) | DB: 435)
    * *Intent:* /* * If sym->section == SHN_ABS, then the first line of the * else section would cause a core dump, ...
  * `elf_deflabel` (Impact: 1380.8 | O(2^N) | DB: 53)
  * `elf_section_attrib` (Impact: 669.7 | O(N^6) | DB: 54)
  * `elf_section_names` (Impact: 107.5 | O(N^4) | DB: 22)
  * `elf_add_gsym_reloc` (Impact: 85.3 | O(N^6) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 412`, `structural_boundaries: 325`, `args: 82`, `func_start: 47`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1627`, `dead_code: 7`, `fragile_debt: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 243`, `import: 17`
* *Defense:* `safety: 18`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` nasm.h, stdscan.h, hashtbl.h, ver.h, outlib.h, outform.h, eval.h, rbtree.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/parser.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.36 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.791 IQR)
- **Top Global Matches:** file_cluster_8: 14.36, file_cluster_13: 14.433, file_cluster_11: 14.556
- **Magnitude:** 5317.94 | **LOC:** 1475 | **CtrlFlow:** 78.7% | **Authorship Centralization:** 76.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 226
- **Risk Profile:** Cognitive Load (98.5758%), Tech Debt (9.6809%)
**Top Internal Functions/Classes:**
  * `parse_eops` (Impact: 3821.7 | O(2^N) | DB: 226)
    * *Intent:* if (vect->type <= EXPR_REG_END) /* false if a register is present */
  * `process_size_override` (Impact: 157.7 | O(N^6) | DB: 18)
  * `parse_mref` (Impact: 96.3 | O(N^5) | DB: 19)
  * `mref_set_optype` (Impact: 79.8 | O(N^6) | DB: 19)
  * `parse_decorators` (Impact: 79.2 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 447`, `structural_boundaries: 121`, `args: 5`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 868`, `orphaned_logic: 2`
* *Architecture:* `api: 169`, `import: 12`
* *Defense:* `safety: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` nasm.h, stdscan.h, parser.h, assemble.h, floats.h, insns.h, eval.h, error.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x86/insns.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.046 IQR)
- **Top Global Matches:** file_cluster_8: 15.046, file_cluster_0: 15.155, file_cluster_17: 15.256
- **Magnitude:** 4577.02 | **LOC:** 1672 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 61.9%
- **Algorithmic:** O(N^5) | **DB Complexity:** 277
- **Risk Profile:** Cognitive Load (97.9411%), Tech Debt (9.1293%)
**Top Internal Functions/Classes:**
  * `show_bytecodes` (Impact: 2246.2 | O(N^5) | DB: 277)
    * *Intent:* # # Extract byte codes in human-friendly form. Added as a comment # to insnsa.c/insnsd.c to help deb...
  * `format_insn` (Impact: 260.8 | O(N^5) | DB: 77)
  * `relaxed_forms` (Impact: 125.5 | O(N^2) | DB: 50)
    * *Intent:* # Generate relaxed form patterns if applicable # * is used for an optional source operand, duplicati...
  * `startseq` (Impact: 61.4 | O(N^3) | DB: 28)
  * `count_bytecodes` (Impact: 56.8 | O(N^3) | DB: 11)
    * *Intent:* # Count primary bytecodes, for statistics
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 690`, `structural_boundaries: 239`, `args: 32`, `func_start: 15`
* *Risk/State:* `state_mutation: 1700`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `import: 3`
* *Defense:* `cleanup: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ndmask, of, the, position, bytecode, explicit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/eval.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.907 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.455 IQR)
- **Top Global Matches:** file_cluster_8: 12.907, file_cluster_13: 13.117, file_cluster_7: 13.285
- **Magnitude:** 2847.34 | **LOC:** 1041 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (82.9663%), Tech Debt (8.8296%)
**Top Internal Functions/Classes:**
  * `expr6` (Impact: 781.8 | O(2^N) | DB: 24)
  * `expr5` (Impact: 231.2 | O(N^6) | DB: 14)
  * `rexp3` (Impact: 225.9 | O(N^6) | DB: 16)
  * `cexpr` (Impact: 130.5 | O(2^N) | DB: 5)
  * `expr3` (Impact: 105.8 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 159`, `args: 32`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `state_mutation: 481`, `orphaned_logic: 1`
* *Architecture:* `api: 203`, `import: 10`
* *Defense:* `safety: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` nasm.h, assemble.h, labels.h, ilog2.h, floats.h, eval.h, error.h, compiler.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/rdsrc.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.701 IQR)
- **Top Global Matches:** file_cluster_8: 14.701, file_cluster_0: 14.708, file_cluster_11: 14.949
- **Magnitude:** 2580.2 | **LOC:** 1291 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 176
- **Risk Profile:** Cognitive Load (97.1911%), Tech Debt (17.4204%)
**Top Internal Functions/Classes:**
  * `html_filename` (Impact: 765.7 | O(2^N) | DB: 176)
  * `addidx` (Impact: 221.9 | O(N^2) | DB: 112)
  * `word_txt` (Impact: 95.4 | O(2^N) | DB: 5)
  * `include` (Impact: 25.4 | O(N^1) | DB: 19)
  * `untabify` (Impact: 9.6 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 164`, `args: 35`, `func_start: 27`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1414`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 5`
* *Architecture:* `io: 14`, `import: 1`
* *Defense:* `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` this, File::Spec, visible
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `travis/nasm-t.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.939 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.132 IQR)
- **Top Global Matches:** file_cluster_8: 9.939, file_cluster_13: 10.247, file_cluster_17: 10.433
- **Magnitude:** 1814.48 | **LOC:** 599 | **CtrlFlow:** 67.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 65
- **Risk Profile:** Cognitive Load (44.1755%), Tech Debt (14.1176%)
**Top Internal Functions/Classes:**
  * `show_diff` (Impact: 1258.2 | O(2^N) | DB: 65)
  * `expand_templates` (Impact: 358.4 | O(2^N) | DB: 30)
    * *Intent:* # # Expand ref/id in descriptors array
  * `test_updated` (Impact: 105.7 | O(N^6) | DB: 4)
  * `is_valid_desc` (Impact: 10.8 | O(N^2))
    * *Intent:* # # Check if descriptor has mandatory fields
  * `read_stdfile` (Impact: 5.4 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 84`, `args: 23`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 36`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 33`, `api: 22`, `import: 9`
* *Defense:* `safety: 7`, `test: 8`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` difflib, os, json, argparse, filecmp, subprocess, sys, fnmatch...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/genps.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.344 IQR)
- **Top Global Matches:** file_cluster_8: 14.344, file_cluster_0: 14.395, file_cluster_11: 14.523
- **Magnitude:** 1653.14 | **LOC:** 1311 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (78.5995%), Tech Debt (14.8347%)
**Top Internal Functions/Classes:**
  * `ps_start_page` (Impact: 231.9 | O(2^N) | DB: 42)
    * *Intent:* # Start a PostScript page
  * `int2base` (Impact: 191.3 | O(N^2) | DB: 81)
    * *Intent:* # # Convert an integer to a chosen base #
  * `ps_string` (Impact: 118.7 | O(2^N) | DB: 19)
    * *Intent:* # Generate a PostScript string
  * `ps_break_lines` (Impact: 107.4 | O(N^5) | DB: 30)
    * *Intent:* # # Break or convert paragraphs into lines, and push them # onto the @pslines array. #
  * `ps_break_pages` (Impact: 51.4 | O(N^1) | DB: 26)
    * *Intent:* # # This formats lines inside the global @pslines array into pages, # updating the page and y-coordi...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 303`, `structural_boundaries: 213`, `args: 39`, `func_start: 15`
* *Risk/State:* `state_mutation: 911`, `dead_code: 7`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 17`, `import: 2`
* *Defense:* `cleanup: 56`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Spec, it, longer, require, font
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/nasm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.676 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.134 IQR)
- **Top Global Matches:** file_cluster_13: 13.676, file_cluster_8: 13.777, file_cluster_11: 13.992
- **Magnitude:** 1565.98 | **LOC:** 2170 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (78.7416%), Tech Debt (22.6278%)
**Top Internal Functions/Classes:**
  * `assemble_file` (Impact: 347.5 | O(N^6) | DB: 27)
  * `nasm_set_limit` (Impact: 173.3 | O(N^6) | DB: 19)
  * `main` (Impact: 134.9 | O(N^5) | DB: 23)
  * `define_macros` (Impact: 81.3 | O(N^3) | DB: 12)
  * `nasm_quote_filename` (Impact: 66.5 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 110`, `args: 23`, `func_start: 21`, `class_start: 11`
* *Risk/State:* `state_mutation: 445`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 4`, `api: 107`, `import: 21`
* *Defense:* `safety: 6`, `immutability_locks: 40`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` nasm.h, assemble.h, floats.h, stdscan.h, insns.h, eval.h, iflag.h, error.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/quote.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.606 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.928 IQR)
- **Top Global Matches:** file_cluster_8: 14.606, file_cluster_13: 14.623, file_cluster_11: 14.689
- **Magnitude:** 1506.32 | **LOC:** 571 | **CtrlFlow:** 93.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 87
- **Risk Profile:** Cognitive Load (94.1963%), Tech Debt (13.9801%)
**Top Internal Functions/Classes:**
  * `nasm_unquote_anystr` (Impact: 673.9 | O(N^6) | DB: 59)
  * `nasm_quote` (Impact: 191.5 | O(N^2) | DB: 87)
    * *Intent:* /* SPDX-License-Identifier: BSD-2-Clause */ /* Copyright 1996-2020 The NASM Authors - All Rights Res...
  * `emit_utf8` (Impact: 33.5 | O(N^2) | DB: 27)
  * `nasm_quote_cstr` (Impact: 3.9 | O(N^1) | DB: 3)
    * *Intent:* #define EMIT_UTF8(c) \
  * `ctlbit` (Impact: 2.2 | O(N^1))
    * *Intent:* /* * Note: this is invalid even for "classic" (pre-UTF16) 31-bit * UTF-8 if the value is >= 0x800000...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 13`, `args: 4`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 540`, `orphaned_logic: 2`
* *Architecture:* `api: 54`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` quote.h, error.h, compiler.h, nctype.h, nasmlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outmacho.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.461 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.598 IQR)
- **Top Global Matches:** file_cluster_8: 13.461, file_cluster_13: 13.621, file_cluster_7: 13.851
- **Magnitude:** 1315.38 | **LOC:** 2530 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (66.734%), Tech Debt (11.4327%)
**Top Internal Functions/Classes:**
  * `macho_dbg_output` (Impact: 131.7 | O(N^6) | DB: 32)
  * `macho_dbg_linenum` (Impact: 61.8 | O(N^5) | DB: 8)
    * *Intent:* /* * This is a NASM special symbol. We never allow it into * the Macho-O symbol table, even if it's ...
  * `new_file_list` (Impact: 40.9 | O(N^4) | DB: 16)
  * `macho_pragma` (Impact: 31.6 | O(N^2) | DB: 2)
  * `macho_write_segment` (Impact: 27.6 | O(N^3) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 161`, `args: 24`, `func_start: 22`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 672`, `orphaned_logic: 4`
* *Architecture:* `api: 148`, `import: 16`
* *Defense:* `safety: 2`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` macho.h, nasm.h, hashtbl.h, ver.h, outlib.h, labels.h, ilog2.h, rbtree.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outas86.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.288 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.126 IQR)
- **Top Global Matches:** file_cluster_8: 13.288, file_cluster_13: 13.37, file_cluster_0: 13.657
- **Magnitude:** 1310.26 | **LOC:** 580 | **CtrlFlow:** 73.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (79.3307%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `as86_out` (Impact: 254.7 | O(N^6) | DB: 12)
  * `as86_deflabel` (Impact: 200.0 | O(N^6) | DB: 18)
  * `as86_write_section` (Impact: 155.1 | O(N^4) | DB: 12)
  * `as86_add_piece` (Impact: 131.1 | O(N^6) | DB: 16)
  * `as86_write` (Impact: 100.9 | O(N^3) | DB: 29)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 55`, `args: 17`, `func_start: 11`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 309`
* *Architecture:* `api: 69`, `import: 9`
* *Defense:* `safety: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` nasm.h, outlib.h, outform.h, saa.h, error.h, compiler.h, nctype.h, nasmlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `include/compiler.h` (C | Tier 4 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.616 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 4.637 IQR)
- **Top Global Matches:** file_cluster_8: 10.616, file_cluster_13: 10.852, file_cluster_12: 11.294
- **Magnitude:** 1217.84 | **LOC:** 480 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 54.5%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (39.8472%), Tech Debt (18.8722%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 10`, `args: 8`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `fragile_debt: 1`
* *Architecture:* `api: 8`, `import: 22`
* *Defense:* `safety: 12`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 138.749
  * `Choke Point (Betweenness):` 0.010026 | `Ripple Effect (Closeness):` 0.312156
  * `Imports (Out-Degree: 5):` limits.h, config.h, stdlib.h, stdbit.h, endian.h, nasmint.h, watcom.h, unconfig.h...
  * `Imported By (In-Degree: 57):` (Excluded from Brief to save tokens)

### `output/outbin.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.46 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.753 IQR)
- **Top Global Matches:** file_cluster_8: 13.46, file_cluster_7: 13.84, file_cluster_13: 13.872
- **Magnitude:** 1187.58 | **LOC:** 1637 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (72.206%), Tech Debt (18.9279%)
**Top Internal Functions/Classes:**
  * `bin_directive` (Impact: 222.5 | O(N^6) | DB: 24)
  * `write_srecord` (Impact: 104.7 | O(N^6) | DB: 14)
  * `bin_cleanup` (Impact: 91.8 | O(2^N) | DB: 20)
    * *Intent:* int64_t length; /* section length in bytes */
  * `bin_secname` (Impact: 81.5 | O(N^6) | DB: 15)
    * *Intent:* /* Step 2: Sort the progbits sections into their output order. */
  * `do_output_srec` (Impact: 48.8 | O(N^3) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 78`, `args: 22`, `func_start: 17`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 433`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 85`
* *Defense:* `safety: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` nasm.h, stdscan.h, outlib.h, labels.h, outform.h, eval.h, saa.h, error.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `misc/omfdump.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.874 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.133 IQR)
- **Top Global Matches:** file_cluster_8: 13.874, file_cluster_13: 14.068, file_cluster_0: 14.105
- **Magnitude:** 1078.76 | **LOC:** 819 | **CtrlFlow:** 65.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (76.3224%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hexdump_data` (Impact: 95.2 | O(N^6) | DB: 7)
  * `dump_segdef` (Impact: 55.6 | O(N^3) | DB: 15)
  * `dump_fixdat` (Impact: 46.7 | O(N^3) | DB: 6)
  * `expand_buffer` (Impact: 40.2 | O(N^6) | DB: 5)
  * `dump_omf` (Impact: 32.5 | O(N^3) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 76`, `args: 9`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 462`
* *Architecture:* `io: 4`, `api: 115`, `import: 3`
* *Defense:* `safety: 31`, `immutability_locks: 64`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ctype.h, bytesex.h, compiler.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/codeview.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.997 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.105 IQR)
- **Top Global Matches:** file_cluster_8: 12.997, file_cluster_13: 13.007, file_cluster_0: 13.255
- **Magnitude:** 877.84 | **LOC:** 799 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (85.2423%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write_symbolinfo_symbols` (Impact: 72.6 | O(N^4) | DB: 8)
  * `register_reloc` (Impact: 58.2 | O(N^4) | DB: 20)
  * `calc_md5` (Impact: 53.8 | O(N^5) | DB: 11)
  * `cv8_typevalue` (Impact: 41.0 | O(N^2) | DB: 9)
  * `cv8_deflabel` (Impact: 38.8 | O(N^2) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 122`, `args: 33`, `func_start: 24`, `class_start: 40`
* *Risk/State:* `state_mutation: 315`, `dead_code: 2`
* *Architecture:* `io: 2`, `api: 136`, `import: 11`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` nasm.h, hashtbl.h, version.h, outlib.h, pecoff.h, saa.h, md5.h, error.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `disasm/disasm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.95 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.261 IQR)
- **Top Global Matches:** file_cluster_8: 14.95, file_cluster_13: 14.96, file_cluster_11: 15.082
- **Magnitude:** 857.86 | **LOC:** 1801 | **CtrlFlow:** 89.9% | **Authorship Centralization:** 77.8%
- **Algorithmic:** O(N^5) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (85.3886%), Tech Debt (9.959%)
**Top Internal Functions/Classes:**
  * `eatbyte` (Impact: 165.8 | O(N^5) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 23`, `func_start: 1`
* *Risk/State:* `state_mutation: 634`, `orphaned_logic: 1`
* *Architecture:* `api: 48`, `import: 8`
* *Defense:* `safety: 31`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` regdis.h, insns.h, disp8.h, tables.h, compiler.h, disasm.h, bytesex.h, sync.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `disasm/prefix.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.331 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.026 IQR)
- **Top Global Matches:** file_cluster_8: 13.331, file_cluster_13: 13.604, file_cluster_7: 13.696
- **Magnitude:** 851.66 | **LOC:** 481 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (97.1059%), Tech Debt (10.8287%)
**Top Internal Functions/Classes:**
  * `parse_prefixes` (Impact: 332.5 | O(N^4) | DB: 45)
  * `parse_rex` (Impact: 60.2 | O(N^3) | DB: 57)
    * *Intent:* /* ------ Set value for all moptypes ------ */ /* case statements for original REX */
  * `xbits` (Impact: 5.0 | O(N^2) | DB: 1)
    * *Intent:* /* SPDX-License-Identifier: BSD-2-Clause */ /* Copyright 2025 The NASM Authors - All Rights Reserved...
  * `evex_vreg` (Impact: 3.4 | O(N^2) | DB: 2)
  * `parse_evex` (Impact: 3.3 | O(N^1) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 63`, `args: 3`, `func_start: 37`
* *Risk/State:* `state_mutation: 332`, `orphaned_logic: 1`
* *Architecture:* `api: 67`, `import: 2`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` nasmlib.h, disasm.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/error.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.735 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.631 IQR)
- **Top Global Matches:** file_cluster_8: 12.735, file_cluster_13: 12.739, file_cluster_7: 12.995
- **Magnitude:** 815.3 | **LOC:** 754 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (70.8177%), Tech Debt (38.6283%)
**Top Internal Functions/Classes:**
  * `die_hard` (Impact: 439.6 | O(2^N) | DB: 14)
  * `set_warning_status` (Impact: 99.8 | O(N^2) | DB: 21)
  * `is_suppressed` (Impact: 34.0 | O(N^3) | DB: 2)
  * `true_error_type` (Impact: 6.8 | O(N^3) | DB: 4)
  * `pop_warnings` (Impact: 4.8 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 66`, `args: 11`, `func_start: 15`, `class_start: 11`
* *Risk/State:* `state_mutation: 157`, `orphaned_logic: 5`
* *Architecture:* `api: 54`, `import: 6`
* *Defense:* `safety: 1`, `doc: 8`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` strlist.h, srcfile.h, error.h, compiler.h, nasmlib.h, listing.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `disasm/ndisasm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.017 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.049 IQR)
- **Top Global Matches:** file_cluster_13: 13.017, file_cluster_8: 13.105, file_cluster_11: 13.41
- **Magnitude:** 800.72 | **LOC:** 404 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (79.5424%), Tech Debt (12.4936%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 565.3 | O(N^6) | DB: 81)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 33`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 207`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 23`, `import: 10`
* *Defense:* `safety: 3`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` nasm.h, disasm.h, ver.h, insns.h, errno.h, error.h, compiler.h, nctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/strfunc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.606 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 4.965 IQR)
- **Top Global Matches:** file_cluster_8: 14.606, file_cluster_13: 14.697, file_cluster_11: 14.731
- **Magnitude:** 773.44 | **LOC:** 330 | **CtrlFlow:** 86.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (90.0467%), Tech Debt (33.6677%)
**Top Internal Functions/Classes:**
  * `utf8_to_16be` (Impact: 112.2 | O(N^6) | DB: 28)
  * `utf8_to_16le` (Impact: 111.8 | O(N^6) | DB: 27)
    * *Intent:* /* SPDX-License-Identifier: BSD-2-Clause */ /* Copyright 1996-2009 The NASM Authors - All Rights Res...
  * `utf8_to_32be` (Impact: 101.5 | O(N^6) | DB: 26)
  * `utf8_to_32le` (Impact: 101.0 | O(N^6) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 18`, `func_start: 4`
* *Risk/State:* `state_mutation: 318`, `orphaned_logic: 4`
* *Architecture:* `api: 24`, `import: 2`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` nasmlib.h, nasm.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/listing.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.733 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.626 IQR)
- **Top Global Matches:** file_cluster_13: 12.733, file_cluster_8: 12.752, file_cluster_0: 13.023
- **Magnitude:** 724.26 | **LOC:** 412 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (78.3796%), Tech Debt (11.5515%)
**Top Internal Functions/Classes:**
  * `list_output` (Impact: 165.5 | O(N^4) | DB: 14)
  * `list_update_options` (Impact: 105.3 | O(2^N) | DB: 10)
  * `list_emit` (Impact: 76.7 | O(N^6) | DB: 5)
  * `list_uplevel` (Impact: 29.8 | O(N^2) | DB: 4)
  * `list_downlevel` (Impact: 27.9 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 51`, `args: 9`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 192`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 44`, `import: 7`
* *Defense:* `safety: 1`, `immutability_locks: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` nasm.h, strlist.h, error.h, compiler.h, nctype.h, nasmlib.h, listing.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x86/preinsns.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.817 IQR)
- **Top Global Matches:** file_cluster_8: 13.817, file_cluster_0: 14.06, file_cluster_13: 14.126
- **Magnitude:** 621.3 | **LOC:** 669 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 47.1%
- **Algorithmic:** O(N) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (88.4853%), Tech Debt (37.9847%)
**Top Internal Functions/Classes:**
  * `adjust_instruction_flags` (Impact: 23.9 | O(N^1) | DB: 1)
  * `adjust_fl_zu` (Impact: 18.7 | O(N^1) | DB: 5)
  * `process_macro` (Impact: 13.0 | O(N^1) | DB: 7)
    * *Intent:* # # Actually invoke a macro #
  * `subst_list` (Impact: 7.2 | O(N^1) | DB: 2)
    * *Intent:* # # Build output by substituting the variables for each argument, #
  * `add_flag` (Impact: 5.5 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 138`, `args: 30`, `func_start: 11`
* *Risk/State:* `state_mutation: 529`, `fragile_debt: 6`
* *Architecture:* `io: 4`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 7`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` macro, strict, integer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/dwarf.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.401 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.175 IQR)
- **Top Global Matches:** file_cluster_8: 11.401, file_cluster_7: 12.038, file_cluster_13: 12.21
- **Magnitude:** 541.8 | **LOC:** 592 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 21`, `class_start: 21`
* *Risk/State:* `state_mutation: 495`
* *Architecture:* `api: 21`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.472
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.010753
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `macros/macros.pl` (PERL) | Magnitude: 418.18 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 132, structural_boundaries: 59, branch: 53, indent_tabs: 51
- `doc/ttfmetrics.ph` (PERL) | Magnitude: 70.7 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 47, state_mutation: 33, indent_spaces: 24, pointers: 23
- `doc/findfont.ph` (PERL) | Magnitude: 248.16 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 69, branch: 53, structural_boundaries: 42
- `tools/mkdep.pl` (PERL) | Magnitude: 0.33 | Delta: **0.165 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 300, branch: 149, structural_boundaries: 91, indent_tabs: 91
- `doc/pspdf.pl` (PERL) | Magnitude: 181.46 | Delta: **0.227 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 75, branch: 57, indent_spaces: 54, structural_boundaries: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `disasm/diserror.c` (C) | Magnitude: 17.96 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, api: 5, structural_boundaries: 4, state_mutation: 4
- `asm/listing.c` (C) | Magnitude: 724.26 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 238, state_mutation: 192, branch: 97, structural_boundaries: 51
- `output/outdbg.c` (C) | Magnitude: 39.7 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 17, state_mutation: 17, pointers: 14
- `tools/cleanfile` (PERL) | Magnitude: 0.2 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 174, branch: 52, indent_spaces: 45, indent_tabs: 38
- `asm/preproc.h` (C) | Magnitude: 20.2 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: immutability_locks: 6, api: 5, pointers: 5, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tools/syncfiles.pl` (PERL) | Magnitude: 0.11 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 100, indent_tabs: 31, branch: 27, indent_spaces: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `asm/error.c` (C) | Magnitude: 815.3 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 157, indent_spaces: 131, branch: 82, indent_tabs: 75
- `doc/rdsrc.pl` (PERL) | Magnitude: 2580.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 1414, indent_spaces: 648, branch: 427, structural_boundaries: 164
- `output/codeview.c` (C) | Magnitude: 877.84 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 493, state_mutation: 315, pointers: 199, api: 136
- `disasm/disasm.c` (C) | Magnitude: 857.86 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 634, indent_spaces: 483, branch: 205, pointers: 124
- `asm/quote.c` (C) | Magnitude: 1506.32 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 540, branch: 173, indent_spaces: 159, indent_tabs: 101

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `templates/template.mk` (MAKEFILE) | Magnitude: 10.52 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1
- `include/saa.h` (C) | Magnitude: 48.76 | Delta: **0.229 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 41, api: 33, pointers: 29, safety: 20

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `asm/preproc.c` -> Churn: **100.0%** | Cog Load: 96.3415% | Debt: 19.2531%
- `asm/nasm.c` -> Churn: **81.0%** | Cog Load: 78.7416% | Debt: 22.6278%
- `x86/insns.pl` -> Churn: **79.85%** | Cog Load: 97.9411% | Debt: 9.1293%
- `asm/assemble.c` -> Churn: **69.07%** | Cog Load: 98.8357% | Debt: 13.3941%
- `x86/preinsns.pl` -> Churn: **54.67%** | Cog Load: 88.4853% | Debt: 37.9847%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `doc/rdsrc.pl` -> **H. Peter Anvin** (100.0% isolated ownership) | Magnitude: 2580.2
- `doc/genps.pl` -> **H. Peter Anvin** (100.0% isolated ownership) | Magnitude: 1653.14
- `output/outas86.c` -> **H. Peter Anvin** (100.0% isolated ownership) | Magnitude: 1310.26
- `output/outbin.c` -> **H. Peter Anvin** (100.0% isolated ownership) | Magnitude: 1187.58
- `misc/omfdump.c` -> **H. Peter Anvin** (100.0% isolated ownership) | Magnitude: 1078.76

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `include/nasm.h` -> **Severity: 0.594** (Bridge: 0.0114 * Flux: 52.1702%)
- `include/iflag.h` -> **Severity: 0.065** (Bridge: 0.0008 * Flux: 83.2506%)
- `asm/listing.h` -> **Severity: 0.02** (Bridge: 0.0002 * Flux: 98.7711%)
- `include/disp8.h` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 99.8051%)
- `output/elf.h` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 98.1603%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `include/nctype.h` -> **Severity: 4.783** (Embedded: 0.1374 * Error Risk: 34.7985%)
- `x86/x86const.h` -> **Severity: 2.172** (Embedded: 0.1051 * Error Risk: 20.6717%)
- `asm/srcfile.h` -> **Severity: 2.086** (Embedded: 0.1156 * Error Risk: 18.0454%)
- `include/nasm.h` -> **Severity: 1.619** (Embedded: 0.1912 * Error Risk: 8.4719%)
- `include/compiler.h` -> **Severity: 1.212** (Embedded: 0.3122 * Error Risk: 3.8812%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `include/nasm.h` -> **Severity: 3946.406** (Blast Radius: 46.475 * Doc Risk: 84.9146%)
- `include/nasmint.h` -> **Severity: 2371.238** (Blast Radius: 26.689 * Doc Risk: 88.847%)
- `include/compiler.h` -> **Severity: 2104.628** (Blast Radius: 138.749 * Doc Risk: 15.1686%)
- `include/error.h` -> **Severity: 1767.2** (Blast Radius: 17.672 * Doc Risk: 100.0%)
- `include/iflag.h` -> **Severity: 1061.68** (Blast Radius: 10.657 * Doc Risk: 99.6228%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
