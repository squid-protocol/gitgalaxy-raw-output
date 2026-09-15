# ARCHITECTURAL_BRIEF: pypy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pypy/pypy.git` |
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
| Total Artifacts | 5994 |
| Analyzed Artifacts (Scanned) | 5000 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 994 |
| Total LOC | 987348 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 83.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5988 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1493 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.0924 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 289 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 4416 | 931883 | 88.3% |
| C | 295 | 46907 | 5.9% |
| PLAINTEXT | 175 | 0 | 3.5% |
| CPP | 27 | 4122 | 0.5% |
| SHELL | 24 | 131 | 0.5% |
| MARKDOWN | 18 | 0 | 0.4% |
| XML | 17 | 0 | 0.3% |
| MAKEFILE | 13 | 2198 | 0.3% |
| BATCH | 5 | 391 | 0.1% |
| HTML | 3 | 969 | 0.1% |
| JSON | 2 | 2 | 0.0% |
| M4 | 2 | 599 | 0.0% |
| ASSEMBLY | 2 | 97 | 0.0% |
| CSS | 1 | 49 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +0.34; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 30%, Data / Markup / Trivial 18%, Interface Declarations Files 17%, Defensive Guards Files 13%, Parameter Forwarders Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4806 | 96.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 193 | 3.9% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 994*

**Composition by Extension & Reason:**
- `.rst`: 217x Excluded (Unsupported Extension: '.rst'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 181x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Lexical Monotony: High structural repetition detected in 2366 LOC), 2x Excluded (Lexical Monotony: High structural repetition detected in 2215 LOC)
- `.py`: 15x Excluded: Neighborhood Micro-Mass Limit Exceeded, 12x Excluded (Embedded Hex Payload: 1024 hex tokens in 699 LOC), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dectest`: 143x Excluded (Unsupported Extension: '.decTest')
- `no_extension`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 12 LOC)
- `.png`: 15x Excluded (Explicitly Denied Extension: '.png')
- `.gif`: 11x Excluded (Explicitly Denied Extension: '.gif')
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 23 LOC), 1x Excluded (Machine-Generated Source Code Signature: 16 LOC), 1x Excluded (Machine-Generated Source Code Signature: 29 LOC)
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 98 LOC), 1x Excluded (Machine-Generated Source Code Signature: 182 LOC), 1x Excluded (Embedded Array/Matrix Payload: 55661 commas in 4104 LOC)
- `.dot`: 8x Excluded (Unsupported Extension: '.dot')
- `.0`: 7x Excluded (Unsupported Extension: '.0')
- `.au`: 6x Excluded (Unsupported Extension: '.au')
- `.graffle`: 6x Excluded (Unsupported Extension: '.graffle')
- `.pdf`: 6x Excluded (Explicitly Denied Extension: '.pdf')
- `.patch`: 6x Excluded (Unsupported Extension: '.patch')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 32.3 | 30.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 67.1 | 77.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 15.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 23.6 | 10.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 45.7 | 9.5 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 86.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.4 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 71.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 95.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 29031 | 2258 | 10 | `rpython/rlib/rvmprof/src/shared/libbacktrace/dwarf.c` |
| cleanup | 3126 | 655 | 1 | `pypy/module/mmap/test/test_mmap.py` |
| guards | 97791 | 3274 | 48 | `pypy/module/micronumpy/test/test_ndarray.py` |
| danger | 39939 | 3238 | 21 | `extra_tests/cffi_tests/test_c.py` |
| concurrency | 2990 | 514 | 1 | `lib-python/2.7/test/test_multiprocessing.py` |
| connectivity | 95601 | 4160 | 51 | `rpython/annotator/test/test_annrpython.py` |
| io | 20576 | 1799 | 9 | `lib-python/2.7/test/test_socket.py` |
| crypto | 103 | 53 | 0 | `lib-python/2.7/ssl.py` |
| ipc | 927 | 141 | 0 | `lib-python/2.7/test/test_subprocess.py` |
| time | 1056 | 235 | 0 | `lib-python/2.7/test/test_datetime.py` |
| serialization | 232 | 83 | 0 | `pypy/interpreter/test/test_zzpickle_and_slow.py` |
| regex | 1669 | 275 | 0 | `lib-python/2.7/test/test_re.py` |
| events | 2782 | 337 | 0 | `lib-python/2.7/compiler/pycodegen.py` |
| tests | 34116 | 1734 | 17 | `extra_tests/cffi_tests/test_c.py` |
| docs | 21891 | 2480 | 10 | `rpython/jit/metainterp/optimizeopt/test/test_optimizeopt.py` |
| debt | 9571 | 1628 | 5 | `rpython/annotator/test/test_annrpython.py` |
| mutation | 512701 | 4071 | 269 | `lib-python/2.7/plat-mac/macerrors.py` |
| dead_code | 29167 | 2892 | 15 | `rpython/jit/metainterp/optimizeopt/test/test_optimizeopt.py` |
| credential | 22 | 19 | 0 | `extra_tests/test_string.py` |
| threat | 9248 | 1510 | 5 | `lib-python/2.7/test/test_descr.py` |
| ml_ai | 1621 | 163 | 0 | `pypy/module/micronumpy/test/test_ndarray.py` |
| ui | 153 | 26 | 0 | `lib-python/2.7/idlelib/ReplaceDialog.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.8333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib-python/2.7/test/test_socket.py` (Hits: 328)
- `pypy/module/posix/test/test_posix2.py` (Hits: 311)
- `lib-python/2.7/test/test_ssl.py` (Hits: 300)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **os.py** (`lib-python/2.7/os.py`) — 935 inbound connections
2. **unittest.py** (`_pytest/unittest.py`) — 591 inbound connections
3. **rarithmetic.py** (`rpython/rlib/rarithmetic.py`) — 380 inbound connections
4. **objectmodel.py** (`rpython/rlib/objectmodel.py`) — 349 inbound connections
5. **__future__.py** (`lib-python/2.7/__future__.py`) — 314 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_import.py** (`pypy/module/imp/test/test_import.py`) — 92 outbound dependencies
2. **test_sundry.py** (`lib-python/2.7/test/test_sundry.py`) — 66 outbound dependencies
3. **Python.h** (`pypy/module/cpyext/include/Python.h`) — 61 outbound dependencies
4. **api.py** (`pypy/module/cpyext/api.py`) — 54 outbound dependencies
5. **test_fixers.py** (`lib-python/2.7/lib2to3/tests/test_fixers.py`) — 46 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main` **(Many-Argument Workhorses)** (@ `lib-python/2.7/test/regrtest.py`) -> Impact: **1147.3** | LOC: 746
- `convertsimple` **(Many-Argument Workhorses)** (@ `pypy/module/cpyext/src/getargs.c`) -> Impact: **681.2** | LOC: 783
  * *Intent:* */
