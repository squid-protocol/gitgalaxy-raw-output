# ARCHITECTURAL_BRIEF: ncdu
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_zig/ncdu` |
| **Timestamp** | `2026-08-07T04:29:31.501222+00:00` |
| **Scan Duration** | `0.16s` |
| **Git Branch** | `master` |
| **Git Commit** | `a216bc2d35b6edf4dadf55350f09d7cbf229fbf7` |
| **Git Remote** | `https://github.com/rofl0r/ncdu.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 27 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 89.9 | 48.1 | 73.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 54.2 | 78.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 33.8 | 24.2 | 0.0 |
| Testing Exposure | 0.8 | 80.0 | 29.8 | 2.5 | 80.0 |
| API Exposure | 0.0 | 12.6 | 7.7 | 7.8 | 7.6 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 60.3 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 33.3 | 100.0 | 86.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.9 | 57.7 | 55.6 | 38.0 |
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

- `browse_key` (@ `src/browser.c`) -> Impact: **245.1** | LOC: 225
- `cons` (@ `src/dir_import.c`) -> Impact: **157.4** | LOC: 319
- `delete_key` (@ `src/delete.c`) -> Impact: **65.2** | LOC: 56
- `help_key` (@ `src/help.c`) -> Impact: **52.1** | LOC: 38
- `dirlist_cmp` (@ `src/dirlist.c`) -> Impact: **48.8** | LOC: 40
- `output_string` (@ `src/dir_export.c`) -> Impact: **45.0** | LOC: 19
- `rval` (@ `src/dir_import.c`) -> Impact: **44.9** | LOC: 50
- `dirlist_sort` (@ `src/dirlist.c`) -> Impact: **42.3** | LOC: 46
  * *Intent:* /* sort columns: * 1 -> 2 -> 3 -> 4 * NAME: name -> size -> asize -> items * SIZE: size -> asize -> name -> items * ASIZE: asize -> size -> name -> it...
- `delete_dir` (@ `src/delete.c`) -> Impact: **42.1** | LOC: 43
- `iteminfo` (@ `src/dir_import.c`) -> Impact: **41.0** | LOC: 112

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 26 | 4091.52 | 51.3% | 35.66% |
| `doc` | 1 | 49.46 | 13.09% | 18.35% |
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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `113` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/util.c` (C) -> Cumulative Risk: **662.92**
- **Archetype:** `file_cluster_13` (Distance: 14.156 IQR)
- **Magnitude:** 579.48 | **LOC:** 435 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.6408%), Safety Score (99.3618%)
- **Heaviest Functions:** `fmtmode` (Impact: 37.1), `formatsize` (Impact: 28.1), `getpath` (Impact: 19.9)

### 2. `src/dir_common.c` (C) -> Cumulative Risk: **640.38**
- **Archetype:** `file_cluster_13` (Distance: 12.138 IQR)
- **Magnitude:** 212.96 | **LOC:** 233 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (96.228%), Safety Score (92.2898%)
- **Heaviest Functions:** `draw_progress` (Impact: 24.0), `dir_key` (Impact: 20.0), `dir_draw` (Impact: 16.4)

### 3. `src/dir_export.c` (C) -> Cumulative Risk: **612.65**
- **Archetype:** `file_cluster_13` (Distance: 11.776 IQR)
- **Magnitude:** 161.64 | **LOC:** 195 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (87.7675%), Cognitive Load (86.9541%)
- **Heaviest Functions:** `output_string` (Impact: 45.0), `output_info` (Impact: 23.1), `item` (Impact: 15.6)

### 4. `src/delete.c` (C) -> Cumulative Risk: **607.25**
- **Archetype:** `file_cluster_8` (Distance: 12.127 IQR)
- **Magnitude:** 273.06 | **LOC:** 254 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (91.6588%), Safety Score (90.369%)
- **Heaviest Functions:** `delete_key` (Impact: 65.2), `delete_dir` (Impact: 42.1), `delete_draw_confirm` (Impact: 16.7)

### 5. `src/exclude.c` (C) -> Cumulative Risk: **579.9**
- **Archetype:** `file_cluster_13` (Distance: 13.295 IQR)
- **Magnitude:** 145.24 | **LOC:** 139 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.3328%), Safety Score (97.6757%)
- **Heaviest Functions:** `exclude_addfile` (Impact: 14.9), `has_cachedir_tag` (Impact: 13.4), `exclude_match` (Impact: 12.8)

### 6. `src/browser.c` (C) -> Cumulative Risk: **576.21**
- **Archetype:** `file_cluster_8` (Distance: 12.908 IQR)
- **Magnitude:** 775.98 | **LOC:** 568 | **CtrlFlow:** 87.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.3085%), Cognitive Load (88.7122%)
- **Heaviest Functions:** `browse_key` (Impact: 245.1), `browse_draw_info` (Impact: 39.6), `browse_draw_graph` (Impact: 38.2)

### 7. `src/help.c` (C) -> Cumulative Risk: **561.8**
- **Archetype:** `file_cluster_8` (Distance: 11.337 IQR)
- **Magnitude:** 159.16 | **LOC:** 213 | **CtrlFlow:** 93.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (87.7311%), Verification (80.0%)
- **Heaviest Functions:** `help_key` (Impact: 52.1), `help_draw` (Impact: 16.6), `help_init` (Impact: 1.2)

### 8. `src/dirlist.c` (C) -> Cumulative Risk: **549.03**
- **Archetype:** `file_cluster_13` (Distance: 14.078 IQR)
- **Magnitude:** 412.48 | **LOC:** 399 | **CtrlFlow:** 77.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.6285%), Cognitive Load (89.9159%)
- **Heaviest Functions:** `dirlist_cmp` (Impact: 48.8), `dirlist_sort` (Impact: 42.3), `dirlist_fixup` (Impact: 36.0)

### 9. `src/path.c` (C) -> Cumulative Risk: **532.42**
- **Archetype:** `file_cluster_13` (Distance: 13.228 IQR)
- **Magnitude:** 174.66 | **LOC:** 247 | **CtrlFlow:** 81.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.8189%), Cognitive Load (88.6779%)
- **Heaviest Functions:** `path_split` (Impact: 27.9), `path_chdir` (Impact: 15.0), `path_real` (Impact: 6.7)

### 10. `src/shell.c` (C) -> Cumulative Risk: **531.9**
- **Archetype:** `file_cluster_13` (Distance: 11.28 IQR)
- **Magnitude:** 41.1 | **LOC:** 83 | **CtrlFlow:** 81.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (95.5022%), Safety Score (91.3239%)
- **Heaviest Functions:** `shell_draw` (Impact: 12.1), `shell_init` (Impact: 1.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/browser.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.908 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.27 IQR)
- **Top Global Matches:** file_cluster_8: 12.908, file_cluster_13: 13.112, file_cluster_7: 13.305
- **Magnitude:** 775.98 | **LOC:** 568 | **CtrlFlow:** 87.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.7122%), Tech Debt (15.0706%)
**Top Internal Functions/Classes:**
  * `browse_key` (Impact: 245.1)
  * `browse_draw_info` (Impact: 39.6)
  * `browse_draw_graph` (Impact: 38.2)
  * `browse_draw_flag` (Impact: 25.1)
  * `browse_draw` (Impact: 22.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 33`, `args: 9`, `func_start: 9`, `class_start: 10`
* *Risk/State:* `state_mutation: 294`, `orphaned_logic: 3`
* *Architecture:* `io: 3`, `api: 44`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, string.h, time.h, stdlib.h, ncurses.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/util.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.156 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.198 IQR)
- **Top Global Matches:** file_cluster_13: 14.156, file_cluster_8: 14.326, file_cluster_11: 14.366
- **Magnitude:** 579.48 | **LOC:** 435 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.9695%), Tech Debt (91.2033%)
**Top Internal Functions/Classes:**
  * `fmtmode` (Impact: 37.1)
  * `formatsize` (Impact: 28.1)
  * `getpath` (Impact: 19.9)
  * `ncresize` (Impact: 13.4)
  * `addparentstats` (Impact: 10.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 38`, `args: 13`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 336`, `orphaned_logic: 13`
* *Architecture:* `io: 2`, `api: 62`, `import: 7`
* *Defense:* `safety: 6`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string.h, stdlib.h, locale.h, util.h, unistd.h, ncurses.h, stdarg.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_import.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.786 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.108 IQR)
- **Top Global Matches:** file_cluster_8: 11.786, file_cluster_13: 11.94, file_cluster_7: 12.242
- **Magnitude:** 465.78 | **LOC:** 616 | **CtrlFlow:** 76.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.7011%), Tech Debt (25.3592%)
**Top Internal Functions/Classes:**
  * `cons` (Impact: 157.4)
  * `rval` (Impact: 44.9)
  * `iteminfo` (Impact: 41.0)
  * `item` (Impact: 21.3)
  * `rnum` (Impact: 17.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 30`, `args: 12`, `func_start: 14`
* *Risk/State:* `state_mutation: 86`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 14`, `import: 6`
* *Defense:* `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, string.h, stdlib.h, errno.h, stdio.h, limits.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dirlist.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.078 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.943 IQR)
- **Top Global Matches:** file_cluster_13: 14.078, file_cluster_8: 14.096, file_cluster_11: 14.303
- **Magnitude:** 412.48 | **LOC:** 399 | **CtrlFlow:** 77.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.9159%), Tech Debt (30.5308%)
**Top Internal Functions/Classes:**
  * `dirlist_cmp` (Impact: 48.8)
  * `dirlist_sort` (Impact: 42.3)
    * *Intent:* /* sort columns: * 1 -> 2 -> 3 -> 4 * NAME: name -> size -> asize -> items * SIZE: size -> asize -> ...
  * `dirlist_fixup` (Impact: 36.0)
  * `dirlist_top` (Impact: 31.4)
  * `dirlist_set_sort` (Impact: 14.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 22`, `args: 7`, `func_start: 7`, `class_start: 5`
* *Risk/State:* `state_mutation: 206`, `orphaned_logic: 2`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdlib.h, global.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/delete.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.127 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.091 IQR)
- **Top Global Matches:** file_cluster_8: 12.127, file_cluster_13: 12.237, file_cluster_7: 12.582
- **Magnitude:** 273.06 | **LOC:** 254 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.6416%), Tech Debt (48.9756%)
**Top Internal Functions/Classes:**
  * `delete_key` (Impact: 65.2)
  * `delete_dir` (Impact: 42.1)
  * `delete_draw_confirm` (Impact: 16.7)
  * `delete_process` (Impact: 10.6)
  * `delete_draw` (Impact: 8.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 28`, `args: 6`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 97`, `orphaned_logic: 4`
* *Architecture:* `api: 19`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unistd.h, global.h, string.h, errno.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_common.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.138 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.362 IQR)
- **Top Global Matches:** file_cluster_13: 12.138, file_cluster_8: 12.214, file_cluster_0: 12.462
- **Magnitude:** 212.96 | **LOC:** 233 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.8936%), Tech Debt (86.2387%)
**Top Internal Functions/Classes:**
  * `draw_progress` (Impact: 24.0)
  * `dir_key` (Impact: 20.0)
  * `dir_draw` (Impact: 16.4)
  * `curpath_resize` (Impact: 7.2)
  * `dir_setlasterr` (Impact: 6.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 20`, `args: 8`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 89`, `orphaned_logic: 7`
* *Architecture:* `io: 2`, `api: 26`, `import: 5`
* *Defense:* `safety: 2`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, string.h, stdlib.h, stdio.h, stdarg.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/path.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.228 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.537 IQR)
- **Top Global Matches:** file_cluster_13: 13.228, file_cluster_8: 13.584, file_cluster_11: 13.633
- **Magnitude:** 174.66 | **LOC:** 247 | **CtrlFlow:** 81.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.6779%), Tech Debt (48.1804%)
**Top Internal Functions/Classes:**
  * `path_split` (Impact: 27.9)
    * *Intent:* */
  * `path_chdir` (Impact: 15.0)
  * `path_real` (Impact: 6.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 7`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 105`, `orphaned_logic: 2`
* *Architecture:* `api: 18`, `import: 7`
* *Defense:* `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, string.h, stdlib.h, errno.h, unistd.h, stdio.h, limits.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_export.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.776 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.276 IQR)
- **Top Global Matches:** file_cluster_13: 11.776, file_cluster_8: 11.983, file_cluster_11: 12.184
- **Magnitude:** 161.64 | **LOC:** 195 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.9541%), Tech Debt (64.4004%)
**Top Internal Functions/Classes:**
  * `output_string` (Impact: 45.0)
  * `output_info` (Impact: 23.1)
  * `item` (Impact: 15.6)
  * `dir_export_init` (Impact: 8.8)
  * `output_int` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 15`, `args: 5`, `func_start: 6`
* *Risk/State:* `state_mutation: 44`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 15`, `import: 5`
* *Defense:* `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, string.h, time.h, stdlib.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/help.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.337 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.802 IQR)
- **Top Global Matches:** file_cluster_8: 11.337, file_cluster_13: 11.597, file_cluster_7: 11.854
- **Magnitude:** 159.16 | **LOC:** 213 | **CtrlFlow:** 93.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.1775%), Tech Debt (41.2713%)
**Top Internal Functions/Classes:**
  * `help_key` (Impact: 52.1)
  * `help_draw` (Impact: 16.6)
  * `help_init` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 3`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 76`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 10`, `import: 3`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, string.h, ncurses.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_scan.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.988 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.993 IQR)
- **Top Global Matches:** file_cluster_13: 12.988, file_cluster_8: 13.345, file_cluster_11: 13.565
- **Magnitude:** 149.32 | **LOC:** 406 | **CtrlFlow:** 82.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.9589%), Tech Debt (23.0251%)
**Top Internal Functions/Classes:**
  * `process` (Impact: 30.8)
    * *Intent:* #endif #ifdef SELINUX_MAGIC
  * `dir_walk` (Impact: 7.7)
    * *Intent:* #endif #ifdef CGROUP2_SUPER_MAGIC
  * `dir_scan_init` (Impact: 4.5)
    * *Intent:* /* Reads all filenames in the currently chdir'ed directory and stores it as a * nul-separated list o...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 10`, `args: 5`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 91`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 13`, `import: 11`
