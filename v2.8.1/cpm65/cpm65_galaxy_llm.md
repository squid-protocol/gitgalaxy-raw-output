# ARCHITECTURAL_BRIEF: cpm65
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/davidgiven/cpm65.git` |
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
| Total Artifacts | 427 |
| Analyzed Artifacts (Scanned) | 213 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 214 |
| Total LOC | 42377 |
| Volatility Index | 0.014 |
| % Scanned of codebase = | 49.9% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8515 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.34 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 11 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 114 | 29656 | 53.5% |
| C | 35 | 8191 | 16.4% |
| PYTHON | 34 | 2493 | 16.0% |
| CPP | 9 | 1678 | 4.2% |
| LUA | 6 | 228 | 2.8% |
| PLAINTEXT | 5 | 0 | 2.3% |
| MARKDOWN | 4 | 0 | 1.9% |
| SHELL | 4 | 74 | 1.9% |
| YAML | 1 | 42 | 0.5% |
| MAKEFILE | 1 | 15 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Mainframe / COBOL & Config` (z -0.74; from the repo's file-archetype mix)
> **File Composition:** I/O & Config Routines Files 36%, Declarative / Non-Code 32%, Large Core Modules 8%, Data / Markup / Trivial 8%, Interface Declarations Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 204 | 95.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 4.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 214*

**Composition by Extension & Reason:**
- `.ld`: 29x Unsupported Format (.ld)
- `.txt`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.s`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 59, Signals: 0), 1x Zero-Density Threshold (LOC: 75, Signals: 0)
- `.bas`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 15x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.fnt`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inc`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 53, Signals: 0)
- `.c`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pas`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.pas')
- `.html`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.6 | 16.3 | 5.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 44.4 | 56.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 29.4 | 11.2 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 32.4 | 1.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 63.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.8 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 61.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1010 | 47 | 5 | `apps/asm.c` |
| cleanup | 33 | 14 | 0 | `tools/libbdf.c` |
| guards | 567 | 42 | 7 | `apps/asm.c` |
| danger | 259 | 52 | 4 | `apps/asm.c` |
| concurrency | 35 | 8 | 0 | `scripts/get-roms.sh` |
| connectivity | 368 | 87 | 4 | `apps/qe.c` |
| io | 99 | 26 | 1 | `tools/multilink.cc` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2 | 2 | 0 | `tools/mkdfs.c` |
| time | 2 | 1 | 0 | `tools/mkimd.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `src/arch/neo6502/build.py` |
| events | 7 | 4 | 0 | `apps/asm.c` |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 143 | 34 | 3 | `tools/cpmemu/emulator.c` |
| mutation | 5524 | 170 | 67 | `apps/asm.c` |
| dead_code | 261 | 91 | 3 | `src/arch/snes/main.asm` |
| credential | 1 | 1 | 0 | `scripts/get-roms.sh` |
| threat | 36 | 12 | 0 | `apps/qe.c` |
| ml_ai | 51 | 16 | 0 | `src/arch/osi/build.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tools/multilink.cc` (Hits: 12)
- `tools/mkimd.c` (Hits: 9)
- `src/arch/nano6502/buildimage.py` (Hits: 9)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **config.py** (`config.py`) — 12 inbound connections
2. **drivers.inc** (`apps/drivers.inc`) — 10 inbound connections
3. **printi.h** (`lib/printi.h`) — 5 inbound connections
4. **neo6502.h** (`src/arch/neo6502/utils/neo6502.h`) — 5 inbound connections
5. **globals.h** (`tools/cpmemu/globals.h`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **biosbdos.c** (`tools/cpmemu/biosbdos.c`) — 12 outbound dependencies
2. **fileio.c** (`tools/cpmemu/fileio.c`) — 11 outbound dependencies
3. **xextobin.cc** (`tools/xextobin.cc`) — 10 outbound dependencies
4. **qe.c** (`apps/qe.c`) — 9 outbound dependencies
5. **mkdfs.c** (`tools/mkdfs.c`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ansi_parse` **(Compute Cores)** (@ `apps/ansiterm.c`) -> Impact: **196.7** | LOC: 313
- `bdos_entry` **(Compute Cores)** (@ `tools/cpmemu/biosbdos.c`) -> Impact: **99.7** | LOC: 89
- `consumeToken` **(Compute Cores)** (@ `apps/asm.c`) -> Impact: **84.0** | LOC: 201
- `vt52_parse` **(Compute Cores)** (@ `apps/ansiterm.c`) -> Impact: **79.1** | LOC: 168
- `main` **(Compute Cores)** (@ `apps/ansiterm.c`) -> Impact: **58.6** | LOC: 153
- `consumeExpressionNode` **(Compute Cores)** (@ `apps/asm.c`) -> Impact: **49.0** | LOC: 132
- `colon` **(Compute Cores)** (@ `apps/qe.c`) -> Impact: **49.0** | LOC: 104
- `main` **(Compute Cores)** (@ `tools/img2osi.c`) -> Impact: **47.6** | LOC: 120
- `placeCode` **(Compute Cores)** (@ `apps/asm.c`) -> Impact: **46.7** | LOC: 114
- `parseArgs` **(Compute Cores)** (@ `tools/mkoricdsk.cc`) -> Impact: **42.4** | LOC: 52

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `apps` | 33 | 5451.2 | 33.59% | 16.8% |
| `src/arch/snes` | 8 | 566.74 | 9.78% | 15.64% |
| `src/arch/neo6502/utils` | 7 | 358.9 | 47.64% | 36.23% |
| `src/arch/nano6502` | 4 | 316.32 | 33.44% | 3.49% |
| `src/bdos` | 11 | 244.36 | 2.19% | 14.86% |
| `src/arch/kim-1` | 12 | 202.8 | 3.74% | 8.79% |
| `src/arch/atari800` | 4 | 179.02 | 4.58% | 7.13% |
| `src/arch/kim-1/boot` | 5 | 175.18 | 5.82% | 77.54% |
| `lib` | 9 | 162.64 | 3.92% | 10.45% |
| `src/arch/commodore/diskaccess` | 12 | 157.56 | 1.25% | 13.91% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/arch/kim-1/boot/bootsd.S` -> **99.9884%** Exposure
- `src/arch/snes/loader.S` -> **99.9874%** Exposure
- `src/arch/neo6502/utils/neo6502.c` -> **98.9013%** Exposure
- `src/arch/kim-1/boot/boot.S` -> **97.4328%** Exposure
- `apps/cpuinfo.asm` -> **97.0688%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `apps/cpm65.inc` -> **100.0%** Exposure
- `apps/drivers.inc` -> **100.0%** Exposure
- `src/arch/snes/snes.inc` -> **100.0%** Exposure
- `apps/ansiterm.c` -> **100.0%** Exposure
- `apps/attr.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/arch/snes/main.asm` -> **13** Orphaned Functions | **2** Duplicates
- `apps/objdump.c` -> **15** Orphaned Functions | **0** Duplicates
- `src/arch/kim-1/boot/bootsd.S` -> **10** Orphaned Functions | **2** Duplicates
- `tools/cpmemu/fileio.c` -> **11** Orphaned Functions | **0** Duplicates
- `src/arch/oric/oric.S` -> **7** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `352` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `apps/objdump.c` (C) -> Cumulative Risk: **655.16**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Encapsulated Accessors Files` (z +0.16)
- **Magnitude:** 227.34 | **LOC:** 343 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Tech Debt (94.7881%)
- **Heaviest Functions:** `main` (Many-Argument Workhorses, Impact: 38.7), `getrelo` (Compute Cores, Impact: 6.4), `print` (Compute Cores, Impact: 4.7)

### 2. `scripts/get-roms.sh` (SHELL) -> Cumulative Risk: **596.79**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +0.01)
- **Magnitude:** 4.04 | **LOC:** 42 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.9683%)
- **Heaviest Functions:** `get_rom` (Compute Cores, Impact: 7.6), `__global_context__` (I/O & Config Routines, Impact: 2.0)

