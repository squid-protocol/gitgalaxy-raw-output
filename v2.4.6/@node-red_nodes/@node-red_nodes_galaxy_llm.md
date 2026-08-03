# ARCHITECTURAL_BRIEF: @node-red_nodes
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@node-red_nodes` |
| **Timestamp** | `2026-08-03T21:09:20.379753+00:00` |
| **Scan Duration** | `1.31s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 38 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 98.0 | 12.7 | 5.9 | 0.0 |
| Error & Exception Exposure | 0.0 | 97.3 | 6.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.9 | 2.3 | 2.3 |
| API Exposure | 0.0 | 5.8 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 35.8 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 75.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 50.0 | 44.7 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 45.0 | 45.4 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 10.8 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `exports` (@ `package/core/network/10-mqtt.js`) -> Impact: **1337.4** | LOC: 713
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `exports` (@ `package/core/sequence/17-split.js`) -> Impact: **1257.6** | LOC: 799
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `exports` (@ `package/core/network/21-httprequest.js`) -> Impact: **887.1** | LOC: 405
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `exports` (@ `package/core/function/15-change.js`) -> Impact: **799.4** | LOC: 346
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `exports` (@ `package/core/parsers/70-CSV.js`) -> Impact: **729.3** | LOC: 232
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `exports` (@ `package/core/function/89-delay.js`) -> Impact: **703.4** | LOC: 407
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation *
- `exports` (@ `package/core/function/10-switch.js`) -> Impact: **676.0** | LOC: 354
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `exports` (@ `package/core/function/89-trigger.js`) -> Impact: **623.3** | LOC: 289
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `oneditprepare` (@ `package/core/function/10-switch.html`) -> Impact: **516.2** | LOC: 227
- `onpaletteadd` (@ `package/core/common/21-debug.html`) -> Impact: **511.5** | LOC: 430

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `label` (@ `package/core/common/20-inject.html`) -> **O(2^N) [Recursive]**
- `label` (@ `package/core/function/15-change.html`) -> **O(2^N) [Recursive]**
- `nodeSend` (@ `package/core/network/31-tcpin.js`) -> **O(2^N) [Recursive]**
- `label` (@ `package/core/function/89-delay.html`) -> **O(2^N) [Recursive]**
- `label` (@ `package/core/function/89-trigger.html`) -> **O(2^N) [Recursive]**
- `label` (@ `package/core/network/10-mqtt.html`) -> **O(2^N) [Recursive]**
- `label` (@ `package/core/storage/10-file.html`) -> **O(2^N) [Recursive]**
- `label` (@ `package/core/common/98-unknown.html`) -> **O(2^N) [Recursive]**
- `label` (@ `package/core/storage/10-file.html`) -> **O(2^N) [Recursive]**
- `oneditprepare` (@ `package/core/common/20-inject.html`) -> **O(N^6)**

### Highest Data Gravity (Database Complexity)
- `exports` (@ `package/core/network/21-httprequest.js`) -> DB Complexity: **153**
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `exports` (@ `package/core/sequence/17-split.js`) -> DB Complexity: **138**
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `onpaletteadd` (@ `package/core/common/21-debug.html`) -> DB Complexity: **93**
- `exports` (@ `package/core/common/21-debug.js`) -> DB Complexity: **88**
- `exports` (@ `package/core/function/89-trigger.js`) -> DB Complexity: **88**
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `exports` (@ `package/core/function/89-delay.js`) -> DB Complexity: **85**
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation *
- `exports` (@ `package/core/sequence/19-batch.js`) -> DB Complexity: **66**
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `oneditprepare` (@ `package/core/function/15-change.html`) -> DB Complexity: **63**
- `exports` (@ `package/core/parsers/70-CSV.js`) -> DB Complexity: **63**
  * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
