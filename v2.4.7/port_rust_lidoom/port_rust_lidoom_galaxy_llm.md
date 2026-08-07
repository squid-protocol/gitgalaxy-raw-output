# ARCHITECTURAL_BRIEF: port_rust_lidoom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/port_rust_lidoom` |
| **Timestamp** | `2026-08-07T03:29:50.617865+00:00` |
| **Scan Duration** | `0.1s` |
| **Git Branch** | `main` |
| **Git Commit** | `57dd73a1c613730ad303ac375247230640fa4b64` |
| **Git Remote** | `https://github.com/fwcd/lidoom.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 9 malicious artifacts.

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
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 8 | 636 | 80.0% |
| MARKDOWN | 1 | 0 | 10.0% |
| SHELL | 1 | 4 | 10.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.449`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4 | 40.0% |
| file_cluster_13 | 3 | 30.0% |
| file_cluster_4 | 2 | 20.0% |

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

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 81.9 | 30.5 | 24.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 93.7 | 27.0 | 5.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 93.1 | 16.1 | 0.0 | 0.0 |
| Testing Exposure | 0.5 | 2.5 | 2.0 | 2.4 | 0.8 |
| API Exposure | 0.0 | 5.8 | 2.8 | 2.4 | 5.8 |
| Concurrency Exposure | 0.0 | 100.0 | 64.7 | 97.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 38.5 | 12.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 80.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 69.9 | 24.4 | 22.9 | 3.2 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `buildenv.sh` (Hits: 1)
- `README.md` (Hits: 0)
- `src/constants.rs` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`README.md`) — 0 inbound connections
2. **buildenv.sh** (`buildenv.sh`) — 0 inbound connections
3. **constants.rs** (`src/constants.rs`) — 0 inbound connections
4. **controller.rs** (`src/controller.rs`) — 0 inbound connections
5. **doom.rs** (`src/doom.rs`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **doom.rs** (`src/doom.rs`) — 27 outbound dependencies
2. **gui.rs** (`src/gui.rs`) — 22 outbound dependencies
3. **controller.rs** (`src/controller.rs`) — 18 outbound dependencies
4. **mapper.rs** (`src/mapper.rs`) — 13 outbound dependencies
5. **main.rs** (`src/main.rs`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run` (@ `src/gui.rs`) -> Impact: **63.4** | LOC: 108
- `run` (@ `src/mapper.rs`) -> Impact: **58.1** | LOC: 83
- `run` (@ `src/controller.rs`) -> Impact: **27.9** | LOC: 37
- `draw_frame` (@ `src/doom.rs`) -> Impact: **12.9** | LOC: 34
- `main` (@ `src/main.rs`) -> Impact: **11.6** | LOC: 58
- `convert_key` (@ `src/controller.rs`) -> Impact: **8.9** | LOC: 19
- `gamepad_button_to_action` (@ `src/mapper.rs`) -> Impact: **8.8** | LOC: 16
- `convert_key` (@ `src/gui.rs`) -> Impact: **6.1** | LOC: 42
- `run` (@ `src/updater.rs`) -> Impact: **5.6** | LOC: 8
- `convert_gamepad_button` (@ `src/controller.rs`) -> Impact: **4.9** | LOC: 18

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 8 | 467.42 | 33.67% | 18.07% |
| `__monolith__` | 2 | 6.48 | 2.5% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/doom.rs` -> **93.0674%** Exposure
- `src/main.rs` -> **25.1327%** Exposure
- `src/gui.rs` -> **13.7842%** Exposure
- `src/controller.rs` -> **12.5845%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/updater.rs` -> **99.95%** Exposure
- `src/gui.rs` -> **97.6645%** Exposure
- `src/doom.rs` -> **86.6672%** Exposure
- `src/mapper.rs` -> **49.7015%** Exposure
- `src/controller.rs` -> **12.4492%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/doom.rs` -> **3** Orphaned Functions | **0** Duplicates
- `src/main.rs` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/controller.rs`** -> AI Confidence: **99.31%**
2. **`src/gui.rs`** -> AI Confidence: **99.31%**
3. **`src/mapper.rs`** -> AI Confidence: **99.31%**
4. **`src/doom.rs`** -> AI Confidence: **99.18%**
5. **`src/main.rs`** -> AI Confidence: **99.08%**
6. **`buildenv.sh`** -> AI Confidence: **99.06%**
7. **`src/constants.rs`** -> AI Confidence: **98.84%**
8. **`src/message.rs`** -> AI Confidence: **98.84%**
9. **`src/updater.rs`** -> AI Confidence: **98.83%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `103` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/doom.rs` (RUST) -> Cumulative Risk: **452.14**
- **Archetype:** `file_cluster_13` (Distance: 12.238 IQR)
- **Magnitude:** 55.16 | **LOC:** 124 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (93.0674%), State Flux (86.6672%), Concurrency (85.1953%)
- **Heaviest Functions:** `draw_frame` (Impact: 12.9), `convert_action` (Impact: 4.8), `get_key` (Impact: 4.5)

### 2. `src/gui.rs` (RUST) -> Cumulative Risk: **394.25**
- **Archetype:** `file_cluster_13` (Distance: 14.725 IQR)
- **Magnitude:** 112.9 | **LOC:** 171 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.6645%), Concurrency (97.0279%), Cognitive Load (49.6667%)
- **Heaviest Functions:** `run` (Impact: 63.4), `convert_key` (Impact: 6.1), `convert_mouse_button` (Impact: 4.4)

### 3. `src/mapper.rs` (RUST) -> Cumulative Risk: **377.08**
- **Archetype:** `file_cluster_4` (Distance: 12.36 IQR)
- **Magnitude:** 123.18 | **LOC:** 145 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), Cognitive Load (81.8685%), State Flux (49.7015%)
- **Heaviest Functions:** `run` (Impact: 58.1), `gamepad_button_to_action` (Impact: 8.8), `key_to_action` (Impact: 4.9)

