# ARCHITECTURAL_BRIEF: cpm65
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/cpm65` |
| **Timestamp** | `2026-08-07T03:49:43.948578+00:00` |
| **Scan Duration** | `0.89s` |
| **Git Branch** | `master` |
| **Git Commit** | `ff7f5f938607195c562e53f0a4558086aab4663a` |
| **Git Remote** | `https://github.com/davidgiven/cpm65.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 80 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 99.9 | 24.0 | 7.6 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 46.6 | 56.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 24.2 | 10.4 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 12.6 | 2.3 | 2.3 |
| API Exposure | 0.0 | 17.4 | 2.6 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 38.5 | 23.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 32.4 | 1.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 96.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 18.6 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Documentation Exposure | 5.9 | 100.0 | 33.9 | 21.7 | 11.9 |
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

- `ansi_parse` (@ `apps/ansiterm.c`) -> Impact: **173.7** | LOC: 313
- `main` (@ `apps/ansiterm.c`) -> Impact: **98.2** | LOC: 153
- `consumeToken` (@ `apps/asm.c`) -> Impact: **94.0** | LOC: 201
- `bdos_entry` (@ `tools/cpmemu/biosbdos.c`) -> Impact: **93.5** | LOC: 89
- `vt52_parse` (@ `apps/ansiterm.c`) -> Impact: **86.4** | LOC: 168
  * *Intent:* #define ACK 0x06 #define DLE 0x10 #define XON 0x11 #define XOFF 0x13 #define NAK 0x15 #define SYN 0x16 #define CAN 0x18 #define SUB 0x1a #define UP 0x...
- `pk_flag` (@ `src/arch/kim-1/utils/imu-k1013.S`) -> Impact: **76.0** | LOC: 700
  * *Intent:* ; Initialized variables
- `file_manipulation` (@ `apps/stat.c`) -> Impact: **60.5** | LOC: 164
- `bdf_load` (@ `tools/libbdf.c`) -> Impact: **59.8** | LOC: 76
- `main` (@ `apps/life.c`) -> Impact: **57.9** | LOC: 83
- `consumeExpressionNode` (@ `apps/asm.c`) -> Impact: **51.6** | LOC: 132

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `apps` | 29 | 7432.7 | 43.05% | 34.56% |
| `src/arch/snes` | 8 | 551.12 | 5.0% | 18.42% |
| `src/arch/neo6502/utils` | 7 | 510.4 | 56.48% | 38.44% |
| `src/bdos` | 11 | 447.76 | 6.88% | 14.65% |
| `src/arch/kim-1/utils` | 6 | 379.16 | 6.92% | 32.61% |
| `src/arch/kim-1` | 14 | 343.97 | 5.54% | 7.66% |
| `src/arch/atari800` | 4 | 213.42 | 26.32% | 30.13% |
| `src/arch/kim-1/boot` | 5 | 187.08 | 9.52% | 60.89% |
| `src/arch/oric` | 3 | 171.96 | 35.06% | 6.18% |
| `src/arch/osi` | 6 | 164.5 | 6.29% | 17.93% |

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `332` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `scripts/get-roms.sh` (SHELL) -> Cumulative Risk: **639.82**
- **Archetype:** `file_cluster_4` (Distance: 10.585 IQR)
- **Magnitude:** 4.76 | **LOC:** 42 | **CtrlFlow:** 81.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Safety Score (99.9517%), Cognitive Load (99.9462%)
- **Heaviest Functions:** `get_rom` (Impact: 14.8), `__global_context__` (Impact: 2.0)

### 2. `apps/objdump.c` (C) -> Cumulative Risk: **638.54**
- **Archetype:** `file_cluster_8` (Distance: 12.578 IQR)
- **Magnitude:** 323.34 | **LOC:** 343 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.0086%), Tech Debt (94.7881%)
- **Heaviest Functions:** `main` (Impact: 43.9), `os` (Impact: 8.5), `print` (Impact: 6.5)

### 3. `src/arch/apple2e/mame-test.lua` (LUA) -> Cumulative Risk: **623.79**
- **Archetype:** `file_cluster_4` (Distance: 11.863 IQR)
- **Magnitude:** 38.04 | **LOC:** 44 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9994%), Concurrency (99.9409%), Cognitive Load (97.3263%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 16.2), `__global_context__` (Impact: 1.1)

