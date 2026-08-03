# ARCHITECTURAL_BRIEF: raspberrypi
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/raspberrypi` |
| **Timestamp** | `2026-08-03T19:27:38.935403+00:00` |
| **Scan Duration** | `1.84s` |
| **Git Branch** | `master` |
| **Git Commit** | `cbb3a102d83dfeb4586e503749111d1bfbf8fc88` |
| **Git Remote** | `https://github.com/dwelch67/raspberrypi.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 323 malicious artifacts.

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
| Total Artifacts | 930 |
| Analyzed Artifacts (Scanned) | 560 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 370 |
| Total LOC | 33941 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 60.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6105 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0189 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7583 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 212 | 25575 | 37.9% |
| MARKDOWN | 115 | 0 | 20.5% |
| ASSEMBLY | 115 | 4982 | 20.5% |
| MAKEFILE | 97 | 3370 | 17.3% |
| BINARY_THREAT | 14 | 14 | 2.5% |
| PLAINTEXT | 7 | 0 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.674`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 376 | 67.1% |
| file_cluster_9 | 34 | 6.1% |
| Unknown | 14 | 2.5% |
| file_cluster_13 | 10 | 1.8% |
| file_cluster_0 | 2 | 0.4% |
| file_cluster_11 | 2 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 122 | 21.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 370*

**Composition by Extension & Reason:**
- `no_extension`: 105x Unsupported Format (.undeterminable), 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2756 LOC)
- `.o`: 58x Excluded (Explicitly Denied Extension: '.o')
- `.h`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Embedded Hex Payload: 4352 hex tokens in 2822 LOC), 2x Excluded (Embedded Hex Payload: 4402 hex tokens in 2906 LOC)
- `.c`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 307 LOC)
- `.elf`: 28x Excluded (Unsupported Extension: '.elf')
- `.list`: 28x Excluded (Unsupported Extension: '.list')
- `.hex`: 25x Excluded (Unsupported Extension: '.hex'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 20x Excluded (Unsupported Extension: '.cfg')
- `.img`: 15x Excluded (Unsupported Extension: '.img')
- `.s`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 1048579 LOC exceeds safe regex boundaries)
- `.ps`: 6x Excluded (Unsupported Extension: '.ps')
- `.bc`: 2x Excluded (Unsupported Extension: '.bc')
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.a`: 1x Excluded (Explicitly Denied Extension: '.a')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 95.1 | 32.2 | 22.5 | 37.8 |
| Error & Exception Exposure | 0.0 | 99.2 | 17.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 26.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 23.8 | 2.8 | 80.0 |
| API Exposure | 0.0 | 16.2 | 8.5 | 8.7 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 39.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 53.7 | 2.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 92.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 86.0 | 96.6 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 36.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 3.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tas/tas.c` (Hits: 13)
- `jtagproxy/msplaunchpad/parport.c` (Hits: 8)
- `twain/trees.c` (Hits: 7)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **zutil.h** (`twain/zutil.h`) — 6 inbound connections
2. **deflate.h** (`twain/deflate.h`) — 2 inbound connections
3. **inffast.h** (`twain/inffast.h`) — 2 inbound connections
4. **inflate.h** (`twain/inflate.h`) — 2 inbound connections
5. **inftrees.h** (`twain/inftrees.h`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **parport.c** (`jtagproxy/ft232rl/parport.c`) — 12 outbound dependencies
2. **parport_fast.c** (`jtagproxy/ft232rl/parport_fast.c`) — 12 outbound dependencies
3. **parport.c** (`jtagproxy/msplaunchpad/parport.c`) — 11 outbound dependencies
4. **syscalls.c** (`newlib0/syscalls.c`) — 10 outbound dependencies
5. **ser.c** (`bootloader01/ser.c`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `assemble` (@ `tas/tas.c`) -> Impact: **9613.6** | LOC: 1513
  * *Intent:* //-------------------------------------------------------------------
- `notmain` (@ `uart02/uart02.clang.opt.s`) -> Impact: **493.1** | LOC: 160
- `notmain` (@ `boards/pi2/bootloader07/bootloader07.c`) -> Impact: **479.2** | LOC: 192
  * *Intent:* //------------------------------------------------------------------------
- `notmain` (@ `boards/pi3/aarch32/bootloader07/bootloader07.c`) -> Impact: **479.2** | LOC: 192
  * *Intent:* //------------------------------------------------------------------------
- `notmain` (@ `boards/pi1/bootloader07/bootloader07.c`) -> Impact: **470.8** | LOC: 181
  * *Intent:* //------------------------------------------------------------------------
- `notmain` (@ `boards/piaplus/bootloader07/bootloader07.c`) -> Impact: **470.8** | LOC: 182
  * *Intent:* //------------------------------------------------------------------------
- `notmain` (@ `boards/pizero/bootloader07/bootloader07.c`) -> Impact: **470.8** | LOC: 182
  * *Intent:* //------------------------------------------------------------------------
- `notmain` (@ `bootloader07/bootloader07.c`) -> Impact: **470.8** | LOC: 181
  * *Intent:* //------------------------------------------------------------------------
- `notmain` (@ `boards/pi3/aarch64/bootloader07/bootloader07.c`) -> Impact: **470.7** | LOC: 180
  * *Intent:* //------------------------------------------------------------------------
- `main` (@ `bootloader07/ihex.c`) -> Impact: **470.1** | LOC: 167

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `assemble` (@ `tas/tas.c`) -> **O(2^N) [Recursive]**
  * *Intent:* //-------------------------------------------------------------------
- `notmain` (@ `uart02/uart02.clang.opt.s`) -> **O(2^N) [Recursive]**
- `hexstrings` (@ `uart02/uart02.clang.opt.s`) -> **O(2^N) [Recursive]**
- `hexstring` (@ `uart02/uart02.clang.opt.s`) -> **O(2^N) [Recursive]**
- `uart_putc` (@ `uart02/uart02.clang.opt.s`) -> **O(2^N) [Recursive]**
- `makefixed` (@ `twain/inflate.c`) -> **O(2^N) [Recursive]**
- `tr_static_init` (@ `twain/trees.c`) -> **O(2^N) [Recursive]**
- `zcfree` (@ `twain/zutil.c`) -> **O(2^N) [Recursive]**
- `uart_putc` (@ `newlib0/uart02.c`) -> **O(2^N) [Recursive]**
  * *Intent:* #define AUX_MU_LSR_REG 0x20215054 #define AUX_MU_MSR_REG 0x20215058 #define AUX_MU_SCRATCH 0x2021505C #define AUX_MU_CNTL_REG 0x20215060 #define AUX_M...
- `ser_open` (@ `bootloader01/ser.c`) -> **O(2^N) [Recursive]**
  * *Intent:* //-----------------------------------------------------------------------------

### Highest Data Gravity (Database Complexity)
- `assemble` (@ `tas/tas.c`) -> DB Complexity: **592**
  * *Intent:* //-------------------------------------------------------------------
- `dissassemble` (@ `tas/tas.c`) -> DB Complexity: **177**
  * *Intent:* //-------------------------------------------------------------------
- `main` (@ `tas/tas.c`) -> DB Complexity: **92**
  * *Intent:* //-------------------------------------------------------------------
- `do_it` (@ `boards/pizero/asmdelay/asmdelay.c`) -> DB Complexity: **69**
- `notmain` (@ `boards/pi2/bootloader07/bootloader07.c`) -> DB Complexity: **56**
  * *Intent:* //------------------------------------------------------------------------
- `notmain` (@ `boards/pi3/aarch32/bootloader07/bootloader07.c`) -> DB Complexity: **56**
  * *Intent:* //------------------------------------------------------------------------
- `notmain` (@ `spi03/spi03.c`) -> DB Complexity: **55**
  * *Intent:* //------------------------------------------------------------------------
- `deflate` (@ `twain/deflate.c`) -> DB Complexity: **54**
- `tr_static_init` (@ `twain/trees.c`) -> DB Complexity: **50**
- `notmain` (@ `boards/pi1/bootloader07/bootloader07.c`) -> DB Complexity: **48**
  * *Intent:* //------------------------------------------------------------------------

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tas` | 8 | 13771.58 | 30.67% | 24.43% |
| `twain` | 25 | 6298.72 | 41.43% | 24.76% |
| `uart02` | 7 | 2219.42 | 17.18% | 4.63% |
| `bootloader07` | 11 | 1656.68 | 38.93% | 23.84% |
| `zero_start` | 8 | 1348.16 | 19.86% | 11.97% |
| `bootloader01` | 9 | 1340.6 | 38.95% | 22.2% |
| `bootloader06` | 8 | 1274.8 | 33.54% | 23.43% |
| `bootloader05` | 8 | 1135.84 | 33.41% | 23.98% |
| `boards/pizero/float02` | 7 | 1125.22 | 31.83% | 18.36% |
| `float02` | 7 | 1125.06 | 31.88% | 18.49% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `blinker06/wdog.c` -> **99.9896%** Exposure
- `boards/pi1/blinker06/wdog.c` -> **99.9896%** Exposure
- `boards/pi2/HYP/blinker06/wdog.c` -> **99.9896%** Exposure
- `boards/piaplus/blinker06/wdog.c` -> **99.9896%** Exposure
- `boards/pizero/blinker06/wdog.c` -> **99.9896%** Exposure
### Highest State Flux (Mutation/Volatility)
- `armjtag/armjtag.c` -> **100.0%** Exposure
- `armjtag/fastblink.c` -> **100.0%** Exposure
- `armjtag/rpi2/armjtag.c` -> **100.0%** Exposure
- `bench02/uart.c` -> **100.0%** Exposure
- `blinker01/blinker01.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `boards/pi2/SVC_BOOT/uart01/periph.c` -> **9** Orphaned Functions | **0** Duplicates
- `boards/pi2/SVC_BOOT/uart02/periph.c` -> **9** Orphaned Functions | **0** Duplicates
- `boards/pi2/bootloader07/periph.c` -> **9** Orphaned Functions | **0** Duplicates
- `boards/pi3/aarch32/bootloader07/periph.c` -> **9** Orphaned Functions | **0** Duplicates
- `boards/piaplus/bootloader07/periph.c` -> **9** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`bootloader07/ihex.c`** -> AI Confidence: **99.32%**
2. **`jtagproxy/ft232rl/parport.c`** -> AI Confidence: **99.31%**
3. **`jtagproxy/ft232rl/parport_fast.c`** -> AI Confidence: **99.31%**
4. **`jtagproxy/msplaunchpad/parport.c`** -> AI Confidence: **99.31%**
5. **`blinker07/blinker07.c`** -> AI Confidence: **99.29%**
6. **`blinker08/blinker08.c`** -> AI Confidence: **99.29%**
7. **`boards/piaplus/float02/float02.c`** -> AI Confidence: **99.29%**
8. **`boards/pizero/float02/float02.c`** -> AI Confidence: **99.29%**
9. **`float02/float02.c`** -> AI Confidence: **99.29%**
10. **`gps_clock/notmain.c`** -> AI Confidence: **99.29%**
11. **`spi03/spi03.c`** -> AI Confidence: **99.29%**
12. **`twain/adler32.c`** -> AI Confidence: **99.29%**
13. **`twain/deflate.c`** -> AI Confidence: **99.29%**
14. **`twain/gzguts.h`** -> AI Confidence: **99.29%**
15. **`twain/inffast.c`** -> AI Confidence: **99.29%**
16. **`twain/zconf.h`** -> AI Confidence: **99.29%**
17. **`twain/zutil.c`** -> AI Confidence: **99.29%**
18. **`spi01/dumphex.c`** -> AI Confidence: **99.2%**
19. **`twain/crc32.c`** -> AI Confidence: **99.2%**
20. **`twain/trees.c`** -> AI Confidence: **99.2%**
21. **`boards/pi1/bootloader07/bootloader07.c`** -> AI Confidence: **99.17%**
22. **`boards/pi3/aarch64/bootloader07/bootloader07.c`** -> AI Confidence: **99.17%**
23. **`boards/piaplus/float02/slowfloat.c`** -> AI Confidence: **99.17%**
24. **`boards/pizero/float02/slowfloat.c`** -> AI Confidence: **99.17%**
25. **`bootloader01/bootloader01.c`** -> AI Confidence: **99.17%**
26. **`bootloader02/bootloader02.c`** -> AI Confidence: **99.17%**
27. **`bootloader07/bootloader07.c`** -> AI Confidence: **99.17%**
28. **`tas/hexstring.c`** -> AI Confidence: **99.17%**
29. **`bootloader01/ser.c`** -> AI Confidence: **99.15%**
30. **`twain/inflate.c`** -> AI Confidence: **99.13%**
31. **`armjtag/armjtag.c`** -> AI Confidence: **99.11%**
32. **`armjtag/rpi2/armjtag.c`** -> AI Confidence: **99.11%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `armjtag/armjtag.c` -> **20.0%** Exposure
- `armjtag/fastblink.c` -> **20.0%** Exposure
- `armjtag/rpi2/armjtag.c` -> **20.0%** Exposure
- `atags/atags.c` -> **20.0%** Exposure
- `blinker02/blinker02.c` -> **20.0%** Exposure
### Raw Memory Manipulation
- `twain/deflate.c` -> **10.0%** Exposure
- `twain/trees.c` -> **10.0%** Exposure
- `jtagproxy/ft232rl/parport.c` -> **0.0183%** Exposure
- `jtagproxy/ft232rl/parport_fast.c` -> **0.0086%** Exposure
- `jtagproxy/msplaunchpad/parport.c` -> **0.0029%** Exposure
### Algorithmic DoS Exposure
- `armjtag/armjtag.c` -> **100.0%** Exposure
- `armjtag/fastblink.c` -> **100.0%** Exposure
- `armjtag/rpi2/armjtag.c` -> **100.0%** Exposure
- `atags/atags.c` -> **100.0%** Exposure
- `blinker01/blinker01.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `87` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `128` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `twain/zutil.c` (C) -> Cumulative Risk: **793.31**
- **Archetype:** `file_cluster_13` (Distance: 14.288 IQR)
- **Magnitude:** 263.92 | **LOC:** 325 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.923%)
- **Heaviest Functions:** `zlibCompileFlags` (Impact: 44.1), `zcfree` (Impact: 25.1), `zcalloc` (Impact: 10.9)