- `__Py_dg_dtoa` **(Many-Argument Workhorses)** (@ `rpython/translator/c/src/dtoa.c`) -> Impact: **504.0** | LOC: 609
  * *Intent:* call to __Py_dg_freedtoa. */
- `__Py_dg_strtod` **(Many-Argument Workhorses)** (@ `rpython/translator/c/src/dtoa.c`) -> Impact: **361.5** | LOC: 753
- `make_formatting_class` **(Compute Cores)** (@ `pypy/objspace/std/newformat.py`) -> Impact: **360.9** | LOC: 770
- `dispatch_bytecode` **(Many-Argument Workhorses)** (@ `pypy/interpreter/pyopcode.py`) -> Impact: **328.3** | LOC: 306
- `make_timsort_class` **(Many-Argument Workhorses)** (@ `rpython/rlib/listsort.py`) -> Impact: **300.7** | LOC: 625
- `llexternal` **(Many-Argument Workhorses)** (@ `rpython/rtyper/lltypesystem/rffi.py`) -> Impact: **277.1** | LOC: 275
- `__init__` **(Many-Argument Workhorses)** (@ `pypy/module/micronumpy/nditer.py`) -> Impact: **272.0** | LOC: 175
- `_parse` **(Many-Argument Workhorses)** (@ `lib-python/2.7/sre_parse.py`) -> Impact: **267.5** | LOC: 310
  * *Intent:* # parse a simple pattern subpattern = SubPattern(state) # precompute constants into local variables subpatternappend = subpattern.append sourceget = s...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib-python/2.7/test` | 473 | 113738.94 | 21.98% | 0.0% |
| `lib-python/2.7` | 198 | 100827.04 | 48.47% | 20.96% |
| `rpython/rlib` | 84 | 38798.74 | 57.39% | 29.56% |
| `rpython/jit/metainterp/test` | 55 | 28712.86 | 27.31% | 0.0% |
| `pypy/objspace/std` | 40 | 27876.88 | 60.47% | 20.08% |
| `pypy/module/micronumpy` | 27 | 20934.9 | 73.22% | 26.44% |
| `rpython/jit/metainterp` | 28 | 19217.72 | 58.92% | 11.6% |
| `lib-python/2.7/idlelib` | 73 | 16718.16 | 44.02% | 23.05% |
| `rpython/jit/metainterp/optimizeopt` | 26 | 16700.42 | 67.47% | 18.0% |
| `pypy/interpreter` | 30 | 16614.92 | 54.39% | 27.37% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `rpython/rlib/rvmprof/src/shared/libbacktrace/Makefile.am` -> **100.0%** Exposure
- `extra_tests/ctypes_tests/test_commethods.py` -> **100.0%** Exposure
- `extra_tests/test_json.py` -> **100.0%** Exposure
- `extra_tests/test_os.py` -> **100.0%** Exposure
- `extra_tests/test_pyrepl/test_basic.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `_pytest/_code/_py2traceback.py` -> **100.0%** Exposure
- `_pytest/_code/code.py` -> **100.0%** Exposure
- `_pytest/_code/source.py` -> **100.0%** Exposure
- `_pytest/assertion/__init__.py` -> **100.0%** Exposure
- `_pytest/assertion/reinterpret.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `rpython/jit/metainterp/optimizeopt/test/test_optimizeopt.py` -> **416** Orphaned Functions | **6** Duplicates
- `lib-python/2.7/lib2to3/tests/test_fixers.py` -> **263** Orphaned Functions | **114** Duplicates
- `rpython/jit/metainterp/test/test_ajit.py` -> **225** Orphaned Functions | **95** Duplicates
- `pypy/module/micronumpy/test/test_ndarray.py` -> **290** Orphaned Functions | **2** Duplicates
- `extra_tests/cffi_tests/test_c.py` -> **231** Orphaned Functions | **6** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `lib_pypy/_cffi_ssl/_stdssl/certificate.py` -> **95.0376%** Exposure
- `lib-python/2.7/ssl.py` -> **47.9938%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `20` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `25078` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `rpython/rlib/parsing/lexer.py` (PYTHON) -> Cumulative Risk: **815.66**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.01)
- **Magnitude:** 227.28 | **LOC:** 213 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9898%), Safety Score (97.8266%)
- **Heaviest Functions:** `find_next_token` (Compute Cores, Impact: 19.0), `make_token` (Defensive Guards, Impact: 10.2), `__init__` (Many-Argument Workhorses, Impact: 9.1)

### 2. `pypy/objspace/std/mapdict.py` (PYTHON) -> Cumulative Risk: **779.32**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.04)
- **Magnitude:** 1954.9 | **LOC:** 1581 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Safety Score (97.6362%)
- **Heaviest Functions:** `STORE_ATTR_slowpath` (Many-Argument Workhorses, Impact: 80.0), `_make_storage_mixin_size_n` (Defensive Guards, Impact: 51.5), `LOAD_ATTR_slowpath` (Many-Argument Workhorses, Impact: 29.3)

### 3. `pypy/module/cpyext/api.py` (PYTHON) -> Cumulative Risk: **777.7**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.67)
- **Magnitude:** 1969.68 | **LOC:** 1885 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.4229%)
- **Heaviest Functions:** `make_wrapper_second_level` (Many-Argument Workhorses, Impact: 142.2), `wrapper_second_level` (Many-Argument Workhorses, Impact: 85.9), `generic_cpy_call` (Many-Argument Workhorses, Impact: 45.0)

### 4. `rpython/translator/c/gc.py` (PYTHON) -> Cumulative Risk: **769.7**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +0.15)
- **Magnitude:** 479.94 | **LOC:** 503 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `OP_GC_GCFLAG_EXTRA` (Many-Argument Workhorses, Impact: 19.4), `compilation_info` (Compute Cores, Impact: 13.5), `OP_GC_RELOAD_POSSIBLY_MOVED` (Defensive Guards, Impact: 10.3)

