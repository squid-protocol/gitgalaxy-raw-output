# ARCHITECTURAL_BRIEF: cosmopolitan
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/cosmopolitan` |
| **Timestamp** | `2026-08-07T03:49:38.526033+00:00` |
| **Scan Duration** | `11.71s` |
| **Git Branch** | `master` |
| **Git Commit** | `eedf7d2db6e5ee0e228862690339c166a3f003a7` |
| **Git Remote** | `https://github.com/jart/cosmopolitan.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3464 malicious artifacts.

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
| Total Artifacts | 17520 |
| Analyzed Artifacts (Scanned) | 5988 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11532 |
| Total LOC | 198259 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 34.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1223 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 249 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 3343 | 157743 | 55.8% |
| ASSEMBLY | 2482 | 26353 | 41.4% |
| SHELL | 47 | 6444 | 0.8% |
| CPP | 34 | 4704 | 0.6% |
| LUA | 29 | 1689 | 0.5% |
| PLAINTEXT | 26 | 14 | 0.4% |
| MARKDOWN | 9 | 0 | 0.2% |
| PYTHON | 7 | 635 | 0.1% |
| YAML | 4 | 36 | 0.1% |
| MAKEFILE | 2 | 564 | 0.0% |
| HTML | 2 | 34 | 0.0% |
| SQLITE | 1 | 7 | 0.0% |
| CSS | 1 | 35 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.148`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 3885 | 64.9% |
| file_cluster_13 | 1961 | 32.7% |
| file_cluster_4 | 63 | 1.1% |
| file_cluster_9 | 28 | 0.5% |
| Unknown | 15 | 0.3% |
| file_cluster_12 | 2 | 0.0% |
| file_cluster_11 | 2 | 0.0% |
| file_cluster_17 | 2 | 0.0% |
| file_cluster_0 | 1 | 0.0% |
| file_cluster_7 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 28 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11532*

**Composition by Extension & Reason:**
- `no_extension`: 3092x Excluded (Binary Format Detected), 255x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 26x Unsupported Format (.undeterminable)
- `.c`: 2771x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 35 LOC), 1x Excluded (Machine-Generated Source Code Signature: 70 LOC)
- `.h`: 2037x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 95646 LOC exceeds safe regex boundaries), 1x Excluded (Lexical Monotony: High structural repetition detected in 4381 LOC)
- `.py`: 1750x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inc`: 182x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 13973 commas in 1086 LOC), 1x Excluded (Embedded Array/Matrix Payload: 23940 commas in 1867 LOC)
- `.txt`: 178x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2622 LOC), 1x Excluded (Monolithic Amalgamation: 34925 LOC exceeds safe regex boundaries)
- `.mk`: 164x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dectest`: 143x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cc`: 135x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 1342 hex tokens in 713 LOC), 1x Excluded (Embedded Hex Payload: 1308 hex tokens in 696 LOC)
- `.cpp`: 95x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.der`: 72x Excluded (Explicitly Denied Extension: '.der')
- `.datax`: 67x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lua`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cosmo`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.cosmo')
- `.s`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2099 LOC), 1x Excluded (Machine-Generated Source Code Signature: 95 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 18.6 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 30.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 23.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.2 | 1.8 | 0.2 |
| API Exposure | 0.0 | 19.9 | 4.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 29.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 62.1 | 86.7 | 100.0 |
| Instability Exposure | 0.0 | 5.2 | 1.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 41.6 | 31.9 | 6.2 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tool/cosmocc/bin/cosmoc++` (Hits: 108)
- `tool/cosmocc/bin/cosmocc` (Hits: 108)
- `tool/cosmocc/bin/unknown-unknown-cosmo-c++` (Hits: 108)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **str.h** (`libc/str/str.h`) — 565 inbound connections
2. **dce.h** (`libc/dce.h`) — 473 inbound connections
3. **calls.h** (`libc/calls/calls.h`) — 406 inbound connections
4. **errno.h** (`libc/errno.h`) — 331 inbound connections
5. **errfuns.h** (`libc/sysv/errfuns.h`) — 324 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Makefile** (`Makefile`) — 166 outbound dependencies
2. **redbean.c** (`tool/net/redbean.c`) — 123 outbound dependencies
3. **printvideo.c** (`tool/viz/printvideo.c`) — 85 outbound dependencies
4. **turfwar.c** (`net/turfwar/turfwar.c`) — 75 outbound dependencies
5. **sig.c** (`libc/intrin/sig.c`) — 62 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main` (@ `examples/romanize.c`) -> Impact: **1052.9** | LOC: 931
- `Anonymous_Block_[Truncated]` (@ `tool/cosmocc/bin/cosmoc++`) -> Impact: **819.2** | LOC: 742
  * *Intent:* #!/bin/sh # fat cosmopolitan c/c++ compiler # https://github.com/jart/cosmopolitan # https://cosmo.zip/
- `Anonymous_Block_[Truncated]` (@ `tool/cosmocc/bin/cosmocc`) -> Impact: **819.2** | LOC: 742
  * *Intent:* #!/bin/sh # fat cosmopolitan c/c++ compiler # https://github.com/jart/cosmopolitan # https://cosmo.zip/
- `Anonymous_Block_[Truncated]` (@ `tool/cosmocc/bin/unknown-unknown-cosmo-c++`) -> Impact: **819.2** | LOC: 742
  * *Intent:* #!/bin/sh # fat cosmopolitan c/c++ compiler # https://github.com/jart/cosmopolitan # https://cosmo.zip/
- `Anonymous_Block_[Truncated]` (@ `tool/cosmocc/bin/unknown-unknown-cosmo-cc`) -> Impact: **819.2** | LOC: 742
  * *Intent:* #!/bin/sh # fat cosmopolitan c/c++ compiler # https://github.com/jart/cosmopolitan # https://cosmo.zip/
- `__fmt` (@ `libc/stdio/fmt.c`) -> Impact: **813.9** | LOC: 651
- `Parse` (@ `tool/net/ljson.c`) -> Impact: **591.4** | LOC: 398
- `getAvailableFeatures` (@ `libc/intrin/x86.c`) -> Impact: **562.3** | LOC: 289
- `Anonymous_Block_[Truncated]` (@ `tool/cosmocc/bin/aarch64-unknown-cosmo-c++`) -> Impact: **560.3** | LOC: 345
  * *Intent:* #!/bin/sh # cosmopolitan c/c++ cross compiler # https://github.com/jart/cosmopolitan # https://cosmo.zip/
- `Anonymous_Block_[Truncated]` (@ `tool/cosmocc/bin/aarch64-unknown-cosmo-cc`) -> Impact: **560.3** | LOC: 345
  * *Intent:* #!/bin/sh # cosmopolitan c/c++ cross compiler # https://github.com/jart/cosmopolitan # https://cosmo.zip/

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `usr/share/ssl/root` | 15 | 70004.66 | 0.33% | 6.67% |
| `libc/intrin` | 473 | 27509.84 | 29.84% | 56.54% |
| `libc/calls` | 413 | 23598.96 | 37.95% | 45.29% |
| `libc/tinymath` | 285 | 21575.28 | 42.69% | 48.43% |
| `libc/sysv/consts` | 1208 | 14349.76 | 5.11% | 0.17% |
| `examples` | 65 | 11441.3 | 50.24% | 0.0% |
| `tool/cosmocc/bin` | 18 | 10877.1 | 66.4% | 37.85% |
| `libc/stdio` | 179 | 9743.22 | 21.6% | 66.77% |
| `tool/viz` | 35 | 9167.84 | 63.76% | 44.63% |
| `libc/str` | 188 | 8262.32 | 22.83% | 57.46% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `ctl/accumulate.h` -> **100.0%** Exposure
- `ctl/equal.h` -> **100.0%** Exposure
- `dsp/core/det3.c` -> **100.0%** Exposure
- `dsp/core/gamma.c` -> **100.0%** Exposure
- `dsp/core/matvmul3.c` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `ape/ape-m1.c` -> **100.0%** Exposure
- `ape/loader.c` -> **100.0%** Exposure
- `ctl/accumulate.h` -> **100.0%** Exposure
- `ctl/advance.h` -> **100.0%** Exposure
- `ctl/copy.h` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tool/net/lfuncs.c` -> **84** Orphaned Functions | **0** Duplicates
- `libc/vga/rlinit-vesa.S` -> **40** Orphaned Functions | **0** Duplicates
- `libc/intrin/ubsan.c` -> **37** Orphaned Functions | **0** Duplicates
- `ctl/string.h` -> **0** Orphaned Functions | **34** Duplicates
- `ctl/string.cc` -> **16** Orphaned Functions | **13** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`dsp/core/getintegercoefficients.c`** -> AI Confidence: **99.48%**
2. **`dsp/prog/play.c`** -> AI Confidence: **99.48%**
3. **`examples/caesar.c`** -> AI Confidence: **99.48%**
4. **`examples/kill.c`** -> AI Confidence: **99.48%**
5. **`examples/kilo.c`** -> AI Confidence: **99.48%**
6. **`examples/linenoise.c`** -> AI Confidence: **99.48%**
7. **`examples/script.c`** -> AI Confidence: **99.48%**
8. **`examples/spawn.c`** -> AI Confidence: **99.48%**
9. **`examples/vga2.c`** -> AI Confidence: **99.48%**
10. **`examples/walk.c`** -> AI Confidence: **99.48%**
11. **`examples/whois.c`** -> AI Confidence: **99.48%**
12. **`libc/calls/chdir.c`** -> AI Confidence: **99.48%**
13. **`libc/calls/closefrom.c`** -> AI Confidence: **99.48%**
14. **`libc/calls/dup.c`** -> AI Confidence: **99.48%**
15. **`libc/calls/dup2.c`** -> AI Confidence: **99.48%**
16. **`libc/calls/dup3.c`** -> AI Confidence: **99.48%**
17. **`libc/calls/fchdir.c`** -> AI Confidence: **99.48%**
18. **`libc/calls/fchmod.c`** -> AI Confidence: **99.48%**
19. **`libc/calls/fchmodat.c`** -> AI Confidence: **99.48%**
20. **`libc/calls/fchownat.c`** -> AI Confidence: **99.48%**
21. **`libc/calls/fcntl_dupfd.c`** -> AI Confidence: **99.48%**
22. **`libc/calls/fcntl_dupfd_cloexec.c`** -> AI Confidence: **99.48%**
23. **`libc/calls/fcntl_getfd.c`** -> AI Confidence: **99.48%**
24. **`libc/calls/fcntl_getfl.c`** -> AI Confidence: **99.48%**
25. **`libc/calls/fcntl_setfd.c`** -> AI Confidence: **99.48%**
26. **`libc/calls/fcntl_setfl.c`** -> AI Confidence: **99.48%**
27. **`libc/calls/fdatasync.c`** -> AI Confidence: **99.48%**
28. **`libc/calls/fixenotdir.c`** -> AI Confidence: **99.48%**
29. **`libc/calls/fsync.c`** -> AI Confidence: **99.48%**
30. **`libc/calls/ftruncate.c`** -> AI Confidence: **99.48%**
31. **`libc/calls/getcurrentdirectory.c`** -> AI Confidence: **99.48%**
32. **`libc/calls/getdomainname.c`** -> AI Confidence: **99.48%**
33. **`libc/calls/getentropy.c`** -> AI Confidence: **99.48%**
34. **`libc/calls/grantpt.c`** -> AI Confidence: **99.48%**
35. **`libc/calls/linkat.c`** -> AI Confidence: **99.48%**
36. **`libc/calls/lseek.c`** -> AI Confidence: **99.48%**
37. **`libc/calls/makedirs.c`** -> AI Confidence: **99.48%**
38. **`libc/calls/mkdirat.c`** -> AI Confidence: **99.48%**
39. **`libc/calls/mkntpath.c`** -> AI Confidence: **99.48%**
40. **`libc/calls/openat.c`** -> AI Confidence: **99.48%**
41. **`libc/calls/pipe2.c`** -> AI Confidence: **99.48%**
42. **`libc/calls/pledge.c`** -> AI Confidence: **99.48%**
43. **`libc/calls/poll-metal.c`** -> AI Confidence: **99.48%**
44. **`libc/calls/posix_fadvise.c`** -> AI Confidence: **99.48%**
45. **`libc/calls/posix_openpt.c`** -> AI Confidence: **99.48%**
46. **`libc/calls/ptsname.c`** -> AI Confidence: **99.48%**
47. **`libc/calls/raise.c`** -> AI Confidence: **99.48%**
48. **`libc/calls/readlinkat.c`** -> AI Confidence: **99.48%**
49. **`libc/calls/renameat.c`** -> AI Confidence: **99.48%**
50. **`libc/calls/seccomp.c`** -> AI Confidence: **99.48%**
51. **`libc/calls/sigpending.c`** -> AI Confidence: **99.48%**
52. **`libc/calls/symlinkat.c`** -> AI Confidence: **99.48%**
53. **`libc/calls/tcgetpgrp.c`** -> AI Confidence: **99.48%**
54. **`libc/calls/tcgetsid.c`** -> AI Confidence: **99.48%**
55. **`libc/calls/tcsetpgrp.c`** -> AI Confidence: **99.48%**
56. **`libc/calls/tcsetsid.c`** -> AI Confidence: **99.48%**
57. **`libc/calls/truncate.c`** -> AI Confidence: **99.48%**
58. **`libc/calls/unlockpt.c`** -> AI Confidence: **99.48%**
59. **`libc/calls/utimens.c`** -> AI Confidence: **99.48%**
60. **`libc/fmt/wcstol.c`** -> AI Confidence: **99.48%**
61. **`libc/fmt/wcstoul.c`** -> AI Confidence: **99.48%**
62. **`libc/intrin/exit.c`** -> AI Confidence: **99.48%**
63. **`libc/intrin/exit1.greg.c`** -> AI Confidence: **99.48%**
64. **`libc/intrin/kprintf.greg.c`** -> AI Confidence: **99.48%**
65. **`libc/intrin/msync.c`** -> AI Confidence: **99.48%**
66. **`libc/intrin/posix_madvise-nt.c`** -> AI Confidence: **99.48%**
67. **`libc/intrin/pthread_setcancelstate.c`** -> AI Confidence: **99.48%**
68. **`libc/intrin/sigprocmask-nt.c`** -> AI Confidence: **99.48%**
69. **`libc/intrin/tprecode8to16.c`** -> AI Confidence: **99.48%**
70. **`libc/isystem/sys/mman.h`** -> AI Confidence: **99.48%**
71. **`libc/mem/realpath.c`** -> AI Confidence: **99.48%**
72. **`libc/proc/execve.c`** -> AI Confidence: **99.48%**
73. **`libc/proc/getpriority.c`** -> AI Confidence: **99.48%**
74. **`libc/proc/posix_spawn.c`** -> AI Confidence: **99.48%**
75. **`libc/runtime/efimain.greg.c`** -> AI Confidence: **99.48%**
76. **`libc/runtime/getlogin.c`** -> AI Confidence: **99.48%**
77. **`libc/runtime/getlogin_r.c`** -> AI Confidence: **99.48%**
78. **`libc/runtime/login_tty.c`** -> AI Confidence: **99.48%**
79. **`libc/runtime/set_tls.c`** -> AI Confidence: **99.48%**
80. **`libc/sock/getsockopt.c`** -> AI Confidence: **99.48%**
81. **`libc/sock/listen.c`** -> AI Confidence: **99.48%**
82. **`libc/sock/shutdown.c`** -> AI Confidence: **99.48%**
83. **`libc/sock/socket.c`** -> AI Confidence: **99.48%**
84. **`libc/stdio/fflush_unlocked.c`** -> AI Confidence: **99.48%**
85. **`libc/stdio/fmt.c`** -> AI Confidence: **99.48%**
86. **`libc/stdio/fseek_unlocked.c`** -> AI Confidence: **99.48%**
87. **`libc/stdio/printargs.c`** -> AI Confidence: **99.48%**
88. **`libc/stdio/vcscanf.c`** -> AI Confidence: **99.48%**
89. **`libc/str/strtol.c`** -> AI Confidence: **99.48%**
90. **`libc/str/strtoul.c`** -> AI Confidence: **99.48%**
91. **`libc/thread/pthread_getaffinity_np.c`** -> AI Confidence: **99.48%**
92. **`libc/thread/pthread_kill.c`** -> AI Confidence: **99.48%**
93. **`libc/x/utf16to8.c`** -> AI Confidence: **99.48%**
94. **`net/http/escapejsstringliteral.c`** -> AI Confidence: **99.48%**
95. **`net/http/parsehttpmessage.c`** -> AI Confidence: **99.48%**
96. **`net/https/fetch.c`** -> AI Confidence: **99.48%**
97. **`tool/args/args2.c`** -> AI Confidence: **99.48%**
98. **`tool/chat/server.c`** -> AI Confidence: **99.48%**
99. **`tool/decode/ent.c`** -> AI Confidence: **99.48%**
100. **`tool/lambda/bru2bin.c`** -> AI Confidence: **99.48%**
101. **`tool/lambda/lam2bin.c`** -> AI Confidence: **99.48%**
102. **`tool/net/libresolv_query.c`** -> AI Confidence: **99.48%**
103. **`tool/net/ljson.c`** -> AI Confidence: **99.48%**
104. **`tool/viz/datauri.c`** -> AI Confidence: **99.48%**
105. **`tool/viz/fold.c`** -> AI Confidence: **99.48%**
106. **`tool/viz/fontspace.c`** -> AI Confidence: **99.48%**
107. **`tool/viz/getifaddrs.c`** -> AI Confidence: **99.48%**
108. **`tool/viz/maxmind.c`** -> AI Confidence: **99.48%**
109. **`tool/viz/od16.c`** -> AI Confidence: **99.48%**
110. **`libc/str/crc32c.cc`** -> AI Confidence: **99.48%**
111. **`dsp/tty/ident.c`** -> AI Confidence: **99.39%**
112. **`examples/greenbean.c`** -> AI Confidence: **99.39%**
113. **`examples/portscan.c`** -> AI Confidence: **99.39%**
114. **`examples/rote.c`** -> AI Confidence: **99.39%**
115. **`examples/vga.c`** -> AI Confidence: **99.39%**
116. **`libc/calls/clock_nanosleep-sys.c`** -> AI Confidence: **99.39%**
117. **`libc/calls/close.c`** -> AI Confidence: **99.39%**
118. **`libc/calls/copy_file_range.c`** -> AI Confidence: **99.39%**
119. **`libc/calls/fstat.c`** -> AI Confidence: **99.39%**
120. **`libc/calls/fstatat.c`** -> AI Confidence: **99.39%**
121. **`libc/calls/getcwd.c`** -> AI Confidence: **99.39%**
122. **`libc/calls/getloadavg.c`** -> AI Confidence: **99.39%**
123. **`libc/calls/getprogramexecutablename.greg.c`** -> AI Confidence: **99.39%**
124. **`libc/calls/getrandom.c`** -> AI Confidence: **99.39%**
125. **`libc/calls/getrlimit.c`** -> AI Confidence: **99.39%**
126. **`libc/calls/mkdtemp.c`** -> AI Confidence: **99.39%**
127. **`libc/calls/mknod.c`** -> AI Confidence: **99.39%**
128. **`libc/calls/openatemp.c`** -> AI Confidence: **99.39%**
129. **`libc/calls/pledge-linux.c`** -> AI Confidence: **99.39%**
130. **`libc/calls/prctl.c`** -> AI Confidence: **99.39%**
131. **`libc/calls/pread.c`** -> AI Confidence: **99.39%**
132. **`libc/calls/pwrite.c`** -> AI Confidence: **99.39%**
133. **`libc/calls/read.c`** -> AI Confidence: **99.39%**
134. **`libc/calls/setrlimit.c`** -> AI Confidence: **99.39%**
135. **`libc/calls/splice.c`** -> AI Confidence: **99.39%**
136. **`libc/calls/tcdrain.c`** -> AI Confidence: **99.39%**
137. **`libc/calls/tcgetattr-nt.c`** -> AI Confidence: **99.39%**
138. **`libc/calls/tcsetattr-nt.c`** -> AI Confidence: **99.39%**
139. **`libc/calls/unlinkat.c`** -> AI Confidence: **99.39%**
140. **`libc/intrin/createfile.c`** -> AI Confidence: **99.39%**
141. **`libc/intrin/describesiginfo.c`** -> AI Confidence: **99.39%**
142. **`libc/intrin/munmap-sysv.c`** -> AI Confidence: **99.39%**
143. **`libc/intrin/printmaps.c`** -> AI Confidence: **99.39%**
144. **`libc/intrin/sys_gettid.greg.c`** -> AI Confidence: **99.39%**
145. **`libc/intrin/wsarecv.c`** -> AI Confidence: **99.39%**
146. **`libc/mem/setenv.c`** -> AI Confidence: **99.39%**
147. **`libc/proc/fexecve.c`** -> AI Confidence: **99.39%**
148. **`libc/proc/sched_getaffinity.c`** -> AI Confidence: **99.39%**
149. **`libc/proc/setpriority-nt.c`** -> AI Confidence: **99.39%**
150. **`libc/runtime/cosmo2.c`** -> AI Confidence: **99.39%**
151. **`libc/runtime/getinterpreterexecutablename.c`** -> AI Confidence: **99.39%**
152. **`libc/runtime/inflate.c`** -> AI Confidence: **99.39%**
153. **`libc/runtime/opensymboltable.greg.c`** -> AI Confidence: **99.39%**
154. **`libc/runtime/zipos-seek.c`** -> AI Confidence: **99.39%**
155. **`libc/sock/bind.c`** -> AI Confidence: **99.39%**
156. **`libc/sock/connect.c`** -> AI Confidence: **99.39%**
157. **`libc/sock/inet_pton.c`** -> AI Confidence: **99.39%**
158. **`libc/sock/recv.c`** -> AI Confidence: **99.39%**
159. **`libc/sock/recvfrom.c`** -> AI Confidence: **99.39%**
160. **`libc/sock/recvmsg.c`** -> AI Confidence: **99.39%**
161. **`libc/sock/sendmsg.c`** -> AI Confidence: **99.39%**
162. **`libc/sock/setsockopt.c`** -> AI Confidence: **99.39%**
163. **`libc/stdio/appendr.c`** -> AI Confidence: **99.39%**
164. **`libc/stdio/appendw.c`** -> AI Confidence: **99.39%**
165. **`libc/stdio/getdelim_unlocked.c`** -> AI Confidence: **99.39%**
166. **`libc/system/cocmd.c`** -> AI Confidence: **99.39%**
167. **`libc/system/popen.c`** -> AI Confidence: **99.39%**
168. **`libc/thread/pthread_barrier_wait.c`** -> AI Confidence: **99.39%**
169. **`libc/thread/pthread_exit.c`** -> AI Confidence: **99.39%**
170. **`libc/thread/sem_timedwait.c`** -> AI Confidence: **99.39%**
171. **`libc/x/syslog.c`** -> AI Confidence: **99.39%**
172. **`tool/curl/curl.c`** -> AI Confidence: **99.39%**
173. **`tool/viz/basicidea.c`** -> AI Confidence: **99.39%**
174. **`tool/viz/bing.c`** -> AI Confidence: **99.39%**
175. **`tool/viz/derasterize.c`** -> AI Confidence: **99.39%**
176. **`tool/viz/getglyph.c`** -> AI Confidence: **99.39%**
177. **`tool/viz/img.c`** -> AI Confidence: **99.39%**
178. **`examples/nesemu1.cc`** -> AI Confidence: **99.39%**
179. **`libc/calls/faccessat.c`** -> AI Confidence: **99.35%**
180. **`libc/stdio/nftw.c`** -> AI Confidence: **99.35%**
181. **`tool/decode/x86opinfo.c`** -> AI Confidence: **99.35%**
182. **`dsp/core/getintegercoefficients8.c`** -> AI Confidence: **99.34%**
183. **`dsp/tty/describe.c`** -> AI Confidence: **99.34%**
184. **`dsp/tty/ttymove.c`** -> AI Confidence: **99.34%**
185. **`examples/hiredis.c`** -> AI Confidence: **99.34%**
186. **`examples/romanize.c`** -> AI Confidence: **99.34%**
187. **`examples/statfs.c`** -> AI Confidence: **99.34%**
188. **`libc/calls/fixupnewfd.c`** -> AI Confidence: **99.34%**
189. **`libc/calls/getgroups.c`** -> AI Confidence: **99.34%**
190. **`libc/calls/gethostname.c`** -> AI Confidence: **99.34%**
191. **`libc/calls/madvise.c`** -> AI Confidence: **99.34%**
192. **`libc/calls/pipe2-sysv.c`** -> AI Confidence: **99.34%**
193. **`libc/calls/setgroups.c`** -> AI Confidence: **99.34%**
194. **`libc/calls/xoflags.c`** -> AI Confidence: **99.34%**
195. **`libc/intrin/describeschedpolicy.c`** -> AI Confidence: **99.34%**
196. **`libc/intrin/describesicode.c`** -> AI Confidence: **99.34%**
197. **`libc/intrin/describesockoptname.c`** -> AI Confidence: **99.34%**
198. **`libc/intrin/describestatfs.c`** -> AI Confidence: **99.34%**
199. **`libc/intrin/pthread_rwlock_rdlock.c`** -> AI Confidence: **99.34%**
200. **`libc/intrin/pthread_rwlock_wrlock.c`** -> AI Confidence: **99.34%**
201. **`libc/intrin/strerror_r.c`** -> AI Confidence: **99.34%**
202. **`libc/intrin/tprecode16to8.c`** -> AI Confidence: **99.34%**
203. **`libc/stdio/dumphexc.c`** -> AI Confidence: **99.34%**
204. **`libc/stdio/fclose.c`** -> AI Confidence: **99.34%**
205. **`libc/stdio/fgets_unlocked.c`** -> AI Confidence: **99.34%**
206. **`libc/stdio/fopenflags.c`** -> AI Confidence: **99.34%**
207. **`libc/stdio/freopen.c`** -> AI Confidence: **99.34%**
208. **`libc/stdio/gcvt.c`** -> AI Confidence: **99.34%**
209. **`libc/stdio/setvbuf.c`** -> AI Confidence: **99.34%**
210. **`libc/str/strnwidth.c`** -> AI Confidence: **99.34%**
211. **`libc/thread/sem_destroy.c`** -> AI Confidence: **99.34%**
212. **`libc/x/utf8to16.c`** -> AI Confidence: **99.34%**
213. **`libc/x/utf8to32.c`** -> AI Confidence: **99.34%**
214. **`net/http/encodehttpheadervalue.c`** -> AI Confidence: **99.34%**
215. **`net/http/encodelatin1.c`** -> AI Confidence: **99.34%**
216. **`net/http/unchunk.c`** -> AI Confidence: **99.34%**
217. **`tool/viz/dumphexc.c`** -> AI Confidence: **99.34%**
218. **`dsp/core/scalevolume.c`** -> AI Confidence: **99.32%**
219. **`examples/print-struct.c`** -> AI Confidence: **99.32%**
220. **`libc/calls/parsepromises.c`** -> AI Confidence: **99.32%**
221. **`libc/fmt/atoi.c`** -> AI Confidence: **99.32%**
222. **`libc/fmt/atol.c`** -> AI Confidence: **99.32%**
223. **`libc/fmt/strtonum.c`** -> AI Confidence: **99.32%**
224. **`libc/isystem/strings.h`** -> AI Confidence: **99.32%**
225. **`libc/isystem/tgmath.h`** -> AI Confidence: **99.32%**
226. **`libc/mem/levenshtein.c`** -> AI Confidence: **99.32%**
227. **`libc/runtime/getdosenviron.c`** -> AI Confidence: **99.32%**
228. **`libc/runtime/metalprintf.greg.c`** -> AI Confidence: **99.32%**
229. **`libc/stdio/fgetws_unlocked.c`** -> AI Confidence: **99.32%**
230. **`libc/stdio/strtold.c`** -> AI Confidence: **99.32%**
231. **`libc/str/lz4len.c`** -> AI Confidence: **99.32%**
232. **`libc/str/strcasecmp.c`** -> AI Confidence: **99.32%**
233. **`libc/thread/pthread_spin_lock.c`** -> AI Confidence: **99.32%**
234. **`libc/tinymath/asinh.c`** -> AI Confidence: **99.32%**
235. **`libc/tinymath/atanhl.c`** -> AI Confidence: **99.32%**
236. **`libc/tinymath/entropy.c`** -> AI Confidence: **99.32%**
237. **`libc/tinymath/expl.c`** -> AI Confidence: **99.32%**
238. **`libc/tinymath/lgammal.c`** -> AI Confidence: **99.32%**
239. **`libc/x/utf32to8.c`** -> AI Confidence: **99.32%**
240. **`net/finger/describesyn.c`** -> AI Confidence: **99.32%**
241. **`net/http/decodelatin1.c`** -> AI Confidence: **99.32%**
242. **`net/http/encodebase64.c`** -> AI Confidence: **99.32%**
243. **`net/http/parsecidr.c`** -> AI Confidence: **99.32%**
244. **`net/http/parseforwarded.c`** -> AI Confidence: **99.32%**
245. **`tool/decode/word.c`** -> AI Confidence: **99.32%**
246. **`tool/lambda/asc2bin.c`** -> AI Confidence: **99.32%**
247. **`tool/viz/bin2asm.c`** -> AI Confidence: **99.32%**
248. **`net/http/gethttpheader.inc`** -> AI Confidence: **99.32%**
249. **`ape/ape-m1.c`** -> AI Confidence: **99.31%**
250. **`dsp/scale/gyarados.c`** -> AI Confidence: **99.31%**
251. **`dsp/scale/magikarp.c`** -> AI Confidence: **99.31%**
252. **`dsp/tty/rgb2ansi.c`** -> AI Confidence: **99.31%**
253. **`dsp/tty/write.c`** -> AI Confidence: **99.31%**
254. **`examples/art.c`** -> AI Confidence: **99.31%**
255. **`examples/asteroids.c`** -> AI Confidence: **99.31%**
256. **`examples/ctrlc.c`** -> AI Confidence: **99.31%**
257. **`examples/spawn_bench.c`** -> AI Confidence: **99.31%**
258. **`examples/stackexplorer.c`** -> AI Confidence: **99.31%**
259. **`examples/stat.c`** -> AI Confidence: **99.31%**
260. **`examples/trapping.c`** -> AI Confidence: **99.31%**
261. **`examples/ttyinfo.c`** -> AI Confidence: **99.31%**
262. **`examples/wall.c`** -> AI Confidence: **99.31%**
263. **`libc/calls/_ptsname.c`** -> AI Confidence: **99.31%**
264. **`libc/calls/abort.c`** -> AI Confidence: **99.31%**
265. **`libc/calls/arc4random.c`** -> AI Confidence: **99.31%**
266. **`libc/calls/assertfail.c`** -> AI Confidence: **99.31%**
267. **`libc/calls/chdir-nt.c`** -> AI Confidence: **99.31%**
268. **`libc/calls/clktck.c`** -> AI Confidence: **99.31%**
269. **`libc/calls/clock_getres.c`** -> AI Confidence: **99.31%**
270. **`libc/calls/clock_nanosleep-openbsd.c`** -> AI Confidence: **99.31%**
271. **`libc/calls/clock_nanosleep-xnu.c`** -> AI Confidence: **99.31%**
272. **`libc/calls/clock_nanosleep.c`** -> AI Confidence: **99.31%**
273. **`libc/calls/clock_settime.c`** -> AI Confidence: **99.31%**
274. **`libc/calls/commandv.c`** -> AI Confidence: **99.31%**
275. **`libc/calls/createfileflags.c`** -> AI Confidence: **99.31%**
276. **`libc/calls/dup-nt.c`** -> AI Confidence: **99.31%**
277. **`libc/calls/dup3-sysv.c`** -> AI Confidence: **99.31%**
278. **`libc/calls/faccessat-nt.c`** -> AI Confidence: **99.31%**
279. **`libc/calls/fchmodat-linux.c`** -> AI Confidence: **99.31%**
280. **`libc/calls/fcntl_lock.c`** -> AI Confidence: **99.31%**
281. **`libc/calls/flocks.c`** -> AI Confidence: **99.31%**
282. **`libc/calls/fstat-nt.c`** -> AI Confidence: **99.31%**
283. **`libc/calls/fstatat-nt.c`** -> AI Confidence: **99.31%**
284. **`libc/calls/fstatfs.c`** -> AI Confidence: **99.31%**
285. **`libc/calls/ftruncate-nt.c`** -> AI Confidence: **99.31%**
286. **`libc/calls/getcpu.c`** -> AI Confidence: **99.31%**
287. **`libc/calls/getcpucount.c`** -> AI Confidence: **99.31%**
288. **`libc/calls/getuid.c`** -> AI Confidence: **99.31%**
289. **`libc/calls/ioctl.c`** -> AI Confidence: **99.31%**
290. **`libc/calls/isatty.c`** -> AI Confidence: **99.31%**
291. **`libc/calls/linkat-nt.c`** -> AI Confidence: **99.31%**
292. **`libc/calls/lseek-nt.c`** -> AI Confidence: **99.31%**
293. **`libc/calls/mkntcmdline.c`** -> AI Confidence: **99.31%**
294. **`libc/calls/mkntenvblock.c`** -> AI Confidence: **99.31%**
295. **`libc/calls/ntspawn.c`** -> AI Confidence: **99.31%**
296. **`libc/calls/open-nt.c`** -> AI Confidence: **99.31%**
297. **`libc/calls/openat-metal.c`** -> AI Confidence: **99.31%**
298. **`libc/calls/openat-sysv.c`** -> AI Confidence: **99.31%**
299. **`libc/calls/park.c`** -> AI Confidence: **99.31%**
300. **`libc/calls/poll-nt.c`** -> AI Confidence: **99.31%**
301. **`libc/calls/posix_fadvise-nt.c`** -> AI Confidence: **99.31%**
302. **`libc/calls/ppoll.c`** -> AI Confidence: **99.31%**
303. **`libc/calls/preadv.c`** -> AI Confidence: **99.31%**
304. **`libc/calls/pselect.c`** -> AI Confidence: **99.31%**
305. **`libc/calls/pwritev.c`** -> AI Confidence: **99.31%**
306. **`libc/calls/read-nt.c`** -> AI Confidence: **99.31%**
307. **`libc/calls/readv-metal.c`** -> AI Confidence: **99.31%**
308. **`libc/calls/readv-nt.c`** -> AI Confidence: **99.31%**
309. **`libc/calls/readv.c`** -> AI Confidence: **99.31%**
310. **`libc/calls/renameat-nt.c`** -> AI Confidence: **99.31%**
311. **`libc/calls/restrict.c`** -> AI Confidence: **99.31%**
312. **`libc/calls/sched_get_priority_max.c`** -> AI Confidence: **99.31%**
313. **`libc/calls/sched_get_priority_min.c`** -> AI Confidence: **99.31%**
314. **`libc/calls/sched_getcpu.c`** -> AI Confidence: **99.31%**
315. **`libc/calls/sched_setscheduler.c`** -> AI Confidence: **99.31%**
316. **`libc/calls/select-nt.c`** -> AI Confidence: **99.31%**
317. **`libc/calls/sigaction.c`** -> AI Confidence: **99.31%**
318. **`libc/calls/sigsuspend.c`** -> AI Confidence: **99.31%**
319. **`libc/calls/sigtimedwait-nt.c`** -> AI Confidence: **99.31%**
320. **`libc/calls/sigtimedwait.c`** -> AI Confidence: **99.31%**
321. **`libc/calls/sleep.c`** -> AI Confidence: **99.31%**
322. **`libc/calls/statfs.c`** -> AI Confidence: **99.31%**
323. **`libc/calls/sysinfo-nt.c`** -> AI Confidence: **99.31%**
324. **`libc/calls/tcflow.c`** -> AI Confidence: **99.31%**
325. **`libc/calls/tcflush.c`** -> AI Confidence: **99.31%**
326. **`libc/calls/tcgetattr.c`** -> AI Confidence: **99.31%**
327. **`libc/calls/tcgetwinsize.c`** -> AI Confidence: **99.31%**
328. **`libc/calls/tcsendbreak.c`** -> AI Confidence: **99.31%**
329. **`libc/calls/tcsetwinsize.c`** -> AI Confidence: **99.31%**
330. **`libc/calls/tmpdir.c`** -> AI Confidence: **99.31%**
331. **`libc/calls/tmpfd.c`** -> AI Confidence: **99.31%**
332. **`libc/calls/ttyname_r.c`** -> AI Confidence: **99.31%**
333. **`libc/calls/uname.c`** -> AI Confidence: **99.31%**
334. **`libc/calls/unassert.c`** -> AI Confidence: **99.31%**
335. **`libc/calls/unlinkat-nt.c`** -> AI Confidence: **99.31%**
336. **`libc/calls/unveil.c`** -> AI Confidence: **99.31%**
337. **`libc/calls/utimensat-nt.c`** -> AI Confidence: **99.31%**
338. **`libc/calls/utimensat-old.c`** -> AI Confidence: **99.31%**
339. **`libc/calls/utimensat-sysv.c`** -> AI Confidence: **99.31%**
340. **`libc/calls/utimes.c`** -> AI Confidence: **99.31%**
341. **`libc/calls/warmup.c`** -> AI Confidence: **99.31%**
342. **`libc/calls/winexec.c`** -> AI Confidence: **99.31%**
343. **`libc/calls/write-nt.c`** -> AI Confidence: **99.31%**
344. **`libc/calls/write.c`** -> AI Confidence: **99.31%**
345. **`libc/calls/writev-nt.c`** -> AI Confidence: **99.31%**
346. **`libc/calls/writev.c`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `net/http/ssh.c` -> **99.9991%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `117` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13566` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `libc/intrin/maps.c` (C) -> Cumulative Risk: **748.43**
- **Archetype:** `file_cluster_4` (Distance: 14.364 IQR)
- **Magnitude:** 630.0 | **LOC:** 431 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `__maps_mark` (Impact: 27.9), `__maps_unmark` (Impact: 26.4), `__maps_init` (Impact: 10.9)

### 2. `libc/runtime/clone.c` (C) -> Cumulative Risk: **739.02**
- **Archetype:** `file_cluster_4` (Distance: 13.975 IQR)
- **Magnitude:** 272.92 | **LOC:** 592 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9991%), Documentation (94.5843%)
- **Heaviest Functions:** `volatile` (Impact: 52.9), `FreebsdThreadMain` (Impact: 32.0), `volatile` (Impact: 3.0)

### 3. `net/turfwar/turfwar.c` (C) -> Cumulative Risk: **721.26**
- **Archetype:** `file_cluster_4` (Distance: 13.777 IQR)
- **Magnitude:** 1334.72 | **LOC:** 2951 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (98.7147%)
- **Heaviest Functions:** `main` (Impact: 53.6), `describe_backtrace` (Impact: 30.2), `IsValidNick` (Impact: 29.0)

### 4. `libc/proc/kill-nt.c` (C) -> Cumulative Risk: **718.62**
- **Archetype:** `file_cluster_4` (Distance: 12.498 IQR)
- **Magnitude:** 96.44 | **LOC:** 130 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Concurrency (99.9485%)
- **Heaviest Functions:** `sys_kill_nt` (Impact: 41.9)

### 5. `libc/intrin/cursor.c` (C) -> Cumulative Risk: **712.06**
- **Archetype:** `file_cluster_4` (Distance: 12.757 IQR)
- **Magnitude:** 74.48 | **LOC:** 87 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9541%)
- **Heaviest Functions:** `__cursor_unref` (Impact: 8.8), `__cursor_new` (Impact: 8.0), `__cursor_ref` (Impact: 4.2)

### 6. `libc/intrin/clock_gettime-freebsd.c` (C) -> Cumulative Risk: **711.42**
- **Archetype:** `file_cluster_4` (Distance: 12.445 IQR)
- **Magnitude:** 303.58 | **LOC:** 242 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (99.9995%)
- **Heaviest Functions:** `sys_clock_gettime_freebsd_vdso` (Impact: 29.2), `binuptime` (Impact: 19.6), `gettc` (Impact: 18.9)

### 7. `net/http/ssh.c` (C) -> Cumulative Risk: **710.69**
- **Archetype:** `file_cluster_13` (Distance: 14.27 IQR)
- **Magnitude:** 637.7 | **LOC:** 417 | **CtrlFlow:** 59.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Secrets Risk (99.9991%)
- **Heaviest Functions:** `ParseOpensshKnownHost` (Impact: 38.6), `ExtractEd25519PrivateKey` (Impact: 33.7), `ParseOpensshKnownHosts` (Impact: 32.9)

### 8. `libc/intrin/fds.c` (C) -> Cumulative Risk: **710.08**
- **Archetype:** `file_cluster_13` (Distance: 13.577 IQR)
- **Magnitude:** 280.4 | **LOC:** 198 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.0525%)
- **Heaviest Functions:** `__init_fds` (Impact: 65.2), `TokAtoi` (Impact: 11.3), `SetupWinStd` (Impact: 8.5)

### 9. `tool/viz/malloc_scalability.c` (C) -> Cumulative Risk: **709.92**
- **Archetype:** `file_cluster_4` (Distance: 13.956 IQR)
- **Magnitude:** 85.62 | **LOC:** 59 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.7598%)
- **Heaviest Functions:** `test` (Impact: 5.8), `worker` (Impact: 5.6), `main` (Impact: 5.5)

### 10. `libc/runtime/zipos-open.c` (C) -> Cumulative Risk: **709.53**
- **Archetype:** `file_cluster_13` (Distance: 13.141 IQR)
- **Magnitude:** 309.04 | **LOC:** 250 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.6169%)
- **Heaviest Functions:** `__zipos_load` (Impact: 57.0), `__zipos_open` (Impact: 26.6), `__zipos_mkfd` (Impact: 23.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `usr/share/ssl/root/amazon.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/share/ssl/root/certum.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/share/ssl/root/comodo.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/share/ssl/root/digicert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/share/ssl/root/geotrust.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/share/ssl/root/globalsign.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/share/ssl/root/godaddy.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/share/ssl/root/google.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/share/ssl/root/isrg.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/share/ssl/root/quovadis.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/share/ssl/root/redbean.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/share/ssl/root/starfield.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/share/ssl/root/usertrust.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `usr/share/ssl/root/verisign.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libc/stdckdint.h` (C | Tier 1.5 | 🚨 AI THREAT: 99.01%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.347 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.883 IQR)
- **Top Global Matches:** file_cluster_8: 13.347, file_cluster_11: 13.558, file_cluster_0: 13.598
- **Magnitude:** 4434.68 | **LOC:** 626 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (73.6978%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 80`, `args: 3`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 343`
* *Architecture:* `api: 141`, `import: 2`
* *Defense:* `safety: 21`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.326
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` type_traits, limits
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

### `libc/intrin/demangle.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.281 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.106 IQR)
- **Top Global Matches:** file_cluster_8: 14.281, file_cluster_11: 14.446, file_cluster_13: 14.45
- **Magnitude:** 4093.3 | **LOC:** 4488 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.8751%), Tech Debt (16.137%)
**Top Internal Functions/Classes:**
  * `demangle_read_uqname` (Impact: 289.2)
  * `demangle_push_type_qualifier` (Impact: 235.6)
  * `demangle_read_encoding_impl` (Impact: 200.3)
  * `demangle_read_expression_impl` (Impact: 142.1)
  * `demangle_read_function` (Impact: 98.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 820`, `structural_boundaries: 766`, `args: 90`, `func_start: 73`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 6`, `state_mutation: 1593`, `planned_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `api: 570`, `import: 4`
* *Defense:* `safety: 71`, `doc: 36`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` stdalign.h, stddef.h, stdint.h, stdbool.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/nesemu1.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.754 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.936 IQR)
- **Top Global Matches:** file_cluster_13: 14.754, file_cluster_8: 14.805, file_cluster_11: 14.947
- **Magnitude:** 2418.92 | **LOC:** 1869 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (94.9527%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ReadKeyboard` (Impact: 96.6)
  * `RenderingTick` (Impact: 75.6)
  * `PpuAccess` (Impact: 73.3)
  * `Access` (Impact: 52.4)
  * `Tick` (Impact: 38.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 401`, `structural_boundaries: 134`, `args: 57`, `func_start: 48`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 4`, `state_mutation: 1731`, `planned_debt: 3`, `duplicate_logic: 5`, `orphaned_logic: 12`
* *Architecture:* `io: 2`, `import: 46`
* *Defense:* `safety: 2`, `doc: 1`, `sync_locks: 6`, `immutability_locks: 14`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` vector, core.h, runtime.h, arraylist2.internal.h, stdio.h, itoa8.h, inttypes.h, knobs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libc/stdio/fmt.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.501 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.084 IQR)
- **Top Global Matches:** file_cluster_13: 14.501, file_cluster_8: 14.559, file_cluster_11: 14.642
- **Magnitude:** 2316.62 | **LOC:** 1561 | **CtrlFlow:** 83.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (97.5626%), Tech Debt (11.3884%)
**Top Internal Functions/Classes:**
  * `__fmt` (Impact: 813.9)
  * `__fmt_bround` (Impact: 86.7)
    * *Intent:* --precision;
  * `__fmt_fpiprec` (Impact: 34.0)
  * `__fmt_dfpbits` (Impact: 13.7)
  * `__fmt_atoi` (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 538`, `structural_boundaries: 103`, `args: 9`, `func_start: 10`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1209`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 116`, `import: 26`
* *Defense:* `safety: 9`, `doc: 2`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` itoa.h, errfuns.h, ctype.h, strwidth.h, utf16.h, fenv.h, serialize.h, str.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libc/vga/tty.greg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.698 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.865 IQR)
- **Top Global Matches:** file_cluster_8: 14.698, file_cluster_13: 14.777, file_cluster_11: 14.921
- **Magnitude:** 2295.02 | **LOC:** 1398 | **CtrlFlow:** 67.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.6031%), Tech Debt (9.1379%)
**Top Internal Functions/Classes:**
  * `TtySelectGraphicsRendition` (Impact: 183.1)
  * `_TtyWrite` (Impact: 130.6)
  * `TtyCsi` (Impact: 114.2)
  * `_StartTty` (Impact: 51.4)
  * `TtyCntrl` (Impact: 46.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 453`, `structural_boundaries: 220`, `args: 85`, `func_start: 85`, `class_start: 6`
* *Risk/State:* `state_mutation: 1027`, `orphaned_logic: 2`
* *Architecture:* `api: 134`, `import: 13`
* *Defense:* `safety: 53`, `doc: 6`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` itoa.h, errfuns.h, vga.internal.h, prot.h, thompike.h, ctype.h, map.h, safemacros.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tool/viz/printvideo.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.83 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.048 IQR)
- **Top Global Matches:** file_cluster_13: 13.83, file_cluster_8: 14.124, file_cluster_11: 14.225
- **Magnitude:** 1770.42 | **LOC:** 1460 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (95.0909%), Tech Debt (10.2761%)
**Top Internal Functions/Classes:**
  * `ReadKeyboard` (Impact: 295.5)
  * `DescribeAdjustments` (Impact: 58.4)
  * `DescribeAlgorithms` (Impact: 38.1)
  * `GetOpts` (Impact: 34.5)
  * `HasAdjustments` (Impact: 27.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 421`, `structural_boundaries: 217`, `args: 47`, `func_start: 51`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 9`, `state_mutation: 879`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 15`, `api: 114`, `import: 85`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 11`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 76):` runtime.h, ipproto.h, w.h, strwidth.h, f.h, kprintf.h, assert.h, stb_image_resize.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tool/net/redbean.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.994 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.447 IQR)
- **Top Global Matches:** file_cluster_13: 13.994, file_cluster_8: 14.409, file_cluster_11: 14.495
- **Magnitude:** 1731.72 | **LOC:** 7318 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (64.8006%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `StoreAsset` (Impact: 83.5)
    * *Intent:* #endif /** * @fileoverview redbean - single-file distributable web server * * redbean makes it possi...
  * `LuaSetCookie` (Impact: 40.2)
  * `LuaProgramTokenBucket` (Impact: 28.3)
  * `LuaSetHeader` (Impact: 24.9)
  * `StorePath` (Impact: 23.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 197`, `args: 12`, `func_start: 92`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 942`, `dead_code: 3`
* *Architecture:* `io: 15`, `api: 263`, `concurrency: 7`, `import: 122`
* *Defense:* `safety: 34`, `doc: 53`, `sync_locks: 1`, `immutability_locks: 48`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.406
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 99):` cosmo.h, runtime.h, inaddr.h, appendresourcereport.internal.h, ipproto.h, w.h, x509_crt.h, counters.inc...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `libc/intrin/kprintf.greg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.56 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.845 IQR)
- **Top Global Matches:** file_cluster_13: 14.56, file_cluster_11: 14.876, file_cluster_8: 14.914
- **Magnitude:** 1673.86 | **LOC:** 1172 | **CtrlFlow:** 88.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (88.6525%), Tech Debt (11.0581%)
**Top Internal Functions/Classes:**
  * `kformat` (Impact: 535.1)
    * *Intent:* #ifdef __x86_64__
  * `klog` (Impact: 30.6)
  * `kemitquote` (Impact: 11.8)
  * `_klog_serial` (Impact: 9.6)
  * `klogopen` (Impact: 7.8)
    * *Intent:* #elif defined(__aarch64__)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 40`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 893`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 126`, `concurrency: 6`, `import: 51`