### 3. `src/arch/neo6502/utils/nattr.c` (C) -> Cumulative Risk: **578.15**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z -0.27)
- **Magnitude:** 102.58 | **LOC:** 121 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (92.2054%)
- **Heaviest Functions:** `main` (Compute Cores, Impact: 39.6), `setattrs` (Compute Cores, Impact: 8.1), `getattrs` (Compute Cores, Impact: 6.9)

### 4. `apps/sys.c` (C) -> Cumulative Risk: **577.05**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.05)
- **Magnitude:** 195.22 | **LOC:** 315 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.1279%)
- **Heaviest Functions:** `copy_file` (I/O & Config Routines, Impact: 20.1), `copy_reserved_sectors` (I/O & Config Routines, Impact: 13.1), `main` (I/O & Config Routines, Impact: 12.4)

### 5. `apps/life.c` (C) -> Cumulative Risk: **575.04**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.22)
- **Magnitude:** 170.5 | **LOC:** 168 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.8167%)
- **Heaviest Functions:** `main` (Compute Cores, Impact: 34.1), `life` (I/O & Config Routines, Impact: 14.6), `fatal` (Interface Declarations, Impact: 1.8)

### 6. `apps/submit.c` (C) -> Cumulative Risk: **574.11**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.55)
- **Magnitude:** 165.22 | **LOC:** 220 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (92.6717%)
- **Heaviest Functions:** `process_byte` (Compute Cores, Impact: 28.8), `main` (Many-Argument Workhorses, Impact: 23.6), `printi` (Compute Cores, Impact: 7.9)

