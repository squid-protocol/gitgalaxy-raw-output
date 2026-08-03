# ARCHITECTURAL_BRIEF: cpm65
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/cpm65` |
| **Timestamp** | `2026-08-03T19:27:23.036935+00:00` |
| **Scan Duration** | `0.91s` |
| **Git Branch** | `master` |
| **Git Commit** | `ff7f5f938607195c562e53f0a4558086aab4663a` |
| **Git Remote** | `https://github.com/davidgiven/cpm65.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 80 malicious artifacts.

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
| Total Artifacts | 427 |
| Analyzed Artifacts (Scanned) | 198 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 229 |
| Total LOC | 41281 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 46.4% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8186 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | inf | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8462 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 7 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 108 | 28806 | 54.5% |
| C | 32 | 8142 | 16.2% |
| PYTHON | 28 | 2296 | 14.1% |
| CPP | 9 | 1678 | 4.5% |
| LUA | 6 | 228 | 3.0% |
| PLAINTEXT | 5 | 0 | 2.5% |
| MARKDOWN | 4 | 0 | 2.0% |
| SHELL | 4 | 74 | 2.0% |
| YAML | 1 | 42 | 0.5% |
| MAKEFILE | 1 | 15 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.958`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 158 | 79.8% |
| file_cluster_13 | 23 | 11.6% |
| file_cluster_4 | 8 | 4.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 4.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 229*

**Composition by Extension & Reason:**
- `.py`: 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ld`: 29x Unsupported Format (.ld)
- `.txt`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.s`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bas`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 15x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.fnt`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pas`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.pas')
- `.inc`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.asm`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.9 | 24.6 | 7.6 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 21.4 | 6.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 24.2 | 10.4 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.4 | 2.3 | 80.0 |
| API Exposure | 0.0 | 17.4 | 2.6 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 38.5 | 23.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 32.4 | 1.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 96.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 18.6 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Documentation Exposure | 6.7 | 100.0 | 52.9 | 41.1 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 32.1 | 1.8 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.7 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/arch/snes/snes.inc` (Hits: 101)
- `tools/cpmemu/fileio.c` (Hits: 14)
- `tools/mkimd.c` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **config.py** (`config.py`) — 12 inbound connections
2. **drivers.inc** (`apps/drivers.inc`) — 7 inbound connections
3. **neo6502.h** (`src/arch/neo6502/utils/neo6502.h`) — 5 inbound connections
4. **globals.h** (`tools/cpmemu/globals.h`) — 5 inbound connections
5. **sys.c** (`apps/sys.c`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **biosbdos.c** (`tools/cpmemu/biosbdos.c`) — 12 outbound dependencies
2. **fileio.c** (`tools/cpmemu/fileio.c`) — 11 outbound dependencies
3. **xextobin.cc** (`tools/xextobin.cc`) — 10 outbound dependencies
4. **qe.c** (`apps/qe.c`) — 9 outbound dependencies
5. **mkdfs.c** (`tools/mkdfs.c`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ansi_parse` (@ `apps/ansiterm.c`) -> Impact: **568.6** | LOC: 313
- `main` (@ `apps/ansiterm.c`) -> Impact: **324.4** | LOC: 153
- `vt52_parse` (@ `apps/ansiterm.c`) -> Impact: **281.4** | LOC: 168
  * *Intent:* #define ACK 0x06 #define DLE 0x10 #define XON 0x11 #define XOFF 0x13 #define NAK 0x15 #define SYN 0x16 #define CAN 0x18 #define SUB 0x1a #define UP 0x...
- `consumeExpressionNode` (@ `apps/asm.c`) -> Impact: **276.6** | LOC: 132
- `bdos_entry` (@ `tools/cpmemu/biosbdos.c`) -> Impact: **271.4** | LOC: 89
- `consumeToken` (@ `apps/asm.c`) -> Impact: **262.1** | LOC: 201
- `pk_flag` (@ `src/arch/kim-1/utils/imu-k1013.S`) -> Impact: **226.0** | LOC: 700
  * *Intent:* ; Initialized variables
- `debug` (@ `tools/cpmemu/emulator.c`) -> Impact: **207.6** | LOC: 50
- `disk_status` (@ `src/arch/kim-1/utils/format.S`) -> Impact: **205.0** | LOC: 615
- `file_manipulation` (@ `apps/stat.c`) -> Impact: **191.3** | LOC: 164

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `banner_wait` (@ `src/arch/nano6502/nano6502.S`) -> **O(2^N) [Recursive]**
- `disk_status` (@ `src/arch/kim-1/utils/format.S`) -> **O(2^N) [Recursive]**
- `consumeExpressionNode` (@ `apps/asm.c`) -> **O(2^N) [Recursive]**
- `next` (@ `apps/capsdrv.asm`) -> **O(2^N) [Recursive]**
- `next` (@ `apps/vt52drv.asm`) -> **O(2^N) [Recursive]**
- `buffered_sector` (@ `src/arch/commodore/common/genericdisk.S`) -> **O(2^N) [Recursive]**
- `main_success` (@ `src/arch/commodore/diskaccess/yload1541.S`) -> **O(2^N) [Recursive]**
- `version` (@ `src/arch/kim-1/utils/imu-sdshield.S`) -> **O(2^N) [Recursive]**
  * *Intent:* ; Uninitialized program variables
- `increase_cury` (@ `src/arch/osi/osi.S`) -> **O(2^N) [Recursive]**
- `do_retry` (@ `src/arch/osi/osi.S`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `ansi_parse` (@ `apps/ansiterm.c`) -> DB Complexity: **86**
- `main` (@ `tools/img2osi.c`) -> DB Complexity: **73**
- `write_image` (@ `tools/mkimd.c`) -> DB Complexity: **62**
- `vt52_parse` (@ `apps/ansiterm.c`) -> DB Complexity: **50**
  * *Intent:* #define ACK 0x06 #define DLE 0x10 #define XON 0x11 #define XOFF 0x13 #define NAK 0x15 #define SYN 0x16 #define CAN 0x18 #define SUB 0x1a #define UP 0x...
- `main` (@ `apps/objdump.c`) -> DB Complexity: **50**
- `bdf_load` (@ `tools/libbdf.c`) -> DB Complexity: **48**
- `main` (@ `tools/mkoricdsk.cc`) -> DB Complexity: **43**
- `main` (@ `tools/multilink.cc`) -> DB Complexity: **40**
- `consumeToken` (@ `apps/asm.c`) -> DB Complexity: **38**
- `file_manipulation` (@ `apps/stat.c`) -> DB Complexity: **37**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `apps` | 29 | 10673.5 | 44.0% | 34.56% |
| `src/arch/kim-1/utils` | 6 | 931.26 | 6.92% | 32.61% |
| `src/arch/neo6502/utils` | 7 | 645.0 | 56.48% | 38.44% |
| `src/arch/snes` | 8 | 592.62 | 5.0% | 18.42% |
| `src/bdos` | 11 | 511.36 | 6.88% | 14.65% |
| `src/arch/kim-1` | 14 | 380.47 | 5.54% | 7.66% |
| `src/arch/commodore/diskaccess` | 13 | 267.02 | 5.47% | 10.91% |
| `src/arch/atari800` | 4 | 250.62 | 26.32% | 30.13% |
| `src/arch/commodore` | 4 | 216.06 | 28.98% | 27.73% |
| `src/arch/oric` | 3 | 214.86 | 35.06% | 6.18% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cpmfs/hello.asm` -> **100.0%** Exposure
- `scripts/mame-test.sh` -> **100.0%** Exposure
- `scripts/oric-mame-test.sh` -> **100.0%** Exposure
- `src/arch/commodore/pet-mame-test.sh` -> **100.0%** Exposure
- `apps/cpuinfo.asm` -> **99.9775%** Exposure
### Highest State Flux (Mutation/Volatility)
- `apps/cpm65.inc` -> **100.0%** Exposure
- `apps/drivers.inc` -> **100.0%** Exposure
- `src/arch/bbcmicro/mos.inc` -> **100.0%** Exposure
- `src/arch/snes/globals.inc` -> **100.0%** Exposure
- `src/arch/snes/snes.inc` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `apps/objdump.c` -> **15** Orphaned Functions | **0** Duplicates
- `src/arch/snes/main.asm` -> **8** Orphaned Functions | **6** Duplicates
- `apps/xrecv.asm` -> **11** Orphaned Functions | **0** Duplicates
- `src/arch/kim-1/utils/format.S` -> **11** Orphaned Functions | **0** Duplicates
- `src/arch/nano6502/utils/baudrate.S` -> **11** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`apps/attr.c`** -> AI Confidence: **99.48%**
2. **`tools/mkoricdsk.cc`** -> AI Confidence: **99.48%**
3. **`tools/shuffle.cc`** -> AI Confidence: **99.48%**
4. **`tools/xextobin.cc`** -> AI Confidence: **99.48%**
5. **`apps/asm.c`** -> AI Confidence: **99.39%**
6. **`tools/mkdfs.c`** -> AI Confidence: **99.39%**
7. **`tools/mkimd.c`** -> AI Confidence: **99.39%**
8. **`tools/mkusr.cc`** -> AI Confidence: **99.39%**
9. **`apps/ansiterm.c`** -> AI Confidence: **99.34%**
10. **`src/arch/neo6502/utils/nattr.c`** -> AI Confidence: **99.34%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `tools/build.py` -> **100.0%** Exposure
- `src/arch/snes/checksum.py` -> **99.3177%** Exposure
- `apps/bedit.asm` -> **20.0%** Exposure
- `apps/dinfo.asm` -> **20.0%** Exposure
- `apps/ls.asm` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `tools/fillfile.cc` -> **99.9997%** Exposure
- `tools/mkusr.cc` -> **99.995%** Exposure
- `tools/shuffle.cc` -> **99.987%** Exposure
- `tools/mkcombifs.cc` -> **99.9568%** Exposure
### Raw Memory Manipulation
- `tools/cpmemu/biosbdos.c` -> **0.6964%** Exposure
- `apps/sys.c` -> **0.0002%** Exposure
- `tools/mkimd.c` -> **0.0001%** Exposure
### Algorithmic DoS Exposure
- `src/arch/apple2e/apple2e.S` -> **100.0%** Exposure
- `src/arch/atari800/atari800.S` -> **100.0%** Exposure
- `src/arch/commodore/c64/c64.S` -> **100.0%** Exposure
- `src/arch/commodore/pet.S` -> **100.0%** Exposure
- `src/arch/commodore/vic20/vic20.S` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `332` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `apps/objdump.c` (C) -> Cumulative Risk: **757.91**
- **Archetype:** `file_cluster_8` (Distance: 12.578 IQR)
- **Magnitude:** 395.94 | **LOC:** 343 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (97.2008%)
- **Heaviest Functions:** `main` (Impact: 101.0), `os` (Impact: 16.5), `print` (Impact: 12.5)

### 2. `src/arch/atari800/utils/setfnt.c` (C) -> Cumulative Risk: **728.46**
- **Archetype:** `file_cluster_13` (Distance: 12.616 IQR)
- **Magnitude:** 116.56 | **LOC:** 77 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9216%)
- **Heaviest Functions:** `main` (Impact: 55.4)

### 3. `tools/mkusr.cc` (CPP) -> Cumulative Risk: **720.73**
- **Archetype:** `file_cluster_13` (Distance: 12.397 IQR)
- **Magnitude:** 0.16 | **LOC:** 109 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (99.995%)
- **Heaviest Functions:** `parseArgs` (Impact: 48.0), `main` (Impact: 33.0), `ppread` (Impact: 14.2)

### 4. `tools/shuffle.cc` (CPP) -> Cumulative Risk: **715.77**
- **Archetype:** `file_cluster_13` (Distance: 12.146 IQR)
- **Magnitude:** 0.25 | **LOC:** 129 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (99.987%)
- **Heaviest Functions:** `main` (Impact: 101.0), `write_file` (Impact: 69.6), `chartoint` (Impact: 8.3)

### 5. `apps/attr.c` (C) -> Cumulative Risk: **705.7**
- **Archetype:** `file_cluster_13` (Distance: 12.793 IQR)
- **Magnitude:** 216.54 | **LOC:** 144 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9934%)
- **Heaviest Functions:** `main` (Impact: 54.2), `getword` (Impact: 17.2), `print_filename` (Impact: 10.8)

