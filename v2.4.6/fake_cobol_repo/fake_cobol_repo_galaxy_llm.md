# ARCHITECTURAL_BRIEF: fake_cobol_repo
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/fake_cobol_repo` |
| **Timestamp** | `2026-08-03T19:28:51.734572+00:00` |
| **Scan Duration** | `0.13s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
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
| Total Artifacts | 3 |
| Analyzed Artifacts (Scanned) | 3 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 0 |
| Total LOC | 80 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 100.0% |
| Dominant Lang | COBOL |

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
| COBOL | 3 | 80 | 100.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `8.979`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 3 | 100.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 0*


## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 16.8 | 67.6 | 39.4 | 33.9 | 16.8 |
| Error & Exception Exposure | 20.6 | 80.0 | 41.9 | 25.1 | 20.6 |
| Tech Debt Exposure | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Testing Exposure | 2.4 | 2.6 | 2.5 | 2.5 | 2.4 |
| API Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 47.5 | 99.0 | 79.2 | 91.2 | 47.5 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 68.5 | 95.3 | 84.5 | 89.7 | 95.3 |
| Algorithmic DoS Exposure | 3.1 | 19.7 | 8.8 | 3.7 | 3.1 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 14.0 | 4.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 33.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `DIRTY02.cbl` (Hits: 6)
- `CLEAN01.cbl` (Hits: 3)
- `DIRTY03.cbl` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CLEAN01.cbl** (`CLEAN01.cbl`) — 0 inbound connections
2. **DIRTY02.cbl** (`DIRTY02.cbl`) — 0 inbound connections
3. **DIRTY03.cbl** (`DIRTY03.cbl`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CLEAN01.cbl** (`CLEAN01.cbl`) — 0 outbound dependencies
2. **DIRTY02.cbl** (`DIRTY02.cbl`) — 0 outbound dependencies
3. **DIRTY03.cbl** (`DIRTY03.cbl`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `000-MAIN` (@ `DIRTY03.cbl`) -> Impact: **3.3** | LOC: 6
- `000-MAIN` (@ `DIRTY02.cbl`) -> Impact: **3.2** | LOC: 5
- `000-MAIN` (@ `CLEAN01.cbl`) -> Impact: **1.8** | LOC: 6
- `300-NORMAL-PATH` (@ `DIRTY02.cbl`) -> Impact: **1.8** | LOC: 6
- `100-SAFE-PATH` (@ `DIRTY02.cbl`) -> Impact: **1.6** | LOC: 2
- `200-DANGER-PATH` (@ `DIRTY02.cbl`) -> Impact: **1.6** | LOC: 3
- `400-PHANTOM-PARA` (@ `DIRTY02.cbl`) -> Impact: **1.6** | LOC: 3
- `999-GHOST-TOWN` (@ `DIRTY03.cbl`) -> Impact: **1.6** | LOC: 2

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Data Gravity (Database Complexity)
- `000-MAIN` (@ `CLEAN01.cbl`) -> DB Complexity: **10**
- `000-MAIN` (@ `DIRTY02.cbl`) -> DB Complexity: **10**
- `300-NORMAL-PATH` (@ `DIRTY02.cbl`) -> DB Complexity: **10**
- `000-MAIN` (@ `DIRTY03.cbl`) -> DB Complexity: **10**
- `999-GHOST-TOWN` (@ `DIRTY03.cbl`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 3 | 27.1 | 39.43% | 99.99% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `DIRTY02.cbl` -> **100.0%** Exposure
- `DIRTY03.cbl` -> **99.9984%** Exposure
- `CLEAN01.cbl` -> **99.9842%** Exposure
### Highest State Flux (Mutation/Volatility)
- `DIRTY03.cbl` -> **98.9714%** Exposure
- `DIRTY02.cbl` -> **91.2492%** Exposure
- `CLEAN01.cbl` -> **47.5021%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `DIRTY02.cbl` -> **5** Orphaned Functions | **0** Duplicates
- `DIRTY03.cbl` -> **2** Orphaned Functions | **0** Duplicates
- `CLEAN01.cbl` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`CLEAN01.cbl`** -> AI Confidence: **98.84%**
2. **`DIRTY02.cbl`** -> AI Confidence: **98.83%**
3. **`DIRTY03.cbl`** -> AI Confidence: **98.83%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `DIRTY02.cbl` -> **13.9831%** Exposure
### Weaponizable Injection Vectors
- `DIRTY02.cbl` -> **99.9998%** Exposure
### Algorithmic DoS Exposure
- `DIRTY02.cbl` -> **19.7305%** Exposure
- `DIRTY03.cbl` -> **3.7018%** Exposure
- `CLEAN01.cbl` -> **3.1033%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `0` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `DIRTY02.cbl` (COBOL) -> Cumulative Risk: **693.61**
- **Archetype:** `file_cluster_8` (Distance: 9.138 IQR)
- **Magnitude:** 14.52 | **LOC:** 37 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Injection Surface (99.9998%), State Flux (91.2492%)
- **Heaviest Functions:** `000-MAIN` (Impact: 3.2), `300-NORMAL-PATH` (Impact: 1.8), `100-SAFE-PATH` (Impact: 1.6)

### 2. `DIRTY03.cbl` (COBOL) -> Cumulative Risk: **503.93**
- **Archetype:** `file_cluster_8` (Distance: 9.294 IQR)
- **Magnitude:** 9.38 | **LOC:** 25 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9984%), State Flux (98.9714%), Documentation (89.7216%)
- **Heaviest Functions:** `000-MAIN` (Impact: 3.3), `999-GHOST-TOWN` (Impact: 1.6)

### 3. `CLEAN01.cbl` (COBOL) -> Cumulative Risk: **435.6**
- **Archetype:** `file_cluster_8` (Distance: 7.658 IQR)
- **Magnitude:** 3.2 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9842%), Documentation (95.2574%), Stability (50.0%)
- **Heaviest Functions:** `000-MAIN` (Impact: 1.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `DIRTY02.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.138 IQR)
- **Top Global Matches:** file_cluster_8: 9.138, file_cluster_7: 9.921, file_cluster_0: 9.973
- **Magnitude:** 14.52 | **LOC:** 37 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (67.5536%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `000-MAIN` (Impact: 3.2 | O(N^2) | DB: 10)
  * `300-NORMAL-PATH` (Impact: 1.8 | O(N^2) | DB: 10)
  * `100-SAFE-PATH` (Impact: 1.6 | O(N^2))
  * `200-DANGER-PATH` (Impact: 1.6 | O(N^2))
  * `400-PHANTOM-PARA` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 10`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 4`, `orphaned_logic: 5`
* *Architecture:* `io: 6`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 333.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `DIRTY03.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.294 IQR)
- **Top Global Matches:** file_cluster_8: 9.294, file_cluster_7: 10.095, file_cluster_1: 10.269
- **Magnitude:** 9.38 | **LOC:** 25 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (33.9244%), Tech Debt (99.9984%)
**Top Internal Functions/Classes:**
  * `000-MAIN` (Impact: 3.3 | O(N^2) | DB: 10)
  * `999-GHOST-TOWN` (Impact: 1.6 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 9`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `orphaned_logic: 2`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 333.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CLEAN01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.658 IQR)
- **Top Global Matches:** file_cluster_8: 7.658, file_cluster_7: 8.644, file_cluster_1: 8.812
- **Magnitude:** 3.2 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (16.7982%), Tech Debt (99.9842%)
**Top Internal Functions/Classes:**
  * `000-MAIN` (Impact: 1.8 | O(N^2) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 333.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `DIRTY02.cbl` (COBOL) | Magnitude: 14.52 | Delta: **0.783 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 10, io: 6, func_start: 5
- `DIRTY03.cbl` (COBOL) | Magnitude: 9.38 | Delta: **0.801 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 9, state_mutation: 4, io: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `CLEAN01.cbl` -> **Severity: 31752.435** (Blast Radius: 333.333 * Doc Risk: 95.2574%)
- `DIRTY03.cbl` -> **Severity: 29907.17** (Blast Radius: 333.333 * Doc Risk: 89.7216%)
- `DIRTY02.cbl` -> **Severity: 22840.01** (Blast Radius: 333.333 * Doc Risk: 68.5201%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