### 7. `apps/ansiterm.c` (C) -> Cumulative Risk: **572.71**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.76)
- **Magnitude:** 886.0 | **LOC:** 952 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.8768%)
- **Heaviest Functions:** `ansi_parse` (Compute Cores, Impact: 196.7), `vt52_parse` (Compute Cores, Impact: 79.1), `main` (Compute Cores, Impact: 58.6)

### 8. `apps/qe.c` (C) -> Cumulative Risk: **569.23**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.00)
- **Magnitude:** 983.2 | **LOC:** 1241 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.5634%)
- **Heaviest Functions:** `colon` (Compute Cores, Impact: 49.0), `main` (Many-Argument Workhorses, Impact: 28.7), `insert_mode` (Compute Cores, Impact: 24.8)

### 9. `src/arch/neo6502/utils/neo6502.c` (C) -> Cumulative Risk: **568.4**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.49)
- **Magnitude:** 43.7 | **LOC:** 60 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.9013%)
- **Heaviest Functions:** `printattrs` (Compute Cores, Impact: 8.9), `print_d32` (Compute Cores, Impact: 6.7), `getword` (I/O & Config Routines, Impact: 6.1)

### 10. `apps/asm.c` (C) -> Cumulative Risk: **568.3**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.01)
- **Magnitude:** 1239.08 | **LOC:** 2139 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9988%), Safety Score (90.3563%)
- **Heaviest Functions:** `consumeToken` (Compute Cores, Impact: 84.0), `consumeExpressionNode` (Compute Cores, Impact: 49.0), `placeCode` (Compute Cores, Impact: 46.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `apps/asm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1239.08 | **LOC:** 2139 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.7648%), Tech Debt (8.6347%)
**Top Internal Functions/Classes:**
  * `consumeToken` **(Compute Cores)** (Impact: 84.0)
  * `consumeExpressionNode` **(Compute Cores)** (Impact: 49.0)
  * `placeCode` **(Compute Cores)** (Impact: 46.7)
  * `parse` **(I/O & Config Routines)** (Impact: 36.5)
  * `consumeArgument` **(I/O & Config Routines)** (Impact: 31.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 195 instances
* *State Mutation (weighted view):* 617
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 212`, `args: 50`, `func_start: 78`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 227`, `unreferenced_by_name: 2`
* *Architecture:* `api: 11`, `import: 8`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cpm.h, ctype.h, printi.h, stdbool.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/qe.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 983.2 | **LOC:** 1241 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.8325%), Tech Debt (9.5136%)
**Top Internal Functions/Classes:**
  * `colon` **(Compute Cores)** (Impact: 49.0)
  * `main` **(Many-Argument Workhorses)** (Impact: 28.7)
    * *Intent:* /* ======================================================================= */ /* EDITOR OPERATIONS *...
  * `insert_mode` **(Compute Cores)** (Impact: 24.8)
  * `draw_line` **(Compute Cores)** (Impact: 22.9)
  * `compute_length` **(Many-Argument Workhorses)** (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 157 instances
* *State Mutation (weighted view):* 488
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 156`, `args: 63`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 174`, `unreferenced_by_name: 2`
* *Architecture:* `api: 63`, `import: 9`
* *Defense:* `safety: 2`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cpm.h, ctype.h, screen.h, limits.h, stdbool.h, stdint.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ansiterm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 886.0 | **LOC:** 952 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.0231%), Tech Debt (15.3095%)
**Top Internal Functions/Classes:**
  * `ansi_parse` **(Compute Cores)** (Impact: 196.7)
  * `vt52_parse` **(Compute Cores)** (Impact: 79.1)
  * `main` **(Compute Cores)** (Impact: 58.6)
  * `xmodem_receive` **(I/O & Config Routines)** (Impact: 18.6)
  * `xmodem_send` **(I/O & Config Routines)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 161 instances
* *State Mutation (weighted view):* 488
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 252`, `structural_boundaries: 98`, `args: 18`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 166`, `planned_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cpm.h, printi.h, screen.h, serial.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/stat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 399.98 | **LOC:** 655 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.4%), Tech Debt (11.5456%)
**Top Internal Functions/Classes:**
  * `file_manipulation` **(Compute Cores)** (Impact: 42.3)
  * `scan` **(Compute Cores)** (Impact: 15.7)
    * *Intent:* /* Reads the next input token into the 4-byte accumulator. */
  * `device_manipulation` **(I/O & Config Routines)** (Impact: 14.6)
    * *Intent:* /* Handle device assignment, querying, and miscellaneous other things */
  * `compare_accumulator` **(Compute Cores)** (Impact: 9.8)
    * *Intent:* /* Compares the accumulator with an array of uint8_t[4] words. Returns the * matching index plus one...
  * `set_drive_status` **(I/O & Config Routines)** (Impact: 8.3)
    * *Intent:* /* Handles the A:=R/O and A: DSK: cases. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 202
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 82`, `args: 24`, `func_start: 23`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 76`, `unreferenced_by_name: 2`
* *Architecture:* `api: 24`, `import: 7`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cpm.h, printi.h, stdbool.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/objdump.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 227.34 | **LOC:** 343 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0045%), Tech Debt (94.7881%)
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 38.7)
  * `getrelo` **(Compute Cores)** (Impact: 6.4)
  * `print` **(Compute Cores)** (Impact: 4.7)
  * `os` **(Compute Cores)** (Impact: 4.7)
  * `oh1` **(Compute Cores)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 37`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 47`, `unreferenced_by_name: 15`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 6502data.h, cpm.h, stdbool.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/snes/main.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 217.84 | **LOC:** 1764 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.2808%), Tech Debt (25.172%)
**Top Internal Functions/Classes:**
  * `get_current_key` **(I/O & Config Routines)** (Impact: 9.3)
  * `tty_conout` **(I/O & Config Routines)** (Impact: 6.0)
  * `load_font_data` **(I/O & Config Routines)** (Impact: 4.5)
  * `fd_wait_until_drive_ready` **(I/O & Config Routines)** (Impact: 3.8)
  * `loop` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 19`, `func_start: 94`
* *Risk/State:* `state_mutation: 7`, `dead_code: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 13`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` snes.inc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/sys.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 195.22 | **LOC:** 315 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.206%), Tech Debt (13.1217%)
**Top Internal Functions/Classes:**
  * `copy_file` **(I/O & Config Routines)** (Impact: 20.1)
  * `copy_reserved_sectors` **(I/O & Config Routines)** (Impact: 13.1)
  * `main` **(I/O & Config Routines)** (Impact: 12.4)
  * `print_filename` **(Compute Cores)** (Impact: 6.5)
  * `copy_system_files` **(Interface Declarations)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 22`, `args: 11`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 40`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.013953
  * `Imports (Out-Degree: 0):` cpm.h, stdbool.h, stdint.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `apps/copy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 183.22 | **LOC:** 251 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.299%), Tech Debt (14.3183%)
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 20.4)
  * `copy_file` **(I/O & Config Routines)** (Impact: 12.7)
  * `parse_cmdline` **(I/O & Config Routines)** (Impact: 11.4)
  * `print_fcb` **(Compute Cores)** (Impact: 11.3)
  * `getword` **(I/O & Config Routines)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 22`, `args: 5`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 35`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cpm.h, stdbool.h, stdint.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/life.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 170.5 | **LOC:** 168 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.8204%), Tech Debt (19.3321%)
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 34.1)
  * `life` **(I/O & Config Routines)** (Impact: 14.6)
  * `fatal` **(Interface Declarations)** (Impact: 1.8)
  * `cr` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 14`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 40`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cpm.h, printi.h, screen.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/submit.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 165.22 | **LOC:** 220 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.3375%), Tech Debt (24.6237%)
**Top Internal Functions/Classes:**
  * `process_byte` **(Compute Cores)** (Impact: 28.8)
  * `main` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `printi` **(Compute Cores)** (Impact: 7.9)
  * `printn` **(Compute Cores)** (Impact: 5.7)
  * `fatal` **(Compute Cores)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 23`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 27`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cpm.h, ctype.h, stdbool.h, stdint.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/snes/snes.inc` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 132.38 | **LOC:** 123 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 50`
* *Risk/State:* `state_mutation: 115`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004651
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/arch/atari800/atari800.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 129.08 | **LOC:** 1337 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5961%), Tech Debt (28.5082%)
**Top Internal Functions/Classes:**
  * `screen_jmptable_hi` **(Compute Cores)** (Impact: 16.1)
  * `key_down` **(Compute Cores)** (Impact: 6.5)
  * `clok_done` **(I/O & Config Routines)** (Impact: 4.3)
  * `KIR` **(I/O & Config Routines)** (Impact: 3.4)
  * `IVNM` **(I/O & Config Routines)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 22`, `args: 8`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 20`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/cpm65.inc` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 117.92 | **LOC:** 105 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.0415%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* `state_mutation: 91`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/nano6502/buildimage.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 111.44 | **LOC:** 118 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.8194%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 35`
* *Architecture:* `io: 9`, `import: 2`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` os, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bdos/filesystem.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 105.58 | **LOC:** 1868 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6549%), Tech Debt (10.0044%)
**Top Internal Functions/Classes:**
  * `find_first` **(I/O & Config Routines)** (Impact: 8.6)
  * `merge_error` **(I/O & Config Routines)** (Impact: 7.0)
  * `error$` **(I/O & Config Routines)** (Impact: 6.0)
  * `no_more_files` **(I/O & Config Routines)** (Impact: 5.0)
  * `eof` **(I/O & Config Routines)** (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 31`, `func_start: 26`
* *Risk/State:* `state_mutation: 15`, `dead_code: 8`, `unreferenced_by_name: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.479
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009302
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `apps/mkfs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 105.16 | **LOC:** 171 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.8707%), Tech Debt (33.4388%)
**Top Internal Functions/Classes:**
  * `printip` **(Compute Cores)** (Impact: 15.0)
    * *Intent:* /* * Prints a 32-bit decimal number with optional left padding and configurable * precision. *. */
  * `main` **(I/O & Config Routines)** (Impact: 12.4)
  * `print` **(Compute Cores)** (Impact: 4.7)
  * `printhex4` **(Compute Cores)** (Impact: 4.7)
  * `printx` **(Interface Declarations)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 18`, `args: 11`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `unreferenced_by_name: 2`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cpm.h, stdbool.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/snes/checksum.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 104.06 | **LOC:** 84 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.9337%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checksum` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* # applies the SNES checksum to a ROM # usage: # checksum.py LOROM filein [fileout] # checksum.py HIR...
  * `usage` **(Interface Declarations)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 3 instances