### 6. `tools/mkcombifs.cc` (CPP) -> Cumulative Risk: **702.2**
- **Archetype:** `file_cluster_13` (Distance: 12.675 IQR)
- **Magnitude:** 0.25 | **LOC:** 168 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (99.9568%)
- **Heaviest Functions:** `main` (Impact: 64.9), `parseArguments` (Impact: 53.1), `get1541TrackSize` (Impact: 10.9)

### 7. `apps/life.c` (C) -> Cumulative Risk: **688.28**
- **Archetype:** `file_cluster_8` (Distance: 12.356 IQR)
- **Magnitude:** 352.34 | **LOC:** 168 | **CtrlFlow:** 89.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.8817%)
- **Heaviest Functions:** `main` (Impact: 165.4), `life` (Impact: 45.0), `fatal` (Impact: 2.4)

### 8. `src/arch/neo6502/utils/nattr.c` (C) -> Cumulative Risk: **684.19**
- **Archetype:** `file_cluster_13` (Distance: 12.263 IQR)
- **Magnitude:** 210.28 | **LOC:** 121 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9564%)
- **Heaviest Functions:** `main` (Impact: 98.5), `getattrs` (Impact: 13.2), `setattrs` (Impact: 11.6)

### 9. `src/arch/neo6502/utils/ndir.c` (C) -> Cumulative Risk: **683.92**
- **Archetype:** `file_cluster_13` (Distance: 11.849 IQR)
- **Magnitude:** 125.88 | **LOC:** 95 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.4596%)
- **Heaviest Functions:** `main` (Impact: 45.9), `opendir` (Impact: 12.9), `closedir` (Impact: 3.4)