### 4. `src/arch/atari800/mame-test.lua` (LUA) -> Cumulative Risk: **623.79**
- **Archetype:** `file_cluster_4` (Distance: 11.863 IQR)
- **Magnitude:** 38.04 | **LOC:** 44 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9994%), Concurrency (99.9409%), Cognitive Load (97.3263%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 16.2), `__global_context__` (Impact: 1.1)

### 5. `src/arch/neo6502/utils/nattr.c` (C) -> Cumulative Risk: **589.51**
- **Archetype:** `file_cluster_13` (Distance: 12.263 IQR)
- **Magnitude:** 145.58 | **LOC:** 121 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (97.6207%), Safety Score (94.0504%)
- **Heaviest Functions:** `main` (Impact: 41.3), `getattrs` (Impact: 9.2), `setattrs` (Impact: 8.1)

### 6. `src/arch/neo6502/utils/neo6502.c` (C) -> Cumulative Risk: **587.84**
- **Archetype:** `file_cluster_13` (Distance: 12.054 IQR)
- **Magnitude:** 67.5 | **LOC:** 60 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.2287%), Tech Debt (98.9013%)
- **Heaviest Functions:** `getword` (Impact: 8.1), `printattrs` (Impact: 6.4), `print_d32` (Impact: 5.0)

### 7. `apps/asm.c` (C) -> Cumulative Risk: **581.59**
- **Archetype:** `file_cluster_8` (Distance: 13.103 IQR)
- **Magnitude:** 1828.38 | **LOC:** 2139 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (97.1352%), Cognitive Load (93.0746%)
- **Heaviest Functions:** `consumeToken` (Impact: 94.0), `consumeExpressionNode` (Impact: 51.6), `parse` (Impact: 45.5)

### 8. `apps/life.c` (C) -> Cumulative Risk: **580.2**
- **Archetype:** `file_cluster_8` (Distance: 12.356 IQR)
- **Magnitude:** 219.34 | **LOC:** 168 | **CtrlFlow:** 89.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.4919%), Documentation (95.8247%)
- **Heaviest Functions:** `main` (Impact: 57.9), `life` (Impact: 19.5), `fatal` (Impact: 2.4)

### 9. `apps/qe.c` (C) -> Cumulative Risk: **575.39**
- **Archetype:** `file_cluster_8` (Distance: 13.279 IQR)
- **Magnitude:** 1310.6 | **LOC:** 1241 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.3668%), Safety Score (96.3997%)
- **Heaviest Functions:** `colon` (Impact: 43.2), `main` (Impact: 30.4), `insert_file` (Impact: 22.0)

### 10. `apps/stat.c` (C) -> Cumulative Risk: **571.58**
- **Archetype:** `file_cluster_8` (Distance: 12.831 IQR)
- **Magnitude:** 664.02 | **LOC:** 655 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.8667%), Safety Score (93.5301%)
- **Heaviest Functions:** `file_manipulation` (Impact: 60.5), `device_manipulation` (Impact: 28.1), `scan` (Impact: 21.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `apps/asm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.103 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.392 IQR)
- **Top Global Matches:** file_cluster_8: 13.103, file_cluster_7: 13.452, file_cluster_13: 13.458
- **Magnitude:** 1828.38 | **LOC:** 2139 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.0746%), Tech Debt (9.0899%)
**Top Internal Functions/Classes:**
  * `consumeToken` (Impact: 94.0)
  * `consumeExpressionNode` (Impact: 51.6)
  * `parse` (Impact: 45.5)
  * `placeCode` (Impact: 40.7)
  * `consumeArgument` (Impact: 31.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 413`, `structural_boundaries: 156`, `args: 8`, `func_start: 78`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 963`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 240`, `import: 8`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, string.h, stdint.h, stdbool.h, printi.h, cpm.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/qe.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.279 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.812 IQR)
