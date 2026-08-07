# ARCHITECTURAL_BRIEF: gnucobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/gnucobol` |
| **Timestamp** | `2026-08-07T03:51:06.894382+00:00` |
| **Scan Duration** | `2.35s` |
| **Git Branch** | `main` |
| **Git Commit** | `d139d06201cf0aba9d143e0f675f446c19603b36` |
| **Git Remote** | `https://github.com/paulsmith/gnucobol.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 152 malicious artifacts.

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
| Total Artifacts | 382 |
| Analyzed Artifacts (Scanned) | 194 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 188 |
| Total LOC | 151502 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 50.8% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3924 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1308 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4165 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| M4 | 73 | 81822 | 37.6% |
| C | 46 | 61461 | 23.7% |
| PLAINTEXT | 36 | 0 | 18.6% |
| MAKEFILE | 11 | 1696 | 5.7% |
| COBOL | 9 | 1461 | 4.6% |
| SHELL | 6 | 533 | 3.1% |
| BATCH | 4 | 812 | 2.1% |
| MARKDOWN | 3 | 0 | 1.5% |
| PERL | 3 | 547 | 1.5% |
| YACC | 2 | 3165 | 1.0% |
| POWERSHELL | 1 | 5 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.356`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 144 | 74.2% |
| file_cluster_13 | 5 | 2.6% |
| file_cluster_9 | 2 | 1.0% |
| file_cluster_0 | 2 | 1.0% |
| file_cluster_11 | 1 | 0.5% |
| file_cluster_6 | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 39 | 20.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 188*