### 4. `src/main.rs` (RUST) -> Cumulative Risk: **342.78**
- **Archetype:** `file_cluster_8` (Distance: 9.424 IQR)
- **Magnitude:** 29.02 | **LOC:** 90 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9988%), Safety Score (87.4183%), Cognitive Load (27.857%)
- **Heaviest Functions:** `main` (Impact: 11.6)

### 5. `src/updater.rs` (RUST) -> Cumulative Risk: **334.4**
- **Archetype:** `file_cluster_4` (Distance: 14.199 IQR)
- **Magnitude:** 28.84 | **LOC:** 16 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (99.95%), Spec Match (80.0%), Documentation (23.9022%)
- **Heaviest Functions:** `run` (Impact: 5.6)

### 6. `src/controller.rs` (RUST) -> Cumulative Risk: **319.92**
- **Archetype:** `file_cluster_8` (Distance: 13.257 IQR)
- **Magnitude:** 78.28 | **LOC:** 102 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (75.6729%), Documentation (15.1376%)
- **Heaviest Functions:** `run` (Impact: 27.9), `convert_key` (Impact: 8.9), `convert_gamepad_button` (Impact: 4.9)

### 7. `src/message.rs` (RUST) -> Cumulative Risk: **177.41**
- **Archetype:** `file_cluster_8` (Distance: 7.601 IQR)
- **Magnitude:** 26.48 | **LOC:** 95 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (69.8555%), Api Exposure (5.2535%), Verification (2.2977%)

### 8. `buildenv.sh` (SHELL) -> Cumulative Risk: **135.09**
- **Archetype:** `file_cluster_8` (Distance: 10.573 IQR)
- **Magnitude:** 4.28 | **LOC:** 5 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (93.7027%), Spec Match (26.6667%), Api Exposure (5.7813%), Cognitive Load (5.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 3.2)

### 9. `src/constants.rs` (RUST) -> Cumulative Risk: **46.33**
- **Archetype:** `file_cluster_13` (Distance: 6.468 IQR)
- **Magnitude:** 13.56 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (20.0%), Documentation (16.2862%), Cognitive Load (5.0%), Api Exposure (4.5816%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/mapper.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.36 IQR)
- **Top Global Matches:** file_cluster_4: 12.36, file_cluster_8: 12.472, file_cluster_13: 12.568
- **Magnitude:** 123.18 | **LOC:** 145 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.8685%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 58.1)
  * `gamepad_button_to_action` (Impact: 8.8)
  * `key_to_action` (Impact: 4.9)
  * `movement_dir_to_action` (Impact: 4.4)
  * `camera_dir_to_action` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 32`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 1`, `concurrency: 31`, `import: 5`
* *Defense:* `safety: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 100.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Key, MouseButton, crate::message::Action, MapperMessage, GamepadTrigger, GamepadButton, ControllerMessage, tokio::sync::mpsc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/gui.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.725 IQR)
- **Top Global Matches:** file_cluster_13: 14.725, file_cluster_11: 14.794, file_cluster_4: 14.812
- **Magnitude:** 112.9 | **LOC:** 171 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.6667%), Tech Debt (13.7842%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 63.4)
  * `convert_key` (Impact: 6.1)
  * `convert_mouse_button` (Impact: 4.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 34`, `args: 9`, `func_start: 3`
