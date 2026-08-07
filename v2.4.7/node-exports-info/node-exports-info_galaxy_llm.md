# ARCHITECTURAL_BRIEF: node-exports-info
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/node-exports-info` |
| **Timestamp** | `2026-08-07T05:15:18.855959+00:00` |
| **Scan Duration** | `0.09s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 20 malicious artifacts.

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
| Total Artifacts | 26 |
| Analyzed Artifacts (Scanned) | 25 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 340 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.2% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3926 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4675 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7636 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 10 | 243 | 40.0% |
| TYPESCRIPT | 10 | 78 | 40.0% |
| JSON | 2 | 19 | 8.0% |
| MARKDOWN | 2 | 0 | 8.0% |
| PLAINTEXT | 1 | 0 | 4.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.114`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 12 | 48.0% |
| file_cluster_8 | 9 | 36.0% |
| file_cluster_16 | 1 | 4.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 12.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 47.0 | 15.2 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 93.7 | 32.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Testing Exposure | 0.5 | 2.7 | 1.6 | 1.9 | 0.5 |
| API Exposure | 0.0 | 13.4 | 5.8 | 5.8 | 5.8 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 39.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 66.4 | 80.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 2.4 | 11.9 | 7.9 | 9.5 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/.nycrc` (Hits: 0)
- `package/tsconfig.json` (Hits: 0)
- `package/CHANGELOG.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ranges.js** (`package/ranges.js`) — 5 inbound connections
2. **getCategoryFlags.js** (`package/getCategoryFlags.js`) — 2 inbound connections
3. **isCategory.js** (`package/isCategory.js`) — 2 inbound connections
4. **getConditionsForCategory.js** (`package/getConditionsForCategory.js`) — 1 inbound connections
5. **getRangePairs.js** (`package/getRangePairs.js`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **getCategoriesForRange.js** (`package/getCategoriesForRange.js`) — 6 outbound dependencies
2. **getCategory.js** (`package/getCategory.js`) — 5 outbound dependencies
3. **getCategoryFlags.js** (`package/getCategoryFlags.js`) — 4 outbound dependencies
4. **getConditionsForCategory.js** (`package/getConditionsForCategory.js`) — 4 outbound dependencies
5. **getRange.js** (`package/getRange.js`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getConditionsForCategory` (@ `package/getConditionsForCategory.js`) -> Impact: **36.0** | LOC: 28
  * *Intent:* /** @type {import('./getConditionsForCategory')} */
- `getCategory` (@ `package/getCategory.js`) -> Impact: **9.3** | LOC: 12
  * *Intent:* /** @type {import('./getCategory')} */
- `getRange` (@ `package/getRange.js`) -> Impact: **7.5** | LOC: 11
  * *Intent:* /** @type {import('./getRange')} */
- `isCategory` (@ `package/isCategory.js`) -> Impact: **5.7** | LOC: 10
  * *Intent:* /** @type {import('./isCategory')} */
- `getCategoriesForRange` (@ `package/getCategoriesForRange.js`) -> Impact: **4.0** | LOC: 11
  * *Intent:* /** @type {import('./getCategoriesForRange')} */
- `getCategoryFlags` (@ `package/getCategoryFlags.js`) -> Impact: **4.0** | LOC: 11
  * *Intent:* /** @type {import('./getCategoryFlags')} */
- `entries` (@ `package/getCategoriesForRange.js`) -> Impact: **3.8** | LOC: 7
- `getCategoryInfo` (@ `package/getCategoryInfo.js`) -> Impact: **3.7** | LOC: 5
  * *Intent:* /** @type {import('./getCategoryInfo')} */
