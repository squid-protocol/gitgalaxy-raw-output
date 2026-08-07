# ARCHITECTURAL_BRIEF: @tiptap_extension-node-range
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@tiptap_extension-node-range` |
| **Timestamp** | `2026-08-07T05:13:22.219326+00:00` |
| **Scan Duration** | `0.08s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 7 malicious artifacts.

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
| Total Artifacts | 9 |
| Analyzed Artifacts (Scanned) | 9 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 0 |
| Total LOC | 308 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 100.0% |
| Dominant Lang | TYPESCRIPT |

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
| TYPESCRIPT | 7 | 308 | 77.8% |
| MARKDOWN | 1 | 0 | 11.1% |
| PLAINTEXT | 1 | 0 | 11.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.251`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 7 | 77.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 22.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 0*


## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 98.4 | 32.9 | 23.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 92.0 | 50.4 | 60.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 26.9 | 0.0 | 0.0 |
| Testing Exposure | 0.6 | 80.0 | 24.2 | 2.5 | 80.0 |
| API Exposure | 4.1 | 16.2 | 8.2 | 6.6 | 6.6 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 39.2 | 32.9 | 0.0 |
| Commented Logic Exposure | 0.0 | 13.8 | 2.0 | 0.0 | 0.0 |
| Specification Exposure | 26.7 | 100.0 | 81.9 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 11.1 | 80.3 | 43.5 | 46.6 | 51.3 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/LICENSE.md` (Hits: 0)
- `package/package.json` (Hits: 0)
- `package/src/helpers/NodeRangeBookmark.ts` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **LICENSE.md** (`package/LICENSE.md`) — 0 inbound connections
2. **package.json** (`package/package.json`) — 0 inbound connections
3. **NodeRangeBookmark.ts** (`package/src/helpers/NodeRangeBookmark.ts`) — 0 inbound connections
4. **NodeRangeSelection.ts** (`package/src/helpers/NodeRangeSelection.ts`) — 0 inbound connections
5. **getNodeRangeDecorations.ts** (`package/src/helpers/getNodeRangeDecorations.ts`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **node-range.ts** (`package/src/node-range.ts`) — 6 outbound dependencies
2. **NodeRangeSelection.ts** (`package/src/helpers/NodeRangeSelection.ts`) — 5 outbound dependencies
3. **index.ts** (`package/src/index.ts`) — 5 outbound dependencies
4. **NodeRangeBookmark.ts** (`package/src/helpers/NodeRangeBookmark.ts`) — 3 outbound dependencies
5. **getNodeRangeDecorations.ts** (`package/src/helpers/getNodeRangeDecorations.ts`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `addProseMirrorPlugins` (@ `package/src/node-range.ts`) -> Impact: **36.7** | LOC: 112
- `mousedown` (@ `package/src/node-range.ts`) -> Impact: **30.1** | LOC: 48
- `constructor` (@ `package/src/helpers/NodeRangeSelection.ts`) -> Impact: **25.7** | LOC: 23
- `getSelectionRanges` (@ `package/src/helpers/getSelectionRanges.ts`) -> Impact: **21.6** | LOC: 31
- `decorations` (@ `package/src/node-range.ts`) -> Impact: **12.2** | LOC: 36
  * *Intent:* // when selecting some text we want to render some decorations // to preview a `NodeRangeSelection`
- `addKeyboardShortcuts` (@ `package/src/node-range.ts`) -> Impact: **7.4** | LOC: 64
- `getNodeRangeDecorations` (@ `package/src/helpers/getNodeRangeDecorations.ts`) -> Impact: **7.2** | LOC: 25
- `eq` (@ `package/src/helpers/NodeRangeSelection.ts`) -> Impact: **5.3** | LOC: 3
- `extendBackwards` (@ `package/src/helpers/NodeRangeSelection.ts`) -> Impact: **5.0** | LOC: 16
- `extendForwards` (@ `package/src/helpers/NodeRangeSelection.ts`) -> Impact: **5.0** | LOC: 16

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/src/helpers` | 5 | 16.33 | 40.35% | 37.71% |
| `package/src` | 2 | 14.99 | 14.24% | 0.0% |
| `package` | 2 | 2.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/src/helpers/isNodeRangeSelection.ts` -> **100.0%** Exposure
- `package/src/helpers/getNodeRangeDecorations.ts` -> **88.5488%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/src/helpers/NodeRangeBookmark.ts` -> **100.0%** Exposure
- `package/src/helpers/NodeRangeSelection.ts` -> **100.0%** Exposure
- `package/src/helpers/getNodeRangeDecorations.ts` -> **41.2291%** Exposure
- `package/src/node-range.ts` -> **32.9226%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/helpers/getNodeRangeDecorations.ts` -> **1** Orphaned Functions | **0** Duplicates
- `package/src/helpers/isNodeRangeSelection.ts` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/src/helpers/getSelectionRanges.ts`** -> AI Confidence: **99.06%**
2. **`package/src/helpers/NodeRangeSelection.ts`** -> AI Confidence: **99.03%**
3. **`package/src/node-range.ts`** -> AI Confidence: **98.93%**
4. **`package/src/helpers/NodeRangeBookmark.ts`** -> AI Confidence: **98.88%**
5. **`package/src/helpers/isNodeRangeSelection.ts`** -> AI Confidence: **98.84%**
6. **`package/src/helpers/getNodeRangeDecorations.ts`** -> AI Confidence: **98.83%**
7. **`package/src/index.ts`** -> AI Confidence: **98.83%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `11` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/helpers/NodeRangeSelection.ts` (TYPESCRIPT) -> Cumulative Risk: **624.16**
- **Archetype:** `file_cluster_13` (Distance: 12.648 IQR)
- **Magnitude:** 10.72 | **LOC:** 116 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (98.3662%), Safety Score (92.0487%)
- **Heaviest Functions:** `constructor` (Impact: 25.7), `eq` (Impact: 5.3), `extendBackwards` (Impact: 5.0)

### 2. `package/src/helpers/NodeRangeBookmark.ts` (TYPESCRIPT) -> Cumulative Risk: **422.21**
- **Archetype:** `file_cluster_13` (Distance: 11.284 IQR)
- **Magnitude:** 1.42 | **LOC:** 27 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (71.5669%), Documentation (51.2818%)
- **Heaviest Functions:** `resolve` (Impact: 2.0), `constructor` (Impact: 1.9), `map` (Impact: 1.9)

### 3. `package/src/node-range.ts` (TYPESCRIPT) -> Cumulative Risk: **411.3**
- **Archetype:** `file_cluster_13` (Distance: 9.917 IQR)
- **Magnitude:** 13.03 | **LOC:** 211 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Safety Score (68.8497%), Stability (50.0%)
- **Heaviest Functions:** `addProseMirrorPlugins` (Impact: 36.7), `mousedown` (Impact: 30.1), `decorations` (Impact: 12.2)

### 4. `package/src/helpers/getNodeRangeDecorations.ts` (TYPESCRIPT) -> Cumulative Risk: **391.32**
- **Archetype:** `file_cluster_13` (Distance: 9.464 IQR)
- **Magnitude:** 1.16 | **LOC:** 29 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (88.5488%), Safety Score (60.5532%), Stability (50.0%)
- **Heaviest Functions:** `getNodeRangeDecorations` (Impact: 7.2)

### 5. `package/src/helpers/getSelectionRanges.ts` (TYPESCRIPT) -> Cumulative Risk: **300.5**
- **Archetype:** `file_cluster_13` (Distance: 9.404 IQR)
- **Magnitude:** 2.71 | **LOC:** 35 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (60.087%), Stability (50.0%), Documentation (41.7798%)
- **Heaviest Functions:** `getSelectionRanges` (Impact: 21.6)

### 6. `package/src/helpers/isNodeRangeSelection.ts` (TYPESCRIPT) -> Cumulative Risk: **199.2**
- **Archetype:** `file_cluster_13` (Distance: 12.6 IQR)
- **Magnitude:** 0.32 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Stability (50.0%), Spec Match (26.6667%), Documentation (11.1315%)
- **Heaviest Functions:** `isNodeRangeSelection` (Impact: 2.1)

### 7. `package/src/index.ts` (TYPESCRIPT) -> Cumulative Risk: **165.59**
- **Archetype:** `file_cluster_13` (Distance: 6.871 IQR)
- **Magnitude:** 1.96 | **LOC:** 10 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (46.6667%), Documentation (46.6192%), Api Exposure (16.2302%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/node-range.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.917 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.618 IQR)
- **Top Global Matches:** file_cluster_13: 9.917, file_cluster_8: 9.936, file_cluster_0: 10.332
- **Magnitude:** 13.03 | **LOC:** 211 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.4725%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addProseMirrorPlugins` (Impact: 36.7)
  * `mousedown` (Impact: 30.1)
  * `decorations` (Impact: 12.2)
    * *Intent:* // when selecting some text we want to render some decorations // to preview a `NodeRangeSelection`
  * `addKeyboardShortcuts` (Impact: 7.4)
  * `attributes` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 38`, `args: 11`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core, getSelectionRanges.js, getNodeRangeDecorations.js, NodeRangeSelection.js, isNodeRangeSelection.js, state
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/helpers/NodeRangeSelection.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.648 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.462 IQR)
- **Top Global Matches:** file_cluster_13: 12.648, file_cluster_0: 12.786, file_cluster_11: 12.929
- **Magnitude:** 10.72 | **LOC:** 116 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.3662%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 25.7)
  * `eq` (Impact: 5.3)
  * `extendBackwards` (Impact: 5.0)
  * `extendForwards` (Impact: 5.0)
  * `create` (Impact: 5.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 24`, `args: 13`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 37`, `dead_code: 1`
* *Architecture:* `api: 9`, `import: 6`
* *Defense:* `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` getSelectionRanges.js, transform, model, NodeRangeBookmark.js, state
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/helpers/getSelectionRanges.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.404 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.485 IQR)
- **Top Global Matches:** file_cluster_13: 9.404, file_cluster_0: 9.724, file_cluster_8: 9.836
- **Magnitude:** 2.71 | **LOC:** 35 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.6418%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getSelectionRanges` (Impact: 21.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 7`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` state, model
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.871 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.885 IQR)
- **Top Global Matches:** file_cluster_13: 6.871, file_cluster_8: 7.561, file_cluster_7: 8.534
- **Magnitude:** 1.96 | **LOC:** 10 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`
* *Risk/State:* None
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node-range.js, getSelectionRanges.js, getNodeRangeDecorations.js, NodeRangeSelection.js, isNodeRangeSelection.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/helpers/NodeRangeBookmark.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.284 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.735 IQR)
- **Top Global Matches:** file_cluster_13: 11.284, file_cluster_0: 11.593, file_cluster_17: 11.615
- **Magnitude:** 1.42 | **LOC:** 27 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.2932%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolve` (Impact: 2.0)
  * `constructor` (Impact: 1.9)
  * `map` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeRangeSelection.js, transform, model
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/helpers/getNodeRangeDecorations.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.464 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.335 IQR)
- **Top Global Matches:** file_cluster_13: 9.464, file_cluster_8: 9.686, file_cluster_0: 9.745
- **Magnitude:** 1.16 | **LOC:** 29 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.4531%), Tech Debt (88.5488%)
**Top Internal Functions/Classes:**
  * `getNodeRangeDecorations` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` state, view
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/LICENSE.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 50 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/helpers/isNodeRangeSelection.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.6 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.137 IQR)
- **Top Global Matches:** file_cluster_13: 12.6, file_cluster_8: 12.757, file_cluster_0: 13.327
- **Magnitude:** 0.32 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `isNodeRangeSelection` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeRangeSelection.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/src/node-range.ts` (TYPESCRIPT) | Magnitude: 13.03 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 143, structural_boundaries: 38, immutability_locks: 33, branch: 24
- `package/src/helpers/NodeRangeSelection.ts` (TYPESCRIPT) | Magnitude: 10.72 | Delta: **0.138 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 70, state_mutation: 37, structural_boundaries: 24, immutability_locks: 22
- `package/src/helpers/isNodeRangeSelection.ts` (TYPESCRIPT) | Magnitude: 0.32 | Delta: **0.157 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, safety: 2, args: 1, func_start: 1
- `package/src/helpers/getNodeRangeDecorations.ts` (TYPESCRIPT) | Magnitude: 1.16 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, immutability_locks: 4, state_mutation: 3
- `package/src/helpers/NodeRangeBookmark.ts` (TYPESCRIPT) | Magnitude: 1.42 | Delta: **0.309 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 9, state_mutation: 6, args: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/helpers/NodeRangeSelection.ts` -> **Severity: 8920.336** (Blast Radius: 111.111 * Doc Risk: 80.2831%)
- `package/src/helpers/NodeRangeBookmark.ts` -> **Severity: 5697.972** (Blast Radius: 111.111 * Doc Risk: 51.2818%)
- `package/src/node-range.ts` -> **Severity: 5273.228** (Blast Radius: 111.111 * Doc Risk: 47.4591%)
- `package/src/index.ts` -> **Severity: 5179.906** (Blast Radius: 111.111 * Doc Risk: 46.6192%)
- `package/src/helpers/getSelectionRanges.ts` -> **Severity: 4642.195** (Blast Radius: 111.111 * Doc Risk: 41.7798%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