### 2. `twain/inflate.c` (C) -> Cumulative Risk: **756.73**
- **Archetype:** `file_cluster_11` (Distance: 14.401 IQR)
- **Magnitude:** 717.0 | **LOC:** 1497 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (90.4651%)
- **Heaviest Functions:** `inflateCopy` (Impact: 54.3), `makefixed` (Impact: 45.9), `inflateInit2_` (Impact: 40.2)

### 3. `boards/piaplus/float02/float02.c` (C) -> Cumulative Risk: **727.88**
- **Archetype:** `file_cluster_9` (Distance: 17.61 IQR)
- **Magnitude:** 191.8 | **LOC:** 143 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (91.0487%)
- **Heaviest Functions:** `notmain` (Impact: 95.2)

### 4. `float02/float02.c` (C) -> Cumulative Risk: **723.52**
- **Archetype:** `file_cluster_9` (Distance: 17.333 IQR)
- **Magnitude:** 193.1 | **LOC:** 149 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (88.7583%)
- **Heaviest Functions:** `notmain` (Impact: 95.4)

### 5. `twain/deflate.c` (C) -> Cumulative Risk: **722.17**
- **Archetype:** `file_cluster_8` (Distance: 14.043 IQR)
- **Magnitude:** 1934.4 | **LOC:** 1966 | **CtrlFlow:** 82.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.5302%)
- **Heaviest Functions:** `deflate` (Impact: 349.0), `deflate_slow` (Impact: 117.0), `deflate_rle` (Impact: 101.2)

