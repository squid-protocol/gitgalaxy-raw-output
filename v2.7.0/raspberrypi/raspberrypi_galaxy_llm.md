# ARCHITECTURAL_BRIEF: raspberrypi
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dwelch67/raspberrypi.git` |
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
| Total Artifacts | 930 |
| Analyzed Artifacts (Scanned) | 616 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 314 |
| Total LOC | 48095 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.75 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 258 | 39421 | 41.9% |
| MARKDOWN | 117 | 0 | 19.0% |
| ASSEMBLY | 117 | 5097 | 19.0% |
| MAKEFILE | 101 | 3563 | 16.4% |
| BINARY_THREAT | 14 | 14 | 2.3% |
| PLAINTEXT | 9 | 0 | 1.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.275`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 476 | 77.3% |
| Unknown | 14 | 2.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 126 | 20.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 314*

**Composition by Extension & Reason:**
- `no_extension`: 109x Unsupported Format (.undeterminable), 1x Excluded (Lexical Monotony: High structural repetition detected in 2756 LOC)
- `.o`: 58x Excluded (Explicitly Denied Extension: '.o')
- `.elf`: 28x Excluded (Unsupported Extension: '.elf')
- `.list`: 28x Excluded (Unsupported Extension: '.list')
- `.hex`: 25x Excluded (Unsupported Extension: '.hex'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 20x Excluded (Unsupported Extension: '.cfg')
- `.img`: 15x Excluded (Unsupported Extension: '.img')
- `.h`: 3x Excluded (Embedded Hex Payload: 4352 hex tokens in 2822 LOC), 3x Zero-Density Threshold (LOC: 120, Signals: 0), 2x Excluded (Embedded Hex Payload: 4402 hex tokens in 2906 LOC)
- `.ps`: 6x Excluded (Unsupported Extension: '.ps')
- `.s`: 2x Statistical Anomaly (Z-Score: -5.51 < -4.55), 1x Excluded (Monolithic Amalgamation: 1048579 LOC exceeds safe regex boundaries), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 3x Excluded (Machine-Generated Source Code Signature: 307 LOC)
- `.bc`: 2x Excluded (Unsupported Extension: '.bc')
- `.a`: 1x Excluded (Explicitly Denied Extension: '.a')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.3 | 23.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 37.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 47.3 | 50.2 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 9.6 | 2.5 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 89.1 | 11.9 | 8.2 | 8.2 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 39.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 53.7 | 3.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 88.8 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 85.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6670 | 180 | 4 | `zlib/deflate.c` |
| cleanup | 773 | 120 | 8 | `spi01/Makefile` |
| guards | 565 | 71 | 1 | `twain/zlib.h` |
| danger | 135 | 30 | 0 | `zlib/deflate.c` |
| concurrency | 60 | 10 | 0 | `boards/pi2/SVC/blinker01/vectors.s` |
| connectivity | 3656 | 458 | 15 | `twain/zlib.h` |
| io | 204 | 118 | 2 | `tas/tas.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 51 | 12 | 0 | `boards/piaplus/mmu/novectors.s` |
| tests | 0 | 0 | 0 | - |
| docs | 39 | 14 | 0 | `twain/inflate.c` |
| debt | 414 | 29 | 0 | `tas/tas.c` |
| mutation | 11898 | 310 | 37 | `tas/tas.c` |
| dead_code | 1587 | 359 | 8 | `boards/pizero/asmdelay/start.s` |
| credential | 0 | 0 | 0 | - |
| threat | 343 | 33 | 0 | `twain/inflate.c` |
| ml_ai | 582 | 88 | 1 | `twain/Makefile` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tas/tas.c` (Hits: 7)
- `spi01/blinker02.s` (Hits: 6)
- `bootloader07/Makefile` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ser.h** (`bootloader01/ser.h`) — 1 inbound connections
2. **blinker.h** (`spi01/blinker.h`) — 1 inbound connections
3. **twaindef.h** (`twain/twaindef.h`) — 1 inbound connections
4. **README** (`README`) — 0 inbound connections
5. **README** (`aarch64/README`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **parport.c** (`jtagproxy/ft232rl/parport.c`) — 12 outbound dependencies
2. **parport_fast.c** (`jtagproxy/ft232rl/parport_fast.c`) — 12 outbound dependencies
3. **parport.c** (`jtagproxy/msplaunchpad/parport.c`) — 11 outbound dependencies
4. **syscalls.c** (`newlib0/syscalls.c`) — 10 outbound dependencies
5. **ser.c** (`bootloader01/ser.c`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `assemble` (@ `tas/tas.c`) -> Impact: **720.5** | LOC: 1513
  * *Intent:* //-------------------------------------------------------------------
- `inflate` (@ `twain/inflate.c`) -> Impact: **392.7** | LOC: 648
  * *Intent:* */
- `inflate` (@ `zlib/inflate.c`) -> Impact: **392.7** | LOC: 648
  * *Intent:* */
- `inflate` (@ `zlib/thumb/inflate.c`) -> Impact: **392.7** | LOC: 648
  * *Intent:* */
- `dissassemble` (@ `tas/tas.c`) -> Impact: **295.9** | LOC: 597
  * *Intent:* //-------------------------------------------------------------------
- `deflate` (@ `twain/deflate.c`) -> Impact: **206.1** | LOC: 312
  * *Intent:* /* ========================================================================= */
- `deflate` (@ `zlib/deflate.c`) -> Impact: **206.1** | LOC: 312
  * *Intent:* /* ========================================================================= */
- `deflate` (@ `zlib/thumb/deflate.c`) -> Impact: **206.1** | LOC: 312
  * *Intent:* /* ========================================================================= */
- `_tr_flush_block` (@ `twain/trees.c`) -> Impact: **129.9** | LOC: 318
  * *Intent:* /* =========================================================================== * Determine the best encoding for the current block: dynamic trees, sta...
- `_tr_flush_block` (@ `zlib/thumb/trees.c`) -> Impact: **129.9** | LOC: 318
  * *Intent:* /* =========================================================================== * Determine the best encoding for the current block: dynamic trees, sta...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `twain` | 25 | 6965.32 | 38.1% | 26.6% |
| `zlib` | 25 | 6949.56 | 38.77% | 30.19% |
| `zlib/thumb` | 24 | 6907.38 | 39.06% | 28.86% |
| `tas` | 6 | 4058.14 | 24.44% | 41.56% |
| `uart02` | 7 | 1255.62 | 9.98% | 18.91% |
| `zero_start` | 8 | 1201.36 | 14.52% | 48.87% |
| `bootloader06` | 8 | 837.5 | 22.79% | 47.1% |
| `bootloader01` | 9 | 822.8 | 27.4% | 43.35% |
| `bootloader05` | 8 | 810.54 | 23.09% | 47.65% |
| `boards/pizero/float02` | 7 | 775.52 | 26.49% | 32.64% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `atags/vectors.s` -> **100.0%** Exposure
- `boards/pi1/bootloader07/vectors.s` -> **100.0%** Exposure
- `boards/pi2/bootloader07/vectors.s` -> **100.0%** Exposure
- `boards/pi3/aarch32/bootloader07/vectors.s` -> **100.0%** Exposure
- `boards/pi3/imgtest/bs32.s` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `armjtag/armjtag.c` -> **100.0%** Exposure
- `armjtag/rpi2/armjtag.c` -> **100.0%** Exposure
- `bench02/uart.c` -> **100.0%** Exposure
- `blinker07/blinker07.c` -> **100.0%** Exposure
- `blinker08/blinker08.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `boards/pizero/asmdelay/start.s` -> **16** Orphaned Functions | **0** Duplicates
- `bench02/novectors.s` -> **15** Orphaned Functions | **0** Duplicates
- `boards/pi2/SVC_BOOT/uart01/vectors.s` -> **14** Orphaned Functions | **0** Duplicates
- `boards/pi2/SVC_BOOT/uart02/vectors.s` -> **14** Orphaned Functions | **0** Duplicates
- `boards/pi2/bootloader07/vectors.s` -> **11** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `87` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `212` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `twain/zutil.c` (C) -> Cumulative Risk: **660.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 222.12 | **LOC:** 325 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.9157%)
- **Heaviest Functions:** `zlibCompileFlags` (Impact: 32.1), `zcalloc` (Impact: 13.2), `zcfree` (Impact: 9.7)

### 2. `zlib/thumb/zutil.c` (C) -> Cumulative Risk: **655.21**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 228.2 | **LOC:** 325 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (95.3033%)
- **Heaviest Functions:** `zlibCompileFlags` (Impact: 32.1), `zcalloc` (Impact: 13.2), `zcfree` (Impact: 9.7)

### 3. `zlib/zutil.c` (C) -> Cumulative Risk: **655.21**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 228.2 | **LOC:** 325 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (95.3033%)
- **Heaviest Functions:** `zlibCompileFlags` (Impact: 32.1), `zcalloc` (Impact: 13.2), `zcfree` (Impact: 9.7)

### 4. `zlib/inflate.c` (C) -> Cumulative Risk: **623.16**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1807.58 | **LOC:** 1497 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.7247%)
- **Heaviest Functions:** `inflate` (Impact: 392.7), `inflateInit2_` (Impact: 26.6), `inflateCopy` (Impact: 23.1)

### 5. `zlib/thumb/inflate.c` (C) -> Cumulative Risk: **623.16**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1807.58 | **LOC:** 1497 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.7247%)
- **Heaviest Functions:** `inflate` (Impact: 392.7), `inflateInit2_` (Impact: 26.6), `inflateCopy` (Impact: 23.1)

### 6. `twain/inflate.c` (C) -> Cumulative Risk: **613.83**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1741.1 | **LOC:** 1497 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.652%)
- **Heaviest Functions:** `inflate` (Impact: 392.7), `inflateInit2_` (Impact: 26.6), `inflateCopy` (Impact: 23.1)

### 7. `boards/piaplus/float02/slowfloat.c` (C) -> Cumulative Risk: **602.47**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 526.92 | **LOC:** 665 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.1256%)
- **Heaviest Functions:** `floatXAdd` (Impact: 52.0), `floatXToFloat32` (Impact: 45.0), `roundFloatXTo24` (Impact: 25.9)

### 8. `boards/pizero/float02/slowfloat.c` (C) -> Cumulative Risk: **602.47**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 526.92 | **LOC:** 665 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.1256%)
- **Heaviest Functions:** `floatXAdd` (Impact: 52.0), `floatXToFloat32` (Impact: 45.0), `roundFloatXTo24` (Impact: 25.9)

### 9. `float02/slowfloat.c` (C) -> Cumulative Risk: **602.47**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 526.92 | **LOC:** 665 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.1256%)
- **Heaviest Functions:** `floatXAdd` (Impact: 52.0), `floatXToFloat32` (Impact: 45.0), `roundFloatXTo24` (Impact: 25.9)

### 10. `twain/deflate.c` (C) -> Cumulative Risk: **601.1**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2015.84 | **LOC:** 1966 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.3455%)
- **Heaviest Functions:** `deflate` (Impact: 206.1), `deflateInit2_` (Impact: 95.4), `longest_match` (Impact: 78.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tas/tas.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4005.52 | **LOC:** 2936 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.0895%), Tech Debt (8.3006%)
**Top Internal Functions/Classes:**
  * `assemble` (Impact: 720.5)
    * *Intent:* //-------------------------------------------------------------------
  * `dissassemble` (Impact: 295.9)
    * *Intent:* //-------------------------------------------------------------------
  * `main` (Impact: 95.3)
    * *Intent:* //-------------------------------------------------------------------
  * `parse_immed` (Impact: 32.4)
    * *Intent:* //-------------------------------------------------------------------
  * `parse_low_reg` (Impact: 19.8)
    * *Intent:* //-------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 885 instances
* *State Mutation (weighted view):* 2700
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 727`, `structural_boundaries: 495`, `args: 14`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 930`, `unreferenced_by_name: 2`
* *Architecture:* `io: 7`, `api: 13`, `import: 3`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zlib/deflate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2022.9 | **LOC:** 1966 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.5422%), Tech Debt (25.4616%)
**Top Internal Functions/Classes:**
  * `deflate` (Impact: 206.1)
    * *Intent:* /* ========================================================================= */
  * `deflateInit2_` (Impact: 95.4)
    * *Intent:* /* ========================================================================= */
  * `longest_match` (Impact: 78.1)
    * *Intent:* #ifndef FASTEST /* =========================================================================== * Set...
  * `deflate_slow` (Impact: 59.9)
    * *Intent:* #ifndef FASTEST /* =========================================================================== * Sam...
  * `deflate_rle` (Impact: 50.2)
    * *Intent:* #endif /* FASTEST */ /* =========================================================================== ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 336 instances
* *State Mutation (weighted view):* 1064
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 107`, `args: 2`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 392`, `dead_code: 5`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 43`, `import: 1`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` deflate.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zlib/thumb/deflate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2022.9 | **LOC:** 1966 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.5422%), Tech Debt (25.4616%)
**Top Internal Functions/Classes:**
  * `deflate` (Impact: 206.1)
    * *Intent:* /* ========================================================================= */
  * `deflateInit2_` (Impact: 95.4)
    * *Intent:* /* ========================================================================= */
  * `longest_match` (Impact: 78.1)
    * *Intent:* #ifndef FASTEST /* =========================================================================== * Set...
  * `deflate_slow` (Impact: 59.9)
    * *Intent:* #ifndef FASTEST /* =========================================================================== * Sam...
  * `deflate_rle` (Impact: 50.2)
    * *Intent:* #endif /* FASTEST */ /* =========================================================================== ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 336 instances
* *State Mutation (weighted view):* 1064
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 107`, `args: 2`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 392`, `dead_code: 5`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 43`, `import: 1`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` deflate.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `twain/deflate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2015.84 | **LOC:** 1966 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.593%), Tech Debt (25.5235%)
**Top Internal Functions/Classes:**
  * `deflate` (Impact: 206.1)
    * *Intent:* /* ========================================================================= */
  * `deflateInit2_` (Impact: 95.4)
    * *Intent:* /* ========================================================================= */
  * `longest_match` (Impact: 78.1)
    * *Intent:* #ifndef FASTEST /* =========================================================================== * Set...
  * `deflate_slow` (Impact: 59.9)
    * *Intent:* #ifndef FASTEST /* =========================================================================== * Sam...
  * `deflate_rle` (Impact: 50.2)
    * *Intent:* #endif /* FASTEST */ /* =========================================================================== ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 334 instances
* *State Mutation (weighted view):* 1057
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 107`, `args: 5`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 389`, `dead_code: 5`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 43`, `import: 1`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` deflate.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zlib/inflate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1807.58 | **LOC:** 1497 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.3486%), Tech Debt (33.7977%)
**Top Internal Functions/Classes:**
  * `inflate` (Impact: 392.7)
    * *Intent:* */
  * `inflateInit2_` (Impact: 26.6)
  * `inflateCopy` (Impact: 23.1)
  * `updatewindow` (Impact: 21.5)
    * *Intent:* */
  * `inflateReset2` (Impact: 20.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 373 instances
* *State Mutation (weighted view):* 1141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 333`, `structural_boundaries: 142`, `args: 5`, `func_start: 19`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 395`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 22`, `import: 6`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inffast.h, inffixed.h, inflate.h, inftrees.h, stdio.h, zutil.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zlib/thumb/inflate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1807.58 | **LOC:** 1497 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.3486%), Tech Debt (33.7977%)
**Top Internal Functions/Classes:**
  * `inflate` (Impact: 392.7)
    * *Intent:* */
  * `inflateInit2_` (Impact: 26.6)
  * `inflateCopy` (Impact: 23.1)
  * `updatewindow` (Impact: 21.5)
    * *Intent:* */
  * `inflateReset2` (Impact: 20.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 373 instances
* *State Mutation (weighted view):* 1141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 333`, `structural_boundaries: 142`, `args: 5`, `func_start: 19`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 395`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 22`, `import: 6`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inffast.h, inffixed.h, inflate.h, inftrees.h, stdio.h, zutil.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `twain/inflate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1741.1 | **LOC:** 1497 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.2162%), Tech Debt (34.6755%)
**Top Internal Functions/Classes:**
  * `inflate` (Impact: 392.7)
    * *Intent:* */
  * `inflateInit2_` (Impact: 26.6)
  * `inflateCopy` (Impact: 23.1)
  * `updatewindow` (Impact: 21.5)
    * *Intent:* */
  * `inflateReset2` (Impact: 20.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 352 instances
* *State Mutation (weighted view):* 1075
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 333`, `structural_boundaries: 142`, `args: 5`, `func_start: 19`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 371`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `doc: 12`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inffast.h, inffixed.h, inflate.h, inftrees.h, zutil.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `twain/trees.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1223.6 | **LOC:** 1225 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.128%), Tech Debt (14.4759%)
**Top Internal Functions/Classes:**
  * `_tr_flush_block` (Impact: 129.9)
    * *Intent:* /* =========================================================================== * Determine the best ...
  * `send_tree` (Impact: 44.3)
    * *Intent:* /* =========================================================================== * Send a literal or d...
  * `scan_tree` (Impact: 36.0)
    * *Intent:* /* =========================================================================== * Scan a literal or d...
  * `gen_bitlen` (Impact: 29.9)
    * *Intent:* /* =========================================================================== * Compute the optimal...
  * `build_tree` (Impact: 24.9)
    * *Intent:* /* =========================================================================== * Construct one Huffm...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 233 instances
* *State Mutation (weighted view):* 722
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 55`, `args: 4`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 256`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 43`, `import: 3`
* *Defense:* `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` deflate.h, stdio.h, trees.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zlib/thumb/trees.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1223.6 | **LOC:** 1225 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.128%), Tech Debt (14.4759%)
**Top Internal Functions/Classes:**
  * `_tr_flush_block` (Impact: 129.9)
    * *Intent:* /* =========================================================================== * Determine the best ...
  * `send_tree` (Impact: 44.3)
    * *Intent:* /* =========================================================================== * Send a literal or d...
  * `scan_tree` (Impact: 36.0)
    * *Intent:* /* =========================================================================== * Scan a literal or d...
  * `gen_bitlen` (Impact: 29.9)
    * *Intent:* /* =========================================================================== * Compute the optimal...
  * `build_tree` (Impact: 24.9)
    * *Intent:* /* =========================================================================== * Construct one Huffm...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 233 instances
* *State Mutation (weighted view):* 722
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 55`, `args: 4`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 256`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 43`, `import: 4`
* *Defense:* `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, deflate.h, stdio.h, trees.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zlib/trees.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1223.6 | **LOC:** 1225 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.128%), Tech Debt (14.4759%)
**Top Internal Functions/Classes:**
  * `_tr_flush_block` (Impact: 129.9)
    * *Intent:* /* =========================================================================== * Determine the best ...
  * `send_tree` (Impact: 44.3)
    * *Intent:* /* =========================================================================== * Send a literal or d...
  * `scan_tree` (Impact: 36.0)
    * *Intent:* /* =========================================================================== * Scan a literal or d...
  * `gen_bitlen` (Impact: 29.9)
    * *Intent:* /* =========================================================================== * Compute the optimal...
  * `build_tree` (Impact: 24.9)
    * *Intent:* /* =========================================================================== * Construct one Huffm...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 233 instances
* *State Mutation (weighted view):* 722
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 55`, `args: 4`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 256`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 43`, `import: 4`
* *Defense:* `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, deflate.h, stdio.h, trees.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/piaplus/float02/slowfloat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 526.92 | **LOC:** 665 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.5978%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `floatXAdd` (Impact: 52.0)
  * `floatXToFloat32` (Impact: 45.0)
  * `roundFloatXTo24` (Impact: 25.9)
    * *Intent:* //static flag le64( bits64X a, bits64X b ) //{ //return ( a.a0 < b.a0 ) || ( ( a.a0 == b.a0 ) && ( a...
  * `roundFloatXTo53` (Impact: 25.9)
  * `floatXToInt32` (Impact: 21.6)
    * *Intent:* //ax.isZero = TRUE; //return ax; //} //ax.isZero = FALSE; //ax.sig = shortShift64Left( ax.sig, 23 );...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 287
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 64`, `args: 15`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `state_mutation: 107`, `dead_code: 6`
* *Architecture:* `api: 22`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pizero/float02/slowfloat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 526.92 | **LOC:** 665 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.5978%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `floatXAdd` (Impact: 52.0)
  * `floatXToFloat32` (Impact: 45.0)
  * `roundFloatXTo24` (Impact: 25.9)
    * *Intent:* //static flag le64( bits64X a, bits64X b ) //{ //return ( a.a0 < b.a0 ) || ( ( a.a0 == b.a0 ) && ( a...
  * `roundFloatXTo53` (Impact: 25.9)
  * `floatXToInt32` (Impact: 21.6)
    * *Intent:* //ax.isZero = TRUE; //return ax; //} //ax.isZero = FALSE; //ax.sig = shortShift64Left( ax.sig, 23 );...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 287
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 64`, `args: 15`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `state_mutation: 107`, `dead_code: 6`
* *Architecture:* `api: 22`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `float02/slowfloat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 526.92 | **LOC:** 665 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.5978%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `floatXAdd` (Impact: 52.0)
  * `floatXToFloat32` (Impact: 45.0)
  * `roundFloatXTo24` (Impact: 25.9)
    * *Intent:* //static flag le64( bits64X a, bits64X b ) //{ //return ( a.a0 < b.a0 ) || ( ( a.a0 == b.a0 ) && ( a...
  * `roundFloatXTo53` (Impact: 25.9)
  * `floatXToInt32` (Impact: 21.6)
    * *Intent:* //ax.isZero = TRUE; //return ax; //} //ax.isZero = FALSE; //ax.sig = shortShift64Left( ax.sig, 23 );...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 287
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 64`, `args: 15`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `state_mutation: 107`, `dead_code: 6`
* *Architecture:* `api: 22`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `armjtag/armjtag.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `armjtag/rpi2/armjtag.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `blinker01/blinker01.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pi1/blinker01/blinker01.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pi2/HYP/blinker01/blinker01.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pi2/SVC/blinker01/blinker01.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/piaplus/blinker01/blinker01.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `boards/pizero/blinker01/blinker01.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bootloader05/blinker.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bootloader06/blinker.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `uart02/uart02.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `uart02/uart02.clang.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `armjtag/Makefile` -> **Severity: 159.9** (Blast Radius: 1.599 * Doc Risk: 100.0%)
- `armjtag/rpi2/Makefile` -> **Severity: 159.9** (Blast Radius: 1.599 * Doc Risk: 100.0%)
- `atags/Makefile` -> **Severity: 159.9** (Blast Radius: 1.599 * Doc Risk: 100.0%)
- `bench02/Makefile` -> **Severity: 159.9** (Blast Radius: 1.599 * Doc Risk: 100.0%)
- `blinker01/Makefile` -> **Severity: 159.9** (Blast Radius: 1.599 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
