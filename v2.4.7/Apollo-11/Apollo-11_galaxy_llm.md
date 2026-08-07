# ARCHITECTURAL_BRIEF: Apollo-11
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/Apollo-11` |
| **Timestamp** | `2026-08-07T03:29:13.397814+00:00` |
| **Scan Duration** | `1.26s` |
| **Git Branch** | `master` |
| **Git Commit** | `247dd7d0d1b0e7f9f270750ec08983e0a72e73e1` |
| **Git Remote** | `https://github.com/chrislgarry/Apollo-11` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

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
> **Architectural Drift Z-Score:** `3.991`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 114 | 46.3% |
| file_cluster_13 | 33 | 13.4% |
| file_cluster_4 | 18 | 7.3% |
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
| Cognitive Load Exposure | 0.0 | 73.4 | 39.4 | 45.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.1 | 71.2 | 78.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.5 | 24.5 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 46.4 | 80.0 | 80.0 |
| API Exposure | 0.0 | 7.0 | 0.5 | 0.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 34.1 | 17.9 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 85.4 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 12.7 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 62.1 | 81.8 | 0.0 |
| Instability Exposure | 0.0 | 3.9 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 49.5 | 0.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 100.0 | 23.2 | 11.9 | 11.9 |
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

- `R60CALL` (@ `Comanche055/P20-P25.agc`) -> Impact: **114.4** | LOC: 453
- `EJSCAN` (@ `Luminary099/EXECUTIVE.agc`) -> Impact: **68.5** | LOC: 54
- `EJSCAN` (@ `Comanche055/EXECUTIVE.agc`) -> Impact: **61.3** | LOC: 48
- `CHARIN2` (@ `Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc`) -> Impact: **60.8** | LOC: 39
- `HMSOUT` (@ `Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc`) -> Impact: **55.7** | LOC: 74
- `RATEZRO` (@ `Comanche055/P40-P47.agc`) -> Impact: **50.5** | LOC: 247
- `P23` (@ `Comanche055/P20-P25.agc`) -> Impact: **47.9** | LOC: 117
- `MAXDV` (@ `Comanche055/INTERPRETER.agc`) -> Impact: **42.4** | LOC: 108
  * *Intent:* # Page 1170 # IF THE MAJOR PARTS OF THE DIVISOR AND DIVIDEND ARE EQUAL, BUT THE MINOR PARTS ARE SUCH THAT THE # DIVIDEND IS STRICTLY LESS THAN THE DIV...
- `WTLST5` (@ `Comanche055/WAITLIST.agc`) -> Impact: **42.4** | LOC: 51
  * *Intent:* # Page 1228
- `MAXDV` (@ `Luminary099/INTERPRETER.agc`) -> Impact: **42.4** | LOC: 108
  * *Intent:* # Page 1065 # IF THE MAJOR PARTS OF THE DIVISOR AND DIVIDEND ARE EQUAL, BUT THE MINOR PARTS ARE SUCH THAT THE # DIVIDEND IS STRICTLY LESS THAN THE DIV...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Comanche055` | 84 | 28860.08 | 37.8% | 35.81% |
| `Luminary099` | 89 | 27972.58 | 40.09% | 36.24% |
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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1370` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Luminary099/UPDATE_PROGRAM.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **641.77**
- **Archetype:** `file_cluster_4` (Distance: 12.557 IQR)
- **Magnitude:** 345.04 | **LOC:** 557 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Concurrency (99.8027%), Spec Match (95.2381%), Safety Score (86.8982%)
- **Heaviest Functions:** `UPERROR` (Impact: 16.7), `LDLOOP72` (Impact: 15.5), `DELTATOK` (Impact: 13.5)

### 2. `Luminary099/IMU_COMPENSATION_PACKAGE.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **639.93**
- **Archetype:** `file_cluster_4` (Distance: 13.987 IQR)
- **Magnitude:** 351.34 | **LOC:** 418 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Concurrency (99.908%), Safety Score (92.5572%), Spec Match (86.6667%)
- **Heaviest Functions:** `DRFTSUB2` (Impact: 21.2), `IRIGCOMP` (Impact: 17.0), `NBD3` (Impact: 14.9)

### 3. `Comanche055/IMU_COMPENSATION_PACKAGE.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **631.41**
- **Archetype:** `file_cluster_4` (Distance: 13.684 IQR)
- **Magnitude:** 291.94 | **LOC:** 369 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Concurrency (99.9869%), Safety Score (88.1129%), Verification (80.0%)
- **Heaviest Functions:** `DRFTSUB2` (Impact: 21.2), `IRIGZ` (Impact: 13.0), `NBDONLY` (Impact: 9.7)

### 4. `Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **627.72**
- **Archetype:** `file_cluster_8` (Distance: 13.862 IQR)
- **Magnitude:** 3092.62 | **LOC:** 3810 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (98.6014%), Safety Score (90.4829%), Concurrency (85.7541%)
- **Heaviest Functions:** `CHARIN2` (Impact: 60.8), `HMSOUT` (Impact: 55.7), `DPTEST` (Impact: 26.8)

### 5. `Comanche055/PHASE_TABLE_MAINTENANCE.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **613.34**
- **Archetype:** `file_cluster_13` (Distance: 12.451 IQR)
- **Magnitude:** 221.58 | **LOC:** 417 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Tech Debt (97.9745%), Concurrency (90.3403%), Safety Score (88.8953%)
- **Heaviest Functions:** `BELOW2` (Impact: 11.1), `ONEORTWO` (Impact: 9.5), `CHECKB` (Impact: 7.2)

### 6. `Comanche055/CM_ENTRY_DIGITAL_AUTOPILOT.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **612.09**
- **Archetype:** `file_cluster_4` (Distance: 13.425 IQR)
- **Magnitude:** 951.74 | **LOC:** 1274 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (92.9825%), Safety Score (92.4402%), Concurrency (86.5321%)
- **Heaviest Functions:** `BODYRATE` (Impact: 27.3), `ATTRATES` (Impact: 23.5), `EXDAP` (Impact: 21.9)

### 7. `Comanche055/UPDATE_PROGRAM.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **604.91**
- **Archetype:** `file_cluster_4` (Distance: 12.543 IQR)
- **Magnitude:** 357.94 | **LOC:** 556 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Concurrency (99.7503%), Spec Match (87.5%), Safety Score (86.2514%)
- **Heaviest Functions:** `LDLOOP72` (Impact: 15.6), `UPERROR` (Impact: 14.6), `DELTATOK` (Impact: 13.6)

### 8. `Comanche055/TVCDAPS.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **599.45**
- **Archetype:** `file_cluster_8` (Distance: 12.168 IQR)
- **Magnitude:** 474.92 | **LOC:** 785 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Tech Debt (99.0829%), Documentation (96.3694%), Safety Score (92.3733%)
- **Heaviest Functions:** `DAPINIT` (Impact: 20.0), `FWDFLTR` (Impact: 9.4), `PSTROKER` (Impact: 8.9)

