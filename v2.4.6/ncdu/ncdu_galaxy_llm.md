# ARCHITECTURAL_BRIEF: ncdu
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_zig/ncdu` |
| **Timestamp** | `2026-08-03T20:08:47.896480+00:00` |
| **Scan Duration** | `0.2s` |
| **Git Branch** | `master` |
| **Git Commit** | `a216bc2d35b6edf4dadf55350f09d7cbf229fbf7` |
| **Git Remote** | `https://github.com/rofl0r/ncdu.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 27 malicious artifacts.

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
| Total Artifacts | 36 |
| Analyzed Artifacts (Scanned) | 31 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 2829 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 86.1% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1667 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.8794 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 25.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9846 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 26 | 2501 | 83.9% |
| PLAINTEXT | 2 | 0 | 6.5% |
| MARKDOWN | 1 | 0 | 3.2% |
| M4 | 1 | 55 | 3.2% |
| PERL | 1 | 273 | 3.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.212`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 16 | 51.6% |
| file_cluster_8 | 10 | 32.3% |
| file_cluster_9 | 2 | 6.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 9.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `.h`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.am`: 1x Excluded (Unsupported Extension: '.am')
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 89.9 | 48.6 | 74.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.9 | 34.3 | 22.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 30.7 | 13.9 | 0.0 |
| Testing Exposure | 0.8 | 80.0 | 35.3 | 2.6 | 80.0 |
| API Exposure | 0.0 | 12.6 | 7.7 | 7.8 | 7.6 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 60.3 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 33.3 | 100.0 | 86.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 69.3 | 90.6 | 46.7 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 40.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 2.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doc/ncdu.pod` (Hits: 14)
- `src/exclude.c` (Hits: 5)
- `src/browser.c` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **global.h** (`src/global.h`) — 21 inbound connections
2. **util.h** (`src/util.h`) — 3 inbound connections
3. **dirlist.h** (`src/dirlist.h`) — 2 inbound connections
4. **browser.h** (`src/browser.h`) — 1 inbound connections
5. **delete.h** (`src/delete.h`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **global.h** (`src/global.h`) — 19 outbound dependencies
2. **dir_scan.c** (`src/dir_scan.c`) — 11 outbound dependencies
3. **main.c** (`src/main.c`) — 8 outbound dependencies
4. **shell.c** (`src/shell.c`) — 8 outbound dependencies
5. **path.c** (`src/path.c`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `cons` (@ `src/dir_import.c`) -> Impact: **440.2** | LOC: 319
- `browse_key` (@ `src/browser.c`) -> Impact: **362.0** | LOC: 225
- `dirlist_fixup` (@ `src/dirlist.c`) -> Impact: **231.2** | LOC: 70
- `delete_dir` (@ `src/delete.c`) -> Impact: **122.2** | LOC: 43
- `delete_key` (@ `src/delete.c`) -> Impact: **96.3** | LOC: 56
- `input_handle` (@ `src/main.c`) -> Impact: **90.7** | LOC: 48
- `browse_draw_flag` (@ `src/browser.c`) -> Impact: **85.7** | LOC: 17
- `help_key` (@ `src/help.c`) -> Impact: **77.2** | LOC: 38
- `dirlist_cmp` (@ `src/dirlist.c`) -> Impact: **72.1** | LOC: 40
- `output_string` (@ `src/dir_export.c`) -> Impact: **67.0** | LOC: 19

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `dirlist_fixup` (@ `src/dirlist.c`) -> **O(2^N) [Recursive]**
- `delete_dir` (@ `src/delete.c`) -> **O(2^N) [Recursive]**
- `cons` (@ `src/dir_import.c`) -> **O(2^N) [Recursive]**
- `input_handle` (@ `src/main.c`) -> **O(2^N) [Recursive]**
- `item` (@ `src/dir_export.c`) -> **O(2^N) [Recursive]**
- `hlink_check` (@ `src/dir_mem.c`) -> **O(2^N) [Recursive]**
  * *Intent:* */ #include "global.h" #include <string.h> #include <stdlib.h> #include <khashl.h> static struct dir *root; /* root directory struct we're scanning */...
- `hlink_init` (@ `src/dir_mem.c`) -> **O(2^N) [Recursive]**
- `browse_draw_flag` (@ `src/browser.c`) -> **O(N^6)**
- `has_cachedir_tag` (@ `src/exclude.c`) -> **O(N^4)**
- `shell_draw` (@ `src/shell.c`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `browse_key` (@ `src/browser.c`) -> DB Complexity: **63**
- `cons` (@ `src/dir_import.c`) -> DB Complexity: **40**
- `dirlist_sort` (@ `src/dirlist.c`) -> DB Complexity: **33**
  * *Intent:* /* sort columns: * 1 -> 2 -> 3 -> 4 * NAME: name -> size -> asize -> items * SIZE: size -> asize -> name -> items * ASIZE: asize -> size -> name -> it...
- `formatsize` (@ `src/util.c`) -> DB Complexity: **27**
- `dirlist_fixup` (@ `src/dirlist.c`) -> DB Complexity: **23**
- `path_split` (@ `src/path.c`) -> DB Complexity: **21**
  * *Intent:* */
- `getpath` (@ `src/util.c`) -> DB Complexity: **19**
- `has_cachedir_tag` (@ `src/exclude.c`) -> DB Complexity: **18**
- `draw_progress` (@ `src/dir_common.c`) -> DB Complexity: **17**
- `help_draw` (@ `src/help.c`) -> DB Complexity: **15**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 26 | 4884.02 | 51.6% | 32.38% |
| `doc` | 1 | 49.46 | 17.75% | 18.35% |
| `__monolith__` | 4 | 21.88 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/quit.c` -> **100.0%** Exposure
- `src/shell.c` -> **95.5022%** Exposure
- `src/exclude.c` -> **95.202%** Exposure
- `src/util.c` -> **91.2033%** Exposure
- `src/dir.h` -> **86.3872%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/browser.c` -> **100.0%** Exposure
- `src/delete.c` -> **100.0%** Exposure
- `src/dir_common.c` -> **100.0%** Exposure
- `src/dir_export.c` -> **100.0%** Exposure
- `src/dir_mem.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/util.c` -> **13** Orphaned Functions | **0** Duplicates
- `src/dir_common.c` -> **7** Orphaned Functions | **0** Duplicates
- `src/delete.c` -> **4** Orphaned Functions | **0** Duplicates
- `src/exclude.c` -> **4** Orphaned Functions | **0** Duplicates
- `src/browser.c` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/dir_scan.c`** -> AI Confidence: **99.48%**
2. **`src/main.c`** -> AI Confidence: **99.48%**
3. **`src/path.c`** -> AI Confidence: **99.48%**
4. **`src/shell.c`** -> AI Confidence: **99.48%**
5. **`src/browser.c`** -> AI Confidence: **99.34%**
6. **`src/help.c`** -> AI Confidence: **99.32%**
7. **`src/util.c`** -> AI Confidence: **99.31%**
8. **`src/dir_common.c`** -> AI Confidence: **99.23%**
9. **`src/dir_export.c`** -> AI Confidence: **99.23%**
10. **`src/dir_import.c`** -> AI Confidence: **99.22%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/browser.c` -> **20.0%** Exposure
- `src/dirlist.c` -> **20.0%** Exposure
- `src/exclude.c` -> **20.0%** Exposure
- `src/shell.c` -> **20.0%** Exposure
### Algorithmic DoS Exposure
- `src/browser.c` -> **100.0%** Exposure
- `src/delete.c` -> **100.0%** Exposure
- `src/dir_common.c` -> **100.0%** Exposure
- `src/dir_import.c` -> **100.0%** Exposure
- `src/dirlist.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `113` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/exclude.c` (C) -> Cumulative Risk: **768.45**
- **Archetype:** `file_cluster_13` (Distance: 13.321 IQR)
- **Magnitude:** 169.24 | **LOC:** 139 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9934%)
- **Heaviest Functions:** `has_cachedir_tag` (Impact: 31.4), `exclude_match` (Impact: 18.8), `exclude_addfile` (Impact: 14.9)

### 2. `src/util.c` (C) -> Cumulative Risk: **761.61**
- **Archetype:** `file_cluster_13` (Distance: 14.164 IQR)
- **Magnitude:** 597.48 | **LOC:** 435 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.8909%)
- **Heaviest Functions:** `fmtmode` (Impact: 55.1), `formatsize` (Impact: 28.1), `getpath` (Impact: 19.9)

### 3. `src/path.c` (C) -> Cumulative Risk: **713.21**
- **Archetype:** `file_cluster_13` (Distance: 13.276 IQR)
- **Magnitude:** 187.66 | **LOC:** 247 | **CtrlFlow:** 81.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (94.7967%)
- **Heaviest Functions:** `path_split` (Impact: 40.9), `path_chdir` (Impact: 15.0), `path_real` (Impact: 6.7)

### 4. `src/dir_common.c` (C) -> Cumulative Risk: **708.31**
- **Archetype:** `file_cluster_13` (Distance: 12.138 IQR)
- **Magnitude:** 231.06 | **LOC:** 233 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (97.9057%)
- **Heaviest Functions:** `draw_progress` (Impact: 34.6), `dir_draw` (Impact: 23.9), `dir_key` (Impact: 20.0)

### 5. `src/dirlist.c` (C) -> Cumulative Risk: **694.91**
- **Archetype:** `file_cluster_13` (Distance: 14.071 IQR)
- **Magnitude:** 604.68 | **LOC:** 399 | **CtrlFlow:** 77.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (98.9299%)
- **Heaviest Functions:** `dirlist_fixup` (Impact: 231.2), `dirlist_cmp` (Impact: 72.1), `dirlist_sort` (Impact: 62.3)

### 6. `src/browser.c` (C) -> Cumulative Risk: **678.61**
- **Archetype:** `file_cluster_8` (Distance: 12.908 IQR)
- **Magnitude:** 971.48 | **LOC:** 568 | **CtrlFlow:** 87.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (96.7436%)
- **Heaviest Functions:** `browse_key` (Impact: 362.0), `browse_draw_flag` (Impact: 85.7), `browse_draw_info` (Impact: 57.6)

### 7. `src/delete.c` (C) -> Cumulative Risk: **673.04**
- **Archetype:** `file_cluster_8` (Distance: 12.127 IQR)
- **Magnitude:** 388.76 | **LOC:** 254 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (98.1873%)
- **Heaviest Functions:** `delete_dir` (Impact: 122.2), `delete_key` (Impact: 96.3), `delete_draw_confirm` (Impact: 16.7)

### 8. `src/shell.c` (C) -> Cumulative Risk: **660.01**
- **Archetype:** `file_cluster_13` (Distance: 11.28 IQR)
- **Magnitude:** 51.1 | **LOC:** 83 | **CtrlFlow:** 81.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.7267%)
- **Heaviest Functions:** `shell_draw` (Impact: 22.1), `shell_init` (Impact: 1.1)

### 9. `src/help.c` (C) -> Cumulative Risk: **622.25**
- **Archetype:** `file_cluster_8` (Distance: 11.337 IQR)
- **Magnitude:** 190.26 | **LOC:** 213 | **CtrlFlow:** 93.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `help_key` (Impact: 77.2), `help_draw` (Impact: 22.6), `help_init` (Impact: 1.2)

### 10. `src/dir_export.c` (C) -> Cumulative Risk: **609.59**
- **Archetype:** `file_cluster_13` (Distance: 11.776 IQR)
- **Magnitude:** 197.64 | **LOC:** 195 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.0899%), Cognitive Load (86.9541%)
- **Heaviest Functions:** `output_string` (Impact: 67.0), `item` (Impact: 29.6), `output_info` (Impact: 23.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/browser.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.908 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.27 IQR)
- **Top Global Matches:** file_cluster_8: 12.908, file_cluster_13: 13.112, file_cluster_7: 13.305
- **Magnitude:** 971.48 | **LOC:** 568 | **CtrlFlow:** 87.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (88.7122%), Tech Debt (15.0706%)
**Top Internal Functions/Classes:**
  * `browse_key` (Impact: 362.0 | O(N^2) | DB: 63)
  * `browse_draw_flag` (Impact: 85.7 | O(N^6) | DB: 1)
  * `browse_draw_info` (Impact: 57.6 | O(N^2) | DB: 8)
  * `browse_draw_graph` (Impact: 38.2 | O(N^1) | DB: 9)
  * `browse_draw` (Impact: 22.7 | O(N^1) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 33`, `args: 9`, `func_start: 9`, `class_start: 10`
