# ARCHITECTURAL_BRIEF: port_rust_doomgeneric
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/port_rust_doomgeneric` |
| **Timestamp** | `2026-08-03T19:06:14.800202+00:00` |
| **Scan Duration** | `0.13s` |
| **Git Branch** | `main` |
| **Git Commit** | `a8941bf227d80cabd9a3212bd190a180fcf18d3f` |
| **Git Remote** | `https://github.com/LinusCDE/doomgeneric-rs.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3 malicious artifacts.

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
| Total Artifacts | 9 |
| Analyzed Artifacts (Scanned) | 4 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 136 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 44.4% |
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
| RUST | 3 | 136 | 75.0% |
| MARKDOWN | 1 | 0 | 25.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 2`
> **Architectural Drift Z-Score:** `6.521`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 1 | 25.0% |
| file_cluster_8 | 1 | 25.0% |
| file_cluster_7 | 1 | 25.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 25.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Unsupported Format (.toml)
- `.rs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 61.7 | 22.7 | 6.3 | 61.7 |
| Error & Exception Exposure | 0.0 | 25.8 | 8.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 47.7 | 43.1 | 100.0 |
| Testing Exposure | 0.3 | 2.6 | 1.8 | 2.4 | 2.6 |
| API Exposure | 4.4 | 8.2 | 5.7 | 4.4 | 4.4 |
| Concurrency Exposure | 0.0 | 21.4 | 7.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.7 | 33.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 71.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 1.6 | 100.0 | 67.0 | 99.3 | 99.3 |
| Algorithmic DoS Exposure | 0.0 | 87.7 | 30.6 | 4.2 | 87.7 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 19.7 | 7.7 | 3.4 | 3.4 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `README.md` (Hits: 0)
- `src/game.rs` (Hits: 0)
- `src/input.rs` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`README.md`) — 0 inbound connections
2. **game.rs** (`src/game.rs`) — 0 inbound connections
3. **input.rs** (`src/input.rs`) — 0 inbound connections
4. **lib.rs** (`src/lib.rs`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **game.rs** (`src/game.rs`) — 9 outbound dependencies
2. **input.rs** (`src/input.rs`) — 3 outbound dependencies
3. **README.md** (`README.md`) — 0 outbound dependencies
4. **lib.rs** (`src/lib.rs`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `DG_GetKey` (@ `src/game.rs`) -> Impact: **25.1** | LOC: 17
- `from_char` (@ `src/input.rs`) -> Impact: **12.3** | LOC: 7
- `DG_DrawFrame` (@ `src/game.rs`) -> Impact: **10.8** | LOC: 8
- `DG_SetWindowTitle` (@ `src/game.rs`) -> Impact: **7.2** | LOC: 9
- `init` (@ `src/game.rs`) -> Impact: **4.4** | LOC: 9
- `DG_Init` (@ `src/game.rs`) -> Impact: **3.0** | LOC: 8
- `DG_GetTicksMs` (@ `src/game.rs`) -> Impact: **2.8** | LOC: 5
- `tick` (@ `src/game.rs`) -> Impact: **2.8** | LOC: 5
- `set_window_title` (@ `src/game.rs`) -> Impact: **2.3** | LOC: 12
- `DG_SleepMs` (@ `src/game.rs`) -> Impact: **2.2** | LOC: 4

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `DG_GetKey` (@ `src/game.rs`) -> **O(N^3)**
- `DG_DrawFrame` (@ `src/game.rs`) -> **O(N^3)**
- `from_char` (@ `src/input.rs`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `set_window_title` (@ `src/game.rs`) -> DB Complexity: **5**
- `DG_GetKey` (@ `src/game.rs`) -> DB Complexity: **2**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 3 | 147.62 | 22.68% | 47.7% |
| `__monolith__` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/game.rs` -> **99.9961%** Exposure
- `src/input.rs` -> **43.0999%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/game.rs` -> **99.7308%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/game.rs` -> **7** Orphaned Functions | **0** Duplicates
- `src/input.rs` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/game.rs`** -> AI Confidence: **99.18%**
2. **`src/input.rs`** -> AI Confidence: **99.09%**
3. **`src/lib.rs`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/input.rs` -> **19.7306%** Exposure
- `src/game.rs` -> **3.4334%** Exposure
### Algorithmic DoS Exposure
- `src/game.rs` -> **87.7012%** Exposure
- `src/input.rs` -> **4.2477%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `12` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/game.rs` (RUST) -> Cumulative Risk: **606.19**
- **Archetype:** `file_cluster_0` (Distance: 13.735 IQR)
- **Magnitude:** 94.38 | **LOC:** 109 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9961%), State Flux (99.7308%), Documentation (99.3484%)
- **Heaviest Functions:** `DG_GetKey` (Impact: 25.1), `DG_DrawFrame` (Impact: 10.8), `DG_SetWindowTitle` (Impact: 7.2)

### 2. `src/input.rs` (RUST) -> Cumulative Risk: **284.02**
- **Archetype:** `file_cluster_8` (Distance: 10.232 IQR)
- **Magnitude:** 40.2 | **LOC:** 57 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (43.0999%), Logic Bomb (19.7306%)
- **Heaviest Functions:** `from_char` (Impact: 12.3)

### 3. `src/lib.rs` (RUST) -> Cumulative Risk: **19.65**
- **Archetype:** `file_cluster_7` (Distance: 10.602 IQR)
- **Magnitude:** 13.04 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (13.3333%), Api Exposure (4.4211%), Documentation (1.5894%), Verification (0.3064%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/game.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.735 IQR)
- **Top Global Matches:** file_cluster_0: 13.735, file_cluster_13: 13.781, file_cluster_11: 14.021
- **Magnitude:** 94.38 | **LOC:** 109 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (61.711%), Tech Debt (99.9961%)
**Top Internal Functions/Classes:**
  * `DG_GetKey` (Impact: 25.1 | O(N^3) | DB: 2)
  * `DG_DrawFrame` (Impact: 10.8 | O(N^3))
  * `DG_SetWindowTitle` (Impact: 7.2 | O(N^2))
  * `init` (Impact: 4.4 | O(N^2))
  * `DG_Init` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 28`, `args: 15`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 24`, `planned_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 7`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 26`, `doc: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 250.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::input::KeyData, std::convert::TryFrom, std::os::raw, std::thread::sleep, std::time::Duration, Instant, std::cell::RefCell, std::ffi::CStr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/input.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.232 IQR)
- **Top Global Matches:** file_cluster_8: 10.232, file_cluster_13: 10.375, file_cluster_7: 10.561
- **Magnitude:** 40.2 | **LOC:** 57 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.3191%), Tech Debt (43.0999%)
**Top Internal Functions/Classes:**
  * `from_char` (Impact: 12.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 6`, `args: 11`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `safety: 3`, `doc: 5`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 250.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::key_bindings, once_cell::sync::Lazy, std::os::raw
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_7` (Drift: 10.602 IQR)
- **Top Global Matches:** file_cluster_7: 10.602, file_cluster_8: 10.77, file_cluster_1: 10.858
- **Magnitude:** 13.04 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 250.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 49 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 250.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/game.rs` (RUST) | Magnitude: 94.38 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 28, safety: 26, state_mutation: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/lib.rs` (RUST) | Magnitude: 13.04 | Delta: **0.168 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 2, api: 2, encapsulation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/input.rs` (RUST) | Magnitude: 40.2 | Delta: **0.143 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, api: 27, encapsulation: 27, immutability_locks: 22

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/input.rs` -> **Severity: 25000.0** (Blast Radius: 250.0 * Doc Risk: 100.0%)
- `src/game.rs` -> **Severity: 24837.1** (Blast Radius: 250.0 * Doc Risk: 99.3484%)
- `src/lib.rs` -> **Severity: 397.35** (Blast Radius: 250.0 * Doc Risk: 1.5894%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