* *Amplified Cascading Flux:* 26 instances
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 5`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 26`
* *Architecture:* `io: 5`, `api: 2`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/neo6502/utils/nattr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 102.58 | **LOC:** 121 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.7915%), Tech Debt (27.1931%)
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 39.6)
  * `setattrs` **(Compute Cores)** (Impact: 8.1)
  * `getattrs` **(Compute Cores)** (Impact: 6.9)
    * *Intent:* #include <stdio.h> #include <stdlib.h> #include <string.h> #include <cpm.h> #include "neo6502.h"
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 6`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cpm.h, neo6502.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/neo6502/neo6502.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 102.32 | **LOC:** 1708 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.9329%), Tech Debt (11.7079%)
**Top Internal Functions/Classes:**
  * `delete_exit` **(I/O & Config Routines)** (Impact: 13.5)
  * `bdos_WRITERANDOMFILLED` **(I/O & Config Routines)** (Impact: 8.8)
  * `internal_READSEQUENTIAL` **(I/O & Config Routines)** (Impact: 4.9)
  * `screen_jmptable_hi` **(I/O & Config Routines)** (Impact: 3.5)
  * `_start` **(I/O & Config Routines)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 35`, `args: 1`, `func_start: 17`
* *Risk/State:* `state_mutation: 17`, `unreferenced_by_name: 5`
* *Architecture:* `api: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/attr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 101.44 | **LOC:** 144 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.9878%), Tech Debt (22.8298%)
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 23.2)
  * `print_filename` **(Compute Cores)** (Impact: 7.7)
  * `getword` **(I/O & Config Routines)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 11`, `args: 1`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 20`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cpm.h, ctype.h, printi.h, stdbool.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/nano6502/nano6502.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 98.08 | **LOC:** 1143 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6847%), Tech Debt (13.9745%)
**Top Internal Functions/Classes:**
  * `banner_wait` **(I/O & Config Routines)** (Impact: 6.5)
  * `screen_getchar_data` **(I/O & Config Routines)** (Impact: 4.8)
  * `screen_getchar_wait` **(I/O & Config Routines)** (Impact: 4.7)
  * `jmptable_hi` **(I/O & Config Routines)** (Impact: 4.0)
  * `wait_serial_in` **(I/O & Config Routines)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 18`, `func_start: 29`