### 5. `pypy/module/micronumpy/types.py` (PYTHON) -> Cumulative Risk: **765.64**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.41)
- **Magnitude:** 3035.74 | **LOC:** 2770 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9467%)
- **Heaviest Functions:** `record_coerce` (Many-Argument Workhorses, Impact: 37.6), `make_integer_min_dtype` (Type Conversions, Impact: 33.2), `_coerce` (Many-Argument Workhorses, Impact: 26.7)

### 6. `lib_pypy/pyrepl/commands.py` (PYTHON) -> Cumulative Risk: **764.8**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.47)
- **Magnitude:** 501.6 | **LOC:** 394 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.3427%)
- **Heaviest Functions:** `do` (Compute Cores, Impact: 13.6), `kill_range` (Compute Cores, Impact: 12.8), `do` (Compute Cores, Impact: 10.6)

### 7. `rpython/translator/revdb/gencsupp.py` (PYTHON) -> Cumulative Risk: **761.42**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.90)
- **Magnitude:** 157.86 | **LOC:** 213 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9989%)
- **Heaviest Functions:** `emit_residual_call` (Many-Argument Workhorses, Impact: 14.7), `write_revdb_def_file` (Compute Cores, Impact: 12.8), `prepare_function` (Compute Cores, Impact: 12.4)

### 8. `dotviewer/graphparse.py` (PYTHON) -> Cumulative Risk: **758.95**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.10)
- **Magnitude:** 215.86 | **LOC:** 143 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.264%)
- **Heaviest Functions:** `parse_plain` (Many-Argument Workhorses, Impact: 49.5), `guess_type` (Compute Cores, Impact: 18.2), `dot2plain_graphviz` (Defensive Guards, Impact: 11.1)

### 9. `rpython/jit/backend/ppc/locations.py` (PYTHON) -> Cumulative Risk: **757.62**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z -0.11)
- **Magnitude:** 161.68 | **LOC:** 176 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Api Exposure (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 7.1), `get_fp_offset` (Parameter Forwarders, Impact: 2.0), `__init__` (Parameter Forwarders, Impact: 1.8)