* *Risk/State:* `state_mutation: 294`, `orphaned_logic: 3`
* *Architecture:* `io: 3`, `api: 44`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, ncurses.h, stdlib.h, time.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dirlist.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.071 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.951 IQR)
- **Top Global Matches:** file_cluster_13: 14.071, file_cluster_8: 14.088, file_cluster_11: 14.296
- **Magnitude:** 604.68 | **LOC:** 399 | **CtrlFlow:** 77.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (89.9159%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dirlist_fixup` (Impact: 231.2 | O(2^N) | DB: 23)
  * `dirlist_cmp` (Impact: 72.1 | O(N^2) | DB: 5)
  * `dirlist_sort` (Impact: 62.3 | O(N^2) | DB: 33)
    * *Intent:* /* sort columns: * 1 -> 2 -> 3 -> 4 * NAME: name -> size -> asize -> items * SIZE: size -> asize -> ...
  * `cmp_mtime` (Impact: 9.1 | O(N^1) | DB: 4)
    * *Intent:* */ #include "global.h" #include <string.h> #include <stdlib.h>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 22`, `args: 7`, `func_start: 7`, `class_start: 5`
* *Risk/State:* `state_mutation: 208`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string.h, stdlib.h, global.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/util.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.164 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.198 IQR)
- **Top Global Matches:** file_cluster_13: 14.164, file_cluster_8: 14.333, file_cluster_11: 14.373
- **Magnitude:** 597.48 | **LOC:** 435 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (80.9695%), Tech Debt (91.2033%)
**Top Internal Functions/Classes:**
  * `fmtmode` (Impact: 55.1 | O(N^2) | DB: 12)
  * `formatsize` (Impact: 28.1 | O(N^1) | DB: 27)
  * `getpath` (Impact: 19.9 | O(N^1) | DB: 19)
  * `ncresize` (Impact: 13.4 | O(N^1) | DB: 1)
  * `addparentstats` (Impact: 10.4 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 38`, `args: 14`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 336`, `orphaned_logic: 13`
* *Architecture:* `io: 2`, `api: 62`, `import: 7`
* *Defense:* `safety: 6`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdarg.h, util.h, unistd.h, ncurses.h, stdlib.h, locale.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_import.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.794 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.118 IQR)
- **Top Global Matches:** file_cluster_8: 11.794, file_cluster_13: 11.949, file_cluster_7: 12.251
- **Magnitude:** 545.48 | **LOC:** 616 | **CtrlFlow:** 76.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (75.7011%), Tech Debt (12.6549%)
**Top Internal Functions/Classes:**
  * `cons` (Impact: 440.2 | O(2^N) | DB: 40)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 30`, `args: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 86`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 14`, `import: 6`