**Composition by Extension & Reason:**
- `.vcxproj`: 24x Excluded (Unsupported Extension: '.vcxproj')
- `.filters`: 24x Excluded (Unsupported Extension: '.filters')
- `.conf`: 19x Excluded (Unsupported Extension: '.conf')
- `no_extension`: 6x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 349 LOC)
- `.user`: 14x Excluded (Unsupported Extension: '.user')
- `.am`: 9x Excluded (Unsupported Extension: '.am'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.words`: 10x Excluded (Unsupported Extension: '.words')
- `.sln`: 8x Excluded (Unsupported Extension: '.sln')
- `.po`: 8x Excluded (Unsupported Extension: '.po')
- `.vcproj`: 6x Excluded (Unsupported Extension: '.vcproj')
- `.m4`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 276 LOC)
- `.sh`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpj`: 4x Excluded (Unsupported Extension: '.cpj')
- `.rc`: 4x Excluded (Unsupported Extension: '.rc')
- `.c`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 98.9 | 24.7 | 6.6 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 33.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 19.1 | 2.3 | 0.0 |
| API Exposure | 0.0 | 17.6 | 3.9 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 26.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 95.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.9 | 16.1 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doc/cobcinfo.sh` (Hits: 126)
- `libcob/fileio.c` (Hits: 60)
- `cobc/cobc.c` (Hits: 36)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **config.h.in** (`build_windows/config.h.in`) — 27 inbound connections
2. **libcob.h** (`libcob.h`) — 15 inbound connections
3. **coblocal.h** (`libcob/coblocal.h`) — 11 inbound connections
4. **cobc.h** (`cobc/cobc.h`) — 10 inbound connections
5. **defaults.h.in** (`build_windows/defaults.h.in`) — 9 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **common.c** (`libcob/common.c`) — 48 outbound dependencies
2. **cobc.c** (`cobc/cobc.c`) — 34 outbound dependencies
3. **screenio.c** (`libcob/screenio.c`) — 21 outbound dependencies
4. **call.c** (`libcob/call.c`) — 19 outbound dependencies
5. **fileio.h** (`libcob/fileio.h`) — 19 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `cob_sys_waitpid` (@ `libcob/common.c`) -> Impact: **1759.0** | LOC: 2131
- `process_command_line` (@ `cobc/cobc.c`) -> Impact: **1161.7** | LOC: 2311
  * *Intent:* #endif #ifdef SIGTERM
- `get_dupno` (@ `libcob/flmdb.c`) -> Impact: **763.9** | LOC: 1147
- `print_program_data` (@ `cobc/cobc.c`) -> Impact: **723.9** | LOC: 1107
- `cob_gen_optim` (@ `cobc/codeoptim.c`) -> Impact: **686.5** | LOC: 1532
  * *Intent:* #include <config.h> #include <stdio.h> #include <stdlib.h> #include <stddef.h> #include <stdarg.h> #include <string.h> #include <ctype.h> #include "co...
- `get_suppress_cond` (@ `cobc/tree.c`) -> Impact: **674.6** | LOC: 1104
- `print_program_code` (@ `cobc/cobc.c`) -> Impact: **585.0** | LOC: 1376
- `field_accept` (@ `libcob/screenio.c`) -> Impact: **568.0** | LOC: 1245
- `cb_build_picture` (@ `cobc/tree.c`) -> Impact: **389.3** | LOC: 451
- `cob_set_file_format` (@ `libcob/fileio.c`) -> Impact: **356.6** | LOC: 592

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `libcob` | 31 | 48776.18 | 57.65% | 11.46% |
| `cobc` | 20 | 29208.5 | 42.42% | 25.4% |
| `m4` | 34 | 2940.47 | 7.7% | 24.86% |
| `tests/testsuite.src` | 36 | 2432.92 | 1.24% | 0.0% |
| `bin` | 4 | 1060.82 | 33.21% | 16.57% |
| `tests/cobol85` | 22 | 1008.14 | 6.26% | 0.0% |
| `__monolith__` | 12 | 289.92 | 0.82% | 1.31% |
| `doc` | 2 | 228.7 | 32.41% | 24.67% |
| `extras` | 2 | 196.38 | 33.17% | 10.14% |
| `build_aux` | 3 | 178.32 | 61.5% | 66.67% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `build_aux/mkinstalldirs` -> **100.0%** Exposure
- `m4/extern-inline.m4` -> **100.0%** Exposure
- `m4/printf-posix.m4` -> **100.0%** Exposure
- `m4/wint_t.m4` -> **100.0%** Exposure
- `build_aux/bootstrap` -> **99.9998%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bin/gcdiff.c` -> **100.0%** Exposure
- `cobc/cobc.c` -> **100.0%** Exposure
- `cobc/codeoptim.c` -> **100.0%** Exposure
- `cobc/config.c` -> **100.0%** Exposure
- `cobc/field.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `libcob/common.c` -> **82** Orphaned Functions | **0** Duplicates
- `cobc/tree.c` -> **45** Orphaned Functions | **0** Duplicates
- `cobc/typeck.c` -> **44** Orphaned Functions | **0** Duplicates
- `libcob/intrinsic.c` -> **36** Orphaned Functions | **0** Duplicates
- `libcob/move.c` -> **33** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`bin/gcdiff.c`** -> AI Confidence: **99.48%**
2. **`cobc/config.c`** -> AI Confidence: **99.48%**
3. **`cobc/field.c`** -> AI Confidence: **99.48%**
4. **`libcob/cobgetopt.c`** -> AI Confidence: **99.48%**
5. **`libcob/move.c`** -> AI Confidence: **99.48%**
6. **`libcob/reportio.c`** -> AI Confidence: **99.48%**
7. **`libcob/screenio.c`** -> AI Confidence: **99.48%**
8. **`libcob/termio.c`** -> AI Confidence: **99.48%**
9. **`cobc/cobc.c`** -> AI Confidence: **99.39%**
10. **`cobc/tree.c`** -> AI Confidence: **99.39%**
11. **`libcob/common.c`** -> AI Confidence: **99.39%**
12. **`libcob/mlio.c`** -> AI Confidence: **99.39%**
13. **`libcob/numeric.c`** -> AI Confidence: **99.39%**
14. **`libcob/strings.c`** -> AI Confidence: **99.39%**
15. **`libcob/fileio.c`** -> AI Confidence: **99.34%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `31` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `433` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cobc/tree.c` (C) -> Cumulative Risk: **641.93**
- **Archetype:** `file_cluster_8` (Distance: 14.479 IQR)
- **Magnitude:** 4959.18 | **LOC:** 6804 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (96.373%), Documentation (96.3722%)
- **Heaviest Functions:** `get_suppress_cond` (Impact: 674.6), `cb_build_picture` (Impact: 389.3), `cb_build_intrinsic` (Impact: 259.8)

### 2. `libcob/common.c` (C) -> Cumulative Risk: **611.35**
- **Archetype:** `file_cluster_8` (Distance: 15.24 IQR)
- **Magnitude:** 9000.4 | **LOC:** 8748 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (94.9199%), Safety Score (94.2946%)
- **Heaviest Functions:** `cob_sys_waitpid` (Impact: 1759.0), `check_current_date` (Impact: 165.9), `cob_correct_numeric` (Impact: 144.5)

### 3. `libcob/move.c` (C) -> Cumulative Risk: **598.85**
- **Archetype:** `file_cluster_8` (Distance: 14.461 IQR)
- **Magnitude:** 3518.82 | **LOC:** 2540 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.8076%), Safety Score (97.311%)
- **Heaviest Functions:** `cob_move_display_to_edited` (Impact: 183.0), `cob_move` (Impact: 161.9), `cob_get_s64_pic9` (Impact: 99.6)

### 4. `libcob/flmdb.c` (C) -> Cumulative Risk: **592.16**
- **Archetype:** `file_cluster_8` (Distance: 13.803 IQR)
- **Magnitude:** 2233.34 | **LOC:** 1563 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.5344%), Cognitive Load (96.0891%)
- **Heaviest Functions:** `get_dupno` (Impact: 763.9), `lmdb_read_next` (Impact: 108.8), `lmdb_open` (Impact: 82.8)

