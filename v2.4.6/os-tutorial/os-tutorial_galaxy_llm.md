# ARCHITECTURAL_BRIEF: os-tutorial
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/os-tutorial` |
| **Timestamp** | `2026-08-03T19:27:33.071260+00:00` |
| **Scan Duration** | `0.42s` |
| **Git Branch** | `master` |
| **Git Commit** | `8002382ee56f876119f77217220b8a5034e9bac1` |
| **Git Remote** | `https://github.com/cfenollosa/os-tutorial.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 129 malicious artifacts.

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
| Total Artifacts | 228 |
| Analyzed Artifacts (Scanned) | 225 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 6807 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 98.7% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.625 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 117 | 3385 | 52.0% |
| ASSEMBLY | 71 | 3150 | 31.6% |
| MARKDOWN | 25 | 0 | 11.1% |
| MAKEFILE | 12 | 272 | 5.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.277`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 162 | 72.0% |
| file_cluster_13 | 37 | 16.4% |
| file_cluster_11 | 1 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 25 | 11.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 66 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 82.9 | 17.9 | 9.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 15.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.6 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 8.3 | 2.4 | 2.3 |
| API Exposure | 0.0 | 18.6 | 7.6 | 6.0 | 0.0 |
| Concurrency Exposure | 0.0 | 51.7 | 2.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 20.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 2.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 82.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 2.4 | 100.0 | 67.0 | 83.3 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 11.8 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 0.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `15-video-ports/drivers/ports.c` (Hits: 4)
- `16-video-driver/drivers/ports.c` (Hits: 4)
- `17-video-scroll/drivers/ports.c` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **boot_sect_print.asm** (`05-bootsector-functions-strings/boot_sect_print.asm`) — 1 inbound connections
2. **boot_sect_print_hex.asm** (`05-bootsector-functions-strings/boot_sect_print_hex.asm`) — 1 inbound connections
3. **boot_sect_disk.asm** (`07-bootsector-disk/boot_sect_disk.asm`) — 1 inbound connections
4. **32bit-switch.asm** (`10-32bit-enter/32bit-switch.asm`) — 1 inbound connections
5. **README.md** (`00-environment/README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **keyboard.c** (`23-fixes/drivers/keyboard.c`) — 8 outbound dependencies
2. **isr.c** (`21-shell/cpu/isr.c`) — 7 outbound dependencies
3. **keyboard.c** (`21-shell/drivers/keyboard.c`) — 7 outbound dependencies
4. **isr.c** (`22-malloc/cpu/isr.c`) — 7 outbound dependencies
5. **keyboard.c** (`22-malloc/drivers/keyboard.c`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `print_letter` (@ `20-interrupts-timer/drivers/keyboard.c`) -> Impact: **629.4** | LOC: 187
- `print_char` (@ `21-shell/drivers/screen.c`) -> Impact: **127.5** | LOC: 45
- `print_char` (@ `22-malloc/drivers/screen.c`) -> Impact: **127.5** | LOC: 45
- `print_char` (@ `23-fixes/drivers/screen.c`) -> Impact: **127.5** | LOC: 45
- `print_char` (@ `17-video-scroll/drivers/screen.c`) -> Impact: **111.7** | LOC: 42
- `print_char` (@ `18-interrupts/drivers/screen.c`) -> Impact: **111.7** | LOC: 42
- `print_char` (@ `20-interrupts-timer/drivers/screen.c`) -> Impact: **111.7** | LOC: 42
- `print_char` (@ `16-video-driver/drivers/screen.c`) -> Impact: **34.8** | LOC: 26
- `hex_to_ascii` (@ `22-malloc/libc/string.c`) -> Impact: **24.3** | LOC: 19
- `hex_to_ascii` (@ `23-fixes/libc/string.c`) -> Impact: **24.3** | LOC: 19

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `print_letter` (@ `20-interrupts-timer/drivers/keyboard.c`) -> **O(2^N) [Recursive]**
- `loop` (@ `01-bootsector-barebones/boot_sect_simple.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ; A simple boot sector program that loops forever
- `start` (@ `05-bootsector-functions-strings/boot_sect_print.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ; keep this in mind: ; while (string[i] != 0) { print string[i]; i++ } ; the comparison for string end (null byte)
- `print_string_pm_loop` (@ `08-32bit-print/32bit-print.asm`) -> **O(2^N) [Recursive]**
- `print_string_pm_loop` (@ `14-checkpoint/boot/32bit_print.asm`) -> **O(2^N) [Recursive]**
- `start` (@ `14-checkpoint/boot/print.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ; keep this in mind: ; while (string[i] != 0) { print string[i]; i++ } ; the comparison for string end (null byte)
- `print_string_pm_loop` (@ `15-video-ports/boot/32bit_print.asm`) -> **O(2^N) [Recursive]**
- `start` (@ `15-video-ports/boot/print.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ; keep this in mind: ; while (string[i] != 0) { print string[i]; i++ } ; the comparison for string end (null byte)
- `print_string_pm_loop` (@ `16-video-driver/boot/32bit_print.asm`) -> **O(2^N) [Recursive]**
- `start` (@ `16-video-driver/boot/print.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ; keep this in mind: ; while (string[i] != 0) { print string[i]; i++ } ; the comparison for string end (null byte)

### Highest Data Gravity (Database Complexity)
- `print_char` (@ `21-shell/drivers/screen.c`) -> DB Complexity: **20**
- `print_char` (@ `22-malloc/drivers/screen.c`) -> DB Complexity: **20**
- `print_char` (@ `23-fixes/drivers/screen.c`) -> DB Complexity: **20**
- `print_char` (@ `17-video-scroll/drivers/screen.c`) -> DB Complexity: **18**
- `print_char` (@ `18-interrupts/drivers/screen.c`) -> DB Complexity: **18**
- `print_char` (@ `20-interrupts-timer/drivers/screen.c`) -> DB Complexity: **18**
- `print_char` (@ `16-video-driver/drivers/screen.c`) -> DB Complexity: **11**
- `kprint_at` (@ `16-video-driver/drivers/screen.c`) -> DB Complexity: **9**
  * *Intent:* /********************************************************** * Public Kernel API functions * **********************************************************...
- `kprint_at` (@ `17-video-scroll/drivers/screen.c`) -> DB Complexity: **9**
  * *Intent:* /********************************************************** * Public Kernel API functions * **********************************************************...
- `int_to_ascii` (@ `17-video-scroll/kernel/util.c`) -> DB Complexity: **9**
  * *Intent:* /**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `20-interrupts-timer/drivers` | 6 | 970.04 | 17.65% | 28.08% |
| `23-fixes/cpu` | 10 | 395.38 | 9.48% | 38.55% |
| `21-shell/cpu` | 10 | 389.84 | 8.9% | 38.53% |
| `22-malloc/cpu` | 10 | 389.84 | 8.9% | 38.53% |
| `21-shell/drivers` | 4 | 376.68 | 39.19% | 35.81% |
| `22-malloc/drivers` | 4 | 376.68 | 39.19% | 35.81% |
| `23-fixes/drivers` | 4 | 376.18 | 38.7% | 35.25% |
| `20-interrupts-timer/cpu` | 8 | 364.98 | 8.67% | 34.48% |
| `19-interrupts-irqs/cpu` | 6 | 336.94 | 5.63% | 29.53% |
| `18-interrupts/drivers` | 4 | 316.86 | 18.18% | 38.28% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `12-kernel-c/function.c` -> **100.0%** Exposure
- `12-kernel-c/functioncalls.c` -> **100.0%** Exposure
- `12-kernel-c/localvars.c` -> **100.0%** Exposure
- `12-kernel-c/pointers.c` -> **100.0%** Exposure
- `13-kernel-barebones/kernel.c` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `15-video-ports/kernel/kernel.c` -> **100.0%** Exposure
- `16-video-driver/drivers/screen.c` -> **100.0%** Exposure
- `17-video-scroll/drivers/screen.c` -> **100.0%** Exposure
- `17-video-scroll/kernel/kernel.c` -> **100.0%** Exposure
- `17-video-scroll/kernel/util.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `21-shell/cpu/isr.c` -> **5** Orphaned Functions | **0** Duplicates
- `22-malloc/cpu/isr.c` -> **5** Orphaned Functions | **0** Duplicates
- `23-fixes/cpu/isr.c` -> **5** Orphaned Functions | **0** Duplicates
- `19-interrupts-irqs/cpu/isr.c` -> **4** Orphaned Functions | **0** Duplicates
- `20-interrupts-timer/cpu/isr.c` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`21-shell/drivers/keyboard.c`** -> AI Confidence: **99.48%**
2. **`22-malloc/drivers/keyboard.c`** -> AI Confidence: **99.48%**
3. **`23-fixes/drivers/keyboard.c`** -> AI Confidence: **99.48%**
4. **`20-interrupts-timer/drivers/keyboard.c`** -> AI Confidence: **99.29%**
5. **`17-video-scroll/kernel/util.c`** -> AI Confidence: **99.17%**
6. **`21-shell/cpu/isr.c`** -> AI Confidence: **99.16%**
7. **`22-malloc/cpu/isr.c`** -> AI Confidence: **99.16%**
8. **`23-fixes/cpu/isr.c`** -> AI Confidence: **99.16%**
9. **`22-malloc/kernel/kernel.c`** -> AI Confidence: **99.13%**
10. **`23-fixes/kernel/kernel.c`** -> AI Confidence: **99.13%**
11. **`17-video-scroll/drivers/screen.c`** -> AI Confidence: **99.09%**
12. **`18-interrupts/drivers/screen.c`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `17-video-scroll/drivers/screen.c` -> **20.0%** Exposure
- `18-interrupts/drivers/screen.c` -> **20.0%** Exposure
- `20-interrupts-timer/drivers/screen.c` -> **20.0%** Exposure
- `21-shell/drivers/screen.c` -> **20.0%** Exposure
- `22-malloc/drivers/screen.c` -> **20.0%** Exposure
### Algorithmic DoS Exposure
- `16-video-driver/drivers/screen.c` -> **100.0%** Exposure
- `17-video-scroll/drivers/screen.c` -> **100.0%** Exposure
- `17-video-scroll/kernel/util.c` -> **100.0%** Exposure
- `18-interrupts/drivers/screen.c` -> **100.0%** Exposure
- `18-interrupts/kernel/util.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `138` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `22-malloc/libc/string.c` (C) -> Cumulative Risk: **756.76**
- **Archetype:** `file_cluster_13` (Distance: 13.662 IQR)
- **Magnitude:** 163.38 | **LOC:** 78 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9992%)
- **Heaviest Functions:** `hex_to_ascii` (Impact: 24.3), `int_to_ascii` (Impact: 13.6), `strcmp` (Impact: 8.1)

### 2. `23-fixes/libc/string.c` (C) -> Cumulative Risk: **756.76**
- **Archetype:** `file_cluster_13` (Distance: 13.662 IQR)
- **Magnitude:** 163.38 | **LOC:** 78 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9992%)
- **Heaviest Functions:** `hex_to_ascii` (Impact: 24.3), `int_to_ascii` (Impact: 13.6), `strcmp` (Impact: 8.1)

### 3. `21-shell/drivers/screen.c` (C) -> Cumulative Risk: **741.71**
- **Archetype:** `file_cluster_13` (Distance: 13.482 IQR)
- **Magnitude:** 307.28 | **LOC:** 150 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `print_char` (Impact: 127.5), `kprint_at` (Impact: 16.0), `get_cursor_offset` (Impact: 3.5)

### 4. `22-malloc/drivers/screen.c` (C) -> Cumulative Risk: **741.71**
- **Archetype:** `file_cluster_13` (Distance: 13.482 IQR)
- **Magnitude:** 307.28 | **LOC:** 150 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `print_char` (Impact: 127.5), `kprint_at` (Impact: 16.0), `get_cursor_offset` (Impact: 3.5)

### 5. `23-fixes/drivers/screen.c` (C) -> Cumulative Risk: **741.02**
- **Archetype:** `file_cluster_13` (Distance: 13.445 IQR)
- **Magnitude:** 307.3 | **LOC:** 151 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `print_char` (Impact: 127.5), `kprint_at` (Impact: 16.0), `get_cursor_offset` (Impact: 3.5)

### 6. `20-interrupts-timer/drivers/screen.c` (C) -> Cumulative Risk: **719.19**
- **Archetype:** `file_cluster_13` (Distance: 13.554 IQR)
- **Magnitude:** 276.98 | **LOC:** 139 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `print_char` (Impact: 111.7), `kprint_at` (Impact: 16.0), `get_cursor_offset` (Impact: 3.5)

### 7. `17-video-scroll/drivers/screen.c` (C) -> Cumulative Risk: **718.43**
- **Archetype:** `file_cluster_13` (Distance: 13.494 IQR)
- **Magnitude:** 277.0 | **LOC:** 140 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `print_char` (Impact: 111.7), `kprint_at` (Impact: 16.0), `get_cursor_offset` (Impact: 3.5)

### 8. `18-interrupts/drivers/screen.c` (C) -> Cumulative Risk: **718.43**
- **Archetype:** `file_cluster_13` (Distance: 13.494 IQR)
- **Magnitude:** 277.0 | **LOC:** 140 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `print_char` (Impact: 111.7), `kprint_at` (Impact: 16.0), `get_cursor_offset` (Impact: 3.5)

### 9. `16-video-driver/drivers/screen.c` (C) -> Cumulative Risk: **698.09**
- **Archetype:** `file_cluster_13` (Distance: 13.409 IQR)
- **Magnitude:** 176.84 | **LOC:** 123 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9972%)
- **Heaviest Functions:** `print_char` (Impact: 34.8), `kprint_at` (Impact: 16.0), `get_cursor_offset` (Impact: 3.5)

### 10. `22-malloc/libc/mem.c` (C) -> Cumulative Risk: **690.4**
- **Archetype:** `file_cluster_13` (Distance: 14.121 IQR)
- **Magnitude:** 58.64 | **LOC:** 34 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `kmalloc` (Impact: 6.7), `memory_copy` (Impact: 2.3), `memory_set` (Impact: 2.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `20-interrupts-timer/drivers/keyboard.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.286 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.294 IQR)
- **Top Global Matches:** file_cluster_8: 7.286, file_cluster_7: 8.219, file_cluster_1: 8.484
- **Magnitude:** 641.16 | **LOC:** 212 | **CtrlFlow:** 97.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (28.4717%), Tech Debt (14.6655%)
**Top Internal Functions/Classes:**
  * `print_letter` (Impact: 629.4 | O(2^N))
  * `keyboard_callback` (Impact: 1.6 | O(N^1) | DB: 1)
    * *Intent:* #include "keyboard.h" #include "ports.h" #include "../cpu/isr.h" #include "screen.h"
  * `init_keyboard` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` keyboard.h, ports.h, isr.h, screen.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `23-fixes/drivers/screen.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.445 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.431 IQR)
- **Top Global Matches:** file_cluster_13: 13.445, file_cluster_8: 13.645, file_cluster_7: 13.822
- **Magnitude:** 307.3 | **LOC:** 151 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (62.394%), Tech Debt (69.7059%)
**Top Internal Functions/Classes:**
  * `print_char` (Impact: 127.5 | O(N^6) | DB: 20)
  * `kprint_at` (Impact: 16.0 | O(N^2) | DB: 9)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `get_cursor_offset` (Impact: 3.5 | O(N^1) | DB: 2)
  * `clear_screen` (Impact: 3.5 | O(N^2) | DB: 6)
    * *Intent:* int offset = port_byte_in(REG_SCREEN_DATA) << 8; /* High byte: << 8 */
  * `set_cursor_offset` (Impact: 2.1 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 12`, `args: 12`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 111`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 33`, `import: 4`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` screen.h, stdint.h, ports.h, mem.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `21-shell/drivers/screen.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.482 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_13: 13.482, file_cluster_8: 13.62, file_cluster_7: 13.797
- **Magnitude:** 307.28 | **LOC:** 150 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (62.1654%), Tech Debt (70.3784%)
**Top Internal Functions/Classes:**
  * `print_char` (Impact: 127.5 | O(N^6) | DB: 20)
  * `kprint_at` (Impact: 16.0 | O(N^2) | DB: 9)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `get_cursor_offset` (Impact: 3.5 | O(N^1) | DB: 2)
  * `clear_screen` (Impact: 3.5 | O(N^2) | DB: 6)
    * *Intent:* int offset = port_byte_in(REG_SCREEN_DATA) << 8; /* High byte: << 8 */
  * `set_cursor_offset` (Impact: 2.1 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 12`, `args: 12`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 111`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 33`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` screen.h, ports.h, mem.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `22-malloc/drivers/screen.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.482 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_13: 13.482, file_cluster_8: 13.62, file_cluster_7: 13.797
- **Magnitude:** 307.28 | **LOC:** 150 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (62.1654%), Tech Debt (70.3784%)
**Top Internal Functions/Classes:**
  * `print_char` (Impact: 127.5 | O(N^6) | DB: 20)
  * `kprint_at` (Impact: 16.0 | O(N^2) | DB: 9)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `get_cursor_offset` (Impact: 3.5 | O(N^1) | DB: 2)
  * `clear_screen` (Impact: 3.5 | O(N^2) | DB: 6)
    * *Intent:* int offset = port_byte_in(REG_SCREEN_DATA) << 8; /* High byte: << 8 */
  * `set_cursor_offset` (Impact: 2.1 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 12`, `args: 12`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 111`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 33`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` screen.h, ports.h, mem.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `17-video-scroll/drivers/screen.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.494 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.107 IQR)
- **Top Global Matches:** file_cluster_13: 13.494, file_cluster_8: 13.619, file_cluster_7: 13.812
- **Magnitude:** 277.0 | **LOC:** 140 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (59.0217%), Tech Debt (53.2847%)
**Top Internal Functions/Classes:**
  * `print_char` (Impact: 111.7 | O(N^6) | DB: 18)
  * `kprint_at` (Impact: 16.0 | O(N^2) | DB: 9)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `get_cursor_offset` (Impact: 3.5 | O(N^1) | DB: 2)
  * `clear_screen` (Impact: 3.5 | O(N^2) | DB: 6)
    * *Intent:* int offset = port_byte_in(REG_SCREEN_DATA) << 8; /* High byte: << 8 */
  * `set_cursor_offset` (Impact: 2.1 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 11`, `args: 12`, `func_start: 9`
* *Risk/State:* `state_mutation: 102`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 29`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` screen.h, ports.h, util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `18-interrupts/drivers/screen.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.494 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.107 IQR)
- **Top Global Matches:** file_cluster_13: 13.494, file_cluster_8: 13.619, file_cluster_7: 13.812
- **Magnitude:** 277.0 | **LOC:** 140 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (59.0217%), Tech Debt (53.2847%)
**Top Internal Functions/Classes:**
  * `print_char` (Impact: 111.7 | O(N^6) | DB: 18)
  * `kprint_at` (Impact: 16.0 | O(N^2) | DB: 9)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `get_cursor_offset` (Impact: 3.5 | O(N^1) | DB: 2)
  * `clear_screen` (Impact: 3.5 | O(N^2) | DB: 6)
    * *Intent:* int offset = port_byte_in(REG_SCREEN_DATA) << 8; /* High byte: << 8 */
  * `set_cursor_offset` (Impact: 2.1 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 11`, `args: 12`, `func_start: 9`
* *Risk/State:* `state_mutation: 102`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 29`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` screen.h, ports.h, util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `20-interrupts-timer/drivers/screen.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.554 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.126 IQR)
- **Top Global Matches:** file_cluster_13: 13.554, file_cluster_8: 13.596, file_cluster_7: 13.788
- **Magnitude:** 276.98 | **LOC:** 139 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (58.736%), Tech Debt (53.9809%)
**Top Internal Functions/Classes:**
  * `print_char` (Impact: 111.7 | O(N^6) | DB: 18)
  * `kprint_at` (Impact: 16.0 | O(N^2) | DB: 9)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `get_cursor_offset` (Impact: 3.5 | O(N^1) | DB: 2)
  * `clear_screen` (Impact: 3.5 | O(N^2) | DB: 6)
    * *Intent:* int offset = port_byte_in(REG_SCREEN_DATA) << 8; /* High byte: << 8 */
  * `set_cursor_offset` (Impact: 2.1 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 11`, `args: 12`, `func_start: 9`
* *Risk/State:* `state_mutation: 102`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 29`, `import: 2`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` screen.h, ports.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `16-video-driver/drivers/screen.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.409 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.165 IQR)
- **Top Global Matches:** file_cluster_13: 13.409, file_cluster_8: 13.473, file_cluster_7: 13.664
- **Magnitude:** 176.84 | **LOC:** 123 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (53.2286%), Tech Debt (63.3853%)
**Top Internal Functions/Classes:**
  * `print_char` (Impact: 34.8 | O(N^2) | DB: 11)
  * `kprint_at` (Impact: 16.0 | O(N^2) | DB: 9)
    * *Intent:* /********************************************************** * Public Kernel API functions * ********...
  * `get_cursor_offset` (Impact: 3.5 | O(N^1) | DB: 2)
  * `clear_screen` (Impact: 3.5 | O(N^2) | DB: 6)
    * *Intent:* int offset = port_byte_in(REG_SCREEN_DATA) << 8; /* High byte: << 8 */
  * `set_cursor_offset` (Impact: 2.1 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 11`, `args: 12`, `func_start: 9`
* *Risk/State:* `state_mutation: 81`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 27`, `import: 2`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` screen.h, ports.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `19-interrupts-irqs/cpu/interrupt.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.636 IQR)
- **Top Global Matches:** file_cluster_8: 7.636, file_cluster_7: 8.547, file_cluster_1: 8.662
- **Magnitude:** 176.34 | **LOC:** 426 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.3886%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `irq_common_stub` (Impact: 12.3 | O(N^1))
    * *Intent:* ; Common IRQ code. Identical to ISR code except for the 'call' ; and the 'pop ebx'
  * `isr_common_stub` (Impact: 4.0 | O(N^1))
    * *Intent:* ; Defined in isr.c ; Common ISR code
  * `isr0` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 0: Divide By Zero Exception
  * `isr1` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 1: Debug Exception
  * `isr2` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 2: Non Maskable Interrupt Exception
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 116`, `args: 20`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 48`
* *Architecture:* `api: 48`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `20-interrupts-timer/cpu/interrupt.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.636 IQR)
- **Top Global Matches:** file_cluster_8: 7.636, file_cluster_7: 8.547, file_cluster_1: 8.662
- **Magnitude:** 176.34 | **LOC:** 426 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.3886%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `irq_common_stub` (Impact: 12.3 | O(N^1))
    * *Intent:* ; Common IRQ code. Identical to ISR code except for the 'call' ; and the 'pop ebx'
  * `isr_common_stub` (Impact: 4.0 | O(N^1))
    * *Intent:* ; Defined in isr.c ; Common ISR code
  * `isr0` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 0: Divide By Zero Exception
  * `isr1` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 1: Debug Exception
  * `isr2` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 2: Non Maskable Interrupt Exception
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 116`, `args: 20`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 48`
* *Architecture:* `api: 48`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `21-shell/cpu/interrupt.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.636 IQR)
- **Top Global Matches:** file_cluster_8: 7.636, file_cluster_7: 8.547, file_cluster_1: 8.662
- **Magnitude:** 176.34 | **LOC:** 426 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.3886%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `irq_common_stub` (Impact: 12.3 | O(N^1))
    * *Intent:* ; Common IRQ code. Identical to ISR code except for the 'call' ; and the 'pop ebx'
  * `isr_common_stub` (Impact: 4.0 | O(N^1))
    * *Intent:* ; Defined in isr.c ; Common ISR code
  * `isr0` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 0: Divide By Zero Exception
  * `isr1` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 1: Debug Exception
  * `isr2` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 2: Non Maskable Interrupt Exception
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 116`, `args: 20`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 48`
* *Architecture:* `api: 48`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `22-malloc/cpu/interrupt.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.636 IQR)
- **Top Global Matches:** file_cluster_8: 7.636, file_cluster_7: 8.547, file_cluster_1: 8.662
- **Magnitude:** 176.34 | **LOC:** 426 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.3886%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `irq_common_stub` (Impact: 12.3 | O(N^1))
    * *Intent:* ; Common IRQ code. Identical to ISR code except for the 'call' ; and the 'pop ebx'
  * `isr_common_stub` (Impact: 4.0 | O(N^1))
    * *Intent:* ; Defined in isr.c ; Common ISR code
  * `isr0` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 0: Divide By Zero Exception
  * `isr1` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 1: Debug Exception
  * `isr2` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 2: Non Maskable Interrupt Exception
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 116`, `args: 20`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 48`
* *Architecture:* `api: 48`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `23-fixes/cpu/interrupt.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.631 IQR)
- **Top Global Matches:** file_cluster_8: 7.631, file_cluster_7: 8.578, file_cluster_1: 8.64
- **Magnitude:** 175.06 | **LOC:** 381 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.423%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `irq_common_stub` (Impact: 12.4 | O(N^1))
    * *Intent:* ; Common IRQ code. Identical to ISR code except for the 'call' ; and the 'pop ebx'
  * `isr_common_stub` (Impact: 4.1 | O(N^1))
    * *Intent:* ; Defined in isr.c ; Common ISR code
  * `isr0` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 0: Divide By Zero Exception
  * `isr1` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 1: Debug Exception
  * `isr2` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 2: Non Maskable Interrupt Exception
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 120`, `args: 20`, `func_start: 50`
* *Risk/State:* None
* *Architecture:* `api: 48`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `22-malloc/libc/string.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.662 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.56 IQR)
- **Top Global Matches:** file_cluster_13: 13.662, file_cluster_8: 13.791, file_cluster_7: 14.055
- **Magnitude:** 163.38 | **LOC:** 78 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (66.0885%), Tech Debt (99.4101%)
**Top Internal Functions/Classes:**
  * `hex_to_ascii` (Impact: 24.3 | O(N^2) | DB: 6)
  * `int_to_ascii` (Impact: 13.6 | O(N^2) | DB: 9)
    * *Intent:* #include "string.h" #include "../cpu/type.h" /**
  * `strcmp` (Impact: 8.1 | O(N^2) | DB: 2)
  * `reverse` (Impact: 5.6 | O(N^2) | DB: 7)
  * `strlen` (Impact: 3.7 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 8`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 83`, `orphaned_logic: 4`
* *Architecture:* `api: 20`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` type.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `23-fixes/libc/string.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.662 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.56 IQR)
- **Top Global Matches:** file_cluster_13: 13.662, file_cluster_8: 13.791, file_cluster_7: 14.055
- **Magnitude:** 163.38 | **LOC:** 78 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (66.0885%), Tech Debt (99.4101%)
**Top Internal Functions/Classes:**
  * `hex_to_ascii` (Impact: 24.3 | O(N^2) | DB: 6)
  * `int_to_ascii` (Impact: 13.6 | O(N^2) | DB: 9)
    * *Intent:* #include "string.h" #include <stdint.h> /**
  * `strcmp` (Impact: 8.1 | O(N^2) | DB: 2)
  * `reverse` (Impact: 5.6 | O(N^2) | DB: 7)
  * `strlen` (Impact: 3.7 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 8`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 83`, `orphaned_logic: 4`
* *Architecture:* `api: 20`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdint.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `20-interrupts-timer/kernel/util.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.577 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.712 IQR)
- **Top Global Matches:** file_cluster_13: 14.577, file_cluster_8: 14.727, file_cluster_11: 14.929
- **Magnitude:** 116.1 | **LOC:** 48 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (57.4069%), Tech Debt (99.9447%)
**Top Internal Functions/Classes:**
  * `int_to_ascii` (Impact: 13.6 | O(N^2) | DB: 9)
    * *Intent:* /**
  * `reverse` (Impact: 5.6 | O(N^2) | DB: 7)
  * `memory_copy` (Impact: 4.3 | O(N^1) | DB: 3)
    * *Intent:* #include "util.h"
  * `strlen` (Impact: 3.7 | O(N^1) | DB: 2)
  * `memory_set` (Impact: 2.2 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 5`, `args: 4`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 75`, `orphaned_logic: 3`
* *Architecture:* `api: 11`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `21-shell/libc/string.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.896 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.729 IQR)
- **Top Global Matches:** file_cluster_13: 13.896, file_cluster_8: 13.962, file_cluster_7: 14.21
- **Magnitude:** 114.72 | **LOC:** 57 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (57.5675%), Tech Debt (99.9792%)
**Top Internal Functions/Classes:**
  * `int_to_ascii` (Impact: 13.6 | O(N^2) | DB: 9)
    * *Intent:* #include "string.h" /**
  * `strcmp` (Impact: 8.1 | O(N^2) | DB: 2)
  * `reverse` (Impact: 5.6 | O(N^2) | DB: 7)
  * `strlen` (Impact: 3.7 | O(N^1) | DB: 2)
  * `append` (Impact: 2.0 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 7`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 65`, `orphaned_logic: 4`
* *Architecture:* `api: 14`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `18-interrupts/cpu/interrupt.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.31 IQR)
- **Top Global Matches:** file_cluster_8: 7.31, file_cluster_7: 8.291, file_cluster_1: 8.396
- **Magnitude:** 112.62 | **LOC:** 290 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.4308%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isr_common_stub` (Impact: 6.1 | O(N^1))
    * *Intent:* ; Defined in isr.c ; Common ISR code
  * `isr0` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 0: Divide By Zero Exception
  * `isr1` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 1: Debug Exception
  * `isr2` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 2: Non Maskable Interrupt Exception
  * `isr3` (Impact: 2.2 | O(N^1))
    * *Intent:* ; 3: Int 3 Exception
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 71`, `args: 10`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 32`
* *Architecture:* `api: 32`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `21-shell/cpu/isr.h` (C | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.006 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.034 IQR)
- **Top Global Matches:** file_cluster_8: 7.006, file_cluster_7: 8.005, file_cluster_1: 8.279
- **Magnitude:** 74.58 | **LOC:** 90 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 56`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 58`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `22-malloc/cpu/isr.h` (C | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.006 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.034 IQR)
- **Top Global Matches:** file_cluster_8: 7.006, file_cluster_7: 8.005, file_cluster_1: 8.279
- **Magnitude:** 74.58 | **LOC:** 90 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 56`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 58`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` type.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `23-fixes/cpu/isr.h` (C | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.072 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.181 IQR)
- **Top Global Matches:** file_cluster_8: 7.072, file_cluster_7: 8.063, file_cluster_1: 8.335
- **Magnitude:** 74.58 | **LOC:** 96 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 56`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 58`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdint.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `18-interrupts/kernel/util.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.889 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.702 IQR)
- **Top Global Matches:** file_cluster_13: 14.889, file_cluster_11: 14.924, file_cluster_6: 15.11
- **Magnitude:** 74.52 | **LOC:** 31 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (48.8749%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `int_to_ascii` (Impact: 13.6 | O(N^2) | DB: 9)
    * *Intent:* /**
  * `memory_copy` (Impact: 4.3 | O(N^1) | DB: 3)
    * *Intent:* #include "util.h"
  * `memory_set` (Impact: 2.2 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 3`, `args: 2`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 48`, `planned_debt: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `19-interrupts-irqs/kernel/util.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.889 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.702 IQR)
- **Top Global Matches:** file_cluster_13: 14.889, file_cluster_11: 14.924, file_cluster_6: 15.11
- **Magnitude:** 74.52 | **LOC:** 31 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (48.8749%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `int_to_ascii` (Impact: 13.6 | O(N^2) | DB: 9)
    * *Intent:* /**
  * `memory_copy` (Impact: 4.3 | O(N^1) | DB: 3)
    * *Intent:* #include "util.h"
  * `memory_set` (Impact: 2.2 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 3`, `args: 2`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 48`, `planned_debt: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `19-interrupts-irqs/cpu/isr.h` (C | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.011 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.036 IQR)
- **Top Global Matches:** file_cluster_8: 7.011, file_cluster_7: 8.01, file_cluster_1: 8.284
- **Magnitude:** 73.56 | **LOC:** 89 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 55`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 57`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `20-interrupts-timer/cpu/isr.h` (C | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.011 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.036 IQR)
- **Top Global Matches:** file_cluster_8: 7.011, file_cluster_7: 8.01, file_cluster_1: 8.284
- **Magnitude:** 73.56 | **LOC:** 89 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 55`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 57`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `17-video-scroll/kernel/util.c` (C) | Magnitude: 58.22 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 36, indent_spaces: 12, branch: 5, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `21-shell/cpu/idt.c` (C) | Magnitude: 12.46 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 7, indent_spaces: 7, listeners: 3, structural_boundaries: 2
- `22-malloc/cpu/idt.c` (C) | Magnitude: 12.46 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 7, indent_spaces: 7, listeners: 3, structural_boundaries: 2
- `18-interrupts/kernel/util.c` (C) | Magnitude: 74.52 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 48, indent_spaces: 14, branch: 6, api: 6
- `19-interrupts-irqs/kernel/util.c` (C) | Magnitude: 74.52 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 48, indent_spaces: 14, branch: 6, api: 6
- `23-fixes/libc/mem.h` (C) | Magnitude: 17.16 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 5, api: 3, structural_boundaries: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `18-interrupts/kernel/kernel.c` (C) | Magnitude: 2.28 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 4, structural_boundaries: 1, func_start: 1, api: 1
- `19-interrupts-irqs/kernel/kernel.c` (C) | Magnitude: 2.28 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 4, structural_boundaries: 1, func_start: 1, api: 1
- `23-fixes/cpu/ports.c` (C) | Magnitude: 17.14 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 10, indent_spaces: 8, structural_boundaries: 4, func_start: 4
- `20-interrupts-timer/kernel/kernel.c` (C) | Magnitude: 3.58 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 4, import: 3, api: 2, structural_boundaries: 1
- `21-shell/Makefile` (MAKEFILE) | Magnitude: 6.78 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 11, structural_boundaries: 6, func_start: 6, io: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `10-32bit-enter/32bit-switch.asm` -> **Severity: 0.251** (Embedded: 0.0045 * Error Risk: 56.3158%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `10-32bit-enter/32bit-switch.asm` -> **Severity: 547.959** (Blast Radius: 8.13 * Doc Risk: 67.3996%)
- `17-video-scroll/drivers/screen.c` -> **Severity: 439.5** (Blast Radius: 4.395 * Doc Risk: 99.9999%)
- `18-interrupts/cpu/idt.h` -> **Severity: 439.5** (Blast Radius: 4.395 * Doc Risk: 100.0%)
- `18-interrupts/cpu/isr.h` -> **Severity: 439.5** (Blast Radius: 4.395 * Doc Risk: 100.0%)
- `18-interrupts/drivers/screen.c` -> **Severity: 439.5** (Blast Radius: 4.395 * Doc Risk: 99.9999%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