### 9. `Luminary099/LANDING_ANALOG_DISPLAYS.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **597.21**
- **Archetype:** `file_cluster_8` (Distance: 11.524 IQR)
- **Magnitude:** 362.9 | **LOC:** 534 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9637%), Spec Match (96.4286%), Documentation (91.5867%), Verification (80.0%)
- **Heaviest Functions:** `SPEEDRUN` (Impact: 14.9), `DISINDAT` (Impact: 13.8), `ALTOUT` (Impact: 13.3)

### 10. `Luminary099/SERVICER.agc` (AGC_ASSEMBLY) -> Cumulative Risk: **593.34**
- **Archetype:** `file_cluster_13` (Distance: 12.945 IQR)
- **Magnitude:** 1131.86 | **LOC:** 1716 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9998%), Spec Match (97.7778%), Concurrency (89.5035%), Safety Score (84.3194%)
- **Heaviest Functions:** `REREADAC` (Impact: 29.0), `NOREASON` (Impact: 19.1), `COPYCYC1` (Impact: 16.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *THE KEYBOARD AND DISPLAY SYSTEM PROGRAM OPERATES UNDER EXECUTIVE CONTROL AND PROCESSES INFORMATION EXCHANGED BETWEEN THE AGC AND THE COMPUTER OPERATOR. THE INPUTS TO THE PROGRAM ARE FROM THE KEYBOARD, FROM INTERNAL PROGRAM, AND FROM THE UPLINK.*
- **Global Archetype:** `file_cluster_8` (Drift: 13.862 IQR)
- **Top Global Matches:** file_cluster_8: 13.862, file_cluster_13: 13.927, file_cluster_4: 13.965
- **Magnitude:** 3092.62 | **LOC:** 3810 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (72.5368%), Tech Debt (20.5528%)
**Top Internal Functions/Classes:**
  * `CHARIN2` (Impact: 60.8)
  * `HMSOUT` (Impact: 55.7)
  * `DPTEST` (Impact: 26.8)
    * *Intent:* # DPTEST ENTER WITH SF ROUT NUMBER IN A. # RETURNS TO L+1 IF NO DP. # RETURNS TO L+2 IF DP....
  * `NUM` (Impact: 24.0)
  * `HMSIN` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 844`, `structural_boundaries: 1170`, `args: 128`, `func_start: 286`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1263`, `orphaned_logic: 27`
* *Architecture:* `io: 6`, `api: 85`, `concurrency: 140`, `import: 37`
* *Defense:* `safety: 23`, `doc: 96`, `test: 4`, `sync_locks: 23`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DSPCOUNT, 7, 41, ENDNVSB1, NVSBENDL, ENDBLFF, TESTOFUF, ENDRQWT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/P20-P25.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *MOD NO -- 2 BY P. VOLANTE*
- **Global Archetype:** `file_cluster_8` (Drift: 13.267 IQR)
- **Top Global Matches:** file_cluster_8: 13.267, file_cluster_13: 13.344, file_cluster_7: 13.432
- **Magnitude:** 2749.94 | **LOC:** 5183 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.819%), Tech Debt (28.658%)
**Top Internal Functions/Classes:**
  * `REMODE` (Impact: 24.6)
    * *Intent:* # RADMODES # # SUBROUTINES CALLED: # # RRTONLY, RRSONL, RMODINV (ACTUALLY PART OF) # # JOBS OR TASKS...
  * `LMINT` (Impact: 19.5)
  * `R22LEM3` (Impact: 18.8)
  * `RR1AX2` (Impact: 17.2)
  * `R29DVEND` (Impact: 17.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 848`, `structural_boundaries: 974`, `args: 144`, `func_start: 226`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 942`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 33`
* *Architecture:* `io: 15`, `api: 159`, `concurrency: 214`, `import: 64`
* *Defense:* `safety: 44`, `doc: 239`, `test: 2`, `sync_locks: 44`, `cleanup: 74`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 25, RADARUPT, R29S1, WWPOS, P20S, P20S3, PREPOS29, 31...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/INTERPRETER.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 13.859 IQR)
- **Top Global Matches:** file_cluster_8: 13.859, file_cluster_12: 14.02, file_cluster_7: 14.049
- **Magnitude:** 2749.34 | **LOC:** 3076 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.9981%), Tech Debt (29.7572%)
**Top Internal Functions/Classes:**
  * `MAXDV` (Impact: 42.4)
    * *Intent:* # Page 1065 # IF THE MAJOR PARTS OF THE DIVISOR AND DIVIDEND ARE EQUAL, BUT THE MINOR PARTS ARE SUCH...
  * `INDJUMP` (Impact: 34.8)
    * *Intent:* # Page 1011 # THE FOLLOWING IS THE JUMP TABLE FOR OP CODES WHICH MAY HAVE INDEXABLE ADDRESSES OR MAY...
  * `BHIZ` (Impact: 34.5)
  * `UNIT` (Impact: 24.4)
    * *Intent:* # Page 1070 # THE FOLLOWING ROUTINE EXECUTES THE UNIT INSTRUCTION, WHICH TAKES THE UNIT OF THE VECTO...
  * `MISCJUMP` (Impact: 23.1)
    * *Intent:* # CODES 10 AND 14 MUST NOT PUSH UP. CODE 04 MAY BE USED FOR VECTOR DECLARE BEFORE PUSHUP IF DESIRED....
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 701`, `structural_boundaries: 907`, `args: 89`, `func_start: 241`
* *Risk/State:* `state_mutation: 1407`, `dead_code: 2`, `orphaned_logic: 33`
* *Architecture:* `io: 3`, `api: 124`, `import: 3`
* *Defense:* `safety: 3`, `doc: 102`, `sync_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 01, 00, 1400, 0
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/INTERPRETER.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Colossus 2A, AKA Comanche 055. It is part of the source code for the Command Module's (CM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 13.852 IQR)
- **Top Global Matches:** file_cluster_8: 13.852, file_cluster_12: 14.013, file_cluster_7: 14.04
- **Magnitude:** 2743.0 | **LOC:** 3064 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.9829%), Tech Debt (30.8028%)
**Top Internal Functions/Classes:**
  * `MAXDV` (Impact: 42.4)
    * *Intent:* # Page 1170 # IF THE MAJOR PARTS OF THE DIVISOR AND DIVIDEND ARE EQUAL, BUT THE MINOR PARTS ARE SUCH...
  * `INDJUMP` (Impact: 34.8)
    * *Intent:* # Page 1116 # THE FOLLOWING IS THE JUMP TABLE FOR OP CODES WHICH MAY HAVE INDEXABLE ADDRESSES OR MAY...
  * `BHIZ` (Impact: 34.5)
  * `UNIT` (Impact: 24.4)
    * *Intent:* # Page 1175 # THE FOLLOWING ROUTINE EXECUTES THE UNIT INSTRUCTION, WHICH TAKES THE UNIT OF THE VECTO...
  * `MISCJUMP` (Impact: 23.2)
    * *Intent:* # CODES 10 AND 14 MUST NOT PUSH UP. CODE 04 MAY BE USED FOR VECTOR DECLARE BEFORE PUSHUP IF DESIRED....
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 701`, `structural_boundaries: 906`, `args: 89`, `func_start: 243`
* *Risk/State:* `state_mutation: 1400`, `dead_code: 2`, `orphaned_logic: 34`
* *Architecture:* `io: 3`, `api: 124`, `import: 3`
* *Defense:* `safety: 3`, `doc: 102`, `sync_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 01, 00, 1400, 0
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/P20-P25.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *MOD NO -- 1 MOD BY -- N. BRODEUR*
- **Global Archetype:** `file_cluster_8` (Drift: 12.311 IQR)
- **Top Global Matches:** file_cluster_8: 12.311, file_cluster_13: 12.552, file_cluster_7: 12.563
- **Magnitude:** 1563.86 | **LOC:** 3530 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.5711%), Tech Debt (14.5086%)
**Top Internal Functions/Classes:**
  * `R60CALL` (Impact: 114.4)
  * `P23` (Impact: 47.9)
  * `S22DSPPA` (Impact: 22.2)
  * `S22DSPP` (Impact: 18.5)
  * `DECRM61` (Impact: 17.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 489`, `structural_boundaries: 417`, `args: 26`, `func_start: 105`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 592`, `orphaned_logic: 19`
* *Architecture:* `io: 14`, `api: 52`, `concurrency: 136`, `import: 52`
* *Defense:* `safety: 11`, `doc: 121`, `test: 1`, `sync_locks: 11`, `cleanup: 56`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MRKBUF2, S22LSITE, RENDEZ, P20S2, 34, P20S, S2231X13, P20S3...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/P40-P47.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *IS THIS AN EXTERNAL DELTA V BURN NO CSTEER = ECSTEER YES CSTEER = ZERO SET UP THRUST FOR P40 20,000 LBS P41 ENTERS HERE ORIGINAL TIG MAY BE SLIPPED BY P40S/SV SET ORIGINAL TIME OF IGNITION FOR S40.9 IMU STATUS CHECK COMPUTE VGTIG,UT COMPUTE PREFERRED ATTITUDE NARROW DEADBAND FOR MANEUVER (EBANK6) ATTITUDE MANEUVER FOR UPDATEVG ALLOW CLOCKTASK P41 INITIALIZE FOR CLOCKTASK WHICH IS CALLED Page 685 BELOW FOR R2 SET FOR UPDATEVG AND TEST FOR STEERING AFTER AVERAGE G (4.1 PROTECTION) V34 V33 SET MRKRTEMP FOR GIMBAL TRIM (-1) ENTRY FROM TST,TRIM SET CNTR +0 FOR RESTART LOGIC IN S40.6 +0 SAYS NORMAL ENTRY +1 (PRE40.6) SAYS RESTART ENTRY TEST TO FIND TIME TO WAIT FOR GIMBAL TEST PLUS, DELAY FOR 18 SECONDS HOLE DELAY FOR TRIM ONLY TASK 6.2 = PRE40.6(-0CS), CLOKTASK(100CS) 4.23 = P40S/SV (PRIO12) P4...*
- **Global Archetype:** `file_cluster_4` (Drift: 12.768 IQR)
- **Top Global Matches:** file_cluster_4: 12.768, file_cluster_8: 12.79, file_cluster_13: 12.836
- **Magnitude:** 1422.54 | **LOC:** 2430 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.9763%), Tech Debt (46.3677%)
**Top Internal Functions/Classes:**
  * `RATEZRO` (Impact: 50.5)
  * `ENDV97E` (Impact: 25.5)
  * `SERVXT` (Impact: 19.1)
  * `TSTRXUT` (Impact: 17.3)
  * `NOTADDUL` (Impact: 15.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 341`, `structural_boundaries: 480`, `args: 98`, `func_start: 100`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 485`, `dead_code: 1`, `orphaned_logic: 40`
* *Architecture:* `io: 12`, `api: 56`, `concurrency: 231`, `import: 42`
* *Defense:* `safety: 17`, `doc: 82`, `sync_locks: 17`, `cleanup: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` S41, CSMMASS, P40S2, P40S5, P41, DAPS6, 17, PACTOFF...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/P51-P53.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *ALIGNS THE IMU TO ONE OF THREE ORIENTATIONS SELECTED BY THE ASTRONAUT. THE PRESENT IMU ORIENTATION IS KNOWN AND IS STORED IN REFSMMAT. THE THREE POSSIBLE ORIENTATIONS MAY BE:*
- **Global Archetype:** `file_cluster_8` (Drift: 12.172 IQR)
- **Top Global Matches:** file_cluster_8: 12.172, file_cluster_7: 12.421, file_cluster_4: 12.513
- **Magnitude:** 1206.2 | **LOC:** 2342 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.9528%), Tech Debt (12.4088%)
**Top Internal Functions/Classes:**
  * `DSPOPTN` (Impact: 40.6)
  * `B2F8` (Impact: 36.0)
  * `PROGRAV` (Impact: 31.7)
  * `PICAPAR` (Impact: 26.6)
  * `R51P63` (Impact: 23.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 448`, `structural_boundaries: 245`, `args: 35`, `func_start: 80`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 11`, `state_mutation: 387`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 21`, `api: 20`, `concurrency: 116`, `import: 15`
* *Defense:* `safety: 2`, `doc: 85`, `sync_locks: 2`, `cleanup: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EBANK, 04, P50S1, COUNT, P50S, 15, STARAD, XYMARK...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/SERVICER.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *SUBROUTINE TO READ PIPA COUNTERS, TRYING TO BE VERY CAREFUL SO THAT WILL BE RESTARTABLE. PIPA READINGS ARE STORED IN THE VECTOR DELV. THE HIGH ORDER PART OF EACH COMPONENT CONTAINS THE PIPA READING, RESTARTS BEGIN AT REREADAC.*
- **Global Archetype:** `file_cluster_13` (Drift: 12.945 IQR)
- **Top Global Matches:** file_cluster_13: 12.945, file_cluster_8: 13.038, file_cluster_4: 13.099
- **Magnitude:** 1131.86 | **LOC:** 1716 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.2567%), Tech Debt (21.4617%)
**Top Internal Functions/Classes:**
  * `REREADAC` (Impact: 29.0)
    * *Intent:* # Page 871
  * `NOREASON` (Impact: 19.1)
  * `COPYCYC1` (Impact: 16.5)
    * *Intent:* # Page 876
  * `LRVJOB` (Impact: 14.8)
  * `PIPSDONE` (Impact: 13.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 504`, `args: 59`, `func_start: 90`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 481`, `dead_code: 3`, `orphaned_logic: 14`
* *Architecture:* `api: 79`, `concurrency: 74`, `import: 41`
* *Defense:* `safety: 9`, `doc: 47`, `test: 2`, `sync_locks: 9`, `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` R12STUFF, 34, PHSNAME5, LRADRET, SERV2, SERV1, DVCNTR, SERV...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/EXTENDED_VERBS.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_13` (Drift: 12.159 IQR)
- **Top Global Matches:** file_cluster_13: 12.159, file_cluster_8: 12.177, file_cluster_4: 12.283
- **Magnitude:** 998.86 | **LOC:** 1682 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (57.7406%), Tech Debt (46.5951%)
**Top Internal Functions/Classes:**
  * `VERB69` (Impact: 33.6)
  * `LST2FAN` (Impact: 31.5)
  * `IMUATTCK` (Impact: 24.6)
    * *Intent:* # Page 281 # IMUATTCK VERB 43 DESCRIPTION # LOAD IMU ATTITUDE ERROR METERS # # 1. REQUIRE P00 OR FRE...
  * `RRDESNBK` (Impact: 22.4)
    * *Intent:* # Page 269 # DESIGNATE TO DESIRED GIMBAL ANGLES.
  * `AURLOKON` (Impact: 22.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 422`, `structural_boundaries: 391`, `args: 59`, `func_start: 100`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 191`, `fragile_debt: 3`, `orphaned_logic: 11`
* *Architecture:* `io: 19`, `api: 36`, `concurrency: 79`, `import: 36`
* *Defense:* `safety: 20`, `doc: 41`, `sync_locks: 20`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 7, ALPHASB, WWPOS, EXTVERBS, 34, EXTVB1, OGC, BCDU...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/CM_ENTRY_DIGITAL_AUTOPILOT.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Colossus 2A, AKA Comanche 055. It is part of the source code for the Command Module's (CM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_4` (Drift: 13.425 IQR)
- **Top Global Matches:** file_cluster_4: 13.425, file_cluster_13: 13.482, file_cluster_8: 13.605
- **Magnitude:** 951.74 | **LOC:** 1274 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.7031%), Tech Debt (14.7076%)
**Top Internal Functions/Classes:**
  * `BODYRATE` (Impact: 27.3)
  * `ATTRATES` (Impact: 23.5)
    * *Intent:* # Page 1073 # CALCULATE BODY ATTITUDE RATES AND INTEGRATE TO OBTAIN ATTITUDE ANGLES. # # CB PHIDOT T...
  * `EXDAP` (Impact: 21.9)
    * *Intent:* # 2. IF C(45) GEQ CALFA GEQ -C(45), USE CMDAPMOD = +1 # BETA: ROLL ERROR = SGN(-SALF) (BETACOM -BETA...
  * `EXDAP2` (Impact: 20.7)
  * `COMPAT` (Impact: 20.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 461`, `args: 55`, `func_start: 57`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 462`, `dead_code: 8`, `orphaned_logic: 5`
* *Architecture:* `io: 7`, `api: 86`, `concurrency: 42`, `import: 12`
* *Defense:* `safety: 3`, `doc: 35`, `sync_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DAPS1, COUNT, 15, T5LOC, ETRYDAP, RATEAVG, 20, AOG
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/IMU_CALIBRATION_AND_ALIGNMENT.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *POSITIONING ROUTINES FOR THE IMU PERFORMANCE TESTS AS WELL AS SOME OF THE TESTS THEMSELVES. FOR A DESCRIPTION OF THESE SUBROUTINES AND THE OPERATING PROCEDURES (TYPICALLY) SEE STG MEMO 685.THEORETICAL REF.E-1973 TAKE CARE OF DRIFT FLAG CALCULATE -COS LATITUDE AND SIN LATITUDE GYROCOMPASS COMES IN HERE Page 424 SEE IF IN OPTICAL VERIFICATION NO YES IF GLOKFAIL SET, GIMBAL LOCK +1 IF IN GIMBAL LOCK,OTHERWISE 0 RESET GIMBAL LOCK FLAG BIT 14 FLAG 3 IF ONE GO AND DO A PIPA TEST ONLY ALIGN AND MEASURE VERTICAL PIPA RATE Page 425 PIPA TEST PIP PULSE CATCHING ROUTINE Page 426 DEC585 HAS BEEN REDEFINED FOR LEM TAKE PLATFORM OUT OF GIMBAL LOCK ABOUT 1 HOUR VERTICAL DRIFT TEST 0 IF POSN 4 OFFSET PLATFORM ALLOW ONLY SOUTH GYRO EARTH RATE COMPENS Page 427 IMU NOT IN USE BIT 8 FLAG 0 Page 428 COARSE ALI...*
- **Global Archetype:** `file_cluster_8` (Drift: 12.65 IQR)
- **Top Global Matches:** file_cluster_8: 12.65, file_cluster_13: 12.775, file_cluster_4: 12.873
- **Magnitude:** 941.38 | **LOC:** 1407 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.1351%), Tech Debt (55.3653%)
**Top Internal Functions/Classes:**
  * `OPTDATA` (Impact: 22.6)
  * `RETARG` (Impact: 14.8)
  * `CHKCOMED` (Impact: 11.3)
  * `RETARG1` (Impact: 10.9)
  * `PIPJOBB` (Impact: 10.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 301`, `args: 26`, `func_start: 88`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 432`, `orphaned_logic: 29`
* *Architecture:* `io: 3`, `api: 26`, `concurrency: 70`, `import: 22`
* *Defense:* `safety: 12`, `doc: 39`, `sync_locks: 12`, `cleanup: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ALTIM, EBANK, ESTIMS, COUNT, IMUCAL1, LAT, EARTHR, GEOSAVE1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/T4RUPT_PROGRAM.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *CHANNEL 30 AND CALLS THE APPROPRIATE SUBROUTINES. THE BITS PROCESSED AND THEIR RELEVANT SUBROUTINES ARE:*
- **Global Archetype:** `file_cluster_8` (Drift: 12.547 IQR)
- **Top Global Matches:** file_cluster_8: 12.547, file_cluster_7: 12.668, file_cluster_13: 12.718
- **Magnitude:** 939.8 | **LOC:** 1468 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.054%), Tech Debt (21.1647%)
**Top Internal Functions/Classes:**
  * `STORCMD` (Impact: 28.0)
  * `PROCTNON` (Impact: 16.7)
    * *Intent:* # PROCESS IMU TURN-ON REQUESTS AFTER WAITING 1 SAMPLE FOR ALL SIGNALS TO ARRIVE.
  * `PIPFAIL` (Impact: 16.6)
    * *Intent:* # # JOBS OR TASKS INITIATED: NONE. # # SUBROUTINES CALLED: 1) SETISSW, AND 2) ALARM (SEE FUNCTIONAL ...
  * `ITURNON` (Impact: 15.0)
    * *Intent:* # JOBS OR TASKS INITIATED: NONE. # # SUBROUTINES CALLED: ALARM, IF THE ISS TURN-ON REQUEST IS NOT PR...
  * `OPTDRIVE` (Impact: 14.6)
    * *Intent:* # SHAFT STOP MONITOR-ZONE UPDATE
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 387`, `args: 51`, `func_start: 103`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 238`, `orphaned_logic: 9`
* *Architecture:* `io: 10`, `api: 76`, `concurrency: 25`, `import: 11`
* *Defense:* `doc: 84`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DSPCOUNT, COUNT, CDUIND, RELTAB, 12, OPTDRV, FFTAG12, T4RUP...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/P-AXIS_RCS_AUTOPILOT.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 12.604 IQR)
- **Top Global Matches:** file_cluster_8: 12.604, file_cluster_7: 12.857, file_cluster_13: 12.905
- **Magnitude:** 876.4 | **LOC:** 1057 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.084%), Tech Debt (16.8857%)
**Top Internal Functions/Classes:**
  * `RATERROR` (Impact: 28.1)
  * `PJETSLEC` (Impact: 26.7)
  * `BACKP` (Impact: 21.5)
  * `LAST` (Impact: 11.1)
  * `PAXIS` (Impact: 10.8)
    * *Intent:* # THE FOLLOWING T5RUPT ENTRY BEGINS THE PROGRAM WHICH CONTROLS THE P-AXIS ACTION OF THE LEM USING TH...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 388`, `args: 22`, `func_start: 50`
