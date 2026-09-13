# ARCHITECTURAL_BRIEF: port_rust_doomgeneric
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/LinusCDE/doomgeneric-rs.git` |
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
| Total Artifacts | 9 |
| Analyzed Artifacts (Scanned) | 5 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4 |
| Total LOC | 166 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 55.6% |
| Dominant Lang | RUST |

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
| RUST | 4 | 166 | 80.0% |
| MARKDOWN | 1 | 0 | 20.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4 | 80.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 20.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Unsupported Format (.toml)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 26.9 | 13.1 | 12.7 | 26.9 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 64.6 | 30.6 | 29.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 43.9 | 37.8 | 37.8 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.5 | 2.4 | 2.4 | 2.5 |
| Connectivity (formerly API Exposure) | 0.0 | 16.4 | 7.7 | 7.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 21.4 | 5.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 91.7 | 29.4 | 12.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 75.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 62.0 | 73.9 | 54.1 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 27 | 3 | 13 | `src/game.rs` |
| cleanup | 0 | 0 | 0 | - |
| guards | 36 | 3 | 22 | `src/input.rs` |
| danger | 4 | 2 | 3 | `src/game.rs` |
| concurrency | 2 | 1 | 2 | `src/game.rs` |
| connectivity | 36 | 3 | 27 | `src/input.rs` |
| io | 1 | 1 | 1 | `build.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 13 | 3 | 7 | `src/lib.rs` |
| debt | 2 | 2 | 1 | `build.rs` |
| mutation | 16 | 3 | 8 | `src/game.rs` |
| dead_code | 9 | 3 | 7 | `src/game.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `build.rs` (Hits: 1)
- `README.md` (Hits: 0)
- `src/game.rs` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **game.rs** (`src/game.rs`) — 9 outbound dependencies
2. **input.rs** (`src/input.rs`) — 3 outbound dependencies
3. **README.md** (`README.md`) — 0 outbound dependencies
4. **build.rs** (`build.rs`) — 0 outbound dependencies
5. **lib.rs** (`src/lib.rs`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main` (@ `build.rs`) -> Impact: **15.8** | LOC: 36
  * *Intent:* // Example custom build script.
- `DG_GetKey` (@ `src/game.rs`) -> Impact: **13.0** | LOC: 17
- `from_char` (@ `src/input.rs`) -> Impact: **4.6** | LOC: 7
- `DG_DrawFrame` (@ `src/game.rs`) -> Impact: **3.4** | LOC: 8
- `DG_SetWindowTitle` (@ `src/game.rs`) -> Impact: **3.3** | LOC: 9
- `draw_frame` (@ `src/game.rs`) -> Impact: **2.3** | LOC: 1
- `init` (@ `src/game.rs`) -> Impact: **1.9** | LOC: 9
- `set_window_title` (@ `src/game.rs`) -> Impact: **1.8** | LOC: 1
- `DG_SleepMs` (@ `src/game.rs`) -> Impact: **1.6** | LOC: 4
- `get_key` (@ `src/game.rs`) -> Impact: **1.5** | LOC: 1

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 3 | 98.22 | 8.45% | 45.92% |
| `__monolith__` | 2 | 23.4 | 13.45% | 18.88% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/game.rs` -> **99.9961%** Exposure
- `build.rs` -> **37.7541%** Exposure
- `src/input.rs` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `build.rs` -> **91.6827%** Exposure
- `src/game.rs` -> **25.8902%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/game.rs` -> **7** Orphaned Functions | **0** Duplicates
- `build.rs` -> **1** Orphaned Functions | **0** Duplicates
- `src/input.rs` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `12` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/game.rs` (RUST) -> Cumulative Risk: **429.94**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 52.68 | **LOC:** 109 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9961%), Documentation (93.75%), Safety Score (57.9145%)
- **Heaviest Functions:** `DG_GetKey` (Impact: 13.0), `DG_DrawFrame` (Impact: 3.4), `DG_SetWindowTitle` (Impact: 3.3)

### 2. `build.rs` (RUST) -> Cumulative Risk: **377.44**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 22.4 | **LOC:** 38 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (91.6827%), Safety Score (64.5656%), Documentation (54.076%)
- **Heaviest Functions:** `main` (Impact: 15.8)

### 3. `src/input.rs` (RUST) -> Cumulative Risk: **262.27**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 32.5 | **LOC:** 57 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (37.7541%), Api Exposure (16.413%)
- **Heaviest Functions:** `from_char` (Impact: 4.6)

### 4. `src/lib.rs` (RUST) -> Cumulative Risk: **7.89**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 13.04 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (5.5883%), Verification (2.2977%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/game.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 52.68 | **LOC:** 109 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.5895%), Tech Debt (99.9961%)
**Top Internal Functions/Classes:**
  * `DG_GetKey` (Impact: 13.0)
  * `DG_DrawFrame` (Impact: 3.4)
  * `DG_SetWindowTitle` (Impact: 3.3)
  * `draw_frame` (Impact: 2.3)
  * `init` (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 28`, `args: 15`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`, `planned_debt: 1`, `unreferenced_by_name: 7`
* *Architecture:* `api: 7`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 200.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Instant, crate::input::KeyData, once_cell::sync::Lazy, std::cell::RefCell, std::convert::TryFrom, std::ffi::CStr, std::os::raw, std::thread::sleep...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/input.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 32.5 | **LOC:** 57 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.7533%), Tech Debt (37.7541%)
**Top Internal Functions/Classes:**
  * `from_char` (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 6`, `args: 11`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `doc: 5`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 200.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` once_cell::sync::Lazy, std::os::raw, super::key_bindings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build.rs` (RUST | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 22.4 | **LOC:** 38 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.8941%), Tech Debt (37.7541%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 15.8)
    * *Intent:* // Example custom build script.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 8`, `args: 5`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 200.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 13.04 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 200.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 49 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 200.0
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

- `src/input.rs` -> **Severity: 20000.0** (Blast Radius: 200.0 * Doc Risk: 100.0%)
- `src/game.rs` -> **Severity: 18750.0** (Blast Radius: 200.0 * Doc Risk: 93.75%)
- `build.rs` -> **Severity: 10815.2** (Blast Radius: 200.0 * Doc Risk: 54.076%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