* *Risk/State:* `state_mutation: 9`, `dead_code: 2`, `unreferenced_by_name: 5`
* *Architecture:* `api: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/drivers.inc` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 90.72 | **LOC:** 44 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.9714%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.046512
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/arch/oric/oric.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 90.48 | **LOC:** 1521 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6024%), Tech Debt (22.4815%)
**Top Internal Functions/Classes:**
  * `jmptable_hi` **(I/O & Config Routines)** (Impact: 7.5)
  * `screen_jmptable_hi` **(I/O & Config Routines)** (Impact: 7.0)
  * `sector2_start` **(I/O & Config Routines)** (Impact: 6.3)
  * `jasmin_start` **(I/O & Config Routines)** (Impact: 4.4)
    * *Intent:* ; Jasmin boot code starts here.
  * `banner_end` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 28`, `args: 4`, `func_start: 18`
* *Risk/State:* `state_mutation: 10`, `dead_code: 4`, `fragile_debt: 1`, `unreferenced_by_name: 7`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ls.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 90.38 | **LOC:** 608 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.6148%), Tech Debt (18.7408%)
**Top Internal Functions/Classes:**
  * `no_fill_wildcards` **(I/O & Config Routines)** (Impact: 5.5)
  * `no_archived` **(I/O & Config Routines)** (Impact: 5.0)
  * `mul128` **(I/O & Config Routines)** (Impact: 4.7)
  * `test_nfiles` **(I/O & Config Routines)** (Impact: 3.5)
  * `jloop` **(I/O & Config Routines)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 24`, `func_start: 28`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 4`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cpm65.inc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/nano6502/buildsysimage.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 90.18 | **LOC:** 98 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.2364%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 28`