* *Defense:* `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, statfs.h, string.h, types.h, stat.h, stdlib.h, magic.h, errno.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/exclude.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.295 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.376 IQR)
- **Top Global Matches:** file_cluster_13: 13.295, file_cluster_0: 13.701, file_cluster_9: 13.703
- **Magnitude:** 145.24 | **LOC:** 139 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.5199%), Tech Debt (95.202%)
**Top Internal Functions/Classes:**
  * `exclude_addfile` (Impact: 14.9)
    * *Intent:* */ #include "global.h" #include <stdio.h> #include <stdlib.h> #include <string.h>
  * `has_cachedir_tag` (Impact: 13.4)
  * `exclude_match` (Impact: 12.8)
  * `exclude_add` (Impact: 4.0)
  * `exclude_clear` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 15`, `args: 4`, `func_start: 5`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 77`, `orphaned_logic: 4`
* *Architecture:* `io: 5`, `api: 19`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, string.h, stdlib.h, stdio.h, fnmatch.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_mem.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.327 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.624 IQR)
- **Top Global Matches:** file_cluster_13: 13.327, file_cluster_8: 13.48, file_cluster_11: 13.74
- **Magnitude:** 138.74 | **LOC:** 216 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.3378%), Tech Debt (33.8333%)
**Top Internal Functions/Classes:**
  * `hlink_check` (Impact: 21.7)
    * *Intent:* */ #include "global.h" #include <string.h> #include <stdlib.h> #include <khashl.h> static struct dir...
  * `final` (Impact: 17.1)
  * `hlink_init` (Impact: 6.5)
  * `dir_mem_init` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 16`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `state_mutation: 81`, `orphaned_logic: 1`
