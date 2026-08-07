# ARCHITECTURAL_BRIEF: @node-red_nodes
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@node-red_nodes` |
| **Timestamp** | `2026-08-07T05:12:21.524990+00:00` |
| **Scan Duration** | `1.22s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 38 malicious artifacts.

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
| Total Artifacts | 596 |
| Analyzed Artifacts (Scanned) | 577 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 19 |
| Total LOC | 34823 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.8% |
| Dominant Lang | JAVASCRIPT |

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
| HTML | 383 | 20260 | 66.4% |
| JSON | 108 | 8307 | 18.7% |
| XML | 46 | 4 | 8.0% |
| JAVASCRIPT | 38 | 6252 | 6.6% |
| MARKDOWN | 1 | 0 | 0.2% |
| PLAINTEXT | 1 | 0 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.423`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 491 | 85.1% |
| file_cluster_17 | 8 | 1.4% |
| file_cluster_13 | 7 | 1.2% |
| file_cluster_4 | 5 | 0.9% |
| file_cluster_11 | 3 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 61 | 10.6% |
| Static: Literature & Documentation | 2 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 19*

**Composition by Extension & Reason:**
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Static Asset Blob without Intent: 1163 LOC), 1x Excluded (Static Asset Blob without Intent: 1039 LOC)
- `.html`: 1x Excluded (Machine-Generated Source Code Signature: 51 LOC), 1x Excluded (Saturation: Line 62 exceeds 500 chars), 1x Excluded (Saturation: Line 71 exceeds 500 chars)
- `.demo`: 2x Excluded (Unsupported Extension: '.demo')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 13.0 | 5.9 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.2 | 13.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 12.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.3 | 2.3 | 2.3 |
| API Exposure | 0.0 | 5.8 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 35.8 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 75.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 50.0 | 44.7 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 87.5 | 26.1 | 28.1 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/core/network/21-httprequest.js` (Hits: 37)
- `package/core/network/22-websocket.html` (Hits: 22)
- `package/core/network/21-httpin.html` (Hits: 18)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`package/README.md`) — 0 inbound connections
2. **05-junction.html** (`package/core/common/05-junction.html`) — 0 inbound connections
3. **20-inject.html** (`package/core/common/20-inject.html`) — 0 inbound connections
4. **21-debug.html** (`package/core/common/21-debug.html`) — 0 inbound connections
5. **24-complete.html** (`package/core/common/24-complete.html`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **21-httprequest.js** (`package/core/network/21-httprequest.js`) — 14 outbound dependencies
2. **21-httpin.js** (`package/core/network/21-httpin.js`) — 11 outbound dependencies
3. **10-mqtt.js** (`package/core/network/10-mqtt.js`) — 5 outbound dependencies
4. **22-websocket.js** (`package/core/network/22-websocket.js`) — 5 outbound dependencies
5. **21-debug.js** (`package/core/common/21-debug.js`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `exports` (@ `package/core/network/10-mqtt.js`) -> Impact: **407.6** | LOC: 713
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `exports` (@ `package/core/sequence/17-split.js`) -> Impact: **387.8** | LOC: 799
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `ChangeNode` (@ `package/core/function/15-change.js`) -> Impact: **290.7** | LOC: 341
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation * * Licensed under the Apache License, Version 2.0 (the "License"); * you m...
- `exports` (@ `package/core/network/21-httprequest.js`) -> Impact: **267.9** | LOC: 405
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `JoinNode` (@ `package/core/sequence/17-split.js`) -> Impact: **261.4** | LOC: 379
- `HTTPRequest` (@ `package/core/network/21-httprequest.js`) -> Impact: **260.2** | LOC: 354
- `DelayNode` (@ `package/core/function/89-delay.js`) -> Impact: **253.1** | LOC: 385
- `createLWT` (@ `package/core/network/10-mqtt.js`) -> Impact: **243.3** | LOC: 210
  * *Intent:* /** * Perform the connect action * @param {MQTTInNode|MQTTOutNode} node * @param {Object} msg * @param {Function} done */
- `exports` (@ `package/core/function/15-change.js`) -> Impact: **240.7** | LOC: 346
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `TriggerNode` (@ `package/core/function/89-trigger.js`) -> Impact: **227.2** | LOC: 284
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation * * Licensed under the Apache License, Version 2.0 (the "License"); * you m...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/core/function` | 18 | 7465.52 | 80.08% | 78.27% |
| `package/core/network` | 16 | 5545.44 | 55.5% | 94.32% |
| `package/core/common` | 20 | 4114.86 | 50.34% | 90.86% |
| `package/core/sequence` | 6 | 3041.2 | 74.15% | 94.83% |
| `package/core/parsers` | 10 | 1484.22 | 66.4% | 85.45% |
| `package/core/storage` | 4 | 706.62 | 64.86% | 85.96% |
| `package/icons` | 46 | 455.36 | 4.67% | 0.0% |
| `package/examples/parser/csv` | 10 | 173.38 | 0.0% | 0.0% |
| `package/examples/network/http` | 7 | 126.68 | 0.0% | 0.0% |
| `package/examples/storage/read file` | 4 | 71.2 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/locales/es-ES/common/24-complete.html` -> **100.0%** Exposure
- `package/locales/ko/common/21-debug.html` -> **100.0%** Exposure
- `package/core/common/21-debug.js` -> **100.0%** Exposure
- `package/core/common/90-comment.js` -> **100.0%** Exposure
- `package/core/common/91-global-config.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/core/common/20-inject.html` -> **100.0%** Exposure
- `package/core/common/21-debug.html` -> **100.0%** Exposure
- `package/core/common/24-complete.html` -> **100.0%** Exposure
- `package/core/common/25-catch.html` -> **100.0%** Exposure
- `package/core/common/25-status.html` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/core/sequence/17-split.js` -> **2** Orphaned Functions | **41** Duplicates
- `package/core/network/10-mqtt.js` -> **12** Orphaned Functions | **29** Duplicates
- `package/core/network/10-mqtt.html` -> **1** Orphaned Functions | **29** Duplicates
- `package/core/function/10-switch.js` -> **6** Orphaned Functions | **24** Duplicates
- `package/core/function/15-change.js` -> **1** Orphaned Functions | **29** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/core/network/21-httprequest.js`** -> AI Confidence: **99.39%**
2. **`package/core/network/10-mqtt.js`** -> AI Confidence: **99.34%**
3. **`package/core/storage/23-watch.js`** -> AI Confidence: **99.32%**
4. **`package/core/network/21-httpin.js`** -> AI Confidence: **99.31%**
5. **`package/core/common/20-inject.js`** -> AI Confidence: **99.29%**
6. **`package/core/function/rbe.js`** -> AI Confidence: **99.29%**
7. **`package/core/network/32-udp.js`** -> AI Confidence: **99.29%**
8. **`package/core/parsers/70-CSV.js`** -> AI Confidence: **99.29%**
9. **`package/core/parsers/70-JSON.js`** -> AI Confidence: **99.29%**
10. **`package/core/parsers/70-YAML.js`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `67` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/core/sequence/18-sort.js` (JAVASCRIPT) -> Cumulative Risk: **774.85**
- **Archetype:** `file_cluster_4` (Distance: 15.27 IQR)
- **Magnitude:** 515.1 | **LOC:** 267 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9928%)
- **Heaviest Functions:** `SortNode` (Impact: 97.6), `exports` (Impact: 87.5), `processMessage` (Impact: 28.5)

### 2. `package/core/function/89-delay.js` (JAVASCRIPT) -> Cumulative Risk: **739.83**
- **Archetype:** `file_cluster_4` (Distance: 14.38 IQR)
- **Magnitude:** 857.0 | **LOC:** 425 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9984%), Cognitive Load (96.5569%)
- **Heaviest Functions:** `DelayNode` (Impact: 253.1), `exports` (Impact: 215.5), `done` (Impact: 13.2)

### 3. `package/core/parsers/70-XML.js` (JAVASCRIPT) -> Cumulative Risk: **734.95**
- **Archetype:** `file_cluster_4` (Distance: 13.498 IQR)
- **Magnitude:** 127.42 | **LOC:** 49 | **CtrlFlow:** 73.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9991%), Concurrency (99.7641%)
- **Heaviest Functions:** `XMLNode` (Impact: 33.2), `exports` (Impact: 27.8), `done` (Impact: 22.9)

### 4. `package/core/function/80-template.js` (JAVASCRIPT) -> Cumulative Risk: **727.75**
- **Archetype:** `file_cluster_4` (Distance: 13.734 IQR)
- **Magnitude:** 412.4 | **LOC:** 225 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9987%), Concurrency (99.9714%)
- **Heaviest Functions:** `exports` (Impact: 69.5), `TemplateNode` (Impact: 50.3), `done` (Impact: 31.6)

### 5. `package/core/common/20-inject.js` (JAVASCRIPT) -> Cumulative Risk: **724.95**
- **Archetype:** `file_cluster_17` (Distance: 14.128 IQR)
- **Magnitude:** 442.66 | **LOC:** 198 | **CtrlFlow:** 79.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9975%), Concurrency (95.8277%)
- **Heaviest Functions:** `exports` (Impact: 86.8), `InjectNode` (Impact: 83.4), `doneEvaluating` (Impact: 34.1)

### 6. `package/core/function/89-trigger.js` (JAVASCRIPT) -> Cumulative Risk: **693.15**
- **Archetype:** `file_cluster_4` (Distance: 15.613 IQR)
- **Magnitude:** 1004.08 | **LOC:** 306 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9641%)
- **Heaviest Functions:** `TriggerNode` (Impact: 227.2), `exports` (Impact: 188.4), `processMessage` (Impact: 111.2)

### 7. `package/core/sequence/19-batch.js` (JAVASCRIPT) -> Cumulative Risk: **674.29**
- **Archetype:** `file_cluster_17` (Distance: 12.836 IQR)
- **Magnitude:** 458.62 | **LOC:** 318 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9519%), Cognitive Load (90.8555%)
- **Heaviest Functions:** `exports` (Impact: 99.9), `BatchNode` (Impact: 62.2), `concat_msg` (Impact: 24.1)

### 8. `package/core/network/32-udp.js` (JAVASCRIPT) -> Cumulative Risk: **656.95**
- **Archetype:** `file_cluster_8` (Distance: 12.741 IQR)
- **Magnitude:** 456.52 | **LOC:** 285 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9991%), Tech Debt (90.6513%), Cognitive Load (84.4155%)
- **Heaviest Functions:** `exports` (Impact: 149.2), `UDPout` (Impact: 107.4), `UDPin` (Impact: 73.2)

### 9. `package/core/sequence/17-split.js` (JAVASCRIPT) -> Cumulative Risk: **642.18**
- **Archetype:** `file_cluster_17` (Distance: 13.783 IQR)
- **Magnitude:** 1719.16 | **LOC:** 816 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9989%), Cognitive Load (94.9366%)
- **Heaviest Functions:** `exports` (Impact: 387.8), `JoinNode` (Impact: 261.4), `processReduceMessageQueue` (Impact: 179.2)

### 10. `package/core/network/21-httprequest.js` (JAVASCRIPT) -> Cumulative Risk: **612.97**
- **Archetype:** `file_cluster_13` (Distance: 12.931 IQR)
- **Magnitude:** 797.82 | **LOC:** 855 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9977%), State Flux (99.9351%), Verification (80.0%)
- **Heaviest Functions:** `exports` (Impact: 267.9), `HTTPRequest` (Impact: 260.2), `updateKey` (Impact: 95.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/core/sequence/17-split.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.783 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.24 IQR)
- **Top Global Matches:** file_cluster_17: 13.783, file_cluster_8: 13.846, file_cluster_11: 14.037
- **Magnitude:** 1719.16 | **LOC:** 816 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.9366%), Tech Debt (99.9989%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 387.8)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `JoinNode` (Impact: 261.4)
  * `processReduceMessageQueue` (Impact: 179.2)
    * *Intent:* // There are no more messages to process, clear the active flag
  * `SplitNode` (Impact: 138.4)
  * `done` (Impact: 46.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 123`, `args: 38`, `func_start: 58`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 388`, `dead_code: 1`, `duplicate_logic: 41`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `concurrency: 2`
* *Defense:* `safety: 102`, `doc: 1`, `immutability_locks: 2`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/10-mqtt.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.1 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.75 IQR)
- **Top Global Matches:** file_cluster_8: 13.1, file_cluster_13: 13.222, file_cluster_11: 13.32
- **Magnitude:** 1657.96 | **LOC:** 1512 | **CtrlFlow:** 81.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.213%), Tech Debt (99.9988%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 407.6)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `createLWT` (Impact: 243.3)
    * *Intent:* /** * Perform the connect action * @param {MQTTInNode|MQTTOutNode} node * @param {Object} msg * @par...
  * `MQTTBrokerNode` (Impact: 213.9)
  * `setOptions` (Impact: 178.5)
  * `subscriptionHandler` (Impact: 124.5)
    * *Intent:* /** * Helper function for copying the MQTT v5 srcUserProperties object (parameter1) to the propertie...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 60`, `args: 42`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 76`, `dead_code: 1`, `duplicate_logic: 29`, `orphaned_logic: 12`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 6`, `import: 5`
* *Defense:* `safety: 88`, `doc: 68`, `immutability_locks: 18`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mqtt, proxyHelper, url, is-utf8, https-proxy-agent
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/15-change.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.987 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.593 IQR)
- **Top Global Matches:** file_cluster_8: 13.987, file_cluster_11: 14.165, file_cluster_17: 14.21
- **Magnitude:** 1175.84 | **LOC:** 363 | **CtrlFlow:** 74.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.0199%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `ChangeNode` (Impact: 290.7)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation * * Licensed under the Ap...
  * `exports` (Impact: 240.7)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `applyRule` (Impact: 127.8)
  * `getToValue` (Impact: 123.1)
  * `getFromValue` (Impact: 116.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 53`, `args: 24`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 103`, `duplicate_logic: 29`, `orphaned_logic: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 99`, `doc: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/89-trigger.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.613 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.281 IQR)
- **Top Global Matches:** file_cluster_4: 15.613, file_cluster_11: 15.977, file_cluster_17: 16.075
- **Magnitude:** 1004.08 | **LOC:** 306 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.6024%), Tech Debt (99.9641%)
**Top Internal Functions/Classes:**
  * `TriggerNode` (Impact: 227.2)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation * * Licensed under the Ap...
  * `exports` (Impact: 188.4)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `processMessage` (Impact: 111.2)
  * `resolve` (Impact: 57.9)
  * `resolve` (Impact: 44.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 50`, `args: 25`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 260`, `dead_code: 3`, `duplicate_logic: 10`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 60`, `import: 1`
* *Defense:* `safety: 56`, `doc: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mustache
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/21-debug.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.346 IQR)
- **Top Global Matches:** file_cluster_8: 13.346, file_cluster_17: 13.49, file_cluster_11: 13.595
- **Magnitude:** 857.38 | **LOC:** 695 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.7995%), Tech Debt (97.4812%)
**Top Internal Functions/Classes:**
  * `onpaletteadd` (Impact: 161.5)
  * `handleDebugMessage` (Impact: 52.2)
  * `oneditprepare` (Impact: 46.0)
  * `requestDebugNodeList` (Impact: 42.4)
  * `activateAjaxCall` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 96`, `args: 57`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 325`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 9`
* *Architecture:* `io: 8`, `concurrency: 5`
* *Defense:* `safety: 66`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` debug-utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/89-delay.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.38 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.584 IQR)
- **Top Global Matches:** file_cluster_4: 14.38, file_cluster_11: 14.491, file_cluster_17: 14.54
- **Magnitude:** 857.0 | **LOC:** 425 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.5569%), Tech Debt (99.9984%)
**Top Internal Functions/Classes:**
  * `DelayNode` (Impact: 253.1)
  * `exports` (Impact: 215.5)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation *
  * `done` (Impact: 13.2)
  * `done` (Impact: 8.3)
  * `maxKeptMsgsCount` (Impact: 7.5)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation * * Licensed under the Ap...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 43`, `args: 31`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 241`, `dead_code: 3`, `duplicate_logic: 20`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 23`
* *Defense:* `safety: 41`, `doc: 1`, `immutability_locks: 7`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/21-httprequest.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.931 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.947 IQR)
- **Top Global Matches:** file_cluster_13: 12.931, file_cluster_17: 13.073, file_cluster_11: 13.114
- **Magnitude:** 797.82 | **LOC:** 855 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.3216%), Tech Debt (99.9977%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 267.9)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `HTTPRequest` (Impact: 260.2)
  * `updateKey` (Impact: 95.9)
  * `nodeDone` (Impact: 11.7)
  * `checkNodeAgentPatch` (Impact: 9.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 55`, `args: 13`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 98`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 10`, `orphaned_logic: 3`
* *Architecture:* `io: 37`, `api: 1`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 39`, `doc: 7`, `immutability_locks: 32`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` uuid, tough-cookie, hpagent, mustache, proxyHelper, url, https, got...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/10-switch.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.034 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.637 IQR)
- **Top Global Matches:** file_cluster_8: 14.034, file_cluster_11: 14.135, file_cluster_17: 14.263
- **Magnitude:** 731.34 | **LOC:** 527 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.2191%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 205.8)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `SwitchNode` (Impact: 75.2)
  * `getV1` (Impact: 40.8)
  * `applyRule` (Impact: 29.1)
  * `getV1` (Impact: 28.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 79`, `args: 44`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 126`, `planned_debt: 1`, `duplicate_logic: 24`, `orphaned_logic: 6`
* *Architecture:* `api: 1`, `concurrency: 1`
* *Defense:* `safety: 72`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/21-debug.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.152 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.679 IQR)
- **Top Global Matches:** file_cluster_11: 14.152, file_cluster_13: 14.23, file_cluster_8: 14.284
- **Magnitude:** 714.84 | **LOC:** 330 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `DebugNode` (Impact: 155.6)
  * `exports` (Impact: 139.7)
  * `clearTimeout` (Impact: 88.7)
  * `done` (Impact: 44.2)
  * `prepareStatus` (Impact: 32.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 32`, `args: 15`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 149`, `duplicate_logic: 16`, `orphaned_logic: 1`
* *Architecture:* `io: 11`, `api: 1`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 43`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` events, util, fs-extra, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/10-switch.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.057 IQR)
- **Top Global Matches:** file_cluster_17: 13.057, file_cluster_8: 13.251, file_cluster_11: 13.443
- **Magnitude:** 696.6 | **LOC:** 480 | **CtrlFlow:** 67.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.7583%), Tech Debt (35.3555%)
**Top Internal Functions/Classes:**
  * `addItem` (Impact: 191.1)
  * `oneditprepare` (Impact: 155.6)
  * `exportRule` (Impact: 39.5)
  * `outputLabels` (Impact: 26.4)
  * `validate` (Impact: 20.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 97`, `args: 25`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 178`, `dead_code: 1`, `orphaned_logic: 7`
* *Architecture:* None
* *Defense:* `safety: 58`, `test: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/10-mqtt.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.069 IQR)
- **Top Global Matches:** file_cluster_8: 12.069, file_cluster_17: 12.555, file_cluster_7: 12.58
- **Magnitude:** 692.36 | **LOC:** 1010 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.4202%), Tech Debt (99.5244%)
**Top Internal Functions/Classes:**
  * `oneditprepare` (Impact: 96.1)
  * `setUpSection` (Impact: 41.9)
  * `oneditsave` (Impact: 27.2)
  * `oneditprepare` (Impact: 23.7)
  * `saveV5Message` (Impact: 18.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 168`, `args: 48`, `func_start: 51`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 312`, `duplicate_logic: 29`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 4`
* *Defense:* `safety: 47`, `doc: 3`, `sync_locks: 1`, `immutability_locks: 7`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/20-inject.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.894 IQR)
- **Top Global Matches:** file_cluster_17: 12.894, file_cluster_8: 12.959, file_cluster_11: 13.113
- **Magnitude:** 616.62 | **LOC:** 733 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.2408%), Tech Debt (67.8939%)
**Top Internal Functions/Classes:**
  * `oneditprepare` (Impact: 88.1)
  * `oneditsave` (Impact: 58.8)
  * `label` (Impact: 57.9)
  * `outputLabels` (Impact: 27.5)
  * `doInject` (Impact: 18.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 117`, `args: 26`, `func_start: 17`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 295`, `dead_code: 4`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 7`
* *Architecture:* None
* *Defense:* `safety: 51`, `doc: 2`, `immutability_locks: 7`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/10-function.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.063 IQR)
- **Top Global Matches:** file_cluster_8: 12.063, file_cluster_17: 12.304, file_cluster_4: 12.438
- **Magnitude:** 565.46 | **LOC:** 706 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.1579%), Tech Debt (99.9718%)
**Top Internal Functions/Classes:**
  * `oneditprepare` (Impact: 51.7)
  * `addItem` (Impact: 50.5)
  * `prepareLibraryConfig` (Impact: 48.9)
  * `buildEditor` (Impact: 15.6)
  * `onchange` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 139`, `args: 46`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 235`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 14`, `orphaned_logic: 9`
* *Architecture:* `concurrency: 16`
* *Defense:* `safety: 26`, `immutability_locks: 11`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/parsers/70-CSV.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.321 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.221 IQR)
- **Top Global Matches:** file_cluster_17: 16.321, file_cluster_11: 16.514, file_cluster_0: 16.604
- **Magnitude:** 564.14 | **LOC:** 691 | **CtrlFlow:** 82.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.9231%), Tech Debt (21.0693%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 216.7)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `CSVNode` (Impact: 104.8)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation * * Licensed under the Ap...
  * `clean` (Impact: 66.3)
  * `done` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 30`, `args: 7`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 169`, `dead_code: 5`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 70`, `doc: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` csv, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/sequence/18-sort.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.27 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.139 IQR)