### 10. `apps/ansiterm.c` (C) -> Cumulative Risk: **680.78**
- **Archetype:** `file_cluster_8` (Distance: 12.898 IQR)
- **Magnitude:** 1925.0 | **LOC:** 952 | **CtrlFlow:** 92.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (95.2479%)
- **Heaviest Functions:** `ansi_parse` (Impact: 568.6), `main` (Impact: 324.4), `vt52_parse` (Impact: 281.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `apps/asm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.103 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.392 IQR)
- **Top Global Matches:** file_cluster_8: 13.103, file_cluster_7: 13.452, file_cluster_13: 13.458
- **Magnitude:** 2792.88 | **LOC:** 2139 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (93.0746%), Tech Debt (9.0899%)
**Top Internal Functions/Classes:**
  * `consumeExpressionNode` (Impact: 276.6 | O(2^N) | DB: 21)
  * `consumeToken` (Impact: 262.1 | O(N^5) | DB: 38)
  * `parse` (Impact: 143.0 | O(N^6) | DB: 16)
  * `placeCode` (Impact: 128.2 | O(N^6) | DB: 28)
  * `consumeArgument` (Impact: 101.8 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 413`, `structural_boundaries: 156`, `args: 8`, `func_start: 78`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 963`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 240`, `import: 8`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdbool.h, string.h, cpm.h, ctype.h, stdint.h, stdlib.h, printi.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ansiterm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.898 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.235 IQR)