- `getRangePairs` (@ `package/getRangePairs.js`) -> Impact: **1.9** | LOC: 3
  * *Intent:* /** @type {import('./getRangePairs')} */

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package` | 25 | 313.81 | 13.34% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest State Flux (Mutation/Volatility)
- `package/getCategoriesForRange.js` -> **100.0%** Exposure
- `package/getCategory.js` -> **100.0%** Exposure
- `package/getCategoryInfo.js` -> **100.0%** Exposure
- `package/getConditionsForCategory.js` -> **100.0%** Exposure
- `package/getRange.js` -> **100.0%** Exposure

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/ranges.js`** -> AI Confidence: **99.29%**
2. **`package/ranges.d.ts`** -> AI Confidence: **99.29%**
3. **`package/getConditionsForCategory.js`** -> AI Confidence: **98.96%**
4. **`package/getConditionsForCategory.d.ts`** -> AI Confidence: **98.96%**
5. **`package/getCategory.js`** -> AI Confidence: **98.93%**
6. **`package/getRangePairs.js`** -> AI Confidence: **98.88%**
7. **`package/getCategoryInfo.js`** -> AI Confidence: **98.87%**
8. **`package/getCategoryInfo.d.ts`** -> AI Confidence: **98.87%**
9. **`package/isCategory.js`** -> AI Confidence: **98.86%**
10. **`package/eslint.config.mjs`** -> AI Confidence: **98.85%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `16` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/getCategory.js` (JAVASCRIPT) -> Cumulative Risk: **412.29**
- **Archetype:** `file_cluster_13` (Distance: 13.178 IQR)
- **Magnitude:** 29.62 | **LOC:** 22 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.6632%), Stability (50.0%)
- **Heaviest Functions:** `getCategory` (Impact: 9.3)

### 2. `package/getCategoriesForRange.js` (JAVASCRIPT) -> Cumulative Risk: **400.73**
- **Archetype:** `file_cluster_13` (Distance: 12.919 IQR)
- **Magnitude:** 20.1 | **LOC:** 21 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (84.3358%), Stability (50.0%)
- **Heaviest Functions:** `getCategoriesForRange` (Impact: 4.0), `entries` (Impact: 3.8)

### 3. `package/getConditionsForCategory.js` (JAVASCRIPT) -> Cumulative Risk: **381.15**
- **Archetype:** `file_cluster_13` (Distance: 13.301 IQR)
- **Magnitude:** 87.02 | **LOC:** 127 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (68.2895%), Stability (50.0%)
- **Heaviest Functions:** `getConditionsForCategory` (Impact: 36.0)

### 4. `package/getRange.js` (JAVASCRIPT) -> Cumulative Risk: **357.44**
- **Archetype:** `file_cluster_13` (Distance: 13.671 IQR)
- **Magnitude:** 23.78 | **LOC:** 20 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (93.3333%), Safety Score (88.3124%), Stability (50.0%)
- **Heaviest Functions:** `getRange` (Impact: 7.5)

### 5. `package/getCategoryFlags.js` (JAVASCRIPT) -> Cumulative Risk: **345.6**
- **Archetype:** `file_cluster_8` (Distance: 9.819 IQR)
- **Magnitude:** 11.84 | **LOC:** 57 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (92.2864%), Safety Score (62.7525%), Stability (50.0%)
- **Heaviest Functions:** `getCategoryFlags` (Impact: 4.0)

### 6. `package/isCategory.js` (JAVASCRIPT) -> Cumulative Risk: **328.38**
- **Archetype:** `file_cluster_13` (Distance: 13.59 IQR)
- **Magnitude:** 16.92 | **LOC:** 16 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Safety Score (81.6417%), Spec Match (73.3333%), Stability (50.0%)
- **Heaviest Functions:** `isCategory` (Impact: 5.7)

### 7. `package/getCategoryInfo.js` (JAVASCRIPT) -> Cumulative Risk: **311.13**
- **Archetype:** `file_cluster_13` (Distance: 13.229 IQR)
- **Magnitude:** 13.86 | **LOC:** 12 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Safety Score (86.4797%), Spec Match (53.3333%), Stability (50.0%)
- **Heaviest Functions:** `getCategoryInfo` (Impact: 3.7)

### 8. `package/eslint.config.mjs` (JAVASCRIPT) -> Cumulative Risk: **294.34**
- **Archetype:** `file_cluster_8` (Distance: 8.077 IQR)
- **Magnitude:** 17.26 | **LOC:** 15 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (86.6667%), State Flux (68.9316%), Safety Score (66.4144%), Stability (50.0%)

### 9. `package/getRangePairs.js` (JAVASCRIPT) -> Cumulative Risk: **281.93**
- **Archetype:** `file_cluster_13` (Distance: 12.086 IQR)
- **Magnitude:** 6.02 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9984%), Safety Score (72.3122%), Stability (50.0%), Spec Match (40.0%)
- **Heaviest Functions:** `getRangePairs` (Impact: 1.9)

### 10. `package/ranges.d.ts` (TYPESCRIPT) -> Cumulative Risk: **215.09**
- **Archetype:** `file_cluster_8` (Distance: 6.725 IQR)
- **Magnitude:** 1.63 | **LOC:** 19 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Cognitive Load (46.2403%), Documentation (11.9203%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/getConditionsForCategory.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.301 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.635 IQR)
- **Top Global Matches:** file_cluster_13: 13.301, file_cluster_8: 13.401, file_cluster_7: 13.601
- **Magnitude:** 87.02 | **LOC:** 127 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.9351%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getConditionsForCategory` (Impact: 36.0)
    * *Intent:* /** @type {import('./getConditionsForCategory')} */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 33`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 11`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 35.087
  * `Choke Point (Betweenness):` 0.002717 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 1):` isCategory, range, getConditionsForCategory, type
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/getCategory.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.178 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.697 IQR)
- **Top Global Matches:** file_cluster_13: 13.178, file_cluster_8: 13.838, file_cluster_11: 13.972
- **Magnitude:** 29.62 | **LOC:** 22 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.9957%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCategory` (Impact: 9.3)
    * *Intent:* /** @type {import('./getCategory')} */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 9`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ranges, range, getCategory, object.entries, semver
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/getRange.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.671 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.851 IQR)
- **Top Global Matches:** file_cluster_13: 13.671, file_cluster_8: 14.34, file_cluster_11: 14.477
- **Magnitude:** 23.78 | **LOC:** 20 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getRange` (Impact: 7.5)
    * *Intent:* /** @type {import('./getRange')} */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 7`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` object.entries, ranges, range, getRange
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/getCategoriesForRange.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.919 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.551 IQR)
- **Top Global Matches:** file_cluster_13: 12.919, file_cluster_8: 13.558, file_cluster_11: 13.673
- **Magnitude:** 20.1 | **LOC:** 21 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.7051%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCategoriesForRange` (Impact: 4.0)
    * *Intent:* /** @type {import('./getCategoriesForRange')} */
  * `entries` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 8`, `args: 2`, `func_start: 3`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ranges, array.prototype.flatmap, object.entries, semver, types, getCategoriesForRange
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/getConditionsForCategory.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.289 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 2.529 IQR)
- **Top Global Matches:** file_cluster_8: 6.289, file_cluster_13: 7.276, file_cluster_7: 7.559
- **Magnitude:** 18.01 | **LOC:** 20 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.86%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 14`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types, |
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/eslint.config.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.077 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.77 IQR)
- **Top Global Matches:** file_cluster_8: 8.077, file_cluster_13: 8.181, file_cluster_1: 8.36
- **Magnitude:** 17.26 | **LOC:** 15 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` flat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/isCategory.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.59 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.913 IQR)
- **Top Global Matches:** file_cluster_13: 13.59, file_cluster_8: 14.032, file_cluster_7: 14.232
- **Magnitude:** 16.92 | **LOC:** 16 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isCategory` (Impact: 5.7)
    * *Intent:* /** @type {import('./isCategory')} */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 5`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 102.062
  * `Choke Point (Betweenness):` 0.014493 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 1):` isCategory, getRangePairs
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/ranges.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.719 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.071 IQR)
- **Top Global Matches:** file_cluster_8: 7.719, file_cluster_7: 8.33, file_cluster_1: 8.568
- **Magnitude:** 16.34 | **LOC:** 20 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.8174%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 203.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.198413
  * `Imports (Out-Degree: 0):` ranges.d.ts
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/.nycrc` (JSON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.26 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/getCategoryInfo.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.229 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.164 IQR)
- **Top Global Matches:** file_cluster_13: 13.229, file_cluster_8: 13.883, file_cluster_7: 14.009
- **Magnitude:** 13.86 | **LOC:** 12 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCategoryInfo` (Impact: 3.7)
    * *Intent:* /** @type {import('./getCategoryInfo')} */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` getCategoryInfo, getCategoryFlags, getConditionsForCategory
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 13.12 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/getCategoryFlags.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.819 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.415 IQR)
- **Top Global Matches:** file_cluster_8: 9.819, file_cluster_13: 10.041, file_cluster_7: 10.141
- **Magnitude:** 11.84 | **LOC:** 57 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.8715%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCategoryFlags` (Impact: 4.0)
    * *Intent:* /** @type {import('./getCategoryFlags')} */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 6`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 56.016
  * `Choke Point (Betweenness):` 0.008152 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 1):` types, isCategory, range, getCategoryFlags
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/getRangePairs.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.086 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.355 IQR)
- **Top Global Matches:** file_cluster_13: 12.086, file_cluster_8: 12.729, file_cluster_7: 12.842
- **Magnitude:** 6.02 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getRangePairs` (Impact: 1.9)
    * *Intent:* /** @type {import('./getRangePairs')} */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 111.379
  * `Choke Point (Betweenness):` 0.009058 | `Ripple Effect (Closeness):` 0.094697
  * `Imports (Out-Degree: 1):` object.entries, ranges, getRangePairs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/getCategoryInfo.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.977 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.652 IQR)