- `oneditprepare` (@ `package/core/function/10-switch.html`) -> DB Complexity: **60**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/core/function` | 18 | 9023.22 | 76.92% | 44.63% |
| `package/core/network` | 16 | 6794.64 | 49.77% | 61.91% |
| `package/core/common` | 20 | 5675.06 | 49.59% | 71.38% |
| `package/core/sequence` | 6 | 3208.0 | 69.08% | 50.46% |
| `package/core/parsers` | 10 | 1999.92 | 66.4% | 65.22% |
| `package/core/storage` | 4 | 774.62 | 64.86% | 66.09% |
| `package/icons` | 46 | 455.36 | 4.67% | 0.0% |
| `package/examples/parser/csv` | 10 | 173.38 | 0.0% | 0.0% |
| `package/examples/network/http` | 7 | 126.68 | 0.0% | 0.0% |
| `package/examples/storage/read file` | 4 | 71.2 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/locales/es-ES/common/24-complete.html` -> **100.0%** Exposure
- `package/locales/ko/common/21-debug.html` -> **100.0%** Exposure
- `package/core/common/90-comment.js` -> **100.0%** Exposure
- `package/core/common/91-global-config.js` -> **100.0%** Exposure
- `package/core/common/98-unknown.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/core/common/20-inject.html` -> **100.0%** Exposure
- `package/core/common/21-debug.html` -> **100.0%** Exposure
- `package/core/common/24-complete.html` -> **100.0%** Exposure
- `package/core/common/25-catch.html` -> **100.0%** Exposure
- `package/core/common/25-status.html` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/core/common/60-link.html` -> **1** Orphaned Functions | **14** Duplicates
- `package/core/network/31-tcpin.html` -> **0** Orphaned Functions | **15** Duplicates
- `package/core/network/10-mqtt.html` -> **0** Orphaned Functions | **13** Duplicates
- `package/core/common/21-debug.html` -> **8** Orphaned Functions | **0** Duplicates
- `package/core/function/89-delay.html` -> **3** Orphaned Functions | **5** Duplicates

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

### Exploit Generation Surface
- `package/core/common/20-inject.html` -> **100.0%** Exposure
- `package/core/common/21-debug.html` -> **100.0%** Exposure
- `package/core/common/24-complete.html` -> **100.0%** Exposure
- `package/core/common/25-catch.html` -> **100.0%** Exposure
- `package/core/common/25-status.html` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `package/core/common/20-inject.html` -> **100.0%** Exposure
- `package/core/common/21-debug.html` -> **100.0%** Exposure
- `package/core/common/24-complete.html` -> **100.0%** Exposure
- `package/core/common/25-catch.html` -> **100.0%** Exposure
- `package/core/common/25-status.html` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `67` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/core/parsers/70-XML.js` (JAVASCRIPT) -> Cumulative Risk: **921.17**
- **Archetype:** `file_cluster_4` (Distance: 13.511 IQR)
- **Magnitude:** 126.32 | **LOC:** 49 | **CtrlFlow:** 73.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `exports` (Impact: 91.4)

### 2. `package/core/function/89-trigger.js` (JAVASCRIPT) -> Cumulative Risk: **844.2**
- **Archetype:** `file_cluster_4` (Distance: 15.641 IQR)
- **Magnitude:** 949.38 | **LOC:** 306 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `exports` (Impact: 623.3)

### 3. `package/core/sequence/18-sort.js` (JAVASCRIPT) -> Cumulative Risk: **842.26**
- **Archetype:** `file_cluster_4` (Distance: 15.328 IQR)
- **Magnitude:** 505.2 | **LOC:** 267 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `exports` (Impact: 274.8)

### 4. `package/core/common/20-inject.js` (JAVASCRIPT) -> Cumulative Risk: **819.29**
- **Archetype:** `file_cluster_17` (Distance: 14.113 IQR)
- **Magnitude:** 429.66 | **LOC:** 198 | **CtrlFlow:** 79.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `exports` (Impact: 281.3)