- **Top Global Matches:** file_cluster_8: 12.898, file_cluster_13: 13.223, file_cluster_7: 13.282
- **Magnitude:** 1925.0 | **LOC:** 952 | **CtrlFlow:** 92.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 86
- **Risk Profile:** Cognitive Load (84.7586%), Tech Debt (15.3095%)
**Top Internal Functions/Classes:**
  * `ansi_parse` (Impact: 568.6 | O(N^6) | DB: 86)
  * `main` (Impact: 324.4 | O(N^6) | DB: 15)
  * `vt52_parse` (Impact: 281.4 | O(N^6) | DB: 50)
    * *Intent:* #define ACK 0x06 #define DLE 0x10 #define XON 0x11 #define XOFF 0x13 #define NAK 0x15 #define SYN 0x...
  * `xmodem_receive` (Impact: 73.9 | O(N^6) | DB: 15)
  * `xmodem_send` (Impact: 50.8 | O(N^5) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 26`, `args: 5`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 532`, `planned_debt: 5`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 64`, `import: 5`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cpm.h, screen.h, printi.h, stdio.h, serial.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/qe.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.279 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.812 IQR)
- **Top Global Matches:** file_cluster_8: 13.279, file_cluster_13: 13.479, file_cluster_11: 13.618
- **Magnitude:** 1734.7 | **LOC:** 1241 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (75.6332%), Tech Debt (9.5136%)
**Top Internal Functions/Classes:**
  * `colon` (Impact: 138.2 | O(N^6) | DB: 9)
  * `main` (Impact: 82.4 | O(N^5) | DB: 22)
    * *Intent:* /* ======================================================================= */
  * `insert_file` (Impact: 61.6 | O(N^5) | DB: 10)
    * *Intent:* /* ======================================================================= */
  * `insert_mode` (Impact: 47.1 | O(N^4) | DB: 6)
  * `draw_line` (Impact: 45.6 | O(N^4) | DB: 13)
    * *Intent:* *nextp = inp;
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 131`, `args: 21`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 714`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 183`, `import: 9`
* *Defense:* `safety: 2`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdbool.h, string.h, cpm.h, ctype.h, screen.h, stdint.h, stdlib.h, limits.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/stat.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.831 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.145 IQR)
- **Top Global Matches:** file_cluster_8: 12.831, file_cluster_13: 12.985, file_cluster_7: 13.203
- **Magnitude:** 957.92 | **LOC:** 655 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (72.1877%), Tech Debt (11.5281%)
**Top Internal Functions/Classes:**
  * `file_manipulation` (Impact: 191.3 | O(N^6) | DB: 37)
  * `device_manipulation` (Impact: 79.0 | O(N^5) | DB: 3)
  * `scan` (Impact: 51.2 | O(N^4) | DB: 7)
  * `compare_accumulator` (Impact: 22.8 | O(N^4) | DB: 8)
  * `set_drive_status` (Impact: 21.1 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 73`, `args: 19`, `func_start: 23`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 317`, `orphaned_logic: 2`
* *Architecture:* `io: 8`, `api: 117`, `import: 7`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdbool.h, string.h, cpm.h, stdint.h, stdlib.h, printi.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/objdump.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.578 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.712 IQR)
- **Top Global Matches:** file_cluster_8: 12.578, file_cluster_13: 12.715, file_cluster_7: 12.986
- **Magnitude:** 395.94 | **LOC:** 343 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (89.5198%), Tech Debt (94.7881%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 101.0 | O(N^4) | DB: 50)
  * `os` (Impact: 16.5 | O(N^3) | DB: 4)
  * `print` (Impact: 12.5 | O(N^3) | DB: 2)
  * `getrelo` (Impact: 5.7 | O(N^1) | DB: 4)
  * `oh1` (Impact: 4.9 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 32`, `args: 6`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 197`, `orphaned_logic: 15`
* *Architecture:* `io: 2`, `api: 23`, `import: 7`
* *Defense:* `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdbool.h, string.h, cpm.h, stdint.h, stdlib.h, 6502data.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/sys.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.05%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.245 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.839 IQR)
- **Top Global Matches:** file_cluster_8: 12.245, file_cluster_13: 12.406, file_cluster_7: 12.67
- **Magnitude:** 362.52 | **LOC:** 315 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (89.1411%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `copy_file` (Impact: 76.2 | O(N^5) | DB: 23)
  * `copy_reserved_sectors` (Impact: 38.4 | O(N^4) | DB: 12)
  * `main` (Impact: 22.4 | O(N^3) | DB: 9)
  * `print_filename` (Impact: 10.8 | O(N^4) | DB: 3)
  * `copy_system_files` (Impact: 9.3 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 21`, `args: 9`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 153`
* *Architecture:* `io: 2`, `api: 32`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015228
  * `Imports (Out-Degree: 0):` stdbool.h, cpm.h, stdint.h, stdlib.h, stdio.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `apps/life.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.356 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.288 IQR)