* *Architecture:* `io: 7`, `import: 2`
* *Defense:* `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` os, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/arch/commodore/pet.S` -> **nick-less** (100.0% isolated ownership) | Magnitude: 79.42

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `apps/drivers.inc` -> **Severity: 4.646** (Embedded: 0.0465 * Error Risk: 99.8855%)
- `config.py` -> **Severity: 4.377** (Embedded: 0.0558 * Error Risk: 78.4202%)
- `apps/sys.c` -> **Severity: 1.313** (Embedded: 0.014 * Error Risk: 94.1279%)
- `src/bdos/filesystem.S` -> **Severity: 0.489** (Embedded: 0.0093 * Error Risk: 52.5743%)
- `src/arch/snes/snes.inc` -> **Severity: 0.462** (Embedded: 0.0047 * Error Risk: 99.4157%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `apps/sys.c` -> **Severity: 1377.8** (Blast Radius: 13.778 * Doc Risk: 100.0%)
- `src/bdos/filesystem.S` -> **Severity: 1047.9** (Blast Radius: 10.479 * Doc Risk: 100.0%)
- `apps/adm3adrv.S` -> **Severity: 388.1** (Blast Radius: 3.881 * Doc Risk: 100.0%)
- `apps/adm3atst.asm` -> **Severity: 388.1** (Blast Radius: 3.881 * Doc Risk: 100.0%)
- `apps/bedit.asm` -> **Severity: 388.1** (Blast Radius: 3.881 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