### 5. `libcob/fextfh.c` (C) -> Cumulative Risk: **592.06**
- **Archetype:** `file_cluster_8` (Distance: 13.981 IQR)
- **Magnitude:** 1680.72 | **LOC:** 1336 | **CtrlFlow:** 85.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.2885%), Safety Score (97.5907%)
- **Heaviest Functions:** `EXTFH` (Impact: 294.7), `copy_fcd_to_file` (Impact: 63.5), `copy_file_to_fcd` (Impact: 59.0)

### 6. `libcob/screenio.c` (C) -> Cumulative Risk: **591.21**
- **Archetype:** `file_cluster_8` (Distance: 13.828 IQR)
- **Magnitude:** 2702.68 | **LOC:** 3613 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (95.776%), Safety Score (91.8326%)
- **Heaviest Functions:** `field_accept` (Impact: 568.0), `cob_convert_key` (Impact: 132.7), `get_line_and_col_from_field` (Impact: 49.6)

### 7. `libcob/mlio.c` (C) -> Cumulative Risk: **590.64**
- **Archetype:** `file_cluster_13` (Distance: 13.35 IQR)
- **Magnitude:** 477.34 | **LOC:** 937 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.5687%), Documentation (88.804%)
- **Heaviest Functions:** `cob_xml_generate` (Impact: 42.6), `cob_is_valid_uri` (Impact: 26.0), `generate_json_from_tree` (Impact: 20.8)

### 8. `libcob/fsqlxfd.c` (C) -> Cumulative Risk: **587.79**
- **Archetype:** `file_cluster_8` (Distance: 14.856 IQR)
- **Magnitude:** 4856.6 | **LOC:** 2449 | **CtrlFlow:** 88.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.6646%), Documentation (98.4261%)
- **Heaviest Functions:** `cob_sql_stmt` (Impact: 333.7), `convert_to_date` (Impact: 217.7), `cob_load_xfd` (Impact: 128.9)

### 9. `libcob/numeric.c` (C) -> Cumulative Risk: **587.74**
- **Archetype:** `file_cluster_8` (Distance: 13.899 IQR)
- **Magnitude:** 2494.08 | **LOC:** 2689 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.0917%), Documentation (92.0312%)
- **Heaviest Functions:** `cob_decimal_get_binary` (Impact: 46.1), `cob_get_long_ebcdic_sign` (Impact: 41.4), `cob_cmp_numdisp` (Impact: 40.2)

