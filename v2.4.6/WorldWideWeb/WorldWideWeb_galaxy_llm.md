# ARCHITECTURAL_BRIEF: WorldWideWeb
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/WorldWideWeb` |
| **Timestamp** | `2026-08-03T19:23:43.181358+00:00` |
| **Scan Duration** | `0.3s` |
| **Git Branch** | `main` |
| **Git Commit** | `032807bfe9b77b434c638667cba051be50047b23` |
| **Git Remote** | `https://github.com/simonw/1991-WWW-NeXT-Implementation.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 21 malicious artifacts.

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
| Total Artifacts | 63 |
| Analyzed Artifacts (Scanned) | 31 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 32 |
| Total LOC | 3791 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 49.2% |
| Dominant Lang | OBJECTIVE-C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2709 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.282 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1838 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| OBJECTIVE-C | 18 | 2541 | 58.1% |
| HTML | 8 | 791 | 25.8% |
| MAKEFILE | 2 | 39 | 6.5% |
| C | 1 | 420 | 3.2% |
| MARKDOWN | 1 | 0 | 3.2% |
| PLAINTEXT | 1 | 0 | 3.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.328`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 22 | 71.0% |
| file_cluster_13 | 7 | 22.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 6.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 32*

**Composition by Extension & Reason:**
- `.h`: 2x Excluded (Machine-Generated Source Code Signature: 12 LOC), 1x Excluded (Machine-Generated Source Code Signature: 20 LOC), 1x Excluded (Machine-Generated Source Code Signature: 31 LOC)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.dependencies'), 1x Excluded (Binary Format Detected)
- `.style`: 6x Excluded (Unsupported Extension: '.style')
- `.tiff`: 3x Excluded (Explicitly Denied Extension: '.tiff')
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 83 LOC)
- `.iconheader`: 2x Excluded (Unsupported Extension: '.iconheader')
- `.c`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.proj`: 1x Excluded (Unsupported Extension: '.proj')
- `.m`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.debug`: 1x Excluded (Unsupported Extension: '.debug')
- `.nib`: 1x Excluded (Unsupported Extension: '.nib')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 94.4 | 33.8 | 9.7 | 0.0 |
| Error & Exception Exposure | 0.0 | 95.2 | 35.2 | 30.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 53.3 | 59.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 26.3 | 2.3 | 2.3 |
| API Exposure | 0.0 | 13.5 | 2.9 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 44.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 2.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 93.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 29.0 | 11.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 31.2 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 1.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 36.7 | 1.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.4 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `WorldWideWeb.app/default.html` (Hits: 19)
- `default.html` (Hits: 19)
- `,Features.html` (Hits: 18)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Anchor.h** (`Anchor.h`) — 7 inbound connections
2. **HTStyle.h** (`HTStyle.h`) — 7 inbound connections
3. **HyperText.h** (`HyperText.h`) — 7 inbound connections
4. **HyperAccess.h** (`HyperAccess.h`) — 3 inbound connections
5. **HyperManager.h** (`HyperManager.h`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **NewsAccess.m** (`NewsAccess.m`) — 18 outbound dependencies
2. **FileAccess.m** (`FileAccess.m`) — 12 outbound dependencies
3. **HyperText.m** (`HyperText.m`) — 11 outbound dependencies
4. **Anchor.m** (`Anchor.m`) — 9 outbound dependencies
5. **WorldWideWeb_main.m** (`WorldWideWeb_main.m`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `change_run` (@ `ParseHTML.h`) -> Impact: **117.3** | LOC: 111
  * *Intent:* case S_word: /* We have just had non-white characters */
- `loadAnchor` (@ `HyperManager.m`) -> Impact: **117.2** | LOC: 213
  * *Intent:* // Load an anchor from some access loadAnchor: // ------------------------------- // // This implementation simply looks for an access with the right ...
- `HTStyleForRun` (@ `HTStyle.m`) -> Impact: **84.6** | LOC: 29
  * *Intent:* /* StyleSheet Functions ** ====================
- `Unknown_Block` (@ `HText.c`) -> Impact: **79.7** | LOC: 274
- `accessName` (@ `NewsAccess.m`) -> Impact: **76.7** | LOC: 94
  * *Intent:* /* Read in an Article ** ------------------ */
- `open` (@ `StyleToy.m`) -> Impact: **67.5** | LOC: 31
  * *Intent:* // Open a style sheet from a file // ------------------------------ //
- `applyStyle` (@ `HyperText.m`) -> Impact: **58.4** | LOC: 24
  * *Intent:* // Class methods // ------------- //
- `newAddress` (@ `Anchor.m`) -> Impact: **55.9** | LOC: 38
  * *Intent:* // Create new or find old named anchor // ----------------------------------- //
- `ask_name` (@ `FileAccess.m`) -> Impact: **51.1** | LOC: 35
  * *Intent:* // Get Filename near a "hint" node // ------------------------------- // // On entry, // hint is a hypertext whose name is to be used as a hint for //...
- `response` (@ `NewsAccess.m`) -> Impact: **49.2** | LOC: 28

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `newAddress` (@ `Anchor.m`) -> **O(2^N) [Recursive]**
  * *Intent:* // Create new or find old named anchor // ----------------------------------- //
- `HTStyleForRun` (@ `HTStyle.m`) -> **O(2^N) [Recursive]**
  * *Intent:* /* StyleSheet Functions ** ====================
- `applyStyle` (@ `HyperText.m`) -> **O(2^N) [Recursive]**
  * *Intent:* // Class methods // ------------- //
- `open` (@ `StyleToy.m`) -> **O(2^N) [Recursive]**
  * *Intent:* // Open a style sheet from a file // ------------------------------ //
- `free` (@ `Anchor.m`) -> **O(2^N) [Recursive]**
- `node` (@ `Anchor.m`) -> **O(2^N) [Recursive]**
  * *Intent:* // Follow a link to its destination // --------------------------------
- `new` (@ `Anchor.m`) -> **O(2^N) [Recursive]**
  * *Intent:* // Creation Methods // ================ //
- `parent` (@ `Anchor.m`) -> **O(2^N) [Recursive]**
  * *Intent:* // Get list of sources
- `initialize` (@ `FileAccess.m`) -> **O(2^N) [Recursive]**
  * *Intent:* #import "HTFTP.h" // FTP protocol routines #import "HTFile.h" // File access routines #define THIS_TEXT (HyperText *)[[[NXApp mainWindow] contentView]...
- `manager` (@ `HyperAccess.m`) -> **O(2^N) [Recursive]**
  * *Intent:* // Methods to return the values of instance variables

### Highest Data Gravity (Database Complexity)
- `Unknown_Block` (@ `HText.c`) -> DB Complexity: **39**
- `loadAnchor` (@ `HyperManager.m`) -> DB Complexity: **37**
  * *Intent:* // Load an anchor from some access loadAnchor: // ------------------------------- // // This implementation simply looks for an access with the right ...
- `change_run` (@ `ParseHTML.h`) -> DB Complexity: **33**
  * *Intent:* case S_word: /* We have just had non-white characters */
- `Unknown_Block` (@ `HText.c`) -> DB Complexity: **30**
- `accessName` (@ `NewsAccess.m`) -> DB Complexity: **26**
  * *Intent:* /* Read in an Article ** ------------------ */
- `HTStyleForRun` (@ `HTStyle.m`) -> DB Complexity: **24**
  * *Intent:* /* StyleSheet Functions ** ====================
- `Unknown_Block` (@ `HText.c`) -> DB Complexity: **22**
  * *Intent:* /* Fill the screen with blank after the file ** --------------------------
- `writeSGML` (@ `ParseHTML.h`) -> DB Complexity: **20**
- `ask_name` (@ `FileAccess.m`) -> DB Complexity: **13**
  * *Intent:* // Get Filename near a "hint" node // ------------------------------- // // On entry, // hint is a hypertext whose name is to be used as a hint for //...
- `appendStartBlock` (@ `HyperText.m`) -> DB Complexity: **13**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 27 | 4189.72 | 35.29% | 57.27% |
| `WorldWideWeb.app` | 3 | 43.86 | 5.37% | 0.0% |
| `Test` | 1 | 15.3 | 11.12% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `HyperAccess.m` -> **100.0%** Exposure
- `,Features.html` -> **99.9996%** Exposure
- `TextToy.m` -> **99.9995%** Exposure
- `Features.html` -> **99.9994%** Exposure
- `Upgrade.html` -> **99.8017%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Anchor.m` -> **100.0%** Exposure
- `FileAccess.m` -> **100.0%** Exposure
- `HTStyle.m` -> **100.0%** Exposure
- `HyperManager.m` -> **100.0%** Exposure
- `HyperText.m` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `TextToy.m` -> **12** Orphaned Functions | **0** Duplicates
- `FileAccess.m` -> **11** Orphaned Functions | **0** Duplicates
- `HyperAccess.m` -> **11** Orphaned Functions | **0** Duplicates
- `StyleToy.m` -> **11** Orphaned Functions | **0** Duplicates
- `Anchor.m` -> **10** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Anchor.m`** -> AI Confidence: **99.48%**
2. **`FileAccess.m`** -> AI Confidence: **99.48%**
3. **`HyperText.m`** -> AI Confidence: **99.48%**
4. **`NewsAccess.m`** -> AI Confidence: **99.48%**
5. **`WorldWideWeb_main.m`** -> AI Confidence: **99.48%**
6. **`HyperAccess.m`** -> AI Confidence: **99.34%**
7. **`HyperManager.m`** -> AI Confidence: **99.34%**
8. **`StyleToy.m`** -> AI Confidence: **99.34%**
9. **`TextToy.m`** -> AI Confidence: **99.34%**
10. **`HTStyle.m`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `StyleToy.m` -> **20.0%** Exposure
- `HText.c` -> **20.0%** Exposure
- `NewsAccess.m` -> **0.1325%** Exposure
### Weaponizable Injection Vectors
- `NewsAccess.m` -> **36.7163%** Exposure
### Raw Memory Manipulation
- `HText.c` -> **10.0%** Exposure
- `StyleToy.m` -> **2.4306%** Exposure
- `NewsAccess.m` -> **0.0017%** Exposure
### Algorithmic DoS Exposure
- `FileAccess.m` -> **100.0%** Exposure
- `HyperManager.m` -> **100.0%** Exposure
- `NewsAccess.m` -> **100.0%** Exposure
- `ParseHTML.h` -> **100.0%** Exposure
- `StyleToy.m` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `110` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `HText.c` (C) -> Cumulative Risk: **776.89**
- **Archetype:** `file_cluster_8` (Distance: 13.543 IQR)
- **Magnitude:** 615.2 | **LOC:** 794 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.5419%)
- **Heaviest Functions:** `Unknown_Block` (Impact: 79.7), `Unknown_Block` (Impact: 34.0), `Unknown_Block` (Impact: 30.9)

### 2. `HyperManager.m` (OBJECTIVE-C) -> Cumulative Risk: **659.25**
- **Archetype:** `file_cluster_13` (Distance: 14.129 IQR)
- **Magnitude:** 248.52 | **LOC:** 441 | **CtrlFlow:** 96.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (98.659%)
- **Heaviest Functions:** `loadAnchor` (Impact: 117.2), `registerAccess` (Impact: 13.4), `new` (Impact: 4.3)

### 3. `StyleToy.m` (OBJECTIVE-C) -> Cumulative Risk: **647.69**
- **Archetype:** `file_cluster_8` (Distance: 12.863 IQR)
- **Magnitude:** 260.32 | **LOC:** 345 | **CtrlFlow:** 95.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (98.6183%)
- **Heaviest Functions:** `open` (Impact: 67.5), `display_style` (Impact: 25.4), `load_style` (Impact: 17.1)

### 4. `NewsAccess.m` (OBJECTIVE-C) -> Cumulative Risk: **630.65**
- **Archetype:** `file_cluster_13` (Distance: 14.676 IQR)
- **Magnitude:** 473.06 | **LOC:** 905 | **CtrlFlow:** 94.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Algorithmic Dos (100.0%), Verification (80.0%), Spec Match (80.0%)
- **Heaviest Functions:** `accessName` (Impact: 76.7), `response` (Impact: 49.2), `initialize` (Impact: 28.1)

### 5. `HTStyle.m` (OBJECTIVE-C) -> Cumulative Risk: **626.66**
- **Archetype:** `file_cluster_8` (Distance: 14.609 IQR)
- **Magnitude:** 509.16 | **LOC:** 353 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9996%), Safety Score (91.7329%)
- **Heaviest Functions:** `HTStyleForRun` (Impact: 84.6), `HTStyleRead` (Impact: 28.4), `HTStyleSheetRemoveStyle` (Impact: 21.6)

### 6. `HyperText.m` (OBJECTIVE-C) -> Cumulative Risk: **625.82**
- **Archetype:** `file_cluster_8` (Distance: 14.592 IQR)
- **Magnitude:** 423.78 | **LOC:** 1614 | **CtrlFlow:** 98.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (98.0286%), Safety Score (95.1659%)
- **Heaviest Functions:** `applyStyle` (Impact: 58.4), `windowWillClose` (Impact: 24.3), `appendBegin` (Impact: 21.6)

### 7. `FileAccess.m` (OBJECTIVE-C) -> Cumulative Risk: **577.84**
- **Archetype:** `file_cluster_13` (Distance: 13.559 IQR)
- **Magnitude:** 227.8 | **LOC:** 643 | **CtrlFlow:** 97.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (98.106%)
- **Heaviest Functions:** `ask_name` (Impact: 51.1), `save` (Impact: 31.1), `saveIn` (Impact: 9.1)

### 8. `ParseHTML.h` (OBJECTIVE-C) -> Cumulative Risk: **553.34**
- **Archetype:** `file_cluster_8` (Distance: 13.71 IQR)
- **Magnitude:** 575.54 | **LOC:** 1170 | **CtrlFlow:** 96.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `change_run` (Impact: 117.3), `parse_example` (Impact: 35.7), `findSGML` (Impact: 30.9)

### 9. `Anchor.m` (OBJECTIVE-C) -> Cumulative Risk: **514.62**
- **Archetype:** `file_cluster_8` (Distance: 13.308 IQR)
- **Magnitude:** 340.3 | **LOC:** 364 | **CtrlFlow:** 97.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (93.1734%), Cognitive Load (80.5053%)
- **Heaviest Functions:** `newAddress` (Impact: 55.9), `selectDiagnostic` (Impact: 31.1), `follow` (Impact: 18.6)

### 10. `WorldWideWeb_main.m` (OBJECTIVE-C) -> Cumulative Risk: **452.13**
- **Archetype:** `file_cluster_13` (Distance: 12.309 IQR)
- **Magnitude:** 40.54 | **LOC:** 73 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Algorithmic Dos (100.0%), Tech Debt (90.7814%), Cognitive Load (76.7007%)
- **Heaviest Functions:** `main` (Impact: 9.9), `int_default` (Impact: 7.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `HText.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.543 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.362 IQR)
- **Top Global Matches:** file_cluster_8: 13.543, file_cluster_13: 13.632, file_cluster_0: 13.834
- **Magnitude:** 615.2 | **LOC:** 794 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (71.3876%), Tech Debt (91.5363%)
**Top Internal Functions/Classes:**
  * `Unknown_Block` (Impact: 79.7 | O(N^3) | DB: 39)
  * `Unknown_Block` (Impact: 34.0 | O(N^2) | DB: 30)
  * `Unknown_Block` (Impact: 30.9 | O(N^2) | DB: 22)
    * *Intent:* /* Fill the screen with blank after the file ** --------------------------
  * `Unknown_Block` (Impact: 11.0 | O(N^2) | DB: 2)
    * *Intent:* text->top_of_screen+DISPLAY_LINES-1, /* Seen */
  * `Unknown_Block` (Impact: 8.5 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 45`, `args: 1`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 343`, `duplicate_logic: 8`
* *Architecture:* `api: 91`, `import: 5`
* *Defense:* `safety: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HText.h, HyperText.h, ctype.h, HTString.h, HTUtils.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ParseHTML.h` (OBJECTIVE-C | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.71 IQR)
- **Top Global Matches:** file_cluster_8: 13.71, file_cluster_16: 13.964, file_cluster_13: 14.01
- **Magnitude:** 575.54 | **LOC:** 1170 | **CtrlFlow:** 96.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (66.901%), Tech Debt (20.365%)
**Top Internal Functions/Classes:**
  * `change_run` (Impact: 117.3 | O(N^2) | DB: 33)
    * *Intent:* case S_word: /* We have just had non-white characters */
  * `parse_example` (Impact: 35.7 | O(N^2) | DB: 9)
    * *Intent:* /* Start a highlighted area
  * `findSGML` (Impact: 30.9 | O(N^2) | DB: 6)
    * *Intent:* #ifdef CHARACTER_TRACE
  * `check` (Impact: 25.0 | O(N^2) | DB: 6)
  * `writeSGML` (Impact: 19.9 | O(N^2) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 6`, `args: 107`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 285`, `dead_code: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 1`, `import: 1`
* *Defense:* `safety: 1`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTStyle.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HTStyle.m` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.609 IQR)
- **Top Global Matches:** file_cluster_8: 14.609, file_cluster_13: 14.792, file_cluster_17: 14.919
- **Magnitude:** 509.16 | **LOC:** 353 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (76.3138%), Tech Debt (59.0398%)
**Top Internal Functions/Classes:**
  * `HTStyleForRun` (Impact: 84.6 | O(2^N) | DB: 24)
    * *Intent:* /* StyleSheet Functions ** ====================
  * `HTStyleRead` (Impact: 28.4 | O(N^2) | DB: 12)
  * `HTStyleSheetRemoveStyle` (Impact: 21.6 | O(N^2) | DB: 6)
  * `HTStyleSheetRead` (Impact: 16.6 | O(N^2) | DB: 7)
  * `HTStyleNamed` (Impact: 16.0 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `args: 56`, `func_start: 15`
* *Risk/State:* `state_mutation: 236`, `dead_code: 2`, `orphaned_logic: 6`
* *Architecture:* `io: 4`, `import: 2`
* *Defense:* `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTStyle.h, HTUtils.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `NewsAccess.m` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.676 IQR)
- **Top Global Matches:** file_cluster_13: 14.676, file_cluster_11: 14.947, file_cluster_17: 14.959
- **Magnitude:** 473.06 | **LOC:** 905 | **CtrlFlow:** 94.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (78.2527%), Tech Debt (53.8873%)
**Top Internal Functions/Classes:**
  * `accessName` (Impact: 76.7 | O(N^2) | DB: 26)
    * *Intent:* /* Read in an Article ** ------------------ */
  * `response` (Impact: 49.2 | O(N^2) | DB: 9)
  * `initialize` (Impact: 28.1 | O(N^2) | DB: 9)
    * *Intent:* // Initialisaion for this class // ---------------------------- //
  * `loadAnchor` (Impact: 24.2 | O(N^2) | DB: 4)
    * *Intent:* /* Read in the HEADer of the article: ** ** The header fields are either ignored, or formatted and p...
  * `next_char` (Impact: 9.2 | O(N^1) | DB: 4)
    * *Intent:* static struct sockaddr_in soc_address; /* Binary network address */ static int s; /* Socket for conn...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 6`, `args: 81`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 258`, `dead_code: 5`, `fragile_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 8`, `api: 4`, `import: 18`
* *Defense:* `safety: 4`, `immutability_locks: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` streams.h, HTUtils.h, libc.h, netdb.h, NewsAccess.h, ctype.h, errno.h, types.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HyperText.m` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.592 IQR)
- **Top Global Matches:** file_cluster_8: 14.592, file_cluster_17: 14.755, file_cluster_0: 14.843
- **Magnitude:** 423.78 | **LOC:** 1614 | **CtrlFlow:** 98.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (76.9498%), Tech Debt (58.7558%)
**Top Internal Functions/Classes:**
  * `applyStyle` (Impact: 58.4 | O(2^N) | DB: 4)
    * *Intent:* // Class methods // ------------- //
  * `windowWillClose` (Impact: 24.3 | O(N^1) | DB: 3)
  * `appendBegin` (Impact: 21.6 | O(N^2) | DB: 12)
  * `applyToSimilar` (Impact: 20.4 | O(N^2) | DB: 9)
  * `appendStartBlock` (Impact: 17.1 | O(N^2) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 1`, `args: 30`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 230`, `dead_code: 1`, `orphaned_logic: 5`
* *Architecture:* `io: 5`
* *Defense:* `safety: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` HyperText.h, HyperAccess.h, HTAnchor.h, HTAnchor.h, HTStyle.h, HTML.h, HTML.h, appkit.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Anchor.m` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.308 IQR)
- **Top Global Matches:** file_cluster_8: 13.308, file_cluster_13: 13.309, file_cluster_17: 13.703
- **Magnitude:** 340.3 | **LOC:** 364 | **CtrlFlow:** 97.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (80.5053%), Tech Debt (93.1734%)
**Top Internal Functions/Classes:**
  * `newAddress` (Impact: 55.9 | O(2^N) | DB: 9)
    * *Intent:* // Create new or find old named anchor // ----------------------------------- //
  * `selectDiagnostic` (Impact: 31.1 | O(N^1) | DB: 1)
  * `follow` (Impact: 18.6 | O(N^2))
  * `free` (Impact: 17.4 | O(2^N))
  * `equivalent` (Impact: 15.9 | O(N^2) | DB: 2)
    * *Intent:* // Case insensitive string comparison // ---------------------------------- // On entry, // s Points...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 2`, `args: 30`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 105`, `orphaned_logic: 10`
* *Architecture:* `io: 2`, `import: 9`
* *Defense:* `safety: 7`, `immutability_locks: 6`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Object.h, ctype.h, HyperText.h, typedstream.h, HyperManager.h, Anchor.h, appkit.h, HTParse.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `StyleToy.m` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.863 IQR)
- **Top Global Matches:** file_cluster_8: 12.863, file_cluster_13: 12.967, file_cluster_2: 13.3
- **Magnitude:** 260.32 | **LOC:** 345 | **CtrlFlow:** 95.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (74.7037%), Tech Debt (98.6183%)
**Top Internal Functions/Classes:**
  * `open` (Impact: 67.5 | O(2^N) | DB: 8)
    * *Intent:* // Open a style sheet from a file // ------------------------------ //
  * `display_style` (Impact: 25.4 | O(N^2) | DB: 2)
    * *Intent:* // ACTION METHODS // ==============
  * `load_style` (Impact: 17.1 | O(N^2) | DB: 11)
    * *Intent:* // Load style from Panel
  * `NextButton` (Impact: 12.6 | O(N^3) | DB: 2)
  * `PreviousButton` (Impact: 9.6 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 2`, `args: 20`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 98`, `orphaned_logic: 11`
* *Architecture:* `io: 3`, `api: 1`, `import: 5`
* *Defense:* `safety: 2`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` HyperText.h, HTStyle.h, HTParse.h, HTUtils.h, StyleToy.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HyperManager.m` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.129 IQR)
- **Top Global Matches:** file_cluster_13: 14.129, file_cluster_17: 14.18, file_cluster_11: 14.39
- **Magnitude:** 248.52 | **LOC:** 441 | **CtrlFlow:** 96.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (94.426%), Tech Debt (98.659%)
**Top Internal Functions/Classes:**
  * `loadAnchor` (Impact: 117.2 | O(N^2) | DB: 37)
    * *Intent:* // Load an anchor from some access loadAnchor: // ------------------------------- // // This impleme...
  * `registerAccess` (Impact: 13.4 | O(N^2) | DB: 2)
    * *Intent:* // Access Management functions
  * `new` (Impact: 4.3 | O(2^N) | DB: 2)
  * `name` (Impact: 2.2 | O(N^1))
  * `traceOn` (Impact: 2.0 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 2`, `args: 16`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 99`, `dead_code: 3`, `fragile_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `io: 6`, `api: 1`, `import: 6`
* *Defense:* `safety: 4`, `immutability_locks: 7`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` HTAccess.h, HyperText.h, WWWPageLayout.h, HyperManager.h, HTParse.h, HTUtils.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `FileAccess.m` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.559 IQR)
- **Top Global Matches:** file_cluster_13: 13.559, file_cluster_8: 13.863, file_cluster_2: 13.937
- **Magnitude:** 227.8 | **LOC:** 643 | **CtrlFlow:** 97.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (42.0331%), Tech Debt (98.106%)
**Top Internal Functions/Classes:**
  * `ask_name` (Impact: 51.1 | O(N^2) | DB: 13)
    * *Intent:* // Get Filename near a "hint" node // ------------------------------- // // On entry, // hint is a h...
  * `save` (Impact: 31.1 | O(N^2) | DB: 12)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////////// // S A V I N ...
  * `saveIn` (Impact: 9.1 | O(N^1) | DB: 8)
    * *Intent:* // Save as a file using save panel (any format) // -------------------------------- // On entry, // ...
  * `linkToNew` (Impact: 6.5 | O(N^1) | DB: 5)
  * `initialize` (Impact: 4.2 | O(2^N))
    * *Intent:* #import "HTFTP.h" // FTP protocol routines #import "HTFile.h" // File access routines #define THIS_T...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 2`, `args: 26`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 99`, `orphaned_logic: 11`
* *Architecture:* `io: 7`, `api: 1`, `import: 12`
* *Defense:* `safety: 8`, `doc: 28`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTUtils.h, libc.h, types.h, FileAccess.h, stat.h, HTTCP.h, HTFTP.h, HTFile.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HTextNeXT.h` (OBJECTIVE-C | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.367 IQR)
- **Top Global Matches:** file_cluster_8: 8.367, file_cluster_7: 9.193, file_cluster_13: 9.242
- **Magnitude:** 84.66 | **LOC:** 173 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 13`, `func_start: 13`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 15`, `import: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTAnchor.h, HTStyle.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `TextToy.m` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.247 IQR)
- **Top Global Matches:** file_cluster_13: 11.247, file_cluster_8: 11.306, file_cluster_2: 11.588
- **Magnitude:** 68.7 | **LOC:** 136 | **CtrlFlow:** 90.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (52.7749%), Tech Debt (99.9995%)
**Top Internal Functions/Classes:**
  * `windowDidBecomeMain` (Impact: 6.7 | O(N^1) | DB: 4)
  * `registerAccess` (Impact: 5.4 | O(N^1) | DB: 1)
  * `followLink` (Impact: 4.2 | O(2^N))
  * `dump` (Impact: 4.2 | O(2^N))
  * `Do_getStartLength` (Impact: 3.4 | O(N^1) | DB: 4)
    * *Intent:* /* Action Methods ** ==============
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 2`, `args: 3`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `orphaned_logic: 12`
* *Architecture:* `io: 3`, `import: 6`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` HyperText.h, TextToy.h, Anchor.h, appkit.h, List.h, HTUtils.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HyperAccess.m` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.734 IQR)
- **Top Global Matches:** file_cluster_8: 11.734, file_cluster_13: 11.79, file_cluster_17: 12.399
- **Magnitude:** 50.28 | **LOC:** 159 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (37.5839%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `manager` (Impact: 4.2 | O(2^N))
    * *Intent:* // Methods to return the values of instance variables
  * `accessName` (Impact: 4.2 | O(N^1))
  * `hyperTextDidBecomeMain` (Impact: 4.2 | O(2^N))
  * `setManager` (Impact: 2.3 | O(N^1) | DB: 1)
  * `setOpenString` (Impact: 2.2 | O(N^1) | DB: 1)
    * *Intent:* // History: // 26 Sep 90 Written TBL #include <stdio.h> #include <appkit/appkit.h> #import "HyperAcc...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 2`, `args: 2`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `orphaned_logic: 11`
* *Architecture:* `import: 6`
* *Defense:* `safety: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` HTUtils.h, HyperAccess.h, HyperManager.h, Anchor.h, appkit.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Anchor.h` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 98.78%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.536 IQR)
- **Top Global Matches:** file_cluster_8: 8.536, file_cluster_13: 9.337, file_cluster_7: 9.528
- **Magnitude:** 44.92 | **LOC:** 58 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.2334%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 7`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `import: 3`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 136.25
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.282353
  * `Imports (Out-Degree: 0):` List.h, appkit.h, Object.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `WorldWideWeb_main.m` (OBJECTIVE-C | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.309 IQR)
- **Top Global Matches:** file_cluster_13: 12.309, file_cluster_2: 12.453, file_cluster_8: 12.804
- **Magnitude:** 40.54 | **LOC:** 73 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (76.7007%), Tech Debt (90.7814%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 9.9 | O(N^2) | DB: 9)
  * `int_default` (Impact: 7.7 | O(N^1) | DB: 2)
    * *Intent:* /* * Generated by the NeXT Interface Builder. * * History: * 27 Feb 91 Modified TBL to initialise NX...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `args: 13`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 21`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` libc.h, Application.h, PrintInfo.h, string.h, defaults.h, HTUtils.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HyperAccess.h` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.961 IQR)
- **Top Global Matches:** file_cluster_8: 8.961, file_cluster_13: 9.246, file_cluster_2: 9.457
- **Magnitude:** 35.88 | **LOC:** 56 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.2468%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 4`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `io: 2`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 65.22
  * `Choke Point (Betweenness):` 0.006322 | `Ripple Effect (Closeness):` 0.119048
  * `Imports (Out-Degree: 2):` Anchor.h, List.h, Object.h, HyperText.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Features.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.586 IQR)
- **Top Global Matches:** file_cluster_8: 5.586, file_cluster_7: 6.815, file_cluster_1: 6.984
- **Magnitude:** 30.14 | **LOC:** 258 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (99.9994%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 86`, `args: 28`
* *Risk/State:* `fragile_debt: 24`
* *Architecture:* `io: 18`, `api: 10`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `,Features.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.606 IQR)
- **Top Global Matches:** file_cluster_8: 5.606, file_cluster_7: 6.828, file_cluster_1: 6.998
- **Magnitude:** 30.02 | **LOC:** 252 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (99.9996%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 86`, `args: 28`
* *Risk/State:* `fragile_debt: 24`
* *Architecture:* `io: 18`, `api: 10`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugs.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.826 IQR)
- **Top Global Matches:** file_cluster_8: 5.826, file_cluster_7: 7.011, file_cluster_1: 7.175
- **Magnitude:** 20.46 | **LOC:** 124 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (89.7963%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 47`, `args: 22`
* *Risk/State:* `fragile_debt: 3`
* *Architecture:* `io: 6`, `api: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `TcpAccess.m` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.175 IQR)
- **Top Global Matches:** file_cluster_13: 11.175, file_cluster_8: 11.512, file_cluster_2: 11.7
- **Magnitude:** 20.14 | **LOC:** 109 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (73.1059%), Tech Debt (98.9347%)
**Top Internal Functions/Classes:**
  * `accessName` (Impact: 7.3 | O(N^1) | DB: 12)
  * `name` (Impact: 2.2 | O(N^1))
    * *Intent:* #import "TcpAccess.h" #import "Anchor.h" #import "HTUtils.h" #import "HTTP.h" /* Module parameters: ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 2`, `args: 4`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `import: 4`
* *Defense:* `safety: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Anchor.h, TcpAccess.h, HTTP.h, HTUtils.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HTStyle.h` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 98.73%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.271 IQR)
- **Top Global Matches:** file_cluster_8: 8.271, file_cluster_13: 9.004, file_cluster_7: 9.018
- **Magnitude:** 19.02 | **LOC:** 78 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.2749%), Tech Debt (94.7457%)
**Top Internal Functions/Classes:**
  * `HTStylePick` (Impact: 2.0 | O(N^1))
    * *Intent:* void *anchor; /* Anchor id if any, else zero */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 8`, `args: 15`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 16`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 136.878
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.284058
  * `Imports (Out-Degree: 0):` appkit.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `WorldWideWeb.app/default.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.668 IQR)
- **Top Global Matches:** file_cluster_8: 6.668, file_cluster_7: 7.704, file_cluster_1: 7.837
- **Magnitude:** 15.98 | **LOC:** 50 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.1135%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 29`, `args: 19`
* *Risk/State:* None
* *Architecture:* `io: 19`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `default.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.668 IQR)
- **Top Global Matches:** file_cluster_8: 6.668, file_cluster_7: 7.704, file_cluster_1: 7.837
- **Magnitude:** 15.98 | **LOC:** 50 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.1135%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 29`, `args: 19`
* *Risk/State:* None
* *Architecture:* `io: 19`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Upgrade.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.165 IQR)
- **Top Global Matches:** file_cluster_8: 6.165, file_cluster_7: 7.232, file_cluster_1: 7.343
- **Magnitude:** 15.86 | **LOC:** 43 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.32%), Tech Debt (99.8017%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 23`, `args: 6`
* *Risk/State:* `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.054 IQR)
- **Top Global Matches:** file_cluster_13: 12.054, file_cluster_8: 12.332, file_cluster_9: 12.639
- **Magnitude:** 15.48 | **LOC:** 43 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.1949%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 17`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 1`
* *Architecture:* `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Makefile.postamble, Makefile.dependencies, Makefile.preamble, app.make
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HyperManager.h` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.006 IQR)
- **Top Global Matches:** file_cluster_8: 7.006, file_cluster_13: 8.043, file_cluster_7: 8.235
- **Magnitude:** 15.42 | **LOC:** 35 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.7149%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `func_start: 14`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 39.85
  * `Choke Point (Betweenness):` 0.002299 | `Ripple Effect (Closeness):` 0.1
  * `Imports (Out-Degree: 1):` List.h, HyperAccess.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `HyperManager.m` (OBJECTIVE-C) | Magnitude: 248.52 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 99, indent_spaces: 68, branch: 50, func_start: 26