- **Top Global Matches:** file_cluster_8: 13.279, file_cluster_13: 13.479, file_cluster_11: 13.618
- **Magnitude:** 1310.6 | **LOC:** 1241 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6332%), Tech Debt (9.5136%)
**Top Internal Functions/Classes:**
  * `colon` (Impact: 43.2)
  * `main` (Impact: 30.4)
    * *Intent:* /* ======================================================================= */
  * `insert_file` (Impact: 22.0)
    * *Intent:* /* ======================================================================= */
  * `draw_line` (Impact: 20.1)
    * *Intent:* *nextp = inp;
  * `insert_mode` (Impact: 20.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 131`, `args: 21`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 714`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 183`, `import: 9`
* *Defense:* `safety: 2`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, string.h, stdint.h, stdbool.h, limits.h, cpm.h, screen.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ansiterm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.898 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.235 IQR)
- **Top Global Matches:** file_cluster_8: 12.898, file_cluster_13: 13.223, file_cluster_7: 13.282
- **Magnitude:** 1025.3 | **LOC:** 952 | **CtrlFlow:** 92.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.7586%), Tech Debt (15.3095%)
**Top Internal Functions/Classes:**
  * `ansi_parse` (Impact: 173.7)
  * `main` (Impact: 98.2)
  * `vt52_parse` (Impact: 86.4)
    * *Intent:* #define ACK 0x06 #define DLE 0x10 #define XON 0x11 #define XOFF 0x13 #define NAK 0x15 #define SYN 0x...
  * `xmodem_receive` (Impact: 24.4)
  * `xmodem_send` (Impact: 19.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 26`, `args: 5`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 532`, `planned_debt: 5`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 64`, `import: 5`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` serial.h, printi.h, screen.h, cpm.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/stat.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.831 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.145 IQR)
- **Top Global Matches:** file_cluster_8: 12.831, file_cluster_13: 12.985, file_cluster_7: 13.203
- **Magnitude:** 664.02 | **LOC:** 655 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.1877%), Tech Debt (11.5281%)
**Top Internal Functions/Classes:**
  * `file_manipulation` (Impact: 60.5)
  * `device_manipulation` (Impact: 28.1)
  * `scan` (Impact: 21.5)
  * `set_drive_status` (Impact: 11.2)
  * `main` (Impact: 10.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 73`, `args: 19`, `func_start: 23`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 317`, `orphaned_logic: 2`
* *Architecture:* `io: 8`, `api: 117`, `import: 7`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdint.h, string.h, stdbool.h, printi.h, cpm.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/objdump.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.578 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.712 IQR)
- **Top Global Matches:** file_cluster_8: 12.578, file_cluster_13: 12.715, file_cluster_7: 12.986
- **Magnitude:** 323.34 | **LOC:** 343 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.5198%), Tech Debt (94.7881%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 43.9)
  * `os` (Impact: 8.5)
  * `print` (Impact: 6.5)
  * `getrelo` (Impact: 5.7)
  * `oh1` (Impact: 3.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 32`, `args: 6`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 197`, `orphaned_logic: 15`
* *Architecture:* `io: 2`, `api: 23`, `import: 7`
* *Defense:* `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdint.h, string.h, stdbool.h, 6502data.h, cpm.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/copy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.611 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.6 IQR)
- **Top Global Matches:** file_cluster_8: 12.611, file_cluster_13: 12.718, file_cluster_7: 13.009
- **Magnitude:** 272.22 | **LOC:** 251 | **CtrlFlow:** 77.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.2998%), Tech Debt (14.3183%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 20.4)
  * `copy_file` (Impact: 18.3)
  * `parse_cmdline` (Impact: 12.4)
  * `print_fcb` (Impact: 10.4)
  * `getword` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 16`, `args: 3`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 168`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 21`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdint.h, stdbool.h, cpm.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/sys.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.05%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.245 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.839 IQR)
- **Top Global Matches:** file_cluster_8: 12.245, file_cluster_13: 12.406, file_cluster_7: 12.67
- **Magnitude:** 272.02 | **LOC:** 315 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0268%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `copy_file` (Impact: 28.1)
  * `copy_reserved_sectors` (Impact: 17.2)
  * `main` (Impact: 12.4)
  * `copy_system_files` (Impact: 5.1)
  * `print_filename` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 21`, `args: 9`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 153`
* *Architecture:* `io: 2`, `api: 32`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015228
  * `Imports (Out-Degree: 0):` stdint.h, stdbool.h, cpm.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `apps/submit.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.366 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.473 IQR)