### 10. `cobc/field.c` (C) -> Cumulative Risk: **585.96**
- **Archetype:** `file_cluster_8` (Distance: 13.78 IQR)
- **Magnitude:** 3374.52 | **LOC:** 3249 | **CtrlFlow:** 78.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (94.0488%), Safety Score (93.7677%)
- **Heaviest Functions:** `validate_pic` (Impact: 238.0), `validate_elementary_item` (Impact: 175.5), `create_implicit_picture` (Impact: 142.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `libcob/common.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.24 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.0 IQR)
- **Top Global Matches:** file_cluster_8: 15.24, file_cluster_13: 15.348, file_cluster_11: 15.406
- **Magnitude:** 9000.4 | **LOC:** 8748 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.9199%), Tech Debt (37.2586%)
**Top Internal Functions/Classes:**
  * `cob_sys_waitpid` (Impact: 1759.0)
  * `check_current_date` (Impact: 165.9)
  * `cob_correct_numeric` (Impact: 144.5)
    * *Intent:* /* * Copy the returning 'cob_field' and return address of the copy * This is done to avoid passing b...
  * `cob_check_numdisp` (Impact: 72.7)
    * *Intent:* *p = '4';
  * `cob_exit_common` (Impact: 57.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2151`, `structural_boundaries: 750`, `args: 151`, `func_start: 188`, `class_start: 50`
* *Risk/State:* `safety_bypasses: 96`, `high_risk_execution: 2`, `state_mutation: 4423`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 4`, `orphaned_logic: 82`
* *Architecture:* `io: 30`, `api: 735`, `import: 49`
* *Defense:* `safety: 195`, `doc: 2`, `immutability_locks: 205`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` curses.h, gmp.h, curses.h, sysdefines.h, errno.h, unistd.h, sqlext.h, xmlwriter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/cobc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.016 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.164 IQR)
- **Top Global Matches:** file_cluster_8: 15.016, file_cluster_13: 15.1, file_cluster_11: 15.139
- **Magnitude:** 8995.02 | **LOC:** 8434 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.7737%), Tech Debt (16.0281%)
**Top Internal Functions/Classes:**
  * `process_command_line` (Impact: 1161.7)
    * *Intent:* #endif #ifdef SIGTERM
  * `print_program_data` (Impact: 723.9)
  * `print_program_code` (Impact: 585.0)
  * `process` (Impact: 153.2)
  * `main` (Impact: 109.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1314`, `structural_boundaries: 417`, `args: 107`, `func_start: 116`, `class_start: 64`
* *Risk/State:* `safety_bypasses: 187`, `high_risk_execution: 3`, `state_mutation: 3468`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 7`, `orphaned_logic: 16`
* *Architecture:* `io: 36`, `api: 492`, `import: 33`
* *Defense:* `safety: 150`, `doc: 1`, `immutability_locks: 136`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` direct.h, unistd.h, sqlext.h, flag.def, cobgetopt.h, windows.h, sql.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fileio.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.676 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.592 IQR)
- **Top Global Matches:** file_cluster_8: 14.676, file_cluster_0: 14.916, file_cluster_11: 14.916
- **Magnitude:** 5430.9 | **LOC:** 7364 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.9126%), Tech Debt (16.8774%)
**Top Internal Functions/Classes:**
  * `cob_set_file_format` (Impact: 356.6)
  * `cob_file_save_status` (Impact: 98.0)
  * `cob_set_file_defaults` (Impact: 76.0)
  * `lineseq_write` (Impact: 68.0)
  * `lineseq_rewrite` (Impact: 63.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1484`, `structural_boundaries: 317`, `args: 6`, `func_start: 62`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 110`, `state_mutation: 3061`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 21`
* *Architecture:* `io: 60`, `api: 532`, `import: 5`
* *Defense:* `safety: 75`, `immutability_locks: 83`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` defaults.h, fileio.h, dlfcn.h, signal.h, wait.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/tree.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.479 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.018 IQR)
- **Top Global Matches:** file_cluster_8: 14.479, file_cluster_13: 14.671, file_cluster_11: 14.673
- **Magnitude:** 4959.18 | **LOC:** 6804 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.373%), Tech Debt (60.3589%)
**Top Internal Functions/Classes:**
  * `get_suppress_cond` (Impact: 674.6)
  * `cb_build_picture` (Impact: 389.3)
  * `cb_build_intrinsic` (Impact: 259.8)
  * `cb_name_1` (Impact: 174.9)
  * `get_category_from_arguments` (Impact: 49.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1003`, `structural_boundaries: 368`, `args: 40`, `func_start: 81`, `class_start: 78`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 2146`, `planned_debt: 7`, `fragile_debt: 6`, `orphaned_logic: 45`
* *Architecture:* `api: 595`, `import: 10`
* *Defense:* `safety: 72`, `immutability_locks: 139`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cobc.h, tree.h, limits.h, parser.h, stdio.h, stdlib.h, ctype.h, stddef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fsqlxfd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.856 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.42 IQR)
- **Top Global Matches:** file_cluster_8: 14.856, file_cluster_13: 15.12, file_cluster_11: 15.124
- **Magnitude:** 4856.6 | **LOC:** 2449 | **CtrlFlow:** 88.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.1813%), Tech Debt (12.8783%)
**Top Internal Functions/Classes:**
  * `cob_sql_stmt` (Impact: 333.7)
  * `convert_to_date` (Impact: 217.7)
  * `cob_load_xfd` (Impact: 128.9)
  * `bld_fields` (Impact: 113.4)
  * `convert_from_date` (Impact: 108.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 906`, `structural_boundaries: 120`, `args: 32`, `func_start: 37`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 115`, `state_mutation: 2608`, `orphaned_logic: 13`
* *Architecture:* `io: 8`, `api: 297`, `import: 2`
* *Defense:* `safety: 12`, `doc: 2`, `immutability_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` defaults.h, fileio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/move.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.461 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.009 IQR)
- **Top Global Matches:** file_cluster_8: 14.461, file_cluster_13: 14.635, file_cluster_0: 14.692
- **Magnitude:** 3518.82 | **LOC:** 2540 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.8302%), Tech Debt (26.4078%)
**Top Internal Functions/Classes:**
  * `cob_move_display_to_edited` (Impact: 183.0)
  * `cob_move` (Impact: 161.9)
  * `cob_get_s64_pic9` (Impact: 99.6)
  * `cob_get_s64_compx` (Impact: 50.0)
  * `cob_get_u64_compx` (Impact: 46.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 805`, `structural_boundaries: 216`, `args: 19`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 1905`, `orphaned_logic: 33`
* *Architecture:* `api: 462`, `import: 11`
* *Defense:* `safety: 56`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` stdio.h, errno.h, coblocal.h, stdlib.h, ctype.h, stddef.h, math.h, locale.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/field.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.78 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.642 IQR)
- **Top Global Matches:** file_cluster_8: 13.78, file_cluster_13: 14.009, file_cluster_11: 14.085
- **Magnitude:** 3374.52 | **LOC:** 3249 | **CtrlFlow:** 78.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.6786%), Tech Debt (16.5467%)
**Top Internal Functions/Classes:**
  * `validate_pic` (Impact: 238.0)
  * `validate_elementary_item` (Impact: 175.5)
  * `create_implicit_picture` (Impact: 142.8)
  * `cb_eval_op` (Impact: 110.8)
  * `cb_get_usage_string` (Impact: 107.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 814`, `structural_boundaries: 221`, `args: 46`, `func_start: 52`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1161`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `api: 260`, `import: 9`
* *Defense:* `safety: 2`, `immutability_locks: 83`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cobc.h, tree.h, limits.h, stdio.h, stdlib.h, ctype.h, stddef.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/typeck.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.259 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.479 IQR)
- **Top Global Matches:** file_cluster_8: 13.259, file_cluster_13: 13.601, file_cluster_7: 13.652
- **Magnitude:** 2957.06 | **LOC:** 13270 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.2029%), Tech Debt (59.6616%)
**Top Internal Functions/Classes:**
  * `cb_is_integer_field` (Impact: 76.1)
  * `cb_build_length` (Impact: 59.6)
  * `cb_emit_write` (Impact: 56.4)
  * `cb_build_register_when_compiled` (Impact: 53.9)
  * `cb_check_field_debug` (Impact: 51.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 784`, `structural_boundaries: 395`, `args: 30`, `func_start: 95`, `class_start: 53`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 1315`, `planned_debt: 14`, `fragile_debt: 4`, `orphaned_logic: 44`
* *Architecture:* `api: 359`, `import: 14`
* *Defense:* `safety: 20`, `doc: 1`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` cobc.h, tree.h, limits.h, stdio.h, system.def, stdlib.h, ctype.h, stddef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/codeoptim.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.928 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.805 IQR)
- **Top Global Matches:** file_cluster_8: 13.928, file_cluster_13: 14.264, file_cluster_7: 14.315
- **Magnitude:** 2750.42 | **LOC:** 2767 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.4273%), Tech Debt (8.028%)
**Top Internal Functions/Classes:**
  * `cob_gen_optim` (Impact: 686.5)
    * *Intent:* #include <config.h> #include <stdio.h> #include <stdlib.h> #include <stddef.h> #include <stdarg.h> #...
  * `output_storage` (Impact: 4.1)
    * *Intent:* */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 467`, `args: 135`, `func_start: 2`
* *Risk/State:* `state_mutation: 1870`, `orphaned_logic: 1`
* *Architecture:* `api: 141`, `import: 9`
* *Defense:* `safety: 3`, `immutability_locks: 210`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cobc.h, tree.h, stdio.h, stdarg.h, stdlib.h, ctype.h, stddef.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/screenio.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.828 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.512 IQR)
- **Top Global Matches:** file_cluster_8: 13.828, file_cluster_13: 14.0, file_cluster_11: 14.142
- **Magnitude:** 2702.68 | **LOC:** 3613 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.776%), Tech Debt (22.4366%)
**Top Internal Functions/Classes:**
  * `field_accept` (Impact: 568.0)
  * `cob_convert_key` (Impact: 132.7)
  * `get_line_and_col_from_field` (Impact: 49.6)
  * `cob_screen_init` (Impact: 44.6)
    * *Intent:* #endif
  * `cob_settings_screenio` (Impact: 38.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 590`, `structural_boundaries: 132`, `args: 33`, `func_start: 58`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1157`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`, `orphaned_logic: 12`
* *Architecture:* `io: 1`, `api: 268`, `import: 21`
* *Defense:* `safety: 21`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` curses.h, sysdefines.h, curses.h, errno.h, unistd.h, libcob.h, ncurses.h, coblocal.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/numeric.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.899 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.191 IQR)
- **Top Global Matches:** file_cluster_8: 13.899, file_cluster_13: 14.171, file_cluster_0: 14.272
- **Magnitude:** 2494.08 | **LOC:** 2689 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.5136%), Tech Debt (38.2871%)
**Top Internal Functions/Classes:**
  * `cob_decimal_get_binary` (Impact: 46.1)
  * `cob_get_long_ebcdic_sign` (Impact: 41.4)
  * `cob_cmp_numdisp` (Impact: 40.2)
    * *Intent:* *val += 1;
  * `cob_add_packed` (Impact: 39.4)
  * `cob_decimal_do_round` (Impact: 39.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 566`, `structural_boundaries: 225`, `args: 10`, `func_start: 75`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1353`, `fragile_debt: 3`, `orphaned_logic: 26`
* *Architecture:* `api: 267`, `import: 14`
* *Defense:* `safety: 43`, `doc: 2`, `immutability_locks: 63`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` gmp.h, ieeefp.h, stdio.h, errno.h, stdarg.h, mpir.h, coblocal.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/call.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.022 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.044 IQR)
- **Top Global Matches:** file_cluster_8: 14.022, file_cluster_13: 14.164, file_cluster_0: 14.296
- **Magnitude:** 2451.92 | **LOC:** 2319 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.082%), Tech Debt (15.1678%)
**Top Internal Functions/Classes:**
  * `cob_resolve_internal` (Impact: 83.0)
  * `cob_set_library_path` (Impact: 48.3)
  * `cob_call` (Impact: 45.8)
  * `cob_exit_call` (Impact: 44.7)
  * `cache_preload` (Impact: 40.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 290`, `args: 52`, `func_start: 59`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 2`, `state_mutation: 1240`, `orphaned_logic: 15`
* *Architecture:* `io: 7`, `api: 295`, `import: 19`
* *Defense:* `safety: 44`, `doc: 7`, `immutability_locks: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` sysdefines.h, errno.h, unistd.h, libcob.h, coblocal.h, windows.h, string.h, system.def...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fodbc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.847 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.267 IQR)
- **Top Global Matches:** file_cluster_8: 13.847, file_cluster_13: 14.143, file_cluster_7: 14.189
- **Magnitude:** 2306.46 | **LOC:** 1871 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.2543%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `chkSts` (Impact: 144.9)
  * `join_environment` (Impact: 86.2)
  * `getOdbcMsg` (Impact: 67.3)
  * `odbc_open` (Impact: 64.8)
  * `chkOdbc` (Impact: 56.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 460`, `structural_boundaries: 189`, `args: 12`, `func_start: 30`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 1255`
* *Architecture:* `api: 215`, `import: 6`
* *Defense:* `safety: 9`, `doc: 4`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fileio.h, sqlext.h, sqludf.h, sqlcli1.h, sql.h, sqlca.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/flmdb.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.803 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.819 IQR)
- **Top Global Matches:** file_cluster_8: 13.803, file_cluster_11: 13.969, file_cluster_13: 14.015
- **Magnitude:** 2233.34 | **LOC:** 1563 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.0891%), Tech Debt (13.3418%)
**Top Internal Functions/Classes:**
  * `get_dupno` (Impact: 763.9)
  * `lmdb_read_next` (Impact: 108.8)
    * *Intent:* /* START INDEXED file with positioning */
  * `lmdb_open` (Impact: 82.8)
  * `lmdb_start_internal` (Impact: 55.6)
  * `mdb_cob_status` (Impact: 55.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 142`, `args: 18`, `func_start: 41`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 735`, `planned_debt: 15`
* *Architecture:* `io: 6`, `api: 225`, `import: 6`
* *Defense:* `safety: 28`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stat.h, fileio.h, file.h, libgen.h, sysmacros.h, lmdb.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/foci.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.775 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.847 IQR)
- **Top Global Matches:** file_cluster_8: 13.775, file_cluster_13: 14.099, file_cluster_7: 14.121
- **Magnitude:** 1955.62 | **LOC:** 1664 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.2174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `chkSts` (Impact: 108.2)
  * `oci_open` (Impact: 62.8)
  * `join_environment` (Impact: 56.4)
  * `oci_setup_stmt` (Impact: 55.0)
  * `oci_read_next` (Impact: 50.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 386`, `structural_boundaries: 167`, `args: 11`, `func_start: 30`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 1093`
* *Architecture:* `api: 182`, `import: 2`
* *Defense:* `safety: 18`, `doc: 4`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` oci.h, fileio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fisam.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.025 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.785 IQR)
- **Top Global Matches:** file_cluster_8: 14.025, file_cluster_13: 14.292, file_cluster_0: 14.369
- **Magnitude:** 1901.06 | **LOC:** 1670 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.4069%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isam_read_next` (Impact: 125.2)
  * `isam_open` (Impact: 115.5)
  * `fisretsts` (Impact: 53.5)
  * `isam_rewrite` (Impact: 39.1)
  * `isam_start` (Impact: 31.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 470`, `structural_boundaries: 198`, `args: 8`, `func_start: 26`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 1089`
* *Architecture:* `io: 2`, `api: 179`, `import: 5`
* *Defense:* `safety: 14`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.093
  * `Choke Point (Betweenness):` 0.000476 | `Ripple Effect (Closeness):` 0.015385
  * `Imports (Out-Degree: 1):` isconfig.h, fileio.h, isam.h, disam.h, vbisam.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `libcob/reportio.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.667 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.018 IQR)
