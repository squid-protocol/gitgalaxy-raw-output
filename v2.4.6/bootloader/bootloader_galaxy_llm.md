# ARCHITECTURAL_BRIEF: bootloader
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/bootloader` |
| **Timestamp** | `2026-08-03T19:43:33.393368+00:00` |
| **Scan Duration** | `0.4s` |
| **Git Branch** | `main` |
| **Git Commit** | `f58194f0dd2dbd6bd1e44d4a8cf4cafde7b3e78f` |
| **Git Remote** | `https://github.com/rust-osdev/bootloader.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 98 malicious artifacts.

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
| Total Artifacts | 175 |
| Analyzed Artifacts (Scanned) | 112 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 63 |
| Total LOC | 6542 |
| Volatility Index | 0.018 |
| % Scanned of codebase = | 64.0% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3457 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -1.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.75 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 98 | 6420 | 87.5% |
| MARKDOWN | 6 | 0 | 5.4% |
| JSON | 4 | 85 | 3.6% |
| PLAINTEXT | 3 | 0 | 2.7% |
| ASSEMBLY | 1 | 37 | 0.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.155`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 36 | 32.1% |
| file_cluster_8 | 35 | 31.2% |
| file_cluster_0 | 25 | 22.3% |
| file_cluster_4 | 3 | 2.7% |
| file_cluster_16 | 2 | 1.8% |
| file_cluster_17 | 1 | 0.9% |
| file_cluster_9 | 1 | 0.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 8.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 63*

**Composition by Extension & Reason:**
- `.toml`: 26x Unsupported Format (.toml), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.toml')
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ld`: 4x Excluded (Unsupported Extension: '.ld')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 3x Excluded (Unsupported Extension: '.lock')
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.0 | 70.1 | 12.9 | 9.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 94.8 | 45.4 | 53.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 23.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.7 | 0.0 | 0.0 |
| API Exposure | 0.0 | 7.8 | 2.2 | 2.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 6.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 97.0 | 2.8 | 0.0 | 0.0 |
| Specification Exposure | 33.3 | 100.0 | 96.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.1 | 1.8 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 12.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 32.8 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 37.8 | 18.5 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 4.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `bios/stage-2/src/protected_mode.rs` (Hits: 17)
- `bios/stage-2/src/vesa.rs` (Hits: 6)
- `bios/stage-3/src/main.rs` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **serial.rs** (`common/src/serial.rs`) — 7 inbound connections
2. **config.rs** (`api/src/config.rs`) — 1 inbound connections
3. **entropy.rs** (`common/src/entropy.rs`) — 1 inbound connections
4. **Changelog.md** (`Changelog.md`) — 0 inbound connections
5. **README.md** (`README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.rs** (`uefi/src/main.rs`) — 47 outbound dependencies
2. **lib.rs** (`common/src/lib.rs`) — 35 outbound dependencies
3. **main.rs** (`bios/stage-4/src/main.rs`) — 31 outbound dependencies
4. **load_kernel.rs** (`common/src/load_kernel.rs`) — 30 outbound dependencies
5. **level_4_entries.rs** (`common/src/level_4_entries.rs`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `construct_memory_map` (@ `common/src/legacy_memory_region.rs`) -> Impact: **342.1** | LOC: 394
- `new` (@ `common/src/load_kernel.rs`) -> Impact: **140.6** | LOC: 68
- `create_boot_info` (@ `common/src/lib.rs`) -> Impact: **138.7** | LOC: 118
- `get_best_mode` (@ `bios/stage-2/src/vesa.rs`) -> Impact: **127.5** | LOC: 46
- `create_disk_image` (@ `src/disk_image.rs`) -> Impact: **112.3** | LOC: 99
  * *Intent:* /// Creates a bootable disk image from the given bootloader executable.
- `new` (@ `common/src/level_4_entries.rs`) -> Impact: **110.2** | LOC: 87
  * *Intent:* /// Initializes a new instance. /// /// Marks the statically configured virtual address ranges from the config as used.
- `load_segments` (@ `common/src/load_kernel.rs`) -> Impact: **107.2** | LOC: 45
- `_start` (@ `bios/stage-4/src/main.rs`) -> Impact: **98.7** | LOC: 229
- `init_logger` (@ `uefi/src/main.rs`) -> Impact: **98.0** | LOC: 81
- `create_mbr_disk` (@ `src/mbr.rs`) -> Impact: **96.4** | LOC: 90

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `new` (@ `common/src/load_kernel.rs`) -> **O(2^N) [Recursive]**
- `construct_memory_map` (@ `common/src/legacy_memory_region.rs`) -> **O(2^N) [Recursive]**
- `init_logger` (@ `uefi/src/main.rs`) -> **O(2^N) [Recursive]**
- `serialize` (@ `api/src/config.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Serializes the configuration to a byte array. /// /// This is used by the [`crate::entry_point`] macro to store the configuration in a /// dedicat...
- `new` (@ `common/src/level_4_entries.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Initializes a new instance. /// /// Marks the statically configured virtual address ranges from the config as used.
- `write_str` (@ `common/src/serial.rs`) -> **O(2^N) [Recursive]**
- `len` (@ `src/file_data_source.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Get the length of the inner data source
- `fmt` (@ `src/file_data_source.rs`) -> **O(2^N) [Recursive]**
- `random` (@ `api/src/config.rs`) -> **O(2^N) [Recursive]**
- `new_default` (@ `api/src/config.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Creates a new default configuration with the following values: /// /// - `kernel_stack_size`: 80kiB /// - `mappings`: See [`Mappings::new_default(...

### Highest Data Gravity (Database Complexity)
- `construct_memory_map` (@ `common/src/legacy_memory_region.rs`) -> DB Complexity: **20**
- `run_qemu` (@ `tests/runner/src/lib.rs`) -> DB Complexity: **20**
- `create_mbr_disk` (@ `src/mbr.rs`) -> DB Complexity: **17**
- `create_disk_image` (@ `src/disk_image.rs`) -> DB Complexity: **16**
  * *Intent:* /// Creates a bootable disk image from the given bootloader executable.
- `start` (@ `bios/stage-2/src/main.rs`) -> DB Complexity: **15**
- `_start` (@ `bios/stage-4/src/main.rs`) -> DB Complexity: **15**
- `main_inner` (@ `uefi/src/main.rs`) -> DB Complexity: **14**
- `create_boot_info` (@ `common/src/lib.rs`) -> DB Complexity: **11**
- `create_gpt_disk` (@ `src/gpt.rs`) -> DB Complexity: **10**
- `load_file_from_disk` (@ `uefi/src/main.rs`) -> DB Complexity: **10**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `common/src` | 9 | 1570.76 | 13.23% | 26.6% |
| `bios/stage-2/src` | 8 | 886.8 | 20.16% | 56.91% |
| `src` | 6 | 801.02 | 37.54% | 45.46% |
| `uefi/src` | 2 | 476.22 | 19.85% | 54.45% |
| `api/src` | 3 | 374.88 | 7.57% | 66.66% |
| `bios/stage-3/src` | 4 | 216.48 | 32.63% | 55.22% |
| `bios/stage-4/src` | 2 | 149.44 | 8.23% | 69.55% |
| `bios/boot_sector/src` | 5 | 131.9 | 10.83% | 72.06% |
| `tests/runner/src` | 1 | 120.12 | 48.48% | 0.0% |
| `tests/test_kernels/ramdisk/src/bin` | 4 | 109.82 | 10.29% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bios/boot_sector/src/boot.s` -> **99.9992%** Exposure
- `api/src/info.rs` -> **99.9945%** Exposure
- `api/src/config.rs` -> **99.9901%** Exposure
- `common/config/src/lib.rs` -> **99.9859%** Exposure
- `bios/stage-2/src/disk.rs` -> **99.9708%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bios/common/src/racy_cell.rs` -> **100.0%** Exposure
- `common/src/entropy.rs` -> **100.0%** Exposure
- `common/src/framebuffer.rs` -> **100.0%** Exposure
- `common/src/gdt.rs` -> **100.0%** Exposure
- `common/src/logger.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `api/src/info.rs` -> **10** Orphaned Functions | **6** Duplicates
- `api/src/config.rs` -> **0** Orphaned Functions | **7** Duplicates
- `src/lib.rs` -> **7** Orphaned Functions | **0** Duplicates
- `bios/stage-2/src/fat.rs` -> **2** Orphaned Functions | **3** Duplicates
- `bios/stage-2/src/disk.rs` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/file_data_source.rs`** -> AI Confidence: **99.24%**
2. **`src/disk_image.rs`** -> AI Confidence: **99.23%**
3. **`bios/stage-3/src/screen.rs`** -> AI Confidence: **99.18%**
4. **`tests/test_kernels/lower_memory_free/src/bin/lower_memory_free.rs`** -> AI Confidence: **99.18%**
5. **`tests/test_kernels/ramdisk/src/bin/ramdisk.rs`** -> AI Confidence: **99.18%**
6. **`uefi/src/main.rs`** -> AI Confidence: **99.18%**
7. **`common/src/framebuffer.rs`** -> AI Confidence: **99.16%**
8. **`common/src/load_kernel.rs`** -> AI Confidence: **99.16%**
9. **`src/lib.rs`** -> AI Confidence: **99.16%**
10. **`examples/basic/src/main.rs`** -> AI Confidence: **99.15%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `api/src/info.rs` -> **20.0%** Exposure
- `bios/stage-2/src/disk.rs` -> **20.0%** Exposure
- `bios/stage-2/src/fat.rs` -> **20.0%** Exposure
- `bios/stage-2/src/vesa.rs` -> **20.0%** Exposure
- `bios/stage-3/src/paging.rs` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `tests/runner/src/lib.rs` -> **100.0%** Exposure
### Raw Memory Manipulation
- `bios/stage-2/src/main.rs` -> **0.0001%** Exposure
### Algorithmic DoS Exposure
- `api/src/info.rs` -> **100.0%** Exposure
- `bios/stage-2/src/disk.rs` -> **100.0%** Exposure
- `bios/stage-2/src/fat.rs` -> **100.0%** Exposure
- `bios/stage-2/src/main.rs` -> **100.0%** Exposure
- `bios/stage-2/src/vesa.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `598` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `bios/stage-3/src/screen.rs` (RUST) -> Cumulative Risk: **856.71**
- **Archetype:** `file_cluster_4` (Distance: 11.764 IQR)
- **Magnitude:** 135.06 | **LOC:** 129 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.5403%)
- **Heaviest Functions:** `write_char` (Impact: 21.6), `write_pixel` (Impact: 17.7), `write_rendered_char` (Impact: 13.4)

### 2. `bios/stage-2/src/disk.rs` (RUST) -> Cumulative Risk: **844.93**
- **Archetype:** `file_cluster_0` (Distance: 11.774 IQR)
- **Magnitude:** 106.98 | **LOC:** 118 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `read_exact_into` (Impact: 21.7), `slice_mut` (Impact: 12.6), `read_exact_at` (Impact: 9.2)

### 3. `common/src/framebuffer.rs` (RUST) -> Cumulative Risk: **729.59**
- **Archetype:** `file_cluster_13` (Distance: 11.763 IQR)
- **Magnitude:** 145.12 | **LOC:** 155 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `write_pixel` (Impact: 28.9), `write_char` (Impact: 21.7), `write_rendered_char` (Impact: 13.4)

### 4. `src/mbr.rs` (RUST) -> Cumulative Risk: **689.69**
- **Archetype:** `file_cluster_8` (Distance: 11.01 IQR)
- **Magnitude:** 130.06 | **LOC:** 101 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9995%), Documentation (84.9971%)
- **Heaviest Functions:** `create_mbr_disk` (Impact: 96.4)

### 5. `src/lib.rs` (RUST) -> Cumulative Risk: **683.04**
- **Archetype:** `file_cluster_0` (Distance: 11.56 IQR)
- **Magnitude:** 182.62 | **LOC:** 236 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (84.37%)
- **Heaviest Functions:** `create_fat_filesystem_image` (Impact: 38.0), `create_uefi_tftp_folder` (Impact: 32.8), `create_bios_image` (Impact: 17.0)

### 6. `bios/stage-2/src/main.rs` (RUST) -> Cumulative Risk: **680.08**
- **Archetype:** `file_cluster_0` (Distance: 10.904 IQR)
- **Magnitude:** 91.3 | **LOC:** 271 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Algorithmic Dos (100.0%), State Flux (99.1837%)
- **Heaviest Functions:** `start` (Impact: 44.9), `fail` (Impact: 4.3), `load_file` (Impact: 3.1)

### 7. `uefi/src/main.rs` (RUST) -> Cumulative Risk: **660.41**
- **Archetype:** `file_cluster_17` (Distance: 12.852 IQR)
- **Magnitude:** 451.3 | **LOC:** 567 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.6752%)
- **Heaviest Functions:** `init_logger` (Impact: 98.0), `main_inner` (Impact: 66.2), `create_page_tables` (Impact: 37.4)

### 8. `api/src/info.rs` (RUST) -> Cumulative Risk: **657.2**
- **Archetype:** `file_cluster_0` (Distance: 15.129 IQR)
- **Magnitude:** 171.76 | **LOC:** 382 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9945%)
- **Heaviest Functions:** `as_mut` (Impact: 8.3), `from` (Impact: 8.3), `from` (Impact: 8.3)

### 9. `src/fat.rs` (RUST) -> Cumulative Risk: **623.29**
- **Archetype:** `file_cluster_13` (Distance: 11.065 IQR)
- **Magnitude:** 131.28 | **LOC:** 94 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.8459%), State Flux (99.2589%)
- **Heaviest Functions:** `add_files_to_image` (Impact: 80.0), `create_fat_filesystem` (Impact: 33.8)

### 10. `src/file_data_source.rs` (RUST) -> Cumulative Risk: **622.7**
- **Archetype:** `file_cluster_13` (Distance: 12.736 IQR)
- **Magnitude:** 127.86 | **LOC:** 67 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9992%), Documentation (95.8346%)
- **Heaviest Functions:** `copy_to` (Impact: 49.6), `len` (Impact: 35.1), `fmt` (Impact: 18.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `uefi/src/main.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.852 IQR)
- **Top Global Matches:** file_cluster_17: 12.852, file_cluster_0: 12.897, file_cluster_13: 12.943
- **Magnitude:** 451.3 | **LOC:** 567 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (33.2079%), Tech Debt (9.1999%)
**Top Internal Functions/Classes:**
  * `init_logger` (Impact: 98.0 | O(2^N) | DB: 2)
  * `main_inner` (Impact: 66.2 | O(N^4) | DB: 14)
  * `create_page_tables` (Impact: 37.4 | O(N^4) | DB: 6)
    * *Intent:* /// Creates page table abstraction types for both the bootloader and kernel page tables.
  * `panic` (Impact: 25.0 | O(2^N) | DB: 1)
  * `locate_and_open_protocol` (Impact: 21.6 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 154`, `args: 24`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 101`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 6`, `import: 10`
* *Defense:* `safety: 63`, `doc: 2`, `test: 3`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SystemTable, core::arch::asm, bootloader_x86_64_common::
    Kernel, FileMode, pxe::BaseCode, ScopedProtocol, uefi::table::cfg, PixelFormat...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common/src/legacy_memory_region.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.409 IQR)
- **Top Global Matches:** file_cluster_8: 11.409, file_cluster_16: 11.624, file_cluster_0: 11.715
- **Magnitude:** 416.82 | **LOC:** 596 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (7.3877%), Tech Debt (58.4411%)
**Top Internal Functions/Classes:**
  * `construct_memory_map` (Impact: 342.1 | O(2^N) | DB: 20)
  * `len` (Impact: 5.3 | O(2^N))
    * *Intent:* /// Creates a new frame allocator based on the given legacy memory regions. /// /// Skips the frame ...
  * `max_phys_addr` (Impact: 4.1 | O(N^3))
  * `new_from_len` (Impact: 3.8 | O(N^3))
    * *Intent:* /// Creates a new slice
  * `memory_map_max_region_count` (Impact: 2.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 75`, `args: 25`, `func_start: 21`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 32`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* `safety: 41`, `doc: 37`, `test: 25`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*, align_down, PhysFrame, bootloader_api::info::MemoryRegion, structures::paging::FrameAllocator, mem::MaybeUninit, align_up, Size4KiB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bios/stage-2/src/fat.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.94%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.929 IQR)
- **Top Global Matches:** file_cluster_8: 10.929, file_cluster_16: 11.002, file_cluster_0: 11.144
- **Magnitude:** 377.58 | **LOC:** 506 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (9.9112%), Tech Debt (40.5117%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 49.2 | O(N^6) | DB: 1)
  * `classify_fat_entry` (Impact: 45.8 | O(N^4))
  * `find_file_in_root_dir` (Impact: 42.5 | O(N^5) | DB: 3)
  * `fat_entry_of_nth_cluster` (Impact: 23.9 | O(N^4) | DB: 1)
  * `fat_type` (Impact: 17.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 96`, `args: 29`, `func_start: 25`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 25`, `duplicate_logic: 3`, `orphaned_logic: 2`
* *Architecture:* `api: 22`, `import: 2`
* *Defense:* `safety: 41`, `test: 3`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Seek, Read, SeekFrom, crate::disk::AlignedBuffer, core::char::DecodeUtf16Error
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common/src/load_kernel.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.96 IQR)
- **Top Global Matches:** file_cluster_16: 11.96, file_cluster_8: 12.075, file_cluster_13: 12.091
- **Magnitude:** 350.18 | **LOC:** 827 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (8.1177%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 140.6 | O(2^N) | DB: 3)
  * `load_segments` (Impact: 107.2 | O(N^6) | DB: 2)
  * `handle_load_segment` (Impact: 62.1 | O(N^6) | DB: 6)
  * `entry_point` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 66`, `args: 18`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 21`
* *Architecture:* `api: 9`, `import: 6`
* *Defense:* `safety: 22`, `doc: 49`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` header, PageTableFlags, mapper::MappedFrame, PageSize, program::self, align_up, ops::Add, bootloader_api::config::Mapping...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.687 IQR)
- **Top Global Matches:** file_cluster_16: 11.687, file_cluster_13: 11.782, file_cluster_8: 11.819
- **Magnitude:** 344.46 | **LOC:** 700 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (6.4611%), Tech Debt (14.5094%)
**Top Internal Functions/Classes:**
  * `create_boot_info` (Impact: 138.7 | O(N^6) | DB: 11)
  * `set_up_mappings` (Impact: 35.8 | O(N^3) | DB: 6)
    * *Intent:* /// Sets up mappings for a kernel stack and the framebuffer. /// /// The `kernel_bytes` slice should...
  * `init_logger` (Impact: 16.8 | O(N^3) | DB: 1)
    * *Intent:* /// Initialize a text-based logger using the given pixel-based framebuffer as output.
  * `mapping_addr` (Impact: 15.5 | O(N^2) | DB: 1)
  * `mapping_addr_page_aligned` (Impact: 11.6 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 101`, `args: 21`, `func_start: 12`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 41`, `orphaned_logic: 3`
* *Architecture:* `io: 4`, `api: 44`, `import: 10`
* *Defense:* `safety: 27`, `doc: 62`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PageTableFlags, Size2MiB, PageSize, info::FrameBuffer, usize_conversions::FromUsize, mem::MaybeUninit, core::alloc::Layout, bootloader_boot_config::BootConfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/config.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.9%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.08 IQR)
- **Top Global Matches:** file_cluster_8: 12.08, file_cluster_0: 12.196, file_cluster_7: 12.28
- **Magnitude:** 192.92 | **LOC:** 614 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.5135%), Tech Debt (99.9901%)
**Top Internal Functions/Classes:**
  * `serialize` (Impact: 65.3 | O(2^N))
    * *Intent:* /// Serializes the configuration to a byte array. /// /// This is used by the [`crate::entry_point`]...
  * `random` (Impact: 35.4 | O(2^N))
  * `config_serde` (Impact: 7.4 | O(N^3))
  * `new_default` (Impact: 7.3 | O(2^N))
    * *Intent:* /// Creates a new default configuration with the following values: /// /// - `kernel_stack_size`: 80...
  * `random` (Impact: 5.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 49`, `args: 14`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `planned_debt: 5`, `duplicate_logic: 7`
* *Architecture:* `api: 27`, `import: 2`
* *Defense:* `safety: 57`, `doc: 118`, `test: 7`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009009
  * `Imports (Out-Degree: 0):` super::*, crate::concat::*, version_info
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.56 IQR)
- **Top Global Matches:** file_cluster_0: 11.56, file_cluster_13: 11.642, file_cluster_8: 11.805
- **Magnitude:** 182.62 | **LOC:** 236 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (10.1667%), Tech Debt (77.9618%)
**Top Internal Functions/Classes:**
  * `create_fat_filesystem_image` (Impact: 38.0 | O(N^5) | DB: 1)
  * `create_uefi_tftp_folder` (Impact: 32.8 | O(N^3) | DB: 2)
  * `create_bios_image` (Impact: 17.0 | O(N^2) | DB: 1)
  * `create_uefi_image` (Impact: 16.3 | O(N^2))
  * `create_uefi_fat_partition` (Impact: 8.4 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 47`, `args: 15`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`, `orphaned_logic: 7`
* *Architecture:* `api: 15`, `import: 8`
* *Defense:* `safety: 11`, `doc: 21`, `immutability_locks: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::fs, uefi::UefiBoot, ops::Deref, anyhow::Context, crate::file_data_source::FileDataSource, tempfile::NamedTempFile, collections::BTreeMap, bios::BiosBoot...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bios/stage-2/src/vesa.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.957 IQR)
- **Top Global Matches:** file_cluster_8: 10.957, file_cluster_16: 11.097, file_cluster_0: 11.107
- **Magnitude:** 181.54 | **LOC:** 237 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (12.8624%), Tech Debt (69.0378%)
**Top Internal Functions/Classes:**
  * `get_best_mode` (Impact: 127.5 | O(N^6) | DB: 2)
  * `get_mode` (Impact: 11.0 | O(N^3))
  * `query` (Impact: 6.2 | O(N^3) | DB: 1)
  * `query` (Impact: 5.9 | O(N^3) | DB: 4)
  * `enable` (Impact: 2.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 49`, `args: 17`, `func_start: 5`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 6`, `api: 11`, `import: 3`
* *Defense:* `safety: 28`, `doc: 5`, `test: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bootloader_x86_64_bios_common::PixelFormat, disk::AlignedBuffer, crate::AlignedArrayBuffer, core::arch::asm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/info.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.129 IQR)
- **Top Global Matches:** file_cluster_0: 15.129, file_cluster_16: 15.51, file_cluster_13: 15.619
- **Magnitude:** 171.76 | **LOC:** 382 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (16.4761%), Tech Debt (99.9945%)
**Top Internal Functions/Classes:**
  * `as_mut` (Impact: 8.3 | O(N^3) | DB: 2)
  * `from` (Impact: 8.3 | O(N^3))
  * `from` (Impact: 8.3 | O(N^3))
  * `as_ref` (Impact: 7.2 | O(N^3))
  * `info` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 39`, `args: 20`, `func_start: 20`, `class_start: 9`
* *Risk/State:* `state_mutation: 25`, `dead_code: 4`, `duplicate_logic: 6`, `orphaned_logic: 10`
* *Architecture:* `api: 51`, `concurrency: 7`, `import: 2`
* *Defense:* `safety: 37`, `doc: 146`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` slice, bootloader_api::BootInfo, crate::config::ApiVersion, core::ops
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/disk_image.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.504 IQR)
- **Top Global Matches:** file_cluster_8: 10.504, file_cluster_13: 10.532, file_cluster_0: 10.579
- **Magnitude:** 166.02 | **LOC:** 184 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (11.5855%), Tech Debt (49.5861%)
**Top Internal Functions/Classes:**
  * `create_disk_image` (Impact: 112.3 | O(N^3) | DB: 16)
    * *Intent:* /// Creates a bootable disk image from the given bootloader executable.
  * `pad_to_nearest_block_size` (Impact: 21.4 | O(N^3) | DB: 3)
  * `from` (Impact: 8.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 37`, `args: 10`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 4`, `api: 2`, `import: 5`
* *Defense:* `safety: 5`, `doc: 10`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Write, Seek, anyhow::Context, thiserror::Error, std::fs::OpenOptions, path::Path, process::Command, io::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common/src/framebuffer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.763 IQR)
- **Top Global Matches:** file_cluster_13: 11.763, file_cluster_8: 11.871, file_cluster_4: 11.906
- **Magnitude:** 145.12 | **LOC:** 155 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (27.6065%), Tech Debt (16.2747%)
**Top Internal Functions/Classes:**
  * `write_pixel` (Impact: 28.9 | O(N^4) | DB: 1)
  * `write_char` (Impact: 21.7 | O(N^5) | DB: 1)
    * *Intent:* /// Writes a single char to the framebuffer. Takes care of special control characters, such as /// n...
  * `write_rendered_char` (Impact: 13.4 | O(N^4) | DB: 1)
    * *Intent:* /// Prints a rendered char into the framebuffer. /// Updates `self.x_pos`.
  * `get_char_raster` (Impact: 8.5 | O(N^3))
    * *Intent:* /// Returns the raster of the given char or the raster of [`font_constants::BACKUP_CHAR`].
  * `write_str` (Impact: 7.2 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 29`, `args: 13`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 20`, `orphaned_logic: 1`
* *Architecture:* `api: 7`, `concurrency: 12`, `import: 5`
* *Defense:* `safety: 5`, `doc: 17`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*, RasterHeight, get_raster, RasterizedChar, get_raster_width, PixelFormat, bootloader_api::info::FrameBufferInfo, core::fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bios/stage-3/src/screen.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.764 IQR)
- **Top Global Matches:** file_cluster_4: 11.764, file_cluster_8: 11.839, file_cluster_13: 11.873
- **Magnitude:** 135.06 | **LOC:** 129 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (69.4263%), Tech Debt (95.5022%)
**Top Internal Functions/Classes:**
  * `write_char` (Impact: 21.6 | O(N^5) | DB: 1)
  * `write_pixel` (Impact: 17.7 | O(N^4) | DB: 1)
  * `write_rendered_char` (Impact: 13.4 | O(N^4) | DB: 1)
  * `write_str` (Impact: 7.2 | O(N^3) | DB: 1)
  * `write_str` (Impact: 5.4 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 32`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 23`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 4`, `concurrency: 12`, `import: 3`
* *Defense:* `safety: 8`, `doc: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` get_bitmap, noto_sans_mono_bitmap::BitmapChar, bootloader_x86_64_bios_common::BiosFramebufferInfo, BitmapHeight, PixelFormat, core::fmt, racy_cell::RacyCell, FontWeight...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/fat.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.065 IQR)
- **Top Global Matches:** file_cluster_13: 11.065, file_cluster_8: 11.238, file_cluster_17: 11.411
- **Magnitude:** 131.28 | **LOC:** 94 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (33.7227%), Tech Debt (24.0736%)
**Top Internal Functions/Classes:**
  * `add_files_to_image` (Impact: 80.0 | O(N^6) | DB: 2)
  * `create_fat_filesystem` (Impact: 33.8 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 29`, `args: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 6`
* *Defense:* `safety: 7`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::collections::BTreeMap, crate::KERNEL_FILE_NAME, anyhow::Context, crate::file_data_source::FileDataSource, std::fs::File, fs, fatfs::Dir, path::Path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/mbr.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.01 IQR)
- **Top Global Matches:** file_cluster_8: 11.01, file_cluster_13: 11.031, file_cluster_11: 11.411
- **Magnitude:** 130.06 | **LOC:** 101 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (65.9856%), Tech Debt (55.2516%)
**Top Internal Functions/Classes:**
  * `create_mbr_disk` (Impact: 96.4 | O(N^4) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 25`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 31`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 4`
* *Defense:* `safety: 2`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File, mbrman::BOOT_ACTIVE, Seek, anyhow::Context, SeekFrom, path::Path, std::io::Cursor, std::
    fs::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bios/stage-4/src/main.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.192 IQR)
- **Top Global Matches:** file_cluster_13: 11.192, file_cluster_8: 11.26, file_cluster_0: 11.265
- **Magnitude:** 129.04 | **LOC:** 308 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (12.8814%), Tech Debt (39.5018%)
**Top Internal Functions/Classes:**
  * `_start` (Impact: 98.7 | O(N^5) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 57`, `args: 11`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 25`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` load_and_switch_to_kernel, PageTableFlags, Size2MiB, x86_64::PhysAddr, PhysicalMapping, bootloader_x86_64_common::
    Kernel, E820MemoryRegion, PixelFormat...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/file_data_source.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.736 IQR)
- **Top Global Matches:** file_cluster_13: 12.736, file_cluster_0: 13.088, file_cluster_11: 13.13
- **Magnitude:** 127.86 | **LOC:** 67 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (33.6759%), Tech Debt (31.5212%)
**Top Internal Functions/Classes:**
  * `copy_to` (Impact: 49.6 | O(N^6) | DB: 9)
    * *Intent:* /// Copy this data source to the specified target that implements io::Write
  * `len` (Impact: 35.1 | O(2^N))
    * *Intent:* /// Get the length of the inner data source
  * `fmt` (Impact: 18.0 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 17`, `args: 5`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 3`, `import: 5`
* *Defense:* `safety: 8`, `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::fs, std::path::PathBuf, core::fmt::Debug, anyhow::Context, io, Formatter, std::io::Cursor
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common/src/level_4_entries.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.642 IQR)
- **Top Global Matches:** file_cluster_13: 11.642, file_cluster_16: 11.957, file_cluster_8: 12.0
- **Magnitude:** 122.86 | **LOC:** 230 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (6.3249%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 110.2 | O(2^N) | DB: 5)
    * *Intent:* /// Initializes a new instance. /// /// Marks the statically configured virtual address ranges from ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 27`, `args: 7`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 8`, `doc: 20`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` seq::IteratorRandom, structures::paging::Page, header, info::MemoryRegion, crate::
    BootInfo, core::alloc::Layout, rand::
    distributions::Distribution, entropy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/runner/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.499 IQR)
- **Top Global Matches:** file_cluster_4: 11.499, file_cluster_0: 11.766, file_cluster_13: 11.943
- **Magnitude:** 120.12 | **LOC:** 151 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (48.4811%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_qemu` (Impact: 23.8 | O(N^3) | DB: 20)
  * `run_test_kernel_internal` (Impact: 11.7 | O(N^2) | DB: 1)
  * `run_test_kernel_on_uefi_pxe` (Impact: 4.8 | O(N^3))
  * `run_test_kernel_on_uefi` (Impact: 3.5 | O(N^2))
  * `run_test_kernel_on_bios` (Impact: 3.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 38`, `args: 10`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 27`, `orphaned_logic: 3`
* *Architecture:* `io: 4`, `api: 7`, `concurrency: 30`, `import: 4`
* *Defense:* `safety: 15`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::
        io::Read, Stdio, bootloader::DiskImageBuilder, std::path::Path, process::Command, bootloader::BootConfig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bios/stage-2/src/disk.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.774 IQR)
- **Top Global Matches:** file_cluster_0: 11.774, file_cluster_8: 11.88, file_cluster_13: 12.013
- **Magnitude:** 106.98 | **LOC:** 118 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (52.2135%), Tech Debt (99.9708%)
**Top Internal Functions/Classes:**
  * `read_exact_into` (Impact: 21.7 | O(N^4) | DB: 6)
  * `slice_mut` (Impact: 12.6 | O(2^N) | DB: 5)
  * `read_exact_at` (Impact: 9.2 | O(N^3) | DB: 3)
  * `seek` (Impact: 9.1 | O(N^4) | DB: 1)
  * `read_exact_into` (Impact: 2.4 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 39`, `args: 11`, `func_start: 10`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 37`, `duplicate_logic: 4`
* *Architecture:* `api: 11`, `import: 1`
* *Defense:* `safety: 3`, `doc: 1`, `test: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::dap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bios/stage-2/src/main.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.904 IQR)
- **Top Global Matches:** file_cluster_0: 10.904, file_cluster_13: 10.934, file_cluster_8: 11.004
- **Magnitude:** 91.3 | **LOC:** 271 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (30.3965%), Tech Debt (37.7541%)
**Top Internal Functions/Classes:**
  * `start` (Impact: 44.9 | O(N^4) | DB: 15)
  * `fail` (Impact: 4.3 | O(2^N))
  * `load_file` (Impact: 3.1 | O(N^1) | DB: 4)
  * `_start` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 69`, `args: 7`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 1`, `state_mutation: 32`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `safety: 4`, `doc: 5`, `test: 3`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` this partition type to store the second bootloader stage, Seek, LittleEndian, SeekFrom, slice, crate::
    disk::Read, bootloader_x86_64_bios_common::BiosFramebufferInfo, hlt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common/src/logger.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.882 IQR)
- **Top Global Matches:** file_cluster_13: 12.882, file_cluster_16: 13.161, file_cluster_8: 13.313
- **Magnitude:** 90.5 | **LOC:** 72 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (11.0046%), Tech Debt (75.7011%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 30.4 | O(2^N) | DB: 1)
    * *Intent:* /// Create a new instance that logs to the given framebuffer.
  * `log` (Impact: 21.3 | O(2^N) | DB: 2)
  * `force_unlock` (Impact: 21.2 | O(2^N))
    * *Intent:* /// Force-unlocks the logger to prevent a deadlock. /// /// ## Safety /// This method is not memory ...
  * `enabled` (Impact: 2.7 | O(N^2))
  * `flush` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 19`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`, `orphaned_logic: 2`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 16`, `doc: 7`, `sync_locks: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` conquer_once::spin::OnceCell, crate::framebuffer::FrameBufferWriter, serial::SerialPort, core::fmt::Write, spinning_top::Spinlock, bootloader_api::info::FrameBufferInfo
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_kernels/ramdisk/src/bin/memory_map.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.249 IQR)
- **Top Global Matches:** file_cluster_13: 10.249, file_cluster_0: 10.395, file_cluster_8: 10.459
- **Magnitude:** 65.44 | **LOC:** 89 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (16.5087%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `kernel_main` (Impact: 45.2 | O(N^4) | DB: 2)
  * `panic` (Impact: 4.3 | O(2^N))
    * *Intent:* /// This function is called on panic.
  * `active_level_4_table` (Impact: 2.5 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 26`, `args: 4`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 2`, `doc: 1`, `test: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Translate, RAMDISK_CONTENTS, PageTableFlags, structures::paging::OffsetPageTable, PageTable, x86_64::registers::control::Cr3, config::Mapping, info::MemoryRegionKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/gpt.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.162 IQR)
- **Top Global Matches:** file_cluster_13: 13.162, file_cluster_17: 13.284, file_cluster_0: 13.355
- **Magnitude:** 63.18 | **LOC:** 71 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (70.0955%), Tech Debt (34.3407%)
**Top Internal Functions/Classes:**
  * `create_gpt_disk` (Impact: 42.1 | O(N^2) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 17`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 19`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File, Seek, anyhow::Context, path::Path, std::
    fs::self, io::self
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bios/stage-2/src/screen.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.048 IQR)
- **Top Global Matches:** file_cluster_0: 10.048, file_cluster_8: 10.112, file_cluster_13: 10.339
- **Magnitude:** 54.9 | **LOC:** 47 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (21.4165%), Tech Debt (50.0%)
**Top Internal Functions/Classes:**
  * `print_str` (Impact: 25.6 | O(N^4))
  * `panic` (Impact: 18.6 | O(2^N))
  * `write_str` (Impact: 2.8 | O(N^2) | DB: 1)
  * `print_char` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 12`, `args: 9`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 4`, `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fmt::Write, core::arch::asm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/basic/src/main.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.507 IQR)
- **Top Global Matches:** file_cluster_8: 10.507, file_cluster_4: 10.575, file_cluster_17: 10.603
- **Magnitude:** 52.48 | **LOC:** 70 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (41.743%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 41.4 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 19`, `args: 4`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 4`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 6`, `import: 3`
* *Defense:* `safety: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exit, ovmf_prebuilt::Arch, std::env, Prebuilt, std::process::Command, FileType, Source
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/test_kernels/default_settings/src/bin/check_boot_info.rs` (RUST) | Magnitude: 17.48 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, test: 8, structural_boundaries: 7, decorators: 4
- `tests/test_kernels/pie/src/bin/check_boot_info.rs` (RUST) | Magnitude: 17.48 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, test: 8, structural_boundaries: 7, decorators: 4
- `tests/test_kernels/higher_half/src/bin/check_boot_info.rs` (RUST) | Magnitude: 17.48 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, test: 8, structural_boundaries: 7, decorators: 4
- `tests/test_kernels/pie/src/bin/should_panic.rs` (RUST) | Magnitude: 8.16 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: decorators: 4, structural_boundaries: 3, indent_spaces: 3, args: 2
- `tests/test_kernels/default_settings/src/bin/should_panic.rs` (RUST) | Magnitude: 8.16 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: decorators: 4, structural_boundaries: 3, indent_spaces: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/test_kernels/stack_address/src/bin/basic_boot.rs` (RUST) | Magnitude: 10.28 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 7, test: 4, decorators: 4
- `tests/test_kernels/write_usable_memory/src/bin/write_usable_memory.rs` (RUST) | Magnitude: 30.24 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 11, state_mutation: 5, decorators: 4
- `bios/stage-3/src/paging.rs` (RUST) | Magnitude: 34.26 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 19, state_mutation: 10, args: 8
- `bios/stage-4/src/main.rs` (RUST) | Magnitude: 129.04 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 185, structural_boundaries: 57, state_mutation: 25, safety: 17
- `tests/test_kernels/map_phys_mem/src/bin/check_boot_info.rs` (RUST) | Magnitude: 17.76 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 8, test: 8, decorators: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `common/src/lib.rs` (RUST) | Magnitude: 344.46 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 336, structural_boundaries: 101, doc: 62, api: 44
- `common/src/load_kernel.rs` (RUST) | Magnitude: 350.18 | Delta: **0.115 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 216, structural_boundaries: 66, doc: 49, branch: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `uefi/src/main.rs` (RUST) | Magnitude: 451.3 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 410, structural_boundaries: 154, state_mutation: 101, safety: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `bios/stage-3/src/screen.rs` (RUST) | Magnitude: 135.06 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 32, state_mutation: 23, branch: 12
- `bios/common/src/racy_cell.rs` (RUST) | Magnitude: 38.36 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: concurrency: 24, generics: 9, structural_boundaries: 8, indent_spaces: 7
- `tests/runner/src/lib.rs` (RUST) | Magnitude: 120.12 | Delta: **0.267 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 38, concurrency: 30, state_mutation: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `common/config/src/lib.rs` (RUST) | Magnitude: 20.98 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 29, indent_spaces: 26, api: 10, encapsulation: 10
- `tests/test_kernels/higher_half/src/bin/verify_higher_half.rs` (RUST) | Magnitude: 10.62 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 7, decorators: 4, pointers: 4
- `src/mbr.rs` (RUST) | Magnitude: 130.06 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 31, structural_boundaries: 25, branch: 14
- `src/disk_image.rs` (RUST) | Magnitude: 166.02 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 137, structural_boundaries: 37, branch: 30, state_mutation: 19
- `tests/test_kernels/fixed_kernel_address/src/lib.rs` (RUST) | Magnitude: 19.18 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, api: 5, state_mutation: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `bios/boot_sector/src/boot.s` (ASSEMBLY) | Magnitude: 22.04 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, args: 16, structural_boundaries: 12, func_start: 7

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `bios/stage-2/src/disk.rs` -> Churn: **100.0%** | Cog Load: 52.2135% | Debt: 99.9708%
- `src/lib.rs` -> Churn: **52.29%** | Cog Load: 10.1667% | Debt: 77.9618%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `uefi/src/main.rs` -> **Spencer** (100.0% isolated ownership) | Magnitude: 451.3
- `common/src/legacy_memory_region.rs` -> **Spencer** (100.0% isolated ownership) | Magnitude: 416.82
- `api/src/config.rs` -> **rezky_nightky** (100.0% isolated ownership) | Magnitude: 192.92
- `bios/stage-2/src/vesa.rs` -> **Spencer** (100.0% isolated ownership) | Magnitude: 181.54
- `api/src/info.rs` -> **Burkhard Mittelbach** (100.0% isolated ownership) | Magnitude: 171.76

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `common/src/serial.rs` -> **Severity: 3.325** (Embedded: 0.0631 * Error Risk: 52.7273%)
- `common/src/entropy.rs` -> **Severity: 0.173** (Embedded: 0.009 * Error Risk: 19.2155%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `common/src/serial.rs` -> **Severity: 5849.919** (Blast Radius: 58.501 * Doc Risk: 99.9969%)
- `api/src/info.rs` -> **Severity: 841.8** (Blast Radius: 8.418 * Doc Risk: 100.0%)
- `bios/boot_sector/src/fail.rs` -> **Severity: 841.8** (Blast Radius: 8.418 * Doc Risk: 100.0%)
- `bios/boot_sector/src/main.rs` -> **Severity: 841.8** (Blast Radius: 8.418 * Doc Risk: 100.0%)
- `bios/common/src/lib.rs` -> **Severity: 841.8** (Blast Radius: 8.418 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