### 10. `rpython/annotator/unaryop.py` (PYTHON) -> Cumulative Risk: **755.71**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.00)
- **Magnitude:** 1143.04 | **LOC:** 1038 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.4153%)
- **Heaviest Functions:** `s_isinstance` (Defensive Guards, Impact: 25.8), `getanyitem` (Defensive Guards, Impact: 23.1), `transform_varargs` (Many-Argument Workhorses, Impact: 16.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `rpython/jit/metainterp/test/test_ajit.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 5868.26 | **LOC:** 5055 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.4638%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_cmp_fastpaths` **(Defensive Guards)** (Impact: 32.7)
  * `test_nested_retrace` **(Defensive Guards)** (Impact: 27.3)
  * `test_inputarg_reset_bug` **(Compute Cores)** (Impact: 26.2)
    * *Intent:* ## j = 0 ## while j < 100: ## j += 1 ## c = 0 ## j = 0 ## while j < 2: ## j += 1 ## if c == 0:...
  * `test_retrace_ending_up_retracing_another_loop` **(Compute Cores)** (Impact: 22.8)
  * `make_int` **(Defensive Guards)** (Impact: 19.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 702 instances
* *State Mutation (weighted view):* 2580
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 496`, `structural_boundaries: 1733`, `args: 697`, `func_start: 680`, `class_start: 140`
* *Risk/State:* `safety_bypasses: 218`, `high_risk_execution: 1`, `state_mutation: 1176`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 9`, `duplicate_logic: 95`, `unreferenced_by_name: 225`
* *Architecture:* `io: 30`, `api: 376`, `import: 57`
* *Defense:* `safety: 373`, `doc: 1`, `test: 225`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` gc, math, py, pytest, rpython.jit.codewriter.policy, rpython.jit.metainterp, rpython.jit.metainterp.pyjitpl, rpython.jit.metainterp.test.support...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib-python/2.7/decimal.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 5098.96 | **LOC:** 6222 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.2119%), Tech Debt (18.8027%)
**Top Internal Functions/Classes:**
  * `__pow__` **(Many-Argument Workhorses)** (Impact: 122.6)
    * *Intent:* """Return self ** other [ % modulo]. With two arguments, compute self**other. With three arguments, ...
  * `_power_exact` **(Many-Argument Workhorses)** (Impact: 109.8)
    * *Intent:* """Attempt to compute self**other exactly. Given Decimals self and other and an integer p, attempt t...
  * `__new__` **(Many-Argument Workhorses)** (Impact: 95.2)
    * *Intent:* # Generally, the value of the Decimal instance is given by # (-1)**_sign * _int * 10**_exp # Special...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 78.1)
  * `quantize` **(Many-Argument Workhorses)** (Impact: 69.6)
    * *Intent:* """Quantize self so its exponent is the same as that of exp. Similar to self._rescale(exp._exp) but ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 728 instances
* *Concurrency (weighted view):* 50
* *State Mutation (weighted view):* 2306
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 935`, `structural_boundaries: 868`, `args: 233`, `func_start: 232`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 850`, `dead_code: 25`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 2`, `api: 173`, `concurrency: 10`, `import: 9`
* *Defense:* `safety: 39`, `doc: 221`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.001711
  * `Imports (Out-Degree: 5):` collections, decimal, doctest, itertools, locale, math, numbers, re...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `rpython/annotator/test/test_annrpython.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 4909.2 | **LOC:** 4842 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.1961%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `f` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `f` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `test_nonneg_cleverness` **(Defensive Guards)** (Impact: 15.0)
  * `test_general_nonneg_cleverness` **(Defensive Guards)** (Impact: 15.0)
  * `f` **(Many-Argument Workhorses)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 382 instances
* *State Mutation (weighted view):* 2023
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 2333`, `args: 858`, `func_start: 854`, `class_start: 197`
* *Risk/State:* `safety_bypasses: 145`, `high_risk_execution: 6`, `state_mutation: 1259`, `dead_code: 2`, `fragile_debt: 5`, `duplicate_logic: 114`
* *Architecture:* `io: 2`, `api: 542`, `import: 41`
* *Defense:* `safety: 775`, `doc: 5`, `test: 329`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.0004
  * `Imports (Out-Degree: 24):` __future__, collections, os, py.test, rpython.annotator, rpython.annotator.annrpython, rpython.annotator.classdesc, rpython.annotator.dictdef...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rpython/rlib/parsing/pypackrat.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 4598.58 | **LOC:** 3135 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.219%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_if_` **(Defensive Guards)** (Impact: 47.3)
  * `_enclosed` **(Defensive Guards)** (Impact: 41.6)
  * `_repetition` **(Defensive Guards)** (Impact: 41.0)
  * `_productionargs` **(Defensive Guards)** (Impact: 36.1)
  * `_arguments` **(Defensive Guards)** (Impact: 34.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 862 instances
* *State Mutation (weighted view):* 3551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 466`, `structural_boundaries: 571`, `args: 73`, `func_start: 73`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 85`, `state_mutation: 1827`
* *Architecture:* `api: 37`, `import: 2`
* *Defense:* `safety: 300`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.132
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.0012
  * `Imports (Out-Degree: 2):` rpython.rlib.parsing.makepackrat, rpython.rlib.parsing.tree
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `rpython/jit/backend/test/runner_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 4531.16 | **LOC:** 5486 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.0298%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_call_release_gil_variable_function_and_arguments` **(Compute Cores)** (Impact: 61.3)
  * `nan_and_infinity` **(Many-Argument Workhorses)** (Impact: 39.0)
  * `test_nan_and_infinity` **(Compute Cores)** (Impact: 38.6)
  * `test_floats_and_guards` **(Compute Cores)** (Impact: 37.6)
  * `test_jump` **(Compute Cores)** (Impact: 37.1)
    * *Intent:* # this test generates small loops where the JUMP passes many # arguments of various types, shuffling...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 608 instances
* *State Mutation (weighted view):* 2983
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 487`, `structural_boundaries: 965`, `args: 224`, `func_start: 206`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 157`, `state_mutation: 1767`, `dead_code: 4`, `fragile_debt: 4`, `duplicate_logic: 6`
* *Architecture:* `io: 30`, `api: 213`, `import: 90`
* *Defense:* `safety: 523`, `doc: 78`, `test: 145`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.201
  * `Choke Point (Betweenness):` 0.000115 | `Ripple Effect (Closeness):` 0.002327
  * `Imports (Out-Degree: 28):` __future__, ctypes, gc, math, operator, os, py, random...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `rpython/jit/metainterp/pyjitpl.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4369.84 | **LOC:** 3900 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (85.2194%), Tech Debt (14.1974%)
**Top Internal Functions/Classes:**
  * `do_residual_call` **(Many-Argument Workhorses)** (Impact: 99.9)
  * `_get_opimpl_method` **(Many-Argument Workhorses)** (Impact: 83.1)
    * *Intent:* # ____________________________________________________________
  * `handler` **(Many-Argument Workhorses)** (Impact: 80.8)
    * *Intent:* #
  * `get_list_of_active_boxes` **(Many-Argument Workhorses)** (Impact: 39.6)
  * `_build_allboxes` **(Many-Argument Workhorses)** (Impact: 38.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 571 instances
* *Api Near Db Sink:* 26 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 2094
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 589`, `structural_boundaries: 746`, `args: 268`, `func_start: 268`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 5`, `state_mutation: 952`, `dead_code: 22`, `fragile_debt: 14`
* *Architecture:* `io: 3`, `api: 215`, `import: 49`
* *Defense:* `safety: 177`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.001008 | `Ripple Effect (Closeness):` 0.06102
  * `Imports (Out-Degree: 23):` __future__, py, rpython.config.translationoption, rpython.jit.backend.llsupport.ffisupport, rpython.jit.codewriter, rpython.jit.codewriter.effectinfo, rpython.jit.codewriter.jitcode, rpython.jit.codewriter.liveness...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `rpython/rlib/rbigint.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4194.58 | **LOC:** 3668 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (61.2565%), Tech Debt (10.4172%)
**Top Internal Functions/Classes:**
  * `pow` **(Many-Argument Workhorses)** (Impact: 80.8)
  * `_format_recursive` **(Many-Argument Workhorses)** (Impact: 65.4)
  * `_int_bitwise` **(Many-Argument Workhorses)** (Impact: 62.1)
    * *Intent:* """ Bitwise and/or/xor operations """
  * `_bitwise` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* """ Bitwise and/or/xor operations """
  * `tobytes` **(Many-Argument Workhorses)** (Impact: 61.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 748 instances
* *State Mutation (weighted view):* 2313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 696`, `structural_boundaries: 632`, `args: 173`, `func_start: 173`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 817`, `dead_code: 17`, `planned_debt: 2`, `fragile_debt: 5`
* *Architecture:* `io: 5`, `api: 117`, `import: 17`
* *Defense:* `safety: 93`, `doc: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.773
  * `Choke Point (Betweenness):` 0.001022 | `Ripple Effect (Closeness):` 0.114963
  * `Imports (Out-Degree: 4):` math, rpython.annotator, rpython.rlib, rpython.rlib.debug, rpython.rlib.objectmodel, rpython.rlib.rarithmetic, rpython.rlib.rstring, rpython.rtyper...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `lib_pypy/cffi/_pycparser/ply/yacc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3736.02 | **LOC:** 3426 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (94.1226%), Tech Debt (28.7846%)
**Top Internal Functions/Classes:**
  * `yacc` **(Many-Argument Workhorses)** (Impact: 262.1)
    * *Intent:* # ----------------------------------------------------------------------------- # yacc(module) # # B...
  * `parsedebug` **(Many-Argument Workhorses)** (Impact: 162.3)
    * *Intent:* # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! # parsedebug(). # # ...
  * `parseopt` **(Many-Argument Workhorses)** (Impact: 139.1)
    * *Intent:* #--! parsedebug-end # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ...
  * `parseopt_notrack` **(Many-Argument Workhorses)** (Impact: 127.3)
    * *Intent:* #--! parseopt-end # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! # ...
  * `lr_parse_table` **(Compute Cores)** (Impact: 101.2)
    * *Intent:* # ----------------------------------------------------------------------------- # lr_parse_table() #...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 607 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 2066
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 583`, `structural_boundaries: 369`, `args: 110`, `func_start: 105`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 97`, `high_risk_execution: 3`, `state_mutation: 852`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 10`
* *Architecture:* `io: 27`, `api: 91`, `import: 10`
* *Defense:* `safety: 81`, `doc: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` , base64, inspect, os.path, re, sys, types, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rpython/translator/c/src/dtoa.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3549.34 | **LOC:** 3024 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.8377%), Tech Debt (21.1642%)
**Top Internal Functions/Classes:**
  * `__Py_dg_dtoa` **(Many-Argument Workhorses)** (Impact: 504.0)
    * *Intent:* call to __Py_dg_freedtoa. */
  * `__Py_dg_strtod` **(Many-Argument Workhorses)** (Impact: 361.5)
  * `bigcomp` **(Many-Argument Workhorses)** (Impact: 59.5)
    * *Intent:* Returns 0 on success, -1 on failure (e.g., due to a failed malloc call). */
  * `mult` **(Compute Cores)** (Impact: 48.1)
    * *Intent:* /* multiply two Bigints. Returns a new Bigint, or NULL on failure. Ignores the signs of a and b. */...
  * `quorem` **(Many-Argument Workhorses)** (Impact: 37.6)
    * *Intent:* bits (28--31) are zero and bit 27 is set. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 717 instances
* *State Mutation (weighted view):* 2166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 590`, `structural_boundaries: 133`, `args: 58`, `func_start: 32`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 732`, `dead_code: 3`, `fragile_debt: 9`, `unreferenced_by_name: 3`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `safety: 6`, `doc: 2`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` assert.h, errno.h, float.h, limits.h, asm.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib-python/2.7/test/test_descr.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3451.9 | **LOC:** 4984 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.7651%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_rich_comparisons` **(Defensive Guards)** (Impact: 36.5)
    * *Intent:* # Testing rich comparisons... class Z(complex): pass z = Z(1) self.assertEqual(z, 1+0j) self.assertE...
  * `test_basic_inheritance` **(Compute Cores)** (Impact: 32.4)
    * *Intent:* # Testing inheritance from basic types... class hexint(int): def __repr__(self): return hex(self) de...
  * `test_set_class` **(C Struct Operations)** (Impact: 26.5)
    * *Intent:* # Testing __class__ assignment... class C(object): pass class D(object): pass class E(object): pass ...
  * `test_metaclass` **(C Struct Operations)** (Impact: 24.4)
    * *Intent:* # Testing __metaclass__... class C: __metaclass__ = type def __init__(self): self.__state = 0 def ge...
  * `test_pickle_slots` **(Defensive Guards)** (Impact: 24.3)
    * *Intent:* # Testing pickling of classes with __slots__ ... import pickle, cPickle # Pickling of classes with _...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 294 instances
* *High Risk Execution (weighted view):* 17
* *State Mutation (weighted view):* 1371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 319`, `structural_boundaries: 1602`, `args: 462`, `func_start: 444`, `class_start: 401`
* *Risk/State:* `safety_bypasses: 300`, `high_risk_execution: 23`, `state_mutation: 783`, `dead_code: 1`, `fragile_debt: 29`, `duplicate_logic: 54`, `unreferenced_by_name: 131`
* *Architecture:* `io: 19`, `api: 382`, `import: 32`
* *Defense:* `safety: 245`, `doc: 5`, `test: 140`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` __builtin__, _testcapi, abc, binascii, cPickle, cStringIO, copy, copy_reg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra_tests/cffi_tests/test_c.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 3231.58 | **LOC:** 4527 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.6674%), Tech Debt (99.91%)
**Top Internal Functions/Classes:**
  * `_test_bitfield_details` **(Defensive Guards)** (Impact: 33.6)
  * `_test_wchar_variant` **(Defensive Guards)** (Impact: 30.7)
  * `test_buffer` **(Defensive Guards)** (Impact: 23.4)
  * `find_and_load_library` **(Defensive Guards)** (Impact: 18.1)
  * `check` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* #
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 317 instances
* *State Mutation (weighted view):* 2069
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 252`, `structural_boundaries: 1769`, `args: 276`, `func_start: 273`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 436`, `high_risk_execution: 1`, `state_mutation: 1435`, `dead_code: 2`, `fragile_debt: 6`, `duplicate_logic: 6`, `unreferenced_by_name: 231`
* *Architecture:* `io: 44`, `api: 268`, `import: 41`
* *Defense:* `safety: 1185`, `doc: 1`, `test: 539`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __builtin__, _cffi_backend, _weakref, array, builtins, ctypes.util, gc, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pypy/module/_cffi_backend/test/_backend_test_c.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 3212.68 | **LOC:** 4505 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.1996%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_test_bitfield_details` **(Defensive Guards)** (Impact: 33.6)
  * `_test_wchar_variant` **(Defensive Guards)** (Impact: 30.7)
  * `test_buffer` **(Defensive Guards)** (Impact: 23.4)
  * `find_and_load_library` **(Defensive Guards)** (Impact: 18.1)
  * `check` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* #
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 311 instances
* *State Mutation (weighted view):* 2052
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 1753`, `args: 275`, `func_start: 272`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 434`, `high_risk_execution: 1`, `state_mutation: 1430`, `dead_code: 2`, `fragile_debt: 7`, `duplicate_logic: 6`, `unreferenced_by_name: 231`
* *Architecture:* `io: 40`, `api: 268`, `import: 33`
* *Defense:* `safety: 1181`, `doc: 2`, `test: 534`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __builtin__, _cffi_backend, _weakref, array, builtins, contextlib, ctypes.util, gc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pypy/module/micronumpy/test/test_ndarray.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3188.24 | **LOC:** 4479 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.4524%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_fromstring` **(Defensive Guards)** (Impact: 20.8)
  * `test_subarrays` **(Defensive Guards)** (Impact: 17.9)
  * `test_data` **(Defensive Guards)** (Impact: 15.0)
  * `test_fromstring_types` **(Defensive Guards)** (Impact: 13.5)
  * `test_memoryview` **(Defensive Guards)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 288 instances
* *State Mutation (weighted view):* 1841
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 2589`, `args: 323`, `func_start: 320`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 1265`, `fragile_debt: 6`, `duplicate_logic: 2`, `unreferenced_by_name: 290`
* *Architecture:* `io: 40`, `api: 324`, `import: 342`
* *Defense:* `safety: 1521`, `test: 294`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` _weakref, array, cPickle, math, mmap, numpy, numpy.core.multiarray, operator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib-python/2.7/lib2to3/tests/test_fixers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 3167.26 | **LOC:** 4545 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.9153%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_prefix_preservation` **(Compute Cores)** (Impact: 19.6)
  * `assert_runs_after` **(Compute Cores)** (Impact: 12.8)
  * `test_call` **(Compute Cores)** (Impact: 10.5)
  * `test` **(Compute Cores)** (Impact: 9.2)
  * `test_import_from` **(Compute Cores)** (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 134 instances
* *State Mutation (weighted view):* 1615
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 832`, `args: 466`, `func_start: 462`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 1347`, `dead_code: 4`, `fragile_debt: 4`, `duplicate_logic: 114`, `unreferenced_by_name: 263`
* *Architecture:* `io: 16`, `api: 514`, `import: 13`
* *Defense:* `safety: 7`, `doc: 931`, `test: 442`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` , ..fixes.fix_imports, ..fixes.fix_imports2, ..fixes.fix_urllib, .foo, .green.eggs, __future__, a...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib-python/2.7/lib-tk/Tkinter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3143.22 | **LOC:** 3868 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.4312%), Tech Debt (99.636%)
**Top Internal Functions/Classes:**
  * `search` **(Many-Argument Workhorses)** (Impact: 39.1)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 30.3)
  * `_options` **(Defensive Guards)** (Impact: 27.3)
    * *Intent:* """Internal function."""
  * `_grid_configure` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* """Internal function."""
  * `_stringify` **(Defensive Guards)** (Impact: 19.7)
    * *Intent:* """Internal function."""
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 268 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 949
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 297`, `structural_boundaries: 984`, `args: 516`, `func_start: 515`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 89`, `high_risk_execution: 1`, `state_mutation: 413`, `fragile_debt: 11`, `duplicate_logic: 38`
* *Architecture:* `io: 20`, `api: 482`, `import: 12`
* *Defense:* `safety: 73`, `doc: 504`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.354
  * `Choke Point (Betweenness):` 0.000137 | `Ripple Effect (Closeness):` 0.015192
  * `Imports (Out-Degree: 4):` FixTk, Tkconstants, Tkinter, _tkinter, os, re, sys, traceback...
  * `Imported By (In-Degree: 81):` (Excluded from Brief to save tokens)

### `lib-python/2.7/pydoc.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3060.98 | **LOC:** 2424 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.5287%), Tech Debt (57.6638%)
**Top Internal Functions/Classes:**
  * `docmodule` **(Many-Argument Workhorses)** (Impact: 111.6)
    * *Intent:* """Produce HTML documentation for a module object."""
  * `docclass` **(Many-Argument Workhorses)** (Impact: 92.4)
  * `docmodule` **(Many-Argument Workhorses)** (Impact: 85.4)
    * *Intent:* """Produce text documentation for a given module object."""
  * `docclass` **(Many-Argument Workhorses)** (Impact: 74.5)
    * *Intent:* """Produce text documentation for a given class object."""
  * `docroutine` **(Many-Argument Workhorses)** (Impact: 71.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Rce:* 6 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 421 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 14
* *Sec Tainted Injection (weighted view):* 6
* *State Mutation (weighted view):* 1370
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 544`, `structural_boundaries: 468`, `args: 188`, `func_start: 148`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 73`, `high_risk_execution: 8`, `state_mutation: 528`, `dead_code: 4`, `fragile_debt: 3`, `duplicate_logic: 12`
* *Architecture:* `io: 88`, `api: 147`, `concurrency: 4`, `import: 24`
* *Defense:* `safety: 119`, `doc: 93`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.000235 | `Ripple Effect (Closeness):` 0.002376
  * `Imports (Out-Degree: 20):` BaseHTTPServer, StringIO, Tkinter, __builtin__, collections, error, formatter, getopt...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pypy/module/micronumpy/types.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3035.74 | **LOC:** 2770 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.7675%), Tech Debt (99.9467%)
**Top Internal Functions/Classes:**
  * `record_coerce` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `make_integer_min_dtype` **(Type Conversions)** (Impact: 33.2)
  * `_coerce` **(Many-Argument Workhorses)** (Impact: 26.7)
    * *Intent:* # TODO: Make sure the shape and the array match from pypy.module.micronumpy.descriptor import W_Dtyp...
  * `floordiv` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `pow` **(Compute Cores)** (Impact: 18.9)
    * *Intent:* #complex mod does not exist in numpy #@simple_binary_op #def mod(self, v1, v2): # return math.fmod(v...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 273 instances
* *State Mutation (weighted view):* 992
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 1055`, `args: 378`, `func_start: 376`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 446`, `dead_code: 24`, `planned_debt: 3`, `fragile_debt: 8`, `duplicate_logic: 54`
* *Architecture:* `api: 381`, `import: 29`
* *Defense:* `safety: 182`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.035396
  * `Imports (Out-Degree: 21):` , functools, math, pypy.interpreter.baseobjspace, pypy.interpreter.error, pypy.module.micronumpy, pypy.module.micronumpy.base, pypy.module.micronumpy.concrete...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib-python/2.7/lib-tk/turtle.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2912.9 | **LOC:** 4035 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.984%), Tech Debt (17.7846%)
