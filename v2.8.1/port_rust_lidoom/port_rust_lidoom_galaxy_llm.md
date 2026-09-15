# ARCHITECTURAL_BRIEF: port_rust_lidoom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/fwcd/lidoom.git` |
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
| Total Artifacts | 18 |
| Analyzed Artifacts (Scanned) | 10 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 640 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 55.6% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 8 | 636 | 80.0% |
| MARKDOWN | 1 | 0 | 10.0% |
| SHELL | 1 | 4 | 10.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** State Mutators Files 40%, Data / Markup / Trivial 30%, Declarative / Non-Code 10%, Generic / Templated Code Files 10%, Interface Declarations Files 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 9 | 90.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 10.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.toml`: 1x Unsupported Format (.toml)
- `.gif`: 1x Excluded (Explicitly Denied Extension: '.gif')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 79.5 | 20.8 | 14.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.7 | 34.7 | 45.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 98.3 | 27.7 | 25.1 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 19.6 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 15.8 | 5.6 | 3.5 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 55.5 | 85.2 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 81.5 | 18.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 77.8 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 55.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 37 | 6 | 9 | `src/gui.rs` |
| cleanup | 0 | 0 | 0 | - |
| guards | 25 | 7 | 6 | `src/gui.rs` |
| danger | 16 | 3 | 2 | `src/main.rs` |
| concurrency | 48 | 6 | 11 | `src/main.rs` |
| connectivity | 20 | 8 | 3 | `src/message.rs` |
| io | 1 | 1 | 0 | `buildenv.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 1 | 0 | `src/main.rs` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 21 | 6 | 4 | `src/doom.rs` |
| tests | 2 | 1 | 0 | `src/doom.rs` |
| docs | 13 | 2 | 3 | `src/message.rs` |
| debt | 5 | 4 | 1 | `src/gui.rs` |
| mutation | 75 | 7 | 17 | `src/gui.rs` |
| dead_code | 8 | 5 | 1 | `src/doom.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 2 | 1 | 0 | `src/mapper.rs` |
| ml_ai | 10 | 2 | 2 | `src/gui.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `buildenv.sh` (Hits: 1)
- `README.md` (Hits: 0)
- `src/constants.rs` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **mapper.rs** (`src/mapper.rs`) — 1 inbound connections
2. **README.md** (`README.md`) — 0 inbound connections
3. **buildenv.sh** (`buildenv.sh`) — 0 inbound connections
4. **constants.rs** (`src/constants.rs`) — 0 inbound connections
5. **controller.rs** (`src/controller.rs`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **doom.rs** (`src/doom.rs`) — 27 outbound dependencies
2. **gui.rs** (`src/gui.rs`) — 22 outbound dependencies
3. **controller.rs** (`src/controller.rs`) — 18 outbound dependencies
4. **mapper.rs** (`src/mapper.rs`) — 13 outbound dependencies
5. **main.rs** (`src/main.rs`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run` **(Many-Argument Workhorses)** (@ `src/gui.rs`) -> Impact: **55.6** | LOC: 108
- `run` **(Defensive Guards)** (@ `src/mapper.rs`) -> Impact: **50.9** | LOC: 83
- `run` **(Defensive Guards)** (@ `src/controller.rs`) -> Impact: **24.4** | LOC: 37
- `draw_frame` **(Many-Argument Workhorses)** (@ `src/doom.rs`) -> Impact: **12.9** | LOC: 34
- `main` **(Interface Declarations)** (@ `src/main.rs`) -> Impact: **7.9** | LOC: 58
- `convert_key` **(State Mutators)** (@ `src/controller.rs`) -> Impact: **6.6** | LOC: 19
- `gamepad_button_to_action` **(State Mutators)** (@ `src/mapper.rs`) -> Impact: **6.5** | LOC: 16
- `run` **(Generic / Templated Code)** (@ `src/updater.rs`) -> Impact: **5.6** | LOC: 8
- `convert_key` **(State Mutators)** (@ `src/gui.rs`) -> Impact: **4.3** | LOC: 42
- `convert_gamepad_button` **(State Mutators)** (@ `src/controller.rs`) -> Impact: **3.7** | LOC: 18

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Interface Declarations**: signature/entry function exposing API with minimal logic
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **State Mutators**: general-purpose function that reassigns or mutates state

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 8 | 361.52 | 22.71% | 31.2% |
| `__monolith__` | 2 | 5.48 | 2.56% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/doom.rs` -> **98.2933%** Exposure
- `src/controller.rs` -> **50.7022%** Exposure
- `src/gui.rs` -> **37.7541%** Exposure
- `src/updater.rs` -> **37.7541%** Exposure
- `src/main.rs` -> **25.1327%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/mapper.rs` -> **81.4663%** Exposure
- `src/gui.rs` -> **50.0%** Exposure
- `src/doom.rs` -> **22.5316%** Exposure
- `src/main.rs` -> **13.7452%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/doom.rs` -> **4** Orphaned Functions | **0** Duplicates
- `src/controller.rs` -> **1** Orphaned Functions | **0** Duplicates
- `src/gui.rs` -> **1** Orphaned Functions | **0** Duplicates
- `src/main.rs` -> **1** Orphaned Functions | **0** Duplicates
- `src/updater.rs` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `105` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/mapper.rs` (RUST) -> Cumulative Risk: **607.82**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +0.07)
- **Magnitude:** 110.18 | **LOC:** 145 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9985%), State Flux (81.4663%)
- **Heaviest Functions:** `run` (Defensive Guards, Impact: 50.9), `gamepad_button_to_action` (State Mutators, Impact: 6.5), `key_to_action` (State Mutators, Impact: 3.7)

### 2. `src/doom.rs` (RUST) -> Cumulative Risk: **482.57**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +0.88)
- **Magnitude:** 43.16 | **LOC:** 124 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.2933%), Concurrency (85.1953%)
- **Heaviest Functions:** `draw_frame` (Many-Argument Workhorses, Impact: 12.9), `convert_action` (State Mutators, Impact: 3.6), `get_key` (Callbacks & Closures, Impact: 3.4)

### 3. `src/gui.rs` (RUST) -> Cumulative Risk: **458.65**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +0.74)
- **Magnitude:** 78.1 | **LOC:** 171 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Verification (80.0%), State Flux (50.0%)
- **Heaviest Functions:** `run` (Many-Argument Workhorses, Impact: 55.6), `convert_key` (State Mutators, Impact: 4.3), `convert_mouse_button` (State Mutators, Impact: 3.2)

### 4. `src/controller.rs` (RUST) -> Cumulative Risk: **382.25**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z -0.07)
- **Magnitude:** 52.88 | **LOC:** 102 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (98.682%), Tech Debt (50.7022%)
- **Heaviest Functions:** `run` (Defensive Guards, Impact: 24.4), `convert_key` (State Mutators, Impact: 6.6), `convert_gamepad_button` (State Mutators, Impact: 3.7)

### 5. `src/main.rs` (RUST) -> Cumulative Risk: **362.4**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.21)
- **Magnitude:** 26.32 | **LOC:** 90 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9988%), Safety Score (91.6827%), Cognitive Load (29.4831%)
- **Heaviest Functions:** `main` (Interface Declarations, Impact: 7.9)

### 6. `src/updater.rs` (RUST) -> Cumulative Risk: **347.48**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.03)
- **Magnitude:** 10.84 | **LOC:** 16 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (90.6079%), Tech Debt (37.7541%)
- **Heaviest Functions:** `run` (Generic / Templated Code, Impact: 5.6)

### 7. `src/message.rs` (RUST) -> Cumulative Risk: **112.8**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Declarative / Non-Code` (z +0.39)
- **Magnitude:** 26.48 | **LOC:** 95 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Api Exposure (10.5071%), Verification (2.2977%)

### 8. `buildenv.sh` (SHELL) -> Cumulative Risk: **81.16**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Data / Markup / Trivial` (z +0.00)
- **Magnitude:** 3.28 | **LOC:** 5 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (70.2063%), Cognitive Load (5.1174%), Api Exposure (3.5258%), Verification (2.3153%)
- **Heaviest Functions:** `Anonymous_Block` (Unclassified, Impact: 2.2)

### 9. `src/constants.rs` (RUST) -> Cumulative Risk: **7.89**
- **Archetype:** `file_cluster_3` (Distance: N/A IQR)
- **Composition Archetype:** `Data / Markup / Trivial` (z +0.00)
- **Magnitude:** 13.56 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (5.5883%), Verification (2.2977%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/mapper.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 110.18 | **LOC:** 145 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.5468%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` **(Defensive Guards)** (Impact: 50.9)
  * `gamepad_button_to_action` **(State Mutators)** (Impact: 6.5)
  * `key_to_action` **(State Mutators)** (Impact: 3.7)
  * `movement_dir_to_action` **(State Mutators)** (Impact: 3.2)
  * `camera_dir_to_action` **(State Mutators)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 32`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 1`, `concurrency: 11`, `import: 5`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 170.507
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` ControllerMessage, GamepadButton, GamepadStick, GamepadTrigger, HashSet, Key, MapperMessage, MouseButton...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/gui.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 78.1 | **LOC:** 171 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.3647%), Tech Debt (37.7541%)
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 55.6)
  * `convert_key` **(State Mutators)** (Impact: 4.3)
  * `convert_mouse_button` **(State Mutators)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 34`, `args: 9`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DOOM_WIDTH, GUIMessage, Key, LIGHTHOUSE_COLS, LIGHTHOUSE_ROWS, MouseButton, Pos, Result...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controller.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 52.88 | **LOC:** 102 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.3383%), Tech Debt (50.7022%)
**Top Internal Functions/Classes:**
  * `run` **(Defensive Guards)** (Impact: 24.4)
  * `convert_key` **(State Mutators)** (Impact: 6.6)
  * `convert_gamepad_button` **(State Mutators)** (Impact: 3.7)
  * `convert_mouse_button` **(State Mutators)** (Impact: 3.2)
  * `convert_gamepad_axis2d` **(State Mutators)** (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 18`, `args: 5`, `func_start: 5`
* *Risk/State:* `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 9`, `import: 5`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GamepadAxis2DEvent, GamepadButton, GamepadButtonEvent, GamepadControlEvent, GamepadStick, GamepadTrigger, InputEvent, Key...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doom.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 43.16 | **LOC:** 124 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.7131%), Tech Debt (98.2933%)
**Top Internal Functions/Classes:**
  * `draw_frame` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `convert_action` **(State Mutators)** (Impact: 3.6)
  * `get_key` **(Callbacks & Closures)** (Impact: 3.4)
  * `run` **(State Mutators)** (Impact: 3.2)
  * `new` **(Generic / Templated Code)** (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 25`, `args: 12`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 3`, `concurrency: 6`, `import: 7`
* *Defense:* `safety: 3`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DOOM_WIDTH, Frame, KEY_DOWN, KEY_ENTER, KEY_ESCAPE, KEY_FIRE, KEY_LEFT, KEY_RIGHT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/message.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 26.48 | **LOC:** 95 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `class_start: 10`
* *Risk/State:* None
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Direction, Frame, Vec2, lighthouse_client::protocol::Delta
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 26.32 | **LOC:** 90 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.4831%), Tech Debt (25.1327%)
**Top Internal Functions/Classes:**
  * `main` **(Interface Declarations)** (Impact: 7.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 39`, `args: 3`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 16`, `import: 7`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LIGHTHOUSE_URL, Lighthouse, anyhow::Result, clap::Parser, doom::LighthouseDoom, lighthouse_client::protocol::Authentication, std::thread, sync::mpsc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/constants.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 13.56 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DOOMGENERIC_RESY, doomgeneric::game::DOOMGENERIC_RESX
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/updater.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10.84 | **LOC:** 16 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2389%), Tech Debt (37.7541%)
**Top Internal Functions/Classes:**
  * `run` **(Generic / Templated Code)** (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TokioWebSocket, anyhow::Result, crate::message::UpdaterMessage, lighthouse_client::Lighthouse, tokio::sync::mpsc, tracing::debug
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `buildenv.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 3.28 | **LOC:** 5 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Unclassified)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 1`, `api: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.2 | **LOC:** 110 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` screencast.gif, mapper.rs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/mapper.rs` -> **Severity: 5.664** (Embedded: 0.1111 * Error Risk: 50.9739%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/mapper.rs` -> **Severity: 17050.7** (Blast Radius: 170.507 * Doc Risk: 100.0%)
- `src/controller.rs` -> **Severity: 9216.6** (Blast Radius: 92.166 * Doc Risk: 100.0%)
- `src/doom.rs` -> **Severity: 9216.6** (Blast Radius: 92.166 * Doc Risk: 100.0%)
- `src/gui.rs` -> **Severity: 9216.6** (Blast Radius: 92.166 * Doc Risk: 100.0%)
- `src/updater.rs` -> **Severity: 9216.6** (Blast Radius: 92.166 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