### 6. `bootloader01/prograspi.c` (C) -> Cumulative Risk: **721.21**
- **Archetype:** `file_cluster_9` (Distance: 16.568 IQR)
- **Magnitude:** 541.46 | **LOC:** 331 | **CtrlFlow:** 70.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (99.2412%)
- **Heaviest Functions:** `readhex` (Impact: 108.3), `raspload` (Impact: 27.2), `main` (Impact: 21.5)

### 7. `boards/pizero/float02/float02.c` (C) -> Cumulative Risk: **719.57**
- **Archetype:** `file_cluster_9` (Distance: 17.22 IQR)
- **Magnitude:** 193.24 | **LOC:** 151 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (87.7782%)
- **Heaviest Functions:** `notmain` (Impact: 95.5)

### 8. `twain/trees.c` (C) -> Cumulative Risk: **715.43**
- **Archetype:** `file_cluster_8` (Distance: 14.48 IQR)
- **Magnitude:** 1282.6 | **LOC:** 1225 | **CtrlFlow:** 77.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9756%)
- **Heaviest Functions:** `tr_static_init` (Impact: 67.8), `send_tree` (Impact: 57.3), `gen_bitlen` (Impact: 46.0)

### 9. `twain/twain.c` (C) -> Cumulative Risk: **708.63**
- **Archetype:** `file_cluster_8` (Distance: 12.628 IQR)
- **Magnitude:** 276.06 | **LOC:** 262 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.8617%)
- **Heaviest Functions:** `notmain` (Impact: 81.4), `add_one` (Impact: 12.3), `next_coarse_offset` (Impact: 5.7)