* *Defense:* `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` errno.h, global.h, limits.h, stdlib.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/delete.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.127 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.091 IQR)
- **Top Global Matches:** file_cluster_8: 12.127, file_cluster_13: 12.237, file_cluster_7: 12.582
- **Magnitude:** 388.76 | **LOC:** 254 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (88.6416%), Tech Debt (48.9756%)
**Top Internal Functions/Classes:**
  * `delete_dir` (Impact: 122.2 | O(2^N) | DB: 11)
  * `delete_key` (Impact: 96.3 | O(N^2) | DB: 12)
  * `delete_draw_confirm` (Impact: 16.7 | O(N^1))
  * `delete_process` (Impact: 15.1 | O(N^2) | DB: 7)
  * `delete_draw` (Impact: 8.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 28`, `args: 6`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 97`, `orphaned_logic: 4`
* *Architecture:* `api: 19`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string.h, errno.h, global.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_common.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.138 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.362 IQR)
- **Top Global Matches:** file_cluster_13: 12.138, file_cluster_8: 12.214, file_cluster_0: 12.462
- **Magnitude:** 231.06 | **LOC:** 233 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (76.8936%), Tech Debt (86.2387%)
**Top Internal Functions/Classes:**
  * `draw_progress` (Impact: 34.6 | O(N^2) | DB: 17)
  * `dir_draw` (Impact: 23.9 | O(N^2) | DB: 1)
  * `dir_key` (Impact: 20.0 | O(N^1) | DB: 2)
  * `curpath_resize` (Impact: 7.2 | O(N^1) | DB: 2)
  * `dir_setlasterr` (Impact: 6.7 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 20`, `args: 8`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 89`, `orphaned_logic: 7`
* *Architecture:* `io: 2`, `api: 26`, `import: 5`
* *Defense:* `safety: 2`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdarg.h, global.h, stdlib.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_export.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.776 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.276 IQR)
- **Top Global Matches:** file_cluster_13: 11.776, file_cluster_8: 11.983, file_cluster_11: 12.184
- **Magnitude:** 197.64 | **LOC:** 195 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (86.9541%), Tech Debt (64.4004%)
**Top Internal Functions/Classes:**
  * `output_string` (Impact: 67.0 | O(N^2) | DB: 2)
  * `item` (Impact: 29.6 | O(2^N) | DB: 4)
  * `output_info` (Impact: 23.1 | O(N^1) | DB: 1)
  * `dir_export_init` (Impact: 8.8 | O(N^1) | DB: 10)
  * `output_int` (Impact: 4.5 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 15`, `args: 5`, `func_start: 6`
* *Risk/State:* `state_mutation: 44`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 15`, `import: 5`
* *Defense:* `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, stdlib.h, time.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/help.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.337 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.802 IQR)
- **Top Global Matches:** file_cluster_8: 11.337, file_cluster_13: 11.597, file_cluster_7: 11.854
- **Magnitude:** 190.26 | **LOC:** 213 | **CtrlFlow:** 93.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (74.1775%), Tech Debt (41.2713%)
**Top Internal Functions/Classes:**
  * `help_key` (Impact: 77.2 | O(N^2) | DB: 11)
  * `help_draw` (Impact: 22.6 | O(N^2) | DB: 15)
  * `help_init` (Impact: 1.2 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 3`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 76`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 10`, `import: 3`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ncurses.h, global.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/path.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.276 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.549 IQR)