**Top Internal Functions/Classes:**
  * `pen` **(Many-Argument Workhorses)** (Impact: 59.7)
    * *Intent:* """Return or set the pen's attributes. Arguments: pen -- a dictionary with some or all of the below ...
  * `_undogoto` **(Compute Cores)** (Impact: 39.6)
    * *Intent:* """Reverse a _goto. Used for undo() """
  * `_drawturtle` **(Compute Cores)** (Impact: 32.3)
    * *Intent:* """Manages the correct rendering of the turtle with respect to its shape, resizemode, stretch and ti...
  * `dot` **(Many-Argument Workhorses)** (Impact: 28.5)
    * *Intent:* """Draw a dot with diameter size, using color. Optional arguments: size -- an integer >= 1 (if given...
  * `circle` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* """ Draw a circle with given radius. Arguments: radius -- a number extent (optional) -- a number ste...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 423 instances
* *High Risk Execution (weighted view):* 4
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 1432
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 425`, `structural_boundaries: 372`, `args: 216`, `func_start: 214`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 6`, `state_mutation: 586`, `dead_code: 6`, `fragile_debt: 3`, `duplicate_logic: 3`
* *Architecture:* `io: 3`, `api: 146`, `import: 11`
* *Defense:* `safety: 50`, `doc: 183`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Tkinter, can, copy, directory, math, os, os.path, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rpython/rtyper/test/test_rpbc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2877.76 | **LOC:** 2218 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.1185%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `f` **(Compute Cores)** (Impact: 45.8)
  * `test_call_star_and_keywords_starargs` **(Compute Cores)** (Impact: 41.1)
  * `f` **(Compute Cores)** (Impact: 23.8)
  * `test_call_star_and_keywords` **(Compute Cores)** (Impact: 22.9)
  * `test_call_keywords` **(Compute Cores)** (Impact: 19.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 299 instances
* *State Mutation (weighted view):* 1119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 1165`, `args: 406`, `func_start: 404`, `class_start: 104`
* *Risk/State:* `safety_bypasses: 58`, `high_risk_execution: 7`, `state_mutation: 521`, `dead_code: 4`, `fragile_debt: 1`, `duplicate_logic: 73`, `unreferenced_by_name: 104`
* *Architecture:* `api: 292`, `import: 48`
* *Defense:* `safety: 187`, `test: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` py, rpython.annotator, rpython.config.translationoption, rpython.rlib.cache, rpython.rlib.nonconst, rpython.rlib.objectmodel, rpython.rtyper, rpython.rtyper.llannotation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rpython/rlib/rvmprof/src/shared/libbacktrace/dwarf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2863.64 | **LOC:** 3039 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.7227%), Tech Debt (14.1775%)
**Top Internal Functions/Classes:**
  * `read_function_entry` **(Many-Argument Workhorses)** (Impact: 228.6)
    * *Intent:* /* Read one entry plus all its children. Add function addresses to VEC. Returns 1 on success, 0 on e...
  * `find_address_ranges` **(Many-Argument Workhorses)** (Impact: 158.9)
    * *Intent:* read, 0 if there is some error. */
  * `read_line_program` **(Many-Argument Workhorses)** (Impact: 118.6)
    * *Intent:* /* Read the line program, adding line mappings to VEC. Return 1 on success, 0 on failure. */
  * `read_attribute` **(Many-Argument Workhorses)** (Impact: 112.4)
    * *Intent:* *IS_VALID to 1. We don't try to store the value of other attribute forms, because we don't care abou...
  * `dwarf_lookup_pc` **(Many-Argument Workhorses)** (Impact: 98.5)
    * *Intent:* 0 if not. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 421 instances
* *State Mutation (weighted view):* 1336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 450`, `structural_boundaries: 545`, `args: 47`, `func_start: 46`, `class_start: 108`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 494`, `fragile_debt: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 70`, `immutability_locks: 129`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` backtrace.h, config.h, dwarf2.h, errno.h, filenames.h, internal.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pypy/objspace/std/listobject.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2829.58 | **LOC:** 2530 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.5137%), Tech Debt (79.9323%)
**Top Internal Functions/Classes:**
  * `setslice` **(Many-Argument Workhorses)** (Impact: 48.3)
  * `descr_sort` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* """ L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*; cmp(x, y) -> -1, 0, 1"""
  * `find_or_count` **(Many-Argument Workhorses)** (Impact: 35.5)
  * `_safe_find_or_count` **(Many-Argument Workhorses)** (Impact: 32.9)
  * `get_strategy_from_list_object` **(Compute Cores)** (Impact: 25.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 313 instances
* *State Mutation (weighted view):* 1130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 773`, `args: 316`, `func_start: 307`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 504`, `dead_code: 2`, `fragile_debt: 7`, `duplicate_logic: 15`
* *Architecture:* `io: 3`, `api: 272`, `import: 29`
* *Defense:* `safety: 103`, `doc: 45`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.326
  * `Choke Point (Betweenness):` 0.001007 | `Ripple Effect (Closeness):` 0.062928
  * `Imports (Out-Degree: 20):` math, operator, pypy.interpreter.baseobjspace, pypy.interpreter.error, pypy.interpreter.gateway, pypy.interpreter.miscutils, pypy.interpreter.signature, pypy.interpreter.typedef...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `rpython/jit/backend/x86/assembler.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2747.2 | **LOC:** 2782 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.8716%), Tech Debt (14.3599%)
**Top Internal Functions/Classes:**
  * `_build_wb_slowpath` **(Many-Argument Workhorses)** (Impact: 59.0)
  * `assemble_loop` **(Many-Argument Workhorses)** (Impact: 40.8)
  * `_build_malloc_slowpath` **(Many-Argument Workhorses)** (Impact: 37.7)
    * *Intent:* """ While arriving on slowpath, we have a gcpattern on stack 0. The arguments are passed in ecx and ...
  * `load_from_mem` **(Many-Argument Workhorses)** (Impact: 35.5)
    * *Intent:* # ----------
  * `generate_body` **(Many-Argument Workhorses)** (Impact: 33.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 311 instances
* *State Mutation (weighted view):* 1256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 387`, `structural_boundaries: 409`, `args: 177`, `func_start: 177`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 634`, `dead_code: 16`, `planned_debt: 5`, `fragile_debt: 8`
* *Architecture:* `io: 1`, `api: 143`, `import: 39`
* *Defense:* `safety: 171`, `doc: 10`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 5.3e-05 | `Ripple Effect (Closeness):` 0.0008
  * `Imports (Out-Degree: 25):` __future__, itertools, pdb, rpython.jit.backend.llsupport, rpython.jit.backend.llsupport.asmmemmgr, rpython.jit.backend.llsupport.assembler, rpython.jit.backend.llsupport.descr, rpython.jit.backend.llsupport.gcmap...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `rpython/memory/gc/incminimark.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2744.94 | **LOC:** 3407 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.2423%), Tech Debt (32.1574%)