- **Top Global Matches:** file_cluster_8: 12.366, file_cluster_13: 12.386, file_cluster_7: 12.774
- **Magnitude:** 227.62 | **LOC:** 220 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.2751%), Tech Debt (24.6237%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 27.0)
  * `process_byte` (Impact: 22.4)
  * `fatal` (Impact: 6.8)
  * `print` (Impact: 6.5)
  * `printi` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 23`, `args: 6`, `func_start: 8`
* *Risk/State:* `state_mutation: 127`, `orphaned_logic: 2`
* *Architecture:* `io: 3`, `api: 19`, `import: 6`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, string.h, stdint.h, stdbool.h, cpm.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/life.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.356 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.288 IQR)
- **Top Global Matches:** file_cluster_8: 12.356, file_cluster_13: 12.432, file_cluster_7: 12.776
- **Magnitude:** 219.34 | **LOC:** 168 | **CtrlFlow:** 89.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.2964%), Tech Debt (18.5489%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 57.9)
  * `life` (Impact: 19.5)
  * `fatal` (Impact: 2.4)
  * `cr` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 6`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 119`, `orphaned_logic: 1`
* *Architecture:* `api: 16`, `import: 4`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` screen.h, stdio.h, printi.h, cpm.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/snes/main.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.968 IQR)
- **Top Global Matches:** file_cluster_8: 8.968, file_cluster_7: 9.821, file_cluster_1: 10.031
- **Magnitude:** 215.74 | **LOC:** 1764 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.6894%), Tech Debt (33.1878%)
**Top Internal Functions/Classes:**
  * `load_font_data` (Impact: 4.5)
  * `tty_conout` (Impact: 4.2)
  * `bios_setsec` (Impact: 3.6)
  * `fd_complete_transfer` (Impact: 3.5)
  * `screen_putstring` (Impact: 3.5)
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

### `src/bdos/main.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.102 IQR)
- **Top Global Matches:** file_cluster_8: 6.102, file_cluster_7: 7.41, file_cluster_1: 7.623
- **Magnitude:** 205.72 | **LOC:** 122 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
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

### `apps/attr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.793 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.847 IQR)
- **Top Global Matches:** file_cluster_13: 12.793, file_cluster_8: 13.003, file_cluster_11: 13.354
- **Magnitude:** 172.54 | **LOC:** 144 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.7819%), Tech Debt (22.8298%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 24.2)
  * `getword` (Impact: 9.2)
  * `print_filename` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 8`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 115`, `orphaned_logic: 1`
* *Architecture:* `api: 17`, `import: 8`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, string.h, stdint.h, stdbool.h, printi.h, cpm.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/neo6502/utils/nattr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.263 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.173 IQR)
- **Top Global Matches:** file_cluster_13: 12.263, file_cluster_8: 12.319, file_cluster_7: 12.737
- **Magnitude:** 145.58 | **LOC:** 121 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.1628%), Tech Debt (27.1931%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 41.3)
  * `getattrs` (Impact: 9.2)
    * *Intent:* #include <stdio.h> #include <stdlib.h> #include <string.h> #include <cpm.h> #include "neo6502.h"
  * `setattrs` (Impact: 8.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 5`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 69`, `orphaned_logic: 1`
* *Architecture:* `api: 16`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` neo6502.h, string.h, cpm.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/atari800/atari800.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.49 IQR)
- **Top Global Matches:** file_cluster_8: 8.49, file_cluster_7: 9.355, file_cluster_1: 9.576
- **Magnitude:** 139.58 | **LOC:** 1337 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.9506%), Tech Debt (23.2188%)
**Top Internal Functions/Classes:**
  * `screen_jmptable_hi` (Impact: 17.5)
  * `key_down` (Impact: 7.9)
  * `clok_done` (Impact: 4.3)
  * `KIR` (Impact: 3.4)
  * `IVNM` (Impact: 3.3)
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

### `src/arch/snes/snes.inc` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.562 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.091 IQR)
- **Top Global Matches:** file_cluster_8: 11.562, file_cluster_7: 12.216, file_cluster_17: 12.276
- **Magnitude:** 132.38 | **LOC:** 123 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`
* *Risk/State:* `state_mutation: 115`
* *Architecture:* `io: 101`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005076
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ccp.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.48 IQR)
- **Top Global Matches:** file_cluster_8: 8.48, file_cluster_7: 9.363, file_cluster_1: 9.581
- **Magnitude:** 129.74 | **LOC:** 1185 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.7787%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `print_00` (Impact: 12.0)
  * `monitor_digit` (Impact: 8.5)
  * `print_filename_bytes` (Impact: 8.2)
    * *Intent:* ; Prints A bytes at 'temp', followed by a space.
  * `monitor_exit` (Impact: 6.3)
  * `monitor_nextchar` (Impact: 5.8)
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