* *Risk/State:* `state_mutation: 23`, `planned_debt: 2`
* *Architecture:* `api: 1`, `concurrency: 12`, `import: 7`
* *Defense:* `safety: 108`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 100.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` message::ControllerMessage, MouseButton, sdl2::event::Event, Zero, LIGHTHOUSE_ROWS, crate::constants::DOOM_HEIGHT, anyhow::anyhow, tracing::info...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/controller.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.257 IQR)
- **Top Global Matches:** file_cluster_8: 13.257, file_cluster_4: 13.261, file_cluster_13: 13.353
- **Magnitude:** 78.28 | **LOC:** 102 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6729%), Tech Debt (12.5845%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 27.9)
  * `convert_key` (Impact: 8.9)
  * `convert_gamepad_button` (Impact: 4.9)
  * `convert_mouse_button` (Impact: 4.4)
  * `convert_gamepad_axis2d` (Impact: 4.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 18`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 1`
* *Architecture:* `api: 1`, `concurrency: 24`, `import: 5`
* *Defense:* `safety: 57`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 100.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MouseButton, Key, ServerMessage, InputEvent, GamepadTrigger, GamepadButtonEvent, futures::prelude::*, GamepadButton...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doom.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.238 IQR)
- **Top Global Matches:** file_cluster_13: 12.238, file_cluster_0: 12.24, file_cluster_8: 12.468
- **Magnitude:** 55.16 | **LOC:** 124 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.307%), Tech Debt (93.0674%)
**Top Internal Functions/Classes:**
  * `draw_frame` (Impact: 12.9)
  * `convert_action` (Impact: 4.8)
  * `get_key` (Impact: 4.5)
  * `run` (Impact: 3.8)
  * `new` (Impact: 2.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 25`, `args: 12`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 11`, `planned_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 3`, `concurrency: 6`, `import: 7`
* *Defense:* `safety: 15`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 100.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` KEY_ESCAPE, KEY_UP, crate::message::GUIMessage, KeyData, LIGHTHOUSE_ROWS, crate::constants::DOOM_HEIGHT, KEY_LEFT, KEY_FIRE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.424 IQR)
- **Top Global Matches:** file_cluster_8: 9.424, file_cluster_0: 9.575, file_cluster_13: 9.583
- **Magnitude:** 29.02 | **LOC:** 90 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.857%), Tech Debt (25.1327%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 11.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 39`, `args: 3`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 16`, `import: 7`
* *Defense:* `safety: 3`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 100.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` clap::Parser, Lighthouse, tokio::runtime::Runtime, lighthouse_client::protocol::Authentication, LIGHTHOUSE_URL, task, doom::LighthouseDoom, tracing::info...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/updater.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.199 IQR)
- **Top Global Matches:** file_cluster_4: 14.199, file_cluster_13: 14.395, file_cluster_16: 14.98
- **Magnitude:** 28.84 | **LOC:** 16 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `concurrency: 19`, `import: 5`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 100.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lighthouse_client::Lighthouse, crate::message::UpdaterMessage, tracing::debug, tokio::sync::mpsc, anyhow::Result, TokioWebSocket
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/message.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.601 IQR)
- **Top Global Matches:** file_cluster_8: 7.601, file_cluster_7: 8.107, file_cluster_0: 8.259
- **Magnitude:** 26.48 | **LOC:** 95 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `class_start: 10`
* *Risk/State:* None
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 100.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Vec2, Direction, Frame, lighthouse_client::protocol::Delta
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/constants.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.468 IQR)
- **Top Global Matches:** file_cluster_13: 6.468, file_cluster_8: 6.474, file_cluster_7: 7.473
- **Magnitude:** 13.56 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 100.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DOOMGENERIC_RESY, doomgeneric::game::DOOMGENERIC_RESX
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `buildenv.sh` (SHELL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.573 IQR)
- **Top Global Matches:** file_cluster_8: 10.573, file_cluster_12: 10.773, file_cluster_0: 11.04
- **Magnitude:** 4.28 | **LOC:** 5 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 1`, `api: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 100.0
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 100.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/doom.rs` (RUST) | Magnitude: 55.16 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 25, safety: 15, args: 12
- `src/constants.rs` (RUST) | Magnitude: 13.56 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 2, immutability_locks: 2, encapsulation: 2, structural_boundaries: 1
- `src/gui.rs` (RUST) | Magnitude: 112.9 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 136, safety: 108, structural_boundaries: 34, branch: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/mapper.rs` (RUST) | Magnitude: 123.18 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 118, safety: 41, branch: 32, structural_boundaries: 32
- `src/updater.rs` (RUST) | Magnitude: 28.84 | Delta: **0.196 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 19, structural_boundaries: 9, safety: 5, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/controller.rs` (RUST) | Magnitude: 78.28 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 73, safety: 57, concurrency: 24, branch: 18
- `src/main.rs` (RUST) | Magnitude: 29.02 | Delta: **0.151 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 39, concurrency: 16, safety_bypasses: 12
- `buildenv.sh` (SHELL) | Magnitude: 4.28 | Delta: **0.2 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 2, safety_bypasses: 2, indent_spaces: 2, structural_boundaries: 1
- `src/message.rs` (RUST) | Magnitude: 26.48 | Delta: **0.506 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 41, decorators: 12, structural_boundaries: 11, class_start: 10

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/message.rs` -> **Severity: 6985.55** (Blast Radius: 100.0 * Doc Risk: 69.8555%)
- `src/mapper.rs` -> **Severity: 3632.84** (Blast Radius: 100.0 * Doc Risk: 36.3284%)
- `src/gui.rs` -> **Severity: 3219.79** (Blast Radius: 100.0 * Doc Risk: 32.1979%)
- `src/updater.rs` -> **Severity: 2390.22** (Blast Radius: 100.0 * Doc Risk: 23.9022%)
- `src/doom.rs` -> **Severity: 2293.13** (Blast Radius: 100.0 * Doc Risk: 22.9313%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
