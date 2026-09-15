# ARCHITECTURAL_BRIEF: nasm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/netwide-assembler/nasm.git` |
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
| Total Artifacts | 1337 |
| Analyzed Artifacts (Scanned) | 247 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1090 |
| Total LOC | 55740 |
| Volatility Index | 0.012 |
| % Scanned of codebase = | 18.5% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3207 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3204 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9321 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 9 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 141 | 45564 | 57.1% |
| M4 | 39 | 554 | 15.8% |
| PERL | 36 | 7909 | 14.6% |
| PLAINTEXT | 10 | 0 | 4.0% |
| MARKDOWN | 6 | 0 | 2.4% |
| MAKEFILE | 5 | 817 | 2.0% |
| SHELL | 4 | 131 | 1.6% |
| CSS | 2 | 239 | 0.8% |
| BATCH | 1 | 5 | 0.4% |
| ASSEMBLY | 1 | 0 | 0.4% |
| PYTHON | 1 | 504 | 0.4% |
| JSON | 1 | 17 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled App` (z -1.20; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 21%, Large Core Modules 19%, Declarative / Non-Code 18%, Compute Cores Files 9%, Interface Declarations Files 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 231 | 93.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 16 | 6.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1090*

**Composition by Extension & Reason:**
- `.asm`: 472x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.t`: 217x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 191x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 86x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.src`: 24x Excluded (Unsupported Extension: '.src')
- `.mac`: 22x Excluded (Unsupported Extension: '.mac')
- `no_extension`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 349 LOC)
- `.sh`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 23 LOC)
- `.pl`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 362 LOC), 1x Excluded (Machine-Generated Source Code Signature: 36 LOC)
- `.c`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 81 LOC), 1x Excluded (Machine-Generated Source Code Signature: 300 LOC)
- `.dat`: 6x Excluded (Unsupported Extension: '.dat')
- `.in`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 672 LOC)
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 231 LOC), 1x Excluded (Machine-Generated Source Code Signature: 33 LOC), 1x Excluded (Embedded Hex Payload: 37664 hex tokens in 9447 LOC)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.0 | 36.0 | 13.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 50.8 | 64.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 32.2 | 11.9 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 20.5 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.3 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 48.2 | 23.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 92.7 | 2.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 82.3 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.4 | 1.4 | 2.1 | 2.2 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 91.3 | 10.2 | 5.0 | 5.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 72.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 13566 | 145 | 118 | `asm/preproc.c` |
| cleanup | 169 | 48 | 2 | `Mkfiles/openwcom.mak` |
| guards | 3617 | 137 | 35 | `asm/preproc.c` |
| danger | 569 | 71 | 8 | `x86/insns.pl` |
| concurrency | 121 | 4 | 0 | `Mkfiles/openwcom.mak` |
| connectivity | 1472 | 173 | 15 | `include/nasm.h` |
| io | 221 | 46 | 2 | `travis/nasm-t.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 19 | 6 | 0 | `output/outelf.c` |
| time | 12 | 5 | 0 | `asm/nasm.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 702 | 29 | 1 | `doc/rdsrc.pl` |
| events | 27 | 10 | 0 | `autoconf/m4/pa_func_attribute.m4` |
| tests | 8 | 1 | 0 | `travis/nasm-t.py` |
| docs | 12 | 4 | 0 | `asm/error.c` |
| debt | 1284 | 69 | 10 | `doc/rdsrc.pl` |
| mutation | 18153 | 147 | 179 | `asm/preproc.c` |
| dead_code | 381 | 129 | 5 | `zlib/inflate.c` |
| credential | 0 | 0 | 0 | - |
| threat | 563 | 51 | 6 | `asm/preproc.c` |
| ml_ai | 15 | 11 | 0 | `output/outbin.c` |
| ui | 30 | 9 | 0 | `doc/nasmdoc.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.3571**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `travis/nasm-t.py` (Hits: 32)
- `misc/nasmstab` (Hits: 17)
- `autogen.sh` (Hits: 17)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **compiler.h** (`include/compiler.h`) — 81 inbound connections
2. **nasmlib.h** (`include/nasmlib.h`) — 58 inbound connections
3. **nasm.h** (`include/nasm.h`) — 41 inbound connections
4. **error.h** (`include/error.h`) — 34 inbound connections
5. **nctype.h** (`include/nctype.h`) — 25 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **compiler.h** (`include/compiler.h`) — 24 outbound dependencies
2. **nasm.c** (`asm/nasm.c`) — 20 outbound dependencies
3. **outelf.c** (`output/outelf.c`) — 17 outbound dependencies
4. **directiv.c** (`asm/directiv.c`) — 16 outbound dependencies
5. **outmacho.c** (`output/outmacho.c`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `byte_code_compile` **(Many-Argument Workhorses)** (@ `x86/insns.pl`) -> Impact: **895.3** | LOC: 599
  * *Intent:* # # The operands word lists the order of the operands: # # r = register field in the modr/m # m = modr/m # v = VEX "v" field or DFV # i = immediate # ...
- `do_directive` **(Many-Argument Workhorses)** (@ `asm/preproc.c`) -> Impact: **621.0** | LOC: 1101
  * *Intent:* /** * find and process preprocessor directive in passed line * Find out if a line contains a preprocessor directive, and deal * with it if so. * * If ...
- `matches` **(Many-Argument Workhorses)** (@ `disasm/disasm.c`) -> Impact: **534.5** | LOC: 811
  * *Intent:* * corresponds to the data stream in data and parse it into "ins" if * so. "ins" has already been partially initialized in disasm() to * point contain ...
- `process_ea` **(Many-Argument Workhorses)** (@ `asm/assemble.c`) -> Impact: **523.3** | LOC: 466
- `parse_line` **(Many-Argument Workhorses)** (@ `asm/parser.c`) -> Impact: **482.0** | LOC: 720
- `inflate` **(Many-Argument Workhorses)** (@ `zlib/inflate.c`) -> Impact: **414.8** | LOC: 675
  * *Intent:* */
- `disasm` **(Many-Argument Workhorses)** (@ `disasm/disasm.c`) -> Impact: **362.1** | LOC: 401
- `process_arg` **(Many-Argument Workhorses)** (@ `asm/nasm.c`) -> Impact: **333.7** | LOC: 394
- `calcsize` **(Compute Cores)** (@ `asm/assemble.c`) -> Impact: **326.0** | LOC: 722
  * *Intent:* /* Common construct */ #define case3(x) case (x): case (x)+1: case (x)+2 #define case4(x) case3(x): case (x)+3 /* * calcsize() is assumed to be proces...
- `tokenize` **(Compute Cores)** (@ `asm/preproc.c`) -> Impact: **296.2** | LOC: 408
  * *Intent:* /* * Tokenize a line of text. This is a very simple process since we * don't need to parse the value out of e.g. numeric tokens: we * simply split one...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `asm` | 34 | 23656.06 | 51.97% | 23.92% |
| `output` | 22 | 14946.36 | 43.88% | 16.0% |
| `zlib` | 15 | 4738.8 | 41.96% | 22.08% |
| `x86` | 7 | 4156.9 | 51.13% | 13.57% |
| `disasm` | 7 | 3598.86 | 51.28% | 30.6% |
| `doc` | 14 | 3212.71 | 44.7% | 19.31% |
| `nasmlib` | 28 | 2627.28 | 48.17% | 53.56% |
| `misc` | 11 | 1473.26 | 47.82% | 19.15% |
| `include` | 24 | 1135.78 | 16.87% | 4.43% |
| `travis` | 3 | 632.96 | 26.25% | 4.71% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `autoconf/m4/pa_func_attribute.m4` -> **100.0%** Exposure
- `common/errstubs.c` -> **99.9729%** Exposure
- `asm/srcfile.c` -> **99.9447%** Exposure
- `autoconf/m4/pa_prog_cc.m4` -> **99.929%** Exposure
- `autoconf/m4/pa_variadic_macros.m4` -> **99.929%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `asm/assemble.c` -> **100.0%** Exposure
- `asm/directiv.c` -> **100.0%** Exposure
- `asm/eval.c` -> **100.0%** Exposure
- `asm/exprlib.c` -> **100.0%** Exposure
- `asm/floats.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `asm/preproc.c` -> **16** Orphaned Functions | **0** Duplicates
- `nasmlib/saa.c` -> **15** Orphaned Functions | **0** Duplicates
- `zlib/inflate.c` -> **14** Orphaned Functions | **0** Duplicates
- `asm/error.c` -> **10** Orphaned Functions | **0** Duplicates
- `output/outlib.c` -> **10** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `663` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `nasmlib/saa.c` (C) -> Cumulative Risk: **686.82**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.48)
- **Magnitude:** 371.66 | **LOC:** 357 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.3906%)
- **Heaviest Functions:** `saa_wbytes` (Many-Argument Workhorses, Impact: 19.4), `saa_fwrite` (Many-Argument Workhorses, Impact: 14.9), `saa_rbytes` (Defensive Guards, Impact: 10.1)

### 2. `asm/exprlib.c` (C) -> Cumulative Risk: **678.66**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.73)
- **Magnitude:** 173.18 | **LOC:** 181 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.708%)
- **Heaviest Functions:** `expr_class` (Compute Cores, Impact: 40.5), `is_simple` (Compute Cores, Impact: 14.9), `is_really_simple` (Compute Cores, Impact: 13.5)

### 3. `zlib/zutil.c` (C) -> Cumulative Risk: **671.7**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.43)
- **Magnitude:** 198.78 | **LOC:** 300 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (97.8298%)
- **Heaviest Functions:** `zlibCompileFlags` (Compute Cores, Impact: 30.1), `zcalloc` (Many-Argument Workhorses, Impact: 13.2), `zcfree` (Compute Cores, Impact: 9.8)

### 4. `asm/nasm.c` (C) -> Cumulative Risk: **671.14**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.40)
- **Magnitude:** 2082.04 | **LOC:** 2170 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 61.1%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.4887%)
- **Heaviest Functions:** `process_arg` (Many-Argument Workhorses, Impact: 333.7), `help` (Compute Cores, Impact: 179.0), `main` (Many-Argument Workhorses, Impact: 99.3)

### 5. `asm/preproc.c` (C) -> Cumulative Risk: **668.42**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.69)
- **Magnitude:** 8440.58 | **LOC:** 9262 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 54.2%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.7507%), Cognitive Load (94.8689%)
- **Heaviest Functions:** `do_directive` (Many-Argument Workhorses, Impact: 621.0), `tokenize` (Compute Cores, Impact: 296.2), `if_condition` (Many-Argument Workhorses, Impact: 187.6)

### 6. `nasmlib/file.c` (C) -> Cumulative Risk: **666.71**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.06)
- **Magnitude:** 198.92 | **LOC:** 405 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 71.4%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9794%), Safety Score (83.9496%)
- **Heaviest Functions:** `nasm_open_read` (Compute Cores, Impact: 22.8), `nasm_open_write` (Compute Cores, Impact: 19.2), `nasm_file_size` (Compute Cores, Impact: 13.1)

### 7. `x86/preinsns.pl` (PERL) -> Cumulative Risk: **658.3**
- **Archetype:** `file_cluster_1` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.62)
- **Magnitude:** 900.52 | **LOC:** 669 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.2637%)
- **Heaviest Functions:** `func_multisize` (Compute Cores, Impact: 289.8), `process_insn` (Compute Cores, Impact: 29.4), `substitute` (Compute Cores, Impact: 27.7)

### 8. `asm/assemble.c` (C) -> Cumulative Risk: **657.45**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.22)
- **Magnitude:** 4346.72 | **LOC:** 4164 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 47.6%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.6268%)
- **Heaviest Functions:** `process_ea` (Many-Argument Workhorses, Impact: 523.3), `calcsize` (Compute Cores, Impact: 326.0), `matches` (Many-Argument Workhorses, Impact: 250.7)

### 9. `x86/insns.pl` (PERL) -> Cumulative Risk: **655.43**
- **Archetype:** `file_cluster_1` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.07)
- **Magnitude:** 2658.18 | **LOC:** 1672 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 44.4%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.6383%)
- **Heaviest Functions:** `byte_code_compile` (Many-Argument Workhorses, Impact: 895.3), `format_insn` (Many-Argument Workhorses, Impact: 183.7), `relaxed_forms` (Compute Cores, Impact: 52.5)

### 10. `asm/labels.c` (C) -> Cumulative Risk: **653.43**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.66)
- **Magnitude:** 588.94 | **LOC:** 720 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.9718%)
- **Heaviest Functions:** `define_label` (Many-Argument Workhorses, Impact: 72.8), `declare_label_lptr` (Many-Argument Workhorses, Impact: 50.6), `out_symdef` (Compute Cores, Impact: 30.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `asm/preproc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 8440.58 | **LOC:** 9262 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 54.2%
- **Risk Profile:** Cognitive Load (94.8689%), Tech Debt (13.548%)
**Top Internal Functions/Classes:**
  * `do_directive` **(Many-Argument Workhorses)** (Impact: 621.0)
    * *Intent:* /** * find and process preprocessor directive in passed line * Find out if a line contains a preproc...
  * `tokenize` **(Compute Cores)** (Impact: 296.2)
    * *Intent:* /* * Tokenize a line of text. This is a very simple process since we * don't need to parse the value...
  * `if_condition` **(Many-Argument Workhorses)** (Impact: 187.6)
    * *Intent:* /* * Determine whether one of the various `if' conditions is true or * not. * * We must free the tli...
  * `expand_smacro_with_params` **(Many-Argument Workhorses)** (Impact: 110.0)
    * *Intent:* /* * Expand one single-line macro instance given a specific macro and a * specific set of parameters...
  * `parse_smacro_template` **(Compute Cores)** (Impact: 89.3)
    * *Intent:* * is set, set the nparam, varadic and params field in the template. * The varadic field is not used ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1496 instances
* *State Mutation (weighted view):* 4685
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1625`, `structural_boundaries: 1168`, `args: 353`, `func_start: 211`, `class_start: 117`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 1693`, `planned_debt: 4`, `fragile_debt: 6`, `unreferenced_by_name: 16`
* *Architecture:* `io: 1`, `api: 43`, `import: 15`
* *Defense:* `safety: 44`, `doc: 2`, `immutability_locks: 228`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` assemble.h, compiler.h, dbginfo.h, error.h, eval.h, hashtbl.h, listing.h, nasm.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/assemble.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 4346.72 | **LOC:** 4164 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 47.6%
- **Risk Profile:** Cognitive Load (97.5752%), Tech Debt (11.2164%)
**Top Internal Functions/Classes:**
  * `process_ea` **(Many-Argument Workhorses)** (Impact: 523.3)
  * `calcsize` **(Compute Cores)** (Impact: 326.0)
    * *Intent:* /* Common construct */ #define case3(x) case (x): case (x)+1: case (x)+2 #define case4(x) case3(x): ...
  * `matches` **(Many-Argument Workhorses)** (Impact: 250.7)
  * `gencode` **(Many-Argument Workhorses)** (Impact: 211.2)
  * `prefix_byte` **(Compute Cores)** (Impact: 84.1)
    * *Intent:* /* * Return the byte value of a legacy prefix (possibly depending on context) * Returns one of the e...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 639 instances
* *State Mutation (weighted view):* 1982
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1143`, `structural_boundaries: 574`, `args: 127`, `func_start: 61`, `class_start: 26`
* *Risk/State:* `state_mutation: 704`, `dead_code: 1`, `fragile_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 10`
* *Defense:* `safety: 17`, `immutability_locks: 114`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` assemble.h, compiler.h, dbginfo.h, disp8.h, error.h, insns.h, listing.h, nasm.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outelf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3094.38 | **LOC:** 3636 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (91.7092%), Tech Debt (9.3116%)
**Top Internal Functions/Classes:**
  * `elf_deflabel` **(Many-Argument Workhorses)** (Impact: 211.0)
  * `elf_section_attrib` **(Many-Argument Workhorses)** (Impact: 187.4)
    * *Intent:* /* parse section attributes */
  * `elf64_out` **(Compute Cores)** (Impact: 156.8)
  * `elfx32_out` **(Compute Cores)** (Impact: 129.4)
  * `elf32_out` **(Compute Cores)** (Impact: 100.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 518 instances
* *State Mutation (weighted view):* 1743
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 625`, `structural_boundaries: 461`, `args: 108`, `func_start: 52`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 707`, `dead_code: 7`, `fragile_debt: 4`
* *Architecture:* `api: 14`, `import: 17`
* *Defense:* `safety: 19`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` compiler.h, dwarf.h, elf.h, error.h, eval.h, hashtbl.h, nasm.h, nasmlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outobj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2782.24 | **LOC:** 2822 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (93.0445%), Tech Debt (10.3817%)
**Top Internal Functions/Classes:**
  * `obj_deflabel` **(Many-Argument Workhorses)** (Impact: 181.9)
  * `obj_directive` **(Compute Cores)** (Impact: 169.6)
  * `obj_segment` **(Compute Cores)** (Impact: 153.3)
  * `obj_write_fixup` **(Many-Argument Workhorses)** (Impact: 150.4)
  * `obj_write_file` **(Compute Cores)** (Impact: 104.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 511 instances
* *State Mutation (weighted view):* 1636
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 524`, `structural_boundaries: 300`, `args: 66`, `func_start: 43`, `class_start: 88`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 614`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `api: 8`, `import: 12`
* *Defense:* `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` asmutil.h, compiler.h, ctype.h, error.h, eval.h, nasm.h, nasmlib.h, nctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x86/insns.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 2658.18 | **LOC:** 1672 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (97.9819%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `byte_code_compile` **(Many-Argument Workhorses)** (Impact: 895.3)
    * *Intent:* # # The operands word lists the order of the operands: # # r = register field in the modr/m # m = mo...
  * `format_insn` **(Many-Argument Workhorses)** (Impact: 183.7)
  * `relaxed_forms` **(Compute Cores)** (Impact: 52.5)
    * *Intent:* # Generate relaxed form patterns if applicable # * is used for an optional source operand, duplicati...
  * `decodify` **(Many-Argument Workhorses)** (Impact: 35.4)
    * *Intent:* # # Turn a code string into a sequence of bytes #
  * `startseq` **(Compute Cores)** (Impact: 32.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 430 instances
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 1290
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 694`, `structural_boundaries: 255`, `args: 24`, `func_start: 15`
* *Risk/State:* `state_mutation: 430`, `dead_code: 1`
* *Architecture:* `io: 8`, `api: 15`, `import: 3`
* *Defense:* `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bytecode, explicit, ndmask, of, position, the
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `disasm/disasm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2469.66 | **LOC:** 1801 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (96.2255%), Tech Debt (8.3643%)
**Top Internal Functions/Classes:**
  * `matches` **(Many-Argument Workhorses)** (Impact: 534.5)
    * *Intent:* * corresponds to the data stream in data and parse it into "ins" if * so. "ins" has already been par...
  * `disasm` **(Many-Argument Workhorses)** (Impact: 362.1)
  * `do_ea` **(Many-Argument Workhorses)** (Impact: 127.8)
    * *Intent:* /* * Process an effective address (ModRM) specification. */
  * `eatbyte` **(Many-Argument Workhorses)** (Impact: 93.3)
    * *Intent:* /* * This is called when we don't have a complete instruction. If it * is a standalone *single-byte*...
  * `append_evex_reg_deco` **(Many-Argument Workhorses)** (Impact: 21.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 397 instances
* *State Mutation (weighted view):* 1218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 484`, `structural_boundaries: 267`, `args: 49`, `func_start: 15`, `class_start: 14`
* *Risk/State:* `state_mutation: 424`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 46`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` bytesex.h, compiler.h, disasm.h, disp8.h, insns.h, regdis.h, sync.h, tables.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/nasm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2082.04 | **LOC:** 2170 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 61.1%
- **Risk Profile:** Cognitive Load (95.0777%), Tech Debt (9.6331%)
**Top Internal Functions/Classes:**
  * `process_arg` **(Many-Argument Workhorses)** (Impact: 333.7)
  * `help` **(Compute Cores)** (Impact: 179.0)
  * `main` **(Many-Argument Workhorses)** (Impact: 99.3)
  * `assemble_file` **(Compute Cores)** (Impact: 79.4)
  * `nasm_set_limit` **(Compute Cores)** (Impact: 50.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 302 instances
* *State Mutation (weighted view):* 932
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 550`, `structural_boundaries: 295`, `args: 83`, `func_start: 39`, `class_start: 20`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 328`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 16`, `import: 21`
* *Defense:* `safety: 11`, `immutability_locks: 58`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` assemble.h, compiler.h, error.h, eval.h, floats.h, iflag.h, insns.h, labels.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outmacho.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1867.06 | **LOC:** 2530 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (71.4597%), Tech Debt (9.7597%)
**Top Internal Functions/Classes:**
  * `macho_output` **(Compute Cores)** (Impact: 99.7)
  * `add_reloc` **(Many-Argument Workhorses)** (Impact: 93.0)
  * `macho_symdef` **(Many-Argument Workhorses)** (Impact: 87.3)
  * `macho_section` **(Compute Cores)** (Impact: 75.3)
  * `macho_dbg_output` **(Compute Cores)** (Impact: 39.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 333 instances
* *State Mutation (weighted view):* 1081
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 346`, `structural_boundaries: 302`, `args: 96`, `func_start: 41`, `class_start: 75`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 415`, `dead_code: 1`, `fragile_debt: 3`
* *Architecture:* `api: 11`, `import: 16`
* *Defense:* `safety: 6`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` compiler.h, dwarf.h, error.h, hashtbl.h, ilog2.h, labels.h, macho.h, nasm.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zlib/inflate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1866.08 | **LOC:** 1527 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.8434%), Tech Debt (46.2538%)
**Top Internal Functions/Classes:**
  * `inflate` **(Many-Argument Workhorses)** (Impact: 414.8)
    * *Intent:* */
  * `inflateInit2_` **(Many-Argument Workhorses)** (Impact: 26.5)
  * `updatewindow` **(Many-Argument Workhorses)** (Impact: 24.2)
    * *Intent:* */
  * `inflateReset2` **(Compute Cores)** (Impact: 20.9)
  * `inflateCopy` **(C Struct Operations)** (Impact: 17.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 377 instances
* *State Mutation (weighted view):* 1158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 350`, `structural_boundaries: 159`, `args: 29`, `func_start: 23`, `class_start: 21`
* *Risk/State:* `state_mutation: 404`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 14`
* *Architecture:* `api: 23`, `import: 6`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` inffast.h, inffixed.h, inflate.h, inftrees.h, stdio.h, zutil.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/parser.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1839.22 | **LOC:** 1475 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 62.5%
- **Risk Profile:** Cognitive Load (88.3232%), Tech Debt (16.4872%)
**Top Internal Functions/Classes:**
  * `parse_line` **(Many-Argument Workhorses)** (Impact: 482.0)
  * `parse_eops` **(Many-Argument Workhorses)** (Impact: 143.7)
    * *Intent:* /* * Parse an extended expression, used by db et al. "elem" is the element * size; initially comes f...
  * `parse_mref` **(Compute Cores)** (Impact: 55.3)
  * `process_size_override` **(Compute Cores)** (Impact: 52.7)
  * `mref_set_optype` **(Compute Cores)** (Impact: 34.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 292 instances
* *State Mutation (weighted view):* 902
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 437`, `structural_boundaries: 197`, `args: 53`, `func_start: 15`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 318`, `fragile_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 12`
* *Defense:* `safety: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` assemble.h, compiler.h, error.h, eval.h, floats.h, insns.h, nasm.h, nasmlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/rdsrc.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 1662.1 | **LOC:** 1291 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (84.1494%), Tech Debt (16.6986%)
**Top Internal Functions/Classes:**
  * `write_html` **(Compute Cores)** (Impact: 92.3)
  * `got_para` **(Compute Cores)** (Impact: 49.8)
  * `write_txt` **(Compute Cores)** (Impact: 45.8)
  * `word_html` **(Compute Cores)** (Impact: 40.7)
  * `word_txt` **(Compute Cores)** (Impact: 31.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 388 instances
* *Memory Alloc (weighted view):* 15
* *State Mutation (weighted view):* 1171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 409`, `structural_boundaries: 194`, `args: 28`, `func_start: 27`
* *Risk/State:* `state_mutation: 395`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 5`
* *Architecture:* `io: 8`, `api: 27`, `import: 1`
* *Defense:* `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Spec, this, visible
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outbin.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1595.96 | **LOC:** 1637 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.6538%), Tech Debt (9.831%)
**Top Internal Functions/Classes:**
  * `bin_cleanup` **(Compute Cores)** (Impact: 153.2)
  * `bin_assign_attributes` **(Compute Cores)** (Impact: 117.5)
  * `bin_read_attribute` **(Many-Argument Workhorses)** (Impact: 92.2)
  * `bin_directive` **(Compute Cores)** (Impact: 66.7)
  * `bin_out` **(Compute Cores)** (Impact: 49.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 303 instances
* *State Mutation (weighted view):* 949
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 156`, `args: 32`, `func_start: 22`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 343`, `fragile_debt: 2`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 1`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` compiler.h, error.h, eval.h, labels.h, nasm.h, nasmlib.h, nctype.h, outform.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outieee.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1460.6 | **LOC:** 1491 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (74.9919%), Tech Debt (11.9203%)
**Top Internal Functions/Classes:**
  * `ieee_write_fixup` **(Many-Argument Workhorses)** (Impact: 159.6)
    * *Intent:* /* * this routine is unalduterated bloatware. I usually don't do this * but I might as well see what...
  * `ieee_segment` **(Compute Cores)** (Impact: 105.3)
    * *Intent:* /* * segment registry */
  * `ieee_write_file` **(Compute Cores)** (Impact: 73.0)
  * `ieee_deflabel` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* /* * callback for labels */
  * `ieee_out` **(Compute Cores)** (Impact: 35.1)
    * *Intent:* /* * Put data out */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 251 instances
* *State Mutation (weighted view):* 801
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 209`, `args: 40`, `func_start: 26`, `class_start: 59`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 299`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `api: 4`, `import: 11`
* *Defense:* `safety: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` asmutil.h, compiler.h, ctype.h, error.h, nasm.h, nasmlib.h, nctype.h, outform.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outcoff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1211.1 | **LOC:** 1406 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (92.9343%), Tech Debt (9.0642%)
**Top Internal Functions/Classes:**
  * `coff_section_names` **(Compute Cores)** (Impact: 156.1)
  * `coff_out` **(Compute Cores)** (Impact: 87.2)
  * `coff_deflabel` **(Many-Argument Workhorses)** (Impact: 62.6)
  * `coff_directives` **(Compute Cores)** (Impact: 52.1)
  * `coff_write` **(I/O & Config Routines)** (Impact: 28.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 196 instances
* *State Mutation (weighted view):* 623
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 291`, `structural_boundaries: 120`, `args: 46`, `func_start: 26`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 231`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 14`
* *Defense:* `safety: 9`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` compiler.h, error.h, eval.h, ilog2.h, nasm.h, nasmlib.h, nctype.h, outform.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/genps.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 1116.84 | **LOC:** 1311 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (77.9418%), Tech Debt (13.778%)
**Top Internal Functions/Classes:**
  * `ps_flow_lines` **(Many-Argument Workhorses)** (Impact: 84.8)
  * `ps_break_pages` **(Compute Cores)** (Impact: 51.4)
    * *Intent:* # # This formats lines inside the global @pslines array into pages, # updating the page and y-coordi...
  * `ps_break_lines` **(Compute Cores)** (Impact: 47.5)
    * *Intent:* # # Break or convert paragraphs into lines, and push them # onto the @pslines array. #
  * `mkparaarray` **(Compute Cores)** (Impact: 44.0)
    * *Intent:* # element in the array contains (font, string), # where font can be one of: # -1 end link # -2 begin...
  * `ps_string` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* # Generate a PostScript string
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 37 instances
* *Amplified Cascading Flux:* 259 instances
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 798
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 233`, `args: 27`, `func_start: 15`
* *Risk/State:* `state_mutation: 280`, `dead_code: 8`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 12`, `api: 15`, `import: 2`
* *Defense:* `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Spec, font, it, longer, require
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/floats.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1071.44 | **LOC:** 903 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (82.6107%), Tech Debt (12.3122%)
**Top Internal Functions/Classes:**
  * `float_const` **(Many-Argument Workhorses)** (Impact: 165.4)
  * `ieee_flconvert` **(Many-Argument Workhorses)** (Impact: 99.7)
    * *Intent:* /* * --------------------------------------------------------------------------- * convert * -------...
  * `ieee_flconvert_bin` **(Many-Argument Workhorses)** (Impact: 57.8)
    * *Intent:* /* Handle floating-point numbers with radix 2^bits and binary exponent */
  * `to_packed_bcd` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `ieee_round` **(Many-Argument Workhorses)** (Impact: 32.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 186 instances
* *State Mutation (weighted view):* 563
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 101`, `args: 21`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `state_mutation: 191`, `unreferenced_by_name: 3`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 2`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` compiler.h, error.h, floats.h, nasm.h, nctype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/eval.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 920.44 | **LOC:** 1041 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (82.2022%), Tech Debt (9.9317%)
**Top Internal Functions/Classes:**
  * `expr6` **(Compute Cores)** (Impact: 81.6)
  * `evaluate` **(Many-Argument Workhorses)** (Impact: 45.4)
  * `expr5` **(Compute Cores)** (Impact: 44.5)
  * `rexp3` **(Compute Cores)** (Impact: 44.1)
  * `add_vectors` **(Compute Cores)** (Impact: 35.1)
    * *Intent:* /* * Add two vector datatypes. We have some bizarre behaviour on far- * absolute segment types: we p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 143 instances
* *State Mutation (weighted view):* 436
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 173`, `args: 51`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `state_mutation: 150`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* `safety: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` assemble.h, compiler.h, error.h, eval.h, floats.h, ilog2.h, labels.h, nasm.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zlib/crc32.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 917.4 | **LOC:** 1052 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.3942%), Tech Debt (33.3702%)
**Top Internal Functions/Classes:**
  * `crc32_z` **(Many-Argument Workhorses)** (Impact: 161.8)
    * *Intent:* #endif /* ========================================================================= */
  * `make_crc_table` **(I/O & Config Routines)** (Impact: 31.0)
    * *Intent:* */
  * `write_table` **(Compute Cores)** (Impact: 12.4)
    * *Intent:* */
  * `write_table32hi` **(Compute Cores)** (Impact: 12.4)
    * *Intent:* */
  * `write_table64` **(Compute Cores)** (Impact: 12.4)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 185 instances
* *State Mutation (weighted view):* 568
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 45`, `args: 65`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `state_mutation: 198`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 26`, `concurrency: 1`, `import: 4`
* *Defense:* `sync_locks: 2`, `immutability_locks: 25`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` crc32.h, stdatomic.h, stdio.h, zutil.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x86/preinsns.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 900.52 | **LOC:** 669 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (35.6181%)
**Top Internal Functions/Classes:**
  * `func_multisize` **(Compute Cores)** (Impact: 289.8)
  * `process_insn` **(Compute Cores)** (Impact: 29.4)
  * `substitute` **(Compute Cores)** (Impact: 27.7)
    * *Intent:* # # Substitute variables in a pattern #
  * `parse_args` **(Compute Cores)** (Impact: 27.4)
    * *Intent:* # # Macro helper functions for common constructs # # Parse arguments handling variable setting
  * `adjust_fl_zu` **(Many-Argument Workhorses)** (Impact: 23.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 143 instances
* *State Mutation (weighted view):* 430
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 154`, `args: 24`, `func_start: 11`
* *Risk/State:* `state_mutation: 144`, `fragile_debt: 6`
* *Architecture:* `io: 2`, `api: 11`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` integer, macro, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outaout.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 803.88 | **LOC:** 896 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (93.1476%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `aout_deflabel` **(Many-Argument Workhorses)** (Impact: 157.6)
  * `aout_out` **(Compute Cores)** (Impact: 100.4)
  * `aout_add_gsym_reloc` **(Many-Argument Workhorses)** (Impact: 56.3)
    * *Intent:* * RELTYPE_GOT references require the _exact_ symbol address to be * used; RELTYPE_ABSOLUTE reference...
  * `aout_add_gotoff_reloc` **(C Struct Operations)** (Impact: 17.5)
    * *Intent:* /* * This routine deals with ..gotoff relocations. These _must_ refer * to a symbol, due to a perver...
  * `aout_fixup_relocs` **(Compute Cores)** (Impact: 15.7)
    * *Intent:* /* * a.out files have the curious property that all references to * things in the data or bss sectio...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 109 instances
* *State Mutation (weighted view):* 377
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 96`, `args: 25`, `func_start: 16`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 159`, `dead_code: 1`
* *Architecture:* `api: 5`, `import: 11`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` compiler.h, error.h, eval.h, nasm.h, nasmlib.h, nctype.h, outform.h, outlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zlib/infback.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 770.1 | **LOC:** 629 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.1131%), Tech Debt (14.5439%)
**Top Internal Functions/Classes:**
  * `inflateBack` **(Many-Argument Workhorses)** (Impact: 217.3)
    * *Intent:* */
  * `inflateBackInit_` **(Many-Argument Workhorses)** (Impact: 33.8)
    * *Intent:* */
  * `fixedtables` **(Compute Cores)** (Impact: 13.3)
    * *Intent:* */
  * `inflateBackEnd` **(Compute Cores)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 486
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 47`, `args: 9`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `state_mutation: 174`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` inffast.h, inffixed.h, inflate.h, inftrees.h, zutil.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/quote.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 756.96 | **LOC:** 571 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (89.3282%), Tech Debt (18.8354%)
**Top Internal Functions/Classes:**
  * `nasm_unquote_anystr` **(Many-Argument Workhorses)** (Impact: 157.3)
  * `nasm_quote` **(Compute Cores)** (Impact: 100.5)
    * *Intent:* * quote.c */ #include "compiler.h" #include "nasmlib.h" #include "quote.h" #include "nctype.h" #incl...
  * `nasm_skip_string` **(Compute Cores)** (Impact: 31.7)
    * *Intent:* /* * Find the end of a quoted string; returns the pointer to the terminating * character (either the...
  * `emit_utf8` **(Many-Argument Workhorses)** (Impact: 13.1)
  * `nasm_quote_cstr` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* /* * Same as nasm_quote, but take the length of a C string; * the lenp argument is optional. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 141 instances
* *State Mutation (weighted view):* 428
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 59`, `args: 8`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 146`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 9`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` compiler.h, error.h, nasmlib.h, nctype.h, quote.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/directiv.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 624.2 | **LOC:** 652 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (84.1214%), Tech Debt (13.6367%)
**Top Internal Functions/Classes:**
  * `process_directives` **(Compute Cores)** (Impact: 192.9)
    * *Intent:* /* * Process a line from the assembler and try to handle it if it * is a directive. Return true if t...
  * `set_cpu` **(Compute Cores)** (Impact: 40.7)
  * `parse_directive_line` **(Compute Cores)** (Impact: 27.6)
  * `get_bits` **(Compute Cores)** (Impact: 12.7)
  * `directive_valid` **(C Struct Operations)** (Impact: 10.6)
    * *Intent:* /* * Check to see if a string matches a valid directive name (sans [], * whitespace must be already ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 321
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 105`, `args: 8`, `func_start: 6`, `class_start: 7`
* *Risk/State:* `state_mutation: 107`, `fragile_debt: 2`
* *Architecture:* `api: 4`, `import: 16`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` assemble.h, compiler.h, error.h, eval.h, floats.h, iflag.h, ilog2.h, labels.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `travis/nasm-t.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 614.28 | **LOC:** 599 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (78.7433%), Tech Debt (14.1176%)
**Top Internal Functions/Classes:**
  * `test_run` **(Compute Cores)** (Impact: 54.0)
  * `test_update` **(Compute Cores)** (Impact: 28.5)
    * *Intent:* # # Compile sources and generate new targets
  * `prepare_desc` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `hexdump` **(Compute Cores)** (Impact: 16.8)
  * `exec_nasm` **(Compute Cores)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 3 instances
* *Amplified Cascading Flux:* 111 instances
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 352
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 92`, `args: 23`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 4`, `state_mutation: 130`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 32`, `api: 22`, `import: 9`
* *Defense:* `safety: 5`, `test: 8`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` argparse, difflib, filecmp, fnmatch, json, os, re, subprocess...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `misc/omfdump.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 611.96 | **LOC:** 819 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.8759%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dump_segdef` **(Many-Argument Workhorses)** (Impact: 43.6)
    * *Intent:* /* SEGDEF16 or SEGDEF32 */
  * `dump_fixdat` **(Compute Cores)** (Impact: 40.8)
    * *Intent:* /* helper routine used in fixup and modend dumps */
  * `hexdump_data` **(Many-Argument Workhorses)** (Impact: 28.1)
  * `dump_pubdef` **(Many-Argument Workhorses)** (Impact: 26.7)
  * `dump_omf` **(Compute Cores)** (Impact: 22.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 85 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 77`, `args: 33`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 90`
* *Architecture:* `io: 3`, `api: 5`, `import: 3`
* *Defense:* `safety: 31`, `immutability_locks: 64`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bytesex.h, compiler.h, ctype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `asm/preproc.c` -> Churn: **91.28%** | Cog Load: 94.8689% | Debt: 13.548%
- `asm/nasm.c` -> Churn: **83.5%** | Cog Load: 95.0777% | Debt: 9.6331%
- `asm/assemble.c` -> Churn: **65.7%** | Cog Load: 97.5752% | Debt: 11.2164%
- `x86/insns.pl` -> Churn: **65.3%** | Cog Load: 97.9819% | Debt: 0.0%
- `nasmlib/file.c` -> Churn: **58.97%** | Cog Load: 60.9412% | Debt: 77.4981%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `doc/rdsrc.pl` -> **H. Peter Anvin** (100.0% isolated ownership) | Magnitude: 1662.1
- `output/outbin.c` -> **H. Peter Anvin** (100.0% isolated ownership) | Magnitude: 1595.96
- `output/outcoff.c` -> **H. Peter Anvin** (100.0% isolated ownership) | Magnitude: 1211.1
- `doc/genps.pl` -> **H. Peter Anvin** (100.0% isolated ownership) | Magnitude: 1116.84
- `asm/floats.c` -> **H. Peter Anvin** (100.0% isolated ownership) | Magnitude: 1071.44

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `include/nasmlib.h` -> **Severity: 0.186** (Bridge: 0.0021 * Flux: 88.8622%)
- `include/iflag.h` -> **Severity: 0.019** (Bridge: 0.0004 * Flux: 48.2531%)
- `include/ilog2.h` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 92.8154%)
- `asm/listing.h` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 78.0172%)
- `zlib/zutil.h` -> **Severity: 0.009** (Bridge: 0.0009 * Flux: 10.1541%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `include/nasmlib.h` -> **Severity: 13.796** (Embedded: 0.2439 * Error Risk: 56.5555%)
- `include/compiler.h` -> **Severity: 13.634** (Embedded: 0.3494 * Error Risk: 39.021%)
- `include/bytesex.h` -> **Severity: 10.176** (Embedded: 0.1465 * Error Risk: 69.4378%)
- `include/nasm.h` -> **Severity: 9.179** (Embedded: 0.1694 * Error Risk: 54.1763%)
- `include/nctype.h` -> **Severity: 7.383** (Embedded: 0.1293 * Error Risk: 57.0947%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `include/compiler.h` -> **Severity: 15944.1** (Blast Radius: 159.441 * Doc Risk: 100.0%)
- `include/nasmlib.h` -> **Severity: 4456.3** (Blast Radius: 44.563 * Doc Risk: 100.0%)
- `include/nasm.h` -> **Severity: 2977.1** (Blast Radius: 29.771 * Doc Risk: 100.0%)
- `include/bytesex.h` -> **Severity: 2207.3** (Blast Radius: 22.073 * Doc Risk: 100.0%)
- `include/error.h` -> **Severity: 1397.7** (Blast Radius: 13.977 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