### `src/bdos/filesystem.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.043 IQR)
- **Top Global Matches:** file_cluster_8: 9.043, file_cluster_7: 9.847, file_cluster_1: 10.079
- **Magnitude:** 123.68 | **LOC:** 1868 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8324%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `find_first` (Impact: 9.6)
  * `merge_error` (Impact: 9.0)
  * `error$` (Impact: 7.0)
  * `no_more_files` (Impact: 7.0)
  * `eof` (Impact: 4.5)
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

### `src/arch/neo6502/neo6502.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.548 IQR)
- **Top Global Matches:** file_cluster_8: 8.548, file_cluster_7: 9.43, file_cluster_1: 9.641
- **Magnitude:** 120.42 | **LOC:** 1708 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.1698%), Tech Debt (9.6197%)
**Top Internal Functions/Classes:**
  * `unimplemented_string` (Impact: 12.5)
  * `bdos_WRITERANDOMFILLED` (Impact: 8.8)
  * `screen_jmptable_hi` (Impact: 6.5)
  * `delete_exit` (Impact: 6.0)
  * `internal_READSEQUENTIAL` (Impact: 4.9)
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

### `apps/cpm65.inc` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.343 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.803 IQR)
- **Top Global Matches:** file_cluster_8: 12.343, file_cluster_7: 12.918, file_cluster_1: 13.14
- **Magnitude:** 118.92 | **LOC:** 105 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.1209%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* `state_mutation: 102`
* *Architecture:* None
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
- **Magnitude:** 118.66 | **LOC:** 171 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.6734%), Tech Debt (33.4388%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 16.2)
  * `printip` (Impact: 8.0)
  * `print` (Impact: 6.5)
  * `printhex4` (Impact: 3.5)
  * `fatal` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 18`, `args: 5`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 59`, `orphaned_logic: 2`
* *Architecture:* `api: 13`, `import: 6`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdint.h, string.h, stdbool.h, cpm.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/oric/oric.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.473 IQR)
- **Top Global Matches:** file_cluster_8: 8.473, file_cluster_7: 9.353, file_cluster_1: 9.573
- **Magnitude:** 114.72 | **LOC:** 1521 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.7126%), Tech Debt (18.5253%)
**Top Internal Functions/Classes:**
  * `jmptable_hi` (Impact: 8.5)
  * `sector2_start` (Impact: 7.7)
  * `jasmin_start` (Impact: 5.8)
    * *Intent:* ; Jasmin boot code starts here.
  * `column_store_values` (Impact: 5.8)
  * `dma` (Impact: 4.0)
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