* *Defense:* `safety: 12`, `doc: 10`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 48):` files.h, cosmo.h, runtime.h, vga.internal.h, runtime.h, nr.h, createfile.h, utf16.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tool/viz/life.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.527 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.012 IQR)
- **Top Global Matches:** file_cluster_13: 13.527, file_cluster_8: 13.611, file_cluster_11: 13.901
- **Magnitude:** 1511.66 | **LOC:** 1448 | **CtrlFlow:** 61.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (95.739%), Tech Debt (10.5054%)
**Top Internal Functions/Classes:**
  * `LoadFile` (Impact: 112.7)
  * `ReadKeyboard` (Impact: 102.6)
  * `OnMouse` (Impact: 62.3)
  * `RasterZoomed` (Impact: 41.6)
  * `GetOpts` (Impact: 30.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 207`, `args: 64`, `func_start: 80`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 686`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 6`, `api: 117`, `import: 55`
* *Defense:* `safety: 7`, `doc: 1`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 52):` itoa.h, mf.h, sw.h, nt2sysv.h, runtime.h, stdio.h, mb.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tool/cosmocc/bin/cosmoc++` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.585 IQR)
- **Top Global Matches:** file_cluster_4: 13.585, file_cluster_8: 13.902, file_cluster_11: 14.074
- **Magnitude:** 1438.9 | **LOC:** 748 | **CtrlFlow:** 97.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.3568%), Tech Debt (11.7272%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 819.2)
    * *Intent:* #!/bin/sh # fat cosmopolitan c/c++ compiler # https://github.com/jart/cosmopolitan # https://cosmo.z...
  * `__global_context__` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 552`, `structural_boundaries: 14`, `args: 35`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 118`, `state_mutation: 489`, `orphaned_logic: 2`