- **Top Global Matches:** file_cluster_8: 6.977, file_cluster_13: 7.445, file_cluster_7: 8.127
- **Magnitude:** 3.6 | **LOC:** 17 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` types, |, getCategoryFlags
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/getCategory.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.131 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.151 IQR)
- **Top Global Matches:** file_cluster_13: 8.131, file_cluster_8: 8.262, file_cluster_7: 9.209
- **Magnitude:** 3.08 | **LOC:** 5 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.7 | **LOC:** 135 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.12 | **LOC:** 106 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/getCategoryFlags.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.246 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.498 IQR)
- **Top Global Matches:** file_cluster_8: 7.246, file_cluster_13: 7.926, file_cluster_7: 8.314
- **Magnitude:** 2.03 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/getCategoriesForRange.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.469 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.116 IQR)
- **Top Global Matches:** file_cluster_13: 8.469, file_cluster_8: 8.538, file_cluster_7: 9.409
- **Magnitude:** 1.67 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/getRange.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.469 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.116 IQR)
- **Top Global Matches:** file_cluster_13: 8.469, file_cluster_8: 8.538, file_cluster_7: 9.409
- **Magnitude:** 1.67 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/getRangePairs.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.469 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.116 IQR)
- **Top Global Matches:** file_cluster_13: 8.469, file_cluster_8: 8.538, file_cluster_7: 9.409
- **Magnitude:** 1.67 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/isCategory.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.86 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.392 IQR)
- **Top Global Matches:** file_cluster_13: 12.86, file_cluster_8: 13.139, file_cluster_0: 13.661
- **Magnitude:** 1.67 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/types.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 8.196 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.321 IQR)
- **Top Global Matches:** file_cluster_16: 8.196, file_cluster_13: 8.38, file_cluster_8: 8.612
- **Magnitude:** 1.66 | **LOC:** 9 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 11`
* *Risk/State:* None
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ranges, |
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ranges.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.725 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 2.685 IQR)
- **Top Global Matches:** file_cluster_8: 6.725, file_cluster_7: 7.895, file_cluster_1: 8.135
- **Magnitude:** 1.63 | **LOC:** 19 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.2403%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.16 | **LOC:** 58 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/getCategoriesForRange.d.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, args: 1, func_start: 1, api: 1
- `package/getRange.d.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, args: 1, func_start: 1, api: 1
- `package/getRangePairs.d.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, args: 1, func_start: 1, api: 1
- `package/getConditionsForCategory.js` (JAVASCRIPT) | Magnitude: 87.02 | Delta: **0.1 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 73, state_mutation: 47, structural_boundaries: 33, branch: 28
- `package/getCategory.d.ts` (TYPESCRIPT) | Magnitude: 3.08 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, branch: 1, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/types.d.ts` (TYPESCRIPT) | Magnitude: 1.66 | Delta: **0.184 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, api: 4, generics: 2, reflection_metaprogramming: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/eslint.config.mjs` (JAVASCRIPT) | Magnitude: 17.26 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 10, events: 3, structural_boundaries: 2, branch: 1
- `package/getCategoryFlags.js` (JAVASCRIPT) | Magnitude: 11.84 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 31, doc: 8, structural_boundaries: 6, state_mutation: 5
- `package/getCategoryInfo.d.ts` (TYPESCRIPT) | Magnitude: 3.6 | Delta: **0.468 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_tabs: 6, import: 2, branch: 1
- `package/ranges.js` (JAVASCRIPT) | Magnitude: 16.34 | Delta: **0.611 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 14, branch: 12, bitwise_ops: 7, doc: 2
- `package/getCategoryFlags.d.ts` (TYPESCRIPT) | Magnitude: 2.03 | Delta: **0.68 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_tabs: 5, args: 1, func_start: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/isCategory.js` -> **Severity: 1.449** (Bridge: 0.0145 * Flux: 100.0%)
- `package/getRangePairs.js` -> **Severity: 0.906** (Bridge: 0.0091 * Flux: 99.9984%)
- `package/getCategoryFlags.js` -> **Severity: 0.752** (Bridge: 0.0082 * Flux: 92.2864%)
- `package/getConditionsForCategory.js` -> **Severity: 0.272** (Bridge: 0.0027 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/isCategory.js` -> **Severity: 9.071** (Embedded: 0.1111 * Error Risk: 81.6417%)
- `package/getRangePairs.js` -> **Severity: 6.848** (Embedded: 0.0947 * Error Risk: 72.3122%)
- `package/getCategoryFlags.js` -> **Severity: 5.229** (Embedded: 0.0833 * Error Risk: 62.7525%)
- `package/getConditionsForCategory.js` -> **Severity: 2.845** (Embedded: 0.0417 * Error Risk: 68.2895%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/ranges.js` -> **Severity: 2419.952** (Blast Radius: 203.011 * Doc Risk: 11.9203%)
- `package/isCategory.js` -> **Severity: 892.175** (Blast Radius: 102.062 * Doc Risk: 8.7415%)
- `package/getCategoryFlags.js` -> **Severity: 667.728** (Blast Radius: 56.016 * Doc Risk: 11.9203%)
- `package/getRangePairs.js` -> **Severity: 531.066** (Blast Radius: 111.379 * Doc Risk: 4.7681%)
- `package/getConditionsForCategory.js` -> **Severity: 418.248** (Blast Radius: 35.087 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