**Top Internal Functions/Classes:**
  * `major_collection_step` **(Many-Argument Workhorses)** (Impact: 61.2)
    * *Intent:* # Note - minor collections seem fast enough so that one # is done before every major collection step
  * `external_malloc` **(Many-Argument Workhorses)** (Impact: 53.7)
    * *Intent:* # XXX kill alloc_young and make it always True """Allocate a large object using the ArenaCollection ...
  * `writebarrier_before_copy` **(Many-Argument Workhorses)** (Impact: 45.9)
  * `_minor_collection` **(Compute Cores)** (Impact: 44.4)
    * *Intent:* # ---------- # Nursery collection """Perform a minor collection: find the objects from the nursery t...
  * `_trace_drag_out` **(Many-Argument Workhorses)** (Impact: 38.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 419 instances
* *State Mutation (weighted view):* 1470
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 335`, `args: 150`, `func_start: 150`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 632`, `dead_code: 23`, `planned_debt: 2`, `fragile_debt: 21`
* *Architecture:* `io: 3`, `api: 106`, `import: 25`
* *Defense:* `safety: 10`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.183
  * `Choke Point (Betweenness):` 8.1e-05 | `Ripple Effect (Closeness):` 0.001473
  * `Imports (Out-Degree: 10):` os, rpython.memory.gc, rpython.memory.gc.base, rpython.memory.gc.minimarkpage, rpython.memory.support, rpython.rlib, rpython.rlib.debug, rpython.rlib.objectmodel...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `rpython/rlib/runicode.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2735.82 | **LOC:** 1901 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (92.8228%), Tech Debt (15.0753%)
**Top Internal Functions/Classes:**
  * `str_decode_unicode_escape` **(Many-Argument Workhorses)** (Impact: 109.0)
  * `str_decode_utf_7` **(Many-Argument Workhorses)** (Impact: 96.9)
  * `str_decode_utf_16_helper` **(Many-Argument Workhorses)** (Impact: 95.8)
  * `make_unicode_escape_function` **(Many-Argument Workhorses)** (Impact: 85.9)
  * `str_decode_utf_32_helper` **(Many-Argument Workhorses)** (Impact: 85.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 422 instances
* *State Mutation (weighted view):* 1301
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 269`, `args: 77`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 457`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 7`
* *Architecture:* `io: 3`, `api: 65`, `import: 8`
* *Defense:* `safety: 21`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.077641
  * `Imports (Out-Degree: 4):` rpython.rlib, rpython.rlib.objectmodel, rpython.rlib.rarithmetic, rpython.rlib.rstring, rpython.rlib.unicodedata, rpython.rtyper.lltypesystem, rpython.tool.sourcetools, sys
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `lib-python/2.7/tarfile.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2672.44 | **LOC:** 2633 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.5185%), Tech Debt (16.0057%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 121.1)
  * `gettarinfo` **(Many-Argument Workhorses)** (Impact: 67.5)
    * *Intent:* """Create a TarInfo object from the result of os.stat or equivalent on an existing file. The file is...
  * `open` **(Many-Argument Workhorses)** (Impact: 51.4)
    * *Intent:* #-------------------------------------------------------------------------- # Below are the classmet...
  * `add` **(Many-Argument Workhorses)** (Impact: 40.0)
    * *Intent:* """Add the file `name' to the archive. `name' may be any type of file (directory, fifo, symbolic lin...
  * `_extract_member` **(Many-Argument Workhorses)** (Impact: 34.0)
    * *Intent:* """Extract the TarInfo object tarinfo to a physical file called targetpath. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 373 instances
* *State Mutation (weighted view):* 1291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 420`, `args: 146`, `func_start: 144`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 545`, `dead_code: 11`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 64`, `api: 115`, `import: 23`
* *Defense:* `safety: 101`, `doc: 116`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.000479 | `Ripple Effect (Closeness):` 0.13116
  * `Imports (Out-Degree: 9):` StringIO, __builtin__, bz2, cStringIO, calendar, copy, errno, grp...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pypy/objspace/std/mapdict.py` -> Churn: **100.0%** | Cog Load: 87.9505% | Debt: 47.9351%
- `rpython/rlib/rbigint.py` -> Churn: **76.8%** | Cog Load: 61.2565% | Debt: 10.4172%
- `rpython/rlib/rsignal.py` -> Churn: **60.86%** | Cog Load: 67.6364% | Debt: 51.3683%
- `rpython/rtyper/lltypesystem/ll2ctypes.py` -> Churn: **60.86%** | Cog Load: 89.5228% | Debt: 50.4771%
- `rpython/translator/c/src/signals.c` -> Churn: **60.86%** | Cog Load: 70.4947% | Debt: 97.6367%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `rpython/jit/metainterp/pyjitpl.py` -> **CF Bolz-Tereick** (100.0% isolated ownership) | Magnitude: 4369.84
- `lib_pypy/cffi/_pycparser/ply/yacc.py` -> **Charalampos Stratakis** (100.0% isolated ownership) | Magnitude: 3736.02
- `rpython/rlib/runicode.py` -> **mattip** (100.0% isolated ownership) | Magnitude: 2735.82
- `rpython/jit/codewriter/jtransform.py` -> **CF Bolz-Tereick** (100.0% isolated ownership) | Magnitude: 2607.16
- `rpython/rtyper/lltypesystem/ll2ctypes.py` -> **mattip** (100.0% isolated ownership) | Magnitude: 2208.8

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pypy/interpreter/baseobjspace.py` -> **Severity: 1.191** (Bridge: 0.0119 * Flux: 99.9998%)
- `rpython/annotator/annrpython.py` -> **Severity: 1.19** (Bridge: 0.0119 * Flux: 100.0%)
- `pypy/interpreter/module.py` -> **Severity: 0.966** (Bridge: 0.0097 * Flux: 100.0%)
- `rpython/rtyper/extfuncregistry.py` -> **Severity: 0.889** (Bridge: 0.0089 * Flux: 99.8341%)
- `rpython/rlib/debug.py` -> **Severity: 0.727** (Bridge: 0.0073 * Flux: 99.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib-python/2.7/os.py` -> **Severity: 28.501** (Embedded: 0.3114 * Error Risk: 91.5297%)
- `lib-python/2.7/re.py` -> **Severity: 22.605** (Embedded: 0.2286 * Error Risk: 98.8976%)
- `lib-python/2.7/copy_reg.py` -> **Severity: 22.39** (Embedded: 0.2285 * Error Risk: 97.988%)
- `lib-python/2.7/subprocess.py` -> **Severity: 21.296** (Embedded: 0.2166 * Error Risk: 98.3012%)
- `lib-python/2.7/ntpath.py` -> **Severity: 20.825** (Embedded: 0.2099 * Error Risk: 99.2066%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib-python/2.7/os.py` -> **Severity: 2817.713** (Blast Radius: 58.416 * Doc Risk: 48.2353%)
- `lib-python/2.7/copy_reg.py` -> **Severity: 1727.756** (Blast Radius: 25.131 * Doc Risk: 68.75%)
- `_pytest/unittest.py` -> **Severity: 1331.454** (Blast Radius: 13.858 * Doc Risk: 96.0784%)
- `lib-python/2.7/re.py` -> **Severity: 1215.866** (Blast Radius: 19.896 * Doc Risk: 61.1111%)
- `rpython/rlib/rarithmetic.py` -> **Severity: 990.117** (Blast Radius: 11.519 * Doc Risk: 85.9551%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