### 10. `twain/crc32.c` (C) -> Cumulative Risk: **698.83**
- **Archetype:** `file_cluster_13` (Distance: 14.555 IQR)
- **Magnitude:** 503.0 | **LOC:** 426 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9953%)
- **Heaviest Functions:** `make_crc_table` (Impact: 59.9), `crc32` (Impact: 36.3), `crc32_combine_` (Impact: 20.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tas/tas.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.492 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.601 IQR)
- **Top Global Matches:** file_cluster_8: 14.492, file_cluster_13: 14.835, file_cluster_7: 14.855
- **Magnitude:** 13649.12 | **LOC:** 2936 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 592
- **Risk Profile:** Cognitive Load (95.0593%), Tech Debt (8.3006%)
**Top Internal Functions/Classes:**
  * `assemble` (Impact: 9613.6 | O(2^N) | DB: 592)
    * *Intent:* //-------------------------------------------------------------------
  * `dissassemble` (Impact: 372.4 | O(N^4) | DB: 177)
    * *Intent:* //-------------------------------------------------------------------
  * `main` (Impact: 310.9 | O(N^6) | DB: 92)
    * *Intent:* //-------------------------------------------------------------------
  * `parse_immed` (Impact: 194.6 | O(N^4) | DB: 15)
    * *Intent:* //-------------------------------------------------------------------
  * `parse_low_reg` (Impact: 80.8 | O(N^2) | DB: 7)
    * *Intent:* //-------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 825`, `structural_boundaries: 397`, `args: 12`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 2710`, `orphaned_logic: 2`
* *Architecture:* `io: 13`, `api: 69`, `import: 3`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdlib.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `twain/deflate.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.043 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.955 IQR)
- **Top Global Matches:** file_cluster_8: 14.043, file_cluster_11: 14.264, file_cluster_0: 14.275
- **Magnitude:** 1934.4 | **LOC:** 1966 | **CtrlFlow:** 82.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (80.9291%), Tech Debt (27.3237%)
**Top Internal Functions/Classes:**
  * `deflate` (Impact: 349.0 | O(N^6) | DB: 54)
  * `deflate_slow` (Impact: 117.0 | O(N^6) | DB: 21)
    * *Intent:* /* =========================================================================== * Read a new buffer f...
  * `deflate_rle` (Impact: 101.2 | O(N^6) | DB: 23)
  * `deflate_fast` (Impact: 80.9 | O(N^6) | DB: 13)
  * `deflateInit2_` (Impact: 80.3 | O(N^4) | DB: 38)
    * *Intent:* /* good lazy nice chain */ /* 0 */ {0, 0, 0, 0, deflate_stored}, /* store only */ /* 1 */ {4, 4, 8, ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 337`, `structural_boundaries: 73`, `func_start: 19`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 798`, `dead_code: 4`, `fragile_debt: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 190`, `import: 1`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deflate.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `twain/trees.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.48 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.067 IQR)