### 5. `package/core/function/80-template.js` (JAVASCRIPT) -> Cumulative Risk: **803.84**
- **Archetype:** `file_cluster_4` (Distance: 13.792 IQR)
- **Magnitude:** 384.5 | **LOC:** 225 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `exports` (Impact: 218.0)

### 6. `package/core/network/32-udp.js` (JAVASCRIPT) -> Cumulative Risk: **800.82**
- **Archetype:** `file_cluster_8` (Distance: 12.742 IQR)
- **Magnitude:** 584.42 | **LOC:** 285 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9991%)
- **Heaviest Functions:** `exports` (Impact: 488.6)

### 7. `package/core/parsers/70-YAML.js` (JAVASCRIPT) -> Cumulative Risk: **799.88**
- **Archetype:** `file_cluster_8` (Distance: 13.227 IQR)
- **Magnitude:** 88.1 | **LOC:** 42 | **CtrlFlow:** 81.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9997%), Logic Bomb (99.9967%)
- **Heaviest Functions:** `exports` (Impact: 71.3)

### 8. `package/core/function/89-delay.js` (JAVASCRIPT) -> Cumulative Risk: **799.62**
- **Archetype:** `file_cluster_4` (Distance: 14.419 IQR)
- **Magnitude:** 976.0 | **LOC:** 425 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `exports` (Impact: 703.4)

### 9. `package/core/sequence/19-batch.js` (JAVASCRIPT) -> Cumulative Risk: **785.9**
- **Archetype:** `file_cluster_17` (Distance: 12.925 IQR)
- **Magnitude:** 504.72 | **LOC:** 318 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `exports` (Impact: 312.0)