- `TextToy.m` (OBJECTIVE-C) | Magnitude: 68.7 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, state_mutation: 23, branch: 19, func_start: 14
- `WorldWideWeb_main.m` (OBJECTIVE-C) | Magnitude: 40.54 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, state_mutation: 21, args: 13, indent_tabs: 11
- `NewsAccess.m` (OBJECTIVE-C) | Magnitude: 473.06 | Delta: **0.271 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 258, branch: 108, indent_tabs: 103, args: 81
- `Makefile` (MAKEFILE) | Magnitude: 15.48 | Delta: **0.278 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 17, import: 4, indent_spaces: 2, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `Anchor.m` (OBJECTIVE-C) | Magnitude: 340.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 105, indent_spaces: 78, branch: 73, indent_tabs: 31
- `HyperAccess.m` (OBJECTIVE-C) | Magnitude: 50.28 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, branch: 14, func_start: 14, state_mutation: 12
- `HText.c` (C) | Magnitude: 615.2 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 343, pointers: 199, indent_spaces: 199, api: 91
- `StyleToy.m` (OBJECTIVE-C) | Magnitude: 260.32 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 98, indent_spaces: 96, branch: 44, pointers: 44
- `HyperText.m` (OBJECTIVE-C) | Magnitude: 423.78 | Delta: **0.163 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 230, indent_spaces: 121, branch: 61, pointers: 59

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Anchor.h` -> **Severity: 21.706** (Embedded: 0.2824 * Error Risk: 76.875%)
- `HTStyle.h` -> **Severity: 16.876** (Embedded: 0.2841 * Error Risk: 59.4118%)
- `HyperAccess.h` -> **Severity: 9.524** (Embedded: 0.119 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `HTStyle.h` -> **Severity: 13687.225** (Blast Radius: 136.878 * Doc Risk: 99.9958%)
- `HyperText.h` -> **Severity: 4286.171** (Blast Radius: 101.582 * Doc Risk: 42.1942%)
- `HText.c` -> **Severity: 1991.634** (Blast Radius: 20.008 * Doc Risk: 99.5419%)
- `HTextNeXT.h` -> **Severity: 1991.052** (Blast Radius: 20.008 * Doc Risk: 99.5128%)
- `Anchor.h` -> **Severity: 1624.141** (Blast Radius: 136.25 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