* *Architecture:* `api: 6`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdlib.h, global.h, khashl.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.087 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.784 IQR)
- **Top Global Matches:** file_cluster_13: 11.087, file_cluster_8: 11.498, file_cluster_9: 11.771
- **Magnitude:** 126.28 | **LOC:** 360 | **CtrlFlow:** 87.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.7796%), Tech Debt (41.9193%)
**Top Internal Functions/Classes:**
  * `input_handle` (Impact: 31.8)
  * `main` (Impact: 25.8)
  * `screen_draw` (Impact: 20.3)
    * *Intent:* */ #include "global.h" #include <stdlib.h> #include <stdio.h> #include <string.h>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 4`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`, `orphaned_logic: 1`
* *Architecture:* `api: 19`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, string.h, stdlib.h, errno.h, time.h, unistd.h, yopt.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/ncdu.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.771 IQR)
- **Top Global Matches:** file_cluster_8: 10.771, file_cluster_13: 11.017, file_cluster_7: 11.027
- **Magnitude:** 49.46 | **LOC:** 446 | **CtrlFlow:** 91.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.09%), Tech Debt (18.3521%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 7`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 29`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `import: 7`
* *Defense:* `doc: 73`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` effect, C, cases
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/util.h` (C | Tier 0 | 🚨 AI THREAT: 98.75%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.955 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.578 IQR)
- **Top Global Matches:** file_cluster_13: 12.955, file_cluster_8: 13.063, file_cluster_9: 13.11
- **Magnitude:** 47.56 | **LOC:** 196 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.5786%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dir_ext_ptr` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 24`, `args: 11`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 24`
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 52.556
  * `Choke Point (Betweenness):` 0.011494 | `Ripple Effect (Closeness):` 0.393496
  * `Imports (Out-Degree: 1):` global.h, ncurses.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/shell.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.28 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.943 IQR)
- **Top Global Matches:** file_cluster_13: 11.28, file_cluster_8: 11.843, file_cluster_9: 11.859
- **Magnitude:** 41.1 | **LOC:** 83 | **CtrlFlow:** 81.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.6667%), Tech Debt (95.5022%)
**Top Internal Functions/Classes:**
  * `shell_draw` (Impact: 12.1)
  * `shell_init` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 22`, `orphaned_logic: 2`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` global.h, dirlist.h, stdlib.h, util.h, config.h, wait.h, unistd.h, ncurses.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/global.h` (C | Tier 1.5 | 🚨 AI THREAT: 99.01%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.537 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.806 IQR)
- **Top Global Matches:** file_cluster_13: 8.537, file_cluster_8: 8.567, file_cluster_7: 9.448
- **Magnitude:** 37.32 | **LOC:** 133 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `args: 2`, `class_start: 3`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 21`, `import: 19`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 377.819
  * `Choke Point (Betweenness):` 0.241379 | `Ripple Effect (Closeness):` 0.701449
  * `Imports (Out-Degree: 10):` types.h, util.h, quit.h, dirlist.h, exclude.h, shell.h, config.h, stdio.h...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/dir.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.653 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.566 IQR)
- **Top Global Matches:** file_cluster_8: 8.653, file_cluster_9: 9.089, file_cluster_7: 9.507
- **Magnitude:** 31.46 | **LOC:** 142 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
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
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `quit_key` (Impact: 9.2)
  * `quit_draw` (Impact: 2.3)
  * `quit_init` (Impact: 1.1)
    * *Intent:* */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 4`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 4`, `orphaned_logic: 3`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, ncurses.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/exclude.h` (C | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.067 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.516 IQR)
- **Top Global Matches:** file_cluster_8: 9.067, file_cluster_9: 9.12, file_cluster_7: 9.872
- **Magnitude:** 19.16 | **LOC:** 36 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- `src/dirlist.c` (C) | Magnitude: 412.48 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 206, indent_spaces: 124, branch: 75, pointers: 57
- `src/global.h` (C) | Magnitude: 37.32 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 21, macros: 21, import: 19, indent_spaces: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/delete.h` (C) | Magnitude: 18.16 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, args: 4, api: 4, ownership: 3
- `src/exclude.h` (C) | Magnitude: 19.16 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: args: 5, api: 5, structural_boundaries: 3, ownership: 3
- `src/delete.c` (C) | Magnitude: 273.06 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 155, state_mutation: 97, branch: 82, structural_boundaries: 28
- `src/dir_import.c` (C) | Magnitude: 465.78 | Delta: **0.154 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 228, pointers: 125, branch: 99, state_mutation: 86
- `src/browser.c` (C) | Magnitude: 775.98 | Delta: **0.204 IQR** | Secondary Pull: `file_cluster_13`
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

- `src/util.h` -> **Severity: 29.681** (Embedded: 0.3935 * Error Risk: 75.4284%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/global.h` -> **Severity: 37731.423** (Blast Radius: 377.819 * Doc Risk: 99.8664%)
- `src/util.h` -> **Severity: 5155.481** (Blast Radius: 52.556 * Doc Risk: 98.095%)
- `src/dirlist.h` -> **Severity: 4266.458** (Blast Radius: 44.411 * Doc Risk: 96.0676%)
- `src/dir.h` -> **Severity: 4167.332** (Blast Radius: 41.696 * Doc Risk: 99.9456%)
- `src/exclude.h` -> **Severity: 2191.342** (Blast Radius: 41.696 * Doc Risk: 52.5552%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