### 10. `package/core/function/16-range.js` (JAVASCRIPT) -> Cumulative Risk: **773.0**
- **Archetype:** `file_cluster_8` (Distance: 14.393 IQR)
- **Magnitude:** 172.98 | **LOC:** 72 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `exports` (Impact: 86.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/core/sequence/17-split.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.806 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.524 IQR)
- **Top Global Matches:** file_cluster_17: 13.806, file_cluster_8: 13.837, file_cluster_11: 14.04
- **Magnitude:** 1663.66 | **LOC:** 816 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 138
- **Risk Profile:** Cognitive Load (78.8462%), Tech Debt (9.1057%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 1257.6 | O(N^6) | DB: 138)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 123`, `args: 38`, `func_start: 58`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 388`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 2`
* *Defense:* `safety: 102`, `doc: 1`, `immutability_locks: 2`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/10-mqtt.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.06 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.282 IQR)
- **Top Global Matches:** file_cluster_8: 13.06, file_cluster_13: 13.205, file_cluster_7: 13.292
- **Magnitude:** 1437.66 | **LOC:** 1512 | **CtrlFlow:** 81.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (25.7543%), Tech Debt (9.4893%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 1337.4 | O(N^6) | DB: 47)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 60`, `args: 42`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 76`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 11`, `import: 5`
* *Defense:* `safety: 88`, `doc: 68`, `immutability_locks: 18`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is-utf8, mqtt, https-proxy-agent, proxyHelper, url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/20-inject.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.892 IQR)
- **Top Global Matches:** file_cluster_17: 12.892, file_cluster_8: 12.952, file_cluster_11: 13.109
- **Magnitude:** 1389.02 | **LOC:** 733 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (79.2408%), Tech Debt (36.0617%)
**Top Internal Functions/Classes:**
  * `label` (Impact: 388.8 | O(2^N) | DB: 19)
  * `oneditprepare` (Impact: 279.0 | O(N^6) | DB: 38)
  * `oneditsave` (Impact: 193.2 | O(N^6) | DB: 24)
  * `outputLabels` (Impact: 91.1 | O(N^6) | DB: 15)
  * `doInject` (Impact: 53.3 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 117`, `args: 26`, `func_start: 17`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 295`, `dead_code: 4`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* None
* *Defense:* `safety: 51`, `doc: 2`, `immutability_locks: 7`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/21-debug.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.339 IQR)
- **Top Global Matches:** file_cluster_8: 13.339, file_cluster_17: 13.495, file_cluster_11: 13.593
- **Magnitude:** 1162.88 | **LOC:** 695 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 93
- **Risk Profile:** Cognitive Load (98.0028%), Tech Debt (51.0352%)
**Top Internal Functions/Classes:**
  * `onpaletteadd` (Impact: 511.5 | O(N^6) | DB: 93)
  * `oneditprepare` (Impact: 148.5 | O(N^6) | DB: 32)
  * `activateAjaxCall` (Impact: 61.4 | O(N^5) | DB: 2)
  * `label` (Impact: 43.0 | O(N^4) | DB: 12)
  * `onclick` (Impact: 26.1 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 96`, `args: 57`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 325`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 8`, `concurrency: 5`
* *Defense:* `safety: 66`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` debug-utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/10-switch.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.046 IQR)
- **Top Global Matches:** file_cluster_17: 13.046, file_cluster_8: 13.239, file_cluster_11: 13.432
- **Magnitude:** 1086.0 | **LOC:** 480 | **CtrlFlow:** 67.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (97.7518%), Tech Debt (25.6695%)
**Top Internal Functions/Classes:**
  * `oneditprepare` (Impact: 516.2 | O(N^6) | DB: 60)
  * `exportRule` (Impact: 96.7 | O(N^4) | DB: 2)
  * `outputLabels` (Impact: 90.0 | O(N^6) | DB: 5)
  * `validate` (Impact: 68.0 | O(N^6) | DB: 4)
  * `getValueLabel` (Impact: 24.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 97`, `args: 25`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 178`, `dead_code: 1`, `orphaned_logic: 5`
* *Architecture:* None
* *Defense:* `safety: 58`, `test: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/10-mqtt.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.082 IQR)
- **Top Global Matches:** file_cluster_8: 12.082, file_cluster_17: 12.573, file_cluster_7: 12.592
- **Magnitude:** 1035.76 | **LOC:** 1010 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (62.0449%), Tech Debt (73.9129%)
**Top Internal Functions/Classes:**
  * `oneditprepare` (Impact: 312.6 | O(N^6) | DB: 50)
  * `oneditsave` (Impact: 87.3 | O(N^6) | DB: 17)
  * `oneditprepare` (Impact: 76.7 | O(N^6) | DB: 11)
  * `oneditprepare` (Impact: 40.6 | O(N^5) | DB: 6)
  * `validate` (Impact: 36.9 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 168`, `args: 48`, `func_start: 51`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 312`, `duplicate_logic: 13`
* *Architecture:* `concurrency: 9`
* *Defense:* `safety: 47`, `doc: 3`, `sync_locks: 1`, `immutability_locks: 7`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/21-httprequest.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.978 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.643 IQR)
- **Top Global Matches:** file_cluster_13: 12.978, file_cluster_17: 13.129, file_cluster_11: 13.153
- **Magnitude:** 996.92 | **LOC:** 855 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 153
- **Risk Profile:** Cognitive Load (62.9123%), Tech Debt (23.4989%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 887.1 | O(N^6) | DB: 153)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 55`, `args: 13`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 100`, `dead_code: 2`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 37`, `api: 1`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 39`, `doc: 7`, `immutability_locks: 32`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` http, form-data, got, tough-cookie, hash-sum, mustache, crypto, uuid...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/89-delay.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.419 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.083 IQR)
- **Top Global Matches:** file_cluster_4: 14.419, file_cluster_11: 14.506, file_cluster_17: 14.575
- **Magnitude:** 976.0 | **LOC:** 425 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 85
- **Risk Profile:** Cognitive Load (87.9184%), Tech Debt (10.8586%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 703.4 | O(N^6) | DB: 85)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 43`, `args: 31`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 241`, `dead_code: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 23`
* *Defense:* `safety: 41`, `doc: 1`, `immutability_locks: 7`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/89-trigger.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.641 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.901 IQR)
- **Top Global Matches:** file_cluster_4: 15.641, file_cluster_11: 15.987, file_cluster_17: 16.1
- **Magnitude:** 949.38 | **LOC:** 306 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 88
- **Risk Profile:** Cognitive Load (95.8547%), Tech Debt (12.9043%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 623.3 | O(N^6) | DB: 88)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 50`, `args: 25`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 260`, `dead_code: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 60`, `import: 1`
* *Defense:* `safety: 56`, `doc: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mustache
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/15-change.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.977 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.5 IQR)
- **Top Global Matches:** file_cluster_8: 13.977, file_cluster_11: 14.169, file_cluster_17: 14.238
- **Magnitude:** 909.94 | **LOC:** 363 | **CtrlFlow:** 74.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (79.1157%), Tech Debt (11.4936%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 799.4 | O(N^6) | DB: 41)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 53`, `args: 24`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 103`, `orphaned_logic: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 99`, `doc: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/parsers/70-CSV.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.309 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.193 IQR)
- **Top Global Matches:** file_cluster_17: 16.309, file_cluster_11: 16.502, file_cluster_0: 16.594
- **Magnitude:** 903.54 | **LOC:** 691 | **CtrlFlow:** 82.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (84.9231%), Tech Debt (14.2772%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 729.3 | O(N^6) | DB: 63)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 30`, `args: 7`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 169`, `dead_code: 5`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 70`, `doc: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` csv, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/15-change.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.307 IQR)
- **Top Global Matches:** file_cluster_17: 13.307, file_cluster_8: 13.422, file_cluster_11: 13.723
- **Magnitude:** 868.76 | **LOC:** 367 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (75.6059%), Tech Debt (33.6743%)
**Top Internal Functions/Classes:**
  * `oneditprepare` (Impact: 248.5 | O(N^6) | DB: 63)
  * `label` (Impact: 219.5 | O(2^N) | DB: 33)
  * `validate` (Impact: 98.4 | O(N^6) | DB: 5)
  * `oneditsave` (Impact: 36.1 | O(N^6) | DB: 6)
  * `oneditresize` (Impact: 7.6 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 92`, `args: 16`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 246`, `orphaned_logic: 5`
* *Architecture:* None
* *Defense:* `safety: 32`, `immutability_locks: 3`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/10-switch.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.995 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.632 IQR)
- **Top Global Matches:** file_cluster_8: 13.995, file_cluster_11: 14.111, file_cluster_17: 14.261
- **Magnitude:** 812.54 | **LOC:** 527 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (82.0457%), Tech Debt (17.0432%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 676.0 | O(N^6) | DB: 46)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 79`, `args: 44`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 128`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 1`
* *Defense:* `safety: 72`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/10-function.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.047 IQR)
- **Top Global Matches:** file_cluster_8: 12.047, file_cluster_17: 12.31, file_cluster_4: 12.445
- **Magnitude:** 729.56 | **LOC:** 706 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (70.7196%), Tech Debt (33.3573%)
**Top Internal Functions/Classes:**
  * `prepareLibraryConfig` (Impact: 157.1 | O(N^6) | DB: 24)
  * `oneditprepare` (Impact: 154.2 | O(N^6) | DB: 24)
  * `getLibsList` (Impact: 37.5 | O(N^5) | DB: 8)
  * `getAllUsedModules` (Impact: 37.2 | O(N^6) | DB: 6)
  * `getEditorErrorCount` (Impact: 17.9 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 139`, `args: 46`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 235`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `concurrency: 16`
* *Defense:* `safety: 26`, `immutability_locks: 11`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/60-link.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.673 IQR)
- **Top Global Matches:** file_cluster_8: 12.673, file_cluster_17: 12.939, file_cluster_11: 13.096
- **Magnitude:** 664.84 | **LOC:** 406 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (75.1108%), Tech Debt (99.9291%)
**Top Internal Functions/Classes:**
  * `onEditPrepare` (Impact: 138.5 | O(N^6) | DB: 6)
  * `onEditSave` (Impact: 130.9 | O(N^6) | DB: 13)
  * `validate` (Impact: 30.7 | O(N^6) | DB: 2)
  * `label` (Impact: 25.3 | O(N^4) | DB: 9)
  * `onAdd` (Impact: 22.3 | O(N^4) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 67`, `args: 36`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 196`, `duplicate_logic: 14`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 1`
* *Defense:* `safety: 23`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/89-delay.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.839 IQR)
- **Top Global Matches:** file_cluster_8: 12.839, file_cluster_17: 13.214, file_cluster_11: 13.299
- **Magnitude:** 621.3 | **LOC:** 325 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (74.9942%), Tech Debt (95.9997%)
**Top Internal Functions/Classes:**
  * `oneditprepare` (Impact: 178.7 | O(N^6) | DB: 26)
  * `label` (Impact: 136.9 | O(2^N) | DB: 24)
  * `oneditsave` (Impact: 30.5 | O(N^5) | DB: 6)
  * `validate` (Impact: 24.5 | O(N^6))
  * `validate` (Impact: 18.5 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 46`, `args: 17`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 165`, `duplicate_logic: 5`, `orphaned_logic: 3`
* *Architecture:* None
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/21-debug.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.156 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.856 IQR)
- **Top Global Matches:** file_cluster_11: 14.156, file_cluster_13: 14.243, file_cluster_8: 14.274
- **Magnitude:** 613.54 | **LOC:** 330 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 88
- **Risk Profile:** Cognitive Load (93.9262%), Tech Debt (13.5469%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 457.9 | O(N^6) | DB: 88)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 32`, `args: 15`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 149`, `orphaned_logic: 1`
* *Architecture:* `io: 11`, `api: 1`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 43`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` events, fs-extra, util, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/32-udp.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.742 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.093 IQR)
- **Top Global Matches:** file_cluster_8: 12.742, file_cluster_11: 12.937, file_cluster_13: 12.95
- **Magnitude:** 584.42 | **LOC:** 285 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (84.4155%), Tech Debt (13.2666%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 488.6 | O(N^6) | DB: 30)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 17`, `args: 15`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 84`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 6`, `import: 2`
* *Defense:* `safety: 25`, `doc: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dgram, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/sequence/18-sort.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.328 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.675 IQR)
- **Top Global Matches:** file_cluster_4: 15.328, file_cluster_17: 15.638, file_cluster_11: 15.874
- **Magnitude:** 505.2 | **LOC:** 267 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (95.5045%), Tech Debt (13.9652%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 274.8 | O(N^6) | DB: 53)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 85`, `args: 31`, `func_start: 16`
* *Risk/State:* `state_mutation: 151`, `dead_code: 6`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 74`
* *Defense:* `safety: 18`, `doc: 1`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/sequence/19-batch.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.925 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.246 IQR)
- **Top Global Matches:** file_cluster_17: 12.925, file_cluster_8: 13.08, file_cluster_4: 13.176
- **Magnitude:** 504.72 | **LOC:** 318 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (77.158%), Tech Debt (12.1797%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 312.0 | O(N^6) | DB: 66)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 82`, `args: 36`, `func_start: 26`
* *Risk/State:* `state_mutation: 174`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 12`
* *Defense:* `safety: 13`, `doc: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/common/20-inject.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.113 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.517 IQR)
- **Top Global Matches:** file_cluster_17: 14.113, file_cluster_4: 14.116, file_cluster_8: 14.22
- **Magnitude:** 429.66 | **LOC:** 198 | **CtrlFlow:** 79.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (90.682%), Tech Debt (16.6986%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 281.3 | O(N^6) | DB: 44)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 14`, `args: 14`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 132`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 12`, `import: 1`
* *Defense:* `safety: 18`, `doc: 1`, `immutability_locks: 6`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cronosjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/31-tcpin.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.549 IQR)
- **Top Global Matches:** file_cluster_8: 10.549, file_cluster_7: 11.155, file_cluster_1: 11.19
- **Magnitude:** 424.78 | **LOC:** 421 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (42.6626%), Tech Debt (99.9426%)
**Top Internal Functions/Classes:**
  * `oneditprepare` (Impact: 113.2 | O(N^5) | DB: 4)
  * `oneditprepare` (Impact: 56.5 | O(N^6) | DB: 5)
  * `oneditprepare` (Impact: 40.1 | O(N^5) | DB: 3)
  * `validate` (Impact: 18.5 | O(N^6) | DB: 1)
  * `validate` (Impact: 18.5 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 57`, `args: 27`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 90`, `duplicate_logic: 15`
* *Architecture:* None
* *Defense:* `safety: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/function/rbe.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.215 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.418 IQR)
- **Top Global Matches:** file_cluster_8: 15.215, file_cluster_17: 15.348, file_cluster_11: 15.35
- **Magnitude:** 418.76 | **LOC:** 102 | **CtrlFlow:** 89.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (88.9105%), Tech Debt (27.5003%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 316.8 | O(N^6) | DB: 33)
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