* *Architecture:* `io: 108`, `concurrency: 116`, `import: 1`
* *Defense:* `safety: 27`, `sync_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` files, code
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tool/cosmocc/bin/cosmocc` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.59 IQR)
- **Top Global Matches:** file_cluster_4: 13.59, file_cluster_8: 13.908, file_cluster_11: 14.079
- **Magnitude:** 1438.9 | **LOC:** 748 | **CtrlFlow:** 97.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (99.3568%), Tech Debt (11.7272%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 819.2)
    * *Intent:* #!/bin/sh # fat cosmopolitan c/c++ compiler # https://github.com/jart/cosmopolitan # https://cosmo.z...
  * `__global_context__` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 552`, `structural_boundaries: 14`, `args: 35`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 118`, `state_mutation: 489`, `orphaned_logic: 2`
* *Architecture:* `io: 108`, `concurrency: 116`, `import: 1`
* *Defense:* `safety: 27`, `sync_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` files, code
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `ctl/shared_ptr.h` (C) | Magnitude: 276.14 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 411, api: 128, state_mutation: 123, structural_boundaries: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `libc/integral/cxx.inc` (C) | Magnitude: 17.96 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 21, state_mutation: 15, structural_boundaries: 12, reflection_metaprogramming: 11
- `tool/scripts/renameheader` (SHELL) | Magnitude: 16.94 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: io: 14, structural_boundaries: 11, branch: 8, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tool/scripts/loc` (SHELL) | Magnitude: 1.42 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 25, structural_boundaries: 10, reflection_metaprogramming: 5, ipc_rpc_bridges: 5
- `libc/calls/struct/cpuset.h` (C) | Magnitude: 32.86 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: macros: 22, reflection_metaprogramming: 19, api: 13, bitwise_ops: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/sysinfo.c` (C) | Magnitude: 46.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, state_mutation: 21, debug_prints: 18, branch: 10
- `libc/tinymath/log10f.c` (C) | Magnitude: 83.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 58, indent_tabs: 39, branch: 8, structural_boundaries: 6
- `libc/calls/struct/stat.internal.h` (C) | Magnitude: 24.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, io: 10, api: 9, args: 8
- `libc/tinymath/emodl.h` (C) | Magnitude: 19.2 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, macros: 3, api: 2, state_mutation: 2
- `libc/sock/syscall_fd.internal.h` (C) | Magnitude: 28.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 24, args: 13, api: 13, immutability_locks: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tool/scripts/man2txt` (SHELL) | Magnitude: 12.44 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: io: 6, state_mutation: 6, branch: 3, structural_boundaries: 3
- `ape/apeinstall.sh` (SHELL) | Magnitude: 199.0 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 115, indent_spaces: 112, io: 102, state_mutation: 69

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `libc/thread/pthread_detach.c` (C) | Magnitude: 46.28 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, state_mutation: 12, import: 9, concurrency: 8
- `libc/proc/kill-nt.c` (C) | Magnitude: 96.44 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, state_mutation: 30, branch: 22, import: 21
- `net/turfwar/turfwar.c` (C) | Magnitude: 1334.72 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 862, state_mutation: 514, pointers: 415, structural_boundaries: 315
- `libc/mem/pthread_setspecific.c` (C) | Magnitude: 33.94 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 13, structural_boundaries: 11, import: 8
- `libc/runtime/clone.c` (C) | Magnitude: 272.92 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 132, state_mutation: 94, pointers: 91, doc: 78

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tool/net/definitions.lua` (LUA) | Magnitude: 3.56 | Delta: **0.188 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: sec_high_risk_execution: 141, doc: 77, sec_reflection_metaprogramming: 33, sec_dead_code: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `libc/calls/struct/flock.internal.h` (C) | Magnitude: 15.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 3, structural_boundaries: 2, safety_bypasses: 2, import: 2
- `libc/calls/struct/sched_param.internal.h` (C) | Magnitude: 15.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 3, structural_boundaries: 2, safety_bypasses: 2, import: 2
- `libc/calls/struct/sigaltstack.internal.h` (C) | Magnitude: 15.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 3, structural_boundaries: 2, safety_bypasses: 2, import: 2
- `libc/calls/struct/termios.internal.h` (C) | Magnitude: 15.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 3, structural_boundaries: 2, safety_bypasses: 2, import: 2
- `libc/intrin/describentoverlapped.h` (C) | Magnitude: 15.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 3, structural_boundaries: 2, safety_bypasses: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `libc/tinymath/csqrt.c` (C) | Magnitude: 63.52 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 37, state_mutation: 36, branch: 12, api: 11
- `libc/runtime/symbols.internal.h` (C) | Magnitude: 40.68 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: api: 25, indent_spaces: 14, structural_boundaries: 13, pointers: 10
- `libc/tinymath/ccoshl.c` (C) | Magnitude: 4.52 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: scientific: 3, ownership: 3, api: 2, structural_boundaries: 1
- `libc/tinymath/cexpl.c` (C) | Magnitude: 4.52 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: scientific: 3, ownership: 3, api: 2, structural_boundaries: 1
- `libc/tinymath/csinhl.c` (C) | Magnitude: 4.52 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: scientific: 3, ownership: 3, api: 2, structural_boundaries: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tool/cosmocc/bin/cosmocross` -> Churn: **100.0%** | Cog Load: 98.0594% | Debt: 18.9753%
- `tool/net/definitions.lua` -> Churn: **55.91%** | Cog Load: 5.0% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `libc/stdckdint.h` -> **Justine Tunney** (100.0% isolated ownership) | Magnitude: 4434.68
- `libc/intrin/demangle.c` -> **Justine Tunney** (100.0% isolated ownership) | Magnitude: 4093.3
- `examples/nesemu1.cc` -> **Justine Tunney** (100.0% isolated ownership) | Magnitude: 2418.92
- `libc/stdio/fmt.c` -> **Justine Tunney** (100.0% isolated ownership) | Magnitude: 2316.62
- `tool/viz/printvideo.c` -> **Justine Tunney** (100.0% isolated ownership) | Magnitude: 1770.42

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `libc/calls/struct/timeval.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `libc/str/str.h` -> **Severity: 1876.9** (Blast Radius: 18.769 * Doc Risk: 100.0%)
- `libc/math.h` -> **Severity: 1695.2** (Blast Radius: 16.952 * Doc Risk: 100.0%)
- `libc/runtime/runtime.h` -> **Severity: 836.4** (Blast Radius: 8.364 * Doc Risk: 100.0%)
- `libc/calls/calls.h` -> **Severity: 765.4** (Blast Radius: 7.654 * Doc Risk: 100.0%)
- `libc/thread/thread.h` -> **Severity: 716.5** (Blast Radius: 7.165 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
