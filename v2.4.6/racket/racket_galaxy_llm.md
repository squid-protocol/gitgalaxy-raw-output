# ARCHITECTURAL_BRIEF: racket
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/racket` |
| **Timestamp** | `2026-08-03T21:26:57.946740+00:00` |
| **Scan Duration** | `15.48s` |
| **Git Branch** | `master` |
| **Git Commit** | `afbc55a2ad3d98158c1cc8207be87936e3706c5a` |
| **Git Remote** | `https://github.com/racket/racket` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2990 malicious artifacts.

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
| Total Artifacts | 5828 |
| Analyzed Artifacts (Scanned) | 3249 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2579 |
| Total LOC | 689104 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 55.7% |
| Dominant Lang | SCHEME |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8273 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1916 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.4476 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 97 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SCHEME | 1894 | 425072 | 58.3% |
| C | 711 | 191305 | 21.9% |
| MAKEFILE | 199 | 21837 | 6.1% |
| PLAINTEXT | 123 | 1 | 3.8% |
| M4 | 82 | 15985 | 2.5% |
| ASSEMBLY | 59 | 16491 | 1.8% |
| MARKDOWN | 45 | 0 | 1.4% |
| SHELL | 35 | 8828 | 1.1% |
| CPP | 25 | 2342 | 0.8% |
| BATCH | 12 | 334 | 0.4% |
| HTML | 10 | 2261 | 0.3% |
| PYTHON | 9 | 1033 | 0.3% |
| CSHARP | 9 | 879 | 0.3% |
| CSS | 8 | 172 | 0.2% |
| XML | 7 | 0 | 0.2% |
| APEX | 7 | 1137 | 0.2% |
| YAML | 5 | 440 | 0.2% |
| JAVASCRIPT | 4 | 792 | 0.1% |
| PERL | 2 | 182 | 0.1% |
| PHP | 2 | 4 | 0.1% |
| POWERSHELL | 1 | 9 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.746`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2864 | 88.2% |
| file_cluster_13 | 154 | 4.7% |
| file_cluster_9 | 21 | 0.6% |
| file_cluster_12 | 18 | 0.6% |
| file_cluster_11 | 7 | 0.2% |
| file_cluster_17 | 5 | 0.2% |
| file_cluster_0 | 5 | 0.2% |
| file_cluster_15 | 2 | 0.1% |
| file_cluster_4 | 2 | 0.1% |
| Unknown | 1 | 0.0% |
| file_cluster_6 | 1 | 0.0% |
| file_cluster_7 | 1 | 0.0% |
| file_cluster_2 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 167 | 5.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2579*

**Composition by Extension & Reason:**
- `.rkt`: 969x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 65x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Unsupported Format (.undeterminable)
- `.scrbl`: 481x Excluded (Unsupported Extension: '.scrbl'), 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Unsupported Format (.scrbl)
- `.rktl`: 160x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 31x Excluded (Unsupported Extension: '.rktl'), 2x Unsupported Format (.rktl)
- `.zuo`: 159x Unsupported Format (.zuo)
- `no_extension`: 86x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 40x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 9058 LOC)
- `.rktd`: 55x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 46x Unsupported Format (.patch)
- `.ms`: 37x Unsupported Format (.ms)
- `.vcxproj`: 32x Unsupported Format (.vcxproj)
- `.stex`: 27x Unsupported Format (.stex)
- `.txt`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4297 LOC), 1x Excluded (Monolithic Amalgamation: 40576 LOC exceeds safe regex boundaries)
- `.aux`: 20x Unsupported Format (.aux)
- `.png`: 18x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 21.4 | 10.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 14.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.1 | 2.3 | 2.3 |
| API Exposure | 0.0 | 19.1 | 2.8 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 88.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.4 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 78.7 | 1.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 43.8 | 28.1 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.6 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `racket/src/bc/foreign/foreign.rktc` (Hits: 550)
- `racket/src/ChezScheme/zlib/configure` (Hits: 391)
- `racket/src/ChezScheme/configure` (Hits: 155)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **schpriv.h** (`racket/src/bc/src/schpriv.h`) — 59 inbound connections
2. **ffi_common.h** (`racket/src/bc/foreign/libffi/include/ffi_common.h`) — 47 inbound connections
3. **system.h** (`racket/src/ChezScheme/c/system.h`) — 34 inbound connections
4. **lz4.h** (`racket/src/ChezScheme/lz4/lib/lz4.h`) — 33 inbound connections
5. **schmach.h** (`racket/src/bc/src/schmach.h`) — 33 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **newgc.c** (`racket/src/bc/gc2/newgc.c`) — 25 outbound dependencies
2. **zuo.c** (`racket/src/zuo/zuo.c`) — 25 outbound dependencies
3. **expeditor.c** (`racket/src/ChezScheme/c/expeditor.c`) — 24 outbound dependencies
4. **scheme.h** (`racket/src/bc/include/scheme.h`) — 24 outbound dependencies
5. **lightning.h** (`racket/src/bc/src/lightning/lightning.h`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `user_read_result` (@ `racket/src/bc/src/portfun.c`) -> Impact: **13005.5** | LOC: 1943
  * *Intent:* #define MAX_USER_INPUT_REUSE_SIZE 1024 /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */ /* Result checking */ /* * * * * * * * * * ...
- `regmatch` (@ `racket/src/bc/src/regexp.c`) -> Impact: **9323.2** | LOC: 1944
- `string_to_from_locale` (@ `racket/src/bc/src/string.c`) -> Impact: **6707.7** | LOC: 2094
- `generate_float_point_arith` (@ `racket/src/bc/src/jitarith.c`) -> Impact: **5485.0** | LOC: 1066
- `evt_struct_is_ready` (@ `racket/src/bc/src/struct.c`) -> Impact: **4318.1** | LOC: 1539
- `scheme_do_eval` (@ `racket/src/bc/src/eval.c`) -> Impact: **4297.0** | LOC: 1311
- `collect_now` (@ `racket/src/bc/gc2/newgc.c`) -> Impact: **4191.4** | LOC: 1867
- `can_direct_native` (@ `racket/src/bc/src/jitcall.c`) -> Impact: **3337.2** | LOC: 664
- `Anonymous_Block_[Truncated]` (@ `racket/src/bc/foreign/foreign.rktc`) -> Impact: **2997.2** | LOC: 3523
- `generate_inlined_struct_op` (@ `racket/src/bc/src/jitinline.c`) -> Impact: **2844.5** | LOC: 875

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `HAMT_SUBSET_OF` (@ `racket/src/bc/src/hamt_subset.inc`) -> **O(2^N) [Recursive]**
- `make-a-seq` (@ `racket/collects/compiler/private/xform.rkt`) -> **O(2^N) [Recursive]**
- `trans` (@ `racket/collects/launcher/launcher.rkt`) -> **O(2^N) [Recursive]**
- `build-string-from-pair` (@ `racket/collects/syntax/to-string.rkt`) -> **O(2^N) [Recursive]**
- `list-xtail` (@ `racket/src/ChezScheme/s/np-info.ss`) -> **O(2^N) [Recursive]**
- `fxwraparound` (@ `racket/src/ChezScheme/s/reboot.ss`) -> **O(2^N) [Recursive]**
- `get-accum` (@ `racket/src/expander/read/graph.rkt`) -> **O(2^N) [Recursive]**
- `read-struct` (@ `racket/src/expander/read/struct.rkt`) -> **O(2^N) [Recursive]**
- `test_ratio` (@ `racket/src/ChezScheme/lz4/tests/test-lz4-list.py`) -> **O(2^N) [Recursive]**
- `double_check` (@ `racket/src/ChezScheme/lz4/tests/test-lz4-speed.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block_[Truncated]` (@ `racket/src/bc/foreign/foreign.rktc`) -> DB Complexity: **1335**
- `hello_[Truncated]` (@ `racket/src/ChezScheme/zlib/configure`) -> DB Complexity: **1081**
- `regmatch` (@ `racket/src/bc/src/regexp.c`) -> DB Complexity: **693**
- `string_to_from_locale` (@ `racket/src/bc/src/string.c`) -> DB Complexity: **689**
- `Anonymous_Block_[Truncated]` (@ `racket/src/ChezScheme/configure`) -> DB Complexity: **503**
- `user_read_result` (@ `racket/src/bc/src/portfun.c`) -> DB Complexity: **488**
  * *Intent:* #define MAX_USER_INPUT_REUSE_SIZE 1024 /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */ /* Result checking */ /* * * * * * * * * * ...
- `evt_struct_is_ready` (@ `racket/src/bc/src/struct.c`) -> DB Complexity: **388**
- `collect_now` (@ `racket/src/bc/gc2/newgc.c`) -> DB Complexity: **374**
- `scheme_do_eval` (@ `racket/src/bc/src/eval.c`) -> DB Complexity: **356**
- `main` (@ `racket/src/bc/foreign/libffi/testsuite/libffi.bhaible/test-callback.c`) -> DB Complexity: **351**
  * *Intent:* /*

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `racket/src/ChezScheme/s` | 121 | 862461.1 | 12.14% | 3.37% |
| `racket/collects/racket/private` | 112 | 187387.75 | 17.23% | 4.24% |
| `racket/src/bc/src` | 153 | 168058.12 | 47.7% | 15.22% |
| `racket/collects/racket` | 103 | 143488.76 | 16.62% | 1.56% |
| `racket/collects/racket/contract/private` | 52 | 139344.28 | 12.94% | 3.5% |
| `racket/src/cs/rumble` | 66 | 130242.29 | 13.69% | 1.88% |
| `pkgs/racket-benchmarks/tests/racket/benchmarks/common` | 72 | 127078.3 | 13.67% | 0.0% |
| `racket/collects/syntax/parse/private` | 24 | 62240.4 | 17.13% | 23.45% |
| `racket/collects/setup` | 31 | 54214.29 | 9.61% | 4.34% |
| `racket/src/schemify` | 53 | 47773.38 | 13.67% | 0.47% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.github/scripts/adjust-sarif-tool.sh` -> **100.0%** Exposure
- `.github/scripts/matting.sh` -> **100.0%** Exposure
- `racket/src/ChezScheme/lz4/contrib/gen_manual/gen-lz4-manual.sh` -> **100.0%** Exposure
- `racket/src/ChezScheme/lz4/ossfuzz/ossfuzz.sh` -> **100.0%** Exposure
- `racket/src/ChezScheme/lz4/ossfuzz/travisoss.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.github/scripts/matting.sh` -> **100.0%** Exposure
- `racket/src/ChezScheme/configure` -> **100.0%** Exposure
- `racket/src/ChezScheme/lz4/contrib/gen_manual/gen-lz4-manual.sh` -> **100.0%** Exposure
- `racket/src/ChezScheme/makefiles/installsh` -> **100.0%** Exposure
- `racket/src/ChezScheme/maketarball` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `racket/src/zuo/zuo.c` -> **109** Orphaned Functions | **6** Duplicates
- `racket/src/ChezScheme/mats/foreign2.c` -> **89** Orphaned Functions | **0** Duplicates
- `racket/src/bc/src/mzrt.c` -> **5** Orphaned Functions | **53** Duplicates
- `racket/src/bc/src/eval.c` -> **52** Orphaned Functions | **0** Duplicates
- `racket/src/ChezScheme/mats/foreign3.c` -> **47** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`racket/src/start/config.inc`** -> AI Confidence: **99.48%**
2. **`racket/src/ChezScheme/lz4/programs/lz4cli.c`** -> AI Confidence: **99.48%**
3. **`racket/src/ChezScheme/lz4/tests/frametest.c`** -> AI Confidence: **99.48%**
4. **`racket/src/ChezScheme/zlib/contrib/minizip/miniunz.c`** -> AI Confidence: **99.48%**
5. **`racket/src/ChezScheme/zlib/contrib/minizip/minizip.c`** -> AI Confidence: **99.48%**
6. **`racket/src/ChezScheme/zlib/examples/gznorm.c`** -> AI Confidence: **99.48%**
7. **`racket/src/ChezScheme/zlib/test/minigzip.c`** -> AI Confidence: **99.48%**
8. **`racket/src/ChezScheme/zlib/zconf.h`** -> AI Confidence: **99.48%**
9. **`racket/src/bc/foreign/libffi/src/mips/ffi.c`** -> AI Confidence: **99.48%**
10. **`racket/src/bc/foreign/libffi/testsuite/libffi.call/ffitest.h`** -> AI Confidence: **99.48%**
11. **`racket/src/bc/src/eval.c`** -> AI Confidence: **99.48%**
12. **`racket/src/bc/src/print.c`** -> AI Confidence: **99.48%**
13. **`racket/src/bc/src/regexp.c`** -> AI Confidence: **99.48%**
14. **`racket/src/bc/src/string.c`** -> AI Confidence: **99.48%**
15. **`racket/src/start/start.c`** -> AI Confidence: **99.48%**
16. **`racket/src/ChezScheme/c/gc.c`** -> AI Confidence: **99.43%**
17. **`racket/src/ChezScheme/zlib/zutil.h`** -> AI Confidence: **99.43%**
18. **`racket/src/ChezScheme/zlib/zconf.h.in`** -> AI Confidence: **99.42%**
19. **`pkgs/plt-services/meta/props`** -> AI Confidence: **99.39%**
20. **`racket/src/ChezScheme/lz4/examples/compress_functions.c`** -> AI Confidence: **99.39%**
21. **`racket/src/ChezScheme/lz4/tests/checkFrame.c`** -> AI Confidence: **99.39%**
22. **`racket/src/ChezScheme/lz4/tests/fullbench.c`** -> AI Confidence: **99.39%**
23. **`racket/src/ChezScheme/lz4/tests/fuzzer.c`** -> AI Confidence: **99.39%**
24. **`racket/src/ChezScheme/zlib/contrib/minizip/unzip.c`** -> AI Confidence: **99.39%**
25. **`racket/src/ChezScheme/zlib/contrib/minizip/zip.c`** -> AI Confidence: **99.39%**
26. **`racket/src/ChezScheme/zlib/contrib/untgz/untgz.c`** -> AI Confidence: **99.39%**
27. **`racket/src/ChezScheme/zlib/examples/gun.c`** -> AI Confidence: **99.39%**
28. **`racket/src/bc/sgc/sgc.c`** -> AI Confidence: **99.39%**
29. **`racket/src/bc/src/dynext.c`** -> AI Confidence: **99.39%**
30. **`racket/src/bc/src/read.c`** -> AI Confidence: **99.39%**
31. **`racket/src/rktio/rktio_fd.c`** -> AI Confidence: **99.39%**
32. **`racket/src/rktio/rktio_flock.c`** -> AI Confidence: **99.39%**
33. **`racket/src/rktio/rktio_fs.c`** -> AI Confidence: **99.39%**
34. **`racket/src/rktio/rktio_ltps.c`** -> AI Confidence: **99.39%**
35. **`racket/src/zuo/zuo.c`** -> AI Confidence: **99.39%**
36. **`racket/src/ChezScheme/c/scheme.c`** -> AI Confidence: **99.35%**
37. **`racket/src/bc/src/salloc.c`** -> AI Confidence: **99.35%**
38. **`racket/src/ChezScheme/c/compress-io.c`** -> AI Confidence: **99.34%**
39. **`racket/src/ChezScheme/c/main.c`** -> AI Confidence: **99.34%**
40. **`racket/src/ChezScheme/c/segment.c`** -> AI Confidence: **99.34%**
41. **`racket/src/ChezScheme/lz4/examples/HCStreaming_ringBuffer.c`** -> AI Confidence: **99.34%**
42. **`racket/src/ChezScheme/zlib/contrib/minizip/mztools.c`** -> AI Confidence: **99.34%**
43. **`racket/src/ChezScheme/zlib/gzguts.h`** -> AI Confidence: **99.34%**
44. **`racket/src/ChezScheme/zlib/infback.c`** -> AI Confidence: **99.34%**
45. **`racket/src/bc/src/hash.c`** -> AI Confidence: **99.34%**
46. **`racket/src/bc/src/jitarith.c`** -> AI Confidence: **99.34%**
47. **`racket/src/bc/src/jitcall.c`** -> AI Confidence: **99.34%**
48. **`racket/src/bc/src/optimize.c`** -> AI Confidence: **99.34%**
49. **`racket/src/bc/src/sfs.c`** -> AI Confidence: **99.34%**
50. **`racket/src/bc/src/validate.c`** -> AI Confidence: **99.34%**
51. **`racket/src/rktio/rktio_cpu.c`** -> AI Confidence: **99.34%**
52. **`racket/src/rktio/rktio_syslog.c`** -> AI Confidence: **99.34%**
53. **`racket/src/mzcom/mzcom.cxx`** -> AI Confidence: **99.34%**
54. **`racket/src/ChezScheme/examples/crepl.c`** -> AI Confidence: **99.32%**
55. **`racket/src/bc/foreign/libffi/src/m32r/ffi.c`** -> AI Confidence: **99.32%**
56. **`racket/src/bc/foreign/libffi/src/powerpc/ffi_linux64.c`** -> AI Confidence: **99.32%**
57. **`racket/src/bc/foreign/libffi/src/powerpc/ffi_sysv.c`** -> AI Confidence: **99.32%**
58. **`racket/src/bc/foreign/libffi/src/sh/ffi.c`** -> AI Confidence: **99.32%**
59. **`racket/src/bc/src/char.c`** -> AI Confidence: **99.32%**
60. **`racket/src/bc/src/linklet.c`** -> AI Confidence: **99.32%**
61. **`racket/src/bc/src/mzmarksrc.c`** -> AI Confidence: **99.32%**
62. **`racket/src/ChezScheme/lz4/tests/test-lz4-speed.py`** -> AI Confidence: **99.31%**
63. **`racket/src/ChezScheme/lz4/tests/test-lz4-versions.py`** -> AI Confidence: **99.31%**
64. **`racket/src/ChezScheme/c/expeditor.c`** -> AI Confidence: **99.31%**
65. **`racket/src/ChezScheme/c/io.c`** -> AI Confidence: **99.31%**
66. **`racket/src/ChezScheme/c/new-io.c`** -> AI Confidence: **99.31%**
67. **`racket/src/ChezScheme/c/self-exe.c`** -> AI Confidence: **99.31%**
68. **`racket/src/ChezScheme/c/stats.c`** -> AI Confidence: **99.31%**
69. **`racket/src/ChezScheme/lz4/lib/lz4.c`** -> AI Confidence: **99.31%**
70. **`racket/src/ChezScheme/lz4/lib/lz4frame.c`** -> AI Confidence: **99.31%**
71. **`racket/src/ChezScheme/lz4/ossfuzz/compress_frame_fuzzer.c`** -> AI Confidence: **99.31%**
72. **`racket/src/ChezScheme/lz4/ossfuzz/compress_fuzzer.c`** -> AI Confidence: **99.31%**
73. **`racket/src/ChezScheme/lz4/ossfuzz/compress_hc_fuzzer.c`** -> AI Confidence: **99.31%**
74. **`racket/src/ChezScheme/lz4/programs/bench.c`** -> AI Confidence: **99.31%**
75. **`racket/src/ChezScheme/lz4/programs/lz4io.c`** -> AI Confidence: **99.31%**
76. **`racket/src/ChezScheme/lz4/tests/roundTripTest.c`** -> AI Confidence: **99.31%**
77. **`racket/src/ChezScheme/zlib/examples/gzlog.c`** -> AI Confidence: **99.31%**
78. **`racket/src/bc/foreign/libffi/src/aarch64/ffi.c`** -> AI Confidence: **99.31%**
79. **`racket/src/bc/foreign/libffi/src/arm/ffi.c`** -> AI Confidence: **99.31%**
80. **`racket/src/bc/foreign/libffi/src/closures.c`** -> AI Confidence: **99.31%**
81. **`racket/src/bc/foreign/libffi/src/dlmalloc.c`** -> AI Confidence: **99.31%**
82. **`racket/src/bc/foreign/libffi/src/kvx/ffi.c`** -> AI Confidence: **99.31%**
83. **`racket/src/bc/foreign/libffi/src/m68k/ffi.c`** -> AI Confidence: **99.31%**
84. **`racket/src/bc/foreign/libffi/src/tile/ffi.c`** -> AI Confidence: **99.31%**
85. **`racket/src/bc/foreign/libffi/src/x86/ffi64.c`** -> AI Confidence: **99.31%**
86. **`racket/src/bc/foreign/libffi/testsuite/libffi.bhaible/test-call.c`** -> AI Confidence: **99.31%**
87. **`racket/src/bc/gc2/newgc.c`** -> AI Confidence: **99.31%**
88. **`racket/src/bc/main.c`** -> AI Confidence: **99.31%**
89. **`racket/src/bc/src/future.c`** -> AI Confidence: **99.31%**
90. **`racket/src/bc/src/jit.c`** -> AI Confidence: **99.31%**
91. **`racket/src/bc/src/number.c`** -> AI Confidence: **99.31%**
92. **`racket/src/bc/src/port.c`** -> AI Confidence: **99.31%**
93. **`racket/src/bc/src/thread.c`** -> AI Confidence: **99.31%**
94. **`racket/src/bc/src/unwind/libunwind.c`** -> AI Confidence: **99.31%**
95. **`racket/src/cs/c/boot.c`** -> AI Confidence: **99.31%**
96. **`racket/src/cs/c/main.c`** -> AI Confidence: **99.31%**
97. **`racket/src/rktio/rktio_convert.c`** -> AI Confidence: **99.31%**
98. **`racket/src/rktio/rktio_file.c`** -> AI Confidence: **99.31%**
99. **`racket/src/rktio/rktio_fs_change.c`** -> AI Confidence: **99.31%**
100. **`racket/src/rktio/rktio_network.c`** -> AI Confidence: **99.31%**
101. **`racket/src/rktio/rktio_poll_set.c`** -> AI Confidence: **99.31%**
102. **`racket/src/rktio/rktio_process.c`** -> AI Confidence: **99.31%**
103. **`racket/src/rktio/rktio_time.c`** -> AI Confidence: **99.31%**
104. **`racket/src/start/ustart.c`** -> AI Confidence: **99.31%**
105. **`.github/scripts/matting.sh`** -> AI Confidence: **99.29%**
106. **`.github/scripts/run-racket-tests.sh`** -> AI Confidence: **99.29%**
107. **`racket/src/ChezScheme/lz4/contrib/gen_manual/gen-lz4-manual.sh`** -> AI Confidence: **99.29%**
108. **`racket/src/ChezScheme/lz4/ossfuzz/travisoss.sh`** -> AI Confidence: **99.29%**
109. **`racket/src/ChezScheme/makefiles/installsh`** -> AI Confidence: **99.29%**
110. **`racket/src/bc/src/sysname`** -> AI Confidence: **99.29%**
111. **`racket/src/ChezScheme/s/default.def`** -> AI Confidence: **99.29%**
112. **`racket/src/ChezScheme/s/nt.def`** -> AI Confidence: **99.29%**
113. **`racket/src/ChezScheme/zlib/contrib/puff/Makefile`** -> AI Confidence: **99.29%**
114. **`racket/src/ChezScheme/zlib/old/os2/zlib.def`** -> AI Confidence: **99.29%**
115. **`racket/src/bc/cmdline.inc`** -> AI Confidence: **99.29%**
116. **`racket/src/bc/sgc/collect.inc`** -> AI Confidence: **99.29%**
117. **`racket/src/bc/src/bgnfloat.inc`** -> AI Confidence: **99.29%**
118. **`racket/src/bc/src/pc_keys.inc`** -> AI Confidence: **99.29%**
119. **`racket/src/bc/src/print_vector.inc`** -> AI Confidence: **99.29%**
120. **`racket/src/bc/src/ratfloat.inc`** -> AI Confidence: **99.29%**
121. **`racket/src/bc/src/schemex.inc`** -> AI Confidence: **99.29%**
122. **`racket/src/bc/src/schround.inc`** -> AI Confidence: **99.29%**
123. **`racket/src/start/cmdl_to_argv.inc`** -> AI Confidence: **99.29%**
124. **`pkgs/base/info.rkt`** -> AI Confidence: **99.29%**
125. **`pkgs/racket-benchmarks/mini-bar-plot/bm.rkt`** -> AI Confidence: **99.29%**
126. **`pkgs/racket-benchmarks/tests/racket/benchmarks/common/mit-prelude.sch`** -> AI Confidence: **99.29%**
127. **`pkgs/racket-benchmarks/tests/racket/benchmarks/common/nfa.sch`** -> AI Confidence: **99.29%**
128. **`pkgs/racket-benchmarks/tests/racket/benchmarks/common/sboyer.sch`** -> AI Confidence: **99.29%**
129. **`pkgs/racket-benchmarks/tests/racket/benchmarks/common/takr.sch`** -> AI Confidence: **99.29%**
130. **`pkgs/racket-benchmarks/tests/racket/benchmarks/common/takr2.sch`** -> AI Confidence: **99.29%**
131. **`pkgs/racket-benchmarks/tests/racket/benchmarks/common/wrap-common.rkt`** -> AI Confidence: **99.29%**
132. **`pkgs/racket-benchmarks/tests/racket/benchmarks/common/wrap.rkt`** -> AI Confidence: **99.29%**
133. **`pkgs/racket-benchmarks/tests/racket/benchmarks/hash/summary.rkt`** -> AI Confidence: **99.29%**
134. **`pkgs/racket-doc/ffi/examples/magick.rkt`** -> AI Confidence: **99.29%**
135. **`pkgs/racket-doc/ffi/examples/tcl.rkt`** -> AI Confidence: **99.29%**
136. **`pkgs/racket-doc/ffi/examples/use-tcl.rkt`** -> AI Confidence: **99.29%**
137. **`pkgs/racket-doc/ffi/examples/xosd.rkt`** -> AI Confidence: **99.29%**
138. **`pkgs/racket-doc/scribblings/guide/arith.rkt`** -> AI Confidence: **99.29%**
139. **`pkgs/racket-doc/scribblings/guide/contracts/examples/1b.rkt`** -> AI Confidence: **99.29%**
140. **`pkgs/racket-doc/scribblings/guide/contracts/examples/2.rkt`** -> AI Confidence: **99.29%**
141. **`pkgs/racket-doc/scribblings/guide/contracts/examples/3.rkt`** -> AI Confidence: **99.29%**
142. **`pkgs/racket-doc/scribblings/guide/contracts/examples/ho-version2.rkt`** -> AI Confidence: **99.29%**
143. **`pkgs/racket-doc/scribblings/guide/contracts/examples/ho-version2a.rkt`** -> AI Confidence: **99.29%**
144. **`pkgs/racket-doc/scribblings/guide/contracts/examples/ho-version3.rkt`** -> AI Confidence: **99.29%**
145. **`pkgs/racket-doc/scribblings/guide/contracts/examples/ho-version3a.rkt`** -> AI Confidence: **99.29%**
146. **`pkgs/racket-doc/scribblings/guide/contracts/examples/ho-version3b.rkt`** -> AI Confidence: **99.29%**
147. **`pkgs/racket-doc/scribblings/guide/contracts/examples/ho-version4.rkt`** -> AI Confidence: **99.29%**
148. **`pkgs/racket-doc/scribblings/guide/literal-main-get-info.rkt`** -> AI Confidence: **99.29%**
149. **`pkgs/racket-doc/scribblings/guide/literal-main-language-info.rkt`** -> AI Confidence: **99.29%**
150. **`pkgs/racket-doc/scribblings/reference/match-grammar.rkt`** -> AI Confidence: **99.29%**
151. **`pkgs/racket-doc/scribblings/reference/mz.rkt`** -> AI Confidence: **99.29%**
152. **`pkgs/racket-doc/scribblings/reference/prog-steps.rkt`** -> AI Confidence: **99.29%**
153. **`pkgs/racket-doc/scribblings/reference/rx.rkt`** -> AI Confidence: **99.29%**
154. **`pkgs/racket-index-exe/help/installer.rkt`** -> AI Confidence: **99.29%**
155. **`pkgs/racket-index/help/info.rkt`** -> AI Confidence: **99.29%**
156. **`pkgs/racket-index/help/private/command.rkt`** -> AI Confidence: **99.29%**
157. **`pkgs/racket-index/help/private/family.rkt`** -> AI Confidence: **99.29%**
158. **`pkgs/racket-index/help/private/search.rkt`** -> AI Confidence: **99.29%**
159. **`pkgs/racket-index/scribblings/main/config.rkt`** -> AI Confidence: **99.29%**
160. **`pkgs/racket-index/scribblings/main/contents.rkt`** -> AI Confidence: **99.29%**
161. **`pkgs/racket-index/scribblings/main/private/family.rkt`** -> AI Confidence: **99.29%**
162. **`pkgs/racket-index/scribblings/main/private/index-scope.rkt`** -> AI Confidence: **99.29%**
163. **`pkgs/racket-index/scribblings/main/private/local-redirect.rkt`** -> AI Confidence: **99.29%**
164. **`pkgs/racket-index/scribblings/main/private/manuals.rkt`** -> AI Confidence: **99.29%**
165. **`pkgs/racket-index/scribblings/main/private/notice.rkt`** -> AI Confidence: **99.29%**
166. **`pkgs/racket-index/scribblings/main/private/release.rkt`** -> AI Confidence: **99.29%**
167. **`pkgs/racket-index/scribblings/main/private/utils.rkt`** -> AI Confidence: **99.29%**
168. **`pkgs/racket-index/setup/private/doc-path.rkt`** -> AI Confidence: **99.29%**
169. **`pkgs/racket-index/setup/private/validate-scribblings.rkt`** -> AI Confidence: **99.29%**
170. **`pkgs/racket-index/setup/scribble.rkt`** -> AI Confidence: **99.29%**
171. **`pkgs/racket-index/setup/xref.rkt`** -> AI Confidence: **99.29%**
172. **`pkgs/racket-test/tests/utils/sexp-diff.rkt`** -> AI Confidence: **99.29%**
173. **`pkgs/scheme-doc/info.rkt`** -> AI Confidence: **99.29%**
174. **`racket/collects/acks/acks.rkt`** -> AI Confidence: **99.29%**
175. **`racket/collects/compiler/cm-accomplice.rkt`** -> AI Confidence: **99.29%**
176. **`racket/collects/compiler/compilation-path.rkt`** -> AI Confidence: **99.29%**
177. **`racket/collects/compiler/compile-file.rkt`** -> AI Confidence: **99.29%**
178. **`racket/collects/compiler/depend.rkt`** -> AI Confidence: **99.29%**
179. **`racket/collects/compiler/embed.rkt`** -> AI Confidence: **99.29%**
180. **`racket/collects/compiler/find-exe.rkt`** -> AI Confidence: **99.29%**
181. **`racket/collects/compiler/module-suffix.rkt`** -> AI Confidence: **99.29%**
182. **`racket/collects/compiler/option.rkt`** -> AI Confidence: **99.29%**
183. **`racket/collects/compiler/private/cm-file.rkt`** -> AI Confidence: **99.29%**
184. **`racket/collects/compiler/private/cm-hash.rkt`** -> AI Confidence: **99.29%**
185. **`racket/collects/compiler/private/cm-log.rkt`** -> AI Confidence: **99.29%**
186. **`racket/collects/compiler/private/cm-minimal.rkt`** -> AI Confidence: **99.29%**
187. **`racket/collects/compiler/private/cm-path.rkt`** -> AI Confidence: **99.29%**
188. **`racket/collects/compiler/private/cm-security.rkt`** -> AI Confidence: **99.29%**
189. **`racket/collects/compiler/private/collects-path.rkt`** -> AI Confidence: **99.29%**
190. **`racket/collects/compiler/private/recompile-cache.rkt`** -> AI Confidence: **99.29%**
191. **`racket/collects/compiler/private/write-perm.rkt`** -> AI Confidence: **99.29%**
192. **`racket/collects/db/private/generic/common.rkt`** -> AI Confidence: **99.29%**
193. **`racket/collects/db/private/generic/ffi-common.rkt`** -> AI Confidence: **99.29%**
194. **`racket/collects/db/private/generic/prepared.rkt`** -> AI Confidence: **99.29%**
195. **`racket/collects/db/private/sqlite3/dbsystem.rkt`** -> AI Confidence: **99.29%**
196. **`racket/collects/db/private/sqlite3/ffi.rkt`** -> AI Confidence: **99.29%**
197. **`racket/collects/db/private/sqlite3/main.rkt`** -> AI Confidence: **99.29%**
198. **`racket/collects/dynext/file.rkt`** -> AI Confidence: **99.29%**
199. **`racket/collects/dynext/filename-version.rkt`** -> AI Confidence: **99.29%**
200. **`racket/collects/ffi/unsafe/alloc.rkt`** -> AI Confidence: **99.29%**
201. **`racket/collects/ffi/unsafe/atomic.rkt`** -> AI Confidence: **99.29%**
202. **`racket/collects/ffi/unsafe/com.rkt`** -> AI Confidence: **99.29%**
203. **`racket/collects/ffi/unsafe/custodian.rkt`** -> AI Confidence: **99.29%**
204. **`racket/collects/ffi/unsafe/os-async-channel.rkt`** -> AI Confidence: **99.29%**
205. **`racket/collects/ffi/unsafe/port.rkt`** -> AI Confidence: **99.29%**
206. **`racket/collects/ffi/unsafe/private/win32.rkt`** -> AI Confidence: **99.29%**
207. **`racket/collects/ffi/unsafe/try-atomic.rkt`** -> AI Confidence: **99.29%**
208. **`racket/collects/ffi/unsafe/vm.rkt`** -> AI Confidence: **99.29%**
209. **`racket/collects/ffi/vector.rkt`** -> AI Confidence: **99.29%**
210. **`racket/collects/ffi/winapi.rkt`** -> AI Confidence: **99.29%**
211. **`racket/collects/file/cache.rkt`** -> AI Confidence: **99.29%**
212. **`racket/collects/file/convertible.rkt`** -> AI Confidence: **99.29%**
213. **`racket/collects/file/glob.rkt`** -> AI Confidence: **99.29%**
214. **`racket/collects/file/private/check-path.rkt`** -> AI Confidence: **99.29%**
215. **`racket/collects/file/private/strip-prefix.rkt`** -> AI Confidence: **99.29%**
216. **`racket/collects/file/resource.rkt`** -> AI Confidence: **99.29%**
217. **`racket/collects/file/tar.rkt`** -> AI Confidence: **99.29%**
218. **`racket/collects/file/untar.rkt`** -> AI Confidence: **99.29%**
219. **`racket/collects/file/untgz.rkt`** -> AI Confidence: **99.29%**
220. **`racket/collects/file/zip.rkt`** -> AI Confidence: **99.29%**
221. **`racket/collects/json/main.rkt`** -> AI Confidence: **99.29%**
222. **`racket/collects/launcher/launcher.rkt`** -> AI Confidence: **99.29%**
223. **`racket/collects/net/http-client.rkt`** -> AI Confidence: **99.29%**
224. **`racket/collects/net/osx-ssl.rkt`** -> AI Confidence: **99.29%**
225. **`racket/collects/net/uri-codec.rkt`** -> AI Confidence: **99.29%**
226. **`racket/collects/net/url-connect.rkt`** -> AI Confidence: **99.29%**
227. **`racket/collects/net/url-exception.rkt`** -> AI Confidence: **99.29%**
228. **`racket/collects/net/url-string.rkt`** -> AI Confidence: **99.29%**
229. **`racket/collects/net/url.rkt`** -> AI Confidence: **99.29%**
230. **`racket/collects/net/win32-ssl.rkt`** -> AI Confidence: **99.29%**
231. **`racket/collects/openssl/libcrypto.rkt`** -> AI Confidence: **99.29%**
232. **`racket/collects/openssl/libssl.rkt`** -> AI Confidence: **99.29%**
233. **`racket/collects/pkg/db.rkt`** -> AI Confidence: **99.29%**
234. **`racket/collects/pkg/dirs-catalog.rkt`** -> AI Confidence: **99.29%**
235. **`racket/collects/pkg/main.rkt`** -> AI Confidence: **99.29%**
236. **`racket/collects/pkg/name.rkt`** -> AI Confidence: **99.29%**
237. **`racket/collects/pkg/path.rkt`** -> AI Confidence: **99.29%**
238. **`racket/collects/pkg/private/addl-installs.rkt`** -> AI Confidence: **99.29%**
239. **`racket/collects/pkg/private/archive.rkt`** -> AI Confidence: **99.29%**
240. **`racket/collects/pkg/private/catalog-archive.rkt`** -> AI Confidence: **99.29%**
241. **`racket/collects/pkg/private/catalog-copy.rkt`** -> AI Confidence: **99.29%**
242. **`racket/collects/pkg/private/catalog-show.rkt`** -> AI Confidence: **99.29%**
243. **`racket/collects/pkg/private/catalog-update.rkt`** -> AI Confidence: **99.29%**
244. **`racket/collects/pkg/private/catalog.rkt`** -> AI Confidence: **99.29%**
245. **`racket/collects/pkg/private/check-will-exist.rkt`** -> AI Confidence: **99.29%**
246. **`racket/collects/pkg/private/clone-path.rkt`** -> AI Confidence: **99.29%**
247. **`racket/collects/pkg/private/collects.rkt`** -> AI Confidence: **99.29%**
248. **`racket/collects/pkg/private/config.rkt`** -> AI Confidence: **99.29%**
249. **`racket/collects/pkg/private/content.rkt`** -> AI Confidence: **99.29%**
250. **`racket/collects/pkg/private/create.rkt`** -> AI Confidence: **99.29%**
251. **`racket/collects/pkg/private/download.rkt`** -> AI Confidence: **99.29%**
252. **`racket/collects/pkg/private/get-info.rkt`** -> AI Confidence: **99.29%**
253. **`racket/collects/pkg/private/git-url-scheme.rkt`** -> AI Confidence: **99.29%**
254. **`racket/collects/pkg/private/git.rkt`** -> AI Confidence: **99.29%**
255. **`racket/collects/pkg/private/install.rkt`** -> AI Confidence: **99.29%**
256. **`racket/collects/pkg/private/lock.rkt`** -> AI Confidence: **99.29%**
257. **`racket/collects/pkg/private/metadata.rkt`** -> AI Confidence: **99.29%**
258. **`racket/collects/pkg/private/migrate.rkt`** -> AI Confidence: **99.29%**
259. **`racket/collects/pkg/private/mod-paths.rkt`** -> AI Confidence: **99.29%**
260. **`racket/collects/pkg/private/network.rkt`** -> AI Confidence: **99.29%**
261. **`racket/collects/pkg/private/orig-pkg.rkt`** -> AI Confidence: **99.29%**
262. **`racket/collects/pkg/private/params.rkt`** -> AI Confidence: **99.29%**
263. **`racket/collects/pkg/private/path.rkt`** -> AI Confidence: **99.29%**
264. **`racket/collects/pkg/private/pkg-db.rkt`** -> AI Confidence: **99.29%**
265. **`racket/collects/pkg/private/prefetch.rkt`** -> AI Confidence: **99.29%**
266. **`racket/collects/pkg/private/print.rkt`** -> AI Confidence: **99.29%**
267. **`racket/collects/pkg/private/remove.rkt`** -> AI Confidence: **99.29%**
268. **`racket/collects/pkg/private/show.rkt`** -> AI Confidence: **99.29%**
269. **`racket/collects/pkg/private/stage.rkt`** -> AI Confidence: **99.29%**
270. **`racket/collects/pkg/private/trash.rkt`** -> AI Confidence: **99.29%**
271. **`racket/collects/pkg/strip.rkt`** -> AI Confidence: **99.29%**
272. **`racket/collects/planet/private/data.rkt`** -> AI Confidence: **99.29%**
273. **`racket/collects/planet/private/prefix-dispatcher.rkt`** -> AI Confidence: **99.29%**
274. **`racket/collects/planet/private/short-syntax-helpers.rkt`** -> AI Confidence: **99.29%**
275. **`racket/collects/racket/bool.rkt`** -> AI Confidence: **99.29%**
276. **`racket/collects/racket/bytes.rkt`** -> AI Confidence: **99.29%**
277. **`racket/collects/racket/contract/private/and.rkt`** -> AI Confidence: **99.29%**
278. **`racket/collects/racket/contract/private/arity-checking.rkt`** -> AI Confidence: **99.29%**
279. **`racket/collects/racket/contract/private/arr-i.rkt`** -> AI Confidence: **99.29%**
280. **`racket/collects/racket/contract/private/arr-util.rkt`** -> AI Confidence: **99.29%**
281. **`racket/collects/racket/contract/private/arrow-collapsible.rkt`** -> AI Confidence: **99.29%**
282. **`racket/collects/racket/contract/private/arrow-common.rkt`** -> AI Confidence: **99.29%**
283. **`racket/collects/racket/contract/private/arrow-higher-order.rkt`** -> AI Confidence: **99.29%**
284. **`racket/collects/racket/contract/private/arrow-val-first.rkt`** -> AI Confidence: **99.29%**
285. **`racket/collects/racket/contract/private/base.rkt`** -> AI Confidence: **99.29%**
286. **`racket/collects/racket/contract/private/blame.rkt`** -> AI Confidence: **99.29%**
287. **`racket/collects/racket/contract/private/box.rkt`** -> AI Confidence: **99.29%**
288. **`racket/collects/racket/contract/private/case-arrow.rkt`** -> AI Confidence: **99.29%**
289. **`racket/collects/racket/contract/private/collapsible-common.rkt`** -> AI Confidence: **99.29%**
290. **`racket/collects/racket/contract/private/exists.rkt`** -> AI Confidence: **99.29%**
291. **`racket/collects/racket/contract/private/generate.rkt`** -> AI Confidence: **99.29%**
292. **`racket/collects/racket/contract/private/guts.rkt`** -> AI Confidence: **99.29%**
293. **`racket/collects/racket/contract/private/hash.rkt`** -> AI Confidence: **99.29%**
294. **`racket/collects/racket/contract/private/helpers.rkt`** -> AI Confidence: **99.29%**
295. **`racket/collects/racket/contract/private/legacy.rkt`** -> AI Confidence: **99.29%**
296. **`racket/collects/racket/contract/private/list.rkt`** -> AI Confidence: **99.29%**
297. **`racket/collects/racket/contract/private/merge-cache.rkt`** -> AI Confidence: **99.29%**
298. **`racket/collects/racket/contract/private/misc.rkt`** -> AI Confidence: **99.29%**
299. **`racket/collects/racket/contract/private/module-boundary-ctc.rkt`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `racket/src/ChezScheme/zlib/contrib/dotzlib/DotZLib/UnitTests.cs` -> **0.6474%** Exposure
- `racket/src/ChezScheme/unicode/unicode-char-cases.ss` -> **0.0283%** Exposure
- `racket/collects/racket/private/path.rkt` -> **0.0031%** Exposure
- `racket/src/regexp/analyze/convert.rkt` -> **0.0015%** Exposure
- `racket/src/ChezScheme/s/reboot.ss` -> **0.0001%** Exposure
### Exploit Generation Surface
- `pkgs/racket-index/scribblings/main/private/local-redirect.rkt` -> **100.0%** Exposure
- `racket/collects/compiler/private/xform.rkt` -> **100.0%** Exposure
- `racket/collects/launcher/launcher.rkt` -> **100.0%** Exposure
- `racket/collects/net/url-string.rkt` -> **100.0%** Exposure
- `racket/collects/planet/private/command.rkt` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `racket/src/ChezScheme/maketarball` -> **100.0%** Exposure
- `racket/src/ChezScheme/rpm/Makefile` -> **100.0%** Exposure
- `racket/src/ChezScheme/zlib/Makefile.in` -> **100.0%** Exposure
- `racket/src/bc/foreign/libffi/doc/Makefile.in` -> **100.0%** Exposure
- `pkgs/racket-index/help/private/command.rkt` -> **100.0%** Exposure
### Raw Memory Manipulation
- `racket/src/ChezScheme/lz4/lib/lz4frame.c` -> **10.0%** Exposure
- `racket/src/ChezScheme/zlib/contrib/minizip/unzip.c` -> **10.0%** Exposure
- `racket/src/ChezScheme/zlib/deflate.c` -> **10.0%** Exposure
- `racket/src/ChezScheme/zlib/examples/gzlog.c` -> **10.0%** Exposure
- `racket/src/ChezScheme/zlib/trees.c` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `pkgs/plt-services/meta/props` -> **100.0%** Exposure
- `racket/src/ChezScheme/archive/checkin` -> **100.0%** Exposure
- `racket/src/ChezScheme/configure` -> **100.0%** Exposure
- `racket/src/ChezScheme/zlib/configure` -> **100.0%** Exposure
- `racket/src/ChezScheme/zlib/os400/make.sh` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `180` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2501` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `racket/src/ChezScheme/c/io.c` (C) -> Cumulative Risk: **826.13**
- **Archetype:** `file_cluster_13` (Distance: 13.0 IQR)
- **Magnitude:** 317.78 | **LOC:** 287 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9895%)
- **Heaviest Functions:** `S_fixedpathp` (Impact: 65.8), `S_file_regularp` (Impact: 19.3), `S_file_directoryp` (Impact: 19.3)

### 2. `racket/src/bc/src/mzrt.c` (C) -> Cumulative Risk: **826.1**
- **Archetype:** `file_cluster_4` (Distance: 13.143 IQR)
- **Magnitude:** 676.86 | **LOC:** 754 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (99.9956%)
- **Heaviest Functions:** `rwlock_wrlock` (Impact: 13.1), `rwlock_rdlock` (Impact: 12.9), `mzrt_rwlock_wrlock_worker` (Impact: 8.9)

### 3. `pkgs/racket-index/scribblings/main/private/search.js` (JAVASCRIPT) -> Cumulative Risk: **825.06**
- **Archetype:** `file_cluster_8` (Distance: 11.899 IQR)
- **Magnitude:** 1551.46 | **LOC:** 1214 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `SanitizeHTML` (Impact: 1137.4), `InitializeSearch` (Impact: 62.9), `MakeLanguageFamilySuggestions` (Impact: 37.5)

### 4. `racket/src/zuo/zuo.c` (C) -> Cumulative Risk: **820.85**
- **Archetype:** `file_cluster_8` (Distance: 14.969 IQR)
- **Magnitude:** 9685.08 | **LOC:** 7672 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `zuo_in` (Impact: 1282.4), `zuo_process` (Impact: 577.0), `continue_step` (Impact: 304.8)

### 5. `racket/src/ChezScheme/zlib/os400/make.sh` (SHELL) -> Cumulative Risk: **817.93**
- **Archetype:** `file_cluster_12` (Distance: 14.863 IQR)
- **Magnitude:** 419.74 | **LOC:** 367 | **CtrlFlow:** 75.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 186.3), `Anonymous_Block` (Impact: 65.8), `Anonymous_Block` (Impact: 8.8)

### 6. `racket/src/ChezScheme/c/schlib.c` (C) -> Cumulative Risk: **804.65**
- **Archetype:** `file_cluster_13` (Distance: 13.42 IQR)
- **Magnitude:** 287.7 | **LOC:** 322 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `S_call_help` (Impact: 13.2), `S_return` (Impact: 9.4), `Ssymbol_to_string` (Impact: 5.5)

### 7. `racket/src/rktio/rktio_wide.c` (C) -> Cumulative Risk: **803.84**
- **Archetype:** `file_cluster_13` (Distance: 13.931 IQR)
- **Magnitude:** 716.22 | **LOC:** 344 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.2389%)
- **Heaviest Functions:** `utf8ish_to_utf16ish` (Impact: 177.8), `utf16ish_to_utf8ish` (Impact: 153.4), `rktio_convert_to_wchar` (Impact: 19.6)

### 8. `racket/src/bc/src/network.c` (C) -> Cumulative Risk: **799.57**
- **Archetype:** `file_cluster_8` (Distance: 13.198 IQR)
- **Magnitude:** 4544.62 | **LOC:** 2793 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (99.9998%)
- **Heaviest Functions:** `do_udp_send_it` (Impact: 391.4), `check_fd_sema` (Impact: 321.4), `udp_bind_or_connect` (Impact: 240.6)

### 9. `racket/src/bc/src/unwind/libunwind.c` (C) -> Cumulative Risk: **790.49**
- **Archetype:** `file_cluster_8` (Distance: 14.364 IQR)
- **Magnitude:** 3480.08 | **LOC:** 3496 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `fetch_proc_info` (Impact: 1157.0), `read_operand` (Impact: 178.7), `tdep_uc_addr` (Impact: 125.4)

### 10. `racket/src/rktio/rktio_envvars.c` (C) -> Cumulative Risk: **778.93**
- **Archetype:** `file_cluster_8` (Distance: 13.921 IQR)
- **Magnitude:** 620.36 | **LOC:** 479 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.6387%)
- **Heaviest Functions:** `rktio_envvars` (Impact: 30.2), `rktio_setenv` (Impact: 24.4), `rktio_envvars_to_block` (Impact: 22.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `racket/src/ChezScheme/s/cpprim.ss` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.632 IQR)
- **Top Global Matches:** file_cluster_8: 10.632, file_cluster_7: 11.379, file_cluster_1: 11.593
- **Magnitude:** 115025.89 | **LOC:** 8613 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.4244%), Tech Debt (9.1333%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 960`, `structural_boundaries: 524`, `args: 131`, `func_start: 131`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 315`, `dead_code: 2`, `planned_debt: 31`
* *Architecture:* `io: 13`, `import: 1`
* *Defense:* `safety: 55`, `immutability_locks: 307`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/ChezScheme/s/cpnanopass.ss` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.663 IQR)
- **Top Global Matches:** file_cluster_8: 11.663, file_cluster_17: 12.182, file_cluster_15: 12.262
- **Magnitude:** 97214.62 | **LOC:** 10910 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (20.5424%), Tech Debt (8.8948%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1339`, `structural_boundaries: 934`, `args: 45`, `func_start: 45`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 1160`, `dead_code: 7`, `planned_debt: 23`, `fragile_debt: 3`
* *Architecture:* `io: 57`, `import: 10`
* *Defense:* `safety: 72`, `doc: 15`, `immutability_locks: 305`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/ChezScheme/s/io.ss` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.512 IQR)
- **Top Global Matches:** file_cluster_8: 10.512, file_cluster_7: 11.128, file_cluster_15: 11.217
- **Magnitude:** 86770.48 | **LOC:** 6399 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.7219%), Tech Debt (8.1334%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1032`, `structural_boundaries: 488`, `args: 65`, `func_start: 65`, `class_start: 7`
* *Risk/State:* `state_mutation: 271`, `dead_code: 2`, `planned_debt: 5`
* *Architecture:* `io: 38`
* *Defense:* `safety: 14`, `doc: 86`, `sync_locks: 1`, `immutability_locks: 34`, `cleanup: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/ChezScheme/s/cp0.ss` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.377 IQR)
- **Top Global Matches:** file_cluster_8: 10.377, file_cluster_17: 10.939, file_cluster_7: 10.964
- **Magnitude:** 71125.08 | **LOC:** 5881 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.0886%), Tech Debt (11.7274%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 889`, `structural_boundaries: 581`, `args: 58`, `func_start: 58`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 5`, `state_mutation: 36`, `dead_code: 30`, `planned_debt: 12`, `fragile_debt: 12`
* *Architecture:* `io: 3`, `import: 1`
* *Defense:* `safety: 71`, `doc: 88`, `test: 10`, `immutability_locks: 458`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/racket/private/class-internal.rkt` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.81 IQR)
- **Top Global Matches:** file_cluster_8: 9.81, file_cluster_7: 10.618, file_cluster_1: 10.817
- **Magnitude:** 48074.26 | **LOC:** 4838 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.6145%), Tech Debt (8.5589%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 424`, `structural_boundaries: 172`, `args: 116`, `func_start: 116`
* *Risk/State:* `state_mutation: 24`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `io: 19`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/ChezScheme/s/expeditor.ss` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.816 IQR)
- **Top Global Matches:** file_cluster_8: 9.816, file_cluster_7: 10.379, file_cluster_1: 10.612
- **Magnitude:** 38496.41 | **LOC:** 3056 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.9458%), Tech Debt (8.4693%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 385`, `structural_boundaries: 239`, `args: 92`, `func_start: 92`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 78`, `fragile_debt: 1`
* *Architecture:* `io: 14`
* *Defense:* `safety: 5`, `doc: 105`, `immutability_locks: 37`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/ChezScheme/s/5_3.ss` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.804 IQR)
- **Top Global Matches:** file_cluster_8: 9.804, file_cluster_7: 10.544, file_cluster_1: 10.738
- **Magnitude:** 31924.25 | **LOC:** 3804 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.041%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 586`, `structural_boundaries: 165`, `args: 26`, `func_start: 26`
* *Risk/State:* `state_mutation: 75`
* *Architecture:* None
* *Defense:* `safety: 2`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/setup/setup-core.rkt` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.399 IQR)
- **Top Global Matches:** file_cluster_8: 9.399, file_cluster_7: 10.204, file_cluster_1: 10.442
- **Magnitude:** 31642.57 | **LOC:** 2244 | **CtrlFlow:** 91.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.3414%), Tech Debt (8.7486%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 33`, `args: 75`, `func_start: 75`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 35`, `fragile_debt: 1`
* *Architecture:* `io: 18`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/racket/private/for.rkt` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.804 IQR)
- **Top Global Matches:** file_cluster_8: 9.804, file_cluster_7: 10.628, file_cluster_15: 10.746
- **Magnitude:** 29112.93 | **LOC:** 2823 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.2638%), Tech Debt (8.0792%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 101`, `args: 77`, `func_start: 77`
* *Risk/State:* `state_mutation: 50`, `planned_debt: 1`
* *Architecture:* `io: 10`
* *Defense:* `safety: 26`, `immutability_locks: 98`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkgs/racket-index/setup/scribble.rkt` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.985 IQR)
- **Top Global Matches:** file_cluster_8: 8.985, file_cluster_7: 9.857, file_cluster_1: 10.087
- **Magnitude:** 28500.52 | **LOC:** 1832 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.1612%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 345`, `structural_boundaries: 62`, `args: 63`, `func_start: 63`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `io: 25`, `import: 1`
* *Defense:* `safety: 3`, `immutability_locks: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/racket/pretty.rkt` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.039 IQR)
- **Top Global Matches:** file_cluster_8: 9.039, file_cluster_7: 9.912, file_cluster_1: 10.132
- **Magnitude:** 28420.78 | **LOC:** 1700 | **CtrlFlow:** 75.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.7742%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 102`, `args: 76`, `func_start: 76`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `io: 13`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/ChezScheme/s/bytevector.ss` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.943 IQR)
- **Top Global Matches:** file_cluster_8: 9.943, file_cluster_7: 10.633, file_cluster_15: 10.795
- **Magnitude:** 28306.08 | **LOC:** 1574 | **CtrlFlow:** 75.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.0768%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 93`, `args: 94`, `func_start: 94`
* *Risk/State:* `state_mutation: 76`
* *Architecture:* None
* *Defense:* `doc: 14`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/ChezScheme/s/syntax.ss` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.812 IQR)
- **Top Global Matches:** file_cluster_8: 10.812, file_cluster_7: 11.138, file_cluster_15: 11.218
- **Magnitude:** 25316.44 | **LOC:** 10586 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.0796%), Tech Debt (8.0779%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 619`, `structural_boundaries: 382`, `args: 13`, `func_start: 13`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 9`, `state_mutation: 21`, `dead_code: 24`, `planned_debt: 3`
* *Architecture:* `io: 38`, `import: 2`
* *Defense:* `safety: 3`, `doc: 591`, `immutability_locks: 147`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/openssl/mzssl.rkt` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.193 IQR)
- **Top Global Matches:** file_cluster_8: 9.193, file_cluster_7: 10.049, file_cluster_1: 10.258
- **Magnitude:** 24626.9 | **LOC:** 1794 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.9203%), Tech Debt (14.3663%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 107`, `args: 84`, `func_start: 84`
* *Risk/State:* `state_mutation: 39`, `planned_debt: 2`, `fragile_debt: 5`
* *Architecture:* `io: 24`
* *Defense:* `safety: 1`, `immutability_locks: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/racket/treelist.rkt` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.916 IQR)
- **Top Global Matches:** file_cluster_8: 8.916, file_cluster_7: 9.832, file_cluster_1: 10.032
- **Magnitude:** 24485.77 | **LOC:** 1718 | **CtrlFlow:** 89.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.2217%), Tech Debt (9.261%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 27`, `args: 111`, `func_start: 111`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 4`
* *Architecture:* `io: 13`, `import: 1`
* *Defense:* `safety: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/cs/rumble/struct.ss` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.812 IQR)
- **Top Global Matches:** file_cluster_8: 9.812, file_cluster_7: 10.68, file_cluster_1: 10.908
- **Magnitude:** 21463.04 | **LOC:** 1520 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.4662%), Tech Debt (9.1493%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 120`, `args: 77`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `fragile_debt: 1`
* *Architecture:* `io: 4`
* *Defense:* `safety: 88`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/ChezScheme/s/compile.ss` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.373 IQR)
- **Top Global Matches:** file_cluster_8: 9.373, file_cluster_7: 10.105, file_cluster_15: 10.218
- **Magnitude:** 20961.02 | **LOC:** 2352 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.5407%), Tech Debt (8.1546%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 348`, `structural_boundaries: 303`, `args: 31`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 59`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `io: 18`, `import: 1`
* *Defense:* `safety: 4`, `doc: 15`, `immutability_locks: 54`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/cs/rumble/foreign.ss` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.654 IQR)
- **Top Global Matches:** file_cluster_8: 9.654, file_cluster_7: 10.535, file_cluster_1: 10.754
- **Magnitude:** 20698.19 | **LOC:** 2098 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.7796%), Tech Debt (8.793%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 279`, `structural_boundaries: 107`, `args: 49`, `func_start: 49`, `class_start: 7`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 10`, `fragile_debt: 1`
* *Architecture:* `io: 6`
* *Defense:* `safety: 79`, `sync_locks: 1`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/ChezScheme/s/format.ss` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.49 IQR)
- **Top Global Matches:** file_cluster_8: 9.49, file_cluster_7: 10.123, file_cluster_15: 10.382
- **Magnitude:** 20637.48 | **LOC:** 1785 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.5324%), Tech Debt (8.3402%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 186`, `args: 24`, `func_start: 24`, `class_start: 7`
* *Risk/State:* `state_mutation: 54`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 77`
* *Defense:* `doc: 34`, `immutability_locks: 53`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/ChezScheme/s/prims.ss` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.112 IQR)
- **Top Global Matches:** file_cluster_8: 10.112, file_cluster_15: 10.726, file_cluster_7: 10.827
- **Magnitude:** 20508.08 | **LOC:** 2997 | **CtrlFlow:** 77.7% | **Authorship Centralization:** 62.5%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.641%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 549`, `structural_boundaries: 158`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 129`
* *Architecture:* `io: 9`
* *Defense:* `safety: 7`, `doc: 17`, `sync_locks: 2`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/syntax/parse/private/rep.rkt` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.05 IQR)
- **Top Global Matches:** file_cluster_8: 9.05, file_cluster_7: 9.911, file_cluster_1: 10.131
- **Magnitude:** 19269.72 | **LOC:** 1973 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.2907%), Tech Debt (8.7737%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 71`, `args: 143`, `func_start: 143`
* *Risk/State:* `state_mutation: 7`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/compiler/embed.rkt` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.776 IQR)
- **Top Global Matches:** file_cluster_8: 8.776, file_cluster_7: 9.684, file_cluster_1: 9.893
- **Magnitude:** 18962.39 | **LOC:** 2041 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.7837%), Tech Debt (11.0817%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 257`, `structural_boundaries: 69`, `args: 49`, `func_start: 49`
* *Risk/State:* `state_mutation: 3`, `fragile_debt: 3`
* *Architecture:* `io: 24`, `import: 1`
* *Defense:* `safety: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/portfun.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.802 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.424 IQR)
- **Top Global Matches:** file_cluster_8: 13.802, file_cluster_7: 14.09, file_cluster_13: 14.126
- **Magnitude:** 17974.72 | **LOC:** 4713 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 488
- **Risk Profile:** Cognitive Load (94.9514%), Tech Debt (15.3358%)
**Top Internal Functions/Classes:**
  * `user_read_result` (Impact: 13005.5 | O(2^N) | DB: 488)
    * *Intent:* #define MAX_USER_INPUT_REUSE_SIZE 1024 /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ...
  * `do_general_read_bytes` (Impact: 611.7 | O(N^6) | DB: 29)
  * `sha_bytes` (Impact: 326.5 | O(N^6) | DB: 24)
  * `display_write` (Impact: 199.7 | O(N^6) | DB: 18)
  * `peeked_read` (Impact: 172.5 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1043`, `structural_boundaries: 348`, `args: 238`, `func_start: 180`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 1716`, `planned_debt: 2`, `orphaned_logic: 17`
* *Architecture:* `io: 124`, `api: 615`, `import: 4`
* *Defense:* `doc: 2`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` schpriv.h, mzmark_portfun.inc, schrktio.h, racket_version.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkgs/racket-benchmarks/tests/racket/benchmarks/common/dynamic2.sch` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.049 IQR)
- **Top Global Matches:** file_cluster_8: 10.049, file_cluster_17: 10.554, file_cluster_7: 10.732
- **Magnitude:** 17333.99 | **LOC:** 2348 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.2857%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 96`, `args: 149`, `func_start: 149`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 60`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `io: 24`
* *Defense:* `safety: 11`, `immutability_locks: 46`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkgs/racket-benchmarks/tests/racket/benchmarks/common/dynamic.sch` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.848 IQR)
- **Top Global Matches:** file_cluster_8: 9.848, file_cluster_17: 10.408, file_cluster_7: 10.548
- **Magnitude:** 17311.95 | **LOC:** 2341 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.6369%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 96`, `args: 149`, `func_start: 149`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 39`, `dead_code: 6`
* *Architecture:* `io: 24`
* *Defense:* `safety: 11`, `immutability_locks: 46`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `racket/src/ChezScheme/zlib/contrib/blast/blast.c` (C) | Magnitude: 6.89 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 324, indent_spaces: 226, pointers: 98, branch: 62
- `racket/src/ChezScheme/zlib/gzlib.c` (C) | Magnitude: 1058.22 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 218, state_mutation: 196, pointers: 100, branch: 91
- `racket/src/bc/src/setjmpup.c` (C) | Magnitude: 219.56 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 139, state_mutation: 121, pointers: 72, api: 36
- `racket/src/ChezScheme/zlib/contrib/dotzlib/DotZLib/AssemblyInfo.cs` (CSHARP) | Magnitude: 0.15 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: decorators: 12, structural_boundaries: 2, import: 2, sec_high_risk_execution: 2
- `racket/src/ChezScheme/lz4/lib/lz4frame.c` (C) | Magnitude: 3096.84 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 805, indent_spaces: 805, pointers: 544, branch: 215

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `racket/src/ChezScheme/lz4/tests/frametest.c` (C) | Magnitude: 2302.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 872, state_mutation: 814, pointers: 268, branch: 203
- `racket/src/ChezScheme/zlib/examples/gzlog.c` (C) | Magnitude: 936.16 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 390, state_mutation: 259, scientific: 230, pointers: 202
- `racket/src/bc/foreign/libffi/src/arc/ffi.c` (C) | Magnitude: 463.0 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 231, indent_spaces: 219, pointers: 176, branch: 134
- `racket/src/ChezScheme/lz4/lib/lz4hc.c` (C) | Magnitude: 3342.82 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 866, indent_spaces: 601, api: 217, immutability_locks: 190
- `racket/src/ChezScheme/zlib/inflate.c` (C) | Magnitude: 831.08 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 413, indent_spaces: 351, pointers: 205, branch: 115

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `racket/src/ChezScheme/zlib/configure` (SHELL) | Magnitude: 1391.6 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 488, indent_spaces: 486, io: 391, branch: 218
- `racket/src/bc/src/lightning/i386/core-common.h` (C) | Magnitude: 38.52 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 326, reflection_metaprogramming: 271, pointers: 28, branch: 13
- `racket/src/bc/src/lightning/i386/fp.h` (C) | Magnitude: 18.36 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 162, reflection_metaprogramming: 156, import: 3, doc: 2
- `racket/src/ChezScheme/lz4/tests/test_install.sh` (SHELL) | Magnitude: 36.88 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: safety_bypasses: 21, state_mutation: 19, indent_spaces: 16, branch: 13
- `racket/src/bc/src/lightning/ppc/asm.h` (C) | Magnitude: 13.9 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 465, reflection_metaprogramming: 445, bitwise_ops: 140, indent_spaces: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `racket/src/bc/foreign/libffi/src/sh64/ffi.c` (C) | Magnitude: 299.58 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 148, indent_spaces: 83, pointers: 65, branch: 53
- `racket/src/bc/foreign/libffi/testsuite/libffi.call/bpo_38748.c` (C) | Magnitude: 24.86 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, api: 10, pointers: 9, state_mutation: 7
- `racket/src/bc/foreign/libffi/src/raw_api.c` (C) | Magnitude: 337.34 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 194, pointers: 90, branch: 62, api: 44
- `racket/src/mzcom/com_glue.c` (C) | Magnitude: 180.56 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 104, doc: 73, pointers: 66, state_mutation: 43
- `racket/src/ChezScheme/c/schlib.c` (C) | Magnitude: 287.7 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 129, indent_spaces: 117, api: 75, structural_boundaries: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `racket/src/ChezScheme/s/engine.ss` (SCHEME) | Magnitude: 35.8 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 72, doc: 25, closures: 22, state_mutation: 19
- `racket/src/worksp/msvcprep.ps1` (POWERSHELL) | Magnitude: 21.68 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 6, indent_spaces: 6, doc: 5, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pkgs/racket-index/scribblings/main/private/search-context.html` (HTML) | Magnitude: 101.8 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 67, state_mutation: 36, branch: 30, structural_boundaries: 21
- `racket/collects/file/zip.rkt` (SCHEME) | Magnitude: 657.41 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 122, dead_code: 21, branch: 20, sec_high_risk_execution: 9
- `racket/src/ChezScheme/nanopass/tests/compiler.ss` (SCHEME) | Magnitude: 79.66 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1281, structural_boundaries: 347, branch: 130, closures: 101
- `pkgs/racket-benchmarks/tests/racket/benchmarks/common/conform.sch` (SCHEME) | Magnitude: 5395.79 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 129, args: 70, func_start: 70, branch: 60
- `racket/src/ChezScheme/zlib/nintendods/Makefile` (MAKEFILE) | Magnitude: 161.16 | Delta: **0.544 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 17, branch: 11, api: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `pkgs/racket-index/scribblings/main/private/root-info.js` (JAVASCRIPT) | Magnitude: 15.92 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, state_mutation: 7, structural_boundaries: 5, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `racket/src/bc/src/mzrt.c` (C) | Magnitude: 676.86 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 327, pointers: 279, state_mutation: 270, api: 173
- `racket/src/rktio/rktio_file.c` (C) | Magnitude: 917.52 | Delta: **0.216 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 355, state_mutation: 190, pointers: 179, branch: 126

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `racket/src/ChezScheme/examples/macro.ss` (SCHEME) | Magnitude: 15.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 53, indent_spaces: 9, dead_code: 7, reflection_metaprogramming: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `racket/src/ChezScheme/s/cback.ss` (SCHEME) | Magnitude: 12.08 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 14, structural_boundaries: 1, globals: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `racket/src/ChezScheme/c/system.h` (C) | Magnitude: 16.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 13, macros: 8, api: 1, ownership: 1
- `racket/src/bc/foreign/libffi/src/x86/ffi.c` (C) | Magnitude: 1084.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 499, indent_spaces: 349, branch: 221, api: 173
- `racket/src/bc/src/hash.c` (C) | Magnitude: 2061.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 669, state_mutation: 626, pointers: 258, branch: 241
- `racket/src/ChezScheme/lz4/lib/lz4frame_static.h` (C) | Magnitude: 12.6 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: ownership: 5, macros: 3, import: 1
- `racket/src/ChezScheme/zlib/contrib/minizip/unzip.c` (C) | Magnitude: 18.03 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 667, state_mutation: 630, pointers: 385, branch: 214

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pkgs/racket-benchmarks/tests/racket/benchmarks/common/maze.sch` (SCHEME) | Magnitude: 2059.58 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 173, doc: 150, args: 46, func_start: 46
- `racket/src/ChezScheme/lz4/examples/compress_functions.c` (C) | Magnitude: 22.62 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, branch: 10, dead_code: 8, import: 8
- `racket/src/ChezScheme/zlib/gzread.c` (C) | Magnitude: 241.46 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 109, state_mutation: 99, pointers: 67, branch: 41
- `racket/src/ChezScheme/zlib/msdos/Makefile.emx` (MAKEFILE) | Magnitude: 49.72 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, indent_tabs: 10, func_start: 4, api: 4
- `racket/src/ChezScheme/zlib/old/Makefile.emx` (MAKEFILE) | Magnitude: 49.72 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, indent_tabs: 10, func_start: 4, api: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `racket/src/version/racket_version.h` -> Churn: **76.47%** | Cog Load: 52.909% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `racket/src/ChezScheme/s/cpnanopass.ss` -> **Matthew Flatt** (100.0% isolated ownership) | Magnitude: 97214.62
- `racket/src/ChezScheme/s/io.ss` -> **Matthew Flatt** (100.0% isolated ownership) | Magnitude: 86770.48
- `racket/collects/setup/setup-core.rkt` -> **Matthew Flatt** (100.0% isolated ownership) | Magnitude: 31642.57
- `pkgs/racket-index/setup/scribble.rkt` -> **Matthew Flatt** (100.0% isolated ownership) | Magnitude: 28500.52
- `racket/src/ChezScheme/s/bytevector.ss` -> **Gustavo Massaccesi** (100.0% isolated ownership) | Magnitude: 28306.08

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `racket/src/bc/include/scheme.h` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 72.4723%)
- `racket/src/ChezScheme/lz4/ossfuzz/fuzz_helpers.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 98.2932%)
- `racket/src/bc/src/mzrt.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 89.7011%)
- `racket/src/bc/src/schpriv.h` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 10.4254%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `racket/src/bc/foreign/libffi/include/ffi_common.h` -> **Severity: 966.491** (Blast Radius: 9.665 * Doc Risk: 99.9991%)
- `racket/src/ChezScheme/zlib/zlib.h` -> **Severity: 909.124** (Blast Radius: 9.283 * Doc Risk: 97.9343%)
- `racket/src/bc/include/scheme.h` -> **Severity: 517.8** (Blast Radius: 5.178 * Doc Risk: 100.0%)
- `racket/src/bc/src/schpriv.h` -> **Severity: 503.4** (Blast Radius: 5.034 * Doc Risk: 100.0%)
- `racket/src/rktio/rktio_private.h` -> **Severity: 304.4** (Blast Radius: 3.044 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