- **Top Global Matches:** file_cluster_8: 12.356, file_cluster_13: 12.432, file_cluster_7: 12.776
- **Magnitude:** 352.34 | **LOC:** 168 | **CtrlFlow:** 89.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (81.2964%), Tech Debt (18.5489%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 165.4 | O(N^5) | DB: 13)
  * `life` (Impact: 45.0 | O(N^4) | DB: 27)
  * `fatal` (Impact: 2.4 | O(N^1))
  * `cr` (Impact: 1.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 6`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 119`, `orphaned_logic: 1`
* *Architecture:* `api: 16`, `import: 4`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` screen.h, printi.h, stdio.h, cpm.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/submit.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.366 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.473 IQR)
- **Top Global Matches:** file_cluster_8: 12.366, file_cluster_13: 12.386, file_cluster_7: 12.774
- **Magnitude:** 321.22 | **LOC:** 220 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (78.2751%), Tech Debt (24.6237%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 63.4 | O(N^4) | DB: 19)
  * `process_byte` (Impact: 60.4 | O(N^5) | DB: 20)
  * `print` (Impact: 12.5 | O(N^3) | DB: 2)
  * `printn` (Impact: 10.9 | O(N^3) | DB: 3)
  * `printi` (Impact: 10.8 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 23`, `args: 6`, `func_start: 8`
* *Risk/State:* `state_mutation: 127`, `orphaned_logic: 2`
* *Architecture:* `io: 3`, `api: 19`, `import: 6`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdbool.h, string.h, cpm.h, ctype.h, stdint.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/copy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.611 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.6 IQR)
- **Top Global Matches:** file_cluster_8: 12.611, file_cluster_13: 12.718, file_cluster_7: 13.009
- **Magnitude:** 272.22 | **LOC:** 251 | **CtrlFlow:** 77.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (74.2998%), Tech Debt (14.3183%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 20.4 | O(N^1) | DB: 22)
  * `copy_file` (Impact: 18.3 | O(N^1) | DB: 15)
  * `parse_cmdline` (Impact: 12.4 | O(N^1) | DB: 5)
  * `print_fcb` (Impact: 10.4 | O(N^1) | DB: 6)
  * `getword` (Impact: 9.2 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 16`, `args: 3`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 168`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 21`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdbool.h, cpm.h, stdint.h, stdlib.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/kim-1/utils/imu-k1013.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.989 IQR)
- **Top Global Matches:** file_cluster_8: 7.989, file_cluster_7: 8.908, file_cluster_1: 9.104
- **Magnitude:** 265.08 | **LOC:** 793 | **CtrlFlow:** 96.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.6618%), Tech Debt (35.0735%)
**Top Internal Functions/Classes:**
  * `pk_flag` (Impact: 226.0 | O(2^N))
    * *Intent:* ; Initialized variables
  * `usage_msg` (Impact: 2.9 | O(N^4))
  * `fdc_msg` (Impact: 2.6 | O(N^4))
  * `real_msg` (Impact: 2.6 | O(N^4))
  * `diskfull_msg` (Impact: 2.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 2`, `func_start: 14`
* *Risk/State:* `orphaned_logic: 9`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/kim-1/utils/format.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.07 IQR)
- **Top Global Matches:** file_cluster_8: 8.07, file_cluster_7: 8.956, file_cluster_1: 9.178
- **Magnitude:** 259.08 | **LOC:** 757 | **CtrlFlow:** 81.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (7.9074%), Tech Debt (44.3425%)
**Top Internal Functions/Classes:**
  * `disk_status` (Impact: 205.0 | O(2^N) | DB: 3)
  * `warning_drv` (Impact: 2.8 | O(N^4))
  * `invalid_drv` (Impact: 2.6 | O(N^4))
  * `usage_msg` (Impact: 2.6 | O(N^4))
  * `abort_msg` (Impact: 2.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 7`, `func_start: 32`
* *Risk/State:* `state_mutation: 5`, `dead_code: 1`, `orphaned_logic: 11`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/snes/main.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.968 IQR)
- **Top Global Matches:** file_cluster_8: 8.968, file_cluster_7: 9.821, file_cluster_1: 10.031
- **Magnitude:** 237.34 | **LOC:** 1764 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (6.6894%), Tech Debt (33.1878%)
**Top Internal Functions/Classes:**
  * `tty_conout` (Impact: 5.7 | O(N^2) | DB: 1)
  * `load_font_data` (Impact: 4.5 | O(N^1))
  * `fd_wait_for_seek_ending` (Impact: 4.5 | O(2^N))
    * *Intent:* ; falls through
  * `fd_complete_transfer` (Impact: 4.5 | O(N^2) | DB: 1)
  * `screen_putstring` (Impact: 4.5 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 8`, `func_start: 119`
* *Risk/State:* `state_mutation: 20`, `dead_code: 3`, `duplicate_logic: 6`, `orphaned_logic: 8`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` snes.inc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/attr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.793 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.847 IQR)
- **Top Global Matches:** file_cluster_13: 12.793, file_cluster_8: 13.003, file_cluster_11: 13.354
- **Magnitude:** 216.54 | **LOC:** 144 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (80.7819%), Tech Debt (22.8298%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 54.2 | O(N^4) | DB: 27)
  * `getword` (Impact: 17.2 | O(N^3) | DB: 7)
  * `print_filename` (Impact: 10.8 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 8`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 115`, `orphaned_logic: 1`
* *Architecture:* `api: 17`, `import: 8`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdbool.h, string.h, cpm.h, ctype.h, stdint.h, stdlib.h, printi.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/neo6502/utils/nattr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.263 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.173 IQR)
- **Top Global Matches:** file_cluster_13: 12.263, file_cluster_8: 12.319, file_cluster_7: 12.737
- **Magnitude:** 210.28 | **LOC:** 121 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (80.1628%), Tech Debt (27.1931%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 98.5 | O(N^4) | DB: 12)
  * `getattrs` (Impact: 13.2 | O(N^2) | DB: 5)
    * *Intent:* #include <stdio.h> #include <stdlib.h> #include <string.h> #include <cpm.h> #include "neo6502.h"
  * `setattrs` (Impact: 11.6 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 5`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 69`, `orphaned_logic: 1`
* *Architecture:* `api: 16`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string.h, cpm.h, stdlib.h, stdio.h, neo6502.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bdos/main.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.102 IQR)
- **Top Global Matches:** file_cluster_8: 6.102, file_cluster_7: 7.41, file_cluster_1: 7.623
- **Magnitude:** 205.72 | **LOC:** 122 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.207%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ccp.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.48 IQR)
- **Top Global Matches:** file_cluster_8: 8.48, file_cluster_7: 9.363, file_cluster_1: 9.581
- **Magnitude:** 184.74 | **LOC:** 1185 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (6.7787%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `monitor_exit` (Impact: 21.3 | O(2^N))
  * `print_00` (Impact: 20.0 | O(N^3))
  * `monitor_digit` (Impact: 13.5 | O(N^3) | DB: 2)
  * `print_filename_bytes` (Impact: 13.2 | O(N^3) | DB: 4)
    * *Intent:* ; Prints A bytes at 'temp', followed by a space.
  * `monitor_nextchar` (Impact: 11.8 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 11`, `func_start: 37`
* *Risk/State:* `state_mutation: 20`, `dead_code: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/kim-1/utils/imu-sdshield.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.534 IQR)
- **Top Global Matches:** file_cluster_8: 7.534, file_cluster_7: 8.504, file_cluster_1: 8.721
- **Magnitude:** 181.66 | **LOC:** 614 | **CtrlFlow:** 96.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (7.974%), Tech Debt (22.6389%)
**Top Internal Functions/Classes:**
  * `version` (Impact: 154.5 | O(2^N) | DB: 1)
    * *Intent:* ; Uninitialized program variables
  * `usage_msg` (Impact: 2.8 | O(N^4))
  * `firmware_opt` (Impact: 2.6 | O(N^4))
  * `firmware_msg2` (Impact: 2.6 | O(N^4))
  * `imagerr_msg` (Impact: 2.6 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 1`, `func_start: 9`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bdos/filesystem.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.043 IQR)