* *Risk/State:* `state_mutation: 451`, `orphaned_logic: 6`
* *Architecture:* `io: 3`, `api: 97`, `concurrency: 6`, `import: 3`
* *Defense:* `safety: 8`, `doc: 23`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DAPS1, EBANK, 16, AOSQ
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/P51-P53.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *ALIGNS THE IMU TO ONE OF THREE ORIENTATIONS SELECTED BY THE ASTRONAUT. THE PRESENT IMU ORIENTATION IS KNOWN AND IS STORED IN REFSMMAT. THE THREE POSSIBLE ORIENTATIONS MAY BE:*
- **Global Archetype:** `file_cluster_8` (Drift: 11.839 IQR)
- **Top Global Matches:** file_cluster_8: 11.839, file_cluster_13: 11.969, file_cluster_7: 12.08
- **Magnitude:** 842.74 | **LOC:** 2214 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.6828%), Tech Debt (9.8918%)
**Top Internal Functions/Classes:**
  * `PICAPAR` (Impact: 27.4)
  * `P52T` (Impact: 25.9)
  * `P52B` (Impact: 21.6)
  * `COARSTYP` (Impact: 20.4)
  * `TERM52` (Impact: 19.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 239`, `args: 23`, `func_start: 65`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 260`, `dead_code: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 17`, `api: 17`, `concurrency: 55`, `import: 39`
* *Defense:* `safety: 6`, `doc: 83`, `sync_locks: 6`, `cleanup: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` V06N89, P50S, R56, 26P50S, P50S2, RDCDUS, P50S3, PICAPAR...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/LUNAR_LANDING_GUIDANCE_EQUATIONS.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 12.505 IQR)
- **Top Global Matches:** file_cluster_8: 12.505, file_cluster_13: 12.732, file_cluster_7: 12.783
- **Magnitude:** 806.96 | **LOC:** 1475 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.2117%), Tech Debt (32.6357%)
**Top Internal Functions/Classes:**
  * `STARTP67` (Impact: 19.1)
  * `REDESMON` (Impact: 12.8)
  * `RODCOMP` (Impact: 12.2)
  * `ROOTLOOP` (Impact: 12.0)
    * *Intent:* # CONVERGE ON ROOT
  * `QUADGUID` (Impact: 11.0)
    * *Intent:* # # AS PUBLISHED -- # ___ __ ___ __ # ___ ___ 6(VDG + VG) 12(RDG - RG) # ACG = ADG + ----------- + -...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 337`, `args: 41`, `func_start: 75`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 376`, `orphaned_logic: 17`