- **Top Global Matches:** file_cluster_4: 15.27, file_cluster_17: 15.583, file_cluster_11: 15.837
- **Magnitude:** 515.1 | **LOC:** 267 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.1051%), Tech Debt (99.9928%)
**Top Internal Functions/Classes:**
  * `SortNode` (Impact: 97.6)
  * `exports` (Impact: 87.5)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `processMessage` (Impact: 28.5)
  * `sortMessageGroup` (Impact: 16.1)
  * `sortMessageProperty` (Impact: 16.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 85`, `args: 31`, `func_start: 16`
* *Risk/State:* `state_mutation: 147`, `dead_code: 6`, `duplicate_logic: 10`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 74`
* *Defense:* `safety: 18`, `doc: 1`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/15-change.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.309 IQR)
- **Top Global Matches:** file_cluster_17: 13.309, file_cluster_8: 13.424, file_cluster_11: 13.725
- **Magnitude:** 507.26 | **LOC:** 367 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6059%), Tech Debt (33.6743%)
**Top Internal Functions/Classes:**
  * `oneditprepare` (Impact: 78.8)
  * `addItem` (Impact: 67.1)
  * `label` (Impact: 32.8)
  * `validate` (Impact: 29.1)
  * `createPropertyValue` (Impact: 12.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 92`, `args: 16`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 244`, `orphaned_logic: 5`
* *Architecture:* None
* *Defense:* `safety: 32`, `immutability_locks: 3`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/sequence/19-batch.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.836 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.723 IQR)
- **Top Global Matches:** file_cluster_17: 12.836, file_cluster_8: 13.013, file_cluster_4: 13.201
- **Magnitude:** 458.62 | **LOC:** 318 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.8555%), Tech Debt (99.9519%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 99.9)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `BatchNode` (Impact: 62.2)
    * *Intent:* // the message that caused the overflow
  * `concat_msg` (Impact: 24.1)
  * `add_to_topic_group` (Impact: 12.1)
  * `clearInterval` (Impact: 10.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 82`, `args: 36`, `func_start: 26`
* *Risk/State:* `state_mutation: 170`, `duplicate_logic: 11`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 7`
* *Defense:* `safety: 13`, `doc: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/32-udp.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.741 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.226 IQR)
- **Top Global Matches:** file_cluster_8: 12.741, file_cluster_11: 12.93, file_cluster_13: 12.938
- **Magnitude:** 456.52 | **LOC:** 285 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.4155%), Tech Debt (90.6513%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 149.2)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `UDPout` (Impact: 107.4)
  * `UDPin` (Impact: 73.2)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation * * Licensed under the Ap...
  * `nodeDone` (Impact: 13.0)
  * `nodeDone` (Impact: 9.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 17`, `args: 15`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 84`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 6`, `import: 2`
* *Defense:* `safety: 25`, `doc: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, dgram
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/20-inject.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.128 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.065 IQR)
- **Top Global Matches:** file_cluster_17: 14.128, file_cluster_4: 14.132, file_cluster_8: 14.264
- **Magnitude:** 442.66 | **LOC:** 198 | **CtrlFlow:** 79.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.682%), Tech Debt (99.9975%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 86.8)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `InjectNode` (Impact: 83.4)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation * * Licensed under the Ap...
  * `doneEvaluating` (Impact: 34.1)
  * `evaluateProperty` (Impact: 33.6)
  * `evaluateProperty` (Impact: 15.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 14`, `args: 14`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 132`, `duplicate_logic: 7`, `orphaned_logic: 4`
* *Architecture:* `api: 1`, `concurrency: 12`, `import: 1`
* *Defense:* `safety: 18`, `doc: 1`, `immutability_locks: 6`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cronosjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/80-template.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.734 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.951 IQR)
- **Top Global Matches:** file_cluster_4: 13.734, file_cluster_17: 14.08, file_cluster_8: 14.092
- **Magnitude:** 412.4 | **LOC:** 225 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.5287%), Tech Debt (99.9987%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 69.5)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `TemplateNode` (Impact: 50.3)
  * `done` (Impact: 31.6)
    * *Intent:* /* istanbul ignore else */
  * `output` (Impact: 21.5)
  * `lookup` (Impact: 17.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 44`, `args: 18`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 133`, `duplicate_logic: 9`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 25`, `import: 2`
* *Defense:* `safety: 18`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mustache, js-yaml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/storage/10-file.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.351 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.695 IQR)
- **Top Global Matches:** file_cluster_13: 13.351, file_cluster_11: 13.483, file_cluster_8: 13.526
- **Magnitude:** 399.32 | **LOC:** 457 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.4314%), Tech Debt (99.9972%)
**Top Internal Functions/Classes:**
  * `FileNode` (Impact: 89.3)
  * `processMsg2` (Impact: 84.6)
  * `exports` (Impact: 77.9)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `done` (Impact: 38.2)
  * `processMsg` (Impact: 23.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 22`, `args: 12`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 51`, `duplicate_logic: 5`, `orphaned_logic: 4`
* *Architecture:* `io: 11`, `api: 1`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 23`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, iconv-lite, fs-extra, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/60-link.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.659 IQR)
- **Top Global Matches:** file_cluster_8: 12.659, file_cluster_17: 12.924, file_cluster_11: 13.084
- **Magnitude:** 385.74 | **LOC:** 406 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.1108%), Tech Debt (99.996%)
**Top Internal Functions/Classes:**
  * `onEditPrepare` (Impact: 43.2)
  * `onEditSave` (Impact: 40.0)
  * `label` (Impact: 10.5)
  * `onAdd` (Impact: 9.3)
  * `validate` (Impact: 9.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 67`, `args: 36`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 194`, `duplicate_logic: 18`, `orphaned_logic: 2`
* *Architecture:* `concurrency: 1`
* *Defense:* `safety: 23`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/60-link.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.277 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.339 IQR)
- **Top Global Matches:** file_cluster_8: 13.277, file_cluster_13: 13.417, file_cluster_7: 13.466
- **Magnitude:** 334.64 | **LOC:** 287 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.5515%), Tech Debt (96.7586%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 85.5)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation * * Licensed under the Ap...
  * `LinkCallNode` (Impact: 51.8)
  * `getTargetNode` (Impact: 24.2)
  * `LinkOutNode` (Impact: 20.5)
  * `returnLinkMessage` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 33`, `args: 25`, `func_start: 24`
* *Risk/State:* `state_mutation: 74`, `duplicate_logic: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 20`, `doc: 26`, `immutability_locks: 22`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crypto
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/parsers/70-JSON.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.405 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.848 IQR)
- **Top Global Matches:** file_cluster_11: 14.405, file_cluster_13: 14.411, file_cluster_17: 14.525
- **Magnitude:** 322.94 | **LOC:** 139 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.4331%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `JSONNode` (Impact: 83.6)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation * * Licensed under the Ap...
  * `exports` (Impact: 69.7)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
  * `done` (Impact: 41.5)
  * `done` (Impact: 22.2)
  * `done` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 8`, `args: 3`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 78`, `dead_code: 1`, `duplicate_logic: 13`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 19`, `doc: 1`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` json-schema-draft-06.json, ajv
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/rbe.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.226 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.418 IQR)
- **Top Global Matches:** file_cluster_8: 15.226, file_cluster_17: 15.358, file_cluster_11: 15.36
- **Magnitude:** 309.96 | **LOC:** 102 | **CtrlFlow:** 89.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.9105%), Tech Debt (27.5003%)
**Top Internal Functions/Classes:**
  * `RbeNode` (Impact: 113.9)
  * `exports` (Impact: 94.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 7`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 99`, `orphaned_logic: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 38`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `package/core/parsers/70-JSON.js` (JAVASCRIPT) | Magnitude: 322.94 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, state_mutation: 78, branch: 44, func_start: 23
- `package/core/common/21-debug.js` (JAVASCRIPT) | Magnitude: 714.84 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 230, state_mutation: 149, branch: 89, safety: 43
- `package/core/parsers/70-HTML.js` (JAVASCRIPT) | Magnitude: 183.72 | Delta: **0.176 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 83, indent_spaces: 79, branch: 24, safety: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/core/storage/10-file.js` (JAVASCRIPT) | Magnitude: 399.32 | Delta: **0.132 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 129, state_mutation: 51, branch: 49, safety: 23
- `package/core/network/21-httprequest.js` (JAVASCRIPT) | Magnitude: 797.82 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 330, branch: 142, state_mutation: 98, structural_boundaries: 55
- `package/core/network/21-httpin.js` (JAVASCRIPT) | Magnitude: 295.4 | Delta: **0.164 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 223, state_mutation: 101, branch: 44, structural_boundaries: 43
- `package/core/function/90-exec.js` (JAVASCRIPT) | Magnitude: 167.98 | Delta: **0.219 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 67, state_mutation: 64, branch: 25, safety: 13
- `package/core/function/10-function.js` (JAVASCRIPT) | Magnitude: 121.96 | Delta: **0.226 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, state_mutation: 26, branch: 21, safety: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `package/core/common/25-catch.html` (HTML) | Magnitude: 217.1 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 186, state_mutation: 124, branch: 53, structural_boundaries: 42
- `package/core/common/20-inject.js` (JAVASCRIPT) | Magnitude: 442.66 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 166, state_mutation: 132, branch: 54, func_start: 18
- `package/core/sequence/17-split.js` (JAVASCRIPT) | Magnitude: 1719.16 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 751, state_mutation: 388, branch: 245, structural_boundaries: 123
- `package/core/common/20-inject.html` (HTML) | Magnitude: 616.62 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 673, state_mutation: 295, branch: 194, structural_boundaries: 117
- `package/core/function/15-change.html` (HTML) | Magnitude: 507.26 | Delta: **0.115 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 337, state_mutation: 244, branch: 92, structural_boundaries: 92

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/core/function/89-delay.js` (JAVASCRIPT) | Magnitude: 857.0 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 378, state_mutation: 241, branch: 137, structural_boundaries: 43
- `package/core/sequence/18-sort.js` (JAVASCRIPT) | Magnitude: 515.1 | Delta: **0.313 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 218, state_mutation: 147, structural_boundaries: 85, concurrency: 74
- `package/core/parsers/70-XML.js` (JAVASCRIPT) | Magnitude: 127.42 | Delta: **0.34 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, state_mutation: 26, branch: 17, safety: 8
- `package/core/function/80-template.js` (JAVASCRIPT) | Magnitude: 412.4 | Delta: **0.346 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 173, state_mutation: 133, structural_boundaries: 44, branch: 41
- `package/core/function/89-trigger.js` (JAVASCRIPT) | Magnitude: 1004.08 | Delta: **0.364 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 260, indent_spaces: 252, branch: 122, concurrency: 60

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/core/common/24-complete.js` (JAVASCRIPT) | Magnitude: 43.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 27, indent_spaces: 17, func_start: 4, branch: 3
- `package/core/common/25-status.js` (JAVASCRIPT) | Magnitude: 46.32 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 30, indent_spaces: 19, func_start: 4, branch: 3
- `package/core/parsers/70-YAML.js` (JAVASCRIPT) | Magnitude: 71.1 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, state_mutation: 15, branch: 13, safety: 9
- `package/core/function/10-switch.js` (JAVASCRIPT) | Magnitude: 731.34 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 325, branch: 132, state_mutation: 126, structural_boundaries: 79
- `package/core/network/21-httpin.html` (HTML) | Magnitude: 204.54 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 259, state_mutation: 100, structural_boundaries: 60, branch: 45

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/core/function/rbe.js` -> **Severity: 151.433** (Blast Radius: 1.73 * Doc Risk: 87.5336%)
- `package/core/common/05-junction.js` -> **Severity: 81.349** (Blast Radius: 1.73 * Doc Risk: 47.0225%)
- `package/core/common/21-debug.js` -> **Severity: 76.511** (Blast Radius: 1.73 * Doc Risk: 44.2259%)
- `package/core/function/15-change.js` -> **Severity: 73.33** (Blast Radius: 1.73 * Doc Risk: 42.387%)
- `package/core/parsers/70-YAML.js` -> **Severity: 58.689** (Blast Radius: 1.73 * Doc Risk: 33.9244%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
