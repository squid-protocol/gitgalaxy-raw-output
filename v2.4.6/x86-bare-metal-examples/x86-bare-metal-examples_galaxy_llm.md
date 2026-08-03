# ARCHITECTURAL_BRIEF: x86-bare-metal-examples
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/x86-bare-metal-examples` |
| **Timestamp** | `2026-08-03T19:27:41.470349+00:00` |
| **Scan Duration** | `0.27s` |
| **Git Branch** | `master` |
| **Git Commit** | `528ab2becc4992218ca0b7e297f3e1f1674268de` |
| **Git Remote** | `https://github.com/cirosantilli/x86-bare-metal-examples.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 19 malicious artifacts.

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
| Total Artifacts | 116 |
| Analyzed Artifacts (Scanned) | 98 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 18 |
| Total LOC | 2492 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 84.5% |
| Dominant Lang | ASSEMBLY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 67 | 1833 | 68.4% |
| MARKDOWN | 12 | 0 | 12.2% |
| MAKEFILE | 9 | 210 | 9.2% |
| SHELL | 5 | 56 | 5.1% |
| C | 5 | 393 | 5.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.609`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 85 | 86.7% |
| file_cluster_9 | 1 | 1.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 12 | 12.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 18*

**Composition by Extension & Reason:**
- `.ld`: 4x Excluded (Unsupported Extension: '.ld')
- `.cfg`: 4x Excluded (Unsupported Extension: '.cfg')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.adoc`: 1x Excluded (Lexical Monotony: High structural repetition detected in 2455 LOC)
- `.gdb`: 1x Excluded (Unsupported Extension: '.gdb')
- `.sym`: 1x Excluded (Unsupported Extension: '.sym')
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bld`: 1x Excluded (Unsupported Extension: '.bld')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.fd`: 1x Excluded (Unsupported Extension: '.fd')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 99.5 | 18.1 | 10.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 35.8 | 36.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 33.7 | 0.0 | 0.0 |
| Testing Exposure | 0.4 | 3.2 | 2.1 | 2.3 | 2.3 |
| API Exposure | 0.0 | 12.1 | 1.7 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 35.7 | 0.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 13.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 98.1 | 1.1 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 84.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 3.2 | 100.0 | 70.8 | 84.5 | 46.7 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 0.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 5.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `rtc.S` (Hits: 18)
- `serial.S` (Hits: 9)
- `pc_speaker.S` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **LICENSE.adoc** (`LICENSE.adoc`) — 0 inbound connections
2. **README.adoc** (`c_hello_world/README.adoc`) — 0 inbound connections
3. **README.adoc** (`grub/README.adoc`) — 0 inbound connections
4. **README.adoc** (`grub/chainloader/README.adoc`) — 0 inbound connections
5. **README.adoc** (`grub/linux/README.adoc`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **kernel.c** (`multiboot/osdev/kernel.c`) — 3 outbound dependencies
2. **main.c** (`uefi/main.c`) — 2 outbound dependencies
3. **main.c** (`multiboot/hello-world/main.c`) — 1 outbound dependencies
4. **LICENSE.adoc** (`LICENSE.adoc`) — 0 outbound dependencies
5. **README.adoc** (`c_hello_world/README.adoc`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `loop` (@ `ps2_keyboard.S`) -> Impact: **17.4** | LOC: 9
- `do_e820` (@ `bios_detect_memory.S`) -> Impact: **12.8** | LOC: 15
  * *Intent:* /* This was copy pasted from: * http://wiki.osdev.org/Detecting_Memory_%28x86%29#Getting_an_E820_Memory_Map * * use the INT 0x15, eax= 0xE820 BIOS fun...
- `clear` (@ `multiboot/hello-world/main.c`) -> Impact: **12.3** | LOC: 6
- `CLEAR_LABEL` (@ `intel-protected/startup.asm`) -> Impact: **11.3** | LOC: 141
- `update_in_progress` (@ `rtc.S`) -> Impact: **10.8** | LOC: 56
- `loop` (@ `bios_serial.S`) -> Impact: **10.4** | LOC: 8
- `loop` (@ `bios_hello_world.S`) -> Impact: **10.3** | LOC: 6
- `loop` (@ `no-linker-script/main.S`) -> Impact: **10.3** | LOC: 6
- `start` (@ `bios_pixel.S`) -> Impact: **9.5** | LOC: 20
- `Anonymous_Block_[Truncated]` (@ `nasm/run`) -> Impact: **9.0** | LOC: 11

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `do_e820` (@ `bios_detect_memory.S`) -> **O(2^N) [Recursive]**
  * *Intent:* /* This was copy pasted from: * http://wiki.osdev.org/Detecting_Memory_%28x86%29#Getting_an_E820_Memory_Map * * use the INT 0x15, eax= 0xE820 BIOS fun...
- `stage2` (@ `bios_disk_load.S`) -> **O(2^N) [Recursive]**
- `loop` (@ `bios_hello_world.S`) -> **O(2^N) [Recursive]**
- `start` (@ `bios_keyboard_loop.S`) -> **O(2^N) [Recursive]**
- `start` (@ `bios_pixel.S`) -> **O(2^N) [Recursive]**
- `start` (@ `bios_pixel_line.S`) -> **O(2^N) [Recursive]**
- `loop` (@ `bios_serial.S`) -> **O(2^N) [Recursive]**
- `one_sec` (@ `bios_sleep.S`) -> **O(2^N) [Recursive]**
- `loop` (@ `infinite_loop.S`) -> **O(2^N) [Recursive]**
- `main_start` (@ `intel-protected/main.asm`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `update_in_progress` (@ `rtc.S`) -> DB Complexity: **42**
- `loop` (@ `pc_speaker.S`) -> DB Complexity: **9**
  * *Intent:* /* Loop forever to keep hearing it. */
- `CLEAR_LABEL` (@ `intel-protected/startup.asm`) -> DB Complexity: **6**
- `Anonymous_Block` (@ `configure`) -> DB Complexity: **4**
  * *Intent:* #!/usr/bin/env bash # grub-pc-bin: without it, grub-mkrescue just fails, and you have no idea why! # We love you, GRUB. # https://superuser.com/questi...
- `clear` (@ `multiboot/hello-world/main.c`) -> DB Complexity: **4**
- `loop` (@ `bios_serial.S`) -> DB Complexity: **3**
- `loop` (@ `ps2_keyboard.S`) -> DB Complexity: **3**
- `msg` (@ `real_segmentation.S`) -> DB Complexity: **3**
- `not_started` (@ `smp.S`) -> DB Complexity: **3**
  * *Intent:* /* TODO improve this spinlock. */
- `Anonymous_Block_[Truncated]` (@ `nasm/run`) -> DB Complexity: **3**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 61 | 587.32 | 18.01% | 28.8% |
| `nasm` | 8 | 153.08 | 20.92% | 45.96% |
| `multiboot/hello-world` | 4 | 81.3 | 24.93% | 24.83% |
| `uefi` | 3 | 55.62 | 11.41% | 33.33% |
| `multiboot/osdev` | 4 | 43.36 | 8.84% | 25.0% |
| `intel-protected` | 3 | 41.8 | 3.74% | 25.69% |
| `no-linker-script` | 3 | 34.5 | 25.02% | 0.0% |
| `grub/chainloader` | 2 | 28.68 | 2.5% | 0.0% |
| `c_hello_world` | 5 | 23.68 | 4.0% | 80.0% |
| `grub/linux` | 2 | 19.26 | 2.5% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `c_hello_world/entry.S` -> **100.0%** Exposure
- `pit_once.S` -> **100.0%** Exposure
- `c_hello_world/clean` -> **100.0%** Exposure
- `c_hello_world/run` -> **100.0%** Exposure
- `nasm/run` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `configure` -> **100.0%** Exposure
- `nasm/run` -> **100.0%** Exposure
- `run` -> **100.0%** Exposure
- `c_hello_world/main.c` -> **100.0%** Exposure
- `multiboot/hello-world/main.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `bios_detect_memory.S` -> **6** Orphaned Functions | **0** Duplicates
- `nasm/protected_mode_so.asm` -> **3** Orphaned Functions | **0** Duplicates
- `apm_shutdown2.S` -> **2** Orphaned Functions | **0** Duplicates
- `intel-protected/startup.asm` -> **0** Orphaned Functions | **2** Duplicates
- `nasm/bios_hello_world.asm` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`multiboot/osdev/kernel.c`** -> AI Confidence: **99.32%**
2. **`grub/chainloader/Makefile`** -> AI Confidence: **99.29%**
3. **`configure`** -> AI Confidence: **99.29%**
4. **`nasm/run`** -> AI Confidence: **99.29%**
5. **`run`** -> AI Confidence: **99.29%**
6. **`common.h`** -> AI Confidence: **99.29%**
7. **`c_hello_world/main.c`** -> AI Confidence: **99.06%**
8. **`multiboot/hello-world/main.c`** -> AI Confidence: **98.86%**
9. **`Makefile`** -> AI Confidence: **98.84%**
10. **`grub/linux/Makefile`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `multiboot/hello-world/main.c` -> **20.0%** Exposure
- `bios_clear_screen.S` -> **16.2479%** Exposure
- `real_segmentation.S` -> **13.3908%** Exposure
- `serial.S` -> **13.1935%** Exposure
- `smp.S` -> **11.5694%** Exposure
### Weaponizable Injection Vectors
- `printf/Makefile` -> **100.0%** Exposure
- `bios_clear_screen.S` -> **99.9999%** Exposure
- `real_segmentation.S` -> **99.9998%** Exposure
- `serial.S` -> **99.9995%** Exposure
- `smp.S` -> **99.9937%** Exposure
### Raw Memory Manipulation
- `intel-protected/startup.asm` -> **0.0434%** Exposure
### Algorithmic DoS Exposure
- `multiboot/hello-world/main.c` -> **100.0%** Exposure
- `bios_detect_memory.S` -> **1.6097%** Exposure
- `bios_initial_state.S` -> **1.1319%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `configure` (SHELL) -> Cumulative Risk: **591.85**
- **Archetype:** `file_cluster_8` (Distance: 10.942 IQR)
- **Magnitude:** 18.22 | **LOC:** 30 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9729%), Safety Score (99.6922%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 4.3), `__global_context__` (Impact: 1.5)

### 2. `multiboot/hello-world/main.c` (C) -> Cumulative Risk: **567.23**
- **Archetype:** `file_cluster_8` (Distance: 12.857 IQR)
- **Magnitude:** 49.16 | **LOC:** 37 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `clear` (Impact: 12.3), `puts` (Impact: 3.2), `putc` (Impact: 1.1)

### 3. `bios_clear_screen.S` (ASSEMBLY) -> Cumulative Risk: **484.42**
- **Archetype:** `file_cluster_8` (Distance: 6.193 IQR)
- **Magnitude:** 15.48 | **LOC:** 33 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (99.9999%), Tech Debt (99.177%), Documentation (88.9355%)

### 4. `bios_pixel_line.S` (ASSEMBLY) -> Cumulative Risk: **464.76**
- **Archetype:** `file_cluster_8` (Distance: 10.236 IQR)
- **Magnitude:** 13.94 | **LOC:** 20 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9994%), Documentation (97.7376%), Cognitive Load (93.3829%)
- **Heaviest Functions:** `start` (Impact: 6.5), `end` (Impact: 1.1)

### 5. `c_hello_world/main.c` (C) -> Cumulative Risk: **449.37**
- **Archetype:** `file_cluster_8` (Distance: 12.572 IQR)
- **Magnitude:** 15.24 | **LOC:** 13 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Tech Debt (99.9955%), Spec Match (80.0%), Documentation (79.999%)
- **Heaviest Functions:** `main` (Impact: 3.0)

### 6. `nasm/bios_hello_world.asm` (ASSEMBLY) -> Cumulative Risk: **447.65**
- **Archetype:** `file_cluster_8` (Distance: 8.277 IQR)
- **Magnitude:** 11.7 | **LOC:** 22 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), Documentation (94.7896%), Safety Score (80.0%)
- **Heaviest Functions:** `.loop` (Impact: 7.4), `start` (Impact: 1.6), `msg` (Impact: 1.2)

### 7. `nasm/run` (SHELL) -> Cumulative Risk: **430.94**
- **Archetype:** `file_cluster_8` (Distance: 14.918 IQR)
- **Magnitude:** 22.76 | **LOC:** 14 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (86.6667%), Documentation (86.3754%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 9.0), `__global_context__` (Impact: 1.5)

### 8. `run` (SHELL) -> Cumulative Risk: **430.94**
- **Archetype:** `file_cluster_8` (Distance: 14.918 IQR)
- **Magnitude:** 22.76 | **LOC:** 14 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (86.6667%), Documentation (86.3754%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 9.0), `__global_context__` (Impact: 1.5)

### 9. `bios_cursor_position.S` (ASSEMBLY) -> Cumulative Risk: **405.77**
- **Archetype:** `file_cluster_8` (Distance: 6.493 IQR)
- **Magnitude:** 15.32 | **LOC:** 23 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9783%), Documentation (98.4113%), Safety Score (61.25%)

### 10. `bios_pixel.S` (ASSEMBLY) -> Cumulative Risk: **404.02**
- **Archetype:** `file_cluster_8` (Distance: 10.358 IQR)
- **Magnitude:** 17.12 | **LOC:** 30 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9201%), Documentation (85.4458%), Cognitive Load (66.648%)
- **Heaviest Functions:** `start` (Impact: 9.5), `end` (Impact: 1.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `uefi/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.335 IQR)
- **Top Global Matches:** file_cluster_8: 9.335, file_cluster_0: 10.022, file_cluster_7: 10.131
- **Magnitude:** 51.04 | **LOC:** 38 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 4`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common.h` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.759 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.37 IQR)
- **Top Global Matches:** file_cluster_8: 7.759, file_cluster_7: 8.683, file_cluster_1: 8.972
- **Magnitude:** 50.8 | **LOC:** 817 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0933%), Tech Debt (16.553%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`
* *Risk/State:* `state_mutation: 5`, `planned_debt: 5`
* *Architecture:* `io: 1`, `api: 24`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `multiboot/hello-world/main.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.857 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.554 IQR)
- **Top Global Matches:** file_cluster_8: 12.857, file_cluster_13: 12.868, file_cluster_0: 13.318
- **Magnitude:** 49.16 | **LOC:** 37 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (70.2063%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `clear` (Impact: 12.3 | O(N^3) | DB: 4)
  * `puts` (Impact: 3.2 | O(N^2) | DB: 2)
  * `putc` (Impact: 1.1 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 10`, `args: 1`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdint.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `intel-protected/startup.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.806 IQR)
- **Top Global Matches:** file_cluster_8: 7.806, file_cluster_7: 8.801, file_cluster_1: 8.902
- **Magnitude:** 38.26 | **LOC:** 394 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (6.2192%), Tech Debt (77.0583%)
**Top Internal Functions/Classes:**
  * `CLEAR_LABEL` (Impact: 11.3 | O(N^1) | DB: 6)
  * `GS` (Impact: 7.9 | O(N^1))
  * `STARTUP` (Impact: 3.7 | O(N^1))
  * `GS` (Impact: 1.5 | O(N^1))
    * *Intent:* ; fixup TSS pointer
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 65`, `args: 79`, `func_start: 5`, `class_start: 3`
* *Risk/State:* `state_mutation: 5`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 3`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.297 IQR)
- **Top Global Matches:** file_cluster_8: 7.297, file_cluster_17: 8.131, file_cluster_7: 8.433
- **Magnitude:** 36.08 | **LOC:** 83 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.188%), Tech Debt (67.7158%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 20`, `func_start: 6`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 4`, `concurrency: 1`
* *Defense:* `safety: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `nasm/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.297 IQR)
- **Top Global Matches:** file_cluster_8: 7.297, file_cluster_17: 8.131, file_cluster_7: 8.433
- **Magnitude:** 36.08 | **LOC:** 83 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.188%), Tech Debt (67.7158%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 20`, `func_start: 6`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 4`, `concurrency: 1`
* *Defense:* `safety: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bios_detect_memory.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.818 IQR)
- **Top Global Matches:** file_cluster_8: 6.818, file_cluster_1: 7.869, file_cluster_7: 8.0
- **Magnitude:** 33.54 | **LOC:** 75 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.1126%), Tech Debt (99.9757%)
**Top Internal Functions/Classes:**
  * `do_e820` (Impact: 12.8 | O(2^N))
    * *Intent:* /* This was copy pasted from: * http://wiki.osdev.org/Detecting_Memory_%28x86%29#Getting_an_E820_Mem...
  * `do_e820.jmpin` (Impact: 4.8 | O(N^2))
  * `do_e820.notext` (Impact: 3.3 | O(N^2))
  * `do_e820.e820f` (Impact: 3.2 | O(N^2))
  * `do_e820.skipent` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 15`, `args: 2`, `func_start: 8`
* *Risk/State:* `high_risk_execution: 1`, `orphaned_logic: 6`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `nasm/protected_mode_thiscouldbebetter.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.315 IQR)
- **Top Global Matches:** file_cluster_8: 9.315, file_cluster_1: 9.977, file_cluster_7: 10.133
- **Magnitude:** 31.02 | **LOC:** 116 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (22.8944%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `for_each_char` (Impact: 8.9 | O(2^N) | DB: 2)
  * `loop_forever` (Impact: 6.2 | O(2^N))
  * `stage2` (Impact: 5.2 | O(N^1))
  * `gdt` (Impact: 2.5 | O(2^N))
  * `gdt_end` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 20`, `args: 20`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `grub/chainloader/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.253 IQR)
- **Top Global Matches:** file_cluster_8: 9.253, file_cluster_7: 10.095, file_cluster_0: 10.209
- **Magnitude:** 27.68 | **LOC:** 14 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 3`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `nasm/protected_mode_so.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.526 IQR)
- **Top Global Matches:** file_cluster_8: 7.526, file_cluster_7: 8.622, file_cluster_1: 8.741
- **Magnitude:** 23.12 | **LOC:** 94 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.9256%), Tech Debt (99.9466%)
**Top Internal Functions/Classes:**
  * `.loop` (Impact: 7.6 | O(N^1))
  * `b32` (Impact: 5.0 | O(N^1))
  * `.done` (Impact: 2.1 | O(N^1))
  * `print32` (Impact: 1.6 | O(N^1))
  * `gdt_descriptor` (Impact: 1.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 25`, `args: 20`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `planned_debt: 1`, `orphaned_logic: 3`
* *Architecture:* None
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `nasm/run` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.918 IQR)
- **Top Global Matches:** file_cluster_8: 14.918, file_cluster_12: 15.164, file_cluster_17: 15.257
- **Magnitude:** 22.76 | **LOC:** 14 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 9.0 | O(N^1) | DB: 3)
  * `__global_context__` (Impact: 1.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 3`
* *Risk/State:* `state_mutation: 12`, `orphaned_logic: 2`
* *Architecture:* None
* *Defense:* `safety: 4`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.918 IQR)
- **Top Global Matches:** file_cluster_8: 14.918, file_cluster_12: 15.164, file_cluster_17: 15.257
- **Magnitude:** 22.76 | **LOC:** 14 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 9.0 | O(N^1) | DB: 3)
  * `__global_context__` (Impact: 1.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 3`
* *Risk/State:* `state_mutation: 12`, `orphaned_logic: 2`
* *Architecture:* None
* *Defense:* `safety: 4`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `multiboot/hello-world/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.027 IQR)
- **Top Global Matches:** file_cluster_8: 8.027, file_cluster_7: 9.053, file_cluster_1: 9.232
- **Magnitude:** 18.34 | **LOC:** 26 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.7308%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 7`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 3`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `multiboot/osdev/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.098 IQR)
- **Top Global Matches:** file_cluster_8: 8.098, file_cluster_7: 9.096, file_cluster_1: 9.298
- **Magnitude:** 18.28 | **LOC:** 23 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 3`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `grub/linux/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.891 IQR)
- **Top Global Matches:** file_cluster_8: 8.891, file_cluster_0: 9.774, file_cluster_7: 9.816
- **Magnitude:** 18.26 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `io: 3`, `api: 3`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `printf/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.181 IQR)
- **Top Global Matches:** file_cluster_8: 9.181, file_cluster_7: 10.06, file_cluster_0: 10.192
- **Magnitude:** 18.24 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 3`
* *Defense:* `safety: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `configure` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.942 IQR)
- **Top Global Matches:** file_cluster_8: 10.942, file_cluster_7: 11.561, file_cluster_0: 11.641
- **Magnitude:** 18.22 | **LOC:** 30 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (99.5195%), Tech Debt (99.9729%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 4.3 | O(N^1) | DB: 4)
    * *Intent:* #!/usr/bin/env bash # grub-pc-bin: without it, grub-mkrescue just fails, and you have no idea why! #...
  * `__global_context__` (Impact: 1.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 4`, `state_mutation: 12`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `no-linker-script/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.762 IQR)
- **Top Global Matches:** file_cluster_8: 8.762, file_cluster_7: 9.691, file_cluster_1: 9.889
- **Magnitude:** 18.2 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 3`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ps2_keyboard.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.901 IQR)
- **Top Global Matches:** file_cluster_8: 5.901, file_cluster_7: 7.232, file_cluster_1: 7.417
- **Magnitude:** 17.68 | **LOC:** 17 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loop` (Impact: 17.4 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 2`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bios_pixel.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.358 IQR)
- **Top Global Matches:** file_cluster_8: 10.358, file_cluster_17: 11.066, file_cluster_7: 11.143
- **Magnitude:** 17.12 | **LOC:** 30 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (66.648%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `start` (Impact: 9.5 | O(2^N) | DB: 2)
  * `end` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 7`, `args: 5`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 6`
* *Architecture:* None
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `paging.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.011 IQR)
- **Top Global Matches:** file_cluster_8: 5.011, file_cluster_7: 6.629, file_cluster_1: 6.752
- **Magnitude:** 15.66 | **LOC:** 44 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.3407%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bios_clear_screen.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.193 IQR)
- **Top Global Matches:** file_cluster_8: 6.193, file_cluster_7: 7.535, file_cluster_1: 7.682
- **Magnitude:** 15.48 | **LOC:** 33 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (26.8941%), Tech Debt (99.177%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 4`
* *Risk/State:* `high_risk_execution: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `smp.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.759 IQR)
- **Top Global Matches:** file_cluster_8: 6.759, file_cluster_7: 7.948, file_cluster_1: 8.1
- **Magnitude:** 15.48 | **LOC:** 106 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (11.6987%), Tech Debt (97.023%)
**Top Internal Functions/Classes:**
  * `not_started` (Impact: 4.6 | O(2^N) | DB: 3)
    * *Intent:* /* TODO improve this spinlock. */
  * `init` (Impact: 2.5 | O(2^N))
  * `interrupt_handler` (Impact: 2.2 | O(N^1))
  * `not_pit` (Impact: 2.1 | O(N^1))
  * `message` (Impact: 1.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 12`, `args: 1`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 2`, `planned_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `concurrency: 1`
* *Defense:* `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cs.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.489 IQR)
- **Top Global Matches:** file_cluster_8: 5.489, file_cluster_7: 6.975, file_cluster_1: 7.087
- **Magnitude:** 15.42 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (25.0633%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bios_color.S` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.819 IQR)
- **Top Global Matches:** file_cluster_8: 5.819, file_cluster_7: 7.245, file_cluster_1: 7.378
- **Magnitude:** 15.38 | **LOC:** 25 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (33.5322%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `multiboot/hello-world/main.c` (C) | Magnitude: 49.16 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 24, indent_spaces: 14, structural_boundaries: 10, api: 8
- `nasm/run` (SHELL) | Magnitude: 22.76 | Delta: **0.246 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 12, branch: 5, safety: 4, indent_spaces: 4
- `run` (SHELL) | Magnitude: 22.76 | Delta: **0.246 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 12, branch: 5, safety: 4, indent_spaces: 4
- `uefi/main.c` (C) | Magnitude: 3.58 | Delta: **0.321 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 3, api: 2, import: 2, structural_boundaries: 1
- `c_hello_world/main.c` (C) | Magnitude: 15.24 | Delta: **0.332 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 9, indent_spaces: 8, api: 3, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `apm_shutdown2.S` (ASSEMBLY) | Magnitude: 6.42 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 14, dead_code: 5, func_start: 3, branch: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `multiboot/hello-world/main.c` -> **Severity: 1020.4** (Blast Radius: 10.204 * Doc Risk: 100.0%)
- `multiboot/hello-world/Makefile` -> **Severity: 1020.38** (Blast Radius: 10.204 * Doc Risk: 99.998%)
- `uefi/Makefile` -> **Severity: 1019.866** (Blast Radius: 10.204 * Doc Risk: 99.9477%)
- `multiboot/hello-world/entry.asm` -> **Severity: 1015.497** (Blast Radius: 10.204 * Doc Risk: 99.5195%)
- `no-linker-script/main.S` -> **Severity: 1013.57** (Blast Radius: 10.204 * Doc Risk: 99.3307%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