- **Top Global Matches:** file_cluster_8: 13.667, file_cluster_13: 13.986, file_cluster_7: 14.051
- **Magnitude:** 1801.28 | **LOC:** 1836 | **CtrlFlow:** 85.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.0014%), Tech Debt (14.9926%)
**Top Internal Functions/Classes:**
  * `cob_report_generate` (Impact: 108.0)
  * `dumpFlags` (Impact: 78.7)
  * `report_line` (Impact: 73.5)
  * `reportDumpOneLine` (Impact: 59.4)
  * `cob_report_terminate` (Impact: 55.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 525`, `structural_boundaries: 88`, `args: 1`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 971`, `planned_debt: 3`, `orphaned_logic: 6`
* *Architecture:* `io: 2`, `api: 118`, `import: 9`
* *Defense:* `safety: 6`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` stdio.h, errno.h, coblocal.h, stdlib.h, ctype.h, stddef.h, libcob.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fbdb.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.75 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.632 IQR)
- **Top Global Matches:** file_cluster_8: 13.75, file_cluster_13: 14.054, file_cluster_0: 14.078
- **Magnitude:** 1722.76 | **LOC:** 2009 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.5214%), Tech Debt (12.7371%)
**Top Internal Functions/Classes:**
  * `ix_bdb_open` (Impact: 261.1)
  * `ix_bdb_read_next` (Impact: 115.7)
  * `bdb_lock_record` (Impact: 37.8)
  * `bdb_nofile` (Impact: 35.5)
  * `bdb_test_record_lock` (Impact: 35.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 404`, `structural_boundaries: 122`, `args: 1`, `func_start: 30`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 833`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 8`, `api: 154`, `import: 2`
* *Defense:* `safety: 31`, `immutability_locks: 24`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` db.h, fileio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fextfh.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.981 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.06 IQR)
- **Top Global Matches:** file_cluster_8: 13.981, file_cluster_13: 14.303, file_cluster_7: 14.313
- **Magnitude:** 1680.72 | **LOC:** 1336 | **CtrlFlow:** 85.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.8318%), Tech Debt (15.3912%)
**Top Internal Functions/Classes:**
  * `EXTFH` (Impact: 294.7)
  * `copy_fcd_to_file` (Impact: 63.5)
  * `copy_file_to_fcd` (Impact: 59.0)
  * `update_fcd_to_file` (Impact: 30.1)
  * `update_file_to_fcd` (Impact: 27.6)
    * *Intent:* /* * Free up allocated memory
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 69`, `args: 11`, `func_start: 15`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 917`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 192`, `import: 1`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fileio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/intrinsic.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.058 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.115 IQR)
- **Top Global Matches:** file_cluster_8: 13.058, file_cluster_13: 13.299, file_cluster_7: 13.47
- **Magnitude:** 1190.66 | **LOC:** 6809 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.63%), Tech Debt (73.9771%)
**Top Internal Functions/Classes:**
  * `cob_check_numval_f` (Impact: 77.8)
  * `numval` (Impact: 36.3)
    * *Intent:* /* NUMVAL */
  * `cob_alloc_field` (Impact: 13.8)
  * `get_interval_and_current_year_from_args` (Impact: 12.4)
    * *Intent:* /* Get the sum of the squares of the differences from the mean */
  * `cob_mpf_sin` (Impact: 11.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 114`, `args: 29`, `func_start: 53`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 610`, `fragile_debt: 1`, `orphaned_logic: 36`
* *Architecture:* `api: 180`, `import: 19`
* *Defense:* `safety: 43`, `immutability_locks: 91`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` gmp.h, errno.h, timeb.h, libcob.h, coblocal.h, math.h, windows.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/debug.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.85 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.018 IQR)
- **Top Global Matches:** file_cluster_8: 12.85, file_cluster_13: 13.109, file_cluster_7: 13.236
- **Magnitude:** 1109.94 | **LOC:** 1579 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.9757%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cb_tree_print` (Impact: 120.3)
  * `cb_tag_str` (Impact: 92.7)
    * *Intent:* #include "config.h" #include "defaults.h" #include "cobc/cobc.h" #include "libcob/common.h" #include...
  * `cb_category_str` (Impact: 37.9)
  * `print_program` (Impact: 21.6)
  * `print_file` (Impact: 13.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 159`, `args: 35`, `func_start: 34`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 494`
* *Architecture:* `io: 1`, `api: 144`, `import: 18`
* *Defense:* `safety: 5`, `doc: 4`, `test: 2`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` string.h, defaults.h, time.h, tree.h, stat.h, vis.h, stdio.h, stdarg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/scanner.l` (YACC | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.752 IQR)
- **Top Global Matches:** file_cluster_8: 12.752, file_cluster_7: 13.2, file_cluster_13: 13.245
- **Magnitude:** 1067.84 | **LOC:** 2489 | **CtrlFlow:** 87.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.1288%), Tech Debt (45.272%)
**Top Internal Functions/Classes:**
  * `error` (Impact: 66.0)
    * *Intent:* */
  * `error` (Impact: 21.6)
  * `error` (Impact: 19.1)
  * `error` (Impact: 8.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 294`, `structural_boundaries: 43`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 922`, `planned_debt: 4`, `fragile_debt: 7`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `import: 7`
* *Defense:* `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `m4/ltsugar.m4` (M4 | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.646 IQR)
- **Top Global Matches:** file_cluster_8: 9.646, file_cluster_7: 10.497, file_cluster_17: 10.544
- **Magnitude:** 1031.95 | **LOC:** 125 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.7458%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `args: 69`, `func_start: 14`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/pplex.l` (YACC | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.659 IQR)
- **Top Global Matches:** file_cluster_8: 12.659, file_cluster_13: 13.201, file_cluster_7: 13.234
- **Magnitude:** 1002.06 | **LOC:** 2165 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.84%), Tech Debt (13.0192%)
**Top Internal Functions/Classes:**
  * `err_handling` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 345`, `structural_boundaries: 181`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 968`, `planned_debt: 2`, `fragile_debt: 5`
* *Architecture:* `io: 13`, `import: 9`
* *Defense:* `immutability_locks: 38`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/config.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.904 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.715 IQR)
- **Top Global Matches:** file_cluster_13: 13.904, file_cluster_11: 14.0, file_cluster_8: 14.066
- **Magnitude:** 974.24 | **LOC:** 818 | **CtrlFlow:** 78.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.5754%), Tech Debt (14.696%)
**Top Internal Functions/Classes:**
  * `cb_config_entry` (Impact: 299.9)
  * `cb_load_conf_file` (Impact: 51.7)
  * `cb_load_conf` (Impact: 27.0)
  * `invalid_value` (Impact: 26.3)
  * `cb_read_conf` (Impact: 17.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 63`, `args: 12`, `func_start: 10`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 6`, `state_mutation: 445`, `dead_code: 3`, `orphaned_logic: 4`
* *Architecture:* `io: 4`, `api: 62`, `import: 12`
* *Defense:* `safety: 14`, `immutability_locks: 47`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` defaults.h, cobc.h, tree.h, limits.h, stdio.h, config.def, stdlib.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/cobol85/report.pl` (PERL) | Magnitude: 588.14 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 558, indent_tabs: 302, branch: 144, structural_boundaries: 76
- `extras/CBL_OC_DUMP.cob` (COBOL) | Magnitude: 195.38 | Delta: **0.456 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 199, state_mutation: 60, structural_boundaries: 55, branch: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/run_prog_manual.sh.in` (SHELL) | Magnitude: 51.44 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, io: 25, branch: 24, safety_bypasses: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/cobol85/summary.pl` (PERL) | Magnitude: 180.14 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 164, indent_tabs: 26, structural_boundaries: 21, encapsulation: 19
- `cobc/config.c` (C) | Magnitude: 974.24 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 482, state_mutation: 445, branch: 232, pointers: 94
- `libcob/mlio.c` (C) | Magnitude: 477.34 | Delta: **0.138 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 277, state_mutation: 243, branch: 110, pointers: 101
- `libcob/cobgetopt.c` (C) | Magnitude: 72.3 | Delta: **0.393 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 46, macros: 14, branch: 13, api: 10
- `bin/cobcrun.c` (C) | Magnitude: 40.72 | Delta: **0.419 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 47, debug_prints: 21, state_mutation: 20, import: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `m4/extern-inline.m4` (M4) | Magnitude: 16.12 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 51, dead_code: 16, fragile_debt: 6, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `bin/gcdiff.c` (C) | Magnitude: 928.36 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 562, state_mutation: 527, branch: 216, debug_prints: 83
- `copy/xfhfcd.cpy` (COBOL) | Magnitude: 0.53 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 1, indent_spaces: 1
- `libcob/strings.c` (C) | Magnitude: 730.2 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 459, indent_tabs: 395, pointers: 166, branch: 115
- `libcob/termio.c` (C) | Magnitude: 927.56 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 521, state_mutation: 484, branch: 215, pointers: 195
- `cobc/cobc.c` (C) | Magnitude: 8995.02 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 3886, state_mutation: 3468, branch: 1314, pointers: 1022

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `m4/intl.m4` (M4) | Magnitude: 20.2 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 128, dead_code: 42, structural_boundaries: 32, dependency_injection: 32
- `build_aux/bootstrap` (SHELL) | Magnitude: 56.06 | Delta: **0.193 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: branch: 26, indent_spaces: 23, safety_bypasses: 22, state_mutation: 21

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `libcob/fisam.c` -> **Severity: 0.048** (Bridge: 0.0005 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `libcob/coblocal.h` -> **Severity: 4.534** (Embedded: 0.0714 * Error Risk: 63.5099%)
- `libcob/common.h` -> **Severity: 4.421** (Embedded: 0.0756 * Error Risk: 58.5025%)
- `libcob/fileio.h` -> **Severity: 2.574** (Embedded: 0.0492 * Error Risk: 52.2885%)
- `cobc/cobc.h` -> **Severity: 2.288** (Embedded: 0.0513 * Error Risk: 44.6256%)
- `libcob/sysdefines.h` -> **Severity: 2.276** (Embedded: 0.0423 * Error Risk: 53.743%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `libcob/fileio.h` -> **Severity: 3550.7** (Blast Radius: 35.507 * Doc Risk: 100.0%)
- `libcob/common.h` -> **Severity: 2666.292** (Blast Radius: 27.112 * Doc Risk: 98.3436%)
- `libcob/coblocal.h` -> **Severity: 2137.0** (Blast Radius: 21.37 * Doc Risk: 100.0%)
- `cobc/cobc.h` -> **Severity: 1292.4** (Blast Radius: 12.924 * Doc Risk: 100.0%)
- `cobc/tree.h` -> **Severity: 1224.4** (Blast Radius: 12.244 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