* *Architecture:* `io: 10`, `api: 50`, `concurrency: 14`, `import: 14`
* *Defense:* `safety: 2`, `doc: 33`, `sync_locks: 2`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COUNT, 20, 11, E2DPS, DVCNTR, LANDCNST, PIF, PHSNAME2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/AOSTASK_AND_AOSJOB.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *1/ACCS PROVIDES THE INTERFACE BETWEEN THE GUIDANCE PROGRAMS AND THE DIGITAL AUTOPILOT. WHENEVER THERE IS A CHANGE IN THE MASS OF THE VEHICLE, IN THE DEADBAND SELECTED, IN THE VEHICLE CONFIGURATION (ASCENT-DESCENT- DOCKED), AND DURING A FRESH START OR A RESTART, 1/ACCS IS CALLED TO COMMUNICATE THE DATA CHANGES TO THE DAP.*
- **Global Archetype:** `file_cluster_8` (Drift: 12.905 IQR)
- **Top Global Matches:** file_cluster_8: 12.905, file_cluster_13: 12.978, file_cluster_7: 13.079
- **Magnitude:** 788.2 | **LOC:** 1070 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.8822%), Tech Debt (17.3%)
**Top Internal Functions/Classes:**
  * `SPSLOOP2` (Impact: 18.4)
  * `FIXMIN` (Impact: 12.8)
  * `ACCTHERE` (Impact: 12.4)
  * `SKIPDB1` (Impact: 10.5)
  * `STACCDOT` (Impact: 9.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 454`, `args: 22`, `func_start: 45`
* *Risk/State:* `state_mutation: 458`, `dead_code: 1`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 104`, `concurrency: 6`, `import: 6`
* *Defense:* `safety: 12`, `doc: 33`, `test: 1`, `sync_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EBANK, COUNT, AOSQ, 20, DAPS3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/FRESH_START_AND_RESTART.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *SUNDISK REV 120 FUNCTIONAL DESCRIPTION SLAP1 MAN INITIATED FRESH START 1. EXECUTE STARTSUB 2. TURN OFF DSKY DISCRETE-LAMPS 3. CLEAR FAIL REGISTERS,SELF-CHECK ERROR COUNTER AND RESTART COUNTER 4. EXECUTE DOFSTART DOFSTART MACHINE INITIATED FRESH START 1. CLEAR SELF-CHECK REGISTERS, MODE REGISTER AND CDUZ REGISTER 2. CLEAR PHASE TABLE 3. INITIALIZE IMU FLAGS 4. INITIALIZE FLAGWORDS 5. TRANSFER CONTROL TO IDLE LOOP IN DUMMYJOB GOPROG HARDWARE RESTART 0. EXECUTE STARTSUB 1. TRANSFER CONTROL TO DOFSTART IF ANY OF THE FOLLOWING CONDITIONS EXIST. A. RESTART OCCURED DURING EXECUTION OF ERASCHK B. BOTH OSCILLATOR FAIL AND AGC WARNING ARE ON C. MARK REJECT AND EITHER NAV OR MAIN DSKY ERROR LIGHT RESET ARE ON. 2. SCHEDULE A T5RUPT PROGRAM FOR THE DAP 3. SET FLAGWRD5 BITS FOR INTWAKE ROUTINE 4. EXTING...*
- **Global Archetype:** `file_cluster_8` (Drift: 12.635 IQR)
- **Top Global Matches:** file_cluster_8: 12.635, file_cluster_13: 12.667, file_cluster_7: 12.843
- **Magnitude:** 784.48 | **LOC:** 1481 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.5445%), Tech Debt (14.7336%)
**Top Internal Functions/Classes:**
  * `V5OUT2` (Impact: 20.9)
  * `PCLOOP` (Impact: 19.0)
  * `DOFSTART` (Impact: 11.5)
  * `GOP00FIX` (Impact: 11.5)
  * `V37` (Impact: 11.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 466`, `args: 57`, `func_start: 60`
* *Risk/State:* `state_mutation: 357`, `orphaned_logic: 6`
* *Architecture:* `io: 11`, `api: 67`, `concurrency: 33`, `import: 23`
* *Defense:* `safety: 13`, `doc: 41`, `sync_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BESTI, OGANOW, LST1, VAC5LOC, SUBEXIT, PREMM1, PACTOFF, STARIND...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/DISPLAY_INTERFACE_ROUTINES.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Luminary 1A build 099. It is part of the source code for the Lunar Module's (LM) Apollo Guidance Computer (AGC), for Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 12.777 IQR)
- **Top Global Matches:** file_cluster_8: 12.777, file_cluster_13: 12.846, file_cluster_4: 12.883
- **Magnitude:** 775.46 | **LOC:** 1460 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.4606%), Tech Debt (92.5133%)
**Top Internal Functions/Classes:**
  * `NORMRET` (Impact: 18.6)
  * `FLASHSUB` (Impact: 18.4)
  * `OKTOPLAY` (Impact: 16.6)
  * `LINUSCHR` (Impact: 14.6)
  * `JOBXCHS` (Impact: 13.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 352`, `args: 34`, `func_start: 121`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 238`, `dead_code: 1`, `orphaned_logic: 34`
* *Architecture:* `io: 10`, `api: 45`, `concurrency: 23`, `import: 5`
* *Defense:* `safety: 18`, `doc: 39`, `sync_locks: 18`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DISPLAYS, COUNT, FFTAG4, WHOCARES, NVWORD, NVSAVE, 10
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/DISPLAY_INTERFACE_ROUTINES.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Comanche, build 055. It is part of the source code for the Command Module's (CM) Apollo Guidance Computer (AGC), Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 12.836 IQR)
- **Top Global Matches:** file_cluster_8: 12.836, file_cluster_13: 12.861, file_cluster_4: 12.884
- **Magnitude:** 769.2 | **LOC:** 1477 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.0076%), Tech Debt (91.6281%)
**Top Internal Functions/Classes:**
  * `NORMRET` (Impact: 18.6)
  * `FLASHSUB` (Impact: 18.4)
  * `OKTOPLAY` (Impact: 16.6)
    * *Intent:* # Page 1471
  * `LINUSCHR` (Impact: 14.6)
  * `JOBXCHS` (Impact: 13.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 350`, `args: 34`, `func_start: 121`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 235`, `dead_code: 2`, `orphaned_logic: 33`
* *Architecture:* `io: 10`, `api: 45`, `concurrency: 23`, `import: 5`
* *Defense:* `safety: 18`, `doc: 38`, `sync_locks: 18`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DISPLAYS, COUNT, FFTAG4, WHOCARES, NVWORD, NVSAVE, 10
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/IMU_MODE_SWITCHING_ROUTINES.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *LOG SECTION IMU MODE SWITCHING MOD BY- R.MELANSON TO ADD DOCUMENTATION ASSEMBLY SUNDISK REV. 82*
- **Global Archetype:** `file_cluster_4` (Drift: 12.956 IQR)
- **Top Global Matches:** file_cluster_4: 12.956, file_cluster_13: 12.97, file_cluster_8: 13.013
- **Magnitude:** 751.2 | **LOC:** 1068 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.743%), Tech Debt (43.1993%)
**Top Internal Functions/Classes:**
  * `GSELECT` (Impact: 21.4)
  * `PRESTAND` (Impact: 17.3)
  * `POSTAND` (Impact: 16.8)
  * `8192AUG` (Impact: 13.1)
  * `IMUZEROA` (Impact: 13.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 306`, `args: 36`, `func_start: 74`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 268`, `dead_code: 2`, `orphaned_logic: 14`
* *Architecture:* `io: 1`, `api: 44`, `concurrency: 35`, `import: 10`
* *Defense:* `safety: 12`, `doc: 48`, `sync_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SCALSAVE, EBANK, COUNT, MODESW, 1400, CDUIND, P05P06, 11...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/BURN_BABY_BURN--MASTER_IGNITION_ROUTINE.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *KILLTASK IS USED TO REMOVE A TASK FROM THE WAITLIST BY SUBSTITUTING A NULL TASK CALLED `NULLTASK' (OF COURSE), WHICH MERELY DOES A TC TASKOVER. IF THE SAME TASK IS SCHEDULED MORE THAN ONCE, ONLY THE ONE WHICH WILL OCCUR FIRST IS REMOVED. IF THE TASK IS NOT SCHEDULED, KILLTASK TAKES NO ACTION AND RETURNS WITH NO ALARM. KILLTASK LEAVES INTERRUPTS INHIBITED SO CALLER MUST RELINT*
- **Global Archetype:** `file_cluster_4` (Drift: 12.415 IQR)
- **Top Global Matches:** file_cluster_4: 12.415, file_cluster_13: 12.556, file_cluster_8: 12.685
- **Magnitude:** 748.68 | **LOC:** 1060 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.6937%), Tech Debt (33.2961%)
**Top Internal Functions/Classes:**
  * `P41TABLE` (Impact: 42.1)
  * `P40AUTO` (Impact: 14.6)
  * `STCLOK3` (Impact: 11.8)
  * `TIG-35` (Impact: 11.1)
    * *Intent:* # ********************************
  * `ASTNRETN` (Impact: 10.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 260`, `args: 50`, `func_start: 66`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 212`, `dead_code: 1`, `orphaned_logic: 12`
* *Architecture:* `io: 4`, `api: 31`, `concurrency: 128`, `import: 20`
* *Defense:* `safety: 13`, `doc: 31`, `test: 2`, `sync_locks: 13`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TRKMKCNT, P40S2, 36, OMEGAQ, STARIND, TTOGO, 31, P40S3...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/IMU_MODE_SWITCHING_ROUTINES.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *LOG SECTION IMU MODE SWITCHING MOD BY- R.MELANSON TO ADD DOCUMENTATION ASSEMBLY SUNDISK REV. 82 FUNCTIONAL DESCRIPTION- TO DELAY FURTHER EXECUTION OF THE CALLING ROUTINE UNTIL ITS SELECTED I/O FUNCTION IS COMPLETE. THE FOLLOWING CHECKS ON THE CALLING ROUTINES MODECADR ARE MADE AND ACTED UPON. 1) +0 INDICATES INCOMPLETE I/O OPERATION.CALLING ROUTINE IS PUT TO SLEEP. 2) -1 INDICATES COMPLETED I/O OPERATION. STALL BYPASSES JOBSLEEP CALL AND RETURNS TO CALLING ROUTINE AT L+3 3) -0 INDICATES COMPLETED I/O WITH FAILURE. STALL CLEARS MODECADR AND RETURNS TO CALLING ROUTINE AT L+2. 4) VALUE GREATER THAN 0 INDICATES TWO ROUTINES CALLING FOR USE OF SAME DEVICE. STALL EXITS TO ABORT WHICH EXECUTES A PROGRAM RESTART WHICH IN TURN CLEARS ALL MODECADR REGISTERS. CALLING SEQUENCE- L TC BANKCALL L+1 CADR ...*
- **Global Archetype:** `file_cluster_13` (Drift: 12.927 IQR)
- **Top Global Matches:** file_cluster_13: 12.927, file_cluster_8: 12.934, file_cluster_4: 12.938
- **Magnitude:** 746.84 | **LOC:** 1067 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.5922%), Tech Debt (43.4398%)
**Top Internal Functions/Classes:**
  * `GSELECT` (Impact: 21.4)
  * `PRESTAND` (Impact: 17.3)
  * `POSTAND` (Impact: 16.8)
  * `8192AUG` (Impact: 13.1)
  * `IMUZEROA` (Impact: 13.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 305`, `args: 36`, `func_start: 74`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 265`, `dead_code: 1`, `orphaned_logic: 14`
* *Architecture:* `io: 1`, `api: 44`, `concurrency: 35`, `import: 10`
* *Defense:* `safety: 12`, `doc: 48`, `sync_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SCALSAVE, EBANK, COUNT, MODESW, 1400, CDUIND, P05P06, 11...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Comanche055/EXTENDED_VERBS.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *Part of the source code for Comanche, build 055. It is part of the source code for the Command Module's (CM) Apollo Guidance Computer (AGC), Apollo 11.*
- **Global Archetype:** `file_cluster_8` (Drift: 11.77 IQR)
- **Top Global Matches:** file_cluster_8: 11.77, file_cluster_4: 11.926, file_cluster_13: 11.96
- **Magnitude:** 739.68 | **LOC:** 1316 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.18%), Tech Debt (22.4474%)
**Top Internal Functions/Classes:**
  * `VERB69` (Impact: 33.6)
  * `LST2FAN` (Impact: 31.5)
  * `IMUATTCK` (Impact: 22.5)
    * *Intent:* # Page 249 # IMUATTCK VERB 43 DESCRIPTION # LOAD IMU ATTITUDE ERROR METERS # 1. REQUIRE PROGRAM 00 A...
  * `IMUZEROK` (Impact: 16.7)
    * *Intent:* # (NOT IN USE YET)
  * `OPTCOARK` (Impact: 15.1)
    * *Intent:* # Page 242 # TEMPORARY ROUTINE TO RUN THE OPTICS CDUS FROM THE KEYBOARD
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 338`, `structural_boundaries: 208`, `args: 33`, `func_start: 85`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 119`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 5`, `api: 28`, `concurrency: 55`, `import: 9`
* *Defense:* `safety: 12`, `doc: 33`, `sync_locks: 12`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 7, STROKER, SUBEXIT, EXTVERBS, PACTOFF, 10, W, RHOSB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/FRESH_START_AND_RESTART.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *FLASH V 37 ON DSKY MM CHANGE REQUEST*
- **Global Archetype:** `file_cluster_8` (Drift: 12.199 IQR)
- **Top Global Matches:** file_cluster_8: 12.199, file_cluster_13: 12.364, file_cluster_7: 12.437
- **Magnitude:** 697.4 | **LOC:** 1243 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.8184%), Tech Debt (18.9264%)
**Top Internal Functions/Classes:**
  * `SETUP70` (Impact: 17.1)
  * `PCLOOP` (Impact: 15.5)
  * `V37` (Impact: 15.1)
    * *Intent:* # D. DEBRIS # MMNUMBER, MPAC +1, MINDEX, BASETEMP +C(MINDEX), FLAGWRD0, FLAGWRD1, FLAGWRD2, MODREG, ...
  * `RENDV00` (Impact: 13.2)
  * `DOFSTRT1` (Impact: 12.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 477`, `args: 27`, `func_start: 55`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 334`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 10`, `api: 60`, `concurrency: 20`, `import: 11`
