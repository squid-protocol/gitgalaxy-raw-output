# ARCHITECTURAL_BRIEF: Apollo-11
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/Apollo-11` |
| **Timestamp** | `2026-08-03T19:03:10.588712+00:00` |
| **Scan Duration** | `1.29s` |
| **Git Branch** | `master` |
| **Git Commit** | `247dd7d0d1b0e7f9f270750ec08983e0a72e73e1` |
| **Git Remote** | `https://github.com/chrislgarry/Apollo-11` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

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
| Total Artifacts | 262 |
| Analyzed Artifacts (Scanned) | 246 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16 |
| Total LOC | 74063 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 93.9% |
| Dominant Lang | AGC_ASSEMBLY |

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
| AGC_ASSEMBLY | 171 | 74063 | 69.5% |
| MARKDOWN | 74 | 0 | 30.1% |
| PLAINTEXT | 1 | 0 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.098`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 118 | 48.0% |
| file_cluster_13 | 32 | 13.0% |
| file_cluster_4 | 15 | 6.1% |
| file_cluster_7 | 4 | 1.6% |
| file_cluster_9 | 2 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 75 | 30.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 16*

**Composition by Extension & Reason:**
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.agc`: 1x Excluded (Lexical Monotony: High structural repetition detected in 3786 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2636 LOC)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lockb`: 1x Excluded (Unsupported Extension: '.lockb')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 73.2 | 39.2 | 44.7 | 0.0 |
| Error & Exception Exposure | 0.0 | 96.4 | 29.1 | 21.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.4 | 24.5 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 46.4 | 80.0 | 80.0 |
| API Exposure | 0.0 | 7.0 | 0.5 | 0.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 36.0 | 17.9 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 85.4 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 12.7 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 62.1 | 81.8 | 0.0 |
| Instability Exposure | 0.0 | 3.9 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 49.5 | 0.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 100.0 | 23.8 | 11.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 1.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Luminary099/P51-P53.agc` (Hits: 21)
- `Comanche055/P61-P67.agc` (Hits: 20)
- `Luminary099/EXTENDED_VERBS.agc` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
2. **README.md** (`Comanche055/README.md`) — 0 inbound connections
3. **LICENSE.md** (`LICENSE.md`) — 0 inbound connections
4. **README.md** (`Luminary099/README.md`) — 0 inbound connections
5. **README.md** (`README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **TAGS_FOR_RELATIVE_SETLOC.agc** (`Comanche055/TAGS_FOR_RELATIVE_SETLOC.agc`) — 40 outbound dependencies
2. **P20-P25.agc** (`Comanche055/P20-P25.agc`) — 38 outbound dependencies
3. **P20-P25.agc** (`Luminary099/P20-P25.agc`) — 36 outbound dependencies
4. **FRESH_START_AND_RESTART.agc** (`Comanche055/FRESH_START_AND_RESTART.agc`) — 35 outbound dependencies
5. **PINBALL_GAME_BUTTONS_AND_LIGHTS.agc** (`Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc`) — 35 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `R60CALL` (@ `Comanche055/P20-P25.agc`) -> Impact: **206.2** | LOC: 453
- `P23` (@ `Comanche055/P20-P25.agc`) -> Impact: **85.8** | LOC: 117
- `EJSCAN` (@ `Luminary099/EXECUTIVE.agc`) -> Impact: **68.5** | LOC: 54
- `VERB69` (@ `Comanche055/EXTENDED_VERBS.agc`) -> Impact: **65.7** | LOC: 33
- `VERB69` (@ `Luminary099/EXTENDED_VERBS.agc`) -> Impact: **65.7** | LOC: 33
- `EJSCAN` (@ `Comanche055/EXECUTIVE.agc`) -> Impact: **61.3** | LOC: 48
- `CHARIN2` (@ `Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc`) -> Impact: **60.8** | LOC: 39
- `REP11A` (@ `Comanche055/P11.agc`) -> Impact: **53.0** | LOC: 140
- `RATEZRO` (@ `Comanche055/P40-P47.agc`) -> Impact: **50.5** | LOC: 247
- `DSPOPTN` (@ `Luminary099/P51-P53.agc`) -> Impact: **46.2** | LOC: 84

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `SMODECHK` (@ `Comanche055/AGC_BLOCK_TWO_SELF-CHECK.agc`) -> **O(2^N) [Recursive]**
- `CNTRLOOP` (@ `Comanche055/AGC_BLOCK_TWO_SELF-CHECK.agc`) -> **O(2^N) [Recursive]**
- `DOBRATE1` (@ `Comanche055/CM_ENTRY_DIGITAL_AUTOPILOT.agc`) -> **O(2^N) [Recursive]**
- `NOTYET` (@ `Comanche055/CM_ENTRY_DIGITAL_AUTOPILOT.agc`) -> **O(2^N) [Recursive]**
- `CMNTOVFL` (@ `Comanche055/CONIC_SUBROUTINES.agc`) -> **O(2^N) [Recursive]**
- `VERB69` (@ `Comanche055/EXTENDED_VERBS.agc`) -> **O(2^N) [Recursive]**
- `DONOUN47` (@ `Comanche055/EXTENDED_VERBS.agc`) -> **O(2^N) [Recursive]**
- `DONOUN46` (@ `Comanche055/EXTENDED_VERBS.agc`) -> **O(2^N) [Recursive]**
- `NOKILL` (@ `Comanche055/EXTENDED_VERBS.agc`) -> **O(2^N) [Recursive]**
- `DONOUN48` (@ `Comanche055/EXTENDED_VERBS.agc`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `DOFSTRT1` (@ `Luminary099/FRESH_START_AND_RESTART.agc`) -> DB Complexity: **54**
- `STARTDAP` (@ `Luminary099/DAPIDLER_PROGRAM.agc`) -> DB Complexity: **50**
- `STARTSB2` (@ `Luminary099/FRESH_START_AND_RESTART.agc`) -> DB Complexity: **46**
- `DOFSTART` (@ `Comanche055/FRESH_START_AND_RESTART.agc`) -> DB Complexity: **45**
- `STARTSB2` (@ `Comanche055/FRESH_START_AND_RESTART.agc`) -> DB Complexity: **42**
- `FLESHPOT` (@ `Luminary099/POWERED_FLIGHT_SUBROUTINES.agc`) -> DB Complexity: **42**
- `R60CALL` (@ `Comanche055/P20-P25.agc`) -> DB Complexity: **32**
- `DSPOFF` (@ `Luminary099/FRESH_START_AND_RESTART.agc`) -> DB Complexity: **30**
- `DSPOFF` (@ `Comanche055/FRESH_START_AND_RESTART.agc`) -> DB Complexity: **29**
  * *Intent:* # R1,R2,R3)
- `READRDOT` (@ `Luminary099/P20-P25.agc`) -> DB Complexity: **28**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Comanche055` | 84 | 28960.38 | 37.62% | 35.79% |
| `Luminary099` | 89 | 27778.48 | 39.88% | 36.24% |
| `Translations` | 69 | 219.42 | 0.0% | 0.0% |
| `__monolith__` | 4 | 8.58 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Comanche055/ASSEMBLY_AND_OPERATION_INFORMATION.agc` -> **100.0%** Exposure
- `Luminary099/ASSEMBLY_AND_OPERATION_INFORMATION.agc` -> **100.0%** Exposure
- `Comanche055/INTER-BANK_COMMUNICATION.agc` -> **99.9999%** Exposure
- `Luminary099/INTER-BANK_COMMUNICATION.agc` -> **99.9999%** Exposure
- `Luminary099/RTB_OP_CODES.agc` -> **99.9683%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Comanche055/AGC_BLOCK_TWO_SELF-CHECK.agc` -> **100.0%** Exposure
- `Comanche055/AUTOMATIC_MANEUVERS.agc` -> **100.0%** Exposure
- `Comanche055/CM_ENTRY_DIGITAL_AUTOPILOT.agc` -> **100.0%** Exposure
- `Comanche055/DOWN-TELEMETRY_PROGRAM.agc` -> **100.0%** Exposure
- `Comanche055/EXECUTIVE.agc` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Comanche055/P40-P47.agc` -> **40** Orphaned Functions | **0** Duplicates
- `Comanche055/INTERPRETER.agc` -> **34** Orphaned Functions | **0** Duplicates
- `Luminary099/DISPLAY_INTERFACE_ROUTINES.agc` -> **34** Orphaned Functions | **0** Duplicates
- `Comanche055/DISPLAY_INTERFACE_ROUTINES.agc` -> **33** Orphaned Functions | **0** Duplicates
- `Luminary099/INTERPRETER.agc` -> **33** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `Comanche055/DISPLAY_INTERFACE_ROUTINES.agc` -> **20.0%** Exposure
- `Comanche055/EXTENDED_VERBS.agc` -> **20.0%** Exposure
- `Comanche055/FRESH_START_AND_RESTART.agc` -> **20.0%** Exposure
- `Comanche055/P11.agc` -> **20.0%** Exposure
- `Comanche055/P76.agc` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `Comanche055/P51-P53.agc` -> **100.0%** Exposure
- `Luminary099/P51-P53.agc` -> **96.5605%** Exposure
### Raw Memory Manipulation
- `Comanche055/PINBALL_NOUN_TABLES.agc` -> **9.9999%** Exposure
- `Luminary099/PINBALL_NOUN_TABLES.agc` -> **9.9956%** Exposure
- `Luminary099/POWERED_FLIGHT_SUBROUTINES.agc` -> **9.7935%** Exposure
- `Comanche055/POWERED_FLIGHT_SUBROUTINES.agc` -> **9.7472%** Exposure
- `Luminary099/INTERPRETER.agc` -> **0.0451%** Exposure
### Algorithmic DoS Exposure
- `Comanche055/P11.agc` -> **100.0%** Exposure
- `Comanche055/P76.agc` -> **99.7264%** Exposure
- `Comanche055/STABLE_ORBIT.agc` -> **34.7153%** Exposure
- `Luminary099/RESTART_TABLES.agc` -> **1.345%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1370` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Luminary099/IMU_COMPENSATION_PACKAGE.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **611.01**
- **Archetype:** `file_cluster_4` (Distance: 14.026 IQR)
- **Magnitude:** 355.34 | **LOC:** 418 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (86.6667%), Verification (80.0%)
- **Heaviest Functions:** `DRFTSUB2` (Impact: 21.2), `IRIGCOMP` (Impact: 17.0), `NBD3` (Impact: 14.9)

### 2. `Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **606.28**
- **Archetype:** `file_cluster_8` (Distance: 13.889 IQR)
- **Magnitude:** 2950.72 | **LOC:** 3810 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (98.6014%), Verification (80.0%)
- **Heaviest Functions:** `CHARIN2` (Impact: 60.8), `HMSOUT` (Impact: 33.7), `MONREQ` (Impact: 29.1)

### 3. `Comanche055/P11.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **601.44**
- **Archetype:** `file_cluster_8` (Distance: 12.061 IQR)
- **Magnitude:** 422.06 | **LOC:** 929 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Algorithmic Dos (100.0%), Concurrency (99.9997%), State Flux (99.9971%), Spec Match (82.6087%)
- **Heaviest Functions:** `REP11A` (Impact: 53.0), `ATERTASK` (Impact: 27.9), `ATTDISP` (Impact: 21.2)

### 4. `Luminary099/UPDATE_PROGRAM.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **596.83**
- **Archetype:** `file_cluster_4` (Distance: 12.577 IQR)
- **Magnitude:** 383.44 | **LOC:** 557 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (95.2381%), Verification (80.0%)
- **Heaviest Functions:** `UPERROR` (Impact: 30.9), `LDLOOP72` (Impact: 29.4), `STORLP71` (Impact: 18.1)

### 5. `Comanche055/CM_ENTRY_DIGITAL_AUTOPILOT.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **590.87**
- **Archetype:** `file_cluster_4` (Distance: 13.37 IQR)
- **Magnitude:** 923.34 | **LOC:** 1274 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (92.9825%), Verification (80.0%)
- **Heaviest Functions:** `BODYRATE` (Impact: 27.3), `ATTRATES` (Impact: 23.5), `EXDAP` (Impact: 21.9)

### 6. `Comanche055/IMU_COMPENSATION_PACKAGE.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **590.4**
- **Archetype:** `file_cluster_4` (Distance: 13.722 IQR)
- **Magnitude:** 292.24 | **LOC:** 369 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Verification (80.0%), Spec Match (71.4286%)
- **Heaviest Functions:** `DRFTSUB2` (Impact: 21.2), `IRIGZ` (Impact: 13.0), `NBDONLY` (Impact: 9.7)

### 7. `Luminary099/P51-P53.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **584.65**
- **Archetype:** `file_cluster_8` (Distance: 12.192 IQR)
- **Magnitude:** 1214.1 | **LOC:** 2342 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (99.9118%), Spec Match (97.5%), Injection Surface (96.5605%)
- **Heaviest Functions:** `DSPOPTN` (Impact: 46.2), `P52B` (Impact: 39.0), `PICAPAR` (Impact: 26.6)

### 8. `Comanche055/P51-P53.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **572.19**
- **Archetype:** `file_cluster_8` (Distance: 11.853 IQR)
- **Magnitude:** 889.34 | **LOC:** 2214 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Injection Surface (100.0%), Concurrency (99.9979%), State Flux (99.3397%), Spec Match (87.6923%)
- **Heaviest Functions:** `P52B` (Impact: 42.4), `R53A` (Impact: 35.6), `P51AA` (Impact: 31.6)

### 9. `Comanche055/PHASE_TABLE_MAINTENANCE.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **572.02**
- **Archetype:** `file_cluster_13` (Distance: 12.397 IQR)
- **Magnitude:** 208.38 | **LOC:** 417 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Tech Debt (97.9745%), Concurrency (90.3403%), Verification (80.0%)
- **Heaviest Functions:** `BELOW1` (Impact: 6.8), `BELOW2` (Impact: 6.7), `ONEORTWO` (Impact: 5.8)

### 10. `Comanche055/TVCDAPS.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **566.11**
- **Archetype:** `file_cluster_8` (Distance: 12.186 IQR)
- **Magnitude:** 469.82 | **LOC:** 785 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Tech Debt (99.0829%), Documentation (97.0449%), Spec Match (87.8788%)
- **Heaviest Functions:** `DAPINIT` (Impact: 20.0), `PSTROKER` (Impact: 8.9), `FWDFLTR` (Impact: 6.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *THE KEYBOARD AND DISPLAY SYSTEM PROGRAM OPERATES UNDER EXECUTIVE CONTROL AND PROCESSES INFORMATION EXCHANGED BETWEEN THE AGC AND THE COMPUTER OPERATOR. THE INPUTS TO THE PROGRAM ARE FROM THE KEYBOARD, FROM INTERNAL PROGRAM, AND FROM THE UPLINK.*
- **Global Archetype:** `file_cluster_8` (Drift: 13.889 IQR)
- **Top Global Matches:** file_cluster_8: 13.889, file_cluster_13: 13.962, file_cluster_4: 14.012
- **Magnitude:** 2950.72 | **LOC:** 3810 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (72.4991%), Tech Debt (18.6336%)
**Top Internal Functions/Classes:**
  * `CHARIN2` (Impact: 60.8 | O(N^1) | DB: 2)
  * `HMSOUT` (Impact: 33.7 | O(N^1) | DB: 8)
  * `MONREQ` (Impact: 29.1 | O(2^N))
  * `DPTEST` (Impact: 26.8 | O(N^1))
    * *Intent:* # DPTEST ENTER WITH SF ROUT NUMBER IN A. # RETURNS TO L+1 IF NO DP. # RETURNS TO L+2 IF DP....
  * `LIMITCOM` (Impact: 22.2 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 838`, `structural_boundaries: 874`, `args: 98`, `func_start: 286`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1267`, `orphaned_logic: 24`
* *Architecture:* `io: 6`, `api: 85`, `concurrency: 140`, `import: 37`
* *Defense:* `safety: 23`, `doc: 96`, `test: 4`, `sync_locks: 23`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DSPTAB, ENDRTOUT, ENDALM, ENDDPDEC, ENDECVN, ENDNVSB1, DSP2BIT, 7...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/INTERPRETER.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 13.852 IQR)
- **Top Global Matches:** file_cluster_8: 13.852, file_cluster_12: 14.011, file_cluster_7: 14.04
- **Magnitude:** 2745.94 | **LOC:** 3076 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (65.8795%), Tech Debt (29.7572%)
**Top Internal Functions/Classes:**
  * `MAXDV` (Impact: 42.4 | O(N^1) | DB: 25)
    * *Intent:* # Page 1065 # IF THE MAJOR PARTS OF THE DIVISOR AND DIVIDEND ARE EQUAL, BUT THE MINOR PARTS ARE SUCH...
  * `INDJUMP` (Impact: 34.8 | O(N^1))
    * *Intent:* # Page 1011 # THE FOLLOWING IS THE JUMP TABLE FOR OP CODES WHICH MAY HAVE INDEXABLE ADDRESSES OR MAY...
  * `BHIZ` (Impact: 34.5 | O(N^1) | DB: 1)
  * `VRIGHT2` (Impact: 29.5 | O(2^N) | DB: 14)
  * `TEST` (Impact: 28.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 687`, `structural_boundaries: 727`, `args: 65`, `func_start: 241`
* *Risk/State:* `state_mutation: 1393`, `dead_code: 2`, `orphaned_logic: 33`
* *Architecture:* `io: 3`, `api: 124`, `import: 3`
* *Defense:* `safety: 3`, `doc: 102`, `sync_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 01, 00, 1400, 0
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/INTERPRETER.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Colossus 2A, AKA Comanche 055. It is part of the source code for the Command Module's (CM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 13.844 IQR)
- **Top Global Matches:** file_cluster_8: 13.844, file_cluster_12: 14.004, file_cluster_7: 14.031
- **Magnitude:** 2739.6 | **LOC:** 3064 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (65.8645%), Tech Debt (30.8028%)
**Top Internal Functions/Classes:**
  * `MAXDV` (Impact: 42.4 | O(N^1) | DB: 25)
    * *Intent:* # Page 1170 # IF THE MAJOR PARTS OF THE DIVISOR AND DIVIDEND ARE EQUAL, BUT THE MINOR PARTS ARE SUCH...
  * `INDJUMP` (Impact: 34.8 | O(N^1))
    * *Intent:* # Page 1116 # THE FOLLOWING IS THE JUMP TABLE FOR OP CODES WHICH MAY HAVE INDEXABLE ADDRESSES OR MAY...
  * `BHIZ` (Impact: 34.5 | O(N^1) | DB: 1)
  * `VRIGHT2` (Impact: 29.5 | O(2^N) | DB: 14)
  * `TEST` (Impact: 28.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 687`, `structural_boundaries: 729`, `args: 65`, `func_start: 243`
* *Risk/State:* `state_mutation: 1386`, `dead_code: 2`, `orphaned_logic: 34`
* *Architecture:* `io: 3`, `api: 124`, `import: 3`
* *Defense:* `safety: 3`, `doc: 102`, `sync_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 01, 00, 1400, 0
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/P20-P25.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *MOD NO -- 2 BY P. VOLANTE*
- **Global Archetype:** `file_cluster_8` (Drift: 13.278 IQR)
- **Top Global Matches:** file_cluster_8: 13.278, file_cluster_13: 13.361, file_cluster_7: 13.441
- **Magnitude:** 2709.54 | **LOC:** 5183 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (45.7747%), Tech Debt (28.658%)
**Top Internal Functions/Classes:**
  * `UPPSV4` (Impact: 23.8 | O(2^N) | DB: 2)
  * `R29` (Impact: 21.5 | O(2^N) | DB: 3)
    * *Intent:* # Page 596 # SERVICER COMES TO R29 FROM "R29?" IF NOR29FLG, READRFLG, RRREMODE, RRCDUZRO, RRREPOS, A...
  * `R29DLOOP` (Impact: 21.5 | O(2^N))
  * `LMINT` (Impact: 19.5 | O(N^1) | DB: 5)
  * `R29RANGE` (Impact: 19.4 | O(2^N) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 844`, `structural_boundaries: 748`, `args: 89`, `func_start: 226`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 942`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 33`
* *Architecture:* `io: 15`, `api: 159`, `concurrency: 214`, `import: 64`
* *Defense:* `safety: 44`, `doc: 239`, `test: 2`, `sync_locks: 44`, `cleanup: 74`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EBANK, RADARUPT, P20S, F2DPS, R29S1, P20S4, 23, LOSCOUNT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/P20-P25.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *MOD NO -- 1 MOD BY -- N. BRODEUR*
- **Global Archetype:** `file_cluster_8` (Drift: 12.343 IQR)
- **Top Global Matches:** file_cluster_8: 12.343, file_cluster_13: 12.589, file_cluster_7: 12.593
- **Magnitude:** 1739.46 | **LOC:** 3530 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (46.3976%), Tech Debt (14.5086%)
**Top Internal Functions/Classes:**
  * `R60CALL` (Impact: 206.2 | O(2^N) | DB: 32)
  * `P23` (Impact: 85.8 | O(2^N) | DB: 5)
  * `S22DSPP` (Impact: 32.4 | O(2^N) | DB: 1)
  * `DECRM61` (Impact: 17.7 | O(N^1) | DB: 11)
  * `S22NXTIN` (Impact: 17.4 | O(N^1) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 482`, `structural_boundaries: 344`, `args: 22`, `func_start: 105`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 592`, `orphaned_logic: 19`
* *Architecture:* `io: 14`, `api: 52`, `concurrency: 136`, `import: 52`
* *Defense:* `safety: 11`, `doc: 121`, `test: 1`, `sync_locks: 11`, `cleanup: 56`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` QMIN, EBANK, ENDPINS1, P20S, RT23, S2231X13, RT53, 9DWTO6DW...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/P40-P47.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *IS THIS AN EXTERNAL DELTA V BURN NO CSTEER = ECSTEER YES CSTEER = ZERO SET UP THRUST FOR P40 20,000 LBS P41 ENTERS HERE ORIGINAL TIG MAY BE SLIPPED BY P40S/SV SET ORIGINAL TIME OF IGNITION FOR S40.9 IMU STATUS CHECK COMPUTE VGTIG,UT COMPUTE PREFERRED ATTITUDE NARROW DEADBAND FOR MANEUVER (EBANK6) ATTITUDE MANEUVER FOR UPDATEVG ALLOW CLOCKTASK P41 INITIALIZE FOR CLOCKTASK WHICH IS CALLED Page 685 BELOW FOR R2 SET FOR UPDATEVG AND TEST FOR STEERING AFTER AVERAGE G (4.1 PROTECTION) V34 V33 SET MRKRTEMP FOR GIMBAL TRIM (-1) ENTRY FROM TST,TRIM SET CNTR +0 FOR RESTART LOGIC IN S40.6 +0 SAYS NORMAL ENTRY +1 (PRE40.6) SAYS RESTART ENTRY TEST TO FIND TIME TO WAIT FOR GIMBAL TEST PLUS, DELAY FOR 18 SECONDS HOLE DELAY FOR TRIM ONLY TASK 6.2 = PRE40.6(-0CS), CLOKTASK(100CS) 4.23 = P40S/SV (PRIO12) P4...*
- **Global Archetype:** `file_cluster_4` (Drift: 12.805 IQR)
- **Top Global Matches:** file_cluster_4: 12.805, file_cluster_8: 12.81, file_cluster_13: 12.861
- **Magnitude:** 1430.24 | **LOC:** 2430 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (62.7778%), Tech Debt (46.3677%)
**Top Internal Functions/Classes:**
  * `RATEZRO` (Impact: 50.5 | O(N^1) | DB: 14)
  * `SERVXT` (Impact: 36.1 | O(2^N) | DB: 4)
  * `ENDV97E` (Impact: 25.5 | O(N^1) | DB: 22)
  * `TSTRXUT` (Impact: 17.3 | O(N^1) | DB: 6)
  * `GIMDTEST` (Impact: 14.7 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 386`, `args: 86`, `func_start: 100`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 483`, `dead_code: 1`, `orphaned_logic: 40`
* *Architecture:* `io: 12`, `api: 56`, `concurrency: 231`, `import: 42`
* *Defense:* `safety: 17`, `doc: 82`, `sync_locks: 17`, `cleanup: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EBANK, DAPDATR1, CNTR, DEC409, PACTOFF, TIG, DAPFIG, 42...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/P51-P53.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *ALIGNS THE IMU TO ONE OF THREE ORIENTATIONS SELECTED BY THE ASTRONAUT. THE PRESENT IMU ORIENTATION IS KNOWN AND IS STORED IN REFSMMAT. THE THREE POSSIBLE ORIENTATIONS MAY BE:*
- **Global Archetype:** `file_cluster_8` (Drift: 12.192 IQR)
- **Top Global Matches:** file_cluster_8: 12.192, file_cluster_7: 12.438, file_cluster_13: 12.551
- **Magnitude:** 1214.1 | **LOC:** 2342 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (59.0775%), Tech Debt (12.4088%)
**Top Internal Functions/Classes:**
  * `DSPOPTN` (Impact: 46.2 | O(2^N) | DB: 5)
  * `P52B` (Impact: 39.0 | O(2^N))
  * `PICAPAR` (Impact: 26.6 | O(N^1) | DB: 2)
  * `LSDISP` (Impact: 25.5 | O(2^N) | DB: 11)
  * `R51P63` (Impact: 23.8 | O(N^1) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 443`, `structural_boundaries: 167`, `args: 20`, `func_start: 80`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 11`, `state_mutation: 387`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 21`, `api: 20`, `concurrency: 116`, `import: 15`
* *Defense:* `safety: 2`, `doc: 85`, `sync_locks: 2`, `cleanup: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 33, EBANK, AOTMARK2, 15, P50S1, XYMARK, P50S, COUNT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/SERVICER.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *SUBROUTINE TO READ PIPA COUNTERS, TRYING TO BE VERY CAREFUL SO THAT WILL BE RESTARTABLE. PIPA READINGS ARE STORED IN THE VECTOR DELV. THE HIGH ORDER PART OF EACH COMPONENT CONTAINS THE PIPA READING, RESTARTS BEGIN AT REREADAC.*
- **Global Archetype:** `file_cluster_13` (Drift: 12.921 IQR)
- **Top Global Matches:** file_cluster_13: 12.921, file_cluster_8: 13.009, file_cluster_4: 13.082
- **Magnitude:** 1099.56 | **LOC:** 1716 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (68.1509%), Tech Debt (21.4617%)
**Top Internal Functions/Classes:**
  * `REREADAC` (Impact: 29.0 | O(N^1) | DB: 3)
    * *Intent:* # Page 871
  * `NOREASON` (Impact: 17.4 | O(N^1) | DB: 4)
  * `POSALARM` (Impact: 16.8 | O(2^N))
  * `LRVJOB` (Impact: 14.8 | O(N^1) | DB: 6)
  * `PIPSDONE` (Impact: 13.6 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 442`, `args: 45`, `func_start: 90`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 475`, `dead_code: 3`, `orphaned_logic: 14`
* *Architecture:* `api: 79`, `concurrency: 74`, `import: 41`
* *Defense:* `safety: 9`, `doc: 47`, `test: 2`, `sync_locks: 9`, `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EBANK, VSELECT, 23, 34, SERV1, 33, LRVF, PHSNAME5...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/EXTENDED_VERBS.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_13` (Drift: 12.161 IQR)
- **Top Global Matches:** file_cluster_13: 12.161, file_cluster_8: 12.169, file_cluster_4: 12.303
- **Magnitude:** 1034.56 | **LOC:** 1682 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (57.6323%), Tech Debt (46.5951%)
**Top Internal Functions/Classes:**
  * `VERB69` (Impact: 65.7 | O(2^N))
  * `LST2FAN` (Impact: 31.5 | O(N^1))
  * `IMUATTCK` (Impact: 20.4 | O(N^1))
    * *Intent:* # Page 281 # IMUATTCK VERB 43 DESCRIPTION # LOAD IMU ATTITUDE ERROR METERS # # 1. REQUIRE P00 OR FRE...
  * `RRDESNBK` (Impact: 18.6 | O(N^1) | DB: 1)
    * *Intent:* # Page 269 # DESIGNATE TO DESIRED GIMBAL ANGLES.
  * `R04RR` (Impact: 18.6 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 420`, `structural_boundaries: 269`, `args: 34`, `func_start: 100`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 191`, `fragile_debt: 3`, `orphaned_logic: 11`
* *Architecture:* `io: 19`, `api: 36`, `concurrency: 79`, `import: 36`
* *Defense:* `safety: 20`, `doc: 41`, `sync_locks: 20`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EBANK, OGC, ROLLTIME, 01, RPASS36, QPLACE, 23, LOSCOUNT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/IMU_CALIBRATION_AND_ALIGNMENT.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *POSITIONING ROUTINES FOR THE IMU PERFORMANCE TESTS AS WELL AS SOME OF THE TESTS THEMSELVES. FOR A DESCRIPTION OF THESE SUBROUTINES AND THE OPERATING PROCEDURES (TYPICALLY) SEE STG MEMO 685.THEORETICAL REF.E-1973 TAKE CARE OF DRIFT FLAG CALCULATE -COS LATITUDE AND SIN LATITUDE GYROCOMPASS COMES IN HERE Page 424 SEE IF IN OPTICAL VERIFICATION NO YES IF GLOKFAIL SET, GIMBAL LOCK +1 IF IN GIMBAL LOCK,OTHERWISE 0 RESET GIMBAL LOCK FLAG BIT 14 FLAG 3 IF ONE GO AND DO A PIPA TEST ONLY ALIGN AND MEASURE VERTICAL PIPA RATE Page 425 PIPA TEST PIP PULSE CATCHING ROUTINE Page 426 DEC585 HAS BEEN REDEFINED FOR LEM TAKE PLATFORM OUT OF GIMBAL LOCK ABOUT 1 HOUR VERTICAL DRIFT TEST 0 IF POSN 4 OFFSET PLATFORM ALLOW ONLY SOUTH GYRO EARTH RATE COMPENS Page 427 IMU NOT IN USE BIT 8 FLAG 0 Page 428 COARSE ALI...*
- **Global Archetype:** `file_cluster_8` (Drift: 12.663 IQR)
- **Top Global Matches:** file_cluster_8: 12.663, file_cluster_13: 12.793, file_cluster_4: 12.901
- **Magnitude:** 990.88 | **LOC:** 1407 | **CtrlFlow:** 50.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (73.0369%), Tech Debt (55.3653%)
**Top Internal Functions/Classes:**
  * `OPTDATA` (Impact: 41.7 | O(2^N) | DB: 11)
  * `FINETIME` (Impact: 14.8 | O(2^N) | DB: 11)
  * `ZEROING1` (Impact: 14.3 | O(2^N) | DB: 3)
  * `GCOMP4` (Impact: 12.6 | O(2^N) | DB: 1)
  * `SHOW1` (Impact: 11.1 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 247`, `args: 21`, `func_start: 88`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 430`, `orphaned_logic: 29`
* *Architecture:* `io: 3`, `api: 26`, `concurrency: 70`, `import: 22`
* *Defense:* `safety: 12`, `doc: 39`, `sync_locks: 12`, `cleanup: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 34, 33, EBANK, IMUCAL3, ERTHRVSE, IMUCAL1, LENGTHOT, GEOSAVE1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/CM_ENTRY_DIGITAL_AUTOPILOT.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Colossus 2A, AKA Comanche 055. It is part of the source code for the Command Module's (CM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_4` (Drift: 13.37 IQR)
- **Top Global Matches:** file_cluster_4: 13.37, file_cluster_13: 13.422, file_cluster_8: 13.538
- **Magnitude:** 923.34 | **LOC:** 1274 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (62.951%), Tech Debt (14.7076%)
**Top Internal Functions/Classes:**
  * `BODYRATE` (Impact: 27.3 | O(N^1) | DB: 19)
  * `ATTRATES` (Impact: 23.5 | O(N^1) | DB: 19)
    * *Intent:* # Page 1073 # CALCULATE BODY ATTITUDE RATES AND INTEGRATE TO OBTAIN ATTITUDE ANGLES. # # CB PHIDOT T...
  * `EXDAP` (Impact: 21.9 | O(N^1) | DB: 3)
    * *Intent:* # 2. IF C(45) GEQ CALFA GEQ -C(45), USE CMDAPMOD = +1 # BETA: ROLL ERROR = SGN(-SALF) (BETACOM -BETA...
  * `EXDAP2` (Impact: 20.7 | O(N^1) | DB: 10)
  * `DOBRATE1` (Impact: 18.0 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 422`, `args: 47`, `func_start: 57`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 452`, `dead_code: 8`, `orphaned_logic: 5`
* *Architecture:* `io: 7`, `api: 86`, `concurrency: 42`, `import: 12`
* *Defense:* `safety: 3`, `doc: 35`, `sync_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AOG, 15, RATEAVG, 20, ETRYDAP, COUNT, T5LOC, DAPS1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/P51-P53.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *ALIGNS THE IMU TO ONE OF THREE ORIENTATIONS SELECTED BY THE ASTRONAUT. THE PRESENT IMU ORIENTATION IS KNOWN AND IS STORED IN REFSMMAT. THE THREE POSSIBLE ORIENTATIONS MAY BE:*
- **Global Archetype:** `file_cluster_8` (Drift: 11.853 IQR)
- **Top Global Matches:** file_cluster_8: 11.853, file_cluster_13: 11.991, file_cluster_7: 12.091
- **Magnitude:** 889.34 | **LOC:** 2214 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (44.5613%), Tech Debt (9.8918%)
**Top Internal Functions/Classes:**
  * `P52B` (Impact: 42.4 | O(2^N))
  * `R53A` (Impact: 35.6 | O(2^N) | DB: 2)
  * `P51AA` (Impact: 31.6 | O(2^N) | DB: 6)
  * `P51C` (Impact: 27.6 | O(2^N) | DB: 2)
  * `PICAPAR` (Impact: 27.4 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 350`, `structural_boundaries: 177`, `args: 9`, `func_start: 65`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 260`, `dead_code: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 17`, `api: 17`, `concurrency: 55`, `import: 39`
* *Defense:* `safety: 6`, `doc: 83`, `sync_locks: 6`, `cleanup: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PICAPAR, RT53, S52, V06N89, 33, P50S, 26P50S, RDCDUS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/T4RUPT_PROGRAM.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *CHANNEL 30 AND CALLS THE APPROPRIATE SUBROUTINES. THE BITS PROCESSED AND THEIR RELEVANT SUBROUTINES ARE:*
- **Global Archetype:** `file_cluster_8` (Drift: 12.497 IQR)
- **Top Global Matches:** file_cluster_8: 12.497, file_cluster_7: 12.617, file_cluster_13: 12.682
- **Magnitude:** 879.9 | **LOC:** 1468 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (39.7183%), Tech Debt (21.1647%)
**Top Internal Functions/Classes:**
  * `STORCMD` (Impact: 24.5 | O(N^1) | DB: 4)
  * `SYNCT4` (Impact: 14.6 | O(2^N))
  * `DSPSCAN` (Impact: 14.5 | O(2^N) | DB: 1)
  * `PROCTNON` (Impact: 13.9 | O(N^1) | DB: 1)
    * *Intent:* # PROCESS IMU TURN-ON REQUESTS AFTER WAITING 1 SAMPLE FOR ALL SIGNALS TO ARRIVE.
  * `OPTDRIVE` (Impact: 12.8 | O(N^1) | DB: 2)
    * *Intent:* # SHAFT STOP MONITOR-ZONE UPDATE
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 256`, `args: 18`, `func_start: 103`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 238`, `orphaned_logic: 9`
* *Architecture:* `io: 10`, `api: 76`, `concurrency: 25`, `import: 11`
* *Defense:* `doc: 84`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RELTAB, OPTDRV, OPTMODES, T4RUP, COUNT, 12, FFTAG12, DSPCOUNT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/P-AXIS_RCS_AUTOPILOT.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 12.565 IQR)
- **Top Global Matches:** file_cluster_8: 12.565, file_cluster_7: 12.82, file_cluster_13: 12.873
- **Magnitude:** 849.0 | **LOC:** 1057 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (60.9798%), Tech Debt (16.8857%)
**Top Internal Functions/Classes:**
  * `RATERROR` (Impact: 26.3 | O(N^1) | DB: 7)
  * `PJETSLEC` (Impact: 23.2 | O(N^1) | DB: 7)
  * `BACKP` (Impact: 21.5 | O(N^1) | DB: 24)
  * `PAXIS` (Impact: 10.8 | O(N^1) | DB: 10)
    * *Intent:* # THE FOLLOWING T5RUPT ENTRY BEGINS THE PROGRAM WHICH CONTROLS THE P-AXIS ACTION OF THE LEM USING TH...
  * `SUBDIVDE` (Impact: 8.0 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 362`, `args: 16`, `func_start: 50`
* *Risk/State:* `state_mutation: 451`, `orphaned_logic: 6`
* *Architecture:* `io: 3`, `api: 97`, `concurrency: 6`, `import: 3`
* *Defense:* `safety: 8`, `doc: 23`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AOSQ, 16, EBANK, DAPS1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/LUNAR_LANDING_GUIDANCE_EQUATIONS.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 12.504 IQR)
- **Top Global Matches:** file_cluster_8: 12.504, file_cluster_13: 12.735, file_cluster_7: 12.781
- **Magnitude:** 813.76 | **LOC:** 1475 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (67.1678%), Tech Debt (32.6357%)
**Top Internal Functions/Classes:**
  * `P64DISPS` (Impact: 16.9 | O(2^N) | DB: 3)
  * `UNWCLOOP` (Impact: 15.2 | O(2^N) | DB: 6)
  * `RESETRPT` (Impact: 14.6 | O(2^N))
  * `REDESMON` (Impact: 12.8 | O(N^1) | DB: 5)
  * `RODCOMP` (Impact: 12.2 | O(N^1) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 288`, `args: 29`, `func_start: 75`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 376`, `orphaned_logic: 17`
* *Architecture:* `io: 10`, `api: 50`, `concurrency: 14`, `import: 14`
* *Defense:* `safety: 2`, `doc: 33`, `sync_locks: 2`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TTF, RODTRAP, PHSNAME2, 20, P66LOC, TCGFAPPR, 31, COUNT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/FRESH_START_AND_RESTART.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *SUNDISK REV 120 FUNCTIONAL DESCRIPTION SLAP1 MAN INITIATED FRESH START 1. EXECUTE STARTSUB 2. TURN OFF DSKY DISCRETE-LAMPS 3. CLEAR FAIL REGISTERS,SELF-CHECK ERROR COUNTER AND RESTART COUNTER 4. EXECUTE DOFSTART DOFSTART MACHINE INITIATED FRESH START 1. CLEAR SELF-CHECK REGISTERS, MODE REGISTER AND CDUZ REGISTER 2. CLEAR PHASE TABLE 3. INITIALIZE IMU FLAGS 4. INITIALIZE FLAGWORDS 5. TRANSFER CONTROL TO IDLE LOOP IN DUMMYJOB GOPROG HARDWARE RESTART 0. EXECUTE STARTSUB 1. TRANSFER CONTROL TO DOFSTART IF ANY OF THE FOLLOWING CONDITIONS EXIST. A. RESTART OCCURED DURING EXECUTION OF ERASCHK B. BOTH OSCILLATOR FAIL AND AGC WARNING ARE ON C. MARK REJECT AND EITHER NAV OR MAIN DSKY ERROR LIGHT RESET ARE ON. 2. SCHEDULE A T5RUPT PROGRAM FOR THE DAP 3. SET FLAGWRD5 BITS FOR INTWAKE ROUTINE 4. EXTING...*
- **Global Archetype:** `file_cluster_8` (Drift: 12.629 IQR)
- **Top Global Matches:** file_cluster_8: 12.629, file_cluster_13: 12.668, file_cluster_7: 12.838
- **Magnitude:** 785.68 | **LOC:** 1481 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (59.3947%), Tech Debt (14.7336%)
**Top Internal Functions/Classes:**
  * `PCLOOP` (Impact: 32.8 | O(2^N) | DB: 4)
  * `V5OUT2` (Impact: 20.9 | O(N^1) | DB: 5)
  * `GOP00FIX` (Impact: 11.5 | O(N^1) | DB: 6)
  * `T5IDLOC` (Impact: 10.9 | O(2^N))
  * `AGAINMM` (Impact: 10.7 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 394`, `args: 45`, `func_start: 60`
* *Risk/State:* `state_mutation: 357`, `orphaned_logic: 6`
* *Architecture:* `io: 11`, `api: 67`, `concurrency: 33`, `import: 23`
* *Defense:* `safety: 13`, `doc: 41`, `sync_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` VERB37, EBANK, DAPDATR1, 27, BZERO, OGANOW, QPLACE, 13...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/AOSTASK_AND_AOSJOB.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *1/ACCS PROVIDES THE INTERFACE BETWEEN THE GUIDANCE PROGRAMS AND THE DIGITAL AUTOPILOT. WHENEVER THERE IS A CHANGE IN THE MASS OF THE VEHICLE, IN THE DEADBAND SELECTED, IN THE VEHICLE CONFIGURATION (ASCENT-DESCENT- DOCKED), AND DURING A FRESH START OR A RESTART, 1/ACCS IS CALLED TO COMMUNICATE THE DATA CHANGES TO THE DAP.*
- **Global Archetype:** `file_cluster_8` (Drift: 12.826 IQR)
- **Top Global Matches:** file_cluster_8: 12.826, file_cluster_13: 12.907, file_cluster_7: 13.002
- **Magnitude:** 779.8 | **LOC:** 1070 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (62.1585%), Tech Debt (17.3%)
**Top Internal Functions/Classes:**
  * `SPSLOOP2` (Impact: 31.2 | O(2^N) | DB: 18)
  * `FIXMIN` (Impact: 12.8 | O(N^1) | DB: 2)
  * `STCTR` (Impact: 11.2 | O(2^N) | DB: 3)
  * `ACCTHERE` (Impact: 10.7 | O(N^1) | DB: 10)
  * `SKIPDB1` (Impact: 10.5 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 420`, `args: 18`, `func_start: 45`
* *Risk/State:* `state_mutation: 446`, `dead_code: 1`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 104`, `concurrency: 6`, `import: 6`
* *Defense:* `safety: 12`, `doc: 33`, `test: 1`, `sync_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EBANK, 20, AOSQ, COUNT, DAPS3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/EXTENDED_VERBS.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Comanche, build 055. It is part of the source code for the Command Module's (CM) Apollo Guidance Computer (AGC), Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 11.787 IQR)
- **Top Global Matches:** file_cluster_8: 11.787, file_cluster_4: 11.968, file_cluster_13: 11.986
- **Magnitude:** 779.28 | **LOC:** 1316 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (56.9079%), Tech Debt (22.4474%)
**Top Internal Functions/Classes:**
  * `VERB69` (Impact: 65.7 | O(2^N))
  * `LST2FAN` (Impact: 31.5 | O(N^1))
  * `IMUATTCK` (Impact: 18.7 | O(N^1) | DB: 1)
    * *Intent:* # Page 249 # IMUATTCK VERB 43 DESCRIPTION # LOAD IMU ATTITUDE ERROR METERS # 1. REQUIRE PROGRAM 00 A...
  * `DONOUN47` (Impact: 17.1 | O(2^N) | DB: 3)
  * `IMUZEROK` (Impact: 16.7 | O(N^1) | DB: 1)
    * *Intent:* # (NOT IN USE YET)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 147`, `args: 28`, `func_start: 85`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 119`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 5`, `api: 28`, `concurrency: 55`, `import: 9`
* *Defense:* `safety: 12`, `doc: 33`, `sync_locks: 12`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EBANK, RPASS36, QPLACE, 10, PACTOFF, T5TVCDT, STROKER, 7...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/IMU_MODE_SWITCHING_ROUTINES.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *LOG SECTION IMU MODE SWITCHING MOD BY- R.MELANSON TO ADD DOCUMENTATION ASSEMBLY SUNDISK REV. 82*
- **Global Archetype:** `file_cluster_13` (Drift: 12.943 IQR)
- **Top Global Matches:** file_cluster_13: 12.943, file_cluster_4: 12.944, file_cluster_8: 12.978
- **Magnitude:** 763.0 | **LOC:** 1068 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (53.6275%), Tech Debt (43.1993%)
**Top Internal Functions/Classes:**
  * `PRESTAND` (Impact: 32.9 | O(2^N) | DB: 3)
  * `POSTAND` (Impact: 32.4 | O(2^N) | DB: 4)
  * `GSELECT` (Impact: 19.6 | O(N^1) | DB: 7)
  * `COARS1` (Impact: 18.4 | O(2^N) | DB: 4)
  * `GYROAGRE` (Impact: 18.3 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 229`, `args: 21`, `func_start: 74`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 264`, `dead_code: 2`, `orphaned_logic: 14`
* *Architecture:* `io: 1`, `api: 44`, `concurrency: 35`, `import: 10`
* *Defense:* `safety: 12`, `doc: 48`, `sync_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 34, EBANK, 1400, SCALSAVE, MODESW, COUNT, FFTAG3, 11...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/IMU_MODE_SWITCHING_ROUTINES.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *LOG SECTION IMU MODE SWITCHING MOD BY- R.MELANSON TO ADD DOCUMENTATION ASSEMBLY SUNDISK REV. 82 FUNCTIONAL DESCRIPTION- TO DELAY FURTHER EXECUTION OF THE CALLING ROUTINE UNTIL ITS SELECTED I/O FUNCTION IS COMPLETE. THE FOLLOWING CHECKS ON THE CALLING ROUTINES MODECADR ARE MADE AND ACTED UPON. 1) +0 INDICATES INCOMPLETE I/O OPERATION.CALLING ROUTINE IS PUT TO SLEEP. 2) -1 INDICATES COMPLETED I/O OPERATION. STALL BYPASSES JOBSLEEP CALL AND RETURNS TO CALLING ROUTINE AT L+3 3) -0 INDICATES COMPLETED I/O WITH FAILURE. STALL CLEARS MODECADR AND RETURNS TO CALLING ROUTINE AT L+2. 4) VALUE GREATER THAN 0 INDICATES TWO ROUTINES CALLING FOR USE OF SAME DEVICE. STALL EXITS TO ABORT WHICH EXECUTES A PROGRAM RESTART WHICH IN TURN CLEARS ALL MODECADR REGISTERS. CALLING SEQUENCE- L TC BANKCALL L+1 CADR ...*
- **Global Archetype:** `file_cluster_8` (Drift: 12.896 IQR)
- **Top Global Matches:** file_cluster_8: 12.896, file_cluster_13: 12.899, file_cluster_4: 12.924
- **Magnitude:** 758.64 | **LOC:** 1067 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (53.4771%), Tech Debt (43.4398%)
**Top Internal Functions/Classes:**
  * `PRESTAND` (Impact: 32.9 | O(2^N) | DB: 3)
  * `POSTAND` (Impact: 32.4 | O(2^N) | DB: 4)
  * `GSELECT` (Impact: 19.6 | O(N^1) | DB: 7)
  * `COARS1` (Impact: 18.4 | O(2^N) | DB: 4)
  * `GYROAGRE` (Impact: 18.3 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 228`, `args: 21`, `func_start: 74`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 261`, `dead_code: 1`, `orphaned_logic: 14`
* *Architecture:* `io: 1`, `api: 44`, `concurrency: 35`, `import: 10`
* *Defense:* `safety: 12`, `doc: 48`, `sync_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 34, EBANK, 1400, SCALSAVE, MODESW, COUNT, FFTAG3, 11...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/BURN_BABY_BURN--MASTER_IGNITION_ROUTINE.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *KILLTASK IS USED TO REMOVE A TASK FROM THE WAITLIST BY SUBSTITUTING A NULL TASK CALLED `NULLTASK' (OF COURSE), WHICH MERELY DOES A TC TASKOVER. IF THE SAME TASK IS SCHEDULED MORE THAN ONCE, ONLY THE ONE WHICH WILL OCCUR FIRST IS REMOVED. IF THE TASK IS NOT SCHEDULED, KILLTASK TAKES NO ACTION AND RETURNS WITH NO ALARM. KILLTASK LEAVES INTERRUPTS INHIBITED SO CALLER MUST RELINT*
- **Global Archetype:** `file_cluster_4` (Drift: 12.441 IQR)
- **Top Global Matches:** file_cluster_4: 12.441, file_cluster_13: 12.573, file_cluster_8: 12.698
- **Magnitude:** 756.28 | **LOC:** 1060 | **CtrlFlow:** 50.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (71.6625%), Tech Debt (33.2961%)
**Top Internal Functions/Classes:**
  * `P41TABLE` (Impact: 42.1 | O(N^1))
  * `CLOKTASK` (Impact: 17.7 | O(2^N) | DB: 1)
  * `REP40ALM` (Impact: 12.9 | O(2^N) | DB: 3)
  * `STCLOK3` (Impact: 11.8 | O(N^1) | DB: 5)
  * `ASTNRETN` (Impact: 10.8 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 218`, `args: 46`, `func_start: 66`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 212`, `dead_code: 1`, `orphaned_logic: 12`
* *Architecture:* `io: 4`, `api: 31`, `concurrency: 128`, `import: 20`
* *Defense:* `safety: 13`, `doc: 31`, `test: 2`, `sync_locks: 13`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EBANK, 27, TTOGO, TRKMKCNT, AOSQ, P40S, P40S1, P40S3...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/FRESH_START_AND_RESTART.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *FLASH V 37 ON DSKY MM CHANGE REQUEST*
- **Global Archetype:** `file_cluster_8` (Drift: 12.196 IQR)
- **Top Global Matches:** file_cluster_8: 12.196, file_cluster_13: 12.365, file_cluster_7: 12.432
- **Magnitude:** 688.9 | **LOC:** 1243 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (56.8184%), Tech Debt (18.9264%)
**Top Internal Functions/Classes:**
  * `PCLOOP` (Impact: 29.4 | O(2^N) | DB: 5)
  * `SETUP70` (Impact: 17.1 | O(N^1) | DB: 2)
  * `DOFSTRT1` (Impact: 10.9 | O(N^1) | DB: 54)
  * `AGAINMM` (Impact: 10.7 | O(2^N) | DB: 2)
    * *Intent:* # Page 228
  * `DSPOFF` (Impact: 10.4 | O(2^N) | DB: 30)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 405`, `args: 16`, `func_start: 55`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 334`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 10`, `api: 60`, `concurrency: 20`, `import: 11`
* *Defense:* `safety: 7`, `doc: 36`, `sync_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` R, VERB37, EBANK, RRECTCSM, 20, AOSQ, FRANDRES, COUNT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/DISPLAY_INTERFACE_ROUTINES.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 12.696 IQR)
- **Top Global Matches:** file_cluster_8: 12.696, file_cluster_13: 12.777, file_cluster_4: 12.831
- **Magnitude:** 688.66 | **LOC:** 1460 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (59.9598%), Tech Debt (92.5133%)
**Top Internal Functions/Classes:**
  * `NORMRET` (Impact: 15.4 | O(N^1))
  * `FLASHSUB` (Impact: 11.1 | O(N^1) | DB: 1)
  * `OKTOPLAY` (Impact: 10.1 | O(N^1) | DB: 1)
  * `NVDSP` (Impact: 10.1 | O(N^1) | DB: 6)
  * `NV50DSP` (Impact: 8.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 252`, `args: 9`, `func_start: 121`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 232`, `dead_code: 1`, `orphaned_logic: 34`
* *Architecture:* `io: 10`, `api: 45`, `concurrency: 23`, `import: 5`
* *Defense:* `safety: 18`, `doc: 39`, `sync_locks: 18`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FFTAG4, DISPLAYS, NVWORD, WHOCARES, NVSAVE, COUNT, 10
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/DISPLAY_INTERFACE_ROUTINES.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Comanche, build 055. It is part of the source code for the Command Module's (CM) Apollo Guidance Computer (AGC), Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 12.754 IQR)
- **Top Global Matches:** file_cluster_8: 12.754, file_cluster_13: 12.791, file_cluster_4: 12.831
- **Magnitude:** 682.7 | **LOC:** 1477 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (60.4921%), Tech Debt (91.6281%)
**Top Internal Functions/Classes:**
  * `NORMRET` (Impact: 15.4 | O(N^1))
  * `FLASHSUB` (Impact: 11.1 | O(N^1) | DB: 1)
  * `OKTOPLAY` (Impact: 10.1 | O(N^1) | DB: 1)
    * *Intent:* # Page 1471
  * `NVDSP` (Impact: 10.1 | O(N^1) | DB: 6)
  * `LINUSCHR` (Impact: 8.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 251`, `args: 9`, `func_start: 121`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 229`, `dead_code: 2`, `orphaned_logic: 33`
* *Architecture:* `io: 10`, `api: 45`, `concurrency: 23`, `import: 5`
* *Defense:* `safety: 18`, `doc: 38`, `sync_locks: 18`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FFTAG4, DISPLAYS, NVWORD, WHOCARES, NVSAVE, COUNT, 10
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/T4RUPT_PROGRAM.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *CHANNEL 30 AND CALLS THE APPROPRIATE SUBROUTINES. THE BITS PROCESSED AND THEIR RELEVANT SUROUTINES ARE: FUNCTION BIT SUBROUTINE CALLED -------- --- ----------------- TEMP IN LIMITS 15 TLIM ISS TURN-ON REQUEST 14 ITURNON IMU FAIL 13 IMUFAIL (SETISSW) IMU CDU FAIL 12 ICDUFAIL (SETISSW) IMU CAGE 11 IMUCAGE IMU OPERATE 9 IMUOP THE LAST SAMPLED STATE OF THESE BITS IS LEFT IN IMODES30. ALSO, EACH SUBROUTINE CALLED FINDS THE NEW VALUE OF THE BIT IN A, WITH Q SET TO THE PROPER RETURN LOCATION NXTIFAIL. CALLING SEQUENCE: T4RUPT EVERY 480 MILLISECONDS. JOBS OR TASKS INITIATED: NONE. SUBROUTINES CALLED: TLIM, TURNON, SETISSW, IMUCAGE, IMUOP. ERASABELE INITIALIZATION: FRESH START OR RESTART WITH NO GROUPS ACTIVE: C((MODES30) = OCT 37411). RESTART WITH ACTIVE GROUPS: C(IMODES30) = (B(IMODES30)AND(OCT 0...*
- **Global Archetype:** `file_cluster_8` (Drift: 12.439 IQR)
- **Top Global Matches:** file_cluster_8: 12.439, file_cluster_7: 12.502, file_cluster_13: 12.611
- **Magnitude:** 633.78 | **LOC:** 1355 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (36.9079%), Tech Debt (17.4856%)
**Top Internal Functions/Classes:**
  * `MONREPOS` (Impact: 18.5 | O(N^1) | DB: 6)
  * `TRKFLCDU` (Impact: 16.0 | O(N^1))
  * `SYNCT4` (Impact: 14.6 | O(2^N))
  * `DSPSCAN` (Impact: 14.5 | O(2^N) | DB: 1)
  * `PROCTNON` (Impact: 13.8 | O(N^1) | DB: 1)
    * *Intent:* # PROCESS IMU TURN-ON REQUESTS AFTER WAITING 1 SAMPLE FOR ALL SIGNALS TO ARRIVE.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 192`, `args: 13`, `func_start: 61`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 168`, `orphaned_logic: 5`
* *Architecture:* `io: 11`, `api: 61`, `concurrency: 24`, `import: 8`
* *Defense:* `doc: 108`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FFTAG10, EBANK, M11, T4RUP, COUNT, 12, DSPCOUNT, LOSCOUNT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Luminary099/IMU_MODE_SWITCHING_ROUTINES.agc` (AGC_ASSEMBLY) | Magnitude: 763.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: encapsulation: 677, indent_tabs: 583, state_mutation: 264, structural_boundaries: 229
- `Luminary099/EXTENDED_VERBS.agc` (AGC_ASSEMBLY) | Magnitude: 1034.56 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 1054, indent_tabs: 907, branch: 420, structural_boundaries: 269
- `Comanche055/TVCRESTARTS.agc` (AGC_ASSEMBLY) | Magnitude: 89.82 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: encapsulation: 85, indent_tabs: 81, branch: 28, state_mutation: 27
- `Luminary099/AGC_BLOCK_TWO_SELF_CHECK.agc` (AGC_ASSEMBLY) | Magnitude: 379.9 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 353, indent_tabs: 260, structural_boundaries: 164, state_mutation: 161
- `Comanche055/AGC_BLOCK_TWO_SELF-CHECK.agc` (AGC_ASSEMBLY) | Magnitude: 379.92 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 354, indent_tabs: 261, structural_boundaries: 164, state_mutation: 161

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Comanche055/P40-P47.agc` (AGC_ASSEMBLY) | Magnitude: 1430.24 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 1736, indent_tabs: 1532, state_mutation: 483, structural_boundaries: 386
- `Luminary099/R30.agc` (AGC_ASSEMBLY) | Magnitude: 236.0 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 259, indent_tabs: 224, state_mutation: 69, branch: 60
- `Luminary099/RCS_FAILURE_MONITOR.agc` (AGC_ASSEMBLY) | Magnitude: 60.16 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: encapsulation: 77, indent_tabs: 70, structural_boundaries: 30, state_mutation: 24
- `Luminary099/AOTMARK.agc` (AGC_ASSEMBLY) | Magnitude: 462.96 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: encapsulation: 528, indent_tabs: 466, state_mutation: 156, structural_boundaries: 136
- `Comanche055/CM_ENTRY_DIGITAL_AUTOPILOT.agc` (AGC_ASSEMBLY) | Magnitude: 923.34 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: encapsulation: 837, indent_tabs: 740, state_mutation: 452, structural_boundaries: 422

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `Comanche055/ASSEMBLY_AND_OPERATION_INFORMATION.agc` (AGC_ASSEMBLY) | Magnitude: 10.52 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: fragile_debt: 68, doc: 27, spec_exposure: 12, sec_high_risk_execution: 4
- `Luminary099/ASSEMBLY_AND_OPERATION_INFORMATION.agc` (AGC_ASSEMBLY) | Magnitude: 10.52 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: fragile_debt: 56, doc: 31, spec_exposure: 13, sec_high_risk_execution: 7
- `Comanche055/ENTRY_LEXICON.agc` (AGC_ASSEMBLY) | Magnitude: 10.52 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 8, spec_exposure: 6, ownership: 1, sec_dead_code: 1
- `Luminary099/INPUT_OUTPUT_CHANNEL_BIT_DESCRIPTIONS.agc` (AGC_ASSEMBLY) | Magnitude: 10.52 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 10, sec_high_risk_execution: 5, ownership: 1, spec_exposure: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `Luminary099/WAITLIST.agc` (AGC_ASSEMBLY) | Magnitude: 300.98 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: encapsulation: 268, indent_tabs: 231, state_mutation: 143, structural_boundaries: 125
- `Comanche055/IMU_MODE_SWITCHING_ROUTINES.agc` (AGC_ASSEMBLY) | Magnitude: 758.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: encapsulation: 675, indent_tabs: 585, state_mutation: 261, structural_boundaries: 228
- `Luminary099/INTER-BANK_COMMUNICATION.agc` (AGC_ASSEMBLY) | Magnitude: 116.06 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 79, encapsulation: 78, indent_tabs: 64, structural_boundaries: 48
- `Comanche055/INTER-BANK_COMMUNICATION.agc` (AGC_ASSEMBLY) | Magnitude: 116.16 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 79, encapsulation: 78, indent_tabs: 64, structural_boundaries: 49
- `Luminary099/SPS_BACK-UP_RCS_CONTROL.agc` (AGC_ASSEMBLY) | Magnitude: 72.9 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: encapsulation: 89, indent_tabs: 72, structural_boundaries: 33, branch: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `Comanche055/LUNAR_LANDMARK_SELECTION_FOR_CM.agc` (AGC_ASSEMBLY) | Magnitude: 10.52 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: spec_exposure: 4, doc: 3, ownership: 1
- `Comanche055/CONTRACT_AND_APPROVALS.agc` (AGC_ASSEMBLY) | Magnitude: 10.52 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: spec_exposure: 6, doc: 2, ownership: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc` -> **Zachary Pedigo** (100.0% isolated ownership) | Magnitude: 2950.72
- `Luminary099/EXTENDED_VERBS.agc` -> **Matt Chaulklin** (100.0% isolated ownership) | Magnitude: 1034.56
- `Luminary099/UPDATE_PROGRAM.agc` -> **Zachary Pedigo** (100.0% isolated ownership) | Magnitude: 383.44

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Comanche055/TAGS_FOR_RELATIVE_SETLOC.agc` -> **Severity: 406.5** (Blast Radius: 4.065 * Doc Risk: 100.0%)
- `Luminary099/TAGS_FOR_RELATIVE_SETLOC.agc` -> **Severity: 406.5** (Blast Radius: 4.065 * Doc Risk: 100.0%)
- `Comanche055/TVCDAPS.agc` -> **Severity: 394.488** (Blast Radius: 4.065 * Doc Risk: 97.0449%)
- `Luminary099/LANDING_ANALOG_DISPLAYS.agc` -> **Severity: 377.66** (Blast Radius: 4.065 * Doc Risk: 92.9052%)
- `Luminary099/AOSTASK_AND_AOSJOB.agc` -> **Severity: 373.917** (Blast Radius: 4.065 * Doc Risk: 91.9844%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