- **Top Global Matches:** file_cluster_13: 13.276, file_cluster_8: 13.631, file_cluster_11: 13.679
- **Magnitude:** 187.66 | **LOC:** 247 | **CtrlFlow:** 81.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (88.6779%), Tech Debt (48.1804%)
**Top Internal Functions/Classes:**
  * `path_split` (Impact: 40.9 | O(N^2) | DB: 21)
    * *Intent:* */
  * `path_chdir` (Impact: 15.0 | O(N^1) | DB: 5)
  * `path_real` (Impact: 6.7 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 7`, `args: 5`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 105`, `orphaned_logic: 2`
* *Architecture:* `api: 18`, `import: 7`
* *Defense:* `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` errno.h, global.h, unistd.h, limits.h, stdlib.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/exclude.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.321 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.377 IQR)
- **Top Global Matches:** file_cluster_13: 13.321, file_cluster_0: 13.727, file_cluster_9: 13.729
- **Magnitude:** 169.24 | **LOC:** 139 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (74.5199%), Tech Debt (95.202%)
**Top Internal Functions/Classes:**
  * `has_cachedir_tag` (Impact: 31.4 | O(N^4) | DB: 18)
  * `exclude_match` (Impact: 18.8 | O(N^2) | DB: 5)
  * `exclude_addfile` (Impact: 14.9 | O(N^1) | DB: 10)
    * *Intent:* */ #include "global.h" #include <stdio.h> #include <stdlib.h> #include <string.h>
  * `exclude_add` (Impact: 4.0 | O(N^1) | DB: 4)
  * `exclude_clear` (Impact: 2.5 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 15`, `args: 5`, `func_start: 5`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 77`, `orphaned_logic: 4`
* *Architecture:* `io: 5`, `api: 19`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fnmatch.h, global.h, stdlib.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_mem.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.327 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.624 IQR)
- **Top Global Matches:** file_cluster_13: 13.327, file_cluster_8: 13.48, file_cluster_11: 13.74
- **Magnitude:** 164.84 | **LOC:** 216 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (83.3378%), Tech Debt (33.8333%)
**Top Internal Functions/Classes:**
  * `hlink_check` (Impact: 41.7 | O(2^N) | DB: 9)
    * *Intent:* */ #include "global.h" #include <string.h> #include <stdlib.h> #include <khashl.h> static struct dir...
  * `final` (Impact: 17.1 | O(N^1) | DB: 8)
  * `hlink_init` (Impact: 12.6 | O(2^N) | DB: 2)
  * `dir_mem_init` (Impact: 4.8 | O(N^1) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 16`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `state_mutation: 81`, `orphaned_logic: 1`
* *Architecture:* `api: 6`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string.h, stdlib.h, global.h, khashl.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.053 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.792 IQR)
- **Top Global Matches:** file_cluster_13: 11.053, file_cluster_8: 11.463, file_cluster_9: 11.742
- **Magnitude:** 159.38 | **LOC:** 360 | **CtrlFlow:** 87.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (85.7796%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `input_handle` (Impact: 90.7 | O(2^N) | DB: 2)
  * `screen_draw` (Impact: 20.3 | O(N^1))
    * *Intent:* */ #include "global.h" #include <stdlib.h> #include <stdio.h> #include <string.h>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 4`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`
* *Architecture:* `api: 19`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` errno.h, global.h, unistd.h, yopt.h, stdlib.h, stdio.h, string.h, time.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_scan.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.028 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.002 IQR)
- **Top Global Matches:** file_cluster_13: 13.028, file_cluster_8: 13.383, file_cluster_11: 13.603
- **Magnitude:** 149.32 | **LOC:** 406 | **CtrlFlow:** 82.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (83.9589%), Tech Debt (23.0251%)
**Top Internal Functions/Classes:**
  * `process` (Impact: 30.8 | O(N^1) | DB: 11)
    * *Intent:* #endif #ifdef SELINUX_MAGIC
  * `dir_walk` (Impact: 7.7 | O(N^1) | DB: 5)
    * *Intent:* #endif #ifdef CGROUP2_SUPER_MAGIC
  * `dir_scan_init` (Impact: 4.5 | O(N^1) | DB: 3)
    * *Intent:* /* Reads all filenames in the currently chdir'ed directory and stores it as a * nul-separated list o...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 10`, `args: 7`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 91`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 13`, `import: 11`
* *Defense:* `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` errno.h, global.h, unistd.h, dirent.h, attr.h, magic.h, stat.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/shell.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.28 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.943 IQR)
- **Top Global Matches:** file_cluster_13: 11.28, file_cluster_8: 11.843, file_cluster_9: 11.859
- **Magnitude:** 51.1 | **LOC:** 83 | **CtrlFlow:** 81.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (80.5687%), Tech Debt (95.5022%)
**Top Internal Functions/Classes:**
  * `shell_draw` (Impact: 22.1 | O(N^3) | DB: 7)
  * `shell_init` (Impact: 1.1 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 22`, `orphaned_logic: 2`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` util.h, global.h, unistd.h, ncurses.h, wait.h, config.h, dirlist.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/ncdu.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.777 IQR)
- **Top Global Matches:** file_cluster_8: 10.777, file_cluster_13: 11.027, file_cluster_7: 11.033
- **Magnitude:** 49.46 | **LOC:** 446 | **CtrlFlow:** 92.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (17.7507%), Tech Debt (18.3521%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 6`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 29`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `import: 7`
* *Defense:* `doc: 73`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` effect, C, cases
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/util.h` (C | Tier 0 | 🚨 AI THREAT: 98.75%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.974 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.58 IQR)
- **Top Global Matches:** file_cluster_13: 12.974, file_cluster_8: 13.081, file_cluster_9: 13.128
- **Magnitude:** 47.56 | **LOC:** 196 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (82.5786%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dir_ext_ptr` (Impact: 4.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 24`, `args: 12`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 24`
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 52.556
  * `Choke Point (Betweenness):` 0.011494 | `Ripple Effect (Closeness):` 0.393496
  * `Imports (Out-Degree: 1):` ncurses.h, global.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/global.h` (C | Tier 1.5 | 🚨 AI THREAT: 99.01%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.537 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.806 IQR)
- **Top Global Matches:** file_cluster_13: 8.537, file_cluster_8: 8.567, file_cluster_7: 9.448
- **Magnitude:** 37.32 | **LOC:** 133 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `args: 2`, `class_start: 3`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 21`, `import: 19`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 377.819
  * `Choke Point (Betweenness):` 0.241379 | `Ripple Effect (Closeness):` 0.701449
  * `Imports (Out-Degree: 10):` util.h, shell.h, stdint.h, limits.h, browser.h, stat.h, inttypes.h, stddef.h...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/dir.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.653 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.566 IQR)
- **Top Global Matches:** file_cluster_8: 8.653, file_cluster_9: 9.089, file_cluster_7: 9.507
- **Magnitude:** 31.46 | **LOC:** 142 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.0248%), Tech Debt (86.3872%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 8`, `args: 7`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `api: 16`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 41.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.383333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/dirlist.h` (C | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.867 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.91 IQR)
- **Top Global Matches:** file_cluster_8: 8.867, file_cluster_9: 9.283, file_cluster_13: 9.315
- **Magnitude:** 22.34 | **LOC:** 87 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.2749%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `args: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 7`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 44.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.375194
  * `Imports (Out-Degree: 1):` global.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/quit.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.162 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.848 IQR)
- **Top Global Matches:** file_cluster_13: 10.162, file_cluster_8: 10.469, file_cluster_9: 10.5
- **Magnitude:** 20.0 | **LOC:** 51 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `quit_key` (Impact: 9.2 | O(N^1) | DB: 1)
  * `quit_draw` (Impact: 2.3 | O(N^1))
  * `quit_init` (Impact: 1.1 | O(N^1) | DB: 1)
    * *Intent:* */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 4`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 4`, `orphaned_logic: 3`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ncurses.h, global.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/exclude.h` (C | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.067 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.516 IQR)
- **Top Global Matches:** file_cluster_8: 9.067, file_cluster_9: 9.12, file_cluster_7: 9.872
- **Magnitude:** 19.16 | **LOC:** 36 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 5`
* *Risk/State:* None
* *Architecture:* `api: 5`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 41.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.383333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/delete.h` (C | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.055 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.744 IQR)
- **Top Global Matches:** file_cluster_8: 9.055, file_cluster_13: 9.071, file_cluster_9: 9.077
- **Magnitude:** 18.16 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 4`
* *Risk/State:* None
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.366667
  * `Imports (Out-Degree: 1):` global.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/browser.h` (C | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.008 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.764 IQR)
- **Top Global Matches:** file_cluster_13: 9.008, file_cluster_9: 9.01, file_cluster_8: 9.025
- **Magnitude:** 16.64 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 3`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.366667
  * `Imports (Out-Degree: 1):` global.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/help.h` (C | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.008 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.764 IQR)
- **Top Global Matches:** file_cluster_13: 9.008, file_cluster_9: 9.01, file_cluster_8: 9.025
- **Magnitude:** 16.64 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 3`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.366667
  * `Imports (Out-Degree: 1):` global.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/quit.h` (C | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.008 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.764 IQR)
- **Top Global Matches:** file_cluster_13: 9.008, file_cluster_9: 9.01, file_cluster_8: 9.025
- **Magnitude:** 16.64 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 3`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.366667
  * `Imports (Out-Degree: 1):` global.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/browser.h` (C) | Magnitude: 16.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 4, args: 3, api: 3, ownership: 3
- `src/help.h` (C) | Magnitude: 16.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 4, args: 3, api: 3, ownership: 3
- `src/quit.h` (C) | Magnitude: 16.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 4, args: 3, api: 3, ownership: 3
- `src/dirlist.c` (C) | Magnitude: 604.68 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 208, indent_spaces: 124, branch: 75, pointers: 57
- `src/global.h` (C) | Magnitude: 37.32 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 21, macros: 21, import: 19, indent_spaces: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/delete.h` (C) | Magnitude: 18.16 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, args: 4, api: 4, ownership: 3
- `src/exclude.h` (C) | Magnitude: 19.16 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: args: 5, api: 5, structural_boundaries: 3, ownership: 3
- `src/delete.c` (C) | Magnitude: 388.76 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 155, state_mutation: 97, branch: 82, structural_boundaries: 28
- `src/dir_import.c` (C) | Magnitude: 545.48 | Delta: **0.155 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 228, pointers: 125, branch: 99, state_mutation: 86
- `src/browser.c` (C) | Magnitude: 971.48 | Delta: **0.204 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 428, state_mutation: 294, branch: 229, pointers: 105

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/path.h` (C) | Magnitude: 14.6 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ownership: 3, args: 2, api: 2, macros: 2
- `src/shell.h` (C) | Magnitude: 15.12 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, ownership: 4, args: 2, api: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/util.h` -> **Severity: 1.149** (Bridge: 0.0115 * Flux: 99.999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/util.h` -> **Severity: 8.101** (Embedded: 0.3935 * Error Risk: 20.587%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/global.h` -> **Severity: 37778.197** (Blast Radius: 377.819 * Doc Risk: 99.9902%)
- `src/util.h` -> **Severity: 5237.878** (Blast Radius: 52.556 * Doc Risk: 99.6628%)
- `src/dirlist.h` -> **Severity: 4440.696** (Blast Radius: 44.411 * Doc Risk: 99.9909%)
- `src/dir.h` -> **Severity: 4169.6** (Blast Radius: 41.696 * Doc Risk: 100.0%)
- `src/delete.h` -> **Severity: 2223.785** (Blast Radius: 41.696 * Doc Risk: 53.3333%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
