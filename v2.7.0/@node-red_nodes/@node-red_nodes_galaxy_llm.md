# ARCHITECTURAL_BRIEF: @node-red_nodes
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
| Total Artifacts | 596 |
| Analyzed Artifacts (Scanned) | 580 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16 |
| Total LOC | 38137 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 97.3% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| HTML | 383 | 20104 | 66.0% |
| JSON | 111 | 8496 | 19.1% |
| XML | 46 | 4 | 7.9% |
| JAVASCRIPT | 38 | 9533 | 6.6% |
| MARKDOWN | 1 | 0 | 0.2% |
| PLAINTEXT | 1 | 0 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 516 | 89.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 62 | 10.7% |
| Static: Literature & Documentation | 2 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 16*

**Composition by Extension & Reason:**
- `.json`: 3x Excluded (Static Asset Blob without Intent: 1163 LOC), 1x Excluded (Static Asset Blob without Intent: 1039 LOC), 1x Excluded (Static Asset Blob without Intent: 1161 LOC)
- `.html`: 1x Excluded (Machine-Generated Source Code Signature: 51 LOC), 1x Excluded (Saturation: Line 62 exceeds 500 chars), 1x Excluded (Saturation: Line 71 exceeds 500 chars)
- `.demo`: 2x Excluded (Unsupported Extension: '.demo')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unresolved Ambiguity (No Retainable Structure)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.6 | 6.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.9 | 11.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.8 | 3.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.6 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 8.2 | 2.8 | 3.5 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 35.8 | 0.3 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 24.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 44.6 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 56 | 17 | 0 | `package/core/network/31-tcpin.js` |
| cleanup | 87 | 20 | 0 | `package/core/network/31-tcpin.js` |
| guards | 1865 | 75 | 2 | `package/core/network/10-mqtt.js` |
| danger | 348 | 60 | 1 | `package/core/network/10-mqtt.js` |
| concurrency | 330 | 52 | 0 | `package/core/function/89-delay.html` |
| connectivity | 556 | 419 | 2 | `package/core/network/22-websocket.html` |
| io | 46 | 9 | 0 | `package/core/storage/10-file.js` |
| crypto | 3 | 3 | 0 | `package/core/common/60-link.js` |
| ipc | 7 | 2 | 0 | `package/core/common/21-debug.html` |
| time | 121 | 18 | 0 | `package/core/function/89-delay.js` |
| serialization | 48 | 15 | 0 | `package/core/network/10-mqtt.js` |
| regex | 115 | 22 | 0 | `package/core/parsers/70-CSV.js` |
| events | 677 | 92 | 3 | `package/core/network/31-tcpin.js` |
| tests | 0 | 0 | 0 | - |
| docs | 84 | 32 | 0 | `package/core/network/10-mqtt.js` |
| debt | 35 | 23 | 0 | `package/core/common/21-debug.html` |
| mutation | 8058 | 424 | 28 | `package/core/network/10-mqtt.js` |
| dead_code | 110 | 37 | 0 | `package/core/network/10-mqtt.js` |
| credential | 0 | 0 | 0 | - |
| threat | 60 | 19 | 0 | `package/core/function/10-function.js` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 14 | 5 | 0 | `package/core/common/20-inject.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/core/storage/10-file.js` (Hits: 15)
- `package/core/common/21-debug.js` (Hits: 6)
- `package/core/network/21-httprequest.js` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.js** (`package/index.js`) — 1 inbound connections
2. **README.md** (`package/README.md`) — 0 inbound connections
3. **05-junction.html** (`package/core/common/05-junction.html`) — 0 inbound connections
4. **20-inject.html** (`package/core/common/20-inject.html`) — 0 inbound connections
5. **21-debug.html** (`package/core/common/21-debug.html`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **21-httprequest.js** (`package/core/network/21-httprequest.js`) — 14 outbound dependencies
2. **21-httpin.js** (`package/core/network/21-httpin.js`) — 11 outbound dependencies
3. **10-mqtt.js** (`package/core/network/10-mqtt.js`) — 5 outbound dependencies
4. **22-websocket.js** (`package/core/network/22-websocket.js`) — 5 outbound dependencies
5. **21-debug.js** (`package/core/common/21-debug.js`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `createLWT` (@ `package/core/network/10-mqtt.js`) -> Impact: **661.3** | LOC: 739
- `exports` (@ `package/core/network/10-mqtt.js`) -> Impact: **637.5** | LOC: 1323
  * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except in compliance with the License. * You may obtai...
- `setOptions` (@ `package/core/network/10-mqtt.js`) -> Impact: **607.1** | LOC: 1022
  * *Intent:* /** @type {mqtt.MqttClient}*/ this.client;
- `MQTTBrokerNode` (@ `package/core/network/10-mqtt.js`) -> Impact: **505.8** | LOC: 1036
  * *Intent:* //#endregion "Supporting functions" //#region "Broker node"
- `exports` (@ `package/core/parsers/70-CSV.js`) -> Impact: **493.3** | LOC: 674
  * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except in compliance with the License. * You may obtai...
- `exports` (@ `package/core/network/21-httprequest.js`) -> Impact: **403.9** | LOC: 838
  * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except in compliance with the License. * You may obtai...
- `exports` (@ `package/core/network/31-tcpin.js`) -> Impact: **379.5** | LOC: 887
  * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except in compliance with the License. * You may obtai...
- `exports` (@ `package/core/sequence/17-split.js`) -> Impact: **373.7** | LOC: 799
  * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except in compliance with the License. * You may obtai...
- `HTTPRequest` (@ `package/core/network/21-httprequest.js`) -> Impact: **356.8** | LOC: 687
- `exports` (@ `package/core/function/10-switch.js`) -> Impact: **244.7** | LOC: 510
  * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except in compliance with the License. * You may obtai...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/core/network` | 16 | 9236.12 | 43.31% | 14.69% |
| `package/core/function` | 18 | 6515.64 | 58.58% | 12.7% |
| `package/core/common` | 20 | 2857.58 | 33.36% | 29.74% |
| `package/core/sequence` | 6 | 2292.72 | 51.5% | 6.52% |
| `package/core/parsers` | 10 | 1897.3 | 40.83% | 23.16% |
| `package/core/storage` | 4 | 1045.96 | 42.61% | 26.49% |
| `package/icons` | 46 | 455.36 | 0.0% | 0.0% |
| `package/examples/parser/csv` | 10 | 173.38 | 0.0% | 0.0% |
| `package/examples/network/http` | 7 | 126.68 | 0.0% | 0.0% |
| `package/examples/storage/read file` | 4 | 71.2 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/locales/ko/common/21-debug.html` -> **99.8499%** Exposure
- `package/core/storage/23-watch.js` -> **94.7457%** Exposure
- `package/core/common/05-junction.js` -> **73.1059%** Exposure
- `package/core/common/24-complete.js` -> **73.1059%** Exposure
- `package/core/common/25-catch.js` -> **73.1059%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/core/common/20-inject.html` -> **100.0%** Exposure
- `package/core/common/21-debug.html` -> **100.0%** Exposure
- `package/core/common/24-complete.html` -> **100.0%** Exposure
- `package/core/common/25-catch.html` -> **100.0%** Exposure
- `package/core/common/25-status.html` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/core/network/10-mqtt.js` -> **6** Orphaned Functions | **0** Duplicates
- `package/core/function/10-function.js` -> **4** Orphaned Functions | **0** Duplicates
- `package/core/common/20-inject.js` -> **2** Orphaned Functions | **0** Duplicates
- `package/core/common/60-link.js` -> **2** Orphaned Functions | **0** Duplicates
- `package/core/function/15-change.js` -> **2** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `67` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/core/function/89-delay.js` (JAVASCRIPT) -> Cumulative Risk: **729.85**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 773.1 | **LOC:** 425 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.849%), Cognitive Load (96.7372%)
- **Heaviest Functions:** `exports` (Impact: 214.1), `DelayNode` (Impact: 208.8), `maxKeptMsgsCount` (Impact: 6.3)

### 2. `package/core/parsers/70-XML.js` (JAVASCRIPT) -> Cumulative Risk: **719.84**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 104.22 | **LOC:** 49 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.998%)
- **Heaviest Functions:** `exports` (Impact: 27.8), `XMLNode` (Impact: 27.5)

### 3. `package/core/sequence/19-batch.js` (JAVASCRIPT) -> Cumulative Risk: **688.41**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 396.72 | **LOC:** 318 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.1772%), Cognitive Load (91.2924%)
- **Heaviest Functions:** `exports` (Impact: 99.9), `BatchNode` (Impact: 52.0), `concat_msg` (Impact: 24.1)

### 4. `package/core/network/22-websocket.js` (JAVASCRIPT) -> Cumulative Risk: **686.87**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 555.4 | **LOC:** 457 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (91.8838%), Concurrency (84.6488%)
- **Heaviest Functions:** `exports` (Impact: 135.1), `WebSocketListenerNode` (Impact: 72.1), `WebSocketOutNode` (Impact: 29.0)

### 5. `package/core/sequence/18-sort.js` (JAVASCRIPT) -> Cumulative Risk: **644.08**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 321.8 | **LOC:** 267 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9996%), State Flux (99.9883%), Cognitive Load (88.1525%)
- **Heaviest Functions:** `exports` (Impact: 76.1), `SortNode` (Impact: 70.3), `processMessage` (Impact: 20.9)

### 6. `package/core/storage/23-watch.js` (JAVASCRIPT) -> Cumulative Risk: **639.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 104.32 | **LOC:** 74 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.7815%), Tech Debt (94.7457%)
- **Heaviest Functions:** `exports` (Impact: 28.3), `WatchNode` (Impact: 27.9), `close` (Impact: 1.1)

### 7. `package/core/function/10-function.js` (JAVASCRIPT) -> Cumulative Risk: **626.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 666.44 | **LOC:** 545 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9996%), Concurrency (99.9631%), Cognitive Load (97.6601%)
- **Heaviest Functions:** `exports` (Impact: 146.6), `FunctionNode` (Impact: 108.4), `sendResults` (Impact: 50.8)

### 8. `package/core/function/89-trigger.js` (JAVASCRIPT) -> Cumulative Risk: **622.21**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 786.88 | **LOC:** 306 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (95.9323%)
- **Heaviest Functions:** `exports` (Impact: 184.2), `TriggerNode` (Impact: 183.9), `processMessage` (Impact: 108.4)

### 9. `package/core/network/32-udp.js` (JAVASCRIPT) -> Cumulative Risk: **618.12**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 384.12 | **LOC:** 285 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.738%), Cognitive Load (83.2939%)
- **Heaviest Functions:** `exports` (Impact: 129.4), `UDPout` (Impact: 80.4), `UDPin` (Impact: 49.5)

### 10. `package/core/common/20-inject.js` (JAVASCRIPT) -> Cumulative Risk: **614.59**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 275.06 | **LOC:** 198 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (95.139%), Safety Score (89.3967%)
- **Heaviest Functions:** `exports` (Impact: 75.5), `InjectNode` (Impact: 60.9), `evaluateProperty` (Impact: 22.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/core/network/10-mqtt.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3926.98 | **LOC:** 1512 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.0937%), Tech Debt (12.8129%)
**Top Internal Functions/Classes:**
  * `createLWT` (Impact: 661.3)
  * `exports` (Impact: 637.5)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `setOptions` (Impact: 607.1)
    * *Intent:* /** @type {mqtt.MqttClient}*/ this.client;
  * `MQTTBrokerNode` (Impact: 505.8)
    * *Intent:* //#endregion "Supporting functions" //#region "Broker node"
  * `MQTTInNode` (Impact: 100.5)
    * *Intent:* //#endregion "Broker node" //#region "MQTTIn node"
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 209 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 657
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 452`, `structural_boundaries: 110`, `args: 78`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 239`, `dead_code: 12`, `unreferenced_by_name: 6`
* *Architecture:* `api: 1`, `concurrency: 8`, `import: 5`
* *Defense:* `safety: 167`, `doc: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` proxyHelper, https-proxy-agent, is-utf8, mqtt, url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/sequence/17-split.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1417.26 | **LOC:** 816 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.4837%), Tech Debt (10.5761%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 373.7)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `JoinNode` (Impact: 208.5)
  * `SplitNode` (Impact: 112.4)
  * `completeSend` (Impact: 38.3)
  * `reduceMessage` (Impact: 28.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 173 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 550
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 123`, `args: 38`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 204`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `concurrency: 2`
* *Defense:* `safety: 102`, `doc: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/parsers/70-CSV.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1362.28 | **LOC:** 691 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.7866%), Tech Debt (15.6284%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 493.3)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `hasTemplate` (Impact: 151.8)
  * `CSVNode` (Impact: 84.9)
  * `clean` (Impact: 64.6)
    * *Intent:* // pass in an array of column names to be trimmed, de-quoted and retrimmed
  * `addQuotes` (Impact: 12.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 170 instances
* *State Mutation (weighted view):* 526
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 71`, `args: 19`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 186`, `dead_code: 15`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 153`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` csv, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/31-tcpin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1295.46 | **LOC:** 904 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.0429%), Tech Debt (10.4031%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 379.5)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `TcpGet` (Impact: 174.0)
  * `TcpOut` (Impact: 95.2)
  * `TcpIn` (Impact: 94.0)
  * `setupTcpClient` (Impact: 29.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 138 instances
* *Concurrency (weighted view):* 43
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 434
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 89`, `args: 55`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 158`, `dead_code: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 8`, `import: 3`
* *Defense:* `safety: 80`, `doc: 3`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` denque, net, tls
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/21-httprequest.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1293.94 | **LOC:** 855 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.5442%), Tech Debt (20.2594%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 403.9)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `HTTPRequest` (Impact: 356.8)
  * `updateKey` (Impact: 82.4)
  * `buildDigestHeader` (Impact: 49.2)
  * `ha1Compute` (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 97 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 307
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 120`, `args: 33`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 113`, `dead_code: 5`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 4`, `import: 15`
* *Defense:* `safety: 97`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` proxyHelper, cookie, crypto, form-data, got, hash-sum, hpagent, http...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/15-change.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 880.54 | **LOC:** 363 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.8773%), Tech Debt (15.9893%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 223.8)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `ChangeNode` (Impact: 223.5)
  * `applyRule` (Impact: 119.8)
  * `callback` (Impact: 36.3)
  * `getToValue` (Impact: 33.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 53`, `args: 24`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 56`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 99`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/storage/10-file.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 817.2 | **LOC:** 457 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.2145%), Tech Debt (11.2256%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 180.4)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `FileNode` (Impact: 102.7)
  * `processMsg2` (Impact: 96.2)
  * `FileInNode` (Impact: 75.0)
  * `processMsg2` (Impact: 73.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 73 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 56`, `args: 29`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 87`, `unreferenced_by_name: 1`
* *Architecture:* `io: 15`, `api: 1`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 49`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs-extra, iconv-lite, os, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/89-trigger.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 786.88 | **LOC:** 306 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.9323%), Tech Debt (14.0514%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 184.2)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `TriggerNode` (Impact: 183.9)
  * `processMessage` (Impact: 108.4)
  * `processMessageQueue` (Impact: 7.0)
  * `stat` (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 63 instances
* *Concurrency (weighted view):* 100
* *State Mutation (weighted view):* 192
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 50`, `args: 25`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 66`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 20`, `import: 1`
* *Defense:* `safety: 56`, `doc: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mustache
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/10-switch.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 784.08 | **LOC:** 527 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.1663%), Tech Debt (14.5216%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 244.7)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `SwitchNode` (Impact: 107.1)
  * `getV1` (Impact: 40.8)
  * `processMessage` (Impact: 29.4)
  * `getV2` (Impact: 28.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 119`, `args: 56`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 68`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 2`
* *Defense:* `safety: 76`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/89-delay.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 773.1 | **LOC:** 425 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.7372%), Tech Debt (11.512%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 214.1)
    * *Intent:* * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except...
  * `DelayNode` (Impact: 208.8)
  * `maxKeptMsgsCount` (Impact: 6.3)
  * `clearDelayList` (Impact: 6.0)
  * `sendMsgFromBuffer` (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 85 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 44`, `args: 31`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 100`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 8`
* *Defense:* `safety: 41`, `doc: 1`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/10-function.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 666.44 | **LOC:** 545 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.6601%), Tech Debt (17.7329%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 146.6)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `FunctionNode` (Impact: 108.4)
  * `sendResults` (Impact: 50.8)
  * `processMessage` (Impact: 39.5)
  * `updateErrorInfo` (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 54 instances
* *Concurrency (weighted view):* 64
* *State Mutation (weighted view):* 182
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 84`, `args: 57`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 74`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `concurrency: 19`, `import: 5`
* *Defense:* `safety: 42`, `doc: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` acorn, acorn-walk, util, vm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/21-debug.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 629.3 | **LOC:** 695 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.3353%), Tech Debt (8.152%)
**Top Internal Functions/Classes:**
  * `onpaletteadd` (Impact: 108.5)
  * `handleDebugMessage` (Impact: 48.8)
  * `requestDebugNodeList` (Impact: 39.6)
  * `oneditprepare` (Impact: 34.0)
  * `getNodeLabel` (Impact: 33.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 97`, `args: 58`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 86`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 5`
* *Defense:* `safety: 66`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` debug-utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/10-switch.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 602.9 | **LOC:** 480 | **CtrlFlow:** 45.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.3196%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addItem` (Impact: 179.1)
  * `oneditprepare` (Impact: 107.3)
  * `exportRule` (Impact: 32.5)
  * `outputLabels` (Impact: 24.9)
  * `validate` (Impact: 20.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 98`, `args: 26`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 57`
* *Architecture:* `api: 1`
* *Defense:* `safety: 58`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/22-websocket.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 555.4 | **LOC:** 457 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.0071%), Tech Debt (19.3321%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 135.1)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `WebSocketListenerNode` (Impact: 72.1)
    * *Intent:* // A node red node that sets up a local websocket server
  * `WebSocketOutNode` (Impact: 29.0)
  * `handleConnection` (Impact: 18.6)
  * `handleEvent` (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 61 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 195
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 41`, `args: 36`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 73`, `dead_code: 3`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 23`, `doc: 1`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` proxyHelper, https-proxy-agent, url, util, ws
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/20-inject.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 533.46 | **LOC:** 733 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.0217%), Tech Debt (9.3466%)
**Top Internal Functions/Classes:**
  * `oneditprepare` (Impact: 65.7)
  * `label` (Impact: 55.1)
  * `oneditsave` (Impact: 43.1)
  * `doInject` (Impact: 18.7)
    * *Intent:* /** Perform inject, optionally sending a custom msg (refactored for re-use in the form inject button...
  * `outputLabels` (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 119`, `args: 27`, `func_start: 16`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 94`, `fragile_debt: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 51`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/21-httpin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 519.0 | **LOC:** 450 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.3032%), Tech Debt (24.1251%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 165.9)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `HTTPOut` (Impact: 53.2)
  * `HTTPIn` (Impact: 50.0)
  * `rawBodyParser` (Impact: 46.1)
  * `createRequestWrapper` (Impact: 11.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 72`, `args: 28`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 47`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 32`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` body-parser, content-type, cookie-parser, cors, express, hash-sum, is-utf8, media-typer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/21-debug.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 455.06 | **LOC:** 330 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.8151%), Tech Debt (12.7589%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 159.3)
  * `DebugNode` (Impact: 117.6)
  * `prepareStatus` (Impact: 18.8)
  * `prepareValue` (Impact: 13.1)
  * `setNodeState` (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 45`, `args: 24`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 45`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 63`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` events, fs-extra, path, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/sequence/19-batch.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 396.72 | **LOC:** 318 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.2924%), Tech Debt (13.146%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 99.9)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `BatchNode` (Impact: 52.0)
  * `concat_msg` (Impact: 24.1)
  * `add_to_topic_group` (Impact: 12.1)
  * `try_concat` (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 45 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 146
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 82`, `args: 36`, `func_start: 12`
* *Risk/State:* `state_mutation: 56`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 2`
* *Defense:* `safety: 13`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/10-mqtt.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 390.94 | **LOC:** 1010 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.0741%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `oneditprepare` (Impact: 58.5)
  * `setUpSection` (Impact: 41.9)
  * `oneditsave` (Impact: 20.1)
  * `oneditprepare` (Impact: 17.5)
  * `saveV5Message` (Impact: 15.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 168`, `args: 46`, `func_start: 29`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 38`
* *Architecture:* `api: 3`, `concurrency: 4`
* *Defense:* `safety: 47`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/32-udp.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 384.12 | **LOC:** 285 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.2939%), Tech Debt (14.5063%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 129.4)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `UDPout` (Impact: 80.4)
    * *Intent:* // The Output Node
  * `UDPin` (Impact: 49.5)
    * *Intent:* // The Input Node
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 17`, `args: 15`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 39`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 25`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dgram, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/10-function.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 376.14 | **LOC:** 706 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.1904%), Tech Debt (8.1547%)
**Top Internal Functions/Classes:**
  * `addItem` (Impact: 50.5)
  * `prepareLibraryConfig` (Impact: 40.9)
  * `oneditprepare` (Impact: 36.7)
  * `buildEditor` (Impact: 15.6)
  * `onchange` (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 140`, `args: 47`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 45`, `planned_debt: 1`
* *Architecture:* `api: 1`, `concurrency: 6`
* *Defense:* `safety: 26`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/90-exec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 368.04 | **LOC:** 220 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.9539%), Tech Debt (17.6759%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 109.1)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `ExecNode` (Impact: 108.6)
  * `cleanup` (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 21`, `args: 14`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 46`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 1`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 30`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` child_process, fs, is-utf8
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/15-change.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 339.44 | **LOC:** 367 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.6191%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addItem` (Impact: 67.1)
  * `oneditprepare` (Impact: 58.9)
  * `validate` (Impact: 29.1)
  * `label` (Impact: 23.7)
  * `createPropertyValue` (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 92`, `args: 17`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 42`
* *Architecture:* `api: 1`
* *Defense:* `safety: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/sequence/18-sort.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 321.8 | **LOC:** 267 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.1525%), Tech Debt (15.3873%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 76.1)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `SortNode` (Impact: 70.3)
    * *Intent:* // function get_context_val(node, name, dval) { // var context = node.context(); // var val = contex...
  * `processMessage` (Impact: 20.9)
  * `sortMessageGroup` (Impact: 10.7)
  * `sortMessageProperty` (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 85`, `args: 31`, `func_start: 9`
* *Risk/State:* `state_mutation: 25`, `dead_code: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 14`
* *Defense:* `safety: 18`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/20-inject.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 275.06 | **LOC:** 198 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.6994%), Tech Debt (29.6693%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 75.5)
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
  * `InjectNode` (Impact: 60.9)
  * `evaluateProperty` (Impact: 22.2)
  * `repeaterSetup` (Impact: 6.6)
  * `close` (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 29 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 14`, `args: 14`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 30`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 18`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.719
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cronosjs
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

- `package/index.js` -> **Severity: 0.111** (Embedded: 0.0017 * Error Risk: 64.1725%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/core/common/05-junction.js` -> **Severity: 171.9** (Blast Radius: 1.719 * Doc Risk: 100.0%)
- `package/core/common/21-debug.js` -> **Severity: 171.9** (Blast Radius: 1.719 * Doc Risk: 100.0%)
- `package/core/common/91-global-config.js` -> **Severity: 171.9** (Blast Radius: 1.719 * Doc Risk: 100.0%)
- `package/core/function/rbe.js` -> **Severity: 171.9** (Blast Radius: 1.719 * Doc Risk: 100.0%)
- `package/core/parsers/70-XML.js` -> **Severity: 171.9** (Blast Radius: 1.719 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