### `package/core/function/80-template.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.792 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.393 IQR)
- **Top Global Matches:** file_cluster_4: 13.792, file_cluster_8: 14.119, file_cluster_17: 14.135
- **Magnitude:** 384.5 | **LOC:** 225 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 55
- **Risk Profile:** Cognitive Load (81.5287%), Tech Debt (16.2077%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 218.0 | O(N^6) | DB: 55)
    * *Intent:* /** * Copyright JS Foundation and other contributors, http://js.foundation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 44`, `args: 18`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 137`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 25`, `import: 2`
* *Defense:* `safety: 18`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mustache, js-yaml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/network/22-websocket.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.276 IQR)
- **Top Global Matches:** file_cluster_8: 10.276, file_cluster_17: 10.867, file_cluster_7: 10.932
- **Magnitude:** 367.48 | **LOC:** 511 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (30.8708%), Tech Debt (78.5761%)
**Top Internal Functions/Classes:**
  * `oneditprepare` (Impact: 73.6 | O(N^6) | DB: 11)
  * `ws_validateserver` (Impact: 26.5 | O(N^4) | DB: 3)
  * `ws_validateclient` (Impact: 26.5 | O(N^4) | DB: 3)
  * `oneditresize` (Impact: 25.4 | O(N^6) | DB: 2)
  * `ws_oneditprepare` (Impact: 22.7 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 59`, `args: 26`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 89`, `duplicate_logic: 6`, `orphaned_logic: 1`
* *Architecture:* `io: 22`
* *Defense:* `safety: 6`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.73
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `package/core/parsers/70-JSON.js` (JAVASCRIPT) | Magnitude: 310.04 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, state_mutation: 78, branch: 44, func_start: 23
- `package/core/common/21-debug.js` (JAVASCRIPT) | Magnitude: 613.54 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 230, state_mutation: 149, branch: 89, safety: 43
- `package/core/parsers/70-HTML.js` (JAVASCRIPT) | Magnitude: 213.62 | Delta: **0.188 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 83, indent_spaces: 79, branch: 24, safety: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/core/storage/10-file.js` (JAVASCRIPT) | Magnitude: 310.32 | Delta: **0.127 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 129, state_mutation: 51, branch: 49, safety: 23
- `package/core/network/21-httprequest.js` (JAVASCRIPT) | Magnitude: 996.92 | Delta: **0.151 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 330, branch: 142, state_mutation: 100, structural_boundaries: 55
- `package/core/network/21-httpin.js` (JAVASCRIPT) | Magnitude: 344.4 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 223, state_mutation: 103, branch: 44, structural_boundaries: 43
- `package/core/function/90-exec.js` (JAVASCRIPT) | Magnitude: 199.08 | Delta: **0.22 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 67, state_mutation: 64, branch: 25, safety: 13
- `package/core/function/10-function.js` (JAVASCRIPT) | Magnitude: 141.16 | Delta: **0.224 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, state_mutation: 26, branch: 21, safety: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `package/core/common/25-catch.html` (HTML) | Magnitude: 328.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 186, state_mutation: 124, branch: 53, structural_boundaries: 42
- `package/core/common/20-inject.js` (JAVASCRIPT) | Magnitude: 429.66 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 166, state_mutation: 132, branch: 54, func_start: 18
- `package/core/sequence/17-split.js` (JAVASCRIPT) | Magnitude: 1663.66 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 751, state_mutation: 388, branch: 245, structural_boundaries: 123
- `package/core/common/20-inject.html` (HTML) | Magnitude: 1389.02 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 673, state_mutation: 295, branch: 194, structural_boundaries: 117
- `package/core/function/15-change.html` (HTML) | Magnitude: 868.76 | Delta: **0.115 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 337, state_mutation: 246, branch: 92, structural_boundaries: 92

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/core/function/89-delay.js` (JAVASCRIPT) | Magnitude: 976.0 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 378, state_mutation: 241, branch: 137, structural_boundaries: 43
- `package/core/sequence/18-sort.js` (JAVASCRIPT) | Magnitude: 505.2 | Delta: **0.31 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 218, state_mutation: 151, structural_boundaries: 85, concurrency: 74
- `package/core/parsers/70-XML.js` (JAVASCRIPT) | Magnitude: 126.32 | Delta: **0.318 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, state_mutation: 26, branch: 17, safety: 8
- `package/core/function/80-template.js` (JAVASCRIPT) | Magnitude: 384.5 | Delta: **0.327 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 173, state_mutation: 137, structural_boundaries: 44, branch: 41
- `package/core/function/89-trigger.js` (JAVASCRIPT) | Magnitude: 949.38 | Delta: **0.346 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 260, indent_spaces: 252, branch: 122, concurrency: 60

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/core/common/24-complete.js` (JAVASCRIPT) | Magnitude: 43.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 27, indent_spaces: 17, func_start: 4, branch: 3
- `package/core/common/25-status.js` (JAVASCRIPT) | Magnitude: 49.72 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 30, indent_spaces: 19, func_start: 4, branch: 3
- `package/core/parsers/70-YAML.js` (JAVASCRIPT) | Magnitude: 88.1 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, state_mutation: 15, branch: 13, safety: 9
- `package/core/common/25-catch.js` (JAVASCRIPT) | Magnitude: 13.78 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 12, state_mutation: 6, func_start: 4, args: 3
- `package/core/network/21-httpin.html` (HTML) | Magnitude: 310.14 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 259, state_mutation: 100, structural_boundaries: 60, branch: 45

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/core/parsers/70-YAML.js` -> **Severity: 172.977** (Blast Radius: 1.73 * Doc Risk: 99.9866%)
- `package/core/parsers/70-XML.js` -> **Severity: 172.93** (Blast Radius: 1.73 * Doc Risk: 99.9597%)
- `package/core/function/rbe.js` -> **Severity: 167.216** (Blast Radius: 1.73 * Doc Risk: 96.6565%)
- `package/core/common/05-junction.js` -> **Severity: 126.867** (Blast Radius: 1.73 * Doc Risk: 73.3333%)
- `package/core/network/06-httpproxy.js` -> **Severity: 84.842** (Blast Radius: 1.73 * Doc Risk: 49.0418%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