* *Defense:* `safety: 7`, `doc: 36`, `sync_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EBANK, COUNT, VERB37, INTINIT, R, AOSQ, LST1, RRECTCSM...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Luminary099/T4RUPT_PROGRAM.agc` (AGC_ASSEMBLY | Tier 2 | AI Safe: 0.0%)
> **System Purpose:** *CHANNEL 30 AND CALLS THE APPROPRIATE SUBROUTINES. THE BITS PROCESSED AND THEIR RELEVANT SUROUTINES ARE: FUNCTION BIT SUBROUTINE CALLED -------- --- ----------------- TEMP IN LIMITS 15 TLIM ISS TURN-ON REQUEST 14 ITURNON IMU FAIL 13 IMUFAIL (SETISSW) IMU CDU FAIL 12 ICDUFAIL (SETISSW) IMU CAGE 11 IMUCAGE IMU OPERATE 9 IMUOP THE LAST SAMPLED STATE OF THESE BITS IS LEFT IN IMODES30. ALSO, EACH SUBROUTINE CALLED FINDS THE NEW VALUE OF THE BIT IN A, WITH Q SET TO THE PROPER RETURN LOCATION NXTIFAIL. CALLING SEQUENCE: T4RUPT EVERY 480 MILLISECONDS. JOBS OR TASKS INITIATED: NONE. SUBROUTINES CALLED: TLIM, TURNON, SETISSW, IMUCAGE, IMUOP. ERASABELE INITIALIZATION: FRESH START OR RESTART WITH NO GROUPS ACTIVE: C((MODES30) = OCT 37411). RESTART WITH ACTIVE GROUPS: C(IMODES30) = (B(IMODES30)AND(OCT 0...*
- **Global Archetype:** `file_cluster_8` (Drift: 12.505 IQR)
- **Top Global Matches:** file_cluster_8: 12.505, file_cluster_7: 12.572, file_cluster_13: 12.666
- **Magnitude:** 692.58 | **LOC:** 1355 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.0831%), Tech Debt (17.4856%)
**Top Internal Functions/Classes:**
  * `TRKFLCDU` (Impact: 25.5)
  * `MONREPOS` (Impact: 18.5)
  * `RRCDUCHK` (Impact: 17.0)
  * `PROCTNON` (Impact: 16.7)
    * *Intent:* # PROCESS IMU TURN-ON REQUESTS AFTER WAITING 1 SAMPLE FOR ALL SIGNALS TO ARRIVE.
  * `PIPFAIL` (Impact: 16.6)
    * *Intent:* # # JOBS OR TASKS INITIATED: NONE. # # SUBROUTINES CALLED: 1) SETISSW, AND 2) ALARM (SEE FUNCITONAL ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 288`, `args: 44`, `func_start: 61`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 168`, `orphaned_logic: 5`
* *Architecture:* `io: 11`, `api: 61`, `concurrency: 24`, `import: 8`
* *Defense:* `doc: 108`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DSPCOUNT, EBANK, M11, COUNT, CDUIND, FFTAG10, LOSCOUNT, 12...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Luminary099/SPS_BACK-UP_RCS_CONTROL.agc` (AGC_ASSEMBLY) | Magnitude: 85.7 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 89, indent_tabs: 72, structural_boundaries: 39, branch: 32
- `Comanche055/IMU_MODE_SWITCHING_ROUTINES.agc` (AGC_ASSEMBLY) | Magnitude: 746.84 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 675, indent_tabs: 585, structural_boundaries: 305, state_mutation: 265
- `Comanche055/TVCRESTARTS.agc` (AGC_ASSEMBLY) | Magnitude: 99.32 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: encapsulation: 85, indent_tabs: 81, structural_boundaries: 42, branch: 28
- `Luminary099/EXTENDED_VERBS.agc` (AGC_ASSEMBLY) | Magnitude: 998.86 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 1054, indent_tabs: 907, branch: 422, structural_boundaries: 391
- `Comanche055/AGC_BLOCK_TWO_SELF-CHECK.agc` (AGC_ASSEMBLY) | Magnitude: 373.92 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 354, indent_tabs: 261, structural_boundaries: 180, state_mutation: 161

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Luminary099/WAITLIST.agc` (AGC_ASSEMBLY) | Magnitude: 324.88 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 268, indent_tabs: 231, structural_boundaries: 149, state_mutation: 143
- `Luminary099/IMU_MODE_SWITCHING_ROUTINES.agc` (AGC_ASSEMBLY) | Magnitude: 751.2 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: encapsulation: 677, indent_tabs: 583, structural_boundaries: 306, state_mutation: 268
- `Comanche055/P40-P47.agc` (AGC_ASSEMBLY) | Magnitude: 1422.54 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 1736, indent_tabs: 1532, state_mutation: 485, structural_boundaries: 480
- `Comanche055/R30.agc` (AGC_ASSEMBLY) | Magnitude: 235.18 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 278, indent_tabs: 238, branch: 68, state_mutation: 67
- `Luminary099/RCS_FAILURE_MONITOR.agc` (AGC_ASSEMBLY) | Magnitude: 60.16 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: encapsulation: 77, indent_tabs: 70, structural_boundaries: 32, state_mutation: 24

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
- `Luminary099/INTER-BANK_COMMUNICATION.agc` (AGC_ASSEMBLY) | Magnitude: 116.06 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 79, encapsulation: 78, indent_tabs: 64, structural_boundaries: 50
- `Luminary099/P30_P37.agc` (AGC_ASSEMBLY) | Magnitude: 34.66 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: encapsulation: 78, indent_tabs: 72, doc: 16, branch: 14
- `Comanche055/INTER-BANK_COMMUNICATION.agc` (AGC_ASSEMBLY) | Magnitude: 116.16 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 79, encapsulation: 78, indent_tabs: 64, structural_boundaries: 50
- `Comanche055/TVCEXECUTIVE.agc` (AGC_ASSEMBLY) | Magnitude: 170.38 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: encapsulation: 146, indent_tabs: 133, state_mutation: 79, structural_boundaries: 54
- `Luminary099/LUNAR_AND_SOLAR_EPHEMERIDES_SUBROUTINES.agc` (AGC_ASSEMBLY) | Magnitude: 32.62 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: encapsulation: 86, indent_tabs: 75, scientific: 16, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `Comanche055/LUNAR_LANDMARK_SELECTION_FOR_CM.agc` (AGC_ASSEMBLY) | Magnitude: 10.52 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: spec_exposure: 4, doc: 3, ownership: 1
- `Comanche055/CONTRACT_AND_APPROVALS.agc` (AGC_ASSEMBLY) | Magnitude: 10.52 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: spec_exposure: 6, doc: 2, ownership: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Comanche055/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc` -> **Zachary Pedigo** (100.0% isolated ownership) | Magnitude: 3092.62
- `Luminary099/EXTENDED_VERBS.agc` -> **Matt Chaulklin** (100.0% isolated ownership) | Magnitude: 998.86
- `Luminary099/UPDATE_PROGRAM.agc` -> **Zachary Pedigo** (100.0% isolated ownership) | Magnitude: 345.04

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Comanche055/TAGS_FOR_RELATIVE_SETLOC.agc` -> **Severity: 406.5** (Blast Radius: 4.065 * Doc Risk: 100.0%)
- `Luminary099/TAGS_FOR_RELATIVE_SETLOC.agc` -> **Severity: 406.5** (Blast Radius: 4.065 * Doc Risk: 100.0%)
- `Comanche055/TVCDAPS.agc` -> **Severity: 391.742** (Blast Radius: 4.065 * Doc Risk: 96.3694%)
- `Luminary099/LANDING_ANALOG_DISPLAYS.agc` -> **Severity: 372.3** (Blast Radius: 4.065 * Doc Risk: 91.5867%)
- `Luminary099/AOSTASK_AND_AOSJOB.agc` -> **Severity: 370.408** (Blast Radius: 4.065 * Doc Risk: 91.1212%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