- **Top Global Matches:** file_cluster_8: 9.043, file_cluster_7: 9.847, file_cluster_1: 10.079
- **Magnitude:** 168.78 | **LOC:** 1868 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (5.8324%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `merge_error` (Impact: 19.0 | O(N^6) | DB: 6)
  * `find_first` (Impact: 13.1 | O(N^2))
  * `error$` (Impact: 13.0 | O(N^4) | DB: 2)
  * `no_more_files` (Impact: 10.0 | O(N^3) | DB: 5)
  * `eof` (Impact: 9.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 15`, `func_start: 49`
* *Risk/State:* `state_mutation: 19`, `dead_code: 8`
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.010152
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/arch/atari800/atari800.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.49 IQR)
- **Top Global Matches:** file_cluster_8: 8.49, file_cluster_7: 9.355, file_cluster_1: 9.576
- **Magnitude:** 162.58 | **LOC:** 1337 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (7.9506%), Tech Debt (23.2188%)
**Top Internal Functions/Classes:**
  * `screen_jmptable_hi` (Impact: 34.5 | O(N^5) | DB: 11)
  * `key_down` (Impact: 7.9 | O(N^1) | DB: 1)
  * `clok_done` (Impact: 5.8 | O(N^2) | DB: 1)
  * `SIOV_wrapper` (Impact: 4.0 | O(N^2))
    * *Intent:* ; Leave banking bits alone on a 130XE
  * `no_write` (Impact: 3.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 20`, `args: 8`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 34`, `dead_code: 1`, `fragile_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/mkfs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.311 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.899 IQR)
- **Top Global Matches:** file_cluster_8: 11.311, file_cluster_13: 11.403, file_cluster_7: 11.81
- **Magnitude:** 162.06 | **LOC:** 171 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (86.6734%), Tech Debt (33.4388%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 41.6 | O(N^5) | DB: 11)
  * `printip` (Impact: 18.5 | O(N^4) | DB: 5)
  * `print` (Impact: 12.5 | O(N^3) | DB: 2)
  * `printhex4` (Impact: 5.0 | O(N^2) | DB: 3)
  * `fatal` (Impact: 2.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 18`, `args: 5`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 59`, `orphaned_logic: 2`
* *Architecture:* `api: 13`, `import: 6`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdbool.h, string.h, cpm.h, stdint.h, stdlib.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/neo6502/neo6502.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.548 IQR)
- **Top Global Matches:** file_cluster_8: 8.548, file_cluster_7: 9.43, file_cluster_1: 9.641
- **Magnitude:** 150.92 | **LOC:** 1708 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (6.1698%), Tech Debt (9.6197%)
**Top Internal Functions/Classes:**
  * `unimplemented_string` (Impact: 22.5 | O(N^5) | DB: 10)
  * `delete_exit` (Impact: 14.0 | O(N^5))
  * `bdos_WRITERANDOMFILLED` (Impact: 11.8 | O(N^2))
  * `screen_jmptable_hi` (Impact: 8.5 | O(N^2) | DB: 1)
  * `_start` (Impact: 6.1 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 17`, `args: 1`, `func_start: 30`
* *Risk/State:* `state_mutation: 25`, `orphaned_logic: 2`
* *Architecture:* `api: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/nano6502/nano6502.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.274 IQR)
- **Top Global Matches:** file_cluster_8: 8.274, file_cluster_7: 9.174, file_cluster_1: 9.404
- **Magnitude:** 143.88 | **LOC:** 1143 | **CtrlFlow:** 76.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (6.036%), Tech Debt (9.5866%)
**Top Internal Functions/Classes:**
  * `banner_wait` (Impact: 18.5 | O(2^N) | DB: 7)
  * `screen_getchar_wait` (Impact: 10.7 | O(2^N))
  * `wait_serial_in` (Impact: 8.0 | O(2^N) | DB: 2)
  * `putstring_loop` (Impact: 6.4 | O(2^N))
  * `screen_getchar_data` (Impact: 5.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 9`, `func_start: 45`
* *Risk/State:* `state_mutation: 11`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/vt52drv.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.87 IQR)
- **Top Global Matches:** file_cluster_8: 8.87, file_cluster_7: 9.654, file_cluster_1: 9.902
- **Magnitude:** 143.86 | **LOC:** 457 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (16.1886%), Tech Debt (15.8021%)
**Top Internal Functions/Classes:**
  * `mescdone` (Impact: 70.0 | O(N^6) | DB: 10)
  * `driver` (Impact: 17.5 | O(N^6) | DB: 3)
  * `next` (Impact: 5.5 | O(2^N) | DB: 6)
  * `par_done` (Impact: 2.4 | O(N^3))
  * `BIOS` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 15`, `func_start: 9`
* *Risk/State:* `state_mutation: 33`, `orphaned_logic: 2`
* *Architecture:* `io: 3`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cpm65.inc, drivers.inc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/oric/oric.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.473 IQR)
- **Top Global Matches:** file_cluster_8: 8.473, file_cluster_7: 9.353, file_cluster_1: 9.573
- **Magnitude:** 143.42 | **LOC:** 1521 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (5.7126%), Tech Debt (18.5253%)
**Top Internal Functions/Classes:**
  * `jmptable_hi` (Impact: 14.5 | O(N^4) | DB: 5)
  * `sector2_start` (Impact: 14.1 | O(N^4) | DB: 1)
  * `jasmin_start` (Impact: 10.1 | O(N^4) | DB: 1)
    * *Intent:* ; Jasmin boot code starts here.
  * `column_store_values` (Impact: 9.8 | O(N^3))
  * `keyboard_shift_decode_tab` (Impact: 6.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 16`, `args: 4`, `func_start: 51`
* *Risk/State:* `state_mutation: 16`, `dead_code: 4`, `fragile_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ls.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.519 IQR)
- **Top Global Matches:** file_cluster_8: 8.519, file_cluster_7: 9.404, file_cluster_1: 9.622
- **Magnitude:** 134.58 | **LOC:** 608 | **CtrlFlow:** 65.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (10.7999%), Tech Debt (13.8416%)
**Top Internal Functions/Classes:**
  * `no_fill_wildcards` (Impact: 15.0 | O(N^4) | DB: 3)
  * `mul128` (Impact: 13.7 | O(2^N) | DB: 5)
  * `test_nfiles` (Impact: 7.5 | O(N^3) | DB: 1)
  * `lower` (Impact: 7.0 | O(N^3) | DB: 3)
  * `test_ff` (Impact: 5.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 15`, `func_start: 32`
* *Risk/State:* `state_mutation: 23`, `orphaned_logic: 2`
* *Architecture:* `io: 5`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cpm65.inc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/arch/atari800/utils/setfnt.c` (C) | Magnitude: 116.56 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 56, indent_spaces: 46, branch: 14, pointers: 10
- `apps/mbrot.c` (C) | Magnitude: 101.76 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 65, indent_spaces: 51, api: 11, branch: 6
- `tools/cpmemu/fileio.c` (C) | Magnitude: 0.59 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 308, state_mutation: 234, pointers: 105, branch: 79
- `src/arch/neo6502/utils/nattr.c` (C) | Magnitude: 210.28 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 85, state_mutation: 69, branch: 27, api: 16
- `tools/multilink.cc` (CPP) | Magnitude: 0.27 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 129, state_mutation: 112, branch: 28, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/arch/apple2e/mame-test.lua` (LUA) | Magnitude: 52.24 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 13, structural_boundaries: 11, branch: 9
- `src/arch/atari800/mame-test.lua` (LUA) | Magnitude: 52.24 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 13, structural_boundaries: 11, branch: 9
- `scripts/oric-mame-test.sh` (SHELL) | Magnitude: 1.45 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety_bypasses: 10, args: 7, indent_spaces: 6, branch: 4
- `src/arch/commodore/c64/c64-mame-test.lua` (LUA) | Magnitude: 55.4 | Delta: **0.151 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, state_mutation: 12, concurrency: 12, structural_boundaries: 10
- `src/arch/commodore/pet-mame-test.lua` (LUA) | Magnitude: 55.4 | Delta: **0.151 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, state_mutation: 12, concurrency: 12, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `apps/submit.c` (C) | Magnitude: 321.22 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 131, state_mutation: 127, branch: 41, structural_boundaries: 23
- `tools/cpmemu/biosbdos.c` (C) | Magnitude: 1.08 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 414, state_mutation: 341, branch: 180, structural_boundaries: 144
- `tools/mkoricdsk.cc` (CPP) | Magnitude: 0.38 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 163, indent_spaces: 153, branch: 37, globals: 14
- `apps/life.c` (C) | Magnitude: 352.34 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 120, state_mutation: 119, branch: 52, api: 16
- `src/arch/snes/tools/build.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, import: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/arch/kim-1/utils/imu-k1013.S` -> **eduardocasino** (100.0% isolated ownership) | Magnitude: 265.08
- `src/arch/commodore/pet.S` -> **nick-less** (100.0% isolated ownership) | Magnitude: 133.52

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `apps/drivers.inc` -> **Severity: 3.553** (Embedded: 0.0355 * Error Risk: 99.9911%)
- `apps/sys.c` -> **Severity: 1.047** (Embedded: 0.0152 * Error Risk: 68.7718%)
- `src/arch/snes/snes.inc` -> **Severity: 0.454** (Embedded: 0.0051 * Error Risk: 89.4419%)
- `config.py` -> **Severity: 0.442** (Embedded: 0.0609 * Error Risk: 7.2535%)
- `tools/osi.h` -> **Severity: 0.096** (Embedded: 0.0051 * Error Risk: 18.8905%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tools/cpmemu/globals.h` -> **Severity: 2279.6** (Blast Radius: 22.796 * Doc Risk: 100.0%)
- `src/arch/neo6502/utils/neo6502.h` -> **Severity: 2007.865** (Blast Radius: 22.796 * Doc Risk: 88.0797%)
- `apps/sys.c` -> **Severity: 1540.777** (Blast Radius: 15.414 * Doc Risk: 99.9596%)
- `tools/libbdf.h` -> **Severity: 1172.4** (Blast Radius: 11.724 * Doc Risk: 100.0%)
- `apps/drivers.inc` -> **Severity: 879.203** (Blast Radius: 30.178 * Doc Risk: 29.1339%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