### `src/arch/neo6502/utils/ntrunc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.818 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.095 IQR)
- **Top Global Matches:** file_cluster_13: 11.818, file_cluster_8: 11.88, file_cluster_7: 12.347
- **Magnitude:** 113.5 | **LOC:** 132 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.6237%), Tech Debt (26.8941%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 10.5)
  * `getsize` (Impact: 9.1)
  * `open` (Impact: 5.1)
  * `close` (Impact: 4.8)
  * `truncate` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 7`, `args: 2`, `func_start: 6`
* *Risk/State:* `state_mutation: 68`, `orphaned_logic: 1`
* *Architecture:* `io: 5`, `api: 8`, `import: 5`
* *Defense:* `immutability_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` neo6502.h, string.h, cpm.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/nano6502/nano6502.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.274 IQR)
- **Top Global Matches:** file_cluster_8: 8.274, file_cluster_7: 9.174, file_cluster_1: 9.404
- **Magnitude:** 112.98 | **LOC:** 1143 | **CtrlFlow:** 76.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.036%), Tech Debt (9.5866%)
**Top Internal Functions/Classes:**
  * `banner_wait` (Impact: 6.5)
  * `screen_getchar_data` (Impact: 5.8)
  * `screen_getchar_wait` (Impact: 5.7)
  * `jmptable_hi` (Impact: 5.0)
  * `wait_serial_in` (Impact: 4.0)
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

### `src/arch/kim-1/kim-1-sdcard.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.16 IQR)
- **Top Global Matches:** file_cluster_8: 7.16, file_cluster_7: 8.222, file_cluster_1: 8.469
- **Magnitude:** 108.41 | **LOC:** 213 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.6118%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 2`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/arch/snes/charset.inc` (ASSEMBLY | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.476 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.406 IQR)
- **Top Global Matches:** file_cluster_8: 6.476, file_cluster_7: 7.74, file_cluster_1: 7.872
- **Magnitude:** 107.56 | **LOC:** 1157 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 72`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/arch/atari800/utils/setfnt.c` (C) | Magnitude: 79.06 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 56, indent_spaces: 46, branch: 14, pointers: 10
- `apps/mbrot.c` (C) | Magnitude: 87.76 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 65, indent_spaces: 51, api: 11, branch: 6
- `tools/cpmemu/fileio.c` (C) | Magnitude: 0.46 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 308, state_mutation: 234, pointers: 105, branch: 79
- `src/arch/neo6502/utils/nattr.c` (C) | Magnitude: 145.58 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 85, state_mutation: 69, branch: 27, api: 16
- `tools/multilink.cc` (CPP) | Magnitude: 0.19 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 129, state_mutation: 112, branch: 28, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/arch/apple2e/mame-test.lua` (LUA) | Magnitude: 38.04 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 13, structural_boundaries: 12, branch: 9
- `src/arch/atari800/mame-test.lua` (LUA) | Magnitude: 38.04 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 13, structural_boundaries: 12, branch: 9
- `scripts/oric-mame-test.sh` (SHELL) | Magnitude: 1.09 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety_bypasses: 10, args: 7, indent_spaces: 6, branch: 4
- `src/arch/commodore/c64/c64-mame-test.lua` (LUA) | Magnitude: 41.2 | Delta: **0.159 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, state_mutation: 12, concurrency: 12, structural_boundaries: 11
- `src/arch/commodore/pet-mame-test.lua` (LUA) | Magnitude: 41.2 | Delta: **0.159 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, state_mutation: 12, concurrency: 12, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `apps/submit.c` (C) | Magnitude: 227.62 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 131, state_mutation: 127, branch: 41, structural_boundaries: 23
- `tools/cpmemu/biosbdos.c` (C) | Magnitude: 0.72 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 414, state_mutation: 341, branch: 180, structural_boundaries: 144
- `tools/mkoricdsk.cc` (CPP) | Magnitude: 0.25 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 163, indent_spaces: 153, branch: 37, globals: 14
- `apps/life.c` (C) | Magnitude: 219.34 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 120, state_mutation: 119, branch: 52, api: 16
- `src/arch/snes/tools/build.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, import: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/arch/commodore/pet.S` -> **nick-less** (100.0% isolated ownership) | Magnitude: 103.22
- `src/arch/kim-1/utils/imu-k1013.S` -> **eduardocasino** (100.0% isolated ownership) | Magnitude: 101.58

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `config.py` -> **Severity: 3.557** (Embedded: 0.0609 * Error Risk: 58.3877%)
- `apps/drivers.inc` -> **Severity: 3.553** (Embedded: 0.0355 * Error Risk: 99.9903%)
- `apps/sys.c` -> **Severity: 1.439** (Embedded: 0.0152 * Error Risk: 94.4909%)
- `src/bdos/filesystem.S` -> **Severity: 0.532** (Embedded: 0.0102 * Error Risk: 52.4346%)
- `src/arch/snes/snes.inc` -> **Severity: 0.497** (Embedded: 0.0051 * Error Risk: 97.9215%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tools/cpmemu/globals.h` -> **Severity: 2279.6** (Blast Radius: 22.796 * Doc Risk: 100.0%)
- `src/arch/neo6502/utils/neo6502.h` -> **Severity: 1600.423** (Blast Radius: 22.796 * Doc Risk: 70.2063%)
- `apps/sys.c` -> **Severity: 1455.98** (Blast Radius: 15.414 * Doc Risk: 94.4583%)
- `tools/libbdf.h` -> **Severity: 1172.38** (Blast Radius: 11.724 * Doc Risk: 99.9983%)
- `config.py` -> **Severity: 869.542** (Blast Radius: 48.631 * Doc Risk: 17.8804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