- **Top Global Matches:** file_cluster_8: 14.48, file_cluster_13: 14.661, file_cluster_11: 14.714
- **Magnitude:** 1282.6 | **LOC:** 1225 | **CtrlFlow:** 77.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (75.5223%), Tech Debt (17.0324%)
**Top Internal Functions/Classes:**
  * `tr_static_init` (Impact: 67.8 | O(2^N) | DB: 50)
  * `send_tree` (Impact: 57.3 | O(N^4) | DB: 22)
    * *Intent:* /* =========================================================================== * Construct one Huffm...
  * `gen_bitlen` (Impact: 46.0 | O(N^4) | DB: 38)
  * `build_tree` (Impact: 45.5 | O(N^6) | DB: 38)
    * *Intent:* int h; /* heap index */ int n, m; /* iterate over the tree elements */ int bits; /* bit length */ in...
  * `scan_tree` (Impact: 38.0 | O(N^3) | DB: 26)
    * *Intent:* /* =========================================================================== * Generate the codes ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 38`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 748`, `orphaned_logic: 5`
* *Architecture:* `io: 7`, `api: 150`, `import: 3`
* *Defense:* `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` deflate.h, stdio.h, trees.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `uart02/uart02.clang.opt.s` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.38 IQR)
- **Top Global Matches:** file_cluster_8: 8.38, file_cluster_7: 9.286, file_cluster_1: 9.466
- **Magnitude:** 1039.92 | **LOC:** 387 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (12.8014%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `notmain` (Impact: 493.1 | O(2^N) | DB: 3)
  * `hexstrings` (Impact: 373.6 | O(2^N))
  * `hexstring` (Impact: 110.8 | O(2^N))
  * `uart_putc` (Impact: 50.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 106`, `args: 276`, `func_start: 4`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gps_clock/notmain.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.196 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.11 IQR)
- **Top Global Matches:** file_cluster_0: 15.196, file_cluster_9: 15.204, file_cluster_11: 15.215
- **Magnitude:** 854.88 | **LOC:** 494 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (69.2426%), Tech Debt (11.2027%)
**Top Internal Functions/Classes:**
  * `do_nmea` (Impact: 351.8 | O(N^6) | DB: 45)
    * *Intent:* //------------------------------------------------------------------------
  * `show_time` (Impact: 63.4 | O(N^4) | DB: 16)
    * *Intent:* //rc=0; //for(ra=0;ra<11;ra++) //{ //if(s[ra]==0) break; //for(rb=0;rb<8;rb++) //{ //rd=s[ra]; //spi...
  * `spi_one_byte` (Impact: 28.4 | O(N^2))
    * *Intent:* //------------------------------------------------------------------------
  * `hexstrings` (Impact: 24.7 | O(N^2) | DB: 5)
    * *Intent:* //------------------------------------------------------------------------
  * `notmain` (Impact: 18.7 | O(N^2) | DB: 12)
    * *Intent:* //------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 20`, `args: 15`, `func_start: 12`
* *Risk/State:* `state_mutation: 266`, `dead_code: 8`, `orphaned_logic: 1`
* *Architecture:* `api: 44`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fontdata.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/piaplus/float02/slowfloat.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.421 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.122 IQR)
- **Top Global Matches:** file_cluster_8: 13.421, file_cluster_11: 13.508, file_cluster_0: 13.555
- **Magnitude:** 729.72 | **LOC:** 665 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (82.558%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `floatXToFloat32` (Impact: 86.5 | O(N^4) | DB: 26)
  * `floatXAdd` (Impact: 76.0 | O(N^4) | DB: 21)
  * `roundFloatXTo24` (Impact: 56.6 | O(N^4) | DB: 6)
  * `roundFloatXTo53` (Impact: 45.7 | O(N^3) | DB: 8)
  * `floatXToInt32` (Impact: 29.9 | O(N^3) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 54`, `args: 1`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `state_mutation: 294`, `dead_code: 6`
* *Architecture:* `api: 84`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pizero/float02/slowfloat.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.421 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.122 IQR)
- **Top Global Matches:** file_cluster_8: 13.421, file_cluster_11: 13.508, file_cluster_0: 13.555
- **Magnitude:** 729.72 | **LOC:** 665 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (82.558%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `floatXToFloat32` (Impact: 86.5 | O(N^4) | DB: 26)
  * `floatXAdd` (Impact: 76.0 | O(N^4) | DB: 21)
  * `roundFloatXTo24` (Impact: 56.6 | O(N^4) | DB: 6)
  * `roundFloatXTo53` (Impact: 45.7 | O(N^3) | DB: 8)
  * `floatXToInt32` (Impact: 29.9 | O(N^3) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 54`, `args: 1`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `state_mutation: 294`, `dead_code: 6`
* *Architecture:* `api: 84`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `float02/slowfloat.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.1%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.421 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.122 IQR)
- **Top Global Matches:** file_cluster_8: 13.421, file_cluster_11: 13.508, file_cluster_0: 13.555
- **Magnitude:** 729.72 | **LOC:** 665 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (82.558%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `floatXToFloat32` (Impact: 86.5 | O(N^4) | DB: 26)
  * `floatXAdd` (Impact: 76.0 | O(N^4) | DB: 21)
  * `roundFloatXTo24` (Impact: 56.6 | O(N^4) | DB: 6)
  * `roundFloatXTo53` (Impact: 45.7 | O(N^3) | DB: 8)
  * `floatXToInt32` (Impact: 29.9 | O(N^3) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 54`, `args: 1`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `state_mutation: 294`, `dead_code: 6`
* *Architecture:* `api: 84`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `twain/inflate.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.401 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.941 IQR)
- **Top Global Matches:** file_cluster_11: 14.401, file_cluster_8: 14.422, file_cluster_13: 14.426
- **Magnitude:** 717.0 | **LOC:** 1497 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (84.4912%), Tech Debt (80.6679%)
**Top Internal Functions/Classes:**
  * `inflateCopy` (Impact: 54.3 | O(N^4) | DB: 10)
    * *Intent:* #else
  * `makefixed` (Impact: 45.9 | O(2^N) | DB: 9)
  * `inflateInit2_` (Impact: 40.2 | O(N^3) | DB: 8)
  * `inflateReset2` (Impact: 23.9 | O(N^3) | DB: 8)
    * *Intent:* * - Make op and len in inflate_fast() unsigned for consistency * - Add FAR to lcode and dcode declar...
  * `inflateSync` (Impact: 18.1 | O(N^3) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 73`, `args: 5`, `func_start: 13`, `class_start: 12`
* *Risk/State:* `state_mutation: 381`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 86`, `import: 4`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` inffixed.h, inffast.h, inflate.h, zutil.h, inftrees.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pi2/bootloader07/bootloader07.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.787 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.787 IQR)
- **Top Global Matches:** file_cluster_8: 12.787, file_cluster_13: 13.207, file_cluster_7: 13.224
- **Magnitude:** 678.4 | **LOC:** 245 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (76.1679%), Tech Debt (14.3599%)
**Top Internal Functions/Classes:**
  * `notmain` (Impact: 479.2 | O(N^6) | DB: 56)
    * *Intent:* //------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 28`, `args: 23`, `func_start: 1`
* *Risk/State:* `state_mutation: 164`, `orphaned_logic: 1`
* *Architecture:* `api: 31`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pi3/aarch32/bootloader07/bootloader07.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.787 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.787 IQR)
- **Top Global Matches:** file_cluster_8: 12.787, file_cluster_13: 13.207, file_cluster_7: 13.224
- **Magnitude:** 678.4 | **LOC:** 245 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (76.1679%), Tech Debt (14.3599%)
**Top Internal Functions/Classes:**
  * `notmain` (Impact: 479.2 | O(N^6) | DB: 56)
    * *Intent:* //------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 28`, `args: 23`, `func_start: 1`
* *Risk/State:* `state_mutation: 164`, `orphaned_logic: 1`
* *Architecture:* `api: 31`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spi03/spi03.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.47 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.751 IQR)
- **Top Global Matches:** file_cluster_8: 13.47, file_cluster_13: 13.721, file_cluster_0: 13.777
- **Magnitude:** 677.52 | **LOC:** 394 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 55
- **Risk Profile:** Cognitive Load (90.0868%), Tech Debt (11.9029%)
**Top Internal Functions/Classes:**
  * `notmain` (Impact: 275.4 | O(N^5) | DB: 55)
    * *Intent:* //------------------------------------------------------------------------
  * `spi_one_byte` (Impact: 28.4 | O(N^2))
    * *Intent:* //------------------------------------------------------------------------
  * `hexstrings` (Impact: 24.7 | O(N^2) | DB: 5)
    * *Intent:* //------------------------------------------------------------------------
  * `show_string` (Impact: 21.9 | O(N^3) | DB: 9)
    * *Intent:* //------------------------------------------------------------------------
  * `uart_putc` (Impact: 16.3 | O(N^2))
    * *Intent:* //------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 15`, `args: 13`, `func_start: 10`
* *Risk/State:* `state_mutation: 251`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 33`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fontdata.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/piaplus/bootloader07/bootloader07.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.621 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.797 IQR)
- **Top Global Matches:** file_cluster_8: 12.621, file_cluster_13: 13.056, file_cluster_7: 13.067
- **Magnitude:** 645.78 | **LOC:** 233 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (76.9596%), Tech Debt (14.8523%)
**Top Internal Functions/Classes:**
  * `notmain` (Impact: 470.8 | O(N^6) | DB: 48)
    * *Intent:* //------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 26`, `args: 21`, `func_start: 1`
* *Risk/State:* `state_mutation: 142`, `orphaned_logic: 1`
* *Architecture:* `api: 29`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pizero/bootloader07/bootloader07.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.621 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.797 IQR)
- **Top Global Matches:** file_cluster_8: 12.621, file_cluster_13: 13.056, file_cluster_7: 13.067
- **Magnitude:** 645.78 | **LOC:** 233 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (76.9596%), Tech Debt (14.8523%)
**Top Internal Functions/Classes:**
  * `notmain` (Impact: 470.8 | O(N^6) | DB: 48)
    * *Intent:* //------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 26`, `args: 21`, `func_start: 1`
* *Risk/State:* `state_mutation: 142`, `orphaned_logic: 1`
* *Architecture:* `api: 29`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pi1/bootloader07/bootloader07.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.634 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.791 IQR)
- **Top Global Matches:** file_cluster_8: 12.634, file_cluster_13: 13.07, file_cluster_7: 13.08
- **Magnitude:** 644.74 | **LOC:** 230 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (77.176%), Tech Debt (14.9494%)
**Top Internal Functions/Classes:**
  * `notmain` (Impact: 470.8 | O(N^6) | DB: 48)
    * *Intent:* //------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 24`, `args: 20`, `func_start: 1`
* *Risk/State:* `state_mutation: 142`, `orphaned_logic: 1`
* *Architecture:* `api: 28`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bootloader07/bootloader07.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.634 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.791 IQR)
- **Top Global Matches:** file_cluster_8: 12.634, file_cluster_13: 13.07, file_cluster_7: 13.08
- **Magnitude:** 644.74 | **LOC:** 230 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (77.176%), Tech Debt (14.9494%)
**Top Internal Functions/Classes:**
  * `notmain` (Impact: 470.8 | O(N^6) | DB: 48)
    * *Intent:* //------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 24`, `args: 20`, `func_start: 1`
* *Risk/State:* `state_mutation: 142`, `orphaned_logic: 1`
* *Architecture:* `api: 28`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pi3/aarch64/bootloader07/bootloader07.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.634 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.776 IQR)
- **Top Global Matches:** file_cluster_8: 12.634, file_cluster_13: 13.072, file_cluster_7: 13.08
- **Magnitude:** 642.6 | **LOC:** 227 | **CtrlFlow:** 72.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (77.3953%), Tech Debt (15.0489%)
**Top Internal Functions/Classes:**
  * `notmain` (Impact: 470.7 | O(N^6) | DB: 48)
    * *Intent:* //------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 22`, `args: 18`, `func_start: 1`
* *Risk/State:* `state_mutation: 142`, `orphaned_logic: 1`
* *Architecture:* `api: 26`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bootloader07/ihex.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.597 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.842 IQR)
- **Top Global Matches:** file_cluster_8: 12.597, file_cluster_13: 12.754, file_cluster_0: 13.042
- **Magnitude:** 625.5 | **LOC:** 209 | **CtrlFlow:** 90.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (79.5036%), Tech Debt (15.8869%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 470.1 | O(N^6) | DB: 46)
  * `get_one` (Impact: 4.9 | O(N^1) | DB: 4)
  * `PUT32` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 6`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 130`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 15`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdlib.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bootloader01/prograspi.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_9` (Drift: 16.568 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.792 IQR)
- **Top Global Matches:** file_cluster_9: 16.568, file_cluster_11: 16.62, file_cluster_13: 16.629
- **Magnitude:** 541.46 | **LOC:** 331 | **CtrlFlow:** 70.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (69.8718%), Tech Debt (13.5144%)
**Top Internal Functions/Classes:**
  * `readhex` (Impact: 108.3 | O(N^6) | DB: 37)
    * *Intent:* //-----------------------------------------------------------------------------
  * `raspload` (Impact: 27.2 | O(N^3) | DB: 44)
    * *Intent:* //-----------------------------------------------------------------------------
  * `main` (Impact: 21.5 | O(N^2) | DB: 45)
    * *Intent:* //-----------------------------------------------------------------------------
  * `check_packet` (Impact: 18.8 | O(N^1) | DB: 7)
    * *Intent:* //-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 20`, `args: 3`, `func_start: 4`
* *Risk/State:* `state_mutation: 328`, `dead_code: 8`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 33`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdlib.h, stdio.h, ser.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bootloader01/bootloader01.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.792 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.812 IQR)
- **Top Global Matches:** file_cluster_8: 13.792, file_cluster_13: 14.17, file_cluster_0: 14.189
- **Magnitude:** 526.02 | **LOC:** 271 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (70.1766%), Tech Debt (14.7577%)
**Top Internal Functions/Classes:**
  * `notmain` (Impact: 125.7 | O(N^5) | DB: 39)
    * *Intent:* //------------------------------------------------------------------------
  * `recv_packet` (Impact: 55.5 | O(N^3) | DB: 21)
    * *Intent:* //------------------------------------------------------------------------
  * `hexstrings` (Impact: 24.7 | O(N^2) | DB: 5)
    * *Intent:* //------------------------------------------------------------------------
  * `uart_send` (Impact: 16.3 | O(N^2))
    * *Intent:* //------------------------------------------------------------------------
  * `uart_recv` (Impact: 13.8 | O(N^2))
    * *Intent:* #define AUX_MU_IER_REG 0x20215044 #define AUX_MU_IIR_REG 0x20215048 #define AUX_MU_LCR_REG 0x2021504...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 14`, `args: 12`, `func_start: 7`
* *Risk/State:* `state_mutation: 248`, `orphaned_logic: 1`
* *Architecture:* `api: 26`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pizero/asmdelay/asmdelay.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.128 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.32 IQR)
- **Top Global Matches:** file_cluster_8: 13.128, file_cluster_7: 13.562, file_cluster_13: 13.574
- **Magnitude:** 524.54 | **LOC:** 290 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 69
- **Risk Profile:** Cognitive Load (64.353%), Tech Debt (13.3879%)
**Top Internal Functions/Classes:**
  * `do_it` (Impact: 207.7 | O(N^4) | DB: 69)
  * `notmain` (Impact: 20.1 | O(N^2) | DB: 21)
    * *Intent:* //-------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 21`, `args: 16`, `func_start: 2`
* *Risk/State:* `state_mutation: 264`, `orphaned_logic: 1`
* *Architecture:* `api: 28`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `twain/crc32.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.555 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.086 IQR)
- **Top Global Matches:** file_cluster_13: 14.555, file_cluster_0: 14.602, file_cluster_11: 14.636
- **Magnitude:** 503.0 | **LOC:** 426 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (68.9974%), Tech Debt (16.4818%)
**Top Internal Functions/Classes:**
  * `make_crc_table` (Impact: 59.9 | O(N^4) | DB: 35)
    * *Intent:* # define TBLS 8 #else # define TBLS 1 #endif /* BYFOUR */
  * `crc32` (Impact: 36.3 | O(N^3) | DB: 4)
  * `crc32_combine_` (Impact: 20.6 | O(N^3) | DB: 8)
  * `crc32_big` (Impact: 13.7 | O(N^2) | DB: 15)
  * `crc32_little` (Impact: 13.6 | O(N^2) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 23`, `args: 2`, `func_start: 10`
* *Risk/State:* `state_mutation: 256`, `dead_code: 4`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 71`, `import: 3`
* *Defense:* `immutability_locks: 19`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` zutil.h, stdio.h, crc32.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `armjtag/armjtag.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `armjtag/rpi2/armjtag.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `blinker01/blinker01.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `gps_clock/notmain.c` (C) | Magnitude: 854.88 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 266, indent_spaces: 258, branch: 76, macros: 48
- `jtagproxy/msplaunchpad/jtagproxy.c` (C) | Magnitude: 150.28 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 65, indent_spaces: 58, macros: 57, bitwise_ops: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `twain/inflate.c` (C) | Magnitude: 717.0 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 381, indent_spaces: 312, pointers: 197, branch: 111
- `twain/adler32.c` (C) | Magnitude: 220.24 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 143, indent_spaces: 105, api: 30, branch: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `twain/compress.c` (C) | Magnitude: 66.94 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 33, api: 19, pointers: 12
- `twain/zutil.c` (C) | Magnitude: 263.92 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 136, indent_spaces: 91, branch: 57, macros: 38
- `twain/crc32.c` (C) | Magnitude: 503.0 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 256, indent_spaces: 201, api: 71, branch: 55
- `jtagproxy/ft232rl/parport.c` (C) | Magnitude: 274.28 | Delta: **0.155 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 205, state_mutation: 122, pointers: 42, api: 39
- `jtagproxy/ft232rl/parport_fast.c` (C) | Magnitude: 306.58 | Delta: **0.162 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 221, state_mutation: 130, pointers: 41, api: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `twain/inffast.c` (C) | Magnitude: 349.0 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 302, indent_spaces: 225, branch: 71, pointers: 34
- `boards/pi2/SVC/blinker01/blinker01.c` (C) | Magnitude: 65.38 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 35, indent_spaces: 23, bitwise_ops: 12, api: 8
- `boards/pi2/HYP/blinker01/blinker01.c` (C) | Magnitude: 48.28 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 28, indent_spaces: 19, bitwise_ops: 12, api: 5
- `boards/piaplus/blinker01/blinker01.c` (C) | Magnitude: 48.28 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 28, indent_spaces: 19, bitwise_ops: 12, api: 5
- `boards/piaplus/ssd1306a/ssd1306a.c` (C) | Magnitude: 330.68 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 202, state_mutation: 113, structural_boundaries: 56, api: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `video01/video01.c` (C) | Magnitude: 215.08 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 93, indent_spaces: 85, api: 27, structural_boundaries: 26
- `boards/pizero/blinker01/blinker01.c` (C) | Magnitude: 41.16 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, indent_spaces: 13, bitwise_ops: 6, api: 5
- `bootloader02/bootloader02.c` (C) | Magnitude: 267.54 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 105, state_mutation: 93, branch: 30, macros: 20
- `bootloader01/prograspi.c` (C) | Magnitude: 541.46 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 328, indent_spaces: 209, branch: 47, api: 33
- `blinker01/blinker01.c` (C) | Magnitude: 40.74 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, indent_spaces: 13, bitwise_ops: 6, api: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `twain/zutil.h` -> **Severity: 0.086** (Embedded: 0.0114 * Error Risk: 7.4973%)
- `twain/deflate.h` -> **Severity: 0.052** (Embedded: 0.0036 * Error Risk: 14.4578%)
- `spi01/blinker.h` -> **Severity: 0.016** (Embedded: 0.0018 * Error Risk: 8.84%)
- `twain/trees.h` -> **Severity: 0.013** (Embedded: 0.0018 * Error Risk: 7.1%)
- `twain/inffixed.h` -> **Severity: 0.012** (Embedded: 0.0018 * Error Risk: 6.5752%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `twain/zutil.h` -> **Severity: 844.218** (Blast Radius: 8.783 * Doc Risk: 96.1195%)
- `twain/deflate.h` -> **Severity: 398.2** (Blast Radius: 3.982 * Doc Risk: 100.0%)
- `twain/gzguts.h` -> **Severity: 249.286** (Blast Radius: 2.494 * Doc Risk: 99.9542%)
- `spi01/blinker.h` -> **Severity: 248.848** (Blast Radius: 3.238 * Doc Risk: 76.8525%)
- `twain/inflate.h` -> **Severity: 242.0** (Blast Radius: 2.42 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
